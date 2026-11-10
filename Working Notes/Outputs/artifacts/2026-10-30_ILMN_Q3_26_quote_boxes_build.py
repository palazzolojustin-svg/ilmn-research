"""Three Q3'26 call quotes as editable PowerPoint text boxes, styled like the user's Barclays quote box:
rounded rectangle, light-grey fill, orange dashed border, Garamond, bold black and bold-underlined orange emphasis.
Usage: python build.py <out.pptx>
"""
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.dml import MSO_LINE_DASH_STYLE
from pptx.dml.color import RGBColor

OUT = sys.argv[1]
FONT, SIZE = "Garamond", 14
ORANGE, FILL = RGBColor(0xE8, 0x96, 0x2E), RGBColor(0xF2, 0xF2, 0xF2)
N, B, O = {}, {"bold": True}, {"bold": True, "underline": True, "color": ORANGE}

QUOTES = [
    ("Q3'26 conversion and slide", [
        [("“In clinical, ", N), ("78% of volume is currently on the X, and we have seen the pace of conversion slow in recent quarters", B),
         (". This is the dynamic you've heard us talk about. Certain clinical customers are ", N),
         ("keeping current on-market assays on the 6000 while adding X capacity for new tests", B), (". ", N),
         ("We anticipate clinical conversion to reach 80% to 85% in the coming quarters.", O),
         (" And as such, we expect the year-over-year pricing headwinds from the X transition to be lower in 2027 than in 2026.", N)],
        [("As the X conversion is nearly complete, we believe these charts are becoming less relevant in ", N),
         ("showing the price and volume dynamics impacting our revenue growth. As such, we plan to discontinue showing this slide "
          "in our quarterly earnings presentations after Q4 2026", O),
         (".” – Ankur Dhingra, CFO (Q3'26 call)", N)],
    ]),
    ("Q3'26 Billion Cell Atlas", [
        [("“Our Billion Cell Atlas was designed to help address these limitations. ", N), ("Now over halfway complete", B),
         (", the Atlas is advancing toward an ", N),
         ("unprecedented AI-ready perturbation data set that helps biopharma partners connect genetic signals to cellular mechanisms", O),
         (", strengthening target validation, improved disease understanding and enable accelerated drug discovery. ", N),
         ("By working directly with biopharma, we are integrating their input", B),
         (" to ensure the proprietary data set is relevant and built to maximize value for both our partners and Illumina.” "
          "– Jacob Thaysen, CEO (Q3'26 call)", N)],
    ]),
    ("Q3'26 genome pricing Q&A", [
        [("Q: “Jacob, as you guys try to tap into this training model, virtual cell AI opportunity, can you just talk about ", N),
         ("how you see genome pricing playing into that", B),
         ("? I mean, obviously, you think that the X is the box to bet on, but ", N),
         ("there are some pretty cheap genomes that are being talked about out there pushing down to $50", B),
         (".” – Daniel Arias, Stifel", N)],
        [("A: “", N), ("We love elasticity.", O),
         (" We can address any opportunity that we need to. And we see this market could be much, much bigger, and we are -- we have "
          "the -- both the capabilities, but also innovation pipeline to be a very strong player in that. So both developing the data "
          "sets ourselves, but also looking at flywheel that we together with our customers, we create data sets, our customers can add "
          "on to those data sets, and we can create a bigger and bigger data sets for training those model. So we're excited about "
          "that, and ", N),
         ("I'm not super concerned about what others are doing right now.", O),
         ("” – Jacob Thaysen, CEO (Q3'26 call)", N)],
    ]),
]

prs = Presentation()
prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
slide = prs.slides.add_slide(prs.slide_layouts[6])
# Left column: quotes 1 and 2; right column: quote 3
SPOTS = [(0.4, 0.4, 6.1, 3.35), (0.4, 4.0, 6.1, 2.55), (6.83, 0.4, 6.1, 4.25)]

for (name, paras), (x, y, w, h) in zip(QUOTES, SPOTS):
    s = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    s.name = name
    s.adjustments[0] = 0.06
    s.fill.solid(); s.fill.fore_color.rgb = FILL
    s.line.color.rgb = ORANGE; s.line.width = Pt(1); s.line.dash_style = MSO_LINE_DASH_STYLE.DASH
    s.shadow.inherit = False
    tf = s.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.TOP
    tf.margin_left = tf.margin_right = Inches(0.15); tf.margin_top = tf.margin_bottom = Inches(0.08)
    for i, runs in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        if i: p.space_before = Pt(6)
        for t, f in runs:
            r = p.add_run(); r.text = t
            r.font.name = FONT; r.font.size = Pt(SIZE)
            r.font.bold = f.get("bold", False); r.font.underline = f.get("underline", False)
            r.font.color.rgb = f.get("color", RGBColor(0, 0, 0))

prs.save(OUT)
print("saved", OUT)
