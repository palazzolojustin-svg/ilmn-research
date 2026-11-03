"""Per-case values for the Tearsheet.

The statements compute only the active case. The reference model therefore holds each
case's valuation metric (for example FY28E Adj. EBITDA under Bull) as a typed value
in the Tearsheet. This module reproduces that: it flips the case cell on Drivers &
Casing through Excel, recalculates, reads the metric for every target block, writes
the values into the Tearsheet metric cells (blue, as typed inputs) and restores the
active case. Needs the model map written next to the model at build time.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict

from openpyxl import load_workbook

from . import styles as S


def snapshot_cases(model_path: str, spec_path: str, map_path: str | None = None) -> Dict[str, Dict[str, float]]:
    from .excel import ExcelSession
    spec = json.loads(Path(spec_path).read_text(encoding="utf-8"))
    map_path = map_path or str(Path(model_path).with_suffix(".map.json"))
    mp = json.loads(Path(map_path).read_text(encoding="utf-8"))
    metric_row = mp["lines"]["Income Statement"].get(spec["tearsheet"]["metric_line"])
    cols = mp["columns"]
    blocks = spec["tearsheet"]["blocks"]
    cases = spec["cases"]
    values: Dict[str, Dict[str, float]] = {}
    with ExcelSession(model_path) as xl:
        drv = xl.wb.Worksheets("Drivers & Casing")
        is_ws = xl.wb.Worksheets("Income Statement")
        original = drv.Range("B5").Value2
        for case in cases:
            drv.Range("B5").Value2 = case
            xl.app.CalculateFullRebuild()
            values[case] = {}
            for b in blocks:
                col = cols.get(b.get("metric_period"))
                if col and metric_row:
                    values[case][b["label"]] = is_ws.Range(f"{col}{metric_row}").Value2
        drv.Range("B5").Value2 = original
        xl.app.CalculateFullRebuild()
        drv = is_ws = None
    # write the typed values into the tearsheet (openpyxl keeps everything else intact) ...
    wb = load_workbook(model_path)
    ts = wb["Tearsheet"]
    for case, per_block in values.items():
        for label, v in per_block.items():
            cell = mp["tearsheet"]["metric_cells"].get(case, {}).get(label)
            if cell and v is not None:
                ts[cell].value = v
                ts[cell].font = S.font(S.BLUE, True)
    wb.save(model_path)
    # ... then recalculate and save once more so the delivered file carries calculated values
    with ExcelSession(model_path) as xl:
        xl.app.CalculateFullRebuild()
        xl.save()
    return values
