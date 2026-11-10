"""Element VITARI vs NovaSeq X Plus (instrument price, consumables per run, cost per Gb) as one grouped graphic of
editable PowerPoint shapes, sized for the top-right corner of the user's slide 11 (under "Yet Industry Pxing Dynamics Are
Worsening", left of the instrument photo). Bars are indexed to X Plus = 100. Built from shapes rather than a native chart
because chart data labels wrap and collide at this size.
Source: UBS Fast Take, 19 Feb 2026 (company claims); X Plus instrument implied from "~40% below"; $/Gb = consumables per run / output per run.
Usage: python build.py <out.pptx>
"""
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor

OUT = sys.argv[1]
FONT = "Times New Roman"
ORANGE, GREY, BLACK = RGBColor(0xE8, 0x96, 0x2E), RGBColor(0xBF, 0xBF, 0xBF), RGBColor(0, 0, 0)

ROWS = [  # label, X Plus value, VITARI value, X Plus label, VITARI label
    ("Instrument", 1150, 689, "$1.15M", "$689K (−40%)"),
    ("Consumables / run", 32, 3, "$32K", "$3K (−91%)"),
    ("Cost / Gb", 2.00, 1.00, "$2.00", "$1.00 (−50%)"),
]

X0, Y0, W = 9.62, 1.14, 2.23       # graphic origin and width (in)
LBL_W = 0.88                         # category label column
AX = X0 + LBL_W + 0.05               # axis x
BAR_MAX = 0.60                       # X Plus bar length
BAR_H, BAR_GAP, ROW_H = 0.12, 0.02, 0.43
TOP = Y0 + 0.24                      # first row top (below legend)

prs = Presentation()
prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
slide = prs.slides.add_slide(prs.slide_layouts[6])
grp = slide.shapes.add_group_shape()
grp.name = "VITARI vs X Plus specs"
S = grp.shapes


def rect(x, y, w, h, col):
    s = S.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    s.fill.solid(); s.fill.fore_color.rgb = col; s.line.fill.background(); s.shadow.inherit = False
    return s


def text(x, y, w, h, t, size, bold=False, align=PP_ALIGN.LEFT):
    tb = S.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame; tf.word_wrap = False; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    p = tf.paragraphs[0]; p.alignment = align
    r = p.add_run(); r.text = t
    r.font.name = FONT; r.font.size = Pt(size); r.font.bold = bold; r.font.color.rgb = BLACK
    return tb


# Legend
lx = X0 + 0.22
for name, col in (("NovaSeq X Plus", GREY), ("Element VITARI", ORANGE)):
    rect(lx, Y0 + 0.045, 0.08, 0.08, col)
    text(lx + 0.11, Y0, 0.85, 0.17, name, 7.5)
    lx += 0.98

# Rows
for i, (lab, xv, vv, xl, vl) in enumerate(ROWS):
    y = TOP + i * ROW_H
    mid = y + BAR_H + BAR_GAP / 2
    text(X0, mid - 0.09, LBL_W, 0.18, lab, 7.5, bold=True, align=PP_ALIGN.RIGHT)
    rect(AX, y, BAR_MAX, BAR_H, GREY)
    text(AX + BAR_MAX + 0.04, y - 0.015, 0.7, BAR_H + 0.03, xl, 7.5)
    vlen = BAR_MAX * vv / xv
    rect(AX, y + BAR_H + BAR_GAP, vlen, BAR_H, ORANGE)
    text(AX + vlen + 0.04, y + BAR_H + BAR_GAP - 0.015, 0.8, BAR_H + 0.03, vl, 7.5, bold=True)

# Axis line
ax = S.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(AX), Inches(TOP - 0.05), Inches(AX), Inches(TOP + 2 * ROW_H + 2 * BAR_H + BAR_GAP + 0.05))
ax.line.color.rgb = BLACK; ax.line.width = Pt(0.75)

prs.save(OUT)
print("saved", OUT, "bottom at", round(TOP + 2 * ROW_H + 2 * BAR_H + BAR_GAP + 0.05, 2), "in")
