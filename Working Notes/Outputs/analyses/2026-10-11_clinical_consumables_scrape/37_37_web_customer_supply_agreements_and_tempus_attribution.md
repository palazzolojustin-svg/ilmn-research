# Agent 37: 37-web-customer-supply-agreements-and-Tempus-attribution

*Model: sonnet. Run 2026-10-11 02:55:40. Cost $1.44 (API-equivalent).*

**Assignment:** Close the customer-contract gaps (open gaps 2 and 3) by reading raw EDGAR text. Do NOT rely on WebFetch of full 10-Ks, because it truncates. Instead use the EDGAR filing index pages (https://www.sec.gov/Archives/edgar/data/<CIK>/<accession-no-dashes>/), the XBRL R-pages (R2.htm, R4.htm and so on), the exhibit files, and EDGAR full-text search (efts.sec.gov/LATEST/search-index?q=...). (1) Natera 10-K FY25, accession 0001104659-26-020881: find the narrative purchase-obligation or commitments note. Quantify minimum purchase commitments to Illumina by year, and whether Illumina is named. Also pull the Illumina supply agreement exhibits (search 'Natera Illumina Supply Agreement' exhibit 10.x, amendments through the Eleventh). Look for §7(l) price or $/Gb floor, any MFN clause (did the Eighth Amendment MFN survive the Eleventh?), the §7(g) tariff pass-through and whether it is retroactive, volume tiers, rebates, and the term (August 2033). (2) Guardant: the Illumina supply agreement exhibits (to January 2033, 90-day termination for convenience), any MFN, tariff or minimum-purchase terms, and redacted pricing mechanics. (3) Tempus 10-K FY25 (accession 0001193125-26-066961, tem-20251231.htm): read the risk-factor and purchase-commitment text to settle whether 'Purchases from Illumina accounted for approximately 33%, 39% and 33%' and 'sole supplier of the sequencers' are real quotes, and what the $15.9M due at 31 Dec 2025 is. (4) If time remains: Caris Note 8 purchase commitments, GeneDx's single-supplier percentages, and Exact, BillionToOne, Veracyte and Adaptive supplier-concentration text. Quantify the contractual price floors, minimum commitments, term dates and the dollar spend implied with Illumina, and flag any exhibit with new amendment dates in 2025-2026 (a sign of repricing). Cite accession numbers and exhibit numbers. Label verified quotes against unverified snippets.

## Key findings

1. **The §7(g) tariff pass-through in the Eleventh Amendment is non-retroactive. This resolves the conflict in E194 (ledger "retroactive" vs F25).**
   - FACT: Illumina invoices Natera only if the tariff rate exceeds a redacted [*]%. Pass-through starts "thirty days after Illumina begins paying such Tariff Charges at the rate over [*]%… on a non-retroactive basis."
   - The tariff is defined as the Section 122 duty under Presidential Proclamation 11012 (91 Fed. Reg. 9339, 25 Feb 2026), plus any successor Section 301/232 duties. The rate at 2 Mar 2026 was 10%.
   - Natera gets email notice and a pro-rata share of any later rebate or refund.
   - Natera 10-Q Q1'26, accession 0001628280-26-032478, Ex. 10.1. The ledger's "retroactive" reading is probably a confusion with Part E (point 5), which is retroactive.
   - This is a WebFetch reading of the exhibit, not a full read. The percentage threshold is redacted.

2. **I found no most-favored-customer (MFN) language in the Eleventh Amendment.** This does not show the Eighth Amendment MFN survived or died, because I did not read the Eighth Amendment.
   - FACT: a keyword search of the Eleventh Amendment text for "most favored", "MFN" and "lowest price" returned nothing. The same search found no "most favored" or pricing-parity language in the provisions it amends or restates.
   - The amendment restates §1 "Certain Sequencing Consumables", §7(a) pricing, §7(f) project discounts, §7(k) "No Price Increases" and §7(l) "New Product Pricing". It deletes and replaces the "Volume-Based Net Price" definition.
   - OPINION: the MFN may sit in an earlier amendment and survive as an unamended clause, or it may have been dropped earlier. Check the Eighth Amendment (Dec 2023 / Mar 2024) text, which is filed with Natera's FY23/FY24 10-K (e.g. ntra-20231231xex10d28.htm).

3. **§7(l) is a no-increase price-per-Gb rule on new product versions, not an absolute floor.**
   - FACT, quoted: "The inflation-adjusted (based on the PPI) price per gigabase of sequencing (after any applicable discounts) for such new version shall not be higher as compared to the Net Price of the prior version" [*].
   - FACT: Illumina's cost-of-goods-sold increase allowance is limited: "to the extent Illumina's costs of goods sold… materially increase due to factors beyond Illumina's control, then the Net Price… may increase solely to reflect that cost increase and solely for the duration of that cost increase."
   - Read-through (OPINION): this caps Natera's $/Gb at the prior-version level in real terms, so a new flow cell cannot raise Natera's price per Gb. It does not stop Illumina cutting price. It also means the contract has no price floor that protects Illumina's revenue.
   - Open gap 1 asked whether §7(l) is a "contractual $/Gb floor". It is a ceiling on price, not a floor.

4. **Natera has no stated minimum dollar purchase commitment to Illumina. Quarterly minimums exist but are redacted.**
   - FACT: Natera 10-K FY25, R16 (Commitments and Contingencies), accession 0001104659-26-020881. This note does not name Illumina. Totals as of 31 Dec 2025:

   | Category | Total | By year |
   |---|---|---|
   | Laboratory instruments supplier | $18.9M | 2026 $9.2M; 2027 $9.7M |
   | Material suppliers | $107.3M | 2026 $89.3M; 2027 $7.3M; 2028 $8.2M; 2029 $2.6M |
   | Application service providers | $13.6M | n/a |
   | Cloud platform provider | $28.0M | n/a |
   | Other | $89.1M | n/a |
   | **All commitments** | **$256.9M** | mostly 2026-2029 |

   - Materials commitments of $107M against FY25 product cost of revenue of about $811M (R20) mean the long-dated Illumina volume is not locked in as a contractual minimum. The "material suppliers" line may include Illumina, but the note does not say so.
   - FACT: the Eleventh Amendment keeps a quarterly minimum, with the amount redacted. Natera must take delivery each quarter of consumables "that total at least [*] after any discounts". Minimums are waived pro-rata during a Supply Failure. This text is from the web-search summary of the exhibit, not from my own reading of it.
   - The Eleventh Amendment itself has no absolute minimum. Volume discounts depend on "Prior Year Spend" thresholds (Part A, Table A.1): "If Customer has not met the applicable minimum Prior Year Spend… discount for Other Consumables will be [*]."
   - This corrects the open-gaps instruction. The "$11.6M" figure is confirmed as not Natera's; Natera's lines are the ones above.

5. **Part E of the Eleventh Amendment is a custom price schedule for WGS-based MRD (whole-genome sequencing minimal residual disease) tests.** It is retroactive and tiered.
   - FACT: "notwithstanding any price increases to the Current WGS Products, effective retroactively as of [*] Customer will be eligible to claim [*] for WGS-Based MRD Tests… in accordance with the pricing/discount tiers set forth in Table E.1." Table E.1 has a "Per Gb Price for Current WGS Product after [*] (USD)".
   - Price per Gb is volume-tiered against WGS-MRD test counts. This is direct evidence for Q2 that Natera's high-Gb WGS-MRD volume gets a negotiated, falling $/Gb schedule. The values are redacted.
   - The amendment is effective 2 Mar 2026. Its recital: "memorialize price schedules for certain Products and services and address supply, forecasting, and other terms… and to correct certain typographical errors contained in the Tenth Amendment."
   - Amendment history (search summary of the exhibit): 16 Aug 2013 original; 18 Sep 2014; 23 Sep 2015; 8 Jun 2016; 3 Jan 2019; 18 Dec 2019; 8 May 2020; 7 Oct 2021; 31 Dec 2023; 11 Mar 2024; 10 Jan 2025 (Tenth); 2 Mar 2026 (Eleventh).
   - OPINION: two repricing amendments in about 14 months (Jan 2025 and Mar 2026) show Natera's pricing is renegotiated roughly annually.

6. **The Natera term (August 2033) is not in the Eleventh Amendment text.** The ledger's E109 source for it is the 10-K narrative, which I could not retrieve. I did not re-verify it.

7. **Guardant: the only supply-agreement text I could read is Amendment #5 (signed 30 Dec 2020 / 1 Jan 2021).** The Aug 2023 settlement's "new long-term purchase and supply commitment" is not described anywhere I could reach.
   - FACT, Guardant 10-K FY20 Ex. 10.19, accession 0001576280-21-000031.
   - Term: 12 years from the Amendment #5 effective date, so to about Jan 2033. It then auto-renews for one-year periods unless either party gives at least 12 months' notice.
   - Termination: "Customer may terminate this Agreement for convenience and without termination liability at any time upon ninety (90) days' prior written notice… Illumina may not terminate this Agreement for convenience prior to the end of the Initial Term." Guardant must honour accepted purchase orders.
   - No minimum purchase obligation, no exclusivity and no tariff clause appear in that exhibit. Pricing is a discount off "then-current list price", with tiered discounts on cumulative purchases and installed instruments. The tables are redacted [***].
   - No MFN or price-protection language was found in Amendment #5.
   - The Aug 2023 settlement 8-K (accession 0001193125-23-200555, filed 1 Aug 2023) says only that the parties entered "a new long-term purchase and supply commitment". It gives no term, minimum or price.
   - Guardant FY24 and FY25 10-Ks both reference Illumina (accessions 0001576280-25-000044 and 0001576280-26-000013). I could not fetch the exhibit lists, so I found no 2025-26 amendment, and I do not know whether none exists.
   - OPINION: this matches the ledger (E110) and sharpens it. Guardant carries no contractual volume lock-in and has had a 90-day exit since 2021. The switching barriers are qualification cost and validation time, not contract terms.

8. **Caris: the Illumina agreement is an "open offer" supply agreement with no minimum purchase.** This is from a search-engine summary of the 10-K, not a verified quote.
   - UNVERIFIED snippet, Caris 10-K FY25, accession 0002019410-26-000016: entered November 2022 under Illumina's "open offer"; no minimum purchase requirements but "volume discounts and other promotions"; irrevocable by Illumina until August 2033; Caris may terminate at any time on 90 days' notice without liability.
   - Direct WebFetch of the 10-K returned nothing on Illumina because of truncation, so treat this as unverified until Note 8 is read.
   - OPINION: if confirmed, Caris, Natera and Guardant all lack hard minimum commitments. That strengthens the "contracts can become null and void" claim in E113.

9. **Tempus: I could not settle the Illumina attribution; the 33/39/33% vendor-payment figures remain verified only without Illumina's name.**
   - FACT: R13 (business and segment note) has no Illumina mention and no $15.9M. The 10-K main document truncates before the risk factors (accession 0001193125-26-066961).
   - UNVERIFIED: three separate search-engine summaries repeated the same wording. They said Tempus relies on Illumina as a sole supplier for certain sequencers, reagents, blood tubes and equipment, that purchases from Illumina were about 33%, 39% and 33% of total vendor payments for 2025, 2024 and 2023, and that Illumina is the sole supplier of the sequencers and sole provider of their maintenance and repair. The summaries said the same text appears in the S-1 and 10-K filings. They are model paraphrases, not retrieved text.
   - I could not extract text from the FY25 annual-report PDF; the tools returned unreadable content.
   - The existing ledger correction on E213 therefore stands, with one change: three independent summaries now point to Illumina by name, which raises its likelihood. It is not proven.
   - The $15.9M due at 31 Dec 2025 stays unfound.

## Contradictions and stale data

- E194 vs F25 on §7(g): resolved. The pass-through is non-retroactive. Part E's WGS-MRD price claim is the retroactive one.
- E109 (Natera "supply agreement expiring August 2033"): the Eleventh Amendment text shows no term extension. The 2033 date presumably comes from the 10-K narrative, not from this exhibit.
- Natera's Q2'26 10-Q exhibits 10.1 and 10.3 are the 2014 Supply Agreement (TG Consumables, with a 3-year term) and the Third Amendment (June 2016, a 10-year term, so to about 2026). They were re-filed as exhibits. Their re-filing in Q2'26 may signal a restated or consolidated agreement (OPINION). The fetches did not confirm this and did not show a Twelfth Amendment.
- Natera's commitments figure needs correcting: $256.9M total, of which $107.3M is material suppliers (R16). The "$11.6M" is neither Natera nor Illumina.
- The ledger's "Illumina sole supplier through August 2033" for Natera and Caris uses the same date. The Guardant date is January 2033. Check these are not conflated.

## Gaps / what I could not find

- The Natera 10-K narrative text on Illumina and the August 2033 term. The 10-K HTML truncates and the ARS PDF is unreadable here.
- The Eighth Amendment MFN text. Pull Natera FY23 Ex. 10.28 (ntra-20231231xex10d28.htm) and the Tenth Amendment (ntra-20241231xex10d29.htm or xex10d210.htm).
- The Guardant 2023 Collaboration and Settlement Agreement terms, any Guardant amendment after Amendment #5, and Guardant's tariff and MFN text.
- The Tempus risk-factor text and the $15.9M. This needs a local HTML download; I had no shell or PDF reader.
- Caris Note 8, GeneDx, Exact, BillionToOne, Veracyte and Adaptive: not reached.
- No Gb/$ spend could be derived for any customer, because all pricing tables are redacted.

Sources:
- [Natera 10-Q Q1'26 Ex. 10.1, Eleventh Amendment](https://www.sec.gov/Archives/edgar/data/0001604821/000162828026032478/ntra-20260331xex101.htm)
- [Natera 10-K FY25, R16 commitments](https://www.sec.gov/Archives/edgar/data/1604821/000110465926020881/R16.htm)
- [Natera 10-K FY25, R20 segment note](https://www.sec.gov/Archives/edgar/data/1604821/000110465926020881/R20.htm)
- [Natera 10-Q Q2'26 Ex. 10.1](https://www.sec.gov/Archives/edgar/data/0001604821/000162828026054525/ntra-20260630xex101.htm)
- [Natera 10-Q Q2'26 Ex. 10.3](https://www.sec.gov/Archives/edgar/data/0001604821/000162828026054525/ntra-20260630xex103.htm)
- [Guardant Amendment #5, FY20 10-K Ex. 10.19](https://www.sec.gov/Archives/edgar/data/1576280/000157628021000031/exhibit1019-illuminaagreem.htm)
- [Guardant 8-K, 1 Aug 2023](https://www.sec.gov/Archives/edgar/data/1576280/000119312523200555/d542051d8k.htm)
- [Tempus 10-K FY25](https://www.sec.gov/Archives/edgar/data/1717115/000119312526066961/tem-20251231.htm)
- [Caris 10-K FY25](https://www.sec.gov/Archives/edgar/data/2019410/000201941026000016/cai-20251231.htm)
