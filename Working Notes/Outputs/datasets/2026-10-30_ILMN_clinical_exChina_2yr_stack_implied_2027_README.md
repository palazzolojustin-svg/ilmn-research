# ILMN: ex-China clinical consumables two-year stacks, implied Q4'26 and 2027 growth needed

**What it is:** reported ex-China clinical consumables growth and two-year stacks (Q1'25 to Q3'26), plus an implied Q4'26 / FY26 and the FY27 clinical growth needed for total revenue to grow 8.5% (midpoint of high single digits, as specified by the user).

**Compiled:** 2026-10-30. Model: `Outputs/analyses/2026-10-30_ILMN_clinical_2027_implied_bridge.py` (prints all sensitivities). Write-up: `Outputs/analyses/2026-10-30_ILMN_clinical_2027_implied_bridge.md`.

**Inputs:** Illumina decks Q3'25 to Q2'26 (RoW consumables $ and clinical / R&A growth), Q3'26 call (clinical +14%, R&A -6%, FY26 guide $4.64-4.66B, Q4 consumables "5%, 6%"), Bloomberg consensus annuals dated 10 Oct 2026 (pre-Q3 print).

**Columns:** `period`; `clinical_exchina_yoy_pct`; `prior_year_yoy_pct`; `two_year_stack_pts` (simple sum); `status` (reported / implied); `basis`.

**Key assumption:** clinical $ are not disclosed. They are back-solved each quarter from RoW consumables $ and the disclosed clinical and R&A growth rates (FY25 clinical about $1.68B, about 61% of RoW sequencing consumables; FY26E about $1.94B, about 66%).
