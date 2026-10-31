# ILMN: clinical sequencing consumables ex-China, estimated dollars, Q1-Q3 2026

**What it is:** estimated quarterly revenue (US$M) from Illumina's clinical sequencing consumables outside China. Shows the year-over-year and quarter-over-quarter dollar change, and percentage growth.

**Compiled:** 2026-10-31.

**Method:** Illumina does not disclose clinical dollars. It does disclose:
- ex-China sequencing consumables dollars (earnings decks, Q1'24-Q2'26);
- ex-China clinical and research & applied growth rates.

Clinical dollars are back-solved from these with the same method as `analyses/2026-10-30_ILMN_clinical_2027_implied_bridge.py`. For Q1 and Q2 2025 there are two independent back-solves (the 2024-to-2025 decks and the 2025-to-2026 decks), and they agree within about $3M. The 2026 quarters are the 2025 base grown at the reported rate. Q3'26 growth (14%) comes from the Q3'26 call because there is no Q3'26 deck in the folder.

**Precision:** growth rates are disclosed as whole percentages. A ±0.5pt rounding error moves the dollar estimates by about ±$2-5M.

The implied clinical share of ex-China sequencing consumables is about 61% in 2025 and 66-68% in 2026. Management says about 65% (Q2'26 call, which includes China).

## Columns

- `period`: fiscal quarter.
- `clinical_exchina_rev_usd_m_est`: estimated clinical ex-China consumables revenue, $M.
- `prior_year_quarter_usd_m_est`: same quarter a year earlier, $M (estimated).
- `yoy_change_usd_m`: dollar change versus the prior-year quarter.
- `yoy_pct_reported`: Illumina's disclosed growth, % (reported basis).
- `prior_quarter_usd_m_est`: the preceding quarter, $M (Q4'25 = $438M est.).
- `qoq_change_usd_m`: sequential dollar change.
- `qoq_pct`: sequential % change.
