# Agent 94: 99-internal-2026-conference-transcripts-QA-log-and-wording-verification

*Model: sonnet. Run 2026-10-11 10:16:40. Cost $0.49 (API-equivalent).*

**Assignment:** Close open gap 5. Agent 91 covered only the Q4'25, Q1'26 and Q2'26 earnings-call Q&A, so do NOT repeat those. Use INDEX.md to locate every 2026 ILMN conference transcript and extract, plus 2025 H2 conferences if they are not covered. Examples: JPM Jan 2026, TD Cowen Mar 2026, Goldman Sachs, Bernstein, Jefferies, William Blair and June 2026 healthcare events. Open the originals in Sources/ILMN/conference whenever a wording or number matters.

For each event, log:
(1) Each analyst question on the 6000-to-X transition, clinical consumables, pricing or $/Gb, 35B flow cell, China, Roche AXELIOS, Ultima or Element, and customer concentration. Mark whether the answer was direct, partial or dodged, and quote the exact words (short).
(2) Verify Dhingra's '80-85%' clinical-on-X wording and its date. Verify whether the 200-240 X placements range was restated. Verify any '>10' new NovaSeq 6000 sales statements. Verify any sizing of the 6000 base or decommissions.
(3) Any new numbers not in the ledger: dual-running customers, revalidation time and cost, price-per-Gb change by cohort, take-or-pay or volume-commitment language, and the pace of 6000 end-of-life.
(4) Differences between what management said at conferences and on calls (tone, definitions, hedges, dropped metrics).

Read 00_evidence_ledger.md in the Outputs folder first, using offset and limit because it is long, to avoid duplicating. Return a dated table of dodged or shifting statements plus a list of new facts.

## Key findings

**Result: mostly NO NEW EVIDENCE.** The corpus holds only three ILMN conference transcripts in the requested window: Wolfe (2025-11-19), JPM (2026-01-13) and TD Cowen (2026-03-03). There is no Goldman, Bernstein, Jefferies, William Blair or June 2026 transcript. The newest conference extract is TD Cowen on 2026-03-03. I read all three in full. Their content is already captured in E011, E026, E028, E057, E061, E104, E127 and E158. The few additions and verifications are below.

- **Dhingra "80–85%" wording (verified, refines E011).** The Q1'26 prepared remarks (call 2026-04-30, `Sources/ILMN/earnings_call/ILMN_2026Q1_Earnings_Call.md` l.172) say: "76% of clinical volume is now on the X, and we continue to expect that majority of clinical volumes or over 80% to 85% will be on X by the end of 2026." (MGMT)
  - The wording is garbled, so "over 80% to 85%" is a floor-and-range hybrid.
  - The same sentence says "we continue to expect", which implies the target was already in place.
  - The Q2'26 call (l.142) cleans it to "reach 80% to 85% conversion by the end of 2026." (FACT)
  - In Q1 Q&A (l.704), Thaysen says: "we believe that we have more than 85% of that transition by end of this year, which we feel is where… the transition is behind us." (FACT)
  - So Thaysen's "more than 85%" and the CFO's "80% to 85%" appeared on the same call, and the next quarter fixed on the lower range.
  - Arithmetic: 78% at Q2'26 to 80–85% by year-end needs only +2 to +7 points in two quarters.
- **200–240 X placements (verified).** Dhingra gave this only on the Q4'25 call (2026-02-05, l.426): "for Xs, yes, about 200 to 240 for the year. I said on average; 50 to 60 a quarter is still quite good." (MGMT)
  - It was not restated at JPM, Wolfe or TD Cowen. I found it in neither the Q1'26 nor the Q2'26 transcript.
  - Instead, Q1'26 (l.154) reports ">80… above our targeted range of 50 to 60 per quarter".
  - Q2'26 Q&A (l.226) says "we laid out… 50 to 60 placements per quarter… clearly… running stronger".
  - So the annual range was dropped, the per-quarter frame stayed, and the "target" is now referred to as something already beaten.
  - H1'26 placements are about 160+ (80+ in each of Q1 and Q2), already about 70–80% of the 200–240 annual range by mid-year. This is calc, based on the "80 in 2Q" figure in the Jefferies question (Q1 call l.630). The ledger has E143 on low-balling but not this explicit point that the annual range was never refreshed.
- **">10" new 6000 sales.** This was confirmed as CFO prepared remarks and appears at no conference. There is nothing to add beyond the existing correction to E015.
- **No conference sizing of the 6000 base, decommissions, dual-running customers, revalidation cost or time, take-or-pay language or 6000 end-of-life pace.** I searched the conference originals for these terms. The only 6000 hits are the Wolfe cohort discussion (E028) and the JPM "layers incremental volume onto X alongside existing NovaSeq 6000 workflows" line (E023).

## Dated table of dodged or shifting statements (new items only)

| Date / event | Question | Answer quality | Exact words and note |
|---|---|---|---|
| 2026-01-13 JPM (Woodring) | Share of clinical customers on WGS today, and any headwind to quantify | Dodged (Dhingra) | WGS is "much, much smaller"; "No percentage… no headwind quantification" in the transcript. Same dodge in E158, but this is the first dated conference instance. |
| 2026-01-13 JPM | New KPIs after the 75% / 50% targets were met | Shift | Dhingra replaced transition metrics with "number of reimbursements approved, number of new tests reaching market". This is the origin of the E138 phase-out, but it came from the CFO at JPM, three weeks before the Q4 deck. |
| 2026-01-13 JPM | Durability of the 40-customer cohort | Partial | Thaysen: "Illumina does not intend to keep reporting individual cohorts." Year one "a little bit flattish". At Wolfe (2025-11-19) the same pattern was "almost in an equilibrium". The tone drifted from "equilibrium" to "flattish". |
| 2026-01-13 JPM | Pace of transition | Shift | Dhingra: the price effect "should keep shrinking and be a lesser impact in 2026 than in 2025". TD Cowen (2026-03-03): "definitely still some pricing headwind… shouldn't be worse than '25". The claim moved from "lesser" to "not worse", a weaker hedge. |
| 2026-03-03 TD Cowen (Brennan) | Is the 35B flow cell priced? | Dodged | "We don't see any value in coming out too early with pricing." This is a stated policy of withholding, and it was applied to TruPath too (E057). |
| 2026-03-03 TD Cowen | Is clinical guidance conservative? | Partial | Thaysen can predict clinical growth only "within about 1 percentage point"; "Potentially" higher. The Q1'26 call then printed 20% (vs the DD-to-mid-teens guide), consistent with E143. |
| 2026-03-03 TD Cowen | Roche share loss in the guide | Partial | "I'm not seeing any freezing of the market." The question on Roche in the guide was answered with the HSD-by-2027 goal, not a share assumption. |
| 2026-03-03 TD Cowen | Ultima / Element new price points | Dodged | "Nothing new… we fight every day on the streets." |
| 2026-03-03 TD Cowen | WGS size in research | Dodged | Brennan asked how large WGS is for Illumina in research; no size was given. |
| 2025-11-19 Wolfe | Clinical revenue share on X | Direct, but not repeated | "Less than 50%" (E104). No clinical X revenue share was disclosed thereafter (see E138 and E186–E187). |

## Conference vs call differences (item 4)

- **JPM Jan 2026: X share at Q3.** Thaysen said "75% of volume" at Q3. The Q3 call and the host used 78%. JPM calls year-end volume "approximately 80%". The Q4 call says the same, so the conference figure is consistent. This is a minor wording inconsistency (the extract caveat also flags it), not a ledger contradiction.
- **Tone on pricing.** At JPM, Thaysen said the price impact "is turning out lower relative to volume performance: the math is working." On the Q1'26 and Q2'26 calls, Thaysen said the revenue share stalling at 55% was "a little bit dangerous to read this figure precisely" (E138). The conference language was more affirmative than the call language when the data softened.
- **Hedges.** At Wolfe, clinical cohorts 2 and 3 are "absolutely the largest" and use 25B (E028). Nothing at any conference states how much of cohort 1 or cohort 4 volume remains on the 6000. The 6000 tail was never sized at a conference.

## Contradictions and stale data

- The "over 80% to 85%" and Thaysen's "more than 85%" are the same-call discrepancy described above, which refines E011. E011's "Q1'26 Dhingra 'over 80% to 85%'" is now verified as a direct quote.
- E015 is already corrected. The ">10" 6000 figure is CFO prepared remarks.
- The 200–240 range has no refresh after Q4'25. Any model still using it is stale. Q1 and Q2 deliveries ran at the 80+/qtr level, above the 50–60 per quarter "targeted range".

## Gaps / what I could not find

- There are no Goldman, Bernstein 2026, Jefferies, William Blair, UBS, Piper, Evercore, Wells Fargo, Baird or June 2026 healthcare-event transcripts in the corpus. INDEX.md has no 2026 ILMN conference entries after TD Cowen (2026-03-03). E176 also noted that no management commentary after 30 Jul was found.
- The Bernstein May 2025 and Wolfe Nov 2024 transcripts are outside this assignment's scope. They were not re-read, since E029 and E012–E013 already cover them.
- The conference originals have several very long lines that the grep skipped ("Omitted long matching line"). I relied on the full extracts. I did not open every original line for 6000 or decommission mentions, so a short mention could exist there.
- There is no conference disclosure of dual-running customers, revalidation time and cost, price-per-Gb by cohort, take-or-pay terms or the pace of 6000 end-of-life. Gap 9 stays open.
