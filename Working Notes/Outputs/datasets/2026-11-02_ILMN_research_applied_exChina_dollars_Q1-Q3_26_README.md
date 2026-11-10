# ILMN: research & applied sequencing consumables ex-China, estimated dollars, Q1-Q3 2026

**What it is:** estimated quarterly revenue (US$M) from Illumina's research & applied (R&A) sequencing consumables outside China, with year-over-year and quarter-over-quarter dollar and percent change. It is the companion to `2026-10-31_ILMN_clinical_exChina_dollars_Q1-Q3_26.csv`.

**Compiled:** 2026-11-02.

**Method:** the same back-solve as the clinical file (`analyses/2026-10-30_ILMN_clinical_2027_implied_bridge.py`).
- For 2025, R&A equals ex-China sequencing consumables (from the earnings decks) minus back-solved clinical.
- 2026 quarters are the 2025 base grown at Illumina's disclosed R&A ex-China growth: -12% (Q1), -7% (Q2), -6% (Q3, from the Q3 call).
- Check: clinical plus R&A reproduces the deck's ex-China sequencing consumables total of $687M (Q1'26) and $734M (Q2'26) within $1M.
- Q3'26 has no deck in the folder, so its total ($752M) is implied.

**Precision:** growth is disclosed in whole percents, so each estimate carries about ±$2-5M of rounding error.

**Seasonality:** R&A is seasonal. Q4 is high on year-end budget spending and Q1 is low, so the q/q swings mostly reflect the calendar. Use the y/y columns for trend.

## Columns
- `period`: fiscal quarter.
- `ra_exchina_rev_usd_m_est`: estimated R&A ex-China sequencing consumables revenue ($M).
- `prior_year_quarter_usd_m_est`: same quarter a year earlier ($M).
- `yoy_change_usd_m`: dollar change versus the prior-year quarter.
- `yoy_pct_reported`: Illumina's disclosed growth rate (%).
- `prior_quarter_usd_m_est`: preceding quarter ($M; Q4'25 = $275M est.).
- `qoq_change_usd_m` and `qoq_pct`: sequential change.
- `clinical_exchina_usd_m_est` and `total_exchina_seq_consumables_usd_m`: for reference.
