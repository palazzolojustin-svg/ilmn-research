"""Empty one-slide template that matches the ILMN pitch deck in the WGO format exactly.

It is built on that deck's own "Content" layout (title, subtitle, Illumina logo, black header rule
at y=1.14 in, grey footer rule at y=6.95 in, both spanning 0.20-9.77 in), so the header, footer, fonts and
theme are inherited rather than redrawn. On top it adds two full-width section headers in the deck's
section_head style (13 pt bold Garamond, centred, 1 pt black rule 0.32 in below the label) at the deck's
standard top (y=1.22) and bottom (y=4.03) positions, and the deck's footnote line.
Usage: python -I build.py <WGO-format deck.pptx> <out.pptx>
"""
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_CONNECTOR

DECK, OUT = sys.argv[1], sys.argv[2]
FONT = "Garamond"
X0, X1 = 0.20, 9.77          # the deck's rule extents

prs = Presentation(DECK)
# drop the deck's slides; keep its master, layouts and theme
sld_ids = prs.slides._sldIdLst
for sid in list(sld_ids):
    prs.part.drop_rel(sid.rId)
    sld_ids.remove(sid)

content = next(l for l in prs.slide_layouts if l.name == "Content")
s = prs.slides.add_slide(content)


def text(x, y, w, h, t, size, bold=False, italic=False, align=PP_ALIGN.LEFT,
         anchor=MSO_ANCHOR.MIDDLE, color="000000", name=None):
    # same text-box settings as the deck's text() helper
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


def section_head(y, label):
    # the deck's section_head(): label box h=0.3 anchored bottom, 1 pt black rule at y + 0.32
    text(X0, y, X1 - X0, 0.3, label, 13, bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.BOTTOM,
         name=f"Header {label}")
    ln = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(X0), Inches(y + 0.32), Inches(X1), Inches(y + 0.32))
    ln.line.color.rgb = RGBColor.from_string("000000")
    ln.line.width = Pt(1.0)
    ln.name = f"Rule {label}"


s.shapes.title.text = "1: Slide Title"
for ph in s.placeholders:
    if ph.placeholder_format.idx == 1:
        ph.text = "Subtitle: the one-line takeaway"

section_head(1.22, "Top Section Header")
section_head(4.03, "Bottom Section Header")
text(X0, 6.97, X1 - X0, 0.25, "[1] [Footnote / sources]", 8, italic=True, color="595959", name="Footnote")

prs.save(OUT)
print("saved", OUT)
