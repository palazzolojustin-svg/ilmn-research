"""Compact ILMN management-team block (4 execs, no prior-employer line) sized for the top-right panel of the pitch slide.

Built as one grouped object on a 13.333 x 7.5 in slide, placed where the 'Management Has No Stake in the Game' panel sits
(about x 6.75-13.1 in, y 1.25-3.75 in), so copy-paste lands it in place. Same data as the full management-team slide:
2026 DEF 14A ownership (record date 3/26/26, 151,906,915 shares); tenure in role to 10/30/26.
Headshots: <tmp_dir>/photo_<lastname>.png (cropped from Illumina's management page); grey placeholder otherwise.
Usage: python -I build.py <out.pptx> <tmp_dir>
"""
import os, sys
from PIL import Image, ImageDraw, ImageFont
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

OUT, TMP = sys.argv[1], sys.argv[2]
FONT, INK, CAP = "Garamond", "111111", "E6E6E6"
SHARES_OUT = 151_906_915

team = [  # name, title, tenure, shares
    ("Jacob Thaysen", "CEO", "Since Sep '23 (3.1 yrs)", 40_313),
    ("Ankur Dhingra", "CFO", "Since Apr '24 (2.5 yrs)", 13_053),
    ("Steve Barnard", "CTO", "Since Aug '23 (3.2 yrs)", 22_380),
    ("Kevin Pegels", "Chief of Global Ops", "Since 2021 (~5 yrs)", 13_135),
]
pct = lambda s: s / SHARES_OUT * 100
group_pct = pct(sum(t[3] for t in team))


def ceil_label(p):
    for cap in (0.01, 0.02, 0.03, 0.05, 0.1, 0.2, 0.5):
        if p < cap:
            return f"<{cap:g}%"
    return f"{p:.1f}%"


def placeholder(name, path):
    img = Image.new("RGB", (600, 500), (120, 124, 128))
    d = ImageDraw.Draw(img)
    try:
        f = ImageFont.truetype("arialbd.ttf", 130)
    except OSError:
        f = ImageFont.load_default()
    initials = "".join(w[0] for w in name.split())
    w, h = d.textbbox((0, 0), initials, font=f)[2:]
    d.text(((600 - w) / 2, (500 - h) / 2 - 15), initials, fill=(200, 202, 205), font=f)
    img.save(path)


prs = Presentation()
prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
s = prs.slides.add_slide(prs.slide_layouts[6])
grp = s.shapes.add_group_shape()


def text(x, y, w, h, paras, align=PP_ALIGN.CENTER):
    tb = grp.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.TOP
    tf.margin_left = tf.margin_right = Inches(0.03)
    tf.margin_top = tf.margin_bottom = 0
    for i, para in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        for t, size, bold, *ul in para:
            r = p.add_run()
            r.text = t
            r.font.name, r.font.size, r.font.bold = FONT, Pt(size), bold
            r.font.color.rgb = RGBColor.from_string(INK)
            r.font.underline = bool(ul and ul[0])


X0, Y0, W = Inches(6.8), Inches(1.32), Inches(6.25)
gap = Inches(0.12)
card_w = int((W - 3 * gap) / 4)
photo_h, cap_h = Inches(1.2), Inches(0.82)
for i, (name, title, tenure, sh) in enumerate(team):
    x = X0 + i * (card_w + gap)
    png = os.path.join(TMP, f"photo_{name.split()[-1].lower()}.png")  # cropped headshot, if supplied
    if not os.path.exists(png):
        png = os.path.join(TMP, f"phc_{i}.png")
        placeholder(name, png)
    grp.shapes.add_picture(png, x, Y0, card_w, photo_h)
    box = grp.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, Y0 + photo_h, card_w, cap_h)
    box.fill.solid()
    box.fill.fore_color.rgb = RGBColor.from_string(CAP)
    box.line.fill.background()
    box.shadow.inherit = False
    text(x, Y0 + photo_h + Inches(0.05), card_w, cap_h - Inches(0.06), [
        [(name, 11, True, True)],
        [(title, 10, False)],
        [(tenure, 10, False)],
        [(f"{ceil_label(pct(sh))} Ownership", 10, True)],
    ])

text(X0, Y0 + photo_h + cap_h + Inches(0.08), W, Inches(0.3), [[
    (f"Avg. tenure in role ~3.5 yrs; combined ownership {group_pct:.2f}% of shares outstanding "
     f"(2026 proxy, as of 3/26/26)", 10, False)]])

prs.save(OUT)
print("saved", OUT)
