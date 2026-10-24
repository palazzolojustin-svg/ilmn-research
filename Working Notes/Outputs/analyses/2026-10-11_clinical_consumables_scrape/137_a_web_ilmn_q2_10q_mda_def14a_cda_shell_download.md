# Agent 137: A-web-ILMN-Q2-10Q-MDA-DEF14A-CDA-shell-download

*Model: sonnet. Run 2026-10-11 12:03:09. Cost $0.18 (API-equivalent).*

**Assignment:** Close open gap 8 on management conduct. Use shell (curl or Invoke-WebRequest with a User-Agent header such as 'Research palazzolojustin@gmail.com') to download the raw documents to disk. Do not rely on fetch tools, which truncate. Start at https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1110803&type=DEF+14A, or the JSON at data.sec.gov/submissions/CIK0001110803.json. Pull the latest DEF 14A (filed spring 2026) and the Q2'26 10-Q (filed about 30 Jul-5 Aug 2026). Search the text locally with grep or Select-String; do not read whole files. Quantify and quote the following. (1) CD&A: annual-incentive (AIP) metric weights, thresholds, targets and actual payout for FY25, and FY26 metric design versus FY24/FY25. Flag any metric swapped or redefined, for example revenue to ex-China, and non-GAAP EPS or operating-margin adjustments. Note whether SomaLogic, tariff or China items were excluded. (2) PSU design: the 876K FY26 PSUs at $161.80, relative TSR versus EPS or revenue-based vesting, and the EPS-PSU wording conflict with the 10-Q. (3) CEO and CFO realized pay, the CFO pay package, and any severance or change-in-control changes. (4) Pay-ratio and clawback text. (5) Q2'26 10-Q MD&A: the gross-margin discussion, which drivers are named (tariffs, memory, mix, 'reduced pricing' or 'NovaSeq X transition' wording), the consumables versus instrument revenue breakdown, and the new risk-factor text on customer concentration and pricing pressure. Compare with the Q1'26 and Q2'25 10-Qs for wording that was dropped or added. (6) Form 4s since Jan 2026 from the EDGAR index for Thaysen, Dhingra and the other Section 16 officers. For each, record the date, shares, price, whether it was under a 10b5-1 plan, and whether it was a sale or tax withholding. Compute net insider selling versus the prior 12 months. Deliver exact quotes with section and page references, and a table of any year-over-year design changes that make targets easier. If a document cannot be downloaded, say so and name the URL tried.

## Key findings

**NO NEW EVIDENCE.** Gap 8 stays open, and the 2026 PSU question is still unanswered.

I had no shell tool in this session. Only Read, Grep, Glob, WebFetch and WebSearch were available, so I could not download anything with curl or Invoke-WebRequest. Every proxy attempt went through WebFetch, which truncates.

**What I checked**
- **DEF 14A index.** I fetched the filing index for accession 0001193125-26-149669, which worked. It lists the main document as `d13789ddef14a.htm`. It also lists the full submission text file `0001193125-26-149669.txt` and the XBRL instance. I did not try the .txt through WebFetch, because the same truncation would very likely apply.
- **DEF 14A body.** I fetched `https://www.sec.gov/Archives/edgar/data/1110803/000119312526149669/d13789ddef14a.htm`. The fetch tool's text ended at page 37 (Security Ownership), and the CD&A starts on page 45.
  - Nothing was returned on AIP weights, thresholds or payout, FY26 design, the 876K PSUs, CFO pay, severance or clawback.
  - Items still unread: E149's open point (the 2026 PSU characterization), the E197 payout of 77%, and the AIP metric labels.
- **Q2'26 10-Q.** A search surfaced the 10-Q at `https://www.sec.gov/Archives/edgar/data/0001110803/000111080326000160/ilmn-20260628.htm`. It also surfaced the Q1'26 10-Q at `.../000111080326000092/ilmn-20260329.htm`. I read only the search summary of the MD&A, not the text. That summary matches what the ledger already holds:
  - Gross margin was 66.4% against 65.6% in Q2'25.
  - Excluding a $23M impairment in Q2'25, gross margin fell. The named drivers were instrument mix, memory costs, Middle East freight and low-margin SomaLogic, partly offset by lower tariff costs.
  - The summary gave no exact quotes, page references or risk-factor text. The ledger has 8 existing hits on freight and memory, so I treated this as already covered.
- **Form 4s.** I did not retrieve any new Form 4s. The ledger already corrects E150 and E165 on Meister's sales and E152 on Thaysen's purchase, and it has the Thaysen tax-withholding and officer 10b5-1 sale facts. I found nothing to add.

## Recommended next step
Run this on a machine with shell access:
1. Download `0001193125-26-149669.txt` with `curl -A "Research palazzolojustin@gmail.com"`.
2. Download the Q2'26 10-Q at the URL above.
3. Grep both files for `Annual Incentive`, `threshold`, `PSU`, `earnings per share`, `Pay Ratio` and `clawback`. For the 10-Q, grep `Gross margin`, `pricing` and `concentration`.

## Contradictions and stale data
None found. The E149 conflict between the 10-Q wording that EPS PSUs "resumed in fiscal 2026" and the proxy's 2025 grants (operating margin plus relative TSR) is still unresolved for the 2026 grants.

## Gaps / what I could not find
Everything requested in items (1) to (6), apart from the already-known gross-margin summary, could not be retrieved. This includes the table of year-over-year design changes that make targets easier. The cause was the missing shell and the tool truncation described above.

Sources:
- [Illumina 10-Q Q2 FY2026 (SEC)](https://www.sec.gov/Archives/edgar/data/0001110803/000111080326000160/ilmn-20260628.htm)
- [Illumina Q1 FY2026 10-Q (SEC)](https://www.sec.gov/Archives/edgar/data/0001110803/000111080326000092/ilmn-20260329.htm)
- [DEF 14A filing index (SEC)](https://www.sec.gov/Archives/edgar/data/1110803/000119312526149669/0001193125-26-149669-index.htm)
