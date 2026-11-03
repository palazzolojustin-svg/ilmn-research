# Data parsing: Bloomberg and CapIQ exports to the normalised data file

`parse` turns every export the analyst supplies into one JSON file that the later commands read (`inputs1`, `inputs2`, `spec`). The code is `scripts/fmb/parse_data.py`; this file explains what it does so you can predict the output, recognise a bad parse and report the right facts to the analyst. Where this text and the code disagree, the code wins: read it.

## Contents

1. Running `parse`
2. The normalised JSON
3. Bloomberg "Company Financials" printouts (Markdown)
4. Bloomberg and generic xlsx/csv grids
5. CapIQ exports
6. How files are merged
7. Lookup helpers: `find_line()`, `series()`, `DataView`
8. What to tell the analyst after parsing
9. Known limitations

## 1. Running `parse`

```
python "${CLAUDE_SKILL_DIR}/scripts/fmb_cli.py" parse <file1> <file2> ... --out=model_data_raw.json
```

- Write `--out=` with the equals sign and no space. `parse_data.main()` treats every argument that does not start with `--out=` as an input file, so `--out model_data_raw.json` is read as two extra input files and the command dies with `ValueError: unsupported file type`. With fewer than two arguments it prints the module docstring and parses nothing.
- Accepted extensions: `.md` and `.txt` go to the Bloomberg Markdown parser; `.xlsx`, `.xlsm`, `.csv`, `.tsv` go to the grid parser. `.xls` is routed to openpyxl, which cannot open it: have the analyst save as `.xlsx`.
- `detect [folder]` lists candidate files: every xlsx/xls/xlsm/csv/md whose name contains consensus, capiq, capital_iq, capitaliq, bloomberg, income, balance, cash, key_stats, keystats, estimates or financials, skipping folders that start with `.` and the folders `_Build`, `node_modules` and `skills`. It is a finder, not a validator; pass the exact paths to `parse`.
- File order no longer decides between actual and estimate values (section 7), but keep the newest Bloomberg printout first so that, between two estimate columns for the same period, the newer consensus wins.
- stdout prints `wrote <path>`, a JSON block with `ticker`, `currency`, `fy_end_month`, `first_quarter`, `last_actual_quarter`, `last_estimate_quarter`, `n_lines`, then a `sections:` tally (line count per section, `-` for lines with no section). Read the tally every time: it is the quickest way to notice a mis-read printout.

The ILMN example (three printouts: two quarterly windows and one annual) gives 26 periods, 420 lines and 4 suspect rows.

## 2. The normalised JSON

Top-level keys of the file `merge()` writes:

| Key | Type | Meaning |
|---|---|---|
| `files` | list of file names | the inputs, in the order given |
| `periods` | `{pid: {"end": ISO date or null, "estimate": bool}}` | every period seen in any file |
| `lines` | list of line records | every labelled numeric row of every file, in file order; nothing is deduplicated |
| `ticker` | string or null | Bloomberg `Ticker:` line, e.g. `ILMN US Equity`, from the first file that has one |
| `currency` | 3-letter string or null | Bloomberg `Currency:` line, from the first file that has one |
| `fy_end_month` | 1-12 | fiscal year-end month (section 6) |
| `first_quarter` | pid or null | earliest quarter in `periods` |
| `last_actual_quarter` | pid or null | latest quarter whose `estimate` is false |
| `last_estimate_quarter` | pid or null | latest quarter whose `estimate` is true |
| `n_lines` | int | `len(lines)` |

Period ids are the model's own, from `periods.pid_of()`: quarters `1Q25` (`{q}Q{yy}`), fiscal years `FY2025`. A fiscal year is named by the calendar year in which it ends (a year ending June 2027 is `FY2027`). The FY column of a quarterly printout (`2025 Y Est`) and the columns of an annual printout both land on `FY2025`. Half-years from a semi-annual printout get ids such as `1H24` (section 9).

A line record:

```
{"file": "ILMN_Consensus_Quarterlies.md", "sheet": null, "section": "Segment Revenue",
 "label": "Adjusted Gross Margin (%)", "values": {"1Q25": 0.674, "2Q25": 0.694, ...},
 "pct": true, "suspect": false}
```

- `file`: file name only. `sheet`: worksheet title for xlsx, file stem for csv, `null` for Markdown.
- `section`: the most recent block header above the line. A text-only row becomes a section only when every value cell is genuinely empty or its label starts with one of the known headers (`Highlights`, `Segment Revenue`, `Business Breakdown`, `Regional Breakdown`, `Income Statement`, `GAAP Results`, `Company Specific Adjustments`, `Balance Sheet`, `Assets`, `Liabilities & Equity`, `Cash Flow`, `Cash from ...`, `Changes in Working Capital`, `Special Company Reference Items`, `Prior Disclosures`); a data line printed with dashes (`Investments`, `Equity Awards`) is kept as a value-less line and does not change the section. Use `section` to disambiguate duplicate labels, not as a statement name.
- `values`: period id to float. Periods whose cell was blank, `—`, `N/A`, `NM` or otherwise non-numeric are absent. Parentheses mean negative; `$`, `%` and thousands separators are stripped.
- `pct`: true when the label contains `(%)`, starts with `as % of`, or ends with `(%)` (Markdown) / `%` (grids). Bloomberg percent rows are divided by 100, so `67.4` is stored as `0.674`. CapIQ percent rows are not divided (section 5).
- `suspect` / `suspect_pids`: a text cell that is an integer of three or more digits with no decimal point (`to_number()`). Bloomberg prints every value with a decimal (`1,041.0`), so `7300` in a row whose neighbours read `75.0` means the PDF export dropped the point of `73.00`. `merge()` repairs such values when the same label elsewhere (another file, another period) gives an unambiguous scale: it divides by 100, 10 or 1000 when the result lands within 0.2x-5x of the reference median, records the change under `corrections` (and the line's `corrected_pids`), and lists what it could not repair under `unresolved_suspects`. `parse` prints both lists; confirm them with the analyst. Numeric xlsx cells are never suspect and CapIQ rows are never flagged. Each line also carries `est`, the per-period flag saying whether the value came from an estimate column.

What the model takes from this file: `spec_builder.hist_only()` keeps only actual quarters that sit on the model axis (FY totals are rebuilt from quarters), so history is always reported quarters. Estimate columns feed the delta-to-consensus rows and the proposed horizon (`last_estimate_quarter`, `annual_only_years`); annual-only estimate years such as `2029 Y Est` serve nothing else.

## 3. Bloomberg "Company Financials" printouts (Markdown)

The analyst saves the Bloomberg PDF as Markdown and `parse_bloomberg_md()` reads it. In this repo the files live under `Working Notes/Sources/<TICKER>/consensus/` with names like `ILMN_Consensus_Quarterlies.md`, `ILMN_Consensus_Quarterlies_2.md`, `ILMN_Consensus_Annuals.md`: one printout holds about ten period columns, so quarterly history plus the quarterly estimates need two files and the annual estimates a third. Pass all of them; `series()` joins them by label.

Rows as the parser classifies them, in the order it tests them:

| Row | Recognised by | Effect |
|---|---|---|
| `Ticker: ILMN US Equity`, `Currency: USD` | regex anywhere in the text; `Ticker:` must end in `Equity`, `Currency:` tolerates a split such as `US\|D` | `ticker`, `currency` |
| period header | at least `max(2, n/2)` of the cells after the label match `2025Q1`, `2025 Q3 Est`, `2023 Y`, `2026 Y Est`, `2024 H1` (case-insensitive, spaces optional) | column map for the rows that follow; registers each period with its `Est` flag |
| dates row | at least `max(2, n/2)` cells are US dates `m/d/yyyy`, and a header has been seen | period `end` dates (`2025-03-30`); the model derives 13/14-week quarters and 52/53-week years from them |
| units or page header | label starts with `in millions`, `in thousands`, `in billions`, `multiple periods`, `i milli` or `n ons o`; also any row before the first header | skipped |
| section row | label with no numeric cell | becomes `section` for the rows below |
| data row | label plus at least one numeric cell | one line record |

Markdown mechanics (`md_tables()`): a table is a run of lines starting with `|`; separator lines of dashes are dropped; any other line (blank, `----- PAGE 2 -----`) ends the table. The column map and the current section persist across tables, which is what makes multi-page printouts work: each page repeats its period header, and a page whose header came through garbled (fragments such as `i milli` / `n ons o` with no period labels) is read with the previous page's columns. That is right when the page continues the same column set and silently wrong when it does not (an annual page after a quarterly page). Check that each line's `values` carry the ids you expect; if a page was mis-assigned, repair its header row in the Markdown and re-run.

`<br>`-merged rows (`split_br_rows()`): the PDF export sometimes glues two rows into one, with `<br>` between the parts in every cell (`Cost of Revenue<br>Gross Profit | 350.0<br>650.0 | ...`). Any row with `<br>` in a cell is split so that part i of every cell forms row i, and empty rows are dropped. Two special cases:

- Label with at most one non-empty part and every value cell with at most one non-empty part: a wrapped single row; the fragments are joined (`1,234<br>` becomes `1,234`).
- Label in more fragments than the values (`Gross Profit<br>Regional Breakdown | -96.0<br> | ...`): empty fragments are dropped and the values are aligned to the last label fragments, so leading fragments are section titles and trailing ones data lines. A row of values whose label came out empty is attached to the preceding value-less line of the same section. If a label still looks truncated in the `sections:` tally, join it in the Markdown and re-parse.

A cell that still contains `<br>` after splitting takes its last non-empty fragment.

Value parsing (`to_number()`): `(10.0)` is -10; `−` and `–` become `-`; `—`, `-`, `--`, `N/A`, `NA`, `n/a`, `NM`, `n.m.` and `.` are blank; `$` and `%` are stripped; anything else that is not a plain number (`1.2x`, text, dates) is blank with no warning. Percent rows are divided by 100 after parsing.

Within one file, when the same period appears under two headers with different `Est` flags, the later header wins.

## 4. Bloomberg and generic xlsx/csv grids

`load_grids()` reads every worksheet of an xlsx (cached values, `data_only=True`) or the single csv/tsv table; `parse_grid()` then runs per grid:

1. Scan the first 40 rows for a row with at least three cells matching the Bloomberg period labels of section 3. The first such row is the header; cells that do not match are ignored columns.
2. If none is found, try the CapIQ header (section 5). If that fails too, the grid is skipped without a message.
3. Under a Bloomberg-style header, a next row holding at least three dates (US strings or real date cells) is the dates row and supplies `end` dates.
4. Every later row: column A is the label; blank rows and blank labels are skipped; a labelled row with no numeric cell becomes the section; numbers and numeric text (`1,200.0`, `(12.3)`, `12.3%`) become values. `pct` follows section 2 (a label ending in `%` counts) and divides by 100 unless the grid is CapIQ. `suspect` applies only to text cells, so a Bloomberg xlsx holding real numbers never raises it.

Labels must be in column A and the header within the first 40 rows (60 for CapIQ); a block placed elsewhere parses as empty. Move it or save it as a clean sheet.

## 5. CapIQ exports

CapIQ Excel exports (Income Statement, Balance Sheet, Cash Flow, Key Stats; one sheet or one file each) have a header row reading `12 months Dec-31-2023`, `3 months Mar-30-2025`, `LTM 12 months Sep-30-2025`. `capiq_period()` matches `(\d+) months? (ending)? Mon-dd-yyyy`; `parse_grid()` scans the first 60 rows and takes the row with the most such cells (at least three).

- `LTM` columns are skipped, as are 6- and 9-month columns. Only 12-month and 3-month columns become periods.
- Every CapIQ column is an actual (`estimate: false`) with `end` set from the header date.
- Fiscal year end: the most common month among the 12-month columns of the sheet; failing that, of any sheet in the workbook or any other file in the same `parse` run (`parse_files()` shares the evidence); failing that December is assumed and `fy_end_assumed` is set true in the output, which the review step must mention. Period ends up to the 7th of a month (52/53-week calendars: `Jan-03-2027`) are snapped back a week before any month arithmetic, so they map to the right fiscal year and quarter.
- Fiscal year of a column: the end date's year, plus 1 when its month is after `fy_end_month`. Quarter: `after = (month - fy_end_month) % 12`, `after == 0` is Q4, else `after // 3`. A column whose `after` is not a multiple of 3 is dropped.

Ids for a September year end:

| CapIQ header | pid |
|---|---|
| `12 months Sep-30-2024` | `FY2024` |
| `3 months Dec-31-2024` | `1Q25` |
| `3 months Mar-31-2025` | `2Q25` |
| `3 months Jun-30-2025` | `3Q25` |
| `3 months Sep-30-2025` | `4Q25` |

Quirks you must know:

- 52/53-week filers whose period ends spill into the next month break the month arithmetic: `3 months Jan-02-2026` for a December year end is dropped, and `12 months Jan-02-2026` becomes `FY2026` instead of `FY2025`. Correct those header dates to the nominal month end before parsing, or take those periods from the Bloomberg printout, whose explicit labels (`2025 Y`, `2025 Q4`) do not depend on the date.
- Percent rows (`Gross Margin %`) are flagged `pct` but not divided: a text cell `60.0%` stays `60.0`, a numeric percent cell stays whatever Excel holds. The model computes margins from amounts, so use a CapIQ percent row only after checking its scale.
- `suspect` is never set for CapIQ rows.
- `section` is whatever text-only row came last. CapIQ sheets open with rows such as `Currency | USD | USD ...`, which then serve as the section for the whole block. Leave `Data section` blank for CapIQ labels in the inputs workbook and match on the label alone.
- CapIQ labels differ from Bloomberg's (`Total Revenue` vs `Revenue`, `Cash And Equivalents` vs `Cash & Cash Equivalents`). `canon.py` lists the synonyms the Statement Mapping tries; a label that matches none is proposed empty and must be typed by hand in that tab.

## 6. How files are merged

`merge()` folds the per-file results in the order the files were passed:

| Item | Rule |
|---|---|
| `periods[pid].end` | last file that has a date for the period |
| `periods[pid].estimate` | true only if every file that has the period flags it as an estimate; a reported quarter in any file (a CapIQ actual, a newer printout) wins |
| `lines` | concatenated in file order, duplicates kept |
| `ticker`, `currency` | first file that has one |
| `fy_end_month` | first file that has one (CapIQ grids); else the most common month of the `FYxxxx` end dates from the Bloomberg dates row; else 12 |
| `first_quarter`, `last_actual_quarter`, `last_estimate_quarter` | from quarter ids only, sorted by year then quarter; half-years ignored |

Because `lines` keeps duplicates, the lookup helpers decide which copy is used (section 7). Put the newest Bloomberg printout first so its estimates win. Reported quarters are normally identical across files; where a restatement makes them differ, the first file's value wins, so say which vintage the history comes from.

## 7. Lookup helpers: `find_line()`, `series()`, `DataView`

All matching goes through `_norm()`: lower-case, every run of characters outside `a-z`, `0-9` and `%` replaced by one space, then trimmed. `Adjusted Gross Margin (%)` and `adjusted gross margin %` are the same label; `Revenue` and `Total Revenue` are not. Matching is exact after normalisation, never a substring.

- `find_line(data, label, section=None, prefer_file=None)` returns the first line record whose normalised label (and section, when given) matches; `prefer_file` moves lines whose file name contains that string to the front. Use it to inspect one row: its `pct`, `suspect`, file and section.
- `series(data, label, section=None, exclude_sections=None)` returns `{pid: value}` across files. Within one file (and sheet) only the first line with that label counts unless a section is given: Bloomberg repeats balance-sheet labels (`Accounts Receivable`, `Accounts Payable`) in the `Changes in Working Capital` block after the statement line, so the statement line wins. Across files a value from an actual column beats one from an estimate column whatever the order; between two values of the same kind the first file wins. `exclude_sections` drops lines whose section starts with any of the given prefixes; the spec builder uses it so income-statement, balance-sheet and cash-flow lines never read each other's blocks.
- `spec_builder.DataView.series(label, section)` is what the revenue tree, cost tree, drivers, delta rows and Statement Mapping call. It first checks the KPI History tab: when the exact label (case-sensitive, not normalised) is a KPI History row, that row is returned and the data files are not consulted. Otherwise it calls `series()`.
- `spec_builder.hist_only(series, axis)` keeps only actual quarters on the model axis. FY values, half-years and quarters before `first_hist_quarter` are dropped.
- `inputs_workbook._first_label(data, synonyms)` returns the first `canon.py` synonym for which `series()` is non-empty; the Statement Mapping and cost tree proposals come from it.

To see what a label will yield before building:

```
python -c "import json,sys; sys.path.insert(0, r'${CLAUDE_SKILL_DIR}/scripts'); from fmb.parse_data import series; d=json.load(open('model_data_raw.json')); print(series(d, 'Sequencing Consumables', 'Business Breakdown'))"
```

## 8. What to tell the analyst after parsing

Report, in a few sentences, exactly these items from the stdout block and the file:

1. `ticker` and `currency`, or that they were not found (a printout without `Ticker: ... Equity` / `Currency:` leaves them null; they are then typed in the Setup tab at `inputs1`).
2. `fy_end_month` in words and where it came from (CapIQ headers, Bloomberg FY end dates, or the default 12). Never assume December; the dates in `periods` are the evidence.
3. `first_quarter`, `last_actual_quarter`, `last_estimate_quarter`, and the last `FYxxxx` estimate in `periods` (not printed; read it from the file). `inputs1` proposes history from the first quarter of the year three years before the last actual, unless the data's first quarter falls in a later year, in which case it starts there; data starting mid-year leaves empty history columns, and data starting later gives less than three years of history. Say so either way. It also proposes `annual_only_years` as the two years after `last_estimate_quarter`.
4. The `corrections` the parser applied (file, label, period, was -> now) and every `unresolved_suspects` entry. Ask the analyst to confirm the corrections and to supply the unresolved values; a wrong history value flows straight into the model.
5. Anything odd in the `sections:` tally or the lines: one-word sections and truncated labels (wrapped labels), a page whose values landed in the wrong periods, half-year ids, periods without `end` dates.
6. The files used and their order, so the analyst can reorder them if the wrong vintage won.

Never fix values by editing the JSON. Fix the source file (join a wrapped label, restore a decimal, correct a header) and re-run `parse`, so the data file stays reproducible from the exports.

## 9. Known limitations

- Semi-annual periods: `2024 H1` headers are parsed into ids like `1H24` with no `end` date, left out of `first_quarter` / `last_actual_quarter`, and ignored by the period axis and `hist_only()`. The model is quarterly; a half-year reporter needs quarterly figures typed into KPI History or a converted export.
- Missing period-end dates: a printout without a dates row, or a grid without one, leaves `end: null`. `PeriodAxis.build()` then derives the missing ends: thirteen weeks after the previous period end when that end is not a calendar month end (52/53-week calendars keep their rhythm), otherwise the fiscal month end. Weeks in period come from consecutive ends, so a 14-week quarter and a 53-week year appear only where the data's dates say so. `fy_end_month` falls back to 12 when no file supplies it (`fy_end_assumed`).
- KPI history is not in the exports: Bloomberg and CapIQ carry financial lines and Bloomberg's `Segment Revenue`, `Business Breakdown` and `Regional Breakdown` blocks, not operating KPIs such as subscribers, ARPU or instrument placements. The analyst types those into the KPI History tab of the inputs workbook: row 3 holds period headers from column B in any form `parse_pid()` reads (`1Q23`, `1Q2023`, `2023Q1`, `FY2023`, `FY 2023E`, `2023`), column A from row 4 holds the data label exactly as typed in the Revenue Tree's `Data label` column, and only numeric cells are read. `read_inputs()` returns it as `kpi_history` and `DataView.series()` serves it before the data files.
- Duplicate labels: `Revenue` exists in `Highlights` and inside segment blocks, `Total Assets` can sit under a sub-header section. Give `Data section` when a label is ambiguous and check the result with `series()`.
- `Ticker:` needs the `Equity` suffix; `Currency:` takes the first two or three capital letters after it.
- `.xls` raises in openpyxl; csv is read as UTF-8 with BOM tolerance; any other extension raises `unsupported file type`.
- A header beyond row 40 (Bloomberg) or row 60 (CapIQ), or labels outside column A, give an empty parse with no warning.
- Nothing is deduplicated: the same label from three printouts gives three line records, resolved only by the rules in section 7.
