# ILMN segment financials, Q1'24 to Q2'26 (built 2026-10-11)

Scope: quarterly financial cuts for Illumina (ILMN), built from the 10-Qs/10-Ks (primary), earnings decks, earnings-call transcripts (for items the decks do not give) and Bloomberg consensus. Illumina has one reportable segment since the June 24, 2024 GRAIL spin-off, so every "segment" below is an economic cut (product type, region, end-market, platform), not a reported segment with its own margin.

Label key: **[D]** disclosed in the cited source; **[Der]** derived by me, calculation shown; **[E]** estimate/consensus (Bloomberg, pulled 10/10/2026). All $ in millions unless stated. File paths are relative to `Working Notes/`.

## Read this first: basis differences and flags

1. **Consolidated vs Core Illumina (2024).** Q1'24 and Q2'24 consolidated figures include GRAIL (external service revenue of $27M and $29M; GRAIL was spun off June 24, 2024) and are net of intercompany eliminations (-$7M and -$9M, mostly consumables sold to GRAIL). From Q3'24 consolidated = Core. Illumina's own 2025 y/y growth and non-GAAP comparisons use **Core** as the base. The main tables use consolidated "as filed" numbers; a Core-basis y/y table is given for Q1'25 and Q2'25. Sources: Q1'25 10-Q p.31; Q2'25 10-Q p.30-31; FY24 10-K p.34.
2. **Q4 is derived** (10-K full year minus the nine-month figure in the Q3 10-Q) because no Q4 10-Q exists. Illumina's own Q4 deck lines differ from my derived lines by $1M in several places (rounding). Both are shown in Table 1E; totals tie exactly.
3. **Fiscal calendar: the extra week is in Q4'26, not Q3'26.** The year is 52/53 weeks ending the Sunday closest to Dec 31. On the Q2'26 call an analyst asks about "an extra week in the fourth quarter" and the CFO answers "we have 1 extra week this year in Q4, which would largely be a consumables story... maybe 0.5 point or so of revenue contribution" (`Sources/ILMN/earnings_call/ILMN_2026Q2_Earnings_Call.md`, lines ~314-330). The fiscal rule puts Q3'26 end on Sep 27, 2026 (13 weeks) and Q4'26 end on Jan 3, 2027 (14 weeks). **Bloomberg's Q3'26E period label (10/04/2026) conflicts with that rule**, and the brief's "Q3'26 is 14 weeks" does not match the transcript. FY26 is 53 weeks [Der from dates; the filings state the 52/53-week rule but I found no explicit "53 weeks" sentence for FY26].
4. **Q2'25 GAAP cost of product revenue includes a $23M intangible-asset impairment** (Q2'25 10-Q, Note on intangibles: "impairment charge of $23 million recorded in cost of product revenue"; the Q2'26 10-Q cites it again). It lowers Q2'25 GAAP product margin by about 2.5 points and flatters the Q2'26 y/y gross-margin comparison.
5. **SomaLogic (closed Jan 30, 2026) is reported mostly inside the "microarray" revenue bucket**; the Q1'26 call says "from our report perspective, it's in microarrays, mostly in the microarrays". The 10-Q text attributes the *service and other* increase to SomaLogic, and the 10-Q line split cannot place all of it in microarray service, so the line-by-line split is not disclosed (Section 7).
6. **Regions were recast in Q1'26.** Q1'25 and Q2'25 were recast in the 2026 10-Qs; **Q3'25 and Q4'25 recast values are not in any file I was given** (Section 4).
7. **Preliminary vs final FY25.** The JPM deck (Jan 13, 2026) carried *preliminary* Q4'25 revenue of ~$1,155M and non-GAAP EPS of $1.27-$1.30; final Q4'25 (Feb 5, 2026) was $1,159M and $1.35. Installed-base counts also moved (Section 6). Use the Q4'25 deck and the 10-K.
8. **Consensus-file quirks** are listed in Section 9.

---

## 1. Revenue by product type

Source: "Revenue by Source" note in each filing under `Sources/ILMN/filing/`: `ILMN_10-Q_2024Q1.md` (p.13), `..._2024Q2.md` (p.14), `..._2024Q3.md` (p.13), `ILMN_10-K_FY2024.md` (Note 3, p.66), `ILMN_10-Q_2025Q1.md` (p.12), `..._2025Q2.md` (p.13), `..._2025Q3.md` (p.13), `ILMN_10-K_FY2025.md` (Note 2, p.67), `ILMN_10-Q_2026Q1.md` (p.16), `..._2026Q2.md` (p.16). Q1-Q3 columns are [D]; Q4 columns are [Der] = FY (10-K) minus nine months (Q3 10-Q YTD). Consolidated basis.

### 1A. Revenue by product type ($M)

| $M, consolidated as reported | Q1'24 | Q2'24 | Q3'24 | Q4'24 | Q1'25 | Q2'25 | Q3'25 | Q4'25 | Q1'26 | Q2'26 | FY24 | FY25 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sequencing consumables | 691 | 729 | 741 | 698 | 696 | 740 | 747 | 756 | 726 | 775 | 2,858 | 2,939 |
| Microarray consumables | 71 | 78 | 66 | 81 | 72 | 71 | 69 | 76 | 71 | 77 | 297 | 288 |
| Sequencing instruments | 110 | 116 | 104 | 154 | 109 | 96 | 107 | 154 | 118 | 125 | 484 | 465 |
| Microarray instruments | 4 | 4 | 3 | 5 | 3 | 5 | 4 | 4 | 2 | 5 | 17 | 17 |
| Sequencing service & other | 178 | 171 | 150 | 152 | 142 | 136 | 147 | 156 | 151 | 154 | 651 | 581 |
| Microarray service & other | 22 | 14 | 16 | 14 | 19 | 11 | 10 | 13 | 23 | 23 | 65 | 53 |
| **Total consumables** | 762 | 807 | 807 | 779 | 768 | 811 | 816 | 832 | 797 | 852 | 3,155 | 3,227 |
| **Total instruments** | 114 | 120 | 107 | 159 | 112 | 101 | 111 | 158 | 120 | 130 | 501 | 482 |
| **Total service & other** | 200 | 185 | 166 | 166 | 161 | 147 | 157 | 169 | 174 | 177 | 716 | 634 |
| **Total sequencing** | 979 | 1,016 | 995 | 1,004 | 947 | 972 | 1,001 | 1,066 | 995 | 1,054 | 3,993 | 3,985 |
| **Total microarray** | 97 | 96 | 85 | 100 | 94 | 87 | 83 | 93 | 96 | 105 | 379 | 358 |
| **Total revenue** | 1,076 | 1,112 | 1,080 | 1,104 | 1,041 | 1,059 | 1,084 | 1,159 | 1,091 | 1,159 | 4,372 | 4,343 |

What it shows: sequencing consumables are the engine at 63% to 70% of revenue; the swings are mostly Q4 instrument seasonality. Total revenue grew 5.0% in Q4'25, 4.8% in Q1'26 and 9.4% in Q2'26 (reported); Q2'26 came from sequencing instruments (+30%), service & other (+20%, including SomaLogic) and consumables (+5%). Sequencing service & other fell about 20% y/y in Q1-Q2'25 because the 2024 base included GRAIL and strategic-partnership revenue (see 1D). Total microarray rose 20.7% in Q2'26 only because SomaLogic is reported there (Section 7).

### 1B. Y/Y growth, reported (consolidated vs consolidated)

| y/y % (reported) | Q1'24 | Q2'24 | Q3'24 | Q4'24 | Q1'25 | Q2'25 | Q3'25 | Q4'25 | Q1'26 | Q2'26 | FY24 | FY25 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sequencing consumables | n/a | n/a | n/a | n/a | 0.7% | 1.5% | 0.8% | 8.3% | 4.3% | 4.7% | n/a | 2.8% |
| Microarray consumables | n/a | n/a | n/a | n/a | 1.4% | -9.0% | 4.5% | -6.2% | -1.4% | 8.5% | n/a | -3.0% |
| Sequencing instruments | n/a | n/a | n/a | n/a | -0.9% | -17.2% | 2.9% | 0.0% | 8.3% | 30.2% | n/a | -3.9% |
| Microarray instruments | n/a | n/a | n/a | n/a | -25.0% | 25.0% | 33.3% | -20.0% | -33.3% | 0.0% | n/a | 0.0% |
| Sequencing service & other | n/a | n/a | n/a | n/a | -20.2% | -20.5% | -2.0% | 2.6% | 6.3% | 13.2% | n/a | -10.8% |
| Microarray service & other | n/a | n/a | n/a | n/a | -13.6% | -21.4% | -37.5% | -7.1% | 21.1% | 109.1% | n/a | -18.5% |
| **Total consumables** | n/a | n/a | n/a | n/a | 0.8% | 0.5% | 1.1% | 6.8% | 3.8% | 5.1% | n/a | 2.3% |
| **Total instruments** | n/a | n/a | n/a | n/a | -1.8% | -15.8% | 3.7% | -0.6% | 7.1% | 28.7% | n/a | -3.8% |
| **Total service & other** | n/a | n/a | n/a | n/a | -19.5% | -20.5% | -5.4% | 1.8% | 8.1% | 20.4% | n/a | -11.5% |
| **Total sequencing** | n/a | n/a | n/a | n/a | -3.3% | -4.3% | 0.6% | 6.2% | 5.1% | 8.4% | n/a | -0.2% |
| **Total microarray** | n/a | n/a | n/a | n/a | -3.1% | -9.4% | -2.4% | -7.0% | 2.1% | 20.7% | n/a | -5.5% |
| **Total revenue** | n/a | n/a | n/a | n/a | -3.3% | -4.8% | 0.4% | 5.0% | 4.8% | 9.4% | n/a | -0.7% |

Basis: [Der] growth = quarter / same quarter a year earlier - 1 using Table 1A, so Q1'25 and Q2'25 growth is measured against a 2024 base that includes GRAIL (total revenue -3.3% and -4.8%, versus -1.4% and -3.0% on the Core basis the company quotes). Company-published figures for cross-check: Q4'25 sequencing consumables +8% (Q4'25 deck: $755M vs $698M), sequencing instruments ~flat ($154M vs $155M Core), sequencing service +4% ($157M vs $151M; my derived line shows +2.6% because of the $1M rounding differences in Table 1E); Q1'26 sequencing consumables +4% reported / +2% organic; Q2'26 +5% reported / +4% organic (Q1'26 and Q2'26 decks, revenue-by-source reconciliation). Microarray instruments are $2M-$5M a quarter, so their percentage swings are noise.

### 1C. Mix, % of total revenue

| % of total revenue | Q1'24 | Q2'24 | Q3'24 | Q4'24 | Q1'25 | Q2'25 | Q3'25 | Q4'25 | Q1'26 | Q2'26 | FY24 | FY25 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sequencing consumables | 64.2% | 65.6% | 68.6% | 63.2% | 66.9% | 69.9% | 68.9% | 65.2% | 66.5% | 66.9% | 65.4% | 67.7% |
| Microarray consumables | 6.6% | 7.0% | 6.1% | 7.3% | 6.9% | 6.7% | 6.4% | 6.6% | 6.5% | 6.6% | 6.8% | 6.6% |
| Sequencing instruments | 10.2% | 10.4% | 9.6% | 13.9% | 10.5% | 9.1% | 9.9% | 13.3% | 10.8% | 10.8% | 11.1% | 10.7% |
| Microarray instruments | 0.4% | 0.4% | 0.3% | 0.5% | 0.3% | 0.5% | 0.4% | 0.3% | 0.2% | 0.4% | 0.4% | 0.4% |
| Sequencing service & other | 16.5% | 15.4% | 13.9% | 13.8% | 13.6% | 12.8% | 13.6% | 13.5% | 13.8% | 13.3% | 14.9% | 13.4% |
| Microarray service & other | 2.0% | 1.3% | 1.5% | 1.3% | 1.8% | 1.0% | 0.9% | 1.1% | 2.1% | 2.0% | 1.5% | 1.2% |
| **Total consumables** | 70.8% | 72.6% | 74.7% | 70.6% | 73.8% | 76.6% | 75.3% | 71.8% | 73.1% | 73.5% | 72.2% | 74.3% |
| **Total instruments** | 10.6% | 10.8% | 9.9% | 14.4% | 10.8% | 9.5% | 10.2% | 13.6% | 11.0% | 11.2% | 11.5% | 11.1% |
| **Total service & other** | 18.6% | 16.6% | 15.4% | 15.0% | 15.5% | 13.9% | 14.5% | 14.6% | 15.9% | 15.3% | 16.4% | 14.6% |
| **Total sequencing** | 91.0% | 91.4% | 92.1% | 90.9% | 91.0% | 91.8% | 92.3% | 92.0% | 91.2% | 90.9% | 91.3% | 91.8% |
| **Total microarray** | 9.0% | 8.6% | 7.9% | 9.1% | 9.0% | 8.2% | 7.7% | 8.0% | 8.8% | 9.1% | 8.7% | 8.2% |

What it shows: consumables (recurring "razor-blade" revenue) were 73% to 77% of revenue in Q1-Q3 and ~71-72% in Q4 when instrument deliveries peak. Instruments were 9.5% to 11% outside Q4 and 13.6% to 14.4% in Q4. Illumina describes ~90% of FY25 revenue as "recurring" (consumables plus service & other) [D, `deck/ILMN_2026-01-13_JPM_Healthcare_Conference_Slides.md`, slide 4]. FY columns are computed from the 10-K totals.

### 1D. Core-basis y/y for Q1'25 and Q2'25 (the base the company uses)

| Core-basis y/y | Q1'24 Core | Q1'25 | y/y | Q2'24 Core | Q2'25 | y/y |
|---|---|---|---|---|---|---|
| Sequencing consumables | 697 | 696 | -0.1% | 737 | 740 | 0.4% |
| Microarray consumables | 71 | 72 | 1.4% | 78 | 71 | -9.0% |
| Sequencing instruments | 110 | 109 | -0.9% | 116 | 96 | -17.2% |
| Microarray instruments | 4 | 3 | -25.0% | 4 | 5 | 25.0% |
| Sequencing service & other | 151 | 142 | -6.0% | 143 | 136 | -4.9% |
| Microarray service & other | 22 | 19 | -13.6% | 14 | 11 | -21.4% |
| Total consumables | 769 | 768 | -0.1% | 815 | 811 | -0.5% |
| Total instruments | 114 | 112 | -1.8% | 120 | 101 | -15.8% |
| Total service & other | 173 | 161 | -6.9% | 157 | 147 | -6.4% |
| **Total revenue** | 1,056 | 1,041 | -1.4% | 1,092 | 1,059 | -3.0% |

Sources: Core revenue by line from Q1'25 10-Q p.31 (Q1'24 Core: consumables 769, instruments 114, service 173, total 1,056) and Q2'25 10-Q p.30 (Q2'24 Core: 815, 120, 157, total 1,092). Core sequencing split [Der] from the Q2'25 deck revenue-by-source table: Q2'24 Core sequencing consumables 737 / instruments 116 / service 143; YTD'24 1,434 / 226 / 294, so Q1'24 Core = YTD less Q2 = 697 / 110 / 151. Microarray lines are identical on both bases. GRAIL bought consumables from Illumina, which is why Q1'24 Core sequencing consumables (697) exceed the consolidated figure (691); GRAIL's cancer-test revenue sat in sequencing service. Q1'24 Core components sum to 1,055 vs 1,056 reported (rounding). On the Core basis, Q1'25 and Q2'25 consumables were flat, instruments fell 2% and 16%, and service fell 6% to 7% (strategic-partnership revenue, per the 10-Qs).

### 1E. Q4 derivation (10-K full year less nine months) vs company-published Q4

| Line | FY24 (10-K) | 9M'24 (Q3'24 10-Q) | Q4'24 [Der] | Q4'24 per Q4'25 deck [D] | FY25 (10-K) | 9M'25 (Q3'25 10-Q) | Q4'25 [Der] | Q4'25 per Q4'25 deck [D] |
|---|---|---|---|---|---|---|---|---|
| Sequencing consumables | 2,858 | 2,160 | 698 | 698 | 2,939 | 2,183 | 756 | 755 |
| Microarray consumables | 297 | 216 | 81 | not in deck | 288 | 212 | 76 | 77 (Bloomberg) |
| Sequencing instruments | 484 | 330 | 154 | 155 (Core) | 465 | 311 | 154 | 154 |
| Microarray instruments | 17 | 12 | 5 | not in deck | 17 | 13 | 4 | 4 (Bloomberg) |
| Sequencing service & other | 651 | 499 | 152 | 151 (Core) | 581 | 425 | 156 | 157 |
| Microarray service & other | 65 | 51 | 14 | not in deck | 53 | 40 | 13 | 12 (Bloomberg) |
| Total revenue | 4,372 | 3,268 | 1,104 | 1,104 | 4,343 | 3,184 | 1,159 | 1,159 |
| Americas | 2,441 | 1,852 | 589 | 589 | 2,406 | 1,768 | 638 | 638 |
| Europe | 1,185 | 859 | 326 | 326 | 1,264 | 911 | 353 | 353 |
| Greater China | 308 | 228 | 80 | 80 | 243 | 187 | 56 | 55 |
| AMEA | 438 | 329 | 109 | 109 | 430 | 318 | 112 | 113 |

Differences of $1M between [Der] and the deck are rounding (the deck rounds each quarter on its own; the 10-K and 10-Q round the YTD totals). Bloomberg's "actual" Q4'25 sequencing/microarray split (755/77, 154/4, 157/12) follows the deck, not my derivation. Sources: `ILMN_10-K_FY2024.md` p.66; `ILMN_10-Q_2024Q3.md` p.13; `ILMN_10-K_FY2025.md` p.67; `ILMN_10-Q_2025Q3.md` p.13; `deck/ILMN_2025Q4_Earnings_Slides.md` (revenue-by-source and region tables).

### 1F. Consensus [E] for the same lines

Source: `Sources/ILMN/consensus/ILMN_Consensus_Quarterlies.md` and `..._Quarterlies_2.md` (Q3'26E, Q4'26E) and `ILMN_Consensus_Annuals.md` (FY26E-FY28E). Actuals from the filings for comparison.

| $M | Q2'26A | Q3'26E | Q4'26E | FY25A | FY26E | FY27E | FY28E |
|---|---|---|---|---|---|---|---|
| Sequencing consumables | 775 | 789.19 | 814.89 | 2,939 | 3,104.44 | 3,378.44 | 3,694.20 |
| Microarray consumables | 77 | 73.63 | 80.74 | 288 | 302.33 | 303.83 | 309.35 |
| Total consumables (Bloomberg row) | 852 | 860.98 | 894.22 | 3,227 | 3,402.07 | 3,668.56 | 3,963.75 |
| Sequencing instruments | 125 | 109.70 | 128.41 | 465 | 482.62 | 453.65 | 453.69 |
| Microarray instruments | 5 | 4.19 | 4.33 | 17 | 15.52 | 15.54 | 15.39 |
| Total instruments (Bloomberg row) | 130 | 115.20 | 131.52 | 482 | 500.40 | 469.68 | 468.45 |
| Sequencing service & other | 154 | 156.48 | 164.68 | 581 | 626.10 | 654.00 | 683.74 |
| Microarray service & other | 23 | 23.49 | 25.92 | 53 | 95.40 | 100.99 | 105.28 |
| Total service & other | 177 | 178.28 | 189.18 | 634 | 718.69 | 752.27 | 786.08 |
| Product revenue | 982 | 976.77 | 1,028.31 | 3,709 | 3,905.08 | 4,148.57 | 4,450.26 |
| Total sequencing | 1,054 | 1,055.45 | 1,107.05 | 3,985 | 4,213.72 | 4,487.43 | 4,830.64 |
| Total microarray | 105 | 101.08 | 110.83 | 358 | 413.00 | 420.18 | 429.50 |
| **Total revenue** | 1,159 | 1,154.22 | 1,219.78 | 4,343 | 4,624.80 | 4,918.25 | 5,262.82 |
| Implied y/y total revenue [Der] | +9.4% | +6.5% (vs 1,084) | +5.2% (vs 1,159) | -0.7% | +6.5% | +6.3% | +7.0% |
| Implied y/y sequencing consumables [Der] | +4.7% | +5.6% (vs 747) | +7.8% (vs 756) | +2.8% | +5.6% | +8.8% | +9.3% |
| Implied y/y sequencing instruments [Der] | +30.2% | +2.5% (vs 107) | -16.6% (vs 154) | -3.9% | +3.8% | -6.0% | 0.0% |

What it shows: consensus FY26E revenue of $4.625B sits at the midpoint of the raised FY26 guide ($4.60B-$4.64B, Q2'26 deck p.12), and Q3'26E $1,154M is near the top of the $1.14B-$1.16B guide. Consensus has sequencing instruments down 16.6% in Q4'26E against a Q4'25 comp that had >100 NovaSeq X placements, and FY26E microarray service & other jumping to $95.4M from $53M, which is the SomaLogic effect. Bloomberg row sums do not tie exactly (e.g., Q3'26E sequencing + microarray consumables = 862.82 vs "Total consumables" 860.98), because contributor sets differ by line. The extra week sits in Q4'26E (about 0.5 point of revenue per management).

---

## 2. Gross margin

Sources: GAAP lines from the income statements in each filing (`ILMN_10-Q_2024Q1.md` p.7, `..._2024Q2.md` p.6, `..._2024Q3.md` p.6, `ILMN_10-K_FY2024.md` p.51, `ILMN_10-Q_2025Q1.md` p.6, `..._2025Q2.md` p.6, `..._2025Q3.md` p.6, `ILMN_10-K_FY2025.md` p.53, `ILMN_10-Q_2026Q1.md` p.6, `..._2026Q2.md` p.6). Q4 columns = 10-K minus nine months [Der]. Non-GAAP gross margin from the decks (Section 3 for sources). Illumina does not allocate the "amortization of acquired intangible assets" line to product or service, so product and service margins below **exclude** that line; the all-in GAAP margin includes it.

### 2A. GAAP cost of revenue and margins ($M)

| $M, consolidated | Q1'24 | Q2'24 | Q3'24 | Q4'24 | Q1'25 | Q2'25 | Q3'25 | Q4'25 | Q1'26 | Q2'26 | FY24 | FY25 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Product revenue | 876 | 927 | 914 | 938 | 880 | 912 | 927 | 990 | 917 | 982 | 3,656 | 3,709 |
| Cost of product revenue | 255 | 250 | 235 | 278 | 253 | 276 | 267 | 312 | 273 | 291 | 1,017 | 1,107 |
| Service & other revenue | 200 | 185 | 166 | 166 | 161 | 147 | 157 | 169 | 174 | 177 | 716 | 634 |
| Cost of service & other revenue | 106 | 95 | 84 | 81 | 88 | 71 | 68 | 72 | 80 | 80 | 367 | 300 |
| Amortization of acquired intangibles (in COGS) | 48 | 46 | 16 | 17 | 17 | 17 | 16 | 16 | 17 | 18 | 127 | 66 |
| Total cost of revenue | 409 | 391 | 335 | 376 | 358 | 364 | 351 | 400 | 370 | 389 | 1,511 | 1,473 |
| **GAAP gross profit** | 667 | 721 | 745 | 728 | 683 | 695 | 733 | 759 | 721 | 770 | 2,861 | 2,870 |
| Product gross margin, ex-amortization [Der] = (product rev - cost of product)/product rev | 70.9% | 73.0% | 74.3% | 70.4% | 71.2% | 69.7% | 71.2% | 68.5% | 70.2% | 70.4% | 72.2% | 70.2% |
| Service & other gross margin [Der] = (service rev - cost of service)/service rev | 47.0% | 48.6% | 49.4% | 51.2% | 45.3% | 51.7% | 56.7% | 57.4% | 54.0% | 54.8% | 48.7% | 52.7% |
| **GAAP gross margin** [Der] = GP/revenue (ties to company-reported margins) | 62.0% | 64.8% | 69.0% | 65.9% | 65.6% | 65.6% | 67.6% | 65.5% | 66.1% | 66.4% | 65.4% | 66.1% |
| GAAP gross margin ex-amortization of intangibles [Der] = (GP+amort)/revenue | 66.4% | 69.0% | 70.5% | 67.5% | 67.2% | 67.2% | 69.1% | 66.9% | 67.6% | 68.0% | 68.3% | 67.6% |
| Core Illumina GAAP gross margin [D, 10-Q/10-K MD&A; Q4'24 Der = 728/1,104] | 65.7% | 68.0% | 68.9% | 65.9% | n/a | n/a | n/a | n/a | n/a | n/a | 67.1% | n/a |
| **Non-GAAP gross margin** [D, decks; Q1'24 Core Der; FY24 is Core] | 67.0% | 69.4% | 70.5% | 67.4% | 67.4% | 69.4% | 69.2% | 67.0% | 68.2% | 68.2% | 68.6% | 68.2% |

Q4 derivations [Der]: Q4'24 cost of product 1,017 - 739 = 278; cost of service 367 - 286 = 81; amortization 127 - 110 = 17; GP 2,861 - 2,133 = 728. Q4'25 cost of product 1,107 - 795 = 312; cost of service 300 - 228 = 72; amortization 66 - 50 = 16; GP 2,870 - 2,111 = 759 (the Q4'25 deck also shows 759 / 65.5%). The four quarters of cost of product sum to 1 more than the 10-K figure in both years (rounding).

What it shows: the all-in GAAP gross margin has stepped up from 62.0% in Q1'24 (GRAIL's losses and $48M of quarterly amortization) to a 65.5%-67.6% range since the spin-off, and amortization fell from $48M to ~$17M a quarter as the GRAIL-related intangibles went away. Product margin (ex-amortization) was 71.2% in Q1'25, 69.7% in Q2'25 (72.3% excluding the $23M impairment: (912 - 253)/912 [Der]), 71.2% in Q3'25, 68.5% in Q4'25 (instrument-heavy quarter), 70.2% in Q1'26 and 70.4% in Q2'26. Service & other margin rose from 45.3% in Q1'25 to 51.7% in Q2'25 and ~54%-57% since Q3'25 as lower-margin strategic-partnership revenue shrank. Management's explanations: Q2'26 gross margin fell on a non-GAAP basis y/y (69.4% to 68.2%) on higher instrument mix, rising memory-chip and freight costs (Middle East conflict) and lower-margin SomaLogic revenue, partly offset by lower tariff costs (Q2'26 10-Q p.33; Q1'26 and Q2'26 decks p.10). Estimated annual tariff cost was ~$85M as of Q1'25, mostly from importing out of Singapore (Q1'25 10-Q p.28).

### 2B. GAAP-to-non-GAAP gross profit bridge ($M)

| $M | Q1'24 Core | Q2'24 Core | Q3'24 | Q4'24 | Q1'25 | Q2'25 | Q3'25 | Q4'25 | Q1'26 | Q2'26 | FY24 Core | FY25 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GAAP gross profit (Core in 2024) | 693 | 743 | 745 | 728 | 683 | 695 | 733 | 759 | 721 | 770 | 2,909 | 2,870 |
| + Acquisition-related (amortization of intangibles; Q1'26/Q2'26 include $6M/$2M SomaLogic inventory step-up) | 15 | 15 | 16 | 17 | 17 | 16 | 16 | 16 | 23 | 20 | 63 | 66 |
| + Transformational initiatives | 0 | 0 | 0 | 0 | 2 | 1 | 1 | 2 | 0 | 0 | 1 | 5 |
| + Intangible impairment (in cost of product) | 0 | 0 | 0 | 0 | 0 | 23 | 0 | 0 | 0 | 0 | 0 | 23 |
| **Non-GAAP gross profit** | 708 | 758 | 761 | 745 | 702 | 735 | 750 | 777 | 744 | 790 | 2,973 | 2,964 |
| Non-GAAP gross margin | 67.0% | 69.4% | 70.5% | 67.4% | 67.4% | 69.4% | 69.2% | 67.0% | 68.2% | 68.2% | 68.6% | 68.2% |

Sources: deck Table 3 reconciliations: `deck/ILMN_2025Q2_Earnings_Slides.md` (Q2'24 Core, Q2'25, 6M'24/6M'25; Q1'24 Core [Der] = 6M less Q2), `..._2025Q3_...` (Q3'24, Q3'25), `..._2025Q4_...` (Q4'24, Q4'25, FY), `..._2026Q1_...` (Q1'25, Q1'26), `..._2026Q2_...` (Q2'26). Small rounding differences: the 10-Q amortization line for Q2'25 is $17M versus $16M in the deck's acquisition-related item. Amortization expected: $39M for the remainder of 2026 per the Q2'26 10-Q (vs $59M in the Q1'26 10-Q), $78M in 2027 (Core Notes 02 summary of the 10-Q tables).

### 2C. Consensus [E]: gross margin lines

| | Q2'26A | Q3'26E | Q4'26E | FY25A | FY26E | FY27E | FY28E |
|---|---|---|---|---|---|---|---|
| Non-GAAP gross margin | 68.2% | 68.84% | 68.68% | 68.2% | 68.47% | 69.05% | 69.53% |
| Non-GAAP gross profit | 790 | 792.74 | 836.37 | 2,964 | 3,160.66 | 3,401.36 | 3,702.53 |
| "Cost of products sold" (Bloomberg; actuals shown equal GAAP) | 291 | 281.99 | 300.81 | 1,107 | 1,145.81 | 1,189.50 | 1,265.99 |
| "Cost of services sold" | 80 | 80.65 | 82.38 | 300 | 309.74 | 340.71 | 342.94 |
| GAAP gross profit | 770 | 783.94 | 821.73 | 2,870 | 2,740.01 (see flag) | 3,352.10 | 3,636.52 |
| GAAP gross margin | 66.4% | 67.98% | 67.44% | 66.1% | 67.49% | 68.23% | 68.64% |
| Amortization of intangibles | 18 | 16.04 | 16.18 | 66 | 56.20 | 62.03 | 54.35 |

Flags: FY26E GAAP gross profit of $2,740.01M is inconsistent with the same file's FY26E GAAP gross margin of 67.49% (2,740/4,625 = 59.2%); treat the dollar figure as a data error. Consensus amortization of $16M a quarter looks low against the 10-Q's own schedule ($35M actual in 1H'26 plus $39M expected for 2H'26) and FY26E $56.2M is below the $35M + $39M = $74M implied by the filing. The Bloomberg "cost of products/services" rows in the "adjusted" block equal GAAP actuals for historical quarters (e.g., 253, 276, 267, 312), so they are GAAP-basis lines and do not tie to revenue less non-GAAP gross profit.

---

## 3. Operating expenses, profitability, cash flow, shares, tax

Sources: GAAP from the income statements (see Section 2). Non-GAAP from the earnings decks: `deck/ILMN_2025Q2_Earnings_Slides.md` (Q2'24 Core, Q2'25, 6M), `..._2025Q3_...` (Q3'24, Q3'25), `..._2025Q4_...` (Q4'24, Q4'25, FY24 Core, FY25), `..._2026Q1_...` (Q1'25, Q1'26), `..._2026Q2_...` (Q2'26). **2024 non-GAAP is Core Illumina**, the basis the company compares against; Q1'24 Core is [Der] = six-month Core (Q2'25 deck) minus Q2'24 Core. Cash flow from the decks' cash-flow tables.

### 3A. GAAP operating expenses and operating income ($M)

| $M, GAAP, consolidated | Q1'24 | Q2'24 | Q3'24 | Q4'24 | Q1'25 | Q2'25 | Q3'25 | Q4'25 | Q1'26 | Q2'26 | FY24 | FY25 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Research & development | 339 | 325 | 253 | 256 | 252 | 247 | 229 | 239 | 240 | 252 | 1,169 | 967 |
| Selling, general & administrative | 439 | 147 | 239 | 279 | 267 | 234 | 277 | 309 | 272 | 273 | 1,092 | 1,086 |
| Goodwill & intangible impairment | 0 | 1,886 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1,889 | 0 |
| Legal contingency & settlement | 0 | 0 | -488 | 18 | 0 | 0 | 0 | 10 | 0 | 0 | -456 | 10 |
| **GAAP operating income (loss)** | -111 | -1,637 | 741 | 175 | 164 | 214 | 227 | 201 | 209 | 245 | -833 | 807 |
| R&D % of revenue | 31.5% | 29.2% | 23.4% | 23.2% | 24.2% | 23.3% | 21.1% | 20.6% | 22.0% | 21.7% | 26.7% | 22.3% |
| SG&A % of revenue | 40.8% | 13.2% | 22.1% | 25.3% | 25.6% | 22.1% | 25.6% | 26.7% | 24.9% | 23.6% | 25.0% | 25.0% |
| **GAAP operating margin** | -10.3% | -147.2% | 68.6% | 15.9% | 15.8% | 20.2% | 20.9% | 17.3% | 19.2% | 21.1% | -19.1% | 18.6% |

Notes: Q2'24 SG&A of $147M is low because it includes a ~$271M gain on GRAIL contingent-consideration fair value (Q2'25 deck footnote c); the Q2'24 impairment is GRAIL goodwill ($1,466M) and IPR&D ($420M). Q3'24 "legal contingency and settlement" of -$488M is the reversal of the European Commission fine. Q4'24 and Q4'25 [Der]: SG&A 1,092 - 813 = 279 and 1,086 - 777 = 309; the Q4'25 deck shows SG&A $310M, legal $8M and operating profit $202M, versus my $309M, $10M and $201M (rounding in YTD figures). Q4'25 SG&A includes a $19M donation to the Illumina Foundation (deck footnote g). Quarterly R&D fell from $339M (Q1'24, with GRAIL) to $229M-$252M; Q1'26 and Q2'26 R&D were $240M and $252M (-4.8% and +2.0% y/y).

### 3B. Segment-expense view (ASU 2023-07 disclosure, one segment)

| $M | Q1'25 | Q2'25 | Q3'25 | Q4'25 [Der] | FY25 | Q1'26 [Der] | Q2'26 |
|---|---|---|---|---|---|---|---|
| Cost of revenue | 358 | 364 | 351 | 400 | 1,473 | 370 | 389 |
| R&D | 252 | 247 | 229 | 239 | 967 | 240 | 252 |
| Selling & marketing | 165 | 146 | 148 | 160 | 618 | 158 | 164 |
| General & administrative | 102 | 88 | 129 | 149 | 468 | 114 | 109 |
| Income from operations | 164 | 214 | 227 | 201 | 807 | 209 | 245 |

Sources: Q1'25 10-Q p.28 (S&M 165); Q2'25 10-Q p.26 (YTD 311, 190; Q2 146, 88); Q3'25 10-Q segment note (Q3 148/129; YTD 458/319); FY25 10-K Note 12 (618/468); Q1'26 10-Q (S&M 158); Q2'26 10-Q p.29 (YTD 322/223; Q2 164/109). [Der]: Q1'25 G&A = SG&A 267 - S&M 165 = 102; Q4'25 = FY less nine months (S&M 618 - 458 = 160; G&A 468 - 319 = 149); Q1'26 G&A = YTD 223 - Q2 109 = 114. Q3'25 G&A of $129M and Q4'25 of $149M are elevated by ERP-upgrade costs, acquisition costs and the $19M foundation donation. Core Illumina 2024 operating income (consolidated GRAIL excluded): Q1 $116M [Der = 558 - 442], Q2 $442M, Q3 $741M (includes the $488M EC-fine reversal), Q4 $175M, FY $1,473M (Q2'25, Q3'25 10-Q segment notes; FY25 10-K).

### 3C. Non-GAAP profitability ($M, except per share)

| Non-GAAP ($M); 2024 = Core Illumina | Q1'24 | Q2'24 | Q3'24 | Q4'24 | Q1'25 | Q2'25 | Q3'25 | Q4'25 | Q1'26 | Q2'26 | FY24 | FY25 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Revenue (Core basis in 2024) | 1,056 | 1,092 | 1,080 | 1,104 | 1,041 | 1,059 | 1,084 | 1,159 | 1,091 | 1,159 | 4,332 | 4,343 |
| Non-GAAP gross profit | 708 | 758 | 761 | 745 | 702 | 735 | 750 | 777 | 744 | 790 | 2,973 | 2,964 |
| Non-GAAP R&D | 236 | 241 | 249 | 255 | 241 | 243 | 228 | 238 | 239 | 252 | 982 | 950 |
| Non-GAAP SG&A | 254 | 275 | 268 | 271 | 248 | 241 | 256 | 264 | 267 | 278 | 1,069 | 1,009 |
| **Non-GAAP operating income** | 218 | 242 | 244 | 218 | 212 | 252 | 265 | 275 | 239 | 260 | 922 | 1,004 |
| R&D % of revenue [Der] | 22.3% | 22.1% | 23.1% | 23.1% | 23.2% | 22.9% | 21.0% | 20.5% | 21.9% | 21.7% | 22.7% | 21.9% |
| SG&A % of revenue [Der] | 24.1% | 25.2% | 24.8% | 24.5% | 23.8% | 22.8% | 23.6% | 22.8% | 24.5% | 24.0% | 24.7% | 23.2% |
| **Non-GAAP operating margin** [D; Q1'24 Der = 218/1,056] | 20.6% | 22.2% | 22.6% | 19.7% | 20.4% | 23.8% | 24.5% | 23.7% | 21.9% | 22.5% | 21.3% | 23.1% |
| Non-GAAP operating income y/y [Der] | n/a | n/a | n/a | n/a | -2.8% | 4.1% | 8.6% | 26.1% | 12.7% | 3.2% | n/a | 8.9% |
| Non-GAAP tax rate | n/a | 24.2% | 21.0% | 23.7% | 22.0% | 22.2% | 18.6% | 19.5% | 20.5% | 20.5% | 23.6% | 20.5% |
| Non-GAAP net income | 155 | 174 | 181 | 152 | 154 | 187 | 206 | 208 | 177 | 200 | 663 | 756 |
| **Non-GAAP diluted EPS ($)**, Core in 2024 | 0.98 | 1.09 | 1.14 | 0.95 | 0.97 | 1.19 | 1.34 | 1.35 | 1.15 | 1.31 | 4.16 | 4.84 |
| Non-GAAP diluted EPS ($), consolidated in 2024 (incl. GRAIL to Jun 24) | 0.09 | 0.36 | 1.14 | 0.86 | n/a | n/a | n/a | n/a | n/a | n/a | 2.45 | n/a |
| Non-GAAP EPS y/y [Der] | n/a | n/a | n/a | n/a | -1.0% | 9.2% | 17.5% | 42.1% | 18.6% | 10.1% | n/a | 16.3% |

Derivations of Q1'24 Core [Der]: gross profit 1,466 - 758 = 708; R&D 477 - 241 = 236; SG&A 529 - 275 = 254; operating profit 460 - 242 = 218; EPS 2.07 - 1.09 = 0.98; net income 329 - 174 = 155 (all from the six-month and three-month Core columns of Table 3 in the Q2'25 deck appendix). Q1'25 non-GAAP lines are the Q1'25 comparison column in the Q1'26 deck (GP $702M/67.4%, R&D $241M, SG&A $248M, OI $212M/20.4%, EPS $0.97, tax 22.0%); net income $154M is the Bloomberg actual (the Q2'25 deck's six-month $342M less Q2 $187M gives $155M). The check is that the four 2025 quarters sum to the deck's FY25 figures (OI 212 + 252 + 265 + 275 = 1,004 [D: 1,004]; EPS 0.97 + 1.19 + 1.34 + 1.35 = 4.85 vs 4.84 [D]).

What it shows: non-GAAP operating margin expanded from 20.4% in Q1'25 to 23.8%-24.5% in Q2-Q3'25, dipped to 23.7% in Q4'25 and then to 21.9% in Q1'26 (SomaLogic dilution of ~100 bps in the guide, ERP and professional costs, seasonally low revenue) before recovering to 22.5% in Q2'26. Q2'26 non-GAAP operating margin of 22.5% was 130 bps lower y/y (23.8% in Q2'25) while non-GAAP EPS rose 10% to $1.31, helped by lower share count and a 20.5% tax rate. Non-GAAP SG&A grew 7.7% and 15.4% y/y in Q1'26 and Q2'26 (SomaLogic headcount, legal, ERP) versus a 2.6%-4.5% decline in Q3'25-Q4'25. The company's FY27 targets (JPM Jan 2026, p.7): ~26% non-GAAP operating margin ex-China (500+ bps expansion from FY24's 21%), EPS growth of double digits to teens, HSD revenue growth. Q4'24 consolidated non-GAAP EPS ($0.86) differs from Core ($0.95) because of a higher non-GAAP tax line ($62M vs $47M, 31.1% vs 23.7%); the company's Q4'25 y/y (+42%) compares to $0.95 (Q4'25 deck: slide 12 and appendix Table 1).

### 3D. GAAP below the line, tax, shares

| GAAP | Q1'24 | Q2'24 | Q3'24 | Q4'24 | Q1'25 | Q2'25 | Q3'25 | Q4'25 | Q1'26 | Q2'26 | FY24 | FY25 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pre-tax income (loss) | -109 | -1,976 | 720 | 187 | 182 | 306 | 220 | 377 | 157 | 260 | -1,179 | 1,086 |
| Provision for income taxes | 17 | 12 | 15 | 0 | 51 | 71 | 70 | 43 | 23 | 53 | 44 | 236 |
| GAAP effective tax rate [Der] | n/a | n/a | 2.1% | 0.0% | 28.0% | 23.2% | 31.8% | 11.4% | 14.6% | 20.4% | n/a | 21.7% |
| GAAP net income (loss) | -126 | -1,988 | 705 | 187 | 131 | 235 | 150 | 334 | 134 | 207 | -1,223 | 850 |
| GAAP diluted EPS ($) | -0.79 | -12.48 | 4.42 | 1.17 | 0.82 | 1.49 | 0.98 | 2.16 | 0.87 | 1.35 | -7.69 | 5.45 |
| Diluted weighted-average shares (M) | 159.0 | 159.0 | 160.0 | 160.0 | 159.0 | 157.0 | 154.0 | 154.6 | 154.0 | 153.0 | 159.0 | 156.0 |
| Shares outstanding per 10-Q/10-K cover (M), date in note | 159.3 | 159.3 | 158.6 | 158.4 | 158.3 | 153.7 | 152.8 | 152.9 | 151.3 | 151.0 | n/a | n/a |

Notes: Q4'24 [Der] provision = FY 44 - nine-month 44 = 0 (the Q4'25 deck shows $1M; 0.6%); Q4'25 [Der] provision 236 - 193 = 43 (deck: $44M, 11.6%; 11.4% from filing numbers). Q4'24 diluted shares ~160M [Der = NI 187 / EPS 1.17]; Q4'25 ~154.6M [Der = NI 334 / EPS 2.16]; Bloomberg lists 154. GAAP tax rates reported by the company: Q1'25 27.9%, Q2'25 23.4%, Q3'25 31.8% (includes a one-time $42M valuation allowance on foreign tax credits after the July 4, 2025 US tax law), Q4'25 11.6%, Q1'26 14.8%, Q2'26 20.5%; FY25 21.7% (includes a $74M Singapore valuation-allowance release; FY25 10-K income-tax note). Q1'26 and YTD'26 rates (14.8% and 18.4%) are low "primarily due to prior year tax return adjustments" (10-Qs). Cover-page share counts are as of: Apr 26 '24, Aug 2 '24, Nov 1 '24, Feb 7 '25, May 2 '25, Jul 25 '25, Oct 24 '25, Feb 6 '26, Apr 24 '26, Jul 24 '26. The cover-page share count fell about 5% in ~2.25 years (about 2% a year), from 159.3M (Apr '24) to 151.0M (Jul '26).

### 3E. Cash flow and buybacks ($M)

| $M, consolidated | Q1'24 | Q2'24 | Q3'24 | Q4'24 | Q1'25 | Q2'25 | Q3'25 | Q4'25 | Q1'26 | Q2'26 | FY24 | FY25 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cash from operations | 77 | 80 | 316 | 364 | 240 | 234 | 284 | 321 | 289 | 201 | 837 | 1,079 |
| Capex (purchases of property & equipment) | 35 | 32 | 32 | 42 | 32 | 30 | 31 | 54 | 38 | 39 | 142 | 148 |
| **Free cash flow** (CFO - capex, company definition) | 42 | 48 | 284 | 322 | 208 | 204 | 253 | 267 | 251 | 162 | 695 | 931 |
| FCF / non-GAAP net income [Der] (2025 on; FY24 on Core: 1,070/663) | n/a | n/a | n/a | n/a | 135% | 109% | 123% | 128% | 142% | 81% | 161% | 123% |
| Core Illumina FCF (2024; excludes GRAIL) | 251 | 213 | 284 | 322 | n/a | n/a | n/a | n/a | n/a | n/a | 1,070 | n/a |

Sources: cash-flow tables in the decks (Q2'25 deck: Q2'24/Q2'25 and six months; Q3'25: nine months; Q4'25: FY; Q1'26; Q2'26). Q1'24 consolidated is [Der] = six-month 2024 (CFO 157, capex 67, FCF 90) less Q2'24 (80, 32, 48). Core Q1'24 [Der] = 464 - 213 = 251. FY24 consolidated FCF of $695M is depressed by GRAIL operations (Core $1,070M). Quarterly FY sums can differ by $1M (capex 35 + 32 + 32 + 42 = 141 vs 142 reported). Buybacks per decks: Q2'25 ~4.5M shares at $84.66 (~$380M); Q3'25 ~1.24M at $97.10 (~$120M); Q4'25 ~337K at $124.12 (~$42M); Q1'26 ~2.0M at $120.85 (~$242M, plus a new $1.5B authorization announced Apr 30); Q2'26 ~0.94M at $129.07 (~$122M). Q1'25 (cash-flow line $200M, Bloomberg). FY25 repurchases ~$740M (JPM deck p.16). Cash, cash equivalents and short-term investments: Q1'25 $1,237M; Q2'25 $1,155M; Q3'25 ~$1.28B; Q4'25 ~$1.63B; Q1'26 ~$1.16B; Q2'26 ~$1.17B; total debt ~$1.99B at Q2'26 (gross leverage ~1.6x). $30M was paid on Jul 27, 2026 to buy out the remaining SomaLogic contingent consideration (Q2'26 10-Q p.35). The $500M 4.65% notes due Sep 9, 2026 are now current debt.

What it shows: FCF was $931M in FY25 (21.4% of revenue) against non-GAAP net income of $756M (123% conversion), and $412M in 1H'26 (flat vs 1H'25's $412M) because Q2'26 FCF was $162M versus $204M (operating cash flow $201M vs $234M; Bloomberg's cash-flow table shows working-capital outflows of -$26M receivables, -$18M inventory and -$46M other assets in Q2'26; capex $39M vs $30M). Share repurchases by quarter, per the decks, ranged from ~$42M (Q4'25) to ~$380M (Q2'25).

### 3F. Consensus [E]: operating, EPS, cash-flow lines

| | Q2'26A | Q3'26E | Q4'26E | FY25A | FY26E | FY27E | FY28E |
|---|---|---|---|---|---|---|---|
| Non-GAAP R&D | 252 | 246.53 | 249.23 | 950 | 984.15 | 1,020.00 | 1,059.16 |
| Non-GAAP SG&A | 278 | 271.04 | 272.99 | 1,009 | 1,089.72 | 1,121.46 | 1,164.51 |
| **Non-GAAP operating income** | 260 | 276.87 | 312.50 | 1,004 | 1,088.46 | 1,234.92 | 1,396.08 |
| Non-GAAP operating margin | 22.5% | 24.00% | 25.54% | 23.1% | 23.50% | 25.22% | 26.50% |
| Non-GAAP tax rate | 20.5% | 20.4% | 20.4% | 20.5% | 20.49% | 20.46% | 20.43% |
| Non-GAAP net income | 200.4 | 207.13 | 235.13 | 756 | 821.00 | 936.37 | 1,073.19 |
| Diluted shares (M) | 153 | 152.77 | 152.70 | 156 | 153.11 | 152.71 | 152.55 |
| **Non-GAAP diluted EPS ($)** | 1.31 | 1.36 | 1.54 | 4.84 | 5.36 | 6.11 | 7.01 |
| GAAP SG&A | 273 | 283.33 | 285.68 | 1,086 | 1,048.00 | 1,180.11 | 1,233.43 |
| GAAP R&D | 252 | 246.39 | 244.20 | 967 | 981.17 | n/a | n/a |
| GAAP operating income | 245 | 244.52 | 276.95 | 807 | 944.24 | 1,128.29 | 1,306.75 |
| GAAP operating margin | 21.1% | 21.77% | 22.78% | 18.6% | 21.26% | 23.19% | 25.00% |
| GAAP net income | 207 | 194.69 | 218.38 | 850 | 765.77 | 877.79 | 1,019.17 |
| GAAP diluted EPS ($) | 1.35 | 1.28 | 1.43 | 5.45 | 5.02 | 5.71 | 6.56 |
| Stock-based comp | ~73 | 74.63 | 73.93 | 275 | 282.02 | 295.83 | 311.55 |
| Cash from operations | 201 | 326.13 | 353.68 | 1,079 | 1,177.50 | 1,325.72 | 1,459.08 |
| Capex | 40 (Bloomberg; deck 39) | 51.41 | 58.25 | 148 | 197.36 | 203.43 | 198.75 |
| **Free cash flow** | 162 | 335.17 | 283.92 | 931 | 997.28 | 1,101.54 | 1,239.13 |
| Share repurchases | 128 | 90.53 | 90.53 | 742 | 419.65 | 313.00 | 500.50 |

Company guidance for comparison (Q2'26 deck p.12, issued 07/30/2026): FY26 operating margin 23.4%-23.6%, EPS $5.30-$5.40; Q3'26 operating margin ~24%, EPS $1.33-$1.38. Consensus FY26E EPS $5.36 and operating margin 23.50% sit mid-range; Q3'26E EPS $1.36 and 24.00% sit mid-to-upper range. Flags: consensus Q3'26E FCF of $335M (39% FCF margin per the Bloomberg row) is far above any recent quarter and the FY26E FCF of $997M is below the sum of 1H'26 actual ($412M) plus Q3E and Q4E ($619M) = $1,031M, so contributor sets differ; Q3'26E GAAP EPS of $1.28 is below Q2'26A GAAP $1.35. The quarterly stock-based-comp row is printed in a different unit in the Bloomberg file (e.g., "7463" = $74.63M); the annual rows are in $M.

---

## 4. Revenue by region

Source for 2024-2025 (old basis): "Revenue by Geographic Area" note in each filing (same files as Section 1; FY25 10-K p.67). Region is by destination. Greater China = China + Taiwan + Hong Kong. AMEA includes Russia and Turkey. Q4 columns [Der] = 10-K less nine months (Table 1E). The company's own Q4'25 deck shows Greater China $55M and AMEA $113M (my derived $56M and $112M; rounding).

### 4A. Old basis through Q4'25: Americas / Europe / Greater China / AMEA ($M)

| $M (old four-region basis) | Q1'24 | Q2'24 | Q3'24 | Q4'24 | Q1'25 | Q2'25 | Q3'25 | Q4'25 | FY24 | FY25 |
|---|---|---|---|---|---|---|---|---|---|---|
| Americas | 603 | 640 | 609 | 589 | 570 | 586 | 612 | 638 | 2,441 | 2,406 |
| Europe | 279 | 289 | 291 | 326 | 293 | 310 | 309 | 353 | 1,185 | 1,264 |
| Greater China | 78 | 75 | 75 | 80 | 72 | 63 | 52 | 56 | 308 | 243 |
| AMEA (Asia-Pacific, Middle East & Africa) | 116 | 108 | 105 | 109 | 106 | 100 | 111 | 112 | 438 | 430 |
| **Total** | 1,076 | 1,112 | 1,080 | 1,104 | 1,041 | 1,059 | 1,084 | 1,159 | 4,372 | 4,343 |

**Y/Y growth, reported [Der]** (2025 quarters vs consolidated 2024 quarters; GRAIL sat mainly in Americas):

| y/y % reported | Q1'24 | Q2'24 | Q3'24 | Q4'24 | Q1'25 | Q2'25 | Q3'25 | Q4'25 | FY24 | FY25 |
|---|---|---|---|---|---|---|---|---|---|---|
| Americas | n/a | n/a | n/a | n/a | -5.5% | -8.4% | 0.5% | 8.3% | n/a | -1.4% |
| Europe | n/a | n/a | n/a | n/a | 5.0% | 7.3% | 6.2% | 8.3% | n/a | 6.7% |
| Greater China | n/a | n/a | n/a | n/a | -7.7% | -16.0% | -30.7% | -30.0% | n/a | -21.1% |
| AMEA (Asia-Pacific, Middle East & Africa) | n/a | n/a | n/a | n/a | -8.6% | -7.4% | 5.7% | 2.8% | n/a | -1.8% |
| **Total** | n/a | n/a | n/a | n/a | -3.3% | -4.8% | 0.4% | 5.0% | n/a | -0.7% |

**Mix [Der]:**

| % of total revenue | Q1'24 | Q2'24 | Q3'24 | Q4'24 | Q1'25 | Q2'25 | Q3'25 | Q4'25 | FY24 | FY25 |
|---|---|---|---|---|---|---|---|---|---|---|
| Americas | 56.0% | 57.6% | 56.4% | 53.4% | 54.8% | 55.3% | 56.5% | 55.0% | 55.8% | 55.4% |
| Europe | 25.9% | 26.0% | 26.9% | 29.5% | 28.1% | 29.3% | 28.5% | 30.5% | 27.1% | 29.1% |
| Greater China | 7.2% | 6.7% | 6.9% | 7.2% | 6.9% | 5.9% | 4.8% | 4.8% | 7.0% | 5.6% |
| AMEA (Asia-Pacific, Middle East & Africa) | 10.8% | 9.7% | 9.7% | 9.9% | 10.2% | 9.4% | 10.2% | 9.7% | 10.0% | 9.9% |

What it shows: Greater China fell from 7.2% of revenue in Q4'24 to 4.8% in Q3'25 and Q4'25 (reported growth -15%, -31%, -30% in Q2-Q4'25 per the decks) after Illumina was put on China's unreliable entities list in Q1'25 and barred from exporting sequencing instruments there. Excluding China, revenue grew 2.7% in Q3'25 and 7.7% in Q4'25 on a reported basis against a Core base ([Der]; company CC: +2% and +7%). Americas swung from -8.4% (Q2'25) to +8.3% (Q4'25), led by US clinical; Europe grew 5%-8% reported each quarter, with a currency tailwind in the second half (Q3'25 CC +3% vs +6% reported; Q4'25 CC +5% vs +8%). Constant-currency growth by region from the decks: Q2'25 Americas -5%, Europe +6%, Greater China -14%, AMEA -6%; Q3'25 +1%, +3%, -31%, +8%; Q4'25 +8%, +5%, -30%, +6% (Q2'25, Q3'25, Q4'25 decks, slide 3 and region tables). US revenue alone was $2,243M in FY25 (51.6% of revenue), $2,288M in FY24 and $2,359M in FY23 (FY25 10-K p.67). Greater China guidance: FY25 $190M-$210M (Q2'25 deck) raised to ~$220M (Q3'25) versus the $243M actual; FY26 $210M-$220M (Q4'25 call).

### 4B. New basis from Q1'26: USCAN / EMEALA / APAC / Greater China (recast)

| $M (new basis) | Q1'25 (recast) | Q1'26 | y/y [Der] | Q1'26 organic / reported [D, deck] | Q2'25 (recast) | Q2'26 | y/y [Der] | Q2'26 organic / reported [D, deck] | Mix Q1'26 | Mix Q2'26 |
|---|---|---|---|---|---|---|---|---|---|---|
| USCAN (US & Canada) | 555 | 590 | 6.3% | +5% / +6% | 569 | 653 | 14.8% | +13% / +15% | 54.1% | 56.3% |
| EMEALA (Europe, Middle East, Africa, Latin America) | 332 | 356 | 7.2% | +1% / +7% | 355 | 368 | 3.7% | 0% / +4% | 32.6% | 31.8% |
| APAC (Asia-Pacific ex-China) | 82 | 93 | 13.4% | +4% / +13% | 72 | 82 | 13.9% | +9% / +14% | 8.5% | 7.1% |
| Greater China | 72 | 52 | -27.8% | -29% / -27% | 63 | 56 | -11.1% | -19% / -12% | 4.8% | 4.8% |
| **Total** | 1,041 | 1,091 | +4.8% | +1.2% / +4.8% | 1,059 | 1,159 | +9.4% | +6.5% / +9.5% | 100% | 100% |

Sources: Q1'26 10-Q p.16 (Q1'25 recast: 555 / 332 / 72 / 82), Q2'26 10-Q p.16 (Q2'25 recast: 569 / 355 / 63 / 72; YTD'25 1,125 / 686 / 135 / 154; YTD'26 1,243 / 725 / 108 / 175); organic and reported growth from the Q1'26 and Q2'26 decks (revenue-by-region reconciliation tables, pp.4). The 10-Q footnote: "We implemented a new global commercial structure in Q1 2026... Prior period amounts were reclassified." The recast moves Latin America (out of Americas) and Middle East & Africa (out of AMEA) into EMEALA. Check [Der] for Q2'25: old Europe 310 + Latin America ~17 (old Americas 586 - USCAN 569) + Middle East & Africa ~28 (old AMEA 100 - APAC 72) = 355 = recast EMEALA. Greater China is unchanged between the two bases, so its series is continuous. **Acquisition effect by region** (SomaLogic): Q1'26 USCAN -1 pt, EMEALA -1, APAC -9, Greater China -1; Q2'26 USCAN -2, EMEALA -1, APAC -8, Greater China -6 (deck reconciliations; "impact of acquisitions" as a percentage of prior-year regional revenue, i.e., roughly $7M of APAC revenue in Q1'26 and ~$4M of Greater China revenue in Q2'26). This is why Greater China reported -12% but organic -19% in Q2'26.

What it shows: USCAN is the growth engine (+15% reported in Q2'26, +13% organic, tied to US clinical placements and consumables; the Q2'26 call says US/Canada clinical consumables grew above 20%), EMEALA is flat organically (0% in Q2'26, +1% in Q1'26; "near-term dynamics in the region" and FX), APAC ex-China is +4% to +9% organic, and Greater China is 4.8% of revenue and still shrinking (-$20M y/y in Q1'26 and -$7M in Q2'26 per the 10-Qs, "primarily due to our inclusion on the unreliable entities list"). **Gap:** Q3'25 and Q4'25 on the new basis are not in the files provided (the 10-K was filed before the recast); the Q3'26 10-Q (not yet filed when this was built) would be the next place to find Q3'25, and Q4'25 recast would first appear in the FY26 10-K.

### 4C. Consensus [E] by region (Bloomberg basis is unclear, see flag)

| $M | Q2'26A (new basis) | Q3'26E | Q4'26E | FY25A (old basis) | FY26E | FY27E | FY28E |
|---|---|---|---|---|---|---|---|
| "Americas" | 653 | 661.24 | 696.36 | 2,406 | 2,597.57 | 2,853.25 | 3,139.92 |
| "Europe" | 368 | 332.18 | 379.48 | 1,264 | 1,359.88 | 1,461.87 | 1,571.51 |
| Greater China | 56 | 50.87 | 51.86 | 243 | 210.72 | 189.22 | 187.12 |
| "Asia-Pacific, Middle East & Africa" | 82 | 112.71 | 112.77 | 430 | 439.78 | 489.46 | 527.01 |
| Memo: "Europe, Middle East & Africa" (Bloomberg "Prior Disclosures") | n/a | 355.10 | 387.10 | n/a | 1,466.24 | 1,550.11 | 1,691.09 |
| Sum of the four rows [Der] | 1,159 | 1,157.0 | 1,240.5 | 4,343 | 4,608.0 | 4,993.8 | 5,425.6 |
| Total revenue estimate | 1,159 | 1,154.22 | 1,219.78 | 4,343 | 4,624.80 | 4,918.25 | 5,262.82 |

Flag: Bloomberg's Q1'26A and Q2'26A cells in the "Americas/Europe/APAC&ME" rows hold the new-basis USCAN/EMEALA/APAC actuals (590/356/93; 653/368/82), but the Q3'26E onward cells (e.g., Europe $332M, APAC&ME $113M) look like old-basis estimates (Europe alone, AMEA), and the four rows do not sum to the revenue estimate (e.g., FY27E rows sum to $4,994M vs revenue $4,918M; FY28E $5,426M vs $5,263M). Do not compare the regional estimates to the 2026 recast actuals without checking contributor definitions. Greater China consensus (FY26E $210.7M; 1H'26 actual $108M, so 2H'26E = $102.7M) is consistent with the company's FY26 China guide of $210M-$220M.

---

## 5. Customer end-market: clinical vs research & applied (R&A)

Illumina discloses end-market growth **only for sequencing consumables in the rest of world (ROW = ex-Greater China)**, as reported y/y growth, with ROW consumables and instruments in dollars. Sources: Q3'25 deck slide 7 (Q1'24-Q3'25), Q4'25 deck slide 9 (Q1'25-Q4'25 and FY25), Q1'26 deck slide 7 (adds Q1'26), Q2'26 deck slide 7 (adds Q2'26) (`deck/ILMN_2025Q3_...`, `..._2025Q4_...`, `..._2026Q1_...`, `..._2026Q2_...`). All growth rates are "reported" (actual), per the footnotes. [D].

### 5A. ROW sequencing consumables and end-market growth

| ROW (ex-Greater China) | Q1'24 | Q2'24 | Q3'24 | Q4'24 | Q1'25 | Q2'25 | Q3'25 | Q4'25 | Q1'26 | Q2'26 | FY24 | FY25 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ROW sequencing consumables ($M) [D] | 642 | 679 | 684 | 640 | 640 | 690 | 707 | 713 | 687 | 734 | 2,645 | 2,750 |
| ROW sequencing instruments ($M) [D] | 100 | 111 | 98 | 144 | 103 | 92 | 104 | 150 | 114 | 122 | 453 | 449 |
| ROW sequencing consumables y/y, total [D] | +1% | +2% | +9% | +2% | (0%) | +2% | +3% | +11% | +7% | +6% | +4% | +4% |
| **Clinical** consumables y/y, ROW [D] | +7% | +5% | +11% | +8% | +8% | +10% | +12% | +20% | +20% | +15% | +8% | +12% |
| **Research & Applied** consumables y/y, ROW [D] | (5%) | (3%) | +6% | (5%) | (11%) | (9%) | (8%) | (0%) | (12%) | (7%) | (2%) | (7%) |
| Total sequencing consumables incl. China ($M; 2024 Q1-Q2 and FY24 on Core basis: 697, 737, FY 2,872) | 697 | 737 | 741 | 698 | 696 | 740 | 747 | 756 | 726 | 775 | 2,872 | 2,939 |
| Implied Greater China sequencing consumables ($M) [Der] = total - ROW | 55 | 58 | 57 | 58 | 56 | 50 | 40 | 43 | 39 | 41 | 227 | 189 |

Note the FY24 and FY25 columns show the company's full-year growth (FY24: total +4%, clinical +8%, R&A -2%; FY25: +4%, +12%, -7%). ROW instruments for 2025 and 2026 quarters: Q1'25 $103M, Q2'25 $92M, Q3'25 $104M, Q4'25 $150M, Q1'26 $114M, Q2'26 $122M. In Q4'25 the deck lists total sequencing consumables $755M (my derived Q4'25 is 756 and the China figure above is therefore 42-43). The deck's 2024 ROW lines are Core basis, so the implied China figures for 2024 use Core totals (Q1'24 697, Q2'24 737, FY24 2,872 from the Q2'25 and Q4'25 decks); using consolidated totals (691, 729) would understate China by the $6M and $8M of GRAIL intercompany consumables. Implied China sequencing consumables fell from ~$55M-$58M a quarter in 2024 to ~$40M-$43M by Q3'25-Q2'26.

What it shows: clinical (about 65% of sequencing consumables revenue) accelerated from +8% in Q1'25 to +20% in Q4'25 and Q1'26 and +15% in Q2'26, while research & applied declined 7% to 12% in every quarter except Q4'25 (0%); R&A is guided to a mid- to high-single-digit decline for FY26 (Q2'26 call, unchanged), and clinical to mid-teens (raised "toward the high end of the prior guide" on Jul 30, 2026; initial FY26 guide was double digit to mid-teens, Q4'25 call). First-half 2026 clinical growth was ~17% (Q2'26 call). In Q2'26, R&A consumables rose 9% q/q (Q2'26 call), an early sign of stabilization that management says it has not put in guidance.

### 5B. Implied dollar split of ROW sequencing consumables [Der, approximate]

Illumina does not publish dollars by end market. The split can be backed out because the ROW total growth is a weighted average of clinical and R&A growth: prior-year clinical share s = (g_total - g_R&A) / (g_clinical - g_R&A). I applied this to each quarter using unrounded total growth from the dollar figures above and the rounded end-market growth rates. The "other" category (about 3% of consumables, mostly infectious disease, JPM Jan 2026 deck) is embedded in the two groups and cannot be separated. Rounding of the published growth rates (+/-0.5 pt) moves the clinical share by roughly +/-2 pts.

| ROW sequencing consumables | Q1'25 | Q2'25 | Q3'25 | Q4'25 | Q1'26 | Q2'26 |
|---|---|---|---|---|---|---|
| Total ROW consumables ($M) [D] | 640 | 690 | 707 | 713 | 687 | 734 |
| Implied prior-year clinical share | 56% | 56% | 57% | 57% | 60% | 61% |
| Implied clinical $M (current quarter) | ~390 | ~417 | ~435 | ~438 | ~464 | ~482 |
| Implied R&A $M (current quarter) | ~250 | ~273 | ~272 | ~275 | ~223 | ~252 |
| Implied clinical share (current quarter) | ~61% | ~60% | ~62% | ~61% | ~68% | ~66% |

Cross-checks: the JPM Jan 2026 deck states FY25 sequencing consumables were ~60% clinical and ~40% R&A (ex ~3% other); the Q1'26 call says clinical was "more than 65% of our sequencing consumables revenue in the quarter", and the Q2'26 call "approximately 65%". Those management shares are for total sequencing consumables (probably including China) while mine are ROW, so a gap of a point or two is expected; the derivation therefore reconciles. Within clinical (of sequencing consumables, JPM deck p.4): oncology testing ~51%, genetic disease ~25%, reproductive health ~21%, other ~3%.

### 5C. Organic growth and ROW organic growth

"Organic" (from Q1'26) removes currency and acquisitions; "ROW organic" also removes Greater China. Before 2026 there were no acquisitions, so organic = constant currency (CC). Sources: Q1'26 and Q2'26 decks, revenue growth reconciliation (Table 1, p.2); 2025 from the Q2'25, Q3'25 and Q4'25 decks (constant-currency tables) and the Q1'25 call.

| Total company | Q1'25 | Q2'25 | Q3'25 | Q4'25 | Q1'26 | Q2'26 | H1'26 |
|---|---|---|---|---|---|---|---|
| Reported y/y (company basis: Core in 2025) [D/Der] | -1.4% | -3.0% | +0.4% | +5.0% | +4.8% | +9.5% | +7.2% |
| Impact of acquisitions (SomaLogic), pts | n/a | n/a | n/a | n/a | 1.7 | 2.1 | 1.9 |
| Impact of currency on reported growth, pts (+ = tailwind) | -1.2 (Q1'25 call) | ~0 [Der] | +1.3 [Der: 14/1,077] | +1.5 [Der: 16/1,099] | +1.9 | +0.9 | +1.4 |
| **Organic (CC in 2025) y/y** | ~0% ("roughly flat", Q1'25 call; -0.3% [Der] from six-month CC less Q2) | -3% | 0% | +4% | **+1.2%** | **+6.5%** | +3.9% |
| Impact of China, pts | n/a | n/a | n/a | n/a | 2.3 | 1.6 | 1.9 |
| **ROW (ex-China) organic y/y** | "slightly up" (call) | n/d | +2% | +7% | **+3.5%** | **+8.1%** | +5.8% |

FY25 (company basis): reported 0% (Core: 4,343 vs 4,332), CC flat, ex-China CC +2% (Q4'25 deck). Total revenue growth guidance for FY26 on organic terms: initial (Feb 5) ILMN organic 1% to 3%, ROW organic 2% to 4%; Apr 30: unchanged 1% to 3% / 2% to 4% with revenue raised $20M; Jul 30: ILMN organic >4.0%, ROW organic >5.0%; Q3'26 guide: ~4.5% for both (Q4'25, Q1'26, Q2'26 decks, guidance tables). Organic growth by product: Q1'26 sequencing consumables +2% organic (+5% ROW), instruments +8% (+10% ROW), service +4% (+5% ROW), microarray -20% (ROW -20%); Q2'26 consumables +4% (+5% ROW), instruments +30% (+31% ROW), service +13% (+14% ROW), microarray -6% (ROW -4%). Cumulative H1'26: consumables +3% organic (+5% ROW), instruments +18% (+20%), service +9% (+10%), microarray -13% (ROW -12%).

What it shows: the reported 9.5% growth in Q2'26 breaks down as 6.5 pts organic, 2.1 pts from SomaLogic and 0.9 pts currency; excluding China's 1.6-pt drag, the core business grew 8.1%. In Q1'26, only 1.2% of the 4.8% reported growth was organic (acquisition 1.7 pts and currency 1.9 pts); the organic figure was held down by Greater China (-2.3 pts) and a 20% organic decline in legacy microarray (large direct-to-consumer customers, per the Q1'26 call).

### 5D. Gigabase (Gb) growth statements

Management states each quarter that "total sequencing Gb output on our connected high- and mid-throughput instruments" grew more than 30% y/y: Q4'24 (robust growth in both clinical and research), Q1'25 (robust from both), Q2'25 (clinical-driven, research muted), Q3'25 (clinical much stronger; research positive but below 30%), Q4'25, Q1'26 (clinical "well above" 30%) and Q2'26 (clinical "well above" 30%) (earnings-call transcripts, prepared remarks). China instruments are not connected, so Greater China is excluded. The pricing headwind that came with the transition to NovaSeq X is fading because ~90% of R&A volume is already on NovaSeq X (Q4'25 and Q1'26 calls). The JPM Jan 2026 deck (slide 12) frames clinical Gb growth with a ">30% CAGR" label and notes a human genome is >120 Gb versus ~8 Gb for an exome (~15x).

---

## 6. Platform: high-, mid- and low-throughput, NovaSeq X transition, installed base, placements, pull-through

Illumina does **not** disclose consumables revenue by throughput class. What it discloses: (i) NovaSeq X's share of high-throughput (HT) gigabases (Gb) shipped and of HT consumables revenue, (ii) NovaSeq X placements per quarter, (iii) active installed base and placements by instrument family once a year, and (iv) average annual consumables pull-through per instrument (actual and next-year guide). HT = NovaSeq X and NovaSeq 6000; mid-throughput (MT) = NextSeq family; low-throughput (LT) = MiSeq/MiSeq i100, MiniSeq/iSeq 100 (installed-base slide classification, Q4'25 deck slide 15).

### 6A. NovaSeq X as a share of the HT business (the "transition")

| | Q2'24 | Q3'24 | Q4'24 | Q1'25 | Q2'25 | Q3'25 | Q4'25 | Q1'26 | Q2'26 |
|---|---|---|---|---|---|---|---|---|---|
| X share of HT Gb shipped (total) [D, calls] | ~45% | >55% | >65% | ~68% | ~69% | ~78% | ~80% | ~82% | ~83% |
| X share of HT consumables revenue (total) [D, calls] | a little over 25% | >35% | ~40% | ~43% | ~44% | ~51% | ~55% | ~55% | ~59% |
| X share of R&A HT volume [D, calls] | n/d | n/d | n/d | >80% | >80% | ~91% | ~90% | ~90% | n/d |
| X share of clinical volume [D, calls] | n/d | n/d | n/d | >50% | ~55% | ~64% | >2/3 (chart ~71%) | ~76% | ~78% |

Sources (all `Sources/ILMN/earnings_call/`): Q2'24 call (~45% of HT Gb and "a little over 25%" of HT consumables revenue), Q3'24 call (>55%, >35%), Q4'24 call (>65%, ~40%), Q1'25 call (68%, 43%; R&A >80%, clinical >50%), Q2'25 call (69%, 44%; clinical ~55%), Q3'25 call (78%, 51%; 91% of research volumes, 64% of clinical), Q4'25 call (80%, 55%; R&A ~90%), Q1'26 call (82%, 55%; R&A 90%, clinical 76%), Q2'26 call (83%, 59%; clinical 78%). The decks show the same series as charts with 35% to 92% data labels (Q2'26 deck slide 8), but the text extraction does not attach labels to series, so I use the transcripts. Targets: "towards the end of 2025, ~75% of HT Gb shipped and ~50% of HT revenue on NovaSeq X" (Q2'25 deck); achieved in Q3'25 (Q3'25 deck slide 5). Management now expects clinical conversion to reach 80% to 85% of volume by end-2026 (Q1'26 and Q2'26 calls). **Inconsistency:** the Q4'25 deck says "we will phase out transition-specific metrics after Q4 earnings", yet the Q1'26 and Q2'26 decks still show the chart. The share of revenue plateaued at 55% from Q4'25 to Q1'26 and the CEO said it is "a little bit dangerous" to read it precisely (Q1'26 call).

What it shows: by volume the transition is essentially done (about 83% of HT Gb on X; ~90% in R&A), by revenue it is 59% because an X Gb sells at a lower price than a 6000 Gb. As the 6000 mix shrinks, the price-per-Gb headwind fades and Gb growth converts more fully to revenue growth.

### 6B. NovaSeq X placements per quarter

| | Q4'24 | Q1'25 | Q2'25 | Q3'25 | Q4'25 | FY25 | Q1'26 | Q2'26 |
|---|---|---|---|---|---|---|---|---|
| NovaSeq X placements [D] | >90 (91 per Q3'25 call) | >60 | >50 | >55 | >100 (~5 rental/lease) | ~270 (final deck; ~260 in JPM prelim) | >80 (~83 per CFO) | >95 |
| Share to clinical [D] | n/d | n/d | n/d | >50% | >60% | n/d | >60% | n/d |
| Company target | 50-60 per quarter | | | | | | FY26 "reasonably above" the 50-60/qtr range (200-240/yr) | Q2 ~ Q1 levels; 2H elevated, y/y growth moderating |

Sources: decks (Q2'25 slide 3 ">50", Q3'25 slide 3 ">55", Q4'25 slide 3 ">100", Q1'26 slide 4 ">80", Q2'26 slide 4 ">95", Q4'25 slide 15 FY25 ~270, JPM slide 5 ">95" and appendix ~260); calls (Q1'25: "over 60... following more than 90 in Q4 2024"; Q4'25: "over 100 NovaSeq X systems, about five of them on rental or lease", ">60% clinical"; Q1'26: "approximately 20 more than Q1 '25", CFO: "roughly 83 units", some under reagent-rental or lease; Q2'26: "more than 95", plus ">10 NovaSeq 6000 units"). Other placements, FY25 (Q4'25 deck): NovaSeq 6000 ~30, NextSeq 1k/2k ~390, NextSeq 500/550 ~110, MiSeq i100/MiSeq ~1,220, MiniSeq/iSeq ~90; MiSeq i100 alone had ">1,000 placements in 2025" (Q1'26 call) and ">500 since launch" at Q2'25 (Q2'25 deck slide 6). **Inconsistency:** the Q4'25 count was ">95" in the Jan 13 JPM deck and ">100" in the Feb 5 deck; FY25 ~260 became ~270; MiSeq-family installed base ~8,860 became ~8,590 (below).

### 6C. Active installed base, placements and pull-through by platform (FY25, final, as of 02/05/2026)

| | NovaSeq X | NovaSeq 6000 | NextSeq 1k/2k | NextSeq 500/550 | MiSeq i100 / MiSeq | MiniSeq / iSeq 100 |
|---|---|---|---|---|---|---|
| Class | HT | HT | MT | MT | LT | LT |
| First shipment | Q1'23 | Q1'17 | Q4'20 (2000) / Q1'20 (1000) | Q1'14 (500) / Q1'15 (550) | Q4'24 (i100) / Q3'11 (MiSeq) | Q1'16 (MiniSeq) / Q1'18 (iSeq) |
| FY25 placements [D] | ~270 | ~30 | ~390 | ~110 | ~1,220 | ~90 |
| FY25-end active installed base [D] | ~890 | ~1,360 (after ~330 decommissions) | ~2,990 | ~3,460 | ~8,590 | ~3,840 |
| *Preliminary (JPM, 01/13/2026): placements / base* | *~260 / ~890* | *~30 / ~1,360* | *~380 / ~2,990* | *~100 / ~3,460* | *~1,200 / ~8,860* | *~90 / ~3,840* |
| FY25 average pull-through, $K per instrument per year [D] | ~1,350 | ~670 | ~90 | ~100 | ~30 (MiSeq) | ~20 (MiniSeq) |
| **FY26 pull-through guide, $K** [D] | **1,350-1,400** | **600-650** | **80-100** | **90-110** (NextSeq 550) | not guided | not guided |
| Run-rate cross-check [Der] = FY25-end base x FY25 pull-through, $M | ~1,200 | ~910 | ~270 | ~350 | ~260 | ~80 |

Source: `deck/ILMN_2025Q4_Earnings_Slides.md` slide 15 ("FY25 Active Installed Base", as of 02/05/2026) and `deck/ILMN_2026-01-13_JPM_Healthcare_Conference_Slides.md` appendix (preliminary). Footnotes: high-throughput figures exclude HiSeq; active installed base excludes decommissioned instruments and includes reagent-rental units; pull-through is average annualized consumables revenue per instrument; "company doesn't guide low-throughput pull-through". Total active base ~21,000 (>12,000 LT, >6,000 MT, ~2,000 HT; HT capacity ~2x from 2022-2025; JPM slide 4). Implied NovaSeq X base at end-FY24 [Der] = ~890 - ~270 = ~620 (no X decommissions disclosed). Earlier reference: X pull-through averaged "$1.3 million per system" in 2024 (Q4'24 call) and was "above $1.3 million" at JPM Jan 2026 (Q1'26 call).

What it shows: the NovaSeq X is ~4% of units (890 of ~21,000) but, at ~$1.35M a year, about 40% of the sequencing-consumables run-rate by this cross-check; with the 6000 the two HT platforms account for ~69% of the run-rate. The cross-check sums to ~$3.06B, ~4% above the $2.94B of FY25 sequencing consumables, because using year-end instead of average installed base overstates it. Each X placed at $1.35M-$1.4M a year replaces or adds to a 6000 at $0.6M-$0.7M; management says new clinical customers take at least 6 to 9 months to reach normal pull-through (Q2'26 call) and clinical is more than 60% of placements and "much more additional incremental placement than necessarily conversion of the 6,000" (Q1'26 call). Management guided 2026 sequencing consumables growth ex-China at low-single-digit to mid-single-digit (Feb 5, Apr 30) and mid-single-digit (Jul 30); sequencing instruments ex-China at -LSD to flat (Feb 5), flat to +LSD (Apr 30), +LSD (Jul 30) (decks, guidance tables).

### 6D. Sequencing instruments revenue (context)

Sequencing instruments, $M: Q1'25 109, Q2'25 96, Q3'25 107, Q4'25 154, Q1'26 118, Q2'26 125 (10-Q/10-K, Table 1A). Q2'26 +30% organic (10-Q: shipments +29%, "driven by higher NovaSeq X and MiSeq i100 shipments"). On the Q1'26 call an analyst noted that sequencing instrument revenue of $118M was below the ~$125M-$130M the Street expected despite >80 placements; management pointed to volume discounts on orders of 5-10+ units and to reagent-rental or lease placements that are recognized differently (Q1'26 call, CEO and CFO).

---

## 7. New businesses: SomaLogic, multiomics, BioInsight, acquisition revenue in organic growth

### 7A. SomaLogic (closed January 30, 2026; acquired from Standard BioTools together with other specified assets)

Source: Q1'26 10-Q Note 2 and MD&A; Q2'26 10-Q Note 2; Q4'25 and Q2'25 decks; calls.

| Item | Value | Label / source |
|---|---|---|
| Purchase price | $460M = $382M cash + $81M contingent consideration - $3M settlement of preexisting relationship | [D] Q1'26 10-Q p.13 |
| Contingent consideration | Up to $75M milestones (up to $25M for 2025 performance, paid Apr 2026; up to $50M for 2026) + 2% royalty on SOMAmer-based NGS library-prep kits through Jan 2036. On Jul 27, 2026 Illumina paid $30M to buy out the remaining obligations; liability at Jun 28, 2026 was $37M | [D] Q2'26 10-Q Note 4 and Liquidity section |
| Allocation | Intangibles $186M (developed technology $158M/9 yrs, trade name $16M/7 yrs, customer relationships $12M/8 yrs); goodwill $171M (tax deductible); inventory $57M (of which $22M non-current); cash $19M | [D] Q1'26 10-Q p.13-14 |
| Revenue contribution to organic-growth bridge | Q1'26: acquisitions added 1.7 pts to total growth (= ~$17.7M [Der: 1.7% x $1,041M]) and 19 pts to microarray growth (= ~$17.9M [Der: 19% x $94M]). Q2'26: 2.1 pts total (= ~$22.2M [Der: 2.1% x $1,059M]) and 25 pts microarray (= ~$21.8M [Der: 25% x $87M]). H1'26: 1.9 pts total (~$40M [Der]) and 22 pts microarray | [D] Q1'26 and Q2'26 decks, Tables 1-3 |
| Pro forma cross-check | Q1'26 pro forma revenue $1,099M vs reported $1,091M: ~$8M of January pre-close revenue [Der]. 2025 pro forma vs reported: Q1'25 $1,060M vs $1,041M (+$19M), Q2'25 $1,076M vs $1,059M (+$17M), H1'25 $2,136M vs $2,100M (+$36M) [Der] | [D] 10-Q pro forma tables |
| Where it is reported | Mostly in the microarray lines (Q1'26 call, CFO: "from our report perspective, it's in microarrays -- mostly in the microarrays"). 10-Q lines show microarray service & other at $23M in both Q1'26 (vs $19M) and Q2'26 (vs $11M); microarray consumables $71M (vs $72M) and $77M (vs $71M). Because the deck's legacy microarray organic growth is -20% (Q1'26) and -6% (Q2'26), my inference is that SomaLogic revenue is spread across more than the service line (consumables-type kits as well as services); the line split is not disclosed. The 10-Q text says only that service & other rose "primarily due to revenue attributable to SomaLogic" | [D] / inconsistency |
| Management commentary | Q1'26: business "performing in line with our expectations on both revenue and profitability". Q2'26: SomaLogic revenue "continues to track towards the high end of our deal expectations" | [D] calls |
| Original guide | FY26: acquisition adds 1.5 to 2.0 pts to revenue growth (= ~$65M-$87M [Der on $4,343M]), ~100 bps operating-margin dilution, $0.18 EPS dilution; Q1'26 guide: 1.5 pts revenue, 100 bps margin, $0.04 EPS | [D] Q4'25 deck slide 14 |
| Profitability path | Profitable on a non-GAAP operating-income basis in 2027; margins in line with Illumina's in 2028; end markets "growing HSD+ to DD"; "high-margin consumables business as enabled on NGS" | [D] Q2'25 and Q4'25 decks |
| Gross-margin effects | Lower-margin revenue (10-Qs); $6M (Q1'26) and $2M (Q2'26) amortization of the inventory fair-value step-up in cost of revenue, added back in non-GAAP (decks); $7M transaction costs in Q1'26 SG&A | [D] |
| Sequential read-through | Q1'26 (Feb-Mar, two months) ~$17.7M vs Q2'26 (three months) ~$22.2M implies a sequential slowdown per month, but the "acquisition impact" is computed as a share of prior-year revenue and may net out prior Illumina-SomaLogic partnership revenue (the $3M preexisting-relationship settlement), so treat the dollars as approximate | [Der], flag |

What it shows: SomaLogic added about $18M to Q1'26 and $22M to Q2'26 revenue (1.7 and 2.1 points of growth) and roughly $40M in the first half; absent it, legacy microarray revenue fell about 17% to 20% in Q1'26 (large direct-to-consumer customers) and 6% in Q2'26. It is dilutive to margins in 2026 and is not expected to reach Illumina's margin until 2028.

### 7B. Multiomics, single-cell, spatial, BioInsight

No revenue is disclosed for single cell, spatial, proteomics (Illumina Protein Prep, launched Sep 2025) or the 5-base solution (launched Oct 2025). The Q2'26 call explains the reporting: "most of the multiomics products like single cell or TruPath... show up in our consumables revenue", whereas "the Billion Cell Atlas or any other related BioInsight revenue will show up in our services" (sequencing service & other). Q2'26: sequencing service & other grew 14% reported / +13% organic, with higher data revenue from biopharma customers on the Billion Cell Atlas (CFO); the Q2'26 10-Q also cites "increases in revenue from our development and licensing agreements and informatics solutions". Remaining performance obligations for development and licensing contracts were ~$38M at Mar 29, 2026 and ~$43M at Jun 28, 2026 (10-Qs). Timing of "strategic partnerships and data deals can be lumpy" (Q1'26 call). StrataMap spatial launched summer 2026 (Q2'26 call); ex-situ spatial was "available H1'26" (JPM). BioInsight was announced in October 2025, including a billion-cell atlas pharma partnership (JPM slide 5). [D] but unquantified.

### 7C. How acquisition revenue enters the organic calculation

Organic growth = reported growth less the impact of acquisitions less the impact of currency; ROW organic additionally removes Greater China (Q1'26 and Q2'26 decks, footnote a). SomaLogic revenue is excluded from organic growth in Q1'26 (1.7 pts) and Q2'26 (2.1 pts); the files do not say how long the exclusion will last. Illumina's 2026 organic guide therefore compares only the legacy business (see Table in 5C) while the revenue guide ($4.60B-$4.64B) includes SomaLogic. In the Q2'26 deck the Greater China "impact of acquisitions" is 6 pts (presumably SomaLogic's China sales), which is why Greater China reported -12% but organic -19%.

---

## 8. Segment, concentration, backlog, deferred revenue, inventory, purchase obligations, suppliers, manufacturing

### 8A. Core Illumina vs GRAIL in 2024 (segment note)

One reportable segment since the June 24, 2024 spin-off (Illumina kept 14.5% of GRAIL stock). The chief operating decision maker (the CEO) allocates resources on revenue and net income. Sources: segment notes and MD&A in the Q1'25 10-Q p.31, Q2'25 10-Q p.26 and 30-31, Q3'25 10-Q, FY25 10-K Note 12 and the Q2'25-Q4'25 decks.

| $M | Q1'24 | Q2'24 | Q3'24 | Q4'24 | FY24 |
|---|---|---|---|---|---|
| Core Illumina revenue (includes intercompany) | 1,056 | 1,092 | 1,080 | 1,104 | 4,332 |
| GRAIL revenue (service & other) | 27 | 29 | 0 | 0 | 55 |
| Eliminations | (7) | (9) | 0 | 0 | (15) |
| **Consolidated revenue** | 1,076 | 1,112 | 1,080 | 1,104 | 4,372 |
| Core gross profit | 693 | 743 | 745 | 728 [Der] | 2,909 |
| GRAIL gross profit (loss) | (22) | (16) | 0 | 0 | (38) |
| Eliminations | (4) | (6) | 0 | 0 | (10) |
| Consolidated gross profit | 667 | 721 | 745 | 728 | 2,861 |
| Core gross margin | 65.7% | 68.0% | 68.9% | 65.9% [Der] | 67.1% |
| Core income from operations | 116 [Der: 558 - 442] | 442 | 741 | 175 | 1,473 |
| GRAIL total operating expenses (incl. cost of revenue) | 253 [Der: 2,360 - 2,107] | 2,107 (incl. $1,886M impairment) | 0 | 0 | 2,360 |

Core and consolidated are identical from Q3'24. Note the Core Q2'24 intercompany revenue was $9M (YTD $15M). FY24 Core income from operations ($1,473M) is far above FY25 ($807M) mainly because FY24 included a $456M net legal-contingency gain (the reversal of the European Commission fine was $488M in Q3'24), while FY25 carried $10M of legal charges and no impairments. Q1'24 and Q2'24 consolidated gross profit is lowered by GRAIL's $22M and $16M gross losses and by amortization of GRAIL-related intangibles: consolidated amortization was $48M and $46M, of which about $31M-$34M a quarter related to GRAIL (Q2'24: Core $15M + GRAIL $31M of acquisition-related cost of revenue, Q2'25 deck).

### 8B. Customer concentration

"We had no customers that provided more than 10% of total consolidated revenue in 2025, 2024, and 2023." (FY25 10-K, Note on concentration of credit risk, line ~1558). No single distributor or customer is named. US revenue was $2,243M (51.6%) in FY25, $2,288M (52.3%) in FY24 and $2,359M (52.4%) in FY23. Accounts receivable (Bloomberg actuals): $699M (Q1'25), $701M, $729M, $854M (Q4'25), $738M, $764M (Q2'26); days sales outstanding ~60-67 [E file, actual columns].

### 8C. Remaining performance obligations (RPO), contract liabilities (deferred revenue and customer deposits), contract assets

| Date | RPO ($M) | % in next 12 months | % in following 12 months | Contract liabilities ($M), short-term in () | Contract assets ($M) | Revenue recognized from opening contract liabilities |
|---|---|---|---|---|---|---|
| Mar 31, 2024 | 796 | ~87% | ~9% | 324 (248) | 15 (Dec'23: 18) | $95M in Q1'24 |
| Jun 30, 2024 | 717 | ~82% | ~13% | 305 (238) | n/d | $70M Q2'24 (YTD $165M) |
| Sep 29, 2024 | 688 | ~82% | ~13% | 293 (235) | n/d | $48M Q3'24 (YTD $213M) |
| Dec 29, 2024 | 657 | ~78% (in 2025) | ~10% | 327 (260) | 16 | $245M in FY24 |
| Mar 30, 2025 | 891 | ~83% | ~7% | 329 (256) | 15 | $97M Q1'25 |
| Jun 29, 2025 | 862 | 79% | 10% | 324 (247) | 15 | $70M Q2'25 (YTD $166M) |
| Sep 28, 2025 | 747 | 77% | 11% | 307 (234) | 22 | $47M Q3'25 (YTD $214M) |
| Dec 28, 2025 | 738 | ~77% (in 2026) | ~13% | 346 (270) | 21 | $244M in FY25 |
| Mar 29, 2026 | ~1,100 (+ $38M development & licensing, separately) | ~85% | ~9% | 344 (269) | 23 | $98M Q1'26 |
| Jun 28, 2026 | ~1,000 (+ $43M development & licensing) | ~83% | ~11% | 333 (261) | 20 | $71M Q2'26 (YTD $169M) |

Sources: "Performance Obligations" and "Contract Assets and Liabilities" notes in each filing (Q1'24 10-Q p.14, Q2'24, Q3'24, Q1'25 p.13, Q2'25 p.14, Q3'25 p.14, FY24 10-K p.66, FY25 10-K p.68, Q1'26 10-Q p.16, Q2'26 10-Q p.17). Flags: (i) from Q1'26 the 10-Q splits RPO into a "primarily instruments, consumables and instrument service contracts" bucket, quoted in $ billions ("$1.1 billion", "$1.0 billion") and a separate development-and-licensing bucket, so the step from $738M to ~$1.1B may be partly a scope/presentation change (and SomaLogic backlog); management nonetheless said RPO was "up more than 20% year over year, across instruments and consumables" on the Q1'26 call ($1.1B vs $891M = +23% [Der]); Q2'26 ~$1.0B vs $862M = +16% [Der]. (ii) The last column is revenue recognized in the period that had been in contract liabilities at the prior year-end (full-year figures: $245M in FY24, $244M in FY25). (iii) RPO jumped from $657M (Dec'24) to $891M (Mar'25), then eased to $747M-$738M in 2H'25; the filings do not explain the Q1'25 step-up (the Q4'24 and Q1'25 calls cite >90 and >60 NovaSeq X placements).

### 8D. Inventory

| $M | Dec'24 | Mar'25 | Jun'25 | Sep'25 | Dec'25 | Mar'26 | Jun'26 |
|---|---|---|---|---|---|---|---|
| Gross inventory | 660 | 646 | 693 | 719 | 697 | 750 | 778 |
| Reserve | (113) | (109) | (118) | (129) | (133) | (119) | (123) |
| **Net inventory** | 547 | 537 | 575 | 590 | 564 | 631 (611 current + 20 non-current) | 655 (629 current + 26 non-current) |
| Reserve % of gross [Der] | 17.1% | 16.9% | 17.0% | 17.9% | 19.1% | 15.9% | 15.8% |
| Raw materials / WIP / finished goods | n/a | n/a | n/a | n/a | 254 / 398 / 45 | 268 / 427 / 55 | 295 / 426 / 57 |

Sources: inventory notes in the filings (FY24 10-K Note on balance-sheet details; Q1'25, Q2'25, Q3'25 10-Qs; FY25 10-K; Q1'26 and Q2'26 10-Qs). Net inventory in 2024: $587M (Dec'23), $584M (Mar'24), $561M (Jun'24), $574M (Sep'24). Non-current inventory is new in Q1'26: work in process from SomaLogic whose manufacturing process exceeds one year (new accounting policy). Net inventory rose $91M from Dec'25 to Jun'26, of which $57M was acquired with SomaLogic (the Q2'26 10-Q cash-flow text cites "an increase in inventory"; Core Notes 02 attributes the build to SomaLogic, NovaSeq X production and higher input costs, which I did not find in the 10-Q). The Q3'25 10-Q cited "an increase in inventory reserves" as a gross-margin headwind.

### 8E. Purchase obligations

Non-cancelable purchase obligations (licensing and supply arrangements): **$184M** at Dec 28, 2025, "more than half... due during 2026" (FY25 10-K, Note 5); **$212M** at Dec 29, 2024, "approximately half" due within twelve months (FY24 10-K). The 2026 10-Qs contain no update.

### 8F. Single-source suppliers

FY25 10-K Item 1 (Raw Materials, p.10): "Multiple commercial sources provide many of our components and supplies, but there are some raw materials and components that we obtain from single-source suppliers." Illumina says it could redesign products with alternative components or reagents or develop internal supply. Risk factor (10-K): sub-assemblies, components and materials "currently are available from a limited number of sources, and, in the case of some... from only a single source". **No supplier is named in the filings.** The only supplier-cost items named are memory chips (Q2'26 10-Q: "rising memory costs", "higher memory chip and freight costs") and Middle-East-related freight and fuel costs.

### 8G. Manufacturing sites and facilities (FY25 10-K, Item 2, p.12; risk factor)

"Our manufacturing facilities are located in San Diego and the San Francisco Bay Area in California; Madison, Wisconsin; Cambridge, United Kingdom; and Singapore."

| Location | Sq ft | Operation | Lease expiry |
|---|---|---|---|
| San Diego, CA | 860,000 | Office, lab, manufacturing, distribution | 2030-2031 |
| Singapore | 564,000 | Office, lab, manufacturing, distribution | 2027-2037 |
| Cambridge, UK | 181,000 | Office, lab, manufacturing | 2026-2038 |
| SF Bay Area, CA | 166,000 | Office, lab, manufacturing | 2028-2033 |
| Madison, WI | 133,000 | Office, lab, manufacturing | 2033 |
| Eindhoven, Netherlands | 90,000 | Office, distribution | 2036 |
| China | 86,000 | Office, lab | 2026-2028 |
| India | 66,000 | Office, lab | 2027-2029 |

Long-lived assets (PP&E + lease right-of-use) at Dec 28, 2025: US $660M, Singapore $281M, UK $119M, other $69M (total $1,129M). Singapore matters for tariffs and tax: it is the largest source of tariff cost ("importation from our manufacturing facility in Singapore"; estimated total tariff cost ~$85M as of Q1'25, 10-Q p.28) and its tax holidays and incentives lowered the provision by $37M in FY25 (+$0.24 to diluted EPS) and $33M in FY24, expiring from 2035. In February 2026 the US Supreme Court held IEEPA does not authorize the tariffs; refunds are being processed in phases, and recoveries to date "have been immaterial" (Q2'26 10-Q). China: Illumina was added to the unreliable entities list in Q1'25 and may not export sequencing instruments into China (Q1'25 10-Q); China instrument revenue was down 55% in Q4'25 (Q4'25 call).

---

## 9. Source-consistency flags and consensus-file quirks

1. **Q3'26 14 weeks (brief) vs Q4'26 14 weeks (transcript).** See top flag 3. Consensus Q3'26E carries period-end 10/04/2026.
2. **Bloomberg "actual" columns follow the deck rounding, not the 10-K minus 10-Q arithmetic**, for Q4'25 (sequencing consumables 755 vs my 756; microarray consumables 77 vs 76; sequencing service 157 vs 156; microarray service 12 vs 13) and Greater China (55 vs 56).
3. **Bloomberg "Core Illumina - Revenue Including Intersegment Revenue" row is broken for some actual columns**: Q3'25 shows 927 and Q4'25 shows 990 and Q1'26 shows 917 (these are *product* revenue), while Q1'25, Q2'25 and Q2'26 show total revenue. The FY25 annual cell shows 3,709 (product revenue) too. Ignore that row.
4. **Bloomberg "Adjusted" block mixes bases.** "Total Operating Expenses" (519, 481, 506, 557, 512, 525) are GAAP opex (e.g., Q1'25 GAAP 519), while the adjusted SG&A/R&D rows are non-GAAP; "Cost of Products Sold/Services Sold" actuals equal GAAP. Estimates (Q3'26E 281.99 / 80.65) are therefore probably also GAAP-like; adjusted cost of revenue (374.14) does not equal revenue minus adjusted gross profit (1,154.22 - 792.74 = 361.48).
5. **FY26E GAAP gross profit $2,740.01M** conflicts with the 67.49% GAAP gross margin on the same line; **FY26E amortization of $56.2M** is below the filing's own schedule; **FY26E FCF $997M** is less than 1H'26 actual plus Q3E and Q4E.
6. **Regional estimates** are on an unclear basis (Section 4C).
7. **Q4'24 consolidated vs Core non-GAAP EPS** ($0.86 vs $0.95) and tax rate (31.1% vs 23.7%) differ in the Q4'25 deck; Illumina's growth statement (+42%) uses $0.95.
8. **Q4'25 JPM preliminary vs final**: revenue $1,155M vs $1,159M, EPS $1.27-$1.30 vs $1.35, NovaSeq X FY25 shipments ~260 vs ~270, MiSeq-family base ~8,860 vs ~8,590.
9. **SomaLogic classification** (10-Q "service and other" narrative vs call/deck "microarrays") - Section 7.
10. **Transition-metric phase-out**: said to end after Q4'25 earnings (Q4'25 deck slide 10) but still shown in the Q1'26 and Q2'26 decks.
11. **Preexisting-relationship netting**: the SomaLogic $3M settlement and elimination of prior Illumina-SomaLogic partnership revenue may make the "acquisition impact" dollars smaller than SomaLogic's gross revenue.

---

## 10. Source index and gaps

**Filings** (`Sources/ILMN/filing/`): ILMN_10-Q_2024Q1, 2024Q2, 2024Q3, ILMN_10-K_FY2024, ILMN_10-Q_2025Q1, 2025Q2, 2025Q3, ILMN_10-K_FY2025, ILMN_10-Q_2026Q1, 2026Q2. **Decks** (`Sources/ILMN/deck/`): ILMN_2025Q2, 2025Q3, 2025Q4 earnings slides, ILMN_2026-01-13 JPM slides, ILMN_2026Q1, 2026Q2 earnings slides. **Consensus** (`Sources/ILMN/consensus/`): ILMN_Consensus_Quarterlies.md, ILMN_Consensus_Quarterlies_2.md (Q3'26E-Q4'28E), ILMN_Consensus_Annuals.md (FY26E-FY28E; used for annual estimates although not on the original list). **Calls** (`Sources/ILMN/earnings_call/`): 2024Q2-2026Q2 transcripts, used only for items the filings/decks do not give (X transition shares, placements, call-only management statements). **Cross-check**: `Core Notes/02_ILMN_Financial_History_and_Guidance.md` (agrees with the originals on the numbers I tested; its installed-base table shows the preliminary JPM figures, 8,860 MiSeq-family units, rather than the final 8,590).

**Gaps:** (1) Q3'25 and Q4'25 revenue on the new USCAN/EMEALA/APAC basis. (2) Dollar split of SomaLogic across microarray lines. (3) Revenue by throughput class and by clinical vs R&A in dollars (only growth rates and my derived split). (4) Q1'25 non-GAAP and CC detail is taken from the Q1'26 deck comparison column and the Q1'25 call (no Q1'25 deck was provided). (5) 2024 quarterly y/y growth (needs 2023 quarters; not requested). (6) Quarterly installed base (only FY25-end given). (7) FY26 guidance split by acquisition vs FX (not given after Feb 5).
