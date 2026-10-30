# ILMN: clinical high-throughput, NovaSeq X vs NovaSeq 6000, with clinical growth, Q4 2024 to Q3 2026

**What it is:** the clinical-only version of the X vs 6000 table, with clinical consumables growth outside China added. Built 2026-10-30 to the user's layout.

**Sources:** Illumina's original earnings decks (Q2'25 to Q3'26) and Prepared Remarks (Q1'25 to Q3'26), read from investor.illumina.com.
- **Clinical volume shares** come from the transition slide in the Q3'26 deck.
- **Clinical growth** comes from the deck revenue-detail tables. These are reported growth rates, not organic.

**Chart:** `Outputs/artifacts/2026-10-30_ILMN_clinical_X_vs_6000_table.png`

## Columns

- `x_pct_clinical_vol` and `6000_pct_clinical_vol`: disclosed. The 6000 figure is 100 minus the X figure.
- `x_pct_clinical_rev_est` and `6000_pct_clinical_rev_est`: **estimates.** Illumina never discloses the X's share of clinical revenue; every deck charts revenue as a total series only. They assume clinical's 6000/X revenue-per-Gb gap equals the total HT ratio.
  - Formula: X share of clinical revenue = v ÷ (v + (100 − v) × ratio), where v is the X share of clinical volume.
- `ratio_6000_to_x_rev_per_gb_assumed_total`: the total HT ratio, from `2026-10-30_ILMN_X_vs_6000_share_and_rev_per_gb.csv`. Under the assumption above, the clinical ratio equals the total ratio by construction.
- `clinical_consumables_exchina_yoy_pct`: reported growth from the decks.

## Caveats

- **Cross-check.** CEO Jacob Thaysen said clinical revenue on the X was "less than 50%" (Wolfe conference, Nov 2025). The Q3'25 estimate here is 34%, which is consistent with that.
- **The estimated columns can't test whether clinical's price gap differs from research's.** Only a disclosed clinical revenue share could do that.
