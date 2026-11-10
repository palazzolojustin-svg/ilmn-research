"""Clearer version of the NovaSeq X 10B 100-cycle core-lab pricing chart, as native PowerPoint charts.

Replaces the 41-line "spaghetti" chart with two panels that show what actually changed:
  (A) a like-for-like internal price index (Oct-24 = 100): each month, the average log price change across cores
      priced in both that month and the month before, chained. Cores entering or leaving the sample don't move it.
      The Jul-Oct 2026 window is shaded and the annualised pace before/after is labelled.
  (B) the number of price cuts per quarter across internal and external rates (moves smaller than 1% excluded,
      e.g. CNAG's -0.1% FX/rounding move).
Data: datasets/2026-10-31_core_lab_X10B_100c_int_vs_ext.xlsx (per-core monthly $/Gb, columns G onward).
Usage: python build.py <int_vs_ext.xlsx> <out.pptx>
"""
import math
import sys

import openpyxl
from pptx import Presentation
from pptx.chart.data import CategoryChartData
from pptx.dml.color import RGBColor
from pptx.enum.chart import XL_CHART_TYPE, XL_LABEL_POSITION, XL_MARKER_STYLE, XL_TICK_LABEL_POSITION, XL_TICK_MARK
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml import parse_xml
from pptx.oxml.ns import nsdecls, qn
from pptx.util import Inches, Pt

SRC, OUT = sys.argv[1], sys.argv[2]
FONT, ORANGE, GREY, INK, MUTED = "Garamond", "E8962E", "A6A6A6", "000000", "595959"

# ---------- data ----------
ws = openpyxl.load_workbook(SRC, data_only=True).active
rows = list(ws.iter_rows(values_only=True))
hdr = rows[4]
data = [r for r in rows[5:] if r[0] and str(r[0])[:2] == "20"]
months = [str(r[0]) for r in data]
series = {hdr[j]: [r[j] for r in data] for j in range(6, len(hdr)) if hdr[j]}
internal = [k for k in series if k.startswith("Int")]

idx = [100.0]
for t in range(1, len(months)):
    ch = [math.log(series[k][t] / series[k][t - 1]) for k in internal if series[k][t] and series[k][t - 1]]
    idx.append(idx[-1] * math.exp(sum(ch) / len(ch)) if ch else idx[-1])
w0 = months.index("2026-06")  # last month before the window
pace_before = (idx[w0] / idx[0]) ** (12 / w0) - 1
pace_after = (idx[-1] / idx[w0]) ** (12 / (len(months) - 1 - w0)) - 1


def quarter(m):
    y, mo = int(m[:4]), int(m[5:7])
    return f"Q{(mo - 1) // 3 + 1}'{str(y)[2:]}"


quarters = []
for m in months:
    q = quarter(m)
    if q not in quarters:
        quarters.append(q)
cuts = {q: 0 for q in quarters}
for v in series.values():
    for t in range(1, len(months)):
        if v[t] and v[t - 1] and v[t] / v[t - 1] - 1 < -0.01:
            cuts[quarter(months[t])] += 1
before = sum(n for q, n in cuts.items() if q not in ("Q3'26", "Q4'26"))
after = cuts["Q3'26"] + cuts["Q4'26"]

# ---------- slide ----------
prs = Presentation()
prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
s = prs.slides.add_slide(prs.slide_layouts[6])
X, W = 0.4, 7.6


def text(x, y, w, h, parts, size=12, align=PP_ALIGN.LEFT, color=INK, italic=False):
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.02)
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = align
    for t, b in parts:
        r = p.add_run()
        r.text = t
        r.font.name, r.font.size, r.font.bold, r.font.italic = FONT, Pt(size), b, italic
        r.font.color.rgb = RGBColor.from_string(color)
    return tb


def style_axis(ax, size=10):
    ax.has_major_gridlines = False
    ax.major_tick_mark = XL_TICK_MARK.NONE
    ax.format.line.color.rgb = RGBColor.from_string("808080")
    ax.tick_labels.font.name, ax.tick_labels.font.size = FONT, Pt(size)
    ax.tick_labels.font.color.rgb = RGBColor.from_string(INK)


def plot_layout(chart, x, y, w, h):
    pa = chart._chartSpace.find(qn("c:chart")).find(qn("c:plotArea"))
    for old in pa.findall(qn("c:layout")):
        pa.remove(old)
    pa.insert(0, parse_xml(
        f'<c:layout {nsdecls("c")}><c:manualLayout><c:layoutTarget val="inner"/><c:xMode val="edge"/>'
        f'<c:yMode val="edge"/><c:x val="{x}"/><c:y val="{y}"/><c:w val="{w}"/><c:h val="{h}"/>'
        '</c:manualLayout></c:layout>'))


# panel A: like-for-like index
AY, AH = 0.95, 3.0
PX, PW = 0.07, 0.90  # plot-area fractions, used to place the shaded window exactly
text(X, AY - 0.42, W, 0.34, [("Like-for-like internal price index", True), ("  (Oct-24 = 100)", False)], size=13)
n = len(months)
x_at = lambda i: X + W * (PX + PW * i / (n - 1))  # noqa: E731  (midCat axis: point i sits on tick i)
shade = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x_at(w0)), Inches(AY + 0.05), Inches(x_at(n - 1) - x_at(w0)),
                           Inches(AH * 0.80))
shade.fill.solid()
shade.fill.fore_color.rgb = RGBColor.from_string("FBE3C4")
shade.line.fill.background()
shade.shadow.inherit = False

cd = CategoryChartData()
MON = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
cd.categories = [f"{MON[int(m[5:7]) - 1]}-{m[2:4]}" for m in months]
cd.add_series("Internal like-for-like", [round(v, 2) for v in idx])
ch = s.shapes.add_chart(XL_CHART_TYPE.LINE, Inches(X), Inches(AY), Inches(W), Inches(AH), cd).chart
ch.has_title = False
ch.has_legend = False
ch.font.name, ch.font.size = FONT, Pt(10)
ser = ch.plots[0].series[0]
ser.format.line.color.rgb = RGBColor.from_string(ORANGE)
ser.format.line.width = Pt(3)
ser.smooth = False
ser.marker.style = XL_MARKER_STYLE.NONE
ca, va = ch.category_axis, ch.value_axis
style_axis(ca)
ca.tick_label_position = XL_TICK_LABEL_POSITION.LOW
for tag in ("c:tickLblSkip", "c:tickMarkSkip"):
    ca._element.append(parse_xml(f'<{tag} {nsdecls("c")} val="3"/>'))
va.minimum_scale, va.maximum_scale, va.major_unit = 90, 105, 5
style_axis(va)
va.has_major_gridlines = True
va.major_gridlines.format.line.color.rgb = RGBColor.from_string("E6E6E6")
cb = va._element.find(qn("c:crossBetween"))
if cb is None:
    anchor = va._element.find(qn("c:crosses"))
    if anchor is None:
        anchor = va._element.find(qn("c:crossesAt"))
    cb = parse_xml(f'<c:crossBetween {nsdecls("c")} val="midCat"/>')
    anchor.addnext(cb)
cb.set("val", "midCat")
plot_layout(ch, PX, 0.04, PW, 0.80)
y_at = lambda v: AY + AH * (0.04 + 0.80 * (105 - v) / 15)  # noqa: E731
text(x_at(1), y_at(95.5), 3.0, 0.3, [(f"{pace_before:+.0%} a year", True), ("  (Nov-24 to Jun-26)", False)],
     size=11, color=MUTED)
text(x_at(w0) - 2.15, y_at(92.5), 2.1, 0.3, [(f"{pace_after:+.0%} a year", True), ("  (Jul to Oct-26)", False)],
     size=11, align=PP_ALIGN.RIGHT, color="C0504D")

# panel B: price cuts per quarter
BY, BH = 4.45, 2.35
text(X, BY - 0.42, W, 0.34, [("Price cuts per quarter", True), ("  (internal + external rates, 41 series)", False)],
     size=13)
cd = CategoryChartData()
cd.categories = [q if q != "Q4'26" else "Q4'26*" for q in quarters]
cd.add_series("Cuts", [cuts[q] for q in quarters])
ch = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(X), Inches(BY), Inches(W), Inches(BH), cd).chart
ch.has_title = False
ch.has_legend = False
ch.font.name, ch.font.size = FONT, Pt(10)
pl = ch.plots[0]
pl.gap_width = 60
ser = pl.series[0]
for i, q in enumerate(quarters):
    pt = ser.points[i]
    pt.format.fill.solid()
    pt.format.fill.fore_color.rgb = RGBColor.from_string(ORANGE if q in ("Q3'26", "Q4'26") else GREY)
ser.data_labels.show_value = True
ser.data_labels.position = XL_LABEL_POSITION.OUTSIDE_END
ser.data_labels.font.name, ser.data_labels.font.size, ser.data_labels.font.bold = FONT, Pt(11), True
style_axis(ch.category_axis)
va = ch.value_axis
va.minimum_scale, va.maximum_scale = 0, 5
va.visible = False
va.has_major_gridlines = False
plot_layout(ch, PX, 0.06, PW, 0.76)
text(X + 0.75, BY + 0.2, 3.6, 0.35,
     [(f"{after} cuts in Jul–Oct-26", True), (f" vs {before} in the prior 20 months", False)],
     size=12)

text(X, 6.85, W, 0.45, [("Index: average month-on-month price change across cores priced in both months, chained, so "
                         "cores entering or leaving the sample don't move it. Cuts exclude moves under 1%. "
                         "*Q4'26 = October only.", False)], size=9, color=MUTED, italic=True)
prs.save(OUT)
print("index", [round(v, 1) for v in idx])
print("pace before/after", round(pace_before, 3), round(pace_after, 3))
print("cuts", cuts, "before", before, "after", after)
