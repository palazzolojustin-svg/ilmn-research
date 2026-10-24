# Agent 36: 36-web-procurement-catalog-pricing-and-competitor-placements

*Model: sonnet. Run 2026-10-11 02:46:53. Cost $0.47 (API-equivalent).*

**Assignment:** Find primary price and placement evidence for the Jan 2027 35B flow-cell price cut, the NovaSeq X versus competitor cost per Gb, and clinical switching. Sources not yet used: (a) catalogs and quotes from Fisher Scientific, VWR, Cytiva, Genome Technologies, Cambridge Bioscience and Illumina's own store (illumina.com/products) for NovaSeq X 1.5B, 10B, 25B (100, 200, 300-cycle), and any 35B listing, and the NovaSeq 6000 S4 and S2 kits, to compute list $/Gb for each, and the 300-cycle 25B list price to test the '$2.00/Gb' claim; (b) public tenders and awards: UK Contracts Finder and Find a Tender (NHS England Genomic Medicine Service, Genomics England), EU TED, AusTender, NIH RePORTER and NIH S10 instrument grants naming AXELIOS, Element AVITI24 or Ultima UG100, with price paid; (c) Roche, Element, Ultima and PacBio press releases, 8-Ks and investor decks naming clinical or production customers (Macrogen, labs switching from NovaSeq), with placement counts and any stated $/genome, including Roche's Q3 2026 sales release and anything from ASHG 2026 (20-24 Oct) announcements; (d) conference posters and preprints (bioRxiv, medRxiv, ASHG, AMP, ESHG abstracts) from 2025-2026 reporting measured cost per sample and concordance of AXELIOS, AVITI or UG100 versus NovaSeq X for NIPT, MRD, liquid biopsy and exome or genome, including any clinical validation or CAP/CLIA claims; (e) trade press (GenomeWeb, 360Dx, Fierce, STAT, Endpoints) on Illumina price cuts, customer discount negotiations and clinical lab defections.
Quantify: list $/Gb by SKU, the percentage cut versus the NovaSeq 6000, competitor $/Gb and $/genome, and number of named clinical switches. Cite URLs and dates, and mark what is list price versus negotiated. Never invent a price. Hard stop at 20 minutes.

## Key findings

**Result: mostly NO NEW EVIDENCE.** The one useful addition is a catalog-number map for the 25B 300-cycle kit. The '$2.00/Gb' claim (open gap 3) is still untested. The checks ran about 12 minutes, and nothing was fetched from sec.gov or the ASHG/Roche press pages.

- **FACT, new, mapping only.** Illumina's order page lists the NovaSeq X reagent kit catalog numbers. Prices are hidden behind sign-in ("Sign in to add to cart or see pricing"; List Price and Discounts fields are blank). [Illumina order page, fetched 2026-10-11, https://www.illumina.com/systems/sequencing-platforms/novaseq-x-plus/order.html]
  - 1.5B: 20104703 (100c), 20104704 (200c), 20104705 (300c), 20145964 (600c).
  - 5B: 20145965 (100c), 20145966 (200c), 20145967 (300c).
  - 10B: 20085596 (100c), 20085595 (200c), 20085594 (300c).
  - 25B: 20125967 (100c), 20125968 (200c), **20104706 (300c)**.
  - No 35B SKU is listed, which is consistent with E057 and E135.
  - Use these numbers to search Fisher, VWR, Cytiva or Genome Technologies for a reseller price. My general web searches returned none.
- **FACT, confirms E054.** Texas A&M TxGen's price sheet (dated 8 Apr 2025) shows the NovaSeq X 25B 300-cycle flow cell at **$24,951**. [https://www.txgen.tamu.edu/wp-content/uploads/txgen/TxGen_Prices.pdf]
  - This is a core-facility price, not Illumina's list.
  - It equals about $3.1/Gb if the 25B 300-cycle output is ~8,000 Gb. That output figure is my assumption, not read from a page.
  - It matches E054's TxGen value ($3.11), so it adds no new number.
- **FACT, confirms the 25B 100- and 200-cycle lists.** A Vilella recap gives $11,700 (100-cycle) and $14,500 (200-cycle). It says **no 300-cycle price was found** and no new 2×300 NovaSeq X kit was announced. [albertvilella.substack.com, "Everything you need to know from…", https://albertvilella.substack.com/p/everything-you-need-to-know-from, fetched 2026-10-11] The Vilella item is already in the ledger corrections (CORRECTION 29–32).

## Preprints

- **FACT, minor addition to E114/E123.** A bioRxiv preprint dated 13 Mar 2026 from Owkin benchmarked Ultima UG100 against Illumina NovaSeq on FFPE tissue. [https://www.owkin.com/publications/multi-modal-benchmarking-of-the-ultima-ug100-and-illumina-novaseq-sequencing-platforms-using-clinically-relevant-ffpe-tissues]
  - Assays covered: snRNA-seq, whole-transcriptome, exome and genome.
  - It reports "highly comparable results" and a more conservative UG100 variant-calling profile with fewer low-frequency artifacts. Illumina/DRAGEN was more sensitive but noisier.
  - The page showed no cost, no concordance numbers, no NovaSeq model and no CLIA claim.
  - This is research-grade evidence, not a clinical switch.

## Public procurement (UK)

- **FACT, low value.** Find a Tender results showed small Illumina awards only. [Contracts Finder and Find a Tender search results, dates as shown]
  - NHS Grampian genetics reagents award to Illumina Cambridge Ltd: £198,846 (Feb 2026).
  - NovaSeq 6000 maintenance contract: £119,360 (published 11 Feb 2026, term 18 Jan 2026–17 Jan 2027).
  - NovaSeq X Plus system: £1,115,627 (start 20 Mar 2024, end 19 Mar 2025). Whether this price is for the instrument alone is unclear.
  - Nothing named AXELIOS, AVITI or UG100. No $/Gb or consumables award was visible.
  - The ledger (E100) notes Genomics England's £4.67M NovaSeq 6000 extension. The NHS Grampian award and 6000 maintenance contract suggest NHS buyers still service 6000s in 2026. I read only search snippets, so this is weak.

## Competitor placements and clinical switches

- **Named clinical switches found: 0** (AVITI24, UG100 or AXELIOS replacing NovaSeq in production).
- Searches for a Macrogen–AXELIOS order returned only generic launch coverage. Macrogen remains unconfirmed beyond the announcement noted in gap 14.
- Early-access users repeat E124: Foundation Medicine plus sites in the US and Europe. [devdiscourse and eenewseurope launch coverage, Jun 2026]
- A search snippet says AVITI24 is ">35% of new instrument bookings" at Element. I did not open the page, so treat it as unverified.

## Contradictions and stale data

- No contradictions with the ledger. Two caveats:
  - TxGen's April 2025 price may be stale. E054 already shows 25B core prices from $2.50 to $3.30/Gb in 2026.
  - The Illumina order page shows no 35B listing, which supports the H1 2027 window (E057/E135) and nothing sooner.

## Gaps / what I could not find

- The 25B 300-cycle list price: Illumina, Fisher and VWR hide prices, and general web search surfaced no reseller quote. Next step: search the catalog numbers above directly on Fisher, VWR and Genome Technologies, or ask a customer to pull a quote. Cambridge Bioscience and Cytiva were not checked.
- Roche's Q3 sales release (expected late October) and the ASHG 2026 announcements (20–24 Oct) are not yet out.
- Not checked: EU TED, AusTender, NIH RePORTER S10 grants and 8-Ks from Element, Ultima and PacBio. Also not checked: GenomeWeb, 360Dx and Fierce on price-cut or defection stories, AMP/ESHG posters, and AXELIOS clinical-validation preprints. No AXELIOS preprint surfaced in the searches I ran.
