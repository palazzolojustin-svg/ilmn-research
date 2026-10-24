# Agent 62: 62-web-clinical-customer-XBRL-and-exhibits-GRAIL-Natera-Guardant-Tempus-GeneDx-Illumina-su

*Model: sonnet. Run 2026-10-11 03:42:38. Cost $0.74 (API-equivalent).*

**Assignment:** Goal: hard numbers on how much clinical labs commit to buy from Illumina and how much they pay per Gb, from filings. Previous agents (29, 34, 41, 50, 54, 58) could not read raw filings. Use the XBRL API instead: https://data.sec.gov/api/xbrl/companyconcept/CIK##########/us-gaap/<tag>.json and https://data.sec.gov/api/xbrl/frames/. Also use exhibit URLs from filing indexes (https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany...) and mirrors (Stocktitan, Last10K, Justia, sec.report, Fintel) as fallbacks. State which route worked. Targets: (1) GRAIL 10-K FY25 (accession 0001628280-26-017319) and Q2/Q3'26 10-Q: the Illumina supply agreement (term to 28 Feb 2027, 120-day non-renewal notice, take-or-pay or minimum purchases, pricing mechanics, price-reduction clauses, royalty resuming 24 Dec 2026), purchase obligations in dollars by year, and cost of sequencing per test. (2) Natera, Guardant, Tempus, GeneDx, Caris, BillionToOne, Exact Sciences, Myriad: the 'Purchase obligations' table and 'Concentration of suppliers' note for FY25 and Q2'26, naming Illumina; reagent supply agreement exhibits (EX-10) with redacted-price terms; any disclosed 'sequencing cost per sample' or 'cost of sequencing as a percentage of COGS' trend; any statement on switching to Element, Ultima or Roche AXELIOS, or on moving from NovaSeq 6000 to X, and the cost saving quantified. (3) Gross margin changes at each customer that management attributes to sequencing cost per Gb. Quantify: Illumina-related purchase commitments summed across customers, versus Illumina clinical consumables (~$1.9B implied by >65% of $2,939M), to estimate how much of clinical revenue is contractually locked. Cite filing, date, page or section and URL.

## Key findings

**Route that worked:** WebSearch located the filing URLs. WebFetch then read the SEC XBRL "R" pages (`.../R##.htm`) and the filing main documents (long documents are truncated). The `data.sec.gov` XBRL API (`companyconcept`) returned 404, and `browse-edgar` returned the wrong entity. Mirrors were not needed.

**Verdict:** Little new, but there are three useful additions.

1. **GRAIL has almost no hard purchase commitment to Illumina** (FACT).
   - GRAIL's FY25 10-K Commitments note (R20) lists "non-lease commitments" of **$52.841M**: 2026 $25.023M, 2027 $23.927M, 2028 $3.633M, 2029 $0.258M.
   - These are described as "primarily… contractual commitments for future use of web services, and laboratory supplies." Illumina is not named as the counterparty.
   - Compare GRAIL's Q2'26 cost of screening of $23.3M (E178). The commitments are therefore about one year of cost of screening, not a lock-in of Illumina volume.
   - Source: [GRAIL FY25 10-K, R20](https://www.sec.gov/Archives/edgar/data/1699031/000162828026017319/R20.htm), accession 0001628280-26-017319.
2. **Quantification for the "contractually locked" question** (OPINION, calc).
   - Across the customers checked, the disclosed hard dollar commitments that could be Illumina purchases total at most about $53M (GRAIL, and that figure includes web services). Natera's is $107M of "material suppliers" with Illumina not named (E227). Guardant discloses none.
   - Illumina's clinical consumables are about $1.9B a year (the brief's estimate). Disclosed dollar lock-in is therefore **under about 5% of that figure**, and probably far less.
   - What exists is short-horizon forecast commitments (E258, Natera's binding 4th month), long-dated terms (E110/E232), and customers' ability to walk away (E232: Caris 90 days; Guardant 90 days, below).
   - Read-through: current clinical consumables revenue is not protected by take-or-pay. It depends on validated-assay switching costs, not contracts.
3. **Guardant has a termination-for-convenience right** (FACT, not in the ledger).
   - Verbatim from its FY25 10-K: "We may also terminate the supply agreement for convenience upon 90 days' prior written notice." The initial term runs to January 2033, then renews in one-year terms.
   - The 10-K says nothing on minimum purchases, dollar obligations or alternative platforms. Its Commitments note (R18) covers only litigation, and R17 covers only leases ($237.7M).
   - Source: [Guardant FY25 10-K](https://www.sec.gov/Archives/edgar/data/1576280/000157628026000013/gh-20251231.htm).
   - This refines E110, which gave the January 2033 date only.
4. **Guardant's 2023 settlement included "a new long-term purchase and supply commitment"** (FACT).
   - Terms are undisclosed (duration, amount, minimums), and one search summary called it a "three-year" commitment. That is unverified.
   - Sources: MedTech Dive and BioSpace, Aug 2023. A web search summary attributes the three-year purchase commitment to the 10-K, but I could not verify that in the 10-K text.
5. **Exact Sciences buys from Illumina on a purchase-order basis, with no long-term supply agreement** (FACT, from older 10-Ks).
   - The 10-Ks say OncoExTra is validated only on Illumina. Exact is also tied to Ultima: a "long-term supply agreement" announced 21 Jun 2022, with Exact as an investor. It has been in Ultima's UG 100 early-access program.
   - No prices or percentages were disclosed. Sources: [Exact 10-K FY2023](https://www.sec.gov/Archives/edgar/data/1124140/000112414024000012/exas-20231231.htm) and [BioSpace, 21 Jun 2022](https://www.biospace.com/ultima-genomics-and-exact-sciences-enter-long-term-supply-agreement-aimed-at-improving-patient-access-to-genomic-testing-by-driving-down-sequencing-costs).
   - I read the text through search summaries, not the FY25 10-K itself, so it may be stale. Exact's FY25 and Q2'26 status is unchecked.
   - Relevance: a cancer-testing customer has a contractual alternative sequencer and no Illumina volume commitment.

## GRAIL details (FACT unless noted)

- **Royalty, from the FY25 10-K and Q2'26 10-Q:** 9% in perpetuity on oncology net sales, with anti-stacking down to a 7% floor. GRAIL expects 7% "in the foreseeable future." It drops to 5% after cumulative payments of $1B. Payments are suspended until 24 Dec 2026 or an earlier change of control, "without retroactive effect." Payments that would have been made during the suspension count toward the $1B.
  - The 24 Dec 2026 date matches the brief. The 7% expected rate, the $1B/5% step-down and the "without retroactive effect" wording are details I did not find in the ledger.
  - Sources: [GRAIL Q2'26 10-Q](https://www.sec.gov/Archives/edgar/data/0001699031/000162828026054307/gral-20260630.htm), plus the FY25 10-K via search excerpt.
- **Term, per a search excerpt of the FY25 10-K:** 10 years with two-year automatic renewals, capped at 20 years in total. Illumina is the sole supplier of sequencers and certain reagents. This is consistent with E257 (28 Feb 2027 expiry, 120-day notice).
- **Illumina related-party status:** Illumina cut its stake to under 10% in Q4 2025, so it is no longer a related party (Q2'26 10-Q). Spend with Illumina may therefore no longer be broken out as related-party amounts.
- **Q2'26 10-Q:** no non-renewal notice appears in the parts retrieved, which were partial. Cost of screening was $23.3M for the quarter and $44.6M for the six months. The Commitments note (R15) contained only litigation, so no commitments table sits there. The commitments data for Q2'26 was not found.
- **GRAIL cash:** cash burn was $299M in 2025, with no Illumina funding in 2025 (R9, a cash flow statement).

## Contradictions and stale data

- No contradiction with the brief's known facts.
- E257 (a search paraphrase) is only partly confirmed. I found the 28 Feb 2027 and 120-day language only in secondhand summaries, not in text I read. The 10-K body was truncated in the fetch.
- The "three-year" Guardant purchase commitment is unverified. The MedTech Dive article describes the overall collaboration as three years and does not give the commitment's term.

## Gaps / what I could not find

- I did not read the GRAIL 10-K body (MD&A, supplier-concentration note, risk factors), because the fetch returned only the business section. I also could not get the GRAIL income statement; R4 returned the balance sheet. A shell with `curl` and `grep` would settle this.
- I did not reach the other customers' purchase-obligation and supplier-concentration notes, or their 2025 and Q2'26 10-Qs. Targets: Tempus, GeneDx, Caris, BillionToOne, Myriad, and Exact (FY25).
- I did not read any EX-10 reagent supply agreement with redacted prices. The search surfaced the Caris EX-10.2(A) and Natera EX-10.1, and both are already in the ledger.
- I found no disclosed sequencing cost per sample, no statement of switching to Element, Ultima or Roche AXELIOS, and no quantified NovaSeq 6000-to-X saving in any filing text I reached.
- Gross-margin attributions to sequencing cost per Gb were not collected.
