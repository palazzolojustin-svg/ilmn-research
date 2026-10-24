# ILMN price timeline, January 2023 to 9 October 2026

*Working file 05 for the 2026-10-11 buy-side primer. Prepared 2026-10-11. Last price: $278.17 (Fri 9 Oct 2026 close). Web-sourced facts are tagged [W] with URLs in the source list at the end; everything else comes from the folder (Core Notes, Extracts, insider data).*

## 0. How to read this file, and data caveats

**Bottom line.** Illumina went from $233 (April 2023, as traded) to a closing low of $70.30 (8 April 2025), a fall of about 70%, and then to a record close of $293.69 (5 October 2026), a gain of about 318% off the low. About $92 of that rise came in the last 25 trading days (from $201 on 10 Sep to $294 on 5 Oct). The stock now trades at roughly 52x FY2026 consensus EPS of $5.36, against about 25x at the end of April 2026. Almost none of the 2026 move came from earnings estimates; it was a multiple re-rating.

**Price-series caveats.**

1. **Spin-off adjustment.** The daily series used here is Yahoo Finance daily closes pulled directly as JSON [W1]. Yahoo's pre-24-June-2024 closes are adjusted down for the GRAIL distribution by a factor of 0.9728 (1 GRAIL share per 6 ILMN, worth about 2.7% of the ILMN price at the time). I verified this against two folder sources: JPM's and UBS's rating-history tables show, for example, $143.33 for 8 Feb 2024, while the Yahoo close is $139.43 (ratio 1.028). Post-24-June-2024 closes match the folder tables exactly (for instance $104.38 on 28 Jun 2024, $121.10 on 7 Aug 2024, $153.49 on 4 Nov 2024, $133.61 on 5 Feb 2026, $205.09 on 30 Jul 2026). Percentage moves quoted in the tables are computed on the Yahoo (spin-adjusted, total-return-like) series, so they are correct for a holder who kept the GRAIL shares. **Dollar prices shown are "as traded"**: I multiplied pre-spin Yahoo closes by 1.02796, which reproduces the folder's broker tables to the cent.
2. **Window**: 3 Jan 2023 to 9 Oct 2026 (946 trading days). I could not get 2022 closes, so the 2023 start is 3 Jan.
3. **Cross-checks**: Barclays and Freedom list $126.74 as the 30 Apr 2026 close; the JPM 1Q26 recap says $120.37 on 30 Apr. Yahoo shows $126.74, so the JPM figure appears to be a stale price.
4. **Not verified**: the web is a patchwork of aggregator posts (MarketBeat, Quiver, Tiger, Mitrade, etc.) that frequently auto-generate "why the stock moved" text. Where a cause is attributed only by those, I tag it [W] and "correlated". Where I could find no cause at all, I say "unexplained" rather than invent one. Several dates (Roche SBX reveal, tariff pause, US-China truce, FOMC) come from my own recall and are marked as such.

## (a) Month-end closing prices

The table shows the last trading-day close of each month. "As traded" is the actual closing price; "Yahoo adj." is the spin-adjusted series (identical to as-traded from June 2024 on). Month-on-month change is on the adjusted series. The big picture: a 2023 slide from $214 to $102 (as traded, January to November), a $100-155 range in 2024, a plunge to the mid-$70s in early 2025, and an unbroken climb since October 2025.

| Month | Date | As traded | Yahoo adj. | MoM | What happened |
|---|---|---|---|---|---|
| 2023-01 | 2023-01-31 | $214.19 | $208.37 |  | Start of series. Illumina still carries GRAIL; FTC and EC fights ongoing. |
| 2023-02 | 2023-02-28 | $199.19 | $193.77 | -7.0% | Q4/FY22 print (7 Feb): 2023 EPS guide $1.25-1.50 below Street; -8.0% on 8 Feb. |
| 2023-03 | 2023-03-31 | $232.54 | $226.22 | +16.7% | The 13 Mar +17.0% day (cause not found in sources); 31 Mar FTC orders GRAIL divestiture. Pre-Apr peak $232.7 (13 Apr). |
| 2023-04 | 2023-04-28 | $205.55 | $199.96 | -11.6% | Q1 print 25 Apr (-3.5%); Icahn calls results "very disappointing" (28 Apr). |
| 2023-05 | 2023-05-31 | $196.64 | $191.29 | -4.3% | ISS backs Icahn (10 May, +7.8%); AGM 25 May: Icahn nominee elected, chair ousted (-9.0%). |
| 2023-06 | 2023-06-30 | $187.48 | $182.38 | -4.7% | deSouza resigns; Dadswell interim CEO. |
| 2023-07 | 2023-07-31 | $192.14 | $186.92 | +2.5% | EC fines Illumina EUR 432m (12 Jul). |
| 2023-08 | 2023-08-31 | $165.21 | $160.72 | -14.0% | 9 Aug: FY23 guide cut to roughly flat Core revenue; slide of -14% in month. |
| 2023-09 | 2023-09-29 | $137.27 | $133.54 | -16.9% | Thaysen named CEO (starts 25 Sep). Steady derating after the August guide cut. |
| 2023-10 | 2023-10-31 | $109.42 | $106.44 | -20.3% | Continued derating into Q3 print. |
| 2023-11 | 2023-11-30 | $101.95 | $99.17 | -6.8% | 9 Nov: second guide cut + $821m GRAIL impairment; -8.0% on 10 Nov. Closing low $90.26 adj (~$92.8 as traded) on 13 Nov. |
| 2023-12 | 2023-12-29 | $139.23 | $135.45 | +36.6% | Relief rally (1, 13, 19 Dec each ~+8%); Fifth Circuit vacates FTC order 15 Dec; GRAIL divestiture announced 17 Dec. |
| 2024-01 | 2024-01-31 | $143.00 | $139.11 | +2.7% | JPM conf (pre-announce, 9 Jan, +4.5%). |
| 2024-02 | 2024-02-29 | $139.82 | $136.02 | -2.2% | Q4/FY23 print 8 Feb: flat 2024 Core guide (-3.8%). |
| 2024-03 | 2024-03-28 | $137.31 | $133.58 | -1.8% | Quiet; XLEAP-SBS launch. |
| 2024-04 | 2024-04-30 | $123.05 | $119.70 | -10.4% | No single catalyst found; derating continued ahead of the Q1 print. |
| 2024-05 | 2024-05-31 | $104.28 | $101.44 | -15.3% | Q1 print 2 May (-4.9%), slide to $101.0 as-traded low (30 May) into GRAIL spin. |
| 2024-06 | 2024-06-28 | $104.38 | $104.38 | +2.9% | GRAIL spin-off 24 Jun (1 GRAIL per 6 ILMN, ~2.7% of ILMN price). 6 Jun +7.4% (cause not found). |
| 2024-07 | 2024-07-31 | $122.60 | $122.60 | +17.5% | 16 Jul +7.4%; no company catalyst found in sources (July 2024 small/mid-cap rally is a plausible but unverified factor). |
| 2024-08 | 2024-08-30 | $131.40 | $131.40 | +7.2% | Q2 print 6 Aug (+4.1%), $1.5bn buyback (1 Aug), strategy day 13 Aug (FY27 targets). |
| 2024-09 | 2024-09-30 | $130.41 | $130.41 | -0.8% | EC fine withdrawn 6 Sep ($481m gain). |
| 2024-10 | 2024-10-31 | $144.14 | $144.14 | +10.5% | 2 Oct +7.8% (cause not found); ahead of Q3. |
| 2024-11 | 2024-11-29 | $144.15 | $144.15 | +0.0% | Q3 print 4 Nov (+1.0%); 2024 high close $155 (7 Nov); fades on clinical-cliff debate. |
| 2024-12 | 2024-12-31 | $133.63 | $133.63 | -7.3% | Peak close $147.5 (9 Dec) post-spin; Evercore 3 Dec; slide into year-end. |
| 2025-01 | 2025-01-31 | $132.74 | $132.74 | -0.7% | JPM conf 13 Jan; -5.4% next day; stable ~$133. |
| 2025-02 | 2025-02-28 | $88.74 | $88.74 | -33.1% |  China UEL (4 Feb, -5.3%); Q4 print + weak FY25 guide (7 Feb, -9.6%); Barclays downgrade (10 Feb, -5.5%); Roche SBX / AGBT (20-27 Feb, two -5% days). |
| 2025-03 | 2025-03-31 | $79.34 | $79.34 | -10.6% | China bans instrument imports (4 Mar); NIH indirect-cost cap; tools de-rate. |
| 2025-04 | 2025-04-30 | $77.60 | $77.60 | -2.2% | Tariffs 2 Apr: -6.7% (3 Apr). Closing low $70.30 on 8 Apr, then +8.5% on tariff pause (9 Apr). |
| 2025-05 | 2025-05-30 | $82.24 | $82.24 | +6.0% | Q1 print 8 May: FY25 guide cut (-4.8%); US-China truce 12 May (+7.7%); CEO/CFO buy stock at ~$81. |
| 2025-06 | 2025-06-30 | $95.41 | $95.41 | +16.0% | SomaLogic deal (22-23 Jun); steady grind higher. |
| 2025-07 | 2025-07-31 | $102.71 | $102.71 | +7.7% | Q2 print 31 Jul; 22 Jul +7.6% (cause not found). |
| 2025-08 | 2025-08-29 | $99.96 | $99.96 | -2.7% | 1 Aug -7.8% the day after the Q2 print despite an EPS raise (SomaLogic dilution/tariff worries; broad-market weakness that day not verified). |
| 2025-09 | 2025-09-30 | $94.97 | $94.97 | -5.0% | Drift to $94.97; Protein Prep launch. |
| 2025-10 | 2025-10-31 | $123.54 | $123.54 | +30.1% | Q3 print 30 Oct, +24.8% on 31 Oct - return to growth ex-China. |
| 2025-11 | 2025-11-28 | $131.45 | $131.45 | +6.4% | China allows case-by-case exports (10 Nov); Wolfe conf. |
| 2025-12 | 2025-12-31 | $131.16 | $131.16 | -0.2% | JPM/Barclays PT raises (15 Dec); flat. |
| 2026-01 | 2026-01-30 | $144.81 | $144.81 | +10.4% | JPM conf pre-announce (13 Jan); TSO Comprehensive Medicare rate (20 Jan, +3.9%); SomaLogic closes 30 Jan. |
| 2026-02 | 2026-02-27 | $134.46 | $134.46 | -7.1% | "Claude crash" (3 Feb -4.0%); Q4 print + FY26 guide 5 Feb (-10.4% on 6 Feb); low $114.44 (12 Feb); AXELIOS priced 26 Feb (+4.5%, +5.5% next day). |
| 2026-03 | 2026-03-31 | $123.26 | $123.26 | -8.3% | After the late-Feb AXELIOS relief rally the stock gave back gains; TruPath launch / TD Cowen 3 Mar (-2.5%). |
| 2026-04 | 2026-04-30 | $126.74 | $126.74 | +2.8% | Q1 print 30 Apr. |
| 2026-05 | 2026-05-29 | $162.96 | $162.96 | +28.6% | Q1 beat-and-raise reaction +7.1% (1 May), then 27-29 May +11.9% in 3 days. |
| 2026-06 | 2026-06-30 | $175.83 | $175.83 | +7.9% | JPM upgrade to Overweight (10 Jun, $185); AXELIOS launch 29 Jun; 52w high close $175.8. |
| 2026-07 | 2026-07-31 | $205.10 | $205.10 | +16.6% | Q2 print 30 Jul (guide raised); 30 Jul +5.3%. |
| 2026-08 | 2026-08-31 | $213.63 | $213.63 | +4.2% | Directors sell; 19 Aug +8.9% (no company news found; ONT H1 results/cross-licence same day); UBS upgrade (27 Aug per StockAnalysis). |
| 2026-09 | 2026-09-30 | $273.68 | $273.68 | +28.1% | S&P 500 inclusion (announced 4 Sep, effective 21 Sep); UBS upgrade, PT raises; 15-17 Sep +17.5% in 3 days; 24 Sep +7.3%. |
| 2026-10 | 2026-10-09 | $278.17 | $278.17 | +1.6% | To 9 Oct only: 5 Oct +7.6% (RBC $310), 6 Oct -6.9% (intraday high $309.35), 9 Oct +5.1%. |

**Milestones, all on a closing basis.** 2023 high $232.66 (13 Apr 2023, as traded). 2023 low $92.79 (13 Nov 2023). 2024 range: low $101.05 (30 May 2024, as traded) to high $155.15 (7 Nov 2024). All-period low: $70.30 on 8 Apr 2025 (intraday $68.70 on 9 Apr). 52-week low close $91.00 on 14 Oct 2025 (intraday $88.00). Record close $293.69 (5 Oct 2026); record intraday $309.35 (6 Oct 2026). Year-to-date 2026: +112% (from $131.16 at the 2025 year-end to $278.17).

## (b) Big-moves timeline

### b1. Earnings-day reactions, every quarter Q4/22 to Q2/26

Illumina reports after the close, so the reaction is the next trading day. The table gives the pre-print close, the next-day close and the move. Of the 15 prints, nine were negative on the day after, five were positive and one was flat; three of the five positives were small (+4.1% or less). The two large positive reactions (Q3/25, +24.8%, and Q1/26, +7.1%) are the two prints that marked the shift from "guidance cut" to "beat and raise" and together account for most of the stock's recovery. The five big negatives (-8.0%, -8.0%, -9.6%, -7.8%, -10.4%) mostly involved guidance that the market read as weak or too cautious. Note that the Q4/25 print (-10.4%) was a negative reaction to a beat with conservative 2026 guidance, in a stock that had been rising into the print.

| Qtr | Print date (after close) | Close before | Close next day | Move | What surprised | Driver |
|---|---|---|---|---|---|---|
| Q4/22 | 2023-02-07 | $215.73 | $198.49 | -8.0% | 2023 guide: revenue +7-10%, EPS $1.25-1.50 (below Street); GRAIL overhang | guidance / EPS |
| Q1/23 | 2023-04-25 | $218.68 | $210.95 | -3.5% | 67 NovaSeq X shipments, X target >330, >$100M cost cuts; Icahn called it "very disappointing" [W cnbc] | placements / activism |
| Q2/23 | 2023-08-09 | $184.48 | $185.11 | +0.3% | FY23 guide cut to ~flat Core revenue (from +6-9%) despite 109 X shipments; muted day-after reaction, but the stock fell 14% in August | guidance (consumables) |
| Q3/23 | 2023-11-09 | $106.98 | $98.37 | -8.0% | Second guide cut, X shipments to 330-340, $821M GRAIL impairment | guidance / GRAIL |
| Q4/23 | 2024-02-08 | $143.32 | $137.83 | -3.8% | 2024 guide: flat Core revenue, ~20% op margin (partly pre-announced at JPM on 9 Jan) | guidance / margin |
| Q1/24 | 2024-05-02 | $123.99 | $117.93 | -4.9% | Surprise not extracted in this pass (see Core Notes 04); stock slid into the GRAIL spin | guidance (not extracted) |
| Q2/24 | 2024-08-06 | $116.36 | $121.10 | +4.1% | FY24 revenue guide cut to -2 to -3% but margin raised to 20.5-21% and first EPS guide $3.80-3.95 | margin / EPS |
| Q3/24 | 2024-11-04 | $153.49 | $154.96 | +1.0% | FY24 revenue ~-3%, EPS guide raised to $4.05-4.15; "clinical cliff" debate (stock +2.5% on the day of the print, +1.0% after) | EPS / consumables price vs volume |
| Q4/24 | 2025-02-06 | $122.80 | $111.06 | -9.6% | Revenue +1%, 91 X placements, soft FY25 outlook, after China UEL on 4 Feb | guidance / China |
| Q1/25 | 2025-05-08 | $79.58 | $75.76 | -4.8% | FY25 guide cut to $4.18-4.26B revenue, EPS $4.20-4.30; ~$85M tariff cost; stock had risen 4.2% on the day of the print | guidance / tariffs / NIH |
| Q2/25 | 2025-07-31 | $102.71 | $94.66 | -7.8% | Revenue $1,059M, EPS guide raised to $4.45-4.55, SomaLogic | EPS / M&A |
| Q3/25 | 2025-10-30 | $99.01 | $123.54 | +24.8% | Revenue $1,084M, EPS $1.34, growth ex-China +2%, EPS guide to $4.65-4.75 | return to growth |
| Q4/25 | 2026-02-05 | $133.61 | $119.72 | -10.4% | Revenue $1,159M, EPS $1.35; FY26 guide $4.50-4.60B / $5.05-5.20 | guidance |
| Q1/26 | 2026-04-30 | $126.74 | $135.78 | +7.1% | Revenue $1,091M (+1.2% organic), EPS $1.15; EPS guide to $5.15-5.30; clinical consumables +20% ex-China [W zacks]; X placements >80 | clinical / placements |
| Q2/26 | 2026-07-30 | $205.09 | $205.10 | +0.0% | Revenue $1,159M (+6.5% organic), EPS $1.31 vs $1.23 consensus, >95 X placements; guide to $4.60-4.64B / $5.30-5.40; stock +5.3% on the print day itself, flat next day, then -8.4% over the following 6 sessions (to 7 Aug) | clinical / placements |

### b2. Every single-day move of about 7% or more, plus smaller moves tied to key events

Thirty-five rows. The rule: any close-to-close move of at least 7%, plus selected moves of 4.5% to 7% where the date is a named event (China UEL, tariffs, Roche, AXELIOS, Meister selling, Oct 2026 reversal). "Confirmed (folder)" means the event date and its content are in the folder's sources. "Correlated [W]" means a web source attributes the move to this event but I could not independently confirm causality. "Unverified" or "unexplained" means I found no cause. About a quarter of the 7%+ days (13 Mar 2023, 13 Feb 2023, 6 Jun 2024, 16 Jul 2024, 2 Oct 2024, 1 Oct 2025, 19 Aug 2026) have no identifiable company-specific news; that is itself informative, because it suggests the stock trades on flows and sector beta at least as much as on events.

| Date | Move | Close before -> after (as traded) | Trigger | Driver it indexes on | Confidence |
|---|---|---|---|---|---|
| 2023-02-08 | -8.0% | $215.73 -> $198.49 | Q4/FY22 print (7 Feb after close): 2023 guide of +7-10% revenue and EPS $1.25-1.50, below Street. A BNN Bloomberg headline [W] says shares "plunge 16%" (likely intraday); the close-to-close move is -8.0%. | guidance / EPS | Confirmed (folder) |
| 2023-02-13 | +9.8% | $196.57 -> $215.93 | Rebound of +9.8%; no specific catalyst found in sources (UBS reiterated Neutral, $240 PT, same day). | unexplained | Unverified |
| 2023-03-13 | +17.0% | $194.00 -> $226.93 | +17.0% on 4.9M shares (about 2x normal volume). No catalyst found in the web or folder sources; occurred in the SVB-driven market turmoil. Treat as UNEXPLAINED, verify on a terminal. | unexplained | Unverified |
| 2023-05-10 | +7.8% | $194.25 -> $209.48 | Proxy adviser backs Icahn nominee ahead of AGM [W: timesofsandiego.com 10 May 2023]. Market read a governance shake-up as positive. | governance / activism | Correlated |
| 2023-05-25 | -9.0% | $212.64 -> $193.52 | AGM: Icahn nominee Andrew Teno elected, chair John Thompson ousted; CEO deSouza re-elected with only 71% [W: cnbc.com 25 May 2023]. Sell-the-news, -9.0%. | governance / GRAIL | Correlated |
| 2023-11-10 | -8.0% | $106.98 -> $98.37 | Q3/23 print (9 Nov): second guide cut, NovaSeq X shipments cut to 330-340, $821M GRAIL impairment, board special committee. PTs slashed same day (JPM $110, UBS $111). | guidance (consumables) / GRAIL | Confirmed (folder) |
| 2023-11-13 | -5.7% | $98.37 -> $92.79 | Follow-through -5.7% to the closing low ($92.79 as traded). Capitulation after the PT cuts; first class action over GRAIL filed 11 Nov. | guidance / GRAIL litigation | Correlated |
| 2023-12-01 | +7.7% | $101.95 -> $109.79 | +7.7%. Two days after new CEO Thaysen said at Piper (29 Nov) he would not do large M&A and put China at ~10% of sales; relief that capital would not be wasted again. | CEO / capital allocation | Inference |
| 2023-12-13 | +7.7% | $117.64 -> $126.67 | +7.7% on 13 Dec, the day of the FOMC meeting that signalled rate cuts (macro link is my inference, not in sources); two days later the Fifth Circuit vacated the FTC GRAIL order (15 Dec). | macro / GRAIL | Inference |
| 2023-12-19 | +8.1% | $129.09 -> $139.52 | +8.1%, two days after Illumina announced it would divest GRAIL (17 Dec). The end of the legal fight removed the biggest overhang. | GRAIL resolution | Correlated (folder timeline) |
| 2024-06-06 | +7.4% | $106.79 -> $114.72 | +7.4% on 7.4M shares (volume spike) in the run-up to the GRAIL spin; no catalyst found. Possibly spin-related positioning. | unexplained | Unverified |
| 2024-07-16 | +7.4% | $116.56 -> $125.23 | +7.4%; no company catalyst found. July 2024 was a broad small/mid-cap rally (not verified here). | unexplained / macro | Unverified |
| 2024-10-02 | +7.8% | $128.98 -> $139.02 | +7.8%; no company catalyst found in sources (a month before Q3). | unexplained | Unverified |
| 2025-02-04 | -5.3% | $131.10 -> $124.20 | -5.3%: China adds Illumina to the Unreliable Entities List (UEL). First leg of the 2025 collapse. | China | Confirmed (folder) |
| 2025-02-07 | -9.6% | $122.80 -> $111.06 | Q4/24 print (6 Feb): 91 NovaSeq X placements, revenue +1%, soft FY25 outlook; Barclays downgrades to Underweight ($100) on 10 Feb (-5.5%). | guidance / China | Confirmed (folder) |
| 2025-02-20 | -5.6% | $103.00 -> $97.20 | -5.6%: Roche unveils SBX sequencing chemistry (folder says Feb 2025 / AGBT; the 20 Feb date is my recall of the Roche release, not a folder date). First credible high-volume short-read rival. | competition / Roche | Correlated |
| 2025-04-03 | -6.7% | $81.88 -> $76.42 | -6.7%: day after "Liberation Day" tariffs (2 Apr); Illumina later sized tariff cost at ~$85M (Singapore-made products). | macro / tariffs | Correlated |
| 2025-04-09 | +8.5% | $70.30 -> $76.30 | +8.5% the day after the closing low of $70.30 (8 Apr): the 90-day US tariff pause (date from recall). Intraday low $68.70 on 9 Apr. | macro / tariffs | Inference on pause |
| 2025-04-10 | -6.6% | $76.30 -> $71.26 | -6.6% give-back the next day. | macro / tariffs | Correlated |
| 2025-05-12 | +7.7% | $75.76 -> $81.57 | +7.7% on the day CEO Thaysen (+$1.0M at $80.86) and CFO Dhingra (+$0.5M at $81.21) bought stock [OpenInsider, folder], and the US-China tariff truce was announced (12 May; from recall). | macro / insider buying | Correlated |
| 2025-07-22 | +7.6% | $94.80 -> $102.03 | +7.6% on 2.6M shares; same day Illumina settled a DOJ False Claims Act probe for $9.8M (folder). Weak link: removal of a legal tail. | legal / unexplained | Weak |
| 2025-08-01 | -7.8% | $102.71 -> $94.66 | Q2/25 print (31 Jul): revenue $1,059M, EPS guide raised to $4.45-4.55, SomaLogic deal discussed; yet -7.8% on 4.8M shares. Stock had run +7.7% in July. | guidance (revenue/tariffs) | Confirmed (folder); reason for sell-off unclear |
| 2025-10-01 | +7.7% | $94.97 -> $102.26 | +7.7%; no catalyst found. Sets up the Q3 beat. | unexplained | Unverified |
| 2025-10-31 | +24.8% | $99.01 -> $123.54 | Q3/25 print (30 Oct): revenue $1,084M, EPS $1.34, growth outside China returned (+2%), EPS guide raised to $4.65-4.75. Biggest one-day move in the series (+24.8%) and the true inflection of the stock. UBS PT to $120, JPM to $105. | guidance / return to growth | Confirmed (folder) |
| 2026-02-06 | -10.4% | $133.61 -> $119.72 | Q4/25 print (5 Feb): revenue $1,159M, EPS $1.35, FY26 guide $4.50-4.60B revenue and $5.05-5.20 EPS (1-3% organic growth ex-China, per TD Cowen chat). Read as conservative; JPM cuts PT to $120. | guidance / competition | Confirmed (folder) |
| 2026-02-26 | +4.5% | $121.87 -> $127.40 | +4.5% then +5.5% on 27 Feb (+10.3% in two days): Roche prices AXELIOS at $150/genome (26 Feb per folder timeline). UBS and JPM notes (3 Mar) call it "as expected"/benign; stock rallied on relief (inference). | competition / Roche | Inference |
| 2026-05-01 | +7.1% | $126.74 -> $135.78 | Q1/26 print (30 Apr): revenue $1,091M (+1.2% organic), EPS $1.15, FY26 EPS guide raised to $5.15-5.30, X placements >80. Freedom flash note that morning says the stock reaction "appears unjustified" (i.e. early weakness), yet the close was +7.1%. | guidance / placements | Confirmed (folder) |
| 2026-05-28 | +5.7% | $150.17 -> $158.70 | +5.7%, after +3.4% on 27 May (+11.9% over 27-29 May); no catalyst found. Director Meister sold 669,596 shares at ~$159.86 on 28 May. | unexplained / flows | Unverified |
| 2026-08-19 | +8.9% | $188.29 -> $205.00 | +8.9% on 2.1M shares (normal volume), the biggest unexplained move of 2026; then +4.0% and +2.9% (+13.4% over 18-21 Aug). No Illumina news found. Same day ONT reported H1 results and a $20M cross-licence with an unnamed "global diagnostics company" (folder); read-across is speculation. Director Meister sold 679,574 shares at $214.19 on 19 Aug into the move. | unexplained / flows | Unverified |
| 2026-09-15 | +6.8% | $208.21 -> $222.29 | +6.8%: UBS upgrades to Buy and raises PT to $260 from $135 (date per timothysykes.com; StockAnalysis dates a UBS Buy/$260 to 27 Aug), Argus PT $235, run-up to S&P 500 inclusion. Quiver Quant calls it "a sentiment-and-positioning move". | index / flows / sell-side | Correlated [W] |
| 2026-09-17 | +7.1% | $228.93 -> $245.18 | +7.1%, third straight up day (+17.5% over 15-17 Sep): analyst PT wave plus anticipatory index buying. | index / flows | Correlated [W: tradingkey] |
| 2026-09-24 | +7.3% | $255.38 -> $273.90 | +7.3% on 3.5M shares: House Ways & Means vote 43-0 to advance Medicare coverage for multi-cancer early detection tests (MCED) [W: globalbankingandfinance]; read-through to GRAIL (Illumina retains 14.5% of GRAIL, folder) and to clinical demand. Generally attributed to momentum. | policy / clinical / momentum | Correlated [W] |
| 2026-10-05 | +7.6% | $273.04 -> $293.69 | +7.6% to a record close of $293.69 on 4.2M shares: RBC raises PT to $310 from $230 (Outperform) citing a clinical inflection; follows Piper $305 (28 Sep), Leerink $300 (29 Sep), Guggenheim $305 (30 Sep). RSI ~77, overbought. | sell-side PTs / momentum | Correlated [W] |
| 2026-10-06 | -6.9% | $293.69 -> $273.54 | -6.9% reversal: intraday all-time high $309.35, close $273.54 (-11.6% from the high) on 4.4M shares. Attributed to profit-taking after the run; Meister selling and valuation (~52x P/E) cited by MarketBeat [W]. | profit-taking / valuation | Correlated [W] |
| 2026-10-09 | +5.1% | $264.57 -> $278.17 | +5.1% to $278.17 despite BofA raising PT only to $168 from $140 and staying Underperform; Barclays raised to $200 (UW) on 7 Oct (-2.1%). Dip bought. | flows | Unverified |

### b3. Multi-day phases and drawdowns

| Phase | Dates | Move | What drove it |
|---|---|---|---|
| 2023 collapse | 13 Apr 2023 to 13 Nov 2023 | $232.66 to $92.79 (-60%) | Icahn proxy fight and CEO exit (Apr-Jun), two guide cuts (9 Aug and 9 Nov), GRAIL legal overhang, NovaSeq X cannibalisation |
| Year-end 2023 relief | 13 Nov to 29 Dec 2023 | $92.79 to $139.24 (+50%) | New CEO, no big M&A, FTC order vacated and GRAIL divestiture announced, rate-cut pivot (inference) |
| 2024 base | 30 May 2024 to 7 Nov 2024 | $101.05 to $155.15 (+54%) | GRAIL spin (24 Jun), $1.5bn buyback (1 Aug), 13 Aug strategy day and FY27 targets, EPS guide raises |
| Collapse into the low | 9 Dec 2024 to 8 Apr 2025 | $147.53 to $70.30 (-52%) | China UEL (4 Feb), soft FY25 guide (6 Feb), Barclays downgrade (10 Feb), Roche SBX (Feb), China import ban (4 Mar), tariffs (2-10 Apr), NIH funding cuts |
| Recovery leg 1 | 8 Apr 2025 to 30 Oct 2025 | $70.30 to $99.01 (+41%) | Tariff pause, insider buying (12 May), SomaLogic (Jun), EPS raises |
| Inflection | 31 Oct 2025 | +24.8% in one day | Q3/25 return to growth |
| Plateau | Nov 2025 to Apr 2026 | $114-154 range | Q4/25 guide (-10.4%), Claude crash (3 Feb), AXELIOS pricing (26 Feb, +10.3% in 2 days), PT cuts |
| 2026 re-rating | 30 Apr to 5 Oct 2026 | $126.74 to $293.69 (+132%) | Q1 beat/raise, JPM upgrade (10 Jun), Q2 beat/raise (30 Jul), 19 Aug jump, S&P 500 inclusion and PT wave |
| Last 25 sessions | 10 Sep to 5 Oct 2026 | $201.27 to $293.69 (+46%) | UBS upgrade, index-inclusion front-running, Piper/Leerink/Guggenheim/RBC PT raises to $300-310 |

## (c) What the stock was trading on, phase by phase

**2023: the collapse (as traded, $214 in January to $102 in November, with a $233 peak in April).** Through 2023 the stock traded on two things: the GRAIL legal outcome and whether the NovaSeq X transition would cannibalise consumables sales (the recurring reagents that make up three-quarters of revenue). The year opened with a guide (EPS $1.25-1.50) below Street (8 Feb, -8.0%). It then lurched through Carl Icahn's proxy fight, in which proxy advisers backed his nominee (10 May, +7.8%), his nominee won and the chair was ousted at the AGM (25 May, -9.0%), and CEO Francis deSouza resigned in June. Two guidance cuts (9 Aug, to roughly flat Core revenue; 9 Nov, along with an $821M GRAIL impairment) pushed the stock to a closing low of $92.79 on 13 Nov. The driver label for 2023 is therefore "guidance and consumables growth, with GRAIL as the overhang." The sharp December rebound (+50% in six weeks) was a clearing event: new CEO Jacob Thaysen ruled out big acquisitions, a US court vacated the FTC GRAIL order (15 Dec), and Illumina announced the divestiture (17 Dec). Macro rates also helped, though the folder does not quantify that.

**2024: the base ($101-155 as traded).** After the GRAIL spin-off on 24 June (1 GRAIL share per 6 ILMN, worth about 2.7% of ILMN's price), the stock became a plain-vanilla sequencing company with a "do the arithmetic" story. It traded on EPS and margin delivery rather than revenue: the revenue guide went from flat to -2% to -3% to about -3%, but EPS guidance was introduced at $3.80-3.95 on 6 Aug and raised to $4.05-4.15 on 4 Nov, helped by a $1.5bn buyback (1 Aug) and the FY2027 targets set at the 13 Aug strategy day (high-single-digit growth, at least 500bp of margin expansion). The stock never held a break above $155; the late-2024 debate was the "clinical cliff" (big clinical customers moving to cheaper NovaSeq X runs, so volume +40% but consumables revenue only +5%, per the CFO at Wolfe on 20 Nov). The multiple was supported by buybacks but had no revenue-growth catalyst.

**2025: the low near $70 and the recovery.** The $147.53 peak (9 Dec 2024) turned into a 52% drawdown in four months, driven by a stack of external shocks rather than Illumina's own operating results: China's Unreliable Entities List (4 Feb, -5.3%), a weak FY25 guide (7 Feb, -9.6%), a Barclays downgrade (10 Feb), Roche's SBX reveal (the first credible high-volume rival, about 20 Feb, -5.6%), China's import ban (4 Mar), US tariffs (2-10 Apr), NIH cuts hitting academic spending, and the FY25 guide cut on 8 May. The closing low was $70.30 on 8 Apr 2025, not the "$80" often quoted; the ~$80 level was the 9 May closing area. The turn came with insider buying (CEO and CFO bought ~$1.5M at ~$81 on 12 May) and then steady EPS raises (31 Jul, 30 Oct). The decisive day was 31 Oct 2025 (+24.8%), when growth outside China turned positive (+2%) and the stock stopped being a "melting ice cube". The driver label shifts from "China and macro" in early 2025 to "return to growth / guidance" by October.

**2026: re-rating to ~$280.** January-April 2026 was a range ($114-154) with a hard "sell" on the Q4/25 guide (-10.4% on 6 Feb), the Claude-driven tools sell-off (3 Feb, -4.0%) and competitor noise (Element VITARI on 19 Feb had no visible effect; Roche AXELIOS pricing on 26 Feb produced a +10% two-day relief rally, which suggests the market feared worse). Q1 (30 Apr) was the beat-and-raise (+7.1%), and the stock then rose in a steady ramp: JPM upgraded to Overweight with a $185 target on 10 Jun (stock +1.5%, so mostly priced in), the Q2 print on 30 Jul (+5.3% on the day, flat after, then -8.4% by 7 Aug) lifted guidance to $4.60-4.64B revenue and $5.30-5.40 EPS, and an unexplained +8.9% day on 19 Aug (not on volume) started a second leg. September added a technical driver: S&P 500 inclusion (announced 4 Sep, effective 21 Sep) coincided with a UBS upgrade and a wave of target raises to $300+. Operating numbers improved (Q2 organic growth +6.5%, the best under Thaysen), but price rose roughly 119% from 30 Apr while FY26 consensus EPS rose only ~5%: this is a multiple expansion from about 25x to about 52x FY26 EPS, which means the stock is now priced for the FY27 targets (consensus FY27 EPS $6.11, so ~46x) and for clinical growth staying in the mid-teens.

## (d) Current market data and latest analyst actions (as of 9-11 Oct 2026)

**Market data** (from the Yahoo series and StockAnalysis/MarketBeat [W2][W3]).

| Item | Value | Note |
|---|---|---|
| Last close (9 Oct 2026) | $278.17 (+5.1% on the day) | 5 Oct close $293.69; 6 Oct close $273.54 |
| 52-week range, intraday | $88.00 to $309.35 | low 14 Oct 2025; high 6 Oct 2026 |
| 52-week range, close | $91.00 to $293.69 | |
| Shares outstanding | 151.0M (StockAnalysis); 151.3M (Freedom, Aug); 152.8M used in the Seeking Alpha piece | |
| Market cap | ~$42.0B | 278.17 x 151.0M; MarketBeat quotes $41.86B on 6 Oct at $276 |
| Volume | 60-day average ~2.8M shares; 20-day average ~4.6M (inflated by 32.6M on 18 Sep); 20-day average ex 18 Sep ~2.9M; MarketBeat quotes a 2.15M "average volume" | 18 Sep (32.6M shares, ~12x normal) was the index-inclusion closing trade |
| Valuation | ~52x FY26 consensus EPS $5.36; ~46x FY27 consensus EPS $6.11; StockAnalysis forward P/E 48.7; MarketBeat trailing P/E 51.7 | Consensus from Core Notes 03 (Bloomberg, 10 Oct) |
| Moving averages (6 Oct, MarketBeat) | 50-day $221.46; 200-day $177.17 | Price is ~25% above the 50-day |
| RSI (5 Oct, Mitrade) | 76.9, overbought | |
| Index | Added to S&P 500 effective 21 Sep 2026, replacing Builders FirstSource (BLDR), per S&P DJI [W4]; one web source (Webull) says Molson Coors, which is wrong per the S&P release | Moved from the S&P MidCap 400 |
| Consensus rating and target | MarketBeat: Hold, $222.19 average, range $113-$310, 10 Buy / 6 Hold / 2 Sell (18 analysts), stock 20% above target. StockAnalysis: Buy, $233.55 average (21 analysts), stock 16% above | Targets average 16-20% below the price. On 6 Oct MarketBeat quoted $219.69 |
| Next catalyst | Q3 2026 results Thursday 29 Oct 2026 [W5, StockAnalysis headline 8 Oct]; Q3 ended 4 Oct (14-week quarter). Company guide $1.14-1.16B revenue, $1.33-1.38 EPS; Bloomberg consensus $1,154M and $1.36 (Core Notes) | |

**Latest analyst actions (Sep-Oct 2026), with stated reasons where found.**

| Date | Firm | Action | Stated reason (as reported) |
|---|---|---|---|
| 9 Oct | BofA | PT $168 from $140, stays Underperform | Not found; still the most bearish target (consensus low $113) |
| 7 Oct | Barclays | PT $200 from $160, stays Underweight | Not found. Barclays' standing thesis: near-term growth issues, new competitors, extended valuation (earlier Barclays notes in folder) |
| 5 Oct | RBC Capital | PT $310 from $230, Outperform | Improving fundamentals, durable mid-teens clinical sequencing growth, higher 2026 guide, potential AI applications; "inflection in clinical sequencing demand" |
| 30 Sep | Guggenheim | PT $305 from $226, Buy | Not found |
| 29 Sep | Leerink Partners | PT $300 from $220, Outperform | Not found |
| 28 Sep | Piper Sandler | PT $305 from $225, Overweight | Not found |
| 15 Sep (StockAnalysis lists 27 Aug) | UBS | Neutral to Buy, PT $260 from $135 | Multi-year revenue acceleration and margin expansion. Dating conflict between sources; in the folder UBS was Neutral, $135 as of Feb 2026, so this is an upgrade, not an initiation |
| 15 Sep | Argus | PT $235 | A pipeline of new sequencing products nearing commercialisation |
| 8 Sep | Seeking Alpha (contributor) | Hold, $188 fair value | "Priced for perfection" (folder) |
| 1 Sep | Zacks Research | Strong-Buy to Hold | Quant rank change |
| 5 Aug | Freedom Broker | Downgrade to Hold, $185 | Stock ahead of its value-adjusted rating (folder) |
| 31 Jul | J.P. Morgan | Overweight, PT $230 from $220 | Q2 beat; clinical momentum (folder) |

Observations: (i) five firms raised targets above $300 within eight trading days of the 21 Sep inclusion, and the PT raises followed the price rather than led it (the stock was $273-294 when the $300+ targets were published, so these targets embed 3-12% upside only). (ii) The consensus target ($222-234) is still 16-20% below the price, which typically limits fresh sell-side buy calls from this level. (iii) Even the bears have been chasing: Barclays +25% and BofA +20% in a week or two while keeping negative ratings.

**Company news and conferences, Aug-Oct 2026.** I found no evidence that Illumina presented at the Wells Fargo (9-10 Sep), Morgan Stanley (14-16 Sep) or Baird (15 Sep) healthcare conferences; web searches turned up only peers on those agendas. The latest Illumina conference transcript in the folder remains TD Cowen on 3 Mar 2026 (a known gap in Core Notes). Company-specific news found: the S&P 500 inclusion (4 Sep announcement, 21 Sep effective); the Q3 results date set (29 Oct, announced 8 Oct); SpliceAI2 release for rare disease (8 Oct, "17% more disease-relevant variants"); and a Ways & Means 43-0 vote advancing Medicare coverage of multi-cancer detection tests (Sep, a read-through to GRAIL, in which Illumina holds a 14.5% stake). I found no ASHG 2026 announcement (the meeting is in October) and no press release on the 35B flow cell or its pricing; the folder says the 35B was put on the roadmap in March and an expert expects it around January 2027 at ~20% lower cost per gigabase. Roche's CEO said in September that about one-third of the ~100 first-year AXELIOS placements were made (folder, JPM note 15 Sep).

## (e) Buy-side positioning evidence

**Short interest: sources conflict.** MarketBeat shows 6.46% of float short, 1.63 days to cover, down 10.5% from the prior month, which it calls "improving" [W3]. A search-engine snippet attributed to Benzinga-type data gives 9.7% (4 Sep), 9.9% (18 Sep) and 10.8% (30 Sep), described as rising [W6; I could not open the page, so treat as low confidence]. The two series differ in definition and date, so do not splice them. Neither shows an extreme: even 10.8% on a 1.6-3 day cover is moderate. The honest read is that short covering is a possible, not a dominant, contributor to the September rally.

**Institutional flows.** MarketBeat: institutions own 89.4% and insiders 2.9% (6 Oct) [W3]. For Q2 2026 13F filings, an aggregator reports 917 firms with ~$27.0B of positions and 56 new positions [W7]. Quiver Quant (5 Oct) counts 443 investors adding versus 379 reducing; FMR (Fidelity) added 2.98M shares (+192% to ~$523M), while Sessa Capital and Southpoint cut significant positions [W8]. These are Q2 (30 Jun) positions, so they predate the 21 Sep index buy and the $201-294 September-October run; Q3 13Fs (due mid-Nov) will show who owned the run. Small-fund adds (Marshall Wace +49% to $5.7M, Swedbank +2,119% to $50M) are immaterial. I did not find hedge-fund-crowding rankings, a "crowded long" label or investor-survey data for ILMN; do not claim the name is crowded on this evidence.

**Passive flow.** S&P 500 inclusion required index funds to buy at the 18 Sep close: 32.6M shares traded that day, about 12x the 60-day average and about 22% of shares outstanding. The stock fell 2.3% on that day (a classic "sell the news" pattern) but rallied 23% in the following 11 sessions (to 5 Oct), so index buying was not the end of the move. Typical S&P 500 additions also see a pre-announcement run; here the announcement was met with a -3.3% reaction on 8 Sep and a trough on 10 Sep ($201.27), then a sharp rally.

**Insiders (folder, OpenInsider [OI]).** Director Keith Meister sold about 3.06M shares for about $591M between May and September 2026, with no purchases: 329k (13 May, $145), 670k (28 May, $160), 741k (4 Aug, $200), 680k (19 Aug, $214), 376k (25 Aug, $227), 264k (2 Sep, $217) (MarketBeat also lists 119,501 shares on 4 Sep at $218.40). That is roughly $437M in the last 90 days and a 25-32% cut of his holding per trade; he retains about 777k shares. The CEO and CFO were buyers at ~$81 in May 2025, and director Gottlieb bought small amounts at $117-122 in Nov 2025 and Feb 2026; other executives were small sellers in 2026 (about $0.5M each). MarketBeat counts "0 purchases and 108 sales over six months." The contrast between executive buying at the low and a director selling $591M into strength is the clearest sentiment signal in the data; Meister's sales cluster on up-days (19 Aug +8.9%, 28 May +5.7%), so supply was available into the rallies.

**Stretch indicators.** The stock closed 5 Oct at a 25%+ premium to the 50-day average, RSI 77, 20-day volume 60% above the 60-day average (ex-index day it is roughly flat), a 6 Oct key reversal from $309.35 to $273.54, and a "Hold" consensus with a mean target 16-20% below the price. These are consistent with a crowded, momentum-driven tape but not conclusive evidence of crowding.

## Gaps and items to verify on a terminal

- Unexplained 7%+ days: 13 Feb 2023, 13 Mar 2023 (+17%), 6 Jun 2024, 16 Jul 2024, 2 Oct 2024, 22 Jul 2025, 1 Oct 2025, 28 May 2026, 19 Aug 2026.
- Whether the Feb 2023 drop was -16% intraday (BNN headline) versus -8.0% close.
- Date and nature of UBS's upgrade (27 Aug versus 15 Sep).
- Q1/24 print surprise (not extracted; Core Notes 04 has it).
- Which Wells/MS/Baird September conferences, if any, Illumina attended (not on the websites found).
- Q3 2026 13F data, mid-November.
- SomaLogic announcement date: folder timeline says 22 Jun 2025 (shares +0.1% on 23 Jun), but the task brief says July 2025.

## Sources

Folder: Core Notes/00_Start_Here.md (master timeline); Extracts/ILMN/research (JPM 20260303, UBS 20260303, Freedom 20260501/20260805, JPM 20260731/0805, Barclays 20260507/20260806, Seeking Alpha 20260908); Extracts/ILMN/insider_data (OpenInsider summary; Meister Form 4 files); Core Notes 03 consensus.

Web [W]:
- [W1] Yahoo Finance daily chart JSON: https://query1.finance.yahoo.com/v8/finance/chart/ILMN (period 2023-01-01 to 2026-10-10, interval 1d and 1mo)
- [W2] https://stockanalysis.com/stocks/ilmn/ and https://stockanalysis.com/stocks/ilmn/history/ (last close, shares, market cap, news list)
- [W3] https://www.marketbeat.com/stocks/NASDAQ/ILMN/target/ and https://www.marketbeat.com/instant-alerts/price-illumina-nasdaq-ilmn-shares-down-6-time-to-sell-2026-10-06/
- [W4] S&P DJI announcement mirror: https://www.placera.se/pressmeddelanden/arista-networks-bloom-energy-illumina-and-everpure-set-to-join-s-p-500-others-to-join-s-p-100-s-p-midcap-400-and-s-p-smallcap-600-20260905 ; also https://www.webull.com/news/15548919494258688
- [W5] StockAnalysis news headline: "Illumina to Announce Third Quarter 2026 Financial Results on Thursday, October 29, 2026" (8 Oct 2026)
- [W6] https://www.benzinga.com/quote/ILMN/sentiment (search snippet only; page returned 403)
- [W7] https://www.insiderset.com/stocks/ilmn/institutional-ownership (search snippet)
- [W8] https://www.quiverquant.com/news/Illumina+rises+as+recent+analyst+target+hikes+and+index+inclusion+keep+momentum+intact ; https://www.quiverquant.com/news/Why+Illumina+(ILMN)+Stock+Is+Up+Today
- https://www.mitrade.com/insights/news/live-news/article-0-2138808-20261006 (5 Oct move, RSI)
- https://www.tradingkey.com/news/market-movers/262173925-market-movers-ilmn-20260917 (17 Sep)
- https://www.timothysykes.com/news/illumina-inc-ilmn-news-2026_09_15/ (15 Sep, UBS, Argus, Meister)
- https://www.globalbankingandfinance.com/illumina-shares-rise-7-25-on-thursday-to-close-at-usd-273-90-ilmn-20260924/ (24 Sep, MCED vote)
- https://finviz.com/news/281375/illumina-gets-medicare-boost-for-cancer-test-shares-climb (20 Jan 2026 TSO Comprehensive Medicare rate $2,989.55)
- https://www.cnbc.com/2023/05/25/illumina-installs-carl-icahn-board-nominee-ousts-chair-.html ; https://timesofsandiego.com/business/2023/05/10/proxy-advisor-backs-icahn-in-illumina-fight-despite-corporate-raiders-new-legal-problems/ ; https://www.bnnbloomberg.ca/illumina-plunges-16-on-weaker-than-expected-2023-profit-outlook-1.1867879 (headline only)
