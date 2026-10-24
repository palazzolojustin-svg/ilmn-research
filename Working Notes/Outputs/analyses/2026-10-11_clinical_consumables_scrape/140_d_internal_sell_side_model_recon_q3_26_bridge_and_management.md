# Agent 140: D-internal-sell-side-model-recon-Q3-26-bridge-and-management-credibility-scorecard

*Model: sonnet. Run 2026-10-11 12:06:24. Cost $0.67 (API-equivalent).*

**Assignment:** Use only the local corpus: the Working Notes Extracts and Sources for the ILMN calls, decks, conferences, expert calls and sell-side notes, plus the ledger and all prior findings files in Outputs/analyses/2026-10-11_clinical_consumables_scrape. Do not repeat earlier assignments: 45 (HT revenue-at-risk bridge), 60 (contradiction audit), 76 (Q3'26 framework), 91 and 96 (dodged questions), 124 (6000 tail Q&A) and 128 (customer-level bottom-up). First read INDEX.md and 00_open_gaps.md, and grep the findings folder for the numbers cited below so you add something new. Produce four deliverables. (1) A single reconciled model for thesis Q1+Q2. Build a quarterly FY26-FY28 sequencing-consumables bridge that explicitly separates: (a) the 6000-to-X conversion of the remaining 17% of HT Gb at different relative $/Gb ratios (2.4x/3.4x/3.7x), (b) organic Gb growth by segment (clinical, research) with clinical at 20/25/30%, (c) within-platform price decline (5/10/15%), and (d) a 35B cut of -20% from Jan 2027, applied to what share of Gb (25B customers only versus all X). Show the 2026 Q3/Q4 and FY27 consumable dollars against consensus ($789M Q3'26E, $815M Q4'26E, FY27 $3,378M). State the break-even clinical Gb growth that keeps consumables at consensus, and the implied probability-weighted view. Use the ledger numbers; flag anything that contradicts them. (2) Sell-side scan: from the research notes and conference transcripts in the corpus, collect every analyst's explicit assumption for X price/Gb decline, the 6000 tail, clinical Gb growth and 35B, with the firm, date and quote. Show where the sell side differs from management's mid-teens / mid-20s model, and flag the outliers. (3) A management credibility scorecard from the calls only. For each quoted claim in the ledger's MANAGEMENT section (E138-E146) and the claims on the 6000 tail, rate whether later evidence confirmed, contradicted or left it unresolved. Add any fresh case from the transcripts that the ledger does not list, for example language shifts between consecutive calls on 'no cliff', 'headwind', 'conservative guide', the 'fully converted' cohort, or question topics that were dodged by Dhingra or Thaysen. Quote the lines. (4) A checklist for the Q3'26 call (~29 Oct 2026): 10 specific numbers or disclosures to look for, with the threshold that would confirm or refute over-earning. Return concise tables with citations (file, date).

## Key findings

**Verdict: partly new evidence.** The ledger already holds the bridge arithmetic (E001–E009, E187, E205, E210), the sell-side positions and most of the credibility cases. This pass adds:
- a reconciled quarterly break-even grid;
- the 14-week Q4 as the swing factor;
- a rounding band on the "ratio uptick";
- a language-arc case on "headwind";
- a Q3'26 checklist with model-derived thresholds.

All numbers below are my own hand-calculated arithmetic, so label them OPINION (calc). I had no code tool, so expect rounding of about ±1%. I did not open any original in `Sources/`. I re-read the Q4'25, Q1'26 and Q2'26 call extracts only where cited.

1. **Consensus needs more Gb growth than the 20/25/30% clinical grid.**
   - I anchored on Q2'26: HT $535M, X $316M, 6000 $219M, non-HT $240M, with HT Gb split 83/17 (E040, E050).
   - I applied the 6000 conversion pace you specified, the segment Gb growth and a within-platform X price decline.
   - I assumed clinical is 64% of HT Gb (agent 45), research Gb grows 10%, and non-HT consumables fall 1% a quarter.
   - On those assumptions, FY27 consumables come out at about $2.86–2.97B for clinical Gb of 20–30%, against consensus of $3,378M.
   - Consensus therefore embeds HT Gb growth of about 35% a year at a flat X price, or about 53% at −10%/yr price. That is roughly 50–77% clinical Gb growth.
   - This supports E205 (clinical Gb +35–60%) over E083 (+23% base). It also means a 20/25/30% grid is bearish relative to what consensus assumes.

2. **Management's own model (Gb +25–30%, price −15%) gives only +6–10% before the 6000 tail.** The tail costs about 5 points a year at the observed run-off pace (about −2.7% a quarter), so net growth is roughly 0–5%. Consensus FY27 is +8.8% ($3,378M vs $3,104M FY26). This arithmetic does not depend on my quarterly model.

3. **Backtest.**
   - The same model applied to Q1→Q2'26 predicts HT of about +1% q/q. The actual was +6.8% ($501M→$535M, E040).
   - Either Q2 held one-offs or true Gb growth is far above the mid-20s model (consistent with E205's +45% central).
   - The Q3 print decides which.

4. **The 14-week Q4 is the largest uncertainty in the Q4 bar.**
   - Agent 76 confirmed the extra week sits in Q4 (correcting E184). The Q2'26 call extract gives it as "0.5 point", which is about $23M of FY revenue.
   - If the extra week is worth $0 / $23M / the full 1/13, the Q4 consensus of $815M is $815M / $792M / $757M on a 13-week basis.
   - Against Q3 consensus of $789M, that is up 3% / flat / down 4%.

5. **The ratio "uptick" is within rounding noise.**
   - Reported shares are whole percentages. The Q2'26 X/6000 $/Gb ratio is 0.279–0.312 (a 3.2–3.6x relative price) once the ±0.5-point band on both shares is applied.
   - Q1'26 is 0.254–0.283.
   - The bands overlap at 0.279–0.283, so the move from 0.27 to 0.30 that agent 05 and Barclays read is not statistically established. This qualifies the sell-side reading (file 05, finding 3).

6. **Language arc on "headwind," same arithmetic.**
   - Feb 2026: blended consumables "still face headwinds".
   - Apr: the price headwind is "receding".
   - Jul: not "a true headwind".
   - Over the same period the 6000 stayed at 41% of HT revenue and the implied ratio stayed at 0.30.
   - Details are in the scorecard below.

## 1. Reconciled quarterly bridge (FY26 Q3 to FY27)

**Structure.** Index Q2'26 HT Gb = 100, split X 83 and 6000 17.
- X $/Gb = $316M/83 = $3.81M per index point.
- 6000 $/Gb = $219M/17 = $12.9M per index point (3.39x).
- Organic Gb growth lands on X. Remaining 6000 Gb = 17 × (1 − c), where c is the cumulative share converted. c is 12.5% in Q3'26, 25% in Q4'26, 60% in Q4'27 and 80% in Q4'28 (agent 45's phasing).
- Conversion loss per converted Gb is 1 − 1/ratio: 58% at 2.4x, 70.5% at 3.4x, 73% at 3.7x. The ratio sets the price of the Gb that leaves, not the volume.
- Within-platform price applies to X Gb only. A 6000 repricing would be additive.
- The 35B's −20% is applied from Q1'27 and is shown as a separate layer.

**Central case** (clinical +25%, research +10%, X price −10%/yr, 3.4x, no 35B):

| Quarter | X rev $M | 6000 rev $M | HT $M | + non-HT $M | Total $M | Consensus $M |
|---|---|---|---|---|---|---|
| Q3'26 | 333 | 192 | 524 | 238 | **762** | 789 |
| Q4'26 | 349 | 164 | 513 | 235 | **748** | 815 |
| Q1'27 | 363 | 145 | 508 | 233 | 741 | n/a |
| Q2'27 | 376 | 126 | 502 | 231 | 733 | n/a |
| Q3'27 | 390 | 107 | 496 | 228 | 725 | n/a |
| Q4'27 | 403 | 88 | 491 | 226 | 717 | n/a |
| **FY27** | 1,531 | 465 | 1,997 | 918 | **~2,914** | 3,378 |

**FY27 swings from the central case** (all OPINION calc, linear):

| Lever | Setting | FY27 effect |
|---|---|---|
| Clinical Gb growth | 20% / 30% (central 25%) | −$58M / +$58M (about $11.6M per clinical point) |
| X price | −5% / −15% (central −10%) | +$87M / −$87M |
| Relative $/Gb ratio | 2.4x / 3.7x (central 3.4x) | +$50M / −$10M |
| Conversion pace | 40% / 80% by Q4'27 (central 60%) | +$97M / −$97M |
| 35B −20% from Jan 2027, 25B customers only (assume about 50% of X Gb) | | −$153M |
| 35B on all X Gb | | −$306M |
| 35B at 25% effective adoption (staggered rollout) | | −$77M |

- The 35B's scope is not in the corpus (E028 says only that the largest cohorts use 25B). The 50% share is my assumption. Whether the mid-teens price model already contains it is also unknown (agent 76).
- Reading these levers, the central case sits about 14% below consensus. Applying the −$58M clinical, −$87M price and −$153M 35B (25B only) swings to the central case gives about $2.6B. Consensus therefore does not look like a bear-case miss.
- The anchoring problem is point 3 above: the model's central case under-predicted Q2. Treat the level as a stress test and use the break-even grid below as the usable output.

**Break-even HT Gb growth for consensus, annualised.** Clinical equivalent = (HT growth − 3.6)/0.64.

| Case (conversion by that quarter; X price/yr; 6000 rev) | Needed HT Gb growth | Clinical equivalent |
|---|---|---|
| Q4'26: 25% conv; −10%; $164M | 63% | 93% |
| Q4'26: 25% conv; flat | 49% | 70% |
| Q4'26: 12.5% conv; flat; $192M | 36.5% | 51% |
| Q4'26: 0% conv; flat; $219M | 25% | 34% |
| Q4'26 at 12.5% conv, flat, if the extra week is $23M | 23% | 30% |
| Q4'26 at 0% conv, flat, if the extra week is the full 1/13 | below Q2 | none needed |
| Q3'26: 12.5% conv; −10% | 55% | 80% |
| Q3'26: 12.5% conv; flat | 43% | 61% |
| Q3'26: 2.7% conv (Q1→Q2 pace, 6000 about $213M); flat | 23.5% | 31% |
| Q3'26: 2.7% conv; −10%/yr | 34% | 47% |
| Q3'26: 0% conv; flat | 18.5% | 23% |

**Break-even clinical Gb growth that holds consensus.**
- Q3'26: about 31% (flat price, historical run-off) to 47% (−10%/yr price).
- Q4'26: about 30% to 51% if the extra week is worth about $23M, and under 20% if it is worth the full 1/13.
- FY27: about 50–77%.

**Probability-weighted view** (OPINION; weights are my judgment):
- 35% that Q3 clears $789M, because the 14th week and strong Q2 momentum carry it.
- 40% that it lands $765–789M. This would be a "beat-by-the-bar, flat sequentially" result.
- 25% that it comes in below $765M, which would be a clear sign of over-earning unwinding.

For FY27 the central case sits below consensus and the balance of risk is down. Roughly 60% of the probability is that FY27 comes in below $3,378M, with an expected shortfall of 4–8% of consensus. This view rests on the unvalidated central case, so treat it with caution.

## 2. Sell-side scan: delta only

File 05 and the ledger already hold the notes. No broker in the corpus gave an explicit numeric X $/Gb decline, 6000 tail assumption or 35B revenue impact (file 05, "Gaps"). Where the sell side differs from management's mid-teens price and mid-20s volume model:

| Firm and date | Assumption relevant to the model | Versus management |
|---|---|---|
| JPM, 2026-06-10 / 07-31 | Transition pricing headwinds "largely gone exiting this year"; ROW clinical +low/mid-teens CAGR through 2030; FY27 revenue +9.1% | Revenue growth above management's HSD. **Outlier on the high side.** The clinical CAGR implies deceleration. |
| JPM survey, 2026-06-10 | Clinical volume +14.6% (2027), +19.1% (2028) vs spend +9.4% / +14.0%; implied price −4–5% | Price far milder than mid-teens. Volume below the mid-20s. |
| Barclays, 2026-07 | 5.5% revenue CAGR; "another round of pricing headwinds in 2027 and beyond"; 35B "would need to be priced to compete" | Bear side. Agrees with the 35B layer. |
| Freedom, 2026-08-05 | Transition completion "should help mitigate the impact of pricing erosion"; 5.5% consumables CAGR | Aligned with management. |
| BI, 2026-05-01 / 07-31 | "Early stages of trading price for volume"; "60 placements" goal "less meaningful" | Agrees that price is falling. |
| UBS, 2026-02-26 | Expert expects 35B to bring Illumina to about $150/genome (from $175) | The only sizing of the 35B cut, and it is hearsay. |

**Where the sell side differs from consensus mechanics.** FY27 consensus consumables of $3,378M (+8.8%) sit above what the sell side's own growth rates imply for total revenue (+4–6%). Barclays 5.5% and UBS 4.1% imply consumables well below +8.8% once instruments and services are included, while JPM (+9.1%) is the only note consistent with consensus. Treat this as OPINION from my cross-check of file 05, not a broker statement.

## 3. Management credibility scorecard (calls only)

Rating key: C = confirmed by later evidence, X = contradicted, U = unresolved.

**Ledger MANAGEMENT section, E139–E146.** E138 is not readable in the file.

| E | Claim | Rating | Basis |
|---|---|---|---|
| E139 | Disclosure withheld when unfavorable, given when favorable | C | Pull-through shown as ">$1M" in Aug 2024, and as a FY26 guide of $1.35–1.40M. Cohort and transition metrics later dropped (E020). |
| E140 | Guidance record | C | FY23–24 missed; FY25 matched; FY26 raised twice. |
| E141 | 2026 guide path | C | Beats at Q1 and Q2. **U** on whether H2 is conservative (Freedom: no longer "conservative"). |
| E142 | Q4'25 pre-announce | U | No explanation in the calls for the $0.05–0.08 beat. |
| E143 | Low-ball pattern | C | Placements guided 50–60 a quarter, delivered 80–100+. |
| E144 | "Didn't pull anything forward" vs prepared remarks | X | The ledger records the contradiction. |
| E145 | Segment/definition changes | C | "ROW organic" is the headline. Q1'26 total organic +1.2% against clinical +20%. |
| E146 | 26% margin target | U | Softened to "within 50 bps". Test is FY27. |

**Claims on the 6000 tail and transition (from the calls):**

| Date and speaker | Quote | Later evidence | Rating |
|---|---|---|---|
| Q2'25 call, Thaysen | Placements "will have a meaningful H2 impact, though not a cliff" | Clinical ex-China growth +12% Q3'25, +20% Q4'25, +20% Q1'26, +15% Q2'26 | U (fits so far) |
| Q2'25 call, Thaysen | "We are not committing to a 30B at this point." | The 35B is now expected H1 2027 (E214). | U (mild shift) |
| Q4'25 call, Thaysen | Customers keep the 6000 "for validated, traditional assays, so pull-through stays up" | 6000 pull-through guide $600–650K vs $670K FY25. More than 10 new 6000s sold in Q2'26. | C |
| Q4'25 call, Thaysen | "There will be fewer 6000 customers over time." | No decommission count since Q4'25 (E020). | U |
| Q4'25 call, Dhingra | Research 6000→X "substantially complete"; clinical in "latter part"; "mostly done by volume" by end-2026 | Q2'26: research 92%, clinical 78% (target 80–85%), total 83%. But revenue share is only 59% and the "% of HT Gb Shipped" metric is capacity sold (E204). | C on volume. U on revenue. |
| Q4'25 call, Thaysen | Blended consumables "still face headwinds" | | arc below |
| Q1'26 call, Thaysen | "The price headwind is receding as more consumables move to X." Clinical placements are "mostly incremental... rather than conversions of 6000s" | Q2: X revenue share 55%→59% on volume 82%→83% | U (ratio change within rounding) |
| Q1'26 call, Dhingra | "No change in pricing-transition assumptions"; price effects "already in the guide" | Guide raised twice since | C so far |
| Q2'26 call, Thaysen (to Jefferies) | The 6000 is "a standard part of the business"; "not a true headwind"; HiSeq comparison | The over-earning and parallel-running part of the question was not answered (E014) | U |
| Q2'26 call, Thaysen | "It's not a cliff. It's a wave, and we are surfing it." | Same word used in Q2'25 about placements | U |

**Fresh cases not in the ledger:**
1. **Headwind arc.**
   - Feb 2026, Q4'25 call: blended consumables "still face headwinds."
   - Apr, Q1'26 call: the price headwind is "receding."
   - Jul, Q2'26 call: the 6000 is "not a true headwind."
   - Meanwhile the 6000 stayed 41% of HT revenue and the implied ratio stayed about 0.30. The language softened while the underlying split barely moved. OPINION.
2. **The Q4'25 parallel-running admission.** The Q4'25 answer to Guggenheim ("keep the 6000 for validated assays") is itself management confirming the dual-running behavior that the Q2'26 answer to Jefferies avoided.
3. **"Cliff" reused.** Thaysen used "cliff" in Q2'25 (placements→consumables) and again in Q2'26 (clinical). The analyst introduced it in 2026 (Leerink: "no clinical cliff"). In both uses it denied a sudden drop in a quantity that no disclosure measures.

## 4. Q3'26 checklist (call ~29 Oct 2026)

| # | Metric | Confirms over-earning if | Refutes if |
|---|---|---|---|
| 1 | Sequencing consumables | Below $775M (sequential decline) | At or above $789M with 13 weeks |
| 2 | Derived 6000 revenue (HT × (1 − X revenue share)) | At or above $219M (not running off) | At or below about $213M (pace of −2.7% q/q or faster) |
| 3 | X share of HT revenue / volume | Revenue share below 60% or volume stuck at 83% (but move needs >3 pts to beat rounding) | 61%+ and 84–85% |
| 4 | Ex-China clinical growth | Below 12% | 13–16% (comp is +12%) |
| 5 | Clinical Gb language | "Well above 30%" dropped or restated lower | Retained, or a number is given |
| 6 | X pull-through | Below $1.20M annualized | At or above $1.21M, with $1.35M guide kept |
| 7 | Q4 guide on a 13-week basis | Management cannot or will not size the 14th week; implied Q4 below about $790M ex-week | Extra week sized at $25M or less, and Q4 ≥$815M |
| 8 | 35B | List change of ≥15% effective Jan 2027 on existing customers (about $150M FY27 at 50% scope) | Pricing limited to new customers or phased |
| 9 | Disclosure | Pull-through guide, X/6000 base, "% HT Gb" slide or 83%/59% dropped | All retained, or 6000 decommission count restored |
| 10 | 6000 unit sales | More than 10 new 6000s again | None, or a decommission count |

## Contradictions and stale data

- My central FY27 ($2.9B) is far below consensus ($3.4B) because it takes your Gb grid at face value. The backtest (point 3) shows the model under-predicts Q2.
- The ledger's E205 (+35–60% clinical Gb) and E083 (+23%) are still unreconciled. The break-even grid supports E205 on the consensus-implied side.
- The 0.27→0.30 ratio uptick (agent 05, Barclays) falls inside rounding bands.
- E184 still reads "Q3 14 weeks." Agent 76 corrected it to Q4. The "0.5 point" does not equal 1/13 of Q4 consumables (E269).
- All UBS and Bloomberg Intelligence 2025 sections predate the Q1 and Q2 prints (file 05).

## Gaps / what I could not find

- I did not open any original in `Sources/`. All sell-side quotes are from file 05, not rechecked.
- No numeric X $/Gb, 6000 tail or 35B revenue assumption from any broker.
- No sourced split of X Gb on 25B vs 10B flow cells, and no sourced clinical share of HT Gb (I used agent 45's 64%).
- No clinical 6000 instrument count and no dual-running customer count (E020).
- No Q3'26 non-HT consumables guide, so the −1%/qtr is an assumption.
- I did not mine the Q3'24–Q2'25 calls for further language-shift cases beyond those cited.
