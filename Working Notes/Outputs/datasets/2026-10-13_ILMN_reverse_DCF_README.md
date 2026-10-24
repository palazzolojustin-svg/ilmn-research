# ILMN reverse DCF (2026-10-13; updated 2026-10-14)

**File:** `2026-10-13_ILMN_reverse_DCF.xlsx`. One sheet, "Reverse DCF", built with live formulas and recalculated in Excel (no formula errors).

**What it does:** finds the 2027E–2031E revenue growth rate at which a DCF returns today's share price ($271.76, the 14 Oct 2026 close). It assumes management's margin targets and an exit at the **2031E EV/EBITDA equivalent to 30.0x 2031E P/E** (20.4x at the solved case). The equivalent multiple is computed live in L5 as (P/E x 2031 adj. net income + net debt) / 2031 adj. EBITDA, so the result is identical to a 30x P/E exit. The layout follows the user's template:
- Left block: revenue, growth, COGS, gross profit, opex, adjusted EBITDA, margins and two "implied" rows.
- Right block: the valuation bridge (2031 EV/EBITDA, 2031 adjusted EBITDA, PV of terminal value, PV of unlevered FCF, EV, net debt, equity value, FDSO, implied price, upside).

**Terminal value:** 2031 adjusted EBITDA × the equivalent EV/EBITDA, which equals 30x 2031 adjusted net income plus net debt. It is discounted from 31 Dec 2031 at the WACC. Net debt is held constant, because all free cash flow is counted in the PV of unlevered FCF. Adjusted net income (rows 60–62) = (adj. EBIT − $65M net interest) × (1 − 20.5%).

**Key inputs (blue; yellow = key)**
- **Price and timing:** price $271.76; valuation date 14 Oct 2026.
- **Discounting:** WACC 9.5% (sell-side range 8.9–10.2%).
- **Exit:** 30.0x 2031E P/E anchor in B24, converted to EV/EBITDA in L5.
- **Revenue:** 2026E $4,620M, the guidance midpoint.
- **Margins:**
  - Gross margin 68.5% in 2026E rising to 70%.
  - Operating margin 23.5% in 2026E (guide), then 26% in 2027E (management target), held flat after because there is no later target.
  - Depreciation 4.6% falling to 4.1% of revenue.
- **Cash-flow and earnings items:** tax 20.5%; capex 4.9% of revenue; NWC at 15% of incremental revenue; SBC not deducted (switchable); net interest and other expense $65M a year.
- **Balance sheet:** net debt $823M (28 Jun 2026); FDSO 153.0M.

**Result**
- Implied 2027E–2031E revenue CAGR is **15.9%**, with B25 solved so that implied upside in L14 is 0.
- That implies:
  - 2031E revenue of about $9.7B, against consensus of $6.7B.
  - 2031E adjusted EPS of $12.73, against consensus of $11.01.
- **Sensitivity (static solver output, WACC 9.5%):**

  | 2031E P/E (equivalent EV/EBITDA) | Implied revenue CAGR |
  |---|---|
  | 20x (13.7x EV/EBITDA) | 24.8% |
  | 25x (17.0x) | 19.9% |
  | 30x (20.4x) | 15.9% |
  | 35x (23.6x) | 12.7% |
  | 40x (26.9x) | 10.0% |

  At a 30% post-2027 operating margin, the 30x case needs 12.5%.
- **Implied price/Gb rows:** (1 + consumables growth) / (1 + Gb growth) − 1. At the solved growth, the implied annual price/Gb change is about −7% at 25% Gb growth and about −11% at 30%, against an actual −18% to −21% in 2024–2025.

**Sources:**
- Bloomberg consensus (10 Oct 2026).
- ILMN Q2 2026 10-Q and call (30 Jul 2026).
- Aug 2024 strategy-update targets (redefined ex-China; reaffirmed through Q2 2026).
- Core Notes 02, 03, 05, 06 and 08.

**To re-solve:** in Excel, Data > What-If Analysis > Goal Seek. Set L14 to 0 by changing B25. Update the price in B21 first.

**Slide:** `Outputs/analyses/2026-10-14_ILMN_reverse_DCF_slide.pptx` reproduces the summary table and valuation block as native, editable PowerPoint tables (16:9).

**Delta-to-consensus rows (added 2026-10-14):** rows 7, 11 and 15 show the model minus Bloomberg consensus, in bps, for revenue growth, gross margin and adjusted EBITDA margin (2026E–2031E). Consensus inputs sit in the block at rows 82–87 (BBG Annuals, 10 Oct 2026). At the solved case:
- Revenue growth runs about +580 to +960 bps a year above consensus from 2027E.
- Gross margin runs 0 to −80 bps below.
- EBITDA margin runs +20 to −260 bps, because the operating margin is held at management's 26% target while consensus expands it to about 29%.

**Consensus-margin case (updated 2026-10-14, now the base case):** the margin inputs are linked to Bloomberg consensus. Gross margin (row 39) = consensus adj. gross margin (row 85). Operating margin (row 40) = consensus adj. EBITDA margin (row 87) less depreciation %, so EBITDA margin equals consensus. Both margin delta rows are 0 bps. Re-solved: implied 2027E–2031E revenue CAGR **13.9%** (2031E revenue ~$8.9B against consensus $6.7B; revenue growth +383 to +761 bps a year above consensus). Exit 20.6x 2031E EV/EBITDA (equivalent to 30x P/E); 2031E adj. EPS $12.70. Implied price/Gb change about −9% a year at 25% Gb growth and −12% at 30%. Sensitivity tables were recomputed at consensus margins: at a 9.5% WACC, 20x/25x/30x/35x/40x P/E needs 22.6%/17.8%/13.9%/10.8%/8.1%. The management-margin results described above are superseded.
