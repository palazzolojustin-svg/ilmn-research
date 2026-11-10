"""Native PowerPoint table: ILMN's Apr 2023 operating-margin commitment (25% in 2024, 27% in 2025) vs actuals.

Quote: Joydeep Goswami (CFO), Q1'23 call, 25 Apr 2023, Sources/ILMN/earnings_call/ILMN_2023Q1_Earnings_Call.md:282.
Actuals: Core non-GAAP operating margin, Core Notes 02 (FY24 21.3% Core Illumina ex-GRAIL; FY25 23.1%).
Usage: python -I build.py <out.pptx>
"""
import sys
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn
from lxml import etree

OUT = sys.argv[1]
NAVY, GREY, WHITE, INK, RED = "24399A", "E8E8EA", "FFFFFF", "1A1A1A", "C0392B"
FONT = "Arial"

prs = Presentation()
prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
slide = prs.slides.add_slide(prs.slide_layouts[6])

col_w = [Inches(1.6), Inches(5.6), Inches(2.6)]
x = int((prs.slide_width - sum(col_w)) / 2)
shape = slide.shapes.add_table(3, 3, x, Inches(2.2), sum(col_w), Inches(2.6))
tbl = shape.table
tblPr = tbl._tbl.tblPr
for attr in ("firstRow", "bandRow"):
    tblPr.set(attr, "0")
style = tblPr.find(qn("a:tableStyleId"))
if style is not None:
    style.text = "{5940675A-B579-460E-94D1-54222C63F5DA}"  # "No Style, Table Grid" -> we override all borders below
for i, w in enumerate(col_w):
    tbl.columns[i].width = w
tbl.rows[0].height = Inches(0.6)
tbl.rows[1].height = tbl.rows[2].height = Inches(1.0)


def border(cell, side, color=None, w_pt=0.0):
    tcPr = cell._tc.get_or_add_tcPr()
    tag = {"L": "a:lnL", "R": "a:lnR", "T": "a:lnT", "B": "a:lnB"}[side]
    old = tcPr.find(qn(tag))
    if old is not None:
        tcPr.remove(old)
    ln = etree.SubElement(tcPr, qn(tag), w=str(int(Pt(w_pt))) if color else "0")
    if color:
        fill = etree.SubElement(ln, qn("a:solidFill"))
        etree.SubElement(fill, qn("a:srgbClr"), val=color)
    else:
        etree.SubElement(ln, qn("a:noFill"))
    # schema order inside tcPr: lnL, lnR, lnT, lnB, ..., fill
    order = [qn(t) for t in ("a:lnL", "a:lnR", "a:lnT", "a:lnB")]
    lines = sorted([c for c in tcPr if c.tag in order], key=lambda c: order.index(c.tag))
    for c in lines:
        tcPr.remove(c)
    for i, c in enumerate(lines):
        tcPr.insert(i, c)


def fill(cell, color):
    cell.fill.solid()
    cell.fill.fore_color.rgb = RGBColor.from_string(color)


def write(cell, runs, align=PP_ALIGN.LEFT, size=16):
    """runs: list of paragraphs; each paragraph is a list of (text, bold, italic, color)."""
    tf = cell.text_frame
    tf.word_wrap = True
    cell.vertical_anchor = MSO_ANCHOR.MIDDLE
    cell.margin_left = cell.margin_right = Inches(0.15)
    cell.margin_top = cell.margin_bottom = Inches(0.06)
    for pi, para in enumerate(runs):
        p = tf.paragraphs[0] if pi == 0 else tf.add_paragraph()
        p.alignment = align
        for text, bold, italic, color, *sz in para:
            r = p.add_run()
            r.text = text
            f = r.font
            f.name, f.bold, f.italic = FONT, bold, italic
            f.size = Pt(sz[0] if sz else size)
            f.color.rgb = RGBColor.from_string(color)


# header row: merged title bar
hdr = tbl.cell(0, 0)
hdr.merge(tbl.cell(0, 2))
fill(hdr, NAVY)
write(hdr, [[("Operating Margin: Promised vs. Delivered", True, False, WHITE, 20)]], PP_ALIGN.CENTER)

# middle column merged across both data rows: the quote
q = tbl.cell(1, 1)
q.merge(tbl.cell(2, 1))
fill(q, WHITE)
write(q, [
    [("“…non-GAAP operating margins of 25% in 2024 and 27% in 2025”", False, True, INK, 17)],
    [("— Joydeep Goswami, CFO, Q1’23 earnings call (Apr 25, 2023)", False, False, "555555", 12)],
])

rows = [
    ("2024", "25% target", "21.3% actual", "(−370 bps)"),
    ("2025", "27% target", "23.1% actual", "(−390 bps)"),
]
for i, (yr, tgt, act, miss) in enumerate(rows, start=1):
    c0, c2 = tbl.cell(i, 0), tbl.cell(i, 2)
    fill(c0, GREY)
    write(c0, [[(yr, True, False, NAVY, 18)], [(tgt, False, False, NAVY, 12)]], PP_ALIGN.CENTER)
    fill(c2, WHITE)
    write(c2, [[(act, True, False, INK, 16)], [(miss, False, False, RED, 13)]])

# borders: thick navy verticals between columns, light grey horizontals, nothing on the outside
for r in range(3):
    for c in range(3):
        cell = tbl.cell(r, c)
        for side in "LRTB":
            border(cell, side)
for r in (1, 2):
    border(tbl.cell(r, 0), "R", NAVY, 2.25)
    border(tbl.cell(r, 1), "L", NAVY, 2.25)
    border(tbl.cell(r, 1), "R", NAVY, 2.25)
    border(tbl.cell(r, 2), "L", NAVY, 2.25)
for c in range(3):
    border(tbl.cell(1, c), "B", "FFFFFF", 3)
    border(tbl.cell(2, c), "T", "FFFFFF", 3)

note = slide.shapes.add_textbox(x, Inches(4.9), sum(col_w), Inches(0.4))
p = note.text_frame.paragraphs[0]
r = p.add_run()
r.text = ("Core Illumina non-GAAP operating margin. 2024 actual excludes GRAIL. "
          "Source: ILMN Q1’23 call; FY24/FY25 results.")
r.font.name, r.font.size, r.font.italic = FONT, Pt(10), True
r.font.color.rgb = RGBColor.from_string("777777")

prs.save(OUT)
print("saved", OUT)
