# Agent 60: 60-internal-contradiction-audit-metric-definitions-dropped-disclosures-and-Q3-26-checklist

*Model: sonnet. Run 2026-10-11 03:37:34. Cost $1.00 (API-equivalent).*

**Assignment:** Use only the local corpus. Start with INDEX.md and the Extracts for ILMN earnings calls, decks and conferences from Q1 2024 to Q2 2026. Read the evidence ledger first so you do not repeat it, and then do a quote-level audit of metric definitions and disclosure changes, with three jobs. (A) Disclosure-change table: for each of these metrics, give the first and last quarter it was reported, the exact wording at each change, and any explanation given: X share of HT revenue and volume, X and 6000 installed base, pull-through per instrument (and its definition: cohort, trailing, annualized or exit-rate), decommissions, the '>30%' Gb growth wording, clinical vs research consumables split, ex-China growth, the clinical % of sequencing consumables, 'fully converted' customer counts, and non-GAAP definitions (including the treatment of GRAIL, China, stock comp, restructuring and the Bio-Rad or 10x litigation). Flag every case where a metric was introduced when it looked good and dropped when it looked bad, with the quarter and the numbers at the time. (B) Q&A dodges: find the analyst questions on the 6000-vs-X parallel run, price per Gb, the cannibalization of 6000 revenue, clinical customer concentration, and AXELIOS/Ultima/Element competition. For each give the analyst, date, a verbatim short question, the verbatim short answer, and a rating of answered / partially answered / dodged. Include the Jefferies Q2'26 question. (C) Compute from the corpus the quarter-by-quarter implied revenue per Gb (X vs 6000) using the share series in the brief. Then estimate the revenue-at-risk range when the last 17% of HT volume converts, using the 60-70% per-Gb price decline, and with the offset from 20-30% Gb growth in year 1. Add what each of Q3'26 outcomes (X share of HT revenue at 62%, 64% and 66%) would imply. Finish with a checklist of 10 specific items for the 29 Oct 2026 Q3 call. Cite files and dates for everything, and label FACT, MGMT or OPINION.

## Key findings

Most of this audit duplicates the ledger. Only the items below are new, and each cites the E-number it corrects or extends.

1. **CORRECTION to E158. The Q3'25 competition question came from Patrick Donnelly (Citigroup), not Leerink.** He asked about "any pressure or freezing that could offer to the market, particularly on the clinical side." [ILMN Q3 2025 call, Sources/ILMN/earnings_call/ILMN_2025Q3_Earnings_Call.md l.392-414]
   - FACT: Thaysen answered: "most of our competition… competitors are trying to compete and differentiate on one dimension only… Illumina is really the only one that's delivering across all these dimensions."
   - OPINION: He did not address freezing, so I rate it dodged.
2. **No analyst asked about customer concentration or bargaining power on any 2024–Q2'26 call.** FACT (absence): a search of the call files for "concentrat" returned nothing. The only "largest customers" text is management's own, and it supplies the growth claim, not a risk.
   - Q3'25 (Dhingra): business with largest customers "projected to grow faster than the overall company average rate, at least over our strategic plan period." [Q3'25 call l.164]
   - Q1'26 (Thaysen): "large customers, centralized labs here in U.S." with momentum visible "on their own numbers." [Q1'26 call l.616]
   - OPINION: This sits beside the new "small number of large, centralized laboratory customers" risk-factor wording (E107). Management disclosed the risk in the 10-K and nobody has put it to them on a call.
3. **Pull-through is defined as "average annualized figures per instrument," and it stopped appearing after the Q4'25 deck.**
   - FACT: Footnote 3 on the Q4'25 deck and the JPM Jan 2026 deck reads "Average pull through reflects FY25 average annualized figures per instrument, in thousands." The Q4'25 deck adds "Company doesn't guide low-throughput pull-through." [Sources/ILMN/deck/ILMN_2025Q4_Earnings_Slides.md l.380-389; JPM deck 2026-01-13 l.570-580]
   - So it is neither exit-rate nor cohort-based. It is a full-year average, and the installed-base denominator it uses is not defined.
   - FACT: A search of the decks found the pull-through table only in the Q4'25 and JPM Jan 2026 decks. I found none in the Q1'26 or Q2'26 deck text.
   - FACT: On the Q4'25 call Dhingra said "Our pull-through assumptions by platform can be found in our earnings presentation" (l.226). On the Q1'26 call Thaysen only said "at JPMorgan we showed… above $1.3 million of pull-through on the Xs" (l.638).
   - OPINION: The FY26 pull-through guide ($1.35-1.40M for the X, $600-650K for the 6000) has never been reaffirmed or updated in the Q1'26 or Q2'26 materials. This extends E245 and E268. Item 5 in the checklist below is the test.
4. **The wording for what drives high-throughput revenue changed between Q1'26 and Q2'26.**
   - Q1'26 (Dhingra): "High throughput volume drove most of the revenue growth as the NovaSeq X installed base continues to expand and **utilization** increased year-over-year." [Q1'26 call l.158]
   - Q2'26 (Dhingra): "…the NovaSeq X installed base continues to expand and **pull-through** increased year-over-year." [Q2'26 call l.136]
   - FACT: Both are prepared remarks. No pull-through number was given in either.
   - OPINION: Q2'26 is the first time "pull-through increased" is claimed without a figure. The metric is cited when it is up and not quantified.
5. **Price per Gb was left out of the Q3'24 prepared remarks and only surfaced when an analyst asked.** Evercore's Vijay Kumar: "The activity levels were about 40%, but I didn't hear a price for GB commentary. Was that in line with the minus 20, minus 25…?" [Q3'24 call l.304]
   - Dhingra: "Yes, it was in that 25-percentage range… closer towards 25 rather than 20." [l.324]
   - Rating: answered, but only on request. This adds the "who asked" detail to E047/E048.
   - FACT: In the same call Dhingra said consumables grew "at a high single-digit rate this quarter" [l.408]. E048 records +5–7%. I did not reconcile the two, and the high-single-digit claim may refer to high-throughput consumables only.
6. **Thaysen conceded in Q2'24 that mid-throughput pricing is a lever.** Leerink's Souda asked whether cost per Gb is "a lever that you can use… to compete more effectively." Thaysen: "on the mid throughput, we certainly have an opportunity to use our pricing if we need to… even when we provide premium cost per gigabase…we continue to be highly differentiated." [Q2'24 call l.440-454]
   - MGMT: This is the clearest admission that Illumina prices at a premium per Gb. It is partially answered, and it was not followed up.
7. **The Q1'26 question on the initial 6000-to-X price hit (E209) can be quoted exactly.** Souda: "There will be an initial impact from 6,000 pricing to Nova X pricing for consumables within those labs. How are you thinking about that impact? And is that incorporated into the guide?" Thaysen opened with "that was one question with many sub-questions," then covered placements being "much more additional incremental placement than necessarily conversion of the 6,000." [Q1'26 call l.284-298]
   - Rating: dodged on both sub-questions. No clinical price impact was given, and he did not say whether it is in the guide.
8. **Peterson's Q2'26 question was framed as a "sequential slowdown," but the 20%→15% figures are year-over-year.** Thaysen accepted the framing and answered only on the y/y rates (20% down to 15%, US above 20%, Middle East and Latin America slower). [Q2'26 call l.240-260]
   - FACT: The words "over-earning," "decommission pace" and "parallel" were not repeated by management. The only "parallel" language in the Q2'26 call is in the question.
   - This confirms E014 and adds the framing mismatch.
9. **Part C: the 6000's revenue-per-Gb index (HT average = 1.0) by quarter, and what Q3'26 outcomes imply.** The method is below; the tables are in the sections that follow.
   - OPINION (calc): the index is (1 − revenue share) / (1 − volume share). The 6000 index rose from 1.33 in Q2'24 to 2.41 in Q2'26.
   - OPINION (calc): the Q3'26 scenarios show the 6000 losing $12M, $23M or $34M of quarterly revenue.

## A. Disclosure-change table (new items only)

The ledger already covers X pull-through history (E139), clinical split (E076–E077, E208), >30% scope (E207), and transition metrics (E138). This table adds first/last appearances and wording.

| Metric | First / last seen (this audit) | Wording or change | Looked good then dropped? |
|---|---|---|---|
| X and 6000 pull-through table | Last in Q4'25 deck and JPM Jan 2026 deck (decks searched) | "FY25 average annualized figures per instrument"; low-throughput pull-through not guided | FY26 guide not reaffirmed in Q1'26 or Q2'26 decks (extract-level check) |
| Cause of HT revenue growth | Q1'26 "utilization increased"; Q2'26 "pull-through increased" | Wording swap, no number | The key metric is cited as up without a figure |
| Price per Gb | Q3'24 asked by Evercore, not volunteered | "closer towards 25 rather than 20" | Not in prepared remarks while at the top of its range |
| 6000 sales | Q2'26: "placed over 10 NovaSeq 6000 units as some consumers plan to remain on that platform for years" [l.156] | A 6000 count appears in Q2'26 only | No FY25 or Q1'26 comparison given (E015) |
| 40-customer cohort | Q3'25 call "fully transitioned"; deck footnote "fully or largely" (E025) | Bernstein May 2025 already says "customers that are fully transitioned" with no count [Bernstein 2025-05-29 l.230] | Count first given Q3'25 at 40, when the case study looked good |

I did not audit the non-GAAP definitions (GRAIL, China, stock comp, restructuring, Bio-Rad/10x litigation). I ran out of time, and E147/E148 already cover the main items.

## B. Q&A audit (new or corrected rows)

| Date / analyst | Question (short) | Answer (short) | Rating |
|---|---|---|---|
| Q2'24 Souda (Leerink) | Is cost per Gb "a lever… to compete more effectively" in mid-throughput? | "we certainly have an opportunity to use our pricing if we need to" | Partially answered |
| Q3'24 Kumar (Evercore) | "I didn't hear a price for GB commentary." | Dhingra: "closer towards 25 rather than 20" | Answered, on request |
| Q3'24 Peterson (Jefferies) | Pricing headwind and "multiyear contracts… Do those break" with X? | Thaysen: open-offer contracts "not instrument specific… continue with the X"; "That's not how we see [a cliff]" | Contract part answered, price part partial |
| Q2'25 Nambi (Guggenheim) | Any "change in customer behavior in anticipation of competition"? | Turnaround time is "a niche market in the NICU"; "we spend even more time thinking about our customers" | Dodged on behavior, answered on turnaround time |
| Q3'25 Donnelly (Citi) | Competition, "pressure or freezing… on the clinical side"? | "Illumina is really the only one that's delivering across all these dimensions" | Dodged |
| Q1'26 Souda (Leerink) | Initial 6000→X price impact; in the guide? | Placements "more incremental than conversion"; "converted most of our Xs in the research business" | Dodged |
| Q2'26 Peterson (Jefferies) | "Are you over-earning on consumables because at some point, the 6000 get decommissioned?" | "some customers actually purchasing a few 6000… not true headwinds" (E014) | Dodged on size, partly answered on direction |
| 2024–Q2'26, any analyst | Customer concentration / bargaining power | No question found | Never asked |

## C. Implied revenue per Gb and Q3'26 scenarios

All of this is OPINION (calc on the brief's FACT shares). The volume series is Gb shipped, not consumed (E204). Rounding of ±1 point moves the ratios noticeably.

6000 revenue-per-Gb index (HT average = 1.0), computed as (1 − revenue share) / (1 − volume share):

| Quarter | 6000 index |
|---|---|
| Q2'24 | 1.33 |
| Q3'24 | 1.44 |
| Q4'24 | 1.71 |
| Q1'25 | 1.78 |
| Q2'25 | 1.81 |
| Q3'25 | 2.23 |
| Q4'25 | 2.25 |
| Q1'26 | 2.50 |
| Q2'26 | 2.41 |

The X index is stable (0.60 to 0.71, per E002). Dividing the 6000 index by the X index gives the ratios already in E002.

Revenue at risk when the last 17% of HT volume converts. This is the HT run-rate of about $535M a quarter (69% of Q2'26 sequencing consumables) times the 6000's 41% revenue share. The loss on the converting base is 41% × [1 − (1 − price cut) × (1 + volume uplift)]. It assumes the converted volume is priced like average HT volume, and it applies at 100% conversion:

| Price cut / Gb uplift | % of HT revenue | $M per quarter |
|---|---|---|
| 60% / +20% | 21.3% | 114 |
| 60% / +30% | 19.7% | 105 |
| 70% / +20% | 26.2% | 140 |
| 70% / +30% | 25.0% | 134 |

Annualized, that is about $0.42B to $0.56B. This is consistent with E246's central $473M and E004, so I treat it as a cross-check, not new evidence. If about 20% of 6000 volume never converts (E005), scale by 0.8.

Q3'26 implications. The volume share needed for each revenue share uses the X/6000 price ratio of 0.295 (E187), then the dollar split uses $544M of HT (69% of the $789M Q3'26E consumables, E050). Pull-through uses the average X base of about 1,108 (E268):

| Q3'26 X revenue share | Implied X volume share | X revenue | 6000 revenue | 6000 change vs Q2 ($219M) | X pull-through, annualized |
|---|---|---|---|---|---|
| 62% | about 84.7% | $337M | $207M | −$12M | about $1.22M |
| 64% | about 85.8% | $348M | $196M | −$23M | about $1.26M |
| 66% | about 86.8% | $359M | $185M | −$34M | about $1.30M |

- OPINION: These ratios match E270 (85–86% volume for a 61–64% revenue share).
- OPINION: A 62% print needs about +2 pts of volume share in a quarter, against +1 pt in each of the last two.
- OPINION: Only the 66% outcome (6000 near $185M) fits the 6000 path E245 says the FY26 guide needs (about $175M a quarter average in H2). Even that leaves X pull-through at about $1.30M against the $1.46–1.55M H2 requirement in E268.
- OPINION: Reaching the guide requires the 6000 to fall faster, or the guide to be quietly cut.

## D. Checklist for the 29 Oct 2026 Q3 call

1. X share of HT revenue and volume: is the revenue share at or above 62%, and does volume reach 85% or more?
2. Is clinical X volume share given, and does it clear 80% (78% in Q2'26)?
3. Is the Gb output wording still "more than 30%… clinical well above that," and is the scope (connected, ex-China) stated?
4. Does the 6000 get any dollars or counts (new 6000 units placed, a decommission count, an installed-base figure)? "Over 10" was the Q2'26 count.
5. Is the FY26 pull-through table reinstated or reaffirmed ($1.35–1.40M X; $600–650K 6000)? A silent drop is itself a signal (E268).
6. Does the Q3 call define the word "pull-through" or revert to "utilization"?
7. Are the Q3'26 cohort and case-study slides refreshed (n=40 was last measured on 28 Sep 2025)?
8. Is the 35B timing or price mentioned? Illumina's roadmap says H1 2027 (E214).
9. Does anyone ask about customer concentration, the "centralized lab" risk factor, or reagent rental? Nobody has since 2024.
10. Does any analyst ask about Roche AXELIOS placement progress (about one-third of ~100 by September), and do they get more than "multi-dimension" (Q3'25 style)?

## Contradictions and stale data

- E158 names Leerink for the Q3'25 competition question. It was Patrick Donnelly of Citi.
- Q3'24 Dhingra says consumables grew "at a high single-digit rate"; E048 says +5–7%. Unreconciled.
- The pull-through footnote says "average annualized," so any quarterly pull-through number derived from base and revenue (E038) is not on the company's basis.

## Gaps / what I could not find

- I did not complete the non-GAAP definition audit (GRAIL, China, stock comp, restructuring, Bio-Rad/10x litigation).
- I did not check the Q1'25 and Q4'24 decks for X/6000 installed-base disclosures, or the exact quarter each share metric first appeared.
- The Q4'25 decks and the Q1'26/Q2'26 decks were checked by text search only. A table could be present as an image.
- Several call transcripts have long lines marked "[Omitted long matching line]." I could not read those matches, so Q&A in them may be missed.
- The Q1'24 Morgan Stanley excess-capacity question (E158) was not re-read.
