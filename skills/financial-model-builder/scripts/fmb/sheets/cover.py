"""Cover tab (left for the user to design) and the '|' divider tabs."""
from __future__ import annotations

from ..engine import ModelContext
from .. import styles as S


def build_cover(ctx: ModelContext, name: str = "Cover"):
    ws = ctx.wb.create_sheet(name)
    ws.sheet_properties.tabColor = S.GREEN_TS[-6:]
    ws.sheet_view.showGridLines = False
    ws.sheet_view.zoomScale = 130
    ws.column_dimensions["A"].width = 0.0
    ws.column_dimensions["A"].hidden = True
    ws.column_dimensions["B"].width = 8.0
    return ws


def build_divider(ctx: ModelContext, name: str):
    ws = ctx.wb.create_sheet(name)
    ws.sheet_view.showGridLines = False
    ws.column_dimensions["B"].width = 9.0
    return ws
