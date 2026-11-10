"""Street-implied research & applied (R&A) consumables y/y growth, 2027E and 2028E, vs LTM (Q4'25-Q3'26), in the format of
the user's "USHE Adj. Operating Margin" sample: bold Garamond title, blue columns, value labels, % axis, black trend arrow.
Native PowerPoint column chart (editable) plus a separate arrow shape.

Street figures are derived, because no broker or Bloomberg line splits R&A from clinical:
  Bloomberg consensus sequencing consumables (10 Oct 2026) less China (76% of Greater China revenue) gives ex-China growth
  of +9.9% (27E) and +9.8% (28E). Applied to our FY26 ex-China base ($2.93B) and taking out clinical at +14% (27E, the
  Q3'26 pace) and +13% (28E) leaves R&A at +1.7% and +2.8%. LTM = derived ex-China R&A dollars Q4'25-Q3'26 vs a year earlier.
Usage: python build.py <out.pptx>
"""
import sys
from pptx import Presentation
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LABEL_POSITION, XL_TICK_LABEL_POSITION, XL_TICK_MARK
from pptx.enum.shapes import MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.oxml.ns import qn
from pptx.util import Inches, Pt
from lxml import etree

OUT = sys.argv[1]
FONT = "Garamond"
BLUE, BLACK = RGBColor(0x2F, 0x55, 0x97), RGBColor(0, 0, 0)

CATS = ["LTM Q3'26", "2027E", "2028E"]
VALS = [-0.061, 0.017, 0.028]
VMIN, VMAX = -0.08, 0.06

FX, FY, FW, FH = 0.5, 0.82, 3.0, 2.25          # chart frame (in)
PX, PY, PW, PH = 0.17, 0.04, 0.81, 0.84        # inner plot area as fractions of the frame
GAP = 150                                       # bar gap width (%)

prs = Presentation()
prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
slide = prs.slides.add_slide(prs.slide_layouts[6])

# Title
tb = slide.shapes.add_textbox(Inches(FX), Inches(0.5), Inches(FW), Inches(0.3))
tf = tb.text_frame; tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
r = p.add_run(); r.text = "ILMN R&A Consumables Y/Y Growth"
r.font.name = FONT; r.font.size = Pt(13); r.font.bold = True; r.font.color.rgb = BLACK

# Chart
cd = CategoryChartData(); cd.categories = CATS; cd.add_series("R&A consumables y/y", VALS)
gf = slide.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(FX), Inches(FY), Inches(FW), Inches(FH), cd)
ch = gf.chart
ch.has_legend = False; ch.has_title = False
ch.font.name = FONT; ch.font.size = Pt(10); ch.font.color.rgb = BLACK
plot = ch.plots[0]; plot.gap_width = GAP; plot.vary_by_categories = False
ser = plot.series[0]
ser.format.fill.solid(); ser.format.fill.fore_color.rgb = BLUE
ser.invert_if_negative = False
plot.has_data_labels = True
dl = plot.data_labels; dl.number_format = '0.0%'; dl.number_format_is_linked = False
dl.position = XL_LABEL_POSITION.OUTSIDE_END; dl.font.size = Pt(10); dl.font.name = FONT

va = ch.value_axis
va.minimum_scale, va.maximum_scale, va.major_unit = VMIN, VMAX, 0.02
va.has_major_gridlines = False
va.tick_labels.number_format = '0%'; va.tick_labels.number_format_is_linked = False
va.tick_labels.font.size = Pt(10); va.tick_labels.font.name = FONT
va.format.line.color.rgb = RGBColor(0xBF, 0xBF, 0xBF)
va.major_tick_mark = XL_TICK_MARK.NONE
ca = ch.category_axis
ca.tick_label_position = XL_TICK_LABEL_POSITION.LOW     # keep labels at the bottom, below the negative bar
ca.tick_labels.font.size = Pt(10); ca.tick_labels.font.name = FONT
ca.format.line.color.rgb = RGBColor(0xBF, 0xBF, 0xBF)
ca.major_tick_mark = XL_TICK_MARK.NONE

# Fix the inner plot area so the arrow can be placed in data coordinates
pa = ch._chartSpace.find(qn("c:chart")).find(qn("c:plotArea"))
lay = pa.find(qn("c:layout"))
if lay is None:
    lay = etree.SubElement(pa, qn("c:layout")); pa.insert(0, lay)
for k in list(lay): lay.remove(k)
ml = etree.SubElement(lay, qn("c:manualLayout"))
for tag, val in (("layoutTarget", "inner"), ("xMode", "edge"), ("yMode", "edge"),
                 ("x", PX), ("y", PY), ("w", PW), ("h", PH)):
    etree.SubElement(ml, qn("c:" + tag)).set("val", str(val))


def xy(cat_pos, v):
    """cat_pos in category units (0 = centre of first category); v in data units -> slide inches."""
    cw = FW * PW / len(CATS)
    x = FX + FW * PX + cw * (cat_pos + 0.5)
    y = FY + FH * (PY + PH * (VMAX - v) / (VMAX - VMIN))
    return x, y


# Trend arrow: rises from above the LTM bar to beside the 2028E bar, clearing the 2027E label
x1, y1 = xy(0.05, 0.020)
x2, y2 = xy(1.66, 0.050)
ar = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
ar.line.color.rgb = BLACK; ar.line.width = Pt(1.5)
ln = ar.line._get_or_add_ln()
tail = etree.SubElement(ln, qn("a:tailEnd")); tail.set("type", "triangle"); tail.set("w", "med"); tail.set("len", "med")

# Source note
nb = slide.shapes.add_textbox(Inches(FX), Inches(FY + FH + 0.02), Inches(FW), Inches(0.4))
nf = nb.text_frame; nf.word_wrap = True; nf.margin_left = nf.margin_right = nf.margin_top = nf.margin_bottom = 0
np_ = nf.paragraphs[0]
nr = np_.add_run()
nr.text = ("Ex-China. Street = Bloomberg consensus seq. consumables (10 Oct 2026) less China and clinical "
           "at +14% (27E) / +13% (28E); no broker splits R&A. LTM = Q4'25–Q3'26, derived from disclosed growth rates.")
nr.font.name = FONT; nr.font.size = Pt(7); nr.font.italic = True; nr.font.color.rgb = RGBColor(0x59, 0x59, 0x59)

prs.save(OUT)
print("saved", OUT)
