# ILMN model audit, 3 Nov 2026

This note records a cell-by-cell audit of `Outputs/models/ILMN_model_2026-11-03.xlsx`, covering all 14 tabs, along with the fixes made and the items left for the analyst.

## What was checked

Every non-empty cell was checked for:

- error values and `#REF!`;
- external links;
- cross-sheet links that point at the wrong period column or at an empty cell;
- formulas that break their row's pattern for the same column type;
- blanks inside filled rows;
- hardcoded numbers inside formulas;
- the colour rule (typed = blue, formula = black, link = green);
- fonts, number formats and italics;
- comments, leftover note text and document properties.

## Result

The model is mechanically sound:

- There are no broken references, no external links and no period-misaligned links.
- The balance sheet, cash flow and margin checks are at zero.
- Full-year balance-sheet columns pick up the 4Q balance.
- All comments are the analyst's own notes.

The only error cell is Tearsheet E39. It holds the stock data link, which reads as an error outside a live Excel session.

## Fixes made

1. **Income Statement % YoY growth.** FY2023 and 1Q25–4Q25 were blank. They are now typed in blue from reported prior-period revenue: FY2022 $4,584m, and 2024 quarters $1,076m, $1,112m, $1,080m and $1,104m. DCF FY2023 growth (D12) now links to the FY2023 figure.
2. **Drivers & Casing row 125 (other non-GAAP adjustments).** The 1Q26–3Q26 history now links to Income Statement row 71, like every other driver row.
3. **Drivers & Casing working-capital ratio history (rows 139–151, D:F).** The colour changed from black to green, because these cells link to other sheets.
4. **Balance Sheet plug rows 29, 38 and 45.** The blank 1Q25–3Q26 history is now typed as 0, and the FY2025 cells pick up 4Q25.
5. **Tearsheet E39 font.** Changed from Calibri to Arial 11.
6. **DCF FY2026E stub (G35).** The column now discounts only the 4Q26E unlevered free cash flow. It used to count the full FY2026, even though 1Q–3Q26 cash was already in the 3Q26 cash balance the DCF adds. FY2026E present value fell from about $1,060m to $240m.
7. **Tearsheet per-case Adj. EBITDA.** Re-checked against the Income Statement for all five cases. All were current, so nothing changed. The active case was left as found (Bull).

## Left for the analyst

1. **Multiples.** The Tearsheet multiples (E52:F56) and DCF exit multiples (G50:G54) are blank, so price targets, IRRs and the DCF terminal value are not meaningful until they are typed.
2. **Interest (since resolved).** The forecast now carries street's net non-GAAP other expense as interest expense, at about −$15m a quarter. The earlier version had the sign wrong and treated it as income.
3. **Debt.** Debt is flat: the $500m 5.75% notes due 2027 are assumed refinanced, and the 3Q26 balance sheet shows no current portion.
4. **Share-plan cash flows.** Stock issuance proceeds and taxes on net share settlement are zero. History is about +$45m and −$35m a year.
5. **Base cost drivers.** These reproduce street's dollar costs, so costs do not flex when revenue moves.
6. **DCF shares and tax rate.** The DCF uses a fixed 153m shares and 20.5% tax, against the Income Statement's roughly 152.7m and 21%.
7. **4Q26E stub period.** The stub counts the whole 4Q26E cash flow, although the valuation date (2 Nov 2026) is about a third of the way through the quarter.

## Second pass: every case and toggle (3 Nov 2026, afternoon)

### What was run

The model was recalculated under all ten toggle combinations:

- the case selector (Disaster, Bear, Base, Bull, Blowout);
- the reverse DCF "deduct SBC" switch (0 or 1).

Every cell in each scenario was then checked for:

- errors and the check rows;
- impossible values;
- extreme growth swings;
- working-capital days;
- case-ordering inversions;
- Tearsheet snapshots against the live model;
- the DCF and reverse DCF.

The toggles were restored afterwards to Base and 0.

### Mechanical result

The model is clean in every scenario:

- No error cells appear in any scenario, apart from the two stock-data cells (Cover E5 and Tearsheet E39).
- The checks are at zero.
- Results are ordered Disaster < Bear < Base < Bull < Blowout on revenue, adjusted EBITDA, EPS, net income and FCF in every forecast year except 4Q26 FCF.
- The Tearsheet snapshots match the model in all five cases, and the case weights sum to 100%.

### Judgment items found

1. **DCF and Tearsheet give different Base values.** The DCF gives $132 a share; the blended Tearsheet target is $206.
2. **Interest does not respond to cash.** Net interest is street's fixed figure in every case, while cash builds to between $3.3bn (Disaster) and $6.0bn (Blowout) by FY2030, with no interest income on it.
3. **Other non-GAAP adjustments are zero in FY2029/30.** They run at about $70–80m a year in 2027–28.
4. **Two driver-ordering inversions.** Bull's clinical consumables growth is below Base in 2Q28 (14% vs 15%) and 4Q28 (13% vs 14%).
5. **4Q26 FCF is in reverse case order.** It runs from $309m in Disaster to $299m in Blowout, because higher revenue builds working capital.
6. **PP&E shrinks.** It falls from $731m to $630m by FY2030, because street capex is below street depreciation every year.
7. **The $500m 5.75% notes due 2027 are not shown as current.** They stay in long-term debt, with no current portion.
8. **The reverse DCF solve is static.** With the SBC switch at 1, implied upside is −4.9% until Goal Seek is re-run.

## Resolution and final pass (3 Nov 2026)

### Changes made

- **Other non-GAAP adjustments, FY2029/30.** Now street-implied (street adjusted operating income − GAAP operating income − amortization): −$12.6m in FY2029 and −$4.7m in FY2030.
- **Reverse DCF.** The implied CAGR (C26) is now a live solve. The price is a polynomial in (1 + CAGR), and helper rows B92:I120 run Newton iterations on it, so implied upside is 0% at the live price with the SBC switch at either setting. The CAGR is 10.8% with SBC excluded and 11.8% with SBC deducted, at $238.48. The sensitivity grids are still static.
- **Tearsheet.** The per-case EBITDA snapshots were refreshed.
- **Formatting.** The DCF exit multiples were recoloured green, and two Calibri cells on the Implied Discounting Build were changed to Arial.

### Analyst decisions

The analyst fixed the Bull clinical drivers. They chose to leave these as they are: the DCF/Tearsheet valuation gap, street-anchored interest, 4Q26 FCF ordering, PP&E, and debt classification.

### Final pass

All ten scenarios were checked again. No critical mechanical or logical issues remain:

- the only error cells are the two stock-data cells;
- the checks are at zero;
- the case ordering holds;
- the Tearsheet snapshots match the model;
- the reverse DCF solves exactly.
