"""Drivers & Casing sheet.

Layout per cased driver: a bold title row, one row per case (blue inputs; a case
cell may hold a formula or a green link to a side build), and a bold "Active" row
that picks the selected case with SUMIF on the case cell B5. Uncased drivers
(income statement, balance sheet and cash flow items) have a title row and an
Active row of blue inputs. Fiscal-year columns are blank for cased drivers; for
uncased drivers they aggregate the quarters (sum / avg / last). Annual-only years
hold the user's annual inputs, or carry the prior year forward when none is given.
Columns start at the first quarter of the last actual fiscal year; actual-period
cells of the Active row show the driver's realised value as a green link to the build.
"""
from __future__ import annotations

from typing import Dict, List

from .. import styles as S
from ..engine import DRIVERS, ModelContext, SheetBuilder

SECTION_TITLES = {
    "revenue": "Revenue Drivers",
    "cost": "Cost Drivers",
    "is": "Income Statement Drivers",
    "bs": "Balance Sheet Drivers",
    "cf": "Cash Flow Drivers",
}
SECTION_ORDER = ["revenue", "cost", "is", "bs", "cf"]


def build_drivers(ctx: ModelContext, drivers: List[dict]) -> SheetBuilder:
    sb = SheetBuilder(ctx, DRIVERS, axis=ctx.drv_axis, label_width=58.0, zoom=70, freeze="D11")
    ws = sb.ws
    ws.column_dimensions["A"].width = 1.25
    ws.column_dimensions["C"].width = 12.25
    by_section: Dict[str, List[dict]] = {}
    for d in drivers:
        by_section.setdefault(d.get("section", "revenue"), []).append(d)
    for sec in SECTION_ORDER:
        items = by_section.get(sec)
        if not items:
            continue
        sb.section(SECTION_TITLES[sec], marker=False)
        for d in items:
            _driver_block(sb, d)
    return sb


def _driver_block(sb: SheetBuilder, d: dict):
    ctx, ax = sb.ctx, sb.axis
    fmt = d.get("fmt", "pct_plain")
    cased = d.get("cased", True)
    sb.subtitle(d["label"])
    title_row = sb.row - 1
    if d.get("label_note"):
        ctx.notes.append((DRIVERS, f"B{title_row}", d["label_note"]))
    values = d.get("values") or {}
    notes = d.get("notes") or {}
    single = bool(d.get("single"))   # one input column (a constant such as a price point)
    if single:
        est_pids = [ax.first().pid]
    else:
        est_pids = [p.pid for p in ax.periods if p.estimate and (p.kind == "Q" or p.annual_only)]
    first_row = sb.row
    if cased:
        for case in ctx.cases:
            cv = values.get(case) or {}
            line = {"id": f"drv:{d['id']}:{case}", "label": case, "kind": "none", "fmt": fmt,
                    "values": {pid: cv.get(pid) for pid in est_pids if cv.get(pid) is not None},
                    "notes": (notes.get(case) or {}), "fy": "blank", "input_fill": d.get("input_fill", False),
                    "input_color": S.BLUE, "values_only": True,
                    "fill": S.LIGHT_YELLOW if single else None}
            sb.line(line)
        last_row = sb.row - 1
        active_vals = {}
        for p in ax.periods:
            if single and p.pid != est_pids[0]:
                continue
            if p.kind == "FY" and not p.annual_only:
                continue
            if p.estimate or single:
                active_vals[p.pid] = f"=SUMIF($B${first_row}:$B${last_row},$B$5,{{col}}{first_row}:{{col}}{last_row})"
            elif d.get("target"):
                t = d["target"]
                token = t["line"] + ("." + t["sub"] if t.get("sub") else "")
                active_vals[p.pid] = "={" + token + "}"
        active = {"id": f"drv:{d['id']}", "label": "Active", "kind": "none", "fmt": fmt, "bold": True, "top": True,
                  "values": active_vals, "fy": "blank", "values_only": True,
                  "fill": S.LIGHT_YELLOW if single else None}
        if d.get("hist_values"):
            for pid, v in d["hist_values"].items():
                active_vals.setdefault(pid, v)
        row = sb.line(active)
    else:
        cv = values.get("Active") if "Active" in values else values
        vals = {}
        for p in ax.periods:
            if p.kind == "Q" and p.estimate:
                vals[p.pid] = cv.get(p.pid)
            elif p.kind == "Q" and not p.estimate:
                if d.get("target"):
                    t = d["target"]
                    vals[p.pid] = "={" + t["line"] + ("." + t["sub"] if t.get("sub") else "") + "}"
                elif cv.get(p.pid) is not None:
                    vals[p.pid] = cv.get(p.pid)
            elif p.annual_only:
                if cv.get(p.pid) is not None:
                    vals[p.pid] = cv.get(p.pid)
                elif d.get("annual_dsl"):
                    vals[p.pid] = d["annual_dsl"]
                else:
                    prev = ax.prior_year(p)
                    vals[p.pid] = f"={prev.letter}{{row:drv:{d['id']}}}" if prev else None
        vals = {k: v for k, v in vals.items() if v is not None}
        active = {"id": f"drv:{d['id']}", "label": "Active", "kind": "none", "fmt": fmt, "bold": True, "top": True,
                  "values": vals, "fy": d.get("fy", "sum"), "values_only": True, "input_color": S.BLUE,
                  "notes": (notes.get("Active") if "Active" in notes else notes) or {}}
        row = sb.line(active)
        # FY columns aggregate quarters with the chosen rule
        _fy_aggregates(sb, active, row, d.get("fy", "sum"))
    ctx.drv_rows[d["id"]] = row
    sb.blank()


def _fy_aggregates(sb: SheetBuilder, line: dict, row: int, agg: str):
    ax = sb.axis
    vals = line.setdefault("values", {})
    for p in ax.fys():
        if p.annual_only:
            continue
        qs = ax.quarters_of(p.fy)
        if not qs:
            continue
        rng = f"{qs[0].letter}{row}:{qs[-1].letter}{row}"
        if agg == "sum":
            vals[p.pid] = f"=SUM({rng})"
        elif agg == "avg":
            vals[p.pid] = f"=AVERAGE({rng})"
        elif agg == "last":
            vals[p.pid] = f"={qs[-1].letter}{row}"
        elif agg == "first":
            vals[p.pid] = f"={qs[0].letter}{row}"
