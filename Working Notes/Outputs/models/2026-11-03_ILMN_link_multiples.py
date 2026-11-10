"""After `build`: points the Tearsheet multiple cells and the DCF exit-multiple cells at the
Multiples Build tab (green links). Usage: python link_multiples.py <model.xlsx> <ILMN_side_builds.json>"""
import json, sys, copy
from openpyxl import load_workbook
from openpyxl.styles import Font

model_path, side_path = sys.argv[1], sys.argv[2]
side = json.load(open(side_path, encoding="utf-8"))
links = side["multiples_links"]
mp = json.load(open(model_path.replace(".xlsx", ".map.json"), encoding="utf-8"))
wb = load_workbook(model_path)


def green_formula(ws, addr, formula):
    cell = ws[addr.replace("$", "")]
    cell.value = "=" + formula
    f = copy.copy(cell.font)
    cell.font = Font(name=f.name, size=f.size, bold=f.bold, italic=f.italic, color="FF008000")


ts = wb["Tearsheet"]
for case, blocks in mp["tearsheet"]["multiples"].items():
    for blabel, addr in blocks.items():
        green_formula(ts, addr, links["tearsheet"][blabel][case])
dcf = wb["DCF"]
for case, row in mp["dcf"]["exit_rows"].items():
    green_formula(dcf, f"G{row}", links["dcf_exit"][case])
wb.save(model_path)
print("linked Tearsheet multiples and DCF exits to the Multiples Build tab")
