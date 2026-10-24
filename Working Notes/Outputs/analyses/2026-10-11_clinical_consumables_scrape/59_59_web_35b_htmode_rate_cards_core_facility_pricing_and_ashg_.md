# Agent 59: 59-web-35B-HTmode-rate-cards-core-facility-pricing-and-ASHG-AMP-2026-abstracts

*Model: sonnet. Run 2026-10-11 03:37:22. Cost $0.89 (API-equivalent).*

**Assignment:** Aim to build a dated $/Gb price ladder from primary price documents. Use a shell with curl if available, otherwise WebFetch plus the archive.org Wayback (web.archive.org/web/2026*/URL). Do not redo the roadmap-page findings (14B and 35B due H1 2027, with no published price). (1) Core-facility and university rate cards: Harvard Bauer Core FY26, UCLA TCGB (rates dated 1 Jul 2026), Rush genomics core (S4 lane Gb), Broad Genomics Platform, Stanford SGTC, Baylor, Hudson Alpha, Garvan, UMich Advanced Genomics, Dana-Farber MBCF and Vanderbilt VANTAGE. Pull the per-lane or per-flow-cell price for NovaSeq X 1.5B, 10B and 25B, and NovaSeq 6000 S4 and S2 if still listed. Compute $/Gb and the % gap between 6000 and X. Note effective dates and archive snapshots so that price changes over time can be seen. (2) Government pricing: GSA Advantage / GSA schedule 25B-300 price for Illumina, USAspending and SAM.gov awards that name 'NovaSeq X' reagent kits, and Fisher/VWR/Genohub quotes for catalog 20104706. (3) The H2 2026 'HT mode' terms, meaning any Illumina announcement, press release, webinar or support page on higher-throughput modes or run modes for the NovaSeq X. (4) ASHG 2026 (20-24 Oct) program and exhibitor listings, plus Illumina press releases and PR Newswire / Business Wire from 1 Sep to 11 Oct 2026, for any 35B or 14B price, 5-base, constellation or MRD announcements. (5) AMP 2026 and ASHG 2026 abstract listings with 'NovaSeq X' and 'migration', 'validation' or 'comparison', and the bioRxiv 6000 vs 6000Dx exome validation (doi 10.1101/2025.08.19.671033). The goal is any named clinical lab with Gb per sample, cost before and after the move, parallel-run length, revalidation cost, or a stated reason for staying on the 6000. Return a table of source, date, product, $ price, Gb, $/Gb, and URL.

## Key findings

1. **Harvard's Bauer Core raised NovaSeq X prices from FY26 to FY27, mostly on the 25B and 1.5B flow cells.** The 25B-300 lane went from $2,059 to $2,426 (+17.8%) on the Harvard account-code rate. The 1.5B-300 lane went from $1,616 to $2,028 (+25.5%). The 10B-300 lane was nearly flat, $1,304 to $1,314 (+0.8%). FACT. Core rates are a downstream reseller price, but this runs against a steadily falling $/Gb. It fits E064, where Illumina is "sharing" cost increases with customers. A core's pass-through of its own costs could also explain it. [Harvard Bauer Core FY26, https://bauercore.fas.harvard.edu/fy26-ngs-sequencing; FY27, https://bauercore.fas.harvard.edu/fy27-ngs-sequencing; both seen only as search snippets, undated pages, fetch returned 403]
2. **The H2 2026 "HT mode" is now sourced to Illumina's own pages.** The roadmap page says "HT mode increases reads for better sequencing economics" and lists it under "H2 2026". It also promises "enhanced batching flexibility, longer reads, and new high-throughput modes, optimizing flow cell usage to improve read volume." FACT/MGMT. The 23 Feb 2026 press release repeats "enhanced batching flexibility and new high-throughput modes". Neither source gives a price, a read count or an exact date. My reading is that HT mode raises reads per existing flow cell, which would lower $/Gb with no new flow cell. That is OPINION, and it is the likely way a price cut arrives before the 35B in H1 2027. [Illumina roadmap page https://www.illumina.com/systems/sequencing-platforms/novaseq-x-plus/applications/innovation-roadmap.html, undated; press release 2026-02-23 https://www.illumina.com/company/news-center/press-releases/2026/7b4175f1-a13f-401e-9335-3e5eadbb1fe0.html]
3. **UCLA TCGB external rates, "Effective July 1, 2026":** 25B 100/200/300-cycle lanes at $2,164.94 / $3,202.38 / $3,512.47. The page lists 1.5B, 5B, 10B and 25B in 100–600 cycles, ranging $1,210.42–$3,512.47 per lane. It has no NovaSeq 6000 rows, so the 6000 has been dropped from this core's published list. FACT. UCLA's 25B-300 lane is 45% above Harvard's FY26 internal rate. [UCLA Health TCGB pricing, https://www.uclahealth.org/departments/pathology/research-services/technology-center-genomics-bioinformatics-tcgb/pricing, fetched 2026-10-11]
4. **No named clinical lab with a 6000→X migration is found, so ledger gap 6 is unchanged.** The bioRxiv 2025.08.19.671033 paper is a validation at Azienda Ospedaliera Universitaria Senese (Siena, Italy). It compared a research-use 6000 with the CE-IVD 6000Dx on 96 exomes (S2 v1.5, 300 cycles). SNV agreement was 100%, and positive agreement for CNVs was 79% above 150 kb and 91.7% above 900 kb. It does not mention the NovaSeq X, and it gives no cost, parallel-run length or revalidation cost. FACT. It shows that labs in Europe validate on the 6000 for regulatory reasons (the paper says the RUO 6000 lacks the CE-IVD certification needed in Europe) without buying new equipment. That supports E031. [PMC12639258, https://pmc.ncbi.nlm.nih.gov/articles/PMC12639258/, 2025]
5. **Other 2026 core and commercial prices, all FACT from search snippets (not opened):**
   - UConn CGI 25B-300: $2,933.99 per lane, effective 2026-01-01.
   - MD Anderson 25B-300: $2,595 per lane. Its page itself shows no prices, so I could not date this.
   - Novogene Spring 2026 promotion: $2,599 per 25B lane for 1,000 Gb.
   - An academic list (apparently the 08-2026 TGen list): 25B-300 at $25,093.04 per flow cell and 5B-300 at $904.69 per lane.
6. **GSA reseller price for 20104706 (25B-300) is $24,155.04 per flow cell.** That is already in the ledger (the CORRECTION block). I confirmed it on Government Scientific Source, which shows no contract number or date. A separate search put Illumina's list at $16,000, but I did not check that. Note the conflict: the GSA price is above that list and above the CWRU resale price, which shows how far resale prices sit from list.

## Price ladder (new items only)

I computed $/Gb as price ÷ (reads per lane × cycles). The reads per lane are the figures Harvard states: 1B for the 10B, 0.6B for the 1.5B, 2.5B for the 25B. Harvard's 2.5B for the 25B looks low against the nominal 25B ÷ 8 = 3.1B per lane. If the true figure is 3.1B, every 25B $/Gb below falls by about 20%. All figures are nominal Gb, not delivered Gb.

| Source | Date | Product | $ price | Nominal Gb | $/Gb | URL |
|---|---|---|---|---|---|---|
| Harvard Bauer, account code | FY26 | 25B-300 lane | 2,059 | 750 | ~2.75 | bauercore.fas.harvard.edu/fy26-ngs-sequencing |
| Harvard Bauer, PO | FY26 | 25B-300 lane | 2,883 | 750 | ~3.84 | same |
| Harvard Bauer, account code | FY27 | 25B-300 lane | 2,426 | 750 | ~3.23 | bauercore.fas.harvard.edu/fy27-ngs-sequencing |
| Harvard Bauer, PO | FY27 | 25B-300 lane | 3,396 | 750 | ~4.53 | same |
| Harvard Bauer, account code | FY26 | 10B-300 lane | 1,304 | 300 | ~4.35 | fy26 page |
| Harvard Bauer, account code | FY27 | 10B-300 lane | 1,314 | 300 | ~4.38 | fy27 page |
| Harvard Bauer, account code | FY26 / FY27 | 1.5B-300 lane | 1,616 / 2,028 | 180 | ~8.98 / ~11.27 | same |
| UCLA TCGB, external | 2026-07-01 | 25B-300 lane | 3,512.47 | 750 | ~4.68 | uclahealth.org (TCGB pricing) |
| UConn CGI | 2026-01-01 | 25B-300 lane | 2,933.99 | 750 | ~3.91 | honeycrisp.core.uconn.edu/products/358 |
| Government Scientific Source (GSA channel) | 2026 page | 25B-300 flow cell | 24,155.04 | 6,000 (8 lanes × 750) | ~4.03 | govsci.com/product-detail/Illumina-----Inc/20104706/EA/ |

FACT for prices and OPINION for the $/Gb arithmetic. The GSA row uses the same 750 Gb per lane assumption. The ledger's $2.30–3.02/Gb for the GSA price (E054 correction) assumes higher output per lane, so the two disagree. Please decide which output per lane to use before relying on either.

- **10B versus 25B at Harvard FY26 (account code):** the 25B is about 37% cheaper per Gb than the 10B ($2.75 vs $4.35), calc. This is much larger than the ledger's "10B vs S4 only −35%" and supports the "harmonised cost per read" story (E056) only loosely.
- **FY27 narrows the 25B advantage** to about 26% ($3.23 vs $4.38), calc. For this one core, the rate card suggests the 25B discount is shrinking.
- **No NovaSeq 6000 lines were available** in any rate card I could open, so I could not compute a 6000-to-X % gap. UCLA lists no 6000 at all. Harvard and Rush pages were not readable. The 6000 appears to be disappearing from core menus, which is consistent with E053 and my read that cores treat the 6000 as legacy (OPINION).

## Contradictions and stale data

- Harvard's FY27 hike (+17.8% on the 25B) contradicts the ledger's picture of falling per-Gb core prices (E051–E054) and the 5%-ish price decline in the JPM survey (E067). It is a single core's internal cost recovery, not Illumina's list. Treat it as a caution, not a trend.
- The GSA price of $24,155 versus a list of $16,000 (search snippet, unverified) is inconsistent. A reseller price 51% above list needs a source check before use.
- Harvard's "2.5B reads per lane" conflicts with the nominal 25B ÷ 8 = 3.1B. The Gb column in the table inherits this uncertainty.

## Gaps / what I could not find

- **Fetch failures:** Harvard pages returned 403. The Rush June 2026 PDF came back as binary, and I could not read it because no PDF renderer or shell was available. So there is no Rush S4 lane Gb and no 6000 prices from any core. No archive.org snapshots were retrieved, so no price-over-time series exists beyond Harvard FY26→FY27.
- **Not checked:** Broad, Stanford SGTC, Baylor, HudsonAlpha, Garvan, UMich, Dana-Farber, Vanderbilt VANTAGE, Fisher/VWR quotes, Genohub, SAM.gov and USAspending. The tool limits and time left me no way to reach them.
- **No Illumina press release from 1 Sep to 11 Oct 2026** appeared in search, and I found no 35B or 14B price, no ASHG 2026 program or booth listing, and no AMP or ASHG abstract naming a NovaSeq X migration. This is absence in search results, not proof that nothing exists.
- **No dated HT-mode launch** (no software release note, webinar or support page). The v1.4.0 release notes (March 2026) cover the 5B flow cell and staggered starts, not HT mode.

Sources:
- [Harvard Bauer Core FY26](https://bauercore.fas.harvard.edu/fy26-ngs-sequencing)
- [Harvard Bauer Core FY27](https://bauercore.fas.harvard.edu/fy27-ngs-sequencing)
- [UCLA TCGB pricing](https://www.uclahealth.org/departments/pathology/research-services/technology-center-genomics-bioinformatics-tcgb/pricing)
- [Illumina NovaSeq X roadmap](https://www.illumina.com/systems/sequencing-platforms/novaseq-x-plus/applications/innovation-roadmap.html)
- [Illumina press release, 2026-02-23](https://www.illumina.com/company/news-center/press-releases/2026/7b4175f1-a13f-401e-9335-3e5eadbb1fe0.html)
- [Siena validation paper (PMC12639258)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12639258/)
- [Government Scientific Source 20104706](https://www.govsci.com/product-detail/Illumina-----Inc/20104706/EA/)
- [UConn CGI](https://honeycrisp.core.uconn.edu/products/358)
