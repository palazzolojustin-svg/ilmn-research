# Agent 11: Pricing data: NovaSeq 6000 vs NovaSeq X price per Gb

*Model: sonnet. Run 2026-10-11 02:06:13. Cost $1.64 (API-equivalent).*

**Assignment:** Find public price data to quantify the per-Gb price decline from NovaSeq 6000 to NovaSeq X: (1) university/core-facility sequencing price lists (e.g. per-lane or per-flow-cell prices for NovaSeq 6000 S1/S2/S4 vs NovaSeq X 1.5B/10B/25B; many cores publish these, including internal vs external rates, and some show both platforms side by side or year over year); (2) Illumina list prices or quoted reagent kit prices for S4 300-cycle vs 10B/25B 300-cycle and their output in Gb; (3) commercial service providers' price per genome/Gb on each platform; (4) any 2026 price changes and the 35B flow cell. Compute $/Gb for each platform/flow cell and the implied decline (old vs new), noting dates, internal vs external rates and that core prices include labor/overhead. Aim for at least 10 distinct price points with URLs, and summarize the median decline.

## Key findings

1. **Core facilities show about a 50–60% drop in $/Gb from NovaSeq 6000 S4 to NovaSeq X 25B.**
   - The median across public price points is about 53% (S4 about $6.66/Gb vs 25B about $3.11/Gb).
   - The cleanest same-list comparison, Salk (external nonprofit, rates effective 07/01/25), shows -60%.
   - Illumina's own list-price claim is 59% (see item 11). OPINION, computed from the sources below.
2. **The 10B flow cell is only about 35% cheaper per Gb than S4.** At Salk, S4-300 is $13.23/Gb and 10B-300 is $8.61/Gb, a 35% decline. The 10B delivers roughly S4-sized output (about 3 Tb), so the 10B is the "like-for-like" replacement and the 25B is where the large decline comes from. OPINION.
3. **At Salk, a 25B flow cell costs more per flow cell than an S4.** The 25B-300 is $42,560 vs $39,701 for the S4-300, a 7% premium for about 2.7x the nominal Gb. So the per-Gb decline is a volume effect: customers who buy the same dollars of flow cells get far more data. FACT, computed from the Salk list. This is why volume growth has to run well ahead of 1/(1-decline) for revenue to hold.
4. **The 6000's S1 and S2 flow cells are far more expensive per Gb than the S4.** At Salk, S1-300 is about $29/Gb and S2-300 about $25/Gb. A lab moving from those to a 25B sees a 78–82% decline. This is probably why management's "easily more than 60% to 70%" is higher than the S4-to-25B core-facility figure. OPINION.
5. **Illumina's reported mix data implies a roughly 70% revenue-per-Gb decline.** Using the known Q2'26 shares:
   - The 6000 earns (41%/17%) = 2.41 units of revenue per unit of volume.
   - The X earns (59%/83%) = 0.71.
   - That is a 3.4x ratio, so blended X revenue per Gb is about 70% below the 6000's.
   - This matches management's claim and is steeper than the S4-only list-price view. Derived from the user's known facts; OPINION.
6. **Prices have kept falling on both platforms.**
   - Salk's S4-200 external rate was $43,586/flow cell on an older, undated list and is $36,708 on the 07/01/25 list (-16%).
   - Salk's S4-300 was $52,098 on the older list and is $39,701 now (-24%).
   - Dartmouth's FY2027 internal S4-300 is only $11,743 (about $3.91/Gb).
   - So the 6000 is also being repriced, which cuts the "old" revenue base even before conversion. FACT on the numbers; the cause is OPINION.
7. **Core 25B prices are about $2.6–3.3/Gb at the cheaper end (2024–2026 lists).** These include some overhead:
   - CWRU, July 2026: $2.63
   - Dana-Farber, undated: $2.50–2.88
   - UConn, 2026: $2.94
   - TxGen, 2024: $3.11
   - TGen, Aug 2026: $3.14
   - Illumina's list is $2.00/Gb.
8. **The 5B flow cell is new and priced near the 10B.** It appears on core lists from July 2026 (CWRU: $5,600 for 300 cycles, about $3.20/Gb at 1.75 Tb).
9. **Illumina has "harmonised" cost per read across the 10B and 25B flow cells.** Sequencing is now bought in 600M-read-pair units: 5B lane = 1, 10B lane = 2, 25B lane = 5. This is a pricing-structure change in late 2025, with no figures disclosed. MGMT, relayed by NGI Sweden (2025-11-17, https://ngisweden.scilifelab.se/?p=11245).
10. **The 35B price has not been published.**
    - A former Illumina associate director (left July 2025) said the cost per Gb "may drop to about $2 flat" from about $2.50 with the 35B, roughly 20% (Expert call, 2026-07-23, Extracts/ILMN/expert_call/Expert_2026-07-23_Former_Associate_Director_at_Illumina_Inc...md). They said it is "definitely" a price decrease.
    - The Q1'26 call lists new 14B and 35B flow cells on the 18-month X road map (ILMN_2026Q1_Earnings_Call.md).
    - I found no public 35B price and no 35B on Illumina's spec page.
11. **Illumina's own list claim.** "Up to 59%" lower cost per Gb vs the 6000 S4, at a list price of $2.00/Gb (about $200 per 100 Gb genome, consumables only). This implies a list S4 of about $4.9/Gb. MGMT. Source: Illumina X post (from the 2022 launch), https://x.com/illumina/status/1575521223664193541; Illumina page https://www.illumina.com/systems/sequencing-platforms/novaseq-x-plus/applications/broad-sequencing.html
12. **I could not read any Illumina list price for the reagent kits.** Illumina hides them behind login (https://www.illumina.com/products/by-type/sequencing-kits/cluster-gen-sequencing-reagents/novaseq-x-series-reagent-kits.html). Core prices are therefore a proxy, and they include labor, overhead, QC, shipping and tariff surcharges.

## Method and assumptions

- **Output per flow cell.** 25B is 8,000 Gb at 2x150, the low end of Illumina's 8–10.5 Tb spec (https://www.illumina.com/systems/sequencing-platforms/novaseq-x-plus/specifications.html). 10B is 3,000 Gb (spec 3–4 Tb). 1.5B is 500 Gb (spec 500–716 Gb). 5B is about 1,750 Gb (spec 1.5–2 Tb).
- **6000 outputs are my assumptions, not sourced.** S4 is about 3,000 Gb, S2 about 1,000 Gb and S1 about 500 Gb. I also used 800 Gb per S4 lane and 1,000 Gb per 25B lane, per a search-result snippet comparing the two.
- **Using the top of the spec ranges lowers the X $/Gb further.**
- **These are service prices, not Illumina's reagent revenue.** They include labor, margin, QC and shipping. They are a proxy for relative price, not for Illumina's net revenue per Gb.
- **Rates differ by customer type.** Internal rates are typically 35–50% below external ones.

## Price points ($/Gb computed by me)

### NovaSeq 6000 (the old base)

| # | Source and date | Rate type | Price | $/Gb |
|---|---|---|---|---|
| 1 | Salk, 07/01/25: S4-300 | External nonprofit | $39,701/FC ($49,626 for-profit) | $13.23 ($16.54) |
| 2 | Salk, 07/01/25: S2-300 | External nonprofit | $24,938 | $24.9 |
| 3 | Salk, 07/01/25: S1-300 | External nonprofit | $14,564 | $29.1 |
| 4 | Salk, older undated list: S4-300 | External nonprofit | $52,098 | $17.4 |
| 5 | UConn CGI, Jan 2025: S4-300 reagent kit | Internal | $16,578, plus 6.5% shipping and a $490 run fee | $5.53 reagents only; about $6.05 all-in |
| 6 | UNMC, eff. 7/1/2023: S4-300 | Internal / external | $18,957 / $28,436 | $6.32 / $9.48 |
| 7 | Calgary CHGI, June 2024: S4 lane, PE150 | Internal; CAD assumed | $5,600/lane | $7.00 (at 800 Gb/lane) |
| 8 | Michigan State, 19 Jul 2023: S4 2x150 lane | Not stated | $5,953/lane | $7.44 |
| 9 | Dartmouth GMBSR, FY2027: S4-300 and S2-300 | Internal | $11,743 and $7,922 | $3.91 and $7.92 |

Sources:
- 1–4: https://www.salk.edu/science/core-facilities/integrative-genomics-and-bioinformatics-core/scheduling-and-rates/ (row 4 from a search-result snippet, https://salk.edu/science/core-facilities/omics/scheduling-and-rates)
- 5: https://draft.genome.center.uconn.edu/cgi_service_rates
- 6: https://www.unmc.edu/vcr/cores/vcr-cores/genomics/pricing.html (search snippet)
- 7: https://cumming.ucalgary.ca/sites/default/files/teams/97/CHGI%20Internal%20Price%20List%20June%202024.pdf (search snippet; the PDF was unreadable)
- 8: https://rtsf.natsci.msu.edu/_assets/files/genomics/NovaSeq%206000%20Sequencing%20Available%20by%20the%20Lane_19July2023.pdf (search snippet; page later 404)
- 9: https://geiselmed.dartmouth.edu/gsr/sequencing/

### NovaSeq X

| # | Source and date | Rate type | Price | $/Gb |
|---|---|---|---|---|
| 10 | Salk, 07/01/25: 25B-300 | External nonprofit | $42,560/FC ($53,200 for-profit) | $5.32 ($6.65) |
| 11 | Salk, 07/01/25: 10B-300 | External nonprofit | $25,840 | $8.61 |
| 12 | Salk, 07/01/25: 1.5B-300 | External nonprofit | $6,080 | $12.2 |
| 13 | UConn, 2026: 25B-300 (eff. Jan–Dec 2026) | Single rate, includes QC, shipping and 5% tariff | $2,937/lane (about $23,493/FC) | $2.94 |
| 14 | UConn, Jul–Dec 2025: 25B-300 | Single rate | $2,924/lane | $2.92 |
| 15 | Calgary, June 2024 and 2025: 25B lane, PE150 | Internal; CAD assumed | $4,100/lane | $4.10 |
| 16 | TxGen (Texas A&M), May 2024: 25B-300 | Not stated | $3,028/lane | $3.11, as stated by TxGen at 975 Gb/lane |
| 17 | TGen, Aug 2026: 25B-300 and 10B-300 | Academic | $3,137/lane and $1,413/lane | $3.14 and $3.77 (10B lane at 375 Gb) |
| 18 | CWRU, July 2026: 25B / 10B / 5B / 1.5B, 300 cycles | Affiliates and nonprofits | $21,000 / $10,000 / $5,600 / $3,500 | $2.63 / $3.33 / $3.20 / $7.00 |
| 19 | Dana-Farber MBCF, undated: 25B-300, 10B-300 | Internal to external | $20,000–23,000; up to $14,000 | $2.50–2.88; up to $4.67 |
| 20 | UW-Madison, undated: 10B lane | Not stated | $2,050/lane | $5.47 (at 375 Gb) |
| 21 | Novogene | Commercial | WGS $849/sample, 30x | Not a $/Gb figure |

Sources:
- 10–12: Salk page above.
- 13–14: https://honeycrisp.core.uconn.edu/products/358; the 2025 figure is from a search snippet.
- 15: Calgary PDFs (search snippets only).
- 16: https://www.txgen.tamu.edu/wp-content/uploads/2024/04/TxGen_Prices_v12_2024_05_04_v3.pdf (search snippet; PDF unreadable)
- 17: https://www.tgen.org/media/x2dmuqf1/tgen_csc_academic_price_list_08-2026.pdf (search snippet; PDF unreadable)
- 18: https://case.edu/medicine/genomics/pricing
- 19: https://mbcf.dana-farber.org/pricing
- 20: https://cgsi.wisc.edu/bio-tech-update-sequencings-best-bang-for-the-buck/ (a "30% cheaper" 10B claim)
- 21: Novogene site, via search summary only.

### Implied declines (S4 to 25B)

| Pairing | S4 $/Gb | 25B $/Gb | Decline | Comment |
|---|---|---|---|---|
| Salk, same list, same rate class | 13.23 | 5.32 | -60% | Best like-for-like |
| Salk S4 to 10B | 13.23 | 8.61 | -35% | |
| Salk S2 to 25B | 24.9 | 5.32 | -79% | |
| Salk S1 to 25B | 29.1 | 5.32 | -82% | |
| UConn, all-in (2025 to 2026) | 6.05 | 2.94 | -51% | Different dates |
| UConn, reagent only vs 2026 all-in | 5.53 | 2.94 | -47% | |
| Calgary, June 2024, same list | 7.00 | 4.10 | -41% | |
| Median of S4 points (9) vs median of 25B points | 6.66 | 3.11 | -53% | Unpaired, mixed rate types |

- The S4 median uses 3.91, 6.05, 6.32, 7.00, 7.44 and 13.23. Only the first five S4 points are internal-ish.
- The 25B median uses 2.63, 2.69, 2.94, 3.11, 3.14, 4.10 and 5.32.

**Summary.** Paired comparisons give -41% to -60%, with a median of -51%. The unpaired median is -53%. The 10B is only about -35% against S4. Illumina claims 59%.

## Reading this against the thesis

- **S4 customers see a -41% to -60% decline.** That is below management's "more than 60% to 70%". S1/S2 and shared-lane customers see -75% to -85%. The reported mix math gives about -70%. OPINION.
- **Volume growth needed to hold revenue flat.**
  - At -53%, volume must rise about 2.1x.
  - At -60%, it must rise 2.5x.
  - At -70%, it must rise 3.3x.
  - This is simple arithmetic, not a forecast.
- **The "easy" conversions are done.** Conversion has been concentrated in the 25B and 10B flow cells. The remaining 6000 base is probably the S4 and S2 users and the less price-sensitive ones. OPINION.
- **Price floors are falling.** On cheaper lists, the 25B sits at $2.5–3.1/Gb. Further cuts from 35B (about -20%, an expert estimate) would take list to about $2/Gb or lower. The 5B flow cell sits at about $3.2/Gb, so low-volume labs also get cheaper per-Gb access. OPINION.

## Contradictions and stale data

- **Salk S4 prices.** Search snippets cited $43,586 for S4-200 and $52,098 for S4-300 (and a "$54,482 external" figure), while the live 07/01/25 page shows $36,708 and $39,701 external nonprofit. I treated the live page as current. The old list's date is unknown, so the "6000 price cut" signal is only suggestive.
- **Genohub.** It lists 25B at 16,000 Gb, 10B at 6,000 Gb and 1.5B at 1,000 Gb, which is about double Illumina's spec (single-read counting). It shows $2.00/Gb for 25B (https://genohub.com/ngs-sequencer/3/illumina-novaseq-x-plus). I did not use its Gb.
- **Per-lane yields.** One snippet said 25B gives 1,000 Gb/lane and S4 800 Gb/lane. TxGen says 975 Gb. The University of Minnesota page says 750 Gb per 25B lane (https://genomics.umn.edu/service/illumina-novaseq-x-plus-sequencing). That lowers realized yield by about 25% and would raise X $/Gb accordingly.
- **CWRU.** A search summary mentioned "32B" flow cells, but the page I fetched listed no 32B. Treat as unverified.
- **5B timing.** NGI Sweden (Nov 2025) said 5B was due "early 2026". CWRU shows it available from July 2026.
- **Dartmouth.** FY2027 internal S4 at $3.91/Gb is far below other 6000 points and close to X pricing. It may be a reagent-at-cost internal rate or a very low contract price. Treat it as an outlier.
- **Dates.** Several lists are undated (Dana-Farber, UW-Madison). MSU's 2023 sheet and UNMC's July 2023 prices are two or more years old.

## Gaps / what I could not find

- **Illumina list prices** for S4 vs 10B/25B/35B kits, and a 35B price. Illumina's site hides prices behind login, and no 35B price was published. Roche/Illumina press material did not give $ per kit either.
- **Readable PDFs.** TGen, TxGen, Calgary, Weill Cornell, Northwestern, CNAG and TCAG price lists came back as binary. TGen, TxGen and Calgary figures come from search snippets only. Weill Cornell FY2027 (https://research.weill.cornell.edu/sites/default/files/full_price_list_wcm_genomics_core_fy2027.pdf), Northwestern, CNAG and TCAG would add paired data. Please re-pull them with a PDF tool.
- **Same-institution, same-year 6000-vs-X pairs.** Only Salk and Calgary give these; most other sites list only one platform.
- **Per-genome prices by platform from commercial providers** (Azenta, Psomagen, Macrogen). I only found Novogene $849 and academic $510–650 per 30x genome, none split by platform. A 90–100 Gb genome at $650 with library prep is $6.5–7.2/Gb all-in. Those figures are from search summaries, unverified (OICR/GRCF/TGen pages).
- **Johns Hopkins GRCF** pages returned 403.
- **Ultima, Element, Roche AXELIOS $/Gb comparison.** This was outside my scope.
- **Customer concentration and volumes.** Public price lists say nothing about the large clinical customers' negotiated prices, which are likely well below core rates.

Sources:
- https://www.salk.edu/science/core-facilities/integrative-genomics-and-bioinformatics-core/scheduling-and-rates/
- https://draft.genome.center.uconn.edu/cgi_service_rates
- https://honeycrisp.core.uconn.edu/products/358
- https://case.edu/medicine/genomics/pricing
- https://mbcf.dana-farber.org/pricing
- https://geiselmed.dartmouth.edu/gsr/sequencing/
- https://www.illumina.com/systems/sequencing-platforms/novaseq-x-plus/specifications.html
- https://ngisweden.scilifelab.se/?p=11245
- https://cgsi.wisc.edu/bio-tech-update-sequencings-best-bang-for-the-buck/
- https://www.illumina.com/systems/sequencing-platforms/novaseq-x-plus/applications/broad-sequencing.html
- https://x.com/illumina/status/1575521223664193541
