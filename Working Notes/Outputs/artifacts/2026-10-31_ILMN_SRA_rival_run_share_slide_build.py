"""Rival (Element AVITI + MGI DNBSEQ-T7) share of public SRA sequencing runs: native PowerPoint chart + methodology box.

Data: datasets/2026-10-12_thesis_scrape_findings.csv, rows F611 (share of runs) and D056 (share of y/y run growth).
- Share of 6000+X+AVITI+T7 run releases: Q3'24 13,360/581,731 = 2.3%; Q3'25 17,844/489,660 = 3.6%; Q3'26 45,982/606,789 = 7.6%.
- Share of y/y increase in new-platform runs: Q3'25 4,484/48,458 = 9.3%; Q3'26 28,138/119,897 = 23.5%.
Run counts, not Gb. Ultima excluded (instrument string did not resolve), so rival share is understated.
Usage: python build.py <out.pptx>
"""
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION, XL_LABEL_POSITION, XL_TICK_LABEL_POSITION, XL_TICK_MARK
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.dml import MSO_LINE_DASH_STYLE
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.oxml.ns import qn, nsdecls
from pptx.oxml import parse_xml

OUT = sys.argv[1]
FONT = "Garamond"
GREY, ORANGE, RED, INK, HILITE = "BFBFBF", "F5A623", "FF0000", "000000", "E8930C"

cats = ["Q3'24", "Q3'25", "Q3'26"]
share = [13360 / 581731, 17844 / 489660, 45982 / 606789]
capture = [None, 4484 / 48458, 28138 / 119897]
names = ["Rival share of all public runs", "Rival share of y/y growth in runs"]

prs = Presentation()
prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
slide = prs.slides.add_slide(prs.slide_layouts[6])

# ---- chart (left) ----
CX, CY, CW, CH = Inches(0.4), Inches(1.2), Inches(7.6), Inches(4.9)
cd = CategoryChartData()
cd.categories = cats
cd.add_series(names[0], [round(v, 4) for v in share], number_format='0.0%')
cd.add_series(names[1], [None if v is None else round(v, 4) for v in capture], number_format='0.0%')
ch = slide.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, CX, CY, CW, CH, cd).chart
ch.font.name, ch.font.size, ch.font.color.rgb = FONT, Pt(12), RGBColor.from_string(INK)
plot = ch.plots[0]
plot.overlap, plot.gap_width = 0, 70
plot.vary_by_categories = False
for i, s in enumerate(plot.series):
    s.invert_if_negative = False
    s.format.fill.solid(); s.format.fill.fore_color.rgb = RGBColor.from_string([GREY, ORANGE][i])
    s.format.line.fill.background()
    dl = s.data_labels
    dl.show_value, dl.number_format, dl.number_format_is_linked = True, '0.0%', False
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
ch.has_title = False
ch.has_legend = True
ch.legend.position, ch.legend.include_in_layout = XL_LEGEND_POSITION.TOP, False
ch.legend.font.name, ch.legend.font.size = FONT, Pt(12)
leg = ch.legend._element
for old in leg.findall(qn("c:layout")):
    leg.remove(old)
leg.find(qn("c:legendPos")).addnext(parse_xml(
    f'<c:layout {nsdecls("c")}><c:manualLayout><c:xMode val="edge"/><c:yMode val="edge"/>'
    '<c:x val="0.10"/><c:y val="0.0"/><c:w val="0.55"/><c:h val="0.13"/></c:manualLayout></c:layout>'))

# red dashed highlight around the Q3'26 group (position tuned by render check)
box = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(5.95), Inches(1.55), Inches(1.95), Inches(4.2))
box.fill.solid(); box.fill.fore_color.rgb = RGBColor.from_string("FDECEC")
box.fill.transparency = 0.5
box.line.color.rgb = RGBColor.from_string(RED); box.line.width = Pt(1.25)
box.line.dash_style = MSO_LINE_DASH_STYLE.DASH
# make fill semi-transparent via XML alpha
sf = box.fill._xPr.find(qn("a:solidFill"))
sf[0].append(parse_xml(f'<a:alpha {nsdecls("a")} val="45000"/>'))
# send highlight box behind the chart
sp = box._element; tree = sp.getparent(); tree.remove(sp); tree.insert(2, sp)

# ---- methodology box (right) ----
MX, MY, MW = Inches(8.25), Inches(1.0), Inches(4.75)
hdr = slide.shapes.add_textbox(MX, MY, MW, Inches(0.4)).text_frame
hdr.text = "Our Methodology"
p = hdr.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
r = p.runs[0]; r.font.name, r.font.size, r.font.italic = FONT, Pt(14), True
ln = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, MX, MY + Inches(0.42), MX + MW, MY + Inches(0.42))
ln.line.color.rgb = RGBColor.from_string(INK); ln.line.width = Pt(1)

steps = [
    [("[1] ", "b"), ("Queried NCBI's public Sequence Read Archive (SRA), where researchers deposit raw sequencing data, by instrument model for every run released in Q3'24, Q3'25 and Q3'26.", "")],
    [("[2] ", "b"), ("Counted runs on Illumina's NovaSeq 6000 and NovaSeq X against rivals Element AVITI and MGI DNBSEQ-T7.", "")],
    [("[3] ", "b"), ("Calculated the rivals' share of all runs, and their share of the year-over-year increase in runs.", "")],
    [("[4] ", "b"), ("~1.7M", "b"), (" runs across the three quarters, ", ""), ("~46K", "b"),
     (" on rival platforms in Q3'26. Ultima is excluded (its instrument name does not resolve in SRA), so rival share is understated.", "")],
    [("[5] ", "b"), ("Rivals' share of runs more than tripled, from 2.3% to 7.6% in two years", "h"),
     (", and rivals captured ", ""), ("23.5% of y/y run growth in Q3'26, up from 9.3% a year earlier", "h"), (".", "")],
]
tb = slide.shapes.add_textbox(MX, MY + Inches(0.5), MW, Inches(4.9)).text_frame
tb.word_wrap = True
for k, runs in enumerate(steps):
    p = tb.paragraphs[0] if k == 0 else tb.add_paragraph()
    p.space_after = Pt(4)
    for text, style in runs:
        r = p.add_run(); r.text = text
        r.font.name, r.font.size = FONT, Pt(14)
        r.font.color.rgb = RGBColor.from_string(INK)
        if style == "b":
            r.font.bold = True
        if style == "h":
            r.font.bold, r.font.underline = True, True
            r.font.color.rgb = RGBColor.from_string(HILITE)

# orange rule along the bottom, as in the reference slide
bl = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(0.4), Inches(6.35), MX + MW, Inches(6.35))
bl.line.color.rgb = RGBColor.from_string(ORANGE); bl.line.width = Pt(2)

src = slide.shapes.add_textbox(Inches(0.4), Inches(6.4), Inches(12.6), Inches(0.35)).text_frame
src.text = ("Source: NCBI SRA run releases by instrument model (queried 12 Oct 2026). Rivals = Element AVITI + MGI DNBSEQ-T7. "
            "Run counts, not gigabases; most Q3'26 rival growth is DNBSEQ-T7.")
for r in src.paragraphs[0].runs:
    r.font.name, r.font.size, r.font.color.rgb = FONT, Pt(9), RGBColor.from_string("595959")

prs.save(OUT)
print([f"{v:.1%}" for v in share], [None if v is None else f"{v:.1%}" for v in capture])
