# Pre-build review checklist

Run this after `spec` has written `model_spec.json` and `model_data.json` and before the analyst says "go". The engine writes whatever the spec says and never complains: a blank driver cell becomes a zero, an unmatched data label becomes a plug or a flat line, a wrong sign flows through every statement. This review is the only step that reads the numbers the way an analyst would. It ends in one message with three parts: defects you will fix before building (mappings, periods, spec wiring, never an estimate), questions the analyst must answer, and notes they should know. Then wait for "go".

`fmb` below means `python "${CLAUDE_SKILL_DIR}/scripts/fmb_cli.py"`. One-line Python snippets are written for the Bash tool.

## Contents
1. Files and the dry run
2. Data and history
3. Fiscal calendar and horizon
4. Revenue and cost trees
5. Drivers and the Driver Grid
6. Plug lines
7. Statements: signs, balances, shares, tax, non-GAAP, working capital
8. DCF inputs
9. Tearsheet
10. Things the analyst may have forgotten
11. Writing the review message

## 1. Files and the dry run

| File | What it holds for the review |
|---|---|
| `model_data_raw.json` (from `parse`) | `lines[]` with `label`, `section`, `values`, `suspect`; `periods{pid: {end, estimate}}`; `files` |
| `<TICKER>_model_inputs.xlsx` | Setup, Revenue Tree, Cost Tree, Drivers, Variance & Deltas, Statement Mapping, Driver Grid, Multiples, DCF Inputs |
| `model_spec.json` | `company`, `horizon`, `cases`, `drivers[]` (`values[case][pid]`), `sheets[sheet].blocks[]`, `dcf`, `tearsheet`, `comments_policy` |
| `model_data.json` | one series per model line id, actual quarters only; every plug series lives here |

A dry run is allowed and cheap: build into the scratch folder, never into `models/`, and never deliver it.

    fmb build model_spec.json model_data.json --out <scratch>/review_build.xlsx
    fmb verify <scratch>/review_build.xlsx      # recalculates in Excel and saves cached values
    fmb summary <scratch>/review_build.xlsx     # Total Revenue, Operating Income, EBITDA, Net Income, EPS lines for estimate columns

`verify` returns `static.issues`, `colour_violations`, `fingerprints`, `recalc.errors` (error cells), `recalc.checks` (every row labelled `check`/`Check`: `bs_check`, `cash_check`, the Margin Build `op_inc` check) and `ok`. A check row that is non-zero in a historical column is a mapping or sign problem (sections 2, 4, 7) and belongs in the review, not in the fix-after-go loop. `summary` prints `null` until a recalc has cached values, so run it after `verify`; without Excel, read `model_data.json` and the spec instead.

Period axis with weeks, as the engine will build it:

    python -c "import sys,json;sys.path.insert(0,r'${CLAUDE_SKILL_DIR}/scripts');from fmb.build_model import make_axis;s=json.load(open('model_spec.json'));[print(p.pid,p.end,p.weeks,'E' if p.estimate else 'A') for p in make_axis(s).periods]"

## 2. Data and history

- **Suspect values.** Check: `python -c "import json;d=json.load(open('model_data_raw.json'));print([(l['label'],l['section'],l['file']) for l in d['lines'] if l['suspect']])"`. The Bloomberg PDF export drops decimal points (7300 for 73.0). One wrong SBC row poisons `sbc`, `total_sbc`, `cf_sbc`, `ebitda_ex`, `adj_other` (adjusted OI minus GAAP OI minus SBC), the `other_op` cash-flow plug and `adj_tax_rate`. Fix the value in `model_data_raw.json` (divide by 100 after confirming against another file or the analyst) and re-run `spec`. Say: "Bloomberg shows SBC of 7,300 in 1Q25; I read it as 73.0 (dropped decimal). Confirm?"
- **Label collisions.** `series()` merges every data line with the same label when the Statement Mapping row has no `Data section`, and for actual periods the last line in the file wins. Bloomberg uses "Accounts Receivable", "Accounts Payable", "Accrued Liabilities", "Inventory", "Net Income", "Depreciation & Amortization" and "Other Assets" both as balances and as cash-flow changes. Check: compare `receivables`, `payables`, `accrued`, `inventory`, `prepaid` in `model_data.json` with the balance-sheet section of the raw data (a receivable of 46 next to a reported 699 is the cash-flow change). Fix: set `Data section` (column E) on the Statement Mapping tab and re-run `spec`. Say what you remapped; no question needed.
- **GAAP vs adjusted sections.** Bloomberg carries "Income Statement (Adjusted)" and "GAAP Results" with the same labels. `op_inc` prefers "GAAP Results"; cost-tree lines use whatever `Data section` says. If opex comes from the adjusted section, the `other_opex` plug absorbs the GAAP-adjusted gap every quarter. Check: `other_opex` in `model_data.json` is small and sporadic, not a steady amount close to SBC plus amortisation.
- **File vintages.** Each Bloomberg file has its own as-of date; quarterly and annual files pulled on different days give deltas against different consensus vintages. Check the date of each file (its header, file name or modification time) and say the dates in the review.
- **History length.** `horizon.first_hist_quarter` vs the three-year default. Short history (ILMN: six quarters from 1Q25) means `% 2y stack` rows (`needs: py2`) stay blank, the first historical FY has no y/y, and Drivers & Casing starts at the first quarter of the last actual fiscal year with only that year as realised context. Say so once; it is a note, not a question.
- **Recomputed history vs reported.** `pretax`, `ni`, `total_rev` and the statement subtotals are formulas even in history (`eps_basic`/`eps_dil` show reported values there). Check per actual quarter: `op_inc` plus `interest_income`, `interest_expense`, `other_nonop` equals reported "Pre-Tax Income"; less `tax` (and `nci`) equals reported "Net Income"; divided by `shares_dil` equals reported "Diluted EPS". A mismatch is a sign or mapping problem (section 7), fixed before go.

## 3. Fiscal calendar and horizon

- **Period ends.** `horizon.period_ends` comes from the exports; missing ends are month ends from `company.fiscal_year_end_month`. Row 8 shows the end date, row 9 the weeks (13 or 14 per quarter, 52 or 53 per year, first quarter always 13). Print the axis (section 1) and list every quarter with 14 weeks and every year with 53. When Bloomberg and CapIQ disagree on a period end (Bloomberg projected 3Q26 to 2026-10-04, CapIQ's filed balance sheet says 2026-09-27), the reported date wins in `merge()`; check the 10-Q and say which quarter carries the 53rd week. `{weeks}` enters only working-capital balances (`*13/{weeks}`) and custom formulas; `{months}` stays 3 or 12, so `volume_price` per-month lines and `cost_per_unit` lines do not scale for the extra week. Say: "FY2026 is a 53-week year (3Q26 has 14 weeks). Does your 3Q26 growth include the extra week, and does 3Q27 lap it?"
- **Non-December year ends.** Fiscal years are named by the calendar year in which they end (`fiscal_quarter_end`); Bloomberg labels follow the same rule, some companies do not. The Multiples tab proposes target dates as `YYYY-12-31` regardless of the year end. Say which date "FY2027" ends on and ask whether target dates should move to the fiscal year end.
- **Horizon.** `last_quarterly_estimate` beyond the data's `last_estimate_quarter` leaves delta rows blank there (consensus values exist only where the data has them). `annual_only_years` must cover every Tearsheet `metric_period` and the DCF terminal year, which is the last column of the axis. The fiscal year of the last actual quarter is an estimate year (grey band, FY column `E`); the DCF discounts its full-year UFCF with a half-year stub from `valuation_date` while the bridge takes the balance sheet of the last actual quarter, so cash generated in its actual quarters is counted twice; the reference model does the same. Say it as a note. `horizon.report_dates` is always empty from `spec`; row 10 (Earnings Report) stays blank unless you add dates to the spec before building.

- **Annual history columns.** When `annual_hist_years` is set, list which lines have no value in those columns (segments and KPIs the CapIQ export lacks and the Bloomberg annual printout does not cover; `python -c "import json;d=json.load(open('model_data.json'));print([k for k,v in d.items() if isinstance(v,dict) and 'FY2021' not in v])"`), where CapIQ and the Bloomberg annual printout disagree on the same line (CapIQ wins; SG&A is a known case because CapIQ reclassifies amortisation), and the one-offs the plug lines absorbed in those years (goodwill impairments sit in `other_nonop_plug`). Say: "FY2021-FY2024 are annual columns from CapIQ; segment revenue before FY2023 is not available, so Product and Service are blank there and Total Revenue is typed."

## 4. Revenue and cost trees

- **Segments sum to totals.** `total_rev` and every `sum` node are pure sums, in history too; a `sum` node with its own data label keeps its history only for the `% yoy` rows. Check per actual quarter that the top-level lines add to reported "Revenue" and that each parent's data label equals the sum of its children (`model_data.json`). A gap shows up as a non-zero Margin Build `Check` row and as a y/y jump at the first estimate. Say: "Segments sum to 1,041 vs reported 1,041 in 1Q25 (ties); consumables plus instruments leave 12 unexplained in 4Q25: add an 'Other' line (`direct` or `growth`) or accept?"
- **COGS segment ids.** `Segment (revenue line ID)` on the Cost Tree must equal a top-level revenue id; otherwise the line's base falls back to `m_total_rev` silently. Check each `cogs_*` line's `proj_dsl` in the spec names the intended `m_<segment>`.
- **History the driver type needs.** `yoy_pct`, `qoq_pct`, `net_adds`, `bps_qoq`, `bps_yoy` and `flat` project from the prior period, so the line must have a series in `model_data.json` for every actual quarter; with none, the first estimate multiplies a blank cell and the line is zero. `pct_of_base`, `gm_pct`, `absolute`, `pct_level` need no history; `cost_per_unit` needs its volume line on the Revenue Build; `custom` needs whatever it references. Check: every revenue, KPI and cost line id is a key in `model_data.json` with no missing actual quarters, else ask for the KPI History tab.
- **Kinds and units.** `volume_price` revenue = volume x price (x `{months}` when `Price basis` is "per month"): volume units x price units must give reporting units. `share` lines need a driver whose target is the line (it feeds the `% of <parent>` row); without one the build stops with `driver 'None' not found`. KPI `fy_rule` defaults: count and price average, pct takes the last quarter, amount sums; say which rule each KPI got.

## 5. Drivers and the Driver Grid

- **Blank cased cells are zeros.** The Active row is a SUMIF over the case rows, so an empty cell for the chosen case gives 0: `yoy_pct` 0% growth, `gm_pct` 0 (gross margin 0%), `pct_of_base` 0 (no opex), `absolute` 0. Uncased drivers carry the prior year forward only in annual-only years; an empty estimate quarter is blank. Check: `drivers[*].values[case]` holds every estimate quarter and every annual-only year for every case. Say: "Bull is empty for FY2029E-FY2030E on `gm_pct`; that would print a 0% gross margin. Fill it, or copy Base?"
- **Input units.** `%` drivers are decimals (0.05) or typed with the % sign; `bps` drivers are in bps (50 means 50 bps, divided by 10,000 in the formula); amounts are in reporting units (`units`, normally mm). The grid formats `%` as `0.0%`, so 5 typed for 5% shows 500.0%: list any growth or margin value outside -1..1.
- **Compare with realised history.** The grid shows grey history only for level drivers with a target line and no sub-row; growth drivers, margin drivers and working-capital ratios show nothing. Compute realised y/y growth, `% of revenue` and ratios from `model_data.json` for the last four to eight quarters, consensus growth from the delta data labels (`value / prior-year value - 1`), and guidance from the Guidance tab. Say with numbers: "Base sequencing consumables growth is 12% from 3Q26E; the last four quarters printed 3%, 5%, 4%, 6% and consensus has 5%. Intended?"
- **Case shape.** Cases should be ordered Disaster <= Bear <= Base <= Bull <= Blowout for growth and margins (reversed for cost ratios); identical rows across cases make the casing pointless and a Base equal to consensus everywhere deserves a question. Check per driver in the spec.
- **Wiring.** User-defined drivers are kept even when no formula references them (`{drv:id}` token or a line's `driver`), and a target that names a line id with a typo becomes `target: null` while the line it was meant for, having no driver, falls back to `flat`. Check every driver id appears in some `proj_dsl`/`driver` in the spec; list orphans and flat lines.
- **`single` drivers.** The constant is typed in the grid's first estimate column; `build_spec` moves it to the first Drivers & Casing column (the first quarter of the last actual fiscal year, 1Q26 when the last actual is 2Q26). Custom formulas reference it with an explicit absolute period: `{drv:peak_px@1Q26$}`. Check the spec shows the value under that period.
- **Parser corrections.** `parse` prints every lost-decimal value it repaired (7300 -> 73.00) and the ones it could not; confirm both lists with the analyst, and check `fy_end_assumed` (true when a CapIQ quarterly export carried no 12-month column, so December was assumed).
- **Custom formulas.** A token that cannot resolve leaves the cell blank (no error). Check custom lines in the dry run for blanks and read the formula text once in Excel.

## 6. Plug lines

The spec builder adds these so history foots; each has a history series in `model_data.json` and a projection rule the analyst must accept or override.

| Id (sheet) | History = | Projection | Ask about |
|---|---|---|---|
| `other_cogs` (Margin Build) | reported cost of revenue minus modelled COGS lines | `={other_cogs@py}`: same quarter last year, forever | amortisation in COGS (fine) vs a one-off that would repeat |
| `other_opex`, `is_other_opex` (Margin Build, IS) | revenue - COGS - opex lines - GAAP operating income | typed 0 in estimate quarters (blue on light yellow, on the Margin Build, not a driver); annual-only years `@py` | recurring legal, restructuring or amortisation: should it be non-zero? |
| `other_ca`, `other_nca_plug`, `other_cl_plug`, `other_ncl_plug`, `other_eq_plug` (BS) | subtotal minus mapped lines | flat `@pq` | a plug near 10% of its subtotal is an unmapped line; `other_eq_plug` holding treasury stock means `buybacks` never reach equity and `bs_check` fails for any non-zero buyback (map "Treasury Stock" or keep buybacks at 0) |
| `other_op`, `other_inv`, `other_fin` (CFS) | CFO/CFI/CFF total minus mapped lines | typed 0 in estimates | suspect values and unmapped investment purchases land here; one-off financing (a 495 in 4Q25) |
| `fx` (CFS) | net change in cash minus the three totals | typed 0 | nothing unless large |
| `adj_other` (IS) | `adj_oi` - `op_inc` - `sbc` - `amort` | driver `adj_other` (uncased) | restructuring and legal add-backs running off |

Check: `python -c "import json;m=json.load(open('model_data.json'));[print(k,v) for k,v in m.items() if k.startswith('other_') or k in ('fx','adj_other','adj_tax_rate')]"`. Say per plug: "History carries 17 a quarter in `other_cogs` (amortisation); the model holds last year's level. Keep, zero, or model it with `amort`?"

## 7. Statements: signs, balances, shares, tax, non-GAAP, working capital

- **Sign conventions.** The cash flow keeps reported signs: `capex`, `buybacks`, `dividends`, `debt_repaid`, `rsu_tax` negative; `stock_issued` and an issuance in `debt_change` positive. Roll-forwards depend on it: `ppe = ppe@pq - capex - dep`, `treasury += buybacks`, `retained += ni + dividends`, `lt_debt += debt_change + debt_repaid`, `apic += sbc + stock_issued + rsu_tax`, `intangibles -= amort`, `fcf = cfo + capex`. Costs and `tax` are positive; `interest_expense` must be negative because `nonop_net` adds its lines; `nci` positive when the minority earns income. Check the typed sign of every cash-flow driver against its history sign in `model_data.json`. Say: "Capex is typed +40; history is -40. A positive capex shrinks PPE and inflates FCF. I will treat it as -40 unless you say otherwise."
- **Balances that go negative.** `intangibles` minus `amort` every quarter, `ppe` when `dep` exceeds `|capex|` for years, `st_inv`/`lt_inv` flat. Check the last annual column in the dry run.
- **Shares and EPS.** `shares_basic`/`shares_dil` are absolute, uncased, FY average. Buybacks typed with a flat share count, or shares falling with no buybacks, is a question. Diluted must be at least basic; `eps_dil = ni / shares_dil`, `adj_eps = adj_ni / shares_dil`; the DCF `diluted_shares` should match the latest `shares_dil`.
- **Tax.** `tax = pretax x tax_rate`, so a pre-tax loss books a benefit; companies with valuation allowances pay tax on losses. Compare the typed `tax_rate` with history (`tax / pretax` per quarter).
- **Non-GAAP block.** Included when the data has adjusted OI or adjusted EPS (`adjusted_block` Auto). `adj_tax_rate` history is `1 - adj_ni / (adj_oi + nonop_net)` and is often unusable (ILMN prints -110%), so the typed rate needs the company's guided non-GAAP rate. `adj_ebitda = adj_oi + dep` (amortisation is already added back; `+ da` when the data has only combined D&A). Check whether the company's non-GAAP results exclude SBC: most do (Setup `adj_sbc_addback` = Y, the `(+) Stock-Based Compensation` row is in the reconciliation); Illumina does not, so set N, otherwise projected adjusted OI and EBITDA run above the company's definition and consensus by the SBC amount while `adj_other` history absorbs the difference as a steady negative close to SBC. The Tearsheet values on `ebitda` or `adj_ebitda` only (`tearsheet.metric_line`); the Setup `valuation_metric` choice is not applied, so say so before building if the analyst chose P/E, EV/Sales, EV/EBIT or P/FCF.
- **Working capital.** `recv_pct`, `inv_pct`, `prepaid_pct`, `pay_pct`, `accrued_pct`, `defrev_pct` are the balance as a share of the quarter's revenue, COGS or COGS plus opex, normalised to 13 weeks (`drv x base x 13/{weeks}`); the `wc_*` cash-flow lines then equal minus the change in the asset or plus the change in the liability. Compute the realised ratio (balance / quarterly base x weeks/13) for the last four quarters and compare; a ratio typed as an annual share (receivables 15% of annual revenue) understates the balance four-fold. A `wc_*` line whose balance is not on the balance sheet becomes a typed 0.
- **Interest and D&A.** `interest_expense` vs the debt balance and maturities (`st_debt` is due within a year), `interest_income` vs cash; `dep`/`amort` (or `da`) vs capex and the intangible balance; `cf_da` links to the IS lines.
- **Lines the data lacks are dropped.** A cash-flow or balance-sheet line without history (no "Dividends Paid", no "Treasury Stock") does not exist in the model and its default driver is dropped. Say: "The data has no dividend line; if one is coming, we need a mapped series before the build."

## 8. DCF inputs

- **Rates.** `rfr`, `erp`, `kd_after_tax`, `equity_weight`, `tax_rate` as decimals; `beta` around 0.8-1.6. `Ke = rfr + beta x erp`, `WACC = we x Ke + (1 - we) x kd`; a blank input gives WACC 0 and discount factors of 1 with no error. Check none is blank and WACC lands in a sane range (typically 7-12%).
- **Valuation date.** ISO `YYYY-MM-DD`, after the last actual quarter end and before the end of the first estimate fiscal year; the stub is `(FY end - date)/2/365`, negative otherwise. Default is the day `inputs2` ran, which may be stale.
- **Exit multiples.** `dcf.exit_multiples` per case, ordered Disaster <= Bear <= Base <= Bull <= Blowout (a formula such as `=(G52-G50)/2+G50` is allowed). They apply to the last axis column's EBITDA (`FY2030E` with annual-only years 2029-2030), so blank annual-only driver cells (section 5) hit the terminal value directly. DCF `tax_rate` should agree with the IS `tax_rate` driver.
- **Bridge.** `dcf.bridge.cash_lines` and `debt_lines` must be balance-sheet line ids (`cash`, `st_inv`, `lt_inv`; `st_debt`, `lt_debt`, `lease_liab_cur`, `lease_liab`); unknown ids are skipped silently. Ask whether operating lease liabilities belong in debt given where lease cost sits in EBITDA. The balance is the last actual quarter's. `diluted_shares` blank gives `#DIV/0!` in the implied price; `fx_rate` is reporting-to-trading (EUR reporting, USD trading: 1.13, not 0.88).
- **Sanity.** Implied price within a plausible band of the current price, terminal value share of EV, UFCF trend. Say: "Base DCF gives 312 vs 205 today with TV at 78% of EV; the exit multiple of 16x does most of the work."

## 9. Tearsheet

- **Blocks.** At most two (`blocks[:2]`). Each needs `label`, `basis` (NTM or YE), `target_date` (ISO, after `valuation_date`; IRR uses `YEARFRAC` from the DCF date) and `metric_period` on the axis; a period off the axis leaves the metric cell blank and the price target collapses to `(cash - debt) / shares`. `multiple_label` prints "NTM Multiple" whatever the basis.
- **Multiples.** `tearsheet.multiples[case][block]` should fall Blowout > Bull > Base > Bear > Disaster and the later block should not exceed the earlier one without a reason. The sensitivity grid needs `min <= Base <= max` with a step from 5, 2.5, 2, 1, 0.5, 0.25, 0.1, 0.05 that divides both gaps within 25 columns (else seven equal steps); Base at the minimum or maximum gives a one-sided grid.
- **Weights and R/R.** `tearsheet.weights` must sum to 1 (defaults 10/20/40/20/10 or 25/50/25). R/R = average upside of the top `ceil(n/2)` cases (three of five, two of three) divided by the worst case's downside, so Disaster (and usually Bear) must sit below the current price or the ratio is meaningless.
- **Price.** `price.source` writes `=IFERROR(BDP(...),F39)`, `CIQ(...)` or `FDS(...)` in D39 with the typed `current_price` in F39 as fallback; a blank fallback makes every upside `#DIV/0!` on a machine without the add-in. Check `ticker_code` format (Bloomberg `ILMN US Equity`, CapIQ `ILMN`, FactSet `ILMN-US`), `current_price` and `price_date`.
- **Current multiple period.** `current_multiple_period` must be on the axis (default FY after the last actual). Per-case metric values are typed only by `cases` after the build; until then every case shows the active case's metric.

## 10. Things the analyst may have forgotten

Read the folder's notes on the company, then check each item against the inputs. Raise only the ones the notes or the data make relevant.

- **Business.** New product lines or segments mentioned in calls but absent from the Revenue Tree; announced pricing actions with no price driver; seasonality when `qoq_pct` drivers are used; guidance vs Base for every guided metric.
- **Capital allocation.** Buyback authorisation and remaining capacity vs `buybacks`; debt maturities within the horizon (`st_debt` is due within a year) vs `debt_change`; convertibles and dilution vs `shares_dil`; a dividend that is coming; acquisitions typed 0.
- **Below the line.** Restructuring charges running off (`other_opex`, `adj_other`); tax-rate changes; leases in debt; `nci` carried at `@py`; FX (reporting vs trading currency, FX in revenue growth).
- **Delta rows.** A delta row exists only where its `values` are non-empty in the spec; rows without values are dropped silently. The Guidance and Buyside tabs are read but not wired into delta rows, which take values from a data label in the parsed data, so a "delta to guidance" row needs its numbers in a data file or typed into the spec's `deltas` block before the build.
- **Housekeeping.** `comments_policy` vs the notes typed in the grid ("I will add my own" drops them); `author` set (otherwise notes and file properties say "Analyst"); `cover_tab` name; `model_file` name and the `models/` folder.

## 11. Writing the review message

- One message, three headed parts: "Fixing before build" (what you change and why, no question), "Questions" (numbered), "Notes". Keep each question to one decision.
- Put the evidence next to the input: the typed value, the realised history, consensus or guidance, with the source and period in light citations ("3Q25 call", "Bloomberg 2026-11-02").
- Describe consequences, not verdicts: "a 0 gross margin in FY2029E" rather than "wrong". Offer the default you will apply if they do not answer, and never change an estimate yourself.
- Do not re-ask what Setup already settled; do not list items that passed.
- Close with the exact next step: "Reply go and I will build, verify and run cases."
