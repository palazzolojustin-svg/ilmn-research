# Agent 117: A-web-ILMN-primary-gap-closure-via-mirrors-tariff-reserve-VCP-Q4-25-release

*Model: sonnet. Run 2026-10-11 11:16:24. Cost $1.10 (API-equivalent).*

**Assignment:** Close open gaps #1-#3 with routes earlier agents did NOT use, since sec.gov/s24.q4cdn direct fetches failed. Work in this order and stop at ~20 min. (1) Third-party mirrors and aggregators of Illumina primary text: stocktitan.net, sec.report, last10k.com, quartr, marketscreener, investing.com/fool.com/seekingalpha transcript pages, finance.yahoo.com press-release copies, businesswire.com / globenewswire.com original Illumina earnings releases for Q4'25 (Feb 2026), Q1'26 (May 2026) and Q2'26 (Jul 2026), plus archive.org snapshots (web.archive.org/web/2026*/investor.illumina.com...) of the PDF releases. Extract the full GAAP-to-non-GAAP reconciliation tables: Q4'23-Q2'26 add-backs, the $0.05 'Legal contingency' line, acquisition-related sign and amounts, restructuring, and any new add-back category introduced in 2025-26. Build a quarterly table of add-backs ($M and EPS) and flag every definition change. (2) Tariff and gross-margin text: search the Q1'26 and Q2'26 10-Q MD&A (and the earnings-release/call text) for 'tariff', 'inventory reserve', 'excess and obsolete', 'NovaSeq 6000', 'instrument gross margin', 'consumables gross margin', 'service'. Quantify tariff dollars per quarter, the ~$14M Q1'26 reserve release, and any bp bridge of the Q2'26 gross-margin decline. (3) FY25 variable compensation: find the 2026 DEF 14A CD&A text (Compensation Discussion and Analysis) via mirrors; report the VCP/AIP metrics, weights, thresholds/targets/actuals, whether revenue/EPS were adjusted for the $19M Illumina Foundation donation, any change in metrics vs FY24 (e.g. consumables or clinical metrics dropped, adjusted operating margin definition), LTIP PSU metrics and relative-TSR peer set changes, and CEO pay ratio. Quote exact words; label FACT/MGMT/OPINION; say explicitly which gaps remain unresolved and which URLs failed.

## Key findings

Only three items are new. The first is a sec.gov route that works. The second is a few reconciliation numbers that update the ledger. The third is a confirmed non-result on the CD&A. The Q1'26 and Q2'26 tariff, inventory-reserve and 6000 gaps are still open.

1. **The earnings-release exhibits on sec.gov can be fetched** (WebFetch), contrary to the earlier failures. Gap #1's "raw PDF" requirement is therefore mostly solved, but with caveats. WebFetch returns a model-summarised version of each exhibit, not raw text, and some outputs were garbled (see Contradictions). Working URLs:
   - Q4'25: `https://www.sec.gov/Archives/edgar/data/1110803/000111080326000018/q4fy25earningsrelease.htm`
   - Q1'26: `.../0001110803/000111080326000087/q126earningsrelease.htm`
   - Q2'26: `.../0001110803/000111080326000155/q226earningsrelease.htm`
   - Q4'24: `.../1110803/000111080325000014/a4q24earningsrelease.htm`
   - Q3'25: `.../000111080325000071/a3q25earningsrelease.htm`
   - Q1'25: `.../000111080325000044/a1q25earningsrelease.htm`
   - Q2'25: `.../000111080325000057/a2q25earningsrelease.htm` (not fetched)

2. **The Q4'25 `$0.05` Legal contingency line is $8M.** FACT. It is $10M for FY25 (EPS $0.06). [Q4'25 release, 2026-02-05, sec.gov URL above]
   - Q4'24 was +$18M at the operating-profit level (EPS +$0.11), so it was an add-back, not a reversal.
   - The big negative items are Q3'24 −$488M (EPS −$3.07) and FY24 −$456M (EPS −$2.87). Both are the "reversal of the EC fine, including accrued interest".

3. **Q4'25 add-backs are $73M, bridging GAAP $202M to non-GAAP $275M.** FACT.
   - Cost of revenue $18M, R&D $1M, SG&A $46M and legal contingency $8M. The SG&A $46M matches the ledger correction of $21M acquisition-related, $6M transformational and $19M donation.
   - Q4'25 acquisition-related components: $16M intangible amortisation, $11M contingent-consideration fair-value adjustments and $10M SomaLogic/GRAIL legal and other.
   - Possible sign flip, flagged for verification: Q1'26 shows fair-value adjustments as a $16M offset (a gain) to acquisition costs. Q4'25 appears to show $11M as an add-back (a charge).

4. **Q2'26 reconciliation (new data).** FACT. [Q2'26 release, 2026-07-30]
   - Acquisition-related is $11M in operating profit, $20M in gross profit and $0.07 per share. Transformational is $4M ($0.03). Strategic investment is a $(0.15) gain.
   - Non-GAAP operating profit is $260M (22.5%) versus $252M (23.8%) in Q2'25. GAAP gross margin is 66.4% and non-GAAP 68.2% versus 69.4%.
   - First-half 2026 add-backs are only acquisition-related $35M and transformational $10M. First-half 2025 had $41M transformational, $23M impairment and $5M other.
   - The "Other" line is described as "costs related to board membership changes and $2 million for legal accrual". The board-membership item was already known.
   - **No new add-back category appears in 2026.** Restructuring was relabelled "Transformational initiatives". Severance was $47M in YTD25 and the 2026 content is "implementation costs to upgrade our ERP system". This means add-backs are now less discretionary-looking than in 2025.

5. **Add-backs fell sharply year over year.** The EPS bridge to non-GAAP EPS shrank. FACT.
   - Q1'26 operating-profit add-backs were $30M, versus $48M in Q1'25 ($13M + $30M + $5M).
   - Q2'26 was $15M, versus $38M.
   - The Q1'26 non-GAAP EPS of $1.15 relied on a $0.24 strategic-investment loss add-back and a $(0.15) tax adjustment.

6. **Q1'26 reconciliation, gross margin.** FACT. [Q1'26 release, 2026-04-30]
   - GAAP gross profit is $721M (66.1%) and non-GAAP $744M (68.2%), so the gross-margin add-back is $23M (17 amortisation + 6 inventory fair-value step-up).
   - The step-up amortisation is SomaLogic-related, so about $6M of inventory-cost distortion sits in GAAP COGS.
   - Q1'26 transformational is ERP only, at $6M.

7. **Q2'26 gross-margin narrative (10-Q MD&A text).** FACT. [Q2'26 10-Q, acc. 0001110803-26-000160, via search extract]
   - Excluding the $23M Q2'25 impairment, GAAP gross margin fell "primarily due to an increased sales mix toward lower-margin instruments, rising memory costs, higher freight costs resulting from the Middle East conflict, and contribution of lower-margin SomaLogic revenue, partially offset by lower tariff costs as a result of ongoing operational initiatives."
   - No dollar or basis-point figures are given for any driver. Tariffs are now a tailwind in the text, which supports the ledger's E036 "bridge dropped" point.
   - Q1'26 10-Q text: GM up on "decreases in field service and warranty costs and higher product margins, partially offset by… SomaLogic… and higher tariff costs".
   - This is not a bridge, and Q1 tariffs were still a headwind.

8. **Q2'26 call (Webull transcript copy).** MGMT. CFO: "we did secure additional inventory and supply during the quarter for next several quarters to de-risk any near-term movements in the memory prices". Q3 operating margin is guided about 24% on "higher mix of consumables". No analyst asked about gross margin in the transcript provided. [webull.com/news/15319340255159296, Q2'26 call]
   - Implication (OPINION): the pre-buy raises inventory (the ledger's E037 inventory rise $564M→$655M) for a reason unrelated to the 6000.

9. **Q1'26 call:** gross margin "came in ~150 bp above guidance" per the fool.com summary, and management cited "freight costs and higher cost of electronic components" with "margin improvement expected in the second half". MGMT. [fool.com Q1'26 transcript, 2026-04-30]
   - Q2 operating-margin guidance was about 22%, "reflecting a higher mix of instruments".
   - The ~150 bp beat is from a summariser. Verify before using it.

10. **VCP/AIP for FY25 (partly confirms the ledger, adds one structural point).** FACT. [DEF 14A 2026 via search extract, acc. 0001193125-26-149669]
    - The metrics are revenue and non-GAAP operating income, which were equally weighted in FY24 per the FY24 proxy. Payout is 25% at threshold, 100% at target and 200% at maximum, with actual funding of 77%.
    - FY24 changed the VCP to a single 12-month period, replacing two half-year periods (FY25 proxy, acc. 0001193125-25-076900). That removes the H2 reset opportunity, but this was already in the ledger (files 49 and 115_116).
    - The 97:1 pay ratio (CEO $11,018,895 against a median employee at $113,021) is already in the ledger.

11. **Whether the FY25 VCP was adjusted for the $19M donation remains unresolved.** There is no mention in the search extracts. Because VCP uses non-GAAP operating income and the donation was added back in non-GAAP, the donation was likely excluded from VCP income automatically (OPINION, unverified). The 77% funding is below target even on that basis.

## Add-back table (from the exhibits; "n/p" means not parsed)

| Period | GAAP op profit $M | Cost of revenue | R&D | SG&A | Impairment | Legal contingency | Non-GAAP op profit $M | Non-GAAP EPS |
|---|---|---|---|---|---|---|---|---|
| Q1'24 | 116 | 15 | 4 | 83 | – | n/p | 218 | 0.98 |
| Q3'24 | 741 | 16 | 4 | −29 | – | −488 | 244 | 1.14 |
| Q4'24 | 175 | 17 | 1 | 7 | – | +18 | 218 | 0.95 |
| FY24 | 1,473 | 64 | 6 | −168 | 3 | −456 | 922 | 4.16 |
| Q1'25 | 164 | 19 | 11 | 18 | – | n/p | 212 | 0.97 |
| Q2'25 | 214 | n/p | n/p | n/p | 23 | – | 252 | 1.19 |
| Q3'25 | 227 | 17 | 1 | 20 | – | – | 265 | 1.34 |
| Q4'25 | 202 | 18 | 1 | 46 | – | +8 | 275 | 1.35 |
| FY25 | 807 | 94 | 17 | 76 | – | +10 | 1,004 | 4.84 |
| Q1'26 | 209 | gross-margin add-back 23 | n/p | n/p | – | – | 239 | 1.15 |
| Q2'26 | 245 | gross-margin add-back 20 | n/p | n/p | – | – | 260 | 1.31 |

Notes on the table:
- All rows are FACT as parsed.
- Q1'26 and Q2'26 are split by category, not by line item. Q1'26 is acquisition $24M plus transformational $6M. Q2'26 is acquisition $11M plus transformational $4M.
- FY25 SG&A (+$76M) is far below the sum of Q1–Q4 add-backs (Q1 $18M, Q3 $20M, Q4 $46M, Q2 unknown). The offset is probably the large Q2 and Q3 acquisition fair-value gains.
- The Q3'25 release's "Core Illumina" 9-month non-GAAP EPS of $1.14 and consolidated $3.49 look garbled. Do not use them.

## Contradictions and stale data

- **Parse quality:** the WebFetch summaries contained internal inconsistencies, so treat the numbers as indicative until checked against the raw exhibit.
  - The Q4'24 EPS table shows Q4'23 column values identical to FY23 (for example non-GAAP EPS $4.00 in both). Q4'23 cannot be used from this extract.
  - Q1'26: the SG&A non-GAAP of $242M and the stated gross-margin adjustment of $23M do not reconcile with a $30M total operating-profit adjustment. The operating-profit totals ($209M to $239M) and the footnote components are internally consistent. The cost-of-revenue and SG&A line splits are not.
  - Q1'26 acquisition footnote components (17 + 15 + 6 − 16 = 22) differ slightly from the stated $24M, so there is an unstated residual of about $2M.
  - The summariser stated FY25 non-GAAP gross margin "improved to 68.2% from 68.6%". That is a decline. The numbers are probably right and the verb is wrong.
- **Ledger E034 note:** the Q1'26 GAAP gross margin is 66.1% versus 65.6%. The ledger's non-GAAP figure of 68.2% (+80 bp) matches this source.

## Gaps / what I could not find

- **Gap #3 (tariff dollars per quarter, the Q1'26 ~$14M reserve release, 6000-specific E&O, instrument versus consumables gross margin, and a bp bridge for Q2'26): not resolved.** The 10-Q MD&A is truncated by WebFetch before the gross-margin section on both the Q1 and Q2 filings. The only wording found is qualitative, as above. The releases and calls contain no tariff dollar figure. The Q3'26 call question remains the fallback.
- **Gap #2 (CD&A):** the sec.gov DEF 14A fetch ends at "Proposal 1: Election of Directors" (about page 38), before the CD&A (page 45). Not retrieved: the thresholds, targets and actuals for revenue and non-GAAP operating income, any donation adjustment, PSU metrics and the relative-TSR peer set. No change in VCP metrics versus FY24 was found. The metrics are the same two as FY24 with a single 12-month period.
- **URLs that failed or were empty:**
  - 403: app.edgar.tools (Q1'26 release)
  - Empty or irrelevant: barchart.com Q4'25 release; daytraders.com; the proxyvote.com notice (cover page only); gloom.sh (one line only); stocktitan.net DEF 14A (revenue and operating-income weights only, and its "$4.34B/23.1%" results are the company's reported figures).
  - Truncated: the Q1'26 and Q2'26 10-Q MD&A, and the DEF 14A.
- **Not attempted:**
  - Raw EDGAR iXBRL "R" pages for the MD&A.
  - The Q4'23 to Q3'24 releases, apart from the Q4'24 and Q3'25 exhibits.
  - The archive.org PDFs.
  - EDGAR full-text search for the CD&A phrases.
  - A direct curl download of the proxy, which agents 49/53 did locally and which may be the only route to the CD&A.
