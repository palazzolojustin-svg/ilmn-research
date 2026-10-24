# Agent 101: 101-web-shell-GRAIL-Galleri-FDA-briefing-PDFs-and-GRAIL-Illumina-supply-term-decode

*Model: sonnet. Run 2026-10-11 10:27:18. Cost $0.74 (API-equivalent).*

**Assignment:** Close open gap 1. Use Bash/PowerShell to download to disk (curl.exe -L with a browser User-Agent) and decode with pdftotext -layout or pypdf the FDA Galleri advisory-committee briefing PDFs: fda.gov/media/195032, 194909 and 195033. If those fail, search fda.gov for 'Galleri PMA advisory committee briefing'. Extract, with page references and exact short quotes: sequencing platform (NovaSeq 6000 or X), reads or depth per sample, the methylation panel size (CpG count), samples per flow cell, any lab-capacity or throughput statement, and the projected test volumes. Compute Gb per Galleri test and the implied Illumina consumables $ per test at stated NovaSeq X $/Gb rates. Then pull GRAIL's FY25 10-K (gral-20251231) via data.sec.gov or sec.gov/Archives, using curl with the User-Agent 'Research palazzolojustin@gmail.com'. Verify the Illumina supply agreement: term, expiry, notice period (test the claim '28 Feb 2027 / 120-day'), minimum purchase or take-or-pay, price-reduction mechanics, and the royalty-suspension end date (~Dec 2026). Read the Ex. 10.x exhibits and flag which parts are redacted. Also note any GRAIL Q2'26 10-Q or call statements on NHS-Galleri readout timing, the PMA timeline and the cost of goods per test. Quantify the volume (Gb) contribution of MCED to Illumina clinical consumables under 100K, 500K and 1M tests per year. Label FACT, MGMT or OPINION. Hard stop at 20 minutes.

## Key findings

**Status:** the FDA PDF decode failed. This session had no Bash or PowerShell, no `pdftotext`/`pypdf` and no `pdftoppm`, and WebFetch returned only compressed-stream noise for fda.gov/media/195032, 194909 and 195033. The saved binaries are listed under "Gaps". Gap 1 is therefore only partly closed: the supply-agreement terms are tested, but the Galleri depth/CpG/flow-cell data are not.

- **The "28 Feb 2027 / 120-day" claim is supported by a secondary source but still not verified in a primary document I could read.** A search snippet attributed to GRAIL filings reads: "initial term… expire on February 28, 2027… automatically renew for two year terms unless either party provides written notice of non-renewal at least 120 days prior." I could not locate that sentence by fetching the FY25 10-K, which returned only partial text. The date is consistent with the Feb 2017 A&R agreement effective 28 Feb 2017, but the term length in Ex. 10.16 is redacted. [FACT for the snippet; unverified for the filing. Search result 2026-10-11 citing sec.gov/Archives/edgar/data/1699031/000162828026017319/gral-20251231.htm]
- **Implied non-renewal deadline (OPINION, arithmetic):** 120 days before 28 Feb 2027 is about 31 Oct 2026. If a notice window exists, it closes within three weeks of today and just after the 29 Oct Illumina Q3 call. Nothing in the corpus or web shows a notice was given. Watch for a GRAIL 8-K or Q3 10-Q (early Nov).
- **Royalty suspension end is confirmed from a primary exhibit.** The Fourth Amendment (Ex. 10.4 to GRAIL 8-K, 2024-06-21) ties the suspension to the "Disposal Funding Period… until and unless GRAIL consummates a GRAIL Change of Control". It defines an "Interim Period" ending at "the 30 month anniversary" of the separation. 21 Jun 2024 plus 30 months is about 21–24 Dec 2026, which matches the 10-K wording "suspended until December 24, 2026 or any earlier change of control". [FACT. https://www.sec.gov/Archives/edgar/data/1699031/000119312524167037/d797014dex104.htm]
- **Royalty mechanics (FACT per 10-K snippet):** 9% in perpetuity on net sales in oncology, with third-party anti-stacking down to a 7% floor. GRAIL "expects" 7%, falling to 5% after cumulative payments to Illumina reach $1B. Royalties that would have been paid during suspension are "deemed paid" toward the $1B. The royalty survives termination of the supply agreement.
- **Redaction check (new):** In Ex. 10.4 the $ cumulative threshold and the floor % are shown as "$[***]" and "[***]%". The 10-K discloses these figures in text ($1B and 5%, per the snippet), so the redaction does not hide them from investors. In Ex. 10.16 (A&R agreement, S-1 2020, https://www.sec.gov/Archives/edgar/data/1699031/000162827920000227/ex1016-grailsx1xamende.htm) these items are redacted:
  - Section 13.1 Initial/Renewal Term durations.
  - Section 4.1 royalty percentages.
  - Section 4.2 annual revenue/royalty targets, with years running through 2027.
  - Section 6.2 exclusivity period.
  - Sections 7.2–7.4 milestones.
  - The binding-forecast window ("first [***]").
- **Pricing mechanics (FACT, Ex. 10.16):** consumable prices are "Illumina's then current List Price" less discounts set in Exhibit A (contents not visible). The corpus's earlier finding of no take-or-pay on consumables (E279 correction) is consistent: I saw no purchase minimum, only monthly forecasts that are binding for a redacted initial period. Royalty targets by year to 2027 exist but are redacted. This refines E279: the "minimums" run through 2027 and the royalty obligation is not tied to supply termination.
- **Royalty size vs sequencing spend (OPINION, computed from E178 inputs):**
  - At 7% of Q2'26 revenue per test (~$698), the royalty is about $49/test, or about $9M a year on 185K tests (FY25).
  - That likely exceeds Illumina's consumables take per test (see below) once the suspension ends in Dec 2026.
  - So the GRAIL economics for Illumina in 2027 are royalty-led, not Gb-led. The royalty is not clinical consumables revenue.
- **Other Q1'26 data points (FACT, Quartr summary):**
  - Q1'26 cost of screening revenue was $21.2M, up 24%.
  - FY26 Galleri sales growth guidance is 22–32%.
  - Long-term gross margin target is 50–60%.
  - Management expects "modest ASP declines in 2026".
  - 10-K: PMA submitted January 2026; more than 475,000 cumulative tests and more than 185,000 in 2025.
  - Source: https://quartr.com/events/grail-gral-q1-2026_F3fAgQrv
- **Illumina has not been a related party since 17 Nov 2024**, per the 10-K text. The ledger says "since Q4'25"; this wording gives a Nov 2024 date and should be checked against R20. [FACT, 10-K fetch 2026-10-11]

## MCED Gb contribution to Illumina clinical consumables (OPINION, scenario arithmetic)

Depth per test is not verified. I use two bounds from ledger E178's correction: about 8.5 Gb (possible "4x" throughput change) and about 34 Gb (legacy CCGA). Dollars use illustrative rates of $2, $3 and $5 per Gb, which are my assumptions, not sourced X list prices. Per-test sequencing cost is about 17 × $/Gb... per 8.5 Gb: $17, $26, $43; per 34 Gb: $68, $102, $170.

| Tests per year | Gb at 8.5 Gb/test | Gb at 34 Gb/test | $ at $3/Gb (8.5 / 34 Gb) |
|---|---|---|---|
| 100K | 0.85M | 3.4M | $2.6M / $10M |
| 185K (FY25 actual) | 1.6M | 6.3M | $4.8M / $19M |
| 500K | 4.25M | 17M | $12.8M / $51M |
| 1M | 8.5M | 34M | $25.5M / $102M |

- **Scale:** FY25 sequencing consumables were $2,939M and clinical is more than 65%, so about $1.9B+ (ledger inputs). Even 1M tests at 34 Gb and $3/Gb is about $102M, around 5% of clinical consumables. At 8.5 Gb it is about 1%.
- **Management's view is consistent:** "we don't really see that in the number today" (E078, MCED).
- **Cross-check (OPINION):** GRAIL's Q2'26 screening cost was about $382 per test (E178). Sequencing at $26–$102 is roughly 7–27% of that, so most of the cost is labor, lab and other items, not Illumina consumables.
- **Upside case:** NHS-Galleri missed its primary endpoint (E320), so a near-term jump to 500K or more tests depends on FDA approval and US payer coverage, not the UK.

## Contradictions and stale data

- E178 says the commercial depth is "possibly ~8.5 Gb (unverified)". I could not verify or refute this; the FDA submission may use an "updated version" with different depth.
- The "since Q4'25" note on Illumina's related-party status in the E279 correction conflicts with the 10-K text, which says 17 Nov 2024. Unresolved.
- The Ex. 10.4 redaction of the $1B and 5% figures sits against their disclosure in 10-K text. This is not a contradiction, but anyone relying on the exhibit alone would miss them.

## Gaps / what I could not find

- **FDA briefing PDFs not decoded.** All three fetched but unreadable: 195032 (281KB), 194909 (925KB), 195033 (371KB). Saved to `C:\Users\palaz\.claude\projects\C--Users-palaz-OneDrive-Documents-ILMN-Claude-Code-Local-Folder--Build-sandbox\452d9596-d3b6-4b2e-ae4c-8379ba6b38dc\tool-results\` as `webfetch-1791732334917-b3tyut.pdf`, `webfetch-1791732335269-m32no8.pdf` and `webfetch-1791732335882-lisb7j.pdf`. They need a Bash session to run `pdftotext -layout`, then a search for "NovaSeq", "flow cell", "reads", "CpG", "capacity" and "throughput".
- Not found: platform (6000 or X), reads per sample, CpG count, samples per flow cell, lab capacity, projected volumes, COGS per test, NHS-Galleri readout timing statements in the 10-Q. WebFetch could not reach the deep text of the 10-K or Q3'25 10-Q.
- The 10-K supply-agreement paragraph (term, 120-day notice) was seen only in a search snippet. It needs a full-text read of Item 1/Risk Factors in `gral-20251231.htm`.
- investors.grail.com and Justia returned 403.
- The Ex. 10.16 term and renewal lengths stay redacted, so a literal "28 Feb 2027" check against the contract is impossible. Only the filing text can confirm it.

**Sources:** SEC Ex. 10.4 (2024-06-21): https://www.sec.gov/Archives/edgar/data/1699031/000119312524167037/d797014dex104.htm. SEC Ex. 10.16: https://www.sec.gov/Archives/edgar/data/1699031/000162827920000227/ex1016-grailsx1xamende.htm. GRAIL FY25 10-K: https://www.sec.gov/Archives/edgar/data/1699031/000162828026017319/gral-20251231.htm. Quartr Q1'26: https://quartr.com/events/grail-gral-q1-2026_F3fAgQrv.
