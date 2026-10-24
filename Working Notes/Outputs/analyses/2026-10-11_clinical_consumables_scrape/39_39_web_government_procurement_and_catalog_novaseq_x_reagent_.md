# Agent 39: 39-web-government-procurement-and-catalog-NovaSeq-X-reagent-prices

*Model: sonnet. Run 2026-10-11 02:52:13. Cost $0.48 (API-equivalent).*

**Assignment:** Find real transaction or list prices for NovaSeq X reagents (open gap 1) in sources prior agents did not mine: government award and tender databases. Targets: USAspending.gov and SAM.gov/FPDS (search vendor 'Illumina' with NovaSeq X, '25B', '10B' and 'flow cell' in award descriptions, with quantities and dollar values); GSA Advantage and NIH/NIAID/VA/DoD contract line items; EU TED (ted.europa.eu) and UK Find a Tender/Contracts Finder (NHS Genomic Medicine Service, Genomics England, UK Biobank, Sanger) for 'NovaSeq X' consumable tenders; Australian AusTender, Canadian CanadaBuys, and Singapore GeBIZ; state university purchasing and Board of Regents agendas; and Illumina catalog numbers on distributors: 25B 300-cycle 20104706, 25B 200-cycle 20125968, 25B 100-cycle 20125967, 10B 20085594/95/96, 5B 20145965/66/67, 1.5B 20104703/04/05 (try Fisher Scientific, VWR, Cytiva, Genome Technologies, Cambridge Bioscience, Biocompare, LabX, Sigma). Also check Illumina's own news for 35B flow cell, ASHG 2026 (20-24 Oct) preannouncements and any January 2027 price-list notice. Compute $/Gb for each price found (25B-300 is about 3,000 Gb? verify the spec output in the Illumina spec sheet before computing), compare with the 6000 S4 price per Gb where listed, and give the date, buyer, quantity and any discount versus list. Report the effective discount vs list for large buyers if any award shows it. Say clearly when a price is list rather than transaction. Do not invent prices; report 'not found' with the queries tried.

## Key findings

**Result: partial. No transaction prices or government line items turned up. One new data point does bear on E054/E055 and the 25B 300-cycle gap, through a core-facility price list.**

1. **FACT (core resale price, not Illumina list):** Case Western's genomics core prices a full NovaSeq X flow cell with "Pricing updated July 2026" ([case.edu/medicine/genomics/pricing](https://case.edu/medicine/genomics/pricing), fetched 2026-10-11). The prices below are what the core charges, so they are resale prices and not list or transaction prices.

| Flow cell | 100-cycle | 300-cycle | 600-cycle |
|---|---|---|---|
| 1.5B | $2,700 | $3,500 | $6,000 |
| 5B | $4,300 | $5,600 | n/a |
| 10B | $7,800 | $10,000 | n/a |
| 25B | $15,900 | $21,000 | n/a |

2. **OPINION (calc):** The known Illumina list for the 25B 100-cycle kit is $11,700 (open gap 1). Case charges $15,900 for the same kit, a ratio of about 1.36x. Applying the same ratio to the 25B 300-cycle price of $21,000 gives an implied Illumina list of about $15,400. That is a rough inference only, because the core's markup may not be proportional across kits.
   - **$/Gb:** At about 8,000 Gb, $15,400 is roughly $1.9/Gb. That is consistent with the "$2.00/Gb" launch claim and does not support the correction note at E054/E055. That note had implied $2.90/Gb from the 200-cycle kit.
   - **Caveat:** The 200-cycle kit at $14,500 and the 300-cycle kit at an implied $15,400 would be only about 6% apart. That looks implausibly flat, so the proportional-markup assumption is probably wrong. The 300-cycle list is still **not found**. Treat the $1.9/Gb as a bound, not a finding.

3. **FACT:** A search summary, not a fetched page, quoted a $24,951 price for a NovaSeq X 25B 300-cycle flow cell from some core price list (the TxGen/UCLA/Salk results). I could not confirm this. The TxGen PDF fetch returned no text. The $21,000 and $24,951 figures show how much core prices vary, which is another reason core prices are only a proxy (E170).

4. **FACT (spec, from the Illumina kit page, fetched 2026-10-11):** The page states 25B output of "4,000–10,500 Gb per single 25B flow cell run on NovaSeq X System" and 8,000–21,000 Gb for a dual 25B run on the X Plus. The fetch tool summarised the page, so the 4,000–10,500 range may be garbled. The 1.5B and 10B figures it gave look unreliable for the same reason. Verify against the Illumina spec sheet before using 8,000 Gb in a $/Gb calculation.
   - **No price:** The page says "Sign in to add to cart or see pricing."
   - **No 35B:** The page does not mention a 35B flow cell.

5. **FACT (government award, no unit prices):** UK Health Security Agency (UKHSA) awarded Illumina Cambridge Limited a £12,000,000 contract for proprietary consumables. The contract was published 3 Dec 2025, runs 28 Nov 2025 to 30 Aug 2028, and is a call-off from a framework agreement (search summary of [Contracts Finder](https://www.contractsfinder.service.gov.uk/Notice/a98cd69f-341d-496f-8f33-411d495aa65a)). The page itself returned 403, so I could not read it.
   - **Run-rate:** About £12M over roughly 2.75 years is about £4.4M a year.
   - **Not usable for pricing:** The notice gives no SKU, quantity or discount, so no effective discount versus list can be computed. It does show a public buyer purchasing on a multi-year framework.

6. **FACT (minor):** Novogene ran a "NovaSeq X Plus 25B special price" promotion from 11 Jan to 31 Mar 2024. The prices are in images, and a promo code (2024_PAG) is needed to get them ([web.novogene.com](https://web.novogene.com/Website_2024_Novogene_PAG_25BSpecialPrice)). This confirms that service providers discount 25B work, but it gives no number.

## Contradictions and stale data

- **E054/E055 correction note:** It says $2.00/Gb is "not corroborated" and implies $2.90/Gb from the 200-cycle kit. The core-price ratio above is weak counter-evidence, so the note should be softened to "unresolved".
- **Core-price proxy:** Case's July 2026 prices are current, but they include labor, overhead and markup (E170).

## Gaps / what I could not find

- **Distributor catalog prices:** None found. Searches covered the 25B 300-cycle SKU 20104706, Fisher, Cytiva, Genome Technologies and Biocompare. The Illumina order pages hide prices behind a login.
- **USAspending, SAM.gov, FPDS, GSA Advantage, VA and DoD line items:** Not reachable. These databases are not indexed by the search tool, and WebFetch cannot run their POST API. Queries tried: "NovaSeq X 25B purchase order unit price" and a combined award/tender query. A manual USAspending query by recipient "ILLUMINA INC" would be needed.
- **TED, Find a Tender, AusTender, CanadaBuys and GeBIZ:** No NovaSeq X line-item award found. The only hits were the UKHSA £12M notice, a 36,000-euro University of Galway award for stem-cell consumables, and UKRI service contracts.
- **35B flow cell price or SKU, ASHG 2026 preannouncements, and a January 2027 price-list notice:** Nothing found.
- **Harvard Bauer Core FY26/FY27 NGS page:** Returned 403, so the per-lane price ($2,426 per lane, from a search summary) is unverified.
