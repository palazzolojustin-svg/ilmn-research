"""One slide, WGO deck format: JPM customer survey's implied 2027 volume, spend and price change vs Illumina's Q3'26 revenue per Gb.

Survey (JPM, Jun 2026, deck L23, L256, L260), average expected change 2027 vs 2026:
    academic: consumables volume +11.4%, spend +9.0%; clinical: volume +14.6%, spend +9.4%
Blended 65% clinical / 35% research (ILMN Q2'26 sequencing-consumables mix, Bloomberg Intelligence 31 Jul 2026).
Implied price = (1 + spend) / (1 + volume) - 1.
Q3'26: sequencing consumables +6% y/y, connected Gb output growth "above 30%" (Q3'26 call L73, L83)
    -> revenue per Gb = 1.06 / 1.30 - 1 = -18.5% (Gb >30%, so the decline is at least this large).
Layout follows the deck: two columns (0.20 / 5.17 in, 4.60 in wide), section heads at y=1.22 and 4.03,
black-header "no grid" tables, 8 pt italic footnote at y=6.97.
Usage: python -I build.py <WGO-format deck.pptx> <out.pptx>
"""
import sys
from lxml import etree
from pptx import Presentation
from pptx.chart.data import CategoryChartData
from pptx.dml.color import RGBColor
from pptx.enum.chart import XL_CHART_TYPE, XL_LABEL_POSITION, XL_TICK_LABEL_POSITION
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Inches, Pt

DECK, OUT = sys.argv[1], sys.argv[2]
FONT = "Garamond"
ORANGE, GREY = "E8962E", "6D6E71"
LX, LW, RX, RW = 0.20, 4.60, 5.17, 4.60

acad = dict(vol=0.114, spend=0.090)
clin = dict(vol=0.146, spend=0.094)
blend = {k: 0.65 * clin[k] + 0.35 * acad[k] for k in ("vol", "spend")}
price = lambda d: (1 + d["spend"]) / (1 + d["vol"]) - 1
actual = 1.06 / 1.30 - 1


def pct(v, plus=False):
    return f"({abs(v) * 100:.1f}%)" if v < 0 else (f"+{v * 100:.1f}%" if plus else f"{v * 100:.1f}%")


prs = Presentation(DECK)
ids = prs.slides._sldIdLst
for sid in list(ids):
    prs.part.drop_rel(sid.rId)
    ids.remove(sid)
s = prs.slides.add_slide(next(l for l in prs.slide_layouts if l.name == "Content"))
s.shapes.title.text = "Customer Survey vs. Reported Pricing"
for ph in s.placeholders:
    if ph.placeholder_format.idx == 1:
        ph.text = "Customers imply ~4% price erosion in 2027; Q3'26 revenue per Gb fell ~19%"


def text(x, y, w, h, t, size=12, bold=False, italic=False, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.MIDDLE,
         color="000000", name=None):
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    if name:
        tb.name = name
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Inches(0.05)
    tf.margin_top = tf.margin_bottom = Inches(0.02)
    p = tf.paragraphs[0]
    p.alignment = align
    r = p.add_run()
    r.text = t
    f = r.font
    f.name, f.size, f.bold, f.italic = FONT, Pt(size), bold, italic
    f.color.rgb = RGBColor.from_string(color)
    return tb


def section_head(x, w, y, label):
    text(x, y, w, 0.3, label, 13, bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.BOTTOM, name=f"Header {label}")
    ln = s.shapes.add_connector(1, Inches(x), Inches(y + 0.32), Inches(x + w), Inches(y + 0.32))
    ln.line.color.rgb = RGBColor.from_string("000000")
    ln.line.width = Pt(1.0)


def table(x, y, w, header, rows, col_w, row_h=0.32, name="Table"):
    """The deck's blank_table style: black header row, white text, no grid; first column italic.
    header=None gives a plain label/value table with no header row."""
    hdr = header is not None
    if not hdr:
        header = [""] * len(rows[0])
    n_r, n_c = len(rows) + int(hdr), len(header)
    shp = s.shapes.add_table(n_r, n_c, Inches(x), Inches(y), Inches(w), Inches(row_h * n_r))
    shp.name = name
    tbl = shp.table
    tblPr = tbl._tbl.tblPr
    tblPr.set("firstRow", "0")
    tblPr.set("bandRow", "0")
    sid = tblPr.find(qn("a:tableStyleId"))
    if sid is None:
        sid = etree.SubElement(tblPr, qn("a:tableStyleId"))
    sid.text = "{2D5ABB26-0587-4C30-8999-92F81FD0307C}"  # No Style, No Grid
    for i, cw in enumerate(col_w):
        tbl.columns[i].width = Inches(cw)
    for r in range(n_r):
        tbl.rows[r].height = Inches(row_h)
        for c in range(n_c):
            cell = tbl.cell(r, c)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            cell.margin_left = cell.margin_right = Inches(0.05)
            ri = r - int(hdr)
            val = header[c] if ri < 0 else rows[ri][c]
            p = cell.text_frame.paragraphs[0]
            p.alignment = PP_ALIGN.CENTER if ri < 0 else (PP_ALIGN.LEFT if c == 0 else PP_ALIGN.RIGHT)
            run = p.add_run()
            run.text = val
            bold_row = ri == len(rows) - 1 and rows[-1][0].startswith("Reported")
            run.font.name, run.font.size = FONT, Pt(11)
            run.font.italic = (c == 0 and ri >= 0)
            run.font.bold = bold_row
            run.font.color.rgb = RGBColor.from_string("FFFFFF" if ri < 0 else "000000")
            if ri < 0:
                cell.fill.solid()
                cell.fill.fore_color.rgb = RGBColor.from_string("000000")
            else:
                cell.fill.background()
    return tbl


# ---------------- left: chart ----------------
section_head(LX, LW, 1.22, "Implied Change in Price per Gb")
cd = CategoryChartData(number_format='0.0%;(0.0%)')
g1 = cd.add_category("JPM Survey, 2027E")
for c in ("Volume", "Spend", "Price"):
    g1.add_sub_category(c)
g2 = cd.add_category("Q3'26A")
g2.add_sub_category("Rev. / Gb")
cd.add_series("Change", [blend["vol"], blend["spend"], price(blend), actual])
gf = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(LX), Inches(1.62), Inches(LW), Inches(5.25), cd)
gf.name = "Chart"
ch = gf.chart
ch.has_legend = False
ch.has_title = False
ch.font.name, ch.font.size = FONT, Pt(11)
plot = ch.plots[0]
plot.gap_width = 55
plot.vary_by_categories = False
ser = plot.series[0]
ser.invert_if_negative = False
for i, col in enumerate([GREY, GREY, GREY, ORANGE]):
    pt = ser.points[i]
    pt.format.fill.solid()
    pt.format.fill.fore_color.rgb = RGBColor.from_string(col)
    pt.format.line.fill.background()
for dpt in ser._element.findall(qn("c:dPt")):  # keep negative bars filled (PowerPoint inverts them otherwise)
    if dpt.find(qn("c:invertIfNegative")) is None:
        inv = etree.Element(qn("c:invertIfNegative"))
        inv.set("val", "0")
        dpt.find(qn("c:idx")).addnext(inv)
plot.has_data_labels = True
dl = plot.data_labels
dl.number_format = '0.0%;(0.0%)'
dl.number_format_is_linked = False
dl.position = XL_LABEL_POSITION.OUTSIDE_END
dl.font.name, dl.font.size = FONT, Pt(12)
va = ch.value_axis
va.minimum_scale, va.maximum_scale = -0.22, 0.18
va.has_major_gridlines = False
va.tick_label_position = XL_TICK_LABEL_POSITION.NONE
va.format.line.fill.background()
ca = ch.category_axis
ca.tick_label_position = XL_TICK_LABEL_POSITION.LOW
ca.tick_labels.font.name, ca.tick_labels.font.size = FONT, Pt(11)
ca.format.line.color.rgb = RGBColor.from_string("000000")

# ---------------- right: detail tables ----------------
section_head(RX, RW, 1.22, "Survey Detail, 2027E vs. 2026")
rows = [
    ["Academic (n=30)", pct(acad["vol"], True), pct(acad["spend"], True), pct(price(acad))],
    ["Clinical (n=32)", pct(clin["vol"], True), pct(clin["spend"], True), pct(price(clin))],
    ["Blended (65/35)", pct(blend["vol"], True), pct(blend["spend"], True), pct(price(blend))],
    ["Reported Q3'26 y/y", ">30%", "+6.0%", pct(actual)],
]
table(RX, 1.72, RW, ["", "Volume", "Spend", "Price / Gb"], rows, [1.75, 0.95, 0.95, 0.95], name="Survey Detail Table")

section_head(RX, RW, 4.03, "Survey Base")
base = [
    ["Respondents", "62 current ILMN customers"],
    ["Mix", "30 academic / 32 clinical"],
    ["Region", "~65% North America, rest Europe"],
    ["Spend measured", "Lab-wide, all vendors"],
    ["Fielded", "May–Jun 2026"],
]
table(RX, 4.45, RW, None, base, [1.55, 3.05], row_h=0.32, name="Survey Base Table")

text(LX, 6.97, 9.57, 0.40,
     "Source: J.P. Morgan ILMN Customer Survey (Jun 2026); company reports. Survey figures are average expected 2027 vs. 2026 "
     "change in sequencing consumables volume and spend; blended at ILMN's Q2'26 sequencing consumables mix (65% clinical / 35% "
     "research). Price = (1 + spend) / (1 + volume) − 1. Q3'26 revenue per Gb = 1.06 / 1.30 − 1; management cited Gb "
     "growth above 30%, so the reported decline is a floor.",
     size=8, italic=True, color="595959", anchor=MSO_ANCHOR.TOP, name="Footnote")

prs.save(OUT)
print("saved", OUT)
