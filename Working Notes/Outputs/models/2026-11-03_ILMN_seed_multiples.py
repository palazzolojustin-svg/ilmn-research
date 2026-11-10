"""Seeds model_spec.json with numeric multiples so the Tearsheet sensitivity grids build:
each case's implied multiple from the Multiples Build tab when sane, else that case's target P/E
applied to the Base case's net income, net debt and EBITDA (cached values of the last Excel save).
Usage: python seed_multiples.py model_spec.json implied.json model.xlsx"""
import json, sys, openpyxl

spec = json.load(open(sys.argv[1], encoding="utf-8"))
imp = json.load(open(sys.argv[2], encoding="utf-8"))["implied"]
wb = openpyxl.load_workbook(sys.argv[3], data_only=True)
ws = wb["Multiples Build"]


def ok(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool) and 0 < v < 200


def num(*xs):
    return all(isinstance(x, (int, float)) and not isinstance(x, bool) for x in xs)


rows = {"YE2027": {"Blowout": 6, "Bull": 7, "Base": 8, "Bear": 9, "Disaster": 10},
        "YE2028": {"Blowout": 14, "Bull": 15, "Base": 16, "Bear": 17, "Disaster": 18}}
drows = {"Disaster": 23, "Bear": 24, "Base": 25, "Bull": 26, "Blowout": 27}


def base_seed(b, case):
    rb, rc = rows[b]["Base"], rows[b][case]
    pe, ni, debt, cash, ebitda = (ws[f"C{rc}"].value, ws[f"D{rb}"].value, ws[f"F{rb}"].value, ws[f"G{rb}"].value, ws[f"I{rb}"].value)
    return (pe * ni + debt - cash) / ebitda if num(pe, ni, debt, cash, ebitda) and ebitda else None


def dcf_seed(case):
    rb, rc = drows["Base"], drows[case]
    pe, ni, debt, cash, ebitda = (ws[f"C{rc}"].value, ws[f"E{rb}"].value, ws[f"G{rb}"].value, ws[f"H{rb}"].value, ws[f"J{rb}"].value)
    return (pe * ni + debt - cash) / ebitda if num(pe, ni, debt, cash, ebitda) and ebitda else None


# a case with no typed driver values projects nonsense: seed it from the Base case's figures instead
cased = [d for d in spec["drivers"] if d.get("cased") in (True, "Y") or any(c in (d.get("values") or {}) for c in spec["cases"])]
empty_case = {case: not any((d.get("values") or {}).get(case) for d in cased) for case in spec["cases"]}
print("empty cases:", [c for c, e in empty_case.items() if e])
mult = {}
for case in spec["cases"]:
    mult[case] = {}
    for b in ("YE2027", "YE2028"):
        v = None if empty_case[case] else imp[b].get(case)
        v = v if ok(v) else base_seed(b, case)
        if ok(v):
            mult[case][b] = round(v, 2)
spec["tearsheet"]["multiples"] = mult
ex = {}
for case in spec["cases"]:
    v = None if empty_case[case] else imp["dcf"].get(case)
    v = v if ok(v) else dcf_seed(case)
    if ok(v):
        ex[case] = round(v, 2)
spec["dcf"]["exit_multiples"] = ex
json.dump(spec, open(sys.argv[1], "w", encoding="utf-8"), indent=1)
print("seeded:", mult, ex)
