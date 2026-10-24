# 03 Sell-side and consensus working file: Bloomberg consensus (Part A) and sell-side research (Part B)

Prepared 2026-10-11 for the ILMN buy-side primer. Scope: all three Bloomberg consensus printouts and all 31 sell-side and independent research notes on ILMN in the folder. Every number carries a label:

- **[D]** disclosed company data (reported actuals, company guidance as relayed in a note).
- **[E: firm]** an estimate or opinion from that firm. Bloomberg consensus estimates are labelled **[E: BBG cons]**.
- **[Der]** my own calculation from the cited numbers, with the arithmetic shown or implied.

Files read in full: `Sources/ILMN/consensus/ILMN_Consensus_Annuals.md`, `ILMN_Consensus_Quarterlies.md`, `ILMN_Consensus_Quarterlies_2.md` (and the three matching extracts in `Extracts/ILMN/consensus/`), and all 31 files in `Extracts/ILMN/research/`, with the originals in `Sources/ILMN/research/` opened for the JPM, Barclays and UBS tables and price-target math.

---

## Key findings (read these first)

1. **Consensus is the guidance midpoint, and guidance has been raised twice.** Bloomberg FY26E: revenue $4,625M, EPS $5.36, operating margin 23.5%; FY27E $4,918M / $6.11 / 25.2%; FY28E $5,263M / $7.01 / 26.5% (10 Oct snapshot). FY26 EPS consensus is up 5.7% since February and FY28 up 8.7%; the out-years have moved more than the current year (section B3).
2. **The whole forecast is a call on sequencing consumables accelerating** from +4.5% in 1H26 to +8.8% in FY27E and +9.3% in FY28E, while instruments roll over (-6% in FY27E) and China shrinks to $187M. Consumables supply 86-91% of the revenue growth in FY27-28 (A2). Consensus FY27E ex-China growth is about +7.1% on a 53-week base, the low edge of management's "high-single-digit" target, with no visible room for the 1-2 points of multiomics growth management promises (B5e).
3. **Clinical growth decelerated in 2Q26.** Clinical ROW consumables went +20%, +20%, then +15% (Q4'25, Q1'26, Q2'26), blamed on the Middle East and Latin America with the US still above +20%; management guides FY26 to "+mid-teens". JPM models a +low/mid-teens CAGR through 2030. The bulls' case rests on that rate holding; the segment growth rates do not reconcile cleanly to the reported +5% total (B5c).
4. **Price per Gb is the hidden variable.** Sequencing activity (Gb) has grown more than 30% a year while consumables revenue grew +4-5%, implying revenue per Gb fell about 19%. On Ameriprise/Freedom share data the residual 17% of high-throughput Gb on the 6000 earns 41% of high-throughput revenue (3.4x the X's revenue per Gb). Consensus +8.8% in FY27E needs revenue/Gb to fall 16% if Gb grows 30%, or 9% if Gb grows 20% (B5a-b). Barclays flags flat X revenue share on rising X Gb share in 1Q as possible price erosion; JPM and management say pricing headwinds are over.
5. **The sell-side is stale against the stock.** The newest broker note is 5 Aug; the last price in the folder is $278.17 (Seeking Alpha header, about 10 Oct), +35.6% since the 30 Jul close of $205.09. The highest target is JPM's $230 (WACC and terminal-growth cuts explain about $44 of the $185 June target). At $278 ILMN is 52x FY26E and 45x FY27E adjusted EPS and 29x FY27E EV/EBITDA, roughly 13 turns above the June Core Tools multiple of 15.6x, which is back near the ~15-turn historical premium that JPM called cheap in June (B4-iv).
6. **Brokers differ most on 2028:** EPS $6.02 (Barclays) to $7.41 (JPM); revenue growth +5.0% to +12.0%. Only JPM models double-digit growth; consensus FY28E +7.0%.
7. **Roche:** list consumables $150 per genome (20x reuse) vs about $200 for the X; Element's VITARI claims about half the $/Gb at $3k a run. JPM's 62-customer survey shows only 8% would consider buying Axelios within 12 months, 65% of would-be buyers would cut Illumina use and 11% would decommission; UBS flags counting applications (about 14-16% of sequencing consumables) as the real exposure.
8. **Calendar conflict:** Bloomberg dates imply a 14-week Q3; management says the extra week is in Q4 (about +0.5 point). I treat Q4 as the 14-week quarter (section 0).

---

## 0. Read this first: snapshot, calendar and caveats

**Snapshot.** The three Bloomberg "Company Financials" printouts were run on **10 October 2026 between 20:52 and 20:55** (annuals 20:52:20, quarterlies 20:53:20, quarterlies page set 2 20:55:20) with "Est Source: Consensus" and no analytics applied [D: Bloomberg printouts]. That is after the Q2 2026 report (30 July) and the Q3 2026 quarter-end estimate date, but before the Q3 report. Actual columns run to 2Q26 (quarter ended 28 June 2026). Everything after that is a consensus mean.

**What the printouts do not contain.** There is no analyst count, no high/low/standard deviation, no revision history, and no KPI rows (installed base, placements, pull-through, Gb, clinical growth). Those do not exist anywhere in the three files, so I have not invented them. KPI data below come from the broker notes (Part B).

**Fiscal calendar and the 53-week year.** FY2026 ends 3 January 2027, one week later than FY2025 (28 December 2025), so FY2026 has **53 weeks** and FY2027 (ends 2 January 2028) has 52 [D: Bloomberg period-end dates]. FY2027 consensus growth is therefore measured against a 53-week base. **Which quarter holds the extra week is contested, and this matters:**

- Bloomberg's estimate-period end dates (3Q26 ending 4 Oct 2026; 4Q26 ending 3 Jan 2027) imply **3Q26 = 14 weeks and 4Q26 = 13 weeks** (28 June to 4 October is 98 days; 4 October to 3 January is 91 days) [Der]. The Core Notes and the brief for this project carry that reading.
- **Management says the extra week is in Q4.** On the Q2 2026 call the CFO (Dhingra) said Q4 "is largely a consumables story" worth "maybe 0.5 point of revenue" (`Working Notes/Extracts/ILMN/earnings_call/ILMN_2026Q2_Earnings_Call.md`, line 141; also Core Notes `05_ILMN_Earnings_Calls_2025-2026.md` line 668). Ameriprise (31 Jul 2026) and J.P. Morgan (31 Jul 2026) both repeat "an extra week in Q4 … about +0.5pt to revenue".
- Illumina's prior 53-week year (FY2020) also put the 14th week in Q4 (Q4 2020 ended 3 January 2021) [my recollection, not in the folder; treat as unverified]. If so, Q3 2026 ended 27 September 2026 and Bloomberg's "10/04/2026" is a placeholder date.
- **Treatment in this file:** I show Bloomberg's dates as printed but treat management's statement as the better evidence, i.e. **4Q26 is the 14-week quarter** and 3Q26E ($1,154M, versus guidance of $1.14-1.16B) is a 13-week quarter. Whoever builds the primer should confirm against the 10-Q's fiscal-calendar note. Size check [Der]: one full run-rate week of 4Q25 revenue is $1,159M / 13 = about $89M, or about 2 points of FY26 growth, so management's "0.5 point" is much smaller than a naive extra week. Either the extra week is only partly incremental (holiday week) or the 0.5 point is a quarter-level or consumables-only figure. The consensus 4Q26E sequencing consumables growth of +7.9% y/y versus +5.6% in 3Q26E (a gap of about 2.3 points, or about $17M) looks like it embeds only a small calendar benefit.

**Data-quality flags that change how the tables should be read** (details in section A5):

1. Bloomberg's **2026 actual** regional lines are on Illumina's new four-region basis (USCAN, EMEALA, Greater China, APAC), but its **2025 actuals are on the old basis** (Americas, Europe, Greater China, APMEA). So Bloomberg's own Europe "y/y" of +21.5% in 1Q26 is spurious. On a like-for-like basis EMEALA grew about +7% (356 vs 332) [Der from Ameriprise 2026-05-01]. Only Greater China is clean.
2. The **quarterly consensus for 2028 sums to $7.34 of EPS and $5,296M of revenue, versus annual consensus of $7.01 and $5,263M.** Different contributor sets. Use the annual line for the full-year number and the quarterly line for shape only.
3. Several balance-sheet and cash lines are internally inconsistent in the printouts (cash definitions, net debt per share, GAAP gross profit FY26E). Listed in A5.
4. Bloomberg's "Adjusted Operating Income" is the company's non-GAAP number (SBC and acquired-intangible amortisation excluded). It ties to FY25 reported $1,004M. **J.P. Morgan's "Adj. EBIT" is after stock-based compensation** (FY25 $729M = $1,004M - $275M SBC), so JPM margins (about 18%) are not comparable with the company's 23%.

---

## PART A. Bloomberg consensus (snapshot 10 Oct 2026)

### A1. Annual, FY2023A to FY2032E

The next table shows the revenue build by product line. FY23-FY25 are reported [D]; FY26E onward are consensus [E: BBG cons]. Figures are $ millions. Blank cells ("–") are blank in the printout.

| $M | FY23A | FY24A | FY25A | FY26E | FY27E | FY28E | FY29E | FY30E | FY31E | FY32E |
|---|---|---|---|---|---|---|---|---|---|---|
| Revenue | 4,504 | 4,372 | 4,343 | 4,625 | 4,918 | 5,263 | 5,650 | 6,088 | 6,704 | 7,370 |
| Product revenue | 3,787 | 3,656 | 3,709 | 3,905 | 4,149 | 4,450 | 4,806 | 5,274 | 5,946 | 7,116 |
| Service & other | 717 | 716 | 634 | 719 | 752 | 786 | 827 | 876 | 940 | 1,035 |
| Total consumables | 3,083 | 3,155 | 3,227 | 3,402 | 3,669 | 3,964 | 4,341 | 4,792 | 5,403 | 6,454 |
| Sequencing consumables | 2,790 | 2,858 | 2,939 | 3,104 | 3,378 | 3,694 | 4,034 | 4,479 | 5,019 | 5,675 |
| Microarray consumables | 293 | 297 | 288 | 302 | 304 | 309 | 307 | 309 | 324 | 310 |
| Total instruments | 704 | 501 | 482 | 500 | 470 | 468 | 465 | 482 | 543 | 662 |
| Sequencing instruments | 685 | 484 | 465 | 483 | 454 | 454 | 445 | 459 | 498 | 520 |
| Microarray instruments | 19 | 17 | 17 | 15.5 | 15.5 | 15.4 | 15.7 | 14.6 | 15 | – |
| Sequencing service | 637 | 651 | 581 | 626 | 654 | 684 | 714 | 742 | 794 | 842 |
| Microarray service | 80 | 65 | 53 | 95.4 | 101 | 105 | 113 | 121 | 124 | 118 |
| Total sequencing revenue | 4,112 | 3,993 | 3,985 | 4,214 | 4,487 | 4,831 | 5,197 | 5,705 | 6,423 | 7,713 |
| Total microarray revenue | 392 | 379 | 358 | 413 | 420 | 430 | 436 | 441 | 455 | 436 |

The next table shows year-over-year growth and mix [Der: each cell is the current year divided by the prior year, minus 1]. The pattern to take from it: consensus has revenue growth of 6.3-7.8% a year through FY30, driven by sequencing consumables growing 8.8-11%, while instruments are flat to down and China is a shrinking drag. The FY31-FY32 columns accelerate to about 10% with a +19.7% product jump in FY32, which looks like a thin-contributor artefact (see A5) and should not be used.

| y/y growth (Der) | FY23A | FY24A | FY25A | FY26E | FY27E | FY28E | FY29E | FY30E | FY31E | FY32E |
|---|---|---|---|---|---|---|---|---|---|---|
| Revenue | – | -2.9% | -0.7% | +6.5% | +6.3% | +7.0% | +7.4% | +7.8% | +10.1% | +9.9% |
| Product revenue | – | -3.5% | +1.4% | +5.3% | +6.2% | +7.3% | +8.0% | +9.7% | +12.7% | +19.7% |
| Service & other | – | -0.1% | -11.5% | +13.4% | +4.7% | +4.5% | +5.2% | +5.9% | +7.3% | +10.1% |
| Total consumables | – | +2.3% | +2.3% | +5.4% | +7.8% | +8.0% | +9.5% | +10.4% | +12.8% | +19.5% |
| Sequencing consumables | – | +2.4% | +2.8% | +5.6% | +8.8% | +9.3% | +9.2% | +11.0% | +12.1% | +13.1% |
| Microarray consumables | – | +1.4% | -3.0% | +5.0% | +0.5% | +1.8% | -0.7% | +0.5% | +5.0% | -4.2% |
| Total instruments | – | -28.8% | -3.8% | +3.8% | -6.1% | -0.3% | -0.8% | +3.8% | +12.6% | +21.8% |
| Sequencing instruments | – | -29.3% | -3.9% | +3.8% | -6.0% | +0.0% | -1.9% | +3.0% | +8.5% | +4.5% |
| Sequencing service | – | +2.2% | -10.8% | +7.8% | +4.5% | +4.5% | +4.4% | +3.9% | +7.1% | +6.0% |
| Total sequencing revenue | – | -2.9% | -0.2% | +5.7% | +6.5% | +7.6% | +7.6% | +9.8% | +12.6% | +20.1% |
| Total microarray revenue | – | -3.3% | -5.5% | +15.4% | +1.7% | +2.2% | +1.6% | +1.0% | +3.2% | -4.1% |
| Greater China | – | -19.8% | -21.1% | -13.3% | -10.2% | -1.1% | +22.9% | -10.1% | +9.1% | +8.4% |
| Adj. EBITDA | – | +18.9% | +49.7% | +7.6% | +14.7% | +8.9% | +10.4% | +11.5% | +8.7% | +15.4% |
| Adj. operating income | – | +134.8% | +73.1% | +8.4% | +13.5% | +13.1% | +15.8% | +14.6% | +19.4% | +11.1% |
| Adj. net income | – | +184.7% | +93.8% | +8.6% | +14.1% | +14.6% | +13.9% | +17.9% | +19.5% | +17.8% |
| Adj. diluted EPS ($) | – | +184.9% | +97.6% | +10.7% | +14.0% | +14.7% | +14.0% | +18.9% | +15.9% | +11.7% |
| Free cash flow | – | +145.6% | +34.0% | +7.1% | +10.5% | +12.5% | +6.9% | +14.9% | +5.0% | +17.6% |
| Revenue ex-Greater China | – | -1.4% | +0.9% | +7.7% | +7.1% | +7.3% | +6.8% | +8.5% | +10.2% | +10.0% |
| Consumables % of revenue | 68.5% | 72.2% | 74.3% | 73.6% | 74.6% | 75.3% | 76.8% | 78.7% | 80.6% | 87.6% |
| Instruments % of revenue | 15.6% | 11.5% | 11.1% | 10.8% | 9.5% | 8.9% | 8.2% | 7.9% | 8.1% | 9.0% |
| Sequencing consumables % of seq. revenue | 67.9% | 71.6% | 73.8% | 73.7% | 75.3% | 76.5% | 77.6% | 78.5% | 78.1% | 73.6% |
| Greater China % of revenue | 8.5% | 7.0% | 5.6% | 4.6% | 3.8% | 3.6% | 4.1% | 3.4% | 3.4% | 3.3% |

The next table shows the profit and loss from adjusted gross profit to EPS. Adjusted figures exclude SBC and acquired-intangible amortisation. The key readings: consensus has the adjusted operating margin rising from 23.1% (FY25) to 23.5% (FY26E), 25.2% (FY27E), 26.5% (FY28E) and 30.7% (FY32E); opex (SG&A plus R&D) grows only 3-6% a year against revenue growth of 6-8%, which is where all of the margin expansion comes from.

| $M unless noted | FY23A | FY24A | FY25A | FY26E | FY27E | FY28E | FY29E | FY30E | FY31E | FY32E |
|---|---|---|---|---|---|---|---|---|---|---|
| Revenue | 4,504 | 4,372 | 4,343 | 4,625 | 4,918 | 5,263 | 5,650 | 6,088 | 6,704 | 7,371 |
| Adj. gross profit (BBG row) | 2,940 | 2,990 | 2,964 | 3,161 | 3,401 | 3,703 | 4,045 | 4,412 | 4,872 | 5,716 |
| Adj. gross margin (BBG stated, %) | 65.3 | 68.4 | 68.2 | 68.47 | 69.05 | 69.53 | 70.03 | 70.26 | 70.82 | 70.41 |
| Cost of products sold | 1,177 | 1,017 | 1,107 | 1,146 | 1,190 | 1,266 | 1,354 | 1,517 | 1,644 | 2,027 |
| Cost of services sold | 392 | 367 | 300 | 310 | 341 | 343 | 354 | 366 | 382 | – |
| Adj. SG&A | 1,367 | 1,247 | 1,009 | 1,090 | 1,121 | 1,165 | 1,234 | 1,369 | 1,458 | – |
| Adj. R&D | 1,325 | 1,163 | 950 | 984 | 1,020 | 1,059 | 1,099 | 1,096 | 1,176 | – |
| SG&A + R&D [Der] | 2,692 | 2,410 | 1,959 | 2,074 | 2,141 | 2,224 | 2,333 | 2,465 | 2,634 | – |
| SG&A + R&D growth [Der] | – | -10.5% | -18.7% | +5.9% | +3.3% | +3.8% | +4.9% | +5.6% | +6.9% | – |
| Total adj. opex (BBG row, incl. other items) | 3,813 | 3,694 | 2,063 | 2,100 | 2,147 | 2,217 | 2,248 | 2,287 | – | – |
| **Adj. operating income** | 247 | 580 | 1,004 | 1,088 | 1,235 | 1,396 | 1,617 | 1,853 | 2,214 | 2,460 |
| Adj. operating margin (BBG, %) | 5.48 | 13.27 | 23.12 | 23.50 | 25.22 | 26.50 | 27.68 | 28.80 | 29.16 | 30.70 |
| Incremental op. margin [Der: change in op. income / change in revenue] | n.m. | n.m. | n.m. | 30% | 50% | 47% | 57% | 54% | 58% | 37% |
| Adj. EBITDA | 679 | 807 | 1,208 | 1,299 | 1,490 | 1,623 | 1,791 | 1,997 | 2,171 | 2,505 |
| EBITDA margin [Der] | 15.1% | 18.5% | 27.8% | 28.1% | 30.3% | 30.8% | 31.7% | 32.8% | 32.4% | 34.0% |
| Other non-operating income | 12 | 51 | 54 | 54.9 | 58.8 | 56.2 | 58.0 | 40.9 | 11.8 | 23.6 |
| Adj. pre-tax income | 259 | 529 | 950 | 1,031 | 1,174 | 1,347 | 1,504 | 1,749 | 1,998 | 2,551 |
| Income tax | 98 | 139 | 194 | 211.6 | 240.4 | 274.8 | 309.4 | 363.6 | 420.1 | 522.7 |
| Tax rate (%) | 41.8 | 26.3 | 20.5 | 20.49 | 20.46 | 20.43 | 20.65 | 21.12 | 21.41 | 21.25 |
| **Adj. net income** | 137 | 390 | 756 | 821 | 936 | 1,073 | 1,222 | 1,441 | 1,722 | 2,028 |
| Net margin (%) | 3.04 | 8.92 | 17.41 | 17.73 | 18.88 | 20.09 | 21.25 | 22.89 | 23.14 | 24.88 |
| Diluted shares (M) | 158 | 159 | 156 | 153.1 | 152.7 | 152.6 | 151.8 | 149.6 | 149.4 | 164.9 |
| **Adj. diluted EPS ($)** | 0.86 | 2.45 | 4.84 | 5.36 | 6.11 | 7.01 | 7.99 | 9.50 | 11.01 | 12.30 |
| EPS growth [Der] | – | +185% | +98% | +10.7% | +14.0% | +14.7% | +14.0% | +18.9% | +15.9% | +11.7% |
| Dividend per share ($) | 0 | 0 | 0 | 0 | 0 | 0 | – | – | – | – |

The GAAP view and the bridge items follow. The point to take: consensus GAAP EPS runs $0.34 (FY26E) and $0.40 (FY27E) below adjusted (SBC of about $282-296M a year, 6.2% to 5.8% of revenue, plus amortisation of about $56-62M), so a P/E on "adjusted" EPS flatters the multiple by roughly 6-7% versus GAAP.

| $M unless noted | FY23A | FY24A | FY25A | FY26E | FY27E | FY28E | FY29E | FY30E | FY31E | FY32E |
|---|---|---|---|---|---|---|---|---|---|---|
| GAAP gross profit | 2,744 | 2,861 | 2,870 | 2,740 (error, see A5) | 3,352 | 3,637 | 4,034 | – | – | – |
| GAAP gross margin (%) | 60.9 | 65.4 | 66.1 | 67.49 | 68.23 | 68.64 | 68.97 | 69.00 | – | – |
| GAAP operating income | -1,069 | -833 | 807 | 944 | 1,128 | 1,307 | 1,577 | 1,810 | 2,025 | – |
| GAAP operating margin (%) | -23.7 | -19.1 | 18.6 | 21.26 | 23.19 | 25.00 | 26.44 | 27.89 | 28.54 | – |
| GAAP net income | -1,161 | -1,223 | 850 | 766 | 878 | 1,019 | 1,190 | 1,355 | 1,566 | 2,064 |
| GAAP diluted EPS ($) | -7.34 | -7.69 | 5.45 | 5.02 | 5.71 | 6.56 | 7.70 | 9.04 | 10.38 | 12.52 |
| Stock-based compensation | 380 | 370 | 275 | 282 | 296 | 312 | 324 | 354 | 396 | 595 |
| SBC % of revenue | 8.4 | 8.5 | 6.3 | 6.15 | 5.83 | 5.72 | 5.85 | 5.73 | 5.71 | 7.30 |
| Amortisation of intangibles (adj. bridge) | 197 | 130 | 66 | 56 | 62 | 54 | 53 | 48 | 63 | 23 |
| D&A (cash-flow statement) | 432 | 354 | 270 | 269 | 283 | 294 | 298 | 293 | 276 | 292 |

The next table shows cash flow, capital allocation and the balance sheet. The readings: consensus free cash flow (operating cash flow less capex) is about $1.0B in FY26E rising to $1.24B in FY28E, roughly 21-24% of revenue and above 100% of adjusted net income through FY29E. The only large acquisition in the forecast is $413.5M in FY26E, which is SomaLogic (closed 30 Jan 2026, $350M upfront, $363M net cash paid, plus a $25M first milestone paid after Q1) [D: Ameriprise 2026-05-01], though Bloomberg's quarterly sheet shows "Acquisitions 0.00" for 1Q26.

| $M unless noted | FY23A | FY24A | FY25A | FY26E | FY27E | FY28E | FY29E | FY30E | FY31E | FY32E |
|---|---|---|---|---|---|---|---|---|---|---|
| Cash flow from operations | 478 | 837 | 1,079 | 1,178 | 1,326 | 1,459 | 1,586 | 1,788 | 1,850 | 2,133 |
| Capex | -195 | -128 | -148 | -197 | -203 | -199 | -225 | -232 | -252 | -279 |
| Capex % revenue (BBG) | 4.33 | 2.93 | 3.41 | 4.31 | 4.15 | 3.83 | 3.87 | 3.63 | 3.71 | 3.53 |
| **Free cash flow** | 283 | 695 | 931 | 997 | 1,102 | 1,239 | 1,324 | 1,521 | 1,598 | 1,880 |
| FCF margin [Der] | 6.3% | 15.9% | 21.4% | 21.6% | 22.4% | 23.5% | 23.4% | 25.0% | 23.8% | 25.5% |
| FCF / adj. net income [Der] | 207% | 178% | 123% | 121% | 118% | 115% | 108% | 106% | 93% | 93% |
| Acquisitions | -29 | -81 | 0 | -413.5 | -16.7 | -25 | – | – | – | – |
| Share repurchases | 0 | -116 | -742 | -420 | -313 | -501 | -600 | -1,000 | -1,000 | – |
| Debt repayments | 0 | 0 | 0 | -250 | -167 | 0 | – | – | – | – |
| Cash & equivalents (balance sheet) | 1,048 | 1,127 | 1,418 | 1,527 | 2,299 | 3,244 | 4,502 | 5,269 | 6,488 | 10,345 |
| Short-term investments | 6 | 93 | 215 | 133 | 133 | 134 | 122 | 113 | 107 | 66 |
| Current portion of debt | 0 | 499 | 499 | 506 | 506 | 419 | 425 | 385 | 250 | 0.5 |
| Long-term debt | 1,489 | 1,490 | 1,490 | 1,564 | 1,518 | 1,491 | 1,492 | 1,743 | 1,740 | 1,989 |
| Net debt / (cash) (BBG) | 435 | 769 | 356 | 403 | 51 | -221 | -2,650 | -3,407 | -4,633 | – |
| Shareholders' equity | 5,745 | 2,373 | 2,723 | 3,141 | 4,026 | 4,831 | 6,071 | 7,175 | 9,132 | 11,737 |
| Accounts receivable | 734 | 735 | 854 | 798 | 843 | 914 | 951 | 1,016 | 1,128 | 1,073 |
| Inventories | 587 | 547 | 564 | 608 | 625 | 643 | 642 | 634 | 767 | 714 |
| Goodwill | 2,545 | 1,113 | 1,113 | 1,245 | 1,233 | 1,213 | 1,256 | 1,250 | 1,284 | 1,284 |

The last annual table shows geography as printed. Read it with the basis warning in section 0: FY25A is on the old region definitions, so only Greater China is reliable across the break. Greater China is the one line consensus has shrinking: $384M (FY23) to $243M (FY25) to $211M (FY26E, at the bottom of the company's $210-220M guide [D: Ameriprise 2026-02-06]) to $187M (FY28E).

| $M | FY23A | FY24A | FY25A | FY26E | FY27E | FY28E | FY29E | FY30E | FY31E | FY32E |
|---|---|---|---|---|---|---|---|---|---|---|
| Americas (as printed) | 2,521 | 2,441 | 2,406 | 2,598 | 2,853 | 3,140 | 3,630 | 3,997 | 4,360 | 4,725 |
| Europe (as printed) | 1,140 | 1,185 | 1,264 | 1,360 | 1,462 | 1,572 | – | – | – | – |
| EMEA on prior basis | – | – | – | 1,466 | 1,550 | 1,691 | 1,812 | 2,008 | 2,191 | 2,374 |
| Greater China | 384 | 308 | 243 | 211 | 189 | 187 | 230 | 207 | 226 | 245 |
| APMEA (as printed) | 459 | 438 | 430 | 440 | 489 | 527 | 620 | 683 | 745 | 807 |

### A2. What the annual consensus implies [Der]

- **Consensus equals the guidance midpoint on every line, with no cushion.** FY26E revenue $4,624.8M vs guidance $4.60-4.64B (midpoint $4.62B); EPS $5.36 vs $5.30-5.40; operating margin 23.50% vs 23.4-23.6%; Greater China $210.7M vs $210-220M [D: Ameriprise 2026-07-31 guidance table]. Consensus FY26 EPS has risen from $5.07 in early February to $5.36 (+5.7%) because management raised guidance at each of the last two prints. See section B3 for the drift.
- **Sequencing consumables are the whole story.** Sequencing consumables grow +5.6% in FY26E ($2,939M to $3,104M), then **+8.8% in FY27E and +9.3% in FY28E**, adding $274M and $316M. Consumables supply 91% and 86% of the revenue increase in FY27 and FY28 (Δconsumables / Δrevenue = 266.5/293.5 and 295.2/344.6).
- **The consumables acceleration is a call on the lag from record placements.** H1 2026 sequencing consumables grew +4.5% y/y ((726+775)/(696+740)); consensus 2H26 is +6.8% and FY27 +8.8%. Management says new instruments take six to nine months to normalise (Ameriprise 2026-07-31).
- **Instruments are expected to roll over.** FY26E $500M (+3.8%) is already 50% locked in by H1 actuals of $250M (+17.4% y/y); the implied H2 is $247M, down 8% on H2 2025's $269M. FY27E instruments fall 6.1% to $470M and stay flat through FY29. This is consistent with management's statement that 2H instrument growth will not match 1H (JPM 2026-07-31), but it sits awkwardly with placements running at 80-95 a quarter against a 50-60 framework, and with the 4Q26E sequencing-instrument figure of $128M (-16.6% y/y).
- **FY27E is a 6.3% reported growth number on a 53-week base.** If management's own 0.5-point extra-week figure is right, underlying FY27E growth is about 6.8%; ex-Greater China consensus FY27E is +7.1% (4,729 vs 4,414). Management's 2027 target is "high-single-digit" revenue growth excluding China [D: JPM 2026-02-06], so **consensus sits at the low edge of the target on a calendar-adjusted, ex-China basis and does not assume the multiomics 1-2 points on top**. FY28E ex-China is +7.3%.
- **Margins: consensus is below the 26% target in 2027.** FY27E 25.2% vs management's 26.0% adjusted operating margin goal for 2027 [D: JPM 2026-02-06]; FY28E 26.5%. The FY27E incremental operating margin is 50% (change in operating income $146M on change in revenue $293M), against 30% in FY26E when SomaLogic dilutes margin by about 100 bp.
- **EPS growth is operating leverage, not buybacks.** FY27E EPS +14.0% ($5.36 to $6.11) with net income +14.1% and diluted shares -0.3% (153.1M to 152.7M). Buybacks are modelled at $313M in FY27E, about 1.1M shares or 0.7% of the count at $278, so the share count barely moves.
- **Buyback and balance-sheet lines look stale.** Quarterly 3Q26E-4Q26E repurchases are $90.5M each, while the annual FY26E figure is $420M (H1 actual was $370M), so the two sheets disagree by about $130M. The annual debt lines carry the $500M term notes as current through 2027, whereas Seeking Alpha reports the $500M 2026 notes matured on 9 September 2026 and a $300M 2029 note was issued in August (SA 2026-09-08).

### A3. Quarterly, 1Q25 to 4Q28E

Quarterly actuals are 1Q25-2Q26 [D]; 3Q26E-4Q28E are consensus [E: BBG cons]. The 2025 and 2026 quarterlies come from the first quarterlies file (1Q25-2Q27E) and the second file (3Q26E-4Q28E); the overlapping estimate quarters 3Q26E-2Q27E are identical in both files. Reminder: Bloomberg labels 3Q26 as ending 4 October; management says 4Q26 has the extra week (section 0).

Revenue build and geography. The point: consensus has total revenue stepping through $1,154M (3Q26E) and $1,220M (4Q26E), then repeating the seasonal shape (Q1 weakest, Q4 strongest) at 5-8% growth.

| $M | 1Q25 | 2Q25 | 3Q25 | 4Q25 | 1Q26 | 2Q26 | 3Q26E | 4Q26E | 1Q27E | 2Q27E | 3Q27E | 4Q27E | 1Q28E | 2Q28E | 3Q28E | 4Q28E |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Revenue | 1,041 | 1,059 | 1,084 | 1,159 | 1,091 | 1,159 | 1,154 | 1,220 | 1,160 | 1,218 | 1,229 | 1,292 | 1,246 | 1,316 | 1,333 | 1,400 |
| Product revenue | 880 | 912 | 927 | 990 | 917 | 982 | 977 | 1,028 | 977 | 1,031 | 1,045 | 1,098 | 1,056 | 1,120 | 1,143 | 1,199 |
| Total consumables | 768 | 811 | 816 | 832 | 797 | 852 | 861 | 894 | 863 | 914 | 932 | 967 | 935 | 995 | 1,023 | 1,054 |
| Sequencing consumables | 696 | 740 | 747 | 755 | 726 | 775 | 789 | 815 | 792 | 839 | 860 | 888 | 867 | 923 | 953 | 977 |
| Microarray consumables | 72 | 71 | 69 | 77 | 71 | 77 | 73.6 | 80.7 | 72.3 | 77.1 | 74.1 | 81.2 | 73.3 | 78.1 | 75.5 | 83.1 |
| Total instruments | 112 | 101 | 111 | 158 | 120 | 130 | 115 | 132 | 111 | 114 | 112 | 127 | 114 | 116 | 114 | 137 |
| Sequencing instruments | 109 | 96 | 107 | 154 | 118 | 125 | 110 | 128 | 110 | 111 | 108 | 124 | 114 | 116 | 111 | 135 |
| Microarray instruments | 3 | 5 | 4 | 4 | 2 | 5 | 4.2 | 4.3 | 2.3 | 4.8 | 4.1 | 4.2 | 2.4 | 4.7 | 4.0 | 4.2 |
| Service & other | 161 | 147 | 157 | 169 | 174 | 177 | 178 | 189 | 181 | 187 | 186 | 197 | 187 | 195 | 192 | 206 |
| Sequencing service | 142 | 136 | 147 | 157 | 151 | 154 | 156 | 165 | 157 | 160 | 163 | 171 | 162 | 166 | 170 | 180 |
| Microarray service | 19 | 11 | 10 | 12 | 23 | 23 | 23.5 | 25.9 | 24.1 | 26.6 | 24.2 | 26.7 | 24.9 | 29.1 | 23.9 | 27.1 |
| Total sequencing revenue | 947 | 972 | 1,001 | 1,066 | 995 | 1,054 | 1,055 | 1,107 | 1,058 | 1,108 | 1,130 | 1,181 | 1,143 | 1,204 | 1,242 | 1,298 |
| Total microarray revenue | 94 | 87 | 83 | 93 | 96 | 105 | 101 | 111 | 99.0 | 110 | 103 | 112 | 101 | 115 | 103 | 114 |
| Greater China | 72 | 63 | 52 | 55 | 52 | 56 | 50.9 | 51.9 | 44.7 | 46.9 | 46.5 | 48.8 | 42.8 | 44.9 | 46.3 | 47.0 |

Profit and loss. The point: operating margin steps from 22.4% (2Q26) to 24.0% (3Q26E, which equals the company's ~24% guide) and 25.6% (4Q26E), then 29.7% by 4Q28E.

| $M | 1Q25 | 2Q25 | 3Q25 | 4Q25 | 1Q26 | 2Q26 | 3Q26E | 4Q26E | 1Q27E | 2Q27E | 3Q27E | 4Q27E | 1Q28E | 2Q28E | 3Q28E | 4Q28E |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gross profit | 702 | 735 | 750 | 777 | 744 | 790 | 793 | 836 | 797 | 846 | 855 | 898 | 869 | 930 | 943 | 985 |
| Cost of revenue | 358 | 364 | 351 | 400 | 370 | 389 | 374 | 402 | 374 | 386 | 391 | 415 | 389 | 402 | 410 | 445 |
| Adj. SG&A | 248 | 241 | 256 | 264 | 267 | 278 | 271 | 273 | 278 | 284 | 280 | 285 | 287 | 297 | 292 | 297 |
| Adj. R&D | 241 | 243 | 228 | 238 | 239 | 252 | 247 | 249 | 246 | 259 | 255 | 258 | 255 | 269 | 266 | 268 |
| Total adj. opex | 519 | 481 | 506 | 557 | 512 | 525 | 531 | 544 | 532 | 547 | 546 | 558 | 552 | 565 | 565 | 563 |
| Adj. operating income | 212 | 252 | 265 | 275 | 239 | 260 | 277 | 312 | 274 | 300 | 317 | 350 | 323 | 356 | 378 | 415 |
| Adj. EBITDA | 264 | 303 | 332 | 326 | 291 | 278 | 324 | 365 | 340 | 370 | 386 | 421 | 367 | 403 | 428 | 470 |
| Other non-op income | 15 | 10 | 13 | 16 | 15 | 8 | 15.6 | 16.2 | 14.7 | 15.3 | 14.7 | 14.5 | 16.0 | 15.9 | 15.8 | 15.6 |
| Adj. net income | 154 | 187 | 206 | 208 | 177 | 200 | 207 | 235 | 203 | 228 | 240 | 264 | 238 | 271 | 287 | 310 |
| Diluted shares (M) | 159 | 157 | 154 | 154 | 154 | 153 | 153 | 153 | 152 | 153 | 153 | 153 | 153 | 153 | 153 | 153 |
| Adj. diluted EPS ($) | 0.97 | 1.19 | 1.34 | 1.35 | 1.15 | 1.31 | 1.36 | 1.54 | 1.35 | 1.47 | 1.55 | 1.71 | 1.62 | 1.78 | 1.89 | 2.05 |
| GAAP operating income | 164 | 214 | 227 | 202 | 209 | 245 | 245 | 277 | 238 | 269 | 283 | 317 | 275 | 309 | 327 | 363 |
| GAAP net income | 131 | 235 | 150 | 334 | 134 | 207 | 195 | 218 | 184 | 212 | 222 | 246 | 218 | 252 | 263 | 292 |
| GAAP diluted EPS ($) | 0.82 | 1.49 | 0.98 | 2.16 | 0.87 | 1.35 | 1.28 | 1.43 | 1.21 | 1.38 | 1.43 | 1.58 | 1.44 | 1.65 | 1.72 | 1.89 |
| SBC | 73 | 69 | 70 | 63 | 60 | 73 | 74.6 | 73.9 | 78.9 | 73.6 | 74.0 | 73.3 | 87.5 | 78.0 | 78.7 | 76.2 |

Cash flow and balance sheet. The point: consensus free cash flow is $284-358M a quarter from 3Q26E, with 3Q26E at $335M a 39% margin that is inconsistent with its own operating cash flow less capex ($326M - $51M = $275M); treat the 3Q26E FCF as a contributor-set artefact.

| $M | 1Q25 | 2Q25 | 3Q25 | 4Q25 | 1Q26 | 2Q26 | 3Q26E | 4Q26E | 1Q27E | 2Q27E | 3Q27E | 4Q27E | 1Q28E | 2Q28E | 3Q28E | 4Q28E |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cash flow from operations | 240 | 234 | 284 | 321 | 289 | 201 | 326 | 354 | 349 | 372 | 355 | 389 | 388 | 371 | 377 | 405 |
| Capex | 32 | 30 | 31 | 55 | 38 | 40 | 51.4 | 58.2 | 44.2 | 46.7 | 47.4 | 54.3 | 41.9 | 45.8 | 46.9 | 58.3 |
| Free cash flow | 208 | 204 | 253 | 267 | 251 | 162 | 335 | 284 | 314 | 294 | 305 | 315 | 354 | 334 | 340 | 358 |
| Share repurchase | 200 | 370 | 130 | 42 | 242 | 128 | 90.5 | 90.5 | 62.7 | 62.7 | 62.7 | 62.7 | 83.5 | 83.5 | 83.5 | 83.5 |
| Cash & equivalents | 1,113 | 934 | 1,050 | 1,418 | 1,089 | 1,040 | 1,224 | 1,447 | 1,696 | 1,951 | 2,211 | 2,382 | 2,466 | 2,740 | 3,010 | 3,301 |
| Short-term investments | 124 | 221 | 228 | 215 | 66 | 128 | 105 | 112 | 110 | 110 | 110 | 118 | 103 | 103 | 103 | 103 |
| Current debt | 499 | 499 | 998 | 499 | 499 | 500 | 507 | 507 | 508 | 508 | 508 | 508 | 500 | 500 | 450 | 450 |
| Long-term debt | 1,491 | 1,492 | 994 | 1,490 | 1,490 | 1,491 | 1,591 | 1,528 | 1,533 | 1,533 | 1,533 | 1,533 | 1,550 | 1,550 | 1,490 | 1,490 |
| Net debt (Bloomberg ratio row) | 753 | 836 | 714 | 356 | 834 | 823 | 1,117 | 364 | 831 | 688 | 516 | -539 | 1,163 | 1,163 | 1,163 | -615 |
| Shareholders equity | 2,368 | 2,258 | 2,381 | 2,723 | 2,676 | 2,838 | 2,999 | 3,163 | 3,434 | 3,654 | 3,977 | 4,223 | 4,646 | 4,944 | 5,262 | 5,383 |
| Accounts receivable | 699 | 701 | 729 | 854 | 738 | 764 | 768 | 818 | 775 | 796 | 811 | 877 | 839 | 857 | 884 | 968 |
| Inventories | 537 | 575 | 590 | 564 | 611 | 629 | 608 | 620 | 571 | 598 | 602 | 622 | 639 | 672 | 691 | 707 |
| Total assets | 6,182 | 6,087 | 6,177 | 6,644 | 6,559 | 6,650 | 6,313 | 7,038 | 6,522 | 6,746 | 7,028 | 7,959 | 7,280 | 7,554 | 7,823 | 9,117 |

Regions as printed (basis warning applies to everything except Greater China). A like-for-like view for 1Q26 and 2Q26 on the company's new regions, from Ameriprise (2026-05-01, 2026-07-31) and JPM (2026-05-01, 2026-08-05): USCAN $590M (+6.3% reported, +5% organic) and $653M (+14.8% reported, +13% organic); EMEALA $356M (+7.2% reported, +1% organic) and $368M (+3.7% reported, flat organic); APAC $93M (+13.4%) and $82M (+13.9% reported, +9% organic); Greater China $52M (-27.8%) and $56M (-11.1%, JPM organic -19%) [D].

| $M | 1Q25 | 2Q25 | 3Q25 | 4Q25 | 1Q26 | 2Q26 | 3Q26E | 4Q26E | 1Q27E | 2Q27E | 3Q27E | 4Q27E | 1Q28E | 2Q28E | 3Q28E | 4Q28E |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Americas / USCAN (as printed) | 570 | 586 | 612 | 638 | 590 | 653 | 661 | 696 | 675 | 704 | 720 | 755 | 739 | 776 | 796 | 829 |
| Europe / EMEALA (as printed) | 293 | 310 | 309 | 353 | 356 | 368 | 332 | 379 | 339 | 358 | 357 | 408 | 364 | 385 | 384 | 439 |
| Greater China | 72 | 63 | 52 | 55 | 52 | 56 | 50.9 | 51.9 | 44.7 | 46.9 | 46.5 | 48.8 | 42.8 | 44.9 | 46.3 | 47.0 |
| APMEA / APAC (as printed) | 106 | 100 | 111 | 113 | 93 | 82 | 113 | 113 | 110 | 128 | 122 | 129 | 114 | 136 | 133 | 145 |

### A4. Quarterly growth, margins and implied quarters [Der]

The next table shows year-over-year growth for each line and the margin path. The points: (1) revenue growth of 5.1-6.5% through 2027 and 7.4-8.5% in 2028; (2) sequencing consumables growth accelerates from +4.7% (2Q26 actual) to +7.9% (4Q26E) and +9.0-9.4% in 1H27E; (3) instruments swing from +30% (2Q26) to -17% (4Q26E) and -7% to -12% in 1H27E; (4) incremental operating margins run 50-67% from 4Q26E onward, against 8-17% in 2Q-3Q26 when SomaLogic, freight and memory costs bit.

| y/y (Der) | 1Q26 | 2Q26 | 3Q26E | 4Q26E | 1Q27E | 2Q27E | 3Q27E | 4Q27E | 1Q28E | 2Q28E | 3Q28E | 4Q28E |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Revenue | +4.8% | +9.4% | +6.5% | +5.2% | +6.3% | +5.1% | +6.5% | +5.9% | +7.4% | +8.1% | +8.5% | +8.3% |
| Product revenue | +4.2% | +7.7% | +5.4% | +3.9% | +6.5% | +5.0% | +7.0% | +6.8% | +8.1% | +8.6% | +9.4% | +9.3% |
| Total consumables | +3.8% | +5.1% | +5.5% | +7.5% | +8.3% | +7.3% | +8.2% | +8.1% | +8.4% | +8.9% | +9.8% | +9.0% |
| Sequencing consumables | +4.3% | +4.7% | +5.6% | +7.9% | +9.1% | +8.2% | +8.9% | +9.0% | +9.4% | +10.0% | +10.9% | +10.0% |
| Microarray consumables | -1.4% | +8.5% | +6.7% | +4.9% | +1.9% | +0.1% | +0.7% | +0.6% | +1.3% | +1.3% | +1.8% | +2.3% |
| Total instruments | +7.1% | +28.7% | +3.8% | -16.8% | -7.4% | -12.3% | -3.1% | -3.6% | +2.7% | +2.1% | +2.4% | +8.4% |
| Sequencing instruments | +8.3% | +30.2% | +2.5% | -16.6% | -7.0% | -11.1% | -1.7% | -3.8% | +3.9% | +4.3% | +3.3% | +9.7% |
| Service & other | +8.1% | +20.4% | +13.6% | +11.9% | +4.0% | +5.6% | +4.4% | +4.3% | +3.5% | +4.3% | +3.2% | +4.2% |
| Sequencing service | +6.3% | +13.2% | +6.4% | +4.9% | +3.7% | +4.2% | +4.3% | +4.1% | +3.2% | +3.4% | +3.9% | +4.9% |
| Gross profit | +6.0% | +7.5% | +5.7% | +7.6% | +7.2% | +7.0% | +7.8% | +7.4% | +9.0% | +10.0% | +10.4% | +9.6% |
| Adj. operating income | +12.7% | +3.2% | +4.5% | +13.6% | +14.8% | +15.2% | +14.5% | +12.1% | +17.6% | +18.7% | +19.1% | +18.6% |
| Adj. EBITDA | +10.2% | -8.3% | -2.4% | +12.0% | +16.7% | +33.1% | +19.3% | +15.3% | +8.0% | +8.9% | +10.7% | +11.6% |
| Adj. net income | +14.9% | +7.2% | +0.5% | +13.0% | +14.6% | +13.6% | +15.8% | +12.1% | +17.4% | +19.0% | +19.5% | +17.8% |
| Adj. diluted EPS ($) | +18.6% | +10.1% | +1.5% | +14.1% | +17.4% | +12.2% | +14.0% | +11.0% | +20.0% | +21.1% | +21.9% | +19.9% |
| Free cash flow | +20.7% | -20.6% | +32.5% | +6.3% | +24.9% | +81.7% | -9.1% | +10.8% | +13.0% | +13.5% | +11.5% | +13.8% |
| Greater China | -27.8% | -11.1% | -2.2% | -5.7% | -14.1% | -16.2% | -8.6% | -5.8% | -4.2% | -4.3% | -0.5% | -3.8% |
| Total adj. opex | -1.3% | +9.1% | +4.9% | -2.4% | +4.0% | +4.3% | +2.9% | +2.6% | +3.7% | +3.1% | +3.3% | +1.0% |
| Revenue ex-Greater China | +7.2% | +10.7% | +6.9% | +5.8% | +7.3% | +6.2% | +7.2% | +6.5% | +7.9% | +8.6% | +8.8% | +8.8% |
| Adj. gross margin (BBG stated) | 68.2% | 68.2% | 68.8% | 68.7% | 68.8% | 69.2% | 69.3% | 69.0% | 69.5% | 69.9% | 70.2% | 69.6% |
| Adj. operating margin | 21.9% | 22.4% | 24.0% | 25.6% | 23.7% | 24.6% | 25.8% | 27.1% | 25.9% | 27.0% | 28.3% | 29.7% |
| Op. margin change y/y (bps) | +154 | -136 | -46 | +189 | +175 | +217 | +181 | +148 | +223 | +242 | +252 | +255 |
| Incremental op. margin y/y | 54% | 8% | 17% | 62% | 52% | 67% | 54% | 52% | 56% | 57% | 58% | 60% |
| Consumables % of revenue | 73.1% | 73.5% | 74.6% | 73.3% | 74.4% | 75.1% | 75.8% | 74.8% | 75.1% | 75.6% | 76.7% | 75.2% |
| Seq. consumables q/q | -3.8% | +6.7% | +1.8% | +3.3% | -2.8% | +5.9% | +2.5% | +3.3% | -2.4% | +6.4% | +3.3% | +2.5% |

SG&A plus R&D (the "core" opex that JPM quotes as $502M in 4Q25 and $506M in 1Q26) grows [Der]: 1Q26 +3.5%, 2Q26 +9.5%, 3Q26E +6.9%, 4Q26E +4.0%, then +2.4% to +4.3% a quarter through 2028. Bloomberg's separate "Total operating expenses" row includes other items (for example $557M versus $502M in 4Q25), so a y/y on that row is not meaningful and I have not shown it.

**Implied quarters and halves from the full-year consensus.**

| Item | Calculation [Der] | Result |
|---|---|---|
| FY26E revenue minus 1H actual minus 3Q26E | 4,624.8 - 1,091 - 1,159 - 1,154.2 | **Implied 4Q26 = $1,220.6M** (sheet shows $1,219.8M) |
| 2H26E revenue and growth | 1,154.2 + 1,219.8 = 2,374.0 vs 2,243 in 2H25 | +5.8% (vs +7.1% in 1H26: 2,250 vs 2,100) |
| 4Q26E revenue y/y | 1,219.8 / 1,159 | +5.2% (+5.8% ex-China); includes the extra week if management is right |
| FY26E EPS minus 1H actual | 5.36 - 1.15 - 1.31 | 2H26E = $2.90; 3Q26E $1.36, **implied 4Q26E $1.54** (guide-implied $1.535) |
| FY26E operating income minus 1H actual | 1,088.5 - 239 - 260 | 2H26E = $589M; 3Q26E $277M, **4Q26E $312M = 25.6% margin** |
| FY26E sequencing consumables | 3,104.4 - 726 - 775 | 2H26E $1,603M (+6.8% y/y vs 1H +4.5%); implied 4Q26E $814M (+7.9%) |
| FY26E total instruments | 500.4 - 120 - 130 | 2H26E $250M; 4Q26E implied $135M (sheet $131.5M) |
| FY26E service and other | 718.7 - 174 - 177 | 2H26E $368M (+12.8% on 2H25 $326M); BioInsight revenue and SomaLogic annualise here |
| Quarterly sum vs annual, FY27E | 4,898.8 vs 4,918.3; EPS 6.08 vs 6.11 | quarterly 0.4% below annual revenue |
| Quarterly sum vs annual, FY28E | 5,295.8 vs 5,262.8; EPS 7.34 vs 7.01 | quarterly 0.6% above on revenue, **4.7% above on EPS** |

Two conclusions for the primer. First, 4Q26E needs operating margin above 25.5% and EPS of $1.54 to hit the guidance midpoint; Seeking Alpha makes the same point (Q4 margin "above 25%" needed) (SA 2026-09-08), and BI says 3Q guidance was "a touch softer than consensus" and 4Q needs "a more marked step-up" (BI 2026-07-31). Second, the cushion is thin on paper but management has beaten the EPS consensus by $0.08-$0.18 in each of the last five reports (BI 2025-08-01: +$0.18; BI 2025-10-31: +$0.17; JPM 2026-02-06: $1.35 vs $1.21; Barclays 2026-05-07: $1.15 vs $1.05; Barclays 2026-07-31: $1.31 vs $1.23) [D / E: cons].

### A5. Data-quality flags in the three printouts

- **Regional basis break.** Bloomberg's 1Q25-4Q25 regional actuals are on the old basis (Americas $570M, Europe $293M, APMEA $106M in 1Q25) while the company restated 1Q25 on the new basis as USCAN $555M, EMEALA $332M, APAC $82M, Greater China $72M (Ameriprise 2026-05-01). The 3Q26E onward estimates appear to be on a third, mixed basis: Europe 3Q26E of $332M is below 2Q26's $368M, APMEA jumps from $82M (2Q26) to $113M (3Q26E), and a separate "prior disclosure EMEA" row ($355M, $387M) is shown only for estimate periods.
- **GAAP gross profit FY26E $2,740M** against a stated 67.49% GAAP margin (which would be $3,121M): the dollar figure is wrong or from a different contributor set.
- **Gross profit vs stated margin** disagree slightly in forward years (for example FY29E gross profit $4,045M is 71.6% of revenue, while the stated margin is 70.03%); I use the stated margin in text.
- **Net income of $1,161M loss in FY23 and $1,223M loss in FY24** reflect Grail consolidation and impairments; adjusted lines exclude them.
- **Core Illumina 2025 revenue** printed as $3,709M equals product revenue, not total.
- **FCF margin FY26E printed as 24.95%** against my $997M / $4,625M = 21.6%.
- **2032E column** (diluted shares up to 164.9M from 149.4M, product revenue +19.7%, GAAP net income above adjusted, paid-in capital down $2.1B) should be discarded.
- **Net debt per share, book value per share, ROE and the cash-versus-cash-and-short-term-investments rows** swing irregularly between quarters (for example 3Q26E cash plus short-term investments $847M is below cash alone at $1,224M); do not use them.
- **Quarterly adjusted pre-tax income 1Q26 $131M** is a data error (operating income $239M plus other income $15M is $254M); adjusted net income $177M is consistent with the correct figure.
- **Stock-based compensation and "other assets"** are printed with a unit slip (for example 7300 for $73.0M); values in my tables are corrected.
- **Goodwill** in the second quarterlies file prints as "128400" (should be $1,284M).
- **EBITDA** quarterly sums to $1,225M for 2025 versus the annual $1,208M, a $17M difference in the actual year, so Bloomberg's own EBITDA definition is not fully consistent between sheets.

---

## PART B. Sell-side and independent research (31 notes)

### B0. Register of the 31 notes

The table lists every note by publication date as printed inside the note (the filename prefix is sometimes a few days later, shown in brackets where it differs). "Price" is the share price the note itself cites. Ratings and targets are [E: firm]. Bloomberg Intelligence (BI) and Seeking Alpha give no rating or target. Of the 31: JPM 8, UBS 4, Barclays 3, Freedom Broker 4, Ameriprise 3, Bloomberg Intelligence 8, Seeking Alpha 1.

| # | Date (file prefix) | Firm, author | Rating and target | Price | One-line content |
|---|---|---|---|---|---|
| 1 | 2025-11-13 | BI, Palmer | none | n/a | Business profile: lineup, $125B opportunity, government about half of sales, clinical shift, consumables 60% of sequencing revenue |
| 2 | 2025-11-13 | BI, Palmer | none | n/a | M&A and Grail history; Solexa "one of the best deals" |
| 3 | 2026-01-13 | BI, Palmer/Zandi | none | n/a | Reaction to the 4Q25 preannouncement: execution gives "a higher floor" |
| 4 | 2026-01-13 (0116) | JPM, Woodring | Neutral, $130 (set 15 Dec 25) | $145.55 | Alert on 4Q25 preannouncement |
| 5 | 2026-02-06 | Ameriprise, Macino | Buy, no target (FactSet cons. $135.89) | $133.61 | 4Q25 and FY26 guide |
| 6 | 2026-02-06 / 03-11 / 04-24 | BI | none | n/a | Equity outlook with 1Q26 preview |
| 7 | 2026-02-10 | Freedom Broker, Zubkov | Buy, $130 to $140 | $117.25 | "Steady plans for 2026" |
| 8 | 2026-02-06 (0211) | JPM | Neutral, $130 to $120 (Dec-26) | $133.61 | 4Q25 recap; competitive uncertainty ahead of AGBT |
| 9 | 2026-02-05 (0211) | UBS, Leonard | Neutral, $120 to $135 | $133.61 | Clinical signal encouraging; 15x 2027E EV/EBITDA |
| 10 | 2026-02-05 (0212) | Barclays, Sergott | Underweight, $110 | $133.61 | "Getting ready for the main event" (AGBT), 2H-weighted guide |
| 11 | 2026-02-19 (0224) | UBS | Neutral, $135 | $120.09 | Fast take on Element's VITARI |
| 12 | 2026-02-26 (0303) | JPM | Neutral, $120 | $121.87 | Roche prices Axelios 1 at $150 per genome |
| 13 | 2026-02-26 (0303) | UBS | Neutral, $135 | $121.87 | Roche update "as expected"; counting applications vulnerable |
| 14 | 2026-02-26 (0304) | UBS | Neutral, $135 | $127.40 | Expert feedback (n=4) on Axelios; mixed |
| 15 | 2026-05-01 | Ameriprise | Buy, no target (cons. $136.11) | $126.74 | 1Q26 beat and raise |
| 16 | 2026-05-01 | Freedom Broker | Buy, $140 | $126.74 | Flash note: after-hours -1% "unjustified" |
| 17 | 2026-05-01 (+07-23 piece) | BI | none | n/a | Outlook with 2Q26 preview |
| 18 | 2026-05-06 | Freedom Broker | Buy, $140 to $155 | $139.07 | Instruments drive the raise |
| 19 | 2026-05-01 (0506) | JPM | Neutral, $120 to $125 | $120.37 | 1Q26 recap; pricing and competition uncertainty |
| 20 | 2026-04-30 (0507) | Barclays | Underweight, $110 to $122 | $126.74 | "If you seed it, the consumable revs will come...right?" |
| 21 | 2026-06-10 (0615) | JPM | **Upgrade to Overweight, $125 to $185** (Dec-26) | $160.03 | Sticky clinical base; survey of 62 customers |
| 22 | 2026-06-10 (0615) | JPM | (header shows Neutral, pre-upgrade) | $160.03 | The survey report itself |
| 23 | 2026-06-26 | BI | none | n/a | Sequencing "enters a more competitive era" (Axelios vs NovaSeq X) |
| 24 | 2026-07-16 (0721) | JPM | Overweight, $185 to $220 (Dec-26) | $187.15 | Model update |
| 25 | 2026-07-31 | Ameriprise | Buy, no target (cons. $175.72) | $205.09 | 2Q26 beat; guide up |
| 26 | 2026-07-31 | BI | none | n/a | Compilation of 76 earnings previews and outlooks, 2017-2026 |
| 27 | 2026-07-31 | BI | none | n/a | Equity outlook after 2Q26 |
| 28 | 2026-08-05 | Freedom Broker | **Downgrade to Hold**, $155 to $185 | about $203 | "Much of the upside is now priced in" |
| 29 | 2026-07-31 (0805) | JPM | Overweight, $220 to $230 (Dec-27) | $205.09 | 2Q26 recap; DCF rolled to Dec-27 |
| 30 | 2026-07-31 (0806) | Barclays | Underweight, $145 to $160 | $205.09 | "Once a prom king, always a prom king" |
| 31 | 2026-09-08 | Seeking Alpha, Ayers | Hold, DCF value $188 | $218.65 (page header: $278.17 at print) | "Priced for perfection it hasn't earned yet" |

**The key staleness fact.** The newest broker note in the folder is Barclays/JPM/Ameriprise of 31 July and Freedom of 5 August. The last item of any kind is Seeking Alpha on 8 September. The Seeking Alpha page header, printed on 10 October, shows ILMN at **$278.17**, +27.2% in the 33 days since publication versus +1.2% for the S&P 500 [D: SA page header, not the author's analysis]. Every price target in the folder (highest $230, JPM) is below that price. No sell-side commentary in the folder explains the move from about $205 (30 July) to about $278 (10 October).

---

### B1. Note-by-note detail

#### J.P. Morgan (Casey Woodring and team): 8 notes

**JPM-1, 13 Jan 2026 alert (4Q25 preannouncement).** Neutral; target $130 set 15 Dec 2025; price $145.55 on 12 Jan [E: JPM]. Preannounced 4Q25 revenue about $1.16B vs Street $1.10B and guide $1.09-1.13B; +4% constant currency vs guide of about flat; ex-China about $1.10B, +7% cc vs guide about +4%; non-GAAP EPS $1.27-1.30 vs Street $1.21 [D]. Investor focus list: NovaSeq X transition pace, launches, multiomics entry strategy, China/unreliable-entity list, mid-term targets. No estimate change.

**JPM-2, 6 Feb 2026 (4Q25 recap).** Neutral; target cut **$130 to $120** (Dec-26 DCF; WACC 10.2%, terminal growth 4.0%) with the stock at $133.61, i.e. a target 10% below the price [E: JPM]. Reasons: "ongoing competitive concerns and pressured pricing dynamics"; "pushback on the 2H margin ramp implied by the guide". Estimates: FY26 EPS $5.12 (guide $5.05-5.20, BBG $5.07), **FY27 raised to $6.02 from $5.81** (BBG $5.77); revenue $4,549M / $4,886M / $5,147M / $5,429M for FY26-FY29 (FY28 growth 5.4%); EPS FY28 $6.55, FY29 $7.14. Net cash modelled from FY26; no buybacks modelled. Data [D]: 4Q25 sequencing consumables $755M +8% cc (+11% ex-China, $713M); clinical +20% ex-China; total activity on high- and mid-throughput instruments +30% y/y in both 3Q25 and 4Q25; >100 NovaSeq X placements, installed base about 890, >60% of Q4 X placements to clinical; adjusted gross margin 67.0% (-40 bp, tariffs -205 bp); free cash flow $267M vs Street $412M. 2026 guide [D]: organic +1-3% (ex-China +2-4%), $4.50-4.60B vs Street $4.41B; instruments -LSD to flat with 50-60 X placements a quarter; consumables +LSD-MSD ex-China; clinical consumables +DD to mid-teens; research and applied consumables -MSD to -HSD; China $210-220M; operating margin 23.3-23.5% (SomaLogic about -100 bp); EPS $5.05-5.20 (SomaLogic -$0.18; ex-SomaLogic about +10%). 1Q26 guide below JPM and Street (EPS $1.02-1.07 vs Street $1.14). **Pricing [D, mgmt via JPM]:** pricing headwinds from the X transition should begin to ease in 2H26 because about 90% of academic high-throughput volume is already on the X; clinical is more than two-thirds converted; conversion "substantially complete" by end-2026. **Pull-through for 2026 [D]:** NovaSeq X $1.35-1.40M a year; NovaSeq 6000 $600-650k; NextSeq 1k/2k $80-100k; NextSeq 500/550 $90-110k. DCF terminal value 75-86% of EV. Sentiment: Bloomberg ratings 10 Buy / 11 Hold / 3 Sell. Risks listed: academic funding, competition and pricing, launch execution.

**JPM-3, 26 Feb 2026 alert (Roche Axelios 1 pricing).** Neutral, $120, price $121.87 [E: JPM]. Roche announced list consumables of **$150 per genome** (synthesis reagents and consumables only, excluding library prep, and assuming the sensor module is reused 20 times) vs about $200 for NovaSeq X, a headline discount of 25% [D: Roche via JPM]. JPM: "based on our conversations," most investors expected about $150 and some as low as $100, so the news was in line. SBX duplex mode 16 genomes per run, 64 a day, about $2,400 a run; Roche frames cost at about $0.06 per million reads; simplex more than 40B reads a run. cfDNA panel illustration $25 a sample (1.1 Mb, 2,000x, 96 samples). Reuse data: 15 of 16 sensor modules (94%) reached 20 uses; Roche says longer than one week is possible. No estimate change. Stock had fallen 18.9% in one month and 7.1% year to date by 25 Feb. Bloomberg ratings 11 Buy / 11 Hold / 3 Sell.

**JPM-4, 1 May 2026 (1Q26 recap).** Neutral; target **$120 to $125** (WACC 9.8%, terminal growth 4.0%); price $120.37 on 30 April [E: JPM]. Quote: "we remain on the sidelines until there is more visibility on how the landscape will evolve." Catalyst named: Roche Diagnostics Day on 12 May. Estimates: FY26 EPS $5.21 (BBG $5.12), FY27 $5.93 (BBG $5.81), FY28 $6.48 (BBG $6.62); revenue $4,573M / $4,799M / $5,075M / $5,414M. Data [D]: revenue $1,091M vs Street $1.07B; organic +1.2% (guide -1% to +1%); ROW organic +3.5%; sequencing consumables $726M (Street $722M), organic +2%, ROW +5%, **down 4% q/q, "the largest sequential decline in 1Q since 1Q20"**; clinical consumables +20% ROW for a second quarter and more than 65% of sequencing consumables; research and applied -12% ROW; total activity on high- and mid-throughput instruments +30% y/y, clinical "well above"; sequencing instruments $118M vs Street $102M; >80 X placements (vs >60 in 1Q25), installed base about 970, supply-constrained, several multi-unit clinical orders, some volume discounts and reagent-rental or lease placements; performance obligations up more than 20% y/y. Guidance raise was small (+$20M revenue; EPS $5.15-5.30; margin 23.4-23.6%; instruments now flat to +LSD; Q2 about 80 placements and more than 60 in each of Q3 and Q4; pull-through "about $1.3M per instrument or higher"). Q2 guide: revenue $1.12-1.14B, operating margin about 22% vs Street 23.5%. Management on pricing: with more than 90% of research and applied volume already on the X, associated pricing headwinds "to ease through the year". Free cash flow $251M vs Street $502M. Bloomberg ratings 11 / 9 / 3.

**JPM-5, 10 Jun 2026 (upgrade).** **Overweight; target $125 to $185** (Dec-26 DCF; WACC 9.1%, terminal growth 4.5%; EV $28,962M less net debt $328M = equity $28,634M = $185; terminal value 86% of EV; terminal EV/EBITDA 13.4x) on a price of $160.03 (+15.6% upside; stock +22.0% YTD, +88.3% over 12 months) [E: JPM]. Stated reasons: (1) clinical base is sticky: more than 40% of revenue is clinical consumables, 65%+ of sequencing consumables, all major CLIA labs are Illumina users and have moved or are moving to the X (76% of clinical high-throughput Gb on the X in 1Q26), pricing headwinds "largely gone exiting this year", underlying consumables volume growth "at least +30%" using Gb as proxy; (2) multi-year test-volume runway from therapy selection, MRD and MCED, with WGS needing about 15x the data of WES; (3) Roche manageable near term; (4) US A&G recovery into 2H26/2027 is the biggest upside, plus multiomics; (5) valuation. **How JPM builds +HSD organic growth from 2027:** ROW clinical sequencing consumables +low/mid-teens CAGR 2026-30; China clinical consumables -LDD and China sequencing consumables -mid-teens with no recovery; ROW research sequencing consumables +MSD CAGR; total sequencing consumables +LDD CAGR 2026-30; ROW sequencing instruments +MSD/HSD (research +MSD, clinical +HSD); gross margin "in the high 60s" because reagent rentals (LSD% of boxes today) may pressure ASPs; opex +MSD/HSD; adjusted EPS +mid/high-teens through 2030E. Estimates: revenue FY26-29 $4,583M / $4,919M / $5,401M (+9.8%) / $5,876M; EPS $5.23 / $5.98 / $7.01 / $8.11 (BBG $5.23 / $5.93 / $6.78). DCF cash flows: 2028 revenue growth 10%, EBIT margin 26%, 2030 EBIT margin 30%. Sensitivity grid in section B3. Valuation claim: the $185 target implies 19.7x 2027E EV/EBITDA vs 17.8x at the close and a Core Tools average of 15.6x, a premium of 4.1x vs a historical premium of about 15x (2015-2024). Multiomics: management says multiomics plus BioInsight add at least 100-200 bp to growth by 2027; JPM calls this upside, not core. Bloomberg ratings 12 / 6 / 3. Risks: Axelios attrition, delayed MRD/MCED guidelines, pricing, minimal funding improvement.

**JPM-6, 10 Jun 2026 (customer survey report).** Full detail in section B2. The cover shows "Neutral" and no target because the disclosure page pre-dates the same-day upgrade; treat the rating label as stale.

**JPM-7, 16 Jul 2026 (model update).** Overweight; target **$185 to $220** (Dec-26 DCF; WACC 8.9%, terminal growth 4.5%); price $187.15; market cap $28.3B [E: JPM]. Driver: balance sheet and cash flow from the latest 10-Q and "improved visibility into consumables-led growth and a more constructive long-term demand backdrop" in outer years. Estimates: revenue FY26-29 $4,583M / $5,000M (+9.1%) / $5,601M (+12.0%) / $6,199M (+10.7%); adjusted EPS $5.23 / $6.09 / $7.33 / $8.62; adjusted EBIT (after SBC) $825M / $953M / $1,163M / $1,386M. Multiples at $187.15: P/E 35.8x FY26E, 30.7x FY27E, 25.5x FY28E; EV/EBITDA 28.4x / 24.4x / 19.8x. Peer targets in the same note: Natera $315 (OW), Guardant $185 (OW), 10x Genomics $38 (Neutral, price $45.75), Alamar $32, Adaptive $25, BillionToOne $145.

**JPM-8, 31 Jul 2026 (2Q26 recap).** Overweight; target **$220 to $230, date rolled to Dec-27** (WACC printed as 9.8%, terminal growth 4.5%); price $205.09 [E: JPM]. The WACC printed here is higher than the 8.9% in the 16 July note even though the target rose, so the roll-forward and new cash flows more than offset it; the filing is ambiguous and the number should be checked against the original. Results [D]: revenue $1,159M, organic +6.5% (guide +3-5%), ROW +8.1% (guide +4-6%); sequencing instruments $125M (+30% organic, X and MiSeq i100); sequencing consumables $775M, +4% organic, ROW $734M +5%; **clinical consumables +15% ROW vs +20% in each of the prior two quarters** (US/Canada above +20%, "pockets of softness" in Middle East and Latin America); research and applied -7% ROW (vs -12%); service and other $177M vs Street $165M; adjusted gross margin 68.2% (-120 bp y/y), operating margin 22.5%; EPS $1.31 vs Street $1.23; free cash flow $162M vs Street $321M; >95 X placements (about 70% clinical; "as much as half of clinical placements appear to be incremental" vs 6000 upgrades), >10 NovaSeq 6000 placed, volume discounts continue; 78% of clinical volume on the X, 80-85% targeted by year-end. Guidance [D]: revenue $4.60-4.64B, organic >4%, ROW organic ~5%, EPS $5.30-5.40, operating margin 23.4-23.6% unchanged, clinical consumables **+mid-teens**, research -MSD/HSD unchanged, instruments +LSD. 3Q guide: organic ~+4.5%, revenue $1.14-1.16B, operating margin ~24%, EPS $1.33-1.38. **4Q:** management expects normal seasonality but a smaller 4Q decline than usual because of an extra week (about +0.5 point) and pull-through. 2H instrument growth will not match 1H; placements step down in 3Q and rebound in 4Q. BioInsight: Billion Cell Atlas over 300M cells, six biopharma partners (three added after quarter-end). Estimates: revenue $4,627M / $5,047M / $5,652M / $6,261M (growth 6.5% / 9.1% / 12.0% / 10.8%); EPS $5.34 / $6.16 / $7.41 / $8.73 (BBG $5.25 / $5.93 / $6.81); FCFF $839M / $975M / $1,124M / $1,393M. Multiples at $205.09: P/E 38.4x FY26E, 33.3x FY27E, 27.7x FY28E; EV/EBITDA 30.2x / 26.1x / 21.2x; EV/revenue 6.8x / 6.0x / 5.2x; FCFF yield 2.7% / 3.1% / 3.5%. Performance: +56.4% YTD, +92.3% over 12 months; Bloomberg ratings 13 / 6 / 3.

#### UBS (Dan Leonard, Lu Li; Kyle Crews or Nathan Bolanos): 4 notes

All four are Neutral with an asterisk: because ILMN is more volatile than average, UBS widens the Buy/Sell bands to plus or minus 15% of the market return assumption (8.5%) instead of 6% [E: UBS]. Neutral since at least November 2022. Target method: 12-month, based on TTM Dec-2027E EV/EBITDA.

**UBS-1, 5 Feb 2026.** Target **$120 to $135** on **about 15x (from 14x) 2027E EBITDA**; price $133.61; forecast return +1.0% vs the 8.5% hurdle (excess -7.4%) [E: UBS]. UBS raised the multiple "to reflect greater confidence in the growth trajectory" and keeps a discount to the Tools group "to reflect the lower relative growth outlook". Bottom line: Neutral "balances a muted sales growth outlook (lesser than peers') with outsized margin expansion opportunity". Encouraging: clinical NGS consumables +20% in 4Q25 and a mid-teens 2026 guide. Unfavourable: +1-3% organic guide "compares unfavorably" with peers. Estimates (old to new): FY26 EPS $5.19 to $5.07 (-2%; Street $5.07), FY27 $5.90 to $5.74 (-3%; Street $5.81), FY28 $6.65 to $6.54 (-2%; Street $6.45), now including SomaLogic dilution while "raising the 2027-and-beyond outlook to reflect better clinical growth". Forecasts: revenue FY26-30 $4,535M / $4,720M (+4.1%) / $5,022M / $5,348M / $5,690M; EBIT (UBS-adjusted) margin 23.1% in FY26E, 24.6%, 25.9%, 27.1%, 28.4% in FY30E; EPS FY29 $7.43, FY30 $8.40; net cash $208M FY26E rising to $4.8B FY30E; share count falling to 150M by FY30 (buybacks). Multiples at $133.61: P/E 26.4x FY26E, 23.3x FY27E; EV/EBITDA 16.5x / 14.5x. Quant review: all neutral, "no catalyst" in next three months. UBS holds a 0.5%+ position (disclosure).

**UBS-2, 19 Feb 2026 (Fast Take on Element VITARI).** Target $135 unchanged; price $120.09 after a roughly 10% fall from $133.61 on 5 Feb [E: UBS]. The garbled headline bullets say Element's VITARI has an instrument price about 40% below the NovaSeq X Plus (list $689k, implying about $410k), consumables cost per run about one tenth ($3k vs $32k), $/Gb about 50% lower, output per run about one fifth (3T vs 16T), shipping 2H26 [D: Element via UBS; garbled text, flagged]. Check [Der]: $3k / 3,000 Gb = $1.0/Gb vs $32k / 16,000 Gb = $2.0/Gb, consistent with "50% lower". Estimates unchanged (Street FY26 $5.13 / FY27 $5.82 / FY28 $6.58 vs UBS $5.07 / $5.74 / $6.54). P/E 23.7x FY26E, EV/EBITDA 14.8x at $120.09.

**UBS-3, 26 Feb 2026 (First Read, Roche).** Target $135; price $121.87; excess return +2.3% [E: UBS]. Roche's $150 per genome was "widely expect[ed]"; the update is "relatively benign" because (1) large Illumina customers are likely already at similar or better pricing and (2) Illumina's roadmap announced that week suggests about **$150 per genome on NovaSeq X+ if the 35B flow cell is priced consistently with the existing 25B flow cell**. **Where Illumina is more vulnerable: counting applications such as RNA-seq, priced per million reads: Roche about $0.06 vs Illumina's list $0.68 on the 25B flow cell** [D/E; decimals reconstructed from a garbled "$006"/"$068"]. UBS estimates counting applications are about **40% of Illumina's research usage, or about 16% of total sequencing consumables sales** (so research is implied at about 40% of sequencing consumables at that time; with research now about 35%, the counting exposure is about 14% [Der]). Early researcher feedback "skeptical": speed is Axelios's most compelling feature and has limited research relevance; cell barcode and UMI quality in simplex mode vs duplex is a concern for 10x single-cell; 20x reuse is a question for clinical. Estimates unchanged; Street FY27 $5.84.

**UBS-4, 26 Feb 2026 (First Read, expert feedback).** Target $135; price $127.40 (+4.5% on the day vs $121.87) [Der]. Four experts plus a Doc Debates call: one very negative, one very positive, two muted [E: UBS]. Positives: yields impressive (40B reads a run and 16 genomes a chip, versus 7 genomes a chip previously disclosed), reuse data clean with no carryover and "months, not weeks" of chip life, $150 a genome attractive "by a wide margin" against per-lane pricing. Negatives: library prep "very complicated" (duplex needs two adapters and Roche will not share the sequences); software and data format "hoops like the early days of Illumina"; one expert **already pays $175 a genome with Illumina discounts, thinks the 35B flow cell brings Illumina to $150 anyway, believes larger users are at $125 a genome, and had expected Roche at $100**; clinical reuse is "a big no, a nonstarter" for 50% of that expert's clinical users (the pathologists), especially for MRD; summer shipment "a stretch", at least six to eight months to be launch-ready. UBS: "initial take still holds", overhang should soften. Next call planned for 6 March.

#### Barclays (Luke Sergott, with Salem Salem and Anna Kruszenski): 3 notes

Underweight throughout (moved from Equal Weight on 10 Feb 2025); industry view Positive; downside and upside risks listed as innovation widening Illumina's edge and China fears not materialising [E: Barclays].

**BCS-1, 5 Feb 2026.** Target **$110 (unchanged) = 21x FY26 EPS $5.14** (prior 22x on $5.00); price $133.61, 17.7% downside; scenarios $150 up / $60 down [E: Barclays]. Thesis: 1Q guide "much softer than expected", a 2H-weighted ramp "just as stiff competition is expected in 2H"; investors read it as a market freeze or clinical slowdown; steep drop in high-throughput placements in 1Q after a strong 4Q; investors have "little risk appetite for a 2H-weighted guide". Management denied pull-forward. Competition: reports that **Roche would price at about $100 a genome**; Barclays sees **"another round of pricing headwinds in 2027 and beyond"** and research more at risk than sticky clinical. Estimates: FY26 EPS $5.14 (old $5.00; Bloomberg $5.07), FY27 $5.64 (old $5.53; Bloomberg $5.78); revenue $4,514M / $4,736M / $4,979M; EBIT $1,054M / $1,162M / $1,230M. Notes the guide embeds SomaLogic at +1.5-2% to revenue, -100 bp margin, -$0.18 EPS, and that management expects multiomics plus BioInsight to add **at least 1-2% to revenue growth in 2027** [D: 4Q25 call via Barclays].

**BCS-2, 30 Apr 2026.** Target **$110 to $122 = 23.5x FY26 EPS $5.17** (prior 21x on $5.11); price $126.74, 3.7% downside; scenarios $150 / $60 [E: Barclays]. Quote on instruments: placements beat Barclays' estimate by more than 50%, "Apparently ILMN didn't get the memo"; the placement beat produced only about 50 bp of revenue beat, which Barclays reads as the leasing programme working ("seeding the market with as many boxes as they can"); management says a customer will not lease a box "just to have one because this isn't 2014". **Bear point: in-line consumables and "what appears to be lower price/Gb on NSX volumes": X share of Gb up 500 bp but X share of consumables revenue flat at 55%.** Management calls reading that "a frivolous exercise" because of mix (new X volume on 25B flow cells vs 6000 volume on smaller panels that earn more per Gb). Barclays gives the benefit of the doubt but says it "warrants watching" and suggests Illumina may be discounting ahead of Roche and Ultima. Still Underweight because "not sold on the ability to deliver HSD growth in '27". Backlog about one quarter of revenue; margin guide "is not a layup" given a large 2Q-to-3Q step-up. Estimates: FY26 $5.17, FY27 $5.65 (Bloomberg $5.81), FY28 $5.97; revenue $4,576M / $4,785M / $5,047M.

**BCS-3, 31 Jul 2026.** Target **$145 to $160 = 28x FY27 EPS $5.73** (prior 28x on FY26 $5.21, roll-forward); price $205.09, **22.0% downside**; scenarios **$230 up / $100 down** [E: Barclays]. Key text: "not much to pick at this Q"; research is now only 35% of the business; the bull math "60% of the business grows more than 20%, and if research stabilizes, the result is double-digit growth"; but "the bull math ignores competition", which requires "continued price concessions, bundling, and favorable terms"; Barclays calls ILMN "a MSD business" and "cannot justify the 35x PE multiple it currently trades at, which screens at the top of the Tools industry"; "investors are assuming the +HSD% top line is in the bag". **Multiomics:** "beginning to bear fruit", management "on track to deliver 1-2% TW to growth next year", which is above Barclays' expectation, "without getting more clarity/disclosure on the business, we have no way to confirm these numbers". Competition: Axelios (the note attributes it to Element; context and Roche coverage suggest it means Roche's Axelios or Element's product, an apparent naming slip) "can take share of the research market given its pricing advantage in counting applications"; the **35B flow cell "will need to be priced to compete"** but "inherent technological barriers could ultimately prevent this". Estimates: FY26 EPS $5.34 (consensus $5.24), FY27 $5.73 (consensus $5.92, old $5.63), FY28 $6.02; revenue $4,609M / $4,862M / $5,105M; gross margin 68.4% / 67.8% / 67.9% (Barclays has gross margin falling in 2027-28); EBIT $1,084M / $1,181M / $1,248M; FCF $1,022M / $846M / $919M. P/E at $205.09: 38.4x FY26E, 35.8x FY27E.

#### Freedom Broker (Ilya Zubkov): 4 notes

Volatility-adjusted rating: Buy needs expected return divided by annualised volatility above 1.2; Hold between -1.2 and 1.2 (the 5 Aug note states a band of plus or minus 0.35 in its worked example, an internal inconsistency). Target method every time: **50% five-year FCFF DCF, 25% EV/Sales NTM, 25% P/E NTM** [E: Freedom]. Freedom discloses it expects to seek investment-banking compensation from Illumina.

**FB-1, 10 Feb 2026.** Buy; **$130 to $140**; price $117.25; multiples 7x EV/Sales and 30x P/E [E: Freedom]. Estimates: revenue $4,537M / $4,759M / $4,969M; EBIT $1,053M / $1,135M / $1,200M; EPS $5.06 / $5.61 / $5.82. Data [D]: China -31% in 4Q25; clinical consumables +20% in 4Q and +16% in 2H25; **X share of consumables revenue 44% at 2Q25 to 55% at year-end 2025; clinical X share of Gb 71%**; X transition complete in 2026 with 50-60 systems a quarter, about 60% to clinical; adjusted gross margin 67% (-40 bp, tariffs -205 bp). Views: research base case "moderately negative"; instruments stabilising, not growing; 2027 targets "realistic".

**FB-2, 1 May 2026 flash.** Buy; $140; price $126.74; after-hours reaction about -1% called "unjustified" [E: Freedom]. 1Q: ROW organic 3.5% "above management's guidance range"; sequencing instruments +9%; research and applied -12%; EPS +19% y/y. Expects "positive momentum" over the next one to two trading days. (Outcome: the stock was $139.07 five days later, +9.7% [Der].)

**FB-3, 6 May 2026.** Buy; **$140 to $155**; price $139.07; EV $22.8B [E: Freedom]. "Mostly due to expected higher instrument growth": instrument growth for the rest of 2026 raised **from flat to 5%**; guidance "appears conservative" and a beat-and-raise cycle may continue. Estimates new (old): revenue FY26 $4,601M ($4,537M), FY27 $4,824M ($4,759M), FY28 $5,036M ($4,969M); EBIT $1,080M / $1,183M / $1,335M; EPS **$5.31 / $5.70 / $6.37** (old $5.06 / $5.61 / $5.82). Consumables: 1Q $797M +3.8%; microarray consumables -20% ROW organic on large direct-to-consumer customers; X "may approach its peak" with 82% of Gb on the platform by end-2026 [E]; consumables to accelerate in 2H26 and 2027.

**FB-4, 5 Aug 2026.** **Downgrade to Hold; target $155 to $185**; price $203.01 (prior close $198.16), so the new target is 6.6% below the prior close [E: Freedom]. Multiples raised to 8x EV/Sales and 35x P/E. Quote: "following the recent appreciation in ILMN shares, we believe much of the anticipated acceleration in Illumina's fundamentals is now reflected in the stock price." Estimates new (old): revenue FY26 $4,637M ($4,601M), FY27 $4,900M ($4,824M), FY28 $5,151M ($5,036M); EBIT $1,087M / $1,232M / $1,365M; EPS **$5.38 / $5.98 / $6.59** (old $5.31 / $5.70 / $6.37); 3Q26E revenue $1,152M, EPS $1.38; 4Q26E $1,234M, $1.54 [E]. Segment detail [E]: consumables $3,386M / $3,591M / $3,788M (FY26-28; +4.9% / +6.1% / +5.5%); instruments $530M / $544M / $557M; service $721M / $764M / $805M. "No longer consider[s] management's outlook conservative"; future raises "more incremental". Data [D]: 2Q consumables $852M +5%, instruments $130M +29%, service $177M +20%; X is 83% of high-throughput Gb, 59% of high-throughput revenue, 78% of clinical; >10 NovaSeq 6000 shipped to customers planning to run it several more years; "mid-throughput sequencing portfolio" weak.

#### Ameriprise (Christopher Macino): 3 notes

Buy throughout since the stock was added to the Recommended List on 20 May 2021 at $385.31; no target of its own; uses forward P/E vs a 5-year average of **72.2x** (distorted by the GRAIL era) [E: Ameriprise]. The "FactSet consensus" tables inside are consensus, not Ameriprise's.

**AMP-1, 6 Feb 2026.** Price $133.61; forward P/E 26.0x; FactSet cons. target $135.89; FactSet FY26 revenue $4,490M / EPS $5.10; FY27 $4,766M / $5.82. 4Q25 [D]: revenue $1,159M (+5.0% reported, +4.0% cc, +7% ex-China cc) vs consensus $1,099M; EPS $1.35 vs $1.21; sequencing consumables $755M +8.2%; instruments $154M -0.6%; microarrays -7%; Greater China -31.3%; 100+ X placements, installed base 890; operating margin 23.7% (+400 bp). Also: BioInsight "more meaningful revenue" beginning 2027; SomaLogic spatial transcriptomics solution on track for 1H26. Recommendation to "more aggressive investors with multi-year time horizons": "view the recent weakness as an opportunity to accumulate".

**AMP-2, 1 May 2026.** Price $126.74; forward P/E 23.7x; cons. target $136.11; FactSet FY26 $4,557M / $5.18; FY27 $4,811M / $5.89. 1Q [D]: revenue $1,091M +4.8% (organic +1.2%); EPS $1.15 vs guide $1.05; clinical +20% ROW; >65% of sequencing consumables; **X is 55% of high-throughput consumables revenue and 82% of high-throughput Gb shipped**; research and applied about 90% transitioned, clinical 76% (80-85% targeted at year-end); >60% of placements clinical, "many representing incremental capacity rather than direct conversions from the NovaSeq 6000"; SomaLogic closed 30 Jan, net cash paid $363M plus $25M milestone after quarter-end; 18-month NovaSeq X roadmap with 14B and 35B flow cells, staggered flow-cell runs, improved Q70 accuracy; TruPath cuts hands-on time to about 10 minutes. Buyback: 2.0M shares for $242M at $120.85 average; new $1.5B authorisation on 28 April.

**AMP-3, 31 Jul 2026.** Price $205.09; forward P/E 36.4x (trailing 40.5x); cons. target **$175.72**, i.e. the stock was 17% above the consensus target; FactSet FY26 $4,603M / $5.30; FY27 $4,871M / $6.00 [E]. 2Q [D]: revenue $1,159M +9.4% (organic +6.5%); EPS $1.31 vs guide $1.23; sequencing instruments +30.2%; microarray service and other +109% (SomaLogic); **X is 83% of high-throughput Gb and 59% of high-throughput revenue**; clinical 78% on X, research and applied 92%; >10 NovaSeq 6000 placed, which Macino reads as proof the transition "is not an immediate shutdown of older capacity", and management calls "a normal transition dynamic rather than an identifiable consumables headwind"; clinical ROW consumables +15% (from +20%) blamed on the Middle East and Latin America. Multiomics: "Most multiomics products, including single-cell and TruPath, are booked within consumables revenue"; management still expects an incremental 1-2 points of growth in 2027; SomaLogic rebranded SomaScan and SomaSeq, tracking toward the high end of expectations; StrataMap Spatial launched with interest above internal expectations; BioInsight revenue now recognised in sequencing service and other. Free cash flow $162M (tax-payment timing and higher inventory to secure components). Buyback: 0.9M shares for $122M at $129.07 average; about $1.8B authorisation remaining. Analyst: the case "increasingly depends on" whether placements convert into sustained pull-through.

#### Bloomberg Intelligence (Jonathan Palmer, Adeline Zandi, Fallon Helmon): 8 notes

No ratings, targets or estimate tables in any of them; all statements are BI opinion unless marked as company data. Common themes across the eight: NovaSeq X plus new chemistry "should help defend market position"; the transition "has been painful"; China sanctions "cut the contribution in half" (China under 5% of sales); government funding is almost half of sales; Roche's return was "on the horizon" (Mar 2026), "a reality" (Jul 2026); the $125B long-term market and the $800M liquid-biopsy opportunity are old (2022 investor day) figures.

- **Register #1 and #2 (13 Nov 2025):** profile and M&A. Facts used elsewhere: consumables 60% of sequencing revenue; Grail spun 24 June 2024, Illumina kept 14.5%, EU fine $476M, $35-50M incremental spin charges; market cap peaked $76B in 3Q21.
- **#3 (13 Jan 2026):** 4Q25 preannouncement "modestly beat"; EPS growth on flat revenue "proves" self-help works; "creates a higher floor for the stock and significantly reduces downside risk" [E: BI]. Also: 2025 consensus at the time called for consumables +1.5% and instruments -11%; 2024 gross tariff cost estimate $85M; 2025 China about $220M.
- **#6 (Feb/Mar/Apr 2026 outlook):** 1Q26 preview says analysts model 20.5% core operating margin; 2027 targets 26% margin, HSD growth, double-digit to teens EPS growth; 2026 guide described as 1-3% in one place and 2-4% elsewhere (stale versions mixed).
- **#17 (1 May 2026 outlook with 23 Jul 2Q preview):** "in the early stages of trading price for volume" as it defends share against an emerging Roche offering; 2Q26 consensus revenue $1.13B, EPS $1.23, operating margin 22.2%, sequencing consumables +4%, instruments +22%; X placements guided at 200-240 for 2026 originally; "too early to see any real impact" from Axelios.
- **#23 (26 Jun 2026): Roche push.** NovaSeq X "the entrenched standard"; Axelios credible because of sequencing-by-expansion chemistry and Roche's diagnostics reach; "disruption is unlikely to be immediate, but Roche could still chip away where workflow or economic advantages are clear". Comparison table (partly garbled): read length about 230-250 bp (Axelios) vs max 2x150 (X); about 40B reads a run vs about 26B; instrument about $750K vs $985K-$1.2M; cost per genome **$150 (duplex) vs $200 or less**.
- **#27 (31 Jul 2026, post-2Q):** "target of HSD growth in 2027 appears increasingly visible"; clinical 65% of sequencing consumables, up 10 points in two years, "adds ballast"; main negative is the 2H cadence: 4Q "needs a more marked step-up", 3Q guide "a touch softer than consensus"; X placements 95 vs "increasingly less meaningful" goal of 60; 2Q operating margin 22.4% (+20 bp vs consensus). Describes guidance as "5% growth excluding China" and also "more than 5%".
- **#26 (compilation of 76 BI notes, 2017-2026):** cross-cutting: guidance path for 2026 from 1-3% to 2-4% to 4-6% to about 5% ex-China and EPS $5.05-5.20 to $5.15-5.30 to $5.30-5.40; clinical 60% of sequencing revenue (2Q25) to 65% of sequencing consumables (2Q26); X was 44% of high-throughput consumables in 2Q25; history of guidance cuts in 2022, 2023 and early 2025; BI said in May 2025 that 2027's HSD goal "looks further away than ever", and in Feb 2026 that hitting 26% in 2027 was "an open question", then that visibility improved by July. Useful stale-sentiment marker: as recently as 1 May 2026 BI still said there was caution on competitive dynamics.

#### Seeking Alpha (Stephen Ayers): 1 note

**SA-1, 8 Sep 2026.** Hold; no target; **DCF $188 vs price $218.22 (13.8% below)** [E: SA author]. Inputs: year-1 revenue $4.62B; base growth **11% (7.7% in years 1-3, 16.5% in years 4-6, 8.8% in years 7-9; 11.3% nine-year CAGR)**; free cash flow margins 22%, 26%, 30%; WACC 9.74% (beta 1.09); terminal growth 3%. Reading: the market prices "low-double-digit CAGR and FCF margins approaching 30%" against "mid-single-digit organic growth and about 20% FCF margins". Claims: Q2 operating income improved $31M but $18M was government incentives ($22M vs $4M) and $8M was absent restructuring, leaving about $5M of underlying improvement on about $100M of incremental revenue; Q4 operating margin must exceed 25% and second-half free cash flow about $527M to hit the guide; buybacks "nearly stopped" as the price passed $140 (Q2 repurchases 551k at $125.06, 359k at $133.77, 32k at $145.22; zero shares bought under the new $1.5B authorisation); $500M term notes matured 9 September against $1.168B of cash and short-term investments and a $300M 2029 note was issued in August; IEEPA tariff refunds may help Q4; "major unsolved mystery" is management's 1-2 points from new products, not sized by product. Competition: Roche AXELIOS 1 launched late June 2026 at about **$750,000** (about 25% below the X's roughly $1M list), first targeting research and academia; the author speculates 95 Q2 placements may include pull-forward ahead of a cheaper alternative or price concessions (an opinion; management attributed it to genuine demand).

---

### B2. The J.P. Morgan 62-customer survey (10 June 2026), in full

Source: `Extracts/ILMN/research/20260615_JP_Morgan_ILMN_Illumina-_Inc.md` (JPM-6), cross-checked to the upgrade note (JPM-5). This is JPM's own survey of **current Illumina customers**; comments are reproduced unedited and "should not be attributed to J.P. Morgan". Nothing here is a forecast by JPM; it is stated intention by respondents [E: survey respondents via JPM].

**Sample.** 62 current customers: **30 academic and 32 clinical**; about 65% North America, the rest Europe (academic 22 NA / 8 Europe; clinical 18 NA / 14 Europe). Access to Illumina instruments: 33 through a core or shared facility, 23 own, 6 lease or rent. Purchase influence: 23 joint decision-makers, 18 strong influencers, 15 primary decision-makers, 6 some influence. Academic budgets: about 27% have $250k-$999k, 47% $1.0-4.99M, 27% $5.0-9.99M (respondent-weighted midpoint about $3.2M). Clinical volume: 50% process 250-999 samples a month, about 41% 1,000-4,999, about 9% 5,000+ (weighted average about 2,140 a month). Clinical testing types: somatic oncology 24, heme malignancy 22, infectious disease 18, germline 17, pharmacogenomics 13, HLA/transplant 8, NIPT 5. Academic research areas: single-cell 22, human genomics 22, cancer biology 21.

**Spend today.** Weighted average annual instrument spend about $516k (academic) vs $965k (clinical); consumables about $428k vs $857k. Academic labs spend about 16% of operating budget on instruments and 13% on consumables.

**Installed base and recency.** Instruments owned: MiSeq 77%, NextSeq 1000/2000 69%, NovaSeq X/X Plus 58%, NovaSeq 6000 56% on the chart text (the summary page says 16%, a conflict; the chart figure is more consistent with the clinical data of about 75% for NovaSeq 6000). Clinical labs lean to high-throughput (38% of instruments selected vs 26% academic). **Last Illumina instrument purchase: about 47% in 2022 or earlier, 27% in 2023, 21% in 2024 and only about 5% in 2025 through mid-2026**; JPM reads this as clinical acquisitions steady through 2024 then dropping, and academic acquisitions "likely reflecting slower and/or tightening academic budgets". Caution: the survey says only 5% bought in the period when Illumina placed 80-95 X systems a quarter, so respondents are not a representative sample of buyers.

**Illumina's share of each lab's NGS activity, today and in three years:**

| Segment | Today | In 3 years |
|---|---|---|
| Academic small | 47% | 50% |
| Academic medium | 55% | 57% |
| Academic large | 71% | 72% |
| Clinical small | 63% | 63% |
| Clinical medium | 50% | 57% |
| Clinical large | 54% | 54% |

Application mix is expected to stay stable. Academic top three: whole genome 26% to 27%, single-cell RNA/multiomics 21%, bulk RNA-seq 19%. Clinical: somatic oncology panels 23% rising to 26%, clinical exome or genome 21%, RNA/fusion panels 14% and heme panels 14% rising to 16%; JPM notes clinical stays "panel-led".

**Spending outlook (the headline).** The next table shows what respondents plan, as average year-over-year growth. The reading: both groups expect instrument and consumables spending above Illumina's current organic trend, and volume growth exceeds spend growth in every cell.

| Measure | Academic 2027 | Academic 2028 | Clinical 2027 | Clinical 2028 |
|---|---|---|---|---|
| Consumables spend | +9.0% | +12.8% | +9.4% | +14.0% |
| Consumables volume (runs, samples) | +11.4% | +17.3% | +14.6% | +19.1% |
| Instrument spend | +18.6% | +19.0% | +22.2% | +31.0% |
| **Implied price per unit [Der: (1+spend)/(1+volume) - 1]** | **-2.2%** | **-3.8%** | **-4.5%** | **-4.3%** |

Distribution details: 93% of academic and 94% of clinical respondents expect higher consumables spend in 2027; most common bucket +1-10% in 2027 (academic 60%, clinical 56%) and +11-25% in 2028 (academic 47%, clinical 66%). Instrument spend: 90% (academic) and 91% (clinical) expect an increase in 2027; in 2028, 69% of clinical expect +26-50% and academic is split, with 10% expecting a decrease or flat.

Comparison with the Street [Der]: respondents' consumables spend growth of +9% in 2027 equals consensus sequencing consumables growth of +8.8% for FY27E, while their +13-14% in 2028 is above consensus +9.3%. Respondents' volume growth of +11-15% (2027) and +17-19% (2028) is far below the **+30% y/y sequencing activity (Gb) growth** Illumina has reported for several quarters; the survey therefore does not support a continuation of 30% Gb growth, and its implied price decline of 2-5% a year is much milder than the roughly -19% rev-per-Gb change that +30% Gb and +5% consumables revenue imply (section B5). JPM itself says the survey pricing pressure is smaller than the "-DD%" pricing pressure Illumina has recently seen.

**Roche Axelios 1.** 40% of respondents were not familiar with it. Among the 37 who were: average likelihood to buy on a 1-10 scale **6.2 academic vs 4.7 clinical**; 35% scored 7 or higher, 43% scored 4 or lower, 22% neutral. Purchase timing among those considering: **8% in 6-12 months (skews clinical), 35% in 12-24 months (skews academic), 32% in 24+ months (skews clinical), 24% not sure.** **If they bought one, 65% expect to reduce their Illumina footprint** (reduce utilisation without decommissioning: 63% academic, 66% clinical; no change: 26% / 17%; **decommission at least one Illumina instrument: about 11% of each group**). An Illumina reagent-rental offer would make 39% of academics and 37% of clinical respondents less likely to buy Axelios. Decision drivers: data quality is first or joint-first in every group (for and against); cost per sample second. Open-ended comments: cost per sample "is the most interesting part of Axelios and it is very good for gene counting applications"; concerns about a "three-day prep turnaround time and low Q value for simplex mode"; a core facility built around NovaSeq X notes it "will take Tremendous amount of service, labor, and time" to set up a new instrument; clinical respondents satisfied with incumbents ("do not need to add any more vendors").

**Caveats the report itself flags:** small sample (62 labs, only 37 familiar with Axelios), stated intentions not forecasts, all respondents are current Illumina customers, internal inconsistencies (NovaSeq 6000 share 16% vs 56%; academic and clinical counts on the Axelios slides appear swapped between slides).

---

### B3. Estimates side by side

**Latest vintage for each source versus Bloomberg consensus (10 Oct 2026).** The table shows each firm's most recent published numbers. Dates: JPM 31 Jul, Barclays 31 Jul, Freedom 5 Aug, UBS 26 Feb (stale), Bloomberg consensus 10 Oct. Revenue in $ millions, EPS in dollars; growth is year-over-year [Der].

| | FY26E revenue | FY27E revenue (growth) | FY28E revenue (growth) | FY29E revenue | FY26E EPS | FY27E EPS | FY28E EPS | FY29E EPS |
|---|---|---|---|---|---|---|---|---|
| **Bloomberg consensus, 10 Oct** | 4,625 | 4,918 (+6.3%) | 5,263 (+7.0%) | 5,650 | 5.36 | 6.11 | 7.01 | 7.99 |
| JPM [E] | 4,627 | 5,047 (+9.1%) | 5,652 (+12.0%) | 6,261 | 5.34 | 6.16 | 7.41 | 8.73 |
| Freedom Broker [E] | 4,637 | 4,900 (+5.7%) | 5,151 (+5.1%) | n/a | 5.38 | 5.98 | 6.59 | n/a |
| Barclays [E] | 4,609 | 4,862 (+5.5%) | 5,105 (+5.0%) | n/a | 5.34 | 5.73 | 6.02 | n/a |
| UBS [E], 26 Feb (stale) | 4,535 | 4,720 (+4.1%) | 5,022 (+6.4%) | 5,348 | 5.07 | 5.74 | 6.54 | 7.43 |
| FactSet consensus (via Ameriprise), 31 Jul | 4,603 | 4,871 | n/a | n/a | 5.30 | 6.00 | n/a | n/a |

Three-year and four-year compound growth rates [Der: end value over FY25 base, e.g. JPM EPS (8.73 / 4.84)^(1/4) - 1]:

| | Revenue CAGR FY25 to FY28 | EPS CAGR FY25 to FY28 | Revenue CAGR FY25 to FY29 | EPS CAGR FY25 to FY29 |
|---|---|---|---|---|
| Bloomberg consensus | 6.6% | 13.1% | 6.8% | 13.4% |
| JPM | 9.2% | 15.3% | 9.6% | 15.9% |
| Freedom | 5.9% | 10.8% | n/a | n/a |
| Barclays | 5.5% | 7.4% | n/a | n/a |
| UBS (Feb) | 5.0% | 10.5% | n/a | n/a |

Quarterly estimates for the two remaining quarters of FY26 [E]: 3Q26E revenue / EPS: Bloomberg $1,154M / $1.36; JPM $1,152M / $1.35; Freedom $1,152M / $1.38; Barclays n/a / $1.35; company guide $1.14-1.16B / $1.33-1.38. 4Q26E: Bloomberg $1,220M / $1.54; JPM $1,225M / $1.53; Freedom $1,234M / $1.54; Barclays $1.54 EPS; consensus (Barclays table 30 Jul) $1.51.

Margin definitions differ. On the company's adjusted basis FY27E operating margin: Bloomberg 25.2%; Freedom 25.1% ($1,232M / $4,900M); UBS 24.6%; Barclays 24.3% [Der]. JPM's adjusted EBIT ($956M in FY27E on its 31 Jul model) is after SBC; adding back Bloomberg's FY27E SBC of about $296M gives roughly $1,250M or 24.8% on $5,047M [Der, approximate]. Management's target is 26.0% for 2027 [D].

**How consensus has moved.** The table shows the consensus levels quoted by the notes at each date, which is the best record in the folder of how the Street's numbers have drifted. All consensus figures are [E: cons] quoted by the cited note.

| Date | Source quoting | FY26E EPS | FY27E EPS | FY28E EPS | FY26E revenue |
|---|---|---|---|---|---|
| 5 Feb | Bloomberg via Barclays / UBS (UBS 5.81 for FY27, 6.45 for FY28) / JPM | 5.07 | 5.77-5.81 | 6.45-6.54 | 4,416 (Barclays) |
| 5 Feb | FactSet via Ameriprise | 5.10 | 5.82 | n/a | 4,490 |
| 19-26 Feb | Bloomberg via UBS / JPM | 5.12-5.13 | 5.82-5.84 | 6.58-6.60 | n/a |
| 30 Apr-1 May | Bloomberg via Barclays / JPM | 5.12 | 5.81 | 6.62 | 4,534 |
| 1 May | FactSet via Ameriprise | 5.18 | 5.89 | n/a | 4,557 |
| 9 Jun | Bloomberg via JPM | 5.23 | 5.93 | 6.78 | n/a |
| 30-31 Jul | Bloomberg via JPM / Barclays | 5.24-5.25 | 5.92-5.93 | 6.81 | 4,571 (pre-print) |
| 31 Jul | FactSet via Ameriprise | 5.30 | 6.00 | n/a | 4,603 |
| **10 Oct** | **Bloomberg printouts** | **5.36** | **6.11** | **7.01** | **4,625** |

Since early February [Der]: FY26E EPS +5.7% ($5.07 to $5.36), FY27E +5.7% ($5.78 to $6.11) and FY28E +8.7% ($6.45 to $7.01). FY26E revenue +4.7% ($4,416M to $4,625M). The out-year revisions are larger than the current-year revisions, which matches JPM's pattern (JPM's FY26 EPS rose 4% from $5.12 to $5.34 between February and July while its FY28 EPS rose 13% from $6.55 to $7.41).

**J.P. Morgan's estimate path** (the one broker with enough vintages to show drift) [E: JPM]:

| JPM note date | FY26E revenue | FY27E revenue | FY28E revenue | FY26E EPS | FY27E EPS | FY28E EPS | Target |
|---|---|---|---|---|---|---|---|
| 6 Feb | 4,549 | 4,886 | 5,147 | 5.12 | 6.02 | 6.55 | $120 |
| 1 May | 4,573 | 4,799 | 5,075 | 5.21 | 5.93 | 6.48 | $125 |
| 10 Jun | 4,583 | 4,919 | 5,401 | 5.23 | 5.98 | 7.01 | $185 |
| 16 Jul | 4,583 | 5,000 | 5,601 | 5.23 | 6.09 | 7.33 | $220 |
| 31 Jul | 4,627 | 5,047 | 5,652 | 5.34 | 6.16 | 7.41 | $230 (Dec-27) |

Between 1 May and 31 July JPM raised FY28 revenue by $577M (11%) and FY28 EPS by $0.93 (14%), while FY26 revenue rose only $54M (1.2%). The target rose 84% in that window ($125 to $230).

**What drove JPM's target moves [Der from JPM's own sensitivity grid in JPM-5].** The June DCF at the unchanged cash flows gives $141 at a 10.1% WACC and 4.0% terminal growth, $169 at 9.1% / 4.0% and $185 at 9.1% / 4.5%. So of the move from $120 (Feb) to $185 (June), about **$44 (24% of the new target) comes purely from lowering the discount rate by about a point and raising terminal growth by half a point**, and about $21 from higher cash flows and time. Terminal value is 86% of enterprise value; a 4.5% perpetual growth rate is above most nominal-GDP assumptions. JPM's grid:

| WACC / terminal growth | 3.5% | 4.0% | 4.5% | 5.0% | 5.5% |
|---|---|---|---|---|---|
| 8.1% | $190 | $211 | $237 | $273 | $322 |
| 8.6% | $171 | $187 | $208 | $235 | $270 |
| 9.1% | $155 | $169 | $185 | $206 | $232 |
| 9.6% | $142 | $154 | $167 | $183 | $204 |
| 10.1% | $132 | $141 | $152 | $165 | $181 |

At the June cash flows, **a $278 share price needs roughly an 8.1% WACC with 5.0% terminal growth ($273) or higher**, i.e. the top-right corner of JPM's own grid. The later estimate increases move the grid up (FY28 EPS +6% from June to July), but not by enough to change that conclusion by themselves [Der].

---

### B4. Synthesis

#### (i) Bull versus bear by firm

| Firm | Stance (latest) | Bull arguments | Bear arguments or conditions |
|---|---|---|---|
| **J.P. Morgan** | Overweight, $230 | Clinical base is sticky (all major CLIA labs, 76-78% of clinical volume on the X, switching friction); test-volume runway from therapy selection, MRD, MCED and sequencing intensity (WGS about 15x the data of exome); X pricing headwinds "largely gone exiting this year"; Roche manageable near term (reusable flow-cell contamination, higher DNA input, fragmented software); US academic recovery 2H26-2027; multiomics (Fluent, SomaLogic, StrataMap) an add-on; "scarcity value" of HSD growth with mid/high-teens EPS growth; survey shows intent to spend and Illumina share rising | Acknowledges "a longer-term question about the terminal value of ILMN in a more competitive environment remains"; competitive standing "under more pressure now than in the past"; risks are Axelios attrition, MRD/MCED guideline delay, pricing, no funding recovery. Was Neutral until June on exactly the pricing/competition worry |
| **UBS** | Neutral, $135 (last note 26 Feb) | Clinical consumables +20%, mid-teens guide; "outsized margin expansion opportunity" (EBIT margin 23.1% to 28.4% by FY30E); Roche's $150 benign because large customers already pay similar and 35B flow cell reaches about $150; early researcher and expert feedback skeptical on switching | Illumina's organic growth guide compares "unfavorably" with peers; counting applications (about 16% of sequencing consumables) priced at $0.68 per million reads vs Roche $0.06 and Element's $3k runs are the exposed area; target multiple carries a discount to Tools |
| **Barclays** | Underweight, $160 (upside $230, downside $100) | Concedes "plenty of momentum" in clinical, instrument placements beating by more than 50%, leasing "seeding" the base, expects near-term "bulls win" | Illumina is "a MSD business"; competition requires "continued price concessions, bundling, and favorable terms"; X price per Gb may be falling (X Gb share +500 bp, revenue share flat at 55% in 1Q); expects "another round of pricing headwinds in 2027"; Axelios competitive in research counting applications now and Roche in clinical long term; 35B flow cell must be repriced; 35x P/E "top of the Tools industry"; gross margin modelled falling in 2027-28; multiomics 1-2 points unverifiable |
| **Freedom Broker** | Hold, $185 (was Buy until 5 Aug) | Instruments up, consumables to accelerate in 2H26-2027, operating leverage, beat-and-raise cycle, X install base | "Much of the upside is now priced in"; no longer sees guidance as conservative; risks: NGS competition, academic funding, China UEL |
| **Ameriprise** | Buy, no target | Exposure to "genomic medicine of the future"; X and X Plus leverage; forward P/E below the 5-year average (72x, distorted by Grail-era EPS) | Generic risk list; flags the 15% clinical growth slowdown, 6-9 month lag for new X systems to normalise, research funding, China |
| **Bloomberg Intelligence** | no rating | Clinical "ballast"; execution gives "a higher floor"; 2027 HSD target "increasingly visible" | 2H cadence needs "a more marked step-up" in 4Q; Roche "could chip away where workflow or economic advantages are clear"; "trading price for volume" (May) |
| **Seeking Alpha (Ayers)** | Hold, DCF $188 | Operations "much better at a glance"; sequencing structurally growing | Margin gain partly lumpy government incentives and absent restructuring; buybacks nearly stopped; $500M maturity; 1-2 points multiomics unsized; price implies low-double-digit CAGR and about 30% FCF margins |

#### (ii) Where the brokers disagree numerically

- **FY28 EPS is the widest gap: $6.02 (Barclays) to $7.41 (JPM), a 23% spread** [Der]; Freedom $6.59, UBS (stale) $6.54, Bloomberg consensus $7.01. Consensus sits above three of the four brokers in the folder, which means the remaining contributors (not in the folder) must be well above $7.0.
- **FY28 revenue growth: +5.0% (Barclays) vs +12.0% (JPM)**; consensus +7.0%. JPM is the only broker modelling double-digit growth in 2028; it also has FY27 at +9.1% vs Freedom +5.7% and Barclays +5.5% against management's "high-single-digit" target. So within a single month (July) the sell-side range on FY27 growth was 5.5% to 9.1%, and only JPM clears 8%.
- **Gross margin direction.** JPM 68.3% / 68.8% / 69.1% (FY26-28), UBS 68.4% / 68.7% / 68.9%, consensus 68.5% / 69.1% / 69.5%, **Barclays 68.4% / 67.8% / 67.9%** (down in 2027-28). Barclays' bear case is about price, not volume.
- **Tax rate.** Bloomberg 20.5%; JPM models 24.9-25.9% (its adjusted EBIT is after SBC), a definitional difference that makes JPM's EPS growth look more margin-driven than consensus.
- **Share count.** Consensus 153M declining to 151.8M by FY29E; JPM 154M rising to 160M by FY29E (no buybacks modelled, SBC dilution); UBS 154M falling to 150M by FY30E. The difference is worth about 5% of EPS by FY29 [Der: 160 / 151.8 = 1.054].
- **Valuation framework.** JPM uses a DCF with WACC 8.9-9.8% and 4.5% terminal growth; Barclays 28x P/E on FY27; UBS 15x 2027E EV/EBITDA; Freedom 8x EV/Sales and 35x P/E blended with a DCF. At the 10 Oct price none of those frameworks supports the stock (section B4-iv).
- **Why Roche matters differently.** Barclays and UBS treat price (counting applications, 35B flow cell repricing) as the exposure; JPM treats workflow (reusable flow cell, DNA input) as the protection. UBS's expert checks cut both ways: one expert already pays $175 a genome and larger users $125, so a $150 Roche price is not below what big customers pay today.

#### (iii) What the Street collectively embeds, driver by driver

| Driver | What the notes and consensus embed | Source and label |
|---|---|---|
| **Clinical sequencing consumables growth** | Company guide for FY26: **+mid-teens** ROW (raised from DD/mid-teens on 31 Jul); actual +20% in 4Q25 and 1Q26, **+15% in 2Q26** (US/Canada above +20%, Middle East and Latin America soft). JPM: +low/mid-teens CAGR 2026-30. Survey: clinical consumables spend +9.4% / +14.0% and volume +14.6% / +19.1% in 2027 / 2028. Clinical is 65% of sequencing consumables (BI: up 10 points in two years) | [D] / [E: JPM] / [E: survey] |
| **Research and applied consumables** | Guide: FY26 down MSD-HSD, unchanged all year; actual -12% (1Q), -7% (2Q), +9% q/q. JPM: ROW research +MSD CAGR 2026-30. Survey: academic consumables spend +9.0% / +12.8% | [D] / [E: JPM] / [E: survey] |
| **Gb (volume) growth** | Total activity on high- and mid-throughput instruments +30% y/y in 3Q25, 4Q25, 1Q26 and "more than 30%" in 2Q26; clinical "well above". JPM: "underlying consumables volume growth of at least +30%". Survey respondents expect only +11-19% volume growth in 2027-28 | [D] / [E: JPM] / [E: survey] |
| **Price per Gb / pricing** | Management: X-transition pricing headwinds easing through 2026 because research is 90-92% on X and clinical 78%; JPM: "largely gone exiting this year"; survey-implied price per unit -2% to -4.5% a year; Barclays: "another round of pricing headwinds in 2027 and beyond"; JPM models gross margin "in the high 60s" with reagent rentals (LSD% of boxes) pressuring ASPs. Consensus gross margin rises 68.5% to 70.3% (FY26-FY30E), i.e. **consensus assumes no net price erosion at the margin line** | [D] / [E] |
| **NovaSeq 6000 tail** | X is 83% of high-throughput Gb and 59% of high-throughput consumables revenue (2Q26); clinical 78% on X targeted 80-85% by year-end; >10 new NovaSeq 6000 placed in 2Q for assays that will stay; "as much as half of clinical placements are incremental". 6000 pull-through $600-650k vs X $1.35-1.40M. No broker models the residual 6000 volume explicitly | [D] / [E: JPM] |
| **Roche Axelios** | Consensus does not publish a competitive-loss assumption. JPM: manageable; survey: only 8% would consider buying in 6-12 months, 65% of buyers would cut Illumina use, 11% would decommission; UBS: early experts skeptical, library prep and software gaps; BI: "unlikely to be immediate"; Barclays: share loss in research counting applications near term. Roche list: $150 per genome consumables (20x reuse), instrument about $750K vs about $1M | [E] |
| **Multiomics** | Management: at least 1-2 points of growth in 2027 (JPM: "≥100-200 bp by 2027"); SomaLogic +1.5-2.0% of FY26 revenue (tracking high end), -100 bp margin, -$0.18 EPS. Barclays cannot verify; SA calls it unsized. Most multiomics products are booked in consumables | [D] / [E] |
| **China** | FY26 guide $210-220M; consensus $211M (FY26E) falling to $187M (FY28E); JPM: China sequencing consumables -mid-teens with no recovery. China under 5% of sales | [D] / [E] |
| **Margins** | Guide 23.4-23.6% (FY26), 26% in 2027. Consensus 23.5% / 25.2% / 26.5% (FY26-28E); brokers 24.3-25.1% for FY27E (company basis) | [D] / [E] |
| **EPS growth** | Guide FY26 $5.30-5.40; consensus +10.7% / +14.0% / +14.7% (FY26-28E); JPM +mid/high-teens through 2030E | [D] / [E] |
| **Capital return** | Consensus buybacks $420M / $313M / $501M (FY26-28E); buyback pace slowed sharply above $140 per share (SA); about $1.8B authorisation remaining | [E] / [D] |

#### (iv) Valuation data the notes provide, and what they imply at the latest price

Multiples published in the notes (all at the price in each note) [E]:

| Note date | Price | Multiples cited |
|---|---|---|
| 6 Feb (JPM) | $133.61 | P/E 26.1x FY26E, 22.2x FY27E; EV/EBITDA 23.0x FY26E; FCFF yield 3.2% |
| 5 Feb (UBS) | $133.61 | P/E 26.4x FY26E, 23.3x FY27E; EV/EBITDA 16.5x / 14.5x; FCF yield 5.1% |
| 5 Feb (Barclays) | $133.61 | P/E 26.0x FY26E; EV/EBITDA 16.3x; FCF yield 5.2% |
| 5 Feb (Ameriprise) | $133.61 | forward P/E 26.0x vs 5-year average 72.2x |
| 30 Apr (Barclays) | $126.74 | P/E 24.5x FY26E, 22.4x FY27E; EV/EBITDA 15.3x |
| 9 Jun (JPM) | $160.03 | EV/EBITDA 17.8x (2027E) vs Core Tools 15.6x; FCF yield about 4-5%; P/E 30.6x FY26E |
| 15 Jul (JPM) | $187.15 | P/E 35.8x FY26E, 30.7x FY27E; EV/EBITDA 28.4x / 24.4x |
| 30 Jul (JPM, Barclays, Ameriprise) | $205.09 | P/E 38.4x FY26E, 33.3x FY27E (JPM); 38.4x / 35.8x (Barclays); forward 36.4x vs 72.2x (Ameriprise); EV/EBITDA 30.2x / 26.1x (JPM) |
| 5 Aug (Freedom) | about $203 | EV $32.4B; targets 8x EV/Sales, 35x P/E |

**Derived multiples at the latest price in the folder, $278.17 (10 Oct, Seeking Alpha page header) on Bloomberg consensus** [Der]. Market capitalisation $278.17 x 151.3M shares (Barclays 31 Jul) = $42.1B; net debt $823M (Bloomberg ratio row at 2Q26: debt $1,991M less cash and short-term investments $1,168M); enterprise value about $42.9B. The Q3 refinancing ($500M matured, $300M issued) is not reflected, and the share count will have moved slightly with buybacks. The point of the table: the stock is on about 52x this year's adjusted EPS and 29x 2028 EBITDA, a premium to every framework in the folder.

| Year | P/E (adj. EPS) | EV/EBITDA | EV/Sales | FCF yield |
|---|---|---|---|---|
| FY26E | 51.9x | 33.0x | 9.3x | 2.4% |
| FY27E | 45.5x | 28.8x | 8.7x | 2.6% |
| FY28E | 39.7x | 26.4x | 8.2x | 2.9% |
| FY29E | 34.8x | 24.0x | 7.6x | 3.2% |
| FY30E | 29.3x | 21.5x | 7.1x | 3.6% |

- On GAAP EPS the multiples are 55.4x FY26E and 48.7x FY27E [Der]. PEG on FY27E is about 3.3x (45.5x / 14% growth).
- **Premium of the $278.17 price to each published target or value** [Der]: JPM $230, +21%; Barclays' *upside case* of $230, +21%; Barclays base $160, +74%; Freedom $185, +50%; FactSet consensus target $175.72 (31 Jul), +58%; Seeking Alpha DCF $188, +48%; UBS $135 (26 Feb), +106%.
- **Implied multiples of the targets.** JPM $230 on its FY27 EPS of $6.16 is 37.3x; Barclays $160 is 27.9x its FY27 $5.73 (the $278 price is 48.5x that EPS); the price is 45.2x JPM's own FY27E.
- **Relative multiple.** JPM's argument in June and July was that ILMN trades at only a 4.1x EV/EBITDA premium to Core Tools (15.6x) against a historical premium of about 15x. On Bloomberg FY27E EBITDA the stock is now at 28.8x, a premium of about 13 turns to the *June* Core Tools multiple (peer multiples have not been refreshed in the folder), which is back near the historical premium JPM used to call the multiple cheap [Der, with the stale-peer caveat]. The "scarcity value" case in those notes therefore no longer rests on a cheap relative multiple.
- **Market-implied DCF.** Seeking Alpha's reverse view at $218: low-double-digit nine-year revenue CAGR and about 30% free-cash-flow margins. At $278 the requirement is higher still. Consensus has revenue growth of 6-8% through FY30 and FCF margin of 22-25%.
- **Peers cited in the folder.** JPM: Core Tools (DHR, MTD, TMO, WAT) average 15.6x 2027E EV/EBITDA (9 Jun) and +MSD organic growth with +LDD EPS growth in 2028E. Natera, Guardant, Adaptive, BillionToOne, Alamar and 10x Genomics targets are in JPM-7 but no multiples are given for them in the extract.

#### (v) What the notes say about expectations, positioning and stock reactions

No note in the 31 gives short interest, fund holdings, whisper numbers or an explicit "bogey". What exists is indirect and is collected here [E or D as marked].

| Date | Evidence | Source |
|---|---|---|
| 29 Jan | BI: consensus for 2026 was "modest, at about 3% revenue growth and roughly 70 bps of margin gain... a low bar" if consumables momentum holds | BI #26 (4Q25 preview, 29 Jan) |
| 13 Jan to 10 Feb | Stock $145.55 (12 Jan) to $133.61 (5 Feb) to $117.25 (10 Feb): -19.4% in a month [Der], in spite of an EPS beat of $0.14 (4Q25 $1.35 vs Street $1.21) and revenue beat of 5%. Causes in the notes: soft 1Q guide (EPS $1.02-1.07 vs Street $1.14), "pushback on the 2H margin ramp", Roche/AGBT and Element competitive news | JPM-2, BCS-1, FB-1, UBS-2 |
| 5 Feb | Barclays: investors read the guide as "a market freeze" or clinical slowdown; "little risk appetite for a 2H-weighted guide"; many believed placements were pulled forward or a backlog flushed ahead of competitive launches (management denied) | BCS-1 |
| 26 Feb | Roche pricing: JPM says most investors expected about $150 and some as low as $100; stock +4.5% on the day ($121.87 to $127.40) [Der] | JPM-3, UBS-4 |
| 30 Apr | After-hours reaction about -1% despite beat and raise; stock +9.7% over the following five sessions [Der]; Barclays expected shares to rise the next day and "the bull/bear debate to rage on" | FB-2, BCS-2 |
| 9 Jun | JPM: ILMN "one of the most highly debated stocks in our space over the last year and a half"; stock $160.03, +88% over 12 months | JPM-5 |
| 31 Jul | Barclays: "investors are assuming the +HSD% top line is in the bag and new buyers of the stock have to believe that they can deliver this consistently and that we are likely to see them touch DD". BI: 3Q guide "a touch softer than consensus" | BCS-3, #27 |
| 5 Aug | Freedom downgrades on valuation after the "recent strong re-rating"; stock slipped from $205.09 to $198.16 by 4 Aug (-3.4%) [Der] | FB-4 |
| Bloomberg analyst ratings (Buy/Hold/Sell) | 10/11/3 (5 Feb) to 11/11/3 (25 Feb) to 11/9/3 (30 Apr) to 12/6/3 (9 Jun) to 13/6/3 (30 Jul); Buys went from 42% to 59% of ratings [Der] | JPM notes |
| 8 Sep to 10 Oct | Stock $218.65 to $278.17 (+27.2%) with no broker commentary in the folder | SA header |
| FactSet consensus target | $135.89 (5 Feb), $136.11 (30 Apr), $175.72 (30 Jul) vs prices $133.61, $126.74, $205.09: the average target went from +1.7% and +7.4% above the price to **14.3% below** it | Ameriprise |

Stock path for reference [D / Der]: $145.55 (12 Jan), $133.61 (5 Feb), $117.25 (10 Feb), $120.09 (18 Feb), $121.87 (25 Feb), $127.40 (26 Feb), $126.74 (30 Apr), $139.07 (6 May), $160.03 (9 Jun), $187.15 (15 Jul), $205.09 (30 Jul), $198.16 (4 Aug), $218.65 (8 Sep), $278.17 (about 10 Oct). Bloomberg gives +56.4% YTD at $205.09, so the 2025 close was about $131.1 and the stock is up about +112% YTD at $278.17 [Der].

Pointer for the sentiment workstream: a Barclays sector note in the SECTOR folder (`Extracts/SECTOR/research/20260312_Barclays_SECTOR-Tools_...The_Bullet.md`, not one of the 31) attributes ILMN's move around the 4Q25 print to "short covering on better-than-feared EPS", and quotes short interest for other names from Bloomberg. That is the only short-positioning evidence I found and was not read in full.

#### (vi) Stale items and conflicts to resolve

1. **Sell-side coverage ends 5 August; the stock is up about 36% since.** No target is within 20% of the 10 October price. UBS has no note after 26 February ($135 target at that time); Barclays' $160 and Freedom's $185 pre-date a 40% rally from $198.
2. **Which quarter has the extra week** (section 0). Bloomberg dates imply Q3; management said Q4.
3. **JPM 31 July WACC printed 9.8%** versus 8.9% two weeks earlier, with a higher target; check the original.
4. **The 10 October price of $278.17 comes from a Seeking Alpha page header.** I could not verify it elsewhere in the folder. Re-pull a market price from a proper source before the primer states a multiple.
5. **Guidance growth numbers differ across BI pages** (1-3%, 2-4%, 4-6%, "5%", ">5%"): different bases (organic, ex-China, reported). Company guidance as of 31 Jul: reported +5.9-6.8%, organic (all) >4%, ROW organic ~5%.
6. **The JPM survey report header still shows Neutral and no target** while the upgrade note is dated the same day.
7. **UBS Fast Take text is garbled**; the Element figures ($3k vs $32k per run, 3T vs 16T, 40% instrument discount, ships 2H26) are the readable bullets only. Barclays 31 Jul attributes "Axelios" to Element, which looks like a naming slip.
8. **Consensus 2026 buybacks, debt maturities and regional lines** in the Bloomberg sheets are stale or on mixed bases (A5).
9. **Ameriprise's 72.2x "5-year average forward P/E"** is an artefact of Grail-era depressed EPS and should not be used as a valuation anchor.
10. **Old figures recycled in BI notes** ($125B opportunity, 34% penetration by 2027 from the 2022 investor day, $800M liquid biopsy) are stale.
11. **JPM adjusted EBIT** is after SBC, so it is not comparable with Bloomberg consensus, UBS or Freedom EBIT.
12. **Freedom 5 Aug** mixes prior close $198.16 and key-data price $203.01, and its AR threshold in the worked example (±0.35) differs from the stated rule (±1.2).

---

### B5. Derived checks that bear on the central questions

**(a) Revenue per Gb on the NovaSeq 6000 versus the X (Q2 on the "residual 17%").** Ameriprise (31 Jul) and Freedom (5 Aug) give the X at 83% of high-throughput Gb shipped and 59% of high-throughput consumables revenue in 2Q26. So the residual **17% of high-throughput Gb, running on the 6000 and older platforms, earns 41% of high-throughput consumables revenue** [D: share data; Der: ratio]. Revenue per Gb on the 6000 is therefore (41 / 17) / (59 / 83) = **3.4 times** the X's. The same arithmetic for 1Q26 (X at 55% of revenue, 82% of Gb) gives 3.7 times, and for 4Q25 (55% of revenue; Gb share inferred at 77% from Barclays' "+500 bp") about 2.7 times. The ratio mixes list price, flow-cell size and mix (small 6000 flow cells earn more per Gb), which is management's explanation for why a flat X revenue share on rising Gb share is "a frivolous exercise" (BCS-2). It is not a clean price ratio.

The sensitivity below shows what happens to high-throughput consumables revenue if some of the residual 6000 Gb moved to the X at the X's current revenue per Gb [Der]. Assumptions: the volume moves one-for-one, with and without a 20% volume uplift on converted Gb; no change in X pricing. The table shows the arithmetic, not a forecast: it brackets the size of the pricing step that conversion could cost. It does not know how much of the 17% will convert (clinical customers are buying 6000s to keep running validated assays).

| Share of residual 6000 Gb that converts | Change in high-throughput consumables revenue, no volume uplift | With +20% volume uplift on converted Gb |
|---|---|---|
| 25% | -7.2% | -6.6% |
| 50% | -14.5% | -13.2% |
| 75% | -21.7% | -19.9% |
| 100% | -28.9% | -26.5% |

For scale: management says research is 92% converted and clinical 78% (target 80-85% by year-end 2026), so the remaining 17% is mostly clinical and most of it is likely to stay on the 6000 for validated assays; the share that converts in 2027 is the open question.

**(b) Price per Gb implied by Gb growth versus revenue growth (Q2 on pricing).** If sequencing activity grows +30% and ROW sequencing consumables revenue grew +5% in 2Q26, revenue per unit of volume fell about **19%** (1.05 / 1.30 - 1) [Der]; at +25% Gb growth it fell 16%, at +20% about 12.5%. This is a blend of price, flow-cell mix and the lag between activity and revenue recognition. What consensus then requires:

| Gb growth assumption | Revenue/Gb change needed for FY27E consensus sequencing consumables +8.8% | for FY28E +9.3% |
|---|---|---|
| +30% | -16.3% | -15.9% |
| +25% | -13.0% | -12.6% |
| +20% | -9.3% | -8.9% |

So consensus is compatible with the recent run-rate of revenue-per-Gb deflation only if Gb growth stays near +25-30%; if Gb growth normalises to +20% (the survey says +11-19%), price/mix deflation must halve to hold +8.8-9.3%.

**(c) Reconciling clinical and research growth to total (Q1).** ROW sequencing consumables grew +5% in 2Q26 and +5% in 1Q26. With clinical at 60% of last year's base (BI: 60% in 2Q25) growing +15% and research and applied at 40% growing -7%, the weighted growth is +6.2% [Der: 0.6 x 15 - 0.4 x 7]; with 1Q26's +20% and -12% it is +7.2%. Both exceed the reported +5% by 1-2 points, so either the "clinical" and "research" growth rates are not on the same revenue basis as the total (they probably include different pieces such as 6000-related or other consumables), the base shares are lower, or price/mix inside each segment is worse than the headline rates. The reconciliation matters because the forward growth debate is framed in clinical and research segments but the reported total is the number consensus is built on. Worth checking against the 10-Q segment tables.

**(d) Rough pull-through sketch.** Approximately 295 X placements in 2026 (80 in 1Q, 95 in 2Q, then about 60 a quarter per the May guide; actual 2H may be higher), with management saying up to half of clinical placements are incremental. At $1.35-1.40M a year per X versus $0.60-0.65M per 6000, half incremental at about $1.375M and half conversions adding about $0.75M each gives about $313M of annualised consumables once fully utilised, about **10% of FY26E sequencing consumables ($3,104M)** [Der, rough]. That is the order of magnitude behind consensus FY27E +8.8%, before price erosion and before the six to nine month ramp. It is a plausibility check, not a model.

**(e) Multiomics arithmetic.** Management's "1-2 points of growth in 2027" is $46-92M on a $4.6B FY26E base [Der]. The Bloomberg microarray-service line jumped from $10-12M a quarter (2H25) to $23M in 1Q26 and 2Q26 [D], i.e. about $11-12M a quarter or $45-50M a year of incremental SomaLogic-related revenue visible in that line [Der], against a guide of 1.5-2.0% of FY26 revenue ($65-87M) for SomaLogic; the balance is presumably booked in consumables ("most multiomics products... are booked within consumables revenue", AMP-3). Consensus FY27E revenue growth of +6.3% (about +7.1% ex-China, about +6.8% adjusted for the extra week) therefore leaves little room for multiomics to add 1-2 points on top of HSD core growth unless core growth is about 6-7%. The Street cannot verify the figure (Barclays; SA).

---
