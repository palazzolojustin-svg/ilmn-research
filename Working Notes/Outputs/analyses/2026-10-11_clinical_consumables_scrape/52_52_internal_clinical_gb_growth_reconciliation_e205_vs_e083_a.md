# Agent 52: 52-internal-clinical-Gb-growth-reconciliation-E205-vs-E083-and-Q3-26-pre-stage

*Model: sonnet. Run 2026-10-11 03:26:10. Cost $1.66 (API-equivalent).*

**Assignment:** Resolve gap 8 and pre-stage gap 2 using only the local corpus (Working Notes/Extracts, Sources, INDEX.md and the existing findings files in Outputs/analyses/2026-10-11_clinical_consumables_scrape/). The disagreement: ledger E205 implies clinical Gb +35-60% a year from revenue, while E083 says bottom-up +23%, with break-even near +26% a year for the combined worst case. Build a customer-level bottom-up. (1) From the Extracts for Natera, Guardant, Tempus, Caris, GeneDx, Adaptive, BillionToOne, Exact, Veracyte, Myriad, NeoGenomics, Labcorp and Quest (calls 2024-2026), pull quarterly test volumes by product (MRD, tissue CGP, liquid CGP, exome/genome, NIPT, screening) and any stated sequencing depth, reads per sample, panel size, genome vs exome mix or run-count disclosure. Multiply by Gb per test, citing a document for each Gb/test, and flag assumptions. Output a quarterly table for 2024-Q2'26 and a clinical Gb index with low/base/high growth rates for 2026-2028. (2) Cross-check against Illumina's disclosures: clinical ex-China revenue growth, the 'Gb >30%' claim, price decline per year (mid-teens model, 25% in Q3'24, within-platform residual about -4%), the mix-shift estimates in the ledger (E008) and the X-share data. Find which assumption in E205 vs E083 explains the gap: price decline smaller than modelled, Gb weighted to high-intensity tests, pack/mix, reagent rental, price increases, or an inflated clinical definition. Quantify the clinical Gb growth needed to offset (i) a further 6000-to-X conversion at 85% and 90% volume share, and (ii) a 20% 35B price cut from Jan 2027 and a Roche/Ultima-driven further 10% cut. Include the dual-owner share, if any source gives it, and the survey figures (JPM 62-customer survey: 75% of clinical respondents own a 6000, 58% an X). (3) Pre-stage Q3'26 results (29 Oct 2026): build a table of what a print would need to show to confirm or break the bridge (6000 revenue about $138-200M, X pull-through, FY26 guides $1.35-1.40M and $600-650K, clinical growth guide, X share of revenue of about 62-64%), using average installed bases rather than year-end bases, and list the exact questions analysts should ask. (4) Check the Extracts for any customer-concentration data (top-customer % of Illumina revenue, Natera/Guardant/GRAIL/Tempus share, large-customer pricing tiers) and report it. Return concise tables and citations (file name and date). Label FACT/MGMT/OPINION and show formulas. Report contradictions with the ledger explicitly.

## Key findings

NEW means the item is not in the ledger. UPDATE means it changes or quantifies a ledger item.

1. **The E205/E083 gap is mostly a difference in time basis, plus one weighting flaw in E083. It is not a disagreement about the same quantity.** OPINION (calc). E205 is a trailing figure (2025–H1'26 revenue-implied). E083 is a forward 2026–28 forecast. E083's 2026 base of +23% is already below what H1'26 shows. If I swap E083's own test-growth inputs for the Q2'26 prints in E081, its framework gives about +31% (table in §2). Reweighting categories by Gb instead of by revenue adds about 2–3 points more. UPDATE E083, E205.

2. **E083's weights are Illumina's revenue split, applied to Gb.** FACT/OPINION. E083's weights come to oncology 50%, rare disease 25%, reproductive 20% and other 5%. That is the JPM Jan 2026 application split (~51/25/21; [JPM deck slide 4, 2026-01-13]). The high-intensity categories (genomes, liquid CGP) have a larger share of Gb than of revenue, because X consumables cost less per Gb. E083's own sensitivity says rare disease at 35% adds about 2 points. UPDATE E083.

3. **E083's +23% cannot be squared with the mix shift and management's ">30%" total.** OPINION (calc). The formula is clinical Gb growth = (total Gb growth − research weight × research Gb growth) ÷ clinical weight. With clinical at 64% of HT Gb (E009), research Gb at +12% (F28), and E083's +23% for clinical, total HT Gb would be about +19%. With research at +20%, it would be +22%. Both are far below the ">30%" claim. If the clinical X share of volume rose 53%→78% year on year (E186) and clinical revenue rose 15%, then +23% Gb needs clinical price down only 6.5%. That in turn needs the clinical X/6000 $/Gb ratio r ≈ 0.82, against 0.295 observed in total HT. See Table 2c. UPDATE E083, E205.

4. **E205's high end (+60–65%) overreaches. A defensible trailing range is +35–50%, central about +42%.** OPINION (calc). Method B applies r = 0.295 to both clinical and research. That gives a revenue-weighted HT price of about −23% to −25%, which implies total HT Gb of about +37–39%. That is 7–9 points above the ">30%" floor. Anchoring on total +30–38% gives clinical +40–52% (Table 2b). The low end is +34–36% (research Gb +20%, total +30%). UPDATE E205, E187.

5. **Price/volume identification of total HT (NEW).** OPINION (calc on FACT shares). Within-platform $/Gb is unobserved, and it decides how big Gb growth was. Holding the Q2'26 and Q2'25 shares and revenues fixed:
   - Total Gb +30% requires the 6000 at +7% $/Gb and the X at −10%.
   - Total Gb +40% requires a flat 6000 and the X at −16.5%.
   - Total Gb +20% requires the 6000 at +16% and the X at −2.6%.

   Because 6000 lists fell 16–24% (E053), +16% for the 6000 is implausible. That makes +20% total, and so E083, hard to defend. Table 2d has the full grid. UPDATE E008: its single "residual −3.7%" hides these opposite-signed platform moves.

6. **Management has said "clinical volume above 30%" explicitly, in a forward-looking way (UPDATE E049, E085).** MGMT. At JPM on 2026-01-13, Thaysen said "These dynamics are driving clinical sequencing volume growth above 30%". In Q&A: "we continue to have that above 30% volume growth… at least from clinical customers, we expect to – will continue for a while… on the long horizon… for the whole business approximately 25%." Dhingra: "volume will continue to grow, we believe, over 30% in clinical." [Sources/ILMN/conference/ILMN_2026-01-13_44th_Annual_J.P._Morgan_Healthcare_Conference.md l.110, l.238, l.318]. So "clinical well above 30%" (Q1'26, Q2'26) was preceded by an explicit clinical ">30%" forward statement. E083 base (+23%) sits below management's stated forward number.

7. **Forward break-even, clinical Gb CAGR 2027–28 (my own build; it reproduces E247's +26% within rounding).** OPINION (calc, Table 3).

   | Scenario (2-year view) | Break-even Gb CAGR |
   |---|---|
   | Residual only | 4% |
   | Clinical X to 85% | 10% |
   | Clinical X to 90% | 15.5% |
   | 90% plus 35B (−20% on X, 60% adoption) | 20% |
   | Add a further −10% competitive cut | 24% |
   | Full 35B adoption instead | 28% |

   My base clinical Gb (+27% in 2027, +24% in 2028) is about break-even in the two worst cases. My low case (+12.5% CAGR) loses about 18% of clinical HT revenue over two years in the −10% competitive case.

8. **The FY26 X pull-through guide ($1.35–1.40M) looks out of reach on average-base math (NEW, extends E245).** OPINION (calc, Table 4). The FY average X base is about 1,064. FY X revenue must then be $1.44–1.49B, against $592M in H1. H2 therefore needs about $1.46–1.55M annualized, versus about $1.21M in H1'26 and a ~$1.35–1.37M peak in Q4'25 (E038). If Q3 X revenue is consensus-like (~$345M), Q4 needs about $1.55–1.67M annualized. Either the guide is cut or lowered, or 6000 volume moves onto existing X units much faster than trend (an "X-share jump" print). The Q4'25 deck gave the platform guide, and the Q1'26 and Q2'26 decks did not update it (F28 table), so a silent drop in the Q3 deck is itself a signal.

9. **The extra week is in Q4, not Q3 (CORRECTS E184, E176 note).** FACT. Dhingra on the Q2'26 call: "we have 1 extra week this year in Q4, which would largely be a consumables story" [Sources/ILMN/earnings_call/ILMN_2026Q2_Earnings_Call.md l.328]. Calendar arithmetic agrees: Q2 ended 28 Jun, so Q3 ends 27 Sep (13 weeks) and Q4 ends 3 Jan 2027 (14 weeks). The extract says it "adds maybe 0.5 point of revenue" (the source line was omitted, so I could not check it). A 14th week is mechanically 1/13 = 7.7% of Q4 consumables, or roughly 2% of FY revenue. The 0.5-point figure needs clarifying. Q3 y/y growth is not inflated by calendar. The FY pull-through guide, if unadjusted for a 53rd week, gets about a +2% tailwind.

10. **Revenue share of 62–64% in Q3 needs volume share of about 85–86% (NEW).** FACT/OPINION (calc). v = s·r ÷ (s·r + 1 − s). For r = 0.28–0.31, s = 85% gives v = 61–64% and s = 86% gives 63–66%. Volume share has risen only +1 point per quarter recently (82→83%). A 62–64% print therefore needs a faster quarter or a lower X $/Gb. Integer rounding means r is only known to ±0.03 (about ±10%), so no single-quarter move in r is informative (Q1'26 r = 0.254–0.283, Q2'26 r = 0.279–0.312; these overlap).

11. **Dual-owner share: still no direct source. The brief's "58% an X" is the all-respondent number.** FACT. The clinical figure is 17/32 = 53% (E021 correction). Pigeonhole bound: at least 24 + 17 − 32 = 9 clinical respondents (28%), at most 17 (53%), own both. That is 37.5–71% of 6000 owners (E248). Respondent size is unknown, so the revenue share could be higher than the count share. OPINION.

12. **Named-customer bottom-up cannot validate Illumina's clinical Gb. The corpus has no customer-company calls (NEW).** FACT. Extracts contain ILMN, MGI, ONT, PACB, ROCHE, SECTOR and TXG material. None exist for Natera, Guardant, Tempus, Caris, GeneDx, Adaptive, BillionToOne, Exact, Veracyte, Myriad, NeoGenomics, Labcorp or Quest. Customer volumes in this ledger come from web findings (E081). The only customer-company Extract is the Natera associate-director expert call (2026-07-22). Using E082 intensities on named labs, I get about 10 Pb per quarter against about 106 Pb of top-down clinical HT Gb. That is under 10–15% coverage (§1). OPINION. If correct, ~85–90% of clinical Gb sits with unnamed labs or in intensities the specs understate.

## 1. Customer-level snapshot (Q2'26 only; no quarterly series exists in the corpus)

I could not build the quarterly 2024–Q2'26 table. No Extract or Source holds those customers' calls. The volumes are E081 (web findings) and the Gb/test values are E082 (F13). Every Gb/test is a spec-derived estimate (E) or a spec (S).

| Customer / product | Q2'26 volume (E081) | Gb/test assumed (E082 / F13 source) | Tb per quarter | Flag |
|---|---|---|---|---|
| Natera clinical MRD | 283K | 0.5 (range 0.2–1; E; Natera white paper, F13) | ~140 | Excludes one-off tumor exome/WGS per new patient (count unknown) |
| Natera other (1.04M total − ~297K oncology) | ~743K | 1.5 (NIPT 1–2; E) | ~1,100 | Panorama is SNP-targeted, so this may be too high |
| Guardant oncology | ~104K | 60 (blend of liquid CGP ~120 (D) and lighter Reveal; E) | ~6,200 | Largest single item; unverified blend |
| GeneDx exome/genome | 30,785 | 35.6 (assumes 70% exome at 8 Gb, 30% genome at 100 Gb; E) | ~1,100 | Genome mix is not disclosed |
| Caris WES/WTS | 114K+ (E092) | ~13 (exome 8 plus RNA ~5; E) | ~1,500 | RNA depth assumed |
| Adaptive clonoSEQ | 36,111 | <1 (E) | ~20 | Multiplex PCR |
| BillionToOne | 196K | 1.5 (E) | ~290 | Prenatal shallow |
| **Named subtotal** | | | **~10,300 (about 10 Pb)** | |

Top-down comparison. Method: HT revenue $535M × r-adjusted prices (X 59% = $316M, 6000 $219M; r = 0.295) gives about 381M "pX-dollar units". Dividing by an assumed net X price pX gives total HT Gb. Clinical is 64% of that (E009).

| Assumed net X $/Gb | Total HT Gb (Pb/qtr) | Clinical Gb (Pb/qtr) | Named customers' share of clinical |
|---|---|---|---|
| $1.75 | 217 | 139 | ~7% |
| $2.30 | 165 | 106 | ~10% |
| $3.00 | 127 | 81 | ~13% |

The net price is my assumption. Cores quote $2.5–3.1/Gb (E054) and large accounts pay "half or a quarter" (E113). Check: 1,065 X units at $1.35M/yr ÷ $2.30 ≈ 1.6 Tb/day each, about 20% of an X Plus's nominal ~8 Tb/day. That is plausible.

Implication. OPINION. E082 intensities may be low for the big oncology names. Natera's revenue is several hundred million dollars a quarter. A modest share spent on Illumina flow cells would imply tens of Gb per test, not 0.5–1.5. This is untestable here: no Natera COGS split is in the corpus.

## 2. Reconciling E205 and E083

### 2a. E083 re-run on trailing prints (E083's weights, E083's intensity changes)

| Category | Weight | E083 base | Q2'26 print used (E081) | Test growth × intensity → Gb | Contribution |
|---|---|---|---|---|---|
| Rare disease | 25% | +20% / +10% → +32% | GeneDx +32% | 1.32 × 1.10 − 1 = +45% | 11.3 |
| Tissue CGP | 20% | +10% / +5% → +16% | Tempus +31%, Caris +18%; use +22% | 1.22 × 1.05 − 1 = +28% | 5.6 |
| Liquid CGP | 15% | +30% → +30% | Guardant G360 Liquid >30% | +30% | 4.5 |
| Amplicon MRD | 7% | +45% / −5% → +38% | Natera MRD +56%; use +50% | 1.50 × 0.95 − 1 = +42.5% | 3.0 |
| WGS-based MRD | 3% | +80% | no print; keep | +80% | 2.4 |
| NIPT / reproductive | 20% | +6% / −3% → +3% | BillionToOne +35%, Natera total +22%, Myriad prenatal −9%; use +12% | 1.12 × 0.97 − 1 = +8.6% | 1.7 |
| MCED / screening | 5% | +30% | GRAIL +35% | +35% | 1.75 |
| Other | 5% | +10% | none | +10% | 0.5 |
| **Total** | | **+23.4%** | | | **+30.8%** |

Gb weights instead of revenue weights (rare disease 35%, NIPT 12%, other 10%) add about 2–3 points: roughly +33–34%. OPINION. The NIPT and "use" figures are my judgment calls, and ±5 points on NIPT moves the total about 1 point.

### 2b. Top-down clinical Gb from the total claim

Formula: g_c = [G − (1 − w_c) × g_r] ÷ w_c, where G is total HT Gb growth, w_c the clinical weight and g_r research Gb growth.

| G (total) | w_c | g_r | Clinical Gb |
|---|---|---|---|
| 30% | 64% | 20% | +35.6% |
| 30% | 64% | 12% | +40.1% |
| 30% | 64% | 5% | +44.1% |
| 30% | 70% | 20% | +34.3% |
| 30% | 57% | 12% | +43.6% |
| 35% | 64% | 12% | +47.9% |

Research Gb is bounded only by Dhingra's "below the 30% kind of number" (Q3'25 call l.478, E206). Research revenue is −7% and research X share rose 82→92% (E186). A reasonable research Gb is +5–20%.

Why G is probably 30–38%, not higher. When total Gb was +40% (Q2/Q3'24) management said ">40%" (E049). Since Q4'24 it has said ">30%". That wording points to 30–39% (OPINION, from disclosure habit).

### 2c. Gap attribution (E205 central +42% versus E083 +23% = ~19 points)

| Driver | Direction and size | Basis |
|---|---|---|
| E083 uses forward-decelerated test growth; trailing prints are higher | E083 up ~7–8 points (23→31) | Table 2a |
| Revenue weights applied to Gb | E083 up ~2–3 points | E083 sensitivity and JPM slide 4 |
| Omitted categories (clinical research, pharma/clinical trials, population and newborn programs, Illumina's own TSO 500 business, international) | E083 up by an unquantifiable residual, about 5–10 points | "Clinical" is loose (E077, E211); TSO 500 counted in clinical (Q4'23 call l.546–548) |
| E205 Method B assumes the same r in clinical and research | E205 down ~10–15 points (from +60 to ~+45–50) | Implies HT total ~+37–39% |
| ">30%" is a floor, "connected instruments", ex-China | ±3–5 points either way | Q2'25 l.512–514, E207 |
| List increases, tariff (~1 point of growth in Q1'25), reagent rental in price | Reduce implied Gb by ~1–3 points | E033, E039; reagent rental scale is undisclosed |
| Clinical definition inflated | Cannot size; raises clinical revenue growth relative to pure diagnostics | E077 |

Required clinical X/6000 $/Gb ratio r if clinical price is only −5%. Solve (1 − k·0.78) ÷ (1 − k·0.53) = 0.95 for k = 1 − r. This gives k ≈ 0.18 and r ≈ 0.82, meaning the clinical X would be only ~18% cheaper than the 6000. That contradicts the CFO's "easily more than 60% to 70%" (Q2'24, E030) and Salk-type −53–60% list evidence (E051). So a −5% clinical price decline is not credible during a 25-point conversion year. OPINION.

### 2d. Platform-level price/volume identification (total HT, Q2'26 vs Q2'25)

Method: p6 = 1 in Q2'25; pX1 = r1 = 0.353 (v = 44%, s = 69%). Q2'25 Gb = 225/0.353 + 286 = 923 units. Q2'26 has X revenue $316M, 6000 revenue $219M, s = 83%. For a given total growth G, X Gb = 0.83 × 923 × (1 + G), pX2 = 316 ÷ X Gb, and p6_2 = 219 ÷ 6000 Gb.

| Total HT Gb growth G | X $/Gb y/y | 6000 $/Gb y/y |
|---|---|---|
| +20% | −2.6% | +16% |
| +25% | −6.5% | +12% |
| +30% | −10% | +7% |
| +35% | −13.5% | +3% |
| +40% | −16.5% | −0.3% |
| +45% | −19.4% | −3.7% |

Reading it. OPINION. 6000 $/Gb between −5% and +5% implies G of about +33–45%, which supports a high trailing clinical figure. A 6000 at +7% or more needs G near 30%. This table is the quantified version of the ledger's E008 "within-platform residual".

Rounding caveat. Rounded integer shares move r1 across 0.338–0.369 and r2 across 0.279–0.312. The year-on-year fall in r is at least 8% in every combination (centre ~16%). So the direction (the 6000 relatively more expensive per Gb than the X is) is robust, and the size is not.

### 2e. Survey cross-check

JPM survey: clinical planned volume +14.6% (2027) and +19.1% (2028), with spend +9.4% and +14.0% (E067). This is far below both +23% and +42%. The survey is customer-stated plans, n = 32, probably samples or tests rather than Gb, and Illumina-specific spend (E067 correction). I do not treat it as a trailing measure. It is evidence for a forward slowdown, though, so it supports a base case below the trailing +42%.

## 3. Clinical Gb index and offset requirements

Index, 2025 = 100. These rates are my judgment (OPINION), anchored on the H1'26 trailing range (+35–50%), management's "over 30% in clinical… for a while" and the "~25% for the whole business" long-horizon claim (JPM 2026-01-13).

| Case | 2026 | 2027 | 2028 | 2027–28 CAGR |
|---|---|---|---|---|
| Low (+30%, +15%, +10%) | 130 | 150 | 165 | 12.5% |
| Base (+35%, +27%, +24%) | 135 | 171 | 213 | 25.5% |
| High (+45%, +38%, +32%) | 145 | 200 | 264 | 35% |

Break-even formula. Required Gb growth g* = 1 ÷ (cumulative price factor)^(1/N) − 1. Mix factor from converting X share s₀→s₁ at r = 0.295: P(s) = 1 − 0.705 × s. Clinical s₀ = 78%, so P = 0.450.

| Scenario (2 years) | Price factors multiplied | Cumulative | Break-even CAGR |
|---|---|---|---|
| A. Residual within-platform −4%/yr (E008) | 0.96² = 0.922 | 0.922 | 4.1% |
| B. A + clinical X to 85% (P = 0.4006; 0.4006/0.450 = 0.890) | 0.922 × 0.890 | 0.821 | 10.4% |
| C. A + clinical X to 90% (P = 0.3655; 0.812) | 0.922 × 0.812 | 0.749 | 15.5% |
| D. B + 35B (−20%) on 60% of an X dollar share of 0.6: 0.2 × 0.6 × 0.6 = 7.2% | 0.821 × 0.928 | 0.762 | 14.6% |
| E. C + 35B (same) | 0.749 × 0.928 | 0.695 | 19.9% |
| F. E + competitive −10% on X (dollar share 0.65): 0.935 | 0.695 × 0.935 | 0.650 | 24.0% |
| G. 90% conversion, 35B on all X at −20% (0.87), competitive −10% (0.935), residual | 0.922 × 0.812 × 0.87 × 0.935 | 0.609 | 28.1% |

Revenue outcome over two years, as Gb index × price factor. This ignores any elasticity response to price cuts.

| Case | Scenario F | Scenario E |
|---|---|---|
| Low (1.125² = 1.266) | 0.823 (−18%) | 0.880 (−12%) |
| Base (1.27 × 1.24 = 1.575) | 1.024 (+2%) | 1.095 (+9.5%) |
| High (1.38 × 1.32 = 1.822) | 1.184 (+18%) | 1.266 (+27%) |

The conversion mix factors reproduce E006 (85% = −3.4%, 90% = −11.9% on total HT; clinical figures are larger because clinical starts at 78%). E083's +23% sits at break-even only in the F-to-G range and fails in G.

Live inputs from the corpus on the 35B. Thaysen (TD Cowen 2026-03-03): "aggressive pricing brings aggressive volume growth", and he declined to price it. UBS gives about −25% from ~$200 to ~$150/genome (E190). The list-price cuts tend to come in January (hearsay, E058), and the Illumina roadmap says H1 2027 (E214).

## 4. Q3'26 print pre-stage (due 29 Oct 2026)

Average base method. Pull-through is "average annualized… per instrument" (Q4'25 deck footnote, F28), so the denominator is the quarter average, not year end.

### 4a. Base assumptions (OPINION unless marked)

| Item | Value | Basis |
|---|---|---|
| X base, end of Q4'25 / Q1'26 / Q2'26 | ~890 / ~970 / ~1,065 | FACT start; Q2 = 970 + >95 placed (Q2'26 call) |
| X base, end of Q3'26 | ~1,150 | assumes ~85 placements ("elevated, with some moderation in y/y growth", Q2'26 call) |
| Average X base: Q1 / Q2 / Q3 / Q4 | ~930 / ~1,018 / ~1,108 / ~1,195 | FY average ≈ 1,064 |
| 6000 average base Q3 | ~1,250–1,300 | extrapolated; none disclosed since Q4'25 (E020) |
| Q2'26 X pull-through, annualized | $316M × 4 ÷ 1,018 = $1.24M | matches E038 |
| Q1'26 X pull-through, annualized | $276M × 4 ÷ 930 = $1.19M | matches E038 |
| Consensus Q3 sequencing consumables | $789M (+5.6% y/y); HT 69% → $544M (67–71% → $529–560M) | E050 |

### 4b. What Q3 must show for the bridge to hold

| Metric | Q2'26 actual | Guide-consistent print (bridge confirmed) | Trend print (bridge strained) | Break signal |
|---|---|---|---|---|
| Derived 6000 revenue | $219M | $140–190M | $195–210M | >$210M (6000 not declining) |
| X revenue (HT × share) | $316M | $370–380M | $333–348M | <$330M |
| X share of HT revenue | 59% | ~68–69% (needs volume share ~88%) | 61–64% (needs volume share 84.5–86%) | <60% |
| X share of HT volume | 83% | 87–88% | 84–86% | <84% |
| X pull-through (annualized, avg base 1,108) | ~$1.24M | $1.30–1.40M | $1.20–1.26M | <$1.20M |
| Clinical ex-China consumables growth | +15% | 13–15% (H1 ~17%, FY "mid-teens", H2 implied ~13–14%; Q3'25 comp +12%) | 12–14% | <12% |
| 6000 pull-through (annualized, avg 1,275) | ~$0.67M | $0.44–0.60M | $0.61–0.66M | >$0.66M (above the $600–650K FY guide) |
| Q3 RoW organic | 8.1% | ~4.5% guided | ~4.5% | beat to 6–8% with 6000 flat (suggests guide was sandbagged, not that the transition is easy) |
| Gb statement | ">30%, clinical well above" | repeated; ideally with a clinical number | repeated | dropped or lowered to ">25%" |

Formulas:
- Revenue share v = s·r ÷ (s·r + 1 − s), with r = 0.295 for the 88% case.
- X revenue = HT $ × v.
- 6000 revenue = HT $ − X revenue.
- Pull-through = quarterly revenue × 4 ÷ average base.

Guide arithmetic (see Key finding 8):
- FY X revenue = guide × FY average base. $1.35M × 1,064 = $1.44B, and $1.40M × 1,064 = $1.49B. H1 X revenue is $592M, so H2 needs $844–898M.
- FY 6000 revenue = $600–650K × ~1,270 = $762–826M. Subtracting H1 ($444M) leaves H2 at $318–382M, or $159–191M a quarter (±$20M for the base uncertainty; E245's range is $138–200M).
- H2 consensus HT is ($789M + $815M) × 69% = $1,107M. The guide low ends sum to $844M + $318M = $1,162M. Consensus is coherent with the guides only at their low ends.

Because H2 asks for a large step-up in X pull-through and a fall in the 6000, the likelier tell is a back-end-loaded Q3. If Q3 6000 is ≥$195M, the guide-implied 6000 decline falls on Q4: Q4 6000 would need to be ≤ $123–187M, and Q4 has the extra week.

### 4c. Questions for Q3 (priority order)

1. FY26 pull-through guides ($1.35–1.40M X; $600–650K 6000): are they reaffirmed, and does the number include the 53rd week? If you hold them, what H2 annualized X pull-through are you assuming (our math is ~$1.46–1.55M)?
2. What is the 6000 revenue and the 6000 average base in Q3? Please restate the active 6000 and X bases, last disclosed at Q4'25 (E020).
3. Of the Q3 X revenue growth, how much came from 6000 volume moving onto already-installed X (existing-customer conversion) and how much from newly placed units? (Jefferies asked a version of this on Q2'26 and got no numbers, E014.)
4. How many clinical customers run 6000s and Xs in parallel, and what share of 6000 revenue do they represent? (The JPM survey bounds this at 37.5–71% of clinical 6000 owners.)
5. What is clinical Gb growth, as a number, in Q3? The Q2'26 script said "well above" 30% total. You said "volume will grow over 30% in clinical" at JPM in January. Is that a floor, or is clinical now at 40%+?
6. Souda's Q1'26 question, still unanswered (call l.286): what is the first-year consumables price impact in clinical labs adding Xs, and is it in the guide? (E209)
7. Does the ">30%" Gb metric still exclude China and cover only connected instruments? What share of the installed base is connected? Is it Gb sequenced, or Gb shipped (the transition slides say "shipped")? (E204, E207)
8. Q4 has a 14th week. What does it add to Q4 consumables (we compute ~7.7%, about 2% of FY revenue)? What did you mean by "0.5 point"?
9. The 80–85% clinical X volume target for year-end: where is clinical X share at the end of Q3? (Q2: 78%.)
10. 35B: pricing and date, now that the quarter is out. Is any 35B discount structurally different for Natera or Caris, given the Open Offer's "price per Gb shall not increase" clause (E212, E232)?
11. Customer concentration: is any customer now above 10% of revenue? (None through FY25.) Is the Open Offer window (about Aug 2027, E233) a renewal event?

## 5. Customer concentration (task 4; mostly confirmatory)

- FACT. FY23–FY25 10-Ks: "no customers that provided more than 10% of total consolidated revenue" [Sources/ILMN/filing/ILMN_10-K_FY2025.md l.1558; FY2024 l.1576; FY2023 l.1572]. A single customer could therefore account for up to ~$430M a year (10% of $4,343M).
- No top-10 or top-N share, and no named-customer Illumina share appears in any call, deck or Extract I grepped (earnings calls, conferences, decks and research 2025–26). The search returned nothing.
- Already in the ledger: top ~30 customers per region drive planned purchases (E108), the new "small number of large, centralized laboratory customers" risk-factor wording (E107), Tempus ~33% vendor payments (E213, attribution unverified), GeneDx 20/13/11% unnamed supplier (E216), Natera/Caris/Guardant contract terms (E109, E110, E192–E194, E212, E228, E232).
- MGMT, new framing. Dhingra and Thaysen describe clinical growth as coming from "several multi-unit capacity expansions from large clinical customers, including for new clinical trials" (Q2'26 call l.109) and from customers "who have made their decisions" (TD Cowen 2026-03-03).

## Contradictions and stale data

- **E184 and the "Q3 has 14 weeks" note in E176/E184 are wrong.** The extra week is in Q4 (Q2'26 call l.328). Q3 is 13 weeks. Remove the +7% Q3 adjustment.
- **The brief's "58% own an X" is the all-respondent share** (36/62). Clinical respondents are 17/32 = 53% (E021 correction). The brief's "75% own a 6000" is correct for clinical.
- **E083 is not comparable to E205.** It is a 2026–28 forecast, E205 is trailing, and E083's 2026 value has already been overtaken by H1'26. The ledger E246 correction ("bracketed +35–60% versus +23% base") should be read as two different quantities.
- **E205 Method B (+60–65%) conflicts with the total ">30%"** unless total HT Gb is ~37–39% (see Key finding 4). Method C (+44%) is the internally consistent one.
- **E008's "residual −3.7%" masks a split** (X down, 6000 up). It is a blend, not a single within-platform price change (Table 2d).
- **E067 / the survey vs trailing clinical Gb:** survey plans (+14.6% / +19.1% volume) are far below trailing +35–50%. Different measure and sample, but flagged.
- **E247's "+26% worst case" is reproduced** by my scenario G (28%) and F (24%). No contradiction.
- **E082 intensities vs a top-down check:** named labs at E082 Gb/test cover under 10–15% of top-down clinical Gb (Table in §1). Either E082 is too low for the big oncology names, or most clinical Gb is outside the named customers.
- **Management's forward "clinical >30%" (JPM 2026-01-13) differs from the "~25% whole business" long horizon.** Both are management statements. The second is the one E047 captures.
- **The extract wording of the CFO's "0.5 point" for the 14th week conflicts with simple arithmetic** (7.7% of Q4). The source line was omitted in my read, so I could not verify.

## Gaps / what I could not find

- No customer-company calls or filings in the Extracts or Sources. No quarterly 2024–Q2'26 volume or Gb table by product, no stated sequencing depth, reads per sample, genome/exome mix or run counts for Natera, Guardant, Tempus, Caris, GeneDx, Adaptive, BillionToOne, Exact, Veracyte, Myriad, NeoGenomics, Labcorp or Quest. I used E081 (web) for Q2'26 only.
- No source gives the net X $/Gb. All Pb figures depend on my $1.75–3.00 range.
- No revenue-weighted dual-owner share. Only the JPM survey (n = 32 clinical) with counts.
- No Q2'26 or Q3'26 installed-base figures for either platform. X base ~1,065 is a calculation; the 6000 base is extrapolated.
- No clinical Gb figure from management, only "above 30%" and "well above".
- The Q2'26 call "0.5 point" extra-week figure is extract-only.
- I did not check the Sources transcripts for other Q&A on extra-week effects beyond l.314–330.
