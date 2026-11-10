"""ILMN pitch deck shell in the WGO (Texas Stock Pitch) slide-master format, recolored to Illumina.

- 10 x 7.5 in (4:3), the WGO deck's size.
- Theme: Garamond, Illumina orange E8962E / greys.
- Layouts: "Cover" (blank), "Content" (title + subtitle, logo top right, black rule, grey bottom rule),
  "Section TOC" (title + logo over a black/orange rule, WGO divider style).
- Slides: the ILMN v1 cover rescaled from 13.33 in to 10 in wide, TOC dividers between sections,
  a blank Executive Summary, and blank Variance Summaries for Thesis 1 and Thesis 2.
Usage: python build.py <ILMN source.pptx> <out.pptx>
"""
import copy
import io
import re
import sys
import zipfile

from lxml import etree
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.dml import MSO_LINE_DASH_STYLE
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Emu, Inches, Pt

SRC, OUT = sys.argv[1], sys.argv[2]
FONT = "Garamond"
ORANGE, GREY_LOGO, DARK, LIGHT_GREY = "E8962E", "6D6E71", "3A3A3A", "BFBFBF"
TINT, BOX_FILL, QUOTE_FILL = "F9DDBA", "FDF1E3", "F2F2F2"
NS = {"a": "http://schemas.openxmlformats.org/drawingml/2006/main",
      "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
      "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships"}
NSDECL = ('xmlns:a="%s" xmlns:p="%s" xmlns:r="%s"' % (NS["a"], NS["p"], NS["r"]))
EMU = 914400

SECTIONS = [
    ("Executive Summary", "Executive Summary"),
    ("Industry Overview", "Industry Overview"),
    ("Company Overview", "Company Overview"),
    ("Thesis Overview", "Thesis Overview"),
    ("Thesis One", "Thesis One: ILMN is Overearning on Unconverted Customers"),
    ("Thesis Two", "Thesis Two: We Expect Discounting to Accelerate"),
    ("Valuation", "Valuation"),
    ("Risks, Mitigants, & Catalyst Path", "Risks, Mitigants, & Catalyst Path"),
    ("Appendix", "Appendix"),
]

src = zipfile.ZipFile(SRC)
logo_png = io.BytesIO(src.read("ppt/media/image3.png"))  # the illumina wordmark on the v1 cover

prs = Presentation()  # default template is 10 x 7.5 in
prs.slide_width, prs.slide_height = Inches(10), Inches(7.5)
master = prs.slide_master

# ---------------- theme: Illumina colors, Garamond ----------------
theme_part = master.part.part_related_by("http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme")
theme = etree.fromstring(theme_part.blob)
clr = theme.find(".//a:clrScheme", NS)
clr.set("name", "Illumina")
for tag, val in [("dk1", "000000"), ("lt1", "FFFFFF"), ("dk2", DARK), ("lt2", "E0E0E0"),
                 ("accent1", ORANGE), ("accent2", GREY_LOGO), ("accent3", "F9A31E"),
                 ("accent4", TINT), ("accent5", "595959"), ("accent6", LIGHT_GREY),
                 ("hlink", ORANGE), ("folHlink", GREY_LOGO)]:
    el = clr.find("a:" + tag, NS)
    for c in list(el):
        el.remove(c)
    etree.SubElement(el, qn("a:srgbClr")).set("val", val)
fs = theme.find(".//a:fontScheme", NS)
fs.set("name", "Garamond")
for f in ("majorFont", "minorFont"):
    fs.find("a:%s/a:latin" % f, NS).set("typeface", FONT)
# take the fill/line/effect styles from the ILMN deck's theme so copied shapes keep their look (no stray shadows)
src_theme = etree.fromstring(src.read("ppt/theme/theme1.xml"))
fmt = theme.find(".//a:fmtScheme", NS)
fmt.getparent().replace(fmt, copy.deepcopy(src_theme.find(".//a:fmtScheme", NS)))
theme_part._blob = etree.tostring(theme, xml_declaration=True, encoding="UTF-8", standalone=True)

# ---------------- layouts ----------------
layouts = list(prs.slide_layouts)
L_COVER, L_CONTENT, L_TOC = layouts[6], layouts[5], layouts[2]
for lay in layouts:
    if lay not in (L_COVER, L_CONTENT, L_TOC):
        prs.slide_layouts.remove(lay)


def emu(v):
    return int(round(v * EMU))


def xfrm(x, y, w, h):
    return '<a:xfrm><a:off x="%d" y="%d"/><a:ext cx="%d" cy="%d"/></a:xfrm>' % (emu(x), emu(y), emu(w), emu(h))


def ph_xml(sid, name, ph, x, y, w, h, sz, bold, color, anchor="b"):
    b = ' b="1"' if bold else ' b="0"'
    return (
        f'<p:sp {NSDECL}><p:nvSpPr><p:cNvPr id="{sid}" name="{name}"/><p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr>'
        f'<p:nvPr>{ph}</p:nvPr></p:nvSpPr><p:spPr>{xfrm(x, y, w, h)}</p:spPr>'
        f'<p:txBody><a:bodyPr lIns="0" tIns="0" rIns="0" bIns="0" anchor="{anchor}"><a:normAutofit/></a:bodyPr>'
        f'<a:lstStyle><a:lvl1pPr marL="0" indent="0" algn="l"><a:buNone/>'
        f'<a:defRPr sz="{sz}"{b} i="0"><a:solidFill><a:srgbClr val="{color}"/></a:solidFill>'
        f'<a:latin typeface="{FONT}"/></a:defRPr></a:lvl1pPr></a:lstStyle>'
        f'<a:p><a:endParaRPr lang="en-US"/></a:p></p:txBody></p:sp>')


def line_xml(sid, name, x1, y, x2, color, width_pt):
    return (
        f'<p:cxnSp {NSDECL}><p:nvCxnSpPr><p:cNvPr id="{sid}" name="{name}"/><p:cNvCxnSpPr/><p:nvPr userDrawn="1"/></p:nvCxnSpPr>'
        f'<p:spPr>{xfrm(x1, y, x2 - x1, 0)}<a:prstGeom prst="line"><a:avLst/></a:prstGeom>'
        f'<a:ln w="{int(width_pt * 12700)}"><a:solidFill><a:srgbClr val="{color}"/></a:solidFill></a:ln></p:spPr></p:cxnSp>')


def pic_xml(sid, name, rid, x, y, w, h):
    return (
        f'<p:pic {NSDECL}><p:nvPicPr><p:cNvPr id="{sid}" name="{name}" descr="Illumina logo"/><p:cNvPicPr><a:picLocks noChangeAspect="1"/></p:cNvPicPr>'
        f'<p:nvPr userDrawn="1"/></p:nvPicPr><p:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></p:blipFill>'
        f'<p:spPr>{xfrm(x, y, w, h)}<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></p:spPr></p:pic>')


def rebuild_layout(lay, name, parts):
    lay.name = name
    tree = lay.shapes._spTree
    for child in list(tree)[2:]:  # keep nvGrpSpPr and grpSpPr
        tree.remove(child)
    for xml in parts:
        tree.append(etree.fromstring(xml))


LOGO_W = 1.90
LOGO_H = LOGO_W * 0.8287 / 3.4774  # source aspect ratio
_, rid_c = L_CONTENT.part.get_or_add_image_part(logo_png)
logo_png.seek(0)
_, rid_t = L_TOC.part.get_or_add_image_part(logo_png)

rebuild_layout(L_COVER, "Cover", [])
rebuild_layout(L_CONTENT, "Content", [
    ph_xml(2, "Title", '<p:ph type="title"/>', 0.33, 0.30, 7.2, 0.50, 2600, True, "000000"),
    ph_xml(3, "Subtitle", '<p:ph type="body" idx="1"/>', 0.33, 0.80, 7.2, 0.30, 1600, False, "000000", anchor="t"),
    pic_xml(4, "Illumina Logo", rid_c, 9.77 - LOGO_W, 0.33, LOGO_W, LOGO_H),
    line_xml(5, "Header Rule", 0.20, 1.14, 9.77, "000000", 2.25),
    line_xml(6, "Footer Rule", 0.20, 6.95, 9.77, LIGHT_GREY, 1.0),
])
rebuild_layout(L_TOC, "Section TOC", [
    ph_xml(2, "Title", '<p:ph type="title"/>', 0.30, 2.14, 7.0, 0.52, 2800, True, DARK),
    pic_xml(3, "Illumina Logo", rid_t, 9.77 - LOGO_W, 2.14, LOGO_W, LOGO_H),
    line_xml(4, "Rule Black", 0.20, 2.74, 7.37, "000000", 2.25),
    line_xml(5, "Rule Orange", 7.37, 2.74, 9.77, ORANGE, 2.25),
])

# ---------------- helpers for slide content ----------------


def rgb(h):
    return RGBColor.from_string(h)


def text(slide, x, y, w, h, s="", size=14, bold=False, italic=False, align=PP_ALIGN.LEFT,
         anchor=MSO_ANCHOR.MIDDLE, color="000000", name=None):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
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
    r.text = s
    f = r.font
    f.name, f.size, f.bold, f.italic = FONT, Pt(size), bold, italic
    f.color.rgb = rgb(color)
    return tb


def hline(slide, x1, y, x2, color="000000", w=1.0, name=None):
    ln = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y), Inches(x2), Inches(y))
    ln.line.color.rgb = rgb(color)
    ln.line.width = Pt(w)
    if name:
        ln.name = name
    return ln


def box(slide, x, y, w, h, fill=None, line=None, dash=False, name=None, shape=MSO_SHAPE.RECTANGLE):
    s = slide.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    if fill:
        s.fill.solid()
        s.fill.fore_color.rgb = rgb(fill)
    else:
        s.fill.background()
    if line:
        s.line.color.rgb = rgb(line)
        s.line.width = Pt(1.0)
        if dash:
            s.line.dash_style = MSO_LINE_DASH_STYLE.DASH
    else:
        s.line.fill.background()
    s.shadow.inherit = False
    if name:
        s.name = name
    tf = s.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.1)
    return s


def set_title(slide, title, subtitle=None):
    slide.shapes.title.text = title
    if subtitle is not None:
        for ph in slide.placeholders:
            if ph.placeholder_format.idx == 1:
                ph.text = subtitle


def blank_table(slide, x, y, w, rows, cols, row_h, header, col_w=None, name="Table"):
    shp = slide.shapes.add_table(rows, cols, Inches(x), Inches(y), Inches(w), Inches(row_h * rows))
    shp.name = name
    tbl = shp.table
    tblPr = tbl._tbl.tblPr
    tblPr.set("firstRow", "0")
    tblPr.set("bandRow", "0")
    sid = tblPr.find(qn("a:tableStyleId"))
    if sid is None:
        sid = etree.SubElement(tblPr, qn("a:tableStyleId"))
    sid.text = "{2D5ABB26-0587-4C30-8999-92F81FD0307C}"  # No Style, No Grid
    if col_w:
        for i, cw in enumerate(col_w):
            tbl.columns[i].width = Inches(cw)
    for r in range(rows):
        tbl.rows[r].height = Inches(row_h)
        for c in range(cols):
            cell = tbl.cell(r, c)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            cell.margin_left = cell.margin_right = Inches(0.05)
            label = header[c] if r == 0 else ""
            p = cell.text_frame.paragraphs[0]
            p.alignment = PP_ALIGN.LEFT if c == 0 else PP_ALIGN.RIGHT
            run = p.add_run()
            run.text = label
            run.font.name, run.font.size = FONT, Pt(12)
            run.font.italic = (c == 0 and r > 0)
            run.font.color.rgb = rgb("FFFFFF" if r == 0 else "000000")
            if r == 0:
                cell.fill.solid()
                cell.fill.fore_color.rgb = rgb("000000")
                p.alignment = PP_ALIGN.CENTER
            else:
                cell.fill.background()
    return tbl


def quote_box(slide, x, y, w, h, mark=True):
    box(slide, x, y, w, h, fill=QUOTE_FILL, name="Quote Box")
    if mark:
        text(slide, x - 0.25, y - 0.25, 0.8, 0.8, "“", size=66, bold=True, color=ORANGE,
             anchor=MSO_ANCHOR.TOP, name="Quote Mark")
    text(slide, x + 0.15, y + 0.2, w - 0.3, h - 0.75, "", size=14, anchor=MSO_ANCHOR.TOP, name="Quote Text")
    text(slide, x + 0.15, y + h - 0.5, w - 0.3, 0.35, "", size=14, italic=True, align=PP_ALIGN.CENTER,
         name="Quote Attribution")


# ---------------- 1. cover: ILMN v1 cover rescaled to 10 in wide ----------------
cover = prs.slides.add_slide(L_COVER)
src_xml = etree.fromstring(src.read("ppt/slides/slide1.xml"))
SX = 10.0 / 13.333333
logo_png.seek(0)
_, rid_cover = cover.part.get_or_add_image_part(logo_png)
tree = cover.shapes._spTree
for el in src_xml.find(".//p:cSld/p:spTree", NS)[2:]:
    el = copy.deepcopy(el)
    for off in el.iter(qn("a:off")):
        off.set("x", str(int(int(off.get("x")) * SX)))
    for ext in el.iter(qn("a:ext")):
        if ext.get("cx") is not None:
            ext.set("cx", str(int(int(ext.get("cx")) * SX)))
    for tag in ("a:rPr", "a:defRPr", "a:endParaRPr"):
        for rp in el.iter(qn(tag)):
            rp.set("sz", str(int(int(rp.get("sz", "1800")) * SX)))
    for blip in el.iter(qn("a:blip")):
        blip.set(qn("r:embed"), rid_cover)
        for ext in blip.findall(qn("a:extLst")):  # source-only extensions can point at parts we don't copy
            blip.remove(ext)
    tree.append(el)

# ---------------- slides ----------------


def toc_slide(active):
    s = prs.slides.add_slide(L_TOC)
    set_title(s, SECTIONS[active][0])
    y0, step, h = 2.86, 0.33, 0.31
    for i, (_, full) in enumerate(SECTIONS):
        y = y0 + i * step
        if i == active:
            box(s, 0.20, y, 9.57, h, fill=TINT, name="TOC Highlight")
        text(s, 0.25, y, 9.4, h, full, size=16, bold=(i == active),
             color=DARK if i == active else "000000", name=f"TOC Item {i + 1}")
    return s


def exec_summary():
    s = prs.slides.add_slide(L_CONTENT)
    set_title(s, "Executive Summary", "")
    # left: company description + market data
    text(s, 0.33, 1.35, 4.0, 1.85, "", size=16, anchor=MSO_ANCHOR.TOP, name="Company Description")
    text(s, 0.20, 3.28, 4.05, 0.3, "Market Data & Valuation", size=13, bold=True, align=PP_ALIGN.CENTER)
    hline(s, 0.20, 3.58, 4.25, w=1.0)
    labels = ["Base Case Price Target", "Time Horizon", "Current Price", "Market Cap",
              "52 Week Range", "Beta", "EV/EBITDA Multiple", "Short Interest"]
    for i, lab in enumerate(labels):
        y = 3.72 + i * 0.378
        text(s, 0.65, y, 2.2, 0.32, lab, size=13, bold=True, name=f"Data Label {i + 1}")
        text(s, 2.85, y, 0.95, 0.32, "", size=13, bold=True, align=PP_ALIGN.RIGHT, name=f"Data Value {i + 1}")
    # right: theses at a glance
    text(s, 4.65, 1.18, 5.12, 0.3, "Theses-at-a-Glance", size=13, bold=True, align=PP_ALIGN.CENTER)
    hline(s, 4.65, 1.47, 9.77, w=1.0)
    for i, (by, dy) in enumerate([(1.70, 2.62), (3.62, 4.54)]):
        b = box(s, 4.65, by, 5.07, 0.80, fill=BOX_FILL, line=ORANGE, dash=True, name=f"Thesis {i + 1} Box")
        b.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
        b.text_frame.paragraphs[0].alignment = PP_ALIGN.LEFT
        r = b.text_frame.paragraphs[0].add_run()
        r.text = f"{i + 1}. "
        r.font.name, r.font.size, r.font.bold = FONT, Pt(14), True
        r.font.color.rgb = rgb("000000")
        text(s, 4.70, dy, 5.0, 0.80, "", size=14, anchor=MSO_ANCHOR.TOP, name=f"Thesis {i + 1} Description")
    for i, lab in enumerate(["Total Upside", "Total Downside", "Reward/Risk"]):
        y = 5.55 + i * 0.38
        text(s, 5.95, y, 1.6, 0.32, lab, size=13, bold=True, name=f"Return Label {i + 1}")
        text(s, 7.55, y, 0.85, 0.32, "", size=13, bold=True, align=PP_ALIGN.RIGHT, name=f"Return Value {i + 1}")


def variance_header(s, cols, line_y, head_h):
    centers = [1.16, 3.07, 4.98, 6.88, 8.77]
    widths = [1.5, 2.3, 1.5, 2.1, 1.5]
    for c, cx, w in zip(cols, centers, widths):
        text(s, cx - w / 2, line_y - head_h - 0.04, w, head_h, c, size=15, bold=True,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.BOTTOM, name=f"Header {c}")
    hline(s, 0.20, line_y, 9.77, w=1.0)


def variance_rows(s, ys, h):
    centers = [1.16, 3.07, 4.98, 6.88, 8.77]
    widths = [1.75, 1.85, 1.75, 1.95, 1.75]
    for i, y in enumerate(ys):
        box(s, 0.20, y, 9.53, h, line="404040", dash=True, name=f"Variance Row {i + 1}")
        for j, (cx, w) in enumerate(zip(centers, widths)):
            text(s, cx - w / 2, y + 0.05, w, h - 0.1, "", size=14, bold=(j in (0, 4)), italic=(j == 0),
                 align=PP_ALIGN.CENTER, name=f"Row {i + 1} Col {j + 1}")


def variance_1():
    s = prs.slides.add_slide(L_CONTENT)
    set_title(s, "1: Variance Summary", "“What makes the stock go down?”")
    variance_header(s, ["KPI", "FY 2027E Consensus", "Our View", "Source of Variance", "Impact"], 1.56, 0.32)
    variance_rows(s, [1.73, 2.87], 0.98)
    blank_table(s, 0.20, 4.09, 5.22, 7, 5, 0.40, ["", "", "", "", ""],
                col_w=[1.82, 0.85, 0.85, 0.85, 0.85], name="Quarterly Build")
    quote_box(s, 5.86, 4.16, 3.73, 2.68, mark=True)


def variance_2():
    s = prs.slides.add_slide(L_CONTENT)
    set_title(s, "2: Variance Summary", "“What makes the stock go down?”")
    variance_header(s, ["KPI", "FY 2027E Consensus", "Our View", "Source of Variance", "Impact"], 1.73, 0.5)
    variance_rows(s, [1.93, 2.72, 3.53], 0.70)
    blank_table(s, 0.20, 4.66, 4.78, 6, 4, 0.33, ["", "", "", ""],
                col_w=[1.25, 1.18, 1.18, 1.17], name="Annual Build")
    quote_box(s, 5.30, 4.66, 4.45, 1.95, mark=False)


# ---------------- company overview ----------------
# Revenue by type ($M): consumables / instruments / service & other. FY24, FY25: ILMN 10-K FY2025 "Revenue by Source".
# LTM (Q4'25-Q3'26) = FY25 + YTD Q3'26 - YTD Q3'25, from the Q3'26 10-Q "Revenue by Source".
MIX = {"FY24": (3155, 501, 716), "FY25": (3227, 482, 634),
       "LTM": (3227 + 2490 - 2395, 482 + 355 - 324, 634 + 535 - 465)}
LTM_TOTAL = sum(MIX["LTM"])
LTM_SEQ_CONS = 2939 + 2265 - 2183  # sequencing consumables
SPLIT = [("Sequencing consumables", LTM_SEQ_CONS), ("Instruments", MIX["LTM"][1]),
         ("Other (arrays, service)", LTM_TOTAL - LTM_SEQ_CONS - MIX["LTM"][1])]
# ex-China sequencing consumables y/y. FY24/FY25 reported (Q3'25 and Q4'25 decks). LTM is our calculation from the
# quarterly ex-China dollar estimates (datasets 2026-10-31 clinical and 2026-11-02 research files):
# clinical 438+466+481+496 vs 365+389+419+435; research 275+221+252+255 vs 275+252+271+272.
QTRS = ["Q1'25", "Q2'25", "Q3'25", "Q4'25", "Q1'26", "Q2'26", "Q3'26"]
CLIN_Q = [0.08, 0.10, 0.12, 0.20, 0.20, 0.15, 0.14]  # Q3'26 deck "Sequencing Revenue Detail", ROW reported
RA_Q = [-0.11, -0.09, -0.08, 0.00, -0.12, -0.07, -0.06]
GROWTH_CATS = ["FY24", "FY25", "LTM"]
CLIN = [0.08, 0.12, (438 + 466 + 481 + 496) / (365 + 389 + 419 + 435) - 1]
RA = [-0.02, -0.07, (275 + 221 + 252 + 255) / (275 + 252 + 271 + 272) - 1]
# Q3'26: Gb output growth "remained above 30%" (call); sequencing consumables +6%; implied revenue/Gb 1.06/1.30-1
PV = [("Gb volume (floor)", 0.30), ("Revenue per Gb", 1.06 / 1.30 - 1), ("Seq. consumables", 0.06)]

from pptx.chart.data import CategoryChartData  # noqa: E402
from pptx.enum.chart import XL_CHART_TYPE, XL_LABEL_POSITION, XL_LEGEND_POSITION, XL_TICK_LABEL_POSITION, XL_TICK_MARK  # noqa: E402


def section_head(s, x, w, y, label):
    text(s, x, y, w, 0.3, label, size=13, bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.BOTTOM,
         name=f"Header {label}")
    hline(s, x, y + 0.32, x + w, w=1.0)


def runs(tb_shape, parts, size=12, align=PP_ALIGN.LEFT, first=True):
    """parts: list of (text, bold) appended as one paragraph."""
    tf = tb_shape.text_frame
    p = tf.paragraphs[0] if first else tf.add_paragraph()
    p.alignment = align
    for t, b in parts:
        r = p.add_run()
        r.text = t
        r.font.name, r.font.size, r.font.bold = FONT, Pt(size), b
        r.font.color.rgb = rgb("000000")
    return p


def bullet(p):
    pPr = p._p.get_or_add_pPr()
    pPr.set("marL", str(Inches(0.2)))
    pPr.set("indent", str(-Inches(0.2)))
    bu = etree.SubElement(pPr, qn("a:buFont"))
    bu.set("typeface", "Wingdings")
    etree.SubElement(pPr, qn("a:buChar")).set("char", "§")


def chart_fonts(ch, size=10):
    ch.font.name, ch.font.size = FONT, Pt(size)
    ch.font.color.rgb = rgb("000000")


def quiet_axis(ax, fmt=None, visible=True):
    ax.has_major_gridlines = False
    ax.major_tick_mark = XL_TICK_MARK.NONE
    ax.format.line.color.rgb = rgb("808080")
    ax.tick_labels.font.name, ax.tick_labels.font.size = FONT, Pt(10)
    if fmt:
        ax.tick_labels.number_format, ax.tick_labels.number_format_is_linked = fmt, False
    ax.visible = visible


def sub_head(s, x, w, y, label):
    text(s, x, y, w, 0.26, label, size=11, bold=True, align=PP_ALIGN.CENTER, name=f"Subhead {label}")


def sub_head(s, x, w, y, label):
    text(s, x, y, w, 0.26, label, size=11, bold=True, align=PP_ALIGN.CENTER, name=f"Subhead {label}")


def company_overview():
    s = prs.slides.add_slide(L_CONTENT)
    set_title(s, "Company Overview", "Illumina, Inc. (NASDAQ: ILMN)")
    LX, LW, RX, RW = 0.20, 4.60, 5.17, 4.60

    # ---- top left: short description (bottom of quadrant left open) ----
    section_head(s, LX, LW, 1.22, "Company Description")
    tb = text(s, LX + 0.05, 1.64, LW - 0.1, 1.2, "", size=11, anchor=MSO_ANCHOR.TOP, name="Company Description Text")
    tb.text_frame.paragraphs[0].runs[0].text = ""
    items = [
        [("Illumina is the market leader in ", False), ("DNA sequencing", True),
         (": it sells the machines that read DNA (instruments)...", False)],
        [("...but makes most of its money selling the ", False), ("consumables", True),
         (" those instruments use, bought on a ", False), ("recurring basis", True),
         (" as each customer’s sequencing volume requires.", False)],
        [("Customers are ", False), ("clinical labs", True), (" (cancer, prenatal, genetic disease) and ", False),
         ("research", True), (" labs (academia, government, pharma).", False)],
    ]
    for k, parts in enumerate(items):
        p = runs(tb, parts, size=11, first=(k == 0))
        bullet(p)
        if k:
            p.space_before = Pt(4)

    # ---- top right: gigabase volume vs price (chart + plain takeaway) ----
    section_head(s, RX, RW, 1.22, "Gigabase Volume vs. Price")
    sub_head(s, RX, RW, 1.62, "Sequencing Consumables Growth Drivers, Q3'26 y/y")
    cd = CategoryChartData()
    cd.categories = [c for c, _ in PV]
    cd.add_series("Q3'26 y/y", [round(v, 3) for _, v in PV])
    gf = s.shapes.add_chart(XL_CHART_TYPE.BAR_CLUSTERED, Inches(RX + 0.05), Inches(1.88), Inches(RW - 0.1),
                            Inches(1.38), cd)
    gf.name = "Volume Price Chart"
    ch = gf.chart
    chart_fonts(ch, 11)
    ch.has_title = False
    ch.has_legend = False
    pl = ch.plots[0]
    pl.gap_width = 55
    ser = pl.series[0]
    ser.invert_if_negative = False
    for i, (_, v) in enumerate(PV):
        pt = ser.points[i]
        pt.format.fill.solid()
        pt.format.fill.fore_color.rgb = rgb(ORANGE if v > 0 else "7F7F7F")
    for dpt in ser._element.findall(qn("c:dPt")):
        inv = dpt.find(qn("c:invertIfNegative"))
        if inv is None:
            inv = etree.Element(qn("c:invertIfNegative"))
            dpt.find(qn("c:idx")).addnext(inv)
        inv.set("val", "0")
    ser.data_labels.show_value = True
    ser.data_labels.number_format, ser.data_labels.number_format_is_linked = '+0%;-0%', False
    ser.data_labels.position = XL_LABEL_POSITION.OUTSIDE_END
    ser.data_labels.font.name, ser.data_labels.font.size = FONT, Pt(11)
    ca = ch.category_axis
    quiet_axis(ca)
    ca.tick_labels.font.size = Pt(11)
    ca.reverse_order = True
    ca.tick_label_position = XL_TICK_LABEL_POSITION.LOW
    va = ch.value_axis
    va.minimum_scale, va.maximum_scale = -0.35, 0.45
    quiet_axis(va, visible=False)
    tk = box(s, RX + 0.1, 3.30, RW - 0.2, 0.62, line="404040", dash=True, name="Volume Price Takeaway")
    tk.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
    tk.text_frame.margin_top = tk.text_frame.margin_bottom = Inches(0.03)
    runs(tk, [("Customers sequenced 30%+ more gigabases, but revenue per Gb fell ~19%, so ", False),
              ("sequencing consumables grew only ~6%", True), (".", False)], size=11, align=PP_ALIGN.CENTER)

    # ---- bottom left: razor-blade model ----
    lt = MIX["LTM"]
    section_head(s, LX, LW, 4.03, "The Razor-Blade Model")
    b1 = box(s, LX + 0.05, 4.48, 1.55, 0.92, fill="D9D9D9", name="Razor Box", shape=MSO_SHAPE.ROUNDED_RECTANGLE)
    b1.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
    runs(b1, [("The razor: ", True), ("customers buy a sequencer once", False)], size=10.5, align=PP_ALIGN.CENTER)
    runs(b1, [("~%.0f%% of LTM rev." % (100 * lt[1] / LTM_TOTAL), True)], size=10.5, align=PP_ALIGN.CENTER,
         first=False)
    arr = s.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, Inches(LX + 1.66), Inches(4.79), Inches(0.36), Inches(0.30))
    arr.fill.solid()
    arr.fill.fore_color.rgb = rgb("808080")
    arr.line.fill.background()
    arr.shadow.inherit = False
    b2 = box(s, LX + 2.08, 4.48, 2.47, 0.92, fill=ORANGE, name="Blade Box", shape=MSO_SHAPE.ROUNDED_RECTANGLE)
    b2.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = runs(b2, [("The blades: ", True), ("new reagent kits on every run, bought again and again", False)],
             size=10.5, align=PP_ALIGN.CENTER)
    p2 = runs(b2, [("~%.0f%% of LTM revenue" % (100 * lt[0] / LTM_TOTAL), True)], size=14,
              align=PP_ALIGN.CENTER, first=False)
    for para in (p, p2):
        for r in para.runs:
            r.font.color.rgb = rgb("FFFFFF")
    cd = CategoryChartData()
    cd.categories = list(MIX)
    for k, name in enumerate(["Consumables", "Instruments", "Service & other"]):
        cd.add_series(name, [MIX[y][k] / sum(MIX[y]) for y in MIX])
    gf = s.shapes.add_chart(XL_CHART_TYPE.BAR_STACKED_100, Inches(LX), Inches(5.45), Inches(LW), Inches(1.12), cd)
    gf.name = "Revenue Mix Trend"
    ch = gf.chart
    chart_fonts(ch, 10)
    ch.has_title = False
    ch.has_legend = True
    ch.legend.position, ch.legend.include_in_layout = XL_LEGEND_POSITION.RIGHT, False
    ch.legend.font.name, ch.legend.font.size = FONT, Pt(9)
    pl = ch.plots[0]
    pl.gap_width, pl.overlap = 35, 100
    for ser, col, fc in zip(pl.series, [ORANGE, "7F7F7F", "BFBFBF"], ["000000", "FFFFFF", "000000"]):
        ser.format.fill.solid()
        ser.format.fill.fore_color.rgb = rgb(col)
        ser.format.line.color.rgb = rgb("FFFFFF")
        dl = ser.data_labels
        dl.show_value = True
        dl.number_format, dl.number_format_is_linked = '0%', False
        dl.position = XL_LABEL_POSITION.CENTER
        dl.font.name, dl.font.size = FONT, Pt(9)
        dl.font.color.rgb = rgb(fc)
    ca = ch.category_axis
    quiet_axis(ca)
    ca.reverse_order = True
    quiet_axis(ch.value_axis, visible=False)
    tk = text(s, LX, 6.55, LW, 0.32, "", size=11, align=PP_ALIGN.CENTER, name="Razor Takeaway")
    runs(tk, [("~$%.2f of consumables for every $1 of instruments" % (round(lt[0] / lt[1] * 2, 1) / 2), True),
              (" (LTM)", False)], size=11, align=PP_ALIGN.CENTER)

    # ---- bottom right: LTM revenue split + quarterly end-market growth ----
    section_head(s, RX, RW, 4.03, "Revenue Mix & End-Market Growth")
    DW = 1.75
    sub_head(s, RX, DW, 4.43, "LTM Revenue Mix")
    cd = CategoryChartData()
    cd.categories = ["Seq. consumables", "Instruments", "Other"]
    cd.add_series("LTM", [v / LTM_TOTAL for _, v in SPLIT])
    gf = s.shapes.add_chart(XL_CHART_TYPE.DOUGHNUT, Inches(RX), Inches(4.68), Inches(DW), Inches(2.22), cd)
    gf.name = "LTM Revenue Split"
    ch = gf.chart
    chart_fonts(ch, 9)
    ch.has_title = False
    ch.has_legend = True
    ch.legend.position, ch.legend.include_in_layout = XL_LEGEND_POSITION.BOTTOM, False
    ch.legend.font.name, ch.legend.font.size = FONT, Pt(9)
    pl = ch.plots[0]
    hole = pl._element.find(qn("c:holeSize"))
    if hole is None:
        hole = etree.SubElement(pl._element, qn("c:holeSize"))
    hole.set("val", "50")
    ser = pl.series[0]
    for i, col in enumerate([ORANGE, "7F7F7F", "A6A6A6"]):
        pt = ser.points[i]
        pt.format.fill.solid()
        pt.format.fill.fore_color.rgb = rgb(col)
        pt.format.line.color.rgb = rgb("FFFFFF")
    sdl = ser.data_labels
    sdl.show_value = True
    sdl.number_format, sdl.number_format_is_linked = '0%', False
    sdl.font.name, sdl.font.size, sdl.font.bold = FONT, Pt(9), True
    sdl.font.color.rgb = rgb("FFFFFF")

    GX, GW = RX + DW + 0.05, RW - DW - 0.05
    sub_head(s, GX, GW, 4.43, "Seq. Consumables Growth y/y, ex-China")
    cd = CategoryChartData()
    cd.categories = QTRS
    cd.add_series("Clinical", CLIN_Q)
    cd.add_series("Research & applied", RA_Q)
    gf = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(GX), Inches(4.68), Inches(GW), Inches(2.22), cd)
    gf.name = "Clinical vs Research Growth"
    ch = gf.chart
    chart_fonts(ch, 9)
    ch.has_title = False
    ch.has_legend = True
    ch.legend.position, ch.legend.include_in_layout = XL_LEGEND_POSITION.BOTTOM, False
    ch.legend.font.name, ch.legend.font.size = FONT, Pt(9)
    pl = ch.plots[0]
    pl.gap_width, pl.overlap = 50, 0
    for ser, col in zip(pl.series, [ORANGE, "7F7F7F"]):
        ser.invert_if_negative = False
        ser.format.fill.solid()
        ser.format.fill.fore_color.rgb = rgb(col)
        dl = ser.data_labels
        dl.show_value = True
        dl.number_format, dl.number_format_is_linked = '0%;(0%);0%', False
        dl.position = XL_LABEL_POSITION.OUTSIDE_END
        dl.font.name, dl.font.size = FONT, Pt(7.5)
    ca = ch.category_axis
    quiet_axis(ca)
    ca.tick_label_position = XL_TICK_LABEL_POSITION.LOW
    ca.tick_labels.font.size = Pt(8.5)
    va = ch.value_axis
    va.minimum_scale, va.maximum_scale = -0.16, 0.24
    quiet_axis(va, visible=False)

    text(s, 0.20, 6.97, 9.57, 0.25, "Sources: ILMN 10-K FY25, Q3'26 10-Q (LTM = Q4'25–Q3'26), Q3'25–Q3'26 earnings "
         "decks and Q3'26 call. Revenue per Gb is our calculation.", size=8, italic=True, color="595959",
         name="Sources")


# ---------------- alt-data template (blank, with the core-lab sample's university logos) ----------------
import os  # noqa: E402

LOGO_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "2026-11-09_core_lab_university_logos")
SAMPLE_LOGOS = ["MIT", "Harvard", "Cornell", "Penn", "Duke",
                "Northwestern", "UChicago", "Berkeley", "UCLA", "Dartmouth",
                "BU", "Minnesota", "Pitt", "Florida", "MichiganState",
                "UIUC", "TexasAM", "VirginiaTech", "Utah", "Iowa"]


def placeholder_box(s, x, y, w, h, label, name):
    b = box(s, x, y, w, h, fill="F7F7F7", line=LIGHT_GREY, dash=True, name=name)
    b.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = runs(b, [(label, False)], size=12, align=PP_ALIGN.CENTER)
    p.runs[0].font.italic = True
    p.runs[0].font.color.rgb = rgb("7F7F7F")


def core_lab_price_data():
    """Like-for-like internal 10B 100-cycle price index and price cuts by month, from the int-vs-ext workbook."""
    import math
    import openpyxl
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "datasets",
                        "2026-10-31_core_lab_X10B_100c_int_vs_ext.xlsx")
    rows = list(openpyxl.load_workbook(path, data_only=True).active.iter_rows(values_only=True))
    hdr = rows[4]
    data = [r for r in rows[5:] if r[0] and str(r[0])[:2] == "20"]
    months = [str(r[0]) for r in data]
    series = {hdr[j]: [r[j] for r in data] for j in range(6, len(hdr)) if hdr[j]}
    idx = [100.0]
    for t in range(1, len(months)):
        ch = [math.log(series[k][t] / series[k][t - 1]) for k in series
              if k.startswith("Int") and series[k][t] and series[k][t - 1]]
        idx.append(idx[-1] * math.exp(sum(ch) / len(ch)) if ch else idx[-1])
    cuts = [0] * len(months)  # internal + external rate cards; moves under 1% are rounding / FX
    for v in series.values():
        for t in range(1, len(months)):
            if v[t] and v[t - 1] and v[t] / v[t - 1] - 1 < -0.01:
                cuts[t] += 1
    return months, idx, months.index("2026-06"), cuts


def price_build(s, x, y, w, h):
    """Top-right quadrant: like-for-like index with each month's price cuts marked on the line."""
    from pptx.chart.data import CategoryChartData
    from pptx.enum.chart import XL_CHART_TYPE, XL_LABEL_POSITION, XL_MARKER_STYLE, XL_TICK_LABEL_POSITION, XL_TICK_MARK
    from pptx.oxml import parse_xml
    from pptx.oxml.ns import nsdecls
    months, idx, split, cuts = core_lab_price_data()
    n = len(months)
    pace_b = (idx[split] / idx[0]) ** (12 / split) - 1
    pace_a = (idx[-1] / idx[split]) ** (12 / (n - 1 - split)) - 1
    before, after = sum(cuts[:split + 1]), sum(cuts[split + 1:])

    text(s, x, y, w, 0.24, "Like-for-like price index (Oct-24 = 100) and price cuts", size=10, bold=True,
         align=PP_ALIGN.CENTER)
    cy, chh = y + 0.24, h - 0.46
    MON = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    cd = CategoryChartData()
    cd.categories = [f"{MON[int(m[5:7]) - 1]}-{m[2:4]}" for m in months]
    cd.add_series("Index", [round(v, 2) for v in idx])
    gf = s.shapes.add_chart(XL_CHART_TYPE.LINE_MARKERS, Inches(x), Inches(cy), Inches(w), Inches(chh), cd)
    gf.name = "Price Index and Cuts"
    ch = gf.chart
    ch.has_title, ch.has_legend = False, False
    ch.font.name, ch.font.size = FONT, Pt(9)
    ser = ch.plots[0].series[0]
    ser.smooth = False
    ser.format.line.color.rgb = rgb(ORANGE)
    ser.format.line.width = Pt(2.25)
    ser.marker.style = XL_MARKER_STYLE.NONE
    for t, k in enumerate(cuts):  # a dot on each month with a cut, labelled with how many
        if not k:
            continue
        pt = ser.points[t]
        pt.marker.style = XL_MARKER_STYLE.CIRCLE
        pt.marker.size = 5 + 2 * k
        pt.marker.format.fill.solid()
        pt.marker.format.fill.fore_color.rgb = rgb("404040")
        pt.marker.format.line.color.rgb = rgb("FFFFFF")
        dl = pt.data_label
        dl.position = XL_LABEL_POSITION.BELOW
        r = dl.text_frame.paragraphs[0].add_run()
        r.text = str(k)
        r.font.name, r.font.size, r.font.bold = FONT, Pt(9), True
    ca, va = ch.category_axis, ch.value_axis
    for ax in (ca, va):
        ax.has_major_gridlines = False
        ax.major_tick_mark = XL_TICK_MARK.NONE
        ax.format.line.color.rgb = rgb("808080")
        ax.tick_labels.font.name, ax.tick_labels.font.size = FONT, Pt(9)
    ca.tick_label_position = XL_TICK_LABEL_POSITION.LOW
    for tag in ("c:tickLblSkip", "c:tickMarkSkip"):
        ca._element.append(parse_xml(f'<{tag} {nsdecls("c")} val="6"/>'))
    va.minimum_scale, va.maximum_scale, va.major_unit = 90, 105, 5
    cb = va._element.find(qn("c:crossBetween"))
    if cb is None:
        cb = parse_xml(f'<c:crossBetween {nsdecls("c")} val="midCat"/>')
        anchor = va._element.find(qn("c:crosses"))
        if anchor is None:
            anchor = va._element.find(qn("c:crossesAt"))
        anchor.addnext(cb)
    cb.set("val", "midCat")
    PX, PY, PW, PH = 0.07, 0.03, 0.90, 0.80
    pa = ch._chartSpace.find(qn("c:chart")).find(qn("c:plotArea"))
    for old in pa.findall(qn("c:layout")):
        pa.remove(old)
    pa.insert(0, parse_xml(
        f'<c:layout {nsdecls("c")}><c:manualLayout><c:layoutTarget val="inner"/><c:xMode val="edge"/>'
        f'<c:yMode val="edge"/><c:x val="{PX}"/><c:y val="{PY}"/><c:w val="{PW}"/><c:h val="{PH}"/>'
        '</c:manualLayout></c:layout>'))
    xs = x + w * (PX + PW * split / (n - 1))
    top, bot = cy + chh * PY, cy + chh * (PY + PH)
    ln = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(xs), Inches(top), Inches(xs), Inches(bot))
    ln.line.color.rgb = rgb("7F7F7F")
    ln.line.width = Pt(0.75)
    ln.line.dash_style = MSO_LINE_DASH_STYLE.DASH
    ln.name = "Jun-26 Divider"
    y_at = lambda v: top + (bot - top) * (105 - v) / 15  # noqa: E731
    text(s, x + w * 0.10, y_at(93.0), 2.4, 0.22, f"Nov-24 to Jun-26: {pace_b:.0%}/yr, {before} cuts", size=9,
         italic=True, name="Pace Before")
    pa_tb = text(s, xs + 0.03, y_at(104.5), x + w - xs - 0.03, 0.4, f"Jul–Oct-26:", size=9, italic=True,
                 anchor=MSO_ANCHOR.TOP, name="Pace After")
    runs(pa_tb, [(f"{pace_a:.0%}/yr, {after} cuts", False)], size=9, first=False).runs[0].font.italic = True
    text(s, x, y + h - 0.22, w, 0.2, "Dots mark months with price cuts across 41 rate cards; number = cuts that month",
         size=8, italic=True, color="595959", align=PP_ALIGN.CENTER, name="Dot Key")


def alt_data_template():
    from PIL import Image
    s = prs.slides.add_slide(L_CONTENT)
    set_title(s, "[Slide Title]", "[Subtitle]")
    LX, LW, RX, RW = 0.20, 4.60, 5.17, 4.60

    # top left: methodology steps
    section_head(s, LX, LW, 1.22, "Methodology")
    for i in range(5):
        tb = text(s, LX + 0.1, 1.66 + i * 0.44, LW - 0.15, 0.4, "", size=12, anchor=MSO_ANCHOR.TOP,
                  name=f"Method Step {i + 1}")
        runs(tb, [(f"[ {i + 1} ] ", True), ("[Describe step]", False)], size=12)

    # top right: chart placeholder
    section_head(s, RX, RW, 1.22, "Core-Lab Price Build")
    price_build(s, RX + 0.05, 1.64, RW - 0.1, 2.30)

    # bottom left: sample portfolio box with university logos
    BX, BY, BW, BH = LX + 0.05, 4.22, LW - 0.1, 2.62
    frame = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(BX), Inches(BY), Inches(BW), Inches(BH))
    frame.name = "Portfolio Frame"
    frame.adjustments[0] = 0.06
    frame.fill.background()
    frame.line.color.rgb = rgb("000000")
    frame.line.width = Pt(2)
    frame.shadow.inherit = False
    lab = text(s, BX + 0.85, BY - 0.19, BW - 1.7, 0.36, "Core-Lab Sample Portfolio", size=14, bold=True,
               align=PP_ALIGN.CENTER, name="Portfolio Title")
    lab.fill.solid()
    lab.fill.fore_color.rgb = rgb("FFFFFF")
    cols, rows = 5, 4
    cw, ch_ = (BW - 0.3) / cols, (BH - 0.4) / rows
    for k, key in enumerate(SAMPLE_LOGOS):
        path = os.path.join(LOGO_DIR, key + ".png")
        iw, ih = Image.open(path).size
        mw, mh = cw - 0.08, ch_ - 0.14
        sc = min(mw / iw, mh / ih, (0.20 / (iw * ih)) ** 0.5)  # equal visual weight, capped by the cell
        w, h = iw * sc, ih * sc
        cx = BX + 0.15 + (k % cols) * cw + (cw - w) / 2
        cy = BY + 0.25 + (k // cols) * ch_ + (ch_ - h) / 2
        pic = s.shapes.add_picture(path, Inches(cx), Inches(cy), Inches(w), Inches(h))
        pic.name = f"Logo {key}"

    # bottom right: estimate chart + takeaway
    section_head(s, RX, RW, 4.03, "[Sell-Side vs. Our Estimate]")
    placeholder_box(s, RX + 0.05, 4.48, 2.45, 2.38, "[Insert chart]", "Chart Placeholder Bottom")
    call = box(s, RX + 2.62, 4.50, RW - 2.67, 0.85, line="404040", name="Takeaway Box")
    call.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
    runs(call, [("[Key takeaway]", False)], size=12, align=PP_ALIGN.CENTER)
    ev = text(s, RX + 2.62, 5.45, RW - 2.67, 1.4, "", size=11, anchor=MSO_ANCHOR.TOP, name="Supporting Evidence")
    runs(ev, [("[Supporting evidence]:", False)], size=11)
    for _ in range(3):
        bullet(runs(ev, [("[Data point]", False)], size=11, first=False))

    text(s, 0.20, 6.97, 9.57, 0.25, "[1] [Footnote / sources]", size=8, italic=True, color="595959",
         name="Footnote")


toc_slide(0)
exec_summary()
for i in range(1, len(SECTIONS)):
    toc_slide(i)
    if i == 2:
        company_overview()
    if i == 4:
        variance_1()
    if i == 5:
        alt_data_template()
        variance_2()

prs.save(OUT)
print("saved", OUT, len(prs.slides), "slides")
