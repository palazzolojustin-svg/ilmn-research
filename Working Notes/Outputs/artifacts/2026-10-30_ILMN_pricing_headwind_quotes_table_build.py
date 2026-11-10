"""Native PowerPoint table: management saying the X-transition pricing headwind is fading, three calls in a row.

Styled to match the pitch deck (Garamond, orange header, gold quarter column).
Lines: Q3'25 call :472 (Thaysen), Q4'25 call :174 (Dhingra, prepared remarks), Q1'26 call :298 (Thaysen),
in Working Notes/Sources/ILMN/earnings_call/. Cells marked [paste] are left for the user to fill from those lines.
Usage: python -I build.py <out.pptx>
"""
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn
from lxml import etree

OUT = sys.argv[1]
FONT, ORANGE, GOLD, INK, GREY = "Garamond", "E8962E", "F3C64B", "111111", "7F7F7F"

rows = [  # quarter, date, speaker, quote runs (text, italic, color)
    ("Q3’25", "Nov 2025", "Jacob Thaysen, CEO",
     [("“And now with the transition done, we see that, that pricing headwind is, of course, reducing.”", True, INK)]),
    ("Q4’25", "Feb 2026", "Ankur Dhingra, CFO",
     [("[Paste quote: Q4’25 call, line 174 (CFO prepared remarks)]", True, GREY)]),
    ("Q1’26", "Apr 2026", "Jacob Thaysen, CEO",
     [("[Paste quote: Q1’26 call, line 298 (starts “So when this market…”)]", True, GREY)]),
]

prs = Presentation()
prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
s = prs.slides.add_slide(prs.slide_layouts[6])
col_w = [Inches(1.3), Inches(6.2), Inches(2.0)]
x = int((prs.slide_width - sum(col_w)) / 2)
tbl = s.shapes.add_table(len(rows) + 1, 3, x, Inches(2.0), sum(col_w), Inches(3.2)).table
tblPr = tbl._tbl.tblPr
tblPr.set("firstRow", "0"); tblPr.set("bandRow", "0")
tblPr.find(qn("a:tableStyleId")).text = "{5940675A-B579-460E-94D1-54222C63F5DA}"
for i, w in enumerate(col_w):
    tbl.columns[i].width = w
tbl.rows[0].height = Inches(0.5)
for r in range(1, len(rows) + 1):
    tbl.rows[r].height = Inches(0.9)


def border(cell, side, color=None, w_pt=0.0):
    tcPr = cell._tc.get_or_add_tcPr()
    tag = qn({"L": "a:lnL", "R": "a:lnR", "T": "a:lnT", "B": "a:lnB"}[side])
    old = tcPr.find(tag)
    if old is not None:
        tcPr.remove(old)
    ln = etree.SubElement(tcPr, tag, w=str(int(Pt(w_pt))) if color else "0")
    if color:
        etree.SubElement(etree.SubElement(ln, qn("a:solidFill")), qn("a:srgbClr"), val=color)
    else:
        etree.SubElement(ln, qn("a:noFill"))
    order = [qn(t) for t in ("a:lnL", "a:lnR", "a:lnT", "a:lnB")]
    lines = sorted([c for c in tcPr if c.tag in order], key=lambda c: order.index(c.tag))
    for c in lines:
        tcPr.remove(c)
    for i, c in enumerate(lines):
        tcPr.insert(i, c)


def write(cell, paras, align=PP_ALIGN.LEFT, fill=None):
    if fill:
        cell.fill.solid(); cell.fill.fore_color.rgb = RGBColor.from_string(fill)
    else:
        cell.fill.background()
    cell.vertical_anchor = MSO_ANCHOR.MIDDLE
    cell.margin_left = cell.margin_right = Inches(0.12)
    tf = cell.text_frame
    tf.word_wrap = True
    for i, para in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        for text, size, bold, italic, color in para:
            r = p.add_run(); r.text = text
            r.font.name, r.font.size, r.font.bold, r.font.italic = FONT, Pt(size), bold, italic
            r.font.color.rgb = RGBColor.from_string(color)


hdr = tbl.cell(0, 0); hdr.merge(tbl.cell(0, 2))
write(hdr, [[("“Pricing Headwind Is Fading” — Three Calls in a Row", 16, True, False, INK)]], PP_ALIGN.CENTER, ORANGE)
for r, (q, date, who, quote) in enumerate(rows, start=1):
    write(tbl.cell(r, 0), [[(q, 15, True, False, INK)], [(date, 11, False, False, INK)]], PP_ALIGN.CENTER, GOLD)
    write(tbl.cell(r, 1), [[(t, 14, False, it, c) for t, it, c in quote]])
    write(tbl.cell(r, 2), [[(who, 12, False, False, INK)], [("Earnings call", 11, False, False, GREY)]])

for r in range(len(rows) + 1):
    for c in range(3):
        for side in "LRTB":
            border(tbl.cell(r, c), side)
for r in range(1, len(rows) + 1):
    border(tbl.cell(r, 0), "R", ORANGE, 2.25); border(tbl.cell(r, 1), "L", ORANGE, 2.25)
    border(tbl.cell(r, 1), "R", ORANGE, 2.25); border(tbl.cell(r, 2), "L", ORANGE, 2.25)
    if r < len(rows):
        for c in range(3):
            border(tbl.cell(r, c), "B", "D9D9D9", 0.75); border(tbl.cell(r + 1, c), "T", "D9D9D9", 0.75)

prs.save(OUT)
print("saved", OUT)
