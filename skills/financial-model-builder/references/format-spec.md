# Format specification: the reference model, tab by tab

The scripts reproduce the analyst's Spotify model. This file says what a built workbook must look like, where each rule lives in the code (`fmb/styles.py`, `fmb/engine.py`, `fmb/sheets/*.py`, `fmb/build_model.py`) and how it compares with the template file cell by cell. Use it to read a `snapshot` PNG, to decide whether a difference is a defect, and to explain a formatting choice to the analyst. Never restyle cells by hand after a build: every style comes from `styles.style_cell`, and a hand edit breaks the colour audit in `verify`.

Contents
1. Workbook-wide rules (tab order, properties, fonts, colour constants)
2. Period sheets: columns, header block rows 2-10, freeze panes and zoom
3. Row types: section, band, subtitle, line, variance sub-rows, delta rows
4. The colour rule and how `flush()` assigns colours and fills
5. Number formats by line kind
6. Statements (FY columns, totals, check rows)
7. Drivers & Casing block layout
8. Tearsheet cell map
9. DCF rows
10. Cover, dividers, side builds
11. Where the engine deliberately differs from the template, and one known quirk
12. Visual checklist (15 points)

## 1. Workbook-wide rules

Tab order (`build_model.build`): `<cover_tab>` (default `Cover`), `|`, `Revenue Build`, `Margin Build`, `Drivers & Casing`, `||`, every side build in `side_builds` order, `Tearsheet`, `DCF`, `|||`, `Income Statement`, `Cash Flow Statement`, `Balance Sheet`. The cover is the active sheet on open. The `|` tabs are empty dividers that group the tab strip into builds, valuation and statements; the template has exactly these fourteen tabs with the analyst's pitch cover in first place.

Properties (`_stamp`): `creator` and `lastModifiedBy` are `company.author` (fallback `Analyst`); title, description, subject, keywords and category are cleared; every sheet has `fitToPage` off. Cell notes use the same author. `verify` scans values, notes and properties for fingerprints, so nothing else may be written into the file.

Fonts: Arial 11 everywhere (`FONT_NAME`, `FONT_SIZE`); the title in B2 is Arial 14 bold. Gridlines are off on every sheet. The template uses theme colours for its black text and `E8E8E8` bands; the engine writes the same colours as explicit RGB.

| Constant | RGB | Used for |
|---|---|---|
| `BLUE` | 0000FF | typed inputs |
| `BLACK` | 000000 | calculations, labels |
| `GREEN` | 008000 | links to another sheet |
| `WHITE` | FFFFFF | section text, hidden helper date C8 |
| `NAVY` | 003765 | section header rows |
| `YELLOW` | FFFF00 | delta-to-consensus/guidance/buyside rows |
| `LIGHT_YELLOW` | FFFFCC | key input cells (multiples, single-value drivers, plug lines) |
| `GREY_BAND` | E8E8E8 | estimate-period header cells, sub-section bands, DCF estimate FY labels (template theme `lt2`) |
| `GREY_FY` | F2F2F2 | statement FY columns, Drivers FY header cells (template white at -5% tint) |
| `GREY_PT` | D9D9D9 | Tearsheet price-target and blended rows, base-multiple cell of a sensitivity axis |
| `GREEN_TS` | 19B350 | Tearsheet block headers, cover tab colour |

## 2. Period sheets: columns, header block, freeze panes and zoom

Column axis (`periods.PeriodAxis`): data starts in D. For every fiscal year with quarterly columns the four quarters come first and the FY column follows (`1Q23 2Q23 3Q23 4Q23 FY 2023`); years beyond the quarterly horizon get one column each. Labels: quarters `3Q26E` (suffix `E` on estimates), FY with quarters `FY 2026E` (with a space), annual-only years `FY2029E` (no space). The Drivers & Casing axis is the same axis cut at the first quarter of the last actual fiscal year (`drivers_start_pid`) and renumbered from D; the DCF axis holds the FY columns only, from D.

Widths (`setup_period_sheet`): A 2.0 (marker column), B label column, C 2.0 spacer, D to the last period column 13.75, the three columns after it 10.0. B is 54.0 on the builds, 54.375 on the statements and the DCF, 58.0 on Drivers & Casing, which also sets A 1.25 and C 12.25. Default row height 14.25; rows 2 and 3 are 18.0.

| Tab | Zoom | Freeze | Notes |
|---|---|---|---|
| Revenue Build, Margin Build | 70 (`sheets.<name>.zoom` overrides) | D11 | `x` markers in A |
| Drivers & Casing | 70 | D11 | template shows 55 |
| Income Statement, Cash Flow Statement, Balance Sheet | none (100) | D11 | `fy_fill` grey FY columns |
| DCF | 80 | D11 | annual columns only |
| Tearsheet | 71 | none | fixed cell map, section 8 |
| Cover | 130 | none | column A hidden |
| Side builds | spec `zoom` | none | free-form |

The template's freeze panes sit wherever the analyst last scrolled (U15, Y21, D85, D36, L34, Z17); the engine freezes D11 on every period sheet so the label column and the header block stay in view.

Header block (`SheetBuilder.header_block`), identical on the builds and the statements:

| Row | Column B | Period columns |
|---|---|---|
| 2 | `title_line()`: `Spotify Technology S.A. (NYSE: SPOT)`, bold 14 | |
| 3 | `units_line()`: `€ in mm except per share data`, italic | |
| 5 | active case: on Drivers the typed case with a list validation of `cases`; elsewhere `='Drivers & Casing'!B5`; bold, thin top and bottom border | |
| 7 | `Fiscal Year`, bold | period labels, bold; thin top border on every cell from B to the last column |
| 8 | `Period Ending` | period-end dates, `mm-dd-yy`; C8 holds the date 91 days before the first period in white font, as the template does |
| 9 | `Weeks in Period` | quarters typed 13 or 14 (format `general`), FY with quarters `=SUM(D9:G9)`, annual-only years typed 52 (format `int`) |
| 10 | `Earnings Report` (not on Drivers) | report dates of actual quarters only |

Fills on rows 7-9: estimate periods get `GREY_BAND` on the builds and statements; on Drivers the FY columns get `GREY_FY` instead. Row 10 is never filled (the template fills its estimate cells too). Row heights: 5 and 7-10 are 15.0, row 11 is a 4.5 spacer and content starts at row 12; on Drivers rows 6 and 10 are the 4.5 spacers and content starts at row 11. The DCF writes its own short header (section 9).

## 3. Row types

`section(title, marker)`: `NAVY` fill from B to the last column, white bold label in B, `x` in A when `marker` is true, height 15.0, then one blank row. Revenue Build sections and bands carry the marker; Margin Build, the statements, Drivers and the DCF do not (`marker: false` in their blocks).
`band(title)`: `GREY_BAND` fill from B to the last column, bold black label (`Premium:`, `Ads:`), `x` marker, no blank row after.
`subtitle(title)`: bold black label without fill (`Totals:`, `Research & Development:`, `memo`, `Per Share data`, `Current Assets`); `Totals:` on Revenue Build also carries the marker.
`label_only(text)`: a text row with optional bold, italic and fill (`Non-Current Assets`).
`line(def)`: one registered row. The label in B takes `bold`/`italic`/`fill` from the def; `top` or `bottom` draws a thin border on every cell from B to the last column (totals, `Active` rows, delta rows). Blocks render through `SheetBuilder.blocks`: `{"section"}`, `{"band"}`, `{"subtitle"}`, `{"blank": n}`, `{"label"}`, `{"line": {...}, "with_subs", "gap"}` (a blank row follows each line unless `gap` is false) and `{"deltas": [...]}`.

Variance sub-rows (`SUB_DEFS`) sit directly under their parent with ids `<parent>.<key>`:

| Key | Label | Format | Italic | Written where |
|---|---|---|---|---|
| `pct_yoy` | `% yoy` | `pct` | yes | prior-year column exists |
| `pct_2y` | `% 2y stack` | `pct` | yes | two prior years exist |
| `usd_yoy` | `$ yoy` | parent's format | no | prior year |
| `pct_qoq` | `% qoq` | `pct` | yes | prior quarter; quarters only |
| `usd_qoq` | `$ qoq` | parent's format | no | prior quarter; quarters only |
| `pct_total` | `% total` | `pct` | yes | always |
| `bps_yoy`, `bps_2y`, `bps_qoq` | `bps yoy`, `bps 2y stack`, `bps qoq` | `bps` | yes | as the pct rows |
| `net_adds_yoy`, `net_adds_qoq` | `yoy net adds`, `qoq net adds` | `kpi` | no | as the yoy/qoq rows |
| `pct_of` | `% of Revenue` | `pct` | yes | always |

`DEFAULT_SUBS` by kind: `amount` and `price` get `pct_yoy, pct_2y, usd_yoy, pct_qoq, usd_qoq`; `count` gets `net_adds_yoy, pct_yoy, net_adds_qoq, pct_qoq`; `pct` gets `bps_yoy, bps_2y, bps_qoq`. A custom sub-row is a dict with `key, label, dsl, fmt, italic` (the spec builder uses it for `GM %`, `% margin`, `Incremental Operating Margin (y/y)` and the italic `Check` row under `op_inc`). The label text is what the analyst reads in a snapshot; keep the template's wording.

Delta block (`delta_block`): for each item, an external row with id `ext.<source>.<line>.<sub|level>` and label `Consensus Premium Revenue % YoY ` (bold, typed blue values in `pct_cons`, FY columns blank), then the delta row `∆ to Consensus (bps)` (or `(%)` for `level` items): bold italic, `YELLOW` fill on B and on every period cell, thin bottom border from B to the last column, format `bps_delta` or `pct_cons`, written only in periods where the external value exists, then a blank row. The template styles its delta rows the same way (bold italic on `FFFF00`, bottom border).

## 4. The colour rule and `flush()`

`styles.color_for(value)`: a formula containing `!` is `GREEN`, any other formula is `BLACK`, an int or float is `BLUE`; text is `BLACK`. Labels in column B are always black. `flush()` applies it to every period cell of every pending line in this order:

1. `_value_for` decides the content (typed history from `data`, a resolved `dsl`, an FY aggregate, or nothing). An empty cell still receives the line's font, number format and row fill, so later typing inherits the style.
2. `color` on the line def wins outright. Otherwise `color_for` runs; a black result turns blue only when the value came from a typed expression in the data or the driver grid (`_typed_input`, e.g. history typed as `=AVERAGE(205,210)` on Revenue Build row 31, or a Base-case input `=9.3%-0.63%`). `input_color` only recolours values that are already blue; `SUM`/`AVERAGE` aggregates and carry-forward formulas on driver rows therefore stay black, as the template has them.
3. Fill: the line's `fill` (whole row) or, for `input_fill` lines, `LIGHT_YELLOW` on numeric estimate-period cells only (plug lines such as `other_op`, `other_inv`, `notes_debt`, `other_fin`, `fx`).
4. Borders: `top` on every written cell, in addition to the full-width border drawn for the row.
5. On statements (`fy_fill`), every FY column of a year with quarters is painted `GREY_FY` from row 7 to the last written row wherever no fill exists; navy, yellow and band fills win.

`verify` reports `colour_violations` for cross-sheet links coloured blue and local formulas coloured green; it does not judge blue local formulas (see section 11).

## 5. Number formats by line kind

`KIND_FMT` maps a line's `kind` to a `NUMBER_FORMATS` key; `fmt` on the line overrides it, and a literal format string is passed through unchanged.

| Key | Format string | Where |
|---|---|---|
| `amount` (kind `amount`) | `#,##0;\(#,##0\)` | builds |
| `pct` (kind `pct`) | `0.0%;\(0.0%\);\-\%` | build percentages and sub-rows |
| `pct_plain` | `0.0%` | driver inputs, Tearsheet upside and IRR |
| `bps` (kind `bps`) | `0"bps";\(0"bps"\)` | bps sub-rows and bps drivers |
| `bps_delta` | `#,##0" bps";\(#,##0\)" bps";\-` | delta rows |
| `pct_cons` | `0.0%;\(0.0%\);\-` | external consensus rows, `(%)` delta rows |
| `kpi` (kind `count`) | `0.0;\(0.0\)` | subscribers, MAU, net adds |
| `price` (kind `price`) | `\€0.00;\(\€0.00\)` | per-unit amounts; symbol from the reporting currency (`price_format`), multi-letter symbols quoted (`"CHF "0.00`) |
| `amount_s` | `#,##0_);(#,##0)` | statement amounts |
| `pct_s` | `0.0%_);\(0.0%\)` | statement margins, tax rate |
| `shares` (kind `shares`) | `#,##0.00_);(#,##0.00)` | share counts |
| `eps` (kind `eps`) | `0.00_);\(0.00\)` | per-share data |
| `number1`, `number2`, `number4` | `0.0`, `0.00`, `0.0000` | Tearsheet bridge, DCF beta and discount rows, FX |
| `amount_d`, `pct_d` | `#,##0;\(#,##0\);"-"`, `0.0%;\(0.0%\);"-"` | DCF (dash for zero) |
| `mult` (kind `mult`) | `0.0\x` | multiples |
| `px` | `"$"#,##0.00` | Tearsheet prices; symbol from the trading currency (`px_format`) |
| `px_acct` | `_([$$-409]* #,##0.00_);_([$$-409]* \(#,##0.00\);_([$$-409]* "-"??_);_(@_)` | Tearsheet live price cell D39 |
| `weight`, `date`, `int`, `general` | `0%`, `mm-dd-yy`, `0`, `General` | weights, dates, weeks |

Sub-rows take the `SUB_DEFS` format, else the parent's `fmt`, else `amount`; this is why `$ yoy` under an ARPU line shows the currency symbol. The template agrees with every string above at the representative cells (Revenue Build D15/E19/D37, Income Statement D14/D17, DCF D11/D30, Tearsheet E5/E6/E7/N5).

## 6. Statements

Income Statement, Cash Flow Statement and Balance Sheet use the common header, one navy section row at row 12 without marker, `amount_s` lines, bold totals with a thin top border across (`total_rev`, `gp`, `total_opex_is`, `ni`, `cfo`, `cfi`, `fcf`, `cff`, `net_change`, `end_cash`, `total_ca`, `total_nca`, `total_assets`, `total_cl`, `total_ncl`, `total_liab`, `total_equity`, `total_le`), italic `pct_s` sub-rows (`% YoY Growth`, `% Gross Margin`, `% of Revenue`, `% Margin`, `% Net Margin`), bold subtitles `memo`, `Non-GAAP Reconciliation`, `Per Share data`, `Current Assets`, `Shareholders Equity`, and grey FY columns. Check rows are lines labelled `check` (`bs_check`: `={total_assets}-{total_le}`; `cash_check`: `={end_cash}-{Balance Sheet!cash}`, green); `verify` reads every row whose B label is `check` or `Check` and fails the build when any value exceeds 0.5. In the template, typed history on the statements is black and links are black; the rebuild colours them blue and green (section 11).

## 7. Drivers & Casing block layout

`sheets/drivers.py` writes the sections `Revenue Drivers`, `Cost Drivers`, `Income Statement Drivers`, `Balance Sheet Drivers`, `Cash Flow Drivers` (`SECTION_ORDER`), each a navy row without marker, then one block per driver and a blank row after each block:

| Row | Cased driver | Uncased driver |
|---|---|---|
| title | bold label (`subtitle`); `label_note` becomes a note on B | same |
| case rows | one per case in `cases` order, ids `drv:<id>:<Case>`, label = case name; blue inputs in estimate quarters and annual-only years (a typed formula stays blue through `input_color`; a side-build link such as `='ARPU Bridge'!F3/10000` is green); FY columns blank | none |
| `Active` | id `drv:<id>`, bold, thin top border across; estimate columns `=SUMIF($B$14:$B$18,$B$5,F14:F18)`; actual quarters a green link to the target line's realised value on the build (`target.line`, `target.sub`); FY blank | id `drv:<id>`, bold, top border; estimate quarters typed blue; actual quarters green links to the target; FY columns aggregate the quarters by `fy` (`=SUM(D114:G114)`, `=AVERAGE(...)`, `=G120` for `last`); annual-only years typed, or `annual_dsl`, or `=<prior FY column><row>` |

`single` drivers (a constant such as a price point) write only the first column and fill the case rows and the Active row `LIGHT_YELLOW` (template row 67). Number format is the driver's `fmt` (`pct_plain`, `bps`, `amount_s`, `pct_s`, `shares`, `price`). `ctx.drv_rows` maps driver id to its Active row, which `{drv:id}` tokens on the builds reference; the `.map.json` written beside the model lists it under `drivers`. On the uncased Active row typed quarterly inputs are blue while the FY aggregates (`=SUM`, `=AVERAGE`, `=G99`) and annual carry-forwards are black, matching the template.

## 8. Tearsheet cell map

Widths: A 9.0, B 2.25, C 22.25, D 9.25, E 12.0, F 9.0, G 4.75, H 22.25, I 3.75, J 10.375, K 9.0, L 4.75, M 9.0, N-P 9.0, Q 10.375, R 9.0, S 2.25; sensitivity columns T 12.0 and 10.375 after it. Zoom 71, no freeze. The layout is fixed by `sheets/tearsheet.py`; the `.map.json` entry `tearsheet` holds `metric_cells`, `px_cells`, `price` and `multiples`.

Case blocks: block 0 uses columns C-F, block 1 H-K (at most two blocks). Row 3 is `<label> Target` in white bold on `GREEN_TS`, merged across the four columns and centred. From row 4, seven rows per case in `CASE_BLOCK_ORDER` (`Base, Bull, Bear, Blowout, Disaster`):

| Row | C (merged C:D) | E |
|---|---|---|
| 4 | `Base - YE2027`, bold, centred, merged C:F, height 17.25 | |
| 5 | `Adj. EBITDA (FY28E)`, bold | the case's metric: typed blue bold (`case_metric_values`, written by `cases`) or a green link to the Income Statement; `#,##0.0` |
| 6 | `(x) NTM Multiple` | `=$E$54`, absolute link to the multiples grid, `mult` |
| 7 | `Px Tgt`, bold, `GREY_PT` on C-E, thin top border | `=(E5*E6+$E$43-$E$44)/DCF!$D$68*$E$42`, bold, `px` |
| 8 | `% upside/(downside)` | `=E7/$D$39-1`, `pct_plain` |
| 9 | `% IRR` | `=(E7/$D$39)^(1/YEARFRAC(DCF!D40,DATE(2027,12,31)))-1` |
| 10 | blank | |

Five cases fill rows 4-38, three cases rows 4-24. Blended tables start at `M3` for block 0 and `M15` for block 1 (`top = 3 + 12j`): the green header `Blended Px Tgt/Cases - <label>` merged M:R; the next row has bold headers N `Wt`, O `Mult`, P the last word of `metric_label` (`EBITDA`), Q `Px`, R `%`; then one row per case in `CASE_RANK` order (`Blowout, Bull, Base, Bear, Disaster`) with the case name in M, the weight in N (block 0 typed blue `0%`, block 1 `=N<row-12>` black), O `=E6`, P `=E5`, Q `=E7`, R `=Q5/$D$39-1`; then `Blended Px Tgt - <blended_label>` bold on `GREY_PT` across M-P with `=SUMPRODUCT(N5:N9,Q5:Q9)` bold on grey in Q; `% upside/(downside)`; `% IRR`; `R/R` bold `=AVERAGE(R5:R7)/R9*-1` (average upside of the best half of the cases over the worst case). With two blocks, `Blended R/R` `=AVERAGE(Q13,Q25)` sits two rows under the second `R/R` (row 27 with five cases).

Sensitivity grids (`_sensitivity`) start in column T on the same top row as each blended table: a green header `Px Tgt Sensitivity - <label>` merged over the grid; a header row with T `Case`, U `metric_short` (default `EBITDA`) and the multiple axis in V onward, blue bold centred, built by `sensitivity_multiples` from the lowest case multiple to the highest in equal steps through the Base multiple (steps 5, 2.5, 2, 1, 0.5, 0.25, 0.1, 0.05; at most `sensitivity_max_cols`, default 25; seven equal steps as fallback), the Base column cell on `GREY_PT`; case rows in `CASE_RANK` order with `=E5` in U and `=($U5*V$4+$E$43-$E$44)/DCF!$D$68*$E$42` prices; a blank row; `% Upside - <label>` bold; case rows `=V5/$D$39-1`. A block without multiples gets no grid.

Price and bridge, fixed rows: C39 `Current Px` bold; D39 the price, blue in `px_acct`: `=IFERROR(BDP("<ticker_code>","PX_LAST"),F39)` for `bloomberg`, `CIQ(...,"IQ_LASTSALEPRICE")` for `capiq`, `FDS(...,"P_PRICE")` for `factset`, or the typed value for `hardcode`; F39 the typed fallback price (blue, `px`); G39 the price date (blue, `date`). C41 `Equity Value (<reporting ccy>)` with E41 `=D39/E42*DCF!D68` bold green `number1`; C42 `EUR/USD` with E42 `=DCF!D66` green `number4` (typed 1, blue, when the currencies match); C43 `(-) Cash & Investments` E43 `=DCF!D62` green; C44 `(+) Debt & Lease Liabilities` E44 `=-DCF!D63` green; C45 `Enterprise Value` E45 `=E41+E44-E43` bold black; C47 `FY27E Adj. EBITDA (Active Case)` E47 green link to the Income Statement (`current_multiple_period`); C49 `FY27E Adj. EBITDA Multiple` E49 `=E45/E47` bold black on `LIGHT_YELLOW` with a full thin box; C51 `NTM Multiples (x)` bold with the block labels bold and centred in E51, F51; rows 52 onward one case per row in `CASE_RANK` order with the typed multiples blue in `mult` on `LIGHT_YELLOW`, boxed, with `multiple_notes` as notes. The DCF cell addresses come from `ctx.dcf_cells`, so they move with the DCF layout.

## 9. DCF rows

`sheets/dcf.py` uses the FY axis only, B 54.375, zoom 80, freeze D11. Header: B2 title, B3 units, B5 `='Drivers & Casing'!B5`, B7 `Fiscal Year` with the FY labels in row 7 (estimate years on `GREY_BAND`, thin top border across), row 8 a 4.5 spacer, row 9 the navy `Discounted Cash Flow` section. Line ids, labels and formats, in order: `dcf_rev` `Revenue` bold (green link to the Income Statement revenue line), `dcf_growth` `% Growth Rate`, `dcf_cogs` `(-) Cost of Revenue`, `dcf_gp` `Gross Profit` bold, `dcf_gm` `% Margin`, `dcf_opex0..n` `(-) R&D` etc. from `opex_lines`, `dcf_ebit` `EBIT` bold, `dcf_ebit_m` `% Margin`, `dcf_da` `(+) D&A` (sum of `da_lines`), `dcf_da_pct` `% of Revenue`, `dcf_ebitda` `EBITDA` bold, `dcf_ebitda_m` `% Margin`, `dcf_tax_rate` `% Tax Rate` (history links the statement tax rate, estimates `=$D$41`), `dcf_taxes` `(-) Taxes`, `dcf_nopat` `NOPAT` bold, `dcf_da2` `(+) D&A` (`={dcf_da}`), `dcf_nwc` `(+/-) ∆NWC` (sum of the Cash Flow `nwc_lines`), `dcf_nwc_pct` `% of Revenue`, `dcf_capex` `(+/-) CapEx`, `dcf_capex_pct` `% of Revenue`, `dcf_ufcf` `UFCF` bold, `dcf_dp` `Discount Period` (`number2`: first estimate year `=(DATE(2026,12,31)-$D$40)/2/365`, second `=(DATE(2027,12,31)-182.5-$D$40)/365`, then `=H34+1`), `dcf_df` `Discount Factor` `=1/(1+$D$48)^G34`, `dcf_pv` `PV of UFCFs` bold. Amounts use `amount_d`, ratios `pct_d`.

After a blank row, the `WACC` section lists `Valuation date` (blue `date`), `Tax Rate`, `Rfr`, `Beta` (`number2`), `ERP`, `Ke` `=D42+D43*D44` black, `After-Tax Kd`, `Equity Weight`, and `WACC` bold `=D47*D45+(1-D47)*D46`; inputs are blue in D. The `Terminal Value` section carries the case table in F:G starting on the section row itself: one row per case with the typed exit multiple blue in `mult` on `LIGHT_YELLOW`, then `Active` bold `=SUMIF($F$50:$F$54,$B$5,G50:G54)` on `LIGHT_YELLOW`; below the section, `Exit EV/EBITDA` `=G55`, `FY2030E EBITDA` (last FY column of `dcf_ebitda`), `TV` `=D52*D53`, `PV of TV` bold `=D54/(1+D48)^((DATE(2030,12,31)-D40)/365)`. The `Equity Value` section: `PV of UFCF` `=SUM(G36:K36)`, `PV of TV`, `Enterprise Value` bold, `(+) Cash & Investments` (green sum of the Balance Sheet `cash_lines` in the column of the last quarter ending on or before the valuation date), the `debt_label` row (green `=-(...)` of `debt_lines`), any `other_adjustments` rows (typed blue, formulas green), `Equity Value (EUR)` bold, and when the currencies differ `EUR/USD` (blue `number4`) and `Equity Value (USD)` bold, then `Diluted Shares (mm)` blue `number1`, `Implied Share Price (USD)` bold `number2`, `Current Share Price (USD)` `='Tearsheet'!D39` green, `Upside/(Downside)` bold `pct_d`. With three opex lines, two D&A lines, five cases and an FX row the rows match the template: revenue at 11, PV of UFCFs 36, WACC 38-48, Terminal Value 50 with cases F50:G55, Equity Value 57, bridge 59-71 (the template ends at 70 because it folds current lease liabilities into the debt formula where the engine adds an `other_adjustments` row). `ctx.dcf_cells` records `cash`, `debt`, `shares`, `fx`, `val_date`, `wacc`, `exit_rows`, `ebitda_row`, `implied_px`.

## 10. Cover, dividers, side builds

Cover (`sheets/cover.py`): named by `company.cover_tab`, tab colour `19B350`, gridlines off, zoom 130, column A hidden, B 8.0, otherwise empty: the analyst designs it (the template's cover is the pitch title in Arial 18 bold on merged rows 11-16). Dividers `|`, `||`, `|||`: empty, gridlines off, B 9.0, no tab colour.

Side builds (`sheets/side_builds.py`): gridlines off, `zoom` and `widths` from the spec (A 2.0, B 56.0 by default); every `cells` entry goes through `style_cell` with its `fmt` (a `NUMBER_FORMATS` key or a literal string), `bold`, `italic`, `fill` (six hex digits), `top`, `bottom`, `align` and `note`; formulas with `{tokens}` resolve through the engine; colour follows the colour rule unless `color` is given; `merge` ranges apply; `period_tables` write a bold period header from the `from` period and rows whose values are coloured by the rule (default format `bps`). The Spotify rebuild carries `ARPU Bridge` (zoom 70) and `Margin Bridge` (zoom 49) with the template's widths and merges.

## 11. Where the engine deliberately differs from the template

These are by design; do not "fix" them to match the template.

1. Colour rule everywhere. Typed history on the statements is blue and cross-sheet links are green; the template types history in black on the statements and mixes green and black on the Margin Build. Formula cells typed blue in the template (DCF `Exit EV/EBITDA` `=G55`) are black in the rebuild. The rule has to be consistent for the audit colours to mean anything.
2. Drivers `Active` rows show realised history as green links in the actual columns; the template leaves them blank. Row 7 on Drivers has every label bold with the top border across; the template bolds FY labels only.
3. Tearsheet: the typed multiples grid at C51 replaces the template's derived-multiple rows 49-69 (`=$E$49-1/3*($E$49-$E$50)`), because the analyst types each case's multiple in the inputs workbook; weights are typed; sensitivity grids are added from column T; bridge cells E42-E44 link to the DCF instead of holding typed numbers; D39 holds a plain formula with a typed fallback rather than a Bloomberg array formula. Minor template decorations are not drawn: bottom borders under `(x) NTM Multiple`, the `Px Tgt` fill in F/K, italic `% upside` labels, bold-italic `R/R`, the box around `Blended R/R`.
4. DCF `Current Share Price` links to Tearsheet D39 instead of a typed price; `TV` has no bottom border.
5. B5 has top and bottom borders, left-aligned (template: full box, centred); header labels and dates are left or right aligned by Excel defaults (template: centred); estimate cells in row 10 are unfilled; the FY header cell on statements is grey from row 7.
6. Freeze panes D11 on every period sheet; Drivers zoom 70; the cover is blank.

Known quirk, cosmetic: FY aggregates of lines whose quarterly history was typed as formulas (Revenue Build `prem_subs` rows `=AVERAGE(205,210)`, Cash Flow and Balance Sheet rows typed as formulas) come out blue instead of black, because the typed-input flag set while probing the quarters carries into the FY cell. `verify` does not flag it. Typing the history as numbers avoids it.

## 12. Visual checklist

Render with `python fmb_cli.py snapshot <model.xlsx> "Revenue Build!A1:P46" out.png` (also `Drivers & Casing!A1:T40`, `Tearsheet!A1:AB56`, `DCF!A1:K72`, `Income Statement!A1:N40`) and compare against the template.

1. Tab strip: cover (green tab), `|`, Revenue Build, Margin Build, Drivers & Casing, `||`, side builds, Tearsheet, DCF, `|||`, the three statements; nothing else.
2. B2 is the company title in 14 bold, B3 the italic units line with the right currency symbol, B5 the active case with top and bottom borders, equal on every tab.
3. Row 7 reads quarter, quarter, quarter, quarter, FY with `E` on estimates and a thin top border across; estimate columns are grey `E8E8E8` on rows 7-9 (FY columns `F2F2F2` on Drivers).
4. Row 8 dates in `mm-dd-yy`, row 9 weeks (13 or 14, FY sums, 52 on annual-only years), row 10 report dates on actual quarters only; C8 invisible.
5. Section rows navy with white bold text and a blank row after; Revenue Build sections, bands and `Totals:` carry an `x` in column A.
6. Bands grey with bold labels; subtitles bold without fill; `%` sub-rows italic with the template's labels (`% yoy`, `% 2y stack`, `$ yoy`, `% qoq`, `$ qoq`, `% total`).
7. Typed numbers blue, local formulas black, cross-sheet links green; `verify` returns an empty `colour_violations` list.
8. Number formats: parentheses for negatives, one-decimal percentages, `bps` suffix, currency symbol on per-unit lines, `_)` padding on statements, dash for zero on the DCF, `0.0x` multiples, `$` prices on the Tearsheet.
9. Delta rows bold italic on yellow with a bottom border across, in `bps` or `%`, only under periods that have an external value; the external row above them is bold blue.
10. Statements: FY columns light grey from row 7 down, bold totals with a top border, `check` rows showing 0, subtitles `memo` and `Per Share data` present.
11. Drivers: per block a bold title, one row per case in spec order, an `Active` row with a top border and `SUMIF` on `$B$5`, green links in actual columns, blank FY columns on cased drivers, yellow single-value drivers, a dropdown on B5.
12. Tearsheet: green headers, cases Base, Bull, Bear, Blowout, Disaster down the blocks and Blowout to Disaster in the blended tables, grey `Px Tgt` and blended rows, weights summing to 100%, the current multiple and the multiples grid boxed on light yellow, a sensitivity axis passing through the base multiple on a grey cell.
13. DCF: FY columns only, grey estimate labels, four navy sections, the case table beside `Terminal Value` with `Active` on yellow, blue inputs in the WACC block, implied and current share price with upside.
14. Geometry: wide label column B, 13.75 data columns, panes frozen at D11, zoom 70 on the builds and Drivers, 80 on the DCF, 71 on the Tearsheet, gridlines off.
15. Nothing foreign: no notes except the analyst's, author stamp on the properties, no sheet names or text outside this specification; `verify` reports `ok: true`.
