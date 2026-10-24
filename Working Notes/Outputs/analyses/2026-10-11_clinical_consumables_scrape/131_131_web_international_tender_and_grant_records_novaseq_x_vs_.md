# Agent 131: 131-web-international-tender-and-grant-records-NovaSeq-X-vs-6000-unit-prices-and-Wayback-d

*Model: sonnet. Run 2026-10-11 11:53:03. Cost $0.61 (API-equivalent).*

**Assignment:** Close gaps 7 and 9 via sources not yet tried. Earlier agents covered USAspending, US catalogs and core-facility rate cards. (1) Search public-procurement and grant records that show unit prices or volumes for NovaSeq X and NovaSeq 6000 reagents, instruments and service contracts. Use EU TED (ted.europa.eu), UK Contracts Finder and Find a Tender, AusTender, CanadaBuys, GeBIZ, NHS England and Genomics England procurement notices, Medicaid and state purchasing portals (Cal eProcure, Texas SmartBuy), NIH RePORTER (S10 shared-instrumentation awards naming 'NovaSeq X' or 'NovaSeq 6000' in 2024-26, with award amounts), NSF MRI awards, Wellcome and CIHR/CFI awards, and Japanese or Korean tender sites. For each hit, record the buyer, date, item (flow cell size, kit, instrument), quantity, total or unit price, and derived $/Gb. Compare 6000 S4 with X 25B pricing on the same buyer and date where possible. Also look for 6000 service-contract terms, decommission notices and trade-in credits. (2) Try the Wayback CDX API (web.archive.org/cdx/search/cdx), archive.ph or curl to diff Illumina web pages over 2025-26: the NovaSeq 6000 product page and support/end-of-life notices, the NovaSeq X flow-cell and consumables specs, 'cost per Gb' or 'up to 59% lower' claims, and the investor-relations metrics page. Report added, removed or changed claims with snapshot dates. Quantify price or claim changes and cite URLs. Do not invent numbers; report 'blocked' where a route fails.

## Key findings

Evidence is thin. Procurement records confirm that 6000-to-X replacement is happening and show some instrument and flow-cell totals, but none gives a 6000 S4 versus X 25B price on the same buyer and date. The Wayback route is blocked.

- **FACT, new, Spanish X flow-cell tender:** CIBER (Spain's Biomedical Research Networking Center) published a tender on 2025-07-28 (closed 2025-09-02) for 225 NovaSeq X Plus flow cells (155 + 70) at €2,880,000. That works out to about €12,800 per flow cell if every cell is the same type. The listing doesn't say whether the €2.88M is before VAT, or whether it is a mix of 10B and 25B cells. The listing states the total and quantity only, not a unit price, and no award was shown. [bidsonar.com/contracts/494801-2025](https://bidsonar.com/contracts/494801-2025), [tendios](https://tendios.com/en/tenders/68887815fad99609d94b53ca)
- **OPINION, derived $/Gb:** On Illumina's published X specs, a 25B flow cell yields about 8–10.5 Tb at 2×150 and 5.3–7 Tb at 2×100. If all 225 cells were 25B, €12,800 per cell is roughly €1.2–1.6 per Gb. This is only a bound, because the type is unconfirmed. It does not compare with the 6000 or with any ledger E-number.
- **FACT, new, Danish X Plus instrument:** Region Hovedstaden (Rigshospitalet) tender 24076978 covers a second NovaSeq X Plus for whole-genome work. It is described as extra capacity and backup next to an already-installed unit. The final contract value is DKK 8.5M, roughly $1.2–1.3M. [Publications Office of the EU](https://op.europa.eu/en/web/public-procurement/procurement-details/-/procurement/9887a965-67dc-4ed7-ae61-e7653bef4319)
  - OPINION: this is a clinical buyer adding an X without retiring a 6000. It bears on the parallel-running question Jefferies raised, but it is one data point and the 6000 status isn't stated.
- **FACT, new, NIH S10 award with a 6000 replacement:** UAMS Genomics Core received S10OD036394 ($750,000, 2024-06-15 to 2025-06-14) to buy an X Plus to replace its NovaSeq 6000. The abstract claims sequencing cost falls "by up to ~80%." [HigherGov](https://www.highergov.com/grant/S10OD036394/)
  - MGMT-equivalent: this is the applicant's own claim, not an audited figure.
  - It sits beyond the "more than 60% to 70%" per-Gb decline management cites. Note that UF's ICBR cited "up to 60%" for its own 6000-to-X swap. [UF ICBR](https://biotech.ufl.edu/new-instruments-in-the-icbr-ngs-shared-resource-will-lower-dna-sequencing-costs-for-uf-investigators/)
- **FACT, new, Finnish 6000 upgrade:** The University of Turku (FFGC) tendered an X system with DRAGEN Server v4 on 2024-10-31 to "upgrade the existing Novaseq 6000 sequencer, purchased in 2019." It was funded by the Academy of Finland FIRI 2023. No value was given. [Mercell](https://www.mercell.com/da-dk/udbud/241901667/novaseq-x-sequencing-system-and-illumina-dragen-server-v4-udbud.aspx)
- **FACT, new, Canadian blended contract:** PHSA / BC Cancer Research Institute made a direct award to Illumina Canada (notice published 2023-09-29) for "NovaSeq 6000 and X Plus consumables and reagents." The estimated value was C$4.3M, on a one-year, non-volume-commitment term. Illumina was cited as the sole vendor. The notice treats 6000 and X as one requirement. [CanadaBuys](https://canadabuys.canada.ca/en/tender-opportunities/tender-notice/bcphsa12658)
  - This is older than the 2024–26 window, but it shows non-volume-commitment framework buying.
- **FACT, new, 6000 service contract:** Universitätsklinikum Aachen published a NovaSeq 6000 maintenance contract award with Illumina on 2026-03-10. Value and term are paywalled. It shows hospitals were still buying 6000 service in 2026. [auftragone](https://auftragone.com/en/notices/wartungsvertrag-fuer-ein-novaseq6000-system-firma-illumina)
- **FACT, new, Estonian framework:** The University of Tartu awarded a €1.0M framework (published 2026-03-24, updated 2026-06-22) to Nova natura OÜ for Illumina consumables across iScan, MiSeq, NextSeq 2000 and NovaSeq. Illumina products are being sold through a distributor, and the notice gives no itemised pricing. [bidsfactory](https://bidsfactory.com/en/tenders/illumina-genoomiuuringute-aparatuuri-jooksevvahend-ted-85bd6b66f7807f66)
- **FACT, new, Barcelona sequencing-as-a-service:** Fundació Clínic Barcelona's TED notices 528143-2026 and 536530-2026 (July–August 2026) tender NovaSeq X Plus 25B sequencing services of 12 flow cells at 100 cycles, per search snippets only. The PDFs returned empty, so I have no value or award. Source: search result excerpt of [TED 528143-2026](https://ted.europa.eu/es/notice/528143-2026/pdf).
- **FACT, new, Illumina web claims:** On 2026-10-11 the live NovaSeq 6000 page still shows it as an active product.
  - It lists 6 Tb, 20B single reads and 13–44 hours.
  - It carries no end-of-life or discontinuation notice, no pricing, and only a "Compare with NovaSeq X Series" link. [illumina.com NovaSeq page](https://www.illumina.com/systems/sequencing-platforms/novaseq.html)
  - The X spec page has no cost-per-Gb or "% lower" claim. It assumes more than 120 Gb per 30× genome and about 11.3 Gb per 100× exome. [illumina.com X specs](https://www.illumina.com/systems/sequencing-platforms/novaseq-x-plus/specifications.html)
  - This is a single snapshot, not a diff.

## Routes tried and blocked

- **Wayback CDX API and availability API:** The CDX fetch was refused by the tool. The availability API returned an empty snapshot set for the NovaSeq 6000 page for 2025-01-01. Blocked, so there are no snapshot-date diffs for the 6000 page, X specs, "up to 59% lower" claims or the IR metrics page.
- **UK Contracts Finder:** The 2026-02-11 notice returned HTTP 403.
- **TED PDFs:** 308152-2026, 536530-2026, 528143-2026 and 197476-2025 returned empty or unreadable. They are accessible only through search snippets and a saved binary.
- **NIH RePORTER API:** HTTP 405. Only HigherGov gave an S10 hit.

## Contradictions and stale data

- **E-number correction:** I did not map these to E-numbers, since I could not cite specific ones. The UAMS "~80%" cost claim exceeds the management "more than 60% to 70%" per-Gb decline. It is a grant-writing claim and likely compares list prices on a favourable basis.
- **Stale:** the PHSA notice is 2023, and the UAMS S10 and Turku tender are 2024.

## Gaps / what I could not find

- **Unfound:** no same-buyer 6000 S4 versus X 25B unit prices, no 6000 decommission notices, no trade-in credit terms, and no service-contract prices.
- **Unchecked:** AusTender, GeBIZ, Genomics England, NHS England, Cal eProcure, Texas SmartBuy, NSF MRI, Wellcome and CIHR/CFI, and Japanese or Korean sites. A search for a 6000 S4 tender award surfaced only service-provider price lists. I ran no further targeted searches on these.
- **Next step:** the CIBER notice's technical specification (the flow-cell type and a price schedule) would give a firm per-flow-cell figure. Retrieve it from the Spanish Plataforma de Contratación.
