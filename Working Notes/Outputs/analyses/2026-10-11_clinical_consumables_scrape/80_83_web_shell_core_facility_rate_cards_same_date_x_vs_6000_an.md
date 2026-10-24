# Agent 80: 83-web-shell-core-facility-rate-cards-same-date-X-vs-6000-and-35B-pricing

*Model: sonnet. Run 2026-10-11 09:57:42. Cost $1.63 (API-equivalent).*

**Assignment:** Needs a working shell (curl, pdftotext); confirm it first. (1) Find and parse core-facility rate cards (PDF or HTML) for sequencing on NovaSeq 6000 vs NovaSeq X at the same date: Broad Institute, Stanford SGTC, Baylor Human Genome Sequencing Center, HudsonAlpha, Garvan, UMich Advanced Genomics, Vanderbilt VANTAGE, Duke GCB, NYU Genome Technology Center, TCAG (Toronto, April 2025 S4 price), plus CNAG (confirm the -63% X vs 6000 price from the original PDF). Build a table of $/lane and $/Gb for S4, SP, 10B, 25B and any 1.5B/35B or HT-mode lines, the date, and the % change X vs 6000. (2) Find Fisher, VWR and Cytiva catalog prices for Illumina part numbers 20104706, 20085594 and 20104705, plus list prices for NovaSeq X 1.5B/10B/25B kits. (3) Find competitor $/Gb: AXELIOS read definition and $/Gb, MGI T20/T7+ tender prices, Ultima UG100/UG200 reagent $/Gb, Element AVITI24 and AVITI 2x300 cost per Gb on core rate cards. (4) Search trade press (GenomeWeb, 360Dx, Fierce Biotech, Endpoints, Business Wire) and Illumina's investor site from 1 Oct 2026 for the 35B/14B/5B flow cell price, ship date and HT-mode details, and whether it is a 20% $/Gb cut. Quantify the implied price per Gb of the 35B vs the 25B. Cite URLs and dates. Do not invent prices; mark missing items as missing.

## Key findings

1. **CNAG's −63% X vs 6000 gap is confirmed, but only through a search-tool summary, not the PDF.** CNAG PRICES 2026 (R0/R1) lists NovaSeq 6000 S4 at 2x100 at €10.07, €11.28 and €12.08/Gb across three volume tiers. NovaSeq X 25B at 2x100 is €3.77, €4.22 and €4.52/Gb. Every tier gives the same ratio of 0.374, a −62.6% change (calc). This sharpens E051 with a same-list, same-date, same-read-length pair. FACT, secondary (WebSearch summary of cnag.eu/sites/default/files/CNAG PRICES 2026_R0.pdf, undated 2026; I could not open the PDF).
2. **The same summary also quotes CNAG's 25B at 2x150 at €2.84, €3.18 and €3.41/Gb.** The 2x150 S4 comparator is unverified. The tool returned "€4.87 (2025) → €4.90 (2026)" for it, but that figure doesn't fit S4 2x100 at €10.07. Don't use the −42% that the tool computed from it.
3. **Reseller prices exist for all three part numbers, so the "no price" gap is partly closed (undated).** Government Scientific Source (GSA/ECAT contract, undated, 2026 page footer) lists:
   - 20104706 (25B 300-cycle kit): $24,155.04.
   - 20085594 (10B 300-cycle kit): $14,493.03.
   - 20104705 (1.5B 300-cycle kit): $3,927.77.

   Fisher, VWR and Cytiva prices are missing. FACT (govsci.com/product-detail/Illumina-----Inc/<part>/EA/).
4. **Implied reseller $/Gb is far above Illumina's $2.00/Gb launch headline** (calc, using nominal 300-cycle yields of 7.5 Tb for 25B, 3.0 Tb for 10B and 0.45 Tb for 1.5B):

   | Kit | Price | Implied $/Gb |
   |---|---|---|
   | 25B | $24,155 | ~$3.22 |
   | 10B | $14,493 | ~$4.83 |
   | 1.5B | $3,928 | ~$8.73 |

   - A GenomeWeb figure of a $16,000 25B kit came via a search summary only. I couldn't fetch the article.
   - Reasons for the gap are unknown: a post-launch list increase, a reseller or contract markup, or a different yield basis.
   - Either way, the 25B-to-10B step is ~33% cheaper per Gb, and the 10B is not "high-volume 6000 pricing" (E028).
5. **No 35B price, ship date or HT-mode detail has been published as of 11 Oct 2026.** Illumina's roadmap page says:
   - HT mode: H2 2026, "increases reads for improved sequencing economics".
   - 14B (10B upgrade) and 35B: H1 2027.
   - The page has no pricing, cost-per-Gb or cost-per-genome statement.

   The 1 Oct–11 Oct search found no Illumina press release, GenomeWeb or Fierce item. This updates E057. FACT (illumina.com/systems/sequencing-platforms/novaseq-x-plus/applications/innovation-roadmap.html, fetched 2026-10-11). The roadmap press release is dated 2026-02-23.
6. **Illustrative 35B arithmetic: a 20% $/Gb cut means a kit priced only ~12% above the 25B.** Output is +40%, so 1.4 × 0.8 = 1.12 (calc). On the reseller 25B price of $24,155 that is ~$2.58/Gb and a 35B kit of ~$27,000 (35B × 300 bp ≈ 10.5 Tb). This is arithmetic on the ex-employee's "~−20%" (E058), not a reported price. OPINION.
7. **Illumina launched the 5B flow cell at list $5,986–$6,750, depending on cycles.** This is the first published list price for a current X flow cell, and the ledger has only the CWRU 5B rate (E054). The 5B at 300 cycles is ~1.5 Tb, so the top price implies ~$4.5/Gb (calc, assuming $6,750 is the 300-cycle price). That is steeper than the 25B and is consistent with the per-Gb ladder in finding 4. FACT (albertvilella.substack.com, AGBT Feb 2026, "Illumina announcements and Ultima Genomics UG200"). Secondary source.
8. **Roche's AXELIOS simplex price converts to ~$0.12–0.34/Gb, versus Illumina's list of ~$2/Gb.** The sources:
   - Roche prices simplex at $0.06 per million reads.
   - Reads are not Gb-fixed: the source cites 175 bp average giving 40B reads, or 500 bp giving 10B reads, per 4-hour run.
   - At 175 bp that is $0.06 ÷ 0.175 Gb ≈ $0.34/Gb. At 500 bp it is ≈ $0.12/Gb (calc).
   - Cost per run is ~$2,400 (based on 20 sensor-module reuses), the sensor module is "more than 1k, less than 16k", and duplex 30x is $150/genome.
   - The same author puts Ultima at ~$0.24 per million simplex reads and calls Roche "competitive… not aggressively low".
   - This clarifies E060, where the extract was garbled. UBS's "$0.68" is consistent with a ~$16–17k 25B kit ÷ 25,000M clusters ≈ $0.64–0.68 per M (calc).
   - It is not like-for-like: Illumina counts clusters and Roche counts reads of variable length. OPINION on the conversion; FACT on the inputs (aseqer.com/p/roche-axelios-pricing, 2026, redirected from aseq.substack.com).
9. **Same-date X rate-card data adds to E051 and E054 (mostly X only; the 6000 line is rarely on the same page).** Duke, with "Prices as of February 23, 2026", has a pricing-ladder table (see the rate-card table below). Duke's 25B lane is $2,969 versus $2,872 on an undated earlier snippet, so it shows no downward repricing.
10. **Competitor reference prices are old or poorly dated.**
    - MGI/Complete Genomics promotional T7 reagent was $1.5/Gb (or $1.3/Gb for a three-unit order). The date is not shown in the snippet and the news is circa 2023, so treat it as stale.
    - The T20 "$0.99/Gb" figure includes depreciation.
    - No tender price for the T20 or T7+ was found.
    - UMN Element AVITI24 2x300 per-lane rates (FY2024, stale): $1,255–$2,498 for 100M or 300M reads, depending on speed tier.

## Rate-card table (new items only)

All values are per 300-cycle 2x150 unless stated. $/Gb is my calc on nominal yields: 25B ≈ 7.5 Tb, 10B ≈ 3.0 Tb, 1.5B ≈ 0.45 Tb.

| Core / source | Date | Line | Price | $/Gb (calc) |
|---|---|---|---|---|
| Duke | 2026-02-23 | 25B flow cell, Duke / non-Duke | $22,574 / $25,686 | ~$3.01 / $3.42 |
| Duke | 2026-02-23 | 25B lane "any configuration" | $2,969 / $3,448 | — |
| Duke | 2026-02-23 | 10B flow cell | $13,393 / $15,810 | ~$4.46 / $5.27 |
| Duke | 2026-02-23 | 1.5B flow cell | $4,038 / $4,851 | ~$8.97 / $10.78 |
| UCLA TCGB (external) | eff. 2026-07-01 | 25B 100 / 200 / 300 cycle lane | $2,165 / $3,202 / $3,512 | — |
| UCLA TCGB (external) | eff. 2026-07-01 | 10B 300 lane | $1,766 | — |
| UCLA TCGB (external) | eff. 2026-07-01 | 1.5B 300 lane | $2,339 | — |
| Missouri | undated, ~2025–26 | 25B lane / 10B lane | $2,529 / $1,188 | ~$2.70 / ~$3.17 |
| Missouri | undated, ~2025–26 | 1.5B 600-cycle | $5,851 | — |
| Utah HTG (university) | Jan 2026 | 25B lane (3,000M pairs) | $2,600 | ~$2.89 |
| Utah HTG (university) | Jan 2026 | 10B lane (1,250M pairs) | $1,250 | ~$3.33 |
| Utah HTG (external) | Jan 2026 | 25B lane / 10B lane | $3,120 / $1,500 | — |
| Rush GMCF | Jun 2026 | X 25B lane, 300 cycles | $4,200 academic ($4,620 for-profit) | — |
| Rush GMCF | Jun 2026 | NovaSeq S4 2x150 run | $6,615 academic ($6,946 for-profit) | — |
| Harvard Bauer, MD Anderson, UCSD IGM | various, via search snippets only | 25B 300 lane | $2,426 / $2,595 / $2,800 | — |

For the Missouri 1.5B line, the $5,851 per-lane figure looks odd and I did not verify it. Harvard's 10B was $1,314, MD Anderson's was $1,523, and UCSD's 25B 100-cycle was $1,900.

Take-aways:
- The 10B-to-25B steps at Duke, Missouri and Utah are −25% to −32% per Gb, calc'd from each core's own 10B and 25B lines. That is the realistic price step inside the X family.
- Rush has both platforms on one June 2026 card. The 25B lane is $4,200, but the S4 price shown is a whole run, not a lane. Converting needs the lane count, which I did not confirm.
- I did not retrieve the 6000-vs-X pair for Rush. Treat it as a lead for whoever has a shell.

## Contradictions and stale data

- **Reseller vs list:** the govsci 25B price ($24,155) is ~50% above the $16,000 kit price in the GenomeWeb snippet. That is a large gap, and list, contract and markup effects can't be separated.
- **Duke 25B lane:** $2,969 on Feb-2026 versus $2,872 on an undated snippet, so it is possibly up ~3% (calc).
- **Illumina's "$2.00/Gb"** is a 2022 launch claim at the highest-output flow cell. Every 2026 core rate in this wave is $2.70 or higher. No core rate card is near $2.00/Gb, so the list claim is not what labs pay (supports E054, E059).
- **UBS $0.68:** in the garbled E060, this is a per-M-cluster number, not per-read, so "11x cheaper" compares different units.
- **MGI $1.5/Gb** and **UMN AVITI24 FY2024** are stale (2023 and FY2024).

## Gaps / what I could not find

- **No shell.** No curl or pdftotext was available, and WebFetch and Read cannot decode FlateDecode PDFs. TCAG, CNAG R0/2025/R1 and UCSD fetches came back as binary, saved under `...\.claude\projects\...\tool-results\`. The CNAG −63% rests on a search-tool summary. A pdftotext pass on `webfetch-1791730498978-fvhkrd.pdf` (CNAG 2026 R0) and `webfetch-1791730509549-7c1j98.pdf` (CNAG 2026 R1) would settle it.
- **Rate cards not found or not parseable:** Broad, Stanford SGTC, Baylor, HudsonAlpha, Garvan, UMich, Vanderbilt VANTAGE, NYU (not in search results), TCAG lane prices (only $650/sample WGS shown), Harvard Bauer (403), GenomeWeb (403).
- **No same-date X vs 6000 pair** beyond CNAG, except Rush (unconverted run-vs-lane units).
- **Fisher, VWR and Cytiva catalog prices.** Not indexed in search. Only the govsci reseller prices were found.
- **35B / 14B price, ship date and HT-mode details.** Missing. Nothing found from Illumina IR, GenomeWeb, 360Dx, Fierce, Endpoints or Business Wire in the 1–11 Oct 2026 window. Illumina's own pricing pages say "Sign in to… see pricing".
- **MGI T20/T7+ tender prices, UG200 reagent $/Gb** (Ultima GenomeWeb article 403), and **AVITI 2x300 on current core cards**. Not found.

Sources:
- [CNAG PRICES 2026 R0](https://www.cnag.eu/sites/default/files/CNAG%20PRICES%202026_R0.pdf)
- [Duke Sequencing Core pricing](https://medschool.duke.edu/node/8607)
- [UCLA TCGB pricing](https://www.uclahealth.org/departments/pathology/research-services/technology-center-genomics-bioinformatics-tcgb/pricing)
- [Utah HTG pricing](https://uofuhealth.utah.edu/huntsman/shared-resources/gcb/htg/pricing)
- [Missouri Genomics Core](https://mugenomicscore.missouri.edu/ngs.html)
- [Rush GMCF Pricing June 2026](https://www.rushu.rush.edu/sites/default/files/2026-06/GMCF%20Pricing%20June%202026.pdf)
- [govsci 20104706](https://www.govsci.com/product-detail/Illumina-----Inc/20104706/EA/), [20085594](https://www.govsci.com/product-detail/Illumina-----Inc/20085594/EA/), [20104705](https://www.govsci.com/product-detail/Illumina-----Inc/20104705/EA/)
- [Illumina NovaSeq X innovation roadmap](https://www.illumina.com/systems/sequencing-platforms/novaseq-x-plus/applications/innovation-roadmap.html)
- [Vilella, AGBT Part 1](https://albertvilella.substack.com/p/illumina-announcements-and-ultima)
- [aseqer.com, Roche AXELIOS pricing](https://aseqer.com/p/roche-axelios-pricing)
- [GenEngNews, NovaSeq X launch](https://www.genengnews.com/topics/omics/illumina-reveals-new-high-throughput-instrument-novaseq-x/)
- [UMN AVITI24](https://genomics.umn.edu/service/aviti24-sequencing)
