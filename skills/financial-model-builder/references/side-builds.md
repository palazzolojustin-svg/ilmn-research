# Side builds

A side build is a free-form tab (an ARPU bridge, a margin bridge, a pricing walk) that argues a driver's Base case from explicit steps instead of a typed number. The driver's Base-case cells on Drivers & Casing link to the tab's output cells, so the Base case moves when the bridge moves. `fmb/sheets/side_builds.py` renders each tab from a small JSON spec in the house style; `build_model.build` places the tabs between the `||` divider and the Tearsheet and fills them after the build sheets exist, so cross-sheet tokens resolve. You write the spec from the analyst's paragraph; you never choose the numbers.

Contents
1. Where side builds sit in the pipeline
2. The spec
3. Tokens inside cells
4. Linking the driver's Base case
5. The Spotify examples: ARPU Bridge and Margin Bridge
6. From the analyst's paragraph to a spec
7. Formatting conventions for bridges

## 1. Where side builds sit in the pipeline

- The analyst describes each side build on the Side Builds tab of the inputs workbook: `Name (tab)`, `Linked driver ID`, `Describe the build and its layout`. `read_inputs` returns the rows as `inputs["side_builds"]` (`name`, `driver`, `description`); nothing else reads them. The paragraph is your brief and the driver id is the target.
- `build_spec` writes `"side_builds": inputs.get("side_builds_specs") or []`, and nothing populates `side_builds_specs`, so **every `spec` run resets `side_builds` to `[]`**. Keep the specs you write in a JSON file beside the model (for example `models/<TICKER>_side_builds.json`) and merge them into `model_spec.json` after each `spec` run, together with the driver links of section 4:

```python
import json
spec = json.load(open("model_spec.json", encoding="utf-8"))
side = json.load(open("models/SPOT_side_builds.json", encoding="utf-8"))
spec["side_builds"] = side["side_builds"]
for d in spec["drivers"]:
    for pid, f in side.get("driver_links", {}).get(d["id"], {}).items():
        d["values"].setdefault("Base", {})[pid] = f
json.dump(spec, open("model_spec.json", "w", encoding="utf-8"), indent=1)
```

  `driver_links` is your own bookkeeping; the CLI reads only `side_builds` and `drivers`. Then `build`, `verify`, `cases`, and `snapshot <model.xlsx> "ARPU Bridge!A1:K40" out.png` for the visual check.
- Tab order is fixed by `build`: Cover | Revenue Build, Margin Build, Drivers & Casing || side builds in list order, Tearsheet, DCF ||| statements.
- `name` is the sheet title and what the driver formulas quote (`='ARPU Bridge'!F3`). It must be unique and must not be a fixed tab name: `build` creates a placeholder with that name first and later removes the sheet of that name, so a side build called `Revenue Build` or `DCF` deletes or renames the real tab. Excel allows at most 31 characters and none of `[]:*?/\`.
- Build order inside `build`: placeholders are created after Drivers & Casing (for tab order); every period sheet and the DCF are laid out and written (`ctx.finalize()`); each placeholder is replaced by `build_side_build`; the Tearsheet is built; a second `finalize()` writes cell notes. A side build can therefore reference any build or statement row, and nothing references a side build except formulas you write yourself.

## 2. The spec

One object per tab inside `spec["side_builds"]`:

| Key | What it does |
|---|---|
| `name` | sheet title; required |
| `zoom` | `zoomScale` when truthy (70 on the ARPU Bridge, 49 on the wide Margin Bridge) |
| `widths` | `{"B": 59.875, "C": 9.375, ...}` column widths; defaults A = 2.0, B = 56.0, other columns Excel's default |
| `cells` | list of cell objects, written in order; a later entry at the same address overwrites an earlier one |
| `merge` | ranges such as `"B2:C2"`, merged after the cells are written; the top-left cell keeps the value, no wrap is set |
| `period_tables` | see the warning at the end of this section |

Gridlines are always off. `exports` appears in the module docstring but nothing reads it; driver links name cells directly.

Cell object:

| Key | Effect |
|---|---|
| `cell` | A1 address, e.g. `"C7"` |
| `value` | label (string), number, Excel formula (string starting with `=`), formula with `{tokens}` (section 3), or `null` for a styled empty cell |
| `fmt` | a `styles.NUMBER_FORMATS` key or a literal Excel format; omitted = General |
| `bold`, `italic` | default false |
| `color` | 8-character ARGB font colour (`"FF0000FF"` blue, `"FFFF0000"` red); omitted = colour rule below |
| `fill` | 6-character RGB (`"E8E8E8"`, `FF` is prefixed) or 8-character ARGB |
| `top`, `bottom` | thin border on that edge |
| `align` | horizontal alignment (`"center"`, `"right"`) |
| `note` | cell comment, authored with the Setup author name (`Analyst` when blank); the Setup comment policy does not filter these |

Colour rule (`styles.color_for`), applied whenever `color` is omitted:

| Value | Colour |
|---|---|
| number | blue `FF0000FF` (typed input) |
| formula without `!` | black (calculation) |
| formula with `!`, including every resolved token | green `FF008000` (link) |
| label, `null` | black |

Two consequences. A typed input written as arithmetic (`=0.0621895854934938*10000`, `=(5.36/5.06-1)*10000`) is a formula and comes out black: set `"color": "FF0000FF"` on it, as the Spotify specs do, so it reads as an input. Never set blue on a formula containing `!`: `verify` scans every cell from column D rightwards on every tab except Tearsheet and the dividers, and reports a cross-sheet link coloured blue or a local formula coloured green as a colour violation (column C is outside the scan; follow the rule there anyway). Red text is for the analyst's own commentary only.

Formats you will use (`styles.NUMBER_FORMATS`; a key avoids escaping backslashes and quotes in JSON):

| Key | Excel format | Use |
|---|---|---|
| `bps` | `0"bps";\(0"bps"\)` | bridge steps, subtotals, deltas (the Spotify specs spell the literal string; same format) |
| `bps_delta` | `#,##0" bps";\(#,##0\)" bps";\-` | the builds' delta rows; not used on bridges |
| `pct_plain` | `0.0%` | margins, growth rates, hand-off percentages |
| `pct` | `0.0%;\(0.0%\);\-\%` | the builds' style; shows `-%` for zero |
| `amount` | `#,##0;\(#,##0\)` | currency amounts in mm |
| `price` | `\€0.00;\(\€0.00\)` (symbol follows the reporting currency) | per-unit prices such as ARPU |
| `weight` | `0%` | whole-percent inputs (Margin Bridge I3) |
| `mult`, `int`, `general`, `date`, `number1`, `number2`, `number4` | `0.0\x`, `0`, `General`, `mm-dd-yy`, `0.0`, `0.00`, `0.0000` | as named |

Any other literal format passes through, e.g. `"mmm-yy"`. JSON has no date type: `"2026-09-01"` is written as text, so type a date as `"=DATE(2026,9,1)"` with `"fmt": "mmm-yy"` (black, a formula) or use a label such as `"Sep-26"`. A number cell without `fmt` shows a bare integer or decimal.

Notes become comments in the model, so use `note` only for text the analyst asked to have there. `verify` runs the fingerprint regex `claude|anthropic|openpyxl|auto-?generated|generated by|chatgpt|gpt-|llm` (case-insensitive substring) over every string and comment, labels included; one hit fails the build.

**`period_tables` does not build.** `_period_table` imports `coordinate_from_string` from `openpyxl.utils`, which does not export it in openpyxl 3.1 (it lives in `openpyxl.utils.cell`), so a spec with any `period_tables` entry stops `build` with `ImportError`. Write period rows as cells, as the ARPU Bridge does at I13:AB14 (bold period labels on one row, values beneath). For when the import is corrected: `{"anchor": "H13", "from": "3Q25", "lines": {"ab_contrib": {"label": "...", "fmt": "bps", "bold": true, "values": {"3Q25": 13.5, "FY2025": "=I14+J14"}}}}` writes the axis labels from `from` to the end of the axis (`3Q25`, `4Q25`, `FY 2025`, ..., `FY2030E`) in the anchor row starting one column right of the anchor, then one row per line with the label in the anchor column; values follow the colour rule, `fmt` defaults to `bps`, `bold` to true, and values there are not token-resolved.

## 3. Tokens inside cells

A `value` that starts with `=` and contains `{` goes through the engine's resolver (`SheetBuilder.resolver`), anchored at the first column of the model axis (the first history quarter). The tab has no period columns, so **every token needs an explicit period**: `{id@1Q27}`, `{id@FY2025}`, with the canonical ids of `.map.json`'s `columns` (an `E` suffix is tolerated). The result is written as a normal cross-sheet formula and coloured green.

| Token in the spec | Written to the cell (Spotify rebuild) |
|---|---|
| `={Revenue Build!prem_rev@FY2025}` | `='Revenue Build'!R23` |
| `={prem_rev@FY2025}` | the same: without a sheet the id is searched in the order Revenue Build, Margin Build, Income Statement, Balance Sheet, Cash Flow Statement, Drivers & Casing, DCF |
| `={Margin Build!prem_gp.pct_of@4Q25}` | `='Margin Build'!Q76` (a variance sub-row: `<line>.<sub>`) |
| `={Revenue Build!ext.consensus.prem_arpu.pct_yoy@1Q27}` | the consensus row of a delta block (`ext.<source lower-case>.<line>.<sub or level>`; `.delta` appended is the delta row) |
| `={Revenue Build!prem_rev@FY2025$}` | `='Revenue Build'!$R$23` (absolute) |
| `=({Margin Build!prem_gp.pct_of@FY2026}-{Margin Build!prem_gp.pct_of@FY2025})*10000` | `=('Margin Build'!W76-'Margin Build'!R76)*10000` |
| `={row:prem_rev}` | `=23`, the row number (for INDEX/OFFSET constructions) |

The sheet name is a preference, not a constraint: when the id is not on that sheet the lookup order finds it elsewhere. Ids that exist on several sheets (`total_rev` on Revenue Build and Income Statement) need the sheet name. Line ids are the `lines` keys of `.map.json`; an unknown id stops the build with `KeyError: line 'x' not found (from ARPU Bridge, token 'x@FY2025')`.

What does not resolve. These leave the cell **empty, with no error and nothing for `verify` to catch**, so look at the tab after every build (snapshot, or read the cells with openpyxl):

- a token without `@period`: it resolves to the first history column (`{prem_rev}` became `='Revenue Build'!D23`), never what a bridge wants;
- relative offsets `@py`, `@pq`, `@-1`;
- `{drv:...}`: the Drivers & Casing axis starts at the first quarter of the last actual fiscal year, which the anchor is not on (unless history starts there);
- `{sumq:}`, `{avgq:}`, `{lastq:}`, `{firstq:}`: the anchor is a quarter, so reference the FY column directly (`@FY2025`);
- a period outside the axis (`@FY2031` when the horizon ends at FY2030).

Everything else in a formula is plain Excel, written as given: `=(C3-C4+C5)*3/C6`, `=$C$29-E36`, `=AVERAGE(5.36,5.45)`. Cell addresses inside the tab are stable because the tab is static.

## 4. Linking the driver's Base case

On Drivers & Casing a cased driver has a title row, one row per case in the order of `spec["cases"]`, then a bold `Active` row whose `SUMIF` picks the case named in B5. Case rows hold a value for every estimate quarter and every annual-only year (`FY2029E`, `FY2030E`); the FY columns of quarterly years stay blank. The Base-case cell of a period holds whatever `drivers[i].values.Base[pid]` says: a number, or a formula string written verbatim. A formula with `!` is painted green by the colour rule, so the link needs no styling.

The link is plain Excel with the tab name quoted, one output cell per period, scaled to the driver's unit:

| Driver (`fmt`) | Tab unit | Base-case formulas |
|---|---|---|
| `prem_arpu_g` (`pct_plain`) | bps | `='ARPU Bridge'!F3/10000` for 1Q27, `F4` 2Q27, `F5` 3Q27, `F6` 4Q27, `F8`..`F11` 1Q28..4Q28 |
| `prem_gm` (`pct_plain`) | decimal | `='Margin Bridge'!J36` 3Q26, `J37` 4Q26, `J39`..`J42` 1Q27..4Q27, `J44`..`J47` 1Q28..4Q28, `J49` FY2029, `J50` FY2030 |

Two ways to get the formulas into the spec:

1. **Driver Grid** (the durable record): the analyst, or you with openpyxl, puts the formula text in the Base row of the driver under the period column (`1Q27E` ...). `read_inputs` passes any string that starts with `=` through unchanged (only `5%`-style and numeric strings are converted), so it reaches `values.Base`. Enter it as text (a leading apostrophe): the inputs workbook has no sheet called `ARPU Bridge`, and Excel would otherwise try to resolve the name as an external workbook.
2. **`model_spec.json`** directly, through the merge snippet of section 1, after each `spec` run.

Periods the tab does not cover keep their typed numbers (in the Spotify spec `prem_arpu_g` Base holds numbers for 3Q26 and 4Q26 and bridge links from 1Q27). The other cases stay typed numbers: a bridge argues the Base case only.

After the build: `.map.json` `drivers[id]` is the driver's Active row; the Base row is three rows above it with five cases, two with three; `drivers_columns` maps period ids to columns. Confirm those cells are green formulas and that the Active row equals them with B5 = Base, then run `verify` (`ok` must be true) and `cases`. On a roll-forward, add hand-off rows for the new periods and extend `driver_links`.

## 5. The Spotify examples

Both specs sit in `side_builds` of the rebuilt model's spec; every cell carries `fmt`, `bold`, `italic`, `color`, `fill` (`null` where unset).

### ARPU Bridge (feeds `prem_arpu_g`, "Premium ARPU Growth y/y Ex. Add-ons")

`zoom` 70; widths A 2.0, B 59.875, C 9.375, D 9.0, E 37.0, F 9.0, G 9.0, H 56.25, I 9.0 (plus V 10.875, AD 9.0); merges `B2:C2`, `B23:C25`, `B34:C35`. Read left to right:

| Area | Content |
|---|---|
| B2 | title `27E Pricing Increase ARPU Bridge`, bold |
| B3:C6 | US pricing walk: `(+) Seq CC y/y ARPU Accel. Between 1Q26 and 2Q26` 170, `(-) Incr. QoQ Contribution from Add-ons for 2Q26` 14, `(+) Lapped Benelux Tailwind` 10 (blue italic, `bps`), `Net Number of Months in (2Q26 - 1Q26) With U.S Px Incr` 2 (blue italic, no format) |
| B7:C7 | `Net Impact of U.S Pxing Increase` `=(C3-C4+C5)*3/C6`, bold, fill `E8E8E8` |
| B8:C11 | the same walk for the international increase; output C11 `=(C8-C9)*3/C10`, fill `E8E8E8` |
| B12:C13 | `Street Est. CC ARPU y/y 2027E ex. Px Incr` 200 (input), `Total ARPU y/y CC growth` C13 `=C12+C11+C7` (bold, fill `E8E8E8`) |
| B14:C15 | `(-) Contribution y/y ARPU Growth from Add-ons 27E Base Case` C14 `=U14` (blue italic), `Total ARPU y/y CC growth Ex. Add-ons` C15 `=C13-C14` (bold, fill `E8E8E8`) |
| E2:F14 | `Our Estimates` (bold italic header): Q1 27..Q4 27 in F3:F6 as `=0.0621895854934938*10000` etc. (blue italic, `bps`), FY 27 F7 `=C15`, Q1 28..Q4 28 F8:F11 numbers, FY 28 F12 `=C33`, FY 29 500, FY 30 250 (bold) |
| H14, I13:AB14 | period labels `3Q25` .. `FY2030E` in I13:AB13 (bold), `Premium ARPU Growth Contribution from Add Ons y/y` in H14 with one value per period in I14:AB14 (bold italic, `bps`) |
| B17:C22 | street estimates Q1 27E..FY 27E (italic blue; FY row bold italic), `Our Δ to Street` C22 `=C13-C21`, bold italic, fill `FFFF00` |
| B26:C33 | FY28 block: street estimates typed as `=(5.36/5.06-1)*10000` (blue italic), `Our Estimate` C31 `=C30+C22*4/5`, add-on contribution 127, `28E ARPU y/y Ex. Add-ons CC` C33 `=C31-C32` |
| B23, B34 | the analyst's red italic commentary (merged), carried over from their model |

The Base case links to F3:F6 and F8:F11 divided by 10000. In a fresh build the I14:AB14 row should be tokens, one per cell (`={Revenue Build!arpu_addon_contrib@3Q25}` ...; that line is already in bps), and the street cells can link to the consensus rows: `=({Revenue Build!ext.consensus.prem_arpu.pct_yoy@1Q27})*10000` reproduces C17 (588bps).

### Margin Bridge (feeds `prem_gm`, "Premium Gross Margin")

`zoom` 49; widths A 1.875, B 61.375, C 13.0, D 19.0, E 29.375, F 25.375, G 16.875, I 17.25, J 16.875; merges `B2:C2`, `B19:C23`, `B24:C24`. Four blocks:

| Area | Content |
|---|---|
| B2:C18 | marketplace contribution bridge: C3 street GM contribution 72 (`bps`), C4 2025 GP contribution 640 (`amount`), C5 `={Revenue Build!prem_rev@FY2025}` (the only token: a green link to FY2025 Premium Revenue), C6 `=C4/C5*10000`, C7 `=C6+C3`, C8 `=C7+C3`, C9:C10 typed growth 0.1499 / 0.154 (`0.0%`; better as `{Revenue Build!prem_rev.pct_yoy@FY2026}`), C11:C12 implied GP growth (bold), C13 historical CAGR 0.41 (blue), C14 `Our Estimate` `=C13+(I6/10000)` (bold), C15 `=C6*(1+C14)/(1+C9)`, C16 `∆ to street` `=(C15-C6)-(C7-C6)` with fill `FFFF00` on B16 and C16, C17:C18 the same for 27E |
| E2:G7, I2:I6 | ISRCs uploaded per day by year (F blue inputs, G `=F4/F3-1` in `0.0%`), key input I3 0.04 (`0%`, fill `FFFFCC`), I6 `=I3*G7*10000` (`bps`, bold) |
| B24:C33 | pricing increase margin bridge: C25 160 (input), C26 `=(C15-C6)/4`, C27 40, C28 50, C29 `=C25-C26-C27+C28` (bold), C30:C33 `∆ to street 26E`..`29E` `=$C$29-E36` etc. (bold), labels bold italic on `FFFF00` |
| B35:G48 | street table: C `Prem GM %` (blue, `0.0%`), D `y/y change in GM` (blue, `bps`), E `Street Accretion from Pxing` `=D36-$C$3`, F `Our Estimates y/y` `=D36+C16` and `=D41+C31+C18`, G `∆ to street` `=F36-D36` with fill `FFFF00`; FY rows bold |
| I35:J50 | `Our Estimates` hand-off: `Q3 26 Prem GM %` J36 0.3497 .. `Q4 28 Prem GM %` J47 (blue, `0.0%`), FY rows J38 `=C36+0.28%` (forced blue), J43, J48 (bold, not linked), `FY 29` J49 0.39, `FY 30` J50 0.392 |

The Base case links to J36, J37, J39:J42, J44:J47, J49, J50 with no scaling. The hand-off column is the pattern to copy: one row per driver period, in period order, so the links read straight down.

## 6. From the analyst's paragraph to a spec

1. Read the Side Builds row: tab name, driver id, paragraph. Look the driver up on the Drivers tab: its `format` sets the scaling of the link, and its estimate quarters and annual-only years are the hand-off cells you need (Driver Grid headers, or `drivers_columns` in `.map.json` after a first build).
2. Split the paragraph into inputs (numbers the analyst states, with units), calculations (how they combine), the output per period, and comparisons to street or guidance. Ask about anything the paragraph leaves open before "go"; never invent a number.
3. Lay the tab out left to right: B labels and C values for the bridge; E and F for the per-period hand-off (`Our Estimates`); H onwards for a period row taken from the build. Column A stays 2.0; width B to the longest label (56 to 61); value columns 9 to 13.
4. Inputs blue: numbers are blue by the rule; constants typed as arithmetic get `"color": "FF0000FF"`. Anything that exists on the build is a token, not a retyped number: history anchors (`{Revenue Build!prem_rev@FY2025}`), build rows (`{Revenue Build!arpu_addon_contrib@1Q27}`), consensus rows (`ext.consensus...`).
5. Calculations black: plain Excel, one row per step, labels prefixed `(+)` / `(-)`. The output cell: bold, fill `E8E8E8`, `top` and `bottom` borders, label bold.
6. Comparisons to street: typed street figures italic blue (FY rows bold italic); the delta cell bold with fill `FFFF00` on label and value, labelled `∆ to street`.
7. Hand-off cells: one per driver period, in period order, in the driver's unit or with `/10000` in the link; FY rows of quarterly years are not linked (bold, for reading only).
8. No explanatory text beyond labels and the title; no sources, no notes of your own. The analyst adds commentary later; the red merged paragraphs in the Spotify tabs are theirs.
9. Save the JSON file, merge, `build`, look at the tab (every cell meant to hold a formula must be non-empty), write the links, rebuild, `verify`, `cases`, snapshot.

Skeleton for a one-column bridge with a hand-off column:

```json
{"name": "Price Bridge", "zoom": 70, "widths": {"A": 2.0, "B": 58.0, "C": 11.0, "E": 30.0, "F": 11.0},
 "merge": ["B2:C2"],
 "cells": [
  {"cell": "B2", "value": "27E Pricing Bridge", "bold": true, "top": true, "bottom": true},
  {"cell": "B3", "value": "(+) Price increase, US, y/y"},
  {"cell": "C3", "value": 300, "fmt": "bps", "italic": true},
  {"cell": "B4", "value": "(-) Mix drag from add-ons"},
  {"cell": "C4", "value": "={Revenue Build!arpu_addon_contrib@FY2027}", "fmt": "bps", "italic": true},
  {"cell": "B5", "value": "Net pricing contribution", "bold": true, "top": true, "bottom": true},
  {"cell": "C5", "value": "=C3-C4", "fmt": "bps", "bold": true, "fill": "E8E8E8", "top": true, "bottom": true},
  {"cell": "B7", "value": "FY 27E Street Estimate", "bold": true, "italic": true},
  {"cell": "C7", "value": "=({Revenue Build!ext.consensus.prem_arpu.pct_yoy@FY2027})*10000", "fmt": "bps", "bold": true, "italic": true},
  {"cell": "B8", "value": "∆ to street", "bold": true, "italic": true, "fill": "FFFF00"},
  {"cell": "C8", "value": "=C5-C7", "fmt": "bps", "bold": true, "fill": "FFFF00"},
  {"cell": "E2", "value": "Our Estimates", "bold": true, "italic": true},
  {"cell": "E3", "value": "Q1 27 ARPU y/y"},
  {"cell": "F3", "value": "=C5*0.9", "fmt": "bps", "italic": true},
  {"cell": "E4", "value": "Q2 27 ARPU y/y"},
  {"cell": "F4", "value": "=C5", "fmt": "bps", "italic": true}
 ]}
```

with `"driver_links": {"prem_arpu_g": {"1Q27": "='Price Bridge'!F3/10000", "2Q27": "='Price Bridge'!F4/10000"}}` in the same file.

## 7. Formatting conventions for bridges

| Element | Style |
|---|---|
| Title | B2 bold, merged `B2:C2`; the reference adds `top` and `bottom` borders |
| Second block title | bold label in B (Margin Bridge B24), merged with C |
| Bridge step | label `(+) ...` / `(-) ...`; value italic blue with `fmt` `bps` (counts such as months unformatted) |
| Subtotal / output | bold black formula, fill `E8E8E8`, `top` + `bottom`; label bold |
| Delta to street | label `∆ to street` (`∆` U+2206, as the builds' delta rows) bold italic, value bold, fill `FFFF00` on both cells, `fmt` `bps` |
| Street inputs | italic blue; FY rows bold italic; quoted prices as `=(5.36/5.06-1)*10000` with forced blue |
| Hand-off cells | blue (italic for quarters, bold for FY rows), `bps` or `pct_plain` to match the driver, one period per row |
| Percentages | `pct_plain` (`0.0%`); `0%` for whole-percent key inputs |
| Key single input | fill `FFFFCC` (light yellow), as on the Driver Grid |
| Period row | bold black labels in the axis spelling (`3Q25`, `FY 2025`, `3Q26E`, `FY2029E`), values beneath |
| Table column headers | bold; grey band `E8E8E8` on a delta column header (Margin Bridge G35) |
| Commentary | none from you; the analyst's own text is italic red `FFFF0000`, merged across B:C |
| Zoom and widths | 70 (49 when the tab is wider than a screen); A 2.0, B 56 to 61, values 9 to 13, a second label column 30 to 56 |

Every number cell gets a `fmt`; a bps value without one shows as a bare integer, and a link to a `pct_plain` driver reads as 0.0% on Drivers & Casing whatever the bridge shows.
