# Agent 47: 47-web-Natera-Guardant-Illumina-supply-agreements-and-customer-cost-per-test

*Model: sonnet. Run 2026-10-11 03:13:41. Cost $1.05 (API-equivalent).*

**Assignment:** Focus on the contracts and unit economics between Illumina and its largest clinical customers, using EDGAR primary exhibits and earnings-call transcripts not yet mined. (a) Natera (CIK 1604821): list all Illumina supply/collaboration agreement exhibits and amendments (Exhibit 10.x, many with redacted terms) across FY21-FY25 10-Ks and 10-Qs and the Q1/Q2 2026 10-Q; extract term/expiry (reported Aug 2033?), MFN or most-favored pricing clauses, 'Volume-Based Net Price' mechanics, minimum purchase commitments, instrument purchase terms, exclusivity, and whether MFN survived the Eleventh Amendment. (b) Guardant (CIK 1576280): Illumina supply agreement exhibits and amendments (incl. Amendment #5 and later), term, minimums, pricing mechanism. (c) Open-offer: the GRAIL spin Form 10 / Ex. 99.1 and Illumina statements on the 6-year oncology open offer from Aug 2021 (expiry about Aug 2027) and what happens after. (d) Q2 2026 earnings-call transcripts (Natera, Guardant, Tempus, GeneDx, BillionToOne, Caris, Exact) from sources such as Seeking Alpha, Motley Fool, Investing.com, company IR sites: extract every statement on sequencing cost per test/COGS per sample, NovaSeq X adoption, Illumina price concessions, volume growth in samples, second-sourcing (Element, Ultima, Roche AXELIOS, MGI) and gross-margin drivers; compute implied sequencing cost per test change where numbers allow. (e) Secondary: any dated public price for the NovaSeq X 35B/25B/10B/1.5B flow cell (Illumina price list, Genohub, GSA, Fisher) and the S4/25B cost per Gb. Quote exact words; cite URLs and dates. Stop after about 20 minutes.

## Key findings

Time ran out before I could cover everything. Parts (a)–(c) and (e) produced new evidence. Part (d) produced little. The Guardant term is the one item from a search summary only, and I did not read the Guardant exhibit myself.

1. **The Natera and Caris contracts come from Illumina's 2021 "Open Offer" template, and Natera's Aug 2033 expiry is that template's 12-year clock.** (FACT, from the filing and the search summary.)
   - The 12-year term runs from the 18 Aug 2021 GRAIL close, "regardless of when this offer is accepted".
   - The offer stays open for six years, to about Aug 2027.
   - Customers who sign by then keep the 12-year term and its price protections to Aug 2033.
   - Natera's FY25 10-K says Illumina is its sole supplier under a supply agreement that "expires in August 2033" (sec.gov/Archives/edgar/data/1604821/000110465926020881/ntra-20251231x10k.htm).
   - I did not find an end date for the contract terms after the window closes.
   - This closes the "reported Aug 2033?" item in open gap 2.

2. **The Open Offer contains a hard price lock.** (FACT, from the Caris Exhibit 10.2(a), via a fetch summary.)
   - Quote: "The inflation-adjusted...Volume-Based Net Price...shall not increase", with narrow exceptions for material cost increases outside Illumina's control.
   - Illumina's own test-terms page also promises "no price increases for the sequencing products covered".
   - The offer includes a 43% cost-per-Gb cut by 2025. The wording is that the highest-throughput instrument and flow cell will be "at least 43% lower than the comparable cost per gigabase today".
   - Source: Caris Ex. 10.2(a), sec.gov/Archives/edgar/data/2019410/000110465925052381/tm2415719d15_ex10-2a.htm, and the Illumina test-terms page (tst-web.illumina.com/areas-of-interest/cancer/test-terms.html).
   - Read-through (OPINION): lab list prices cannot rise under these contracts, so the ledger's price-increase items (E033, E064) mostly hit non-contract customers.
   - A customer on this template can also use that price-lock to resist price increases on the 6000 (OPINION).

3. **The Open Offer is non-exclusive and has no purchase minimums, and the customer can leave on 90 days' notice.** (FACT, Caris exhibit.)
   - "This Supply Agreement is not contingent on any purchase commitments."
   - Quote: "Customer has a unilateral right to terminate...at any time and for any reason without termination liability upon ninety (90) days' prior written notice."
   - Illumina cannot terminate for convenience.
   - The offer covers US use only, on NextSeq, NextSeqDx and NovaSeq.
   - Implication (OPINION): contracted clinical volumes carry no lock-in. Labs can move to Roche, Ultima or Element at will, which is the bargaining-power point in thesis question 2.
   - The Caris text is the template. I did not verify that Natera's own agreement has the same terms.

4. **Natera's Eighth Amendment (31 Dec 2023) contains a most-favoured-price clause that names GRAIL.** (FACT.)
   - Quote: Natera "will have access to Volume-Based Net Prices that are no less favorable than the Volume-Based Net Prices provided to an Equivalent customer or to GRAIL".
   - It also sets a five-tier NIPT credit structure based on annualized NIPT volume, with credits that "do not expire". Amounts are redacted.
   - The discount tables (5.A, 5.B) are redacted.
   - Source: sec.gov/Archives/edgar/data/1604821/000155837024002083/ntra-20231231xex10d28.htm. The Eighth is Ex. 10.2.8.

5. **The Eleventh Amendment (effective 2 Mar 2026) deleted "Volume-Based Net Price" and replaced it with "Net Price".** (FACT, via fetch summary.)
   - The new definition is the "then-current, actual list price...less any applicable discount". It excludes taxes, shipping, insurance and tariff charges.
   - The fetch summary did not locate a most-favoured clause. It also did not mention GRAIL or a term extension.
   - This answers gap 2(b) only partly (OPINION): the MFN clause was keyed to the "Volume-Based Net Price" label, which the Eleventh Amendment deleted. Whether MFN survives is not settled by this read. Someone should read the full exhibit.
   - Source: sec.gov/Archives/edgar/data/1604821/000162828026032478/ntra-20260331xex101.htm. It was filed with the Q1'26 10-Q.

6. **The Eleventh Amendment lets Illumina pass tariff costs through to Natera.** (FACT.)
   - Tariff charges are defined by reference to Trade Act §122 and Presidential Proclamation 11012.
   - Illumina can invoice Natera for the tariff rate above a redacted threshold.
   - It must give 30 days' notice. Charges are non-retroactive, and Natera gets pro-rata refunds if Illumina gets rebates.
   - This is a contractual price increase even though list price is locked (OPINION). It supports E064 and E033 (Illumina sharing cost increases with customers).

7. **The Eleventh Amendment sets 2026–2028+ calendar-year tiered consumables discounts based on "Prior Year Spend".** (FACT, thresholds redacted.)
   - There are separate discounts for exome-based MRD (WES-based MRD) and genome-based MRD (WGS-based MRD), the latter with a retroactive tier structure.
   - Natera must send monthly certification reports and forecasts. Instrument hardware is in a redacted Table 2, with service credits for volume thresholds.
   - OPINION: this is volume-tiered pricing set by the prior year's spend. A "Prior Year Spend" test means Natera's price per Gb falls as its own spend rises, so volume growth passes through as lower unit price at Natera. That fits E048 (Gb +40%, revenue +5%).

8. **The Tenth Amendment (effective 10 Jan 2025) built a seven-tier WGS-MRD discount, and it has a reopener.** (FACT, tiers redacted.)
   - Table 8 sets discounts on "Eligible Covered Consumables Spend" for the "Current WGS Product".
   - Quote: "If market conditions for MRD Tests materially change during the Term, either Party may initiate and the Parties will engage in good faith discussions regarding the discounting structure set forth herein."
   - Shortage clause: Illumina will "allocate the existing supply in an equitable manner among its customers based on expiring lots."
   - Source: lawinsider.com/contracts/5K1yiQbNUCe. The filing is Ex. 10.2.10.
   - OPINION: the amendment shows Natera negotiating a bespoke genome-MRD price, as in E062 (application-specific pricing). It also gives Natera an explicit route to re-trigger a price cut if competing sequencers cheapen MRD.

9. **Natera's amendment history, with dates.** (FACT, from the Eleventh Amendment recital.)
   - Original agreement: 16 Aug 2013.
   - Amendments: 18 Sep 2014, 23 Sep 2015, 8 Jun 2016, 3 Jan 2019, 18 Dec 2019, 8 May 2020, 7 Oct 2021, 31 Dec 2023, 11 Mar 2024, 10 Jan 2025, then the Eleventh on 2 Mar 2026.
   - The Ninth (Mar 2024; Ex. 10.29 in the FY24 10-K, ntra-20241231xex10d29.htm) is about regulatory documentation support and change notices. The fetch summary showed no pricing or term content.
   - The BamSEC list confirms the Ninth, Tenth and Eleventh exist.
   - Amendment numbering by date is my reading of the recital, not confirmed by fetching the filing index.

10. **Guardant's term runs to Jan 2033, with automatic one-year renewals.** (FACT per search summary of the 10-K and Amendment #5; I did not read the exhibit.)
    - The summary says either party can give non-renewal notice at least 12 months before the renewal date.
    - It says Guardant "may also terminate...for convenience upon 90 days' prior written notice".
    - The agreement dates from Sep 2014, and Amendment #5 extended the term.
    - It is not an Open Offer clone, because it predates the offer and was extended to a different date (Jan 2033 vs Aug 2033).
    - I did not find the pricing mechanism or any post-Amendment-5 exhibits.

11. **Natera's Q2'26 call had no sequencing-cost disclosure.** (FACT, fetch of the Motley Fool transcript, 2026-08-13: fool.com/earnings/call-transcripts/2026/08/13/natera-ntra-q2-2026-earnings-call-transcript/.)
    - The summary found no mention of Illumina, NovaSeq X, per-test sequencing cost or alternative suppliers.
    - Only generic COGS commentary: "we leave a lot of room to achieve COGS improvements over time as volume scales".
    - New products (Fetal Focus, Latitude, Signatera Genome) are "not yet optimized for COGS", and COGS reduction projects should pay back "over the next 12 to 18 months".
    - Implication (OPINION): Natera gives no 6000-to-X migration data, consistent with the gap in E020. Signatera Genome, a WGS-based MRD test, is a new high-Gb product still being ramped.
    - This is a summarised fetch, so a short Illumina mention could have been missed.

12. **Dated core-lab prices for the NovaSeq X flow cell (partly new).** (FACT, search summaries of the core-lab price lists.)
    - TGen Aug 2026: 25B/300 cycles $25,093.04, 10B/300 $11,307.76, 5B $7,237.52.
    - Harvard FY26, per lane: 25B/300 $2,059 on a Harvard account code, $2,883 on a purchase order. 10B/300 $1,304 per lane. 1.5B/300 $1,616 per lane.
    - UCLA, effective 1 Jul 2026, per lane: 25B $2,164.94 (100 cycles), $3,202.38 (200), $3,512.47 (300).
    - Novogene 2026 promotion: 25B $2,549 per lane; 10B $1,599 per lane for 375 Gb.
    - These add Harvard, UCLA and Novogene to E054 (CWRU, Dana-Farber, UConn, TGen). TGen Aug 2026 at $25,093 for the 25B/300 flow cell fits E054's ~$3.14/Gb.
    - Output per lane and per flow cell were not confirmed. I did not compute $/Gb because lane Gb figures were not fetched.
    - The 35B price and date remain unknown. I found nothing on it.

## Contract term map

| Customer | Term / expiry | Price mechanism | Minimums |
|---|---|---|---|
| Natera | Aug 2033 (10-K); original 2013 | Volume-tiered discount on "Prior Year Spend"; Net Price after Mar 2026; MFN in the Eighth Amendment (survival after the Eleventh unverified) | Prior Year Spend thresholds redacted; no commitment found |
| Guardant | Jan 2033, then one-year renewals (summary) | Not found | 90-day termination for convenience (summary) |
| Caris (Open Offer) | 12 years from 18 Aug 2021 | Inflation-adjusted Volume-Based Net Price cannot rise; 43% cost-per-Gb cut by 2025 | None; 90-day exit |
| Open Offer window | Six years, about Aug 2027 | Universal discount schedules | None |

## Contradictions and stale data

- The task brief assumed MFN may have been replaced in the Eleventh Amendment. The text confirms "Volume-Based Net Price" was deleted. The fetch summary did not find an MFN clause, but fetch summaries can miss clauses, so this is unresolved (E-numbers: none; open gap 2(b)).
- The Open Offer does not "expire" in Aug 2027 in the sense of ending pricing. It is only the signing window. Contracts signed before it run to Aug 2033.
- Caris's date list (accepted 22 Sep 2022) shows the Open Offer applies to labs that signed after the 2021 date. Caris is only a template proxy for Natera.

## Gaps / what I could not find

- Whether the Open Offer's 43% cost-per-Gb commitment was measured or met. Nothing in what I read shows how Illumina or any customer tested it.
- What happens to the Open Offer terms for GRAIL after the spin. The GRAIL Form 10 Ex. 99.1 and 10-K fetches returned no Illumina Supply Agreement terms. A search snippet put the GRAIL–Illumina Supply Agreement initial term at 28 Feb 2027 with auto-renewal of two years. I could not open the source, so treat it as unconfirmed.
- Full text of the Eleventh Amendment MFN question, the Guardant exhibits and pricing, and the Ninth Amendment's term content.
- Q2'26 call text for Guardant, Tempus, GeneDx, BillionToOne, Caris and Exact. No implied cost-per-test change was computed.
- Several SEC and Justia fetches returned only summaries or 403/404 errors, so the quotes above come from summarised pages except where marked as quoted from the exhibit.
