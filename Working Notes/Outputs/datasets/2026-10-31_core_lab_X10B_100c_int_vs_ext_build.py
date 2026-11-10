"""Combine the NovaSeq X 10B 100-cycle internal and external core-lab $/Gb tables into one workbook with native Excel line charts.

Source: 2026-10-13_core_lab_price_per_gb.xlsx, sheets RL_X10B_int_100c and RL_X10B_ext_100c (values only, rows 6-30, months 2024-10 to 2026-10).
Medians are live MEDIAN formulas over each table's core columns (NA() where no core has a price, so the line breaks).
Usage: python build.py <source.xlsx> <out.xlsx>; then run the Excel formatting pass (fonts, legend layout) in the companion _format.ps1.
"""
import sys
import openpyxl
from openpyxl.chart import LineChart, Reference
from openpyxl.chart.layout import Layout, ManualLayout
from openpyxl.styles import Font, Alignment
from openpyxl.utils import get_column_letter as L

SRC, OUT = sys.argv[1], sys.argv[2]
FONT = "Garamond"
GREY, ORANGE, DARK, RED = "A6A6A6", "F5A623", "404040", "C00000"
src = openpyxl.load_workbook(SRC, data_only=True)


def grid(name):
    ws = src[name]
    cores = [ws.cell(5, c).value for c in range(2, ws.max_column + 1) if ws.cell(5, c).value]
    months = [ws.cell(r, 1).value for r in range(6, 31)]
    vals = [[ws.cell(r, c).value for c in range(2, 2 + len(cores))] for r in range(6, 31)]
    return cores, months, vals


ci, months, vi = grid("RL_X10B_int_100c")
ce, months_e, ve = grid("RL_X10B_ext_100c")
assert months == months_e

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "X10B_100c_int_vs_ext"
bold = Font(name=FONT, bold=True)
ws["A1"] = "Illumina NovaSeq X 10B, 100 cycles: core-facility $/Gb, internal vs external academic rates, monthly 2024-10 to 2026-10"
ws["A1"].font = Font(name=FONT, bold=True, size=13)
ws["A2"] = ("USD per Gb. Values copied from 2026-10-13_core_lab_price_per_gb.xlsx (sheets RL_X10B_int_100c, RL_X10B_ext_100c); "
            "see that workbook for observed/document-dated/carried flags, local prices and source URLs. "
            "Medians are across the cores with a price that month, so the set of cores changes over time.")
ws["A2"].font = Font(name=FONT, italic=True, size=10)

# Layout: A month | B internal median | C external median | D int cores | E ext cores | gap | internal cores | gap | external cores
H = 5
n_i, n_e = len(ci), len(ce)
c_int0 = 7
c_ext0 = c_int0 + n_i + 1
heads = ["Month", "Internal median", "External median", "Internal cores (n)", "External cores (n)"]
for j, h in enumerate(heads, 1):
    ws.cell(H, j, h).font = bold
ws.cell(H - 1, c_int0, "Internal/academic rate, by core").font = bold
ws.cell(H - 1, c_ext0, "External academic rate, by core").font = bold
for j, c in enumerate(ci):
    ws.cell(H, c_int0 + j, f"Int: {c}").font = bold
for j, c in enumerate(ce):
    ws.cell(H, c_ext0 + j, f"Ext: {c}").font = bold

ri = f"{L(c_int0)}{{r}}:{L(c_int0 + n_i - 1)}{{r}}"
re_ = f"{L(c_ext0)}{{r}}:{L(c_ext0 + n_e - 1)}{{r}}"
for k, m in enumerate(months):
    r = H + 1 + k
    ws.cell(r, 1, m)
    a, b = ri.format(r=r), re_.format(r=r)
    ws.cell(r, 2, f"=IF(COUNT({a})=0,NA(),MEDIAN({a}))").number_format = "$0.00"
    ws.cell(r, 3, f"=IF(COUNT({b})=0,NA(),MEDIAN({b}))").number_format = "$0.00"
    ws.cell(r, 4, f"=COUNT({a})")
    ws.cell(r, 5, f"=COUNT({b})")
    for j, v in enumerate(vi[k]):
        ws.cell(r, c_int0 + j, v).number_format = "$0.00"
    for j, v in enumerate(ve[k]):
        ws.cell(r, c_ext0 + j, v).number_format = "$0.00"
last = H + len(months)
for row in ws.iter_rows(min_row=H, max_row=last):
    for c in row:
        c.font = Font(name=FONT, bold=c.row == H)
ws.column_dimensions["A"].width = 10
for c in "BCDE":
    ws.column_dimensions[c].width = 15
ws.row_dimensions[H].height = 45
for c in ws[H]:
    c.alignment = Alignment(wrap_text=True, vertical="top")
ws.freeze_panes = ws.cell(H + 1, 2)

cats = Reference(ws, min_col=1, min_row=H + 1, max_row=last)


def style(s, color, width, dash=None):
    s.graphicalProperties.line.solidFill = color
    s.graphicalProperties.line.width = int(width * 12700)
    if dash:
        s.graphicalProperties.line.dashStyle = dash
    s.marker.symbol = "none"
    s.smooth = False


def base(title):
    ch = LineChart()
    ch.title = title
    ch.y_axis.number_format = "$0"
    ch.y_axis.majorGridlines = None
    ch.y_axis.delete = False
    ch.x_axis.delete = False
    ch.x_axis.tickLblSkip = 3
    ch.legend.position = "t"
    ch.width, ch.height = 26, 13
    return ch


# Chart 1: medians only
c1 = base("NovaSeq X 10B, 100 cycles: median core-facility price, USD per Gb, internal vs external rate")
c1.add_data(Reference(ws, min_col=2, max_col=3, min_row=H, max_row=last), titles_from_data=True)
c1.set_categories(cats)
style(c1.series[0], DARK, 2.5)
style(c1.series[1], ORANGE, 2.5)
c1.y_axis.scaling.min = 0
ws.add_chart(c1, f"A{last + 3}")

# Chart 2: every core (internal grey solid, external orange dashed) plus the medians
c2 = base("Every core, USD per Gb: internal grey, external orange dashed; medians bold (internal black, external red)")
c2.add_data(Reference(ws, min_col=c_int0, max_col=c_int0 + n_i - 1, min_row=H, max_row=last), titles_from_data=True)
c2.add_data(Reference(ws, min_col=c_ext0, max_col=c_ext0 + n_e - 1, min_row=H, max_row=last), titles_from_data=True)
c2.add_data(Reference(ws, min_col=2, max_col=3, min_row=H, max_row=last), titles_from_data=True)
c2.set_categories(cats)
for s in c2.series[:n_i]:
    style(s, GREY, 0.75)
for s in c2.series[n_i:n_i + n_e]:
    style(s, ORANGE, 0.75, "dash")
style(c2.series[-2], DARK, 3)
style(c2.series[-1], RED, 3)
c2.legend = None
c2.y_axis.scaling.min = 0
ws.add_chart(c2, f"A{last + 30}")

wb.save(OUT)
print("internal cores", n_i, "external cores", n_e, "months", len(months), "rows", H + 1, last)
