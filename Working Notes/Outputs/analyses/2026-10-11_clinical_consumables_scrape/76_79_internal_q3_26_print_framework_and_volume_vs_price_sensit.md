# Agent 76: 79-internal-Q3-26-print-framework-and-volume-vs-price-sensitivity

*Model: sonnet. Run 2026-10-11 09:52:49. Cost $0.20 (API-equivalent).*

**Assignment:** Use only the local corpus (Core Notes, INDEX.md, the Extracts, the evidence ledger E-numbers and the open gaps file). Build a quantified decision framework for the 29 Oct 2026 Q3'26 print and the Jan 2027 35B price cut. (1) Rebuild HT revenue-at-risk. Take the Q2'26 sequencing consumables of $775M, the X share of 59% of HT revenue and 83% of volume, and clinical at roughly 65% or more of the total. Apply a 60-70% per-Gb price decline and compute the revenue loss if the remaining 17% of volume migrated, at 0%, 15%, 25% and 40% volume uplift on conversion, with the cohort evidence (the '40 fully converted clinical customers'). (2) Add a sensitivity table of clinical Gb growth (20%, 25%, 30%, 40%) against price per Gb decline (10%, 15%, 20%, 25%) to show net clinical consumables growth for FY27, then overlay the 35B cut (about 20% lower $/Gb from Jan 2027) and AXELIOS pricing ($150 per genome). (3) List what the corpus says about parallel running of 6000s and Xs (the Jefferies question on the Q2'26 call), and about how many of the roughly 1,360 NovaSeq 6000s are clinical. (4) Write a falsifiable checklist for the Q3 print: the exact metrics, thresholds that would indicate over-earning or ex-China clinical deceleration (for example growth below 10%), X pull-through below $1.35M, and any dropped disclosure. Cite ledger E-numbers and file names for every input, flag any input that contradicts the stated known facts, and save no files. Hard stop at 20 minutes.

## Key findings

Almost all the framework inputs are already in the ledger (E004–E008, E038, E067, E073–E075, E084, E268–E270). This pass adds new quantification of four ledger items: the uplift grid, the clinical Gb-vs-price grid, the 35B overlay, and the two-year-stack thresholds. I found no new source documents and no contradiction with the stated known facts. All numbers below are OPINION (my calc on FACT or MGMT inputs). I did not search outside the files named below.

**1. Revenue at risk with volume uplift (extends E004/E005).**
- Setup: index HT revenue = 100, so the 6000 is 41 and the X is 59. Q2'26 HT is about $535M/qtr (69% of $775M, as in E003), or about $2.14B/yr. One index point is about $21M/yr.
- The inputs are E001, E004 and E030 (60–70% per-Gb decline).
- The grid shows the loss as a % of HT revenue if 100% of the remaining 6000 Gb moves. Uplift is extra Gb on the converting volume.

| Per-Gb decline | 0% uplift | +15% | +25% | +40% | Break-even uplift |
|---|---|---|---|---|---|
| −60% | −24.6% | −22.1% | −20.5% | −18.0% | +150% |
| −65% | −26.7% | −24.5% | −23.1% | −20.9% | +186% |
| −70% | −28.7% | −26.9% | −25.6% | −23.8% | +233% |

- In dollars, the full range is about −$385M to −$615M a year, or −$96M to −$154M a quarter. The 0%-uplift, −70% cell reproduces E004 (−$617M).
- Uplift barely helps. Even +40% recovers only 5–7 index points, about $110–150M a year.
- If only 80% of the 6000 volume moves (E005, E012), scale every cell by 0.8.

**2. The cohort evidence implies far larger uplift than any scenario.**
- E026 says revenue was flat to under +5% in year 1 for the 40 converted customers. At a −60% to −70% per-Gb price cut, that requires converting Gb to rise about 2.4–3.3x.
- Revenue flat means volume ×1/(1−d), which is +150% to +233%. Revenue +5% adds about 5 points to these.
- That is far above the 0–40% uplift cases and above the company-wide Gb growth of >30%.
- It therefore only fits if the cohort volume is mostly incremental (new assays, exome-to-genome). It does not fit a like-for-like workload moving over.
- E027 (selection bias) and E024 (placements "mostly incremental") point the same way. Treat the cohort as evidence about expansion customers, not about the sticky tail.
- The same logic puts E029 in context. "Volume must rise 100%" breaks even only for a 50% cut.

**3. Clinical net growth grid, (1+Gb growth)×(1−price decline)−1 (extends E075/E083/E084).**

| Clinical Gb growth | Price −10% | −15% | −20% | −25% |
|---|---|---|---|---|
| +20% | +8.0% | +2.0% | −4.0% | −10.0% |
| +25% | +12.5% | +6.3% | 0.0% | −6.3% |
| +30% | +17.0% | +10.5% | +4.0% | −2.5% |
| +40% | +26.0% | +19.0% | +12.0% | +5.0% |

- Reconciliation with E073/E075: clinical ex-China was +15% in Q2'26 and about +17% in H1. At a −15% price decline that implies Gb of +35% to +38% (1.15/0.85 and 1.17/0.85).
- That is "well above 30%" and consistent with the management claim. It means the clinical price decline is probably not worse than mid-teens.
- Whether it is smaller than mid-teens is unresolved. E067's survey implies only −4–5%.

**4. 35B overlay (about −20% $/Gb from Jan 2027, E058; sensitivity to E084).**
- Effective price decline = 1−(1−p)×0.8.
  - If the full cut stacks on a −15% base: −32%.
  - On −10%: −28%.
  - On −20%: −36%.
  - On −25%: −40%.
- Gb growth needed to hold clinical revenue flat:

| Scenario | Gb growth needed |
|---|---|
| −15% only | +17.6% |
| −15% plus the full 35B cut | +47% |
| −15% plus a half-weight 35B cut (only the 25B-flow-cell cohorts reprice, E028) | +30.7% |
| −10% plus the full cut | +38.9% |

- For +10% clinical revenue growth in FY27, the needs are Gb +29% with no 35B, and about +62% with a full 35B cut on a −15% base. This is why the 35B date and its scope matter.
- The main uncertainty is whether the mid-teens management price model already contains the 35B cut. If it does, the stacked rows are double-counting. E047 suggests the model is a long-run average, not a named flow-cell cut.
- AXELIOS comparison (E059, E068):
  - Illumina effective prices are $125–175 per genome and list is about $200.
  - A 20% cut gives about $100–140 effective and about $160 at list, against Roche's $150 list.
  - Parity at list is reached only with the 35B cut.
  - This is not like-for-like (E068: duplex 30x vs Illumina's definition).
  - Roche's no-discount structure matters more for mid-throughput accounts than for the large clinical labs that already get $125.

**5. Two-year-stack thresholds for ex-China clinical growth (extends E073/E074/E270).**
- Comps: Q3'25 +12%, Q4'25 +20%. Two-year stacks: Q1'26 28 (20+8), Q2'26 25 (15+10).
- A constant stack of 25–28 implies Q3'26 clinical of +13% to +16%, since the Q3 comp is easy.
- Under the Q2 call's guidance that FY is mid-teens and H1 was about 17%, H2 averages about 13–14% (E074).
- A Q3 print of 13–16% is therefore "in line". Below 12% is a miss, and below 10% is a clear deceleration. A print at or above 15% leaves a heavy Q4 comp.
- The same stack arithmetic implies Q4'26 of only +5% to +8%, against a 20% comp, if the stack holds. A mid-teens FY needs Q4 well above that, so watch Q3 as a test of the FY guide, not of the run-rate.

## Parallel running and the clinical 6000 count (item 3)

- The Q2'26 call exchange is already E014. One precision from the call itself: Peterson's question framed the slowdown as "clinical consumables slow sequentially" and linked it to the over-earning question [ILMN Q2 2026 call, 2026-07-30, Extracts/ILMN/earnings_call/ILMN_2026Q2_Earnings_Call.md l.125–127]. Thaysen's answer attributed the slowdown to "ins and outs" in the Middle East and Latin America. He did not address dual-running economics. FACT.
- The Q1'26 call extract has no match for "decommission" or a 6000 base count. This is consistent with E020 (disclosure stopped).
- Clinical share of the remaining 6000 is only inferential: about 80–83% of remaining 6000 Gb (E009), and about 75% of clinical survey respondents still own a 6000 (E021).
- No corpus number for clinical 6000 instruments. A rough bound is that a clinical share of 6000 Gb of 80% would be about 17%×0.8 ≈ 14% of total HT Gb, with the 6000 base around 1,300 or lower and unlabeled by segment. This is OPINION and not a count. The 6000 base after FY25 is undisclosed.

## Falsifiable Q3'26 checklist (29 Oct, additions only; base is E270 and E268)

| Metric | In line | Over-earning or deceleration signal |
|---|---|---|
| Ex-China clinical growth | 13–16% | <12% weak; <10% clear break |
| X share of HT revenue (at about 1 pt/qtr volume gain, 84% volume share) | 60–62% | <60% (E270); a stall at 59% means r moved |
| X share of HT volume | 84–85% | Flat at 83% |
| X pull-through, Q3 annualized | at or above $1.21M (H1 level) | Below $1.20M, or Q4 requirement of $1.55–1.67M (E268) unaddressed |
| Clinical X volume share | 79–80% | Below 79% (target 80–85% by YE) |
| Derived 6000 revenue | below $210M | At or above $219M |
| Sequencing consumables | at or above $789M (consensus E050) | Below $775M, i.e. a sequential decline |

Dropped-disclosure watches, as additions to the ledger's list:
- Whether the deck still prints 83%/59% and the clinical X share.
- Whether the FY26 platform pull-through guide ($1.35–1.40M) is silently removed (E268).
- Whether the >10 NovaSeq 6000 sales (E015) are repeated or quantified.
- Whether the Q3 Gb statement keeps the "well above" clinical language.
- Whether 35B timing or pricing is given (E057 says Thaysen declined to price it).

## Contradictions and stale data

- No input contradicts the stated known facts.
- E184 (Q3 as a 14-week quarter) is already corrected in the ledger. I confirmed in the Q2'26 extract that the extra week is in Q4. The extract's "0.5 point" does not square with 1/13 of Q4 consumables (E269 flags this). Note that Dhingra's "largely a consumables story" is a Q4 tailwind, which weakens any Q4 read-through to Q3.
- The break-even in E004 (+240% on converting Gb) is consistent with my +233% at −70% decline. The rounding difference comes from the 70.5% observed ratio.

## Gaps / what I could not find

- Whether the mid-teens price model already includes the 35B cut: no source.
- The share of clinical Gb on 25B flow cells (it determines the 35B overlay weight). E028 says cohorts 2 and 3 are the largest and use 25B, but gives no percentage.
- Any clinical 6000 instrument count, or any dual-running customer count (E020).
- The ledger lines I could not fully inspect (the file shows long lines as omitted) are E200+ and some of the later E-numbers. Material may overlap with items beyond the ~E100 and E200–E270 range that I read.
