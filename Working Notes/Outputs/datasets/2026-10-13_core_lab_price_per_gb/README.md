# Core-facility sequencing prices: $/Gb by flow cell, monthly, 2024-10 to 2026-10

*Built 2026-10-14 12:22:16 by `_Build/core_lab_pricing.py`. Workbook: `2026-10-13_core_lab_price_per_gb.xlsx`. CSVs and PNG charts: `2026-10-13_core_lab_price_per_gb/`.*

## What this is

Academic DNA sequencing core facilities (university cores and non-profit institutes such as Broad, Salk, Dana-Farber and CNAG) publish rate cards that list what they charge for a lane or flow cell of sequencing. Converting those prices to US dollars per gigabase (Gb, a billion DNA bases read) makes cores and platforms comparable, and tracking them month by month shows how fast end-user prices are falling.

The dataset covers 70 cores in 8 countries with at least one usable price line. There are 37 main tables and 10 appendix tables (fewer than 8 cores, or non-standard read lengths).

## Layout

- **Summary**: median $/Gb by flow cell by month, plus median, interquartile range and min-max for every table.
- **Coverage**: for each table, the number of cores and how many cells are observed, document-dated or carried forward.
- **One sheet per table**: months down the rows, cores across the columns, values in USD per Gb, with a native Excel line chart. Below the chart data: a flags grid, the local-currency price and unit behind each value, and each core's source URLs and output basis. Sheet names: X25B = NovaSeq X 25B, 6000_S4 = NovaSeq 6000 S4, NS2K = NextSeq 2000, AVITI_* = Element, UG100 = Ultima; `_int` = internal/academic rate, `_ext` = external academic rate, `LP_` = library prep bundled into the price, `RL_` = a read length other than 2x150 (suffix gives the cycles, e.g. `_100c`), `App_` = appendix.
- **LibPrep_bundled**: every price that bundles library preparation with sequencing, as quoted. These are mostly per-sample service prices, so they are listed rather than converted to $/Gb (also `library_prep_bundled_prices.csv`).
- **Sources**: every URL harvested, the core, the snapshot dates that contained price text, tiers and output assumption.
- **Output_specs_FX**: manufacturer output assumptions and exchange rates.
- **Long_data**: every extracted price line from every snapshot (also `long_all_price_lines.csv`).

## Method

1. **Finding cores.** Sonnet web agents searched region by region (US by region, Canada, UK/Ireland, Europe, Asia-Pacific, non-profit institutes) and by platform (Ultima, Element) for public rate cards, older fiscal-year price lists and price-change announcements. About 20 rate cards already in this folder seeded the list. Login-gated rate cards (iLab, CoreSmart, PPMS) were skipped. Commercial providers were excluded.
2. **History.** Every URL was downloaded live (Oct 2026), and PDF price lists linked from live pages were added. Because the Wayback Machine (web.archive.org) throttled requests heavily, archive history was collected for one main rate page per core (the page whose live copy carried the most price lines): the last capture of each quarter since Oct 2024, plus the latest capture before the window. Older price lists found by the search agents or linked from live pages contribute history through the dates printed on them.
3. **Extraction.** Claude Haiku turned each distinct price-list text into structured lines (flow cell, unit, read length, user tier, price, currency, library-prep bundling, stated output, effective dates). Claude Sonnet re-extracted pages whose results were implausible, conflicted with another document from the same core and month, or found no prices where prices were evident.
4. **$/Gb.** Price in USD divided by the Gb that the price buys. Gb uses the manufacturer's maximum specified output at 2x150 (300 cycles), divided by lanes for per-lane prices; Ultima uses wafer output. Where the core states its own output (e.g. '~800M reads per lane'), that is used instead and flagged in `output_basis`. Main tables use 300-cycle runs only.
5. **Months.** A cell is **O** (observed) if a snapshot from that month shows the price, **D** (document-dated) if the month falls inside the effective period printed on the price list, and **C** (carried) if neither, in which case the last observed price is carried forward. Months before a core's first observation are blank. When two documents disagree for the same month, the more recently dated document wins; snapshots beat document dates; per-lane prices beat whole-flow-cell prices.
6. **Tiers.** Main tables use internal (own-institution) rates; a price list with a single, unlabelled price is treated as internal. External academic rates have their own tables. Commercial rates are kept in Long_data but not tabulated. Tariff surcharges are not added.

## Caveats

- **Carried cells are not observations.** Wayback captures some pages monthly and others once or twice a year, so many cells are carried. Use the flags (or the Coverage sheet) before reading a flat line as 'no price change'.
- **Medians mix different cores over time.** Few cores have history, so the number of cores behind each month's median grows toward Oct 2026 (see `cores_with_value`). A change in the median can reflect which cores are included rather than price changes; for discounting, read the core-level columns and the Coverage sheet's first-to-last change.
- **Implausible values are excluded from the tables.** Prices outside a plausible $/Gb band for the platform (usually a per-lane price read as a whole flow cell) were re-checked by Claude Sonnet; any still outside the band are left out of the grids but kept, flagged, in Long_data.
- **Manufacturer output is a ceiling.** Real lane yields are often lower, so true $/Gb is somewhat higher than shown. The bias is similar across cores for the same flow cell, so trends and ranking hold better than levels.
- **Extraction is automated.** Values come from model extraction of messy tables, checked by a second model only where flagged. Spot-check any value you rely on against the URL in the Sources sheet.
- **Exchange rates are fixed** (approximate 2026 rates in Output_specs_FX), so non-US trends show local-price changes only. Local prices are kept for reconversion.
- **Core rates are not Illumina's price.** Cores add labour, overhead and subsidy, and some are subsidised by their institutions. Changes in core prices lag and dampen changes in reagent prices.

## Coverage by table

| Sheet | Table | Cores | Observed cells | Document-dated | Carried | Cores with a price change | Median change first-to-last |
|---|---|---|---|---|---|---|---|
| X25B_int | Illumina NovaSeq X 25B, internal/academic rate | 38 | 72 | 81 | 335 | 11 | 0.0% |
| RL_X25B_int_100c | Illumina NovaSeq X 25B, internal/academic rate, 100 cycles | 21 | 33 | 39 | 136 | 3 | 0.0% |
| RL_X25B_int_200c | Illumina NovaSeq X 25B, internal/academic rate, 200 cycles | 18 | 25 | 37 | 101 | 2 | 0.0% |
| X25B_ext | Illumina NovaSeq X 25B, external academic rate | 17 | 33 | 36 | 134 | 3 | 0.0% |
| RL_X25B_ext_100c | Illumina NovaSeq X 25B, external academic rate, 100 cycles | 8 | 12 | 28 | 29 | 1 | 0.0% |
| X10B_int | Illumina NovaSeq X 10B, internal/academic rate | 39 | 71 | 83 | 386 | 11 | 0.0% |
| RL_X10B_int_100c | Illumina NovaSeq X 10B, internal/academic rate, 100 cycles | 27 | 56 | 70 | 231 | 9 | 0.0% |
| RL_X10B_int_200c | Illumina NovaSeq X 10B, internal/academic rate, 200 cycles | 24 | 42 | 47 | 220 | 7 | 0.0% |
| X10B_ext | Illumina NovaSeq X 10B, external academic rate | 16 | 32 | 36 | 134 | 4 | 0.0% |
| RL_X10B_ext_100c | Illumina NovaSeq X 10B, external academic rate, 100 cycles | 14 | 28 | 36 | 90 | 3 | 0.0% |
| RL_X10B_ext_200c | Illumina NovaSeq X 10B, external academic rate, 200 cycles | 13 | 25 | 36 | 91 | 3 | 0.0% |
| X1.5B_int | Illumina NovaSeq X 1.5B, internal/academic rate | 22 | 44 | 36 | 169 | 6 | 0.0% |
| RL_X1.5B_int_100c | Illumina NovaSeq X 1.5B, internal/academic rate, 100 cycles | 15 | 31 | 16 | 133 | 4 | 0.0% |
| RL_X1.5B_int_200c | Illumina NovaSeq X 1.5B, internal/academic rate, 200 cycles | 15 | 25 | 24 | 93 | 2 | 0.0% |
| RL_X1.5B_int_600c | Illumina NovaSeq X 1.5B, internal/academic rate, 600 cycles | 9 | 9 | 7 | 11 | 1 | 0.0% |
| X1.5B_ext | Illumina NovaSeq X 1.5B, external academic rate | 11 | 22 | 36 | 75 | 3 | 0.0% |
| RL_X1.5B_ext_200c | Illumina NovaSeq X 1.5B, external academic rate, 200 cycles | 9 | 16 | 36 | 32 | 1 | 0.0% |
| 6000_S4_int | Illumina NovaSeq 6000 S4, internal/academic rate | 25 | 29 | 32 | 340 | 4 | 0.0% |
| 6000_S4_ext | Illumina NovaSeq 6000 S4, external academic rate | 14 | 17 | 34 | 145 | 2 | 0.0% |
| 6000_S2_int | Illumina NovaSeq 6000 S2, internal/academic rate | 22 | 24 | 27 | 322 | 5 | 0.0% |
| 6000_S2_ext | Illumina NovaSeq 6000 S2, external academic rate | 13 | 16 | 34 | 139 | 2 | 0.0% |
| 6000_S1_int | Illumina NovaSeq 6000 S1, internal/academic rate | 21 | 24 | 27 | 294 | 5 | 0.0% |
| 6000_S1_ext | Illumina NovaSeq 6000 S1, external academic rate | 14 | 19 | 34 | 147 | 3 | 0.0% |
| 6000_SP_int | Illumina NovaSeq 6000 SP, internal/academic rate | 23 | 28 | 31 | 308 | 5 | 0.0% |
| 6000_SP_ext | Illumina NovaSeq 6000 SP, external academic rate | 14 | 19 | 34 | 147 | 3 | 0.0% |
| NS2K_P4_int | Illumina NextSeq 2000 P4, internal/academic rate | 18 | 38 | 26 | 130 | 7 | 2.0% |
| NS2K_P4_ext | Illumina NextSeq 2000 P4, external academic rate | 9 | 19 | 32 | 30 | 2 | 0.0% |
| NS2K_P3_int | Illumina NextSeq 2000 P3, internal/academic rate | 19 | 43 | 34 | 146 | 9 | 0.0% |
| NS2K_P3_ext | Illumina NextSeq 2000 P3, external academic rate | 10 | 22 | 40 | 36 | 3 | 0.0% |
| NS2K_P2_int | Illumina NextSeq 2000 P2, internal/academic rate | 24 | 51 | 34 | 171 | 9 | 0.0% |
| NS2K_P2_ext | Illumina NextSeq 2000 P2, external academic rate | 13 | 27 | 40 | 56 | 3 | 0.0% |
| NS2K_P1_int | Illumina NextSeq 2000 P1, internal/academic rate | 23 | 50 | 34 | 171 | 8 | 0.0% |
| NS2K_P1_ext | Illumina NextSeq 2000 P1, external academic rate | 13 | 27 | 40 | 56 | 3 | 0.0% |
| AVITI_HIGH_int | Element AVITI High Output, internal/academic rate | 7 | 14 | 8 | 77 | 3 | 0.0% |
| AVITI_HIGH_ext | Element AVITI High Output, external academic rate | 6 | 14 | 15 | 51 | 2 | 0.0% |
| UG100_int | Ultima UG 100 wafer, internal/academic rate | 3 | 5 | 0 | 2 | 0 | 0.0% |
| UG100_ext | Ultima UG 100 wafer, external academic rate | 1 | 1 | 0 | 0 | 0 | nan% |
| App_X5B_int | Illumina NovaSeq X 5B, internal/academic rate (appendix) | 7 | 6 | 6 | 11 | 0 | 0.0% |
| App_X5B_ext | Illumina NovaSeq X 5B, external academic rate (appendix) | 2 | 2 | 2 | 0 | 0 | 0.0% |
| App_AVITI_ULTRAQ_int | Element AVITI Cloudbreak UltraQ, internal/academic rate (appendix) | 4 | 7 | 0 | 2 | 0 | 0.0% |
| App_AVITI_ULTRAQ_ext | Element AVITI Cloudbreak UltraQ, external academic rate (appendix) | 4 | 7 | 0 | 2 | 0 | 0.0% |
| App_AVITI_MEDIUM_int | Element AVITI Medium Output, internal/academic rate (appendix) | 7 | 19 | 7 | 66 | 2 | 0.0% |
| App_AVITI_MEDIUM_ext | Element AVITI Medium Output, external academic rate (appendix) | 6 | 20 | 14 | 42 | 2 | 0.0% |
| App_AVITI_LOW_int | Element AVITI Low Output, internal/academic rate (appendix) | 7 | 15 | 7 | 57 | 2 | 0.0% |
| App_AVITI_LOW_ext | Element AVITI Low Output, external academic rate (appendix) | 4 | 11 | 14 | 28 | 2 | 2.4% |
| App_AVITI24_int | Element AVITI24, internal/academic rate (appendix) | 1 | 1 | 0 | 0 | 0 | nan% |
| App_AVITI24_ext | Element AVITI24, external academic rate (appendix) | 1 | 1 | 0 | 0 | 0 | nan% |

## Columns in the CSVs

- `<sheet>_usd_per_gb.csv`: month rows, one column per core, USD per Gb.
- `<sheet>_flags.csv`: same shape, O / D / C flags.
- `summary_by_table_month.csv`: table, month, cores with value, cores observed that month, median, p25, p75, min, max.
- `coverage_by_table.csv`: as in the table above.
- `sources.csv`: core, institution, country, kind, URL, URL type, how it was found, snapshot dates with price text, price lines extracted, tiers, output assumption.
- `output_specs.csv`: flow-cell output assumptions.
- `long_all_price_lines.csv`: one row per extracted price line per snapshot: core, URL, snapshot timestamp and month, live or Wayback, document date and effective period, flow cell, unit, quantity, read configuration, cycles, tier, local price, currency, FX, USD price, library-prep flag, stated output, Gb per unit, output basis, $/Gb, verbatim snippet, implausible and excluded flags.
