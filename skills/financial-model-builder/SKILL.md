---
name: financial-model-builder
description: Builds a cased three-statement equity research model in Excel (Revenue Build, Margin Build, Drivers & Casing with Disaster/Bear/Base/Bull/Blowout cases, side builds, Tearsheet with blended price targets and sensitivities, DCF, income statement, cash flow, balance sheet) formatted exactly like the analyst's reference model, from Bloomberg consensus and CapIQ exports plus the analyst's own driver estimates typed into an Excel inputs workbook. Use this whenever the user wants to build, rebuild, refresh, roll forward or extend a financial model, earnings model, 3-statement model, DCF, tearsheet, revenue or margin build, driver casing, or mentions Bloomberg consensus or CapIQ statements for a company, even when the word "model" is not used.
compatibility: Python 3.10+ with openpyxl; Excel + pywin32 + pypdfium2 on Windows for recalculation, verification and snapshots (optional elsewhere)
---

# Financial model builder

You build the analyst's model, in their format, from their numbers. The reference layout (a Spotify model) is encoded in the scripts: every tab, row pattern, font, fill, number format and colour rule is reproduced by code, so your job is orchestration and judgment, not formatting. The analyst types every estimate; you never invent driver values.

Non-negotiables, in priority order:
1. **Nothing in the workbook reveals an AI or a tool.** No comments, notes, sources, explanations, sheet names or metadata from you. The only notes are the analyst's own (typed on grid cells) and the author stamp is their name. `verify` scans for fingerprints; a failed scan is a failed build.
2. **Format is the reference model's.** Blue = typed input, black = calculation, green = link from another sheet; Arial 11; gridlines off; navy section headers; yellow delta-to-consensus rows; period columns in the quarter-quarter-quarter-quarter-FY pattern. The scripts do this; do not hand-edit cells afterwards with other styles.
3. **Ask everything up front, then run to the end.** Collect the setup answers, the driver definitions and the estimates first; after the analyst says "go", build, verify and fix without check-ins unless something is truly blocking.
4. **Review before building.** With all inputs in hand, read what the working folder already knows about the company and flag questionable assumptions and modelling quirks. Wait for the analyst's go.

All commands run from the current working folder (the analyst's project or repo). Scripts live in `${CLAUDE_SKILL_DIR}/scripts`; call them with `python "${CLAUDE_SKILL_DIR}/scripts/fmb_cli.py" <command>`. Run `doctor` first in a new environment.

## Workflow

### 0. Orient (one minute)
- `python "${CLAUDE_SKILL_DIR}/scripts/fmb_cli.py" doctor` checks Python packages and Excel. On a machine without Excel the model still builds; recalculation, snapshots and per-case values are skipped and the analyst opens the file in Excel to calculate.
- `... fmb_cli.py detect .` lists Bloomberg and CapIQ files in the folder (xlsx, csv or md). This repo keeps Bloomberg "Company Financials" printouts as Markdown under `Working Notes/Sources/<TICKER>/consensus/`; the parser reads those directly.
- If the Bloomberg consensus or the CapIQ statements are missing, ask for them before anything else. Three full fiscal years of quarterly history is the default; shorter history is allowed but say so.

### 1. Parse the data
`... fmb_cli.py parse <files...> --out model_data_raw.json` normalises every file into one JSON (periods with end dates and estimate flags, line items by section). Report in a few sentences: ticker, currency, fiscal year end (and whether it was assumed), first quarter of history, last reported quarter, last estimate quarter, the lost-decimal values the parser corrected (the Bloomberg PDF export sometimes prints 7300 for 73.00; corrections are listed as was -> now) and any it could not resolve. Confirm both with the analyst or against another file. See `references/data-parsing.md` for layouts and gotchas.

### 2. Setup and definitions (stage 1 of the inputs workbook)
`... fmb_cli.py inputs1 model_data_raw.json --out <TICKER>_model_inputs.xlsx --set key=value ...` writes a pre-filled workbook with these tabs: Setup, Data Files, Revenue Tree, Cost Tree, Drivers, Variance & Deltas, Side Builds, Guidance, Buyside, KPI History, Statement Mapping. `references/inputs-workbook.md` documents every column.

Ask the analyst, in one message, the setup choices the data cannot settle: currency (reporting and trading, FX), history start, estimate horizon (last quarterly estimate and annual-only years), case set (3 or 5), comment policy, author name, price source (Bloomberg/CapIQ/FactSet formula with a typed fallback), valuation metric, whether the company's non-GAAP figures exclude SBC (the `adj_sbc_addback` switch; Illumina, for one, keeps SBC in non-GAAP), target blocks (NTM or year-end, dates, metric periods), cover tab name. Write their answers into the Setup tab (openpyxl) or let them edit the yellow cells, whichever they prefer.

Then define the model with them, in this order, and write each answer into the workbook as you go:
1. **Revenue tree**: segments and sub-lines and how they add up (sum, volume x price, growth, share of parent, direct, KPI lines). Propose a tree from the Bloomberg segment and business-breakdown lines; the analyst confirms or reshapes it. Every line names the data label that holds its history.
2. **Cost tree**: COGS lines (one per segment, or one total) and operating expense lines, each with its history label; SBC by function if the data has it.
3. **Drivers**: for each revenue line, KPI and cost line, ask "driver N: what is it, and how is it represented on the build?" until the analyst says every revenue driver is defined, then the same for cost drivers. Map each answer to a driver type (`references/model-logic.md` lists the types and the formula each produces); anything that does not fit a type becomes `custom` with an explicit formula in the engine's mini-language. Income statement, balance sheet and cash flow drivers (interest, tax rate, D&A, SBC, shares, working-capital ratios, capex, buybacks, dividends, debt) are pre-filled as uncased drivers; keep, drop or add.
4. **Variance rows and delta rows**: which metrics get y/y, 2-year stack, q/q rows and from when; which metrics get delta-to-consensus, delta-to-guidance and delta-to-buyside rows and for which periods. Guidance comes from the folder's notes (earnings calls, decks) when the analyst asks you to find it; buyside numbers are typed from their screenshot into the Buyside tab.
5. **Side builds**: for each one, its tab name, the driver whose Base case it feeds, and the analyst's paragraph describing the build and its layout.
6. **Statement mapping**: show the proposed mapping of data labels to the condensed statement lines; the analyst confirms.

### 3. Estimates (stage 2)
`... fmb_cli.py inputs2 <TICKER>_model_inputs.xlsx model_data_raw.json` adds the Driver Grid (periods across, cases down, one block per driver, realised history in grey), Multiples (per case and target block, plus weights) and DCF Inputs tabs. The analyst fills the yellow cells in Excel: numbers or formulas, a note on a cell when they want a comment on the model cell, a row comment in the last column. Wait for "done". Never fill estimates yourself; if they ask for consensus-implied starting points, put them in a separate scratch file, not the grid.

### 4. Review, then go
`... fmb_cli.py spec <inputs.xlsx> model_data_raw.json --out model_spec.json --data-out model_data.json` compiles everything (grid formulas that point at other grid cells are rewritten into model references; anything it could not translate is listed under `driver_grid_warnings` and must be resolved with the analyst). Before building, read the folder's research on the company (in this repo: `Core Notes/` and `Working Notes/INDEX.md`; elsewhere, whatever notes exist) and run through `references/review-checklist.md`: inputs that contradict history, guidance or consensus; fiscal-calendar quirks (53-week years, non-December year ends); one-offs in history that the plug lines absorbed; segments that do not sum; items the analyst may have forgotten (new product lines, pricing actions, buybacks, debt maturities, FX). Put the concerns in one message and wait for "go".

### 5. Build, verify, fix
- `... fmb_cli.py build model_spec.json model_data.json --out models/<TICKER>_model_<YYYY-MM-DD>.xlsx` writes the workbook and a `.map.json` beside it (row and cell map for the next steps).
- `... fmb_cli.py verify <model.xlsx>` recalculates in a private safe-mode Excel, lists error cells, reads every `check` row (balance sheet, cash, margin build) and scans for fingerprints and colour-rule breaches. Fix the spec or the inputs and rebuild until `ok` is true; a check that does not tie to zero is always a defect.
- `... fmb_cli.py cases <model.xlsx> model_spec.json` flips each case, recalculates and writes each case's valuation metric into the Tearsheet (typed, blue), as the reference model does.
- `... fmb_cli.py snapshot <model.xlsx> "Revenue Build!A1:P46" out.png` renders a tab to PNG; look at the Revenue Build, Drivers & Casing, Tearsheet and DCF against `references/format-spec.md` and fix anything that differs.
- Side builds: turn each paragraph into a side-build spec (`references/side-builds.md`), add it to `side_builds` in the spec, and point the driver's Base-case cells at the tab's output cells with formulas such as `='ARPU Bridge'!F3/10000`. Rebuild and verify.

### 6. Deliver
Save the model, the inputs workbook and the two JSON files together (default `models/` in the working folder; in this repo, `Working Notes/Outputs/models/` with an INDEX entry). Report: what was built, the verify result, the case values written to the Tearsheet, and anything left open (missing history, assumptions you had to make). Keep the summary in the chat, never in the workbook.

### Refresh or roll forward
Parse the new exports, re-run `inputs2` to extend the grid to the new horizon (existing inputs are kept), let the analyst fill the new periods, then `spec`, `build`, `verify`, `cases`. The inputs workbook is the durable record of the analyst's model design; keep it with the model.

## Judgment calls that are yours
- The engine's mini-language (documented at the top of `scripts/fmb/engine.py` and in `references/model-logic.md`) expresses any custom formula; translate the analyst's words into it rather than asking them to learn it.
- When history is missing for a KPI, ask for it (KPI History tab) rather than modelling around it.
- When a company reports items the condensed statements lack, the spec builder adds plug lines so history foots; mention them in the review so the analyst can decide how to project them.
- Fiscal calendars come from the exports' period-end dates; never assume December.
- If Excel automation fails, the model is still valid; say verification was skipped and why.

## References
- `references/format-spec.md`: the reference model's layout and styles, tab by tab, with the checklist used for the visual check.
- `references/model-logic.md`: period axis, formula mini-language, driver types, variance rows, delta blocks, statements, DCF and Tearsheet mechanics.
- `references/inputs-workbook.md`: every tab and column of the inputs workbook and how it is read back.
- `references/data-parsing.md`: Bloomberg and CapIQ layouts, the normalised data file, known export quirks.
- `references/review-checklist.md`: what to check before "go".
- `references/side-builds.md`: writing side-build specs and linking them into the Base case.
- `references/excel-automation.md`: how verification, snapshots and case values use Excel, and what to do when it fails.
