# Agent 120: D-web-Wayback-diffs-of-Illumina-web-pages-and-marketing-claim-fact-check

*Model: sonnet. Run 2026-10-11 11:12:44. Cost $0.07 (API-equivalent).*

**Assignment:** Use web.archive.org (CDX API: web.archive.org/cdx/search/cdx?url=...&output=json, then fetch snapshots) to diff Illumina public pages across 2024-2026 and fact-check management/marketing claims against third parties. Pages: (1) illumina.com NovaSeq X Series product page, specifications table, and NovaSeq 6000 product/support pages (end-of-sale, 'product support lifecycle', service-contract and reagent availability wording, trade-in/upgrade offers); (2) investor.illumina.com pages (Financial Info, Events & Presentations, Key metrics/Supplemental, Governance/Leadership, 'Fact Sheet') to detect removed or renamed disclosures, documents, or leadership entries; (3) the 'cost per genome' / '$200 genome' / '$/Gb' claims and the 35B flow-cell announcement pages; (4) Illumina newsroom press releases 2025-26 that make quantitative or customer claims (e.g. 'customers converted', 'X% of volume', 'Gb on X'), and compare each to the customer's own disclosure or to a later 10-Q. Also check Illumina's 10-K/10-Q Wayback or archived text for deleted or reworded risk-factor language on NovaSeq 6000 transition, customer concentration, reagent rental, and price concessions (compare FY23, FY24, FY25 10-K risk factor headings using sec.gov Archives URLs if reachable). Output a dated change log (what changed, when, why it matters to the over-earning/price-decline thesis or credibility), exact before/after quotes, URLs of snapshots. Label FACT/MGMT/OPINION; clearly state what could not be retrieved.

NO NEW EVIDENCE

I could not retrieve any archived Illumina pages, so there is no change log to report.

- **Ledger and gaps:** I read `00_open_gaps.md` in full. The evidence ledger is over 256KB, so I only searched it for "wayback", "web.archive", "end-of-sale", "lifecycle" and "fact sheet". The only hit was E097, which is CMS data and unrelated to my assignment. I did not read the rest of the ledger.
- **Wayback CDX API:** `web.archive.org/cdx/search/cdx` for the NovaSeq product page is blocked by the fetch tool ("unable to fetch from web.archive.org").
- **Wayback availability API:** I tried `archive.org/wayback/available` for three URLs, and each returned an empty `archived_snapshots`. I treat that as "nothing retrieved", not as proof that no snapshots exist. The URLs were:
  - `illumina.com/systems/sequencing-platforms/novaseq.html`
  - `illumina.com/systems/sequencing-platforms/novaseq-x-plus.html`
  - `investor.illumina.com`
- **Not attempted:** Because snapshots were unavailable, I did not try the FY23, FY24 or FY25 10-K risk-factor comparison on sec.gov. Open gap 1 already records that sec.gov paths returned 403/404.
- **Not checked:** I did not compare newsroom press releases against customers' own disclosures or later 10-Qs.

The Wayback diff work needs a different fetch route, such as a local `curl` against the CDX API run outside this tool.
