"""Build a model workbook from a model spec (JSON) and a normalised data file (JSON).

Tab order follows the reference model:
  Cover | Revenue Build, Margin Build, Drivers & Casing || side builds..., Tearsheet, DCF
  ||| Income Statement, Cash Flow Statement, Balance Sheet
"""
from __future__ import annotations

import datetime as dt
import json
from pathlib import Path
from typing import Optional

from openpyxl.worksheet.properties import PageSetupProperties

from .engine import BS, CFS, DCF, DRIVERS, IS, MARGIN, REV, TEARSHEET, ModelContext, SheetBuilder
from .periods import PeriodAxis
from .sheets.cover import build_cover, build_divider
from .sheets.dcf import build_dcf
from .sheets.drivers import build_drivers
from .sheets.side_builds import build_side_build
from .sheets.tearsheet import build_tearsheet

PERIOD_SHEETS = [
    (REV, dict(zoom=70, fy_fill=False, label_width=54.0)),
    (MARGIN, dict(zoom=70, fy_fill=False, label_width=54.0)),
    (IS, dict(zoom=None, fy_fill=True, label_width=54.375)),
    (CFS, dict(zoom=None, fy_fill=True, label_width=54.375)),
    (BS, dict(zoom=None, fy_fill=True, label_width=54.375)),
]


def make_axis(spec: dict) -> PeriodAxis:
    h = spec["horizon"]
    c = spec.get("company", {})
    return PeriodAxis.build(h["first_hist_quarter"], h["last_actual_quarter"], h["last_quarterly_estimate"],
                            h.get("annual_only_years") or [], h.get("period_ends") or {},
                            int(c.get("fiscal_year_end_month", 12)), int(c.get("fiscal_year_end_day", 31)),
                            h.get("report_dates") or {}, annual_hist_years=h.get("annual_hist_years") or [])


def build(spec: dict, data: dict, out_path: str) -> ModelContext:
    axis = make_axis(spec)
    ctx = ModelContext(spec, axis, data)
    company = spec.get("company", {})
    sheets_cfg = spec.get("sheets", {})

    # 1. cover + divider
    build_cover(ctx, company.get("cover_tab") or "Cover")
    build_divider(ctx, "|")
    # 2. builds and drivers (layout pass)
    builders = {}
    for name, opts in PERIOD_SHEETS[:2]:
        cfg = sheets_cfg.get(name, {})
        sb = SheetBuilder(ctx, name, zoom=cfg.get("zoom", opts["zoom"]), fy_fill=opts["fy_fill"], label_width=opts["label_width"])
        builders[name] = (sb, cfg)
    drv = build_drivers(ctx, spec.get("drivers") or [])
    build_divider(ctx, "||")
    # 3. side builds (filled after the layout pass so links to build rows resolve), tearsheet, DCF
    side_specs = spec.get("side_builds") or []
    for sbs in side_specs:
        ctx.wb.create_sheet(sbs["name"])
    ts_cfg = spec.get("tearsheet") or {}
    # tearsheet is created now to keep the tab order, filled after the DCF exists
    ts_ws = ctx.wb.create_sheet(TEARSHEET)
    build_divider(ctx, "|||")
    for name, opts in PERIOD_SHEETS[2:]:
        cfg = sheets_cfg.get(name, {})
        sb = SheetBuilder(ctx, name, zoom=cfg.get("zoom", opts["zoom"]), fy_fill=opts["fy_fill"], label_width=opts["label_width"])
        builders[name] = (sb, cfg)
    # lay out all period sheets (rows + ids), then DCF (needs IS/BS/CFS ids)
    for name, (sb, cfg) in builders.items():
        sb.blocks(cfg.get("blocks") or [])
    dcf_sb = build_dcf(ctx, spec.get("dcf") or {})
    # move DCF right after the tearsheet
    wb = ctx.wb
    wb._sheets.remove(dcf_sb.ws)
    wb._sheets.insert(wb._sheets.index(ts_ws) + 1, dcf_sb.ws)
    # 4. write every cell, then fill the side builds (their cells may reference build rows)
    ctx.finalize()
    for sbs in side_specs:
        wb.remove(wb[sbs["name"]])
        ws_side = build_side_build(ctx, sbs)
        wb._sheets.remove(ws_side)
        wb._sheets.insert(wb._sheets.index(ts_ws), ws_side)
    # 5. tearsheet (needs registry rows and DCF cells)
    wb.remove(ts_ws)
    ts = build_tearsheet(ctx, ts_cfg)
    wb._sheets.remove(ts)
    wb._sheets.insert(wb._sheets.index(dcf_sb.ws), ts)
    ctx.finalize()
    # 6. metadata and save (plus a map of rows and cells for post-processing steps)
    _stamp(ctx)
    wb.active = 0
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    wb.save(out_path)
    Path(out_path).with_suffix(".map.json").write_text(json.dumps(model_map(ctx), indent=1), encoding="utf-8")
    return ctx


def model_map(ctx: ModelContext) -> dict:
    lines: dict = {}
    for (sheet, lid), row in ctx.registry.items():
        lines.setdefault(sheet, {})[lid] = row
    return {"columns": {p.pid: p.letter for p in ctx.axis.periods},
            "drivers_columns": {p.pid: p.letter for p in ctx.drv_axis.periods},
            "lines": lines, "drivers": ctx.drv_rows, "dcf": ctx.dcf_cells,
            "tearsheet": getattr(ctx, "tearsheet_cells", {})}


def _stamp(ctx: ModelContext):
    wb = ctx.wb
    author = ctx.author or "Analyst"
    wb.properties.creator = author
    wb.properties.lastModifiedBy = author
    wb.properties.title = None
    wb.properties.description = None
    wb.properties.subject = None
    wb.properties.keywords = None
    wb.properties.category = None
    wb.properties.created = dt.datetime.now()
    wb.properties.modified = dt.datetime.now()
    for ws in wb.worksheets:
        ws.sheet_properties.pageSetUpPr = PageSetupProperties(fitToPage=False)


def build_from_files(spec_path: str, data_path: Optional[str], out_path: str) -> ModelContext:
    spec = json.loads(Path(spec_path).read_text(encoding="utf-8"))
    data = json.loads(Path(data_path).read_text(encoding="utf-8")) if data_path else {}
    series = data.get("series", data)
    return build(spec, series, out_path)
