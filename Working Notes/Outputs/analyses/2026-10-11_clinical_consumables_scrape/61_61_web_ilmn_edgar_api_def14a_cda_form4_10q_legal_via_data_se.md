# Agent 61: 61-web-ILMN-EDGAR-api-DEF14A-CDA-Form4-10Q-legal-via-data.sec.gov

*Model: sonnet. Run 2026-10-11 03:45:34. Cost $1.62 (API-equivalent).*

**Assignment:** Earlier agents (53, 57, 49, 46, 38, 42) failed to read raw SEC text. Use different access routes and say which one worked. Routes in order: (a) fetch https://data.sec.gov/submissions/CIK0001110803.json to list filings, then fetch primary documents from https://www.sec.gov/Archives/edgar/data/1110803/<accession-no-dashes>/<file>. Send a descriptive User-Agent header if the tool allows. (b) EDGAR full-text search at efts.sec.gov/LATEST/search-index?q=... (c) Fallback: search-engine caches, Stocktitan, Last10K, secdatabase, Quiver, OpenInsider, WhaleWisdom or Justia mirrors of the same filings. Targets, in priority order: (1) The 2026 DEF 14A, accession 0001193125-26-149669. Extract the CD&A annual and long-term incentive metrics for FY25 and FY26: whether metrics changed (revenue, non-GAAP EPS, ROIC, TSR, any 'clinical' or 'NovaSeq X' metric), payout percentages, target and actual figures, and any non-GAAP adjustments to comp metrics. Also extract the CEO pay ratio, the CEO and CFO total compensation, clawback and hedging policy, and related-party items. (2) Form 4 filings for ILMN officers and directors from Jan 2025 to Oct 2026 (Jacob Thaysen, Ankur Dhingra, Jake Thaysen's team, Meister, board members). List date, transaction code (S, F, M, A), shares, price, and whether the sale was under a 10b5-1 plan. Total the open-market sales in dollars. Also resolve the 'Meister 44,500-share gap' mentioned in the open gaps. (3) Q2'26 10-Q Item 1A and Part II Item 1 (legal proceedings): Element Biosciences litigation, the SEC investigation, the EC fine and GRAIL divestiture aftermath, and 10x/Roche. Quote exact language and any reserve amounts. (4) The 8-Ks of 8 Jan 2026 and 30 Jan 2026, and any 8-K Item 5.02 executive departures in 2025-26. Quantify dollars and dates. Return a table per item with accession numbers and URLs.

## Key findings

Route used: **(a) worked for index pages, XBRL R-pages and Form 4 text, but only partly for narrative documents.**
- `data.sec.gov/submissions/CIK0001110803.json` and `Archives/edgar/data/0001110803/<acc>/…` (CIK zero-padded) returned filing lists, Form 4 `.txt` files, 8-K primaries and XBRL R-pages (`R2`, `R14`).
- Long HTML documents (the DEF 14A, 10-K and 10-Q) are cut off by the fetch tool. For the DEF 14A it stops at about p.38, before the CD&A.
- The tool's summaries of the submissions JSON mislabel form types and accession numbers. See "Contradictions and stale data".

1. **FACT: The Meister "44,500-share gap" is resolved. It is a ledger arithmetic error, not a missing filing.**
   - The Form 4 for 19–21 Aug (acc. 0001193125-26-361476, filed 21 Aug 2026) shows **679,574 shares sold**: 95,000 on 19 Aug, 285,238 on 20 Aug and 299,336 on 21 Aug. The ledger/file 22_b used 641,814, which is 37,760 too low.
   - Holdings before 19 Aug were 2,089,425 indirect shares (2,069,541 after the first line, plus 19,884). The 2,096,205 figure the earlier agent used includes 6,780 direct shares.
   - 37,760 + 6,780 = **44,540**, which is the gap.
   - The holdings chain then ties exactly: 1,409,851 after 21 Aug; 1,317,075 + 92,776 = 1,409,851 at the start of 25 Aug; 1,033,910 after 27 Aug; **770,350 after 4 Sep**.
   - Source: sec.gov Form 4 text, 0001193125-26-361476. This corrects E150/E151 and file 22_b.

2. **FACT: Corrected Meister/Corvex open-market total is about 3.06M shares and about $592M.** It is 100% Code S, indirect, with the 10b5-1 box false on every Form 4 I opened. Window by window:

| Window | Shares | $M | Accession | Note |
|---|---|---|---|---|
| 13–14 May | 329,460 | 47.9 | 0001011438-26-000335 | Ledger figure, not re-read |
| 28 May–1 Jun | 669,596 | 108.2 | 0001011438-26-000371 | Form 144 daily lines: 220,000 / 214,596 / 235,000 shares |
| 4–5 Aug | 741,127 | 148.2 | 0001193125-26-338361 | Form 144 confirms |
| 19–21 Aug | 679,574 | 145.6 | 0001193125-26-361476 | Ledger had 641,814 sh / about $140M |
| 25–27 Aug | 375,941 | 85.2 | 0001193125-26-371756 | Ledger had 375,541 |
| 2–4 Sep | 263,560 | 57.2 | 0001193125-26-383924 | Ledger confirmed |
| **Total** | **~3,059,258** | **~592** | | |

   - This matches the F03/F07 "$591M" figure and corrects the ledger's ~$586M.
   - Prices rose from $145 in May to $231.23 on 27 Aug. Per the Form 144s, the Sep 3–4 sales were also at about $213–221.
   - Stake: about 4.08M indirect shares before the sales and 770,350 after (E150).

3. **FACT: Form 144s add a notice trail and the acquisition history.**
   - The notices are 0001011438-26-000553 (20 Aug, 355,000 sh, $72.8M) and 0001315863-26-000630 (4 Sep, 150,000 sh, $32.0M).
   - Both say the shares were acquired "in the open market" through counterparties between 25 Oct 2023 and 27 Mar 2025.
   - Sales continued until 4 Sep. The last Form 4 I could confirm in the Meister series is 4 Sep, with no later Illumina sale found.
   - Neither Form 144 discloses a plan adoption date.
   - The 7 Oct 2026 Schedule 13G (0000315066-26-002340) is probably from a third party (the filer-agent prefix differs). I did not open it.

4. **FACT: The 2026 DEF 14A pay ratio and PvP table are new** (acc. 0001193125-26-149669, filed 9 Apr 2026).
   - **CEO pay ratio 97:1.** Thaysen's SCT total is $11,018,895 and the median employee's is $113,021.
   - PvP table (R2.htm), the "company-selected measure" is **"Illumina Revenue"**:

| Item | FY25 | FY24 |
|---|---|---|
| Thaysen compensation actually paid (CAP) | $12,832,816 | $17,689,413 |
| Average non-PEO NEO CAP | $4,562,844 | $6,362,249 |
| Company TSR | 36.47 | 36.56 |
| Peer TSR (Nasdaq Biotech) | 122.07 | 91.53 |
| Net income | $850M | ($1,223M) |
| Revenue | $4,343M | $4,332M |

   - The TSR figures are in the R-page's TSR columns (reported with a % sign by the summary). I read them as cumulative $100-based index values, so treat the units as unverified.
   - OPINION: relative TSR has trailed the peer index since 2021 and Thaysen's CAP rose in 2024–25. That sits awkwardly beside a revenue-only company-selected measure when revenue has been flat for four years ($4.33–4.55B).

5. **FACT/MGMT: The FY25 annual incentive was formula-based on revenue and non-GAAP operating income goals, funded at 77%.** This is from search extracts of the DEF 14A, not from the raw CD&A.
   - Payouts were Thaysen $1,155,000, Dhingra $325,325 and Barnard $300,300.
   - Implied targets are $1.5M (150% of a $1.0M salary), about $422.5K and $390K.
   - This refines E197. It confirms the 125%→150% target raise, but the payout is "below-target" only against a higher target.
   - The ledger's "op margin" label for the AIP may be wrong. I could not read the CD&A to confirm.

6. **FACT: The 8-K 2.01 of 30 Jan 2026 gives the SomaLogic terms** (0001110803-26-000014).
   - **$350M upfront cash**, plus "royalty streams and … up to **$75,000,000** in potential milestone payments to Standard BioTools." It covers all SomaLogic shares and interests in two Sengenics entities.
   - This corrects E146's "$350M upfront" framing. The deal is $350M plus up to $75M of milestones plus royalties.

7. **FACT: Executive departures and board changes in 2026.**
   - **Everett Cunningham**, Chief Commercial Officer, notified Illumina on 4 Jan 2026 that he would resign effective 16 Jan 2026 (8-K Item 5.02, filed 8 Jan 2026, 0001110803-26-000006). No dollar amounts were disclosed.
   - **Daniel Skovronsky, MD, PhD** was appointed to the board on 16 Jun 2026, expanding it from 9 to 10 (0001110803-26-000138).
   - Cunningham terminated a 10b5-1 plan on 9 Feb 2026 (E164), about three weeks after he left.

8. **FACT: The Q2'26 10-Q legal note (Note 8) contains only GRAIL-acquisition litigation** (acc. 0001110803-26-000160, filed 31 Jul 2026, R14.htm).
   - It covers the Delaware derivative cases (Icahn Partners settled with "no payment by any party" per the 21 Aug 2025 agreement; the Pavers action is pending, hearing 13 Feb 2026), the federal securities class action (23-cv-2082-LL-MMP, motion to dismiss opposed 4 Feb 2026), and the state class action (certified 15 May 2026, judgment-on-the-pleadings motion denied 26 Jun 2026, hearing 30 Oct 2026).
   - The note has **no accrual amount**. It gives only boilerplate: a liability is recorded "if it is believed to be probable that a loss has been incurred and the amount of the loss can be reasonably estimated."
   - It does **not mention** the SEC document request, the EC fine, Element, 10x/Roche or BillionToOne. The SEC item in E159 must therefore sit in Part II Item 1 or Item 1A, which the tool truncated. I could not verify its wording.

9. **FACT: Small 10-Q items.**
   - The CVR liability is **$40M** at 28 Jun 2026 vs $54M at 28 Dec 2025 (Note 4).
   - The GRAIL indemnification liability is **$1M** at both dates (Note 7).
   - The 4.650% 2026 notes matured in September 2026. Debt is $2B principal across four notes, and the $750M revolver was undrawn (Note 5).
   - These items are not in the ledger.

## Filings tables

**8-K filings 2025-26 (accession, items):**

| Date | Items | Accession |
|---|---|---|
| 2025-03-24 / 03-25 | 5.02 (and 7.01) | 0001110803-25-000029 / -000032 |
| 2025-05-23 | 5.02, 5.07 | 0001110803-25-000051 |
| 2025-06-23 | 1.01, 8.01 | 0001193125-25-144290 |
| 2026-01-08 | 5.02, 7.01 | 0001110803-26-000006 |
| 2026-01-30 | 2.01, 8.01 | 0001110803-26-000014 |
| 2026-04-02 | 5.02, 7.01 | 0001110803-26-000082 |
| 2026-06-23 | 5.02 | 0001110803-26-000138 |

I read only the Jan 8, Jan 30 and Jun 23 2026 filings. The 2025 5.02s and the 2 Apr 2026 one are unread.

**Other filing identifiers:**
- Q2'26 10-Q: 0001110803-26-000160 (filed 2026-07-31)
- Q1'26 10-Q: 0001110803-26-000092 (filed 2026-05-04)
- FY25 10-K: 0001110803-26-000024
- DEF 14A: 0001193125-26-149669
- Annual report: 0001193125-26-149693
- URL pattern: `https://www.sec.gov/Archives/edgar/data/0001110803/<acc-no-dashes>/<file>`

**Other Form 4s seen (not opened):**
- 0001110803-26-000160, -161 (3–4 Aug)
- -168 and -169 (7 Aug). -169 is filed by **Michael C. Sullivan**, CIK 0002147356, report date 5 Aug 2026, an apparent new insider.
- -175 and -177 (Sep 9–10)
- -180, -181 and -183 (Oct 2–7)

## Contradictions and stale data

- **Meister:** corrected as in findings 1–2. The "$586M" and "641,814 sh" values in E150/E151 and file 22_b are low.
- **Form-type mislabels from the tool's JSON summaries:**
  - 0001193125-26-383924 appeared as "FWP" in the JSON summary, but its EDGAR index page shows Form 4.
  - 0001110803-26-000160 appeared as a Form 4 (4 Aug), but the browse-edgar listing shows it is the **10-Q** filed 31 Jul. The same is probably true of the ledger's citations of -000160 as a Form 4, such as line 308 and E-numbers citing it. Re-check them.
  - A fetch also returned "10-Q" for the Oct 2026 accessions -000180/-181, which other evidence shows are retainer Form 4s.
  - Treat form types and dates from `submissions.json` summaries as unreliable. Verify them from the index page.
- **E149 (PSU metrics):**
  - The 2025 proxy grant description (operating margin plus rTSR, 0–250% payout range) is consistent with the earlier correction.
  - The 10-Q wording that EPS-based PSUs "resumed in fiscal 2026" is still unresolved, because I could not read the 2026 proxy CD&A.
- **AIP metric label:** a search extract says "revenue and non-GAAP operating income," while the ledger and earlier summaries say operating margin. Unverified.

## Gaps / what I could not find

- **CD&A (DEF 14A p.45+):** AIP weights, thresholds and actuals, 2026 PSU metrics, 2023–25 PSU payouts, and any non-GAAP adjustments. The fetch tool truncates at about p.38. It needs a shell with `curl`, or the `d13789ddef14a.htm` file read in byte ranges. The CFO's total compensation was also not obtained.
- **Clawback and hedging policy text**, and Item 408(b) insider-trading-policy disclosure (10-K Item 10/9B). The 10-K fetch was also truncated.
- **Q2 10-Q Part II Items 1, 1A and 5.** These are the SEC investigation wording, any 10b5-1 adoptions or terminations, Element, 10x/Roche and EC fine references. They are cut off by the tool, so I have no verbatim text and no reserve amounts.
- **Officer and director Form 4s other than Meister:** Thaysen, Dhingra, Barnard and Sullivan were not opened, so the all-insider table by code (S/F/M/A) is incomplete. The 7 Aug, 3–4 Aug, 9–10 Sep and 2–7 Oct Form 4s are listed above but unread.
- **8-K Item 5.02 filings** of 24–25 Mar 2025, 23 May 2025 and 2 Apr 2026 (the 2 Apr one is the three-director retirement, per the ledger) are unread. The 7 Aug and 12–13 Aug 2026 8-Ks are already covered (E243).
- **Schedule 13G of 7 Oct 2026** (filer unidentified), and whether any further Corvex sale notice (Form 144) followed 4 Sep.

Sources: all SEC EDGAR, fetched 11 Oct 2026, under `https://www.sec.gov/Archives/edgar/data/0001110803/`.
- Form 4s: `000119312526361476`, `000119312526371756`, `000119312526383924`.
- Form 144s: `000101143826000553/primary_doc.xml` and `000131586326000630/primary_doc.xml`.
- 8-Ks: `000110803626000006`, `000110803626000014`, `000110803626000138`.
- 10-Q: `000111080326000160/R14.htm` (plus `R10`, `R11`, `R13`, `R15`).
- DEF 14A: `000119312526149669/R2.htm` and `d13789ddef14a.htm`.

Search extracts of the DEF 14A are via the sec.gov DEF 14A result pages and the Boardroom Alpha / illumina.gcs-web listings.
