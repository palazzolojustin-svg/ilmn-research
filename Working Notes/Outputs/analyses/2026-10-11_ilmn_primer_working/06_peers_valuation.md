# ILMN primer working file 06: Valuation, peer multiples, competitive-landscape facts, and "what should ILMN trade at"

Prepared 2026-10-11. Prices are the 9 Oct 2026 close unless noted. Tags: **[W]** web (URL and date), **[E: source]** folder extract or source file, **[Der]** my calculation (math shown), **[D]** a data point supplied in the task brief (Bloomberg consensus of 10 Oct, ILMN price, shares, debt).

**Bottom line.** At $278.17 ILMN trades at 51.9x FY26E EPS, 45.5x FY27E and 39.7x FY28E, and at 33.0x / 28.7x / 26.4x EV/adjusted EBITDA. That is roughly 75-80% above the median forward P/E of the nine core tools peers (about 26x) and above every peer-based method in this file except one: applying the median EV/Sales of ILMN's diagnostics customers. A reverse DCF says the price needs free cash flow to compound at about 18% a year in FY29-35 (or revenue at about 16% a year with margins reaching 30%), against a consensus revenue CAGR of 6.7% for FY26-28 and a management target of "high single digit" growth in 2027. Nearly all of the stock's move since February is multiple expansion, not estimate revisions (Section 1c).

---

## 1. ILMN valuation now

### 1a. Inputs and enterprise value

The table sets out the capital structure I used. Net debt is the only judgment call, because the brief ($2.0B gross debt, $1.17B cash at Jun 2026) and the web data service (total debt $2.53B including leases) differ, and the $500M note that matured on 9 Sep 2026 is a timing issue. The difference moves EV by about 1.2%, so it does not change any conclusion.

| Item | Value | Tag |
|---|---|---|
| Price (9 Oct 2026 close) | $278.17 | [D]; confirmed [W: stockanalysis.com/stocks/ilmn/statistics/, 2026-10-11] |
| Shares | 151.0M | [D] |
| Market cap | $278.17 x 151.0M = **$42.0B** | [Der] |
| Gross debt / cash (base case) | $2.00B / $1.17B, so net debt **$0.83B** | [D] |
| **Enterprise value (base)** | $42.0B + $0.83B = **$42.8B** | [Der] |
| EV using data-service balance sheet (debt $2.53B incl. leases, net debt $1.36B) | $43.4B (the site shows $43.36B) | [W: stockanalysis.com ILMN statistics, 2026-10-11] |
| JPM DCF net debt, used in its Jun 2026 target | $328M | [E: JPM 2026-06-10, ILMN/research/20260615_JP_Morgan_ILMN_Illumina-_Inc.-_Up*] |

Flags: (1) Cash at Jun 2026 pre-dates the $500M repayment on 9 Sep 2026 and the $300M 2029 notes issued in Aug 2026 (single source, unverified). A Q3 balance sheet (reported around early Nov) will settle this. (2) JPM's $328M net debt looks stale or uses a different cash definition; do not mix it with the $0.83B above.

### 1b. ILMN multiples on Bloomberg consensus

This table converts the Bloomberg consensus (10 Oct 2026) into the standard multiples at $278.17. Read it as: investors pay about $9 of enterprise value for each $1 of FY26 sales and about 2.4 cents of free cash flow per dollar of equity.

| Metric | FY26E | FY27E | FY28E | Math [Der] |
|---|---|---|---|---|
| Revenue ($M) [D] | 4,625 | 4,918 | 5,263 | growth +6.3% FY27, +7.0% FY28 |
| Adj. EBITDA ($M) [D] | 1,299 | 1,490 | 1,623 | |
| Adj. EPS ($) [D] | 5.36 | 6.11 | 7.01 | |
| FCF ($M) [D] | 997 | 1,102 | 1,239 | |
| **EV / Sales** | **9.26x** | **8.71x** | **8.14x** | 42,834 / revenue |
| **EV / adj. EBITDA** | **33.0x** | **28.7x** | **26.4x** | 42,834 / EBITDA |
| **P/E (adj.)** | **51.9x** | **45.5x** | **39.7x** | 278.17 / EPS |
| **FCF yield (on equity)** | **2.37%** | **2.62%** | **2.95%** | FCF / $42,004M market cap |
| FCF yield on EV | 2.33% | 2.57% | 2.89% | FCF / $42,834M |
| NTM P/E (0.25 x FY26 + 0.75 x FY27 EPS = $5.92) | 47.0x | | | 278.17 / 5.92 |
| NTM EV/Sales (NTM revenue $4,845M) | 8.84x | | | 42,834 / 4,845 |

Cross-checks: the data service shows forward P/E 48.7x, EV/Sales 9.65x (trailing) and EV/EBITDA 37.5x (trailing) [W: stockanalysis.com ILMN statistics, 2026-10-11]. Its consensus is FY26 revenue $4.62B (+6.5%), EPS $5.36 (+10.7%), FY27 EPS $6.12 (+14.2%); 21 analysts: 7 Strong Buy, 4 Buy, 6 Hold, 2 Sell, 2 Strong Sell; average price target $233.55 (low $113, high $365), which is 16% below the price [W: stockanalysis.com/stocks/ilmn/forecast/, 2026-10-11]. My Bloomberg-based figures agree with these.

Two scale effects to note: FCF yield of 2.4% is roughly half the "leading ~4-5% FCF yield" JPM cited in June-July at $160-205 (JPM 2026-06-10 and 2026-07-31); the stock has moved far faster than cash flow. FY26 FCF is only 21.6% of revenue and 76.8% of adjusted EBITDA [Der: 997/4,625; 997/1,299].

### 1c. Growth-adjusted view (PEG)

PEG is the P/E divided by the annual EPS growth rate in percent; it asks how much you pay per point of growth. Consensus EPS CAGR (compound annual growth rate) FY26-28 is (7.01 / 5.36)^(1/2) - 1 = **14.4%** [Der]. Consensus revenue CAGR is 6.7%, EBITDA CAGR 11.8%, FCF CAGR 11.5% [Der].

| P/E basis | P/E | PEG (P/E / 14.4) |
|---|---|---|
| FY26E | 51.9x | **3.6x** |
| NTM | 47.0x | 3.3x |
| FY27E | 45.5x | 3.2x |
| Data-service PEG (its own growth definition) | | 4.51x [W: stockanalysis.com ILMN statistics, 2026-10-11] |

A PEG above 2 is usually read as expensive; the core tools peers sit near 2.7x on the same method (Section 2c), so ILMN carries a PEG premium of about 20-35% as well as a P/E premium.

### 1d. ILMN against its own history and the sell-side's multiples

This table lines up every valuation datapoint the folder's research notes give, with the date and the price at which it was struck. The point to take: sell-side frameworks in the folder used 15-28x multiples when the stock was $134-205, and the stock has since moved to multiples nobody in the folder underwrote.

| Source (date) | Datapoint | Price then | What it implies now | Tag |
|---|---|---|---|---|
| Ameriprise (2026-07-31) | 12-mo forward P/E 36.3-36.4x vs **5-yr average forward P/E 72.2x**; says the gap partly reflects GRAIL's 24 Jun 2024 divestiture and the return to "Core Illumina" EPS | $205.09 | Not a valid benchmark: GRAIL losses depressed EPS, which inflated historical P/Es. Do not cite 72.2x as "cheap versus history." Now 47x NTM. | [E: Ameriprise 20260731] |
| JPM (2026-06-10, reiterated 2026-07-31) | ILMN at a **4.1x EV/EBITDA premium to Core Tools** (19.7x at target vs Core Tools 15.6x on 2027E) vs historical premium of ~15x (2015-2024, 1-yr forward). FCF yield ~4-5% | $160 / $205 | The premium on JPM's basis is now far larger: ILMN FY27E EV/EBITDA is 28.7x [Der] vs Core Tools about 15.6x in June (JPM) = premium ~13x, close to the historical premium. Caveat: the 4.1x and the "~3x" appear inconsistent inside the JPM note, and the "historical ~15x" is ambiguous (turns or percent). Treat the "scarcity value" argument as largely consumed. | [E: JPM 20260615, 20260805] |
| JPM (2026-07-31) | DCF target **$230** (Dec-2027): WACC 9.8%, terminal growth 4.5%; adj. P/E 38.4x / 33.3x / 27.7x FY26-28E at $205 | $205.09 | Stock is 21% above the target | [E: JPM 20260805] |
| JPM (2026-06-10) | DCF $185: WACC 9.1%, g 4.5%, EV $28,962M, terminal value 86% of EV | $160 | Sensitivity table: $278 needs about WACC 8.1% with g 5.0%+ (Section 4) | [E: JPM 20260615] |
| Barclays (2026-07-31) | Underweight, PT $160 = **28x FY27E EPS $5.73**. "Cannot justify the 35x PE... top of Tools." EV/EBITDA 24.3x/21.8x/19.9x FY26-28 at $205 (Barclays' EBITDA definition) | $205.09 | At 28x consensus FY27 EPS $6.11 the value is $171 [Der: 28 x 6.11]. Now 45x. | [E: Barclays 20260806] |
| Freedom (2026-08-05) | Hold, PT $185. Blend 50% DCF + 50% relative (**8x NTM EV/Sales, 35x NTM P/E**; raised from 7x and 30x) | $203 | 8x NTM sales = EV $38.8B, equity $37.9B, $251/share; 35x NTM EPS $5.92 = $207 [Der]. Even the raised multiples give below $278. | [E: Freedom 20260805] |
| UBS (2026-02-05) | Neutral, PT $135 = **15x Dec-2027 EV/EBITDA** (up from 14x). EV/EBITDA 16.5x / 14.5x / 12.5x FY26-28E; P/E 26.4x FY26E, 23.3x FY27E at $133.61 | $133.61 | Stock is +108% since; FY26 EPS estimate only +5.7% (from UBS $5.07 to $5.36). Multiple went from 26.4x to 51.9x FY26 P/E. At 15x FY27 EBITDA of $1,490M: $142.5/share [Der]. | [E: UBS 20260211] |
| Seeking Alpha (2026-09-08) | Hold, DCF $188 at $218 price: WACC 9.74%, terminal g 3%, revenue CAGR 11.3% over 9 years (7.7% yrs 1-3, 16.5% yrs 4-6, 8.8% yrs 7-9). "Priced for low-double-digit CAGR and FCF margins approaching 30%" | $218.22 | At $278 the same author's framework would need more again | [E: SeekingAlpha 20260908] |

What happened to the stock: $133.61 (5 Feb) to $160 (9 Jun) to $205 (30 Jul) to $218 (early Sep) to $293.84 (6 Oct close, +7.6% that day) to $278.17 (9 Oct) [E: notes above; W: Aaii/Wealthawesome headline reporting the 6 Oct close of $293.84 on analyst PT raises and AI-data-demand narrative, search results 2026-10-11, https://wealthawesome.com/why-illumina-inc-stock-surged-yesterday-10062026 (not opened; headline only)]. Sell-side targets in the folder (JPM $230, Freedom $185, Barclays $160) pre-date the October move; the data service's current average target is $233.55 [W]. Several brokers may have raised targets in October; I could not see those notes.

---

## 2. Peer multiples

Method and limits. Prices, market caps, EVs, forward P/E and trailing EV/EBITDA are from stockanalysis.com statistics pages, "last updated 11 Oct 2026" with 9 Oct closing prices [W]. Revenue and EPS consensus (S&P Global) are from the matching /forecast/ pages; **FY27-28 consensus is behind a paywall on that site for most names**, so forward EV/Sales is computed on FY26 revenue only and growth is FY26 y/y unless stated. I could not reach MarketBeat or Yahoo for these. EV/EBITDA on that site is **trailing and on a GAAP-style EBITDA basis**, so it is not like-for-like with ILMN's adjusted consensus EBITDA, and for Waters trailing EV/Sales and EV/EBITDA are distorted by the Becton Dickinson biosciences combination (revenue +104% y/y in FY26 consensus). I therefore lean on forward P/E and forward EV/Sales for the valuation work, with EV/EBITDA as secondary. URL pattern for every row: https://stockanalysis.com/stocks/<ticker>/statistics/ and /forecast/, retrieved 2026-10-11 [W].

### 2a. Core tools and life-science peers

This table shows how the large tools companies are valued. The takeaway: the nine core names cluster at a forward P/E of 24-28x (median 26.2x) and 6-8x FY26 EV/Sales, with growth of 2-8% and EPS growth of 5-16%. ILMN's revenue growth (6.5%) is in line with them; its EPS growth is higher.

| Company | Price ($) | Mkt cap ($B) | EV ($B) | Fwd P/E | EV/EBITDA (trailing) | FY26E revenue ($B) / growth | EV / FY26E sales [Der] | EPS growth FY26 / FY27 | Consensus PT |
|---|---|---|---|---|---|---|---|---|---|
| Thermo Fisher (TMO) | 658.02 | 243.3 | 281.8 | 25.1x | 24.0x | 47.88 / +7.5% | 5.9x | +9.9% / +9.7% | $677 |
| Danaher (DHR) | 219.81 | 154.5 | 178.0 | 24.8x | 22.2x | 26.35 / +7.3% | 6.8x | +9.1% / +9.3% | $241 |
| Agilent (A) | 170.54 | 48.1 | 50.5 | 26.0x | 24.3x | 7.50 / +8.0% | 6.7x | +10.9% / n/a | $178.5 |
| Waters (WAT) | 433.77 | 42.6 | 47.6 | 27.9x | 32.8x (distorted by BD deal) | 6.47 / +104% (merger) | 7.4x | +11.1% / +13.4% | $458 |
| Mettler-Toledo (MTD) | 1,549.99 | 31.1 | 33.1 | 31.4x | 26.0x | 4.24 / +5.3% | 7.8x | +10.8% / +9.3% | $1,508 |
| Revvity (RVTY) | 154.18 | 17.2 | 19.5 | 27.3x | 22.3x | 2.85 / -0.1% | 6.9x | +5.8% / +10.0% | $141.5 |
| Bruker (BRKR) | 58.84 | 9.0 | 10.6 | 26.2x | 19.7x | 3.56 / +3.5% | 3.0x | +15.8% / +13.8% | $63.7 |
| Bio-Techne (TECH) | 72.46 | 11.4 | 11.4 | 35.9x | 34.1x | 1.22 (FY Jun-26) / ~0%; FY27 1.27 (+4.4%) | 9.3x | +4.5% / +14.7% | $70.5 |
| Qiagen (QGEN) | 45.38 | 9.4 | 10.2 | 18.2x | 14.0x | 2.14 / +2.2% | 4.8x | +2.3% / n/a | $47.8 |
| **Median of nine** | | | | **26.2x** | **24.0x** | | **6.8x** | | |
| Median of five large caps (TMO, DHR, A, WAT, MTD) | | | | 26.0x | 24.3x | | 6.8x | | |
| **ILMN (base EV $42.8B)** | 278.17 | 42.0 | 42.8 | **47.0x NTM** (51.9x FY26) | 37.5x trailing [W] / 33.0x FY26E adj. [Der] | 4.625 / +6.3-6.5% | **9.3x** | +10.7% / +14.0% | $233.55 |

Notes: medians are mine [Der]. Qiagen's 18x is the low outlier; Bio-Techne and Mettler the high ones. The data-service PEGs for the group are 2.2-3.0x for TMO, DHR, A, WAT, MTD, RVTY, QGEN (3.1x), and 5.8x for Bruker [W]. Barclays (6 Mar 2026) described the group as having "reset multiples to attractive levels" after the AI-disruption sell-off [E: SECTOR/research Barclays 20260312]; the group has since recovered. JPM's June reading of Core Tools at 15.6x 2027E EV/EBITDA [E] is far below the 24x trailing figure here; the gap comes from definitions (adjusted vs GAAP EBITDA, forward vs trailing) and from timing, and I could not reconcile them from the sources.

### 2b. Genomics and sequencing-adjacent peers

This table covers the other sequencing and genomics-tools names, including the folder-only data for Roche and MGI. The takeaway: ONT and PacBio trade at 6-7x sales while growing 0-20% and losing money; Roche, the only sequencing rival with a real balance sheet, trades at 17x earnings.

| Company | Price | Mkt cap | EV | Valuation (forward) | Growth / consensus | Source |
|---|---|---|---|---|---|---|
| 10x Genomics (TXG) | $80.65 | $10.51B | $10.03B | EV/FY26E sales **16.2x** (10.03 / 0.6206); no P/E (EPS $0.04) | FY26E revenue $620.6M (-3.5% vs 2025, which included a one-time patent settlement); PT $69.47 (-14% vs price), 19 analysts "Buy" | [W: stockanalysis.com TXG, 2026-10-11]. Context: JPM (16 Jul) was Neutral with PT $38 [E: JPM 20260721], so the stock is >2x JPM's target. |
| PacBio (PACB) | $2.33 | $724M | $1.20B (net debt $472M) | EV/FY26E sales **7.6x** (1,200 / 158.7); FY27E 6.6x (sum of quarters $182.7M) | FY26E revenue $158.7M (-0.8%); FY27E $182.7M (+15%); FY28E $235M (includes a lumpy $91M 1Q28 quarter in the consensus file, so treat as noisy). Adj. EPS FY26E -$0.52, FY27E -$0.42. PT $2.40 | [W: stockanalysis.com PACB]; [E: Sources/PACB/consensus/PACB_Consensus_Quarterly_2026Q3-2028Q4.md; Q1/Q2-26 actuals $37.2M, $39.0M]. Stock was **$1.30 on 5 Aug** (Barclays PT $1.25 at 4x EV/sales) [E: Barclays 20260812], so up ~79% since. |
| Oxford Nanopore (ONT.L) | 213.4p (9 Oct) | £2.08B | £1.94B (net cash £143M) | EV / consensus revenue: FY26E **7.2x**, FY27E **6.4x**, FY28E **5.4x** [Der: 1,940 / 268.4, 301.9, 356.9] | Bloomberg consensus (10 Oct) revenue FY26E £268.4M (+19.9% on £223.9M), FY27E £301.9M (+12.5%), FY28E £356.9M (+18.2%); adj. EBITDA FY26E -£36.9M, FY27E -£11.7M, FY28E +£19.2M; gross margin 64-65% | [W: stockanalysis.com/quote/lon/ONT/statistics/, 2026-10-10]; [E: Sources/ONT/consensus/ONT_Consensus_Annual.md]. Broker PTs in folder: JPM 220p (5.5x 2027E EV/Sales; ONT 4.5x at 182p vs ILMN "c. 7x" and PacBio "c. 5x"), DB 210p, Barclays 182p (5.8x 2026E) [E: ONT/research 20260831, 20260928, 20261002]. |
| Twist (TWST) | $159.78 | $10.02B | $9.96B | EV/FY26E sales **21.8x** (9.96 / 0.456); no P/E | FY26E (Sep FY) revenue $456M (+21.2%); EPS -$0.96; PT $150 (-6% vs price) | [W: stockanalysis.com TWST]. Barclays called TWST an AI-data "clear winner" [E: SECTOR 20260312]. |
| Roche (ROG) | CHF 357.80 | CHF 286.0B | CHF 313.6B | Fwd P/E **16.9x** [W]; on folder consensus EPS CHF 20.28 (FY26E) / 21.98 (FY27E): **17.6x / 16.3x** [Der]; EV / FY26E consensus EBITDA CHF 26.09B = **12.0x**; EV/Sales 5.0x | Group revenue FY26E CHF 62.78B, FY27E 65.87B (+4.9%); Diagnostics & Devices FY26E revenue CHF 14.04B (22% of group), EBITDA CHF 3.53B (25.3% margin), FY27E revenue 14.91B (+6.2%), EBITDA 3.89B. Broker PTs: UBS CHF 376 (Buy), Barclays CHF 430 (OW), JPM Neutral CHF 325 (Mar) | [W: stockanalysis.com/quote/swx/ROG/statistics/, 2026-10-11]; [E: Sources/ROCHE/consensus/ROCHE_Consensus_Annual.md (Bloomberg 10 Oct 2026); ROCHE/research UBS 20260919, Barclays 20261002, JPM 20260917] |
| MGI Tech (688114) | Rmb ~? (not retrievable; UBS market cap **Rmb31.2B / US$4.64B** as of ~24 Aug 2026) | Rmb31.2B | n/a | Market cap / FY26E consensus revenue Rmb3,262M = **9.6x** [Der]; UBS: 2026E EV/EBITDA **88x**, PT Rmb58 = 7.0x 2026E P/S | Consensus (Bloomberg 10 Oct): revenue Rmb2,780M (2025A) to 3,262M (2026E, +17%), 3,786M (2027E, +16%), 4,316M (2028E, +14%); adj. EPS -0.07 / +0.21 / +0.46; EBITDA Rmb464M / 586M / 742M; gross margin 56% | [E: Sources/MGI/consensus/MGI_Consensus_Annual.md; MGI/research UBS 20260829, 20260504]. **Stale price: the live quote page returned 404; refresh before use.** |

### 2c. Diagnostics customers (clinical NGS consumers of Illumina)

These are the large labs that drive Illumina's clinical consumables growth; the Core Notes name Natera, Guardant, Tempus, Caris, BillionToOne and Exact as the concentrated customer group. The table shows what the market pays for them. The takeaway: they grow 3-8x faster than ILMN (13-49% vs 6.5%) and trade at 4-20x sales, a median of 8.8x, which is almost exactly where ILMN sits (9.3x).

| Company | Price ($) | Mkt cap ($B) | EV ($B) | FY26E revenue ($B) / growth | EV / FY26E sales [Der] | EV/sales per point of growth [Der] | Earnings multiple | Consensus PT |
|---|---|---|---|---|---|---|---|---|
| Natera (NTRA) | 400.71 | 57.76 | 56.91 | 2.91 / +26.2% | 19.6x | 0.75 | EPS -$1.44 FY26E, -$0.20 FY27E: none | $383.7 (-4%) |
| Guardant (GH) | 167.47 | 22.47 | 23.12 | 1.36 / +38.2% | 17.0x | 0.44 | EPS -$1.47 FY26E: none | $200.4 |
| Tempus AI (TEM) | 70.93 | 12.80 | 13.43 | 1.60 / +25.4% | 8.4x | 0.33 | EPS -$0.26 FY26E: none | $72.7 |
| BillionToOne (BLLN) | 98.09 | 4.63 | 4.22 | 0.455 / +49.1%; FY27E 0.574 (+26.2%) | 9.3x | 0.19 | EPS $1.50 FY26E / $1.49 FY27E: **65x / 66x** [Der]; site shows fwd P/E 125.6x (inconsistent, likely different year) | $129 |
| Caris (CAI) | 29.70 | 8.39 | 8.05 | 1.03 / +26.8% | 7.8x | 0.29 | EPS $0.14 FY26E / $0.37 FY27E: **212x / 80x** [Der]; site fwd 110.6x; EV/EBITDA (trailing) 46x | $30.4 |
| GeneDx (WGS) | 67.33 | 2.01 | 2.04 | 0.482 / +12.7%; FY27E 0.599 (+24.3%) | 4.2x | 0.33 | EPS $0.13 / $1.20 FY27E: **56x FY27E** [Der]; site fwd 101.6x | $93.5 |
| **Median of six** | | | | | **8.8x** | **0.33** | | |
| **ILMN** | 278.17 | 42.0 | 42.8 | 4.625 / +6.5% | **9.3x** | **1.43** | 51.9x FY26E, 45.5x FY27E | $233.55 |

Source for all rows: https://stockanalysis.com/stocks/<ticker>/statistics/ and /forecast/, 2026-10-11 [W]. Exact Sciences is being acquired by Abbott (shareholder-approved per Barclays, Mar 2026) so it is omitted [E: SECTOR 20260312]. JPM's July DCF price targets for these names (NTRA $315, GH $185, BLLN $145, TXG $38; WACCs of 7.2-8.7% and terminal growth of 4.5-5.0%) are below or near current prices for most, so those targets are stale [E: JPM 20260721].

---

## 3. Competitive-landscape facts

Context from the Core Notes (09_Competitive_Landscape.md): no audited share figure exists; ILMN's share is variously "mid-60s%" to "80%+" in expert calls, with the experts' numbers generally unsourced [E: Core Notes 09]. The two tables below add what could be sourced.

### 3a. Market-share estimates

This table collects every share datapoint found. Takeaway: the only quantified third-party survey (DeciBio) is from 2023 and covers clinical oncology labs in the US and Europe, so it is stale; everything else is expert opinion.

| Source | Claim | Date | Reliability | Tag |
|---|---|---|---|---|
| DeciBio (consultancy) | Illumina ~80% of surveyed institutions' installed base; Thermo Fisher second, "especially ex-US"; Illumina expected to take only ~60% of new instruments among labs planning to expand within 12 months; novel platforms (ONT, Element, PacBio, Singular) ~20% of planned adoptions but <5% of instruments in use. 70 interviews, US and EU clinical oncology NGS labs | 15 May 2023 | Stale; narrow population (clinical oncology, in-house panels). DeciBio's current framing: Illumina cedes share but its growth trails the market by only ~2% a year | [W: https://decibio.com/insights/how-will-novel-ngs-platforms-impact-the-clinical-oncology-ngs-sequencer-market-over-the-next-year, accessed 2026-10-11] |
| Ex-Illumina AD citing DeciBio | ~80% down to mid-60s, losing ~3 points a year, should "flatline" near 50% | 24 Jul 2026 | Expert recollection | [E: Core Notes 09] |
| Ex-Illumina field scientist | 80% to 70%; at least 30% more to lose by 2029-30 | 24 Jul 2026 | Expert | [E: Core Notes 09] |
| MGI via UBS | ~70% of Chinese public tenders in 2025 | 2025 | Management claim | [E: Core Notes 09; MGI/research] |
| JPM customer survey (62 customers) | Academic customers expect ILMN share to rise 1-3 points; mid-sized clinical labs expect ILMN's share of their work to rise from 50% to 57% | Jun 2026 | Survey, customer-stated intent | [E: JPM 20260615] |

### 3b. Competitor sequencing revenue, platforms, price per genome, instrument list price

This table gives each platform's size, price and instrument cost on one page. Takeaway: ILMN's revenue (about $4.6B) is roughly 9x ONT's (about $0.36B) and PacBio's ($0.16B) combined [Der: 4,625 / (268.4 x ~1.34 + 158.7)], and roughly 50x Element's estimated ~$85M; the price war is at the $80-200 per 30x genome level, and cost per gigabase (Gb) is converging on $1-2.

Conversion: a 30x human genome is about 100 Gb [E: Core Notes 09], so $ per genome / 100 = $ per Gb [Der].

| Vendor | Sequencing-related revenue | Platform and instrument list price | Price per genome | Price per Gb [Der] | Source |
|---|---|---|---|---|---|
| **Illumina** | FY25 revenue $4.34B; FY26E consensus $4.625B (total company, includes ~$0.85B+ quarterly consumables run-rate; clinical >40% of revenue) | NovaSeq X Plus **$689K** list (UBS); other quotes $985K-1.2M (BI/experts), disputed; MiSeq i100 Plus >$100K; NovaSeq X pull-through guide $1.35-1.40M/yr | JPM ~$200; expert $150-250; UBS roadmap ~$150 with 35B flow cell | Blended high-throughput ~$2.50, heading to ~$2.00 on 35B flow cell (list 25B: $0.68/M reads) | [E: Core Notes 09; ILMN/research JPM 20260303, UBS 20260224] |
| **Roche AXELIOS 1** (SBX) | Pre-revenue; RUO launch 29 Jun 2026; target ">$1B" blockbuster, ~100 systems in year one (about one-third placed without "teaser offers", per CEO call 8 Sep) | ~**$750K** instrument; sensor reusable up to 20x | **$150**, no volume discounting; $0.06 per million reads; ~$25 per sample for 1.1Mb liquid-biopsy panel | ~$1.50 | [E: Core Notes 09; ROCHE/research JPM 20260917, Barclays 20261002]. Roche Dx division FY26E revenue CHF 14.0B [E: Roche consensus] |
| **Oxford Nanopore** | FY25 £223.9M (+24% cc); H1-26 £116.7M (+12.3%); FY26E consensus £268.4M; target >$700M by 2030, EBITDA breakeven 2027 | MinION $5K; PromethION is >50% of revenue | ~$345 (2 genomes per flow cell, early access); <$200 roadmap (4 per flow cell); expert: "at least double" Illumina | ~$3.45 now | [E: Core Notes 09; ONT consensus] |
| **PacBio** | FY25 ~$160.0M; FY26 guide cut to $155-165M; consensus $158.7M | Revio ~$482K average price; Vega benchtop $175K | $345 for 20x HiFi genome (SPRQ-Nx, down 30%); not comparable to a 30x short-read genome | n/a | [E: Core Notes 09; PACB consensus] |
| **MGI Tech** | FY25 total Rmb2.78B (-7.7%); sequencing -8%; H1-26 revenue Rmb1.37B (+18.9%); consensus FY26E Rmb3.26B. >1,470 sequencers shipped cumulative by 2025 end | Not disclosed in folder | Not in folder | "same data, lower cost" (expert) | [E: Core Notes 09; MGI consensus] |
| **Element Biosciences** (private) | **~$85M 2025 revenue estimate, up from ~$60M in 2024** (third-party aggregator; low confidence, company has not confirmed). An older release (2023) cited 112 installed instruments and >160 orders | AVITI ~$500K (1B reads per flow cell); VITARI ~$700K (UBS: ~40% below X Plus; 1/10 consumable cost per run; ~1/5 output per run; ships 2H26) | 50X genome "somewhere over $70" (expert); company claims $100 genome later in 2026 | ~$0.5-1.0 (if 50X is ~165 Gb, $70 is ~$0.42/Gb; expert-only) | [W: https://app.dealroom.co/news/note/element-biosciences-raises-upsized-175m-series-e-with-samsung-electronics-backing, 2026-10-11 (revenue estimate source: search summary, not opened)]; [E: Core Notes 09, UBS 2026-02-19] |
| **Ultima Genomics** (private) | Not disclosed; >15 customer sites; $600M raised in 2022 | UG 100 Solaris; instrument price not found | **$80** (UG100 Solaris); target $80-100 (JPM); $50 "somewhere" with new chemistry (expert recollection) | **$0.24 per million reads**; ~$0.8/Gb | [W: https://www.biopharmatrend.com/post/1149-100-billion-reads-per-day-ultima-genomics-expands-sequencing-capacity-and-cuts-costs-by-20, search summary 2026-10-11]; [E: Core Notes 09] |
| **Thermo Ion Torrent / Genexus** | Not broken out. Thermo's Genetic Sciences segment (which houses Ion Torrent plus much else) was **$2.87B in FY25** | Genexus; Oncomine Dx Express Test FDA-approved on Genexus Dx (2025) | n/a (small-panel workflow, not whole genome) | n/a | [W: Thermo FY25 10-K index and BusinessWire 14 Jul 2025 via search results, 2026-10-11]; expert (Abbott): Thermo holds "at least 10-15%" of installed base, unsourced [E: Core Notes 09] |

Funding for private rivals: **Element** raised a $277M Series D (Jul 2024) and an upsized Series E announced **9 Jun 2026** with **$175M from Samsung Electronics**, making Samsung the largest shareholder; other participants and total round size are undisclosed, and no valuation was disclosed [W: https://www.elementbiosciences.com/news/element-biosciences-announces-upsized-series-e-to-accelerate-global-growth-across-ecosystem-of-genomic-multiomic-and-clinical-research-solutions, retrieved 2026-10-11]. **Ultima** raised $600M in May 2022; no newer round found in my searches [W: https://www.biospace.com/article/ultima-genomics-announces-100-genome-after-600m-backing/, search summary].

---

## 4. What should ILMN trade at?

### 4a. Peer-relative framework

Each row applies one peer yardstick to ILMN's own consensus estimates and backs out a per-share value (equity = EV - $0.83B net debt; 151.0M shares). Takeaway: peer-based methods give **$155-$265** a share against $278.17, with the multiple-matched tools methods at **$155-$235** and only the diagnostics-customer EV/Sales method near the current price.

| Method | Yardstick | Applied to | Math [Der] | Implied value / share | vs $278.17 |
|---|---|---|---|---|---|
| Tools median forward P/E | 26.2x (nine-peer median) | NTM EPS $5.92 | 26.2 x 5.92 | **$155** | -44% |
| same | 26.2x | FY27E EPS $6.11 | 26.2 x 6.11 | $160 | -42% |
| Tools median EV/Sales | 6.76x FY26E | FY26E revenue $4,625M | (6.76 x 4,625 - 830) / 151 | **$201** | -28% |
| same, NTM | 6.76x | NTM revenue $4,845M | (6.76 x 4,845 - 830) / 151 | $211 | -24% |
| Tools median EV/EBITDA (trailing, GAAP-style) | 24.0x | FY26E adj. EBITDA $1,299M | (24 x 1,299 - 830) / 151 | $201 | -28% |
| same | 24.0x | FY27E adj. EBITDA $1,490M | (24 x 1,490 - 830) / 151 | $231 | -17% |
| **Growth-adjusted (PEG-matched)** | Peer median PEG 2.7x x ILMN EPS CAGR 14.4% = **38.8x P/E** | NTM EPS $5.92 | 38.8 x 5.92 | **$230** | -17% |
| same | 38.8x | FY27E EPS $6.11 | 38.8 x 6.11 | $237 | -15% |
| Diagnostics-customer median EV/Sales | 8.84x FY26E | FY26E revenue $4,625M | (8.84 x 4,625 - 830) / 151 | **$265** | -5% |
| Diagnostics-customer EV/Sales per point of growth (0.33x) | 0.33 x ILMN growth 6.5 = 2.2x | FY26E revenue | (2.2 x 4,625 - 830) / 151 | ~$60 (not meaningful) | Shown only to make the point that ILMN's growth is a fraction of its customers'; sales multiples are not comparable across such different margin structures |
| Sell-side frameworks | Freedom 8x NTM EV/Sales / 35x NTM P/E | | $251 / $207 | | |
| | Barclays 28x FY27 P/E; UBS 15x FY27 EBITDA; JPM 19.7x FY27 EV/EBITDA | | $171; $143; $189 (JPM's EBITDA basis may differ) | | |

How to read the PEG row: peers' PEG here is the forward P/E divided by the average of FY26 and FY27 consensus EPS growth (median 2.7x; the data-service PEGs give 2.2-3.0x for most names) [Der from Section 2a]. ILMN's higher EPS growth (14.4% vs about 10%) justifies a premium multiple, about 39x versus 26x, but the same arithmetic leaves the stock 15-20% above the PEG-matched value.

What would justify the premium to tools peers: ILMN's revenue growth (6.5%) is no better than the large tools names' (5-8%), so the case rests on (a) EPS growth of 14% a year from margin expansion (adj. operating margin 23.5% / 25.2% / 26.5% FY26-28E [D]), (b) clinical consumables growing mid-teens, (c) the 2027 "high-single-digit" revenue target (JPM; Seeking Alpha), and (d) scarcity of a clinical-sequencing monopoly with sticky switching costs (Core Notes 09). The bear points are Roche AXELIOS pricing at $150 a genome, reagent-rental discounting and concentration in 10-20 clinical customers (Core Notes 09). I did not pull peers' operating margins, so I cannot say whether ILMN's margin is above or below the group's.

### 4b. Reverse DCF: what does $278.17 imply?

This runs the cash-flow math backwards: given today's EV of **$42.83B** [Der: $42.0B + $0.83B], what free cash flow path must a buyer believe? Setup [Der]: FY27E and FY28E FCF are consensus ($1,102M, $1,239M [D]); FY29-35 FCF grows at a constant rate g; terminal growth after FY35 at 3-4%; mid-year discounting from end-2026; valuation date treated as end-2026 (the 0.2-year accretion to today is roughly offset by FY26 Q4 cash flow, so the error is under 2%). I solved for g such that PV of cash flows = $42.83B.

The table shows the implied FY29-35 FCF growth rate for each WACC (discount rate) and terminal growth pair, and the resulting FY26-35 FCF compound growth rate. The takeaway: across the full WACC 9-10% and terminal growth 3-4% range, the market needs **FCF growth of 15-21% a year in FY29-35**, about **14-19% a year for FY26-35**, with 70% of EV in the terminal value.

| WACC | Terminal g | Implied FCF growth FY29-35 | Implied FCF CAGR FY26-35 | FY35 FCF ($M) | Terminal value % of EV |
|---|---|---|---|---|---|
| 9.0% | 3.0% | 17.5% | 16.1% | 3,831 | 71% |
| 9.0% | 3.5% | 16.2% | 15.2% | 3,550 | 72% |
| 9.0% | 4.0% | 14.8% | 14.1% | 3,263 | 73% |
| **9.5%** | **3.5%** | **18.1%** | **16.6%** | **3,979** | **71%** |
| 9.5% | 3.0% | 19.3% | 17.5% | 4,266 | 70% |
| 9.5% | 4.0% | 16.9% | 15.6% | 3,686 | 72% |
| 10.0% | 3.0% | 21.1% | 18.9% | 4,723 | 69% |
| 10.0% | 3.5% | 20.0% | 18.0% | 4,430 | 70% |
| 10.0% | 4.0% | 18.8% | 17.1% | 4,131 | 71% |

Base case (WACC 9.5%, terminal g 3.5%): FCF path $1,102M (FY27), $1,239M, then $1,464M, $1,729M, $2,043M, $2,413M, $2,851M, $3,368M, $3,979M (FY35). That is 4.0x FY26E FCF of $997M in nine years. For context, consensus FCF CAGR for FY26-28 is 11.5%, so the market is asking for acceleration, not just continuation.

The second view builds revenue and margin explicitly, as asked. Assumptions [Der]: FY28 revenue $5,263M with adj. operating margin 26.5% [D], margin rising linearly to a terminal 30% by FY35 (consistent with JPM's DCF, which reaches a 30% EBIT margin in 2030 [E: JPM 20260615]); FCF = 88.8% of adjusted operating income (the FY28E consensus ratio: 1,239 / (0.265 x 5,263)); revenue grows at r in FY29-35.

| WACC | Terminal g | Implied revenue growth FY29-35 | FY35 revenue | Implied revenue CAGR FY26-35 |
|---|---|---|---|---|
| 9.0% | 3.0% / 3.5% / 4.0% | 15.4% / 14.2% / 12.8% | $14.4B / $13.3B / $12.2B | 13.4% / 12.5% / 11.4% |
| **9.5%** | 3.0% / **3.5%** / 4.0% | 17.2% / **16.1%** / 14.8% | $16.0B / **$14.9B** / $13.8B | 14.8% / **13.9%** / 12.9% |
| 10.0% | 3.0% / 3.5% / 4.0% | 18.9% / 17.8% / 16.7% | $17.7B / $16.6B / $15.5B | 16.1% / 15.3% / 14.4% |

At a 30% terminal operating margin and WACC 9.5% / g 3.5%, ILMN needs revenue of about **$14.9B in FY35**, i.e. **16% annual growth for seven years after FY28** (13.9% CAGR over FY26-35), versus a consensus 6.7% CAGR to FY28 and management's high-single-digit 2027 target. Lower terminal margin needs faster growth (28% terminal margin: 17.2%); a 33% terminal margin still needs 14.5%. For scale, ILMN revenue was $4.34B in FY25 (JPM), so FY35 of $14.9B is 3.4x in a decade for a business whose sequencing price per Gb is falling.

What the same model gives for plausible outcomes [Der]. This table shows value per share if revenue grows at a steady rate in FY29-35 with margin rising to 30% by FY35, terminal g 3.5%. Takeaway: even 10% growth for seven years yields about $184-222 a share, 20-34% below the market price.

| Revenue growth FY29-35 | WACC 9.0% | WACC 9.5% | WACC 10.0% |
|---|---|---|---|
| 6% | $178 | $162 | $149 |
| 8% | $199 | $181 | $166 |
| 10% | $222 | $202 | $184 |

Cross-check to JPM's published sensitivity (WACC and terminal growth, per share): JPM's base is $185 at WACC 9.1% and g 4.5%; the cell closest to $278 is WACC 8.1% with g 5.0% ($273) to 5.5% ($322) [E: JPM 20260615]. JPM's July roll-forward ($230 at WACC 9.8%, g 4.5%) shows how aggressive terminal growth of 4.5% carries the value. In other words, getting to $278 requires either revenue growth in the mid-teens through FY35 or a WACC near 8% with terminal growth of 5%, versus a long-run nominal GDP-like 3-4%.

Caveats on the reverse DCF: (1) FCF conversion is held at the consensus ratio; cash taxes, SBC (stock-based compensation) treatment and interest income are not modeled separately. (2) Consensus FCF of $997M for FY26 is about 77% of adjusted EBITDA; a lower conversion would raise the required growth. (3) Terminal values are 70% of EV, so the result is sensitive to WACC and g; the table above gives the range. (4) The model treats the buyback as value-neutral; no per-share share-count shrink is credited.

---

## 5. Source-conflict and staleness list

- Net debt: $0.83B (task brief) vs $1.36B (web data service, includes leases) vs $0.33B (JPM June DCF). EV varies $42.5-43.4B.
- Peer EV/EBITDA is trailing and GAAP-style on the web source; ILMN's is adjusted consensus. JPM's "Core Tools 15.6x 2027E" in June is not reconcilable with 24x trailing today.
- Ameriprise's 72.2x five-year average forward P/E is GRAIL-distorted (the note says so).
- Sell-side targets in the folder (JPM $230, Freedom $185, Barclays $160, UBS $135) pre-date the 6 Oct spike to $293.84; none reflects the October move. Stale.
- MGI price/market cap is the UBS late-August figure; the live quote could not be retrieved. PacBio and TXG have moved sharply since the August Barclays/JPM targets.
- Element 2025 revenue (~$85M) comes from a third-party aggregator in a search summary; it is unconfirmed. DeciBio's share data is from May 2023.
- FY27-28 consensus for most peers is paywalled on the web source, so only FY26 revenue growth and FY26-27 EPS growth were available for peers; ONT, PacBio, MGI and Roche FY27-28 figures come from the folder's Bloomberg files.
- Core Notes conflict on NovaSeq X list price ($689K to $1.2M) and on Roche's instrument cost ($750K to "$2 million" per one expert); carry the $689K and $750K figures with the caveat.
