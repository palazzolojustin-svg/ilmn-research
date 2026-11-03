# Inputs workbook

`<TICKER>_model_inputs.xlsx` is the analyst's interface to the build and the durable record of the model design. `scripts/fmb/inputs_workbook.py` writes it in two stages (`write_stage1`, `write_stage2`), pre-fills it from the parsed data (`propose_inputs`) and reads it back (`read_inputs`); `fmb/spec_builder.build_spec()` turns the dict that `read_inputs` returns into the engine spec. Everything below is what that code does. Where a column is read but not used by the build, this file says so, because a value typed there will not appear in the model.

Commands (each option is one argument with `=`; `--out model.xlsx` with a space is silently ignored and the default name is used):

    python "${CLAUDE_SKILL_DIR}/scripts/fmb_cli.py" inputs1 model_data_raw.json --out=ILMN_model_inputs.xlsx "--set=author:Palazzolo, Justin J"
    python "${CLAUDE_SKILL_DIR}/scripts/fmb_cli.py" inputs2 ILMN_model_inputs.xlsx model_data_raw.json
    python "${CLAUDE_SKILL_DIR}/scripts/fmb_cli.py" spec ILMN_model_inputs.xlsx model_data_raw.json --out=model_spec.json --data-out=model_data.json

`--set=key:value` (or `--set=key=value`) overrides a Setup key before stage 1. A value that itself contains `:` cannot be passed this way, and every `--set` value arrives as text (`current_price` is not cast to a number); write such values with openpyxl instead (section 14).

## Contents

1. Flow: stage 1, stage 2, spec, refresh
2. Conventions shared by every tab
3. Setup
4. Data Files
5. Revenue Tree
6. Cost Tree
7. Drivers
8. Variance & Deltas
9. Side Builds, Guidance, Buyside, KPI History
10. Statement Mapping
11. Driver Grid
12. Multiples
13. DCF Inputs
14. Filling the workbook with openpyxl
15. Limits to remember

## 1. Flow: stage 1, stage 2, spec, refresh

- `inputs1`: `propose_inputs(data, overrides, files)` builds a proposal from `model_data_raw.json`, then `write_stage1` writes eleven tabs: Setup, Data Files, Revenue Tree, Cost Tree, Drivers, Variance & Deltas, Side Builds, Guidance, Buyside, KPI History, Statement Mapping. The analyst (or you, on their instructions) edits them.
- `inputs2`: `read_inputs` -> `build_spec` (for the period axis and the statement lines) -> `write_stage2`, which deletes any existing Driver Grid, Multiples and DCF Inputs tabs and writes fresh ones from the current Drivers tab and Setup. Grey history columns are filled from `model_data` for drivers whose target is a level line with history; drivers feeding a sub-row (`pct_yoy`, `pct_of` ...) show blank grey cells.
- `spec`: `read_inputs` -> `build_spec` -> `model_spec.json` and `model_data.json`. Run it after every edit. A wrong line id in a delta row or a formula does not fail here; it surfaces at `build` as `line 'x' not found` or `driver 'x' not found`.
- Refresh or roll-forward: the stage-1 tabs survive `inputs2` untouched, but the three stage-2 tabs are rebuilt empty: every grid estimate, note, multiple, weight and DCF input is lost. Before re-running `inputs2` on a workbook that already holds estimates, copy it; afterwards transplant the old values and notes by (driver id, case, period id) into the new grid with openpyxl, re-type the Multiples and DCF Inputs cells, and only then let the analyst fill the new periods.

## 2. Conventions shared by every tab

- Row 1 holds the tab's help text (grey italics), row 3 the white-on-navy headers (`003765`), data starts in row 4 and panes freeze under the header. Yellow fill `FFFFCC` marks a cell that is read as an input; grey fill `F2F2F2` marks realised history that is never read.
- Dropdowns are list validations that `read_inputs` does not enforce: an unlisted value passes through (a misspelt driver type silently becomes a `flat` line), so write the option strings exactly as listed here.
- `read_inputs` opens the file with `load_workbook(path)` and no `data_only`: a formula cell returns its formula text, never its value. Only the Driver Grid and the DCF Inputs value column forward formula text to the model; Multiples, weights, exit multiples and KPI History take numbers only, and a formula there counts as empty.
- Text is stripped, blank rows are skipped, and a row is read whenever its key cell is non-empty, even far below the yellow area. Line and driver ids go through `clean_id`: lower-case, every run of non-alphanumerics becomes `_` (`Service & Other` -> `service_other`).
- Dates: a Setup cell holding an Excel date is read as `YYYY-MM-DDTHH:MM:SS`, which the Tearsheet cannot parse (`price_date` must be text `YYYY-MM-DD`). DCF Inputs and the Multiples block table convert Excel dates correctly.

## 3. Setup

Columns: A key (hidden column), B field, C value (yellow), D help. `read_inputs` returns `setup[key] = C`. `propose_inputs` fills `ticker` (first word of the data ticker), `ticker_code`, both currencies, `fiscal_year_end_month`, `last_actual_quarter`, `last_quarterly_estimate`, `first_hist_quarter` (1Q of the third year before the last actual year, floored at the data's first quarter) and `annual_only_years` (the two years after the last estimate year). Everything else keeps the default until the analyst answers.

| Key | Value / dropdown | Use in the build |
|---|---|---|
| `company_name`, `ticker`, `exchange` | text | `company.name`, `company.ticker`, `company.exchange` for the title rows |
| `ticker_code` | `ILMN US Equity` / `ILMN` / `ILMN-US` | the code inside the live price formula |
| `price_source` | `Bloomberg` `CapIQ` `FactSet` `Hardcode` | Tearsheet D39: `=IFERROR(BDP("code","PX_LAST"),F39)`, `CIQ(code,"IQ_LASTSALEPRICE")` or `FDS(code,"P_PRICE")`; Hardcode writes the typed price only |
| `current_price`, `price_date` | number; text `YYYY-MM-DD` | fallback price in F39 and its date in G39 |
| `reporting_currency`, `trading_currency`, `fx_rate` | ISO codes from the list; number | currency symbols of the price formats and the equity bridge; `fx_rate` is cast to float |
| `units` | `mm` `000s` `bn` | `company.units` |
| `fiscal_year_end_month` | 1-12 | fiscal calendar for period ends; cast to int |
| `first_hist_quarter`, `last_actual_quarter`, `last_quarterly_estimate` | period ids `1Q23`, `2Q26`, `4Q28` | the column axis; a blank falls back to the data's first quarter, last actual and last estimate |
| `annual_only_years` | `2029, 2030` | every 4-digit number in the text becomes an annual column after the last quarterly year |
| `case_set` | `Bear/Base/Bull` or `Disaster/Bear/Base/Bull/Blowout` | three cases only for the exact first string (or text starting with `3`); anything else gives five |
| `comments_policy` | `From this workbook` or `I will add my own` | text starting with `I will` strips every note read from the grid, Multiples and DCF Inputs |
| `author` | name | workbook creator and lastModifiedBy, and the author of every note (`Analyst` when blank) |
| `cover_tab` | sheet name | the empty cover sheet (default `Cover`) |
| `model_file` | text | not read by any command; `build --out=` names the file |
| `valuation_metric` | list | not read by the code; the Tearsheet metric is `adj_ebitda` when the Non-GAAP block exists, else `ebitda` |
| `adjusted_block` | `Auto` `Yes` `No` | Non-GAAP reconciliation: Yes always, No never, Auto when Adjusted Operating Income or Adjusted Diluted EPS has history |
| `incremental_blocks` | `Y` `N` | incremental gross-margin rows on the Margin Build |
| `sbc_split` | `Auto` `Yes` `No` | anything but No allows `SBC - <opex>` and `<opex> ex-SBC` rows for cost rows that name an SBC data label |

## 4. Data Files

Columns: Path, Type (dropdown: `Bloomberg consensus`, `CapIQ Income Statement`, `CapIQ Balance Sheet`, `CapIQ Cash Flow`, `CapIQ Key Stats`, `KPI history`, `Guidance`, `Buyside`, `Other`), Notes. Pre-filled with the file names recorded in the data JSON (`.md` files typed as Bloomberg consensus). Read into `files`; nothing downstream uses it. It is the analyst's record of what `parse` consumed; the numbers always come from `parse`.

## 5. Revenue Tree

One row per revenue line or KPI; the order is the order on the Revenue Build, with children directly after their parent. Reading stops at the bold marker row `Other revenue lines in the data (candidates):` that follows the 20 spare rows, so new rows go in the spare rows (or move the candidate block down first).

| Col | Header | Read as | Meaning |
|---|---|---|---|
| A | ID | `id` (clean_id) | model line id; also the driver target and delta-row id |
| B | Label | `label` | row label on the build |
| C | Parent ID | `parent` | blank = top level; top-level non-KPI rows get a `<Label>:` band, a `% total` row, and add up to `total_rev` |
| D | Kind | `kind`, blank = `sum` | see below |
| E, F | Volume line ID, Price line ID | `volume_id`, `price_id` | `volume_price` only: ids of two KPI rows |
| G | Price basis | `per month` / `per period` | `per month` (the default) multiplies by `{months}` |
| H | Data label (history) | `data_label` | label of the history series (case- and punctuation-insensitive match against the data, exact match against KPI History) |
| I | Data section | `data_section` | optional section filter, e.g. `Business Breakdown`, `Highlights`, `GAAP Results` |
| J | Format (KPI) | `format` | `count` `price` `pct` `amount` (KPI rows; default count) |
| K | FY rule (KPI) | `fy_rule` | `sum` `avg` `last` `first` `formula`; defaults: count and price avg, pct last, amount sum |
| L | History formula | `hist_formula` | KPI rows: engine formula that replaces data for history, e.g. `={seq_cons}/{seq_units}` |
| M | Notes | `notes` | analyst's record; not used |

Kinds and the projection each produces (`references/model-logic.md` has the full formulas):
- `sum`: `=child+child` over the non-KPI children; with a data label the sum is projection only and history comes from the data.
- `growth`: level = prior year x (1 + driver). A driver row must target the line (the proposal names it `<id>_g`, type `yoy_pct`); the driver type decides the formula. Without a driver row the build stops with `driver '<id>_g' not found`.
- `share`: `={parent}*{id.pct_total}` (blank parent = `total_rev`); the driver that targets the line feeds the `% of <Parent>` row whatever its type (use `pct_level`, format `%`). A driver row is required.
- `direct`: a level typed as a driver (`absolute`); the driver row that targets it supplies the values.
- `volume_price`: `={volume}*{price}`, times `{months}` per month.
- `kpi`: a count, price, % or amount line that is not revenue and can feed other rows; with no driver it carries the prior period forward.
- `custom`: the engine expects a `formula` key that the workbook does not carry, so the line projects `=0`. Use `direct` plus a `custom` driver instead.

Proposal: every non-percentage line of the data's `Segment Revenue` section becomes a top-level `growth` row (id = slugged label, data section = that section) with a `<id>_g` driver and a consensus delta row. Bloomberg puts non-revenue lines in that section (Adjusted Operating Income, Cash & Cash Equivalents ...): delete those rows together with their drivers and delta rows. Non-percentage `Business Breakdown` labels not already used are listed under the marker as candidates.

## 6. Cost Tree

| Col | Header | Read as | Meaning |
|---|---|---|---|
| A, B | ID, Label | `id`, `label` | Margin Build line; an id containing `cogs` gives a gross-profit id with `cogs` -> `gp` (`cogs_product` -> `gp_product`, `cogs_total` -> `gp_total`), any other id gives `<id>_gp` |
| C | Section | `COGS` / `Opex` / `Other` | COGS rows sit under Cost of Revenue, Opex rows under Operating Expenses; `Other` rows are read but never rendered |
| D | Segment (revenue line ID) | `segment` | a top-level revenue id: the COGS row's base is that segment's revenue (`m_<segment>`); blank = Total Revenue |
| E, F | Data label, Data section | `data_label`, `data_section` | history series; with no history the line starts at the first estimate |
| G | SBC data label | `sbc_data_label` | Opex rows: history of the SBC inside that line (adds `sbc_<id>` and `<id>_ex` rows) |
| H | Volume line ID | `volume_id` | `cost_per_unit` drivers: `={Revenue Build!vol}*{drv}*{months}` |
| I | Notes | `notes` | not used |

Ids the build adds: `m_<segment>` and `m_total_rev` (revenue links), `total_cogs`, `total_gp` and the `other_cogs` plug only when there are two or more COGS rows, `total_opex`, `other_opex` (plug for unmodelled operating items in history), `total_sbc`, `op_inc`. Every cost line has a `pct_of` sub-row (`% of <base>`). Proposal: one `cogs_total` row (first of Cost of Revenue / Cost of Goods Sold / Cost of Sales) plus `sga`, `rd`, `sm`, `ga` and `other_opex_line` when those labels exist in the data.

## 7. Drivers

| Col | Header | Read as | Meaning |
|---|---|---|---|
| A | ID | `id` | driver id: `{drv:id}` in formulas, block key on the grid |
| B | Label (as shown on Drivers & Casing) | `label` | block title |
| C | Section | `Revenue` `Cost` `Income Statement` `Balance Sheet` `Cash Flow` | Drivers & Casing section (unknown text = Revenue) |
| D | Target line ID | `target` | the line the driver feeds; the first driver row targeting a line is the one used |
| E | Type | `type`, blank = `flat` | formula, table below |
| F | Cased (Y/N) | `cased`, blank = Y | Y = one grid row per case; N = one `Active` row |
| G | Format | `%` `bps` `amount` `price` `shares` `x` | grid and model number formats: `0.0%`, `0"bps"`, `#,##0.0`, `0.00`, `#,##0.00`, `0.0x` |
| H | Represented on the build as | `represented`; also `formula` when it starts with `=` | the analyst's description, or the engine formula for `custom` |
| I | FY aggregation | `fy`, blank = sum | uncased drivers' FY columns: `sum` `avg` `last` `first` (`formula` writes nothing) |
| J | Notes | `notes` | not used |

| Type | Target line becomes | Feeds sub-row |
|---|---|---|
| `yoy_pct` | prior year x (1 + d) | `pct_yoy` |
| `qoq_pct` | prior quarter x (1 + d); annual-only years: prior year x (1 + d) | `pct_qoq` |
| `net_adds` | prior period + d | `net_adds_qoq` |
| `bps_qoq`, `bps_yoy` | prior quarter, prior year + d/10000 (percentage lines) | `bps_qoq`, `bps_yoy` |
| `pct_level` | the line is d (a margin, mix or tax rate) | none |
| `pct_of_base` | base x d (cost rows: segment or total revenue) | `pct_of` |
| `gm_pct` | cost = base x (1 - d) | the gross-profit line's `pct_of` (its GM % row), resolved by `build_spec` |
| `cost_per_unit` | volume x d x months (cost rows with a Volume line ID) | none |
| `absolute` | the line is d (an amount typed directly) | none |
| `flat` | prior period; needs no grid input | none |
| `single` | one constant; does not reach the model from the grid (section 15) | none |
| `custom` | the `=` formula of column H, in the engine mini-language | none |

Revenue level lines accept every type except `gm_pct`, `pct_of_base` and `cost_per_unit`; cost lines accept `gm_pct`, `pct_of_base`, `cost_per_unit`, `absolute`, `yoy_pct`, `custom` and `flat`. The statements reference the uncased drivers by id, so keep the ids of `canon.DEFAULT_DRIVERS`: `interest_income`, `interest_expense`, `other_nonop`, `tax_rate`, `dep`, `amort`, `da`, `sbc`, `adj_other`, `adj_tax_rate`, `shares_basic`, `shares_dil`, `recv_pct`, `inv_pct`, `prepaid_pct`, `pay_pct`, `accrued_pct`, `defrev_pct`, `capex`, `debt_change`, `buybacks`, `dividends`, `stock_issued`, `rsu_tax`. Amounts carry the statement's sign (capex and buybacks negative); a working-capital ratio is the quarter-end balance over that quarter's revenue, cost of revenue or costs (13-week basis). `build_spec` drops a default driver that no line references (`da` when `dep` and `amort` exist, `adj_other` and `adj_tax_rate` without the Non-GAAP block, a ratio whose balance-sheet line is absent) and keeps every analyst-added id; the grid still shows blocks for dropped drivers, leave them empty.

## 8. Variance & Deltas

Two tables on one tab. Rows 4 to `deltas_start - 3` are variance rows; then the bold line `DELTA ROWS ...`, the second navy header in row `deltas_start` (18 in a fresh workbook) and the delta rows. `J1` holds `deltas_start=<row>` and `read_inputs` relies on it: never insert or delete rows on this tab and never edit J1.

Variance rows (A Line ID, B `% yoy`, C `% 2y stack`, D `$ yoy`, E `% qoq`, F `$ qoq`, G `% total`, H Start period): a cell is ticked when its text starts with Y. A listed line gets exactly its ticked rows (none ticked = the default set); unlisted lines keep the defaults: amount lines `pct_yoy, pct_2y, usd_yoy, pct_qoq, usd_qoq` (plus `pct_total` for top-level revenue), count KPIs `net_adds_yoy, pct_yoy, net_adds_qoq, pct_qoq`, percentage KPIs `bps_yoy, bps_2y, bps_qoq`, cost lines `pct_yoy, usd_yoy, pct_qoq, usd_qoq` after the fixed `pct_of` row. On revenue lines the row the driver feeds is always kept; on a cost line with a `yoy_pct` driver keep `% yoy` ticked. Start period is read into `start` but not used by the build.

Delta rows (15 spare, each one yellow row):

| Col | Header | Meaning |
|---|---|---|
| A | Sheet | `Revenue Build` or `Margin Build` (blank = Revenue Build); `Income Statement` is in the dropdown but never rendered |
| B | Line ID | required; a line of that sheet: `total_rev` or a tree id; `m_<id>`, a cost id, `gp_<x>`, `total_gp`, `total_opex`, `op_inc` |
| C | Label | text of the `<Source> <Label> % YoY` and `∆ to <Source> (bps)` rows (blank = line id) |
| D | Measure | `growth`: `<line>.pct_yoy` minus the series' implied y/y, in bps; `margin`: `<line>.pct_of` (cost, gross-profit and `op_inc` lines only) minus the series, in bps; `level`: line over series minus 1, in % |
| E | Source | `Consensus` `Guidance` `Buyside` (blank = Consensus); used only in labels and row ids |
| F, G | Data label, Data section | the comparison series in the data; `growth` uses the estimate periods whose prior year is in the same series |
| H, I | From period, To period | optional period ids that clip the columns, inclusive |

A row whose series yields no values is dropped silently; a row whose line or sub-row does not exist stops `build` with `line 'x.pct_of' not found`. Proposal: Total Revenue growth (`Revenue`, section `Highlights`), one growth row per tree line, `Gross Margin (%)` as margin on `total_gp`, `Adjusted Operating Margin (%)` as margin on `op_inc`. With a single COGS row there is no `total_gp`: point that row at `gp_total` (the gross-profit id of the only COGS row). `op_inc` is GAAP operating income; check that the consensus series compares like for like.

## 9. Side Builds, Guidance, Buyside, KPI History

- **Side Builds** (Name (tab), Linked driver ID, Describe the build and its layout; column C wraps): read into `side_builds` as `name`, `driver`, `description`. `build_spec` takes side-build specs only from `side_builds_specs`, which the workbook never produces, so this tab is the analyst's brief: write the spec yourself (`references/side-builds.md`) into `side_builds` of `model_spec.json`, and type the link into the linked driver's Base row on the Driver Grid, e.g. `='ARPU Bridge'!F3/10000`.
- **Guidance** (Line ID, Measure, Period, Low, High, Mid = `=IF(AND(D4<>"",E4<>""),AVERAGE(D4:E4),"")`, Source / date) and **Buyside** (Line ID, Measure, Period, Value, Source) are read into `guidance` and `buyside` (Mid is not read). `build_spec` does not consume either list: a delta row takes its series only from a data label. To get a delta-to-guidance or delta-to-buyside row, add the numbers to the data JSON as a line, e.g. `{"file": "guidance", "sheet": null, "section": "Guidance", "label": "FY26 revenue guidance mid", "values": {"FY2025": 4372.0, "FY2026": 4400.0}, "pct": false, "suspect": false}` (percentages as decimals), and name that label and section on the delta row with the matching Source. `growth` needs the prior-year value in the same `values`; `margin` and `level` take the estimate-period values as they are.
- **KPI History** (A Data label; period labels in row 3 from column B, `1Q23`, `1Q2023`, `2023Q1` and `FY2023` all parse): one row per KPI absent from the exports. The label must equal the Revenue Tree's Data label exactly (case-sensitive; a KPI History label beats the data files), cells must be numbers (formulas are ignored), and only actual quarters on the axis are used. Not pre-filled.

## 10. Statement Mapping

One row per canonical line of `canon.IS_LINES`, `BS_LINES` and `CFS_LINES` (plugs excluded): A Model line ID, B Model label, C Statement, D Data label (yellow), E Data section (yellow), F Keep (Y/N, yellow). Proposal: the first synonym with data, Keep = Y when one is found. Read into `mapping`; `build_spec` applies it line by line: Keep = N drops the line's history (the line disappears unless the model needs it; `interest_income` and `interest_expense` always stay, and `cogs`, `tax`, `sbc`, D&A and share counts fall back to their drivers), and a Data label (with an optional section) replaces the synonym search. Lines with no data are dropped anyway, and reported subtotals that do not tie get plug lines (`other_ca`, `other_nca_plug`, `other_cl_plug`, `other_ncl_plug`, `other_eq_plug`, `other_op`, `other_inv`, `other_fin`, `fx`). `ni` is always computed from the lines above it; its row is informational.

## 11. Driver Grid

Row 3: `Driver ID`, `Case`, the last four actual quarters (`3Q25` ... `2Q26`, grey), every estimate quarter (`3Q26E` ...), the annual-only years (`FY2029E` ...), `Comment`; panes freeze at C4. One block per Drivers row: a bold title row (id, label), then one yellow row per case (`Disaster` ... `Blowout`, or `Bear` `Base` `Bull`) or a single `Active` row for uncased drivers, separated by a blank row. Cells carry the driver's number format; grey cells show the realised value when the driver's target is a level line with history (`dep`, `sbc`, `capex` ...). A `single` driver gets case rows with only the first estimate column yellow; `build_spec` moves that one value to the first Drivers & Casing column (the first quarter of the last actual fiscal year), where custom formulas reference it as `{drv:<id>@<pid>$}`. Formulas typed in the grid may reference other grid cells: `read_inputs` rewrites such A1 references as engine tokens (`{drv:<driver>:<Case>@<pid>}` for another typed estimate, `{drv:<driver>@<pid>}` for a grey history cell) and lists references it could not translate under `driver_grid_warnings`.

`read_inputs` maps the header labels to period ids (the trailing `E` is dropped), skips rows whose column A is bold, and for every other row reads each period cell that is non-empty and not grey-filled:
- numbers stay numbers (`0.05` = 5 %); text `5%` becomes `0.05`; text `1,200` becomes `1200.0`; any other text, including a formula, is kept verbatim;
- the result is `driver_grid[id][case][pid]` (`case` is `Active` for uncased drivers) and becomes the driver's `values` in the spec: blue inputs on the case rows of Drivers & Casing;
- a note on a cell becomes `driver_grid_notes[id][case][pid]` and is written on the same case/period cell of the model, authored by the Setup author (unless `comments_policy` is `I will add my own`);
- the Comment column is read into `driver_grid_notes[id][case]["_row"]`, but the engine writes only period-keyed notes, so it never reaches the model.

Annual-only columns: cased drivers sum their case rows with SUMIF, so an empty cell means 0 (fill every case for every annual year); uncased drivers carry the prior year forward when the cell is empty. Flows (D&A, SBC, capex, buybacks) take full-year amounts; rates and ratios take year-end levels. A formula is copied into the model cell as typed, so it must be valid on Drivers & Casing: arithmetic on constants, or a cross-sheet link to a side-build tab (`='ARPU Bridge'!F3/10000`, coloured green). Never reference a cell of the grid itself.

## 12. Multiples

Left table from row 4: A Case, B Block 1, C Block 2 (yellow, `0.0x`), D Comment (yellow). After a blank row, `Weights (blended price target)` and one row per case with the weight in B (`0%`; defaults 10/20/40/20/10 % or 25/50/25 %). After another blank row, `Current implied multiple on (metric period)` with a period id in B (default `FY<last actual year + 1>`). Block table at G3:L5: Block, Label, Basis (`NTM` / `YE`), Target date, Metric period, Blended label; rows 4 and 5 are the only two blocks. Defaults: `YE<y+1>`, `YE`, `<y+1>-12-31`, `FY<y+2>`, `Near Term Setup`, then `YE<y+2>` ... `FY<y+3>`; the dates assume a December year end.

`read_inputs` returns `tearsheet`: `blocks` (one per non-blank Label: `label`; `basis`, stored only; `target_date`, ISO text or Excel date, drives `% IRR` through `YEARFRAC(valuation date, target date)`; `metric_period`, the Income Statement column of the metric, which must be on the axis; `blended_label`, blank = label, shown as `Blended Px Tgt - <blended label>`); `multiples[case][label]` from numeric cells only; `multiple_notes[case][label]` from a cell note, else the row's Comment copied to every block of that case; `weights[case]` numeric only (not forced to sum to 1; the Tearsheet uses SUMPRODUCT); `current_multiple_period`. The metric follows `metric_line` (section 3), the multiples land blue on yellow in the Tearsheet grid, and each block's `Px Tgt` is `(metric x multiple + cash - debt) / diluted shares x fx`.

## 13. DCF Inputs

A key (grey), B label, C value (yellow), D comment (yellow). Keys: `valuation_date` (default today; text or Excel date), `tax_rate`, `rfr`, `beta`, `erp`, `kd_after_tax`, `equity_weight`, `diluted_shares` (mm), `cash_lines`, `debt_lines` (comma-separated balance-sheet ids, pre-filled from the lines present among `cash, st_inv, lt_inv` and `st_debt, lt_debt, lease_liab_cur, lease_liab`). Below `Exit EV/EBITDA multiple by case`: one row per case keyed `exit_<case>` (`exit_base`), the case name in B, the multiple in C (numbers only), a comment in D.

`read_inputs` returns `dcf`: each key's raw value (rates as decimals such as `0.21`; a formula string would be written into the DCF as that literal formula), `cash_lines` and `debt_lines` as lists, `exit_multiples[Case]`, and `notes` (`notes[key]` from column D, `notes["exit_multiples"][Case]`). Ke and WACC are computed on the DCF tab, and the bridge takes cash and debt from the last balance sheet ending on or before the valuation date. Notes reach the model for `rfr`, `beta`, `erp`, `diluted_shares` and the exit multiples; the DCF tab looks the other inputs up under internal keys (`val_date`, `tax`, `kd`, `we`), so comments on `valuation_date`, `tax_rate`, `kd_after_tax`, `equity_weight`, `cash_lines` and `debt_lines` are dropped.

## 14. Filling the workbook with openpyxl

When the analyst answers in chat and asks you to type for them:
1. `wb = load_workbook(path)`, never with `data_only=True` or `read_only=True` (the first replaces formulas with cached values on save, the second cannot save). Excel must not have the file open, or `wb.save` raises `PermissionError`.
2. Write cell values only (`ws.cell(row=r, column=c, value=v)`); leave fonts, fills and validations alone. Grey fills and bold title rows are what `read_inputs` keys on, so never bold a case row and never fill an input cell grey.
3. Locate rows by their key, not by a remembered row number: Setup by the column A key; trees, Drivers and Statement Mapping by the column A id; the Driver Grid by `(A, B) == (driver id, case)` with A not bold; grid columns by the row-3 label (strip the trailing `E`, or use `periods.parse_pid`).
4. Use the spare yellow rows: Revenue Tree 20 (above the candidate marker), Cost Tree 15, Drivers 25, variance 12, deltas 15, Side Builds 8, Guidance 15, Buyside 15. Rows appended below the yellow area are still read everywhere except the Revenue Tree (stay above the marker) and the variance table (which ends two rows above the delta header). Never `insert_rows` or `delete_rows`: the validations and `J1` hold absolute rows.
5. Values: Python numbers for numbers, decimals for percentages, dropdown options spelt exactly as listed, period ids as `1Q27` / `FY2029`, Setup dates as ISO text, `None` to clear a cell.
6. Notes: `cell.comment = Comment(text, author)` only with the analyst's own words and the Setup author. Never write explanations, sources or remarks anywhere in the workbook: grid notes and comments flow into the model, and `verify` fails the build on fingerprints.
7. Never type estimates: the grid, multiples, weights and DCF inputs are the analyst's. Consensus-implied starting points go in a separate scratch file.
8. Save to the same path, then read it back with `read_inputs` in a short script to check the rows you changed, and run `spec`.

## 15. Limits to remember

- Re-running `inputs2` rebuilds the three stage-2 tabs empty (section 1).
- `single` drivers: the grid stores the constant under the first estimate quarter, but the Drivers & Casing block looks for it under its own first column (the first quarter of the last actual fiscal year), so the value never lands. Put the constant in a side build or inside a `custom` formula.
- `custom` as a Revenue Tree kind projects `=0`; `custom` works as a driver type.
- Stored but not used by the build: the Driver Grid Comment column, the Notes columns of the trees and Drivers, Start period, `model_file`, `valuation_metric`, Data Files, Guidance and Buyside rows.
- Delta rows on `Income Statement` are ignored; `margin` rows need a line with a `pct_of` sub-row.
- Comments on `valuation_date`, `tax_rate`, `kd_after_tax`, `equity_weight`, `cash_lines` and `debt_lines` do not reach the DCF.
