# Model logic

How a built model computes, as implemented in `scripts/fmb/periods.py` (column axis), `engine.py` (line registry and formula language), `spec_builder.py` and `canon.py` (what the inputs workbook turns into), `sheets/drivers.py`, `sheets/dcf.py`, `sheets/tearsheet.py` and `cases.py`. The code is the source of truth; when this file and the code disagree, read the code. Cell references below come from the Illumina example (quarters 1Q25-4Q28, annual-only FY2029-FY2030, columns D-Y) and the Spotify rebuild (quarters 1Q23-4Q28, columns D-AI), so every pattern is shown as the Excel formula it produces.

## Contents
1. Period axis
2. Formula mini-language
3. Line definitions and cell evaluation
4. Variance sub-rows
5. Delta blocks
6. Driver types and the formulas they generate (worked examples)
7. Revenue-tree kinds
8. Cost blocks (Margin Build)
9. Condensed statements
10. Drivers & Casing Active rows
11. DCF
12. Tearsheet
13. Number formats

## 1. Period axis (`periods.py`)

Period ids are `1Q25` for quarters and `FY2025` for fiscal years; `parse_pid` also accepts `1Q2025`, `2025Q1`, `FY 2025E` and `2025` (a trailing `E` is ignored). `PeriodAxis.build(first_hist_q, last_actual_q, last_est_q, annual_only_years, period_ends, fy_end_month)` lays columns out from D (`FIRST_DATA_COL = 4`; A is the marker column, B labels, C a spacer): for every fiscal year from the first history quarter to `last_quarterly_estimate`, its quarters in range and then that year's FY column; after the last quarterly year, one column per entry of `annual_only_years`. FY columns sit between 4Q and the next 1Q because the reference model is laid out that way.

| Property | Rule |
|---|---|
| `label` | `1Q25`, `3Q26E`; FY with quarters `FY 2026E` (with a space); annual-only `FY2029E` (no space) |
| `estimate` | a quarter after `last_actual_quarter`; an FY after the last actual year, or the same year when the last actual quarter is not Q4; annual-only years always |
| `end` | `horizon.period_ends[pid]` from the data, else `fiscal_quarter_end` (month-end quarters; the FY is named by the calendar year it ends in) |
| `weeks` | quarters: `round((end - previous quarter end) / 7)`, the first quarter 13; FY: the sum of its four quarters, else 52. Row 9 (`Weeks in Period`) shows the number for quarters, `=SUM(D9:G9)` for an FY with quarters, 52 for annual-only years |
| `report_date` | `horizon.report_dates[pid]`, written to row 10 (`Earnings Report`) for actual quarters |
| `prior_year(p)` | the same quarter of the prior year; for any FY column (annual-only included) the prior FY column |
| `prior_period(p)` | the previous quarter (4Q of the prior year for a 1Q); for FY columns the prior FY |
| `offset(p, n)` | n quarters for a quarter, n fiscal years for an FY column |

Templates do not know whether they sit in a quarter or a year: `@pq` means "previous quarter" in quarterly columns and "previous year" in FY columns, and `{months}` is 3 or 12. One `proj_dsl` therefore serves estimate quarters and annual-only years alike.

The Drivers & Casing sheet uses `axis.sub_axis(axis.drivers_start_pid())`: the same periods from the first quarter of the last actual fiscal year (fallback: the first estimate period), renumbered from column D. Column letters differ between the builds and the drivers sheet (ILMN: 1Q26 is I on the builds and D on Drivers & Casing; FY2029 is X and S). `build` writes `<model>.map.json` with `columns`, `drivers_columns`, every line's row (`lines`), the Active rows (`drivers`), `dcf` and `tearsheet` cells; use it instead of counting rows.

ILMN axis: D-G 1Q25-4Q25, H FY2025, I-L 1Q26-4Q26 (K and L are estimates), M FY2026E, N-Q 1Q27E-4Q27E, R FY2027E, S-V 1Q28E-4Q28E, W FY2028E, X FY2029E, Y FY2030E. Drivers & Casing: D-G 1Q26-4Q26, H FY2026, I-L 1Q27-4Q27, M FY2027, N-Q 1Q28-4Q28, R FY2028, S FY2029, T FY2030.

## 2. Formula mini-language (`engine.py`)

A line's formula is a template. `SheetBuilder.formula(dsl, period)` expands every `{token}` (`TOKEN_RE`, no nesting) into a reference for the column being written and prefixes `=` when missing; each column of a line is expanded separately, so one template yields the whole row.

| Token | Resolves to | Example (ILMN, 3Q26E = column K) |
|---|---|---|
| `{id}` | line `id` in the same period: the current sheet first, then Revenue Build, Margin Build, Income Statement, Balance Sheet, Cash Flow Statement, Drivers & Casing, DCF, then other sheets (`LOOKUP_ORDER`); another sheet gives `'Sheet'!K14`, which the colour rule paints green | `{m_product}` -> `K14` |
| `{id@py}` / `{id@pq}` | prior year / prior period (section 1) | `{seq_cons@py}` at 1Q27E (N) -> `I38` |
| `{id@fy}` | the FY column of the period's fiscal year | |
| `{id@-2}` / `{id@+1}` | n periods back or forward; the sign is required | `{ab_pct@-6}` |
| `{id@4Q25}` | that period's column | |
| `{...$}` | absolute reference; combines with every form above | `{ab_rpu@2Q26$}` -> `$T$60` |
| `{id.pct_yoy}` | a sub-row (ids are `line.key`) | `{seq_cons.pct_yoy}` -> `K39` |
| `{Sheet Name!id}` | explicit sheet | `{Income Statement!total_rev}` -> `'Income Statement'!K18` |
| `{sumq:id}` `{avgq:id}` `{lastq:id}` `{firstq:id}` | the four quarters of this FY column; blank in quarters and annual-only years | `{sumq:seq_cons}` at FY2026E -> `SUM(I38:L38)` |
| `{drv:id}` | the Active row of driver `id` on Drivers & Casing, same period, through the drivers axis; blank before that axis starts | `{drv:gm_product}` -> `'Drivers & Casing'!F61` |
| `{months}` `{weeks}` | `3` or `12`; this column's weeks cell | `K$9` |
| `{case}` `{col}` `{row:id}` | `'Drivers & Casing'!$B$5`; this column's letter; a line's row number | used by SUMIF and the DCF rows |
| `{data:key}` | the data value of `key` for this period, written as a typed (blue) input | `={data:beg_cash}` -> `=1127.0` |

Rules the resolver enforces:
- A plain `{id}` with no offset and no sheet inside the formula of line `id` itself means the same-named line on another sheet (a link), never the cell being written; with an offset it is a lag of the same line (`={other_cogs@py}`).
- An unknown line id raises `KeyError` and the build stops naming the sheet, row and id. An offset that leaves the axis (the prior year of the first history year, `{drv:}` before the drivers axis) leaves the whole cell blank instead of writing a broken formula.
- Text outside braces goes to Excel unchanged, so `AVERAGE(`, `ROUND(`, constants and `$` anchors are allowed.

Examples: `={seq_cons@py}*(1+{seq_cons.pct_yoy})` -> `=I38*(1+N39)` at 1Q27E and `=W38*(1+X39)` at FY2029E; `={drv:recv_pct}*{Income Statement!total_rev}*13/{weeks}` on the Balance Sheet -> `='Drivers & Casing'!F125*'Income Statement'!K18*13/K$9`; `={ab_rpu@pq}+({ab_rpu@4Q27$}-{ab_rpu@2Q26$})/6` (Spotify) -> `=T60+($AA$60-$T$60)/6`; `={drv:peak_px@1Q26$}` -> `='Drivers & Casing'!$D$67`.

## 3. Line definitions and cell evaluation

A line is a dict in a sheet's `blocks` (`{"line": {...}}`; `L(...)` in `spec_builder.py`). Other blocks: `{"section": title}`, `{"band": title}`, `{"subtitle": title}`, `{"label": text}`, `{"blank": n}`, `{"deltas": [...]}`; a line block takes `gap: false` to suppress the blank row after it.

| Key | Meaning |
|---|---|
| `id`, `label` | registry id (unique per sheet) and the column-B text |
| `kind` | `amount` (default), `count`, `price`, `pct`, `bps`, `shares`, `eps`, `mult`, `number1`, `number2`, `int`, `date`, `none`; sets the number format through `KIND_FMT` and the default variance rows |
| `fmt` | number-format name overriding the kind (`amount_s`, `pct_s`, `pct_plain`, ...) |
| `hist` | actual quarters: a data key (string), `{"kind": "data", "key": ...}`, `{"kind": "formula", "dsl": ...}` or `{"kind": "blank"}`; absent means `dsl` applies to history too |
| `dsl` | template for every column that nothing more specific covers |
| `proj_dsl` | template for estimate quarters (and annual-only years when `annual_dsl` is absent) |
| `annual_dsl` | template for annual-only years |
| `fy` | FY columns with quarters: `sum` (default), `avg`, `last`, `first`, `formula` (uses `fy_dsl`, else `dsl`, else `proj_dsl`), `blank` |
| `fy_hist`, `fy_dsl` | the aggregation of actual FY columns when it differs from `fy`; the template for `formula` |
| `values` | `{pid: value}` overrides: a number is typed (blue), a `=...` string containing `{` is expanded, any other string is written as is; `values_only: true` leaves every other period blank |
| `needs` | `py`, `pq` or `py2`: blank when the comparison column does not exist |
| `q_only` | blank in FY columns, except annual-only years when `annual_dsl` exists |
| `start` | pid before which the row is blank |
| `subs`, `sub_labels`, `sub_start` | variance rows (section 4), label overrides by key, start pid by key |
| `driver` | `{"id": driver, "sub": key}`: the sub-row that links the driver's Active row |
| `total`, `base` | denominators of `pct_total` and `pct_of` (default `total_rev`) |
| `bold`, `italic`, `top`, `bottom`, `fill`, `color`, `input_color`, `input_fill` | style; `input_fill` paints numeric estimate cells light yellow (FFFFCC) |
| `notes`, `label_note` | `{pid: text}` comments on cells; a comment on the label |

`_value_for(line, period)` decides each cell in this order; the first rule that applies wins:
1. `needs` unmet, `q_only` in an FY column, or the column before `start`: blank.
2. `values[pid]` present: that value; with `values_only`, every other period is blank.
3. Sub-rows: section 4.
4. Actual quarter: the `hist` value. A data value that is a string starting with `=` is written as a typed formula (blue) unless it contains `{`, in which case it is expanded.
5. Estimate quarter: `proj_dsl`, else `dsl`.
6. Annual-only year: `annual_dsl`, else `proj_dsl`, else `dsl`, else the data value for that FY.
7. FY column with quarters: the aggregation (`fy_hist` for actual years, `fy` for estimate years) over that year's quarter cells of the same row: `=SUM(S38:V38)`, `=AVERAGE(D120:G120)`, `=V15` (`last`), `=D46` (`first`); `formula` expands its template in the FY column (`@py` is then the prior FY); `blank` writes nothing. An actual year whose quarters have no data stays blank instead of summing to zero.

Colour comes from the value (`styles.color_for`): numbers blue, formulas black, formulas containing `!` green; typed data formulas and `{data:}` values are blue. `verify` checks these rules, so never set `color` to override them.

## 4. Variance sub-rows

`SUB_DEFS` defines the rows that can hang under a line; `{id}` in a template is the parent line.

| Key | Label | Template | Format | Needs | Quarters only |
|---|---|---|---|---|---|
| `pct_yoy` | % yoy | `={id}/{id@py}-1` | pct | py | |
| `pct_2y` | % 2y stack | `={id.pct_yoy}+{id.pct_yoy@py}` | pct | py2 | |
| `usd_yoy` | $ yoy | `={id}-{id@py}` | parent's | py | |
| `pct_qoq` | % qoq | `={id}/{id@pq}-1` | pct | pq | yes |
| `usd_qoq` | $ qoq | `={id}-{id@pq}` | parent's | pq | yes |
| `pct_total` | % total | `={id}/{total}` | pct | | |
| `bps_yoy` | bps yoy | `=({id}-{id@py})*10000` | bps | py | |
| `bps_2y` | bps 2y stack | `={id.bps_yoy}+{id.bps_yoy@py}` | bps | py2 | |
| `bps_qoq` | bps qoq | `=({id}-{id@pq})*10000` | bps | pq | yes |
| `net_adds_yoy` | yoy net adds | `={id}-{id@py}` | kpi | py | |
| `net_adds_qoq` | qoq net adds | `={id}-{id@pq}` | kpi | pq | yes |
| `pct_of` | % of Revenue | `={id}/{base}` | pct | | |

A sub may also be a dict `{"key", "label", "dsl", "fmt", "italic", "needs", "q_only"}` for one-off rows (`spec_builder` uses this for `% of Product Revenue`, `GM %`, `inc_ratio`, `Check`). Sub ids are `parent.key`, so other formulas can reference them (`{op_inc.pct_of@py}`).

Defaults by kind (`DEFAULT_SUBS`; `AMT_SUBS`, `COUNT_SUBS`, `PCT_SUBS` in `spec_builder`): amount and price `pct_yoy, pct_2y, usd_yoy, pct_qoq, usd_qoq`; count `net_adds_yoy, pct_yoy, net_adds_qoq, pct_qoq`; pct `bps_yoy, bps_2y, bps_qoq`; `none` nothing. A Variance & Deltas row for a line replaces the default with its flagged keys in the canonical order above (`sub_list`); a row with nothing flagged falls back to the default. Cost lines use `pct_yoy, usd_yoy, pct_qoq, usd_qoq` after their `pct_of` row.

When a sub-row is blank:
- `needs` rows are written only where the comparison column exists on the axis and the parent has a value in this period and in the comparison period(s). So `% yoy` starts in the second year of history (ILMN I39 `=I38/D38-1`, nothing in D-H), `% 2y stack` in the third (N40 `=N39+I39`), and both appear in FY columns (M39 `=M38/H38-1`, W40 `=W39+R39`).
- `q_only` rows (`% qoq`, `$ qoq`, `bps qoq`, `qoq net adds`) are blank in every FY column, except an annual-only year when the sub carries `annual_dsl` (a driver-fed sub, below).
- `pct_total` and `pct_of` are always written.

Driver-fed subs: when `line.driver.sub` equals the key, the sub gets `proj_dsl` and `annual_dsl` of `={drv:id}`, so estimate quarters and annual-only years show a green link to the driver's Active row while FY columns with quarters still compute the variance from the FY levels (ILMN N39 `='Drivers & Casing'!I51`, W39 `=W38/R38-1`, X39 `='Drivers & Casing'!S51`). Formats: the `SUB_DEFS` format, else the parent's `fmt`, else `KIND_FMT[kind]`, so `$ yoy` under a price line uses the price format.

## 5. Delta blocks

A delta item is `{label, line, sub, measure, source, values}` rendered by `SheetBuilder.delta_block` at the bottom of Revenue Build, Margin Build or Income Statement. `spec_builder.delta_items` builds items from the Variance & Deltas tab rows (`sheet`, `line`, `label`, `measure`, `source`, `data_label`, `data_section`, `from`, `to`):

| `measure` | Compared | External values from `data_label` | Delta row |
|---|---|---|---|
| `growth` (default) | the line's `pct_yoy` sub (or `sub`) | `v / prior-year v - 1` for estimate periods where both exist | `∆ to <source> (bps)` = `=(ref-ext)*10000`, format `bps_delta` |
| `margin` | the line's `pct_of` sub (or `sub`) | the series' estimate-period values | the same bps row |
| `level` | the line itself | the series' estimate-period values | `∆ to <source> (%)` = `=ref/ext-1`, format `pct_cons` |

`from` and `to` clip the periods by column. An item may carry `values` directly instead of `data_label`. `DataView.series` checks KPI History labels before the parsed data, which is the route for guidance and buyside numbers: `build_spec` reads the Guidance and Buyside tabs into `inputs` but does not turn them into delta rows, so a row with `source` = `Guidance` or `Buyside` needs a `data_label` that resolves (a KPI History row, for instance) or `values` added to the spec item. The source text only changes labels and ids.

Rendering (ILMN total revenue, rows 83-84): the external row `ext.consensus.total_rev.pct_yoy` is labelled `Consensus Total Revenue % YoY ` for growth or `Consensus Gross Margin % ` for margin and level, bold, kind `none`, typed blue values, `fy: blank` so an FY column shows only a typed value; the delta row `ext.consensus.total_rev.pct_yoy.delta` is `∆ to Consensus (bps)`, bold italic on yellow (FFFF00) with a bottom border, and exists only where the external value exists: K84 `=(K16-K83)*10000`, M84 `=(M16-M83)*10000`.

## 6. Driver types and the formulas they generate

`build_driver_specs` turns each Drivers-tab row into a driver spec: `id` (`clean_id`), `label`, `section` (`revenue`, `cost`, `is`, `bs`, `cf`), `fmt` from Format (`%` -> `pct_plain`, `bps`, `amount` -> `amount_s`, `price`, `shares`, `x` -> `mult`), `cased` (Y/N), `fy` (`sum` default; `avg`, `last`, `first`), `values` from the Driver Grid (`{case: {pid: value}}`, or `{"Active": {...}}` when uncased), `notes`, `single`, and `target` = `{line, sub}` with `sub` from `_default_sub(type)`: `yoy_pct` -> `pct_yoy`, `qoq_pct` -> `pct_qoq`, `net_adds` -> `net_adds_qoq`, `bps_qoq` -> `bps_qoq`, `bps_yoy` -> `bps_yoy`, `pct_of_base` -> `pct_of`, others none; a `gm_pct` driver's target is re-pointed by `build_spec` to the gross-profit line's `pct_of` row (the GM % the analyst is estimating), and a `single` driver's one value is moved to the first Drivers & Casing column. A driver attaches to the line named by its Target line ID (first match wins). The type and custom formula are consumed by the tree builders and stripped, so the spec stores formulas, not types. Drivers from `canon.DEFAULT_DRIVERS` that nothing references are dropped; a target naming a line absent from the model is cleared, and the Active row then shows no realised history.

What each type writes on the line it drives (`level_line` for revenue, KPI and `direct` lines; `cost_line` for COGS and opex lines). `L` is the line, `D` the driver:

| Type | Estimate quarters (`proj_dsl`) | Annual-only years (`annual_dsl`) | Sub-row fed |
|---|---|---|---|
| `yoy_pct` | `={L@py}*(1+{L.pct_yoy})` | same template (`@py` = prior FY) | `pct_yoy` |
| `qoq_pct` | `={L@pq}*(1+{L.pct_qoq})` | `={L@py}*(1+{drv:D})`: the driver is read as y/y; the `% qoq` row shows the link | `pct_qoq` |
| `net_adds` | `={L@pq}+{L.net_adds_qoq}` | `={L@py}+{drv:D}` | `net_adds_qoq` |
| `bps_qoq` | `={L@pq}+{L.bps_qoq}/10000` | `={L@py}+{L.bps_qoq}/10000` | `bps_qoq` |
| `bps_yoy` | `={L@py}+{L.bps_yoy}/10000` | same template | `bps_yoy` |
| `pct_level`, `absolute` | `={drv:D}` | `={drv:D}` | none: the line is the driver |
| `custom` | the `Represented on the build as` text, which must start with `=` | same formula | none |
| `flat` (no driver) | `={L@pq}` | `={L@py}` | none |
| `pct_of_base` (cost) | `={base}*{drv:D}` | same template | `pct_of` |
| `gm_pct` (cost) | `={base}*(1-{drv:D})` | same template | GM % row of the gross-profit line |
| `cost_per_unit` (cost) | `={Revenue Build!volume_id}*{drv:D}*{months}` | same (`{months}` = 12) | none |
| `single` | one constant per case in the first drivers column; reference it as `{drv:D@<first drivers pid>$}` because the Active row is blank elsewhere | | none |

Cost lines set no `annual_dsl`, so annual-only years reuse `proj_dsl` with `@pq` meaning the prior FY; a cost line without history uses its projection formula for history too. A `growth` tree node without a driver gets an implicit `yoy_pct` driver `<id>_g`, a `direct` node an `absolute` driver `<id>_lvl`, a KPI node is carried `flat`. Every COGS and opex row normally has a driver (the stage-1 workbook proposes `gm_pct` for COGS rows and `<id>_pct` of type `pct_of_base` for opex rows); a cost row or KPI without one is carried forward flat (`={id@pq}`), which the review step should call out. Two plug lines keep history footing: `other_cogs` (reported total cost of revenue minus the modelled COGS lines, projected at the prior year's level) and `other_opex` (reported operating income reconciled to gross profit minus the opex lines, zero in estimates); on the income statement `other_nonop_plug` does the same between operating income and reported pre-tax income. Balance-sheet group totals that an export lacks (CapIQ has no non-current subtotals) are derived from the totals it does report before the per-group plugs are computed, and buybacks reduce APIC when the company reports no treasury line. FY columns with quarters never use the driver; they aggregate the line's quarters by its `fy` rule and compute variance rows from those FY levels.

Worked examples, as built:
- `yoy_pct`, cased: `seq_cons_g` drives `seq_cons` (Revenue Build row 38, `% yoy` row 39; Active row 51). 1Q27E: N38 `=I38*(1+N39)`, N39 `='Drivers & Casing'!I51`. FY2027E: R38 `=SUM(N38:Q38)`, R39 `=R38/M38-1`. FY2029E: X38 `=W38*(1+X39)`, X39 `='Drivers & Casing'!S51`. Drivers & Casing: I51 `=SUMIF($B$46:$B$50,$B$5,I46:I50)`; D51 `='Revenue Build'!I39` (realised 1Q26 growth).
- `gm_pct`, cased: `gm_product` drives `cogs_product` (Margin Build row 42, base `m_product` row 14): K42 `=K14*(1-'Drivers & Casing'!F61)`, `% of Product Revenue` K43 `=K42/K14`; Active D61 `='Margin Build'!I43`, F61 `=SUMIF($B$56:$B$60,$B$5,F56:F60)`.
- `pct_of_base`, cased: `sga_pct` drives `sga` (row 102, base `m_total_rev` row 20): K102 `=K20*'Drivers & Casing'!F77`, K103 `=K102/K20`; FY2029E X102 `=X20*'Drivers & Casing'!S77`.
- `pct_level`, uncased: `tax_rate` on the Income Statement (row 50): history D50 `=D48/D46`; K50 `='Drivers & Casing'!F99`; FY M50 `=M48/M46`; `tax` K48 `=K46*K50`. Drivers row 99: F99 typed 0.21, H99 `=G99` (`fy: last`), D99 `='Income Statement'!I50`.
- `absolute`, uncased: `dep` (Income Statement row 56): K56 `='Drivers & Casing'!F102`; Drivers row 102: H102 `=SUM(D102:G102)`, S102 `=R102` (annual carry of the FY2028 total).
- `bps_qoq`, cased (Spotify): `ab_pct_bps` drives `ab_pct` (row 55, `bps qoq` row 58; Active row 35): 3Q26E U55 `=T55+U58/10000`, U58 `='Drivers & Casing'!F35`; FY2026E W55 `=V55` (`fy: last`); FY2029E AH55 `=AG55+AH58/10000`, AH58 `='Drivers & Casing'!S35`.
- `net_adds` and `qoq_pct` (pattern, ILMN columns): a count line on row r with its driver-fed sub on row s and Active row a gives 1Q27E `=L<r>+N<s>` or `=L<r>*(1+N<s>)` with N<s> linking the driver, and FY2029E `=W<r>+'Drivers & Casing'!S<a>` or `=W<r>*(1+'Drivers & Casing'!S<a>)`.
- `single` (Spotify): `peak_px` occupies column D only (rows 62-66 typed per case, D67 `=SUMIF($B$62:$B$66,$B$5,D62:D66)`, light-yellow fill); `ab_rpu` at 4Q27E uses `={drv:peak_px@1Q26$}` -> `='Drivers & Casing'!$D$67`.
- `custom` (Spotify): `ab_rpu` `={ab_rpu@pq}+({ab_rpu@4Q27$}-{ab_rpu@2Q26$})/6` -> U60 `=T60+($AA$60-$T$60)/6`; `ad_rev` `={ad_arpu}*AVERAGE({ad_mau@pq},{ad_mau})*{months}` -> U88 `=U102*AVERAGE(T96,U96)*3`, with `annual_dsl` `={ad_arpu}*{ad_mau}*{months}` -> AH88 `=AH102*AH96*12`.

## 7. Revenue-tree kinds (`build_revenue_blocks`)

Nodes come from the Revenue Tree tab (`id`, `label`, `parent`, `kind`, `volume_id`, `price_id`, `price_basis`, `data_label`, `data_section`, `format`, `fy_rule`, `hist_formula`); ids are cleaned to `[a-z0-9_]`. A node's history is the actual quarters of `data_label` (FY totals are rebuilt from quarters, never read). The sheet opens with `Totals:` and `total_rev` = the sum of the top-level non-KPI roots, then a grey band `<Label>:` per root and its subtree in order.

| Kind | Formula | Notes |
|---|---|---|
| `sum` | `={child}+{child}+...` over non-KPI children | with history: `hist` plus `proj_dsl`, so actuals stay reported and the sum applies to estimates |
| `volume_price` | `={volume_id}*{price_id}`, plus `*{months}` when `price_basis` starts with `per m` | no history, so the formula is used everywhere |
| `growth` | `level_line` with the node's driver (default `yoy_pct`) | |
| `share` | `={parent}*{id.pct_total}` | `pct_total` relabelled `% of <parent label>` and placed last; `total` = parent; the driver feeds `pct_total` |
| `direct` | `level_line` with the driver (default `absolute`) | |
| `custom` | the node's `formula` as `proj_dsl` | |
| `kpi` | `level_line`; `format` sets the kind: `count` (default), `price`, `%`/`pct`, `amount` | `fy` by kind: count and price `avg`, pct `last`, amount `sum`, overridable by `fy_rule`; `hist_formula` makes history a formula (and `fy_dsl` when `fy_rule` is `formula`); pct KPIs italic, others bold |
| anything else | `={id@pq}` | |

Top-level revenue lines get `pct_total` appended to their variance rows. KPI nodes are not revenue: they are excluded from `total_rev` and from parents' sums, and are what `volume_price`, `share` and custom formulas refer to.

## 8. Cost blocks (`build_cost_blocks`, Margin Build)

Revenue links first: `m_<id>` for every top-level revenue line and `m_total_rev`, green links to Revenue Build with a `% yoy` row.

Cost of Revenue: one line per Cost Tree row whose Section starts with `cogs`, in a band named after its `segment`. The base is `m_<segment>` when the segment is a top-level revenue line, else `m_total_rev`; the first sub is `pct_of` (`% of <base label>`). Where reported total cost of revenue differs from the sum of the modelled COGS lines by more than 0.01, `other_cogs` (`Other Cost of Revenue (amortization, other items)`) carries the difference, history typed and projections `={other_cogs@py}`. With more than one COGS id (the plug counts) the sheet also gets `total_cogs` and `total_gp` (`GM %`); with one, `total_cogs` is that line and gross profit is its `gp` line. The gross-profit id is the cost id with `cogs` replaced by `gp`, else `<id>_gp`.

Incremental-margin block (Setup `incremental_blocks`, default Y), four rows per COGS line with `needs: py` and `fy: formula`: `<gp>_chg` (`y/y $ change in <base> gross profit`), `<base>_chg`, `<cogs>_inc` (`Incremental <base> COGS`) and `<gp>_inc_gm` (`Incremental <Base> Gross Margin`, kind `pct`, subs `bps y/y` and `bps q/q`; ILMN K55 `=K49/K51`). Then the gross-profit line `<gp>` = base minus cost with `<Base> GM %`.

Operating expenses: a bold subtitle `<Label>:` then the line (base `m_total_rev`, `% of Revenue` first). SBC split (Setup `sbc_split` not `no` and the row's `sbc_data_label` has history): `sbc_<id>` projected as `={total_sbc}*{sbc_<id>@py}/{total_sbc@py}` (last year's share of total SBC) and `<id>_ex` = line minus SBC with `ex-SBC % of Revenue`, `ex-SBC % yoy`, `ex-SBC $ yoy`. `other_opex` (`Other Operating Expenses (plug for actuals)`) appears when revenue minus total COGS minus modelled opex differs from reported operating income: history typed, estimate quarters typed `0` on light yellow (blue, for the analyst to overwrite), annual-only years `={other_opex@py}`. `total_opex` sums the opex ids (plug included) with `% of Revenue`, the amount subs and `inc_ratio` (`Incremental Opex/Incremental Revenue (y/y)` = `=({id}-{id@py})/({m_total_rev}-{m_total_rev@py})`); `total_opex_ex` follows when SBC is split. `total_sbc` holds reported SBC and projects `={drv:sbc}`, with the sub `cor` (`SBC - Cost of Revenue (implied)`, total minus the split lines) when a split exists.

Operating Income: `op_inc` history is the reported figure, projections `={total_gp}-{total_opex}`. Subs: `% margin`, `bps y/y` (`=({id.pct_of}-{id.pct_of@py})*10000`), `pct_yoy`, `usd_yoy`, `Incremental Operating Margin (y/y)` and `(q/q)` (quarters only), and `Check` = `=ROUND(gp - total_opex - op_inc, 6)` (ILMN K139 `=ROUND(K33-K121-K132,6)`). The Check must be 0 in every column: in history it proves the plugs reconcile the build to reported operating income, in estimates it is 0 by construction. `verify` reads every row whose label is `check` or `Check` on any sheet and reports non-zero values as failures. Margin Build delta items come last.

## 9. Condensed statements (`build_statement_blocks`, `canon.py`)

`canon.IS_LINES`, `BS_LINES` and `CFS_LINES` list the condensed line sets with Bloomberg and CapIQ synonyms (matched case- and punctuation-insensitively, optionally within a data section) and a role. A Statement Mapping row can point a line at another `data_label` or drop it (`keep` = N). Lines without history are dropped except where noted; `fmt` is `amount_s`.

Income Statement (`fy: sum` unless stated): `is_<root>` per top-level revenue line (history typed, projections link Revenue Build); `total_rev` = their sum with `% YoY Growth`; `cogs` (history; projections link Margin Build `total_cogs` or the single COGS line); `gp`; `is_<opex>` per Margin Build opex id (`other_opex` included); `total_opex_is`; `op_inc_is` = gp minus opex. Below operating income: `interest_income` and `interest_expense` (always present), `other_nonop` (when in the data), projected `={drv:<id>}` when the driver exists else `={<id>@py}`; `nonop_net`; `pretax`; `tax` = `={pretax}*{tax_rate}`; `tax_rate` (kind `pct`, history `={tax}/{pretax}`, projections `{drv:tax_rate}`, FY columns `={tax}/{pretax}`); `nci` when reported (`={nci@py}`); `ni` = pretax minus tax (minus nci). Memo: `dep` and `amort` when either has history or no D&A total exists, else `da`, each from its driver; `ebitda` = `op_inc_is` plus D&A; `sbc`; `ebitda_ex` = ebitda plus sbc. Non-GAAP block (Setup `adjusted_block` = `yes`, or `auto` with adjusted operating income or adjusted EPS in the data): `adj_sbc` = sbc, `adj_amort` = amort, `adj_other` (history = adjusted OI minus OI, SBC and amortisation; projections `{drv:adj_other}`), `adj_oi`, `adj_pretax` = adj_oi plus nonop_net, `adj_tax` = adj_pretax x `adj_tax_rate` (history = 1 minus adjusted NI / (adjusted OI plus non-operating); projections `{drv:adj_tax_rate}`), `adj_ni`, `adj_ebitda` = adj_oi plus `dep` (or `da`). The Tearsheet metric defaults to `adj_ebitda` when the block exists, else `ebitda`. Per share: `shares_basic`, `shares_dil` (`fy: avg`, from drivers); `eps_basic` = ni / shares, `eps_dil`, `adj_eps` = adj_ni / shares_dil, history typed where reported, FY columns recomputed through `fy_dsl`.

Balance Sheet (`fy: last`; totals `fy: formula`): lines are grouped `ca`, `nca`, `cl`, `ncl`, `eq`. Where a reported subtotal (`BS_TOTALS`) differs from the mapped lines by more than 0.01, a plug (`other_ca`, `other_nca_plug`, `other_cl_plug`, `other_ncl_plug`, `other_eq_plug`) holds the difference and is carried flat. Roll-forwards by role:

| Role | Lines | Projection |
|---|---|---|
| `cash` | cash | `={Cash Flow Statement!end_cash}` |
| `pct_rev`, `pct_cogs`, `pct_costs` | receivables, prepaid, deferred_rev; inventory; payables, accrued | `={drv:<x>_pct}*<base>*13/{weeks}` with base `{Income Statement!total_rev}`, `{Income Statement!cogs}` or `({Income Statement!cogs}+{Income Statement!total_opex_is})` (`WC_DRIVER_FOR`) |
| `ppe` | ppe | `={ppe@pq}-{Cash Flow Statement!capex}-{Income Statement!dep}` (capex is negative on the CFS; `da` when there is no `dep`) |
| `intangibles` | intangibles | `={intangibles@pq}-{Income Statement!amort}` when an `amort` line exists |
| `debt` | lt_debt | prior `+{Cash Flow Statement!debt_change}` `+{Cash Flow Statement!debt_repaid}` for the CFS lines present |
| `apic` | apic | prior `+{Income Statement!sbc}` `+stock_issued` `+rsu_tax` |
| `treasury` | treasury | prior `+{Cash Flow Statement!buybacks}` |
| `retained` | retained | prior `+{Income Statement!ni}` `+dividends` |
| `flat`, `plug` | everything else | `={<id>@pq}` |

The `*13/{weeks}` factor states the driver as a ratio to a 13-week quarter's flow, so a 14-week quarter and the 52-week annual-only columns (ratio x annual flow x 13/52) give the same balance. Totals: `total_ca`, `total_nca` (`=SUM(first:last)` of the group), `total_assets`, `total_cl`, `total_ncl`, `total_liab`, `total_equity`, `total_le`, and `bs_check` = total_assets minus total_le.

Cash Flow Statement (`fy: sum`): `cf_ni`, `cf_da`, `cf_sbc` link the Income Statement in every column. Working-capital lines (role `wc:<bs line>`): history typed; projections `=-({Balance Sheet!x}-{Balance Sheet!x@pq})` for asset lines and `=({...}-{...@pq})` for liabilities (an asset increase consumes cash); when the balance-sheet line is missing, typed `0` inputs instead. `investments` = `-(` the changes in `st_inv` and `lt_inv` `)`. Driver lines (`capex`, `debt_change`, `buybacks`, `dividends`, `stock_issued`, `rsu_tax`) take `={drv:<id>}`. `zero` lines (`cf_deftax`, `wc_other`, `acquisitions`, `debt_repaid`) and plugs are typed `0` in estimate quarters (blue on light yellow) and `={<id>@py}` in annual-only years. Plugs so history foots: `other_op` = reported CFO minus (NI, D&A, SBC and the other operating lines); `other_inv` and `other_fin` = reported subtotal minus lines; `fx` = reported net change minus (CFO + CFI + CFF). Totals: `cfo`, `cfi`, `fcf` = cfo + capex, `cff`, `net_change` = cfo + cfi + cff (+ fx). `beg_cash`: the first history quarter is typed `={data:beg_cash}` (balance-sheet cash minus that quarter's net change, else reported BOP), later quarters `={end_cash@pq}`, FY columns `fy: first`, annual-only years `={end_cash@py}`; `end_cash` = net_change + beg_cash (`fy: formula`); `cash_check` = end_cash minus `{Balance Sheet!cash}`.

## 10. Drivers & Casing Active rows (`sheets/drivers.py`)

The sheet uses the drivers axis (section 1). B5 holds the active case with a list validation over `cases`; every other sheet's B5 is `='Drivers & Casing'!B5`. Sections in order: `Revenue Drivers`, `Cost Drivers`, `Income Statement Drivers`, `Balance Sheet Drivers`, `Cash Flow Drivers` (by driver `section`). Each driver is a block with a bold title row (`label_note` becomes its comment), then:

- Cased: one row per case (ids `drv:<id>:<Case>`, typed blue in estimate quarters and annual-only years, FY columns with quarters blank), then the bold `Active` row (`drv:<id>`, top border). Estimate columns: `=SUMIF($B$46:$B$50,$B$5,F46:F50)` (the case labels against B5, same column), which is how one cell flips the whole model. Actual quarters: a green link to the realised value of the target, `={target.line}` or `={target.line.sub}` (ILMN D51 `='Revenue Build'!I39`); no target, nothing. `hist_values` in the spec pre-fill actual periods. `single` drivers occupy only the first drivers column (one constant per case on light yellow; Active `=SUMIF($B$62:$B$66,$B$5,D62:D66)`).
- Uncased: only the `Active` row. Estimate quarters typed (blue) from the grid; actual quarters link the target (`='Income Statement'!I50`) or show a typed value; FY columns with quarters aggregate the row by the driver's `fy`: `=SUM(D102:G102)`, `=AVERAGE(D120:G120)`, `=G99` (`last`), the first quarter for `first`. Annual-only years: the typed value if given, else the spec's `annual_dsl` (Spotify `shares_basic`: `={drv:shares_basic@py}+({drv:shares_basic@4Q28$}-{drv:shares_basic@4Q27$})` -> `=R132+($Q$132-$L$132)`), else a carry of the prior year's column (`=R102`, the FY2028 aggregate, so a `sum` driver carries a full-year total and a `last` driver carries the rate).

`ctx.drv_rows[id]` records the Active row and every `{drv:id}` token resolves to it. Because the axis starts at the last actual fiscal year, a `{drv:}` reference in an earlier column is blank.

## 11. DCF (`sheets/dcf.py`)

Annual columns only: one per FY column of the model axis (history years included), from D; rows start at 11 under `Discounted Cash Flow`. Every row is `fy: formula` and links the FY columns of the statements (green):

| Row id | Label | Formula |
|---|---|---|
| `dcf_rev`, `dcf_growth` | Revenue, % Growth Rate | `{Income Statement!total_rev}` and its `.pct_yoy` (`needs: py`) |
| `dcf_cogs`, `dcf_gp`, `dcf_gm` | (-) Cost of Revenue, Gross Profit, % Margin | link; rev minus cogs; gp / rev |
| `dcf_opex0..n` | (-) <opex label> | one per `opex_lines` (the Income Statement opex ids) |
| `dcf_ebit`, `dcf_ebit_m` | EBIT, % Margin | gp minus the opex rows |
| `dcf_da`, `dcf_da_pct`, `dcf_ebitda`, `dcf_ebitda_m` | (+) D&A, EBITDA | the sum of `da_lines`; EBIT plus D&A |
| `dcf_tax_rate` | % Tax Rate | history `{Income Statement!tax_rate}`; estimates `=$D$41` (the WACC-block input) |
| `dcf_taxes`, `dcf_nopat`, `dcf_da2` | (-) Taxes, NOPAT, (+) D&A | EBIT x rate; EBIT minus taxes; `={dcf_da}` |
| `dcf_nwc`, `dcf_nwc_pct` | (+/-) ∆NWC, % of Revenue | the sum of the CFS working-capital lines (`nwc_lines`) |
| `dcf_capex`, `dcf_capex_pct` | (+/-) CapEx, % of Revenue | `{Cash Flow Statement!capex}` (negative) |
| `dcf_ufcf` | UFCF | NOPAT + D&A + ∆NWC + CapEx |
| `dcf_dp` | Discount Period | estimate years only: first `=(DATE(2027,1,3)-$D$40)/2/365` (half the stub to that year end), second `=(DATE(2028,1,2)-182.5-$D$40)/365`, then the previous cell `+1` |
| `dcf_df`, `dcf_pv` | Discount Factor, PV of UFCFs | `=1/(1+$D$48)^E34`; `=E33*E35` |

WACC block (column D, blue inputs from DCF Inputs; ILMN rows 40-48): Valuation date, Tax Rate, Rfr, Beta, ERP, Ke `=D42+D43*D44`, After-Tax Kd, Equity Weight, WACC `=D47*D45+(1-D47)*D46`. Terminal Value: a case table in F/G (exit multiples typed per case, blue on light yellow; `Active` `=SUMIF($F$50:$F$54,$B$5,G50:G54)`), `Exit EV/EBITDA` = the active cell, `FY2030E EBITDA` = the last column of `dcf_ebitda`, `TV` = their product, `PV of TV` `=D54/(1+D48)^((DATE(2030,12,29)-D40)/365)`. Equity Value: `PV of UFCF` `=SUM(E36:I36)` over estimate years, plus `PV of TV` = Enterprise Value; `(+) Cash & Investments` = `bridge.cash_lines` at the last actual quarter's Balance Sheet column (`='Balance Sheet'!J15+'Balance Sheet'!J16`); `(-) Debt & Lease Liabilities` = `=-(...)` of `bridge.debt_lines`; optional `bridge.other_adjustments` rows (`label`, `value`); Equity Value; when the trading currency differs from the reporting currency, an FX row (`company.fx_rate`, blue) and the converted equity value; `Diluted Shares (mm)` (input); `Implied Share Price` = equity / shares; `Current Share Price` `='Tearsheet'!D39`; Upside = implied / current minus 1. `ctx.dcf_cells` hands these cells to the Tearsheet.

## 12. Tearsheet (`sheets/tearsheet.py`, `cases.py`)

Fixed cells: `Current Px` D39 `=IFERROR(BDP("<ticker_code>","PX_LAST"),F39)` for `price.source` bloomberg (`CIQ(...,"IQ_LASTSALEPRICE")` for capiq, `FDS(...,"P_PRICE")` for factset, the typed value otherwise), F39 the typed fallback price, G39 its date. Bridge (rows 41-45): Equity Value `=D39/E42*DCF!D65` (price in reporting currency x diluted shares), E42 the FX rate (`=DCF!<fx>` or a typed 1), `(-) Cash & Investments` `=DCF!D62`, `(+) Debt & Lease Liabilities` `=-DCF!D63`, Enterprise Value `=E41+E44-E43`; E47 the metric for `current_multiple_period` in the active case (`='Income Statement'!R87`), E49 the current multiple `=E45/E47`. Multiples grid (from row 51): one column per target block, one row per case ranked Blowout, Bull, Base, Bear, Disaster, typed blue on light yellow.

Per-block case columns (block 1 in C-F with values in E, block 2 in H-K with values in J; cases in the order Base, Bull, Bear, Blowout, Disaster, seven rows each from row 4): `<metric_label> (<FYxxE>)` = `='Income Statement'!W87` (green) or, once `cases` has run, the typed case value (blue); `(x) <multiple_label>` = a link to the grid; `Px Tgt` `=(E5*E6+$E$43-$E$44)/DCF!$D$65*$E$42`, that is (metric x multiple + cash - debt) / diluted shares x FX; `% upside/(downside)` = px / $D$39 - 1; `% IRR` `=(E7/$D$39)^(1/YEARFRAC(DCF!D40,DATE(2027,12,31)))-1` from the valuation date to the block's `target_date`.

Blended block per target (M3 and M15): weights in N (block 1 typed, block 2 `=N<row-12>`), Mult, metric and Px links, `%` upside; `Blended Px Tgt - <blended_label>` `=SUMPRODUCT(N5:N9,Q5:Q9)`, its upside and IRR, and `R/R` `=AVERAGE(R5:R7)/R9*-1`: the average upside of the best ceil(n/2) cases over the worst case's downside (Bull and Base over Bear with three cases). With two blocks, `Blended R/R` averages the two.

Why `cases` exists: the statements compute one case at a time, so each case's metric is snapshotted. `fmb_cli.py cases <model.xlsx> <spec.json>` sets B5 to each case in Excel, recalculates, reads the Income Statement metric row at each block's `metric_period` column, writes the values into the metric cells (bold blue) and restores the case; `tearsheet.case_metric_values` in the spec pre-seeds the same cells.

Sensitivity grids start at column T beside each blended block: header `Case`, `EBITDA` (`metric_short`), then the multiple sequence (blue, the Base multiple on grey); one row per case with the metric link and `=($U5*V$4+$E$43-$E$44)/DCF!$D$65*$E$42`; below, `% Upside - <label>` rows `=V5/$D$39-1`. `sensitivity_multiples(low, base, high)` takes the lowest and highest case multiples and tries steps 5, 2.5, 2, 1, 0.5, 0.25, 0.1, 0.05 until both distances from the base are whole steps and the count is at most `sensitivity_max_cols` (25), so the base multiple always sits on the grid (ILMN 14 to 26 by 2); otherwise seven equal steps.

## 13. Number formats (`styles.NUMBER_FORMATS`)

| Name | Format | Used by |
|---|---|---|
| `amount` | `#,##0;\(#,##0\)` | build amounts |
| `pct` | `0.0%;\(0.0%\);\-\%` | build variance and margin rows |
| `pct_plain` | `0.0%` | driver percentages, tearsheet upside |
| `bps`, `bps_delta` | `0"bps";\(0"bps"\)`, `#,##0" bps";\(#,##0\)" bps";\-` | bps rows, delta rows |
| `pct_cons` | `0.0%;\(0.0%\);\-` | external consensus rows |
| `kpi` | `0.0;\(0.0\)` | counts and net adds |
| `price` | `\$0.00;\(\$0.00\)` (symbol from the reporting currency) | per-unit prices |
| `amount_s`, `pct_s`, `shares`, `eps` | `#,##0_);(#,##0)`, `0.0%_);\(0.0%\)`, `#,##0.00_);(#,##0.00)`, `0.00_);\(0.00\)` | statements and drivers |
| `amount_d`, `pct_d`, `mult`, `number1`, `number2`, `number4` | `#,##0;\(#,##0\);"-"`, `0.0%;\(0.0%\);"-"`, `0.0\x`, `0.0`, `0.00`, `0.0000` | DCF and Tearsheet |
| `px`, `px_acct`, `weight`, `date`, `int` | `"$"#,##0.00` (trading currency), the accounting variant, `0%`, `mm-dd-yy`, `0` | Tearsheet price and weights, headers |

## Annual history columns

`horizon.annual_hist_years` (Setup `annual_hist_years`) adds one fiscal-year column per listed year before the first quarterly year: `Period(kind="FY", annual_only=True, estimate=False)`, labelled `FY2021`, grey like the other FY columns, placed first on the axis (columns D onward), with the quarterly history starting after them. Rules:

- Values come from the data, not from quarters: `hist_only()` keeps actual quarters and these annual columns; `DataView.series()` overlays the annual export's values (`source == "capiq"`: the named annual label, else the same label, else a canon synonym, read from the statement's preferred sections first and never from pension, segment, capital-structure, ratio or multiples sheets) on top of the Bloomberg series for those pids, so CapIQ wins where it has the line and the Bloomberg annual printout fills the rest.
- `SheetBuilder._value_for()` types `hist` values in these columns and uses the line's `dsl` for computed lines; a formula whose same-sheet references are all blank in the column stays blank (`_refs_all_blank`), and a ratio row whose parent is blank stays blank, so partial annual detail (segments that only Bloomberg's FY2023+ printout has) does not produce zeros or `#DIV/0!`.
- Totals whose children have no data in a column (Revenue Build `total_rev`, Margin Build `total_cogs`, Income Statement `total_rev`) are typed from the annual export for that column (`values`), so the statements foot even where the segment detail is missing.
- Plug lines (`other_opex`, `other_nonop_plug`, balance-sheet group plugs, cash-flow plugs) are computed for these columns from the same annual sources, so the checks tie; `beg_cash` is seeded in the first annual column from cash less the net change in cash.
- Variance rows work across annual columns (`@py` is the previous annual column; the first one has none). The drivers sheet, the Driver Grid, the DCF's estimate years and the Tearsheet are unaffected; the DCF's annual axis shows the extra history years on the left.
- Weeks in period for an annual column come from the gap to the previous annual column's end (52 or 53), else 52.

