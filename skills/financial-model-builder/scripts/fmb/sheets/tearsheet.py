"""Tearsheet: per-case price targets for one or more target blocks, a weighted
blended price target per block, risk/reward, the current price and bridge, the
multiples grid, and (to the right of the blended blocks) price-target sensitivity
grids whose multiple axis runs from the lowest-case multiple to the highest in equal
steps with the base multiple in the middle.
"""
from __future__ import annotations

import datetime as dt
import math
from typing import Dict, List, Optional

from openpyxl.styles import Alignment
from openpyxl.utils import get_column_letter

from .. import styles as S
from ..engine import DCF, IS, TEARSHEET, ModelContext

CASE_BLOCK_ORDER = ["Base", "Bull", "Bear", "Blowout", "Disaster"]
CASE_RANK = ["Blowout", "Bull", "Base", "Bear", "Disaster"]  # best to worst


def _ordered(cases: List[str], order: List[str]) -> List[str]:
    return [c for c in order if c in cases] + [c for c in cases if c not in order]


def sensitivity_multiples(low: float, base: float, high: float, max_cols: int = 25) -> List[float]:
    """Equal increments from `low` to `high` passing exactly through `base`."""
    if low is None or base is None or high is None or not (low <= base <= high) or high == low:
        return []
    d1, d2 = base - low, high - base
    for step in (5, 2.5, 2, 1, 0.5, 0.25, 0.1, 0.05):
        ok = all(abs(d / step - round(d / step)) < 1e-6 for d in (d1, d2) if d > 0)
        n = round(d1 / step) + round(d2 / step) + 1
        if ok and n <= max_cols:
            return [round(low + i * step, 4) for i in range(n)]
    n = 7
    step = (high - low) / (n - 1)
    return [round(low + i * step, 4) for i in range(n)]


def price_formula(cfg: dict, fallback_cell: str) -> object:
    src = (cfg.get("source") or "hardcode").lower()
    code = cfg.get("ticker_code") or ""
    if src == "bloomberg":
        live = f'BDP("{code}","PX_LAST")'
    elif src == "capiq":
        live = f'CIQ("{code}","IQ_LASTSALEPRICE")'
    elif src == "factset":
        live = f'FDS("{code}","P_PRICE")'
    else:
        return cfg.get("value")
    return f"=IFERROR({live},{fallback_cell})"


def build_tearsheet(ctx: ModelContext, cfg: dict):
    ws = ctx.wb.create_sheet(TEARSHEET)
    ws.sheet_view.showGridLines = False
    ws.sheet_view.zoomScale = 71
    widths = {"A": 9.0, "B": 2.25, "C": 22.25, "D": 9.25, "E": 12.0, "F": 9.0, "G": 4.75, "H": 22.25, "I": 3.75,
              "J": 10.375, "K": 9.0, "L": 4.75, "M": 9.0, "N": 9.0, "O": 9.0, "P": 9.0, "Q": 10.375, "R": 9.0, "S": 2.25}
    for k, v in widths.items():
        ws.column_dimensions[k].width = v
    cases = ctx.cases
    blocks = cfg.get("blocks") or []
    metric_label = cfg.get("metric_label", "Adj. EBITDA")
    metric_line = cfg.get("metric_line", "ebitda")
    mult_label = cfg.get("multiple_label", "NTM Multiple")
    tc = ctx.trading_ccy
    rc = ctx.reporting_ccy
    dcf = getattr(ctx, "dcf_cells", {}) or {}
    px_fmt = S.px_format(tc)
    ws.row_dimensions[4].height = 17.25

    # ---- current price and bridge (rows 39+) -------------------------------------------
    r0 = 39
    S.style_cell(ws[f"C{r0}"], "Current Px", bold=True, color=S.BLACK)
    pcfg = cfg.get("price") or {}
    S.style_cell(ws[f"F{r0}"], pcfg.get("value"), fmt=px_fmt, color=S.BLUE)
    if pcfg.get("date"):
        pd = pcfg["date"]
        if isinstance(pd, str):
            pd = dt.datetime.fromisoformat(pd).date()
        elif isinstance(pd, dt.datetime):
            pd = pd.date()
        S.style_cell(ws[f"G{r0}"], pd, fmt="date", color=S.BLUE)
    pf = price_formula(pcfg, f"F{r0}")
    S.style_cell(ws[f"D{r0}"], pf, fmt="px_acct", color=S.BLUE)
    cur = f"$D${r0}"
    r = r0 + 2
    S.style_cell(ws[f"C{r}"], f"Equity Value ({rc})" if rc != tc else "Equity Value", color=S.BLACK)
    fx_cell = f"E{r + 1}"
    S.style_cell(ws[f"E{r}"], f"=D{r0}/{fx_cell}*DCF!{dcf.get('shares', 'D67')}", fmt="number1", bold=True, color=S.GREEN)
    r_eq = r; r += 1
    S.style_cell(ws[f"C{r}"], f"{rc}/{tc}", color=S.BLACK)
    if dcf.get("fx"):
        S.style_cell(ws[f"E{r}"], f"=DCF!{dcf['fx']}", fmt="number4", color=S.GREEN)
    else:
        S.style_cell(ws[f"E{r}"], 1, fmt="number4", color=S.BLUE)
    r += 1
    S.style_cell(ws[f"C{r}"], "(-) Cash & Investments", color=S.BLACK)
    S.style_cell(ws[f"E{r}"], f"=DCF!{dcf.get('cash', 'D62')}", fmt="number1", color=S.GREEN)
    r_cash = r; r += 1
    S.style_cell(ws[f"C{r}"], "(+) Debt & Lease Liabilities", color=S.BLACK)
    S.style_cell(ws[f"E{r}"], f"=-DCF!{dcf.get('debt', 'D63')}", fmt="number1", color=S.GREEN)
    r_debt = r; r += 1
    S.style_cell(ws[f"C{r}"], "Enterprise Value", color=S.BLACK)
    S.style_cell(ws[f"E{r}"], f"=E{r_eq}+E{r_debt}-E{r_cash}", fmt="number1", bold=True, color=S.BLACK)
    r_ev = r; r += 2
    # current implied multiple on the next fiscal year's metric
    ref_pid = cfg.get("current_multiple_period")
    S.style_cell(ws[f"C{r}"], f"{_short(ref_pid)} {metric_label} (Active Case)", color=S.BLACK)
    is_row = ctx.registry.get((IS, metric_line))
    ref_p = ctx.axis.by_id.get(ref_pid) if ref_pid else None
    if is_row and ref_p:
        S.style_cell(ws[f"E{r}"], f"='{IS}'!{ref_p.letter}{is_row}", fmt="number1", color=S.GREEN)
    r_m = r; r += 2
    S.style_cell(ws[f"C{r}"], f"{_short(ref_pid)} {metric_label} Multiple", color=S.BLACK)
    S.style_cell(ws[f"E{r}"], f"=E{r_ev}/E{r_m}", fmt="mult", bold=True, color=S.BLACK, fill_rgb=S.LIGHT_YELLOW)
    ws[f"E{r}"].border = S.border(True, True, True, True)
    r += 2
    # multiples grid: rows = cases, columns = blocks
    S.style_cell(ws[f"C{r}"], f"{mult_label}s (x)", bold=True, color=S.BLACK)
    grid_hdr = r
    for j, b in enumerate(blocks):
        S.style_cell(ws.cell(row=r, column=5 + j), b["label"], bold=True, color=S.BLACK, align="center")
    r += 1
    mult_cells: Dict[str, Dict[str, str]] = {}
    mults = cfg.get("multiples") or {}
    mnotes = cfg.get("multiple_notes") or {}
    for case in _ordered(cases, CASE_RANK):
        S.style_cell(ws[f"C{r}"], case, color=S.BLACK)
        mult_cells[case] = {}
        for j, b in enumerate(blocks):
            cell = ws.cell(row=r, column=5 + j)
            v = (mults.get(case) or {}).get(b["label"])
            S.style_cell(cell, v, fmt="mult", color=S.BLUE, fill_rgb=S.LIGHT_YELLOW)
            cell.border = S.border(True, True, True, True)
            mult_cells[case][b["label"]] = f"${get_column_letter(5 + j)}${r}"
            note = (mnotes.get(case) or {}).get(b["label"])
            if note:
                ctx.notes.append((TEARSHEET, cell.coordinate, note))
        r += 1
    bridge_cash, bridge_debt = f"$E${r_cash}", f"$E${r_debt}"
    shares_ref = f"DCF!{dcf.get('shares', '$D$67')}".replace("DCF!D", "DCF!$D$")
    fx_ref = f"$E${r_eq + 1}"

    # ---- per-block case columns (C/E and H/J) and blended blocks (M..R) ----------------------
    block_cols = [("C", "D", "E", "F"), ("H", "I", "J", "K")]
    blended_rows = []
    px_cells: Dict[str, Dict[str, str]] = {c: {} for c in cases}
    metric_cells: Dict[str, Dict[str, str]] = {c: {} for c in cases}
    mult_in_block: Dict[str, Dict[str, str]] = {c: {} for c in cases}
    snapshot = cfg.get("case_metric_values") or {}
    for j, b in enumerate(blocks[:2]):
        c0, c1, cv, c3 = block_cols[j]
        label = b["label"]
        metric_period = b.get("metric_period")
        mp = ctx.axis.by_id.get(metric_period) if metric_period else None
        S.style_cell(ws[f"{c0}3"], f"{label} Target", bold=True, color=S.WHITE, fill_rgb=S.GREEN_TS, align="center")
        ws.merge_cells(f"{c0}3:{c3}3")
        rr = 4
        for case in _ordered(cases, CASE_BLOCK_ORDER):
            S.style_cell(ws[f"{c0}{rr}"], f"{case} - {label}", bold=True, color=S.BLACK, align="center")
            ws.merge_cells(f"{c0}{rr}:{c3}{rr}")
            ws.row_dimensions[rr].height = 17.25
            rr += 1
            S.style_cell(ws[f"{c0}{rr}"], f"{metric_label} ({_short(metric_period)})", bold=True, color=S.BLACK)
            ws.merge_cells(f"{c0}{rr}:{c1}{rr}")
            snap = (snapshot.get(case) or {}).get(label)
            if snap is not None:
                S.style_cell(ws[f"{cv}{rr}"], snap, fmt="#,##0.0", bold=True, color=S.BLUE)
            elif is_row and mp:
                S.style_cell(ws[f"{cv}{rr}"], f"='{IS}'!{mp.letter}{is_row}", fmt="#,##0.0", bold=True, color=S.GREEN)
            metric_cells[case][label] = f"{cv}{rr}"
            rr += 1
            S.style_cell(ws[f"{c0}{rr}"], f"(x) {mult_label}", color=S.BLACK)
            ws.merge_cells(f"{c0}{rr}:{c1}{rr}")
            S.style_cell(ws[f"{cv}{rr}"], f"={mult_cells[case][label]}", fmt="mult", color=S.BLACK)
            mult_in_block[case][label] = f"{cv}{rr}"
            rr += 1
            S.style_cell(ws[f"{c0}{rr}"], "Px Tgt", bold=True, color=S.BLACK, fill_rgb=S.GREY_PT, top=True)
            ws.merge_cells(f"{c0}{rr}:{c1}{rr}")
            S.style_cell(ws[f"{cv}{rr}"], f"=({cv}{rr - 2}*{cv}{rr - 1}+{bridge_cash}-{bridge_debt})/{shares_ref}*{fx_ref}",
                         fmt=px_fmt, bold=True, color=S.BLACK, fill_rgb=S.GREY_PT, top=True)
            ws[f"{c1}{rr}"].fill = S.fill(S.GREY_PT)
            px_cells[case][label] = f"{cv}{rr}"
            rr += 1
            S.style_cell(ws[f"{c0}{rr}"], "% upside/(downside)", color=S.BLACK)
            S.style_cell(ws[f"{cv}{rr}"], f"={cv}{rr - 1}/{cur}-1", fmt="pct_plain", color=S.BLACK)
            rr += 1
            S.style_cell(ws[f"{c0}{rr}"], "% IRR", color=S.BLACK)
            td = b.get("target_date")
            if td:
                d = dt.date.fromisoformat(td) if isinstance(td, str) else td
                S.style_cell(ws[f"{cv}{rr}"], f"=({cv}{rr - 2}/{cur})^(1/YEARFRAC(DCF!{dcf.get('val_date', '$D$40')},DATE({d.year},{d.month},{d.day})))-1",
                             fmt="pct_plain", color=S.BLACK)
            rr += 2
        # blended block
        top = 3 + j * 12
        S.style_cell(ws[f"M{top}"], f"Blended Px Tgt/Cases - {label}", bold=True, color=S.WHITE, fill_rgb=S.GREEN_TS, align="center")
        ws.merge_cells(f"M{top}:R{top}")
        hdr = top + 1
        for col, text in zip("NOPQR", ["Wt", "Mult", metric_label.split()[-1], "Px", "%"]):
            S.style_cell(ws[f"{col}{hdr}"], text, bold=True, color=S.BLACK)
        rr = hdr + 1
        weights = cfg.get("weights") or {}
        first = rr
        ranked = _ordered(cases, CASE_RANK)
        up_cells = []
        for case in ranked:
            S.style_cell(ws[f"M{rr}"], case, color=S.BLACK)
            if j == 0:
                S.style_cell(ws[f"N{rr}"], weights.get(case), fmt="weight", color=S.BLUE)
            else:
                S.style_cell(ws[f"N{rr}"], f"=N{rr - 12}", fmt="weight", color=S.BLACK)
            S.style_cell(ws[f"O{rr}"], f"={mult_in_block[case][label]}", fmt="mult", color=S.BLACK)
            S.style_cell(ws[f"P{rr}"], f"={metric_cells[case][label]}", fmt="#,##0.0", color=S.BLACK)
            S.style_cell(ws[f"Q{rr}"], f"={px_cells[case][label]}", fmt=px_fmt, color=S.BLACK)
            S.style_cell(ws[f"R{rr}"], f"=Q{rr}/{cur}-1", fmt="pct_plain", color=S.BLACK)
            up_cells.append(f"R{rr}")
            rr += 1
        last = rr - 1
        S.style_cell(ws[f"M{rr}"], f"Blended Px Tgt - {b.get('blended_label', label)}", bold=True, color=S.BLACK, fill_rgb=S.GREY_PT)
        for col in "NOP":
            ws[f"{col}{rr}"].fill = S.fill(S.GREY_PT)
        S.style_cell(ws[f"Q{rr}"], f"=SUMPRODUCT(N{first}:N{last},Q{first}:Q{last})", fmt=px_fmt, bold=True, color=S.BLACK, fill_rgb=S.GREY_PT)
        r_bl = rr; rr += 1
        S.style_cell(ws[f"M{rr}"], "% upside/(downside)", color=S.BLACK)
        S.style_cell(ws[f"Q{rr}"], f"=Q{r_bl}/{cur}-1", fmt="pct_plain", color=S.BLACK)
        rr += 1
        S.style_cell(ws[f"M{rr}"], "% IRR", color=S.BLACK)
        td = b.get("target_date")
        if td:
            d = dt.date.fromisoformat(td) if isinstance(td, str) else td
            S.style_cell(ws[f"Q{rr}"], f"=(Q{r_bl}/{cur})^(1/YEARFRAC(DCF!{dcf.get('val_date', '$D$40')},DATE({d.year},{d.month},{d.day})))-1",
                         fmt="pct_plain", color=S.BLACK)
        rr += 1
        S.style_cell(ws[f"M{rr}"], "R/R", bold=True, color=S.BLACK)
        n_up = max(1, math.ceil(len(ranked) / 2))
        S.style_cell(ws[f"Q{rr}"], f"=AVERAGE({up_cells[0]}:{up_cells[n_up - 1]})/{up_cells[-1]}*-1", fmt="mult", bold=True, color=S.BLACK)
        blended_rows.append(rr)
        # sensitivity grids to the right
        _sensitivity(ws, ctx, cfg, b, cases, metric_cells, top, px_fmt, bridge_cash, bridge_debt, shares_ref, fx_ref, cur)
    if len(blended_rows) == 2:
        rr = blended_rows[1] + 2
        S.style_cell(ws[f"M{rr}"], "Blended R/R", bold=True, color=S.BLACK)
        S.style_cell(ws[f"Q{rr}"], f"=AVERAGE(Q{blended_rows[0]},Q{blended_rows[1]})", fmt="mult", bold=True, color=S.BLACK)
    ctx.tearsheet_cells = {"metric_cells": metric_cells, "px_cells": px_cells, "price": f"D{r0}", "multiples": mult_cells}
    return ws


def _short(pid: Optional[str]) -> str:
    if not pid:
        return ""
    s = pid.replace("FY", "")
    if s.isdigit():
        return f"FY{s[-2:]}E"
    return pid


def _sensitivity(ws, ctx, cfg, block, cases, metric_cells, top, px_fmt, cash, debt, shares_ref, fx_ref, cur):
    label = block["label"]
    mults = cfg.get("multiples") or {}
    vals = [(mults.get(c) or {}).get(label) for c in cases]
    vals = [v for v in vals if v is not None]
    base = (mults.get("Base") or {}).get(label)
    if not vals or base is None:
        return
    seq = sensitivity_multiples(min(vals), base, max(vals), max_cols=cfg.get("sensitivity_max_cols", 25))
    if not seq:
        return
    c0 = 20  # column T
    S.style_cell(ws.cell(row=top, column=c0), f"Px Tgt Sensitivity - {label}", bold=True, color=S.WHITE, fill_rgb=S.GREEN_TS, align="center")
    ws.merge_cells(start_row=top, start_column=c0, end_row=top, end_column=c0 + 1 + len(seq))
    hdr = top + 1
    S.style_cell(ws.cell(row=hdr, column=c0), "Case", bold=True, color=S.BLACK)
    S.style_cell(ws.cell(row=hdr, column=c0 + 1), block.get("metric_short", "EBITDA"), bold=True, color=S.BLACK)
    for i, m in enumerate(seq):
        cell = ws.cell(row=hdr, column=c0 + 2 + i)
        S.style_cell(cell, m, fmt="mult", bold=True, color=S.BLUE, fill_rgb=S.GREY_PT if abs(m - base) < 1e-9 else None, align="center")
    rr = hdr + 1
    ranked = _ordered(cases, CASE_RANK)
    for case in ranked:
        S.style_cell(ws.cell(row=rr, column=c0), case, color=S.BLACK)
        mc = metric_cells[case][label]
        S.style_cell(ws.cell(row=rr, column=c0 + 1), f"={mc}", fmt="#,##0.0", color=S.BLACK)
        mcell = f"${get_column_letter(c0 + 1)}{rr}"
        for i in range(len(seq)):
            hl = get_column_letter(c0 + 2 + i)
            S.style_cell(ws.cell(row=rr, column=c0 + 2 + i),
                         f"=({mcell}*{hl}${hdr}+{cash}-{debt})/{shares_ref}*{fx_ref}", fmt=px_fmt, color=S.BLACK)
        rr += 1
    rr += 1
    S.style_cell(ws.cell(row=rr, column=c0), f"% Upside - {label}", bold=True, color=S.BLACK)
    rr += 1
    for k, case in enumerate(ranked):
        S.style_cell(ws.cell(row=rr, column=c0), case, color=S.BLACK)
        src_row = hdr + 1 + k
        for i in range(len(seq)):
            hl = get_column_letter(c0 + 2 + i)
            S.style_cell(ws.cell(row=rr, column=c0 + 2 + i), f"={hl}{src_row}/{cur}-1", fmt="pct_plain", color=S.BLACK)
        rr += 1
    for i in range(len(seq) + 2):
        ws.column_dimensions[get_column_letter(c0 + i)].width = 10.375 if i else 12.0
