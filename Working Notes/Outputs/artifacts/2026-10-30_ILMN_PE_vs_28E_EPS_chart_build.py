"""Rebuild the ILMN 26E P/E vs 28E EPS chart as a native PowerPoint chart, extended to 30 Oct 2026.

Inputs
- P/E: Capital IQ export 'Charts (7).xls' (NasdaqGS:ILMN Fwd P/E Est. CY+1, 30 Oct 2025 - 30 Oct 2026).
- The original chart (image) runs on a calendar axis from 13 Oct 2025 to 12 Oct 2026. The 13-29 Oct 2025 P/E points are
  not in the export, so they are read off the original image.
- 28E EPS is not in the export either: it is read off the original image (anchored to its $6.22 / $6.68 / $6.89 / $7.06
  labels) and held flat at $7.06 after 12 Oct 2026 (no revisions assumed).
Geometry: 1 px of the original 998x602 image = 1/96 inch. Data-anchored annotations keep their original y and have their
x rescaled from the old 364-day axis to the new 382-day axis; the legend keeps its place. The original's text callout box is omitted.
Usage: python build.py <Charts.xls> <original_chart.png> <out.pptx>
"""
import sys, copy, datetime
import xlrd
from PIL import Image
from lxml import etree
from pptx import Presentation
from pptx.util import Emu, Pt
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.dml import MSO_LINE_DASH_STYLE
from pptx.dml.color import RGBColor
from pptx.oxml.ns import qn

XLS, PNG, OUT = sys.argv[1:4]
FONT = "Garamond"
ORANGE, YELLOW, GREY_FILL, BROWN, RED, BOX_GREY = "E8962E", "F3C64B", "EFF1F2", "623C0D", "FF0000", "666666"
AX, LBL, BIG, REV, CALL = 13.5, 13.5, 17.5, 21.5, 17          # font sizes (pt)
LINE_W = 3.5                                                    # series line width (pt)
PX = 914400 / 96
px = lambda v: Emu(int(round(v * PX)))
D = datetime.date

# ---- axes geometry ------------------------------------------------------------------------------------
X0, X1, YT, YB = 56, 930, 26.5, 558.5                            # inner plot rectangle in original pixels
A0, OLD_END = D(2025, 10, 13), D(2026, 10, 12)
orig_x = lambda day: X0 + (day - A0).days / (OLD_END - A0).days * (X1 - X0)
y_pe = lambda v: YT + (55 - v) / 35 * (YB - YT)
y_eps = lambda v: YT + (9 - v) / 3 * (YB - YT)

# ---- data ---------------------------------------------------------------------------------------------
sh = xlrd.open_workbook(XLS).sheet_by_index(1)
x_dates = [xlrd.xldate_as_datetime(sh.cell_value(r, 0), 0).date() for r in range(1, sh.nrows)]
x_pe = [sh.cell_value(r, 1) for r in range(1, sh.nrows)]
NEW_END = x_dates[-1]
new_x = lambda day: X0 + (day - A0).days / (NEW_END - A0).days * (X1 - X0)
T = lambda x: X0 + (x - X0) * (OLD_END - A0).days / (NEW_END - A0).days   # old pixel x -> new pixel x

img = Image.open(PNG).convert("RGB"); pix = img.load()
def trace(x, rgb, tol=40):
    ys = sorted(y for y in range(40, img.size[1]) if sum(abs(a - b) for a, b in zip(pix[int(round(x)), y], rgb)) < tol)
    return ys
pre = [A0 + datetime.timedelta(days=k) for k in range((x_dates[0] - A0).days)]
pre = [d for d in pre if d.weekday() < 5]
pre_pe = []
for d in pre:
    ys = trace(orig_x(d), (232, 150, 46))
    pre_pe.append(round(55 - ((ys[0] + ys[-1]) / 2 - YT) / (YB - YT) * 35, 2))
dates, pe = pre + x_dates, pre_pe + x_pe

def eps_px(d):
    ys = trace(orig_x(d), (243, 198, 75))
    return 7.06 - (ys[len(ys) // 2] - 374) / 175.0               # calibrated on the $7.06 (y=374) and $6.22 (y=521) labels
raw = [round(eps_px(d), 2) for d in dates if d <= OLD_END]
eps, cur = [], raw[0]
for i, v in enumerate(raw):                                     # keep a level only if it holds 3+ days (drops anti-aliased ramps)
    if sum(1 for k in range(i, min(i + 3, len(raw))) if abs(raw[k] - v) <= 0.015) >= 3 or abs(v - 6.68) < 0.02:
        cur = v
    eps.append(cur)
eps = [next((s for s in (6.22, 6.68, 6.89, 7.06) if abs(e - s) <= 0.025), e) for e in eps]
eps += [7.06] * (len(dates) - len(eps))

# ---- slide --------------------------------------------------------------------------------------------
prs = Presentation()
prs.slide_width, prs.slide_height = px(998), px(602)
slide = prs.slides.add_slide(prs.slide_layouts[6])

def rect(x0, y0, x1, y1, fill=None, line=None, dash=None, width=1.25, name=None):
    s = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, px(x0), px(y0), px(x1 - x0), px(y1 - y0))
    if fill: s.fill.solid(); s.fill.fore_color.rgb = RGBColor.from_string(fill)
    else: s.fill.background()
    if line:
        s.line.color.rgb = RGBColor.from_string(line); s.line.width = Pt(width)
        if dash: s.line.dash_style = dash
    else: s.line.fill.background()
    s.shadow.inherit = False
    if name: s.name = name
    return s

def line(x0, y0, x1, y1, color="000000", width=0.75, dash=None, name=None):
    c = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, px(x0), px(y0), px(x1), px(y1))
    c.line.color.rgb = RGBColor.from_string(color); c.line.width = Pt(width)
    if dash: c.line.dash_style = dash
    if name: c.name = name
    return c

def text(cx, cy, w, h, paras, align=PP_ALIGN.CENTER, name=None):
    """Text box centred on (cx, cy). paras: list of paragraphs, each a list of (text, fmt)."""
    tb = slide.shapes.add_textbox(px(cx - w / 2), px(cy - h / 2), px(w), px(h))
    tf = tb.text_frame; tf.word_wrap = False; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    if isinstance(paras, str): paras = [[(paras, {})]]
    for i, para in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        for t, f in para:
            r = p.add_run(); r.text = t
            r.font.name = FONT; r.font.size = Pt(f.get("size", LBL))
            r.font.bold = f.get("bold", False); r.font.underline = f.get("underline", False)
            r.font.color.rgb = RGBColor.from_string(f.get("color", "000000"))
    if name: tb.name = name
    return tb

# Highlight boxes sit behind the chart so the lines draw over them.
CRASH_X0 = new_x(D(2026, 10, 28)) - 3
rect(T(807), 25, CRASH_X0, 395, fill=GREY_FILL, line=BROWN, dash=MSO_LINE_DASH_STYLE.DASH, name="Rerating highlight")
rect(CRASH_X0, 25, 937, 395, fill="FFE1E1", line=RED, dash=MSO_LINE_DASH_STYLE.DASH, width=1.5, name="Crash highlight")

# ---- native chart -------------------------------------------------------------------------------------
cd = CategoryChartData(number_format="mmm-yy")
cd.categories = dates
cd.add_series("26E P/E", pe)
cd.add_series("28E EPS", eps)
gf = slide.shapes.add_chart(XL_CHART_TYPE.LINE, 0, 0, px(998), px(602), cd)
gf.name = "ILMN P/E vs 28E EPS chart"
cs = gf.chart._chartSpace
C = lambda tag: qn("c:" + tag)
A = lambda tag: qn("a:" + tag)

def el(parent, tag, **attrs):
    e = etree.SubElement(parent, tag)
    for k, v in attrs.items(): e.set(k, str(v))
    return e

def txpr(size, bold=False, color="000000"):
    t = etree.Element(C("txPr"))
    el(t, A("bodyPr")); el(t, A("lstStyle"))
    p = el(t, A("p")); ppr = el(p, A("pPr"))
    d = el(ppr, A("defRPr"), sz=int(size * 100), b=1 if bold else 0)
    sf = el(d, A("solidFill")); el(sf, A("srgbClr"), val=color)
    el(d, A("latin"), typeface=FONT); el(d, A("cs"), typeface=FONT)
    el(p, A("endParaRPr"), lang="en-US")
    return t

def sppr_line(color=None, width_pt=None):
    sp = etree.Element(C("spPr")); ln = el(sp, A("ln"))
    if color is None: el(ln, A("noFill"))
    else:
        ln.set("w", str(int(width_pt * 12700)))
        sf = el(ln, A("solidFill")); el(sf, A("srgbClr"), val=color)
    return sp

plot = cs.find(".//" + C("plotArea"))
lc = plot.find(C("lineChart"))
sers = lc.findall(C("ser"))
cat_ax, val_ax = plot.find(C("dateAx")), plot.find(C("valAx"))

for ser, color in zip(sers, (ORANGE, YELLOW)):
    for tag in ("spPr", "marker", "smooth"):
        for e in ser.findall(C(tag)): ser.remove(e)
    sp = etree.Element(C("spPr")); ln = el(sp, A("ln"), w=int(LINE_W * 12700), cap="rnd")
    sf = el(ln, A("solidFill")); el(sf, A("srgbClr"), val=color); el(ln, A("round"))
    ser.find(C("tx")).addnext(sp)
    mk = etree.Element(C("marker")); el(mk, C("symbol"), val="none"); sp.addnext(mk)
    el(ser, C("smooth"), val="0")

# EPS series -> its own lineChart on secondary axes
lc2 = copy.deepcopy(lc)
lc2.remove([s for s in lc2.findall(C("ser")) if s.find(C("idx")).get("val") == "0"][0])
lc.remove(sers[1])
for ax in lc2.findall(C("axId")): lc2.remove(ax)
el(lc2, C("axId"), val="3001"); el(lc2, C("axId"), val="3002")
lc.addnext(lc2)

serial = lambda d: (d - D(1899, 12, 30)).days

def chain(anchor, elems):
    for e in elems: anchor.addnext(e); anchor = e
    return anchor

def style_date_ax(ax, cross_id, hidden=False):
    for tag in ("numFmt", "majorTickMark", "minorTickMark", "tickLblPos", "spPr", "txPr", "baseTimeUnit", "majorUnit",
                "majorTimeUnit", "minorUnit", "minorTimeUnit", "crosses", "crossesAt", "auto", "lblOffset", "noMultiLvlLbl"):
        for e in ax.findall(C(tag)): ax.remove(e)
    sc = ax.find(C("scaling")); [sc.remove(e) for e in list(sc) if e.tag != C("orientation")]
    el(sc, C("max"), val=serial(NEW_END)); el(sc, C("min"), val=serial(A0))
    ax.find(C("delete")).set("val", "1" if hidden else "0")
    ax.find(C("crossAx")).set("val", cross_id)
    chain(ax.find(C("axPos")), [etree.Element(C("numFmt"), formatCode="mmm-yy", sourceLinked="0"),
                                etree.Element(C("majorTickMark"), val="none"), etree.Element(C("minorTickMark"), val="none"),
                                etree.Element(C("tickLblPos"), val="nextTo"),
                                sppr_line() if hidden else sppr_line("000000", 0.75), txpr(AX)])
    chain(ax.find(C("crossAx")), [etree.Element(C("crosses"), val="autoZero"), etree.Element(C("auto"), val="0"),
                                  etree.Element(C("lblOffset"), val="100"), etree.Element(C("baseTimeUnit"), val="days"),
                                  etree.Element(C("majorUnit"), val="2"), etree.Element(C("majorTimeUnit"), val="months")])

def style_val_ax(ax, lo, hi, step, fmt, pos, cross_id, crosses):
    for tag in ("majorGridlines", "numFmt", "majorTickMark", "minorTickMark", "tickLblPos", "spPr", "txPr", "crosses",
                "crossesAt", "majorUnit", "crossBetween"):
        for e in ax.findall(C(tag)): ax.remove(e)
    sc = ax.find(C("scaling")); [sc.remove(e) for e in list(sc) if e.tag != C("orientation")]
    el(sc, C("max"), val=hi); el(sc, C("min"), val=lo)
    ax.find(C("delete")).set("val", "0"); ax.find(C("axPos")).set("val", pos)
    ax.find(C("crossAx")).set("val", cross_id)
    chain(ax.find(C("axPos")), [etree.Element(C("numFmt"), formatCode=fmt, sourceLinked="0"),
                                etree.Element(C("majorTickMark"), val="none"), etree.Element(C("minorTickMark"), val="none"),
                                etree.Element(C("tickLblPos"), val="nextTo"), sppr_line(), txpr(AX, bold=True)])
    chain(ax.find(C("crossAx")), [etree.Element(C("crosses"), val=crosses), etree.Element(C("crossBetween"), val="midCat"),
                                  etree.Element(C("majorUnit"), val=str(step))])

cat_id, val_id = cat_ax.find(C("axId")).get("val"), val_ax.find(C("axId")).get("val")
cat2, val2 = copy.deepcopy(cat_ax), copy.deepcopy(val_ax)
cat2.find(C("axId")).set("val", "3001"); val2.find(C("axId")).set("val", "3002")
plot.append(cat2); plot.append(val2)
style_date_ax(cat_ax, val_id)
style_val_ax(val_ax, 20, 55, 5, '0"x"', "l", cat_id, "autoZero")
style_date_ax(cat2, "3002", hidden=True)
style_val_ax(val2, 6, 9, 0.5, '"$"0.00', "r", "3001", "max")

layout = plot.find(C("layout"))
if layout is None: layout = etree.Element(C("layout")); plot.insert(0, layout)
layout.clear()
ml = el(layout, C("manualLayout"))
for tag, val in (("layoutTarget", "inner"), ("xMode", "edge"), ("yMode", "edge"), ("x", X0 / 998), ("y", YT / 602),
                 ("w", (X1 - X0) / 998), ("h", (YB - YT) / 602)):
    el(ml, C(tag), val=val)
for e in plot.findall(C("spPr")): plot.remove(e)
psp = el(plot, C("spPr")); el(psp, A("noFill")); el(el(psp, A("ln")), A("noFill"))

gf.chart.has_legend = True
leg = cs.find(".//" + C("legend"))
for e in list(leg): leg.remove(e)
el(leg, C("legendPos"), val="t")
lml = el(el(leg, C("layout")), C("manualLayout"))
for tag, val in (("xMode", "edge"), ("yMode", "edge"), ("x", 372 / 998), ("y", 6 / 602), ("w", 258 / 998), ("h", 26 / 602)):
    el(lml, C(tag), val=val)
el(leg, C("overlay"), val="1")
leg.append(txpr(AX))

gf.chart.has_title = False
ch = cs.find(C("chart"))
for tag in ("spPr", "txPr"):
    for e in cs.findall(C(tag)): cs.remove(e)
csp = etree.Element(C("spPr")); el(csp, A("noFill")); el(el(csp, A("ln")), A("noFill"))
ch.addnext(csp); csp.addnext(txpr(AX))
pv = ch.find(C("plotVisOnly"))
if pv is not None: pv.set("val", "1")

# ---- annotations --------------------------------------------------------------------------------------
# Data labels: original glyph-box centres (x rescaled, y kept)
for cx, cy, t in [(299.5, 344.5, "32.6x"), (349.5, 547.5, "22.3x"), (350, 415.5, "$6.68"), (211, 543.5, "$6.22"),
                  (615.5, 342.5, "32.7x"), (649, 425.5, "$6.89"), (751.5, 244.5, "39.2x")]:
    text(T(cx), cy, 60, 22, t)

# 51.6x: the original chart's end point (12 Oct), bold with leader
text(T(846), 59, 66, 26, [[("51.6x", {"bold": True, "size": BIG})]])
line(T(878), 59, new_x(OLD_END) - 1, y_pe(pe[dates.index(OLD_END)]) - 2)
# $7.06: bold with leader to the (extended) end of the EPS line
text(T(876), 347, 66, 26, [[("$7.06", {"bold": True, "size": BIG})]])
line(T(908), 346, X1 - 1, y_eps(7.06) - 2)

# New: today's crash
pre_v, post_v = pe[-2], pe[-1]
drop = post_v / pre_v - 1
text(889, y_pe(post_v), 54, 24, [[(f"{post_v:.1f}x", {"bold": True, "size": BIG, "color": RED})]], name="Crash label")
line(917, y_pe(post_v), X1 - 1, y_pe(post_v), color=RED, width=0.75)
note = f"−{abs(drop):.0%} on 30-Oct"
text(876, y_pe(post_v) + 40, 86, 40, [[(note, {"bold": True, "size": 12, "color": RED})],
                                      [("(Q3'26 print)", {"size": 12, "color": RED})]], align=PP_ALIGN.RIGHT, name="Crash note")

# 12% 28E EPS revision bracket (red dashed)
DASH = MSO_LINE_DASH_STYLE.DASH
line(T(304), 533.5, T(735), 533.5, color=RED, dash=DASH)
line(T(723), 424, T(735), 424, color=RED, dash=DASH)
br = slide.shapes.add_shape(MSO_SHAPE.RIGHT_BRACE, px(T(735)), px(424), px(T(756) - T(735)), px(533.5 - 424))
br.fill.background(); br.line.color.rgb = RGBColor.from_string(RED); br.line.width = Pt(0.75)
br.line.dash_style = DASH; br.shadow.inherit = False
line(T(756), 478.5, T(783), 478.5, color=RED, dash=DASH)
rv = slide.shapes.add_textbox(px(T(786)), px(440), px(170), px(72))
rtf = rv.text_frame; rtf.word_wrap = False; rtf.vertical_anchor = MSO_ANCHOR.MIDDLE
rtf.margin_left = rtf.margin_right = rtf.margin_top = rtf.margin_bottom = 0
for i, runs in enumerate(((("12%", True), (" 28E", False)), (("EPS Revision", False),))):
    pp = rtf.paragraphs[0] if i == 0 else rtf.add_paragraph()
    pp.line_spacing = 0.9
    for t, bold in runs:
        r = pp.add_run(); r.text = t; r.font.name = FONT; r.font.size = Pt(REV); r.font.bold = bold
        r.font.color.rgb = RGBColor.from_string(RED)

# Dotted leader off the bottom-right of the highlight box (as in the original)
line(938, 396, 998, 534, color="898989", width=0.75, dash=MSO_LINE_DASH_STYLE.ROUND_DOT)

prs.save(OUT)
if len(sys.argv) > 4:                                           # optional: write the plotted series to CSV
    import csv
    with open(sys.argv[4], "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["date", "pe_26e_capiq_fwd_cy1", "eps_28e", "pe_source", "eps_source"])
        for d, a, b in zip(dates, pe, eps):
            w.writerow([d.isoformat(), round(a, 4), b, "image" if d < x_dates[0] else "CapIQ export",
                        "image" if d <= OLD_END else "held flat (no revisions)"])
print(f"saved {OUT} | {len(pre)} pre-export points read from image | P/E {pre_v:.2f} -> {post_v:.2f} ({drop:.1%})")
print("EPS levels:", sorted(set(eps)))
