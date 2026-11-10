"""Build a native Excel clustered-column chart of ILMN EPS beats vs management guide and vs Street, Q2'25-Q3'26.

Data: Outputs/analyses/2026-10-30_ILMN_EPS_beat_magnitude_vs_guide_and_street.md (user-supplied table).
Q4'25 guide is the midpoint implied by the FY25 guide (no quarterly guide was given).
Usage: python -I build.py <out.xlsx>
"""
import sys
from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference
from openpyxl.chart.label import DataLabelList
from openpyxl.chart.text import RichText
from openpyxl.drawing.text import Paragraph, ParagraphProperties, CharacterProperties, Font, RichTextProperties
from openpyxl.chart.shapes import GraphicalProperties
from openpyxl.drawing.line import LineProperties
from openpyxl.styles import Font as XFont, Alignment

OUT = sys.argv[1]
FONT = "Garamond"
ORANGE, YELLOW, GREY = "E8962E", "F3C64B", "595959"

rows = [  # quarter, beat vs guide (c), % vs guide, beat vs Street (c), % vs Street
    ("Q2'25", 17, 0.167, 18, 0.178),
    ("Q3'25", 17, 0.145, 17, 0.145),
    ("Q4'25*", 15, 0.125, 12, 0.098),
    ("Q1'26", 10.5, 0.100, 10, 0.095),
    ("Q2'26", 8.5, 0.069, 8, 0.065),
    ("Q3'26", 8.5, 0.063, 8, 0.059),
]

wb = Workbook()
ws = wb.active
ws.title = "EPS beat"
ws.append(["Quarter", "Beat vs mgmt guide", "Beat vs Street", "Beat vs guide (cents)", "Beat vs Street (cents)"])
for q, cg, pg, cs, ps in rows:
    ws.append([q, pg, ps, cg, cs])
for r in range(2, len(rows) + 2):
    ws.cell(r, 2).number_format = ws.cell(r, 3).number_format = "0.0%"
for c in ws[1]:
    c.font = XFont(bold=True, name=FONT)
    c.alignment = Alignment(wrap_text=True, horizontal="center")
for col, w in zip("ABCDE", (10, 14, 12, 14, 14)):
    ws.column_dimensions[col].width = w
note_row = len(rows) + 3
ws.cell(note_row, 1, "*Q4'25 guide = midpoint implied by FY25 guide (no quarterly guide). Street = consensus going into the print.").font = XFont(italic=True, size=9, name=FONT)
ws.cell(note_row + 1, 1, "Source: ILMN releases and calls; Bloomberg/FactSet consensus. Q3'26 excludes tariff refunds.").font = XFont(italic=True, size=9, name=FONT)


def text_props(size, color=GREY, bold=False):
    cp = CharacterProperties(latin=Font(typeface=FONT), sz=size * 100, b=bold, solidFill=color)
    return RichText(bodyPr=RichTextProperties(), p=[Paragraph(pPr=ParagraphProperties(defRPr=cp), endParaRPr=cp)])


ch = BarChart()
ch.type, ch.grouping, ch.overlap, ch.gapWidth = "col", "clustered", -10, 80
ch.title = "ILMN EPS beat: vs management guide and vs Street"
ch.style = 10
data = Reference(ws, min_col=2, max_col=3, min_row=1, max_row=len(rows) + 1)
cats = Reference(ws, min_col=1, min_row=2, max_row=len(rows) + 1)
ch.add_data(data, titles_from_data=True)
ch.set_categories(cats)

for s, color in zip(ch.series, (ORANGE, YELLOW)):
    s.graphicalProperties = GraphicalProperties(solidFill=color)
    s.graphicalProperties.line = LineProperties(noFill=True)
    s.dLbls = DataLabelList()
    s.dLbls.showVal, s.dLbls.showSerName, s.dLbls.showCatName, s.dLbls.showLegendKey = True, False, False, False
    s.dLbls.position = "outEnd"
    s.dLbls.numFmt = "0.0%"
    s.dLbls.txPr = text_props(11, "404040", bold=True)

ch.y_axis.numFmt = "0%"
ch.y_axis.scaling.min, ch.y_axis.scaling.max, ch.y_axis.majorUnit = 0, 0.20, 0.05
ch.y_axis.majorGridlines.spPr = GraphicalProperties(ln=LineProperties(solidFill="E5E5E5"))
ch.y_axis.delete = ch.x_axis.delete = False
ch.y_axis.txPr = text_props(11)
ch.x_axis.txPr = text_props(12)
ch.x_axis.spPr = GraphicalProperties(ln=LineProperties(solidFill="BFBFBF"))
ch.y_axis.spPr = GraphicalProperties(ln=LineProperties(noFill=True))
ch.legend.position = "t"
ch.legend.overlay = False
ch.legend.txPr = text_props(12)
ch.title.tx.rich.p[0].pPr = ParagraphProperties(defRPr=CharacterProperties(latin=Font(typeface=FONT), sz=1600, b=True, solidFill="262626"))
for run in ch.title.tx.rich.p[0].r:
    run.rPr = CharacterProperties(latin=Font(typeface=FONT), sz=1600, b=True, solidFill="262626")
ch.title.overlay = False
ch.width, ch.height = 24, 12.5
ws.add_chart(ch, "G2")
wb.save(OUT)
print("saved", OUT)
