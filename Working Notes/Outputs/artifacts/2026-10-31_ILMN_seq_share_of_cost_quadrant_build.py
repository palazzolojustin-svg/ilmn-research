"""Bottom-right quadrant: sequencing reagents as a share of all-in cost per 30x genome, 2022 vs 2026, plus quotes on
price cuts buying less volume. Native PowerPoint chart and shapes, sized to one quadrant (~6.3 x 3.0 in).

Inputs per 30x genome (our calculation; sources):
- Sequencing reagents: 2022 ~$600 (NovaSeq 6000 era; Evercore host framing "$600 to about $200", Core Notes 06),
  2026 ~$200 (NovaSeq X list, JPM 3 Mar 2026; ex-Illumina AD 23 Jul 2026 says ~$250 retail).
- Library prep ~$100, held flat (ex-Illumina AD 23 Jul 2026: "less than $100 per sample"; prep and data "pretty flat").
- Data analysis held flat: research ~$30 ("tens of dollars"), clinical ~$750 (midpoint of "$500-$1,000").
Usage: python build.py <out.pptx>
"""
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION, XL_LABEL_POSITION, XL_TICK_LABEL_POSITION, XL_TICK_MARK
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.dml import MSO_LINE_DASH_STYLE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.oxml.ns import qn, nsdecls
from pptx.oxml import parse_xml

OUT = sys.argv[1]
FONT = "Garamond"
GREY, ORANGE, INK, BOXFILL, BOXLINE = "BFBFBF", "F5A623", "000000", "F2F2F2", "F5A623"

seq = {"2022": 600, "2026": 200}
prep = 100
analysis = {"Research genome": 30, "Clinical genome": 750}
cats = list(analysis)
share = {y: [seq[y] / (seq[y] + prep + analysis[c]) for c in cats] for y in seq}

# quadrant origin (bottom-right of a 13.333 x 7.5 slide); move as a group after pasting
QX, QY = Inches(6.8), Inches(4.2)

prs = Presentation()
prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
slide = prs.slides.add_slide(prs.slide_layouts[6])

# chart title
t = slide.shapes.add_textbox(QX, QY, Inches(3.0), Inches(0.3)).text_frame
t.word_wrap = True
t.text = "Sequencing as % of all-in cost per genome"
r = t.paragraphs[0].runs[0]; r.font.name, r.font.size, r.font.bold = FONT, Pt(11), True

cd = CategoryChartData()
cd.categories = cats
for y in seq:
    cd.add_series(y, [round(v, 3) for v in share[y]], number_format='0%')
ch = slide.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, QX, QY + Inches(0.28), Inches(3.0), Inches(2.45), cd).chart
ch.font.name, ch.font.size, ch.font.color.rgb = FONT, Pt(10), RGBColor.from_string(INK)
plot = ch.plots[0]
plot.overlap, plot.gap_width = 0, 60
plot.vary_by_categories = False
for i, s in enumerate(plot.series):
    s.format.fill.solid(); s.format.fill.fore_color.rgb = RGBColor.from_string([GREY, ORANGE][i])
    s.format.line.fill.background()
    dl = s.data_labels
    dl.show_value, dl.number_format, dl.number_format_is_linked = True, '0%', False
    dl.position = XL_LABEL_POSITION.OUTSIDE_END
    dl.font.name, dl.font.size = FONT, Pt(10)
va = ch.value_axis
va.minimum_scale, va.maximum_scale, va.major_unit = 0.0, 1.0, 0.2
va.has_major_gridlines = False
va.tick_labels.number_format, va.tick_labels.number_format_is_linked = '0%', False
va.tick_labels.font.name, va.tick_labels.font.size = FONT, Pt(10)
va.major_tick_mark = XL_TICK_MARK.OUTSIDE
va.format.line.color.rgb = RGBColor.from_string("808080")
ca = ch.category_axis
ca.tick_label_position = XL_TICK_LABEL_POSITION.LOW
ca.major_tick_mark = XL_TICK_MARK.NONE
ca.tick_labels.font.name, ca.tick_labels.font.size = FONT, Pt(10)
ca.format.line.color.rgb = RGBColor.from_string("808080")
ch.has_title = False
ch.has_legend = True
ch.legend.position, ch.legend.include_in_layout = XL_LEGEND_POSITION.TOP, False
ch.legend.font.name, ch.legend.font.size = FONT, Pt(10)
leg = ch.legend._element
for old in leg.findall(qn("c:layout")):
    leg.remove(old)
leg.find(qn("c:legendPos")).addnext(parse_xml(
    f'<c:layout {nsdecls("c")}><c:manualLayout><c:xMode val="edge"/><c:yMode val="edge"/>'
    '<c:x val="0.55"/><c:y val="0.0"/><c:w val="0.42"/><c:h val="0.10"/></c:manualLayout></c:layout>'))

# footnote
fn = slide.shapes.add_textbox(QX, QY + Inches(2.72), Inches(3.0), Inches(0.35)).text_frame
fn.word_wrap = True
fn.text = ("Per 30x genome. Sequencing ~$600 (2022, NovaSeq 6000) vs ~$200 (2026, NovaSeq X list); "
           "library prep ~$100 and analysis (~$30 research, ~$750 clinical) held flat per ex-Illumina AD. Our calculation.")
for r in fn.paragraphs[0].runs:
    r.font.name, r.font.size, r.font.color.rgb = FONT, Pt(7), RGBColor.from_string("595959")

# quote boxes
quotes = [
    [("“…", ""), ("the library prep is much more expensive than the sequencing", "b"),
     ("… if you drive down the price of sequencing a factor of 2… ", ""),
     ("You might be able to do 20% more.", "b"), ("” – Illumina CEO, Mar 2026", "")],
    [("“…maybe the ", ""), ("price would drop by half", "b"), (", but they would ", ""),
     ("only increase their sequencing by about 25%", "b"), (".” – Former Illumina Assoc. Director", "")],
    [("“The actual sequencing now might only be ", ""), ("5%-10% of the total cost", "b"),
     ("… Reducing it another 10%, 20%, 30%, it ", ""), ("just isn’t really moving the needle", "b"),
     (".” – Former Illumina Assoc. Director", "")],
]
BX, BW, BH, GAP = QX + Inches(3.15), Inches(3.15), Inches(0.93), Inches(0.08)
for k, runs in enumerate(quotes):
    y = QY + k * (BH + GAP)
    shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, BX, y, BW, BH)
    shp.adjustments[0] = 0.08
    shp.fill.solid(); shp.fill.fore_color.rgb = RGBColor.from_string(BOXFILL)
    shp.line.color.rgb = RGBColor.from_string(BOXLINE); shp.line.width = Pt(1)
    shp.line.dash_style = MSO_LINE_DASH_STYLE.DASH
    shp.shadow.inherit = False
    tf = shp.text_frame
    tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.margin_left = tf.margin_right = Inches(0.08); tf.margin_top = tf.margin_bottom = Inches(0.03)
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.LEFT
    for text, style in runs:
        r = p.add_run(); r.text = text
        r.font.name, r.font.size = FONT, Pt(10.5)
        r.font.color.rgb = RGBColor.from_string(INK)
        r.font.bold = style == "b"

prs.save(OUT)
for y in seq:
    print(y, [f"{c}: {v:.0%}" for c, v in zip(cats, share[y])])
