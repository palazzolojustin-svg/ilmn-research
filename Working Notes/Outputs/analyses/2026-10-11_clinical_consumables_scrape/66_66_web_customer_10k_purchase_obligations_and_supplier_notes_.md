# Agent 66: 66-web-customer-10K-purchase-obligations-and-supplier-notes-Tempus-GeneDx-Caris-BillionToO

*Model: sonnet. Run 2026-10-11 03:50:38. Cost $1.37 (API-equivalent).*

**Assignment:** Close open gaps 4, 6 and 7 on customer bargaining power, take-or-pay terms and customer cost per test. Use curl through Bash/PowerShell with a declared SEC User-Agent and download the full FY25 10-K and Q2'26 10-Q for each of Tempus AI, GeneDx, Caris Life Sciences, BillionToOne, Myriad, Exact Sciences and GRAIL (GRAIL accession 0001628280-26-017319). Grep the local copies; do not rely on the truncating fetch tool. Look for: 'Illumina', 'NovaSeq', 'sole source', 'single source', 'purchase obligation', 'minimum purchase', 'supply agreement', 'Ultima', 'Element', 'AXELIOS' and 'cost of revenue per test'. For each company extract: (a) supplier-concentration wording and the Illumina contract term, minimums, take-or-pay amounts, renewal and non-renewal dates; (b) the GRAIL supply agreement body (price, minimums, the 120-day non-renewal notice before 28 Feb 2027, and the exhibit list); (c) any platform shift from NovaSeq 6000 to X, or any second-source validation; (d) cost-of-goods per test or per sample trends that imply $/Gb deflation, and sequencing-cost commentary from the MD&A; (e) exhibits that are Illumina supply agreements (search EX-10 for 'Illumina'), including any redacted pricing tiers or rebate or volume-discount structures. Output a table of company, evidence, quote and accession or URL. Flag which customers can credibly bargain, meaning those with over $100M in annual sequencing spend or an alternative supplier.

## Key findings

**Coverage:** I found a few new, useful items and a lot of dead ends. I had no shell in this run (no curl or grep), only WebFetch and WebSearch. Fetches of the main 10-K and 10-Q documents truncate before the MD&A, commitments and exhibit sections. I could not run the full-text keyword sweep you specified. Coverage by company:
- **Read in primary form (new):** GRAIL R20, the GRAIL Q2'26 10-Q (part), the GeneDx R9 verbatim, and the Tempus-Illumina supply agreement exhibit.
- **Search paraphrase only:** Tempus 10-K (agreement terms) and Caris 10-K.
- **Fetched but no Illumina text returned (truncated):** BillionToOne 10-K and Exact FY25 10-K.
- **Not reached:** Myriad.

1. **The Tempus–Illumina supply agreement is the "open offer" template: 12 years, walk-away on 90 days' notice, no minimums (FACT).**
   - The exhibit says the term runs "12 years thereafter" with "no option to renew" for Appendix A terms.
   - It also says "Customer has a unilateral right to terminate its supply relationship with Illumina at any time and for any reason without termination liability upon ninety (90) days' prior written notice."
   - No minimum purchase or forecast commitment was stated; orders go by purchase order. Pricing, tiers and rebates are redacted "[***]" and "Grandfathered Pricing" is referenced.
   - Most-favored terms are "no less favorable than those entered into with GRAIL or any For-Profit Entity" (for certain IP-access terms, per the fetch summary).
   - Source: [Tempus S-1 exhibit, filed 2021, acc. 0000950123-21-013657](https://www.sec.gov/Archives/edgar/data/1717115/000095012321013657/filename8.htm).
   - This is new. The ledger's E213 covers only Tempus supplier percentages, and E232 and E228 cover Caris and Guardant. Tempus now matches Caris (E232): no lock-in, price can only fall.
   - The 12-year clock presumably also runs from the Aug 2021 GRAIL close (so ~Aug 2033), but I did not verify that.

2. **A "functional exclusivity" clause needs a check (FACT, summarizer reading).**
   - The Tempus exhibit says "All of Customer's purchases of products from Illumina for Clinical Use shall be made under this Agreement."
   - I read this as a pricing-terms clause, not an obligation to buy from Illumina. I did not verify that reading.
   - A search paraphrase of the 10-K says the agreement "does not require minimum orders or exclusive use of Illumina's platform" (Tempus 10-K FY25 search summary, [sec.gov](https://www.sec.gov/Archives/edgar/data/1717115/000119312526066961/tem-20251231.htm)). The wording needs a direct check.

3. **The agreement date for Tempus is June 2021 per the same search paraphrase (unverified).** The Tempus 10-K says the agreement covers sequencers, reagents, consumables and service contracts. It names Illumina as sole supplier for "certain sequencers, reagents, blood tubes and other equipment," at ~33% of 2025 vendor payments. That matches the percentage verified in CORRECTION 252. The same snippet puts lab supplies at ~$260M and ~44% of cost of revenue, which is single-source and unverified. It would also make Tempus an Illumina-spend customer in the low hundreds of millions.

4. **GRAIL R20 names Illumina as a licensor with "minimum annual royalty payments which are cancellable at the Company's discretion" (FACT).**
   - It sits in the commitments note alongside the Chinese University of Hong Kong, plus sales-based royalties on products such as Galleri.
   - Source: [GRAIL FY25 10-K R20, acc. 0001628280-26-017319](https://www.sec.gov/Archives/edgar/data/1699031/000162828026017319/R20.htm).
   - This refines E279. The $52.8M of non-lease commitments is "primarily" web services and lab supplies, and there is no take-or-pay on sequencing consumables. The Illumina minimums that exist are licence royalties, and GRAIL can cancel them.

5. **GRAIL is no longer an Illumina related party (FACT).**
   - The Q2'26 10-Q says "Illumina is not, and was not in the three and six months ended June 30, 2026, a related party."
   - It says Illumina fell below 10% ownership in Q4 2025, so related-party screening revenue and cost are tracked separately only "through November 17, 2025."
   - Source: [GRAIL 10-Q Q2'26, acc. 0001628280-26-054307](https://www.sec.gov/Archives/edgar/data/0001699031/000162828026054307/gral-20260630.htm).
   - It also confirms no change to the supply agreement in Q2'26 and repeats the royalty terms (suspension to 24 Dec 2026, 9%, 7% floor, 5% after $1B), as in CORRECTION 339.

6. **Caris 10-K FY25 (search paraphrase) says Illumina is the sole supplier of NGS instruments and reagent kits and the sole maintenance provider.** Replacements "may not be available" if a product is discontinued or changes substantially. The paraphrase mentions no second platform or purchase commitments. This is consistent with E110 and E199, and it sits oddly beside the Q2'26 call line that "two competitors out there now" could cut cost of goods and add capacity (E199). Source: [Caris 10-K FY25](https://www.sec.gov/Archives/edgar/data/2019410/000201941026000016/cai-20251231.htm). The paraphrase is weak and needs a direct read.

7. **GeneDx supplier-concentration wording, verbatim and new in full (FACT).** Two points are new:
   - **Second supplier:** "Another supplier accounted for approximately 10% and 11% of purchases for the years ended December 31, 2024 and 2023" (not in 2025).
   - **Risk management:** "This risk is managed by maintaining a target quantity of surplus stock. Alternative suppliers are available for some or all of these reagents and supplies."
   - It also shows no purchase-commitments text in R9. The first supplier is 20%, 13% and 11% for 2025, 2024 and 2023 (matches E216).
   - Neither supplier is named. A shift in share across two unnamed suppliers (10-11% falling out of the disclosure while the other rose) is consistent with supplier switching, but nothing proves it.
   - Source: [GeneDx FY25 10-K R9, acc. 0001818331-26-000015](https://www.sec.gov/Archives/edgar/data/1818331/000181833126000015/R9.htm).

8. **The GRAIL–Illumina Fourth Amendment (21 Jun 2024) redacts the royalty floor and threshold (FACT).**
   - Royalty obligations are waived and suspended during the "Interim Period."
   - §4.2(b) is changed to a floor of "[***]%" after cumulative payments reach "[***]".
   - The excerpt shows no take-or-pay, exclusivity or minimum language. I did not get the base agreement text.
   - Source: [8-K Ex. 10.4, acc. 0001193125-24-167025](https://www.sec.gov/Archives/edgar/data/1110803/000119312524167025/d851030dex104.htm).
   - A Justia snippet says the base agreement is a 10-year term with two-year automatic renewals, capped at a 20-year maximum (original effective 28 Feb 2017). That matches the 28 Feb 2027 first expiry in E257. I could not fetch the base agreement or the 120-day notice text myself; E257's 120-day language is still search-paraphrase only.

9. **The GRAIL FY25 10-K has no Illumina supply-agreement exhibit in the filing index (FACT).**
   - Exhibits are only: transition/separation Ex. 10.15, consent Ex. 23.1 and the Ex. 31/32 certifications.
   - The supply agreement is therefore incorporated by reference from earlier filings. Pricing and minimums are not in this filing.
   - The 10-K body search returned only the sole-supplier risk factor, the "high single-digit royalty... in perpetuity" wording, and related-party tables. It did not return the supply term or notice language.
   - Source: [GRAIL FY25 filing index](https://www.sec.gov/Archives/edgar/data/1699031/000162828026017319/).
   - Whether the 120-day notice was exercised cannot be seen from filings yet. Check the GRAIL Q3 10-Q or any 8-K around 5 Nov.

10. **Exact Sciences: the FY25 10-K text returned no Illumina or Ultima mentions (truncated at Regulation; the Business section's supplier text was not in the returned portion).** Nothing new on E281. The only thing the searches confirm is the 21 Jun 2022 "long-term supply agreement" with Ultima, with terms undisclosed ([BioSpace, 2022-06-21](https://www.biospace.com/ultima-genomics-and-exact-sciences-enter-long-term-supply-agreement-aimed-at-improving-patient-access-to-genomic-testing-by-driving-down-sequencing-costs)). Exact was acquired by Abbott (E177), so its bargaining power is now Abbott's.

## Evidence table

| Company | Evidence | Quote | Source |
|---|---|---|---|
| Tempus | Open-offer-style agreement: 12-year term, 90-day walk-away, no minimums | "terminate… at any time and for any reason without termination liability upon ninety (90) days' prior written notice" | [Ex. 10.13, acc. 0000950123-21-013657](https://www.sec.gov/Archives/edgar/data/1717115/000095012321013657/filename8.htm) |
| Tempus | ~33% of vendor payments; no exclusivity (search paraphrase) | not quoted | [10-K FY25](https://www.sec.gov/Archives/edgar/data/1717115/000119312526066961/tem-20251231.htm) |
| GRAIL | No sequencing take-or-pay; Illumina minimums are cancellable licence royalties | "minimum annual royalty payments which are cancellable at the Company's discretion" | [R20, acc. 0001628280-26-017319](https://www.sec.gov/Archives/edgar/data/1699031/000162828026017319/R20.htm) |
| GRAIL | Illumina no longer a related party | "Illumina is not, and was not in the three and six months ended June 30, 2026, a related party" | [10-Q Q2'26, acc. 0001628280-26-054307](https://www.sec.gov/Archives/edgar/data/0001699031/000162828026054307/gral-20260630.htm) |
| GRAIL | Fourth Amendment: royalty floor and threshold redacted | "[***]%" after cumulative payments reach "[***]" | [8-K Ex. 10.4, acc. 0001193125-24-167025](https://www.sec.gov/Archives/edgar/data/1110803/000119312524167025/d851030dex104.htm) |
| Caris | Illumina sole NGS supplier (search paraphrase) | not quoted | [10-K FY25](https://www.sec.gov/Archives/edgar/data/2019410/000201941026000016/cai-20251231.htm) |
| GeneDx | Two unnamed suppliers at 10-20%; alternatives "available for some or all" | "Alternative suppliers are available for some or all of these reagents and supplies." | [R9, acc. 0001818331-26-000015](https://www.sec.gov/Archives/edgar/data/1818331/000181833126000015/R9.htm) |

## Who can credibly bargain

OPINION. The contract evidence shows that customers can leave. Whether they will depends on spend and a validated second platform.
- **Contract lock-in is absent at every customer where the text was read.** That covers Tempus (this wave), Caris (E232), Natera (E227, E258), Guardant (E228) and GRAIL (the cancellable licence minimums above). All can walk on 90 days' notice, and none has a disclosed dollar take-or-pay on Illumina volume.
- **Bargaining power by spend (OPINION):**
  - Tempus: ~33% of vendor payments with ~$260M of lab supplies. If the Illumina share is a third of that lab-supply figure, it is under $100M, but that depends on unverified inputs.
  - Natera, Guardant, Caris and GRAIL were already identified as the large accounts.
  - Credible alternative supplier: only Caris says it wants a second source (E199). Exact had an Ultima agreement (E281, stale).
- Everything that holds these customers is validation cost and assay lock-in, not contract terms. That matches E279.

## Contradictions and stale data

- **E213 / CORRECTION 252:** the Tempus search paraphrase again names Illumina and the 33% figure but not the payable. Its 12-year agreement term (Ex. 10.13) also sits inside the 2033 window used for Natera and Caris.
- **E257:** the 28 Feb 2027 expiry and 120-day notice are still unsupported by a primary body text. The Justia snippet supports the 10-year-plus-two-year-renewals structure only.
- **Possible ledger conflict:** the Tempus exhibit's "no option to renew" language for Appendix A terms is not reconciled with the 12-year term described for Caris.
- **E281:** the Exact FY25 10-K is still not read; the FY23 secondhand reading remains the only evidence.

## Gaps / what I could not find

- **Truncation:** the main 10-K documents truncate before MD&A, commitments and exhibits. The BillionToOne and Exact fetches returned no supplier text at all, so absence there means nothing. The BillionToOne search returned only the FY25 10-K link ([blln-20251231.htm](https://www.sec.gov/Archives/edgar/data/2070849/000207084926000017/blln-20251231.htm)).
- **Not done:** Myriad (Illumina–Myriad strategic partnership coverage on BioSpace is the only lead found), Q2'26 10-Qs for Tempus, GeneDx, Caris and BillionToOne, and any cost-of-revenue-per-test MD&A commentary.
- **Exhibits:** the GRAIL supply agreement body (price, minimums, 120-day notice) is not a filing exhibit in the FY25 10-K and is not in the Form 10 information statement either. It should be in the 2024 Form 10 exhibit list or the amended filings; I did not reach it. No EX-10 Illumina exhibits found for GeneDx, Myriad or BillionToOne.
- **Suggested fix:** rerun items from a shell with curl and grep on the full documents, as the assignment specified.
