"""Dependency-free Markdown -> self-contained HTML page (headings, paragraphs, nested lists, tables,
blockquotes, bold/italic/code/links), with a table of contents and light/dark theme tokens."""
import html
import re

CSS = """
:root{--bg:#fbfaf7;--surface:#ffffff;--text:#1d1c1a;--muted:#5f5d57;--faint:#8a877f;--border:#e2dfd6;
--accent:#1f5fa8;--accent-bg:#e9f1fb;--zebra:#f6f4ee;--code:#f1efe8}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#161615;--surface:#1e1e1c;--text:#ecebe6;
--muted:#bcbab1;--faint:#8f8c84;--border:#34332f;--accent:#7fb2ec;--accent-bg:#1c2a3a;--zebra:#232320;--code:#2a2a27;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#161615;--surface:#1e1e1c;--text:#ecebe6;--muted:#bcbab1;--faint:#8f8c84;--border:#34332f;
--accent:#7fb2ec;--accent-bg:#1c2a3a;--zebra:#232320;--code:#2a2a27;color-scheme:dark}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--text);font-family:"Source Sans 3",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
font-size:17px;line-height:1.65}
.wrap{max-width:820px;margin:0 auto;padding:28px 16px 80px}
header{border-bottom:1px solid var(--border);padding-bottom:16px;margin-bottom:20px}
header .kicker{color:var(--faint);font-size:13px;letter-spacing:.02em}
h1{font-size:30px;line-height:1.25;margin:6px 0 8px}h2{font-size:23px;margin:44px 0 12px;padding-top:8px;border-top:1px solid var(--border)}
h3{font-size:19px;margin:28px 0 8px}h4{font-size:17px;margin:22px 0 6px}
p{margin:0 0 14px}a{color:var(--accent)}strong{font-weight:600}
ul,ol{margin:0 0 14px;padding-left:24px}li{margin:4px 0}li>ul,li>ol{margin:4px 0 4px}
code{background:var(--code);padding:1px 5px;border-radius:4px;font-size:.88em;font-family:ui-monospace,Consolas,monospace}
blockquote{margin:0 0 14px;padding:8px 14px;border-left:3px solid var(--accent);background:var(--accent-bg)}
.tbl{overflow-x:auto;margin:0 0 18px;border:1px solid var(--border);border-radius:8px}
table{border-collapse:collapse;width:100%;font-size:14.5px;background:var(--surface)}
th,td{padding:7px 10px;border-bottom:1px solid var(--border);text-align:left;vertical-align:top}
th{background:var(--zebra);font-weight:600}tr:nth-child(even) td{background:var(--zebra)}
nav.toc{background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:14px 18px;margin:0 0 24px}
nav.toc strong{display:block;margin-bottom:6px}nav.toc ol{margin:0;padding-left:20px;font-size:15px}
.toggle{float:right;font:inherit;font-size:13px;background:transparent;color:var(--muted);border:1px solid var(--border);
border-radius:6px;padding:3px 9px;cursor:pointer}
@media (max-width:600px){body{font-size:16px}h1{font-size:25px}h2{font-size:20px}}
"""


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", lambda m: f"<code>{m.group(1)}</code>", s)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2" rel="noopener">\1</a>', s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![*\w])\*([^*\n]+)\*(?![*\w])", r"<em>\1</em>", s)
    return s


def slug(t, used):
    b = re.sub(r"[^a-z0-9]+", "-", re.sub(r"<[^>]+>", "", t).lower()).strip("-")[:60] or "s"
    s, i = b, 2
    while s in used:
        s, i = f"{b}-{i}", i + 1
    used.add(s)
    return s


def convert(md, title, description):
    lines = md.replace("\r\n", "\n").split("\n")
    out, toc, used = [], [], set()
    h1 = None
    i, n = 0, len(lines)
    para = []

    def flush():
        if para:
            out.append("<p>" + inline(" ".join(x.strip() for x in para)) + "</p>")
            para.clear()

    while i < n:
        ln = lines[i]
        if not ln.strip():
            flush(); i += 1; continue
        m = re.match(r"^(#{1,4})\s+(.*)$", ln)
        if m:
            flush()
            lvl, txt = len(m.group(1)), m.group(2).strip()
            if lvl == 1 and h1 is None:
                h1 = txt; i += 1; continue
            sid = slug(txt, used)
            if lvl == 2:
                toc.append((sid, inline(txt)))
            out.append(f'<h{lvl} id="{sid}">{inline(txt)}</h{lvl}>')
            i += 1; continue
        if ln.lstrip().startswith("|") and i + 1 < n and re.match(r"^\s*\|?\s*:?-{2,}", lines[i + 1]):
            flush()
            def cells(r):
                r = r.strip().strip("|")
                return [c.strip() for c in r.split("|")]
            head = cells(ln); i += 2
            rows = []
            while i < n and lines[i].lstrip().startswith("|"):
                rows.append(cells(lines[i])); i += 1
            t = ["<div class=\"tbl\"><table><thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead><tbody>"]
            for r in rows:
                t.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
            out.append("".join(t) + "</tbody></table></div>")
            continue
        if ln.startswith(">"):
            flush()
            q = []
            while i < n and lines[i].startswith(">"):
                q.append(lines[i].lstrip(">").strip()); i += 1
            out.append("<blockquote>" + inline(" ".join(q)) + "</blockquote>")
            continue
        if re.match(r"^\s*([-*+]|\d+[.)])\s+", ln):
            flush()
            items = []  # (indent, ordered, text)
            while i < n:
                l2 = lines[i]
                mm = re.match(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$", l2)
                if mm:
                    items.append([len(mm.group(1).replace("\t", "    ")), mm.group(2)[0].isdigit(), mm.group(3)])
                    i += 1
                elif l2.strip() and items and (l2.startswith("  ") or l2.startswith("\t")):
                    items[-1][2] += " " + l2.strip(); i += 1
                else:
                    break
            out.append(render_list(items))
            continue
        para.append(ln); i += 1
    flush()
    toc_html = ""
    if toc:
        toc_html = ('<nav class="toc" aria-label="Contents"><strong>Contents</strong><ol>' +
                    "".join(f'<li><a href="#{s}">{t}</a></li>' for s, t in toc) + "</ol></nav>")
    head_title = inline(h1 or title)
    # Page fragment: the artifact publisher supplies the doctype/html/head/body skeleton.
    return f"""<title>{html.escape(title)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;600&display=swap" rel="stylesheet">
<style>{CSS}</style>
<div class="wrap"><header><button class="toggle" type="button" onclick="(function(){{var r=document.documentElement;var d=r.getAttribute('data-theme')==='dark'||(!r.getAttribute('data-theme')&&matchMedia('(prefers-color-scheme: dark)').matches);r.setAttribute('data-theme',d?'light':'dark');}})()">Theme</button>
<div class="kicker">Illumina research · Core Notes addendum</div><h1>{head_title}</h1><p style="color:var(--muted);margin:0">{html.escape(description)}</p></header>
{toc_html}
{"".join(out)}
</div>"""


def render_list(items):
    html_parts, stack = [], []  # stack of (indent, tag)
    for indent, ordered, text in items:
        tag = "ol" if ordered else "ul"
        if not stack or indent > stack[-1][0]:
            html_parts.append(f"<{tag}>"); stack.append((indent, tag))
        else:
            while stack and indent < stack[-1][0]:
                html_parts.append(f"</li></{stack.pop()[1]}>")
            html_parts.append("</li>")
        html_parts.append(f"<li>{inline(text)}")
    while stack:
        html_parts.append(f"</li></{stack.pop()[1]}>")
    return "".join(html_parts)
