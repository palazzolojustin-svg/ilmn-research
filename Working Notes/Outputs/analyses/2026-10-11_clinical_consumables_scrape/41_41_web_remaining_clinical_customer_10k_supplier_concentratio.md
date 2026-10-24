# Agent 41: 41-web-remaining-clinical-customer-10K-supplier-concentration-and-Illumina-agreements

*Model: sonnet. Run 2026-10-11 03:05:41. Cost $0.65 (API-equivalent).*

**Assignment:** Goal: close the supplier-concentration and contract gaps for the clinical customers not yet covered, using raw SEC EDGAR filing text (download the full .htm with Bash/curl using a User-Agent header such as 'Research palazzolojustin@gmail.com', or fetch in pieces; WebFetch truncates). Priority order. (1) Natera FY25 10-K (accession 0001104659-26-020881): quote the Illumina supply-agreement narrative, the August 2033 term, any minimum purchase or take-or-pay language, any pricing-adjustment mechanism, and whether the 'material suppliers' language names Illumina. Then read Ex. 10.28 (FY23) and the Tenth Amendment (ntra-20241231xex10d210.htm) and check whether the Eighth Amendment MFN survived the Eleventh Amendment. (2) Guardant: from the FY23-FY25 10-K exhibit indexes, find any Illumina exhibit after Amendment #5 and the 2023 settlement agreement. Extract term, pricing, minimums, and exclusivity language. (3) For GeneDx (the unnamed 20/13/11% supplier), Exact Sciences/Abbott, BillionToOne, Adaptive, Veracyte, Myriad, NeoGenomics, Tempus (risk-factor text in tem-20251231.htm, accession 0001193125-26-066961, plus the $15.9M payable) and Caris (Note 8 of cai-20251231.htm, accession 0002019410-26-000016, which may describe an open-offer agreement with Illumina; verify the Aug 2033 date and the 90-day termination wording, because it may be conflated with Natera's): pull the sole-source or single-supplier risk factors, purchase obligations tables (total $ and years), supplier-concentration percentages of COGS or purchases, and any statement on NovaSeq X transition savings, revalidation costs, or Illumina price changes. Also search exhibit lists for redacted 'Illumina' supply or development agreements (Ex. 10.x). Quantify: purchase commitments in $, term end dates, supplier % of COGS, and any language showing whether the customer, not Illumina, captures the 6000-to-X saving. Label each point FACT with accession number and page or section. Hard stop at 20 minutes; list what you could not open.

I'm wrapping up. WebFetch truncates the big filings, so I couldn't read most of the 10-K text and I'm reporting what I did confirm.

## Key findings

**1. The "August 2033" date is the GRAIL-era open offer, not something specific to Natera. It does not look conflated.** (FACT, with the term text from the Caris exhibit and the Natera/Caris 10-K wording from search summaries.)
- This corrects and extends E109, E110 and the "unverified" note on Caris's date in E192/F37.
- The Illumina–Caris Supply Agreement (Caris S-1 Ex. 10.2(A), accession 0001104659-25-052381) says "It shall be effective for twelve (12) years from the closing of the Transaction." The Transaction is the GRAIL acquisition, which closed in August 2021, so the term ends August 2033.
- Natera and Caris therefore share an end date because they use the same open-offer template. Guardant's January 2033 date comes from its own bilateral contract (E110).
- The open offer was extended to customers developing oncology tests for six years from closing, per the GRAIL Form 10 exhibit (sec.gov/Archives/edgar/data/1699031/000119312524152397/d556103dex991.htm). I infer that window closes around August 2027. I did not confirm the window's end date or whether Illumina has said anything about renewing it.

**2. Caris's open-offer terms are confirmed in the contract text.** (FACT, Caris S-1 Ex. 10.2(A), accession 0001104659-25-052381; search summary of Caris's 10-K, not read in the 10-K itself)
- Termination: "Customer has a unilateral right to terminate its supply relationship with Illumina at any time and for any reason without termination liability upon ninety (90) days' prior written notice to Illumina."
- Minimums: "This Supply Agreement is not contingent on any purchase commitments by Customer." There is no take-or-pay.
- Exclusivity: the IVD Test Kit Agreement is "Non-exclusive."
- Pricing: the customer picks either Grandfathered Pricing or Universal Pricing, which is a Volume-Based Net Price on tiered volume discounts (Appendix 1).
- MFN: Volume-Based Net Prices must be "no less favorable… than the Volume-Based Net Prices provided to GRAIL."
- Price freeze: "The inflation-adjusted (based on the Bureau of Labor Statistics' Analytical Laboratory Instrument Manufacturing Index in the Producer Price Index) Volume-Based Net Price shall not increase," except for material cost increases beyond Illumina's control.
- Implication (OPINION): Illumina cannot raise the open-offer price except for such cost increases, and it cannot be pushed above what GRAIL pays. Customers can walk on 90 days' notice. Illumina's only lever is volume tiers, which means cuts in $/Gb are contractual. This extends E192 and E194.

**3. The Natera Eighth Amendment MFN is the open-offer MFN, and it most likely survives.** (OPINION, resting on #2 and E192)
- E192 quotes the Eighth Amendment clause as "no less favorable… to an Equivalent customer or to GRAIL." That is the same GRAIL-benchmarked language as the open offer.
- E194 shows the Eleventh Amendment adds the same "shall not increase further" inflation freeze, which matches the open-offer wording above. This suggests Natera's contract is built on the open-offer chassis.
- I did not read the Tenth or Eleventh Amendment text, so I can't say whether the MFN was kept outside the restated sections. It is probably still there, but this is unverified.

**4. Tempus: Illumina is named, and the payable and share are confirmed.** (FACT, from a search summary of the Tempus FY25 10-K, accession 0001193125-26-066961; I did not read the primary text)
- Tempus relies on Illumina "as the sole supplier of the sequencers and as the sole provider of maintenance and repair services."
- Illumina was about 33% of total vendor payments in 2025.
- Amounts due to Illumina were about $15.9M at 31 Dec 2025.
- The risk factor says any disruption in Illumina's operations or "termination or suspension of the relationship" could materially hurt the supply chain and revenue.
- This resolves the open item in gap 3 about the $15.9M payable and the unnamed 33%.
- Note: if purchases from Illumina are 33% of vendor payments, that is not a share of COGS.

**5. GeneDx: Illumina is named among suppliers, but the 20/13/11% supplier is not identified.** (FACT, search summary of FY25 10-K, wgs-20251231.htm, accession 0001818331-26-000015)
- One supplier was about 20%, 13% and 11% of purchases in 2025, 2024 and 2023.
- GeneDx names Illumina, Life Technologies, Twist, Path-Tec and Agilent as limited-source suppliers.
- Switching suppliers "could require that they revalidate their tests."
- The rising share (11% → 20%) is consistent with Illumina, but the filing text I saw doesn't say so. Two of the other named suppliers could also fit. Do not attribute it to Illumina.

**6. Guardant: term and exit rights are confirmed from the FY23 10-K.** (FACT, Guardant FY23 10-K, accession 0001576280-24-000043)
- The supply agreement runs "until January 2033," auto-renews yearly, and Guardant "may also terminate… for convenience upon 90 days' prior written notice." This matches E110.
- The 1 Aug 2023 settlement included "a new long-term purchase and supply commitment" (search summary of the Guardant announcement). The wording does not show whether it is a binding minimum.
- Amendments #1–#5 to the 2014 agreement are on Justia (contracts.justia.com/companies/guardant-health-inc-4491/). Amendment No. 2 gave a five-year term with one-year renewals and 12 months' notice.
- I did not find the exhibit number for the post-Amendment-5 or settlement documents, and I did not read the pricing terms.

## Contradictions and stale data
- E110 and E192/F37 treated Caris's August 2033 date as possibly conflated with Natera's. It is a genuine common date from the 12-year open-offer term.
- The Caris 10-K itself returned nothing when I queried Illumina, so I could not tie its Note 8 wording to the 10-K. The 90-day and no-minimum language comes from the S-1 contract and a search summary of the 10-K, so it may differ slightly in the 10-K.
- The Natera 10-K query for Illumina returned only the Verinata competitor mention. That is a truncation problem, not evidence the supply language is absent. The search summary supports E109 (sole supplier for Panorama, Horizon, Signatera, Prospera, expiring August 2033).

## Gaps / what I could not find
- Bash is disabled in this session, so I could not download the full filings. WebFetch returned partial text only.
- Not opened or not answered:
  - Natera 10-K narrative, purchase-obligation table and "material suppliers" risk factor; Natera Ex. 10.28 and the Tenth Amendment (MFN survival).
  - Caris 10-K Note 8 (the URL with CIK 1856236 returned a 404; the correct CIK is 2019410).
  - Tempus risk-factor primary text and purchase-obligation table.
  - Guardant's post-Amendment-5 and settlement exhibits.
  - GeneDx supplier identity and its purchase obligations.
  - Exact Sciences/Abbott, BillionToOne, Adaptive, Veracyte, Myriad and NeoGenomics.
  - Any statement on who captures the 6000-to-X saving (beyond E043/E044).
  - Redacted Illumina development agreements.
- To close these, someone with local download access should fetch the .htm files directly.

**Net:** this is new but modest: #1–#3 and #5 are material, and I did not find evidence contradicting the known facts.

Sources: [Caris S-1 Ex. 10.2(A)](https://www.sec.gov/Archives/edgar/data/2019410/000110465925052381/tm2415719d15_ex10-2a.htm), [Caris 10-K FY25](https://www.sec.gov/Archives/edgar/data/2019410/000201941026000016/cai-20251231.htm), [Natera 10-K FY25](https://www.sec.gov/Archives/edgar/data/1604821/000110465926020881/ntra-20251231x10k.htm), [Tempus 10-K FY25](https://www.sec.gov/Archives/edgar/data/1717115/000119312526066961/tem-20251231.htm), [GeneDx 10-K FY25](https://www.sec.gov/Archives/edgar/data/1818331/000181833126000015/wgs-20251231.htm), [Guardant 10-K FY23](https://www.sec.gov/Archives/edgar/data/1576280/000157628024000043/gh-20231231.htm), [GRAIL Form 10 exhibit](https://www.sec.gov/Archives/edgar/data/1699031/000119312524152397/d556103dex991.htm), [Guardant contracts on Justia](https://contracts.justia.com/companies/guardant-health-inc-4491/).
