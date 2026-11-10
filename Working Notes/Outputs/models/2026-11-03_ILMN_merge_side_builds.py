"""Merges ILMN_side_builds.json into model_spec.json after every `spec` run.
Usage: python merge_side_builds.py model_spec.json ILMN_side_builds.json"""
import json, sys

spec_path, side_path = sys.argv[1], sys.argv[2]
spec = json.load(open(spec_path, encoding="utf-8"))
side = json.load(open(side_path, encoding="utf-8"))
spec["side_builds"] = side["side_builds"]
sheets = spec["sheets"]
for sheet_name, lines in side.get("line_values", {}).items():
    sh = sheets[sheet_name] if isinstance(sheets, dict) else [x for x in sheets if x.get("name") == sheet_name][0]
    blocks = sh["blocks"] if isinstance(sh, dict) else sh
    for b in blocks:
        if isinstance(b, dict) and "line" in b and b["line"]["id"] in lines:
            b["line"].setdefault("values", {}).update(lines[b["line"]["id"]])
for sheet_name, subs in side.get("line_subs", {}).items():
    sh = sheets[sheet_name] if isinstance(sheets, dict) else [x for x in sheets if x.get("name") == sheet_name][0]
    for b in (sh["blocks"] if isinstance(sh, dict) else sh):
        if isinstance(b, dict) and "line" in b and b["line"]["id"] in subs:
            b["line"]["subs"] = subs[b["line"]["id"]]
for d in spec["drivers"]:
    for pid, f in side.get("driver_links", {}).get(d["id"], {}).items():
        d["values"].setdefault("Base", {})[pid] = f
json.dump(spec, open(spec_path, "w", encoding="utf-8"), indent=1)
print("merged", len(side["side_builds"]), "side builds into", spec_path)
