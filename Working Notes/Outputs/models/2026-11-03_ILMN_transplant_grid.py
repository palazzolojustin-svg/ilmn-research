"""Copies typed Driver Grid cells and DCF Inputs values from an older inputs workbook into a
freshly regenerated one (same driver ids, cases and period ids; grey history columns skipped).
Usage: python transplant_grid.py <old.xlsx> <new.xlsx>"""
import sys, openpyxl
from openpyxl.styles import PatternFill

old_path, new_path = sys.argv[1], sys.argv[2]
old, new = openpyxl.load_workbook(old_path), openpyxl.load_workbook(new_path)


def grid_index(ws):
    hdr = {}
    for col in range(3, ws.max_column + 1):
        v = ws.cell(3, col).value
        if v and v != "Comment":
            hdr[col] = str(v)[:-1] if str(v).endswith("E") else str(v)
    rows = {}
    for r in range(4, ws.max_row + 1):
        a, b = ws.cell(r, 1).value, ws.cell(r, 2).value
        if a and b:
            rows[(a, b)] = r
    return hdr, rows


def is_grey(cell):
    f = cell.fill
    return f is not None and f.fill_type == "solid" and str(f.start_color.rgb).upper().endswith("F2F2F2")


ow, nw = old["Driver Grid"], new["Driver Grid"]
oh, orows = grid_index(ow)
nh, nrows = grid_index(nw)
ncol_of = {pid: col for col, pid in nh.items()}
n = skipped = 0
for (did, case), r in orows.items():
    if case not in ("Disaster", "Bear", "Base", "Bull", "Blowout", "Active"):
        continue
    if (did, case) not in nrows:
        continue
    rn = nrows[(did, case)]
    for col, pid in oh.items():
        c = ow.cell(r, col)
        if c.value is None or c.value == "" or is_grey(c):
            continue
        if pid not in ncol_of:
            skipped += 1; continue
        target = nw.cell(rn, ncol_of[pid])
        if is_grey(target):
            skipped += 1; continue
        target.value = c.value
        if isinstance(c.value, str) and c.value.startswith("="):
            target.data_type = "s"
        n += 1
# DCF Inputs values and Multiples weights / blocks are retyped from the old workbook
od, nd = old["DCF Inputs"], new["DCF Inputs"]
nkeys = {nd.cell(r, 1).value: r for r in range(4, nd.max_row + 1) if nd.cell(r, 1).value}
m = 0
for r in range(4, od.max_row + 1):
    k, v = od.cell(r, 1).value, od.cell(r, 3).value
    if k in nkeys and v is not None:
        nd.cell(nkeys[k], 3).value = v; m += 1
om, nm = old["Multiples"], new["Multiples"]
for r in range(4, om.max_row + 1):
    for c in range(1, om.max_column + 1):
        v = om.cell(r, c).value
        if v is not None and nm.cell(r, c).value in (None, "") and isinstance(v, (int, float, str)):
            nm.cell(r, c).value = v
new.save(new_path)
print(f"transplanted {n} grid cells (skipped {skipped} that are now history or off the axis), {m} DCF inputs")
