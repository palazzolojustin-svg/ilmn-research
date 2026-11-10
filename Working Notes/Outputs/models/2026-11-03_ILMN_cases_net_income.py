"""Per-case Adj. EPS snapshots for the Multiples Build tab (the counterpart of the skill's `cases`
step, which snapshots each case's Adj. EBITDA into the Tearsheet). Flips the case cell through
Excel, reads FY2027E and FY2028E Adj. Net Income, types them (blue) into the tab, recalculates and
returns the implied multiples. Usage: python cases_eps.py <model.xlsx> <model_spec.json> <ILMN_side_builds.json> [--out=multiples.json]"""
import json, sys
from pathlib import Path

sys.path.insert(0, r"C:/Users/palaz/.claude/skills/financial-model-builder/scripts")
from openpyxl import load_workbook
from fmb.excel import ExcelSession
from fmb import styles as S

model_path, spec_path, side_path = sys.argv[1], sys.argv[2], sys.argv[3]
out = next((a.split("=", 1)[1] for a in sys.argv[4:] if a.startswith("--out=")), None)
spec = json.loads(Path(spec_path).read_text(encoding="utf-8"))
side = json.loads(Path(side_path).read_text(encoding="utf-8"))
links = side["multiples_links"]
mp = json.loads(Path(model_path.replace(".xlsx", ".map.json")).read_text(encoding="utf-8"))
eps_row = mp["lines"]["Income Statement"]["adj_ni"]
cols = mp["columns"]
TAB = "Multiples Build"
eps_pid = {"YE2027": "FY2027", "YE2028": "FY2028"}

values = {}
with ExcelSession(model_path) as xl:
    drv = xl.wb.Worksheets("Drivers & Casing"); is_ws = xl.wb.Worksheets("Income Statement")
    original = drv.Range("B5").Value2
    for case in spec["cases"]:
        drv.Range("B5").Value2 = case
        xl.app.CalculateFullRebuild()
        values[case] = {b: (lambda v: v if isinstance(v, (int, float)) and not isinstance(v, bool) and abs(v) < 1e9 else None)(is_ws.Range(f"{cols[p]}{eps_row}").Value2) for b, p in eps_pid.items()}
    drv.Range("B5").Value2 = original
    xl.app.CalculateFullRebuild()
    drv = is_ws = None
wb = load_workbook(model_path)
ws = wb[TAB]
for b, per_case in links["eps_cells"].items():
    for case, addr in per_case.items():
        v = values[case][b]
        if v is not None:
            ws[addr].value = v
            ws[addr].font = S.font(S.BLUE, False)
wb.save(model_path)
implied = {}
with ExcelSession(model_path) as xl:
    xl.wb.Worksheets("Drivers & Casing").Range("B5").Value2 = spec.get("active_case", "Base")   # never leave the model on a flipped case
    xl.app.CalculateFullRebuild()
    ws_x = xl.wb.Worksheets(TAB)
    for key, per_case in links["implied_cells"].items():
        implied[key] = {case: ws_x.Range(addr).Value2 for case, addr in per_case.items()}
    ws_x = None
    xl.save()
print(json.dumps({"eps": values, "implied": implied}, indent=1))
if out:
    Path(out).write_text(json.dumps({"eps": values, "implied": implied}, indent=1), encoding="utf-8")
