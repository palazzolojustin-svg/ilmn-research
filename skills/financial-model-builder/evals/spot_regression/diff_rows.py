"""Row-by-row diff of cached values between the reference model and a rebuild, by label.
Usage: python diff_rows.py <template.xlsx> <rebuild.xlsx> [sheet] [cols e.g. AC,AD,AE,AF,AG,AH,AI]"""
import sys
from openpyxl import load_workbook

t, r = sys.argv[1], sys.argv[2]
sheets = [sys.argv[3]] if len(sys.argv) > 3 and sys.argv[3] != "-" else ["Revenue Build", "Margin Build", "Income Statement", "Cash Flow Statement", "Balance Sheet"]
cols = sys.argv[4].split(",") if len(sys.argv) > 4 else ["U", "AB", "AC", "AG", "AH", "AI"]
wt = load_workbook(t, data_only=True)
wr = load_workbook(r, data_only=True)


def rows_by_label(ws):
    out = {}
    for row in range(1, ws.max_row + 1):
        v = ws[f"B{row}"].value
        if isinstance(v, str) and v.strip() and v.strip() not in out:
            out[v.strip()] = row
    return out


for sh in sheets:
    a, b = rows_by_label(wt[sh]), rows_by_label(wr[sh])
    print(f"== {sh}: {len(a)} labels in template, {len(b)} in rebuild; missing in rebuild: {[k for k in a if k not in b][:15]}")
    for label, ra in a.items():
        rb = b.get(label)
        if rb is None:
            continue
        for c in cols:
            x, y = wt[sh][f"{c}{ra}"].value, wr[sh][f"{c}{rb}"].value
            if isinstance(x, (int, float)) and isinstance(y, (int, float)):
                if abs(x - y) > 1e-6 * max(1, abs(x)) and (abs(x) > 1e-9 or abs(y) > 1e-9):
                    print(f"   {label[:45]:45s} {c:3s} template={x:14.4f} rebuilt={y:14.4f}")
            elif (x is None) != (y is None) and (isinstance(x, (int, float)) or isinstance(y, (int, float))):
                print(f"   {label[:45]:45s} {c:3s} template={x!s:>14} rebuilt={y!s:>14}")
