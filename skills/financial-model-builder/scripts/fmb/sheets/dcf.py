"""DCF tab: annual columns only, laid out exactly like the reference model.

Unlevered free cash flow from the statements, mid-period discounting with a stub
for the first estimate year, terminal value from an exit EV/EBITDA multiple cased
with SUMIF on the case cell, then the bridge to an implied share price.
"""
from __future__ import annotations

import datetime as dt
from typing import List

from openpyxl.utils import get_column_letter

from .. import styles as S
from ..engine import BS, CFS, DCF, DRIVERS, IS, TEARSHEET, ModelContext, SheetBuilder
from ..periods import PeriodAxis


def _annual_axis(ctx: ModelContext) -> PeriodAxis:
    ax = PeriodAxis()
    col = 4
    for p in ctx.axis.fys():
        q = type(p)(p.pid, p.kind, p.fy, p.q, p.estimate, p.annual_only, p.end, p.weeks, col)
        ax._add(q)
        col += 1
    return ax


def build_dcf(ctx: ModelContext, cfg: dict) -> SheetBuilder:
    axis = _annual_axis(ctx)
    sb = SheetBuilder(ctx, DCF, axis=axis, label_width=54.375, zoom=80, freeze="D11", header=False)
    ws = sb.ws
    # short header: company, units, case, FY labels at row 7, spacer row 8
    S.style_cell(ws["B2"], ctx.title_line(), bold=True, color=S.BLACK)
    ws["B2"].font = S.font(S.BLACK, True, False, 14)
    S.style_cell(ws["B3"], ctx.units_line(), italic=True, color=S.BLACK)
    S.style_cell(ws["B5"], f"='{DRIVERS}'!B5", bold=True, color=S.BLACK, top=True, bottom=True)
    S.style_cell(ws["B7"], "Fiscal Year", bold=True, color=S.BLACK, top=True)
    for p in axis.periods:
        S.style_cell(ws[f"{p.letter}7"], p.label, bold=True, color=S.BLACK, top=True,
                     fill_rgb=S.GREY_BAND if p.estimate else None)
    for c in range(2, axis.last_col() + 1):
        ws.cell(row=7, column=c).border = S.border(top=True)
    ws.row_dimensions[8].height = 4.5
    sb.row = 9
    sb.section("Discounted Cash Flow", marker=False)

    opex = cfg.get("opex_lines") or []
    da = cfg.get("da_lines") or ["dep", "amort"]
    nwc = cfg.get("nwc_lines") or []
    capex = cfg.get("capex_line") or "capex"
    rev = cfg.get("revenue_line") or "total_rev"
    cogs = cfg.get("cogs_line") or "cogs"
    tax_rate_line = cfg.get("tax_rate_line") or "tax_rate"
    ebitda_line = cfg.get("ebitda_line") or "ebitda"
    has_capex = (CFS, capex) in ctx.registry

    L = lambda **k: sb.line(k)
    L(id="dcf_rev", label="Revenue", kind="amount", fmt="amount_d", bold=True, dsl="={" + IS + "!" + rev + "}", fy="formula")
    L(id="dcf_growth", label="% Growth Rate", fmt="pct_d", dsl="={" + IS + "!" + rev + ".pct_yoy}", fy="formula", needs="py")
    L(id="dcf_cogs", label="(-) Cost of Revenue", fmt="amount_d", dsl="={" + IS + "!" + cogs + "}", fy="formula")
    L(id="dcf_gp", label="Gross Profit", fmt="amount_d", bold=True, dsl="={dcf_rev}-{dcf_cogs}", fy="formula")
    L(id="dcf_gm", label="% Margin", fmt="pct_d", dsl="={dcf_gp}/{dcf_rev}", fy="formula")
    opex_ids = []
    for i, (oid, olabel) in enumerate(opex):
        lid = f"dcf_opex{i}"
        opex_ids.append(lid)
        L(id=lid, label=f"(-) {olabel}", fmt="amount_d", dsl="={" + IS + "!" + oid + "}", fy="formula")
    L(id="dcf_ebit", label="EBIT", fmt="amount_d", bold=True, dsl="={dcf_gp}" + "".join("-{" + o + "}" for o in opex_ids), fy="formula")
    L(id="dcf_ebit_m", label="% Margin", fmt="pct_d", dsl="={dcf_ebit}/{dcf_rev}", fy="formula")
    L(id="dcf_da", label="(+) D&A", fmt="amount_d", dsl="=" + "+".join("{" + IS + "!" + d + "}" for d in da), fy="formula")
    L(id="dcf_da_pct", label="% of Revenue", fmt="pct_d", dsl="={dcf_da}/{dcf_rev}", fy="formula")
    L(id="dcf_ebitda", label="EBITDA", fmt="amount_d", bold=True, dsl="={dcf_ebit}+{dcf_da}", fy="formula")
    L(id="dcf_ebitda_m", label="% Margin", fmt="pct_d", dsl="={dcf_ebitda}/{dcf_rev}", fy="formula")
    tax_row = sb.line({"id": "dcf_tax_rate", "label": "% Tax Rate", "fmt": "pct_d", "fy": "formula",
                       "values": {}})
    L(id="dcf_taxes", label="(-) Taxes", fmt="amount_d", dsl="={dcf_ebit}*{dcf_tax_rate}", fy="formula")
    L(id="dcf_nopat", label="NOPAT", fmt="amount_d", bold=True, dsl="={dcf_ebit}-{dcf_taxes}", fy="formula")
    L(id="dcf_da2", label="(+) D&A", fmt="amount_d", dsl="={dcf_da}", fy="formula")
    nwc_dsl = "=" + "+".join("{" + CFS + "!" + n + "}" for n in nwc) if nwc else "=0"
    L(id="dcf_nwc", label="(+/-) ∆NWC", fmt="amount_d", dsl=nwc_dsl, fy="formula")
    L(id="dcf_nwc_pct", label="% of Revenue", fmt="pct_d", dsl="={dcf_nwc}/{dcf_rev}", fy="formula")
    L(id="dcf_capex", label="(+/-) CapEx", fmt="amount_d", dsl=("={" + CFS + "!" + capex + "}") if has_capex else "=0", fy="formula")
    L(id="dcf_capex_pct", label="% of Revenue", fmt="pct_d", dsl="={dcf_capex}/{dcf_rev}", fy="formula")
    L(id="dcf_ufcf", label="UFCF", fmt="amount_d", bold=True, dsl="={dcf_nopat}+{dcf_da2}+{dcf_nwc}+{dcf_capex}", fy="formula")
    r_dp = sb.line({"id": "dcf_dp", "label": "Discount Period", "fmt": "number2", "fy": "formula", "values": {}})
    r_df = sb.line({"id": "dcf_df", "label": "Discount Factor", "fmt": "number2", "fy": "formula", "values": {}})
    r_pv = sb.line({"id": "dcf_pv", "label": "PV of UFCFs", "fmt": "amount_d", "bold": True, "fy": "formula", "values": {}})
    sb.blank()

    # ---- WACC block ------------------------------------------------------------------
    sb.section("WACC", marker=False)
    r = sb.row
    inputs = [
        ("Valuation date", "val_date", cfg.get("valuation_date"), "date"),
        ("Tax Rate", "tax", cfg.get("tax_rate"), "pct_d"),
        ("Rfr", "rfr", cfg.get("rfr"), "pct_d"),
        ("Beta", "beta", cfg.get("beta"), "number2"),
        ("ERP", "erp", cfg.get("erp"), "pct_d"),
        ("Ke", "ke", None, "pct_d"),
        ("After-Tax Kd", "kd", cfg.get("kd_after_tax"), "pct_d"),
        ("Equity Weight", "we", cfg.get("equity_weight"), "pct_d"),
        ("WACC", "wacc", None, "pct_d"),
    ]
    rows = {}
    for label, key, val, fmt in inputs:
        rows[key] = r
        bold = key == "wacc"
        S.style_cell(ws[f"B{r}"], label, bold=bold, color=S.BLACK)
        if key == "ke":
            S.style_cell(ws[f"D{r}"], f"=D{rows['rfr']}+D{rows['beta']}*D{rows['erp']}", fmt=fmt, color=S.BLACK)
        elif key == "wacc":
            S.style_cell(ws[f"D{r}"], f"=D{rows['we']}*D{rows['ke']}+(1-D{rows['we']})*D{rows['kd']}", fmt=fmt, bold=True, color=S.BLACK)
        else:
            v = val
            if key == "val_date" and isinstance(v, str):
                v = dt.date.fromisoformat(v)
            S.style_cell(ws[f"D{r}"], v, fmt=fmt, color=S.BLUE)
            note = (cfg.get("notes") or {}).get(key)
            if note:
                ctx.notes.append((DCF, f"D{r}", note))
        r += 1
    sb.row = r + 1
    # tax rate row on the UFCF block: history links the statements, estimates use the input
    tax_vals = {}
    for p in axis.periods:
        if p.estimate:
            tax_vals[p.pid] = f"=$D${rows['tax']}"
        else:
            tax_vals[p.pid] = "={" + IS + "!" + tax_rate_line + "}"
    ctx.line_defs[(DCF, "dcf_tax_rate")]["values"] = tax_vals
    # discounting rows
    est = [p for p in axis.periods if p.estimate]
    dp_vals, df_vals, pv_vals = {}, {}, {}
    for i, p in enumerate(est):
        fy_end = f"DATE({p.end.year},{p.end.month},{p.end.day})"
        if i == 0:
            dp_vals[p.pid] = f"=MAX(0,{fy_end}-$D${rows['val_date']})/2/365"
        elif i == 1:
            dp_vals[p.pid] = f"=(MAX(0,{fy_end}-$D${rows['val_date']})-182.5)/365"
        else:
            prev = est[i - 1]
            dp_vals[p.pid] = f"={prev.letter}{r_dp}+1"
        df_vals[p.pid] = f"=1/(1+$D${rows['wacc']})^{p.letter}{r_dp}"
        pv_vals[p.pid] = f"={p.letter}{{row:dcf_ufcf}}*{p.letter}{r_df}"
    ctx.line_defs[(DCF, "dcf_dp")]["values"] = dp_vals
    ctx.line_defs[(DCF, "dcf_df")]["values"] = df_vals
    ctx.line_defs[(DCF, "dcf_pv")]["values"] = pv_vals

    # ---- Terminal value block ----------------------------------------------------------
    sb.section("Terminal Value", marker=False)
    r = sb.row
    sec_row = r - 2
    # case table to the right (F/G), starting under the section row
    mults = cfg.get("exit_multiples") or {}
    case_rows = {}
    cr = sec_row + 1
    for case in ctx.cases:
        case_rows[case] = cr
        S.style_cell(ws[f"F{cr}"], case, color=S.BLACK)
        S.style_cell(ws[f"G{cr}"], mults.get(case), fmt="mult", color=S.BLUE, fill_rgb=S.LIGHT_YELLOW)
        note = ((cfg.get("notes") or {}).get("exit_multiples") or {}).get(case)
        if note:
            ctx.notes.append((DCF, f"G{cr}", note))
        cr += 1
    first_c, last_c = sec_row, cr - 1
    S.style_cell(ws[f"F{cr}"], "Active", bold=True, color=S.BLACK)
    S.style_cell(ws[f"G{cr}"], f"=SUMIF($F${first_c}:$F${last_c},$B$5,G{first_c}:G{last_c})", fmt="mult", bold=True,
                 color=S.BLACK, fill_rgb=S.LIGHT_YELLOW)
    active_mult_row = cr
    last_fy = axis.last()
    S.style_cell(ws[f"B{r}"], "Exit EV/EBITDA", color=S.BLACK)
    S.style_cell(ws[f"D{r}"], f"=G{active_mult_row}", fmt="mult", color=S.BLACK)
    r_exit = r; r += 1
    # terminal-year metric: the tearsheet's valuation metric (e.g. Adj. EBITDA) when the
    # statements carry it, else the DCF's own EBITDA line
    is_metric_row = ctx.registry.get((IS, ebitda_line))
    main_last = ctx.axis.by_id.get(last_fy.pid)
    if is_metric_row and main_last is not None and ebitda_line != "ebitda":
        metric_label = ctx.line_defs[(IS, ebitda_line)]["label"]
        S.style_cell(ws[f"B{r}"], f"{last_fy.label.replace(' ', '')} {metric_label}", color=S.BLACK)
        S.style_cell(ws[f"D{r}"], f"='{IS}'!{main_last.letter}{is_metric_row}", fmt="amount_d", color=S.GREEN)
    else:
        S.style_cell(ws[f"B{r}"], f"{last_fy.label.replace(' ', '')} EBITDA", color=S.BLACK)
        S.style_cell(ws[f"D{r}"], f"={last_fy.letter}{ctx.registry[(DCF, 'dcf_ebitda')]}", fmt="amount_d", color=S.BLACK)
    r_tebitda = r; r += 1
    S.style_cell(ws[f"B{r}"], "TV", color=S.BLACK)
    S.style_cell(ws[f"D{r}"], f"=D{r_exit}*D{r_tebitda}", fmt="amount_d", color=S.BLACK)
    r_tv = r; r += 1
    S.style_cell(ws[f"B{r}"], "PV of TV", color=S.BLACK)
    e = last_fy.end
    S.style_cell(ws[f"D{r}"], f"=D{r_tv}/(1+D{rows['wacc']})^((DATE({e.year},{e.month},{e.day})-D{rows['val_date']})/365)",
                 fmt="amount_d", bold=True, color=S.BLACK)
    r_pvtv = r; r += 1
    sb.row = max(r, cr + 1) + 1

    # ---- Equity value block ---------------------------------------------------------------
    sb.section("Equity Value", marker=False)
    r = sb.row
    first_est, last_est = est[0], est[-1]
    S.style_cell(ws[f"B{r}"], "PV of UFCF", color=S.BLACK)
    S.style_cell(ws[f"D{r}"], f"=SUM({first_est.letter}{r_pv}:{last_est.letter}{r_pv})", fmt="amount_d", color=S.BLACK)
    r_sumpv = r; r += 1
    S.style_cell(ws[f"B{r}"], "PV of TV", color=S.BLACK)
    S.style_cell(ws[f"D{r}"], f"=D{r_pvtv}", fmt="amount_d", color=S.BLACK)
    r_pvtv2 = r; r += 1
    S.style_cell(ws[f"B{r}"], "Enterprise Value", bold=True, color=S.BLACK)
    S.style_cell(ws[f"D{r}"], f"=D{r_sumpv}+D{r_pvtv2}", fmt="amount_d", bold=True, color=S.BLACK)
    r_ev = r; r += 1
    bridge = cfg.get("bridge") or {}
    # the bridge uses the balance sheet of the last quarter ending on or before the valuation
    # date (the reference model values the company off that quarter's balance sheet, which may
    # be the first estimate quarter when the valuation date falls just after a quarter end)
    laq = ctx.axis.last_actual_quarter()
    val_date = cfg.get("valuation_date")
    if val_date:
        vd = dt.date.fromisoformat(val_date) if isinstance(val_date, str) else val_date
        qs = [q for q in ctx.axis.quarters() if q.end and q.end <= vd]
        if qs:
            laq = qs[-1]
    bs_col = get_column_letter(laq.col)

    def bs_sum(ids: List[str], sign: str = "+") -> str:
        parts = []
        for lid in ids:
            row_ = ctx.registry.get((BS, lid))
            if row_ is None:
                continue
            parts.append(f"'{BS}'!{bs_col}{row_}")
        if not parts:
            return "=0"
        return "=" + ("+".join(parts) if sign == "+" else "-(" + "+".join(parts) + ")")

    cash_f = bs_sum(bridge.get("cash_lines") or ["cash"])
    S.style_cell(ws[f"B{r}"], bridge.get("cash_label", "(+) Cash & Investments"), color=S.BLACK)
    S.style_cell(ws[f"D{r}"], cash_f if cash_f != "=0" else 0, fmt="amount_d")
    r_cash = r; r += 1
    debt_f = bs_sum(bridge.get("debt_lines") or [], sign="-")
    S.style_cell(ws[f"B{r}"], bridge.get("debt_label", "(-) Debt & Lease Liabilities"), color=S.BLACK)
    S.style_cell(ws[f"D{r}"], debt_f if debt_f != "=0" else 0, fmt="amount_d")
    r_debt = r; r += 1
    extra_rows = []
    for adj in bridge.get("other_adjustments") or []:
        S.style_cell(ws[f"B{r}"], adj["label"], color=S.BLACK)
        S.style_cell(ws[f"D{r}"], adj["value"], fmt="amount_d")
        extra_rows.append(r); r += 1
    rc = ctx.reporting_ccy
    tc = ctx.trading_ccy
    S.style_cell(ws[f"B{r}"], f"Equity Value ({rc})" if rc != tc else "Equity Value", bold=True, color=S.BLACK)
    S.style_cell(ws[f"D{r}"], f"=D{r_ev}+D{r_cash}+D{r_debt}" + "".join(f"+D{x}" for x in extra_rows), fmt="amount_d", bold=True, color=S.BLACK)
    r_eq = r; r += 1
    if rc != tc:
        S.style_cell(ws[f"B{r}"], f"{rc}/{tc}", color=S.BLACK)
        S.style_cell(ws[f"D{r}"], ctx.spec.get("company", {}).get("fx_rate", 1.0), fmt="number4", color=S.BLUE)
        r_fx = r; r += 1
        S.style_cell(ws[f"B{r}"], f"Equity Value ({tc})", bold=True, color=S.BLACK)
        S.style_cell(ws[f"D{r}"], f"=D{r_eq}*D{r_fx}", fmt="amount_d", bold=True, color=S.BLACK)
        r_eq2 = r; r += 1
    else:
        r_fx = None
        r_eq2 = r_eq
    S.style_cell(ws[f"B{r}"], "Diluted Shares (mm)", color=S.BLACK)
    shares_val = cfg.get("diluted_shares")
    if shares_val in (None, ""):
        # fall back to the last reported diluted share count on the income statement
        sh_row = ctx.registry.get((IS, "shares_dil"))
        if sh_row:
            shares_val = f"='{IS}'!{get_column_letter(ctx.axis.last_actual_quarter().col)}{sh_row}"
    S.style_cell(ws[f"D{r}"], shares_val, fmt="number1")
    note = (cfg.get("notes") or {}).get("diluted_shares")
    if note:
        ctx.notes.append((DCF, f"D{r}", note))
    r_sh = r; r += 1
    S.style_cell(ws[f"B{r}"], f"Implied Share Price ({tc})", bold=True, color=S.BLACK)
    S.style_cell(ws[f"D{r}"], f"=D{r_eq2}/D{r_sh}", fmt="number2", bold=True, color=S.BLACK)
    r_px = r; r += 1
    S.style_cell(ws[f"B{r}"], f"Current Share Price ({tc})", color=S.BLACK)
    S.style_cell(ws[f"D{r}"], f"='{TEARSHEET}'!D39", fmt="number2", color=S.GREEN)
    r_cur = r; r += 1
    S.style_cell(ws[f"B{r}"], "Upside/(Downside)", color=S.BLACK)
    S.style_cell(ws[f"D{r}"], f"=D{r_px}/D{r_cur}-1", fmt="pct_d", bold=True, color=S.BLACK)
    sb.row = r + 1
    # remember key cells for the tearsheet
    ctx.dcf_cells = {"cash": f"D{r_cash}", "debt": f"D{r_debt}", "shares": f"D{r_sh}", "fx": f"D{r_fx}" if r_fx else None,
                     "val_date": f"D{rows['val_date']}", "wacc": f"D{rows['wacc']}", "exit_rows": case_rows,
                     "ebitda_row": ctx.registry[(DCF, "dcf_ebitda")], "implied_px": f"D{r_px}"}
    return sb
