"""ILMN implied revenue per Gb change y/y at 30% Gb growth, as a native (editable) PowerPoint chart.

Implied rev/Gb y/y = (1 + sequencing consumables growth) / (1 + Gb growth) - 1, with Gb growth held at 30%
(management: connected high/mid-throughput Gb output grew ">30%" in every 2025-2026 quarter).

All growth is total reported sequencing consumables, the reverse DCF's basis. Nothing uses management guidance:
every forward bar is what the reverse DCF (the buyside-implied case at $235.99, 31 Oct 2026) implies.
- 2025A: $2,939M vs $2,872M (reverse DCF C42/B42).
- 2026 YTD: Q1-Q3'26 $2,293M vs Q1-Q3'25 $2,183M (Q1 726/696, Q2 775/740, Q3 792/747; earnings calls).
- FY26E: reverse DCF 2026E consumables = 2025A x (2026E revenue / 2025A revenue) = $2,939M x 4,620/4,343.
- Q4'26E: reverse DCF FY26E consumables less Q1-Q3 actual, vs Q4'25 $755M.
- FY27E: reverse DCF solved revenue CAGR at $235.99 (10.53%); consumables grow with revenue in the model.
Usage: python build.py <out.pptx>
"""
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION, XL_LABEL_POSITION, XL_TICK_LABEL_POSITION, XL_TICK_MARK
from pptx.dml.color import RGBColor

OUT = sys.argv[1]
GB = 0.30
FONT = "Garamond"
GREY, ORANGE, RED, INK = "BFBFBF", "F5A623", "FF0000", "000000"

q25, q26 = [696, 740, 747, 755], [726, 775, 792]
fy25, fy24 = 2939.0, 2872.0
fy26 = fy25 * 4620 / 4343                     # reverse DCF 2026E consumables
q4 = fy26 - sum(q26)
cagr27 = 0.10532
growth = [("2026 YTD", sum(q26) / sum(q25[:3]) - 1, 0),
          ("Q4'26E", q4 / q25[3] - 1, 1), ("FY26E", fy26 / fy25 - 1, 1), ("FY27E", cagr27, 1)]
cats = [c for c, _, _ in growth]
vals = [(1 + g) / (1 + GB) - 1 for _, g, _ in growth]
names = ["Implied rev/Gb y/y change (at 30% Gb growth)",
         "Buyside-implied (reverse DCF @ $235.99)"]

cd = CategoryChartData()
cd.categories = cats
for s in range(2):
    cd.add_series(names[s], [round(v, 4) if grp == s else None for v, (_, _, grp) in zip(vals, growth)], number_format='0%')

prs = Presentation()
prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
slide = prs.slides.add_slide(prs.slide_layouts[6])
gf = slide.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(2.6), Inches(1.0), Inches(8.1), Inches(5.6), cd)
ch = gf.chart
ch.font.name, ch.font.size, ch.font.color.rgb = FONT, Pt(12), RGBColor.from_string(INK)

plot = ch.plots[0]
plot.overlap, plot.gap_width = 100, 60
plot.vary_by_categories = False
for i, s in enumerate(plot.series):
    s.invert_if_negative = False
    s.format.fill.solid(); s.format.fill.fore_color.rgb = RGBColor.from_string([GREY, ORANGE][i])
    if i == 1:
        s.format.line.color.rgb = RGBColor.from_string(RED); s.format.line.width = Pt(2.25)
    else:
        s.format.line.fill.background()
    dl = s.data_labels
    dl.show_value, dl.number_format, dl.number_format_is_linked = True, '0%;-0%;;', False
    dl.position = XL_LABEL_POSITION.OUTSIDE_END
    dl.font.name, dl.font.size, dl.font.color.rgb = FONT, Pt(12), RGBColor.from_string(INK)

va = ch.value_axis
va.minimum_scale, va.maximum_scale, va.major_unit = -0.25, 0.0, 0.05
va.has_major_gridlines = False
va.tick_labels.number_format, va.tick_labels.number_format_is_linked = '0%', False
va.tick_labels.font.name, va.tick_labels.font.size = FONT, Pt(12)
va.major_tick_mark = XL_TICK_MARK.OUTSIDE
va.format.line.color.rgb = RGBColor.from_string("808080")

ca = ch.category_axis
ca.tick_label_position = XL_TICK_LABEL_POSITION.LOW          # labels at the bottom, bars hang from 0%
ca.major_tick_mark = XL_TICK_MARK.NONE
ca.tick_labels.font.name, ca.tick_labels.font.size = FONT, Pt(12)
ca.format.line.color.rgb = RGBColor.from_string("808080")

ch.has_legend = True
ch.legend.position, ch.legend.include_in_layout = XL_LEGEND_POSITION.TOP, False
ch.legend.font.name, ch.legend.font.size = FONT, Pt(12)
ch.has_title = False
prs.save(OUT)
for (c, g, _), v in zip(growth, vals):
    print(c, f"consumables {g:+.1%}", f"rev/Gb {v:.1%}")
