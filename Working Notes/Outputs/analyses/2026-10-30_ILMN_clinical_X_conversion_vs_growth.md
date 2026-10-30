# Clinical NovaSeq X Conversion vs Clinical Growth: Does Inelastic Conversion Hit Revenue Harder?

*Prepared 2026-10-30. Data: `Outputs/datasets/2026-10-30_ILMN_clinical_X_conversion_vs_growth.csv` (see its README). Chart: `Outputs/artifacts/2026-10-30_ILMN_clinical_X_conversion_vs_growth.png`. Total-company version: `2026-10-30_ILMN_X_vs_6000_share_and_rev_per_gb.md`.*

## The thesis being tested

Large, volume-elastic clinical labs can move a lot of volume to the NovaSeq X and still grow revenue. They run far more Gb at the lower price. Smaller, inelastic labs move little volume, but each move costs revenue outright, because they don't add Gb. So a small conversion step can bring an outsized slowdown.

## The data limit

Illumina discloses the X's share of clinical **volume**, but never its share of clinical **revenue**. A clinical-only revenue-per-Gb ratio therefore cannot be calculated from disclosures. The workaround below applies the total high-throughput ratio to clinical, which is an assumption.

## What the data shows

| Quarter | X % clinical volume | Shift (pts) | Revenue cost if no extra Gb | Clinical growth, RoW | Two-year stack |
|---|---|---|---|---|---|
| Q4'24 | 49 | n/a | n/a | 8% | n/a |
| Q1'25 | 51 | +2 | -1.9% | 8% | n/a |
| Q2'25 | 53 | +2 | -1.9% | 10% | n/a |
| Q3'25 | 64 | +11 | -12.4% | 12% | n/a |
| Q4'25 | 71 | +7 | -8.7% | 20% | 28% |
| Q1'26 | 76 | +5 | -7.6% | 20% | 28% |
| Q2'26 | 78 | +2 | -3.0% | 15% | 25% |
| Q3'26 | 78 | 0 | 0% | 14% | 26% |

1. **The elastic case (Q3'25 to Q1'26).** 23 points of clinical volume moved over three quarters. With no extra Gb, that would have cost about 8–12% of clinical high-throughput revenue each quarter. Instead clinical growth rose from 12% to 20%. Those movers added far more volume than the price cut cost them. They were highly elastic, mostly large labs running multi-unit expansions.
2. **The inelastic case (Q2'26).** Only 2 points moved, and growth fell 5 points (20% to 15%). The two-year stack fell 3 points (28% to 25%). This fits the thesis, but conversion can explain at most about 3 points of the drop, and only if those labs added no volume at all. Management blamed the rest on the Middle East and Latin America, and said US clinical was still above 20%.
3. **No conversion (Q3'26).** Nothing moved, and the two-year stack edged back up from 25% to 26%. This also fits: without inelastic conversion, the drag eases.

## Caveats

- Growth is year-on-year, while the cost is quarter-on-quarter. A step in one quarter weighs on the comparison for four quarters.
- Pull-through on new clinical X systems takes 6–9 months, per management. Part of the 20% in Q4'25 and Q1'26 is volume ramping from earlier placements.
- Clinical consumables include mid-throughput, so the cost bars overstate the effect on consumables growth.
- Calls and decks disagree on some clinical figures: Q1'25 growth, Q2'25 volume and Q3'25 growth.
