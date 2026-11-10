"""Caris Life Sciences clinical therapy selection volume growth y/y: total vs MI Profile (tissue), native PowerPoint chart.

Two bars per period, only where both are reported or computable from Caris disclosures:
- Total = clinical therapy selection cases y/y as reported (8-K Ex. 99.1); Q2'25/Q3'25 to one decimal, others "approximately".
- Tissue = MI Profile cases y/y.
  - Q2'25 +17.7% and Q3'25 +12.5%: as reported (8-K).
  - FY'25 = 170,300 / 146,500 (FY24 MI Profile, S-1/A).
  - Q1'26 = 43,600 / ~40,000 (Q1'25 MI Profile, S-1/A).
  - Q2'26 = 48,300 / 42,886 (Q2'25 8-K).
- Q1'25 and Q4'25 are omitted: the Q1'24 and Q4'24 MI Profile counts are not disclosed.
Usage: python build.py <out.pptx>
"""
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION, XL_LABEL_POSITION, XL_TICK_LABEL_POSITION, XL_TICK_MARK
from pptx.dml.color import RGBColor
from pptx.oxml.ns import qn, nsdecls
from pptx.oxml import parse_xml

OUT = sys.argv[1]
FONT = "Garamond"
GREY, ORANGE, INK = "BFBFBF", "F5A623", "000000"

cats = ["FY'25", "Q2'25", "Q3'25", "Q1'26", "Q2'26"]
total = [0.22, 0.220, 0.182, 0.15, 0.18]
tissue = [170300 / 146500 - 1, 0.177, 0.125, 43600 / 40000 - 1, 48300 / 42886 - 1]
names = ["Total clinical therapy selection cases y/y", "MI Profile (tissue CGP) cases y/y"]

cd = CategoryChartData()
cd.categories = cats
for n, vals in zip(names, (total, tissue)):
    cd.add_series(n, [round(v, 4) for v in vals], number_format='0%')

prs = Presentation()
prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
slide = prs.slides.add_slide(prs.slide_layouts[6])
gf = slide.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(2.6), Inches(0.8), Inches(8.1), Inches(5.6), cd)
ch = gf.chart
ch.font.name, ch.font.size, ch.font.color.rgb = FONT, Pt(12), RGBColor.from_string(INK)

plot = ch.plots[0]
plot.overlap, plot.gap_width = 0, 80
plot.vary_by_categories = False
for i, s in enumerate(plot.series):
    s.invert_if_negative = False
    s.format.fill.solid(); s.format.fill.fore_color.rgb = RGBColor.from_string([GREY, ORANGE][i])
    s.format.line.fill.background()
    dl = s.data_labels
    dl.show_value, dl.number_format, dl.number_format_is_linked = True, '0%', False
    dl.position = XL_LABEL_POSITION.OUTSIDE_END
    dl.font.name, dl.font.size, dl.font.color.rgb = FONT, Pt(12), RGBColor.from_string(INK)

va = ch.value_axis
va.minimum_scale, va.maximum_scale, va.major_unit = 0.0, 0.30, 0.05
va.has_major_gridlines = False
va.tick_labels.number_format, va.tick_labels.number_format_is_linked = '0%', False
va.tick_labels.font.name, va.tick_labels.font.size = FONT, Pt(12)
va.major_tick_mark = XL_TICK_MARK.OUTSIDE
va.format.line.color.rgb = RGBColor.from_string("808080")

ca = ch.category_axis
ca.tick_label_position = XL_TICK_LABEL_POSITION.LOW
ca.major_tick_mark = XL_TICK_MARK.NONE
ca.tick_labels.font.name, ca.tick_labels.font.size = FONT, Pt(12)
ca.format.line.color.rgb = RGBColor.from_string("808080")

ch.has_legend = True
ch.legend.position, ch.legend.include_in_layout = XL_LEGEND_POSITION.TOP, False
ch.legend.font.name, ch.legend.font.size = FONT, Pt(12)
# stacked legend in the top-left corner over the plot, as in the ILMN stack chart
leg = ch.legend._element
for old in leg.findall(qn("c:layout")):
    leg.remove(old)
lay = parse_xml(
    f'<c:layout {nsdecls("c")}><c:manualLayout><c:xMode val="edge"/><c:yMode val="edge"/>'
    '<c:x val="0.10"/><c:y val="0.0"/><c:w val="0.48"/><c:h val="0.12"/></c:manualLayout></c:layout>')
leg.find(qn("c:legendPos")).addnext(lay)
ch.has_title = False

note = slide.shapes.add_textbox(Inches(2.6), Inches(6.45), Inches(8.1), Inches(0.6)).text_frame
note.word_wrap = True
note.text = ("Source: Caris Life Sciences 8-K earnings releases (Q2'25-Q2'26) and S-1/A (FY24 and Q1'25 MI Profile cases). "
             "Tissue growth for Q2'25 and Q3'25 as reported; FY'25, Q1'26 and Q2'26 calculated from reported case counts. "
             "Q1'25 and Q4'25 omitted: prior-year MI Profile counts not disclosed.")
for p in note.paragraphs:
    for r in p.runs:
        r.font.name, r.font.size, r.font.color.rgb = FONT, Pt(9), RGBColor.from_string("595959")
prs.save(OUT)
for c, t, m in zip(cats, total, tissue):
    print(c, f"total {t:.1%}", f"tissue {m:.1%}")
