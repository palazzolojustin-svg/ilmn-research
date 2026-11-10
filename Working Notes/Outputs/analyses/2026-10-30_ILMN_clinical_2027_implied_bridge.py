"""Implied Q4'26 and 2027 ex-China clinical consumables growth needed for 8.5% total revenue growth."""
row = {"Q1'24": 642, "Q2'24": 679, "Q3'24": 684, "Q4'24": 640,
       "Q1'25": 640, "Q2'25": 690, "Q3'25": 707, "Q4'25": 713,
       "Q1'26": 687, "Q2'26": 734}
cl = {"Q1'24": .07, "Q2'24": .05, "Q3'24": .11, "Q4'24": .08,
      "Q1'25": .08, "Q2'25": .10, "Q3'25": .12, "Q4'25": .20,
      "Q1'26": .20, "Q2'26": .15, "Q3'26": .14}
ra = {"Q1'25": -.11, "Q2'25": -.09, "Q3'25": -.08, "Q4'25": 0.0,
      "Q1'26": -.12, "Q2'26": -.07, "Q3'26": -.06}
solve = lambda t0, t1, gc, gr: (t1 - t0 * (1 + gr)) / (gc - gr)

# Clinical $ by quarter: 2025 from 2024->2025 deck growth, averaged with 2025->2026 where 2026 deck $ exist
c = {}
for q in ["Q1", "Q2", "Q3", "Q4"]:
    y24, y25, y26 = q + "'24", q + "'25", q + "'26"
    ests = [solve(row[y24], row[y25], cl[y25], ra[y25]) * (1 + cl[y25])]
    if y26 in row:
        ests.append(solve(row[y25], row[y26], cl[y26], ra[y26]))
    c[y25] = sum(ests) / len(ests)
r = {q + "'25": row[q + "'25"] - c[q + "'25"] for q in ["Q1", "Q2", "Q3", "Q4"]}
for q in ["Q1", "Q2", "Q3"]:
    c[q + "'26"] = c[q + "'25"] * (1 + cl[q + "'26"])
    r[q + "'26"] = r[q + "'25"] * (1 + ra[q + "'26"])
fy25_c = sum(c[q + "'25"] for q in ["Q1", "Q2", "Q3", "Q4"])
ytd_c = sum(c[q + "'26"] for q in ["Q1", "Q2", "Q3"])
print("2025 clinical $", {k: round(v) for k, v in c.items()}, "FY25", round(fy25_c))
print("Q3'26 RoW consumables implied", round(c["Q3'26"] + r["Q3'26"]))

# Q4'26 implied clinical, method A: FY26 clinical at 14/15/16%
print("\nMethod A (FY clinical guide):")
for g in (.14, .15, .16):
    q4 = fy25_c * (1 + g) - ytd_c
    print(f"  FY {g:.0%}: Q4 ${q4:.0f}M, {q4 / c['Q4\'25'] - 1:+.1%}")
# Method B: Q4 RoW consumables +5-6% (Dhingra), R&A -6% like Q3
print("Method B (Q4 consumables guide, R&A -6%):")
for gt in (.05, .055, .06):
    tot = row["Q4'25"] * (1 + gt); rq = r["Q4'25"] * 0.94
    print(f"  cons {gt:+.1%}: Q4 clinical ${tot - rq:.0f}M, {(tot - rq) / c['Q4\'25'] - 1:+.1%}")

# Base case Q4'26: RoW consumables +5.5%, R&A -6%
r["Q4'26"] = r["Q4'25"] * 0.94
c["Q4'26"] = row["Q4'25"] * 1.055 - r["Q4'26"]
q4g = c["Q4'26"] / c["Q4'25"] - 1
fy26_c = sum(c[q + "'26"] for q in ["Q1", "Q2", "Q3", "Q4"])
fy26_r = sum(r[q + "'26"] for q in ["Q1", "Q2", "Q3", "Q4"])
fy25_r = sum(r[q + "'25"] for q in ["Q1", "Q2", "Q3", "Q4"])
print(f"\nBase Q4'26 clinical {q4g:+.1%}; FY26 clinical ${fy26_c:.0f}M {fy26_c / fy25_c - 1:+.1%}; R&A ${fy26_r:.0f}M {fy26_r / fy25_r - 1:+.1%}")

# 2026E revenue build (ex-tariff refunds), $M
total26 = 4650.0                         # guide midpoint $4.64-4.66B
china26 = 52 + 56 + 56 + 50              # YTD est + Q4 ~50 -> within $210-220M guide
instr26 = 114 + 122 + 102 + 122          # RoW seq instruments; Q4 ~Street Q4 less China
other26 = total26 - china26 - fy26_c - fy26_r - instr26   # RoW services, microarray, SomaLogic, other
print(f"2026E: total {total26:.0f}, China {china26}, clin {fy26_c:.0f}, R&A {fy26_r:.0f}, instr {instr26}, other {other26:.0f}")

# Street 2027 growth rates (Bloomberg consensus, 10 Oct 2026, pre-Q3)
g_instr = 453.65 / 482.62 - 1
g_china = 189.22 / 210.72 - 1
g_other = (4918.25 - 3378.44 - 453.65) / (4624.80 - 3104.44 - 482.62) - 1
print(f"Street 27 growth: instr {g_instr:+.1%}, China {g_china:+.1%}, services/microarray/other {g_other:+.1%}")

def needed(total_g=.085, ra_g=0.0, china_g=g_china, instr_g=g_instr, other_g=g_other):
    t27 = total26 * (1 + total_g)
    rest = fy26_r * (1 + ra_g) + china26 * (1 + china_g) + instr26 * (1 + instr_g) + other26 * (1 + other_g)
    c27 = t27 - rest
    return c27, c27 / fy26_c - 1

c27, g27 = needed()
print(f"\nBASE 2027: total ${total26 * 1.085:.0f}M; clinical needed ${c27:.0f}M -> {g27:+.1%}")
print("Sensitivity, total growth x R&A growth:")
for tg in (.07, .08, .085, .09):
    print(f"  total {tg:.1%}: " + ", ".join(f"R&A {rg:+.0%} -> {needed(tg, rg)[1]:+.1%}" for rg in (-.05, 0, .03)))
print(f"China flat instead of Street: {needed(china_g=0)[1]:+.1%}")
print(f"Instruments flat instead of Street: {needed(instr_g=0)[1]:+.1%}")
print(f"Other +8% (multiomics 1-2pt mgmt) instead of Street: {needed(other_g=.08)[1]:+.1%}")
# Street-implied clinical: Street seq consumables +8.8% with R&A flat
print(f"Street seq consumables 27 growth {3378.44 / 3104.44 - 1:+.1%}")
print(f"Street total $4,918M (+{4918.25 / total26 - 1:.1%}) -> clinical {needed(total_g=4918.25 / total26 - 1)[1]:+.1%}")
print(f"Clinical at 2yr-stack 26 (=+{.26 - fy26_c / fy25_c + 1:.1%}): total growth = ", end="")
cg = .26 - (fy26_c / fy25_c - 1)
t27 = fy26_c * (1 + cg) + fy26_r + china26 * (1 + g_china) + instr26 * (1 + g_instr) + other26 * (1 + g_other)
print(f"{t27 / total26 - 1:+.1%}")
