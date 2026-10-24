# Agent 69: 69-web-shell-SEC-ILMN-DEF14A-CDA-and-Q2-10Q-PartII-via-curl

*Model: sonnet. Run 2026-10-11 03:53:19. Cost $0.07 (API-equivalent).*

**Assignment:** Closes open gaps 5 and 8. Use a shell (Bash or PowerShell) with curl and a declared SEC User-Agent, for example 'Research palazzolojustin@gmail.com'. Do NOT use the fetch/WebFetch tool for SEC pages, because earlier waves failed with it. Save the downloads under Working Notes/Outputs/datasets/ and grep the saved text. (1) DEF 14A, acc. 0001193125-26-149669, file d13789ddef14a.htm. URL pattern: https://www.sec.gov/Archives/edgar/data/1110803/000119312526149669/d13789ddef14a.htm. Read the CD&A from about p.45. Extract: AIP (annual incentive plan) metrics, weights, thresholds, targets and actual results for FY25, and whether the metric definitions changed from FY24 (revenue, EPS, operating margin, any clinical or NovaSeq X metric); PSU (performance share unit) metrics and 2023-25 payout percentages; any discretion or adjustments (non-GAAP exclusions, GRAIL, China); the FY26 plan design and whether any metric was dropped or added; the clawback and hedging/pledging policies; the CEO pay ratio and realized pay; the say-on-pay vote result, with the 8-K Item 5.07 for the annual meeting; stock ownership guidelines; and any perquisites or severance changes. (2) Q2'26 10-Q, acc. 0001110803-26-000160, file ilmn-20260628.htm. Read Part II Item 1 (legal proceedings: SEC investigation, EC/Article 22 or GRAIL fine, Delaware or other suits, Element/BGI/MGI patents), Item 1A (new risk factors, especially on NovaSeq 6000 end-of-life or transition, customer concentration, pricing and China), and Item 5 (10b5-1 plan adoptions or terminations by officers and directors). Also read MD&A text on consumables, pricing, 'mix' and 'utilization' wording. (3) Note 4 and the MD&A bridge: reconcile the GRAIL CVR liability ($54M to $40M) against the $32M favorable SG&A fair-value change and the SomaLogic contingent consideration ($77M at 28 Jun 2026, $30M paid 27 Jul 2026). Quantify each line and say clearly whether the bridge closes. (4) Form 4 filings for ILMN officers and directors from 2026-01-01 to 2026-10-11, using the EDGAR browse or data.sec.gov submissions JSON. Tabulate sales, with date, price, shares, post-sale holdings, and whether the sale was under a 10b5-1 plan or for tax withholding. Quote exact language. Flag anything that looks like a credibility or alignment issue. Return a table of facts with accession numbers.

NO NEW EVIDENCE: I could not run any of the four tasks, because this session has no shell.

**What I checked**
- I read `00_open_gaps.md` and grepped `00_evidence_ledger.md` for the DEF 14A, 10b5-1, Form 4, CVR, SomaLogic, say-on-pay and clawback items.
- The tools available to me are Glob, Grep, Read, WebFetch and WebSearch. There is no Bash or PowerShell tool, and no deferred shell tool has surfaced. I therefore could not run `curl` with an SEC User-Agent, and I could not save any downloads under `Outputs/datasets/`.
- You told me not to use WebFetch for sec.gov pages, because earlier waves failed with it. I followed that and did not retry it, and I did not substitute secondary summaries and present them as primary reading.

**Status of the four tasks**
- **DEF 14A CD&A (gap 5):** not read. This covers the AIP weights, thresholds and actuals, the 2023-25 PSU payouts, discretion, clawback and hedging, the pay ratio, and the say-on-pay result. The ledger holds only the search-extract facts: the CEO AIP target moved from 125% to 150% of salary, the payout was 77% ($1,155,000), and the SCT total is $11,018,895 (corrections to E197).
- **Q2'26 10-Q Part II and MD&A (gap 5):** not read. This covers legal proceedings, the new risk factors, Item 5 10b5-1 adoptions, and the "mix" and "utilization" wording.
- **CVR / SG&A / SomaLogic bridge (gap 8):** not reconciled. I have no Note 4 or MD&A figures beyond what the gaps file already gives. Those are the CVR liability going from $54M to $40M, the $32M favorable SG&A change, and SomaLogic contingent consideration of $77M at 28 Jun with $30M paid on 27 Jul. I can't say whether the bridge closes.
- **Form 4 table, 2026-01-01 to 2026-10-11:** not built from primary filings. The ledger already covers some of it:
  - Meister's sales (E150, E151, E165).
  - Thaysen's tax-withholding filings (E152).
  - Small officer 10b5-1 sales, and Cunningham's plan termination on 9 Feb 2026 (E164).
  - A warning that some accession citations are mislabeled (the correction under E150).

**To close gaps 5 and 8**
Re-dispatch this assignment to an agent that has Bash or PowerShell. The needed URLs are:
- `https://www.sec.gov/Archives/edgar/data/1110803/000119312526149669/d13789ddef14a.htm`
- `https://www.sec.gov/Archives/edgar/data/1110803/000111080326000160/ilmn-20260628.htm`
- `https://data.sec.gov/submissions/CIK0001110803.json`
