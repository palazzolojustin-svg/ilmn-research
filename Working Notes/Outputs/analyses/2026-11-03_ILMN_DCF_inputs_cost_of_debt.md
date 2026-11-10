# ILMN DCF inputs: after-tax cost of debt, equity weight, diluted shares and bridge lines

*Prepared 3 November 2026 for the DCF Inputs sheet of `Working Notes/Outputs/models/ILMN_model_inputs.xlsx` (valuation date 2 Nov 2026; price $235.99 on 30 Oct 2026; the model's last actual quarter is 2Q26).*

## The short answer

Illumina's after-tax cost of debt is about **4.5-4.6%** on a market basis (pre-tax 5.6-6.0%, taxed at the 20.5% consensus rate) and about **3.5%** on a book-coupon basis (the 4.45% average coupon on its notes). The table gives the values to type, with the alternatives behind each.

| DCF Inputs key | Recommended value | What it is |
|---|---|---|
| `tax_rate` | 0.205 | Consensus adjusted tax rate 20.4-20.6% for 3Q26-4Q28 (Bloomberg, 10 Oct 2026); management's 2026 non-GAAP guide 20.5% (Q2 and Q3 2026 calls) |
| `kd_after_tax` | 0.045 | Pre-tax 5.8% market yield on the term notes (implied by their 27 Sep 2026 fair value) x (1 - 20.5%). Book coupon basis: 4.45% x 0.795 = 3.5%; newest issue basis: 4.96% x 0.795 = 3.9% |
| `equity_weight` | 0.94 | Market cap $35.7bn ($235.99 x 151.2m shares) over market cap plus $2.31bn of debt and leases (3Q26): 0.939. Notes only ($1.79bn): 0.952 |
| `diluted_shares` | 153 | Diluted weighted-average shares: 153m in 2Q26 (the model's last actual), 154m in 3Q26; 151.2m basic shares outstanding on 23 Oct 2026; consensus 152.5-152.8m for 2027-2028 |
| `cash_lines` | cash, st_inv | Both are kept balance-sheet lines: $1,040m cash and $128m short-term investments at 2Q26 ($1,168m) |
| `debt_lines` | st_debt, lt_debt, lease_liab | $500m current notes, $1,491m long-term notes and $454m non-current operating leases at 2Q26 ($2,445m) |

The WACC these inputs give is about 11.0% (cost of equity 4.93% + 1.47 x 4.42% = 11.4%, weighted 94/6). Because debt is only 6% of the capital structure, moving the after-tax cost of debt between 3.5% and 4.5% changes the WACC by 0.06 points, so the choice barely moves the valuation. For reference, JPMorgan's DCF uses a 9.8% WACC (Aug 2026) and the Seeking Alpha DCF 9.74%; the gap to 11% comes from the risk-free rate and beta inputs, not the cost of debt.

## 1. What Illumina owes

Illumina's debt is four series of senior unsecured term notes, $1.8bn of principal in all, plus operating leases. There is no bank debt: the revolving credit facility, a standing bank line, is undrawn. Illumina refinanced in August 2026, which the model's 2Q26 balance sheet does not yet show.

| Instrument | Principal | Coupon | Matures | Note |
|---|---|---|---|---|
| Term notes due 2027 | $500m | 5.750% | 13 Dec 2027 | Issued Dec 2022 |
| Term notes due 2029 | $300m | 4.950% | 19 Sep 2029 | Issued 17 Aug 2026 at 99.971% of par (yield about 4.96%); net proceeds $297m |
| Term notes due 2030 | $500m | 4.750% | 12 Dec 2030 | Issued 25 Nov 2025 |
| Term notes due 2031 | $500m | 2.550% | 23 Mar 2031 | Issued Mar 2021 |
| Term notes due 2026 | repaid | 4.650% | 9 Sep 2026 | $500m repaid in cash on 9 Sep 2026 from the 2029 notes plus cash on hand |
| Operating leases | $524m | 4.4% imputed (CapIQ) | to 2039 | $85m current, $439m non-current at 3Q26; $82m and $454m at 2Q26 |
| Revolving credit facility | undrawn | SOFR plus a rating-based margin | 13 Aug 2031 | New $1.0bn five-year facility dated 13 Aug 2026 replaced the $750m 2023 facility; covenant: debt below 3.5x adjusted EBITDA |

Carrying value of the notes was $1,789m at 27 Sep 2026 ($1,800m less $11m of unamortised discount and issuance costs) and $1,991m at 28 Jun 2026. Gross leverage was about 1.4x trailing EBITDA at 3Q26 (Q3 2026 call). Sources: Q3 2026 10-Q (quarter ended 27 Sep 2026), 8-K of 17 Aug 2026, prospectus supplement for the 2029 notes, FY2025 10-K note 5, CapIQ Capital Structure sheets.

## 2. The pre-tax cost of debt, three ways

- **Book coupon: 4.45%.** The principal-weighted average coupon of the four notes outstanding today (4.425% before the August refinancing). This is what Illumina pays, not what new debt would cost.
- **Reported interest cost: about 4.6-5.0%.** Interest expense on debt was $99m in FY2025 on $2.0bn of notes (5.0%, inflated by the 5.80% notes repaid in Dec 2025 and by amortisation of issuance costs); $70-71m in the first nine months of 2026 ($24m in Q3), about 4.6% annualised. Cash interest paid was $95m in FY2025 (CapIQ).
- **Market yield: about 5.6-6.0% at quarter-end, 4.96% at the August issue.** The 10-Q reports the fair value of the notes at $1,718m against $1,800m of principal at 27 Sep 2026 (95.4% of par). A single yield that discounts the four notes' remaining coupons and principal to that value is 5.6% if the fair value is quoted without accrued interest and 6.0% if it includes it. At 28 Jun 2026 the same calculation gave 4.8-5.0% ($1,959m against $2,000m), and the 3-year notes sold on 17 Aug 2026 yielded about 4.96%. Yields on Illumina's paper therefore rose through September. This market yield is the right input for a WACC: it is what lenders charge Illumina today, and it sits about 0.7-1.0 points above the 4.93% risk-free rate already typed in the sheet, a normal spread for an investment-grade issuer. A 4.45% or 4.96% cost of debt would sit at or below that risk-free rate, which is inconsistent.

Illumina is investment grade (the 2029 notes prospectus says so without naming the ratings; management repeats the goal of keeping the rating, JPM conference Jan 2026). CapIQ's imputed rate on the operating leases is 4.4%.

## 3. The tax rate

The DCF uses one tax rate for both the cash-flow build and the debt tax shield. Consensus is the sensible anchor, as the sheet's own note says: Bloomberg's adjusted (non-GAAP) consensus tax rate is 20.4-20.6% for every quarter from 3Q26 to 4Q28 and 20.6-21.4% for FY2029-FY2032; the GAAP consensus is 21.0-21.5%. Management guides a 20.5% non-GAAP rate for 2026 (Q2 and Q3 2026 calls). Reported GAAP rates are noisier: 21.7% in FY2025, 18.4% for the first half of 2026 and about 16.7% in Q3 2026, helped by prior-year return adjustments and by earnings in Singapore, where tax holidays run to 2035 (FY2025 10-K). The US federal statutory rate is 21%; the marginal rate on US interest deductions including state tax is nearer 24-25%, which would lower the after-tax cost of debt by about 0.2 points, immaterial at a 6% debt weight. Recommended: 0.205.

## 4. The after-tax cost of debt

After-tax cost of debt = pre-tax cost x (1 - tax rate).

| Pre-tax basis | Pre-tax | After tax at 20.5% | After tax at 21% |
|---|---|---|---|
| Market yield at 27 Sep 2026 (recommended) | 5.6-6.0% | 4.5-4.7% | 4.4-4.7% |
| Newest issue, Aug 2026 3-year notes | 4.96% | 3.9% | 3.9% |
| Weighted average coupon | 4.45% | 3.5% | 3.5% |

Type **0.045** (4.5%), the low end of the market range, because the fair-value reading is one quarter-end point and the August issue priced at 4.96%. If you prefer the cost of debt Illumina actually pays, type 0.035; the implied share price moves by well under 1%.

## 5. The equity weight

Market-value weights: equity $35.7bn (151.2m shares at $235.99, or $36.1bn on 153m diluted shares) against debt and leases of $2.31bn at 27 Sep 2026 ($1,789m notes, $524m operating leases), giving an equity weight of 93.9%. Excluding leases, 95.2%; on the 2Q26 bridge balances ($1,991m notes plus $454m non-current leases), 93.6%. All round to **0.94**. Illumina's target structure is similar: an investment-grade rating with gross leverage of 1.4-1.6x EBITDA and $1.8bn of buyback authorisation remaining (Q3 2026 call).

## 6. Diluted shares

The DCF divides equity value by this number, so it should be the current diluted count. Diluted weighted-average shares were 153m in 2Q26 (the model's last actual quarter; basic 151m) and 154m in 3Q26 (basic 151m); 151.2m shares were outstanding on 23 Oct 2026 (Q3 10-Q cover). Management guided about 153m for 2026 (Q2 2026 call) and consensus carries 152.5-152.8m through 2028 as buybacks offset issuance. Type **153** to match the model's last actual quarter; 154 is defensible and changes the implied price by 0.65%.

## 7. The bridge lines

Both ID lists are valid balance-sheet line IDs in the Statement Mapping, so they can stay as they are.

- `cash, st_inv`: $1,040m cash and $128m short-term investments at 2Q26 ($1,168m). The short-term investments are mostly the retained GRAIL shares ($88m) plus time deposits; the GRAIL stake was sold down to $48m by 3Q26. Long-term investments (`lt_inv`) are not a kept line, so they cannot be added; they are small.
- `st_debt, lt_debt, lease_liab`: $500m, $1,491m and $454m at 2Q26 ($2,445m). Two points to know. First, the model has no line for the current portion of operating leases ($82m at 2Q26; `lease_liab_cur` is marked Keep N), so the bridge counts $82m less lease debt than the 10-Q shows, worth about $0.54 per share. Set `lease_liab_cur` to Keep Y if you want it captured. Second, the bridge uses the 2Q26 balance sheet by design, so `st_debt` is the $500m of 4.65% notes that were repaid in September; net debt is little changed because cash fell with them.
- Counting operating leases as debt is your template's convention. It is slightly conservative with an EV/EBITDA exit multiple, because US GAAP operating lease cost is already inside EBITDA; the effect is about $3 per share.

## Sources

- Illumina Form 10-Q for the quarter ended 27 Sep 2026 (debt note, interest expense, tax, shares): https://www.sec.gov/Archives/edgar/data/0001110803/000111080326000207/ilmn-20260927.htm
- Illumina Form 8-K, 17 Aug 2026 (completion of the $300m 4.950% notes due 2029): https://www.sec.gov/Archives/edgar/data/0001110803/000119312526354010/d51146d8k.htm
- Prospectus supplement for the 2029 notes (price 99.971%, net proceeds $297m, use of proceeds): https://www.sec.gov/Archives/edgar/data/0001110803/000119312526346923/d173650d424b2.htm
- `Working Notes/Sources/ILMN/filing/ILMN_10-Q_2026Q2.md` (2Q26 debt note, fair value $1,959m, shares, cash, leases, tax rates)
- `Working Notes/Sources/ILMN/filing/ILMN_10-K_FY2025.md` (note 5 Debt, interest expense $99m, tax rate reconciliation)
- `Working Notes/Sources/ILMN/capiq/2026-11-02_ILMN_CapIQ_Financials.xls` (Capital Structure Summary and Details, Key Stats, Income Statement supplemental items)
- Bloomberg consensus printouts of 10 Oct 2026 in `Working Notes/Sources/ILMN/consensus/` (tax rate and share count estimates)
- `Working Notes/Extracts/ILMN/earnings_call/ILMN_2026Q2_Earnings_Call.md` and `ILMN_2026Q3_Earnings_Call.md` (non-GAAP tax rate 20.5%, cash $1.34bn, debt $1.79bn, leverage 1.4x)
- `Core Notes/08_ILMN_Equity_Research.md` (JPM WACC 8.9-9.8%, Seeking Alpha 9.74%)
