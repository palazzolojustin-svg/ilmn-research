# Agent 38: 38-web-ILMN-DEF14A-Form4-13D-and-10Q-legal-note

*Model: sonnet. Run 2026-10-11 02:54:48. Cost $1.04 (API-equivalent).*

**Assignment:** Settle open gaps 5 and 6 using primary filings downloaded or fetched by exact URL from sec.gov (Illumina CIK 1110803). Use the EDGAR browse JSON (https://data.sec.gov/submissions/CIK0001110803.json) to list filings, then fetch the index and document pages directly. (1) DEF 14A 2026 (d13789ddef14a.htm): read the CD&A. Extract the 2025 and 2026 annual-incentive metrics and weightings (revenue, operating margin, EPS, any 'clinical' or X-transition metric), changes versus the prior year, the PSU metrics (EPS growth vs operating margin vs relative TSR), the TSR peer group, adjustments to GAAP/non-GAAP for incentive purposes, clawback and hedging policy, the CEO pay ratio, the Summary Compensation Table for Thaysen and Dhingra (reconcile the $11.0M SCT to the $12.3M of equity grants), and the severance and change-in-control terms. (2) Form 4s since Jan 2025 for Thaysen, Dhingra (CFO), Meister, Goswami, Davies and directors: list by person with date, shares, price, transaction code (S, F, M, A) and whether the sale was under a 10b5-1 plan. Reconcile the 44,500-share Meister gap, and compute total insider dollar sales vs purchases. Check for any open-market insider buying. (3) Schedule 13D/13G filings after 2024 (Corvex, Vanguard, BlackRock and so on) and any activist engagement. (4) The Q2'26 10-Q (ilmn-20260628.htm) legal-proceedings note (Note 8, about page 26): the status of the Munich injunction (security amount, whether posted, appeals), the Element and BillionToOne suits, and any new reserve or contingency. (5) 8-Ks since Jan 2025 on officer departures (why CLO Davies left), Item 5.02 compensation changes, and share repurchase authorizations (pace of buybacks vs insider selling). Report the numbers and cite the accession number and URL for each. Flag anything that looks like a metric swap, a definition change, or pay-metric softening.

## Key findings

**Most of what I could reach was already in the ledger. The main new items are the 13G holder map, Davies's 2026 10b5-1 sales, the buyback authorization detail and the Icahn settlement. I could not read the CD&A, Note 8 or most Form 4 detail.**

- **13G holders (new, FACT).** I verified two 13G filings by fetching them from sec.gov.
  - FMR LLC reported 16,169,439 shares, 10.7% of the class, with an event date of 30 Sep 2026, filed 6 Oct 2026 (acc. 0000315066-26-002340). It holds sole voting power over 15,355,487 shares. [sec.gov primary_doc.xml](https://www.sec.gov/Archives/edgar/data/0001110803/000031506626002340/primary_doc.xml)
  - Vanguard Capital Management LLC reported 7,939,213 shares, 5.19%, event date 31 Mar 2026, filed 30 Apr 2026 (acc. 0002100119-26-000648). Sole voting power is 1,344,377 shares. [sec.gov](https://www.sec.gov/Archives/edgar/data/0001110803/000210011926000648/primary_doc.xml)
  - A search summary says The Vanguard Group filed a 13G/A showing 0 shares after an internal realignment effective 12 Jan 2026. Vanguard's stake is now reported by its subsidiaries, so a 13G "drop" there is not a sale. That summary is unverified, and I did not open the filing.
  - FMR is a large long-only holder in the stock while Corvex, the Meister holder named in the ledger, was exiting. This is OPINION only.
- **Activist engagement.** I found no new Schedule 13D on Illumina. The EDGAR listing page I fetched showed only 13G and 13G/A filings, the latest dated 5–6 Dec 2024. Corvex's board seat dates from the 25 Mar 2025 8-K already in E222. The only activist item is old: the Icahn derivative suit over GRAIL (see below).
- **Icahn derivative suit settlement (detail new, FACT).** The Delaware Court of Chancery notice (8-K exhibit, acc. 0001110803-26-000168) says Icahn Partners sued on 17 Oct 2023 over the GRAIL acquisition. A release agreement was executed on 21 Aug 2025. The dismissal hearing is 2 Nov 2026, with an objection deadline of 19 Oct 2026. Dismissal is "with prejudice as to the Plaintiffs only"; other derivative actions continue. The ledger (E159) has the 2 Nov hearing but not the terms. [sec.gov ex991notice8726.htm](https://www.sec.gov/Archives/edgar/data/0001110803/000111080326000168/ex991notice8726.htm)
- **Davies (CLO) kept selling after the Coletti announcement (new, FACT via search summary of Form 4s).** Search summaries of Form 4s (aggregator summary, not opened) report these sales, all under Rule 10b5-1(c) plans:
  - 25 Jun 2026: 615 shares at $180.00, leaving 20,953 shares.
  - 30 Jul 2026: 615 shares at $200.00, leaving 20,338 shares.
  - Both were small, about $111K and $123K. The pattern fits E152's small officer sales.
  - The Form 4s are acc. 0001110803-26-000144 and -000161, found via search and not opened.
  - No Illumina source I could read says why Davies left. The 9 Jul 2026 Coletti release does not mention him. Coletti was Align's chief legal and regulatory officer, and her Align resignation was effective 1 Aug 2026. The cause of Davies's exit remains unknown.
- **Other officer Form 4s (FACT via search summary).** Barnard (CTO) had a Code F tax withholding of 1,259 shares on 15 Feb 2026, leaving 33,435 shares. Pegels had a Code F withholding of 1,164 shares at $116.51, leaving 22,721 shares. Dhingra's 6,100-share purchase at $81.21 leaves him at 24,906 shares, up 32%. That matches E152. None of these are discretionary sales.
- **Buyback authorizations (corrects and quantifies E154, FACT).** The Q2'26 10-Q Note 6, which I read, says:
  - In Aug 2024 the board authorized $1.5B, and in Apr 2026 it authorized a further $1.5B.
  - YTD 2026 repurchases were 2,947K shares for $366M, about $124 a share.
  - $279M remains on the 2024 program and the full $1.5B on the 2026 program at 28 Jun 2026.
  - Illumina is therefore buying more than ~$0.37B of stock in H1'26 while Meister's fund sold ~$586M (E195). Total capacity is $1.78B.
  - Source: [ilmn-20260628.htm, acc. 0001110803-26-000160](https://www.sec.gov/Archives/edgar/data/0001110803/000111080326000160/ilmn-20260628.htm)
- **Munich injunction status (MGMT/FACT, Element's wording).**
  - Element's 14 Jul 2026 release says the judgment is provisionally enforceable once Element posts the court-set security, and that Element "expects to post the required security soon." It also says Illumina can appeal as a first-instance matter.
  - I found no source giving the security amount, saying it was posted, or reporting an appeal. [Element release](https://www.elementbiosciences.com/news/element-biosciences-prevails-in-german-patent-case-against-illumina)
  - I did not obtain the Note 8 text, so I cannot confirm any reserve or contingency.
- **Proxy.** I could not extend E197, E220 or the corrections at lines 255 and 264. The WebFetch tool truncates both the DEF 14A and its XBRL `.xml`. The search extracts only repeat these:
  - 2025 annual incentive plan: revenue and non-GAAP operating income goals, funding at 77%.
  - CEO target raised from 125% to 150%.
  - PSUs on three-year average operating margin for 2025–27 plus relative TSR.
  - The proxy has a CEO pay ratio section, but I could not find the figure.

## Open items from the assignment

- **Pay-metric softening, not resolved.** A search snippet says 2025 PSUs vest on "three-year average operating margin for fiscal years 2025-2027". The ledger's line-264 correction cites an EPS-growth footnote for FY2026–28, and the 2026 grants to Sullivan and Coletti use EPS growth plus relative TSR. Operating margin for 2025 grants and EPS growth for 2026 grants would be a mid-stream metric swap. I cannot say whether it is a swap or two different grants without the CD&A.
- **Not completed:** the SCT reconciliation of $11.0M to $12.3M, the TSR peer group, clawback and hedging terms, severance and change-in-control terms, the Meister 44,500-share gap, a full Form 4 list, and total insider dollar sales vs purchases.

## Contradictions and stale data

- The ledger (E153) says Davies left. Every source I could read still shows him acting as CLO through 30 Jul 2026, selling under a 10b5-1 plan. A 2026 summary also shows him signing filings as CLO on 23 Jun. His departure is therefore tied to the Aug 2026 handover to Coletti.
- Pre-2026 search results describe Davies as acting general counsel after Dadswell stepped down on 3 Oct 2024. Title language (interim GC vs CLO) is inconsistent across sources.
- The Vanguard 13G "zero" amendment and the new Vanguard Capital Management 5.19% filing are the same holdings under different reporting entities. Do not treat the zero as a sale.

## Gaps / what I could not find

- The CD&A, Note 8, Form 4 detail and the Meister gap all need a manual download. Specific paths:
  - DEF 14A: `d13789ddef14a.htm`
  - Q2'26 10-Q: `ilmn-20260628.htm`
  - Form 4 XMLs: acc. 0001110803-26-000144 and -000161, plus the Meister filings.
- Element's Delaware case numbers, the accused-product list and any 8-K on the Munich ruling.
- Why Davies left (no 8-K found).
- The S&P 500 inclusion announcement date.

Sources:
- [FMR LLC Schedule 13G](https://www.sec.gov/Archives/edgar/data/0001110803/000031506626002340/primary_doc.xml)
- [Vanguard Capital Management Schedule 13G](https://www.sec.gov/Archives/edgar/data/0001110803/000210011926000648/primary_doc.xml)
- [Illumina Q2'26 10-Q](https://www.sec.gov/Archives/edgar/data/0001110803/000111080326000160/ilmn-20260628.htm)
- [Chancery notice, 8-K exhibit](https://www.sec.gov/Archives/edgar/data/0001110803/000111080326000168/ex991notice8726.htm)
- [Element release, 14 Jul 2026](https://www.elementbiosciences.com/news/element-biosciences-prevails-in-german-patent-case-against-illumina)
- [Illumina release on Coletti and Sullivan](https://www.illumina.com/company/news-center/press-releases/2026/ed351905-6bf1-45ea-93a3-1b3d833db091.html)
- [ILMN Form 4 listing (search summary)](https://www.sec.gov/Archives/edgar/data/0001110803/000111080326000161/form4.xml)
