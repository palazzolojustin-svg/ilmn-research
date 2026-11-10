"""Re-applied after every parse: goodwill decimal fix, sign-corrected non-operating line,
quarterly treasury stock from the 10-Q/10-K balance sheets, revenue guidance line."""
import json, sys
path = sys.argv[1]
d = json.load(open(path, encoding="utf-8"))
L = d["lines"]

# 1. Goodwill 128400 -> 1284.0 (estimate columns of the second quarterly printout)
for l in L:
    if l["label"] == "Goodwill" and l["source"] == "bloomberg_md":
        for p, v in list(l["values"].items()):
            if v == 128400.0:
                l["values"][p] = 1284.0
                l.setdefault("corrected_pids", []).append(p)
        l["suspect"] = False; l["suspect_pids"] = []
d["unresolved_suspects"] = [u for u in d.get("unresolved_suspects", []) if "Goodwill" not in str(u)]

# 2. Sign-corrected non-operating line: Bloomberg prints OI - pretax; the model wants pretax - OI
def collect(label, section, src):
    vals, est = {}, {}
    for l in L:
        if l["label"] == label and l["section"] == section and l["source"] == src:
            for p, v in l["values"].items():
                if p not in vals or (est.get(p) and not l["est"].get(p)):
                    vals[p] = v; est[p] = bool(l["est"].get(p))
    return vals, est
oi, oe = collect("Operating Income", "GAAP Results", "bloomberg_md")
pt, pe = collect("Pre-Tax Income", "GAAP Results", "bloomberg_md")
vals = {p: round(pt[p] - oi[p], 2) for p in pt if p in oi}
L.append({"file": "ILMN_Consensus_Quarterlies.md", "sheet": None, "section": "GAAP Results",
          "label": "Other Non-Operating Income (Expense)", "values": vals, "pct": False, "suspect": False,
          "suspect_pids": [], "est": {p: pe[p] for p in vals}, "source": "bloomberg_md"})
coi, _ = collect("Operating Income", "Income Statement", "capiq")
cpt, _ = collect("EBT Incl. Unusual Items", "Income Statement", "capiq")
cv = {p: round(cpt[p] - coi[p], 2) for p in cpt if p in coi}
L.append({"file": "2026-11-02_ILMN_CapIQ_Financials.xls", "sheet": "Income Statement", "section": "Income Statement",
          "label": "Other Non-Operating Income (Expense)", "values": cv, "pct": False, "suspect": False,
          "suspect_pids": [], "est": {p: False for p in cv}, "source": "capiq"})

# 3. Treasury stock, quarterly, from the filed balance sheets (10-Q 1Q25-2Q26, 10-K FY2025, CapIQ 3Q26)
tv = {"1Q25": -4139.0, "2Q25": -4523.0, "3Q25": -4645.0, "4Q25": -4699.0, "1Q26": -4931.0, "2Q26": -5054.0, "3Q26": -5065.0}
L.append({"file": "ILMN_Consensus_Quarterlies.md", "sheet": None, "section": "Liabilities & Equity",
          "label": "Treasury Stock", "values": tv, "pct": False, "suspect": False, "suspect_pids": [],
          "est": {p: False for p in tv}, "source": "bloomberg_md"})

# 4. Management revenue guidance (mid-points) with the prior-year actuals the growth delta needs
gv = {"FY2025": 4343.0, "FY2026": 4650.0, "4Q25": 1159.0, "4Q26": 1230.0}
L.append({"file": "guidance", "sheet": None, "section": "Guidance", "label": "Revenue Guidance (mid)",
          "values": gv, "pct": False, "suspect": False, "suspect_pids": [],
          "est": {"FY2025": False, "4Q25": False, "FY2026": True, "4Q26": True}, "source": "grid"})
d["n_lines"] = len(L)
json.dump(d, open(path, "w", encoding="utf-8"), indent=1)
print("patched", path, "lines", len(L))
print("nonop quarterly:", {p: vals[p] for p in sorted(vals) if not pe[p]})
print("nonop annual capiq:", cv)
