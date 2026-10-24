# Agent 26: 26-web-ILMN-filings-governance-insiders-legal

*Model: sonnet. Run 2026-10-11 02:36:58. Cost $0.45 (API-equivalent).*

**Assignment:** Open gaps 6, 7, 8, 9, 12 and 17, which concern management conduct and accounting. Work only from primary documents on SEC EDGAR and Illumina IR. Do NOT repeat the Meister, Thaysen or Dhingra purchase confirmations already in the ledger unless the raw Form 4 contradicts them. (1) Open the Illumina FY25 10-K and Q2'26 10-Q directly and read the revenue-recognition, lease, contract-liability and RPO footnotes. Resolve the conflict over reagent rental: is there a '$94.7M estimated future revenue' and an '$18.0M lease receivable', or not? Quantify sales-type vs operating leases, and any change in RPO and contract liabilities over Q1-Q2'26. (2) Read the cost-of-revenue and gross-margin MD&A text. Find the wording on consumables vs instruments, NovaSeq X productivity, tariffs, and the government-incentive line. Find how GRAIL CVR and other items are treated in non-GAAP. Compare year-over-year wording changes. (3) DEF 14A 2026 CD&A (pages ~45-70; fetch the PDF in chunks if needed): annual bonus metrics, weights and targets, any changes vs 2024/2025, tariff/GRAIL adjustments, PSU design (operating margin plus rTSR; EPS PSUs 'resumed in fiscal 2026'), clawback and hedging policy, pay vs performance, CEO pay ratio. (4) Form 4s: pull raw filings for Thaysen, Dhingra (CFO), Goswami, Barnard, the General Counsel, and the directors Meister/Corvex from Jan 2025 to Oct 2026. Tabulate open-market buys vs sales vs tax withholding, and 10b5-1 plan flags. Resolve the ~44,500-share Meister gap between the 5 and 19 Aug Form 4s, the Rule 144 notice, the Corvex 13D/G and the swap footnotes. Check the date of the S&P 500 inclusion announcement against trade dates. Check whether the proxy or 10-Q addresses Meister's GeneDx role as a related party. (5) The Munich ruling of 14 Jul 2026: read the Q2'26 10-Q legal note, the Illumina statement and ip fray full text. Does the injunction or recall touch NovaSeq X consumables or only MiSeq/MiSeqDx? Is it stayed? Give exact quotes and URLs.

## Key findings

Little of this is new. Two items resolve ledger entries (the Munich ruling, E-number not stated in the gaps file, and the reagent-rental conflict in E039). Most of the SEC fetches came back truncated, so most of the assignment is still open.

1. **Munich ruling (gap 12): it covers only legacy MiSeq/MiSeqDx. Illumina says NovaSeq, NextSeq and MiSeq i100 are not affected.**
   - FACT: On 14 Jul 2026 the Munich I Regional Court found that Illumina Inc. and Illumina GmbH infringe an Element imaging-method patent. It ordered an injunction in Germany and a recall of "infringing systems and reagent kits" put into circulation since 31 Mar 2023, with refunds and return costs. The two entities are jointly liable for damages, and Illumina must give a full account of quantities, customers, prices and profits. [Element release via Business Wire, 2026-07-14, https://www.elementbiosciences.com/news/element-biosciences-prevails-in-german-patent-case-against-illumina; ip fray headline, https://ipfray.com/munich-court-finds-illumina-infringes-element-sequencing-patent-orders-injunction-and-product-recall/ (the full text is paywalled)]
   - FACT: Element's release says the judgment applies to "the MiSeq and MiSeqDx, as well as any other Illumina imaging system that functions as described by the court." That wording leaves the scope open. The release does not name NovaSeq, NextSeq or MiSeq i100.
   - MGMT: Roland Schwillinski, Illumina's VP of global IP and litigation, said in an email (quoted in trade-press snippets): "This anticipated procedural ruling was narrow and limited in scope. The German infringement court addressed only infringement allegations and did not consider the validity of the asserted Element patent." He said it applies only to "legacy MiSeq instruments" and not to MiSeq i100, NextSeq or NovaSeq, "which use different technology." Illumina is developing a software update for the impacted German MiSeqs "to allow Illumina to continue supplying MiSeq reagents in Germany." [search snippet, 2026-07; likely from GenomeWeb/Life Sciences IP Review, https://www.lifesciencesipreview.com/biotech/illumina-ordered-to-recall-products-after-german-patent-ruling. I did not open the page, so verify the quote there.]
   - Stay status: the judgment is "provisionally enforceable once Element posts the security set by the court," and Element "expects to post soon." So it is not stayed by default. It is a first-instance decision that Illumina can appeal, and Illumina has not said whether it will. I did not find the security amount or whether it was posted. [Element release, 2026-07-14]
   - OPINION: The "any other imaging system that functions as described" clause is the one thing to watch. Element's text is broader than Illumina's reading, and the court's actual holding was not read. For NovaSeq X consumables the risk looks low on current evidence. I found no source saying NovaSeq X is covered.

2. **Reagent rental (gap 6, E039): the $94.7M and $18.0M figures are now corroborated, but only through search extracts. I could not read the footnote itself.**
   - FACT (secondary): A search extract of the FY25 10-K says "estimation of future revenues" from reagent-rental arrangements was $94.7M. It says the sales-type reagent-rental lease receivable was $18.0M, down from $19.0M in 2024, with $5.3M of lease receivable reclassified to receivables. [Illumina FY25 10-K, https://www.sec.gov/Archives/edgar/data/1110803/000111080326000024/ilmn-20251228.htm, via search extract]
   - This supports F22 and contradicts F21's "no mentions" grep. Two direct 10-K fetches returned truncated text with no lease note. One of them showed only a section index listing REVENUE and DEBT AND OTHER COMMITMENTS.
   - OPINION: At $18.0M the sales-type receivable is tiny next to FY25 consumables of $2,939M. A $94.7M estimated-future-revenue figure is about 3% of FY25 consumables. Reagent rental looks immaterial to the "over-earning" question. I could not quantify operating vs sales-type leases beyond this.

3. **RPO and contract liabilities: the Q2'26 10-Q confirms the ledger (E159, E198).**
   - FACT: RPO is $1.0B at 28 Jun 2026, about 83% due within 12 months. Contract liabilities are $333M vs $346M at 28 Dec 2025. [10-Q Q2'26, https://www.sec.gov/Archives/edgar/data/0001110803/000111080326000160/ilmn-20260628.htm]
   - New: operating lease right-of-use assets are $362M (vs $370M at Dec 2025), and operating lease liabilities are $454M. These are real-estate leases and say nothing about reagent rental.

4. **PSUs: the 10-Q wording on EPS PSUs is confirmed.**
   - FACT: "In fiscal year 2026, we resumed issuing PSU for which the number of shares issuable is based on our performance relative to specified earnings per share targets (EPS PSU)." [10-Q Q2'26]
   - OPINION: The plan went from operating margin plus rTSR in 2025 to adding EPS in 2026. That needs checking against the DEF 14A, because EPS targets can be flattered by buybacks ($366M in H1'26, E151).

5. **Meister and related party (gap 8e): the proxy appears to disclose no related-party issue. This comes from one summary and needs verification.**
   - FACT (summary): The DEF 14A states "No such transactions occurred in fiscal 2025." The Meister/Corvex footnote says only that his firm's funds hold Illumina shares. I saw nothing on GeneDx. [DEF 14A, https://www.sec.gov/Archives/edgar/data/1110803/000119312526149669/d13789ddef14a.htm]
   - Weak evidence. The proxy covers FY25, and the GeneDx-role question may arise later. The 10-Q excerpt also showed no related-party note.

## Contradictions and stale data
- E039 conflict (F21 vs F22): resolved in favor of F22, with the caveat above.
- The Munich scope is contested in wording. Element says "any other Illumina imaging system that functions as described." Illumina says legacy MiSeq only.

## Gaps / what I could not find
- WebFetch returned only partial text for the 10-K, 10-Q and DEF 14A. I could not read these:
  - The 10-K lease/revenue footnote, so there is no sales-type vs operating split.
  - The 10-Q legal note (Note 8), so Illumina's own disclosure of the Munich ruling is unconfirmed.
  - Any cost-of-revenue MD&A wording on consumables, X productivity, tariffs, the government-incentive line or GRAIL CVR in non-GAAP.
  - The CD&A: bonus weights and targets, tariff/GRAIL adjustments, clawback, hedging, pay ratio and pay vs performance.
- The EDGAR Form 4 index loaded only as a summary: about 100 filings from Mar 2025 to Oct 2026, with clusters on 7-9 Mar 2026 and 22-23 May 2026, and a 4/A on 29 May 2026. I pulled no raw Form 4s, so these remain open: the ~44,500-share Meister gap, 10b5-1 flags, Goswami/Barnard/GC trades, the Rule 144 notice, Corvex 13D/G, and the S&P inclusion date vs trade dates.
- Next step: use a tool that can fetch raw filing text, or download the documents into the Inbox, then re-run this assignment. It would also help to fetch the 10-K and 10-Q R-pages and the Form 4 XML directly.
