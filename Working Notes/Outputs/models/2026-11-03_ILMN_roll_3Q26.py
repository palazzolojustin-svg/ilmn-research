"""Rolls model_data_raw.json to 3Q26 actuals: writes the reported 3Q26 value into every Bloomberg
quarterly line named in the actuals file (section|label -> value), marks 3Q26 as reported, and
derives the quarter's cash-flow lines from the nine-month figures less 1Q26 and 2Q26.
Usage: python roll_3q26.py model_data_raw.json q3_2026_actuals.json"""
import json, sys

raw_path, act_path = sys.argv[1], sys.argv[2]
d = json.load(open(raw_path, encoding="utf-8"))
act = json.load(open(act_path, encoding="utf-8"))
vals = act["values"]            # {"Section|Label": number}
ninem = act.get("nine_month", {})  # {"Section|Label": nine-month number}: quarter = 9M - 1Q26 - 2Q26
PID = "3Q26"
L = [l for l in d["lines"] if l["source"] == "bloomberg_md" and l["file"] != "ILMN_Consensus_Annuals.md"]
index = {}
for l in L:
    index.setdefault(f"{l['section']}|{l['label']}", []).append(l)


def put(key, v, note):
    if key not in index:
        print("NO LINE:", key); return
    for l in index[key]:
        l["values"][PID] = v
        l.setdefault("est", {})[PID] = False
    written.append((key, v, note))


written = []
for key, v in vals.items():
    put(key, v, "reported")
for key, v9 in ninem.items():
    if key not in index:
        print("NO LINE (9M):", key); continue
    l = index[key][0]
    q1, q2 = l["values"].get("1Q26"), l["values"].get("2Q26")
    if q1 is None or q2 is None:
        print("cannot derive", key, "1Q26/2Q26 missing"); continue
    put(key, round(v9 - q1 - q2, 2), f"9M {v9} less 1Q26 {q1} and 2Q26 {q2}")
for nl in act.get("new_lines", []):
    d["lines"].append({"file": "ILMN_Consensus_Quarterlies.md", "sheet": None, "section": nl["section"], "label": nl["label"],
                       "values": nl["values"], "pct": False, "suspect": False, "suspect_pids": [],
                       "est": {p: False for p in nl["values"]}, "source": "bloomberg_md"})
    print("added line", nl["section"], "|", nl["label"])
d["n_lines"] = len(d["lines"])
d["periods"][PID]["estimate"] = False
d["periods"][PID]["_end_est"] = False
missing = [k for k, ls in index.items() if ls[0]["values"].get("2Q26") is not None and ls[0]["values"].get(PID) is None]
json.dump(d, open(raw_path, "w", encoding="utf-8"), indent=1)
print("wrote", len(written), "values for", PID)
print("lines with a 2Q26 actual but no 3Q26 value:", missing)
