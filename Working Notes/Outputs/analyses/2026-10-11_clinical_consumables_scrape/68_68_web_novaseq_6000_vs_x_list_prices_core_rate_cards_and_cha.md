# Agent 68: 68-web-NovaSeq-6000-vs-X-list-prices-core-rate-cards-and-challenger-price-per-Gb-AXELIOS-U

*Model: sonnet. Run 2026-10-11 03:49:52. Cost $0.50 (API-equivalent).*

**Assignment:** Close open gaps 1 and 2 on $/Gb deflation, which drives thesis question 2. Earlier agents found no 35B price and several rate cards were missing, so use different sources. (1) Core facility rate cards, via archive.org Wayback snapshots where live pages block: Broad Genomics Platform, Stanford SGTC, Baylor GAC, HudsonAlpha, Garvan, UMich Advanced Genomics, Vanderbilt VANTAGE, UMGC, Duke GCB, NYU Genome Technology Center, TCAG Toronto, Novogene and Psomagen service prices. Record the dated price per lane or per Gb for NovaSeq 6000 S4/S2 versus NovaSeq X 10B/25B (and 1.5B), plus any 35B or HT-mode mention. Compute the implied $/Gb ratio of X to 6000 and any change from 2024 to 2026 snapshots. (2) Distributor catalog list prices from Fisher, VWR, Cytiva, Bio-Strategy, Biocompare and Illumina's own part-number pages (for example 20104704, 20083470, 20085594, and 25B 300-cycle kits). Include S4/S2 and X kit list prices. (3) Competitor $/Gb: Roche AXELIOS ($150 per genome, $0.06/M reads) normalized to $/Gb at 2x150 and compared with NovaSeq X 25B at list and at a typical 60-70% discount. Include Ultima UG100 Solaris ($80 genome claim; verify the current figure), Element AVITI24 and AVITI 'Cloudbreak' pricing, and MGI T20/T7+ (published tenders). (4) Trade press, from GenomeWeb or 360Dx via search snippets, Fierce, STAT, Business Wire and Reuters from Sept to Oct 2026, covering the 35B flow cell or 'January 2027' price claims, ASHG launch teasers, Illumina's Q3 preview commentary and sell-side Q3 previews. Quantify the $/Gb ladder (6000 S4, X 10B, X 25B, 35B if any, AXELIOS, UG100, AVITI24, T20) with date and source for each rung, and flag every unverified figure.

## Key findings

Only a few items here are new. No 35B price, no Broad/Stanford/Baylor/HudsonAlpha/Garvan/Vanderbilt/Duke/NYU/TCAG rate card, and no post-11 Oct trade press turned up.

1. **Novogene's 2026 promo is the first commercial-service rung.**
   - It is $2,549 flat per 25B lane (up to 1,000 Gb), or about $2.55/Gb. [FACT; Novogene "Website Sequencing Savings Promotion 2026", valid for quotes to 30 Sep 2026 and samples by 31 Oct 2026; https://web.novogene.com/Website_Sequencing_Savings_Promotion_2026]
   - A 10B lane is $1,549 for up to 375 Gb, or about $4.13/Gb.
   - A full 25B flow cell starts at $19,699, which is $2.46/Gb at 8,000 Gb. That is less than the GSA catalog price of $24,155 for the 300-cycle kit (E234, E054 correction). It supports the view that vendor service pricing sits well below catalog price.
   - The 25B lane is 38% cheaper per Gb than the 10B lane. This adds to E051, where the 10B lane was only 35% cheaper than the S4 (the S4 is not in this document). [calc]
   - The promo is premade-library, Americas only, research use only. Promo pricing is not list. The source gives no S4 price.

2. **UCLA TCGB (effective 1 Jul 2026) publishes 25B prices by cycle length.** [FACT; https://www.uclahealth.org/departments/pathology/research-services/technology-center-genomics-bioinformatics-tcgb/pricing]
   - 100-cycle: $2,164.94 per lane. 200-cycle: $3,202.38. 300-cycle: $3,512.47.
   - E054 and the file 59 correction already hold the $3,512 figure. The new points are the cycle-length gradient and the date.
   - The 100-cycle lane costs 62% of the 300-cycle lane for one third of the cycles. Per-Gb cost therefore rises sharply on short reads. That matters for MRD and CGP labs that run shorter reads.

3. **UT Austin TxGen quotes 25B-300 at $3,222 per lane.** This comes from a search snippet and its date is unknown. [FACT, undated; https://www.txgen.tamu.edu/wp-content/uploads/txgen/TxGen_Prices.pdf] The ledger holds TxGen 2024 at $3.11/Gb, so this is consistent and not an independent rung.

4. **Element's "$2/Gb / $200 genome" claim is stale.**
   - It is a January 2023 throughput-based pricing announcement, subject to volume terms. [FACT; https://www.elementbiosciences.com/news/element-delivers-200-genome-on-aviti-benchtop-sequencing-system]
   - Do not use it as a 2026 rung. The search tool also returned a "$5/Gb, $1/M reads, kit prices fixed for the lifetime of the system" snippet, with no date. [UNVERIFIED]
   - The Element pricing page (www host) lists no figures, only "industry-low sequencing costs and fixed reagent prices". Cloudbreak Freestyle kits are named without prices. [FACT; https://www.elementbiosciences.com/products/aviti/pricing]

5. **UMGC (Minnesota) shows the real AVITI24 service price and the deflation.**
   - On 15 Sep 2025 UMGC finished an AVITI upgrade: output on the 150- and 300-cycle kits rose 50% (300-cycle medium from 500M to 750M reads). [FACT; https://genomics.umn.edu/news/aviti-upgrade-complete]
   - UMGC says AVITI sequencing is "33% less expensive per million reads (or per GB) compared to fiscal year 2025". It says costs are down 62–71% since FY24 and "several hundred to one thousand dollars per billion reads" cheaper than "Illumina's most affordable platform". [MGMT; core-facility statement]
   - UMN rates per lane, 300-cycle (2x150): medium (750M reads) $1,002–$1,503, high (1.5B reads) $1,175–$1,617. [FACT; https://genomics.umn.edu/service/aviti24-sequencing, undated]
   - At 2x150, 750M reads is about 225 Gb, so about $4.5–6.7/Gb. 1.5B reads is about 450 Gb, so about $2.6–3.6/Gb. [calc; assumes read count means read pairs and 2x150, so verify]
   - On these numbers AVITI24 high-output is in the same range as 25B core rates ($2.5–3.3/Gb, E054). It is not clearly cheaper on service rates, but the "62–71% since FY24" claim shows how fast it fell.
   - UMGC does not run its own NovaSeq X Plus and says outsourcing it is "faster and less expensive". No price is published; quotes are on request. [FACT; https://genomics.umn.edu/service/illumina-novaseq-x-plus-sequencing] This is a weak but real read-through that small cores are exiting X ownership for cost reasons.

6. **Berkeley QB3 (rates for work completed after 1 Jun 2026): NovaSeq X lanes run $1,205–$2,990** by flow cell and read configuration. It has no 6000 line in the page I got, and the full rate table was not exposed. [FACT; https://qb3.berkeley.edu/?p=6524] Treat it as a bracket only. The maximum of $2,990 is close to UConn's $2,934 for the 25B-300 lane.

7. **Ultima's price claim is old.**
   - The only per-unit price I could verify is the UG100 launch (Feb 2024): $100 genome, "$1.00 per Gb or $0.30 per million reads". [FACT; Business Wire 2024-02-06, https://www.businesswire.com/news/home/20240206310974/en/ ; quoted via search snippet]
   - UG200 ($850K, $1.25M dual-wafer) and Solaris 2.0 Max (up to 20B reads per wafer, H2 2026) are already in E069. I found no UG200 reagent $/Gb. The "$80 genome" is therefore a marketing figure and its basis is unverified.

## $/Gb ladder (new rungs only)

| Rung | Price | $/Gb | Date and source | Status |
|---|---|---|---|---|
| Novogene 25B lane | $2,549 | 2.55 | promo to 30 Sep 2026 | FACT |
| Novogene 10B lane | $1,549 | 4.13 (at 375 Gb) | same | FACT |
| UCLA 25B-300 lane | $3,512 | about 3.5 at 1,000 Gb | 1 Jul 2026 | FACT, calc |
| UCLA 25B-100 lane | $2,165 | — | same | FACT; Gb not stated |
| AVITI24 high at UMGC | $1,175–1,617 | about 2.6–3.6 | undated | calc, assumptions |
| UG100 | — | 1.00 | Feb 2024 launch | MGMT, stale |
| 6000 S4, 35B, AXELIOS, T20 | not found | — | — | — |

AXELIOS arithmetic: the $150 genome list at 30x (about 100 Gb) is about $1.50/Gb. [calc] This depends on a 30x/100 Gb genome and on Roche's own "$150" claim. A "$0.06/M reads" quote cannot be converted to $/Gb without Roche's read definition; I did not find it. Per E060, UBS compares it with $0.68/M reads for Illumina's 25B. That is not like-for-like.

## Contradictions and stale data
- The search tool repeated the "$16,000 25B-300 list" snippet. The file 59 correction already says to ignore it. It also came with an AI-written statement that Element's "$2/Gb" is current; that is wrong (it dates from 2023).
- The Novogene full-flow-cell price ($19,699) is below the GSA catalog 25B-300 ($24,155, E234). This is a channel gap, not a contradiction.
- UMGC's "Illumina's most affordable platform" is unspecified. It may be the 6000 S4 or the X, so it is not usable as a platform-specific claim.

## Gaps / what I could not find
- archive.org is blocked in this tool ("unable to fetch from web.archive.org"). That is why I have no 2024-vs-2026 snapshot pairs, and so no 2024-to-2026 $/Gb change for any core other than what E053 already holds.
- No rate card found or fetched for Broad, Stanford SGTC, Baylor GAC, HudsonAlpha, Garvan, UMich, Vanderbilt VANTAGE, Duke, NYU, TCAG or Psomagen. Searches returned only UConn, UCLA, TxGen, Salk, Rush, Harvard, TGen and Dana-Farber, which the ledger already holds. Harvard Bauer FY27 returned 403. MD Anderson's page has no prices ("up to 60% reduction" only).
- No Fisher, VWR, Cytiva or Bio-Strategy list prices for part numbers 20104704, 20083470 or 20085594 were found.
- No 6000 S4 or S2 current price found, so no X/6000 ratio can be computed beyond E051.
- No MGI T20 or T7+ tender prices found.
- No GenomeWeb access (403). No Sept–Oct 2026 trade-press item on the 35B flow cell, a "January 2027" price, ASHG teasers or sell-side Q3 previews appeared. So E057 and E058 remain uncorroborated.
- I did not follow the server-supplied redirect for Element's catalog to a different host (242327440.hs-sites-na2.com), so Cloudbreak catalog prices remain unread.
