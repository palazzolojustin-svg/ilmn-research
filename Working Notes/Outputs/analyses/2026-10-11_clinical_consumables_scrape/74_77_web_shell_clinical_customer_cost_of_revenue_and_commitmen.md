# Agent 74: 77-web-shell-clinical-customer-cost-of-revenue-and-commitments-Guardant-Tempus-GeneDx-Cari

*Model: sonnet. Run 2026-10-11 09:51:28. Cost $0.04 (API-equivalent).*

**Assignment:** Only run if a Bash/PowerShell shell with curl works. Pull the sec.gov filing text or XBRL R-pages for the latest 10-Q or 10-K from Guardant, Tempus, GeneDx, Caris Q2'26, Exact Sciences FY25, Myriad and Veracyte (use data.sec.gov submissions JSON to find accession numbers, with a declared User-Agent). grep the MD&A cost-of-revenue text, the purchase-obligations and commitments notes, and the supplier-concentration text for 'Illumina', 'sequenc', 'flow cell', 'NovaSeq', 'reagent', 'minimum purchase', 'take-or-pay', 'price reduction' and 'per sample/per test'. Quantify for each: cost of revenue per test or per case in the last 6 quarters; the sequencing share of COGS; the stated reason for any change (for example 'lower sequencing reagent costs', 'transition to NovaSeq X'); and the dollar purchase commitments to Illumina by year. Goal: confirm or refute the deflation signal in the Adaptive (E044) and Guardant (E043) evidence against the flat Natera and Caris cost per case, and estimate how much of the clinical customers' sequencing cost decline has already shown up. Return a per-company table with quotes and URLs. Do not re-do Natera, GRAIL or BillionToOne supply agreements, which are already covered. Hard stop at 20 minutes.

NO NEW EVIDENCE

I didn't run this assignment, because it only applies if a Bash or PowerShell shell with curl works. This session has no shell tool. The tools I have are Glob, Grep, Read, WebFetch and WebSearch, so I couldn't call `data.sec.gov` submissions JSON with a declared User-Agent. I also couldn't bulk-download and grep the 10-Q and 10-K text for Guardant, Tempus, GeneDx, Caris, Exact Sciences, Myriad and Veracyte.

I didn't read the evidence ledger or open-gaps file either. I didn't try WebFetch or WebSearch as a substitute, and I checked no filings. A substitute would be slower and less complete than the shell method, and the brief limits this task to the shell route. Partial results could look like confirmation of the Adaptive (E044) and Guardant (E043) deflation signal when none was tested.

**Gaps**
- I have no cost of revenue per test or per case for any of the seven companies over the last six quarters.
- I have no sequencing share of cost of revenue, no stated reasons for changes, and no dollar purchase commitments to Illumina by year.
- I did not test the E043 and E044 deflation signal against the flat Natera and Caris cost per case. I did not estimate how much of the clinical customers' sequencing cost decline has already shown up.

**If you want this covered:** rerun it in a session that has a PowerShell or Bash tool with curl. Otherwise I can do a narrower WebFetch pass on specific sec.gov filing URLs. Tell me which companies to prioritize and I'll start with those.
