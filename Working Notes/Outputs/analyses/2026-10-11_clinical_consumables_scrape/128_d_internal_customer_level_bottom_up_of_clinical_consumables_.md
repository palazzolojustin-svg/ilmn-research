# Agent 128: D-internal-customer-level-bottom-up-of-clinical-consumables-and-6000-tail-by-lab

*Model: sonnet. Run 2026-10-11 11:47:45. Cost $0.30 (API-equivalent).*

**Assignment:** Use only the local corpus (Core Notes, INDEX.md, Extracts for ILMN, expert calls, and all clinical customer and peer extracts; prior outputs under Working Notes/Outputs/analyses/2026-10-11_clinical_consumables_scrape may be read for numbers but do not repeat their bridges). Build a customer-by-customer bottom-up of Illumina clinical consumables: for each named clinical customer (Natera, Guardant, Tempus, Caris, GeneDx, BillionToOne, Exact/Abbott, GRAIL, Myriad, NeoGenomics, Veracyte, Labcorp, Quest, Foundation, Adaptive, Personalis and any others in the corpus), compile every disclosed data point: tests per quarter, reported cost of revenue or sequencing cost per test, sequencer counts and platform (6000 vs X), reagent supplier statements, stated 6000-to-X migration status and timing, and expert-call comments on volume commitments or discounts. From these, estimate implied annual Illumina spend per customer (low/base/high with the arithmetic shown) and sum it against Illumina's clinical consumables (>65% of FY25 sequencing consumables of $2,939M; ex-China clinical growth rates in the brief). Output: (1) a table of customers with implied spend, estimated share of Illumina clinical revenue, and estimated % still on 6000; (2) the top-5 and top-10 concentration estimate and what it implies for bargaining power on the 35B flow cell (~20% lower $/Gb); (3) the estimated $ of revenue lost per 10 points of 6000-to-X conversion in the customers with the most remaining 6000 volume, using the 60-70%+ per-Gb price decline claim; (4) where the bottom-up fails to reconcile with management's classification (e.g. the ex-employee's 'very loose' remark) and the size of the unexplained residual. Cite file, date and quote for every data point; mark FACT, MGMT or OPINION; list contradictions and the missing inputs that stop the reconciliation.

## Key findings

**Verdict: the bottom-up cannot be built from the corpus, and I found almost nothing new.** The local corpus has no extracts for Natera, Guardant, Tempus, Caris, GeneDx, BillionToOne, Exact, GRAIL, Myriad, NeoGenomics, Veracyte, Labcorp, Quest, Foundation, Adaptive or Personalis. Their names appear only in Illumina calls, sell-side notes and expert calls. All the customer data points (tests per quarter, cost per test, supply agreements) sit in the ledger under E081 to E094, E109, E110 and E113. They came from web and EDGAR scrapes, not from the corpus.

I checked these:
- The ledger. The gaps file was fully readable; the ledger itself is too large to read in one pass, so I searched it by keyword instead.
- A name search of the Extracts folder (338 hits in 58 files).
- The JPM 2026-07-21 model-update note. It has price targets only and no Illumina spend by customer.
- The ILMN Q1'26 call. A search for customer concentration and largest-customer disclosure returned nothing.
- The ILMN Q2'26 call.
- The Tegus and AlphaSense expert calls.

Two items are new or materially quantify a ledger item:

- **Concentration (OPINION, new wording).** I did not find it in the ledger under these terms. It supports the top-5 and top-10 question qualitatively only, with no dollar figure.
  - A former Illumina associate director said "Illumina's customer base has a very long tail, with the top 10 or 20 customers making up a very large proportion of the business" (Extracts/ILMN/expert_call/Expert_2026-07-23_Former_Associate_Director…Differentiated_S…, 2026-07-23). The same expert called Roche "Top 10, for sure," although they were unsure of that.
  - Another former associate director said clinical revenue comes "very dominantly" from a few large customers. They named BillionToOne, Natera, Guardant and Exact, and said losing top clients "would be a really big impact" (Expert_2026-08-06…Multi-Omics_and_Clinical_Genomics, 2026-08-06).
  - A former Illumina senior manager said the ~20% ex-China clinical growth "is largely driven by big accounts: … Natera, Tempus, Caris and Foundation Medicine." They also said most clinical volume runs as laboratory-developed tests (LDTs) at those large companies (Expert_Tegus_Former_Senior_Manager_Global_Market_Development, undated).
- **The 6000 tail by lab (OPINION; this refines E166, the job-posting evidence).** A Roche precision-medicine lead said NHS-embedded vendor labs (Foundation, Guardant, Natera) "typically have the vendor-recommended instrumentation plus a second Illumina sequencer for CGP and other non-MRD standard-of-care testing" (Expert_2026-07-29_Precision_Medicine…Roche, 2026-07-29). This is hearsay, but it points to parallel instruments at customer sites.

A third item may already be in the ledger as "few 6000". I did not re-check how it is worded there.
- **Parallel 6000 buying (MGMT).** Thaysen said on the Q2'26 call that "some customers bought a few 6000s this quarter to continue operations" (ILMN Q2 2026 call, Jefferies/Peterson answer, 2026-07-30). That bears on the parallel-running question, but the call does not name the customers.

## Why the bottom-up can't be sized

I will not publish implied-spend numbers, because every input would be invented. The reasons:
- **Concentration:** no disclosure of customer spend or concentration appears in the corpus.
- **Share of clinical revenue:** none of the named customers has a disclosed 6000-versus-X split.
- **Revenue at risk per 10 points of conversion:** the share of each customer's volume that is still on the 6000 is unknown. The 17% volume and 41% revenue shares for the 6000 are firm only at the total-HT level. They are not available by customer.

## Contradictions and stale data
- The Natera call expert said the "big four, plus Natera… are just using Illumina" in the US MRD market. The same expert said Natera "uses aspects of Element Biosciences for ctDNA" (Expert_2026-07-22…Natera, 2026-07-22). This is a loose internal inconsistency and sits against E129. It is not resolved.
- Two ex-employee concentration statements ("top 10 or 20" and "very dominantly") are unquantified and cannot be tested against E113's discount tiers.

## Gaps / what I could not find
- Customer-level extracts (10-K, 10-Q, earnings calls) for the named customers.
- Any Illumina disclosure of top-customer revenue share. Illumina's 10-K 10%-customer note is the likeliest source; it is not in the corpus.
- Any customer-level 6000-versus-X install counts.
- Any quantified reconciliation of the "very loose" classification. No extract gives the size of the residual.

**Practical route:** the ledger's customer figures (E081 to E094) plus a public-filing pull of the Natera, Guardant, Tempus and Caris cost-of-revenue and sequencer-count disclosures would let a later wave build the bottom-up. That needs web or EDGAR access.
