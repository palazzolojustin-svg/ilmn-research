# Agent 29: 29-web-customer-10K-raw-text-purchase-obligations-and-vendor-concentration

*Model: sonnet. Run 2026-10-11 02:43:30. Cost $0.99 (API-equivalent).*

**Assignment:** Goal: close open gaps 4, 5 and 6 by reading raw filing text. WebFetch truncates, so use Bash (curl with a User-Agent header such as 'Research palazzolojustin@gmail.com') or PowerShell Invoke-WebRequest to download filings from sec.gov Archives, save them under C:\Users\palaz\OneDrive\Documents\ILMN Claude Code Local Folder\Inbox\_scratch_29\, then grep them locally. Use data.sec.gov submissions JSON to find the accession numbers. Also try the XBRL R-pages (R2.htm, R4.htm and so on) and the Financial_Report.xlsx. Do not repeat the Natera §7(l) work or the exhibit reads already done.
(1) Tempus AI FY25 10-K and Q2'26 10-Q: confirm the vendor-payment concentration percentages (33%/39%/33% and the $15.9M payable). State whether the vendor is named Illumina, and quote the sentence. Also pull purchase obligations, any Illumina supply agreement, and the cost-of-revenue discussion on sequencing consumables.
(2) GeneDx: confirm whether the 20% supplier (13% in 2024, 11% in 2023) is Illumina, and read the supply-agreement and purchase-commitment notes.
(3) The same check for Exact Sciences, BillionToOne, Adaptive, Veracyte, Myriad, NeoGenomics and Caris (Note 8). Record for each: sole-source language, supplier-concentration %, minimum purchase commitments ($ and years), reagent-rental or placement terms, and any language on the NovaSeq X transition or per-test sequencing cost.
(4) Guardant: read the Illumina supply agreement exhibit(s) (search EDGAR full-text via efts.sec.gov/LATEST/search-index?q=%22Illumina%22&forms=10-K,10-Q,8-K or the Guardant filing index). Extract term, termination for convenience, price-protection or MFN, minimum purchases, and tariff or surcharge pass-through.
(5) Natera: reconcile the purchase obligations ($261.4M versus '$11.6M') in the 10-K contractual-obligations table or the commitments note. Quote it. Check whether the Eighth Amendment MFN (GRAIL reference) appears in any later amendment.
(6) Illumina FY25 10-K and Q2'26 10-Q R-pages: reagent-rental/sales-type lease numbers ($94.7M estimated future revenue; $18.0M receivable), RPO, deferred revenue, and any customer-concentration or product-transition language not yet captured.
Quantify everything. Return a table (company, Illumina dependence evidence, commitment $, term, quote, URL, accession number). Mark anything unverified as unverified. Hard stop at 20 minutes.

## Key findings

**Result: mostly NO NEW EVIDENCE.** I had no shell or curl in this session, only WebFetch and WebSearch. WebFetch truncates large filings, so I could not download them into Inbox or grep them. I read XBRL R-pages and used targeted searches instead. Only a few checks produced something new, and none of the commitment-dollar or contract-term gaps closed.

1. **E213 (Tempus) is half-verified, and the filing does not name Illumina.**
   - The Tempus FY25 10-K policies note (R14) reads: "The Company relies on a sole supplier for certain laboratory materials, equipment and services. Purchases from this supplier accounted for approximately 33%, 39% and 33% of total vendor payments for the years ended December 31, 2025, 2024 and 2023, respectively." (FACT; https://www.sec.gov/Archives/edgar/data/1717115/000119312526066961/R14.htm, accession 0001193125-26-066961.)
   - The 33/39/33 percentages are confirmed. The note says "a sole supplier", not Illumina. The search tool's "Illumina" wording is its paraphrase, so treat "Illumina" as UNVERIFIED in the financial statement note. Whether the risk-factor text names Illumina was not checked.
   - The $15.9M payable and any purchase-obligation table were not found. R9, R10, R13, R16 and R30 are other notes.

2. **GeneDx's 20%/13%/11% supplier is confirmed verbatim and is also unnamed.**
   - The sentence (R9, "Concentration of Credit Risk and Other Risks and Uncertainties") reads: "One supplier accounted for approximately 20%, 13%, and 11% of purchases for the years ended December 31, 2025, 2024, and 2023, respectively." (FACT; https://www.sec.gov/Archives/edgar/data/1818331/000181833126000015/R9.htm, accession 0001818331-26-000015.)
   - The note also says surplus stock is held and that alternatives exist "for some or all" of the reagents.
   - The risk-factor text (main 10-K) names "Illumina, Inc., Life Technologies Corporation, Twist Biosciences Corporation, Path-Tec LLC and Agilent Technologies" as suppliers. It says "there are only a few other manufacturers...capable of supplying and servicing the equipment necessary for our operations, including sequencers." (FACT.)
   - The unnamed 20% supplier is therefore not proven to be Illumina. It could be any of those five.
   - One search summary claimed Illumina was "an estimated 70-80% of consumables and instrument spend". That is an unsourced estimate from a third-party summary. Ignore it.
   - Rising 11% to 13% to 20% across 2023 to 2025 is a real trend if the supplier is Illumina, but that is unproven.

3. **Natera purchase obligations: $261.4M vs "$11.6M" is still unresolved, but a third figure appeared.**
   - A search of the Natera FY25 10-K (accession 0001104659-26-020881) returned "inventory purchase and other contractual obligations totaling $256,942 thousand, with $171,251 thousand due within one year." This is search-extract only (UNVERIFIED).
   - That is near the $261.4M figure but not equal to it, and nowhere near $11.6M. The $11.6M snippet (E109 correction) remains unsupported.
   - I could not reach the commitments note. R50 to R85 are acquisition, allowance, stock compensation, convertible notes, tax and subsequent-event pages. The commitments note was not located.
   - Subsequent events (R85) show a new San Carlos lease commitment of $39.2M.

4. **Guardant supply agreement (extends E110).**
   - The Jan 2021 8-K (Amendment #5; https://www.sec.gov/Archives/edgar/data/1576280/000119312521004140/d106014d8k.htm) confirms the term runs to January 2033, with automatic one-year renewals afterwards.
   - It says "The Company may also terminate the Supply Agreement for convenience upon 90 days' prior written notice." The amendment "updated the list of specific hardware and consumables, including associated pricing terms for each."
   - The 8-K discloses no minimums or exclusivity.
   - A search summary of the base agreement says Guardant gives a "rolling, non-binding forecast", purchase orders may not be "unreasonably" rejected, and sequencer and service-contract prices are "based on Illumina list prices, subject to discounts that vary depending on the volume of hardware and reagents ordered." (Justia contract 290272 returned a 403, so this is search-extract only.)
   - If correct, this points to no minimum take-or-pay and a Guardant-only exit right, which is much looser than Natera's contract (E192 to E194, E212). It is UNVERIFIED at source.
   - I did not open the exhibits and did not find an MFN, tariff or surcharge clause.

5. **The Illumina "$94.7M reagent-rental" figure (F22, E039) is probably not Illumina's.**
   - Illumina's FY25 10-K (accession 0001110803-26-000024) Note 2 Revenue (R10) has no reagent-rental, sales-type-lease, $94.7M or $18.0M language. Debt and leases (R30), investments (R11) and segments (R20) don't either. The R10 text I did see: remaining performance obligations (RPO) of "$738 million" and contract liabilities of "$346 million and $327 million" at 28 Dec 2025 and 29 Dec 2024. (FACT; https://www.sec.gov/Archives/edgar/data/1110803/000111080326000024/R10.htm.) These match E159 and E198, so they add nothing new.
   - The search that surfaced "$94.7M" returned XBRL pages under CIK 874716, which I believe is another company (probably IDEXX, unconfirmed), alongside the Illumina 10-K link. The search tool likely attributed another company's figure to Illumina.
   - **OPINION:** drop $94.7M and $18.0M from the Illumina ledger entries. F21's zero grep hits for "reagent rental" also support this. Illumina's reagent-rental scale remains undisclosed (E039 stands).
   - The only Illumina lease pages I found were the debt and operating-lease note.

## Table

| Company | Dependence evidence | Commitment $ / term | Quote | URL / accession |
|---|---|---|---|---|
| Tempus | "Sole supplier" is 33%/39%/33% of vendor payments (2025/24/23). Illumina not named in the policies note. | Not found | "relies on a sole supplier for certain laboratory materials, equipment and services" | https://www.sec.gov/Archives/edgar/data/1717115/000119312526066961/R14.htm, 0001193125-26-066961 |
| GeneDx | One unnamed supplier is 20%/13%/11% of purchases (2025/24/23). Illumina is one of five named suppliers. | Not found | "One supplier accounted for approximately 20%, 13%, and 11% of purchases" | https://www.sec.gov/Archives/edgar/data/1818331/000181833126000015/R9.htm, 0001818331-26-000015 |
| Natera | Sole supplier (E109). | $256.9M total, $171.3M within 1 year (search extract, UNVERIFIED) | not read in filing | 0001104659-26-020881 |
| Guardant | Supply agreement to Jan 2033 with 90-day convenience termination. List-minus-volume-discount pricing and non-binding forecasts are search-extract only. | No minimums disclosed in the 8-K | "may also terminate the Supply Agreement for convenience upon 90 days' prior written notice" | https://www.sec.gov/Archives/edgar/data/1576280/000119312521004140/d106014d8k.htm, 0001193125-21-004140 |
| Illumina | RPO $738M and contract liabilities $346M at FY25 | The $94.7M and $18.0M figures are not found | n/a | https://www.sec.gov/Archives/edgar/data/1110803/000111080326000024/R10.htm, 0001110803-26-000024 |

## Contradictions and stale data

- E213 says Illumina is about 33% of Tempus's vendor payments. The note itself says only "a sole supplier". Mark E213 "unverified naming".
- E039 / F22: the $94.7M and $18.0M figures are likely cross-attributed from another company's filing. Remove them.
- Natera purchase obligations: $256.9M (search) vs $261.4M (earlier) vs "$11.6M" (unverified). They may be different tables or years.

## Gaps / what I could not find

- Not done: Exact Sciences, BillionToOne, Adaptive, Veracyte, Myriad, NeoGenomics and Caris Note 8. No sole-source language, supplier percentages, minimums, reagent-rental terms or X-transition wording were collected for them.
- Not done: the Tempus Q2'26 10-Q, the Tempus $15.9M payable and purchase obligations, the GeneDx commitments note and the Illumina Q2'26 10-Q R-pages.
- Not done: the Guardant exhibits (MFN, tariff and surcharge clauses) and any later Natera amendment checks on the Eighth Amendment MFN.
- Method note: R-page numbers vary by filing and WebFetch returns a summary, not raw text. Reliable work needs a real download. Run `curl -A "Research palazzolojustin@gmail.com"` on the accession paths above, save to `Inbox\_scratch_29\`, and grep locally.

Sources:
- https://www.sec.gov/Archives/edgar/data/1717115/000119312526066961/R14.htm
- https://www.sec.gov/Archives/edgar/data/1818331/000181833126000015/R9.htm
- https://www.sec.gov/Archives/edgar/data/1818331/000181833126000015/wgs-20251231.htm
- https://www.sec.gov/Archives/edgar/data/1576280/000119312521004140/d106014d8k.htm
- https://www.sec.gov/Archives/edgar/data/1110803/000111080326000024/R10.htm
- https://www.sec.gov/Archives/edgar/data/1604821/000110465926020881/ntra-20251231x10k.htm
