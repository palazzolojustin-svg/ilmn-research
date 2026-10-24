# Agent 108: 108-internal-consumables-gross-margin-bounds-and-mix-decomposition

*Model: sonnet. Run 2026-10-11 10:35:15. Cost $0.96 (API-equivalent).*

**Assignment:** Use only the local corpus (Core Notes, INDEX.md, Extracts and Sources for ILMN earnings decks, calls, 10-K and 10-Q filings and consensus sheets, 2023 to Q2'26) to bound the margin side of thesis question 1, which earlier agents say 'cannot be isolated'. Steps: (1) For each quarter, collect product revenue split (consumables, instruments, services/other), the sequencing consumables $ and the gross margin lines (GAAP and core non-GAAP, product vs service if reported, cost of product revenue, cost of services). (2) Collect every management statement about gross margin drivers (instrument mix, tariffs, memory, freight, China, 'reduced pricing', NovaSeq X consumables margin vs 6000, reagent rental, SomaLogic, GRAIL deconsolidation) with exact quotes and dates, and any quantified basis-point bridges. (3) Build a bounded estimate: assume instrument gross margin ranges (for example 30-50%) and service margin ranges, and back-solve the implied consumables gross margin by quarter, giving the minimum, central and maximum cases. Test whether the implied consumables margin trended down as X share of HT revenue rose from 27% to 59% (correlate quarterly), and estimate what each 5-point X-share move costs in gross margin at plausible 6000 vs X margin gaps (6000 consumable margin assumed 80-85%, X 70-80%). (4) Estimate how much of Q2'26 core gross margin of 68.2% and operating income is attributable to the remaining NovaSeq 6000 consumables (about $219M per quarter by prior agents), and the EPS effect if that revenue converts at -60% to -70% $/Gb with +30% Gb, using the share count and tax rate from the corpus. (5) List the metrics management gave or dropped about gross margin (for example the 'reduced pricing' language), and flag contradictions. Label every derived number OPINION (calc) and show the arithmetic. Save nothing outside your returned findings. Stop at 20 minutes and return findings only.

## Key findings

1. **The margin side can be bounded better than "cannot be isolated".** The GAAP filings split cost of revenue into product and service lines (amortization is a third line). That gives **product gross margin (GM) ex-amortization of about 70–71% in Q1'26 and Q2'26, down from 74.3% in Q3'24**. Service GM rose from about 49% to about 55%. The tables below show the arithmetic. This is new: the ledger has only the core non-GAAP total (E034). FACT, from 10-Q income statements.

2. **After adjusting for tariffs, the implied consumables margin did not fall while X share of HT revenue went from 35% to 55%.** At a 40% instrument margin, the implied consumables margin was 78.8% in Q3'24. It was 78.4% in Q3'25 once the ~$24M tariff cost is added back (X share 51%). Q4'24 was 76.6% against 76.8% for Q4'25 (X share 40% → 55%). The raw, unadjusted series fell about 3.8 points to 75.0% in Q2'26. Tariffs, memory and freight explain most of that. OPINION (calc).

3. **The 6000 consumables probably generate about 22–24% of Q2'26 core gross profit and about 67–71% of core operating income.** That uses $219M a quarter (E003) at an assumed 80–85% margin. It is a very concentrated profit pool. OPINION (calc).

4. **Full conversion would cut gross profit by roughly $84–127M a quarter (central $95–117M) and EPS by about $1.75–2.63 a year.** That is against an annualized Q2'26 EPS of $5.24. The case assumes all 6000 revenue converts at −60% to −70% $/Gb, Gb +30%, and opex unchanged. OPINION (calc).

5. **The ledger's margin-gap assumption (X 70–80% vs 6000 80–85%) implies X unit costs are far lower.** With a −70% price and equal cost per Gb, the X margin would be only about 41%. Holding 70–80% needs X cost per Gb 50–67% below the 6000's. Management said only that X margins "at scale would be comparable" (Q4'23 call). OPINION (calc).

6. **Implied consumables cost per Gb fell, but revenue per Gb fell faster.** From Q3'24 to Q2'26, revenue per Gb fell about 34% (775/741 = 1.046; ÷ 1.58 for the +30%/yr Gb floor over 7 quarters). Implied consumables COGS per Gb fell about 21–29%. The gap is the 3–4 points of margin compression. OPINION (calc, and it depends on the ">30%" Gb floor).

7. **Management gave basis-point (bp) bridges for tariffs in 2025 and then stopped.** Tariffs cost about 110 bp net in Q2'25, 220 bp in Q3'25 and 205 bp in Q4'25. Q1'26 said only "partly offset by tariffs". Q2'26 gave no figure. Q2'26 non-GAAP GM was down 120 bp y/y (68.2% vs 69.4%) with no bp bridge. FACT/MGMT.

8. **"Reduced pricing" was cited as a gross-margin headwind exactly once, in the Q1'25 10-Q.** The quote is in the dropped-disclosure section below. It adds the exact wording to E036. FACT.

9. **The tariff and gross-margin comparisons are noisy.** Q2'25 GAAP product GM includes a $23M impairment charged to cost of product revenue (FY25 10-K). Q3'25 included an inventory-reserve increase (Q3'25 10-Q). FACT.

## 1. Quarterly data

**Revenue split and GAAP cost lines ($M).** Source: 10-Q/10-K income statements. Q4 is FY minus 9M. Core non-GAAP GM comes from the call extracts. The 2024 figures include GRAIL service revenue through June 2024. The tables below show what each quarter contained and the product-GM math.

| Qtr | Product rev | Cost of product | Product GM | Service rev | Cost of service | Service GM | Core non-GAAP GM |
|---|---|---|---|---|---|---|---|
| Q1'24 | 876 | 255 | 70.9% | 200 | 106 | 47.0% | 67.1% |
| Q2'24 | 927 | 250 | 73.0% | 185 | 95 | 48.6% | 69.4% |
| Q3'24 | 914 | 235 | 74.3% | 166 | 84 | 49.4% | 70.5% |
| Q4'24 | 938 | 278 | 70.4% | 166 | 81 | 51.2% | 67.4% |
| Q1'25 | 880 | 253 | 71.2% | 161 | 88 | 45.3% | 67.4% |
| Q2'25 | 912 | 276 (253 ex-impairment) | 69.7% (72.3% adj.) | 147 | 71 | 51.7% | 69.4% |
| Q3'25 | 927 | 267 | 71.2% | 157 | 68 | 56.7% | 69.2% |
| Q4'25 | 990 | 312 | 68.5% | 169 | 72 | 57.4% | 67.0% |
| Q1'26 | 917 | 273 | 70.2% | 175 | 80 | 54.3% | 68.2% |
| Q2'26 | 982 | 291 | 70.4% | 177 | 80 | 54.8% | 68.2% |

- **Reconciliation check (OPINION, calc).** Revenue minus the two cost lines, divided by revenue, gives 70.5% (Q3'24), 67.2% (Q1'25), 69.4% (Q2'25 ex-impairment), 69.1% (Q3'25), 66.9% (Q4'25), 67.6% (Q1'26) and 68.0% (Q2'26). These match the non-GAAP GM within about 0.6 points, so the split is a fair proxy.
- **Source note.** Q4'24 product and service revenue are FY24 less 9M24. The Q3'25 and FY25 10-K lines I opened support the Q4'25 derivation. Q4'24 service GM is FY24 less 9M24 cost lines.
- **Service GM is a hidden contributor.** Service GM rose about 5–6 points (49% → 55%) between Q3'24 and Q2'26 on service revenue of about $175M, so that adds only about 1 point to total GM. It also means part of the product-line margin decline is hidden in the total GM.

**Consumables share of product revenue.** This is the weight w used in the back-solve. It is consumables (sequencing plus microarray) divided by product revenue, with instruments taken as sequencing instruments plus about $3–4M of microarray instruments.

| Qtr | Consumables ÷ product revenue | Source |
|---|---|---|
| Q3'24 | 807/914 = 88.3% | 10-Q (741 + 66) |
| Q4'24 | ≈83.0% | 698 consumables + about 67 microarray; instruments 155 + 4 |
| Q1'25 | 768/880 = 87.3% | 10-Q |
| Q2'25 | 811/912 = 88.9% | 10-Q (740 + 71) |
| Q3'25 | ≈88.1% | Product less instruments (107 + about 3) |
| Q4'25 | ≈84.0% | Product less instruments (154 + about 4) |
| Q1'26 | ≈86.8% | Product less instruments (118 + about 3) |
| Q2'26 | ≈86.9% | Product 982 less instruments (about 129) |

## 2. Bounded back-solve of implied consumables margin

**Method.** Consumables margin m_c = (product GM − (1−w) × instrument margin m_i) ÷ w. I tested m_i = 30%, 40% and 50%. This is OPINION (calc).

Worked example, Q2'26 at m_i = 40%: (70.4 − 0.131×40) ÷ 0.869 = (70.4 − 5.24) ÷ 0.869 = 75.0%.

| Qtr | X % of HT revenue | m_c, m_i = 30% (max) | m_c, m_i = 40% (central) | m_c, m_i = 50% (min) |
|---|---|---|---|---|
| Q3'24 | 35 | 80.2 | 78.8 | 77.5 |
| Q4'24 | 40 | 78.7 | 76.6 | 74.6 |
| Q1'25 | 43 | 77.2 | 75.7 | 74.3 |
| Q2'25 (ex-impairment) | 44 | 77.6 | 76.3 | 75.1 |
| Q3'25 | 51 | 76.8 | 75.4 | 74.1 |
| Q4'25 | 55 | 75.8 | 73.9 | 72.0 |
| Q1'26 | 55 | 76.3 | 74.8 | 73.3 |
| Q2'26 | 59 | 76.5 | 75.0 | 73.5 |

- **Raw correlation.** Pearson r between X share of HT revenue and the central m_c is about −0.88 (n = 8). The slope is about −0.15 point per point of X share, or about −0.77 point per 5 points. This is contaminated by the time trend and by tariffs, which began in April 2025.
- **Tariff-adjusted correlation.** Tariff cost is bp × total revenue: Q2'25 about $12M, Q3'25 about $24M (2.2% × 1,084), Q4'25 about $24M (2.05% × 1,159). I assumed it falls entirely in product cost.
- **Adjusted product GM.** Q2'25 is 73.6% (72.3 + 1.3), Q3'25 is 73.8% (71.2 + 2.6) and Q4'25 is 70.9% (68.5 + 2.4).
- **Adjusted central m_c.** Q3'24 78.8, Q4'24 76.6, Q1'25 75.7, Q2'25 77.8, Q3'25 78.4, Q4'25 76.8.
- **Adjusted correlation.** Against X share of 35, 40, 43, 44, 51 and 55, r ≈ −0.16 (n = 6) and the slope is about −0.13 point per 5 points. That is effectively no measurable erosion.
- **Q1'26 and Q2'26 can't be tariff-adjusted** because management gave no bp figure. If tariffs were $15–24M a quarter, Q2'26 central m_c would be about 76.8–77.7% instead of 75.0%.
- **Caveats.** Instrument margin is not constant. Q4 is instrument-heavy. From 2026, SomaLogic product revenue sits in the product line. The 6000-vs-X margin gap cannot be observed directly. This is a bound, not a measurement.

## 3. Cost of each 5-point X-share move at constant Gb

This builds on E001 and E006 (6000 earns 2.41, X earns 0.71, HT average = 1.0, HT revenue about $535M a quarter). All of this is OPINION (calc).

- **Revenue effect (matches E006).** 0.05 × (2.41 − 0.71) = 0.085 of HT revenue, or about $45.5M a quarter.
- **Gross profit effect, percentage-margin bound.** ΔGP = 0.05 × (0.71×m_X − 2.41×m_6) × $535M.
  - m_6 = 82.5%, m_X = 75%: 0.05 × (0.5325 − 1.988) × 535 = **−$39M**.
  - m_6 = 85%, m_X = 70%: 0.05 × (0.497 − 2.0485) × 535 = −$41.5M.
  - m_6 = 80%, m_X = 80%: 0.05 × (0.568 − 1.928) × 535 = −$36M.
- **Gross profit effect, equal-unit-cost bound.** If cost per Gb is equal on both platforms, the whole $45.5M revenue loss flows to gross profit, and the X margin is only about 41%. That is inconsistent with management's "comparable" claim (finding 5).
- **Range per 5 points of share.** −$36M to −$46M a quarter, central about −$39M. That is about 4.6–5.8% of Q2'26 core gross profit ($790M).
- **Effect on GM%.** (790 − 39) ÷ (1,159 − 45.5) = 67.4% against 68.2%, so about **−0.76 point per 5 points of share**.
- **Why this does not show up historically.**
  - A 24-point rise in X share (35% → 59%) would imply about −3.6 points of GM at constant Gb.
  - Core GM actually moved −2.3 points (70.5% in Q3'24 to 68.2% in Q2'26), with about 2 points of that being tariffs.
  - So Gb growth (+30% a year or more) and COGS productivity absorbed the repricing, as in finding 6. The risk is a lumpy, fast conversion, not a gradual one (E007).

## 4. Q2'26 attribution and EPS

Inputs are FACT from the Q2'26 call: core revenue $1,159M, non-GAAP GM 68.2%, non-GAAP operating margin 22.5%, tax rate 20.5%, about 153M diluted shares, EPS $1.31. The 6000 figure of $219M is from E003.

**Attribution (OPINION, calc).**
- Core gross profit is 1,159 × 68.2% = $790M. Operating income is 1,159 × 22.5% = $261M.
- 6000 gross profit at 80% / 82.5% / 85% is $175M / $181M / $186M.
- That is 22.2% / 22.9% / 23.6% of core gross profit, and 67% / 69% / 71% of operating income.
- It is 18.9% of revenue ($219M ÷ $1,159M).
- Ex-6000, GM would be (790 − 181) ÷ (1,159 − 219) = 64.8%.

**Conversion scenario.** The 6000 revenue moves to X at −60% or −70% $/Gb with +30% Gb, and opex stays constant. New revenue is 219 × (1 − cut) × 1.30.

| Case | New X revenue | Revenue loss | Lost GP (m_6 = 82.5%, m_X = 75%) | ΔEPS per quarter | Annualized |
|---|---|---|---|---|---|
| −60% | $113.9M | −$105.1M | −$95.3M | −$0.50 | −$1.98 |
| −70% | $85.2M | −$133.8M | −$117.1M | −$0.61 | −$2.43 |
| Wide range (m_6 80% / m_X 80% at −60%; m_6 85% / m_X 70% at −70%) | — | — | −$84M to −$127M | −$0.44 to −$0.66 | −$1.75 to −$2.63 |

- **EPS arithmetic.** For the −60% case: 95.3 × (1 − 0.205) ÷ 153 = $0.495 a quarter, or $1.98 a year. It is 38–46% of annualized Q2'26 EPS of $5.24 ($1.31 × 4), which is a base for scale only, not a forecast.
- **Pro-forma margins.** GM falls to about 65.9% at −60% (694.7 ÷ 1,053.9) and about 65.7% at −70% (673 ÷ 1,025). Operating margin falls to about 15.7%.
- **Not all of it converts.** If 20% never moves (E005), the hit is about $1.6–1.9 a year.
- **GP break-even.** At −65% and 75% X margin, break-even needs about +215% Gb on the converting volume (181 ÷ (219 × 0.35 × 0.75) = 3.15×). At −60% it is about +175% (2.75×). That is consistent with the +240% revenue break-even in E004.
- **Missing offsets.** I did not model X service contracts, X instrument margin or opex leverage. This is a mechanical downside bound, not a forecast.

## 5. Management statements on gross-margin drivers

Quotes and dates are from the call and filing extracts.

- **Q1'23 call (FACT):** GM was down 500 bp y/y from less fixed-cost leverage and "lower instrument margins from the NovaSeq X launch, which is typical with a new platform introduction". Goswami expected the high 60s by year-end. Actual Q4'23 was 64.7%, a miss.
- **Evercore, 28 Nov 2023 (Goswami):** lower margins "on the X (instrument and consumables) while production ramps than on the 6K". This extends E035 (6000 "highly profitable"; X margins "comparable at scale").
- **Q4'23 call:** the Q4 GM step-down came from lower revenue, higher-than-expected X contribution, lower-margin partnership revenue "and a mix shift from 6000 to X consumables". Goswami said X consumable margins "should more or less normalize through 2024". This is the one explicit link in the corpus between the 6000→X consumables shift and a GM decline. The 2024 recovery (67.1% → 70.5% by Q3'24) followed.
- **Q3'24 call (Dhingra):** the 450 bp y/y gain came "mainly" from productivity, with the consumables mix "roughly half" of it. Management called the productivity gains "sustainable". Dhingra put the GM target at the "high 60s to 70%".
- **Q1'25 call (Dhingra):** GM was below plan because of a higher instrument mix, pulled-forward HT instrument servicing (software upgrades) and field-service costs.
- **Q3'25 call:** "almost 220 bp" of tariffs, with base GM up about 90 bp. Levers named were instrument GM, the Singapore and India centers, and the manufacturing footprint.
- **Q4'25 call:** tariffs 205 bp, and GM ex-tariffs "improved 165 bps". The call table is y/y (−40 + 205 = +165), but a JPM recap labels the same 165 bp "q/q".
- **Q2'26 call (Dhingra):** the memory cost is "already in Q2 results, so the bulk is in gross margin and Q2 is a starting run rate". Thaysen said Illumina is "sharing some of the increase with customers". This overlaps E064.
- **Q2'26 10-Q:** headwinds named are tariffs, mix, SomaLogic, memory and freight/Middle East energy. Offsets are lower field-service and warranty costs. IEEPA tariff refunds are "immaterial" so far. Management says it "partially mitigated... through supply-chain optimization, cost measures, and pricing actions".
- **Reagent rental, SomaLogic, GRAIL:** no quantified GM bridge exists for any of these in the corpus.
  - GRAIL's deconsolidation lifted reported consolidated GM in Q2'25: 10-Q GM was 65.6% against 64.8%, while the core GM comparison was unfavorable.
  - SomaLogic is described only as "lower-margin" in the Q2'26 10-Q and by Freedom Broker (5 Aug 2026). No numbers.

## 6. Metrics given and dropped

- **"Reduced pricing" is a dropped disclosure.** Q1'25 10-Q MD&A: "…offset by lower product margins, primarily due to reduced pricing, and an increase in field service costs". This is the only appearance I found. Q2'25 onward cites tariffs, impairment, mix and field service instead. The wording disappeared as tariffs became the headline explanation, which gave management a cleaner narrative while X share kept rising (44% → 59%). OPINION.
- **Tariff bp bridge is dropped.** It was given for Q2'25–Q4'25 (110, 220, 205 bp), then dropped from Q1'26. The Q2'26 call, deck and 10-Q have no tariff dollar figure, which blocks the clean adjustment in section 2. The 10-Q does say tariff costs were "lower than the prior quarter". FACT (absence).
- **Product and service GM are never disclosed explicitly.** The Q2'25 10-Q gives "approximately 70%" product GM and "approximately 48–52%" service GM, but only the filings let you build them. The call never gives them. No consumables-only GM is given anywhere.
- **Operating margin was shifted by deferred compensation.** In Q2'26, "about 60 basis points of deferred compensation (EPS neutral, offset in other income)" sits in opex, and management also cited "about 23% excluding the deferred compensation effect". Reported operating margin was 22.5%. This is a presentation choice, not a restatement. It flatters the "ex-item" margin by 60 bp while EPS is unchanged. FACT/OPINION.
- **GAAP vs non-GAAP gap:** Q2'26 GAAP GM was 66.4% against 68.2% non-GAAP. The difference is amortization of acquired intangibles ($18M), stock compensation and similar items.

## Contradictions and stale data

- **Ledger E034 omits several quarters.** It lists Q4'25 67.0%, Q1'26 and Q2'26 68.2%, but not Q1'25 67.4%, Q3'25 69.2% or Q2'25 69.4%. I supply them above.
- **E034's claim that "GM fell as instruments mix, tariffs, memory and freight rose" is partly misleading.** Q4'25 ex-tariff GM was up 165 bp y/y. The y/y decline of 120 bp in Q2'26 has no stated driver beyond freight, memory and SomaLogic.
- **JPM labels the 165 bp as "q/q"; the call implies y/y.** The y/y reading is right: −40 bp reported plus 205 bp of tariffs is +165 bp.
- **Q2'24 sequencing consumables is $737M on the call but $729M in the Q2'25 10-Q comparative.** I used the 10-Q figure for the weights. The same caution applies to other restated comparatives.
- **Q4'25 deck ~90% X share (E046) is unresolved.** I did not retest it.
- **Core GM FY24 and FY25** are given as 67.1% and 66.1% in the FY25 10-K. These are GAAP core, not non-GAAP.

## Gaps / what I could not find

- No consumables-only, X-only or 6000-only gross margin in any document.
- No Q1'26 or Q2'26 tariff dollar or bp figure. This blocks a clean tariff adjustment for the two quarters that matter most.
- No instrument GM by quarter. The 30–50% range is an assumption, and reagent-rental economics (E039) are undisclosed.
- SomaLogic's revenue split between product and service lines, and its margin.
- 2023 quarterly product and service splits, which I did not pull. 2024–26 only.
- No reconciliation of whether the "Gb +30%" floor applies to HT only. This drives the unit-cost result in finding 6.
- I did not search the research notes or the expert calls for X-vs-6000 margin comments beyond a keyword pass. There may be sell-side margin estimates I missed.
