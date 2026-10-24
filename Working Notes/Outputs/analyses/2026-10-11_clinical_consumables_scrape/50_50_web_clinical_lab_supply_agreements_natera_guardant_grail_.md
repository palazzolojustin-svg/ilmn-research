# Agent 50: 50-web-clinical-lab-supply-agreements-Natera-Guardant-GRAIL-Caris-Tempus-GeneDx-raw-text

*Model: sonnet. Run 2026-10-11 03:20:11. Cost $1.84 (API-equivalent).*

**Assignment:** Close gaps 3 and 4 by DOWNLOADING raw filing text to disk (Bash/PowerShell with an EDGAR-compliant User-Agent; save to C:\Users\palaz\OneDrive\Documents\ILMN Claude Code Local Folder\_Build\sandbox\agent50\, then grep) instead of relying on WebFetch summaries. Questions to answer with exact quoted text and quantification. (a) Natera (CIK 1604821): FY25 10-K and exhibit index. Find the Illumina supply agreement and every amendment through the Eleventh. Quote the term end (Aug 2033?), the 'material suppliers' risk factor, the pricing mechanism ('Volume-Based Net Price' and its replacement), whether any most-favoured-customer clause, minimum purchase or take-or-pay survived, and any redacted-exhibit price schedule. Find whether the Open Offer's 43% cost-per-Gb commitment was measured or met and what happens after the Aug 2027 signing window. Natera's COGS per test and R&D commentary on sequencing cost per test in its Q2'26 10-Q. (b) Guardant (CIK 1576280): the exhibit list after Amendment #5 for FY24 and FY25 10-Ks; purchase obligations to Illumina; supplier concentration text. (c) GRAIL (CIK 1609255): the GRAIL-Illumina supply agreement term (check whether the initial term runs to 28 Feb 2027 with a 2-year auto-renewal), take-or-pay and price provisions, and the FY25 10-K and Q2'26 10-Q supplier-risk text. (d) Caris Life Sciences 10-K Note 8 (acc. 0002019410-26-000016) for the 90-day and no-minimum terms; Tempus 10-K/10-Q text naming Illumina and the $15.9M payable and the vendor 33/39/33% concentration; GeneDx's unnamed 20/13/11% supplier; Exact Sciences, BillionToOne, Adaptive, Veracyte, Myriad and NeoGenomics supplier-concentration and purchase-commitment text (state 'not named' if so). Output a table per company: contract term, minimum commitments ($), price-protection or MFN, concentration %, exact quote, URL, accession. Flag any clause that limits or enables switching to Roche, Ultima or Element, and any cost-per-test statement implying a $/Gb decline.

## Key findings

I could not download filings to disk. Bash and PowerShell are both disabled in this session, and I only had WebFetch and WebSearch. Every item below comes from a WebFetch or search summary. No raw text was saved or grepped. Items marked "(search paraphrase)" are search-engine paraphrases of 10-K text, not direct reads. WebFetch also truncates large filings, so several "not found" results are weak negatives.

1. **FACT: The Open Offer's 43% commitment is a price ceiling by 2025, not a revenue floor.** Caris's supply agreement (Ex. 10.2(A), S-1) quotes it as follows: "By 2025, Illumina commits that…the Volume-Based Net Price…per gigabase of sequencing using the highest throughput Illumina instrument then available…will be at least 43% lower than the inflation-adjusted…Volume-Based Net Price…per gigabase of sequencing using the NovaSeq instrument, with an S4 300 flow cell, at full capacity." The baseline was about $4/Gb at the top volume tier (March 2021). The target is therefore ≤ about $2.26/Gb inflation-adjusted. [Caris S-1 Ex. 10.2(A), 2025, https://www.sec.gov/Archives/edgar/data/2019410/000110465925052381/tm2415719d15_ex10-2a.htm]
   - The fetch summary found no stated remedy if the commitment is missed.
   - The 25B list price of $2.00/Gb (E054, E055) is already below the ceiling, so it is probably met on list price. I found no document that actually measures it.
   - The $4 and $2.26 figures come from a single fetch summary and need checking against the raw exhibit.
   - This quantifies E192 and E212: the clause only caps price, so it does not protect Illumina's revenue per Gb.
2. **FACT: The same-or-better pricing clause comes with a refund mechanism.** The Caris text says: "Illumina will refund to Customer the difference between the pricing made available to Customer and the triggering pricing, multiplied by the number of affected units." The comparison is to an "Equivalent customer" (and, per the earlier GRAIL/Natera Eighth Amendment, to GRAIL). This adds the refund mechanics to E192. [same Ex. 10.2(A)]
3. **FACT: Customer-side exit rights are strong in the Caris version of the Open Offer.**
   - Caris "has a unilateral right to terminate its supply relationship with Illumina at any time and for any reason without termination liability upon ninety (90) days' prior written notice."
   - The agreement is "not contingent on any purchase commitments by Customer."
   - It is non-exclusive. The excerpts show no restriction on using competing suppliers.
   - Illumina "cannot terminate…for convenience" and "shall not discontinue any Supplied Product so long as Customer continues to purchase" it. [same exhibit]
   - **Switching:** nothing in the Open Offer text limits adding Roche, Ultima or Element sequencers. The only cost of leaving is losing the Illumina discount tiers.
4. **FACT: Caris's 10-K confirms the same terms (search paraphrase).** The Illumina agreement "does not contain any minimum purchase requirements but provides for volume discounts." It is "irrevocable by Illumina until its expiration in August 2033." Caris names Illumina as sole supplier of NGS instruments and reagent kits. This closes the Caris half of gap 4. [Caris 10-K FY25, acc. 0002019410-26-000016, https://www.sec.gov/Archives/edgar/data/2019410/000201941026000016/cai-20251231.htm]
5. **FACT: The Tempus Illumina attribution and $15.9M payable are now supported (search paraphrase).** This corrects the ledger's note on E213, which said R14 did not name Illumina.
   - Purchases from Illumina were "approximately 33%, 39% and 33% of total vendor payments" for 2025, 2024 and 2023.
   - Tempus "relies on Illumina as the sole supplier of the sequencers and as the sole provider of maintenance and repair services."
   - Amounts due to Illumina were "approximately $15.9 million at December 31, 2025."
   - The note R14 that the earlier wave read may be a different note. I did not read the 10-K text directly. [Tempus 10-K FY25, acc. 0001193125-26-066961, https://www.sec.gov/Archives/edgar/data/1717115/000119312526066961/tem-20251231.htm]
6. **FACT: GRAIL's supply agreement term is supported (search paraphrase of the FY25 10-K).** "The initial term of the Illumina Supply Agreement is scheduled to expire on February 28, 2027. The Illumina Supply Agreement will automatically renew for two year terms unless we or Illumina provide written notice of non-renewal at least 120 days prior to the end of the then-current term." That puts the first non-renewal deadline around late October 2026. Illumina is GRAIL's sole supplier of sequencers and certain reagents and of servicing, and GRAIL pays a "high single-digit royalty…in perpetuity." The fetch of the 10-K body did not return the term passage (so no take-or-pay or price text). [GRAIL 10-K FY25, acc. 0001628280-26-017319, https://www.sec.gov/Archives/edgar/data/1699031/000162828026017319/gral-20251231.htm]
7. **FACT (new): Natera's supply agreement has a binding rolling forecast.**
   - Natera's Q2'26 10-Q (filed Aug 2026) has an Exhibit 10.1 that is the 18 Sep 2014 First Amendment to the "Supply Agreement (TG Consumables)" between Illumina and Natera.
   - The exhibit says: "The 4th calendar month of each Forecast provided under this Agreement is a binding commitment by Customer to take receipt of and pay for that quantity", with a permitted variance of +/-25%.
   - This is not a dollar minimum, but it is a short-horizon take-or-pay. It qualifies the ledger's "no explicit minimum-purchase quantity" (E212).
   - The same exhibit has a redacted "shelf life", a redacted discontinuation-notice period and redacted payment terms.
   - I did not establish why it was refiled in Q2'26. [Natera 10-Q Q2'26, acc. 0001628280-26-054525, https://www.sec.gov/Archives/edgar/data/0001604821/000162828026054525/ntra-20260630xex101.htm]
8. **FACT: The Eleventh Amendment text has no most-favoured-customer language (single fetch).** A keyword search found no "GRAIL", "no less favorable", "terminate" or "2033". "Volume-Based Net Price" "is hereby deleted in its entirety" and replaced by "Net Price" (§2).
   - "Minimum Prior Year Spend" and "Minimum required quantity of [*]" appear only in pricing tables, as redacted tier thresholds.
   - The refund language found is the tariff-charge refund in §7(g): "If after such incremental Tariff Charges are collected Illumina later receives a rebate, refund or any other form of renumeration…". It is not a price refund.
   - This supports the ledger's "MFN possibly superseded" (E192), but the fetch could have been truncated. [Natera 10-Q Q1'26 Ex. 10.1, https://www.sec.gov/Archives/edgar/data/0001604821/000162828026032478/ntra-20260331xex101.htm]
   - The original supply agreement is dated 16 Aug 2013. Natera's August 2033 term would be 20 years from that date, but I could not confirm it.
9. **FACT: GeneDx names Illumina among its limited suppliers (search paraphrase).** GeneDx relies on a limited number of suppliers including Illumina, Life Technologies, Twist, Path-Tec and Agilent. "One supplier accounted for approximately 20%, 13%, and 11% of purchases" in 2025, 2024 and 2023, and that supplier is not named. So Illumina's 20% share is an inference only. [GeneDx 10-K FY25, https://www.sec.gov/Archives/edgar/data/1818331/000181833126000015/wgs-20251231.htm]
10. **FACT: Guardant's last amendment in the search results is Amendment #5.** It is dated 1 Jan 2021 and was filed as Ex. 10.19 to the 2021 10-K. Search results show no later amendment, so the termination-for-convenience and January 2033 terms in E110 may rest on that amendment or on the 10-K text. I could not retrieve the FY24 or FY25 exhibit indexes (Justia returned 403). [Guardant 10-K FY25, https://www.sec.gov/Archives/edgar/data/1576280/000157628026000013/gh-20251231.htm]

## Per-company table

| Company | Contract term | Minimum commitment | Price protection / MFN | Concentration | Source and accession |
|---|---|---|---|---|---|
| Natera | Aug 2033 (search paraphrase of the FY25 10-K; the exhibit text has no "2033") | No $ minimum seen; binding 4th-month forecast, ±25% (2014 First Amendment) | Eighth Amendment MFN; Eleventh Amendment replaced the price definition and shows no MFN text; inflation-adjusted price "shall not increase further" (§7(k)) | Sole supplier for Panorama, Horizon, Signatera, Prospera; tests "only validated" on Illumina | 10-K 0001104659-26-020881; 10-Q 0001628280-26-054525 |
| Caris | 12 years from the GRAIL close (Aug 2021), to Aug 2033; Illumina can't terminate | None; Caris may exit on 90 days' notice | MFN with refund; no price increases except uncontrollable cost; 43% by 2025 | Sole NGS supplier | S-1 Ex. 10.2(A) 0001104659-25-052381; 10-K 0002019410-26-000016 |
| GRAIL | Initial term to 28 Feb 2027; 2-year auto-renewals; 120-day notice (search paraphrase) | Not found | Not found; royalty is "high single-digit" in perpetuity | Sole supplier of sequencers and certain reagents | 10-K 0001628280-26-017319 |
| Tempus | Not found | Not found ($15.9M payable at 31 Dec 2025) | Not found | 33% / 39% / 33% of vendor payments (2025/24/23); sole sequencer and maintenance supplier | 10-K 0001193125-26-066961 |
| GeneDx | Not found | Not found | Not found | Unnamed supplier 20% / 13% / 11% (2025/24/23); Illumina listed among limited suppliers | 10-K 0001818331-26-000015 |
| Guardant | To about Jan 2033 (E110); last amendment found is #5 (1 Jan 2021) | Not found | Not found | "Limited number of vendors" (E110 correction) | 10-K 0001576280-26-000013 |

## Other customers (search paraphrase only)
- **Adaptive:** names Illumina as a key supplier (NextSeq and NovaSeq X Plus systems and reagents). No percentage found.
- **Veracyte:** the results did not identify Illumina as its core sequencing supplier. It has a multi-year Illumina agreement for decentralized IVD kits.
- **Personalis:** says it depends on Illumina as sole supplier of sequencers, reagents and maintenance.
- **Exact Sciences:** OncoExTra is "only validated" on Illumina, and the 2025 MRD and MCED tests will use it. This is from trade press, not the 10-K.
- **Myriad, NeoGenomics, BillionToOne:** no 10-K text retrieved. Treat these as not named or unchecked.

## Cost-per-test statements
- Natera's Q2'26 10-Q cites a gross margin of 64.5% vs 63.4%. It attributes this to "continued progress in reducing cost of revenues associated with tests processed". Cost of product revenue was 35.5% vs 36.8% of product revenue for the first half, from a mix shift where "certain higher volume products have a lower cost per test". Illumina is not named and no $/Gb statement appears. (Search summary; the direct fetch of that 10-Q found no Illumina mention.)

## Contradictions and stale data
- E213 correction: the claim that the Tempus 10-K does not name Illumina is contradicted by the search extract in finding 5. This needs a direct read of the 10-K narrative.
- E212 ("no explicit minimum-purchase quantity"): the 2014 binding-forecast clause shows there is a short-horizon commitment. It is not a minimum dollar volume.
- The ledger says the Open Offer signing window closes Aug 2027. The Open Offer page I fetched says it became available 30 Mar 2021 and gives no explicit expiry. A 12-year term from the March 2021 offer would also not run to Aug 2033, so the "Aug 2033 = 12-year clock" link in the gaps file may be wrong. Caris's term runs from the GRAIL closing (Aug 2021).

## Gaps / what I could not find
- No raw-text download or grep was possible. The FY25 10-K narratives for Natera, Guardant and GRAIL (risk factors, exhibit indexes) remain unread directly.
- The Open Offer addendum PDFs (Section 4(g) disclosures) returned 404. I found no document showing the 43% was measured or met, and nothing on what happens after the signing window.
- The Natera 10-K "material suppliers" wording and the Natera Q2'26 R&D commentary on sequencing cost per test were not found.
- Guardant's purchase obligations to Illumina and its exhibit index after Amendment #5 were not retrieved.
- GRAIL take-or-pay and price terms, and the Q2'26 10-Q supplier text, were not retrieved.
- BillionToOne, Myriad, NeoGenomics, Veracyte and Exact Sciences 10-K concentration text was not retrieved.

Sources:
- [Caris S-1 Ex. 10.2(A)](https://www.sec.gov/Archives/edgar/data/2019410/000110465925052381/tm2415719d15_ex10-2a.htm)
- [Caris 10-K FY25](https://www.sec.gov/Archives/edgar/data/2019410/000201941026000016/cai-20251231.htm)
- [Natera 10-Q Q2'26 Ex. 10.1](https://www.sec.gov/Archives/edgar/data/0001604821/000162828026054525/ntra-20260630xex101.htm)
- [Natera 10-Q Q1'26 Ex. 10.1](https://www.sec.gov/Archives/edgar/data/0001604821/000162828026032478/ntra-20260331xex101.htm)
- [Tempus 10-K FY25](https://www.sec.gov/Archives/edgar/data/1717115/000119312526066961/tem-20251231.htm)
- [GRAIL 10-K FY25](https://www.sec.gov/Archives/edgar/data/1699031/000162828026017319/gral-20251231.htm)
- [GeneDx 10-K FY25](https://www.sec.gov/Archives/edgar/data/1818331/000181833126000015/wgs-20251231.htm)
- [Guardant 10-K FY25](https://www.sec.gov/Archives/edgar/data/1576280/000157628026000013/gh-20251231.htm)
- [Illumina Open Offer terms page](https://www.tst-web.illumina.com/areas-of-interest/cancer/test-terms.html)
