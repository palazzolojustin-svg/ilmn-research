# Agent 109: 110-web-ILMN-accounting-quality-XBRL-GAAP-to-nonGAAP-ICFR-CAMs-receivables-UPLOAD-letters-

*Model: sonnet. Run 2026-10-11 10:43:57. Cost $2.11 (API-equivalent).*

**Assignment:** Close open gap 1 and 2 (agent 106 did not finish). Use data.sec.gov XBRL companyfacts for Illumina (CIK 1110803) in a Bash/Python session, downloading to disk. (a) Build a quarterly table, Q1'23 to Q2'26, of GAAP operating income and GAAP EPS against non-GAAP EPS, listing each add-back (restructuring, acquisition-related, SBC, amortization, GRAIL/legal items) and operating cash flow and FCF. Quantify the gap and flag any add-back category that grew or was newly introduced. (b) Read the FY25 10-K Item 9A (ICFR), all Critical Audit Matter wording for FY22-FY25 (note any change in the matters or auditor language), and the MD&A text explaining the $119M Q4'25 receivables build. Compute DSO and inventory days by quarter. (c) Open the four UPLOAD SEC comment letters (2020-12-03, 2021-11-19, 2023-04-05, 2023-04-17) and the ILMN correspondence, and state whether they concern non-GAAP measures or key metrics. (d) Review ILMN 8-Ks since 2023 for Item 4.02 (non-reliance), 5.02 (executive departures, compensation changes) and 2.02 changes in the reported metrics. Cite accession numbers and URLs. Quantify; flag FACT vs OPINION. Stop at about 20 minutes.

## Key findings

1. **None of the four UPLOAD letters concerns non-GAAP measures, key metrics, revenue recognition or segments (FACT).** I opened the text extract of each on EDGAR; the PDFs were not opened. This closes E373's "not opened" caveat.
   - 2020-12-03 (acc. 0000000000-20-011568): the SEC says it "will not review" the GRAIL Form S-4 (letter dated 2 Dec 2020).
   - 2021-11-19 (0000000000-21-014101): five comments on the Schedule TO-I exchange offer for the GRAIL CVRs (Delaware law condition, "illusory" termination right, Rule 13e-3, fractional shares).
   - 2023-04-05 (0000000000-23-003427): two comments on proxy "overvote" language in the contested-proxy filing.
   - 2023-04-17 (0000000000-23-003796): addressed to Icahn Enterprises' general counsel, not Illumina. It questions the Icahn proxy's claims about board composition, the GRAIL price ($8B vs $10B) and "$50 billion in shareholder value" destroyed.

2. **No Item 4.02 (non-reliance) or 4.01 (auditor change) appears in any Illumina 8-K from 2023-04-25 to 2026-08-17 (FACT).** The EDGAR atom feed lists about 57 8-Ks. I did not see Jan–Apr 2023 filings in the feed.

3. **The FY25 critical audit matter (CAM) does not mention NovaSeq X, which corrects E037.**
   - Inventory excess and obsolescence is the only FY25 CAM. The text cites "future demand, market conditions, and the release of new products that may supersede old ones."
   - The phrase "customer migration to NovaSeq X" is not in the CAM text. Its source is not clear to me.
   - This is the first CAM since FY22 that is not about GRAIL. [FY25 10-K, Ernst & Young report dated 2026-02-11, Sources/ILMN/filing/ILMN_10-K_FY2025.md l.1278-1298]

4. **Item 9A is clean (FACT).**
   - Disclosure controls and ICFR were effective, with no material weakness and an unqualified ICFR opinion from Ernst & Young (auditor since 2000).
   - The only flagged change is the ERP upgrade begun in Q3'25 and due to go live in H1 2027. Management says it "could materially affect" internal controls.
   - A system conversion during the 6000-to-X revenue transition is worth watching, but nothing is wrong today.

5. **The 10-K gives no explanation for the Q4'25 receivables build (FACT).**
   - Liquidity MD&A only lists "increases in accounts receivable" as one driver among several.
   - The cash-flow line is $(108)M in FY25, vs $(25)M in FY24 and $(40)M in FY23.
   - Trade receivables rose from $744M gross to $861M, and no customer exceeded 10% of revenue.
   - A separate "$119M" is deferred income taxes in the same cash-flow statement; the receivables increase on the balance sheet is also $119M ($735M→$854M). Don't conflate them.
   - The Q4'25 call extract has only the FCF figures and no receivables or DSO (days sales outstanding) comment.
   - Fourth-quarter receivables rose +$44M in Q4'23 and +$36M in Q4'24 over the prior Q3, against +$125M in Q4'25. [10-K FY25 l.1121, 1469, 2341; XBRL companyconcept AccountsReceivableNetCurrent]

6. **The GAAP-to-non-GAAP gap is narrowing and mostly reflects the GRAIL divestiture rolling off (FACT plus calc).**
   - The GAAP-to-non-GAAP operating profit gap was $48M (Q1'25), $38M (Q2'25), $30M (Q1'26) and $15M (Q2'26).
   - The H1'26 gap is $45M, or 9% of non-GAAP operating profit. H1'25 was $86M, or 19%.
   - Intangible amortization fell from $48–49M a quarter (Q1'23 and Q1'24) to about $16–18M.

7. **SBC (share-based compensation) is not an add-back (OPINION, inferred).** SBC was $275M in FY25 and $370M in FY24.
   - The reconciliation has no SBC line.
   - The Q2'26 operating gap of $15M is explained by the listed items alone: amortization $18M, step-up $2M, acquisition costs $7M, contingent-consideration gain $(16)M, and transformational initiatives of about $5M (calc from $0.03/share).
   - This is a quality positive: non-GAAP operating margin is burdened by SBC.

8. **Non-GAAP excludes gains as well as costs, which cuts both ways (FACT).**
   - FY25 GAAP EPS was $5.45 against non-GAAP $4.84. The difference is mainly a $333M strategic-investment gain, which is $2.13 per share removed.
   - Contingent-consideration gains of $(32)M in H1'26 and $(32)M in H1'25 are also stripped out, which lowers non-GAAP.
   - I found no evidence that the add-backs flatter non-GAAP profit. Reported add-backs are small relative to the $1.2B quarterly revenue base.

9. **Cash conversion weakened in Q2'26 (FACT).**
   - Q2'26 free cash flow (FCF) was $162M, down from $204M, on operating cash flow of $201M, down from $234M. Capex was $39M, up from $30M.
   - H1'26 FCF was $412M, identical to H1'25, while non-GAAP EPS rose from $2.16 to $2.46 (+14%).
   - Q4'25 FCF was $267M vs $322M in Q4'24, even though FY25 FCF rose to $931M from $695M.
   - [Q2'26 release q226earningsrelease.htm, acc. 0001110803-26-000155; Q4'25 release q4fy25earningsrelease.htm, acc. 0001110803-26-000018]

10. **Inventory days rose through the 6000-to-X transition outside year-end (calc on XBRL).**
    - Inventory days (current inventory ÷ quarterly GAAP cost of revenue × 91) were about 150 in Q1'26 and 147 in Q2'26, against 119–131 in Q4'23–Q2'24.
    - Q4'25 dipped to 128 days, then rebounded.
    - This is in line with E372's falling reserve coverage. Together they are a reasonable Q3 call question.

11. **A new-category check found only one new line (FACT).**
    - "Transformational initiatives" replaced the label "restructuring" by Q1'25.
    - Its content shifted from severance ($47M in FY25) to ERP costs ($14M in FY25, "mainly" in 2026).
    - "Other" in 2025 includes $3M for board membership changes and $2M for a legal accrual.
    - SomaLogic inventory step-up amortization is new in 2026 ($8M in H1'26).
    - The tax lines "GILTI/foreign tax credits" and "incremental non-GAAP tax" appear in the 2023–Q3'24 bridges but not in 2025–26. This is a presentation change, and I could not confirm the reason.

12. **Say-on-pay support improved each year (FACT, calc).**
    - Support was 87% in 2024, about 91% in 2025 and about 93.5% in 2026, based on votes for versus against.
    - Against votes were 16.7M, 11.5M and 8.5M respectively.
    - Auditor ratification drew 7.8M against in 2026, 10.5M in 2025 and 6.8M in 2024.
    - [8-K Item 5.07: 0001110803-24-000030, 0001110803-25-000051, 0001110803-26-000124]

## (a) Quarterly GAAP vs non-GAAP table, Q1'23 to Q2'26

The table sets GAAP operating profit and EPS against non-GAAP EPS, with operating cash flow (OCF) and FCF. Most of the large GAAP swings come from GRAIL (goodwill and IPR&D impairments, contingent consideration) and from the 2024 reversal of the EU fine ($456M of legal accrual), not from the core business. I took figures from the earnings-release exhibits (8-K Ex. 99.1). The figures reconcile to the annual totals (see conflicts below).

| Qtr | GAAP op. profit $M | GAAP EPS | Non-GAAP EPS | OCF $M | FCF $M |
|---|---|---|---|---|---|
| Q1'23 | (64) | 0.02 | 0.08 | 10 | (42) |
| Q2'23 | (88) | (1.48) | 0.32 | 105 | 58 |
| Q3'23 | (754) | (4.77) | 0.33 | 139 | 94 |
| Q4'23 | (164) | (1.11) | 0.14 | 224 | 173 |
| Q1'24 | (111) | (0.79) | 0.98 | 77 | 41 |
| Q2'24 | (1,637) | (12.48) | 1.09 | 80 | 48 |
| Q3'24 | 741 | 4.42 | 1.14 | 316 | 284 |
| Q4'24 | 175 | 1.17 | 0.95 | 364 | 322 |
| Q1'25 | 164 | 0.82 | 0.97 | 240 | 208 |
| Q2'25 | 214 | 1.49 | 1.19 | 234 | 204 |
| Q3'25 | 227 | 0.98 | 1.34 | 284 | 253 |
| Q4'25 | 202 | 2.16 | 1.35 | 321 | 267 |
| Q1'26 | 209 | 0.87 | 1.15 | 289 | 251 |
| Q2'26 | 245 | 1.35 | 1.31 | 201 | 162 |

- **Annual cross-checks:** FY23 GAAP operating profit was $(1,069)M and non-GAAP EPS $0.86 (quarters sum to $0.87). FY24 non-GAAP EPS was $4.16 and FCF $695M. FY25 operating profit was $807M, GAAP EPS $5.45, non-GAAP EPS $4.84 and FCF $931M.
- **Dollar add-backs:**
  - Intangible amortization: $48M (Q1'23), $49M (Q1'24), $16M (Q3'24 and Q3'25), $66M (FY25), $18M (Q2'26).
  - Restructuring: $2M (Q1'23), $36M (Q1'24), $47M severance (FY25).
  - Acquisition costs: $26M (Q1'23), $31M (Q1'24), $22M (H1'26), $15M (H1'25).
  - ERP: $14M (FY25).
  - Legal: Q3'24 reversal $(488)M; FY24 per-share effect $(2.87).
- **Unexplained item:** Q4'25 SG&A adjustments were $0.30 per share (about $47M), against $0.04 in Q4'24. FY25 SG&A adjustments were $0.48. I did not obtain the dollar footnote for Q4'25. A question for the Q3 call: what was in the $0.30?

## (b) CAM wording, FY22 to FY25 (Ernst & Young throughout)

| 10-K | CAMs | Wording note |
|---|---|---|
| FY22 (report 2023-02-17) | GRAIL goodwill impairment ($3.9B); GRAIL contingent consideration ($412M liability, $203M gain) | "Auditing … was complex"; rest-of-text only mentions "forecasted revenues" and discount rate |
| FY23 (2024-02-16) | GRAIL goodwill impairment ($712M); contingent consideration ($387M, $24M gain) | Adds "and required significant auditor judgment" |
| FY24 (2025-02-12) | Contingent consideration ($71M, $315M gain; revenue risk premium); GRAIL IPR&D impairment ($420M) | Goodwill CAM gone. Procedures no longer compare to "analyst expectations" |
| FY25 (2026-02-11) | Excess and obsolete inventory ($564M) only | New subject. "Manual input" data risk flagged |

- **What changed:** the auditor's focus moved from GRAIL valuation to inventory. FY25 is the first CAM to note "accuracy and completeness of the underlying manual inputs provided by supply chain and operations management personnel."
- **Reserve:** the reserve was $133M at year-end 2025 on gross inventory of $697M (19.1%). See E372 for the Q2'26 reserve of $123M.

Quarterly current inventory and receivables (XBRL), with inventory days from GAAP cost of revenue (days ≈ inventory ÷ quarterly cost of revenue × 91):

| Qtr | Inventory $M | Cost of rev. $M | Inv. days | Receivables $M |
|---|---|---|---|---|
| Q1'23 | 586 | 432 | 123 | 665 |
| Q2'23 | 617 | 444 | 126 | 741 |
| Q3'23 | 615 | 435 | 129 | 690 |
| Q4'23 | 587 | 448 | 119 | 734 |
| Q1'24 | 584 | 409 | 130 | 635 |
| Q2'24 | 561 | 391 | 131 | 641 |
| Q3'24 | 574 | 335 | 156 | 699 |
| Q4'24 | 547 | 376 | 132 | 735 |
| Q1'25 | 537 | 358 | 137 | 699 |
| Q2'25 | 575 | 364 | 144 | 701 |
| Q3'25 | 590 | 351 | 153 | 729 |
| Q4'25 | 564 | 400 | 128 | 854 |
| Q1'26 | 611 | 370 | 150 | 738 |
| Q2'26 | 629 | 389 | 147 | 764 |

- Q4 cost of revenue is derived as the full-year figure minus nine months.
- Q3'24 cost of revenue ($335M) is unusually low, so the 156 days there is distorted.
- I did not recompute DSO because E371 already has it for Q4'23–Q2'26.
- [XBRL accessions: 0001110803-24-000010, -24-000024, -24-000044, -24-000052, -25-000019, -25-000046, -25-000060, -25-000073, -26-000024, -26-000092, -26-000160]

## (d) Executive and director 8-Ks not already in the ledger

- **CFO change, 8-K 5.02/7.01, 2024-04-09 (acc. 0000950157-24-000591):** Joydeep Goswami left as CFO and Chief Strategy Officer (effective 15 Apr 2024, with a retention agreement paying a $360,000 lump sum for advisory services).
  - Ankur Dhingra took over: $650,000 base, 65% bonus, $500,000 sign-on bonus (two-year clawback), and a $3.5M equity grant (70% PSUs).
  - The filing says there was no disagreement on "operations or financial reporting." Guidance was reaffirmed in the same 8-K.
  - E328 and E222 do not cover this.
- **General counsel, 8-K 5.02, 2024-10-03 (0000950157-24-001364):** Charles Dadswell stepped down as "mutually agreed separation." He was to be paid a $600,000 advisory lump sum and $620,000 severance.
- **Annual-meeting 8-Ks:** the 2025 filing (0001110803-25-000051) approved the Second Amended and Restated 2015 Stock and Incentive Plan, 124.2M for and 5.3M against.
- **CCO departure:** Cunningham's resignation (effective 16 Jan 2026) gave no reasons, severance or successor in the 8-K (0001110803-26-000006).
- **Credit facility, 8-K 1.01/1.02/2.03, 2026-08-13 (0000950157-26-000888):** a new five-year $1.0B unsecured revolver (maturing 2031) replaced the January 2023 facility. It has a leverage covenant and a $500M accordion. This is a refinancing, not stress.
- **Item 2.05 (exit costs):** there are seven or more 8-K and 8-K/A filings under Item 2.05 (2023-06-26 to 2025-01-14). I did not open them.
- **Thaysen Form 4, 2026-10-05:** he disposed of 1,303 shares at $293.69, leaving 107,770. This supports the 107,770 holdings figure in F15 (E152) over 83,390. The transaction code was not shown to me, so I can't say whether it was tax withholding.
- **Item 2.02 metric-change check:** the Q2'26 release has no new definition language. I saw no dropped or added metric apart from the label changes in key finding 11.

## Contradictions and stale data

- **E037:** the CAM does not name NovaSeq X (key finding 3).
- **E371:** the explanation is not in the 10-K or Q4'25 call extract (key finding 5).
- **Release extractions disagreed with each other for a few cells, so I took the figure that reconciles to the annual total:**
  - Q3'24 GAAP EPS: $4.42 / net income $705M in the Q3'24 release vs $4.03 / $642M in the Q3'25 release. FY24 reconciliation supports $4.42.
  - Q1'24 OCF and FCF: $77M / $41M (Q1'24 release) vs $284M / $251M (Q1'25 release extract). FY24 OCF of $837M supports $77M.
  - Q1'24 non-GAAP EPS: $0.09 and Q2'24 $0.36 in the original releases' extracts, vs $0.98 and $1.09 in the 2025 comparatives. The latter sum to $4.16 for FY24.
  - Treat all my extract-based numbers as moderately reliable until checked against the PDFs or XBRL.

## Gaps / what I could not find

- Bash was disabled, so I could not download companyfacts or compute from the full JSON. I used the companyconcept endpoint for receivables, inventory and cost of revenue.
- Q4'23 to Q4'24 per-category dollar add-backs are missing. I have EPS lines for most quarters and dollar footnotes for only some.
- Non-GAAP operating profit by quarter before Q1'25 is missing (needed for a full operating-profit bridge).
- Q4'25 SG&A adjustment footnote ($0.30 per share).
- Item 2.05 8-Ks, the 2023 5.02 filings (CEO transition) and Jan–Apr 2023 8-Ks were not opened.
- No management explanation for the Q4'25 receivables build was found; it would need the full Q4'25 call transcript.
