# ILMN EPS beat bar chart (2026-10-30)

**What it is:** a native Excel clustered-column chart of Illumina's adjusted EPS beat in each quarter from Q2'25 to Q3'26. For each quarter, one bar shows the beat against management's guidance midpoint and one shows the beat against Street consensus. Bar labels show the percentage beat. The chart can be copied straight into PowerPoint.

**Columns (sheet "EPS beat"):**
- Quarter
- Beat vs mgmt guide (%)
- Beat vs Street (%)
- Beat vs guide (cents)
- Beat vs Street (cents)

**Source:** `analyses/2026-10-30_ILMN_EPS_beat_magnitude_vs_guide_and_street.md` (ILMN releases and calls; consensus going into each print).

**Caveats:**
- **Q4'25 had no quarterly guide.** Its guide is the midpoint implied by the FY25 guide.
- **Q3'26 excludes tariff refunds.**

**Build:** `artifacts/2026-10-30_ILMN_EPS_beat_bar_chart_build.py`.
