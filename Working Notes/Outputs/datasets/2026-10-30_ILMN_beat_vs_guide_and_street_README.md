# ILMN revenue beats vs guidance and Street, Q4 2024 to Q3 2026

- **What:** For each quarter, how far Illumina's revenue growth beat (1) management's guidance midpoint for Rest-of-World (ex-China) organic or constant-currency growth and (2) the Street consensus, in basis points of growth.
- **Compiled:** 2026-10-30, from ILMN earnings call transcripts and decks Q3'24 to Q3'26 (Sources/Extracts), 10-Qs and 10-Ks, Seeking Alpha transcript headers (consensus beat in $), and the Bloomberg consensus printout of 10 Oct 2026.
- **Chart:** `Outputs/artifacts/2026-10-30_ILMN_beat_vs_guide_and_street.png`

## Columns

- `quarter`: fiscal quarter.
- `guide_basis`: the guidance metric as stated at the time. The metric changed three times:
  - total Core cc to Q1'25;
  - ex-China cc from Q2'25 to Q4'25;
  - RoW organic from Q1'26, which also strips SomaLogic.
- `guide_growth_mid_pct`, `actual_growth_pct`: guide midpoint and actual growth, %.
- `beat_vs_guide_bps`: actual minus guide midpoint, in bps.
  - Q4'24 is a $ proxy: the beat versus the $1.07B guide divided by the prior-year base.
- `guide_is_proxy`: yes when no RoW guide was given (Q4'24, Q1'25).
- `consensus_rev_musd`: consensus implied by the Seeking Alpha beat. For Q3'26 it matches Bloomberg's $1,154M.
- `actual_rev_musd`: actual revenue, $M.
- `prior_year_rev_musd`: Core revenue a year earlier, $M. The Q4'23 base is derived.
- `beat_vs_street_musd`, `beat_vs_street_bps`: the beat in $M, and that beat divided by prior-year revenue, in bps.
  - This is total revenue, not RoW organic. No source in the folder gives a Street RoW-organic forecast.
- `notes`: caveats.

## Caveats

- **Q4'25.** Management gave no formal quarterly guide; the 4% is the CFO's implied figure. Against Street, the Seeking Alpha consensus is post-preannouncement. Against the pre-JPM FactSet figure ($1,099M), the beat is about $60M, or about 540 bps.
- **Q3'26.** Revenue is $1,166M, excluding the $37M tariff-refund credit to customers. Reported revenue of $1,129M would be about 22 bps below Street.
- **Q1'25.** The actual (about -0.2% cc) is derived as -1.4% reported plus 1.2 points of FX.
