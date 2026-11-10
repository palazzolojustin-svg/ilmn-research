"""Revenue growth implied by the buy side (reverse DCF at $235.99, 31 Oct 2026) as a native PowerPoint column chart,
styled like the user's price/Gb-cut chart: orange first bar, yellow bars after, bold serif labels, dashed callout box.
Usage: python build.py <out.pptx>
"""
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LABEL_POSITION
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.dml import MSO_LINE_DASH_STYLE
from pptx.dml.color import RGBColor

OUT = sys.argv[1]
FONT = "Times New Roman"
ORANGE, YELLOW, CALLOUT = RGBColor(0xE8, 0x96, 0x2E), RGBColor(0xF3, 0xC6, 0x4B), RGBColor(0xFB, 0xEE, 0xC9)
BLACK = RGBColor(0, 0, 0)

# Reverse DCF (datasets/2026-10-13_ILMN_reverse_DCF.xlsx, row 6): 2025A actual, 2026E $4,620M input, 2027E-31E solved CAGR
CATS = ["2025A", "2026E", "27E–29E\nCAGR"]
VALS = [4343 / 4332 - 1, 4620 / 4343 - 1, 0.1053]

prs = Presentation()
prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
slide = prs.slides.add_slide(prs.slide_layouts[6])

X, Y, W, H = 0.5, 0.5, 2.73, 2.02
cd = CategoryChartData(number_format='0.0%')
cd.categories = CATS
cd.add_series("Revenue growth", VALS)
gf = slide.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(X), Inches(Y), Inches(W), Inches(H), cd)
gf.name = "Buyside implied revenue growth"
ch = gf.chart
ch.has_legend = False
ch.has_title = False
ch.font.name = FONT

plot = ch.plots[0]
plot.gap_width = 45
plot.vary_by_categories = False
ser = plot.series[0]
ser.format.fill.solid(); ser.format.fill.fore_color.rgb = YELLOW
pt = ser.points[0]
pt.format.fill.solid(); pt.format.fill.fore_color.rgb = ORANGE

plot.has_data_labels = True
dl = plot.data_labels
dl.number_format = '0.0%'; dl.number_format_is_linked = False
dl.position = XL_LABEL_POSITION.OUTSIDE_END
dl.font.name = FONT; dl.font.size = Pt(10); dl.font.bold = True; dl.font.color.rgb = BLACK

va = ch.value_axis
va.minimum_scale, va.maximum_scale = 0, 0.135
va.visible = False
va.has_major_gridlines = False
ca = ch.category_axis
ca.tick_labels.font.name = FONT; ca.tick_labels.font.size = Pt(9); ca.tick_labels.font.bold = True
ca.tick_labels.font.color.rgb = BLACK
ca.format.line.color.rgb = BLACK; ca.format.line.width = Pt(0.75)
ca.has_major_gridlines = False
from pptx.enum.chart import XL_TICK_MARK
ca.major_tick_mark = XL_TICK_MARK.NONE

# Callout over the short 2025A bar: 27E-29E CAGR vs 2026E
box = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(X + 0.08), Inches(Y + 0.05), Inches(1.38), Inches(0.36))
box.name = "Callout"
box.fill.solid(); box.fill.fore_color.rgb = CALLOUT
box.line.color.rgb = ORANGE; box.line.width = Pt(0.75); box.line.dash_style = MSO_LINE_DASH_STYLE.DASH
box.shadow.inherit = False
tf = box.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
tf.margin_left = tf.margin_right = Inches(0.05); tf.margin_top = tf.margin_bottom = Inches(0.02)
for i, (t, sz, col, b) in enumerate([("~4pt", 11, ORANGE, True), ("faster annual growth vs. 2026E", 7, BLACK, False)]):
    p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
    p.alignment = PP_ALIGN.LEFT
    r = p.add_run(); r.text = t
    r.font.name = FONT; r.font.size = Pt(sz); r.font.bold = b; r.font.color.rgb = col

prs.save(OUT)
print("saved", OUT, [round(v * 100, 1) for v in VALS])
