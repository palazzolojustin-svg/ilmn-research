# Agent 21: A-internal-original-verification-and-clinical-recalc

*Model: sonnet. Run 2026-10-11 02:31:28. Cost $1.35 (API-equivalent).*

**Assignment:** Close the corpus-verification gaps by opening ORIGINALS in Working Notes/Sources/ILMN (decks as PDF or images, calls, research PDFs), not Extracts. (1) Q2'26, Q1'26, Q4'25 and Q3'25 earnings decks (Sources/ILMN/deck/...): render the transition slides (Q2'26 slide 8, Q4'25 slide 15) and read the chart series for clinical vs research X share of volume and REVENUE, the 6000 pull-through and any installed-base figures. Re-run the clinical-only revenue-at-risk calc: clinical X revenue share, the clinical 6000 revenue per quarter, and the revenue change if the remaining clinical 6000 Gb moved to X at 60-70% lower $/Gb, at Gb growth of 0/15/30/45%. Show the break-even Gb growth. (2) Q2'26 call transcript (Sources/ILMN/earnings_call/ILMN_2026Q2_Earnings_Call.md): quote verbatim the Jefferies/Peterson over-earning/parallel-running question, every answer and follow-up, who answered (Thaysen vs Dhingra), and the exact '6000 purchases' wording. Settle the F02-vs-F14 disagreement on the firm and whether Dhingra answered. (3) Grep all ILMN 10-Q/10-K text in Sources/ILMN/filing for 'active instruments', 'reagent rental', 'lease', 'NovaSeq 6000', 'decommission', 'installed base' and 'dual' and list every disclosed number. (4) Open the UBS PDFs in Sources/ILMN/research to confirm $0.06 vs $0.68 per M reads, the UBS expert's $125-175/genome, and the Element VITARI $3k vs $32k per run figures. (5) Open the JPM Jun 2026 customer survey original and settle 6000 ownership (75% vs 16%), the AXELIOS purchase-intent data, and whether the 4-5% implied price decline is based on planned or realized pricing. (6) Scan all 23 expert-call originals for any statement of clinical-lab Gb growth, 6000 retention or dual running that earlier summaries missed. Return a table of corrected numbers with file/page citations, and flag every number that changes the ledger.

## Key findings

**NEW EVIDENCE.** All Sources files are text/Markdown conversions, with no PDFs or images to render. I read the deck charts through their extracted labels.

- **Clinical X revenue share is not disclosed.** FACT: the Q1'26 and Q2'26 transition slides give a single total-HT revenue series (27, 36, 40, 43, 44, 51, 55, 55, 59%). Volume has three series: total, research and clinical. The gap in `00_open_gaps.md` #1 can't be closed from the decks. Any clinical revenue share is a derived estimate. [Sources/ILMN/deck/ILMN_2026Q2_Earnings_Slides.md, slide 8, lines 103-113; ILMN_2026Q1_Earnings_Slides.md lines 107-134]
- **Exact clinical and research volume series (corrects E010, E157).** Every extracted label is used exactly once under the assignment below. That makes the assignment OPINION (self-consistent inference), but it is tight.
  - Clinical X % of HT Gb, Q2'24 to Q2'26: **35, 43, 49, 51, 53, 64, 71, 76, 78**.
  - Research: **59, 70, 80, 82, 82, 90, 90, 91, 92**.
  - Total: 45, 55, 66, 68, 69, 78, 80, 82, 83.
  - E010 had ~40 (Q3'24), ~50 (Q4'24), ~55 (Q2'25) and ">2/3" (Q4'25). The deck gives 43, 49, 53 and 71. Freedom's 71% for Q4'25 is right.
  - E157 ("Q4'25 deck chart shows ~90%") is resolved. The ~90% is the research line, not a contradiction with the ~80% total.
- **Clinical-only recalculation (quantifies E004, E009).** OPINION (calc). This assumes the 6000-vs-X price ratio is the same in clinical and research, which no source confirms.
  - Total-HT data imply X $/Gb = 0.295 × the 6000's (about 70.5% cheaper).
  - Clinical share of HT Gb is backed out as (92−83)/(92−78) = 64%, with a 57-71% rounding range.
  - Clinical X revenue share is therefore ~51% (research ~77%).
  - Clinical 6000 revenue is ~83% of total 6000 revenue, or ~$182M per quarter (range $172-191M, ~$0.73B/yr). That is ~36% of clinical sequencing consumables (taking clinical as ~$504M, i.e. 65% of $775M) while the 6000 carries only 22% of clinical HT Gb.
  - Clinical X revenue is ~$190M per quarter. Clinical HT revenue is ~$372M.
- **Clinical break-even Gb growth is higher than the total-HT figure in E004.** Total HT needs about +41%. Clinical needs about **+53%** at today's price ratio, and **+42%** at a 60% price cut or **+52%** at a 70% cut. The reason is that clinical has more of its volume still on the 6000 (22% vs 17%).
- **Jefferies/Peterson exchange verified (settles F02 vs F14, E014, E158).** The firm is Jefferies, and the question was asked by Tycho Peterson. Thaysen answered alone, and the operator moved straight to Kumar (Evercore). No Dhingra answer and no follow-up exist. F02 is right and F14 is wrong. Thaysen did not address "over-earning", did not give a 6000 revenue, decommission pace or dual-running count, and did not rebut the premise.
- **The ">10 NovaSeq 6000" line was Dhingra's, not Thaysen's.** It came in CFO prepared remarks, not Q&A, and the transcript says "consumers" (a transcription slip for "customers").
- **JPM survey 6000 ownership settled (E021).** The 16% in the summary bullet is a typo. [JPM, 2026-06-15, `20260615_JP_Morgan_ILMN_Illumina-_Inc.md`, p.8]
  - The chart counts show all 62 respondents at **56%** for the 6000 (35/62) and **58%** for the X (36/62).
  - Clinical (n=32): 6000 **24/32 = 75%**, X **17/32 = 53%** (not 58%).
  - Academic (n=30): 6000 11/30 = 37%, X 19/30 = 63%.
  - Clinical labs in the sample own more 6000s than Xs. The 75% is "owns at least one", not share of volume. The survey says nothing on dual running.
- **Survey-implied price decline (E067).** The 4-5% is stated forward plans, not realized pricing, and it is JPM's inference. The question asks "what do you expect your sequencing consumables spend growth rate to be", with bucket answers (decrease 1-10%, flat, +1-10%, +11-25%, +26-50%). Volume was asked separately. N=32 clinical, so the averages are bucket-based and noisy. Realized prices are not in the survey.
- **UBS figures confirmed (E059, E060, E182).**
  - **$0.06 vs $0.68 per M reads** is confirmed from the garbled "$006 … $068". It is Roche's quote vs Illumina's *list* price on the 25B flow cell, about 11x. UBS puts counting applications at ~40% of research usage and ~16% of total consumables. [UBS, First Read, 2026-03-03]
  - **$125-175/genome** is confirmed, but the note is dated **26 Feb 2026** (file prefix 0304). It comes from one expert on a "Doc Debates" call, not from a clinical customer. The expert said "Already at $175 / genome with his discounts" and that larger users were "already at $125 / genome". He had expected Roche to price at **$100/genome**, and said the 35B "likely brings Illumina pricing to $150 anyway". [UBS 2026-02-26]
  - UBS's own view is that Illumina's roadmap gives "a path to ~$150/genome on the NovaSeq X+ assuming the forthcoming 35B flow cell is priced consistent with the 25B flow cell". That is about −25% from the ~$200 list, against −20% for the ex-AD in E058. [UBS 2026-03-03]
- **Element VITARI figures confirmed, and E182 is corrected.** UBS Fast Take, 2026-02-19: "Instrument price ~40% discount to NovaX+ (list is $689k)". Consumables per run are "~1/10 (~$3k vs ~$32k)", $/Gb "~50% lesser", and output per run "~1/5 vs NovaX+ (3T vs 16T)". Dividing gives ~$1.00/Gb vs ~$2.00/Gb. Shipping is 2H26.
  - **$689K is the VITARI list price, not an X Plus price.** E182 lists "$689K (UBS)" as an X Plus price, which is wrong. A 40% discount implies an X Plus of roughly $1.15M, consistent with Vilella's $1.165M.
- **Installed-base disclosures are even thinner than assumed.** The only 6000 count is the Q4'25 deck slide 15 (as of 2026-02-05). That slide gives 6000 placements ~30, base ~1,360, pull-through ~$670K and an FY26 guide of $600-650K. The X figures are ~270 placements, ~890 base, ~$1,350K and a guide of $1,350-1,400K. Footnotes: the active base "excludes decommissioned instruments and **includes reagent rental units**", and "NovaSeq 6000 active installed base accounts for ~330 decommissions in FY25". Q1'26 and Q2'26 decks have no installed-base slide. [ILMN_2025Q4_Earnings_Slides.md lines 349-389]
- **No 10-K or 10-Q text discloses reagent rental, lease counts, a 6000 base or decommissions.** "reagent rental" appears in zero filings. The only 6000 revenue quantification is in FY2023 filings: lower 6000 pull-through cut sequencing consumables by $92M (Q1'23), $5M (Q2'23) and $30M (Q3'23). That was $127M for FY23, "driven primarily by lower NovaSeq 6000 consumables pull-through". [10-Q 2023Q1 l.1040; 2023Q2 l.1130; 2023Q3 l.1144; 10-K FY2023 l.948] The FY25 10-K and 2026 10-Qs don't name the 6000 in their revenue discussion. This extends E036.
- **JPM Jan 2026 deck, Jan 13 (extends E020).** Active installed base is ~21k (>12k LT, >6k MT, ~2k HT). HT capacity is "~2x" 2022-2025 (theoretical max output). That is about a 26% CAGR, below the ">30%" Gb growth, so utilization or placements must keep rising.

## Revenue-at-risk table (clinical-only)

All figures are on the Q2'26 run-rate of ~$372M per quarter of clinical HT revenue. They are static, single-step effects with price held constant, and they assume all 22% of clinical volume moves. Scale by ~0.8 if 20% never moves (E005). Cases:
- **A:** growth applies to the converted Gb only.
- **B:** growth applies to all clinical HT Gb.

| Case | Gb growth | Price cut on converted Gb | Change in clinical HT revenue | ≈ $M per quarter |
|---|---|---|---|---|
| A | 0% | 60% | −29% | −109 |
| A | 15% | 60% | −26% | −98 |
| A | 30% | 60% | −24% | −87 |
| A | 45% | 60% | −21% | −76 |
| A | 0% | 70% | −34% | −127 |
| A | 15% | 70% | −32% | −119 |
| A | 30% | 70% | −30% | −111 |
| A | 45% | 70% | −28% | −103 |
| B | 0% | 60% | −29% | −109 |
| B | 15% | 60% | −19% | −70 |
| B | 30% | 60% | −8% | −30 |
| B | 45% | 60% | +2.5% | +9 |
| B | 0% | 70% | −34% | −127 |
| B | 15% | 70% | −24% | −91 |
| B | 30% | 70% | −15% | −54 |
| B | 45% | 70% | −5% | −17 |
| B | 0% | 70.5% (observed ratio) | −34.5% | −128 |
| B | 15% | 70.5% | −24.7% | −92 |
| B | 30% | 70.5% | −14.8% | −55 |
| B | 45% | 70.5% | −5.0% | −19 |

**Break-even Gb growth**
- **Case A (converted Gb only):** +150% (60% cut) or +233% (70% cut).
- **Case B (all clinical HT Gb):** +42% (60% cut), +52% (70% cut) or +53% (70.5%).

The ranges are in the findings above.

**Sensitivity to the c = 64% estimate.** Clinical HT share of 57-71% moves the clinical 6000 revenue to $172-191M per quarter. Break-even moves less.

**Consistency check.** The same method at Q3'25 (78% total, 64% clinical, 90% research, 51% revenue share) gives clinical X revenue ~34%. That is consistent with Wolfe's "less than 50%" (E104).

## Other items checked

- **Expert calls (23 scanned).** One new datapoint: an ex-Illumina FAS (left 2024, GCC and US) managed one account with "**21 NovaSeq 6000 and 15 X Pluses**" and said "customers now moving from the NovaSeq 6000 System to the NovaSeq X Plus". That is a single anecdote of dual running at one large population-genomics site. [Expert_2026-07-24_Former_Field_Application_Scientist…, lines 61, 111] The other calls add nothing on clinical Gb growth, 6000 retention or dual running beyond the ledger. These include the ONT "years to switch" call (E116), the 30-40% price-fall estimate (E071) and "6000 obsolete" as the competitive window (E130).
- **Q2'26 call "6000 purchases" wording.** Thaysen: "we did see some customers actually purchasing a few 6000 this quarter to continue their operations. So of course, eventually, they will move over to X, but we don't see that as … a standard part of the business." Then: "It's only a few quarters ago, we still had HiSeqs running in our portfolio. So I don't think that, that is -- will be considered any true headwinds for us." Dhingra's prepared remark: "We also placed over 10 NovaSeq 6000 units as some consumers plan to remain on that platform for years to come." [ILMN_2026Q2_Earnings_Call.md l.246, 256, 156]

## Table of corrected numbers

| Ledger item | Old | Corrected | Source |
|---|---|---|---|
| E010 clinical X vol share | ~40/50/55/>2/3 | 43/49/53/71 (Q3'24, Q4'24, Q2'25, Q4'25) | Q2'26 deck slide 8 |
| E157 | deck ~90% vs call ~80% | 90% is the research line | Q1'26/Q2'26 deck |
| E021 | 75% (clinical 6000), 58% (clinical X), 16% (6000) | 6000: 75% clinical, 56% all, 37% academic. X: 53% clinical, 58% all. The 16% is an error | JPM 2026-06-15 p.8 |
| E067 | "Planned or realized?" | Stated plans, n=32 | JPM p.11 |
| E059 | "UBS Feb 2026 call" | UBS 2026-02-26, one expert, Roche $100 expected | UBS First Read |
| E182 | X Plus $689K (UBS) | $689K is VITARI. X Plus is about $1.15M | UBS 2026-02-19 |
| E004 | HT break-even +41% | Clinical +53% (+42% to +52% on 60-70% cuts) | calc |
| E014 | Peterson (Jefferies per F02; F14 unconfirmed) | Jefferies/Peterson confirmed, Thaysen only, no follow-up | Q2'26 call |
| E015 | ">10" 6000s | Said by Dhingra in prepared remarks | Q2'26 call |
| E003/E009 | 6000 $219M total, ~80-83% clinical | Clinical ~$182M per quarter (range $172-191M) | calc |

## Contradictions and stale data

- The JPM survey summary (16% 6000) conflicts with its own chart counts (56% all, 75% clinical). Use the chart.
- The extraction of the transition charts is unlabelled. The series assignment is inferred, not read from a legend. It is internally consistent, but confirm against the PDF if the exact values matter.
- Q3'24 total HT revenue share is 36% in the decks (27, 36, 40, …). The ledger shows 35-36%.
- The Q4'25 deck says transition metrics would be phased out after Q4 (E138), yet Q1'26 and Q2'26 still carry them, now as three-series volume and one-series revenue.

## Gaps / what I could not find

- No PDF or image originals, so no true chart rendering. IR (investor relations) should be asked for the clinical X revenue share and the 6000 installed base.
- No Q1'26 or Q2'26 installed-base slide. Q4'25 slide 15 is the last 6000 count.
- The JPM survey doesn't say whether respondents run 6000 and X in parallel, only ownership.
- I did not re-open the Q3'25 and Q4'25 deck transition slides for their clinical series. The Q1'26 and Q2'26 series cover them.
- I did not open the DEF 14A, Form 4s or the Caris materials (gaps #8-11), which are outside this assignment.
