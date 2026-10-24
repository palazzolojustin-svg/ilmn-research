# Agent 45: 45-internal-HT-revenue-at-risk-bridge-and-scenarios

*Model: sonnet. Run 2026-10-11 03:12:50. Cost $0.47 (API-equivalent).*

**Assignment:** Build a quantified, auditable bridge from the local corpus only (Core Notes, Extracts/ILMN earnings calls, decks, 10-Qs/10-Ks, expert calls, consensus). Do NOT re-collect facts already in the ledger. Steps: (1) Using the known X/6000 share of HT revenue and Gb volume by quarter (Q2'24 to Q2'26), FY25 pull-through ($1.35M X, $670K 6000), installed bases (~970 X, ~1,360 6000 at Q1'26) and FY25 sequencing consumables ($2,939M), solve for implied $/Gb on X vs 6000 by quarter and implied HT revenue $ by platform; check consistency with the 'more than 60-70%' per-Gb price drop and flag any quarter where the numbers do not reconcile. (2) Split HT revenue into clinical vs research using the >65% clinical claim and the 78% clinical / 92% research X-volume shares; derive the implied clinical 6000 revenue $ and its share of total sequencing consumables. Show sensitivity at 55/65/75% clinical share. (3) Scenarios for the remaining 6000 volume converting to X by end-2026, end-2027 and end-2028: revenue at risk $ and as % of FY26 consumables at conversion price declines of 50/60/70%, with and without volume uplift of 0/15/30% on converted customers (the '40 fully converted clinical customers' evidence). Include the parallel-run effect (labs keeping 6000s running): quantify what share of 6000 revenue could be duplicative if utilization falls. (4) Compute the break-even Gb growth needed on converted volume to hold revenue flat, and compare to management's mid-20s% volume / mid-teens% price LT model and the >30% Gb growth on connected instruments. (5) Add the 35B flow cell (~20% lower $/Gb, ~Jan 2027) as an extra price layer on the X base. Return tables with inputs cited to file and date, formulas stated, and clearly labelled assumptions. Stop after about 20 minutes.

## Key findings

The ledger already holds the core bridge (E001–E009, E187, E205, E210). I'm reporting only what is new or what corrects it. All figures are calculations (OPINION) on ledger inputs, and I opened no raw files. They are consistent with, and extend, the ledger's own derivations.

1. **E210/E041 correction: pull-through reconciles on average bases, not year-end bases.** Pull-through is quarterly consumables divided by the active base (E018), so the denominator should be an average. Using end-2024 and end-2025 bases:
   - **6000:** ~1,660 and ~1,360 (E019, E019 less decommissions) average ~1,510. Times $670K gives ~$1.01B, against the ~$1.05B derived from the E040 quarterly dollars (274+286+252+234). The gap is about 3%.
   - **X:** 630 and 890 (E156, E038) average ~760. Times $1.35M gives ~$1.03B, against ~$0.98B derived (206+225+263+287). The gap is about 4%.
   - **Total:** $2.04B against $2.03B (69% × $2,939M). This confirms the 69% HT share to about 0.5%.
   - E210's X figure of ~$1.2B used the year-end base and overstated X. Its "~4% overshoot" at the total level was partly coincidence.

2. **New test: the FY26 pull-through guides don't match consensus at a 69% HT share.**
   - Guided X pull-through of $1.35–1.40M on an average base of ~1,060 (890 at year-end FY25 to ~1,235 at year-end FY26, my extrapolation) implies X revenue of ~$1.43–1.49B.
   - Guided 6000 pull-through of $600–650K on an average base of ~1,270 implies $0.76–0.83B.
   - Together that is ~$2.2–2.3B of HT. That is 71–75% of consensus FY26 sequencing consumables of $3,104M (E080), against the observed 69%.
   - Either consensus is $55–170M light (1.8–5.5%), or the guide assumes a H2 ramp, or the bases are smaller than I've assumed. This is a Q3 10-Q checkpoint.

3. **The 6000 guide implies a steep H2 decline in 6000 revenue.**
   - H1'26 6000 revenue is ~$444M (225+219, E040). Guided pull-through of $600–650K on an average base of 1,200–1,300 implies full-year revenue of $720–845M, so H2 is $276–401M.
   - That is **$138–200M a quarter, centred on ~$175M**, against $219M in Q2. Q3 consensus of $789M × 69% less a 6000 at $175M leaves X at ~$369M (+17% q/q). Q4 is ~$392M.
   - If the 6000 simply held at $219M, implied X pull-through is only ~$1.18M, below the $1.35M guide.
   - Consensus and guidance are therefore internally coherent only if the 6000 loses about $40M a quarter, or ~$175M annualized (~5.7% of FY26 consumables), within six months. This is the mechanism by which "no cliff" is already priced in. The test is Q3 6000 pull-through, which is not disclosed quarterly and has to be backed out.

4. **Revenue at risk, scaled to FY26** (full grid in the next section).
   - At 100% conversion the run-rate loss is $307–613M, or 9.9–19.8% of FY26 consensus, depending on price cut and uplift.
   - The central case (60% cut, +15% uplift) costs $473M, or 15.2%.
   - At the observed 70.5% cut and no uplift the loss is $617M, matching E004.

5. **Phasing assumption.** I assume 25% / 60% / 80% of the remaining 6000 revenue converts by end-2026 / 2027 / 2028 (ASSUMPTION). It reflects E012 (~20% sticky), E011 (clinical X at 80–85% by end-2026) and E010 (conversion flattening). On that path the central case loses 3.8% of FY26 consumables by end-2026, 9.1% by end-2027 and 12.2% by end-2028.

6. **Parallel-run bound from the JPM survey (corrects and quantifies E021).** Of 32 clinical respondents, 24 own a 6000 and 17 own an X (E021 corrected). By pigeonhole, at least 9 own both and at most 17 do. So **37.5–71% of clinical 6000 owners also have an X**. This counts customers, not revenue, and n=32 is small.

7. **Break-even Gb growth on converted volume is p/(1−p).** That is +100% at a 50% cut, +150% at 60% and +233% at 70%. This extends E187 to the whole grid.

8. **Price-bridge cross-check against the "mid-teens" model.** Three layers add up to roughly the model's mid-teens annual price decline:
   - tail conversion (~6–7% a year of seq. consumables),
   - the 35B (~4% a year),
   - residual within-platform repricing (~4% a year, E008).
   Management's mid-teens therefore leaves no room for further cuts beyond the 35B, and a Roche or Ultima price response would be additive.

9. **The 35B is a separate layer on a much larger base.** At −20% $/Gb on the X base (~$1.27B FY26E, my derivation), the revenue-neutral volume gain is +25%.
   - Revenue loss at constant Gb is $63M / $127M / $253M at 25% / 50% / 100% adoption of the 35B on X volume.
   - That is 2.0% / 4.1% / 8.2% of FY26 consumables.

10. **Combined worst-but-plausible case.** By end-2028, 80% conversion at a 70% cut with +15% uplift, plus a 60% 35B adoption, costs **~$640M, or 20.6% of FY26 consumables** (~30% of HT).
    - Break-even Gb growth is **~+26% a year for 2027–28**, assuming a −5% a year residual price.
    - That sits above E083's base case (+23%) and below E205's revenue-implied clinical Gb of +35–60%.
    - The thesis therefore turns on which of those two Gb numbers is right.

## Bridge and scenario tables

### A. Inputs (all cited to the ledger)
| Input | Value | Source |
|---|---|---|
| Q2'26 sequencing consumables | $775M | E050 |
| HT share of seq. consumables | 69% (confirmed by finding 1) | E003, E210 |
| HT revenue | $535M/qtr | E040 |
| X revenue, Q2'26 | $316M/qtr | E040 |
| 6000 revenue, Q2'26 | $219M/qtr (R = $876M annualized) | E040 |
| X share of HT revenue / Gb | 59% / 83% | E046 |
| FY26 consensus seq. consumables | $3,104M | E080 |
| Price ratio r (X $/Gb ÷ 6000 $/Gb) | (0.59/0.83)/(0.41/0.17) = 0.295 | E187 |

- **Implied cut at r = 0.295:** 70.5%. That is consistent with "easily more than 60–70%" (E030).
- **Earlier quarters:** the ratio does not reconcile before Q3'25 (E030).
- **Absolute $/Gb:** cannot be solved, because Gb is shipped capacity and not consumed Gb (E204). Only ratios are valid.

### B. Revenue at risk
**Formula:** at-risk = R × f × k, where k = 1 − (1−p)(1+u). Here p is the price cut, u is the volume uplift on converted Gb, and f is the share of the remaining 6000 revenue that converts. R is held static, although the 6000 is already declining (finding 3).

| p (cut) | u=0 | u=15% | u=30% |
|---|---|---|---|
| 50% (k) | 0.500 | 0.425 | 0.350 |
| 60% (k) | 0.600 | 0.540 | 0.480 |
| 70% (k) | 0.700 | 0.655 | 0.610 |

The tables below show run-rate loss in $M, with the percentage of FY26 consumables ($3,104M) in brackets. Columns run u = 0 / 15% / 30%.

| p | f=25% (end-2026, R×f=$219M) | f=60% (end-2027, $526M) | f=80% (end-2028, $701M) | f=100% ($876M) |
|---|---|---|---|---|
| 50% | 110 / 93 / 77 (3.5 / 3.0 / 2.5%) | 263 / 223 / 184 (8.5 / 7.2 / 5.9%) | 350 / 298 / 245 (11.3 / 9.6 / 7.9%) | 438 / 372 / 307 (14.1 / 12.0 / 9.9%) |
| 60% | 131 / 118 / 105 (4.2 / 3.8 / 3.4%) | 315 / 284 / 252 (10.2 / 9.1 / 8.1%) | 421 / 378 / 336 (13.5 / 12.2 / 10.8%) | 526 / 473 / 421 (16.9 / 15.2 / 13.5%) |
| 70% | 153 / 143 / 134 (4.9 / 4.6 / 4.3%) | 368 / 344 / 321 (11.9 / 11.1 / 10.3%) | 491 / 459 / 428 (15.8 / 14.8 / 13.8%) | 613 / 574 / 534 (19.8 / 18.5 / 17.2%) |

**Reading the table:** the volume uplift matters less than the price cut. Even +30% uplift at a 70% cut loses 17% of FY26 consumables. Uplift is worth about 2 points per 15% of volume.

### C. Clinical split sensitivity
The method assumes the same r (0.295) in clinical and research, as E187 did. It also assumes that clinical X share of revenue is 51% (78% volume) and that research X share is 77% (92% volume). These come from E186 and E187. Finally it assumes that clinical's HT share of its consumables equals the 69% total.

| Clinical share of HT revenue (s) | Clinical 6000 $/qtr | Annualized | % of total seq. consumables | Research 6000 $/qtr |
|---|---|---|---|---|
| 55% | $144M | $576M | 18.6% | $55M |
| 65% | $170M | $680M | 21.9% | $43M |
| 75% | $196M | $785M | 25.3% | $31M |

- **Formula:** clinical 6000 = s × 535 × (1−0.511). Research 6000 = (1−s) × 535 × (1−0.772).
- **Gb-share cross-check:** solving 0.78c + 0.92(1−c) = 0.83 gives clinical at 64% of HT Gb. That implies s ≈ 70% (E187: 69.5%).
- **Range:** the 6000 total across rows is $199–227M against the 219 observed. This shows how sensitive the split is to s, and that ~65–70% is the best-fitting range.
- **Tail dependence:** whichever s you pick, the clinical tail is ~34% of clinical HT revenue (E187: ~36%).

### D. Parallel-run and duplicative revenue
These calculations use clinical 6000 revenue of $728M a year (E187, $182M × 4) and a 70.5% cut.
- **Dual owners (finding 6):** 37.5–71% of clinical 6000 owners also own an X. Applied to $728M, that is $277–517M of 6000 revenue at dual-owner labs. If all of it moved to existing X capacity, the loss would be $195–364M a year (6.3–11.7% of FY26 consumables). This is a subset of the $617M full-conversion loss and needs no new X placements.
- **Utilization-drop sensitivity:** if 6000 utilization falls by 10 / 20 / 30% with Gb moving to idle X capacity, the loss is $62M / $124M / $185M. That is 2.0% / 4.0% / 6.0% of FY26 consumables. A 20% fall is the same order as the H2 guide-implied 6000 drop of 14–37% (finding 3).
- **Caveats (OPINION):** survey counts are not revenue. Larger labs are more likely to own both. The evidence on how many of these labs run both in parallel is still the Jefferies question that Thaysen did not answer (E014).

### E. Break-even Gb growth
**Formula:** u* = p/(1−p) on converted Gb alone. For volume across a whole base facing a price decline d, g* = 1/(1−d) − 1.

| Case | Break-even |
|---|---|
| Converted Gb only, p = 50 / 60 / 70 / 70.5% | +100% / +150% / +233% / +239% |
| Total HT, full conversion at r=0.295 | +41% (E004) |
| Total HT after 80% conversion (finding 10) | +43% cumulative, ~+19% a year |
| X base, 35B −20% | +25% (E084) |
| Annual price decline of 15% (management) | +17.6% |
| Management model: 25% volume × 85% price | +6.25% revenue |
| −15% price plus the 35B −20%, both applied | +47% |
| 35B and tail layers on top of a −5% residual (finding 10) | ~+26% a year for 2027–28 |

**Comparison:** management's mid-20s volume growth covers a mid-teens decline (+17.6%) with room to spare. It covers the full tail conversion plus the 35B only if the true Gb growth is at the top end (+26–30%). Clinical Gb of +35–60% (E205) clears this easily. E083's base (+23%) does not. The disagreement is between E205 and E083, and neither is cohort data.

### F. 35B layer
| 35B adoption on X volume | Loss at constant Gb ($M) | % of FY26 consumables |
|---|---|---|
| 25% | $63M | 2.0% |
| 50% | $127M | 4.1% |
| 100% | $253M | 8.2% |

- **Formula:** X base × 20% × adoption, with X base of $1,267M. That is my FY26E: 276 + 316 + a 369 / 392 H2 consistent with finding 3.
- **Timing:** Illumina's published window is H1 2027 (E214), not January. The cut size is hearsay (E058).
- **Base effect:** after conversion the X base is larger, so the 35B is worth more. At f=80%, p=70%, u=15% the X base rises by $242M to ~$1.51B, so the 35B at 60% adoption costs ~$181M.
- **Contracts:** Natera's §7(l) caps $/Gb on new products (E212), so for the largest accounts the price cut is mandatory and not discretionary.

## Contradictions and stale data
- **E041/E210 ($1.2B X from year-end base) is overstated.** With average bases X is ~$1.03B (finding 1).
- **Guided pull-through versus consensus** (finding 2) is a ~$55–170M gap at a 69% HT share. The sign depends on the end-2026 base extrapolations, which I assumed.
- **E083/E205 mismatch persists.** Gb needed for the reported revenue is +35–60%, while E083's bottom-up gives +23%. I could not reconcile them from the corpus.
- **E004 versus the clinical bridge:** E004's +41% is total-HT, while clinical needs +42–53% (E187). The dollar loss is unaffected.
- **Static R:** my grid holds the 6000 at $876M, while finding 3 says it falls to ~$700M in H2'26. Subtract the pre-conversion decline to avoid double-counting.
- **"Shipped Gb" (E204)** means the 17% / 41% split is capacity sold, not Gb consumed. If the 6000 tail consumes less than it ships, r is understated.

## Gaps / what I could not find
- **Q3'26 6000 pull-through and X base.** Neither is disclosed after Q4'25. This is the single test that resolves findings 2 and 3 (Q3 results are due 29 Oct 2026, E176).
- **Actual dual-owner revenue share.** Only the survey count exists (n=32).
- **Conversion-schedule evidence** beyond the cohort chart (E025). The 25% / 60% / 80% path is my assumption.
- **6000 versus X margin per Gb** (E035). I could not do a margin bridge, only a revenue bridge.
- **Absolute $/Gb by quarter.** Not solvable because consumed Gb is undisclosed.
- **Whether the 35B cut applies to the whole X base or only new volume.**
