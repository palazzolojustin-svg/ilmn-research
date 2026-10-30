# ILMN EPS beats vs guidance and Street, Q4 2024 to Q3 2026

- **What:** For each quarter, how far Illumina's non-GAAP diluted EPS beat (1) the midpoint of management's guide, given on the prior quarter's call, and (2) the pre-print Street consensus. Each beat is shown in dollars and as a percentage.
- **Compiled:** 2026-10-30, from:
  - ILMN earnings call extracts and decks, Q3'24 to Q3'26
  - Seeking Alpha transcript headers
  - Bloomberg Intelligence previews and post-print notes
  - JPM, Barclays and Ameriprise/FactSet notes
  - the Bloomberg consensus printout of 10 Oct 2026
- **Chart:** `Outputs/artifacts/2026-10-30_ILMN_EPS_beat_vs_guide_and_street.png`
- **Companion (revenue):** `2026-10-30_ILMN_beat_vs_guide_and_street.csv`

## Columns

- `quarter`: fiscal quarter.
- `guide_range`, `guide_mid`: the EPS guidance range and its midpoint.
- `guide_is_proxy`: "yes" when there was no quarterly guide, so the range is FY guide minus year-to-date actual.
  - Q4'24: $4.05–4.15 minus $3.21. The year-to-date figure uses a derived Q1'24 core EPS.
  - Q4'25: $4.65–4.75 minus $3.50.
- `actual_eps`: non-GAAP diluted EPS as reported by management. It is core (ex-GRAIL) for Q4'24 and excludes tariff refunds for Q3'26.
- `beat_vs_guide_usd` / `_pct`: actual minus guide midpoint, in dollars and as a % of the midpoint.
- `consensus_eps`: pre-print consensus. It is SA-implied, and matches the BI previews.
- `beat_vs_street_usd` / `_pct`: actual minus consensus, in dollars and as a % of consensus.
- `notes`: caveats for that quarter.

## Caveats

- **Q4'24:** Seeking Alpha and BI show $0.86, "missing by $0.06". That is consolidated EPS including GRAIL. On the core basis that consensus tracked, EPS was $0.95, a beat of $0.03.
- **Q4'25 and Q4'24 were pre-announced at JPM in January:**
  - Q4'25 at $1.27–1.30, while consensus stayed near $1.21–1.23. Against the pre-announced midpoint, the beat was about $0.06.
  - Q4'24 at $0.91–0.93.
- **Q3'26:** $1.44 excludes the tariff-refund benefit, which was not in guidance.
- **Tax:** the tax rate moved between 18.6% and 22% over the period, which affects the size of the beats. For example, Q3'25 tax came in at 18.6% against about 16% guided.
