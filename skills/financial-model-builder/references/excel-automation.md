# Excel automation: verification, snapshots, per-case values

The model is written by openpyxl, which stores formulas but no results. Excel is used
afterwards for three things: recalculating and checking the workbook (`verify`),
rendering tabs to PNG for the visual check (`snapshot`), and reading each case's
valuation metric into the Tearsheet (`cases`). All three go through one mechanism,
`fmb/excel.py`'s `ExcelSession`.

## Why a private safe-mode instance

Plain COM activation (`DispatchEx("Excel.Application")`) starts Excel with every COM
add-in. On this analyst's machine the S&P Capital IQ add-in opens a sign-in web view at
startup, Excel never finishes registering with COM, the call fails with "Server
execution failed" and a hung EXCEL.EXE stays behind. So `ExcelSession` starts its own
process instead:

```
EXCEL.EXE /x /safe /automation [/r] <workbook>
```

`/x` forces a new instance (the user's open Excel is never touched), `/safe` loads no
add-ins or templates, `/automation` keeps it hidden, `/r` opens read-only (snapshots).
The session then finds that process's workbook window (`EXCEL7` child of `XLMAIN`) and
attaches to the object model through `AccessibleObjectFromWindow`, giving a normal
`Application` COM object. While it waits for the window it dismisses Office dialogs
(`NUIDialog`, e.g. "Excel has detected that you have recovered files") so nothing
blocks and nothing appears on the analyst's screen.

Inside a session: `DisplayAlerts = False`, `Visible = False`, and
`Workbook.EnableAutoRecover = False` so an interrupted session leaves no recovery
entries. `session.save()` restores auto-recovery on the workbook before saving. On exit
the workbook is closed without saving, `Quit()` is called, references are released and
the process is given 15 seconds to exit before it is stopped.

Rules that follow from this:
- Run Excel-bound steps one at a time. Two sessions starting together have timed out.
- Never force-kill a normal-mode Excel. Excel treats it as a crash and may disable the
  user's add-ins (it disabled the CapIQ add-in once; the fix was removing the entry under
  `HKCU\Software\Microsoft\Office\16.0\Excel\Resiliency\DisabledItems`).
- If Excel shows "you have recovered files" on the analyst's screen, the pending
  recovery entries are under `...\Excel\Resiliency\DocumentRecovery`; remove only the
  ones whose embedded path is a model built by this skill.
- A visible Excel window that is not the analyst's belongs to a session that lost its
  parent process; close it from its File menu rather than killing it.

## verify

`python fmb_cli.py verify <model.xlsx>` returns JSON:

- `static`: `issues` (formulas referencing missing sheets, `#REF!`/`#MISSING` text),
  `colour_violations` (cross-sheet link coloured blue, local formula coloured green),
  `fingerprints` (any cell, note or document property mentioning Claude, Anthropic,
  openpyxl, "generated"), `creator` and `lastModifiedBy` (must be the analyst's name).
- `recalc`: `errors` (every cell holding an Excel error after a full recalculation),
  `warnings` (`#DIV/0!` on variance rows: growth over a zero or empty prior period, fixed
  by a start period on the Variance tab, not a modelling defect), `checks` (the numbers
  on every row labelled `check`/`Check`: balance sheet, cash, Margin Build).
- `check_failures`: check rows with any value beyond 0.5.
- `ok`: true only with no issues, no fingerprints, no errors and all checks at zero.

A false `ok` is a defect to fix before delivering. The recalculated workbook is saved,
so the file carries values for anyone who opens it without recalculating.

## snapshot

`python fmb_cli.py snapshot <model.xlsx> "<Sheet>!A1:P46" out.png [scale]` sets the
print area to the range, exports that page to PDF from Excel (read-only session) and
rasterises it with pypdfium2. Use it on Revenue Build, Drivers & Casing, Tearsheet and
DCF and compare with `references/format-spec.md`. `evals/spot_regression/style_diff.py`
prints the programmatic style differences between the reference model and a rebuild.

## cases

`python fmb_cli.py cases <model.xlsx> <spec.json>` reads `<model>.map.json` (written by
`build`: row of every line, column of every period, Tearsheet metric cells), then for each
case sets `Drivers & Casing!B5`, recalculates, reads the valuation metric line for each
target block's metric period, restores the active case, writes the values into the
Tearsheet metric cells as typed inputs (blue) and recalculates and saves once more.

## doctor and fallbacks

`python fmb_cli.py doctor` reports Python, openpyxl, pywin32, pypdfium2 and the Excel
path, and whether build, verify and snapshot are possible. Without Excel (macOS, Linux,
a machine without Office) the model still builds; say that recalculation, checks,
snapshots and per-case values were skipped and that the analyst should open the file
in Excel, press F9 if needed, and read the check rows. `recalc_with_libreoffice` exists
as a conversion fallback where `soffice` is installed; it does not report error cells.
