# Agent 106: 106-web-ILMN-accounting-quality-XBRL-SEC-correspondence-non-GAAP-and-working-capital

*Model: sonnet. Run 2026-10-11 10:32:54. Cost $0.48 (API-equivalent).*

**Assignment:** Test Illumina's earnings quality using primary data not yet mined. Source 1: data.sec.gov XBRL companyfacts and frames for ILMN (CIK 1110803), quarterly from Q1'23 to Q2'26: product revenue vs service revenue, cost of product revenue, receivables and DSO, inventory (raw materials, WIP, finished goods) and days, inventory reserve, deferred revenue, contract liabilities, RPO, capex, capitalized software, SBC, restructuring, acquisition-related and other non-GAAP add-backs. Build a table of the recurring 'one-time' non-GAAP adjustments by quarter. Compare non-GAAP EPS to GAAP EPS and to free cash flow. Check whether DSO, inventory days or deferred revenue moved in ways that suggest channel stuffing, year-end pull-forward, or reagent rental or lease accounting changes. Source 2: SEC EDGAR correspondence (UPLOAD and CORRESP letters) for ILMN 2019-2026, to find any SEC comment on non-GAAP measures, revenue recognition, segment reporting or key metrics. Source 3: the FY25 10-K and Q2'26 10-Q notes on revenue disaggregation, lease and rental arrangements, concentration, and Critical Audit Matters (compare FY22-FY25 CAMs). Source 4: any auditor (Ernst & Young) change or ICFR comment, and 8-K Item 4.02 or 5.02 events since 2023. Quantify every metric change and cite the XBRL tag, accession number or URL. Flag anything that contradicts management's narrative. Do not repeat the DEF14A, Form 4 or CDA work already done. Stop at 20 minutes and return findings only.

## Key findings

Most of what I checked is clean. Two items are new and worth following up: the Q4'25 receivables spike and an inventory-reclassification discrepancy. I did not build the full non-GAAP add-back table, and I did not complete the CAM comparison or the ICFR check (see Gaps).

- **SEC correspondence found no accounting comments on ILMN. The 2019–2026 window is nearly empty.**
  - FACT: The EDGAR UPLOAD list has only 2020-12-03, 2021-11-19, 2023-04-05 and 2023-04-17 in the window (34 filings in total, last one April 2023). The CORRESP list has only 2021-02-05, 2021-11-22 and 2023-04-07.
  - FACT: None concerns non-GAAP measures, revenue recognition, segments or key metrics.
  - The three letters I opened are all transaction-related:
    - 2021-02-05 (0001193125-21-030974) is an acceleration request for the GRAIL Form S-4.
    - 2021-11-22 (0001193125-21-337128) answers comments on the CVR exchange offer, Schedule TO-I.
    - 2023-04-07 (0001193125-23-095383) answers comments on proxy overvote disclosure (PREC14A).
  - I did not open the UPLOAD letters (2020-12-03, 2021-11-19, 2023-04-05, 2023-04-17). The 2023-04-05 and 2023-04-17 UPLOADs fall between the 2023-03-30 PREC14A and the 2023-04-07 response, so they are probably the proxy-overvote comments. The other two are probably the S-4 and CVR comments.
  - URLs: sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1110803&type=CORRESP and type=UPLOAD, fetched 2026-10-11.
  - Takeaway: no public SEC staff challenge to the non-GAAP, "clinical" or pull-through metrics. This is consistent with E147, E159 and E036 and does not contradict them. The ledger says the SEC investigation is a July 2023 document request, which is separate from the comment-letter channel.

- **Auditor: no change.** The 8-K for the 2026 annual meeting reports shareholders ratified Ernst & Young LLP for the fiscal year ending 3 Jan 2027 (For 133,174,094; Against 7,762,010; Abstain 107,927). [sec.gov/Archives/edgar/data/0001110803/000111080326000124/ilmn-20260521.htm, 8-K dated about 2026-05-21/26.] A search for Item 4.01 or 4.02 events returned nothing, but the search is not exhaustive. Not verified from the EDGAR filing index.

- **New: the Q4'25 receivables spike.**
  - FACT: Receivables at 28 Dec 2025 were $854M (XBRL `AccountsReceivableNetCurrent`, accn 0001110803-26-000024). That is up $119M from $735M at 29 Dec 2024. Q4'25 revenue was $1,159M, up 5.0% from $1,104M.
  - Revenue by quarter comes from the XBRL `RevenueFromContractWithCustomerExcludingAssessedTax` series (Q4 derived as FY minus Q1–Q3).
  - Calc: period-end DSO (receivables ÷ quarterly revenue × 91 days) was 67 days in Q4'25 vs 60.6 in Q4'24. Q1'26 was 61.5 on $738M (accn …-26-000092). Q2'26 was 60.0 on $764M (accn …-26-000160), vs 60.3 for Q2'25 ($701M on $1,059M).
  - OPINION: Q4'25 is a +6 to +7 day outlier that fully reversed within a quarter. That pattern fits back-end-loaded December shipments, instrument-heavy shipments, or collections slipping into January. It is not a persistent stretch of terms, since Q1'26 and Q2'26 are back at about 60 days.
  - Prior Q4s were also seasonally high, so the outlier is partly seasonal. In Q4'23, $734M on $1,128M of revenue gives about 59 days. In Q4'24, $735M gives about 60.6 days. So Q4'25 is the only year-end with a clearly higher DSO.
  - I could not read the 10-K MD&A to see management's explanation for the AR build. The Q4'25 call may address it; I did not check.
  - Cash-flow link: a $119M AR build in Q4'25 depressed FY25 operating cash flow, and the Q1'26 release of $116M helped Q1'26. I did not verify the reported operating cash flow.

- **New: inventory figures conflict between XBRL and the 10-Q, and E037's figures need qualifying.**
  - FACT: The Q2'26 10-Q inventory note shows gross inventory of $778M, less a $123M reserve, so net $655M. At 28 Dec 2025, gross was $697M, less a $133M reserve, so net $564M. Components at 28 Jun 2026: raw materials $295M, work in process (WIP) $426M, finished goods $57M. At 28 Dec 2025: $254M, $398M and $45M. (10-Q ilmn-20260628.htm, fetched 2026-10-11.)
  - FACT: The XBRL `InventoryNet` tag reports $629M for 2026-06-28 and $564M for 2025-12-28. The $26M gap equals the "long-term inventory" the 10-Q says is now classified in other assets (SomaLogic-acquired manufacturing processes with cycles over one year).
  - E037 states inventory rose $564M→$655M. That mixes bases: $564M was current-only, while $655M includes the $26M long-term piece. On the same current-only basis the rise is $564M→$629M (+$65M, +11.5%), and total net inventory including the long-term piece is $655M. Because the 10-Q's own December figure excludes any long-term piece, treat the increase as $65M to $91M depending on the basis.
  - The long-term reclassification did not exist at Dec 2025 as presented, so it is a presentation change that makes headline current inventory look $26M lower than total.
  - Raw materials rose 16% (+$41M) and WIP rose 7% (+$28M) in six months. Finished goods rose 27% (+$12M) but are only $57M. So the build is in components and WIP, not finished goods. That is not a channel-stuffing signature (channel stuffing would show in AR and in finished goods at the company, which are flat to modest).
  - The reserve fell $10M (7.5%) while gross inventory rose $81M (11.6%). Reserve coverage dropped from 19.1% to 15.8% of gross inventory. Against a critical audit matter that names the NovaSeq X migration as a driver, a falling reserve ratio during a large 6000→X transition is worth a question to management. This quantifies the E037 observation.
  - Cost of product revenue was $291M in Q2'26 on product revenue of $982M. That gives a product gross margin of 70.4%, vs $276M on $912M (69.7%) in Q2'25. This is GAAP and includes amortization; I did not adjust it.

- **Receivables, inventory and contract liabilities show no sign of channel stuffing or a lease-accounting change.**
  - FACT: Quarterly receivables ran from $635M to $764M over Q1'24–Q2'26. DSO stayed in a 59–62 day band except for Q4'25.
  - FACT: Contract liabilities (XBRL `ContractWithCustomerLiability`) moved in a tight $293M–$346M range since Q1'23:

| Period | Contract liabilities |
|---|---|
| Q1'23 | $324M |
| Q3'24 | $293M (low) |
| Q4'25 | $346M (high) |
| Q2'26 | $333M |

  - This agrees with E198, which gives $346M→$333M. I add the longer series: no step change that would indicate a rental or lease accounting change.

- **Revenue mix: services and other are growing faster than product, and product is still 85% of revenue.**
  - FACT: Q2'26 product revenue was $982M (+7.7% y/y) vs service and other $177M (+20.4% from $147M). Service cost was $80M vs $71M (+12.7%).
  - FACT: 10-K FY25 mix: consumables 74% (72% in FY24, 68% in FY23), instruments 11% (12%, 16%), services/other 15% (16%, 16%). Sequencing was 92% of revenue (91%, 91%).
  - OPINION: The consumables share rising from 68% to 74% in two years is the arithmetic of a falling instrument line plus a large consumables base. It also means any pricing shock hits a larger share of revenue.

- **Customer concentration language: FACT.** The FY25 10-K risk factor says: "A portion of our revenue is increasingly derived from a small number of large, centralized laboratory customers." The loss of, or reduction in purchases by, a key customer "could materially and adversely affect our business." I did not capture whether the 10-K names any customer above 10% of revenue. This is relevant to Q2 (customer bargaining power). It supports E063 on volume discounts, but I found no quantified concentration.

- **Allowance for credit losses.** The allowance rose to $9M at 28 Jun 2026 from $7M at 28 Dec 2025 (10-Q). That is 1.2% of receivables (0.8% before), so a small uptick, not a signal.

- **Capex.** Net purchases of property and equipment were $78M in H1'26 vs $62M in H1'25 (+26%). (10-Q.) This is consistent with investment in the manufacturing build-out. I did not split out capitalized software.

## Contradictions and stale data

- E037 (inventory $564M→$655M) mixes current and total-inventory bases. XBRL `InventoryNet` for 28 Jun 2026 is $629M, and the 10-Q note total is $655M. See the key finding above.
- E039 and the correction at line 228 conflict on reagent rental. My 10-Q extract found no mention of reagent rental or sales-type lease in what was returned, but the fetch tool returned only a partial excerpt, so this is not evidence of absence. It does not resolve the conflict. The 10-K lease footnote still needs direct reading.
- XBRL series for 2022 Q1–Q3 carry different accession styles (e.g. 0001110803-22-000013). I used them only for context.

## Gaps / what I could not find

- I did not build the quarterly non-GAAP "one-time" add-back table (restructuring, acquisition-related, SBC, amortization). I did not retrieve the XBRL tags for those items or the GAAP-to-non-GAAP EPS and free-cash-flow comparison. This is the main unfinished part of the assignment.
- FY22–FY25 critical audit matter comparison not done. The fetch tool truncated the 10-K before the auditor's report. The only CAM evidence is E037.
- Item 9A (ICFR) conclusion, any material weakness, and the 10-K's explanation of the AR build are unread.
- The four UPLOAD letters (2020-12-03, 2021-11-19, 2023-04-05, 2023-04-17) were not opened. Their topics are inferred from the matching CORRESP letters.
- No data.sec.gov frames calls were made, and no 8-K Item 5.02 review was done.
- Tool caveat: all WebFetch results were summarised by a small model, so values should be spot-checked against the XBRL JSON. The receivables, inventory, contract-liability and revenue series are internally consistent with the 10-Q figures (e.g. AR $764M, contract liabilities $333M, revenue $1,159M), which supports their accuracy.
