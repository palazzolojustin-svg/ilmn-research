# Agent 63: 63-web-NovaSeq-X-spec-sheets-Gb-per-lane-core-rate-cards-HT-mode-35B-ASHG

*Model: sonnet. Run 2026-10-11 03:41:46. Cost $0.68 (API-equivalent).*

**Assignment:** Resolve the Gb-per-lane question and the $/Gb ladder from primary sources not yet used. (1) Illumina NovaSeq X Series specifications page and datasheet (illumina.com/systems/sequencing-platforms/novaseq-x-plus/specifications.html, the product spec PDF, the reagent kit 'Documentation' pages, and the NovaSeq X Series Control Software release notes after v1.4.0): output per flow cell for 1.5B, 10B, 25B, plus any 5B, 14B, 35B or 'HT mode' entries; reads per flow cell; Q30 percentages; run times; and list prices for the 1.5B, 10B and 25B kits (Illumina store, distributor catalogs such as Fisher, VWR, Cytiva, Genome Technology Access, Cambridge Bioscience, Biocompare). Compute $/Gb at list for each against NovaSeq 6000 S4 (~3,000 Gb at ~$17-18K) and S2, and say what Gb per 25B lane is used. (2) Core-facility rate cards, from archive.org snapshots if live pages are missing: Broad Genomics Platform, Stanford SGTC, Baylor HGSC, HudsonAlpha, Garvan, UMich Advanced Genomics Core, Vanderbilt VANTAGE, Harvard Bauer, Rush, UCLA TCGB, UC Davis, Cold Spring Harbor, Univ. of Minnesota UMGC, Duke GCB, NYU, MD Anderson ATGC: 6000 and X per-lane or per-Gb prices, dated before and after the X, to measure the real price-per-Gb decline that labs pass on. (3) Illumina press releases, ASHG 2026 (20-24 Oct) exhibitor and workshop listings, and trade press (GenomeWeb, 360Dx, Fierce Biotech, Genetic Engineering News, Bio-IT World, BioSpace) from Aug to Oct 2026 for 35B or 14B or 5B flow cell pricing, launch timing, a '$/Gb' claim (e.g. '$2/Gb' or '$80 genome'), early-access sites, and any statement on 6000 end-of-life or service-support end dates (search the NovaSeq 6000 'end of service' or 'discontinuation' notices and distributor letters). Return a table with source, date, URL and the computed $/Gb.

## Key findings

Most of what I checked is already in the ledger. Four items are new or correct a ledger item.

- **Illumina's spec sheet settles Gb per 25B lane (corrects E259 and the open-gaps item 2).** FACT: At 2×150 bp, a 25B flow cell outputs 8–10.5 Tb. At 2×100 it's 5.3–7 Tb and at 2×50 it's 2.6–3.5 Tb. Reads passing filter are 26–35B single-end and 52–70B paired-end. [Illumina NovaSeq X Series Specifications, fetched 2026-10-11, https://www.illumina.com/systems/sequencing-platforms/novaseq-x-plus/specifications.html]
  - The spec page gives no per-lane figure. I divided by the 25B flow cell's 8 lanes, which is my assumption (OPINION). That gives about 1.0–1.3 Tb per lane at 2×150. That fits Novogene's 1,000 Gb and sits just above Rush's 930 Gb.
  - The 750 Gb figure is too low for 300-cycle runs. For 100-cycle or 200-cycle lanes (UCLA sells both), Gb per lane is lower, so $/Gb must use the matching cycle count.
- **$/Gb on cheap core lists (OPINION, calc).** Using ~1,000 Gb per 25B lane at 300 cycles:

| Source | Date | Price per lane | $/Gb |
|---|---|---|---|
| Harvard Bauer, Harvard account code | FY26 | $2,059 | ~$2.06 |
| Harvard Bauer, PO payment | FY26 | $2,883 | ~$2.88 |
| UConn | 2026-01-01 | $2,934 | ~$2.93 |
| TGen | Jul 2026–Mar 2027 | $3,137 | ~$3.14 |
| UCLA | Jul 2026 | $3,512 | ~$3.51 |
| Rush | Jun 2026 | $4,200 | ~$4.20 at 1,000 Gb (4.52 at the stated 930 Gb) |
| Novogene (commercial promo, 2026) | 2026 | $2,549 | ~$2.55 |

  - Sources are the core pages found via search: UConn honeycrisp.core.uconn.edu/products/358, Rush GMCF Pricing June 2026 PDF, bauercore.fas.harvard.edu/fy26-ngs-sequencing, tgen.org price list 08-2026, uclahealth.org TCGB pricing, and web.novogene.com/Website_Sequencing_Savings_Promotion_2026.
  - Most of these lanes are already in the ledger (E054, E259). What's new is the explicit Gb divisor and the spread: the same 25B lane ranges 2x across cores (about $2.06 to $4.52/Gb).
  - Harvard's $2.06 is the low end and appears to be an internal rate (OPINION).
- **Novogene retired the NovaSeq 6000 on a fixed schedule (new).** FACT: Novogene, a large commercial sequencing provider, stopped taking new 6000 quotes on 2024-12-01 and sample submissions on 2025-02-01. Production ended 2025-03-01 and all support ended 2025-06-01. It moved to an "NovaSeq X Plus fleet". [Novogene notice, https://web.novogene.com/Facebook_Phasing_out_NovaSeq_6000]
  - This is outsourced-provider evidence of research-side conversion. It says nothing about regulated clinical labs.
  - It also shows 6000 volume at outsourcers was already gone by mid-2025, so the remaining 41% of HT revenue is mostly in-house clinical and large-lab accounts (OPINION, consistent with E009).
- **The roadmap page confirms E057 and E261 but adds no price.** FACT: The Illumina innovation roadmap lists these items [https://www.illumina.com/systems/sequencing-platforms/novaseq-x-plus/applications/innovation-roadmap.html]:
  - H1 2026: 5B flow cell, and 1.5B 600-cycle flow cell.
  - H2 2026: HT mode, to "increase reads and improve sequencing economics".
  - H1 2027: Q70 duplex and Q50 simplex, 10B going to 14B reads, "40 percent increased yield on 10B", and the 35B flow cell.
  - The 2026-02-23 press release confirms 25B to 35B reads (+40%) and 14B in 20–22 hours, with no pricing. [https://www.illumina.com/company/news-center/press-releases/2026/7b4175f1-a13f-401e-9335-3e5eadbb1fe0.html]
  - The roadmap puts the 35B in H1 2027, so a January 2027 launch would be early. The ex-employee's January hearsay in E058 is not corroborated.
  - A 40% yield uplift on the 10B and 14B reads at similar kit price would cut 10B $/Gb by roughly 29% (OPINION, calc: 1/1.4). That is a second price cut on the mid-tier, separate from the 35B on the 25B.

## Not found

- **Illumina list prices for the 1.5B, 10B and 25B kits.** The Illumina store requires sign-in to show prices (the order page says "Sign in to add to cart or see pricing"). Search snippets showed a TCAG (University of Toronto core) April 2025 list with the 25B 300-cycle kit at $3,470, but I could not open or verify it. Do not use it as list price. The $16,000 snippet already flagged in the ledger is also unverified.
- **Core rate cards for Broad, Stanford, Baylor, HudsonAlpha, Garvan, UMich, Vanderbilt, UMGC, Duke and NYU.** Search returned none. MD Anderson's X page has no prices, only "up to 60% reduction in sequencing price".
- **Aug–Oct 2026 news.** I found no 35B, 14B or 5B pricing, no `$/Gb` claim, no early-access sites, and no ASHG 2026 announcement. A search result about "first shipments of the 25B flow cell" at ASHG is the 2023 event, not 2026.
- **Illumina's end-of-sale/end-of-life policy PDF and the control software release notes after v1.4.0.** The PDFs came back as unreadable binary. No NovaSeq 6000 end-of-service date from Illumina turned up.
- **Blocked pages.** GenomeWeb returned 403. The Harvard FY27 page also returned 403, but the FY27 price ($2,426 per lane) is already in the ledger.
- **Old vs new core rates.** I found no dated before/after-X rate cards beyond those in E051–E053.

## Contradictions and stale data

- E259 and the open-gaps item treat 750, 930 and 1,000 Gb per 25B lane as live options. The spec sheet supports about 1,000–1,300 Gb at 2×150 and rules out 750 for 300-cycle runs.
- Rush's 930 Gb may be a conservative guaranteed or typical yield, while the spec range is the guaranteed band. I did not verify how Rush defines it.
- Roadmap timing for the 35B is H1 2027 (Illumina page). The "January 2027" figure in E058 is hearsay and sits at the very start of that window.

## Table: source, date, URL, computed $/Gb

| Source | Date | URL | Computed $/Gb |
|---|---|---|---|
| Illumina specs (output basis) | fetched 2026-10-11 | illumina.com/systems/sequencing-platforms/novaseq-x-plus/specifications.html | No price on page; ~1.0–1.3 Tb per lane at 2×150 |
| Harvard Bauer FY26 | FY26 | bauercore.fas.harvard.edu/fy26-ngs-sequencing | ~2.06 to ~2.88 |
| UConn | 2026-01-01 | honeycrisp.core.uconn.edu/products/358 | ~2.93 |
| TGen | 2026-08 list | tgen.org | ~3.14 |
| UCLA TCGB | 2026-07-01 | uclahealth.org (TCGB pricing) | ~3.51 |
| Rush GMCF | 2026-06 | rushu.rush.edu GMCF Pricing June 2026 | ~4.20 to ~4.52 |
| Novogene promo | 2026 | web.novogene.com/Website_Sequencing_Savings_Promotion_2026 | ~2.55 |

No S4 or S2 list price was retrieved in this pass, so I did not compute the 6000 comparison.

**Net:** The Gb-per-lane divisor is resolved. Everything else on pricing, launch dates and 6000 end-of-life remains open.
