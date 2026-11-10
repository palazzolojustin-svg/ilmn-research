# How the sell side models Illumina, and whether anyone models volume (2026-11-01)

*Sources: every broker note in `Sources/ILMN/research/` and the Bloomberg consensus files in `Sources/ILMN/consensus/` (stamped 10 Oct 2026), plus our own reconciliation work (primer working file 03, Core Notes 08, and the broker-assumption, 27E-variance, clinical-bridge and reverse-DCF notes). Two agent sweeps compiled this; the key lines were re-checked. **No broker note after Q3'26 (29 Oct) is in the folder.** The newest broker notes are 31 Jul to 6 Aug 2026.*

## Short answer

The Street models Illumina **top-down, in dollars**. It forecasts revenue by product line (sequencing consumables, instruments, service) and sometimes by end market (clinical vs research, China vs rest of world). Each line is driven by a growth rate, and management's disclosed ratios are used as cross-checks.

**No broker breaks out sequencing volume as a forecast line.** There is no Gb row, no NovaSeq X vs 6000 Gb split, no price-per-Gb row, no 6000 revenue line and no 35B flow cell anywhere. Price erosion shows up only in prose and, for Barclays, in a falling gross margin. A volume × price-per-Gb bridge would therefore be new relative to the Street.

## Does anyone break out volume?

| Broker | Volume or price/Gb row? | What it does forecast | Closest proxy |
|---|---|---|---|
| **JPM** (Overweight, $230 PT, 31 Jul) | No | End-market growth rates (text) plus a total P&L | It cites Gb only as the company's disclosed metric, "≥+30% using sequencing output in Gb" (10 Jun note, L165) |
| **Barclays** (Underweight, $160 PT, 6 Aug) | No | Total P&L only | It reads management's X share of Gb vs X share of revenue as a sign of discounting (7 May note, L218). That is a diagnostic, not a forecast |
| **UBS** (Neutral, $135, last note 4 Mar, stale) | No | One revenue line | $/genome and $/million-read comparisons with Roche (3 Mar) |
| **Freedom** (Hold, $185, 5 Aug) | No | Consumables / Instruments / Service (the most granular) | "Installed base" and "utilization" in prose |
| **Ameriprise** (Buy, no PT) | No (uses FactSet consensus) | n/a | Repeats the company's X Gb and revenue shares |
| **Bloomberg consensus** | No | Sequencing and microarray consumables, instruments, service, region | None |

## How the models are built

**JPM.** JPM has the most structure (10 Jun note, L188). Its model is a set of end-market growth rates for 2026–30E:
- ROW clinical sequencing consumables: "low/mid-teens" CAGR.
- ROW research: mid-single-digit.
- China: no recovery (down mid-teens).
- Total sequencing consumables: low-double-digit CAGR.
- Instruments: mid-to-high single digit.

Estimates:
- Revenue: 2026E $4,627M, 2027E $5,047M (+9.1%), 2028E $5,652M (+12.0%).
- EPS: $5.34, $6.16, $7.41.

JPM values the stock on a DCF. Its PT went from $120 (Feb) to $230 (Jul) as the WACC fell from 10.2% to 8.9–9.8% and terminal growth rose from 4.0% to 4.5%. Terminal value is about 86% of EV.

**Barclays.** Barclays models a total P&L only:
- Revenue growth: +6.1% (2026E), +5.5% (2027E), +5.0% (2028E).
- EPS: $5.34, $5.73, $6.02.
- Gross margin *falls* in 2027 (67.8%), the only broker with that view.
- Valuation is 28x 2027E EPS, a multiple raised every quarter (21x, 23.5x, 28x).
- Its thesis is that ongoing price concessions keep Illumina a mid-single-digit grower, and that the 35B flow cell "will need to be priced to compete."

**Freedom.** Freedom forecasts by product line. Consumables grow +4.9%, +6.1% and +5.5% (2026E–28E), and EPS is $5.38, $5.98 and $6.59. The PT blends DCF, 8x EV/Sales and 35x P/E.

**UBS (stale, 4 Mar).** UBS forecasts EPS of $5.07, $5.74 and $6.54, and values the stock at about 15x 2027E EV/EBITDA, a discount to Tools peers. Its best contribution is sizing Roche exposure: counting applications are about 16% of sequencing consumables.

**Bloomberg consensus (10 Oct, before Q3):**

| | 2025A | 2026E | 2027E | 2028E |
|---|---|---|---|---|
| Revenue ($M) | 4,343 | 4,625 (+6.5%) | 4,918 (+6.3%) | 5,263 (+7.0%) |
| Sequencing consumables ($M) | 2,939 | 3,104 (+5.6%) | 3,378 (**+8.8%**) | 3,694 (**+9.3%**) |
| Sequencing instruments ($M) | 465 | 483 | 454 | 454 |
| Adj. operating margin | 23.1% | 23.5% | 25.2% | 26.5% |
| Adj. EPS | $4.84 | $5.36 | $6.11 | $7.01 |

## What the Street assumes without saying so

- **Price per Gb.** Never modeled. If Gb grows 30%, consensus consumables imply total revenue per Gb falling about 15–16% a year (our back-solve). That is similar to the recent pace.
- **The 6000 tail and conversion drag.** No broker quantifies either. JPM: headwinds "largely gone exiting this year." Barclays: "another round… in '27 and beyond."
- **Gb growth.** Not modeled. Brokers take management's ">30%". JPM's own customer survey implies only +11–19%.
- **The 35B, Roche share loss, and flow-cell mix.** None of these is modeled.
- **Consumables re-acceleration.** Consensus has sequencing consumables accelerating from +4.7% (Q2'26 actual) and +5–6% (Q3/Q4) to about +9% in 2027–28, with instruments falling. Consumables supply about 90% of 2027 revenue growth.

## Why this matters for the pitch

1. **Volume and price per Gb are the Street's blind spot.** Every broker models the dollar outcome. None separates "Gb +30%" from "price per Gb −15–20%." Our bridge does, and it shows how little room 2027's +8.8% consumables growth leaves:
   - If Gb slows to +25%, consensus needs price per Gb to fall no more than about 12–13%.
   - The 35B (now H2'27), a still-unconverted clinical 6000 base, and customer cost-per-test guidance all point to price falling faster than that.
2. **Our variance.** 27E revenue about $4.83–4.86B vs $4.92B, and EPS about $5.64–5.79 vs $6.11. 28E EPS about $6.34 vs $7.01 (`2026-10-18_ILMN_27E_pricing_variance.md`).
3. **Valuation drift.** JPM's PT doubled mostly through lower discount rates and higher terminal growth, and Barclays raised its multiple every quarter. Estimates did not drive the targets.
4. **Disclosure is ending.** Illumina drops the X-vs-6000 volume and revenue split after Q4'26. That removes the one data series brokers use to sanity-check price, and makes a volume × price model harder for the Street to build.

## Gaps

- No post-Q3 broker notes or consensus are in the folder. A fresh Bloomberg or broker pull is needed before the pitch.
- UBS is stale (Mar); its later Buy at $260 is known only from headlines.
- JPM's 31 Jul model table is an image and its rows could not be read.
- EBIT definitions differ: JPM's is after stock-based compensation, while consensus and Barclays use the company's adjusted figure.
