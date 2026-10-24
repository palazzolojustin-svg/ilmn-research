# Agent 18: Over-earning and price/volume model

*Model: sonnet. Run 2026-10-11 12:15:48. Cost $0.81 (API-equivalent).*

**Assignment:** Using ALL findings files listed below, build an explicit, transparent model answering both thesis questions. (1) Over-earning: size the remaining NovaSeq 6000 consumables revenue (total HT and clinical-only; use pull-through x installed base, X-share data, and any HT revenue base), the per-Gb price ratio X/6000 (triangulate management's 60-70%, CFO's ~25% annual, price-list data), and the revenue lost if that volume converts at constant Gb, over what timeline (2026-2028). (2) Offset: required clinical Gb growth to offset conversion plus ongoing price declines (35B, competition), versus evidence-based Gb growth (test growth x intensity from agents 09-13). Produce low/base/high scenarios for 2026-2028 clinical sequencing consumables revenue growth and the 'excess earnings' at risk, with every assumption sourced or labeled. Include sensitivity tables (e.g. price ratio vs Gb growth). Compare with consensus sequencing consumables (+5.6% 2026, +8.8% 2027, +9.4% 2028) and management's clinical mid-teens guide. Be explicit about what is unknowable and which single numbers would change the answer.

## Key findings

1. **OPINION (my model, built on ledger inputs):** about **$500M of FY26 clinical sequencing consumables (~23% of the ~$2.17B total, ~16% of all FY26 consensus consumables) is "excess" revenue.** I define excess as revenue the clinical NovaSeq 6000 Gb earn above what the same Gb would earn at X prices. Clinical 6000 revenue is ~$710M a year (~$182M a quarter, from agent 45 and E187). The revenue-implied 6000/X price ratio is 3.39x (-70.5%), so $710M × 70.5% ≈ $500M. It is not all "at risk" at once. It unwinds at the speed of conversion.

2. **OPINION:** each 10 points of clinical Gb that moves from the 6000 to the X costs ~$240M a year at constant 2026 Gb. That is ~$24M per point, which matches agent 45's ~$36M per point for total HT scaled by the ~64% clinical share of HT Gb. At the 2027 Gb level (+30%) and a post-35B X price, it is ~$31–33M per point.

3. **OPINION:** base-case clinical sequencing consumables grow **+4% in 2027 and +6% in 2028**, against **+15% in 2026**, which is management's mid-teens guide and an H1 run-rate of ~17%. The bear case is -10% in 2027 and -3% in 2028. The bull case is +19% in 2027 and +17% in 2028. Weights of 25/50/25 give about +4% (2027) and +7% (2028).

4. **OPINION:** consensus total sequencing consumables (+8.8% in 2027, +9.4% in 2028) need clinical consumables of roughly +13–14% a year. This assumes research and other grow 0 to -3%. Under base-case price and mix, that requires clinical Gb of about +47% in 2027 and +38% in 2028. Under bull-case price and mix it still requires +32% in 2027. Even if trailing Gb (+40%) persists with base price and mix, I get total sequencing consumables of about +6% in 2027, below +8.8%. The probability-weighted total is about +2.4% in 2027 and +4.9% in 2028. Consensus looks closer to a bull case than a central case. Treat that with caution, because the trailing data say my base Gb may be too low (finding 5).

5. **FACT/OPINION:** trailing clinical Gb growth is high. Backing out Gb from revenue gives about +40–42% central, with a defensible range of +35–50% (agent 52, E205 revised). Management said at JPM on 13 Jan 2026 that "clinical sequencing volume growth above 30%". Agent 140's backtest found its own central case under-predicted Q2'26: the model implied HT +1% q/q, and the actual was +6.8%. My base uses +30% and +26% for 2027 and 2028. That is a deliberate deceleration, not a continuation of the trailing rate.

6. **OPINION:** the price/volume arithmetic is brutal on the conversion step alone. With X $/Gb flat, moving clinical X volume from 79% to 87% in a year cuts revenue by 12.7% at constant Gb. Break-even Gb growth for that step alone is +14.6% at the observed 3.39x ratio, and +21% if the ratio is 5x. The 35B and residual X price declines come on top.

7. **FACT/MGMT:** the FY26 platform guides already imply a steep 6000 decline in H2'26. The guide is $600–650K pull-through on an average 6000 base of ~1,270. That implies full-year 6000 revenue of $0.76–0.83B. H1'26 was ~$444M, so H2 is $138–200M a quarter, against $219M in Q2 (agents 45 and 52). Part of the "over-earning" unwind is therefore already guided. Q3'26 6000 revenue is the first test.

8. **OPINION:** there is a tension between the X pull-through guide and consensus. The guide of $1.35–1.40M needs H2 annualized pull-through of ~$1.46–1.55M, against ~$1.24M in Q2'26 and ~$1.21M in H1. Consensus is coherent with the guides only at the low ends (agent 52 §4, agent 45).

9. **OPINION:** the Q2'26 83%/59% split measures capacity shipped, not consumed. Illumina's transition slides call it "% of HT Gb *Shipped*" (E204). If 6000 customers consume fewer Gb than they buy, the true price ratio is understated, and excess earnings could be larger or smaller than I show.

10. **FACT:** the 35B is not orderable. Illumina's roadmap puts the 14B and 35B in **H1 2027**, and the NovaSeq X order page (11 Oct 2026) lists no 35B or 14B kit (agent 144). The "~Jan 2027" timing in the brief rests on hearsay (E058). The ~20% price cut is also hearsay: a former associate director said "about $2 flat" from ~$2.50/Gb. No broker models the 35B price (agent 124).

11. **OPINION:** the HiSeq→NovaSeq analog says volume did not offset price within the blend, and the tail was long. In 2019, NovaSeq consumable shipments almost doubled and total data was +50%, but total consumables grew only +14%, which is about -24% revenue per Gb (agent 110). About 1,000 HiSeq units were still active four years after launch (end-2020), and 320 of 850 customers had not begun transitioning. This supports a sticky 6000 tail (~15–20%) running past 2028.

12. **Not knowable from the corpus:** net $/Gb by platform, the clinical share of HT Gb, the 35B's price and scope, the number of dual-running customers, and Q3'26 6000 pull-through. Ranked sensitivities are in "What would change the answer".

---

## 1. Model specification (transparent)

**Structure.** I model clinical HT consumables as Gb × a mix-weighted price, and add clinical non-HT consumables separately.

- Let G be the clinical HT Gb index, set to 1.00 at the 2026 midyear anchor (Q2'26 run-rate).
- Let x be the year-average share of clinical Gb on the X. x = 0.79 in 2026.
- Let P_x be the X $/Gb index, 1.00 in 2026. The 6000 $/Gb is 3.39 in the same units.
- Clinical HT revenue index = G × [x·P_x + (1−x)·3.39] ÷ 1.5019.
- The denominator is the 2026 value, 0.79 + 0.21×3.39 = 1.5019.

**Calibration (FACT inputs, OPINION derivation).**

| Input | Value | Source |
|---|---|---|
| Q2'26 HT revenue | $535M (X $316M, 6000 $219M) | A45 §A, E040 |
| X share of HT revenue / Gb | 59% / 83% | brief |
| Revenue ratio r = (0.59/0.83)/(0.41/0.17) | 0.295, so the 6000 earns 3.39x per Gb (X is 70.5% lower) | A45 §A, E187 |
| Rounding band on r | 0.279–0.312 (3.2–3.6x) | A140 §1 point 5 |
| Clinical HT Gb weight | ~64% (range 55–75% revenue share tested) | A45 §C, E009 |
| Clinical X volume / revenue share | 78% / 51% | A45 §C |
| Clinical HT revenue | ~$372M a quarter (~$1.49B annualized) | calc |
| Clinical 6000 revenue | ~$182M a quarter (~$728M annualized) | calc, E187 |

The formula is clinical 6000 = s × 535 × (1 − 0.511), with s the clinical share of HT revenue. s is 55%/65%/75% in agent 45's sensitivity; I use ~69.5%.

**Clarification of agent 45's "clinical tail ~34%".** That is the clinical 6000 as a share of *total* HT revenue ($182M ÷ $535M). As a share of *clinical* HT revenue it is **49%**. I checked the arithmetic: clinical X volume of 78% and r = 0.295 give an X revenue share of 51.1%.

**Dollar anchors (assumptions marked).**

- FY25 sequencing consumables: $2,939M (FACT).
- Clinical share of FY26 consumables: ~70%. This is my derivation. Management says ">65%" and an ex-employee called the classification "very loose". Consensus FY26 of $3,104M (+5.6%) with clinical +15% and research -7% implies ~70%.
- FY26 clinical consumables: ~$2.17B (OPINION).
- Clinical HT share of clinical: ~69%, so HT is ~$1.50B and non-HT ~$0.67B.
- Cross-check: FY26 clinical 6000 revenue is ~$710M. Total FY26 6000 revenue implied by the guide is $0.76–0.83B. Research 6000 is ~$172M a year at Q2 run-rate. The sum is slightly above the guide. This is an unresolved ~$50–100M discrepancy.

**Price-ratio triangulation (the "60–70%" check).**

| Evidence | Implied X vs 6000 per-Gb price | Source |
|---|---|---|
| Revenue/volume share arithmetic, Q2'26 | -70.5% (band -69% to -72%) | A45, A140 |
| MGMT (CFO, Q2'24) | "easily more than 60% to 70%" | E030 |
| Illumina list claim (2022 launch) | up to -59% vs S4 ($2.00/Gb vs ~$4.9/Gb) | A11 #11 |
| Core facility median, S4 → 25B | -53% (Salk, same list: -60%) | A11 #1 |
| Core facility, S4 → 10B | -35% | A11 #2 |
| Core facility, S1/S2 → 25B | -78% to -82% | A11 #4 |
| Large clinical accounts (hearsay) | pay "half or a quarter" of core rates | E113 |

The revenue-implied figure (-70%) sits above the S4-based list evidence (-53% to -60%). The likely reasons are a 6000 base weighted to S1/S2 flow cells and the capacity-versus-consumption issue. Earlier quarters do not reconcile to a stable r (E030).

**CFO's ~25% annual price decline (Nov 2024) and management's mid-teens model.** Q3'24 volume was +40% and consumables revenue +5%, "largely price". Agent 45 decomposes mid-teens into three layers: tail conversion ~6–7%, the 35B ~4% and residual repricing ~4%. I treat the mix effect and X price separately, so my total price drag (-21% in the 2027 base) is harsher than management's mid-teens. That reflects the 35B and a faster clinical conversion.

---

## 2. Scenarios, 2026–2028

**Assumption table.** All are OPINION unless a source is given. "Source" names the anchor.

| Parameter | Bear | Base | Bull | Anchor |
|---|---|---|---|---|
| Clinical Gb growth 2027 / 2028 | +15% / +12% | +30% / +26% | +40% / +32% | A52 low +15/+10, base +27/+24, high +38/+32; trailing +35–50%; JPM Jan 2026 ">30%"; JPM survey volume +14.6%/+19.1% (E067) |
| Year-avg clinical X Gb share 2026 / 2027 / 2028 | 79 / 89 / 94% | 79 / 87 / 93% | 79 / 84 / 88% | Mgmt target 80–85% by end-2026 (Q4'25 and Q2'26 calls); agent 45 phasing 25/60/80% of remaining 6000 converted by end-2026/27/28; E012 ~20% sticky |
| X $/Gb index 2027 | 0.792 | 0.855 | 0.92 | Residual -10%/-5%/-3% × 35B (-20% on 60%/50%/25% of X Gb) |
| X $/Gb index 2028 | 0.729 | 0.812 | 0.894 | Further -8%/-5%/-3% (competition, residual) |
| Clinical non-HT growth | +5% | +8% | +12% | Pure assumption (NextSeq 1k/2k ~$90K pull-through) |
| 2026 clinical growth | +13% | +15% | +17% | Guide mid-teens; H1 ~17%; H2 implied ~13–14% |

**Results on clinical HT revenue** (index vs 2026 = 1.00).

| | 2027 | 2028 |
|---|---|---|
| Bear | 0.825 | 0.762 |
| Base | 1.025 | 1.082 |
| Bull | 1.227 | 1.469 |

Example, base 2027: R = 0.87×0.855 + 0.13×3.39 = 1.1846; revenue = 1.30 × 1.1846 ÷ 1.5019 = 1.025.

**Total clinical sequencing consumables** (FY26 base $2.17B; HT $1.50B plus non-HT $0.67B).

| Case | 2027 $M (y/y) | 2028 $M (y/y) |
|---|---|---|
| Bear | 1,942 (-10.5%) | 1,882 (-3.1%) |
| Base | 2,262 (+4.2%) | 2,406 (+6.4%) |
| Bull | 2,591 (+19.4%) | 3,043 (+17.4%) |
| 25/50/25 weighted | +4.3% | +6.8% |

**Implied total sequencing consumables vs consensus.** I assume non-clinical consumables of -4%/-2%/0% in 2027 and -2%/0%/+2% in 2028 (bear/base/bull). That is an assumption, with research -7% in Q2'26 as the only anchor.

| | 2027 | 2028 | Consensus |
|---|---|---|---|
| Bear | -8.6% | -2.8% | |
| Base | +2.3% | +4.6% | 2027 +8.8% ($3,378M); 2028 +9.4% (~$3,695M) |
| Bull | +13.6% | +13.3% | |
| Weighted | +2.4% | +4.9% | |
| Base Gb +40% (trailing persists) | ~+6% | n/a | |

**Reading the comparison.**

- Consensus implies clinical of roughly +13–14% a year.
- Against management, the clinical mid-teens guide covers 2026 only. The corpus has no explicit 2027 clinical guide. Agent 124 notes management framed 2027 revenue as "HSD" (high single digit), and JPM's FY27 revenue of +9.1% is above that.
- Agent 140's independent hand model also landed well below consensus (FY27 consumables ~$2.9B vs $3,378M). It then backtested badly, because it under-predicted Q2. So the direction (consensus is demanding) agrees across my work and agent 140's, but the level is uncertain.

**Excess earnings at risk** (OPINION). These are the 6000 revenue dollars lost to conversion at constant 2026 Gb. I take $501M of excess (FY26) and multiply by the share of the 6000 tail that has converted by each year-average.

| Case | Share of 6000 Gb converted, 2027 / 2028 | Excess revenue unwound, 2027 / 2028 |
|---|---|---|
| Bear | 48% / 71% | ~$240M / ~$356M |
| Base | 38% / 67% | ~$190M / ~$336M |
| Bull | 24% / 43% | ~$120M / ~$215M |

- Excess unwound in the base case runs ~$165–190M a year, which is ~8% of FY26 clinical consumables. That is a drag clinical Gb growth must absorb every year, before any X price cut.
- The profit pool is more concentrated than the revenue pool (agent 108). I make the 6000 about 22–24% of Q2'26 core gross profit and 67–71% of core operating income, at an assumed 80–85% 6000 margin. These are derived numbers, not reported ones.
- Full conversion of total HT at -60% to -70% and +30% Gb costs EPS about $1.75–2.63 a year on a $5.24 annualized base. The clinical share is roughly two-thirds of that.
- Agent 108 found no measurable erosion in implied consumables margin once tariffs are added back (r ≈ -0.16, n = 6). Raw margin fell ~3.8 points to ~75% in Q2'26. The bounds rest on an assumed 40% instrument margin.

---

## 3. Offset: required vs evidence-based Gb growth

**Required clinical Gb growth to hold clinical HT revenue flat** (OPINION; formula 1 ÷ price factor − 1).

| Scenario | Break-even Gb |
|---|---|
| Mix only, clinical X 79% → 87%, X price flat | +14.6% |
| Mix only, X 79% → 87%, plus 35B at 50% scope and -5% residual (base 2027) | +26.8% |
| Mix only, X 79% → 94%, with bear price path (2-year) | ~+24% |
| Management's mid-teens price alone | +17.6% |
| Mid-teens plus the full 35B -20% | +47% |
| Agent 52 two-year view: 90% X plus 35B plus a further -10% competitive cut | +24% CAGR |
| Same, but 35B on all X | +28% CAGR |

Agent 52's 2-year table (Table 3, scenarios A–G) puts break-even between 4% (residual only) and 28%.

**Sensitivity 1: 2027 clinical HT revenue growth, Gb growth vs X price change.** Mix: x = 0.87 (from 0.79). Prices apply to X only.

| Clinical Gb growth | X price 0% | -8% | -14.5% (base) | -21% |
|---|---|---|---|---|
| +15% | +0.4% | -5.0% | -9.3% | -13.6% |
| +25% | +9.1% | +3.3% | -1.4% | -6.1% |
| +30% | +13.5% | +7.4% | +2.5% | -2.4% |
| +35% | +17.8% | +11.6% | +6.5% | +1.4% |
| +40% | +22.2% | +15.7% | +10.4% | +5.1% |
| +50% | +30.9% | +24.0% | +18.3% | +12.7% |

**Sensitivity 2: one year of conversion (clinical X 79% → 87%), X price flat, price ratio vs Gb growth.** The ratio is how many times more the 6000 earns per Gb.

| Gb growth | 2.5x (r 0.40) | 3.39x (r 0.295) | 4x (r 0.25) | 5x (r 0.20) |
|---|---|---|---|---|
| +15% | +4.5% | +0.4% | -1.9% | -5.0% |
| +25% | +13.6% | +9.1% | +6.6% | +3.3% |
| +35% | +22.7% | +17.8% | +15.1% | +11.5% |
| +45% | +31.8% | +26.5% | +23.7% | +19.8% |
| Break-even Gb | +10% | +14.6% | +17.3% | +21% |

The sensitivity is moderate. Going from 3.39x to 5x costs about 5 points of revenue growth for a given Gb rate. The Gb growth rate matters more than the ratio. The rounding band on r (3.2–3.6x) changes growth by less than 1 point.

**Sensitivity 3: net clinical growth, Gb growth vs a single blended price decline** (agent 76). Net growth = (1+Gb)(1−price) − 1.

| Gb growth | -10% | -15% | -20% | -25% |
|---|---|---|---|---|
| +20% | +8% | +2% | -4% | -10% |
| +30% | +17% | +10.5% | +4% | -2.5% |
| +40% | +26% | +19% | +12% | +5% |

**Evidence-based Gb growth, by input.**

| Input | Evidence | Direction for Gb | Source |
|---|---|---|---|
| Trailing revenue-implied clinical Gb | +35–50%, central ~+42% | High | A52 §2b–c (calc from E205) |
| MGMT clinical volume | ">30%... for a while"; ~25% for the whole business long-term | High, decelerating | JPM, 13 Jan 2026, per A52 #6 |
| Bottom-up category model (E083) | +23% base, range +10% to +35% | Mid; but A52 re-ran it on Q2'26 prints and got ~+31% (+33–34% with Gb weights) | A13, A52 §2a |
| Customer test growth Q2'26 | Natera clinical MRD 283K, +56%; Guardant oncology ~104K, +63%; Reveal >100%; Shield ~66K, ~4x; GeneDx exome/genome 30,785, +32%; Caris cases +18% (revenue +45%); Tempus oncology +31%; Adaptive 36,111, +43%; BillionToOne +35%; GRAIL ~61K, +35%; Natera total +22% | High, but mostly low-Gb tests | A13, A138, A52 |
| Intensity | NIPT ~1–2 Gb; exome ~8; genome ~100 (12–15x exome); tissue CGP ~15; liquid CGP ~120 (likely too high, per A138); tumor-informed amplicon MRD <1; WGS MRD ≥250 | Mix-dependent | A13 (estimates), A138 flag |
| Mix-shift tailwind | Illumina WGS MRD kit: early access May 2026, global launch 2027 | Upside, after 2027 | A13 #3 |
| Forward customer plans | JPM survey of 32 clinical respondents: volume +14.6% (2027), +19.1% (2028); spend +9.4%, +14.0% | Low | E067, A52 §2e |
| Coverage catalysts | NCCN bladder ctDNA-MRD (23 Jun 2026); colon/rectal still prognostic only | Positive, slow | A125 |

**Where the Gb growth gap comes from** (A52 §2c, OPINION). E083 (+23%) is a forward forecast. E205 (+35–60%) is trailing. They are different quantities. Management's own ">30%" is a connected-instrument, ex-China figure for all HT, and it is a floor. Agent 52 argues for +35–50% trailing, with the +60–65% end overreaching.

**Why test growth overstates Gb growth.** The fastest-growing clinical tests are low-intensity. Signatera is multiplex-PCR on ~16 variants (well under 1 Gb per draw, A13). Roche's AXELIOS and Element are aimed at shallow tests, where a Natera associate director said they would take share (NIPT, transplant, infectious disease; A13 #4). The deep tests (CGP, WGS) are stickier.

**Bottom-up cannot be validated.** Agent 52 estimated named customers account for ~10 Pb a quarter against ~106 Pb top-down clinical Gb, so under 10–15% coverage. Agent 138 got similar results. Either per-test intensities are too low for the big oncology names, or most Gb sits with unnamed labs. I cannot test E082 against any customer's reported sequencing cost per test (agent 128: no customer-company filings in the corpus).

**Competition and price layers.**

- **35B (MGMT/hearsay).** About 20% lower $/Gb, per one former Illumina associate director. UBS's expert put the genome price at ~$150 vs ~$200 (agent 76) or vs ~$175 (agent 140). Those two agents disagree on the base price; this is unresolved. Thaysen declined to price it (TD Cowen, 3 Mar 2026) and said "aggressive pricing brings aggressive volume growth". A 20% price cut requires +25% Gb to be revenue-neutral on the X base alone.
- **AXELIOS (FACT):** $150/genome list, ~$750K instrument. Illumina's effective price is $125–175 and its list is ~$200. A 20% cut brings list to ~$160, near parity. It is not like-for-like (agent 76 on E068).
- **Bargaining power.** Natera's supply agreement has a clause that "price per Gb shall not increase" for new products (E212, per agents 52 and 76). An ex-employee said the top 10–20 customers are "a very large proportion of the business" (agent 128). Illumina's 10-Ks report no customer above 10% of revenue through FY25 (A52 §5). Large accounts therefore have the leverage and the contractual structure to force the 35B cut through, which means the price cut is closer to mandatory than discretionary.
- **JPM's view.** Its survey implies a pricing gap of only 2.4–5.2 points, "smaller than the '-DD%' pricing pressure". It also says planned volume grows 2.4–5.2 points faster than planned spend. JPM sees headwinds "largely gone exiting this year". That implies a clinical price decline of ~4–5%, which A52 §2c calls not credible during a 25-point conversion year.

**Parallel running (Jefferies question, Q2'26).**

- FACT: Thaysen attributed the sequential clinical slowdown to "ins and outs" in the Middle East and Latin America. He did not size the dual-running economics (E014).
- MGMT, Q2'26 call: "some customers bought a few 6000s this quarter to continue operations". More than 10 6000s were sold.
- FACT: in the JPM survey, 24 of 32 clinical respondents own a 6000 and 17 own an X. By the pigeonhole principle at least 9 own both and at most 17, which is **37.5–71% of clinical 6000 owners** (agents 45 and 52, n = 32, a count and not revenue).
- OPINION: if all 6000 revenue at dual-owner labs moved to existing X capacity, the loss would be ~$195–364M a year on total clinical 6000 revenue of $728M (agent 45 §D). That loss is a subset of full conversion and needs no new placements.
- Utilization-drop sensitivity (total HT): a 10/20/30% fall in 6000 utilization moves ~$62M/$124M/$185M a year (2.0/4.0/6.0% of FY26 consumables).
- Hearsay: a Roche lead said NHS-embedded labs "typically have the vendor-recommended instrumentation plus a second Illumina sequencer" (agent 128).
- Management said in the Q4'25 call that customers keep the 6000 "for validated, traditional assays, so pull-through stays up" (agent 140). That is an admission of the dual-running behavior that the Q2'26 answer avoided.

---

## 4. What would change the answer

Ranked by the revenue effect on 2027 base clinical consumables (~$2.26B).

| Rank | Number | Sensitivity (OPINION) |
|---|---|---|
| 1 | **35B scope and size.** Does -20% apply to all X Gb or only new/25B volume? | Base X price 0.855 vs 0.95 (no 35B) is ~$107M of HT revenue (~4.9% of clinical). Agent 140 puts it at -$77M to -$306M of total consumables. Agent 45 puts it at $63M/$127M/$253M for 25/50/100% adoption. |
| 2 | **Clinical Gb growth, 2027.** | ±5 points ≈ ±$59M HT (≈ ±2.7% of clinical). The gap between +23% and +42% is worth ~$250M. |
| 3 | **Pace of clinical 6000 → X conversion.** | ±1 point of Gb moved ≈ $24M at constant Gb, ~$31–33M at 2027 volumes. 40% vs 80% conversion by Q4'27 is ±$97M (agent 140, total). |
| 4 | **Whether mid-teens already includes the 35B.** | If yes, my 35B layer double-counts and the base is understated. If no, mid-teens understates the headwind. |
| 5 | **True consumed-Gb price ratio.** | Rounding alone (3.2–3.6x) moves less than 1 point of growth. A 5x ratio costs ~5 points a year. |
| 6 | **Clinical share of HT Gb** (assumed 64%, tested 55–75%). | Changes the clinical 6000 dollars from $144M to $196M a quarter (agent 45 §C), a ±15% swing in the excess-earnings figure. |
| 7 | **Q3'26 numbers (29 Oct 2026).** | 6000 revenue vs $219M; X pull-through vs $1.21–1.24M; ex-China clinical growth vs 13–16% in line (agent 76), below 12% weak; X revenue share vs 60–62% expected; clinical X volume share vs 79–80%; whether the $1.35–1.40M and $600–650K guides survive. |

Q3 consumables of $789M is the consensus (agent 52). The extra week is in Q4, not Q3 (Q2'26 call l.328). Q4 consensus of $815M may be flattered by ~$23M at the "0.5 point" management figure, or ~1/13 of Q4 consumables (7.7%) on simple arithmetic. That discrepancy is unresolved.

**Management behavior relevant to over-earning** (brief item (a), only what bears on this model).

- **Metric labeled "% of HT Gb Shipped" (E204).** The Q2'26 83%/59% split is capacity shipped, not Gb consumed. That limits all of the above.
- **Disclosure retreat (E020, FACT/OPINION).** The 6000 and X installed bases and decommission counts were last given at Q4'25. The FY26 pull-through guides were in the Q4'25 deck and not updated in the Q1/Q2 decks, so a silent drop in Q3 would be a signal.
- **Language arc (agent 140).** In February the "blended consumables still face headwinds"; in April the "price headwind is receding"; in July the 6000 is "not a true headwind". Over the same period the 6000 stayed at 41% of HT revenue and the implied ratio stayed near 0.30.
- **Tariff bp bridge dropped.** Management gave it for Q2–Q4'25 (110/220/205 bp), then dropped it from Q1'26 (agent 108). That prevents clean margin attribution for the two quarters that matter.
- **"Reduced pricing" as a margin driver** appeared once, in the Q1'25 10-Q, then disappeared as tariffs became the stated cause while X share kept rising (agent 108, OPINION).
- **Deferred compensation.** About 60 bp of deferred compensation sits in Q2'26 opex, and management cited "about 23% excluding the deferred compensation effect" against a reported 22.5% (agent 108). It is a presentation choice, EPS-neutral.

---

## Contradictions and stale data

- **35B timing.** The brief says ~Jan 2027. Illumina's roadmap says H1 2027, and the order page lists no 35B (agent 144, 11 Oct 2026). The price cut size is hearsay only.
- **UBS base price.** Agent 76 has the cut from ~$200 to ~$150 per genome; agent 140 has it from ~$175. I did not resolve this.
- **Clinical tail definition.** Agent 45 §C says the clinical tail is "~34% of clinical HT revenue". It is 34% of *total* HT revenue and ~49% of clinical HT revenue (my recomputation).
- **Agent 45's X revenue.** The ledger E041/E210 figure (~$1.2B, year-end base) is overstated. On average bases X is ~$1.03B.
- **E083 (+23%) vs E205 (+35–60%).** Different time bases. Agent 52 narrows E205 to +35–50% and lifts E083 to ~+31% on Q2'26 prints. Neither is cohort data.
- **Agent 76's one-year view vs mine.** Agent 76 finds clinical ex-China growth of +15% in Q2'26 implies Gb of +35–38% at a -15% price decline. My model implies ~+40% at flat X price. They agree to within the rounding.
- **JPM survey ownership.** "58% own an X" is the all-respondent share (36 of 62). Clinical respondents are 17 of 32 (53%).
- **Net clinical price decline.** The JPM survey implies -4–5%; revenue-implied and list data imply far more. They cannot both hold.
- **Direction of the "ratio uptick".** The move from 0.27 to 0.30 that Barclays and agent 05 read is inside rounding (agent 140).
- **E138** in the ledger was unreadable to agent 140.

## Gaps / what I could not find

- **No customer-company data in the corpus.** There are no Natera, Guardant, Tempus or similar extracts, so no customer-level bottom-up or concentration figure exists (agent 128). Agent 138 could not open the FDA SSEDs or Natera/Guardant PDFs, so every Gb per test is an estimate.
- **No sourced net X $/Gb,** and no Illumina list prices (behind a login). All absolute $/Gb figures are core-facility proxies that include labor and overhead.
- **No count of clinical 6000s or of dual-running customers,** and no revenue-weighted dual-owner share.
- **No sourced clinical share of HT Gb.** I used ~64–70%.
- **No sell-side model line for the 6000, X $/Gb or the 35B.** Brokers are compared only through implied growth.
- **No 2027 or 2028 management guide for clinical.** I used consensus and the "HSD" framing for comparison.
- **Q3'26 6000 pull-through and X bases.** Neither is disclosed after Q4'25. This resolves findings 7–8.
- **Non-HT clinical and research growth assumptions** are mine and only loosely anchored.
- **The model holds the 6000 $/Gb flat** while list prices fell 16–24% on core lists (A11 #6). Any 6000 repricing is additive to the downside.
- **Elasticity.** No disclosed volume-versus-price data exist to test whether price cuts raise Gb. The 40 "fully converted" clinical customers show revenue flat to under +5% in year 1, which at a -60–70% cut needs converting Gb of ~2.4–3.3x (agent 76). That is only credible if the volume is mostly incremental (new assays, exome to genome), not like-for-like workload.
