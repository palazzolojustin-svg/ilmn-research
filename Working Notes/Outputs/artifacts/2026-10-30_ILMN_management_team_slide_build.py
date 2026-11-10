"""One-slide ILMN 'Management Team' page (top 4 executives): tenure, prior employers, ownership.

Ownership: 2026 DEF 14A beneficial ownership table, record date 26 Mar 2026, 151,906,915 shares outstanding.
Tenure in role measured to 30 Oct 2026. Photos are grey placeholder pictures: right-click > Change Picture to swap in headshots.
Usage: python -I build.py <out.pptx> <tmp_dir>
"""
import os, sys
from PIL import Image, ImageDraw, ImageFont
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR

OUT, TMP = sys.argv[1], sys.argv[2]
FONT, SERIF = "Arial", "Times New Roman"
NAVY, INK, CAP = "1F3A93", "111111", "E6E6E6"
SHARES_OUT = 151_906_915

team = [  # name, title, background, tenure line, shares (proxy)
    ("Jacob Thaysen", "Chief Executive Officer", "Ex-Agilent, Dako", "CEO since Sep 2023 (3.1 yrs)", 40_313),
    ("Ankur Dhingra", "Chief Financial Officer", "Ex-Summit, CareDx, Agilent", "CFO since Apr 2024 (2.5 yrs)", 13_053),
    ("Steve Barnard", "Chief Technology Officer", "Illumina since 1998 (employee #4)", "CTO since Aug 2023 (3.2 yrs)", 22_380),
    ("Kevin Pegels", "Chief of Global Operations", "Ex-Bayer, Clorox, Levi Strauss", "In role since 2021 (~5 yrs)", 13_135),
]
pct = lambda s: s / SHARES_OUT * 100
group_pct = pct(sum(t[4] for t in team))


def ceil_label(p):
    for cap in (0.01, 0.02, 0.03, 0.05, 0.1, 0.2, 0.5):
        if p < cap:
            return f"<{cap:g}%"
    return f"{p:.1f}%"


def placeholder(name, path):
    img = Image.new("RGB", (780, 720), (120, 124, 128))
    d = ImageDraw.Draw(img)
    try:
        f = ImageFont.truetype("arialbd.ttf", 150)
    except OSError:
        f = ImageFont.load_default()
    initials = "".join(w[0] for w in name.split())
    w, h = d.textbbox((0, 0), initials, font=f)[2:]
    d.text(((780 - w) / 2, (720 - h) / 2 - 20), initials, fill=(200, 202, 205), font=f)
    img.save(path)


prs = Presentation()
prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
s = prs.slides.add_slide(prs.slide_layouts[6])


def text(x, y, w, h, runs, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP):
    tb = s.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Inches(0.05)
    tf.margin_top = tf.margin_bottom = 0
    for i, para in enumerate(runs):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        for t, size, bold, color, *extra in para:
            r = p.add_run()
            r.text = t
            f = r.font
            f.size, f.bold, f.color.rgb = Pt(size), bold, RGBColor.from_string(color)
            f.name = extra[0] if extra and extra[0] else FONT
            if len(extra) > 1:
                f.underline = extra[1]
    return tb


text(Inches(0.4), Inches(0.25), Inches(8), Inches(0.6), [[("Management Team", 30, True, INK)]])
text(Inches(9.9), Inches(0.25), Inches(3.0), Inches(0.6), [[("illumina", 30, False, "F7A800")]], PP_ALIGN.RIGHT)
text(Inches(0.4), Inches(0.9), Inches(12.5), Inches(0.4), [[(
    f"Key mgmt. figures have avg. tenure in role of ~3.5 years and collectively own "
    f"{ceil_label(group_pct)} of shares outstanding", 17, False, INK)]])
ln = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(0.4), Inches(1.4), Inches(12.93), Inches(1.4))
ln.line.color.rgb = RGBColor.from_string(NAVY)
ln.line.width = Pt(2.5)

card_w, photo_h, cap_h, gap = Inches(2.75), Inches(2.55), Inches(1.45), Inches(0.35)
x0 = int((prs.slide_width - 4 * card_w - 3 * gap) / 2)
y0 = Inches(1.85)
for i, (name, title, bg, tenure, sh) in enumerate(team):
    x = x0 + i * (card_w + gap)
    png = os.path.join(TMP, f"ph_{i}.png")
    placeholder(name, png)
    s.shapes.add_picture(png, x, y0, card_w, photo_h)
    box = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y0 + photo_h, card_w, cap_h)
    box.fill.solid()
    box.fill.fore_color.rgb = RGBColor.from_string(CAP)
    box.line.fill.background()
    box.shadow.inherit = False
    text(x, y0 + photo_h + Inches(0.08), card_w, cap_h - Inches(0.1), [
        [(name, 13, True, INK, SERIF, True)],
        [(title, 12, False, INK, SERIF)],
        [(bg, 12, False, INK, SERIF)],
        [(tenure, 12, False, INK, SERIF)],
        [(f"{ceil_label(pct(sh))} Ownership", 12, True, INK, SERIF)],
    ], PP_ALIGN.CENTER)

text(Inches(0.4), Inches(6.95), Inches(12.5), Inches(0.35), [[(
    f"Source: ILMN 2026 proxy (beneficial ownership as of 3/26/26; 151.9M shares out; includes RSUs/PSUs vesting within "
    f"60 days). Combined ownership of the four: {group_pct:.2f}%. Avg. Illumina tenure incl. prior roles ~11 yrs "
    f"(Barnard joined 1998, Pegels 2015). Tenure to 10/30/26.", 9, False, "666666")]])

prs.save(OUT)
print("saved", OUT, f"group={group_pct:.3f}%")
