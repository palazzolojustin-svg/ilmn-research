# ILMN: NovaSeq X vs NovaSeq 6000 share of high-throughput volume and revenue, and the revenue-per-Gb ratio, Q4 2024 to Q3 2026

**What it is:** each quarter's split of Illumina's high-throughput (HT) sequencing consumables between the NovaSeq X and the NovaSeq 6000, by volume (gigabases shipped) and by revenue. It also gives the implied ratio of the 6000's revenue per Gb to the X's.

**Compiled:** 2026-10-30.

**Sources:**
- Q4'24 to Q2'26 extend `2026-10-13_ilmn_6000_vs_X_revenue_per_gb_ratio.csv`, which draws on Illumina's calls and decks.
- Q3'26 (84% of volume, 60% of revenue) is from the Q3 2026 call (CFO Ankur Dhingra, 29 Oct 2026).

**Chart:** `Outputs/artifacts/2026-10-30_ILMN_X_vs_6000_share_and_rev_per_gb.png`

**Formula:** ratio = (6000 revenue share ÷ 6000 Gb share) ÷ (X revenue share ÷ X Gb share). The 6000 shares are 100% minus the X shares.

**Columns:**
- `quarter`
- `x_pct_ht_gb`, `x_pct_ht_rev`: Illumina's disclosed X shares.
- `6000_pct_ht_gb`, `6000_pct_ht_rev`: 100 minus the X shares.
- `ratio_6000_to_x_rev_per_gb`: the ratio.
- `ratio_low`, `ratio_high`: the range if each disclosed share is off by ±0.5 points of rounding.
- `note`

**Caveats:**
- Shares are rounded, so the ratio carries about ±0.2x of error.
- Gb means gigabases shipped, not used.
- The ratio is relative revenue per Gb, not an absolute $/Gb.
- Illumina said on the Q3 2026 call that it will stop showing this slide after Q4 2026.
