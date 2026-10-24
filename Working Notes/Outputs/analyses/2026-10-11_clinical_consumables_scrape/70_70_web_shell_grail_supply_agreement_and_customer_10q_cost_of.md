# Agent 70: 70-web-shell-GRAIL-supply-agreement-and-customer-10Q-cost-of-revenue-per-test

*Model: sonnet. Run 2026-10-11 03:56:15. Cost $1.80 (API-equivalent).*

**Assignment:** Closes open gaps 4 and 7. Use a shell with curl and a declared SEC User-Agent (not the fetch tool), and grep the saved files. (1) GRAIL/Illumina supply agreement: find the original 2017 Illumina-GRAIL supply agreement in GRAIL Inc.'s (CIK for GRAIL, Inc., the original GRAIL registrant, Form 10 / S-1 exhibit lists, plus Illumina's own historical 10-K exhibits), and the 2024 Form 10 for the GRAIL spin-off (exhibit 10.x 'Supply and Commercialization Agreement' and any amendments). Extract: price per unit or per Gb, volume minimums or forecast obligations, price-adjustment mechanics (MFN, annual price cut, benchmark), term, the 120-day notice and the 31 Oct 2026 non-renewal deadline, exclusivity and any rights to use other platforms. Also check the GRAIL Q2'26 10-Q for the same, plus its purchase commitments and the sequencing cost per test in MD&A. (2) Customer primary text, FY25 10-K and Q2'26 10-Q, for Caris Life Sciences, Tempus AI, BillionToOne, Myriad, Exact Sciences, Natera, Guardant, GeneDx and Veracyte. For each, grep for 'Illumina', 'sole', 'single source', 'NovaSeq', 'purchase obligation', 'sequencing', 'cost of', 'reagent', and 'per test'. Extract: supplier-concentration wording, any second platform (Element, Ultima, Roche, MGI), purchase commitments in $ and the term, any statement that cost per sample or per Gb fell, and COGS per test or gross-margin drivers (such as 'lower sequencing costs from NovaSeq X'). Quote exact sentences with the filing URL and accession number. Quantify the implied customer cost-per-test deflation, and state which customers disclose X adoption percentages. Return a table by customer.

## Key findings

I found little that is new for the two gaps. The fetch tool was the only way to read filings. It truncates 10-K and 10-Q documents before the risk factors and MD&A. I had no shell, so the curl-and-grep route was not available. The GRAIL agreement is mostly redacted, and the customer MD&A cost-per-test text could not be read. What I did get:

- **GRAIL agreement, pricing (new, FACT).** The 2017 Amended and Restated Supply and Commercialization Agreement is GRAIL Form 10 Ex. 10.6. Section 3.1(a) sets price at "Illumina's then current List Price… subject to the discount table set forth in Exhibit A", and "List Prices may increase or decrease during the Term in Illumina's sole discretion". The discount percentages are redacted [***].
  - The ledger (E232, E249) shows Caris's Open Offer has a price-can-only-fall clause (§43% ceiling, MFN, refund). GRAIL's own contract has no such protection in the visible text. So the price-cut path is a feature of the Open Offer for third parties, not of the GRAIL supply contract.
  - Source: [GRAIL Form 10 Ex. 10.6](http://www.sec.gov/Archives/edgar/data/0001699031/000119312524132022/d556103dex106.htm), accession 0001193125-24-132022, filed 2024. The fetch returned a truncated copy.
- **GRAIL binding forecast (new, FACT).** §3.4(a) requires a monthly forecast. "The [***] of each Forecast is a binding commitment by GRAIL… to take receipt of and pay for". The binding horizon is redacted. This is the same rolling take-or-pay structure as Natera's 4th-month clause (E258). It is not a dollar minimum. Same source.
- **GRAIL exclusivity (new, FACT).** §6.1–6.2 restrict Illumina, which cannot invest in a rival Screening testing company during the "Exclusivity Period". Extension of that period is conditioned on GRAIL meeting purchase thresholds and "exclusively using Illumina sequencing instruments". The period length and thresholds are redacted. So Illumina's investment exclusivity is tied to GRAIL's sequencer exclusivity. I did not find an outright bar on GRAIL buying other sequencers. This is a partial reading of a truncated file; treat it as unconfirmed. I read nothing on term (§13) or termination.
- **Term and 120-day notice (E257, unchanged).** A search snippet of the FY25 10-K repeats it. Initial term to 28 Feb 2027, then two-year auto-renewals unless either side gives written notice at least 120 days before term end. It also says Illumina's rights are non-exclusive. I could not confirm the text in the filing body. The ex-ledger date arithmetic stands: 120 days before 28 Feb 2027 is about 31 Oct 2026. The Fourth Amendment (Ex. 10.4 to Illumina's 8-K of 21 Jun 2024, accession 0001193125-24-167025) does not touch term, renewal, pricing or exclusivity. It only changes royalties and adds the Interim Period, which suspends §4.1–4.4, 4.5(b) and 4.7.
- **GRAIL MD&A and commitments (no new data).** The Q2'26 10-Q text I could read had nothing on sequencing cost per test, NovaSeq X or a purchase-commitments table. E178 (~$382 screening cost per test) and E279/E286 (no take-or-pay) stand.
- **Natera cost per test (new, quantifies E089, calc).** Cost of product revenues was $266.6M in Q2'26 vs $199.5M in Q2'25. Tests were 1,043,900 vs 853,100. That gives about $255 vs $234 per test, up about 9%. Revenue per test rose faster, about $721 vs $641, up about 12.5%. The 10-Q says gross margin rose on "continued progress in reducing cost of revenues associated with tests processed". Natera is not showing per-test cost deflation. Mix toward oncology and MRD offsets any sequencing saving. Cost of product revenues is not purely sequencing, and the ratio blends all test types.
  - Sources: [Natera Q2'26 10-Q](https://www.sec.gov/Archives/edgar/data/0001604821/000162828026054525/ntra-20260630.htm), accession 0001628280-26-054525, for cost of product revenues. Tests and gross margin are from the Natera Q2'26 release (6 Aug 2026), as returned by search.
- **Caris gross margin (new, FACT).** Gross margin was 66% for FY25 ($539.2M gross profit) vs 43% in FY24 ($178.8M). It was 75% in Q4'25 vs 54% a year earlier. Q2'26 revenue was $263.7M with a 68% gross margin, about 500 bp better y/y, and ~59,200 cases (+18%).
  - Calc: Q2'26 cost of services is about $84M, roughly $1,425 per case. Q2'25 was about $67M on about 50,200 cases, roughly $1,340 per case. So per-case cost was flat to slightly up, and the margin gain came from revenue per case. That fits E092 ("deeper, not cheaper").
  - The 10-K does say Illumina is the sole supplier of NGS instruments and kits, and the sole maintenance and repair provider. That is search-snippet text.
  - Source: [Caris FY25 10-K](https://www.sec.gov/Archives/edgar/data/2019410/000201941026000016/cai-20251231.htm), accession 0002019410-26-000016, via search snippet. The Q2'26 10-Q is accession 0002019410-26-000055. I did not read its MD&A.
- **BillionToOne cost per test (new, FACT).** FY25 revenue was $305.1M (+100%) on 51% more tests, with overall ASP +35%. Gross margin was 68% vs 53%, and the 10-K says "reductions in Overall Cost-Per-Test" drove part of that. This is the only customer here with a stated per-test cost decline. COGS per test fell by "more than 10%" even as the oncology mix rose (this phrase came from a search summary, likely the earnings call).
  - H1'26 10-Q: cost of revenue +$17.5M (+40%), with $10.6M from testing samples and supplies on higher volume and $6.9M from labor. The filing says overall cost per test "stayed relatively stable" as oncology mix rose, "offset by programs to actively reduce variable expenses". Sequencing is not named as a driver.
  - Supplier wording: it relies on "sole- or single-source suppliers" for "certain sequencers, reagents, blood tubes". It does not name Illumina in the text I saw. It says replacing a supplier "could take approximately one to nine months" and that it keeps at least three months of inventory.
  - Sources: [BLLN FY25 10-K](https://www.sec.gov/Archives/edgar/data/2070849/000207084926000017/blln-20251231.htm), accession 0002070849-26-000017; [BLLN Q2'26 10-Q](https://www.sec.gov/Archives/edgar/data/0002070849/000207084926000050/blln-20260630.htm), accession 0002070849-26-000050. Both are known only through search snippets.
- **Myriad and Veracyte (new, FACT).** Myriad's FY25 10-K says it depends on "a limited number of third parties — in some cases single-source suppliers" for equipment and reagents. It does not name Illumina in what I saw. Veracyte relies on "sole suppliers for some of the reagents, equipment, and other materials" and has a multi-year IVD agreement with Illumina on the NextSeq 550Dx (not the NovaSeq). Neither is a stated Illumina sole-source claim. Myriad: accession 0000899923-26-000018. Veracyte: accession 0001384101-26-000010.

## Table by customer (new items only)

| Customer | Supplier wording (new) | Second platform | Purchase commitments | Cost-per-test evidence | X adoption % disclosed |
|---|---|---|---|---|---|
| GRAIL | Contract: list price less discount table, Illumina may change list "in sole discretion"; binding forecast (period redacted) | None found; exclusivity extension tied to Illumina-only use | None on consumables (E279) | ~$382/test screening cost (E178) | No |
| Caris | Illumina sole supplier of instruments, kits and maintenance (snippet) | None found | Not read | GM 66% FY25 vs 43%; per-case cost ~flat (calc) | No |
| BillionToOne | "Sole- or single-source" sequencers/reagents; Illumina not named; 1–9 month switch | None found | Not read | COGS/test −10%+ FY25; "relatively stable" H1'26 | No |
| Natera | (E109, E227 already) | None | (E227) | Cost/test up ~9% y/y (calc) | No |
| Myriad / Veracyte | Single-source wording only; Illumina not named | Veracyte: NextSeq 550Dx IVD | Not read | None | No |
| Tempus, Guardant, GeneDx, Exact | Not re-checked beyond the ledger | | | | No |

No customer I checked discloses an X adoption percentage.

## Contradictions and stale data

- E257's 28 Feb 2027 and 120-day terms still rest on a search snippet. The FY25 10-K body fetch (summary only) gave no term text.
- The GRAIL FY25 10-K says the royalty is "in perpetuity". The Fourth Amendment suspends it to 24 Dec 2026 (already in the ledger's correction).
- My own first summary of Ex. 10.6 claimed §13.1 existed and was redacted. A second fetch showed the text was truncated at §9.1(c), so I treat §13 content as unread.

## Gaps / what I could not find

- GRAIL Ex. 10.6 §13 (term and termination), Exhibit A discount table and §3.4 binding horizon. Plain curl would return the full file.
- MD&A cost-of-revenue text for Caris, Tempus, Exact, Veracyte and Myriad. Also the 10-K and 10-Q commitments notes for Caris and BillionToOne, and the Guardant and Tempus MD&A.
- Exact Sciences (Abbott deal status) was not checked this wave.
- GRAIL's Q3'26 10-Q or 8-K around 5 Nov 2026 would show whether either side served non-renewal notice.

Sources:
- [GRAIL Form 10 Ex. 10.6](http://www.sec.gov/Archives/edgar/data/0001699031/000119312524132022/d556103dex106.htm)
- [Illumina 8-K Ex. 10.4, Fourth Amendment](https://www.sec.gov/Archives/edgar/data/1110803/000119312524167025/d851030dex104.htm)
- [GRAIL Q2'26 10-Q](https://www.sec.gov/Archives/edgar/data/0001699031/000162828026054307/gral-20260630.htm)
- [GRAIL FY25 10-K](https://www.sec.gov/Archives/edgar/data/1699031/000162828026017319/gral-20251231.htm)
- [Natera Q2'26 10-Q](https://www.sec.gov/Archives/edgar/data/0001604821/000162828026054525/ntra-20260630.htm)
- [Caris FY25 10-K](https://www.sec.gov/Archives/edgar/data/2019410/000201941026000016/cai-20251231.htm)
- [Caris Q2'26 10-Q](https://www.sec.gov/Archives/edgar/data/0002019410/000201941026000055/cai-20260630.htm)
- [BillionToOne FY25 10-K](https://www.sec.gov/Archives/edgar/data/2070849/000207084926000017/blln-20251231.htm)
- [BillionToOne Q2'26 10-Q](https://www.sec.gov/Archives/edgar/data/0002070849/000207084926000050/blln-20260630.htm)
- [Myriad FY25 10-K](https://www.sec.gov/Archives/edgar/data/899923/000089992326000018/mygn-20251231.htm)
- [Veracyte FY25 10-K](https://www.sec.gov/Archives/edgar/data/1384101/000138410126000010/vcyt-20251231.htm)
