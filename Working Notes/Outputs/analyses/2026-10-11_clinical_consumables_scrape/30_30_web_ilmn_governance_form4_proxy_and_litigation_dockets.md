# Agent 30: 30-web-ILMN-governance-form4-proxy-and-litigation-dockets

*Model: sonnet. Run 2026-10-11 02:42:52. Cost $0.60 (API-equivalent).*

**Assignment:** Goal: close open gaps 7, 8 and 10 on management conduct and legal risk, using raw text and alternate docket routes. Download with Bash curl or PowerShell (User-Agent 'Research palazzolojustin@gmail.com') into C:\Users\palaz\OneDrive\Documents\ILMN Claude Code Local Folder\Inbox\_scratch_30\ and grep locally, because WebFetch truncates. Do not repeat the CIK lookups already done.
(1) Illumina DEF 14A filed in 2026 (and 2025 for comparison). Extract from the CD&A: annual bonus metrics and weights, how they changed versus 2024 and 2025 (revenue, non-GAAP operating margin, EPS or other), whether the adjustments excluded China, tariffs or GRAIL items, the 2026 PSU design (EPS PSUs 'resumed in fiscal 2026': metric, targets, payout curve), the TSR comparator group, CEO and CFO pay totals, clawback, hedging and pledging policy, and any retention grants. Quote the wording.
(2) Form 4s for Thaysen, Dhingra, Meister, Goswami, Barnard, the general counsel and directors from Jan 2025 to Oct 2026. Pull the raw XML via data.sec.gov submissions. Tabulate date, transaction code (S, F, M, A), shares, price and the 10b5-1 flag. Resolve the 44,500-share gap for Meister. Compute net open-market sales as a share of holdings, and say whether the sales cluster around earnings, price run-ups or the S&P announcement.
(3) Corvex and other activist or large-holder 13D/13G changes in 2025-26, and any 8-K Item 5.02 exec departures or changes.
(4) Munich Regional Court ruling: open the lifesciencesipreview article and any JUVE Patent, Law360 or German court press release. Verify the quote, the patent number, the security amount, whether it was posted, any appeal, and whether the 'any other imaging system that functions as described' wording reaches the NovaSeq X. Read the Illumina Q2'26 10-Q legal note (Note 8) for the same case and for the BillionToOne suit.
(5) Element Biosciences v. Illumina antitrust: find the docket by an alternate route (RECAP via courtlistener API v4 with curl, Justia Dockets, PacerMonitor, govinfo, Law360 or Reuters). Retrieve the amended complaint (ECF 30) allegations about bundling, exclusivity or rebates, the 23 Jul 2026 reply and hearing dates, and any ruling. Also check the Illumina v. BillionToOne Delaware complaint (filed 2026-05-07) for patent numbers and accused products.
Return dated tables and quotes with URLs and accession numbers. Flag anything that looks like a credibility problem (timing, definitions, comp-metric changes). Hard stop at 20 minutes.

## Key findings

I found little new. I had no shell in this session, so I could not download the raw filings or call the CourtListener API. WebFetch truncated the proxy and returned 403 on several sites. Items 1 to 5 below are new or update a ledger item. The rest of the assignment is still open.

1. **Meister's August sale (corrects E150/E151/E165).**
   - FACT: the Corvex funds sold 741,127 shares on 4–5 Aug 2026 in 14 line items at weighted-average prices of $196–$203.50. That is about $148M.
   - FACT: the funds held 2,830,552 shares before the sale and 2,089,425 after. Meister's direct holding of 6,780 shares was not sold.
   - FACT: the 10b5-1 box is unchecked. The Form 4 was filed 6 Aug 2026, two days after the first sale and one week after Q2 results.
   - The 4 Aug leg was about $147M at a $196–$203 price, not at the $227 peak (the ledger's E165 gives $145–$227 and $227 as the 25 Aug peak). The roughly $430M Aug–Sep leg in the correction notes includes later sales at $224–$232.
   - Source: [Stock Titan Form 4 summary, filed 2026-08-06](https://www.stocktitan.net/sec-filings/ILMN/form-4-illumina-inc-insider-trading-activity-cfc1ed94ed1c.html).

2. **Munich ruling (updates E201 and E215).**
   - FACT: ip fray dated it 15 Jul 2026. Business Wire dated it 14 Jul 2026, and lifesciencesipreview 16 Jul 2026.
   - The patent is DE 112008000363, "Device for detection and its use". This is a German national patent, not an EP.
   - Element says the judgment covers "any other Illumina imaging system that functions as described by the court in its holding."
   - MGMT/OPINION: the court's actual holding was not read, so whether this reaches the NovaSeq X is still unresolved. Illumina says the ruling covers only legacy MiSeq instruments.
   - Sources: [ip fray](https://ipfray.com/munich-court-finds-illumina-infringes-element-sequencing-patent-orders-injunction-and-product-recall/), [Element release](https://www.elementbiosciences.com/news/element-biosciences-prevails-in-german-patent-case-against-illumina), [lifesciencesipreview](https://www.lifesciencesipreview.com/biotech/illumina-ordered-to-recall-products-after-german-patent-ruling).

3. **Element's US patent case (new).**
   - FACT: per a search-result summary, Element is asserting five US patents against Illumina in Delaware: 8,612,161; 9,605,301; 9,909,174; 11,001,887; and 12,656,313. These are from the same family as the German case.
   - The antitrust case remains in N.D. California. Judge Noël Wise dismissed all federal claims on 28 May 2026 with leave to amend.
   - I did not open the underlying document. Treat the patent numbers as unverified until checked. The Delaware patent suit may be a different Element case from the Illumina v. BillionToOne complaint (E094).
   - Source: search summary of [Element's Business Wire release, 2026-07-14](https://www.businesswire.com/news/home/20260714274374/en/), which returned 403 when I tried to open it.

4. **2026 proxy PSU design (partly closes gap 10; updates E149).**
   - FACT: the 2026 proxy shows two PSU tranches outstanding. One vests 3 Jan 2027 on three-year relative TSR against "select companies in the Nasdaq Biotechnology Index", paying 0–200% of target. The other vests 2 Jan 2028 on the 2024–2026 average operating margin, paying 0–200% of target.
   - This is consistent with the ledger's correction that 2025 grants were operating margin plus relative TSR.
   - The 10-Q's EPS PSUs "resumed in fiscal 2026" are still not located in the proxy. The 2026 grants are unverified.
   - Thaysen's FY26 annual cash incentive is $563K threshold, $1,500K target and $3,000K maximum.
   - FACT: Thaysen's 2025 equity grants were $8,306,285 in PSUs and $4,000,265 in RSUs, $12,306,550 in total.
   - Source: [DEF 14A, accession 0001193125-26-149669](https://www.sec.gov/Archives/edgar/data/1110803/000119312526149669/d13789ddef14a.htm) (via search extract). The 2025 DEF 14A is [0001193125-25-076900](https://www.sec.gov/Archives/edgar/data/1110803/000119312525076900/d910798ddef14a.htm).

5. **2026 annual meeting (new).**
   - FACT: the 8-K (Item 5.07, event date 21 May 2026, filed 26 May) shows all nine directors elected, including Meister, and say-on-pay approved.
   - 92.85% of shares were present (141M of 151.9M). The vote percentage for say-on-pay was not stated in the summary.
   - The 8-K has no Item 5.02 departures.
   - Source: [8-K, accession 0001110803-26-000124](https://www.sec.gov/Archives/edgar/data/0001110803/000111080326000124/ilmn-20260521.htm).

## Contradictions and stale data

- WebFetch of the DEF 14A said the proxy was "filed December 30, 2024". That is wrong and is a tool artifact. The accession shows a 2026 filing.
- Search sources date the Munich ruling 14, 15 and 16 Jul 2026. I used the earliest, from Business Wire.

## Gaps / what I could not find

- **CD&A (item 1, still open):** bonus metrics and weights, adjustments for China, tariffs or GRAIL, the TSR peer list, CEO and CFO totals, clawback, hedging and pledging, and retention grants. WebFetch cuts off at about page 38, and the CD&A starts at page 45. This needs a local download.
- **Meister's 44,500-share gap:** not resolved. The August Form 4 reconciles internally (2,830,552 − 741,127 = 2,089,425). The gap probably sits in a different filing, such as the swap termination or a May–Jun Form 4.
- **Other Form 4s:** I did not pull Dhingra, Goswami, Barnard, the GC or directors.
- **Corvex:** I found no 13D/13G filings.
- **Munich details:** the security amount, whether it was posted, and any appeal are not in any source I could open. Element's release says it "expects to post" the security.
- **Element antitrust:** I found no docket, no ECF 30 text and no hearing dates. CourtListener, Law360 and GenomeWeb returned 403 or paywalls, and the A&O Shearman page covers only the May ruling.
- **Q2'26 10-Q Note 8:** unread.
- **BillionToOne:** the Delaware complaint and accused products are not retrieved.
