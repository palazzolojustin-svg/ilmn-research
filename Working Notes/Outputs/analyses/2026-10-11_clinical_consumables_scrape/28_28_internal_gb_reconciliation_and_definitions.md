# Agent 28: 28-internal-gb-reconciliation-and-definitions

*Model: sonnet. Run 2026-10-11 02:38:24. Cost $0.99 (API-equivalent).*

**Assignment:** Open gaps 2, 5, 16 and 1, using only the local corpus. Go to the ORIGINALS in Working Notes/Sources/ILMN (decks and PDFs), not just the Extracts. Prior agents mostly used the Extracts. (1) JPM Jan 2026 deck and Strategy Day 2024 deck: extract every slide with Gb, capacity, installed-base or application-level data. This includes the 'HT capacity grew ~26%/yr 2022-25' claim, the ~2k HT installed base vs the 6000 base (~1,360) plus the X base (~890), clinical application splits, and Gb CAGR slide 12. Reconcile the numbers into one table. (2) Build a clinical Gb growth bridge. Use clinical ex-China consumables growth (15-20%) and the stated price decline (mid-teens, and 20-25% in 2024) to back out the implied clinical Gb growth by quarter since Q1'24. Check it against any explicit management statement ('well above 30%'). Test with and without mix-shift effects, and compare it to the customer COGS-per-test evidence in the Extracts for Guardant, Adaptive and GeneDx. State the implied range. (3) Search all ILMN calls, conferences and expert-call Extracts and Sources (grep) for the terms 'clinical' with 'definition', 'clinical research', 'LDT', 'pharma', 'biopharma', 'what is included', 'what we classify'. Compile every statement on what counts as clinical consumables and any change over time, and bridge ~50% (2023) to >65% (2026). Flag classification or re-segmentation changes, including 'research & applied' renamings and the China exclusion. (4) Grep for dropped or changed disclosures across all decks and calls from 2023 to 2026: slide titles, footnotes and metrics that appear in one period and vanish in the next (transition cohort, decommissions, pull-through, Gb growth, reagent rental, X installed base, 6000 shipments). Produce a dated table of 'disclosed → dropped' with the file paths. (5) Pull any analyst questions that went unanswered or deflected in Q1'25-Q2'26 on 6000 revenue, dual-running or clinical X share. List the questioner, date and the exact answer. Mark Q3'26 (29 Oct) print questions that follow. Cite file names and dates.

## Key findings

Mostly confirmatory. Eight points are new or correct a ledger item.

- **FACT: the deck volume metric is "Gb *shipped*", not Gb sequenced.** Every transition slide titles it "NovaSeq X % of HT Gb Shipped" (Q2'25 to Q2'26 decks, JPM Jan 2026 slide 6). This corrects the "volume share" wording in E001 and E046. Shipped Gb is flow-cell capacity sold, not consumed. Meanwhile the ">30%" growth metric is "Gb output on connected HT and MT instruments" (Q2'26 call l.154). The two Gb metrics differ and neither is reconciled for investors.
- **FACT: the ">30%" Gb metric is ex-China and covers HT and MT.** Dhingra, Q2'25 call l.512–514: "China hasn't been connected". The Q2'25 wording said "runs on those connected instruments in high throughput". From Q3'25 on, the script says "high- and mid-throughput". The scope is not constant. It adds to E049.
- **FACT: the installed-base tables reconcile, but not perfectly.** Details in the table below. The ~2k HT figure is rounded down from 2,250. The FY25 base × pull-through sum is ~$3.06B against $2.94B of reported sequencing consumables, a 4% overshoot. This supports E003 and E041. It implies HT is ~69% of sequencing consumables.
- **FACT, a new inconsistency: the MiSeq base differs between decks.** The JPM deck (2026-01-13) shows ~8,860. The Q4'25 deck (Feb 2026) shows ~8,590. A restated total base appears nowhere. The JPM total is ~21k.
- **OPINION (calc): implied clinical Gb growth is about +35% to +60% in 2025–26, and the central estimate is above ">30%".** Details in the bridge below. Management's wording "clinical growth well above" 30% is consistent with this. It is unquantified, and the phrase first appears in Q1'26 and Q2'26.
- **FACT: Dhingra's Q3'25 answer limits research Gb growth.** Q3'25 call l.478: "the GB still grew, albeit below the 30% kind of number". That caps research Gb at under 30%. Clinical was "much, much stronger". The "clinical well above" language is therefore a mathematical necessity, not new information.
- **FACT: clinical-split activity data was disclosed in 2023 and then dropped.** Q1'23 call l.202: clinical sequencing activity +15% y/y, research −4%. Q2'23 call l.220: clinical +23%, research −1%. From Q3'23 only the total appears. The 2023 language said activity was "directionally correlated with revenue over time". From Q2'24 it became "not a predictor of near-term revenue" (Q2'24 call l.148; Q2'25 l.164 repeats it).
- **FACT: the transition-metric phase-out did not happen on schedule.** The Q4'25 deck (slide 10) says "we will phase out transition-specific metrics after Q4 earnings". The Q1'26 and Q2'26 decks still carry both X-share charts. E138 has this. The path to the real drop is concrete: the cohort slide appears only in the Q3'25 deck, and the install-base slide only in the JPM and Q4'25 decks.
- **FACT: the Q1'26 pricing question was only partly answered.** Souda asked about the "initial impact from 6,000 pricing to Nova X pricing for consumables within those labs… incorporated into the guide?" (Q1'26 call l.286). Thaysen answered on placements being "much more additional incremental" than conversions, and on research being converted. He gave no price impact for clinical labs (l.292–298).
- **FACT: Thaysen's Q1'26 line implies the remaining price headwind is clinical.** "We have now converted most of our Xs in the research business… we're not seeing the price headwind as we did before" (l.298). The same point appears in Q3'25 l.472 ("that pricing headwind is, of course, reducing").

## 1. Reconciliation: installed base, pull-through and capacity

I used the JPM Jan 2026 deck (slide 19, appendix) and the Q4'25 deck slide 15. Both are .md conversions of the originals. The JPM Strategy Day 2024 file is a call transcript only. No Strategy Day slide deck is in the corpus.

| Platform | FY25 base | Pull-through ($K) | Base × pull-through ($M) | Source note |
|---|---|---|---|---|
| NovaSeq X | ~890 | ~1,350 | ~1,200 | FY25 shipments ~260 |
| NovaSeq 6000 | ~1,360 | ~670 | ~911 | ~30 shipments, ~330 decommissions |
| NextSeq 1k/2k | ~2,990 | ~90 | ~269 | |
| NextSeq 500/550 | ~3,460 | ~100 | ~346 | |
| MiSeq (all) | ~8,860 JPM / ~8,590 Q4 deck | ~30 | ~266 / ~258 | The two decks differ |
| MiniSeq/iSeq | ~3,840 | ~20 | ~77 | |
| **Total** | **~21.4k** | | **~3,070 (calc)** | vs $2,939M reported seq. consumables, including China |

- HT is ~$2.11B of ~$3.07B, or ~69% (calc). That supports the 69% HT share assumed in E003.
- The 6000 is ~43% of the HT product (calc), which supports E041.
- Slide footnotes: the HT figures exclude HiSeq. The base includes reagent-rental units and excludes decommissions. Pull-through is "average annualized… per instrument".
- The ~4% overshoot probably comes from year-end bases being larger than average bases. This is my inference. The deck does not say.
- JPM slide 4 "~2k HT" is 2,250 on the slide-19 numbers, a ~11% rounding-down. This resolves gap 2: the figures reconcile and no missing group is needed. It still leaves the Q1'26 and Q2'26 6000 base unknown (E020).
- HT capacity "~2x 2022–2025" is "theoretical max output on active HT installed base" (JPM slide 4 footnote 2). A 3-year span gives a ~26% CAGR, and a 4-year span (if 2022 is the start year) gives ~19%. The deck does not say which. I assumed 3 years, as E189 did.
- Calc on stated Gb growth: the cumulative Gb growth over FY23–25 was roughly 1.3 × 1.4 × 1.3 ≈ 2.4x. That is an input-weak estimate, since the 2023 figures are run-based. Against ~2x capacity, it implies utilization rose ~15–20%. OPINION.

## 2. Clinical Gb growth bridge

Method: implied clinical Gb growth = (1 + clinical ex-China revenue growth) / (1 + clinical $/Gb change) − 1. All results are OPINION (calc) on FACT inputs from the decks (clinical growth, E186 shares, E187 ratio).

**A. Stated-price method.** Gb growth required at an assumed price change.

| Quarter | Clinical rev growth | Gb needed at −15% price | Gb needed at −25% price |
|---|---|---|---|
| Q1'24 | 7% | 26% | 43% |
| Q2'24 | 5% | 24% | 40% |
| Q3'24 | 11% | 31% | 48% |
| Q4'24 | 8% | 27% | 44% |
| Q1'25 | 8% | 27% | n/a |
| Q2'25 | 10% | 29% | n/a |
| Q3'25 | 12% | 32% | n/a |
| Q4'25 | 20% | 41% | n/a |
| Q1'26 | 20% | 41% | n/a |
| Q2'26 | 15% | 35% | n/a |

- Q3'24 at −25% gives clinical Gb of ~48%. That is consistent with the total ">40%" stated that quarter and with Dhingra's "about 25% decline on the price" (E048).
- At the −15% long-run assumption, 2025 clinical Gb growth sits near the 30% floor, so "well above" 30% is not needed until Q4'25.

**B. Mix-only price method (clinical X Gb share from E186).** Price index = 1 − (1 − r) × s, where s is the clinical X Gb share and r is the X-to-6000 $/Gb ratio.

| Quarter | y/y price change, r = 0.295 | Implied clinical Gb, r = 0.295 | y/y price change, r = 0.40 | Implied clinical Gb, r = 0.40 |
|---|---|---|---|---|
| Q2'25 | −17% | +32% | −14% | +27% |
| Q3'25 | −21% | +42% | −17% | +35% |
| Q4'25 | −24% | +57% | −19% | +48% |
| Q1'26 | −28% | +65% | −22% | +53% |
| Q2'26 | −28% | +60% | −22% | +47% |

- The bridge ignores list-price increases (E033), the under-filled-flow-cell premium (E032) and the −16% to −24% repricing of the 6000 itself (E053). A further −5% within-platform price would lift the implied range by ~5%. Offsets could push it either way.
- Clinical consumables also include NextSeq and other MT instruments (clinical share is not HT-only). This is a source of error.

**C. Cross-check against total HT Gb (E008 method).** Total HT mix gives −19% price and a +4.7% HT revenue increase, so total HT Gb is ~+30%. Research ex-China consumables are −7%. Research X share rose 82→92%, which gives a −17% price index and implies research Gb of ~+12%. If clinical was ~56% of HT Gb a year ago, then 30% = 0.56 × g + 0.44 × 12%, so clinical HT Gb ≈ **+44%**. This conflicts with the 47–60% from method B. The gap is the clinical-vs-HT scope difference plus the sensitivity to r.

**Implied range:** +35% to +60% for 2025–26. The tightest central estimate is +40–50% for H1'26 (methods A at −20% price, B at r = 0.4, and C). The customer evidence fits the range. Natera MRD +56%, Guardant oncology +63% and Adaptive +43% (E081) are above it. GeneDx +32% exome/genome is below it. Those are test counts and exclude intensity.

COGS-per-test check (E043, E044, E091):
- Adaptive's gross margin rose 64→72% with price flat (assumed), so COGS per test fell ~22%. That is less than the 28% price change in method B, because sequencing is only part of COGS.
- Guardant's −$200 per test fits a ~25–30% sequencing cost cut on a ~$700 test, if sequencing is ~$300 of COGS (my assumption).

Implication: price erosion per clinical Gb is probably in the 20–28% range, not the mid-teens. Volume growth of 40%+ is what holds revenue growth at 15–20%. The system is tracking a faster treadmill than the mid-teens model implies. If the 35B cut hits at −20% on top (E057, E058), clinical Gb must grow >25% to stay neutral (E084). Method A and B imply it is already running above that.

## 3. What counts as "clinical" (call and filing grep)

| Date | Statement | Source |
|---|---|---|
| Q1'23 | "clinical sequencing consumables revenue representing 50%" | Q1'23 call l.112 |
| Q4'23 | "now we have clinical about 50%" | Q4'23 call l.596 |
| Nov 2023 | "over 50%" (analyst) | Piper 2023-11-29 l.242 |
| Q4'24 | Dhingra: of total volume ~2/3 on X, "for clinical that's about 50%" | Q4'24 call l.272 |
| Jan 2025 | "56%" of consumables | JPM 2025-01-14 l.56 |
| Q2'25 | "roughly 60%" | Q2'25 call l.78, l.158 |
| Q1'26 | "more than 65%" of sequencing consumables | Q1'26 call l.94 |
| Q1'26 | Thaysen: "clinical, which is more than 60% of the placements" | Q1'26 call l.294 |
| Q2'26 | "approximately 65%" | Q2'26 call l.76 |

- New: the FY25 10-K and other 10-Ks use no "clinical" definition, and the phrase "Research & Applied" appears in none of the filings (zero matches in /filing). The segment taxonomy exists only in decks and calls. Filings say "translational and clinical markets" and "oncology, genetic health, and reproductive health" (10-K FY25 l.248).
- The decks use "Research & Applied" from Q2'25 on (first match is the Q2'25 deck). The 2023 calls used "Research & Applied" too (Q1'23 call l.202). No renaming event is visible. I found no explicit statement of what is excluded.
- The JPM Jan 2026 deck shows ~60% clinical vs ~40% Research & Applied, "as percent of sequencing consumables. Excludes ~3% Other, primarily consisting of infectious disease testing" (slide 4 footnote 3). So the ~97% split excludes infectious disease. That implies "Other" is outside both segments and the 60/40 pie sums to the 97%. It confirms the ledger's reading that the extract's 60/40 inversion (E079) is an extraction issue, not a company error. The footnote itself is new.
- Application split: oncology ~51%, genetic disease ~25%, reproductive health ~21% (JPM slide 4). These sum to 97%. No Gb or revenue by test type is in any deck. Slide 12 gives only qualitative intensity (">30% CAGR", "~15x Gb", ">120 Gb vs ~8 Gb for exomes). Gap 16 on application-level Gb remains unfilled.
- The TSO 500 point: Thaysen's Q4'23 call line 546–548 counts Illumina's own TSO 500 business (>$100M, "high double-digit growth") inside clinical LDT activity. That means Illumina's own kits are in the "clinical" bucket, which is a different customer type from a lab buying consumables.
- Bridge ~50% (Q1'23) → >65% (Q1'26). Clinical share = 50% → 60% over Q1'23–Q2'25 as research fell and clinical grew mid-to-high single digits. The final 60→65% step is in line with E076's arithmetic. The definition shift cannot be tested. No source describes a change in what is included.

## 4. Dropped or changed disclosures (dated)

| Disclosed | Period | Dropped or changed | Evidence |
|---|---|---|---|
| Clinical vs research sequencing "activity" growth, e.g. clinical +15% / +23% y/y | Q1'23, Q2'23 | Only totals from Q3'23. Clinical reappears qualitatively ("well above") from Q1'26. | Q1'23 call l.202; Q2'23 l.220; Q1'26 l.172 |
| Activity "directionally correlated with revenue over time" | Q1'23–Q4'23 | Q2'24 on: "not a predictor of near-term revenue" | Q4'23 call l.148; Q2'24 l.148; Q2'25 l.164 |
| Gb scope: runs in HT only | Q2'25 | HT+MT from Q3'25; ex-China unstated in scripts | Q2'25 call l.512 vs Q3'25 l.166 |
| "All values include pricing actions announced in Q1'25" footnote | Q2'25–Q4'25 decks | Absent from Q1'26 and Q2'26 deck text I found | decks Q2'25 l.46, Q4'25 l.43 |
| Transition Targets slide with ">75% Gb / >50% revenue" | Q3'25 | Q4'25 onward: charts only | Q3'25 deck l.76–94 |
| 40-customer cohort slide (revenue and Gb, labels only) | Q3'25 deck slide 9 | Not in Q4'25, Q1'26 or Q2'26 decks | Q3'25 deck l.174–197 |
| Installed base, shipments and decommissions table | Q4'25 deck slide 15, JPM Jan 2026 | Not in Q1'26 or Q2'26 decks | Q4'25 deck l.349–389 |
| FY26 pull-through guide by platform (X $1.35–1.40M; 6000 $600–650K) | Q4'25 deck | No update in Q1'26 or Q2'26 decks | Q4'25 deck l.380–381 |
| "We will phase out transition-specific metrics after Q4 earnings" | Q4'25 deck slide 10 | Yet Q1'26 and Q2'26 decks still show X shares | Q4'25 deck l.215; Q2'26 deck l.99–119 |
| Reagent-rental units in the base | Q4'25 deck, JPM Jan 2026 footnote only | Never counted in any deck | JPM deck l.129 |
| Net-basis base (decommissions removed) | Introduced Q4'23 call | Re-bases 6000 pull-through (E018) | Q4'23 call l.162 |

## 5. Unanswered or deflected analyst questions (Q1'25–Q2'26)

- **Souda, Q1'26 call, l.286:** asked about the initial 6000-to-X pricing impact in labs adding Xs and whether it is in the guide. Thaysen's answer (l.292–298) covered placements being incremental and research conversion. It gave no clinical price impact or guide inclusion. Rating: deflected.
- **Arias (Stifel), Q2'25 call, l.508:** asked whether Gb stays above 30% in Q3 and Q4 and whether the 2026 "mid-20s Gb, mid-teens price" framework holds. Dhingra answered "We think so" for clinical and ex-China. He did not address the 2026 framework or price. Partly answered.
- **Catherine (Q3'25 call, l.478):** the Q3'25 CFO answer to her question gave research Gb as "below the 30%" but no figure, and no clinical figure. Partly answered.
- **Peterson (Jefferies), Q2'26 call, l.240:** E014 and the correction stand. Thaysen did answer the sequential-slowdown half (15% vs 20%: US >20%, Middle East and LatAm drag; l.258). He did not answer the over-earning or dual-running half beyond "a standard part of the business" (l.246) and the HiSeq analogy (l.256).
- **Q2'25 call, l.484:** the other half of the same analyst's question ("how much of volume growth from clinical vs research") got only "clinical was stronger than the research segment" and "pricing… still very stable… within the expected range" (l.488–490). No numbers.

## Q3'26 (29 Oct) print checklist additions

1. Does the "Gb output… more than 30%" sentence recur, and is "clinical well above" quantified?
2. Is the 6000 base or X base restated? Reconcile to ~1,360 and ~890 (E020) and flag a changed MiSeq base.
3. Does the X revenue share move above 59% while volume share is ~84%? The r ratio (E187) is the key test.
4. Ask for the Gb metric's China scope and the shipped-vs-consumed gap.
5. Is the Q3'25 "pricing actions" footnote reinstated for the Jan 2027 list-price changes?
6. Souda's unanswered question: what is the clinical lab's first-year price impact?

## Contradictions and stale data

- E010/E046 "volume share" is Gb *shipped*, which is not volume consumed (new).
- MiSeq base 8,860 (JPM) vs 8,590 (Q4'25 deck). Total ~21k unaffected (new).
- The ~2k HT figure on JPM slide 4 vs 2,250 from slide 19 (rounding, new detail for E189).
- Method B (47–60% clinical Gb) vs method C (~44%) disagree. The disagreement is not resolved.
- Management's "mid-teens price decline" vs a 20–28% mix-implied clinical decline (E047, E187 inputs). OPINION.

## Gaps / what I could not find

- No original PDFs. The Sources folder holds .md conversions only. Slide values are from OCR-style chart text, and axis values for the cohort slide are not recoverable.
- No Strategy Day 2024 slide deck exists in the corpus, only the call transcript. I did not re-extract slides from it.
- No application-level Gb split. No sub-segment definition of clinical.
- The 2023 conference grep for "what we classify" returned nothing. Long lines were omitted by the tool in several calls, so some definitions may sit in lines I could not see (Q2'26 l.76, Q4'24 l.96, and the 10-K lines noted as omitted).
- I did not open the expert-call Sources for classification language, due to time. E077's coverage stands.
- Q1'26 Souda's full answer might continue after l.298 with a Dhingra segment on price. I read only to l.298.
