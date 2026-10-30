# ILMN: clinical NovaSeq X conversion vs clinical consumables growth, Q4 2024 to Q3 2026

**What it is:** a quarterly table of three things for Illumina's clinical customers:
- how much of their high-throughput volume has moved to the NovaSeq X;
- how much revenue each quarter's move could cost, if the labs that moved added no extra volume;
- clinical consumables growth in the Rest of World (RoW, meaning excluding China).

**Compiled:** 2026-10-30, from Illumina earnings calls and decks (Q4'24 to Q3'26), via an agent sweep of the calls, the decks, the clinical-consumables scrape (file 08) and Core Notes 16.

**Chart:** `Outputs/artifacts/2026-10-30_ILMN_clinical_X_conversion_vs_growth.png`

## Columns

- `x_pct_clinical_ht_gb`: the X's share of clinical high-throughput Gb, as disclosed.
  - Where calls and decks differ, the deck figure is used: Q2'25 is 53% (the call said "roughly 55%"), and Q4'25 is 71% (the call said "more than two-thirds").
- `qoq_shift_pts`: points of clinical volume that moved to the X during the quarter.
- `x_pct_clinical_ht_rev_derived`: the X's share of clinical revenue. **Illumina does not disclose this.** It is derived by applying the total high-throughput 6000/X revenue-per-Gb ratio to clinical volume. This is the same method Core Notes 16 uses, and it is an assumption.
- `total_ht_ratio_6000_to_x`: from `2026-10-30_ILMN_X_vs_6000_share_and_rev_per_gb.csv`.
- `max_rev_cost_of_shift_pct`: the share of clinical high-throughput revenue lost if the labs that moved added no Gb. Formula: shift × (ratio − 1) ÷ (prior X share + (1 − prior X share) × ratio).
- `clinical_consumables_row_yoy_pct`: clinical consumables growth, RoW, as shown in Illumina's decks. It is reported growth, not organic.
  - For Q1'25 the call said "mid-single digits", while the decks say 8%.
  - For Q3'25 the CEO said "high single-digit", the CFO said "double-digit", and the deck says 12%.
- `clinical_2yr_stack_pct`: this year's growth plus last year's growth for the same quarter.

## Caveats

- **Cost and growth are measured differently.** The cost is quarter-on-quarter, while growth is year-on-year.
- **The cost is a ceiling.** It applies only if the labs that moved added no volume.
- **Clinical consumables include mid-throughput,** which is outside these figures, so the cost overstates the effect on clinical consumables growth.
- **The ratio is borrowed from the total.** Clinical's own 6000/X ratio is unknown.
