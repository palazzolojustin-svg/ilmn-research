# ILMN: NovaSeq 6000 vs NovaSeq X revenue per Gb, quarterly (2026-10-13)

**What it is:** the ratio of revenue per gigabase (Gb) on the NovaSeq 6000 to revenue per Gb on the NovaSeq X, for each quarter Illumina has disclosed the inputs (Q2 2024 to Q2 2026). Q2 2024 is the first quarter disclosed; no figures exist for Q1 2024 or earlier.

**Source:** Illumina earnings calls and investor decks, Q2 2024 to Q2 2026. Illumina discloses the X's share of high-throughput (HT) Gb and of HT consumables revenue; it does not disclose the ratio. Figures were compiled in `Outputs/analyses/2026-10-11_clinical_consumables_scrape/08_transition_and_unit_economics_dataset_corpus.md`; the ratio and index arithmetic is ours.

**Formula:** ratio = (6000 revenue share ÷ 6000 Gb share) ÷ (X revenue share ÷ X Gb share), where the 6000 shares are 100% minus the X shares.

**Columns**
- Quarter.
- X % of HT Gb and X % of HT revenue: Illumina's disclosed shares.
- 6000 % of HT Gb and 6000 % of HT revenue: 100 minus the X shares.
- X and 6000 revenue/Gb index: each platform's revenue per Gb relative to the HT average (1.0 = average). This is not an absolute $/Gb.
- 6000 / X revenue per Gb: the ratio.
- Ratio low and Ratio high: the range implied by Illumina rounding each share to a whole point (±0.5).
- Note: source caveats.

**Caveats**
- Shares are rounded, so the ratio carries about ±0.1–0.2x of error.
- The share is Gb shipped, not Gb used.
- Several shares were stated loosely on the calls ("~45%", ">35%", ">65%", "~80%"); deck values are used where available.
