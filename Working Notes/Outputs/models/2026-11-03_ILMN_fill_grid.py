"""Fills the Driver Grid of the ILMN inputs workbook per the analyst's specification (2026-11-03):
Base rows anchored to Bloomberg consensus, cost drivers as the % that reproduces street's nominal costs,
Greater China from the consensus y/y on Greater China revenue, and realised history in the grey cells.
Usage: python fill_grid.py <inputs.xlsx> <model_data_raw.json> [<hist2024.json>]"""
import json, sys, openpyxl

path, data_path = sys.argv[1], sys.argv[2]
hist24 = json.load(open(sys.argv[3], encoding="utf-8")) if len(sys.argv) > 3 else {}
data = json.load(open(data_path, encoding="utf-8"))
wb = openpyxl.load_workbook(path)
ws = wb["Driver Grid"]

hdr = {}
for col in range(3, ws.max_column + 1):
    v = ws.cell(3, col).value
    if v and v != "Comment":
        hdr[str(v).replace("E", "") if str(v).endswith("E") else str(v)] = col
rows = {}
for r in range(4, ws.max_row + 1):
    a, b = ws.cell(r, 1).value, ws.cell(r, 2).value
    if a and b in ("Base", "Active"):
        rows[a] = r

# periods from the grid header: grey history columns carry no E suffix, estimate columns do
_hdr_raw = {col: str(ws.cell(3, col).value) for col in range(3, ws.max_column + 1) if ws.cell(3, col).value and ws.cell(3, col).value != "Comment"}
HIST_Q = [v for v in _hdr_raw.values() if not v.endswith("E")]
EST_Q = [v[:-1] for v in _hdr_raw.values() if v.endswith("E") and not v.startswith("FY")]
EST_FY = [v[:-1] for v in _hdr_raw.values() if v.endswith("E") and v.startswith("FY")]
print("history columns:", HIST_Q, "| estimate quarters:", EST_Q, "| annual:", EST_FY)


def series(label, section=None, file_sub=None):
    out = {}
    for ln in data["lines"]:
        if ln["label"] == label and (section is None or ln.get("section") == section) and (file_sub is None or file_sub in ln.get("file", "")):
            for k, v in ln["values"].items():
                if v is not None:
                    out.setdefault(k, v)
    return out


def prior(pid):
    if pid.startswith("FY"):
        return f"FY{int(pid[2:]) - 1}"
    return pid[:2] + str(int(pid[2:]) - 1).zfill(2)


def yoy(s, pid):
    p = prior(pid)
    if pid in s and p in s and s[p]:
        return round(s[pid] / s[p] - 1, 6)
    return None


def put(r, pid, value, as_text=False):
    col = hdr[pid]
    cell = ws.cell(r, col)
    cell.value = value
    if as_text and isinstance(value, str):
        cell.data_type = "s"


def put_hist(r, pid, value):
    if value is not None:
        put(r, pid, round(value, 6))


# ---- consensus series --------------------------------------------------------------------------
BB = "Business Breakdown"
cons = {
    "array_cons_g": series("Microarray Consumables", BB),
    "seq_inst_g": series("Sequencing Instruments", BB),
    "array_inst_g": series("Microarray Instruments", BB),
    "service_g": series("Total Service & Other Revenue", BB) or series("Service & Other", "Segment Revenue"),
}
china = series("Greater China", "Regional Breakdown")
china.update({k: v for k, v in series("Greater China", "Gross Profit").items() if k.startswith("FY")})
# merge 2024 history (from the filings) for realised y/y in 3Q25/4Q25
for did, s in cons.items():
    for k, v in hist24.get(did, {}).items():
        s.setdefault(k, v)

for did, s in cons.items():
    r = rows[did]
    for pid in EST_Q + EST_FY:
        v = yoy(s, pid)
        if v is None:
            print("missing consensus", did, pid)
        else:
            put(r, pid, v)
    for pid in HIST_Q:
        put_hist(r, pid, yoy(s, pid))

r = rows["china_seq_cons_g"]
for pid in EST_Q + EST_FY:
    v = yoy(china, pid)
    if v is None:
        print("missing Greater China", pid)
    else:
        put(r, pid, v)
# realised Greater China sequencing consumables y/y from the mix build (total SC - ex-China SC)
tot_sc = series("Sequencing Consumables", BB)
tot_sc.update(hist24.get("seq_cons", {}))
row_sc = {"1Q25": 640, "2Q25": 690, "3Q25": 707, "4Q25": 713, "1Q26": 687, "2Q26": 734, "3Q26": 748, "1Q24": 640 / 1.00, "2Q24": 690 / 1.02, "3Q24": 684.0, "4Q24": 713 / 1.11}
china_sc = {k: tot_sc[k] - row_sc[k] for k in row_sc if k in tot_sc}
for pid in HIST_Q:
    put_hist(r, pid, yoy(china_sc, pid))

# clinical / research realised y/y (reported for 2025; 2026 research is the residual of the mix build)
g_clin = {"1Q25": 0.08, "2Q25": 0.10, "3Q25": 0.12, "4Q25": 0.20, "1Q26": 0.20, "2Q26": 0.15, "3Q26": 0.14}
g_res = {"1Q25": -0.11, "2Q25": -0.09, "3Q25": -0.08, "4Q25": 0.00, "1Q26": -0.12, "2Q26": -0.07, "3Q26": -0.06}
res24, clin24 = {}, {}
for q in ["1Q25", "2Q25", "3Q25", "4Q25"]:
    b = q[:2] + "24"
    res24[b] = (row_sc[q] - row_sc[b] * (1 + g_clin[q])) / (g_res[q] - g_clin[q])
    clin24[b] = row_sc[b] - res24[b]
clin = {q: clin24[q[:2] + "24"] * (1 + g_clin[q]) for q in ["1Q25", "2Q25", "3Q25", "4Q25"]}
res = {q: res24[q[:2] + "24"] * (1 + g_res[q]) for q in ["1Q25", "2Q25", "3Q25", "4Q25"]}
for q in ["1Q26", "2Q26", "3Q26"]:
    p = q[:2] + "25"
    clin[q] = clin[p] * (1 + g_clin[q])
    res[q] = row_sc[q] - clin[q]
clin.update(clin24); res.update(res24)
for pid in HIST_Q:
    put_hist(rows["clins_cons_g"], pid, yoy(clin, pid))
    put_hist(rows["research_cons_g"], pid, yoy(res, pid))

# ---- cost drivers: the % that reproduces street's nominal cost on the model's revenue ------------
ADJ = "Income Statement (Adjusted)"
GAAP = "GAAP Results"
cogs_p = series("Cost of Products Sold", ADJ); cogs_p.update({k: v for k, v in series("Cost of Products Sold", "Europe, Middle East & Africa").items() if k.startswith("FY")})
cogs_s = series("Cost of Services Sold", ADJ); cogs_s.update({k: v for k, v in series("Cost of Services Sold", "Europe, Middle East & Africa").items() if k.startswith("FY")})
sga = series("Selling, General & Administrative", GAAP)
rd = series("Research & Development", GAAP)
# street publishes no GAAP R&D beyond FY2026/4Q28; the adjusted annual line (within 1-2% of GAAP for Illumina) fills FY2029-FY2030
rd.update({k: v for k, v in series("Research & Development", "Europe, Middle East & Africa").items() if k.startswith("FY") and k not in rd})
prod = series("Product", "Segment Revenue"); serv = series("Service & Other", "Segment Revenue"); rev = series("Revenue", "Highlights")
for pid in EST_Q + EST_FY:
    if pid in cogs_p:
        put(rows["gm_product"], pid, f"=1-{cogs_p[pid]}/{{Revenue Build!product}}", as_text=True)
    else:
        print("missing street cogs_product", pid)
    if pid in cogs_s:
        put(rows["gm_service"], pid, f"=1-{cogs_s[pid]}/{{Revenue Build!service}}", as_text=True)
    else:
        print("missing street cogs_service", pid)
    if pid in sga:
        put(rows["sga_pct"], pid, f"={sga[pid]}/{{Revenue Build!total_rev}}", as_text=True)
    else:
        print("missing street sga", pid)
    if pid in rd:
        put(rows["rd_pct"], pid, f"={rd[pid]}/{{Revenue Build!total_rev}}", as_text=True)
    else:
        print("missing street rd (GAAP)", pid)
for pid in HIST_Q:
    put_hist(rows["gm_product"], pid, 1 - cogs_p[pid] / prod[pid])
    put_hist(rows["gm_service"], pid, 1 - cogs_s[pid] / serv[pid])
    put_hist(rows["sga_pct"], pid, sga[pid] / rev[pid])
    put_hist(rows["rd_pct"], pid, rd[pid] / rev[pid])

wb.save(path)
print("saved", path)
