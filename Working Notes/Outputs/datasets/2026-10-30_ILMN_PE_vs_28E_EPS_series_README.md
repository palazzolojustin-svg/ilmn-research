# ILMN 26E P/E and 28E EPS daily series behind the P/E-vs-EPS chart (13 Oct 2025 to 30 Oct 2026)

**What it is:** the two series plotted in `Outputs/artifacts/2026-10-30_ILMN_PE_vs_28E_EPS_chart.pptx`. That file is a native, editable PowerPoint chart, extended to 30 Oct 2026, with the 30 Oct post-Q3 crash highlighted.

**Built:** 2026-10-30 by `Outputs/artifacts/2026-10-30_ILMN_PE_vs_28E_EPS_chart_build.py`.

**Sources:**
- **P/E, 30 Oct 2025 to 30 Oct 2026:** Capital IQ export `Charts (7).xls`, series "NasdaqGS:ILMN - Fwd P/E Est. CY+1".
- **P/E, 13 to 29 Oct 2025:** not in the export, so these 13 points are read off the user's original chart image.
- **28E EPS to 12 Oct 2026:** read off the original chart image, anchored to its $6.22 / $6.68 / $6.89 / $7.06 labels. Accuracy is about ±$0.02.
- **28E EPS after 12 Oct 2026:** held flat at $7.06. The user asked to assume no estimate revisions.

**Columns:**
- `date`
- `pe_26e_capiq_fwd_cy1`
- `eps_28e`
- `pe_source` (image / CapIQ export)
- `eps_source` (image / held flat)

**Key point:** the P/E went from 54.15x on 29 Oct to 43.09x on 30 Oct, a 20.4% fall, after the Q3'26 print.
