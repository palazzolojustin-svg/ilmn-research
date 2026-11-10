"""Roche AXELIOS 1 vs NovaSeq X Plus (instrument price, cost per Gb) as one grouped graphic of editable PowerPoint shapes,
matching the user's edited VITARI graphic: two rows, bold challenger value with the % gap in red, same size and position
(top-right corner of slide 11). Bars are indexed to X Plus = 100.
Sources: AXELIOS ~$750K instrument (Reuters 29 Jun 2026; Seeking Alpha Sep 2026; PacBio expert Aug 2026); $150 per genome
list (Roche, Feb and May 2026), excluding library prep and assuming the sensor module is reused 20 times. X Plus $1.15M and
$2.00/Gb as in the VITARI graphic (UBS, Feb 2026); $2.00/Gb matches Illumina's ~$200 genome list (JPM, Mar 2026) at
~100 Gb per 30X genome, the same basis that puts AXELIOS at $1.50.
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
ORANGE, GREY, BLACK, RED = (RGBColor(0xE8, 0x96, 0x2E), RGBColor(0xBF, 0xBF, 0xBF), RGBColor(0, 0, 0),
                            RGBColor(0xFF, 0x00, 0x00))

ROWS = [  # label, X Plus value, AXELIOS value, X Plus label, AXELIOS value label, AXELIOS gap label
    ("Instrument", 1150, 750, "$1.15M", "$750K", "(−35%)"),
    ("Cost / Gb", 2.00, 1.50, "$2.00", "$1.50", "(−25%)"),
]

X0, Y0 = 9.62, 1.14                  # graphic origin (in)
LBL_W = 0.88                         # category label column
AX = X0 + LBL_W + 0.05               # axis x
BAR_MAX = 0.60                       # X Plus bar length
BAR_H, BAR_GAP, ROW_H = 0.12, 0.02, 0.43
TOP = Y0 + 0.24                      # first row top (below legend)

prs = Presentation()
prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
slide = prs.slides.add_slide(prs.slide_layouts[6])
grp = slide.shapes.add_group_shape()
grp.name = "AXELIOS vs X Plus specs"
S = grp.shapes


def rect(x, y, w, h, col):
    s = S.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    s.fill.solid(); s.fill.fore_color.rgb = col; s.line.fill.background(); s.shadow.inherit = False
    return s


def text(x, y, w, h, runs, size, align=PP_ALIGN.LEFT):
    """runs: list of (text, bold, colour)."""
    tb = S.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame; tf.word_wrap = False; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    p = tf.paragraphs[0]; p.alignment = align
    for t, bold, col in runs:
        r = p.add_run(); r.text = t
        r.font.name = FONT; r.font.size = Pt(size); r.font.bold = bold; r.font.color.rgb = col
    return tb


# Legend
lx = X0 + 0.22
for name, col in (("NovaSeq X Plus", GREY), ("Roche AXELIOS", ORANGE)):
    rect(lx, Y0 + 0.045, 0.08, 0.08, col)
    text(lx + 0.11, Y0, 0.85, 0.17, [(name, False, BLACK)], 7.5)
    lx += 0.98

# Rows
for i, (lab, xv, av, xl, al, gap) in enumerate(ROWS):
    y = TOP + i * ROW_H
    mid = y + BAR_H + BAR_GAP / 2
    text(X0, mid - 0.09, LBL_W, 0.18, [(lab, True, BLACK)], 7.5, align=PP_ALIGN.RIGHT)
    rect(AX, y, BAR_MAX, BAR_H, GREY)
    text(AX + BAR_MAX + 0.04, y - 0.015, 0.7, BAR_H + 0.03, [(xl, False, BLACK)], 7.5)
    alen = BAR_MAX * av / xv
    rect(AX, y + BAR_H + BAR_GAP, alen, BAR_H, ORANGE)
    text(AX + alen + 0.04, y + BAR_H + BAR_GAP - 0.015, 0.8, BAR_H + 0.03,
         [(al + " ", True, BLACK), (gap, True, RED)], 7.5)

# Axis line
bottom = TOP + (len(ROWS) - 1) * ROW_H + 2 * BAR_H + BAR_GAP + 0.05
ax = S.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(AX), Inches(TOP - 0.05), Inches(AX), Inches(bottom))
ax.line.color.rgb = BLACK; ax.line.width = Pt(0.75)

prs.save(OUT)
print("saved", OUT, "bottom at", round(bottom, 2), "in")
