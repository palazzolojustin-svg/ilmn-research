"""Side-build tabs (ARPU bridge, margin bridge, ...): free-form sheets rendered from a
small cell/table spec so the house style is kept without hand-formatting.

spec = {
  "name": "ARPU Bridge", "zoom": 70, "widths": {"B": 59.9, "C": 9.4, ...},
  "cells": [ {"cell": "B2", "value": "27E Pricing ARPU Bridge", "bold": true},
             {"cell": "C3", "value": 170, "fmt": "bps"},
             {"cell": "C7", "value": "=(C3-C4+C5)*3/C6", "fmt": "bps", "bold": true, "fill": "E8E8E8"} ],
  "period_tables": [ {"anchor": "H13", "from": "3Q25", "lines": {"ab_contrib": {"label": "...", "fmt": "bps", "values": {"3Q25": 13.5, ...}}} } ]
}
Other sheets link to side-build cells by address (e.g. ='ARPU Bridge'!F3/10000 typed in a
driver's Base row), so keep output cells at stable addresses.
Values are written as given: numbers blue, formulas black, cross-sheet formulas green.
Driver Base-case cells on Drivers & Casing can link here with "='ARPU Bridge'!F3/10000".
"""
from __future__ import annotations

from .. import styles as S
from ..engine import ModelContext


def build_side_build(ctx: ModelContext, spec: dict):
    ws = ctx.wb.create_sheet(spec["name"])
    ws.sheet_view.showGridLines = False
    if spec.get("zoom"):
        ws.sheet_view.zoomScale = spec["zoom"]
    ws.column_dimensions["A"].width = 2.0
    ws.column_dimensions["B"].width = 56.0
    for k, v in (spec.get("widths") or {}).items():
        ws.column_dimensions[k].width = v
    from ..engine import SheetBuilder
    res = SheetBuilder.resolver(ctx, spec["name"])
    anchor = ctx.axis.first()
    for c in spec.get("cells") or []:
        cell = ws[c["cell"]]
        v = c.get("value")
        if isinstance(v, str) and v.startswith("=") and "{" in v:
            v = res.formula(v, anchor)
        color = c.get("color")
        if color is None and v is not None:
            color = S.color_for(v)
        fill_rgb = c.get("fill")
        if fill_rgb and len(fill_rgb) == 6:
            fill_rgb = "FF" + fill_rgb
        S.style_cell(cell, v, fmt=c.get("fmt"), bold=c.get("bold", False), italic=c.get("italic", False),
                     color=color or S.BLACK, fill_rgb=fill_rgb, top=c.get("top", False), bottom=c.get("bottom", False),
                     align=c.get("align"))
        if c.get("note"):
            ctx.notes.append((spec["name"], c["cell"], c["note"]))
    for m in spec.get("merge") or []:
        ws.merge_cells(m)
    for t in spec.get("period_tables") or []:
        _period_table(ctx, ws, t)
    return ws


def _period_table(ctx: ModelContext, ws, t: dict):
    """A labelled row set across a period header, starting at `anchor` (label column)."""
    from openpyxl.utils import column_index_from_string, coordinate_from_string
    col_letter, row = coordinate_from_string(t["anchor"])
    col0 = column_index_from_string(col_letter)
    sub = ctx.axis.sub_axis(t.get("from", ctx.axis.first().pid), start_col=col0 + 1)
    for p in sub.periods:
        S.style_cell(ws.cell(row=row, column=p.col), p.label, bold=True, color=S.BLACK)
    r = row + 1
    lines = t.get("lines") or t.get("line_ids") or {}
    if not lines:
        raise ValueError(f"period table at {t['anchor']} has no 'lines'")
    for lid, line in lines.items():
        S.style_cell(ws.cell(row=r, column=col0), line.get("label", lid), bold=line.get("bold", True), color=S.BLACK)
        vals = line.get("values") or {}
        for p in sub.periods:
            v = vals.get(p.pid)
            if v is None:
                continue
            S.style_cell(ws.cell(row=r, column=p.col), v, fmt=line.get("fmt", "bps"), bold=line.get("bold", True),
                         color=S.color_for(v))
        r += 1
