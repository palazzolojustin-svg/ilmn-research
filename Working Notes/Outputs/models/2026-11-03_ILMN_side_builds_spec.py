"""Writes the ILMN side-build specs (Ex-China Consumables Mix, Implied Discounting Build) and the
history links of the Revenue Build lines to ILMN_side_builds.json. Usage: python make_side_builds.py <out.json>"""
import json, sys

out_path = sys.argv[1]
MIX = "Ex-China Consumables Mix"
DISC = "Implied Discounting Build"

# ---- Ex-China Consumables Mix -------------------------------------------------------------
# columns: D..G 2023 quarters, H FY2023, I..L 2024 quarters, M FY2024, N..Q 2025 quarters, R FY2025, S 1Q26, T 2Q26
cols = {"1Q23": "D", "2Q23": "E", "3Q23": "F", "4Q23": "G", "FY2023": "H",
        "1Q24": "I", "2Q24": "J", "3Q24": "K", "4Q24": "L", "FY2024": "M",
        "1Q25": "N", "2Q25": "O", "3Q25": "P", "4Q25": "Q", "FY2025": "R",
        "1Q26": "S", "2Q26": "T", "3Q26": "U"}
q23 = ["1Q23", "2Q23", "3Q23", "4Q23"]
q24 = ["1Q24", "2Q24", "3Q24", "4Q24"]
q25 = ["1Q25", "2Q25", "3Q25", "4Q25"]
q26 = ["1Q26", "2Q26", "3Q26"]
prior = {"1Q24": "1Q23", "2Q24": "2Q23", "3Q24": "3Q23", "4Q24": "4Q23", "1Q25": "1Q24", "2Q25": "2Q24", "3Q25": "3Q24", "4Q25": "4Q24", "1Q26": "1Q25", "2Q26": "2Q25", "3Q26": "3Q25"}
fy_of = {"FY2023": q23, "FY2024": q24, "FY2025": q25}

# reported figures (earnings decks slide 7 of Q1 2026 and Q2 2026; Q3 2025 deck for 3Q24 = 684; Q4 2025 call for 4Q24 total)
row_sc = {"1Q25": 640, "2Q25": 690, "3Q25": 707, "4Q25": 713, "1Q26": 687, "2Q26": 734, "3Q26": 748}
row_sc_24 = {"3Q24": 684}
tot_sc_24 = {"1Q24": 691, "2Q24": 729, "3Q24": 741, "4Q24": 698}
g_tot = {"1Q24": 0.01, "2Q24": 0.02, "3Q24": 0.09, "4Q24": 0.02, "1Q25": 0.00, "2Q25": 0.02, "3Q25": 0.03, "4Q25": 0.11, "1Q26": 0.07, "2Q26": 0.06, "3Q26": 0.06}
g_clin = {"1Q24": 0.07, "2Q24": 0.05, "3Q24": 0.11, "4Q24": 0.08, "1Q25": 0.08, "2Q25": 0.10, "3Q25": 0.12, "4Q25": 0.20, "1Q26": 0.20, "2Q26": 0.15, "3Q26": 0.14}
g_res = {"1Q24": -0.05, "2Q24": -0.03, "3Q24": 0.06, "4Q24": -0.05, "1Q25": -0.11, "2Q25": -0.09, "3Q25": -0.08, "4Q25": 0.00, "1Q26": -0.12, "2Q26": -0.07, "3Q26": -0.06}

R_TOT, R_GT, R_GC, R_GR = 5, 6, 7, 8
R_ROW, R_RES, R_CLIN, R_SHARE, R_CHK_R, R_CHK_C = 10, 11, 12, 13, 14, 15
R_CHINA, R_CHINA_G = 17, 18

cells = []


def c(cell, value, **kw):
    d = {"cell": cell, "value": value}
    d.update(kw)
    cells.append(d)


c("B2", "Ex-China Sequencing Consumables: Clinical / Research & Applied Split", bold=True, top=True, bottom=True)
c("B4", "$M", bold=True)
for pid, col in cols.items():
    c(f"{col}4", pid.replace("FY", "FY ") if pid.startswith("FY") else pid, bold=True, align="right", bottom=True)

# row 5: total sequencing consumables (model history where it exists, typed 2024 quarters)
c(f"B{R_TOT}", "Total Sequencing Consumables", bold=True)
for pid in q25 + q26 + ["FY2023", "FY2024", "FY2025"]:
    c(f"{cols[pid]}{R_TOT}", "={Revenue Build!seq_cons@" + pid + "}", fmt="amount", bold=True)
for pid, v in tot_sc_24.items():
    c(f"{cols[pid]}{R_TOT}", v, fmt="amount", bold=True)
# rows 6-8: reported growth rates (inputs)
for r, lab, src in ((R_GT, "Ex-China sequencing consumables y/y (reported)", g_tot), (R_GC, "Clinical y/y, ex-China (reported)", g_clin), (R_GR, "Research & Applied y/y, ex-China (reported)", g_res)):
    c(f"B{r}", lab, italic=True)
    for pid, v in src.items():
        c(f"{cols[pid]}{r}", v, fmt="pct_plain", italic=True)
# row 10: ex-China sequencing consumables
c(f"B{R_ROW}", "Ex-China Sequencing Consumables", bold=True)
for pid, v in row_sc.items():
    c(f"{cols[pid]}{R_ROW}", v, fmt="amount", bold=True, fill="E8E8E8")
for pid in q24:
    if pid in row_sc_24:
        c(f"{cols[pid]}{R_ROW}", row_sc_24[pid], fmt="amount", bold=True, fill="E8E8E8")
    else:
        nxt = [k for k, p in prior.items() if p == pid][0]
        c(f"{cols[pid]}{R_ROW}", f"={cols[nxt]}{R_ROW}/(1+{cols[nxt]}{R_GT})", fmt="amount", bold=True, fill="E8E8E8")
for pid in q23:
    nxt = [k for k, p in prior.items() if p == pid][0]
    c(f"{cols[pid]}{R_ROW}", f"={cols[nxt]}{R_ROW}/(1+{cols[nxt]}{R_GT})", fmt="amount", bold=True, fill="E8E8E8")
# row 11: research & applied; row 12: clinical
c(f"B{R_RES}", "Research & Applied Consumables (ex-China)", bold=True)
c(f"B{R_CLIN}", "Clinical Consumables (ex-China)", bold=True)
for pid in q24:
    nxt = [k for k, p in prior.items() if p == pid][0]
    a, b = cols[pid], cols[nxt]
    c(f"{a}{R_RES}", f"=({b}{R_ROW}-{a}{R_ROW}*(1+{b}{R_GC}))/({b}{R_GR}-{b}{R_GC})", fmt="amount", bold=True, fill="E8E8E8")
    c(f"{a}{R_CLIN}", f"={a}{R_ROW}-{a}{R_RES}", fmt="amount", bold=True, fill="E8E8E8")
for pid in q25:
    a, b = cols[pid], cols[prior[pid]]
    c(f"{a}{R_RES}", f"={b}{R_RES}*(1+{a}{R_GR})", fmt="amount", bold=True, fill="E8E8E8")
    c(f"{a}{R_CLIN}", f"={b}{R_CLIN}*(1+{a}{R_GC})", fmt="amount", bold=True, fill="E8E8E8")
for pid in q26:
    a, b = cols[pid], cols[prior[pid]]
    c(f"{a}{R_CLIN}", f"={b}{R_CLIN}*(1+{a}{R_GC})", fmt="amount", bold=True, fill="E8E8E8")
    c(f"{a}{R_RES}", f"={a}{R_ROW}-{a}{R_CLIN}", fmt="amount", bold=True, fill="E8E8E8")
for pid in q23:
    nxt = [k for k, p in prior.items() if p == pid][0]
    a, b = cols[pid], cols[nxt]
    c(f"{a}{R_CLIN}", f"={b}{R_CLIN}/(1+{b}{R_GC})", fmt="amount", bold=True, fill="E8E8E8")
    c(f"{a}{R_RES}", f"={a}{R_ROW}-{a}{R_CLIN}", fmt="amount", bold=True, fill="E8E8E8")
# FY sums for rows 10-12 and the China rows
for fy, qs in fy_of.items():
    a, b = cols[qs[0]], cols[qs[-1]]
    for r in (R_ROW, R_RES, R_CLIN):
        c(f"{cols[fy]}{r}", f"=SUM({a}{r}:{b}{r})", fmt="amount", bold=True, fill="E8E8E8")
# row 13: clinical share; rows 14-15: implied growth checks
c(f"B{R_SHARE}", "Clinical share of ex-China sequencing consumables", italic=True)
for pid, col in cols.items():
    c(f"{col}{R_SHARE}", f"={col}{R_CLIN}/{col}{R_ROW}", fmt="pct_plain", italic=True)
c(f"B{R_CHK_R}", "Research & Applied y/y, implied", italic=True)
c(f"B{R_CHK_C}", "Clinical y/y, implied", italic=True)
for pid, p in prior.items():
    a, b = cols[pid], cols[p]
    c(f"{a}{R_CHK_R}", f"={a}{R_RES}/{b}{R_RES}-1", fmt="pct_plain", italic=True)
    c(f"{a}{R_CHK_C}", f"={a}{R_CLIN}/{b}{R_CLIN}-1", fmt="pct_plain", italic=True)
for fy, pfy in (("FY2024", "FY2023"), ("FY2025", "FY2024")):
    a, b = cols[fy], cols[pfy]
    c(f"{a}{R_CHK_R}", f"={a}{R_RES}/{b}{R_RES}-1", fmt="pct_plain", italic=True)
    c(f"{a}{R_CHK_C}", f"={a}{R_CLIN}/{b}{R_CLIN}-1", fmt="pct_plain", italic=True)
# rows 17-18: Greater China = total - ex-China
c(f"B{R_CHINA}", "Greater China Sequencing Consumables", bold=True)
c(f"B{R_CHINA_G}", "Greater China y/y", italic=True)
for pid in q24 + q25 + q26 + ["FY2023", "FY2024", "FY2025"]:
    col = cols[pid]
    c(f"{col}{R_CHINA}", f"={col}{R_TOT}-{col}{R_ROW}", fmt="amount", bold=True, fill="E8E8E8")
for pid in q25 + q26 + ["FY2024", "FY2025"]:
    p = prior.get(pid) or {"FY2024": "FY2023", "FY2025": "FY2024"}[pid]
    c(f"{cols[pid]}{R_CHINA_G}", f"={cols[pid]}{R_CHINA}/{cols[p]}{R_CHINA}-1", fmt="pct_plain", italic=True)

mix = {"name": MIX, "zoom": 80, "widths": {"A": 2.0, "B": 52.0, "C": 2.0, **{col: 9.5 for col in cols.values()}}, "cells": cells}

# ---- Implied Discounting Build ---------------------------------------------------------------
dcells = []


def d(cell, value, **kw):
    x = {"cell": cell, "value": value}
    x.update(kw)
    dcells.append(x)


d("B2", "Implied Sequencing Consumables Revenue per GB", bold=True, top=True, bottom=True)
d("B4", "Assumed sequencing volume growth y/y (GB)")
d("C4", 0.30, fmt="pct_plain", fill="FFFFCC")
d("B6", "Period", bold=True, bottom=True)
d("C6", "Seq. Consumables Revenue y/y", bold=True, bottom=True, align="right")
d("D6", "Volume Growth y/y", bold=True, bottom=True, align="right")
d("E6", "Implied Revenue per GB y/y", bold=True, bottom=True, align="right")
periods = ["FY2025", "1Q26", "2Q26", "3Q26", "4Q26", "FY2026", "1Q27", "2Q27", "3Q27", "4Q27", "FY2027",
           "1Q28", "2Q28", "3Q28", "4Q28", "FY2028", "FY2029", "FY2030"]
r = 7
disc_rows = {}
for pid in periods:
    est = pid not in ("FY2025", "1Q26", "2Q26", "3Q26")
    lab = (pid.replace("FY", "FY ") if pid.startswith("FY") else pid) + ("E" if est else "")
    fy = pid.startswith("FY")
    d(f"B{r}", lab, bold=fy)
    d(f"C{r}", "={Revenue Build!seq_cons.pct_yoy@" + pid + "}", fmt="pct_plain", bold=fy)
    d(f"D{r}", "=$C$4", fmt="pct_plain", bold=fy)
    d(f"E{r}", f"=(1+C{r})/(1+D{r})-1", fmt="pct_plain", bold=fy, fill="E8E8E8")
    disc_rows[pid] = r
    r += 1

disc = {"name": DISC, "zoom": 90, "widths": {"A": 2.0, "B": 44.0, "C": 30.0, "D": 20.0, "E": 28.0}, "cells": dcells}

# ---- history links of the Revenue Build lines ------------------------------------------------
hist_pids = q25 + q26 + ["FY2023", "FY2024"]
links = {
    "clins_cons": {pid: f"='{MIX}'!{cols[pid]}{R_CLIN}" for pid in hist_pids},
    "research_cons": {pid: f"='{MIX}'!{cols[pid]}{R_RES}" for pid in hist_pids},
    "china_seq_cons": {pid: f"='{MIX}'!{cols[pid]}{R_CHINA}" for pid in hist_pids},
}

# ---- Multiples Build: Tearsheet and DCF multiples implied by target P/E ------------------------
MULT = "Multiples Build"
mcells = []


def mc(cell, value, **kw):
    x = {"cell": cell, "value": value}
    x.update(kw)
    mcells.append(x)


TS_METRIC = {"Blowout": ("E26", "J26"), "Bull": ("E12", "J12"), "Base": ("E5", "J5"), "Bear": ("E19", "J19"), "Disaster": ("E33", "J33")}
PE_TS = {"YE2027": {"Blowout": 45, "Base": 27, "Disaster": 22}, "YE2028": {"Blowout": 45, "Base": 25, "Disaster": 20}}
PE_DCF = {"Disaster": 14, "Bear": 45, "Base": 20, "Bull": 30, "Blowout": 35}
EPS_G_2031 = round(11.01 / 9.50 - 1, 4)   # consensus FY2031 / FY2030 adjusted EPS (Bloomberg, 10 Oct 2026)
mc("B2", "Multiples Implied by Target P/E", bold=True, top=True, bottom=True)
hdr = ["Case", "Target P/E", None, "Equity Value", "(+) Debt & Leases", "(-) Cash & Investments", "Enterprise Value", None, "Implied EV/EBITDA"]
ts_rows = {}
for bi, (blabel, eps_pid, ebitda_pid, r0) in enumerate((("YE2027", "FY2027", "FY2028", 4), ("YE2028", "FY2028", "FY2029", 12))):
    mc(f"B{r0}", f"{blabel} target: P/E on {eps_pid}E Adj. EPS, EV/EBITDA on {ebitda_pid}E Adj. EBITDA", bold=True)
    h = list(hdr); h[2] = f"Adj. Net Income {eps_pid}E"; h[7] = f"Adj. EBITDA {ebitda_pid}E"
    for j, lab in enumerate(h):
        mc(f"{chr(66 + j)}{r0 + 1}", lab, bold=True, bottom=True, align="right" if j else None)
    order = ["Blowout", "Bull", "Base", "Bear", "Disaster"]
    rows = {case: r0 + 2 + i for i, case in enumerate(order)}
    ts_rows[blabel] = rows
    for case, r in rows.items():
        mc(f"B{r}", case)
        if case == "Bull":
            mc(f"C{r}", f"=AVERAGE(C{rows['Base']},C{rows['Blowout']})", fmt="mult")
        elif case == "Bear":
            mc(f"C{r}", f"=AVERAGE(C{rows['Disaster']},C{rows['Base']})", fmt="mult")
        else:
            mc(f"C{r}", PE_TS[blabel][case], fmt="mult", fill="FFFFCC")
        mc(f"D{r}", "={Income Statement!adj_ni@" + eps_pid + "}", fmt="amount")
        mc(f"E{r}", f"=C{r}*D{r}", fmt="amount")
        mc(f"F{r}", "=Tearsheet!$E$44", fmt="amount")
        mc(f"G{r}", "=Tearsheet!$E$43", fmt="amount")
        mc(f"H{r}", f"=E{r}+F{r}-G{r}", fmt="amount", bold=True)
        mc(f"I{r}", f"=Tearsheet!{TS_METRIC[case][bi]}", fmt="amount")
        mc(f"J{r}", f"=H{r}/I{r}", fmt="mult", bold=True, fill="E8E8E8")
r0 = 20
mc(f"B{r0}", "DCF exit: EV/EBITDA on FY2030E Adj. EBITDA implied by P/E on FY2031E Adj. Net Income", bold=True)
mc(f"B{r0 + 1}", "FY2031E Adj. Net Income growth over FY2030E")
mc(f"C{r0 + 1}", EPS_G_2031, fmt="pct_plain", fill="FFFFCC")
h = ["Case", "Target P/E", "Adj. Net Income FY2030E", "Adj. Net Income FY2031E", "Equity Value", "(+) Debt & Leases FY2030E", "(-) Cash & Investments FY2030E", "Enterprise Value", "Adj. EBITDA FY2030E", "Implied Exit EV/EBITDA"]
for j, lab in enumerate(h):
    mc(f"{chr(66 + j)}{r0 + 2}", lab, bold=True, bottom=True, align="right" if j else None)
dcf_rows = {case: r0 + 3 + i for i, case in enumerate(["Disaster", "Bear", "Base", "Bull", "Blowout"])}
for case, r in dcf_rows.items():
    mc(f"B{r}", case)
    mc(f"C{r}", PE_DCF[case], fmt="mult", fill="FFFFCC")
    mc(f"D{r}", "={Income Statement!adj_ni@FY2030}", fmt="amount")
    mc(f"E{r}", f"=D{r}*(1+$C${r0 + 1})", fmt="amount")
    mc(f"F{r}", f"=C{r}*E{r}", fmt="amount")
    mc(f"G{r}", "={Balance Sheet!st_debt@FY2030}+{Balance Sheet!lt_debt@FY2030}+{Balance Sheet!lease_liab@FY2030}", fmt="amount")
    mc(f"H{r}", "={Balance Sheet!cash@FY2030}+{Balance Sheet!st_inv@FY2030}", fmt="amount")
    mc(f"I{r}", f"=F{r}+G{r}-H{r}", fmt="amount", bold=True)
    mc(f"J{r}", "={Income Statement!adj_ebitda@FY2030}", fmt="amount")
    mc(f"K{r}", f"=I{r}/J{r}", fmt="mult", bold=True, fill="E8E8E8")
mult = {"name": MULT, "zoom": 85, "widths": {"A": 2.0, "B": 12.0, "C": 12.0, "D": 26.0, "E": 26.0, "F": 28.0, "G": 32.0, "H": 18.0, "I": 24.0, "J": 26.0, "K": 26.0}, "cells": mcells}
mult_links = {"tearsheet": {b: {case: f"'{MULT}'!J{r}" for case, r in rows.items()} for b, rows in ts_rows.items()},
              "dcf_exit": {case: f"'{MULT}'!K{r}" for case, r in dcf_rows.items()},
              "eps_cells": {"YE2027": {case: f"D{r}" for case, r in ts_rows["YE2027"].items()}, "YE2028": {case: f"D{r}" for case, r in ts_rows["YE2028"].items()}},
              "implied_cells": {"YE2027": {case: f"J{r}" for case, r in ts_rows["YE2027"].items()}, "YE2028": {case: f"J{r}" for case, r in ts_rows["YE2028"].items()},
                                "dcf": {case: f"K{r}" for case, r in dcf_rows.items()}}}

json.dump({"side_builds": [mix, disc, mult], "line_values": {"Revenue Build": links}, "driver_links": {}, "multiples_links": mult_links, "line_subs": {"Margin Build": {"m_tariff_refund": []}, "Revenue Build": {"tariff_refund": ["usd_yoy"]}}}, open(out_path, "w", encoding="utf-8"), indent=1)
print("wrote", out_path, "cells:", len(cells), len(dcells), len(mcells))
