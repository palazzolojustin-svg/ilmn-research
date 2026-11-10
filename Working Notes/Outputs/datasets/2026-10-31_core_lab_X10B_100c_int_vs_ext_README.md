# NovaSeq X 10B, 100 cycles: core-facility $/Gb, internal vs external rates (2026-10-31)

**File:** `2026-10-31_core_lab_X10B_100c_int_vs_ext.xlsx`, one sheet, "X10B_100c_int_vs_ext".

**What it is.** This workbook combines two tables from `2026-10-13_core_lab_price_per_gb.xlsx`, sheets `RL_X10B_int_100c` and `RL_X10B_ext_100c`:
- the 27-core internal (own-institution) rate table
- the 14-core external academic rate table

Both tables give the NovaSeq X 10B flow cell price at 100 cycles in USD per Gb, monthly from 2024-10 to 2026-10. The values are copied as they stand. For the observed, document-dated and carried flags, local-currency prices and source URLs, see the source workbook and its README.

**Columns**
- **A:** month.
- **B and C:** internal and external median $/Gb. These are live `MEDIAN` formulas across the cores that have a price that month; `NA()` is used if no core has one.
- **D and E:** the number of cores behind each median.
- **G onward:** internal cores ("Int: ..."), then external cores ("Ext: ...").

**Charts** (native Excel line charts, below the data)
1. Internal and external medians.
2. Every core, with internal in grey and external in orange dashed lines, plus both medians in bold (internal black, external red).

**Key values**
- **Internal median:** $10.14/Gb (Oct 2024) to $8.02/Gb (Oct 2026).
- **External median:** $13.73/Gb to $10.70/Gb.
- External rates run about $1.5–3.5/Gb above internal.

**Caveats** (carried over from the source dataset)
- Many cells are carried forward rather than observed.
- The set of cores behind each median grows over time, so a move in the median can reflect which cores are included rather than real price changes.
- Output is the manufacturer's maximum at 2x150, so true $/Gb is somewhat higher.

**Rebuild**
1. `python 2026-10-31_core_lab_X10B_100c_int_vs_ext_build.py <copy of 2026-10-13_core_lab_price_per_gb.xlsx> <out.xlsx>`
2. Then run `2026-10-31_core_lab_X10B_100c_int_vs_ext_format.ps1 -Path <out.xlsx>`. This is the Excel formatting pass: Garamond font and chart layout.
