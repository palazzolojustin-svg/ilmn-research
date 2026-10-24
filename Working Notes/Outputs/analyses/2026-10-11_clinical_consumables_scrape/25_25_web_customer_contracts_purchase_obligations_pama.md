# Agent 25: 25-web-customer-contracts-purchase-obligations-PAMA

*Model: sonnet. Run 2026-10-11 02:37:52. Cost $0.81 (API-equivalent).*

**Assignment:** Open gaps 4, 10, 14 and 15. Work from primary SEC EDGAR and CMS documents. Do NOT repeat the 10-K supplier-language findings already in the ledger (E109, E110). (1) Natera: open the exhibits on EDGAR directly (Ex. 10.28, Ex. 10.2.10, Q1'26 Ex. 10.1 and any Illumina supply agreement amendments). Extract anything not redacted: the Eighth Amendment MFN clause that references GRAIL, the Eleventh Amendment price-protection clause, minimum purchase commitments, term, rebates and pricing mechanics. Confirm the purchase-obligation note in the FY25 10-K and Q2'26 10-Q, and the unverified '$11.6M' snippet. (2) Guardant: read the Illumina supply agreement exhibits (term to Jan 2033, 90-day termination for convenience) and the purchase-obligation note. (3) Run the same purchase-obligation and supplier-concentration check on the latest 10-K/10-Q for Tempus, Caris, GeneDx, Exact Sciences, BillionToOne, Adaptive, Veracyte, Myriad, NeoGenomics and Foundation (Roche). Record quoted dollar commitments, 'sole source' wording and any new mention of alternative sequencers (Ultima, Element, Roche SBX). Check the Caris Q2'26 10-Q for the 'Beyond Illumina' supplier language and for capacity and sequencer purchase commitments. (4) Build a top-10 Illumina clinical customer spend estimate (tests x Gb/test x $/Gb) with low/base/high error bars, using the disclosed COGS and test counts. Quantify implied share of Illumina's ~$1.9B clinical consumables. (5) PAMA/CMS: from the CMS CY2027 preliminary CLFS file and the CDLT July 2026 meeting materials, get per-code rates for 81415-81427, 81479, 0340U and the new genomic sequencing codes. Verify the '$597 vs $1,759.60-$4,375' snippet. Map the exposure to GeneDx, Natera, Guardant and Labcorp/Quest. Note the Nov 2026 final-rule timing. Cite document names, exhibit numbers and URLs.

## Key findings

1. **The "$597 vs $1,759.60–$4,375" snippet is a 2023 event, not CY2027 (corrects gap 14).** Xifin's Billing Beat (12 Dec 2023) says the recommended prices were "$1,759.60 and $4,375", and that CMS "bypassed the recommendation and the agency priced the codes at $597 each". It describes the September 2023 preliminary determinations (a CY2024-cycle event). The article says CMS later eased the concern (CMS "postponed its final pricing decision" and "eventually" issued revised determinations). Do not carry it forward as a CY2027 fact. FACT. [Xifin, 2023-12-12, https://www.xifin.com/billing-beat/cms-preliminary-pricing-for-genomic-procedures-raises-alarm-among-stakeholders/]
2. **Natera's Eleventh Amendment is public (Q1'26 10-Q Ex. 10.1, effective 2 Mar 2026). It has a price-protection clause but no MFN.** This contradicts E109's "unknown" status and updates gap 4. FACT. [Natera 10-Q Q1'26 filed 2026-05-08, Ex. 10.1, https://www.sec.gov/Archives/edgar/data/1604821/000162828026032478/ntra-20260331xex101.htm]
   - **§7(k), no price increases.** The inflation-adjusted Net Price "shall not increase further", with a carve-out if Illumina's COGS "materially increase due to factors beyond Illumina's control".
   - **§7(l), new products.** New product versions must maintain a comparable "inflation-adjusted… price per gigabase of sequencing". This is a contractual per-Gb price anchor, so a new flow cell cannot reset Natera's $/Gb upward.
   - **Discount tiers.** Other consumables get tiered discounts for 2026–2028 based on minimum prior-year spend. The tiers are "in alternative to each other and may not be combined".
   - **MRD pricing.** WES-based MRD gets conditional discounts off list for Current WES Products. WGS-based MRD is priced on a "per Gb Price", both tied to quarterly certification reports.
   - **Tariffs.** Illumina may pass through tariffs above a redacted threshold, with 30 days' notice and no retroactivity.
   - **Minimums and rebates.** No explicit minimum purchase quantity and no rebate language is visible. Pricing is keyed to spend tiers instead.
   - OPINION: Natera's effective $/Gb is contractually capped on the upside and spend-tiered, which supports E113's view that the largest accounts pay far less than list. The tier thresholds and the $/Gb figures are redacted.
3. **The Eighth Amendment MFN clause is confirmed verbatim (Ex. 10.2.8, FY23 10-K, amendment dated 31 Dec 2023).** Natera gets "Volume-Based Net Prices that are no less favorable than the Volume-Based Net Prices provided to an Equivalent customer or to GRAIL for that Supplied Product" (§7.m). FACT. [https://www.sec.gov/Archives/edgar/data/1604821/000155837024002083/ntra-20231231xex10d28.htm]
   - It also contains short-term project discounts for R&D and clinical-trial testing.
   - NIPT Test Fee credits sit on a five-tier volume schedule, and the credits "do not expire" (they apply to future NIPT consumables).
   - The universal grid (Tables 5.A/5.B) discounts by annual sequencing-consumables spend.
   - OPINION: GRAIL is an Illumina-owned (now spun-off) customer, so the MFN sets a pricing floor that follows GRAIL's best volume price. It also ties Natera's price to a large Illumina customer that is no longer inside Illumina. Whether the MFN survived the Eleventh Amendment is unclear, because that amendment shows none (finding 2).
4. **The Tenth Amendment (Ex. 10.2.10) is a WGS-MRD-specific discount schedule, effective 10 Jan 2025.** FACT. [https://www.lawinsider.com/contracts/5K1yiQbNUCe]
   - Discounts follow a Table 8 volume tier based on "Total Eligible Covered Consumables Spend", calculated annually.
   - Natera must file a signed report to claim the tier. The discount "may not be applied to Consumables that are not used for WGS-Based MRD Tests".
   - Supply shortages are allocated "in an equitable manner among its customers based on expiring lots".
   - Illumina must give minimum notice before discontinuing consumables, and Natera can keep buying for an extended period if it forecasts demand.
   - Dollar tiers and minimums are redacted.
   - OPINION: Illumina has priced WGS-MRD (the highest-Gb use case) with a dedicated volume-discount schedule. This is direct evidence that deep-MRD volume is bought at tiered discounts, not list, and it supports the price-versus-volume offset in thesis question 2.
5. **The "$11.6M" Natera snippet is still unverified, and a different number appeared.** A search summary cites Natera "purchase obligations of approximately $261.4 million" (FY25 10-K). I could not confirm it. WebFetch could not reach the commitments note, and no search output tied "$11.6M" to Natera's 10-K. The Q2'26 10-Q excerpt I could read gives only generic wording: it "enters into inventory purchases commitments… based on forecasted demand" and lists reliance on "sole source suppliers" as a risk. It names no dollar figure and does not mention Illumina. Treat both numbers as unverified. The original Natera supply agreement (Q2'26 Ex. 10.1) has a binding 4th-month forecast with ±25% flexibility. Its original term was three years from 18 Sep 2014. Neither number is a Natera minimum purchase commitment to Illumina. [Natera 10-Q Q2'26 filed 2026-08-07, https://www.sec.gov/Archives/edgar/data/1604821/000162828026054525/ntra-20260630.htm]
6. **Tempus's Illumina concentration is quantified in the FY25 10-K (search-derived, not read in the filing).** Illumina was about 33% of total vendor payments in 2025, 39% in 2024 and 33% in 2023. Amounts due to Illumina were about $15.9M at 31 Dec 2025. Illumina is the sole sequencer supplier and the sole maintenance provider. FACT, single source. [Tempus 10-K FY25, https://www.sec.gov/Archives/edgar/data/1717115/000119312526066961/tem-20251231.htm]
   - The 39% to 33% drop in 2025 is a hint that other vendor spend grew faster, not that Illumina spend fell (no dollar total found).
   - A direct WebFetch of the 10-K excerpt did not return these lines, so verify them in the filing.
7. **GeneDx names a supplier at about 20% of purchases in 2025, up from 13% in 2024 and 11% in 2023.** The 10-K lists Illumina, Life Technologies, Twist, Path-Tec and Agilent, and the filing does not say which one is the 20% supplier. Its language says "only a few other manufacturers" can supply and service sequencers, and a switch would require re-validating tests. FACT, search-summarized. [GeneDx 10-K FY25, https://www.sec.gov/Archives/edgar/data/1818331/000181833126000015/wgs-20251231.htm]
   - OPINION: if the 20% supplier is Illumina, the step-up fits GeneDx's volume growth (exome/genome +32%, E081). Treat this as unconfirmed.
8. **CMS CY2027 preliminary CLFS (21 Sep 2026): category cuts confirmed, per-code rates not obtained.**
   - Genomic sequencing is 42 codes at −23% weighted; PLA is 151 codes at −2.4%.
   - 1,528 of 1,947 codes got a weighted median, and 1,171 were below CY2026.
   - The overall average change is about −16%.
   - The cap is 15% per year over 2027–2029.
   - Final rates are due in November 2026, with a 30-day comment period.
   - The fact sheet says per-code rates are in the CMS CLFS file and gives no code-level values. [CMS fact sheet 2026-09-21, https://www.cms.gov/newsroom/fact-sheets/preliminary-calendar-year-cy-2027-medicare-clinical-laboratory-fee-schedule-payment-rates; Forvis Mazars, Oct 2026, https://www.forvismazars.us/forsights/2026/10/cms-releases-preliminary-2027-clinical-lab-fee-schedule-rates]
   - This adds the code counts and the 1,171/1,528 statistic to E097. It does not change E097.
9. **Caris Q2'26 10-Q (filed 2026): I found no text about Illumina, sole source or alternative sequencers in the portion I could retrieve.** This does not mean the 10-Q has none, because the fetch was truncated before Note 8 and the risk factors. The 'Beyond Illumina' snippet is therefore still unverified, not refuted. Caris's FY25 10-K still says Illumina is "the sole supplier of NGS instruments and the associated sequencing reagent kits" and the sole maintenance provider (consistent with E110). It states supply agreements carry purchase commitments "based on a binding forecast for an agreed-upon period of 12 months or less". [Caris 10-Q Q2'26, https://www.sec.gov/Archives/edgar/data/0002019410/000201941026000055/cai-20260630.htm; 10-K FY25, https://www.sec.gov/Archives/edgar/data/2019410/000201941026000016/cai-20251231.htm]

## PAMA exposure map (OPINION, built from E089, E097 and the above)

| Lab | Exposure to the CY2027 cut | Reason |
|---|---|---|
| Natera (Signatera, 0340U) | Low | It is an ADLT. Signatera's ADLT rate was already reset from $3,920 to $3,590 (E089). ADLT rates follow a different mechanism, and I did not find a CY2027 ADLT rate. |
| Guardant | Low for branded tests | Branded oncology tests are PLA/ADLT (E097). No Guardant-specific rate found. |
| GeneDx | Higher, unquantified | Exome/genome tests bill under 81415–81427 and fall in the −23% genomic sequencing group. Its payor mix and Medicare share were not checked. |
| Labcorp / Quest | Moderate | Generic molecular codes (−22%). Stock reaction was about −3% and −5% (E097). |

Illumina read-through: a Medicare cut hits lab revenue per test, so it pressures labs' willingness to pay for Gb only if it spreads to commercial payors. I found no evidence of that.

## Top-10 customer spend estimate (item 4): not built

I did not have defensible tests × Gb/test × $/Gb inputs from the sources reached in time, so I did not produce numbers. Usable anchors found:
- Tempus: Illumina is about 33% of vendor payments, $15.9M payable at year-end (FY25 10-K).
- Natera, Guardant: 1.04M and about 104K oncology tests in Q2'26 (E081), but Gb/test is not disclosed.
- Guardant: the Shield COGS of about $410 per test (E090) could back out sequencing cost only with an assumed share.

## Contradictions and stale data

- **$597 snippet:** dated 2023, not CY2027. Remove it from any CY2027 thesis.
- **Natera MFN:** present in the Eighth Amendment (31 Dec 2023) and absent from the Eleventh (Mar 2026). The ledger's gap 4 treated both as live.
- **Natera term:** the 2014 original had a 3-year term. The FY25 10-K says the current agreement expires in August 2033 (E109). The amendments I read did not state the term.
- **Natera purchase obligations:** $261.4M (search summary) vs "$11.6M" (E109 correction). Neither is verified.

## Gaps / what I could not find

- Guardant's Illumina exhibits and purchase-obligation note (item 2): not opened.
- Exact, BillionToOne, Adaptive, Veracyte, Myriad, NeoGenomics and Foundation purchase-obligation and supplier checks (item 3): not done. A BillionToOne search returned only unrelated results.
- Mentions of Ultima, Element or Roche SBX in any 10-K or 10-Q: none found. The Tempus 10-K excerpt returned no mention, but it was truncated.
- Caris capacity or sequencer purchase commitments: not seen (Note 8 not retrieved).
- CMS per-code CY2027 rates for 81415–81427, 81479 and 0340U: the CMS CLFS file and the CDLT July 2026 materials were not opened. Retrieve the "preliminary median file" linked from https://www.cms.gov/medicare/payment/fee-schedules/clinical-laboratory-fee-schedule-clfs.
- Natera's Q2'26 Ex. 10.1 is an older supply agreement ("TG Consumables"), not a new amendment. The Q2'26 10-Q Ex. 10.2–10.4 were not opened.

Sources: WebFetch of the SEC and CMS documents above; WebSearch summaries for GeneDx, Tempus and Caris, which were not read in the original filings.
