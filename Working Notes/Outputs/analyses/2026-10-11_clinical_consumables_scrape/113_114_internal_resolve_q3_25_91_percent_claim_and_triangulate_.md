# Agent 113: 114-internal-resolve-Q3-25-91-percent-claim-and-triangulate-NovaSeq-6000-revenue-three-way

*Model: sonnet. Run 2026-10-11 10:55:29. Cost $0.93 (API-equivalent).*

**Assignment:** Close open gaps 3 and 4 from 00_open_gaps.md using only the local corpus. Do not repeat the Gb reconciliation or the margin-bound work already done by agents 28, 52, 60, 108 and 112.

(1) Resolve the Q3'25 call line that 'pricing headwinds ease now that 91% of high-throughput volume is on the X'. Open the ORIGINAL Q3'25 transcript and deck under Sources/ILMN, not just the Extracts. Quote the exact sentence and the surrounding Q&A. Work out whether 91% is the research-only share, a cluster or flow-cell share, a shipments share, a 'connected instruments' share, or a chart in the deck, and compare it with the 78% HT Gb share (E046). Then list every X-share figure management gave at each call and conference from Q2'24 to Q2'26. Give the denominator and the wording for each, and flag every change in definition (HT versus all sequencing, Gb versus revenue, research versus clinical, period-end versus average).

(2) Triangulate Q2'26 NovaSeq 6000 consumables revenue three ways. (a) HT revenue × (1 − 59%). (b) 6000 installed base × the pull-through guide ($600-650K annualised, divided by 4, using the average base after decommissions). (c) Implied by the sequencing consumables total minus X, NextSeq and other. Show the quarterly series Q3'25 to Q2'26 for each method, the gap between methods, and what the gap implies about 6000 pull-through, double-counted parallel use, or unreported items. Also pull the 6000 decommission cadence and any 'end of life', 'trade-in', 'price protection' or 'last-time-buy' wording from the corpus.

(3) Using the Q1'26 and Q2'26 sell-side Extracts only, list each analyst's stated bridge for the gross-margin change (tariffs, mix, 6000 inventory, X ramp, and so on) and any estimate of the 6000's gross margin versus the X's. Quantify the revenue and gross-profit at risk if all 6000 volume converts at a >60% price-per-Gb decline with +X% volume uplift, for X = 0, 15, 30 and 50. Return a short table and a list of the exact quotes you relied on, with file and date for each.

## Key findings

1. **FACT: The "91% of high-throughput volume" line is a misstatement. The 91% is the research-and-applied (R&A) share.** In the same Q3'25 call, the CFO's prepared remarks say "roughly 78% of volumes and 51% of revenue in Q3 was sequenced on X. 91% of research volumes were sequenced on X. The clinical X transition has progressed to roughly 64% of volumes." Further on, the closing outlook says "pricing headwinds easing now that 91% of high throughput volume has transitioned to X" (Extracts/ILMN/earnings_call, 2025-10 call; checked against `Sources/ILMN/earnings_call/ILMN_2025Q3_Earnings_Call.md` lines 150 and 204). This closes open gap 4.
2. **FACT: The Q3'25 deck confirms it.** Slide 5, "Transition Targets Update", plots Total, Research & Applied and Clinical panels. Its extracted labels include 91%, 78%, 64%, 51% and 36% (`Sources/ILMN/deck/ILMN_2025Q3_Earnings_Slides.md` line 157). The text extraction doesn't tie labels to series, but 91% matches the call's R&A figure. The Q3'25 total of 78% on slide 5 agrees with E046, so there is no conflict with E046. The Q3'25 total X share of HT Gb was 78%, and the 91% figure applies to a research-only denominator.
3. **FACT: The 91% is not a cluster, flow-cell, shipments or connected-instrument share.** I found no sentence in the call or deck that gives 91% on any of those bases. The next two R&A prints are "roughly 90%" (Q4'25) and "90% of research" (Q1'26), so it reads as a stable research-only series.
4. **MGMT/OPINION: The wrong denominator inflated the "pricing headwind is fading" message at the point of the 2026 outlook.** For total HT, Gb share was 78% and revenue share only 51%, so the unconverted 6000 base was larger than "91%" implies. Clinical volume was only 64% converted. The clean read is that research is nearly finished converting, while clinical still has about a third of its volume on the 6000.
5. **OPINION (calc): The three-way triangulation of Q2'26 NovaSeq 6000 revenue lands at roughly $190–230M, consistent with E003's $219M.** The three methods are (a) $219M, (b) ~$196–215M, (c) ~$188–228M. Details are in the next section.
6. **OPINION (calc): The FY25 bottom-up check, built from the deck's pull-through and base figures, reconciles to reported consumables.** I summed base × pull-through for all six platforms (Q4'25 deck slide 15, `Sources/ILMN/deck/ILMN_2025Q4_Earnings_Slides.md` lines 375–381). On average FY25 bases the total is ~$2.98B, against reported FY25 sequencing consumables of $2,939M, within about 1.5%. On year-end bases it is ~$3.06B. HT comes to ~68% of the total, matching E003's 69% assumption. The 6000 comes to ~$1.01B, about 50% of HT, against ~52% implied by the reported average X revenue share (43/44/51/55%). This strengthens E041, which it narrows from "consistent" to "within ~2 points".
7. **OPINION (calc): The 6000's implied annualised pull-through is flat at ~$670–700K, above the $600–650K FY26 guide.** Method (a) divided by an estimated active base gives $685K, $669K, $679K and $698K for Q3'25 through Q2'26 (assumptions below). That is at or above the top of the guide. If the guide is right, either the base is smaller than I assume or HT is above 69% of consumables. Otherwise the 6000's per-unit use isn't falling, which would fit parallel running. This quantifies E017.
8. **FACT: The relative revenue per Gb of the X versus the 6000 has fallen from ~45% to ~30%.** From the reported volume and revenue shares, the ratio is 0.45 (Q2'24), 0.35 (Q1'25 to Q2'25), 0.29 (Q3'25), 0.31 (Q4'25), 0.27 (Q1'26) and 0.29 (Q2'26). The ratio is X revenue per Gb divided by 6000 revenue per Gb. This is derived from reported shares, so it is a calc on FACT inputs. It says the Gb still on the 6000 earns about 3.4 times the revenue per Gb of the X, consistent with Barclays' report of management saying the 6000 volume is on smaller panels with higher revenue per Gb (finding 11). It also implies a realised price-per-Gb gap of about −70% on conversion, the top of management's "60% to 70%" range.
9. **OPINION (calc): Converting all 6000 volume costs $350–613M of annual revenue at a −60% to −70% price per Gb, even with +50% volume.** The exact grid is in the scenario table. Revenue is only neutral if volume rises by ~150% (at −60%) or ~233% (at −70%).
10. **MGMT (new, supports E130): The CEO said in Q2'25 that some customers will stay on the 6000 "until the end of life" of the assay, "maybe… 2 years more".** The full quote: "customers that will stay on the 6000 until the end of life, so to say, for the assay, where they feel like they maybe have 2 years more end of life. And it's simply from a financial perspective, it doesn't make sense for them to spend the energy and the investment to shift it over to the X" (Q2'25 call, `Sources/ILMN/earnings_call/ILMN_2025Q2_Earnings_Call.md` line 412). E130 only had this as ex-employee hearsay. This is management itself saying a tail of 6000 volume is deliberately not converting, which is a source of over-earning that persists.
11. **MGMT: Jefferies asked directly about over-earning, and the answer did not address parallel running.** The Q2'26 question was "are you over-earning on consumables because at some point, the 6000 get decommissioned… customers running both in parallel eventually wears off?" The CEO answered that "we did see some customers actually purchasing a few 6000 this quarter" (over 10 per the call), that "eventually, they will move over to X, but we don't see that as… a standard part of the business" (transcript garbled at this point), and that it is like the HiSeq roll-off, "not… any true headwinds". The answer gave no volumes, no timing and no pull-through effect (`ILMN_2026Q2_Earnings_Call.md` lines 240–256). Ameriprise recorded the same line as "a normal transition dynamic rather than an identifiable consumables headwind" (Ameriprise, 2026-07-31).
12. **FACT: Sell-side bridges for gross margin are thin.** No Q1'26 or Q2'26 note gives a basis-point split. No analyst gives a gross margin for the 6000 versus the X. Details in the sell-side section.
13. **FACT (new, minor): The CFO said in Q2'26 that new placements are "still about 70-30, 70% being clinical"** (Q2'26 call line 452). This is above the earlier ">60%" (Q4'25, Q1'26 calls). JPM recorded management saying "as much as half of clinical placements appear to be incremental" rather than upgrades (JPM Q2'26 recap, 2026-08-05).

## (1) 91% claim and the X-share series

### Exact quotes (Q3'25 call, Sources/ILMN/earnings_call/ILMN_2025Q3_Earnings_Call.md)
- CFO prepared remarks, line 150: "The X transition progressed significantly in Q3, roughly 78% of volumes and 51% of revenue in Q3 was sequenced on X. 91% of research volumes were sequenced on X. The clinical X transition has progressed to roughly 64% of volumes in the quarter."
- CFO closing outlook, line 204: "Second, in research and applied, we anticipate conditions to remain muted, consistent with the latter half of 2025, with pricing headwinds easing now that 91% of high throughput volume has transitioned to X."
- CFO Q&A, line 628, answering Subbu: "the vast majority of our -- the volumes in the research market have transitioned to X, implying that as and when those markets return to growth or even in a stable environment, the actual pricing headwind should start to dissipate". Here the same point is made correctly, about the research market.
- CEO prepared remarks, line 124: "Clinical will continue to be our primary near-term driver of revenue growth as NovaSeq X volume more than offsets conversion pricing headwinds."

The sentence in the outlook sits in a paragraph about research and applied, so the speaker meant research volume. There is no later correction in the transcript. I did not search other sources for one.

### X-share figures by call and conference
Denominators are "HT" (NovaSeq X plus NovaSeq 6000) unless noted. Shares are of Gb shipped (E-ledger note: this is shipped Gb, not consumed Gb). Wording is as spoken.

| Date / source | Figure | Wording and denominator |
|---|---|---|
| Q2'24 call | ~45% Gb; "a little over 25%" HT revenue | "approximately 45% of high-throughput giga bases sequenced and a little over 25%… of high throughput consumables revenue, was on NovaSeq X Plus." "Sequenced" is used here, not "shipped". |
| Q3'24 call, Dec 2024 Evercore | >55% Gb; >35% revenue; clinical ~40% | CFO, Dec 2024: "in Q3, we said roughly 55% of the volume, 55% of the volume, which equates to 35% revenue, is now on X. On the clinical side, that's about 40% has already transitioned". |
| Q4'24 call | >65% Gb; ~40% revenue | "more than 65% of high throughput giga base is shipped and approximately 40% of high throughput consumables revenue". |
| Jan 2025 JPM | target 75% Gb, 50% revenue by 2H25 | "approximately 75% of total high throughput gigabase shipped and approximately 50% of total high throughput consumables revenue". |
| Q1'25 call | 68% Gb; 43% revenue; research >80%; clinical >50% | Research: "80% of high throughput gigabases shipped to our customers in research". |
| Q2'25 call | 69% / 44%; research >80%; clinical ~55% | Research: "over 80% of the sequencing volumes for our research customers". The unit moves from "gigabases shipped" to "sequencing volumes". |
| Q3'25 call | 78% / 51%; research 91%; clinical 64% | "volumes" and "sequenced on X"; the 91% is research-only; the closing line mislabels it HT. |
| Q4'25 call and JPM Jan 2026 | ~80% / 55%; research ~90% | JPM Jan 2026: "approximately 80% of high-throughput gigabases shipped". Q4'25: "research transition is nearing its end, as now roughly 90%". |
| Q1'26 call | 82% / 55%; research 90%; clinical 76% | CEO: "a little bit dangerous to look at this number too precisely". |
| Q2'26 call | 83% / 59%; clinical 78%; clinical target 80–85% by end-2026 | "approximately 83% of volumes and 59% of revenue had transitioned". |

### Definition changes to flag
- **Unit:** "gigabases sequenced" (Q2'24) became "gigabases shipped" (Q4'24, Q1'25, Jan 2026 JPM), then "volumes" and "sequenced on X" (Q2'25 onward). The decks define it as Gb shipped (ledger, correction at 241), so the "sequenced" wording on calls overstates the precision of consumption.
- **Denominator:** from Q1'25 the research and clinical cuts appear. Research is "high throughput gigabases shipped to customers in research" at first, then "research volumes". Clinical is only ever "clinical volume" (no HT qualifier stated).
- **Clinical target:** the Q1'26 call has the CEO saying "more than 85%… by end of this year" while the same call's prepared remarks say 80–85% (line 172). The Q2'26 call says "80% to 85%". The spoken "more than 85%" is looser than the written target.
- **Period-end versus average:** no call says which it is. The "as of Q2/Q4" wording suggests quarter-end or in-quarter shipments, but this is not stated.
- **Revenue share as read-through:** in Q1'26 the revenue share was flat at 55% while Gb share rose; management's explanation was mix, and the CEO called precise reading "a little bit dangerous" (Q1'26 call line 702). The Q4'25 deck said transition-specific metrics would be phased out after Q4, yet the Q1'26 and Q2'26 decks still carry them (per the segment-financials working note, Outputs/analyses/2026-10-11_ilmn_primer_working/01_segment_financials.md, section 6A).
- **Third-party misreading:** Barclays (2026-05-07) writes "overall NovaSeq X gigabase share rose 500 bps to 76%". 76% is the clinical share on the Q1'26 call; total was 82%. It is a Barclays error in the Extract, but it shows how the multiple cuts confuse readers.

## (2) Triangulation of 6000 consumables revenue

### Inputs (sources)
- Sequencing consumables, $M: Q3'25 747, Q4'25 755, Q1'26 726, Q2'26 775 (calls).
- X share of HT revenue: 51 / 55 / 55 / 59%.
- Deck, FY25 bases and pull-through: X ~890, $1.35M; 6000 ~1,360 after ~330 decommissions, $670K (FY26 guide $600–650K); NextSeq 1k/2k ~2,990, $90K; NextSeq 500/550 ~3,460, $100K; MiSeq ~8,590, $30K; MiniSeq/iSeq ~3,840, $20K (Q4'25 deck slide 15).
- HT = 69% of sequencing consumables (E003 assumption, corroborated by finding 6).

### My assumptions (OPINION, not disclosed)
The company gives no quarterly 6000 base. I assume decommissions at the FY25 pace (~82 a quarter) and placements of ~7 a quarter in 2025 and ~10 in Q2'26. That gives period-average 6000 bases of ~1,470 (Q3'25), ~1,400 (Q4'25), ~1,325 (Q1'26) and ~1,255 (Q2'26). For method (c), the X base is estimated from placements (Q3'25 >55, Q4'25 >100, Q1'26 >80, Q2'26 >95, assuming no X decommissions) and the 970 stated at Q1'26. Non-HT is held at ~$237M a quarter (the FY25 base × pull-through ÷ 4 for the four non-HT platforms), likely a little high in 2026 because the 500/550 base is shrinking.

### Quarterly series ($M, 6000 consumables)

| | Q3'25 | Q4'25 | Q1'26 | Q2'26 |
|---|---|---|---|---|
| (a) HT revenue × (1 − X share), HT = 69% | 252 | 234 | 225 | 219 |
| (b) base × pull-through ÷ 4, at $670K (2025) and $625K (2026 guide mid) | 247 | 234 | 207 | 196 |
| (b) at $650K guide top (2026) | | | 215 | 204 |
| (c) total − non-HT − X, with X at $1.35M pull-through | 253 | 234 | 175 | 194 |
| (c) with X at the ramp-adjusted $1.19–1.24M pull-through (E038) | | | 205 | 228 |
| Implied 6000 annualised pull-through from (a), $K | 685 | 669 | 679 | 698 |

### What the gaps say
- **2025 quarters:** the three methods agree within a few $M. That tells us the disclosed 2025 pull-through, the shares and the 69% HT assumption are internally consistent.
- **Q1'26 and Q2'26:** (a) runs $10–23M above (b). The gap is mainly one of two things. Either the 6000's real per-unit use did not drop to the guide's $600–650K, or the active 6000 base is larger than my decommission path (if only ~40 decommissions a quarter, Q2'26 base is ~1,330 and pull-through from (a) is ~$660K, in line with the FY25 level). Both mean the 6000 is not yet winding down in revenue terms, which supports finding 7 and the over-earning concern.
- **Method (c) is the least reliable:** it depends on how fast new X systems ramp. At the headline $1.35M it gives a Q1'26 figure of $175M, below (a) by $50M, which is not credible given that X units ramp over 6–9 months (Q2'26 call line 180). With ramp adjustment the gap to (a) is −$20M (Q1) and +$9M (Q2).
- **Parallel-use double counting:** none of these methods can separate it. A customer running a 6000 and an X on the same assay shows up in the X's Gb and revenue; the shares do not net it out. Parallel use would push up the 6000's apparent pull-through, which is the direction of the (a)-versus-(b) gap, but I cannot size it. Management has not disclosed any count of such customers.
- **Unreported items:** Greater China is inside the total consumables figure but its HT split is undisclosed; rental and lease units are inside the installed bases and may inflate pull-through (E039). The sequencing consumables figure also includes other items (for example, microarray is separate; service is separate) that I did not model.

### 6000 decommissions, end of life and related wording
- FACT: ~330 decommissions in FY25 (deck footnote: "NovaSeq 6000 active installed base accounts for ~330 decommissions in FY25"), against ~30 6000 placements. That is about 11 decommissions for each 6000 sold. In Q2'26 more than 10 6000s were sold (CEO and JPM).
- FACT: No quarterly decommission count appears in any 2026 deck or call, and the Q1'26 and Q2'26 decks have no installed-base slide by instrument (grep returned nothing).
- MGMT: "stay on the 6000 until the end of life" for the assay, "maybe… 2 years more" (Q2'25 call, above).
- The searches for "price protection", "trade-in" and "last-time buy" in the calls, conferences and decks returned nothing relevant. The only "trade in" hits in the 10-K files are insider-trading-policy text. I did not search the 10-Q MD&A lines marked omitted. The ledger's own "trade-in" hit (line 476) I did not open.
- The HiSeq precedent: the CEO noted "only a few quarters ago, we still had HiSeqs running in our portfolio" (Q2'26 call), so the 6000 tail may run for years, not quarters.

## (3) Sell-side bridges and the revenue and gross-profit at risk

### Each analyst's stated bridge (Extracts/ILMN/research)
No source gives a basis-point split, a tariff dollar figure, or a 6000-versus-X gross margin.

| Quarter | Source | Stated drivers |
|---|---|---|
| Q1'26 (68.2%, +80 bp y/y) | JPM, 2026-05-06 | "cost efficiencies and higher revenue, partially offset by tariffs" |
| Q1'26 | Freedom Broker, 2026-05-06 | "helped by cost efficiencies and higher revenue, partly offset by tariffs"; Q2 gross margin "may be pressured by a higher instrument mix and supply-scaling investments"; some inflation in Q2 |
| Q1'26 | Barclays, 2026-05-07 | 68.2% beat Street 67.1%, but slightly below Barclays' own 68.5%; margin guide "is not a layup by any means" (Q3 is the seasonally higher-margin quarter) |
| Q2'26 (68.2%, down 120 bp y/y) | JPM, 2026-08-05 | "driven by product mix (more instrument sales) and higher freight and memory costs" |
| Q2'26 | Freedom Broker, 2026-08-05 | "declined YoY because of inflation and the SomaLogic acquisition"; expects expansion "mainly on a richer consumables mix, more visible from 2027" |
| Q2'26 | Barclays, 2026-08-06 | 68.2% "labelled in line" with its estimate; no bridge |
| Company, Q2'26 call | CFO | "slightly better than our expectations, especially given product mix from the relatively high sales of instruments… higher freight and memory costs"; Q3 operating margin steps up ~100 bp, some from "higher mix of consumables", plus cost actions "within our gross margin" |

Observations:
- Gross margin was flat sequentially at 68.2% in Q1'26 and Q2'26. Q2 absorbed an instrument-heavy mix, which is lower margin than consumables.
- SomaLogic appears in only one bridge (Freedom). Management's own explanation doesn't mention it, so the drivers are inconsistent across sources.
- The ledger's −60 bp instrument-mix estimate (open gaps, item 7) is not corroborated by any analyst figure.
- Tariffs were last quantified by management at ~220 bp y/y in Q3'25 (Q3'25 call line 170). Tariffs are not quantified in the Q1'26 or Q2'26 sell-side notes.
- No analyst estimates the 6000's gross margin versus the X's. The only margin figure for the 6000 in the ledger is E367's 80–85% assumption (agent calc). I use it below and flag it as an assumption.

### Revenue and gross profit at risk
This is a calc (OPINION). Base case: 6000 consumables of $219M a quarter, $876M a year (method a). Revenue after conversion = $876M × (1 − price decline) × (1 + volume uplift). For gross profit I assume a 6000 gross margin of 82.5% (E367 midpoint: $723M) and an X gross margin of 70% on the converted revenue, both assumptions with no analyst support. Annualised, $M.

| Volume uplift X | Revenue after, −60% | Revenue lost, −60% | Revenue after, −70% | Revenue lost, −70% | Gross profit lost at −65% (X at 70% GM) |
|---|---|---|---|---|---|
| 0% | 350 | −526 | 263 | −613 | −508 |
| 15% | 403 | −473 | 302 | −574 | −476 |
| 30% | 456 | −420 | 342 | −534 | −444 |
| 50% | 526 | −350 | 394 | −482 | −401 |

- Break-even uplift: +150% (at −60%) or +233% (at −70%).
- At −65%, revenue lost is $569M (0%), $523M (15%), $477M (30%) and $416M (50%).
- Context: annualised Q2'26 sequencing consumables is ~$3.1B, so the revenue lost is ~11–20% of consumables. The Q2'26 core operating income of $261M (E367) annualises to ~$1.04B, so the gross-profit loss is about 38–49% of it before any offsetting cost cuts.
- This is an upper-bound exercise. It treats all 6000 volume converting at once, with the entire price gap realised. Mix, the 35B flow cell (a further ~20% $/Gb cut) and new volume are not included. The cohort data (volume offset price in year 1 for the "40 customers") and the "easily more than 60% to 70%" quote argue the tail will convert over years, not at once.
- The realised relative revenue per Gb (29–30%, finding 8) implies about −70%, so the −70% column is the one the data supports for the remaining Gb.

## Contradictions and stale data
- **91% mislabel:** discussed above. The ledger's E046 note "Q4'25 deck chart appears to show ~90% (possibly research-only)" is correct, and the correction at ledger line 209 already says so. I can add that the Q3'25 call itself calls 91% both "research volumes" (line 150) and "high throughput volume" (line 204).
- **Barclays 76%:** Barclays' Q1'26 note labels 76% as overall X Gb share; the call says total 82%, clinical 76%.
- **Clinical target wording:** "more than 85%" (CEO, Q1'26 Q&A) versus "80% to 85%" (Q1'26 prepared remarks and Q2'26 call).
- **Placement mix:** ">60%" clinical (Q4'25, Q1'26) versus "about 70-30" (Q2'26 CFO). Also JPM's "as much as half of clinical placements… incremental".
- **Gross-margin drivers:** SomaLogic cited by Freedom only; instrument mix and freight/memory cited by JPM and the CFO.
- **Stale or unreliable inputs:** the quarterly 6000 and X bases are my estimates. FY25 pull-through ($670K, $1.35M) is the last disclosed; there is no 2026 interim pull-through disclosure.

## Gaps / what I could not find
- The Q3'25 original deck's text extraction doesn't attach labels to series, so my reading that 91% belongs to the R&A panel is supported by the call, not read from the chart.
- No quarterly 6000 decommission count, installed base or pull-through for 2026. Gap 3 items still open: Q1'26 and Q2'26 tariff dollars, consumables-only gross margin, the Q1'26 reserve drop of $14M, and any 6000-specific inventory reserve. I did not open the 10-Q MD&A lines marked "omitted long line".
- No sell-side estimate of 6000 versus X gross margin; the 80–85% (6000) figure is the ledger's assumption.
- No search of Q1'25 and Q4'25 long lines (call lines 138, 172, 174) beyond the extracts the grep returned.
- I did not check the pre-2024 conferences or the JPM Jan 2026 deck for other X-share wording.
- Parallel-use customer count: not disclosed anywhere I looked.
