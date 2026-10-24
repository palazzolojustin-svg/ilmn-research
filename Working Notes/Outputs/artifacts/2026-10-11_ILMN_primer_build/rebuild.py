"""Rebuild the ILMN primer HTML from its parts and regenerate the Markdown copy.
Run from anywhere: python rebuild.py"""
import io, re, pathlib
from html.parser import HTMLParser

B = pathlib.Path(__file__).resolve().parent
OUT = B.parent.parent  # Working Notes/Outputs
PARTS = ["p00_head", "p01_open", "p02_summary", "p03_glossary", "p04_model", "p05_segments", "p06_supply",
         "p07_experts", "p08_questions", "p09_variance", "p10_guidance", "p11_consensus", "p12_competition",
         "p13_valuation", "p14_trades", "p15_trends", "p16_caveats"]

html = "".join(io.open(B / f"{p}.html", encoding="utf-8").read() + "\n" for p in PARTS)
html = html.replace("{{PRICE_CHART}}", io.open(B / "chart_price.svg", encoding="utf-8").read())
io.open(OUT / "artifacts" / "2026-10-11_ILMN_primer.html", "w", encoding="utf-8").write(html)

src = re.sub(r"<title>.*?</title>|<link[^>]*>|<style>.*?</style>|<nav.*?</nav>", "", html, flags=re.S)
src = re.sub(r'<div class="chart">.*?</div>', "\n\n*[Chart omitted in Markdown copy; see the HTML artifact.]*\n\n", src, flags=re.S)


class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.o = []; s.lst = []; s.tbl = None; s.cell = None; s.row = None; s.chip = False

    def w(s, t):
        (s.cell if s.cell is not None else s.o).append(t)

    def handle_starttag(s, t, a):
        c = dict(a).get("class", "")
        if t in ("h1", "h2", "h3", "h4"): s.w("\n\n" + "#" * int(t[1]) + " ")
        elif t == "p": s.w("\n\n")
        elif t in ("ul", "ol"): s.lst.append([t, 0]); s.w("\n")
        elif t == "li":
            l = s.lst[-1] if s.lst else ["ul", 0]; l[1] += 1
            s.w("\n" + ("  " * (len(s.lst) - 1)) + (f"{l[1]}. " if l[0] == "ol" else "- "))
        elif t in ("strong", "b"): s.w("**")
        elif t == "em": s.w("*")
        elif t == "table": s.tbl = []
        elif t == "tr": s.row = []
        elif t in ("td", "th"): s.cell = []
        elif t == "span" and "chip" in c: s.chip = True; s.w(" [")
        elif t == "div" and "lab" in c: s.w("\n\n> **")

    def handle_endtag(s, t):
        if t in ("h1", "h2", "h3", "h4"): s.w("\n")
        elif t in ("ul", "ol"):
            if s.lst: s.lst.pop()
            s.w("\n")
        elif t in ("strong", "b"): s.w("**")
        elif t == "em": s.w("*")
        elif t in ("td", "th"):
            s.row.append(re.sub(r"\s+", " ", "".join(s.cell)).strip().replace("|", "/")); s.cell = None
        elif t == "tr": s.tbl.append(s.row); s.row = None
        elif t == "table":
            rows = s.tbl; s.tbl = None
            if rows:
                n = max(len(r) for r in rows); rows = [r + [""] * (n - len(r)) for r in rows]
                s.o.append("\n\n| " + " | ".join(rows[0]) + " |\n|" + "---|" * n + "\n"
                           + "".join("| " + " | ".join(r) + " |\n" for r in rows[1:]))
        elif t == "span" and s.chip: s.chip = False; s.w("]")

    def handle_data(s, d):
        if s.chip: s.w(d.strip()); return
        s.w(re.sub(r"\s+", " ", d) if s.cell is None else d)


p = P(); p.feed(src); md = "".join(p.o)
md = re.sub(r"> \*\*([^\n]*?)\s*\n+", lambda m: "> **" + m.group(1).strip() + "**\n\n", md)
md = re.sub(r"[ \t]+\n", "\n", md); md = re.sub(r"\n{3,}", "\n\n", md); md = re.sub(r"\n +", "\n", md)
hdr = ("# Illumina buy-side primer (Markdown copy)\n\nMarkdown copy of the artifact at "
       "https://claude.ai/artifact/3JuCZERmQqeQugghZzU2n4 (HTML source: "
       "`Working Notes/Outputs/artifacts/2026-10-11_ILMN_primer.html`). Charts appear only in the HTML version.\n\n")
io.open(OUT / "primers" / "2026-10-11_ILMN_primer.md", "w", encoding="utf-8").write(hdr + md.strip() + "\n")
print("rebuilt HTML and Markdown")
