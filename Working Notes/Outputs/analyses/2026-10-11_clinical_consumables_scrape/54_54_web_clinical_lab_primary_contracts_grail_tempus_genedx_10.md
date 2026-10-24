# Agent 54: 54-web-clinical-lab-primary-contracts-GRAIL-Tempus-GeneDx-10K-raw-text

*Model: sonnet. Run 2026-10-11 03:32:46. Cost $1.13 (API-equivalent).*

**Assignment:** This agent needs a shell. Fetch the raw 10-K and 10-Q text from EDGAR and grep it. Cover: (a) the GRAIL FY25 10-K and Q2'26 10-Q for the Illumina supply agreement: take-or-pay, price, royalty, term, the 28 Feb 2027 expiry and the ~31 Oct 2026 non-renewal notice date. Also check for any GRAIL 8-K on renewal. (b) The Tempus 10-K: the Illumina naming, the $15.9M payable, and supplier concentration. (c) The GeneDx unnamed 20/13/11% supplier. (d) Where available, the Exact, BillionToOne, Adaptive, Veracyte (multi-year Illumina IVD kit agreement), Myriad and NeoGenomics 10-K text on sequencing supplier concentration, purchase commitments, instrument transitions (NovaSeq 6000 to X), and cost-of-revenue commentary. (e) The Natera 10-K narrative on material suppliers, and why the 2014 First Amendment was refiled as Ex. 10.1 to the Q2'26 10-Q. (f) The Caris raw exhibit, to verify the $4/Gb baseline and the 43% wording and whether the commitment was met. Quantify minimum purchase commitments in $ and years, any price-per-Gb schedules, and any language on Illumina price reductions passed to the lab. Provide verbatim short quotes with the filing URL and accession number. Do not repeat what the ledger already holds. Only add raw-text verification or new filings.

## Key findings

Seven items add to or correct the ledger. The first four matter most. I had no shell, only WebFetch and WebSearch. Several fetches returned truncated pages, and a few answers come from a search tool's reading of a filing, not raw text. Each is labelled.

- **GRAIL's royalty to Illumina resumes on 24 Dec 2026 and is not yet in the ledger.** E257 says only "high single-digit royalty in perpetuity".
  - FACT: The 4th amendment (21 Jun 2024) suspends the royalty "until December 24, 2026 or any earlier change of control of GRAIL… without retroactive effect". The suspension period counts toward the cumulative $1B of royalties that triggers a cut to 5%.
  - FACT: The rate is 9%, with anti-stacking down to a 7% floor. "After we have cumulatively paid Illumina royalties totaling $1 billion, the royalty rate will be reduced to 5%".
  - FACT: The source is GRAIL's Q2'26 10-Q (0001628280-26-054307), fetched as text.
  - OPINION: Royalty income is not consumables, but it starts in Q4'26 and is a possible Illumina guidance tailwind. Check whether the 2027 guide includes it.
- **No GRAIL 8-K on the supply agreement renewal exists through 5 Aug 2026.** The EDGAR list shows only earnings, vote and officer-change 8-Ks: 12 Jan, 19 Feb, 5 May, 1 Jun, 22 Jun and 5 Aug 2026. The non-renewal notice date of about 31 Oct 2026 is still open. Check for a 10-Q or 8-K around 5 Nov 2026.
- **Caris: the $4/Gb baseline and the 43% wording are verified in the raw exhibit.** The ledger had these as unverified. Source: Caris S-1 Ex. 10.2(A), https://www.sec.gov/Archives/edgar/data/2019410/000110465925052381/tm2415719d15_ex10-2a.htm (accession 0001104659-25-052381). The tool's summary quotes the exhibit this way:
  - Baseline: "$4, using a NovaSeq instrument with an S4 300 flow cell" at the highest volume tier.
  - Commitment: by 2025 the per-Gb price is "at least 43% lower than the inflation-adjusted… per gigabase", with a worked example of $4 falling to a maximum of $2.26.
  - Whether the commitment was met is still not disclosed.
- **Caris has no purchase commitment and can leave on 90 days' notice.**
  - FACT: Exhibit: "This Supply Agreement is not contingent on any purchase commitments by Customer."
  - FACT: FY25 10-K (search-tool paraphrase, not read raw): no minimum purchase requirement, "volume discounts and other promotions", a right to terminate "at any time and for any reason without termination liability upon 90 days' prior written notice", and "irrevocable by Illumina until… August 2033". The 10-K is at https://www.sec.gov/Archives/edgar/data/2019410/000201941026000016/cai-20251231.htm.
  - OPINION: This corroborates E110 for Guardant and E202 on the absence of lock-in.
- **The Caris exhibit carries a pass-through of better pricing.** FACT (tool summary, wording not quoted verbatim): if GRAIL or an equivalent customer gets better pricing, Caris receives the matching rate "within 45 days… with retroactive refunds for previously invoiced units" (Section 5.e–f). The exhibit also gives Caris pricing no less favorable than GRAIL's. So GRAIL's 2024–27 supply pricing may set a floor on what Illumina can charge Caris.
- **Natera's 10-K narrative now supports August 2033.** FACT (search-tool paraphrase of the 10-K): Illumina is "the sole supplier of sequencers and related reagents for Panorama, Horizon, Signatera and Prospera… pursuant to a supply agreement that expires in August 2033". The filing is https://www.sec.gov/Archives/edgar/data/1604821/000110465926020881/ntra-20251231x10k.htm (accession 0001104659-26-020881). This partly closes the gap in the ledger's correction on E109. It is still not read raw.
- **Natera's Q2'26 10-Q is a bulk refiling of the full 2013–2016 amendment chain, not only the 2014 First Amendment.** The accession is 0001628280-26-054525. The filing gives no stated reason, so the "why" below is inference.
  - Ex. 10.1: First Amendment (18 Sep 2014).
  - Ex. 10.2: Second Amendment (23 Sep 2015), updating the Exhibit B pricing schedules. It has tiered discounts on cumulative consumables spend and exclusivity tied to NIPT.
  - Ex. 10.3: Third Amendment (June 2016).
  - Ex. 10.4: Fourth Amendment.
  - OPINION: The Third Amendment's term ("ten (10) years after the Third Amendment Date") ran out around June 2026, which is the likely trigger for refiling, probably to complete or correct the exhibit record. This is unconfirmed.
- **Natera's Third Amendment (2016) reveals Illumina participation in Natera's test revenue.** FACT: it grants "additional rights in Clinical Oncology Testing", non-exclusive. Redacted terms include a "revenue share" of "kit revenue and… subject test revenue" and regulatory milestones. A minimum applies to temporary consumables, where unit orders are subject to a redacted minimum per purchase order. Illumina's economics therefore include something beyond $/Gb for Signatera-type tests. The size is redacted.
- **Natera's 2014 First Amendment confirms the short binding-forecast mechanism.** It also shows a three-year original term. The ledger correction already covers the binding forecast and ±25% variance. Add the verbatim quote: "The 4th calendar month of each Forecast… is a binding commitment by Customer to take receipt of and pay for" the quantity, with variance of "up to +/-25%".
- **GeneDx's unnamed supplier remains unnamed.**
  - FACT (search-tool paraphrase): FY25 10-K (https://www.sec.gov/Archives/edgar/data/1818331/000181833126000015/wgs-20251231.htm) says one supplier was about 20%, 13% and 11% of purchases in 2025, 2024 and 2023. A second supplier was about 10% and 11% in 2024 and 2023.
  - FACT: Illumina is listed among the key suppliers, along with Life Technologies, Twist, Path-Tec and Agilent.
  - FACT: "changing suppliers would be time-consuming, costly, and might necessitate revalidation of tests".
  - OPINION: The 20% supplier is plausibly Illumina, since the share rose from 11% to 20% as exome and genome volume grew. This is an inference, not a disclosure.

## GRAIL

- FACT (10-K FY25, accession 0001628280-26-017319, https://www.sec.gov/Archives/edgar/data/1699031/000162828026017319/gral-20251231.htm): the initial term expires 28 Feb 2027. It auto-renews for two-year terms unless either party gives written notice at least 120 days before the end of the term. This is the same search-tool text as E257; the fetch tool returned only fragments of the body.
- FACT: GRAIL "rel[ies] on Illumina, Inc. as a sole supplier for our next-generation sequencers and associated reagents".
- Not found: any take-or-pay, minimum purchase or $/Gb price in the 10-K text I could reach. The 2023 and 2024 amendments redact numbers as "[***]".
- Source for the amendment history and the 5% step-down is GRAIL's FY24 10-K (https://www.sec.gov/Archives/edgar/data/1699031/000169903125000041/gral-20241231.htm). I did not open it.

## Tempus

- The search tool repeats the claim that Illumina was ~33% of vendor payments in 2025, with $15.9M due at 31 Dec 2025 and Illumina "the sole supplier of sequencers and… maintenance and repair services". The raw fetch of the 10-K did not surface the passage, and the ledger correction (note R14) says R14 does not name Illumina. Treat the Illumina attribution and the $15.9M as still unverified. This is a conflict between two retrieval methods, not a resolution.

## BillionToOne, Veracyte and others

- BillionToOne FY25 10-K (accession 0002070849-26-000017): the fetched excerpt had no Illumina mention. Its single-molecule NGS (smNGS) platform may reduce Illumina dependence, but this is not confirmed.
- Veracyte: only 2023 press coverage was found (multi-year IVD agreement on NextSeq 550Dx for Prosigna and Percepta). No NovaSeq purchase terms exist in what I retrieved. This is not a high-throughput consumables exposure.

## Contradictions and stale data

- E257 and the gaps file treat the GRAIL royalty as a flat perpetual obligation. It is suspended until 24 Dec 2026.
- The Natera Aug 2033 date is now supported by a 10-K paraphrase, but the 2016 Third Amendment's own term ended around June 2026. The extension amendments (Fifth to Eleventh) are the actual source, so keep the date as 10-K-derived.
- The Tempus attribution is contradicted between the search snippet and the raw R14 note (see above).

## Gaps / what I could not find

- I did not retrieve the raw Item 1A, Item 7 and notes text of the GRAIL 10-K or the Tempus 10-K. The fetch tool truncates long filings, so no true grep was possible.
- Not covered: the Exact, Adaptive, Myriad and NeoGenomics 10-K text; the Veracyte 10-K; any Caris statement on whether the 43% commitment was met; and the Natera 10-K contractual-obligations note (the $11.6M item remains unchecked).
- A shell with curl and grep is still needed for the full-text greps this assignment called for.

Sources:
- [GRAIL Q2'26 10-Q](https://www.sec.gov/Archives/edgar/data/0001699031/000162828026054307/gral-20260630.htm)
- [GRAIL FY25 10-K](https://www.sec.gov/Archives/edgar/data/1699031/000162828026017319/gral-20251231.htm)
- [Caris S-1 Ex. 10.2(A)](https://www.sec.gov/Archives/edgar/data/2019410/000110465925052381/tm2415719d15_ex10-2a.htm)
- [Caris FY25 10-K](https://www.sec.gov/Archives/edgar/data/2019410/000201941026000016/cai-20251231.htm)
- [Natera Q2'26 10-Q Ex. 10.1](https://www.sec.gov/Archives/edgar/data/0001604821/000162828026054525/ntra-20260630xex101.htm)
- [Natera Q2'26 10-Q Ex. 10.2](https://www.sec.gov/Archives/edgar/data/0001604821/000162828026054525/ntra-20260630xex102.htm)
- [Natera Q2'26 10-Q Ex. 10.3](https://www.sec.gov/Archives/edgar/data/0001604821/000162828026054525/ntra-20260630xex103.htm)
- [Natera Q2'26 10-Q Ex. 10.4](https://www.sec.gov/Archives/edgar/data/0001604821/000162828026054525/ntra-20260630xex104.htm)
- [Natera FY25 10-K](https://www.sec.gov/Archives/edgar/data/1604821/000110465926020881/ntra-20251231x10k.htm)
- [GeneDx FY25 10-K](https://www.sec.gov/Archives/edgar/data/1818331/000181833126000015/wgs-20251231.htm)
- [Tempus FY25 10-K](https://www.sec.gov/Archives/edgar/data/1717115/000119312526066961/tem-20251231.htm)
