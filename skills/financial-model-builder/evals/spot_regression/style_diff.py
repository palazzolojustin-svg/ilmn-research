"""Style diff between the reference model and a rebuild, row by row (matched by label).
Usage: python style_diff.py <template.xlsx> <rebuild.xlsx> <sheet> [max_rows]
Prints sheet-level settings and, for each matched label, differences in font (name, size,
bold, italic, colour), fill, number format and borders across a sample of columns."""
import sys
from openpyxl import load_workbook

t, r, sheet = sys.argv[1], sys.argv[2], sys.argv[3]
max_rows = int(sys.argv[4]) if len(sys.argv) > 4 else 400
wt = load_workbook(t)[sheet]
wr = load_workbook(r)[sheet]


def rows_by_label(ws):
    out = {}
    for row in range(1, ws.max_row + 1):
        v = ws.cell(row=row, column=2).value
        if isinstance(v, str) and v.strip() and v.strip() not in out:
            out[v.strip()] = row
    return out


def col(c):
    try:
        if c.font is not None and c.font.color is not None:
            if c.font.color.type == "rgb":
                return c.font.color.rgb
            if c.font.color.type == "theme":
                return f"theme{c.font.color.theme}"
    except Exception:
        pass
    return None


def fill(c):
    try:
        if c.fill is not None and c.fill.fill_type:
            fg = c.fill.fgColor
            return fg.rgb if fg.type == "rgb" else f"theme{fg.theme}/{round(fg.tint or 0, 2)}"
    except Exception:
        pass
    return None


def desc(c):
    b = c.border
    return {"font": c.font.name, "size": c.font.sz, "bold": bool(c.font.bold), "italic": bool(c.font.italic), "colour": col(c),
            "fill": fill(c), "fmt": c.number_format, "top": b.top.style if b and b.top else None, "bottom": b.bottom.style if b and b.bottom else None}


print(f"== {sheet}: template dims {wt.dimensions} zoom {wt.sheet_view.zoomScale} freeze {wt.freeze_panes} grid {wt.sheet_view.showGridLines}")
print(f"== {sheet}: rebuild  dims {wr.dimensions} zoom {wr.sheet_view.zoomScale} freeze {wr.freeze_panes} grid {wr.sheet_view.showGridLines}")
wt_w = {k: round(v.width, 2) for k, v in wt.column_dimensions.items() if v.width}
wr_w = {k: round(v.width, 2) for k, v in wr.column_dimensions.items() if v.width}
print("column widths template:", wt_w)
print("column widths rebuild :", wr_w)
a, b = rows_by_label(wt), rows_by_label(wr)
print(f"labels: {len(a)} in template, {len(b)} in rebuild; only in template: {[k for k in a if k not in b][:20]}; only in rebuild: {[k for k in b if k not in a][:20]}")
print("row order template:", list(a)[:max_rows])
print("row order rebuild :", list(b)[:max_rows])
sample_cols = ["B", "D", "H", "U", "W", "AH"]
n = 0
for label, rt in a.items():
    rr = b.get(label)
    if rr is None:
        continue
    for cl in sample_cols:
        ct, cr = wt[f"{cl}{rt}"], wr[f"{cl}{rr}"]
        if ct.value is None and cr.value is None:
            continue
        dt, dr = desc(ct), desc(cr)
        diffs = {k: (dt[k], dr[k]) for k in dt if dt[k] != dr[k]}
        if diffs:
            print(f"  {label[:40]:40s} {cl}: template r{rt} vs rebuild r{rr}: {diffs}")
            n += 1
    if n > max_rows:
        break
print("style differences printed:", n)
