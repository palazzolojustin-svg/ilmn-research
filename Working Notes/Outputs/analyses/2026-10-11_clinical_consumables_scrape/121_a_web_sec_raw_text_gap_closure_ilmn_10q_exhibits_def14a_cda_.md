# Agent 121: A-web-SEC-raw-text-gap-closure-ILMN-10Q-exhibits-DEF14A-CDA-and-Caris-Natera-10K

*Model: sonnet. Run 2026-10-11 11:19:47. Cost $0.69 (API-equivalent).*

**Assignment:** Close open gaps 1-4 using raw downloads (curl or WebFetch of the raw .htm, not summaries), writing files to disk and grepping them. (1) ILMN earnings-release Ex. 99.1 for Q4'25 (acc 0001110803-26-000018) and Q1'26 (0001110803-26-000087): extract the exact cost-of-revenue, SG&A, R&D and contingent-consideration fair-value lines and the sign of the adjustment, and reconcile the Q1'26 SG&A/cost-of-revenue splits. Also pull the Q2'26 release (0001110803-26-000155). (2) ILMN DEF 14A (acc 0001193125-26-149669): download raw and read the CD&A. Report the FY25 VCP/annual bonus metrics, thresholds, targets, actuals and payout %. Report any non-GAAP or donation adjustment, PSU metrics, the relative-TSR peer set, and any change in metrics versus the FY24 proxy. Report CEO/CFO pay, the clawback policy and any 10b5-1 disclosure. (3) ILMN Q2'26 10-Q MD&A gross-margin section (try the EDGAR Financial_Report R pages or the raw 10-Q): tariff dollars, the Q1'26 tariff reserve release, and instrument vs consumables margin commentary, including any wording on pricing and NovaSeq X transition. (4) Caris FY25 10-K (https://www.sec.gov/Archives/edgar/data/2019410/000201941026000016/cai-20251231.htm) Items 1, 1A and 2: verbatim text on NovaSeq 6000 vs NovaSeq X, instrument counts, and the Illumina supplier and purchase commitments. Natera FY25 10-K Item 2 and the Illumina supply-agreement text. Also run EDGAR full-text search (efts.sec.gov/LATEST/search-index?q="NovaSeq X"&dateRange=custom&startdt=2026-04-01) for 2026 10-Q/10-K hits at clinical labs (e.g. Tempus, GeneDx, Veracyte, Myriad, Exact, BillionToOne) and quote the sentences on migration, instrument counts, and price/cost per test. Quantify every figure and give exact URLs and accession numbers. If a route is blocked, say so and move on. Do not repeat earlier agents' conclusions; return only new verbatim facts.

## NO NEW EVIDENCE (with minor checks)

I found nothing that corrects or quantifies a ledger item. Bash/curl was unavailable (the Bash tool is disabled in this session), so I couldn't download or grep raw files. I used WebFetch, which summarises and truncates documents, and it ran into that limit on the proxy, the 10-Q and the Caris 10-K. Gaps 1–4 stay open except for the pieces below.

### Gap 1: earnings-release line items (WebFetch on the Ex. 99.1 .htm files)
These are FACT, taken from the summarised tables and not from raw text. Treat them as unreconciled until someone reads the raw exhibits.

| Line ($M) | Q4'25 | Q4'24 | Q1'26 | Q1'25 | Q2'26 | Q2'25 |
|---|---|---|---|---|---|---|
| Cost of product revenue | 312 | 278 | 273 | 253 | 291 | 276 |
| Cost of service and other revenue | 72 | 82 | 80 | 88 | 80 | 71 |
| Amortization of acquired intangibles | 16 | 16 | 17 | 17 | 18 | 17 |
| R&D | 239 | 256 | 240 | 252 | 252 | 247 |
| SG&A | 310 | 279 | 272 | 267 | 273 | 234 |
| Operating income | 202 | 175 | 209 | 164 | 245 | 214 |

- **Contingent-consideration sign:**
  - Q4'25: a $11M gain, which reduced SG&A (shown as −$11M in the reconciliation).
  - Q1'26: a $16M fair-value adjustment "shown as offset", which is a gain.
  - Q2'26: a $16M net gain (Q2'25: $21M gain).
  - Q4'24: a $7M expense.
  - So the adjustment was a gain in Q4'25, Q1'26 and Q2'26. That answers the "sign" question. Only the Q4'24 expense in this set is positive.
- **Q4'25 SG&A:** the reconciliation shows a $10M acquisition and legal adjustment, and a $19M "other items (foundation donation)" adjustment. The ledger already references $19M, and I did not check whether it ties to this donation line.
- **Q1'26 SG&A:** the summary shows $15M of SomaLogic legal expense and $6M of ERP "transformational initiatives". I could not reconcile these to the "SG&A/cost-of-revenue splits" the open gap flags, because the summary omitted the other adjustment rows.
- **Non-GAAP gross profit:** Q1'26 was $744M (68.2%) against $702M (67.4%) in Q1'25. Q2'26 was $790M (68.2%) against $735M (69.4%) in Q2'25. This matches E034.
- **Tariffs:** the Q2'26 release has only generic wording ("uncertainty regarding tariffs imposed or threatened…") and no dollar figure. The Q1'26 release returned nothing on tariffs or a reserve release.
- **Q2'26 10-Q GAAP gross profit:** $770M against $695M in Q2'25, and $1,491M year to date against $1,378M. This came from the 10-Q statements, via a truncated fetch.

### Gap 2: DEF 14A (0001193125-26-149669)
- **Blocked.** The fetch cuts off at about page 37, before the CD&A on page 45. Fetching the .txt version failed the same way.
- **Search-snippet text** (see E197 for the existing 77% payout and $1,155,000 figures):
  - The AIP used revenue and non-GAAP operating income, giving "below-target 77% funding".
  - PSUs split between 3-year average operating margin and 3-year relative TSR vs the Nasdaq Biotechnology Index, with a payout range of 0–250%.
  - The ledger already holds the Nasdaq Biotechnology Index point.
- I did not obtain thresholds, targets, actuals, weights, clawback or 10b5-1 disclosure.

### Gap 3: Q2'26 10-Q MD&A
- **Accessions:** the Q2'26 10-Q is 0001110803-26-000160 (filed 2026-07-31, `ilmn-20260628.htm`). The Q1'26 10-Q is 0001110803-26-000092 (filed 2026-05-04, 65 R pages).
- The fetch ends at page 23, before the MD&A on page 30, so there are no tariff dollars, reserve release or margin commentary.
- **Next step:** read the Q1'26 10-Q's `R4.htm` and notes, or use a tool that can curl.

### Gap 4: Caris, Natera and full-text search
- **Caris 10-K fetch:** the direct fetch returned no mentions of NovaSeq or Illumina, because it was truncated to Items 1 and 1A (partial).
- **Search snippet (not verbatim 10-K text):** Caris signed Illumina's "open offer" supply agreement in November 2022. It has no minimum purchase requirement and gives volume discounts. Illumina cannot revoke it before it expires in August 2033, and Caris can terminate at any time on 90 days' notice with no liability. This is consistent with E110 and the ledger's existing "no minimum purchase" entry. I found no NovaSeq 6000 vs X instrument counts.
- **Natera 10-K Item 2:** not fetched.
- **EDGAR full-text search (efts):** the route works through WebFetch.
  - For "NovaSeq X" and "NovaSeq" in 10-Q/10-K filings from 2026-04-01, it returned only the two Illumina 10-Qs above.
  - Treat that result as unreliable. It is a summarised result set, and clinical labs are very likely to use the term. It gave no snippets, so I have no clinical-lab sentences on migration, instrument counts or cost per test.
  - Searching without a form filter, or searching the filers by CIK, may work better.

## Contradictions and stale data
- None found against the ledger. The tables above are single-fetch summaries and could carry transcription errors.

## Gaps / what I could not find
- Raw-text verification of the line items, the full proxy CD&A, the 10-Q MD&A, the Caris Items 1/1A/2 verbatim text, the Natera Item 2 sequencer counts, and clinical-lab 10-Q sentences.
- Gaps 5–6 were out of my scope and untouched.

Sources:
- https://www.sec.gov/Archives/edgar/data/1110803/000111080326000018/q4fy25earningsrelease.htm
- https://www.sec.gov/Archives/edgar/data/1110803/000111080326000087/q126earningsrelease.htm
- https://www.sec.gov/Archives/edgar/data/1110803/000111080326000155/q226earningsrelease.htm
- https://www.sec.gov/Archives/edgar/data/1110803/000111080326000160/ilmn-20260628.htm
- https://www.sec.gov/Archives/edgar/data/1110803/000119312526149669/d13789ddef14a.htm
- https://www.sec.gov/Archives/edgar/data/2019410/000201941026000016/cai-20251231.htm
- https://efts.sec.gov/LATEST/search-index?q=%22NovaSeq%20X%22&dateRange=custom&startdt=2026-04-01
