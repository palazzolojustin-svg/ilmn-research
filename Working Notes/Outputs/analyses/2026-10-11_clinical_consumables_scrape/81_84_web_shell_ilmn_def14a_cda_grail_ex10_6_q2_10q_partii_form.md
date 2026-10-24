# Agent 81: 84-web-shell-ILMN-DEF14A-CDA-GRAIL-Ex10.6-Q2-10Q-PartII-Form4s-download-to-disk

*Model: sonnet. Run 2026-10-11 10:01:00. Cost $0.16 (API-equivalent).*

**Assignment:** Close open gaps 4 and 5, which are the highest-value unread primary documents. WebFetch truncates these filings, so FIRST confirm you have a working shell (PowerShell or Bash). Then use curl.exe or Invoke-WebRequest with a User-Agent header like 'Research Analyst palazzolojustin@gmail.com' to download each file to a local scratch folder. Strip the HTML to text with python (BeautifulSoup or re) and read the text in chunks with Read offset/limit. If the shell does not work, say so up front and return only what you can verify. Do not guess. Targets: (1) Illumina DEF 14A, accession 0001193125-26-149669, main file d13789ddef14a.htm, under https://www.sec.gov/Archives/edgar/data/1110803/000119312526149669/. Read the full CD&A (page 45 onward). Extract: the annual bonus and PSU metrics and weights, the revenue / operating margin / EPS definitions, any GAAP-to-non-GAAP adjustments to incentive pay, the payout percentages, CEO and CFO pay, the clawback, and any hedging, pledging or 10b5-1 policy. Then download the prior-year proxy (0001193125-25-076900, d910798ddef14a.htm) and produce a metric-by-metric diff covering added or dropped metrics, changed weights and changed targets. Look specifically for any pay metric tied to NovaSeq X placements, clinical growth, or sequencing consumables, and for the removal of one. (2) GRAIL-Illumina supply agreement Exhibit 10.6: find the sec.gov exhibit link from the GRAIL FY25 10-K or 10-Q exhibit index. Read §3.4 (binding horizon), §13 (term, termination, renewal), the Exhibit A discount or price table, and any minimum-purchase or take-or-pay terms. Quote exact wording. State whether the GRAIL price per Gb or per flow cell steps down over time. (3) Illumina Q2 2026 10-Q, accession 0001110803-26-000160, file ilmn-20260628.htm. Read Part II Item 1A (risk factor changes), Item 2 (the repurchase table: shares, average price, dollars), and Item 1 legal proceedings (Note 8 or later notes, including the Delaware/Munich/Element matters and any customer disputes). (4) Form 4 filings for Illumina officers and directors since 1 Jan 2026. Use https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1110803&type=4 or data.sec.gov submissions JSON. Tabulate: filer, date, transaction code (S, F, M, A), shares, price, and whether it was under a 10b5-1 plan. Total the open-market sales. Cite the accession number for every item. Output the findings in the required format and flag anything that contradicts the known facts.

I have no shell in this session. My tools are Read, Grep, Glob, WebFetch and WebSearch, so I can't download to disk or run curl, python or pdftotext. I tried the two cheapest checks and I'm writing up the result now.

## Key findings

- **No working shell (FACT).** Targets 1, 3 and 4 need a download-to-disk script, so they stay unread. I have not guessed at any of their contents.
- **DEF 14A (target 1): still truncated.** WebFetch of `d13789ddef14a.htm` returned text ending at page 37, in the security-ownership tables. It said the table of contents puts "Our Approach to Executive Pay" at page 45, and it returned no CD&A text [sec.gov, fetched 2026-10-11, https://www.sec.gov/Archives/edgar/data/1110803/000119312526149669/d13789ddef14a.htm]. This matches open gap 5, so I did not try the prior-year proxy diff.
- **GRAIL Ex. 10.6 (target 2): one small addition to E257 (FACT, search paraphrase, unverified in the body).**
  - E257 gives a 10-year initial term ending 28 Feb 2027, with two-year automatic renewals unless a party gives non-renewal notice 120 days before.
  - A web search summary adds a **maximum term of 20 years**. That cap would end the agreement at 28 Feb 2037 at the latest, though this is inferred from a 2017 start and the 10-year term, not read from the text.
  - The same summary lists amendments dated 27 Sep 2017, 18 Aug 2021 and 18 May 2023, plus a 21 Jun 2024 amendment extending the royalty suspension until the earlier of 2.5 years or a GRAIL change of control. This is consistent with the 24 Dec 2026 royalty resumption in open gap 3.
  - Source: WebSearch result, 2026-10-11, snippet only. Not verified against the exhibit text.
- **Not retrieved:** §3.4, the Exhibit A discount table, any take-or-pay or minimum-purchase wording, and whether the price steps down over time. The GRAIL-side exhibit link was not found either. The search surfaced GRAIL's DEF 14A and 10-Qs, but not the 10-K exhibit index.
- **10-Q Part II and Form 4s (targets 3 and 4): not attempted.** Earlier attempts hit the same truncation at Note 7. I did not try the Form 4 listings.

## Contradictions and stale data

- No contradictions with the known facts.
- E257 should add the 20-year cap, marked as unverified. It does not change the ~31 Oct 2026 first non-renewal deadline.
- The ledger's 2026-10-11 note that accession -000160 is the Q2 10-Q rather than a Form 4 still stands.

## Gaps / what I could not find

All four targets remain open for a run with a real shell (open gaps 4 and 5):

- DEF 14A CD&A, the prior-year proxy diff, and any placement, clinical or consumables pay metric.
- Ex. 10.6 §3.4, §13 and Exhibit A.
- Q2 10-Q Item 1A, the Item 2 repurchase table, and legal Notes 8 onward.
- Form 4s since 1 Jan 2026, with 10b5-1 flags and an open-market sales total.

Next step: run a script that downloads each file with `curl.exe -A "Research Analyst palazzolojustin@gmail.com"`, strips the HTML with python, and then lets an agent read it in chunks.

NO NEW EVIDENCE beyond the unverified 20-year cap and the amendment dates above.

Sources:
- [GRAIL DEF 14A search result](https://www.sec.gov/Archives/edgar/data/0001699031/000162828026027946/gral-20260428.htm)
- [Illumina DEF 14A](https://www.sec.gov/Archives/edgar/data/1110803/000119312526149669/d13789ddef14a.htm)
