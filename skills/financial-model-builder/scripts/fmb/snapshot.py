"""Render a worksheet range to a PNG so the look of a built model can be checked
against the reference model. Windows + Excel: the range is exported to PDF by Excel
(headless) and rasterised with pypdfium2.

Usage: python -m fmb.snapshot <workbook.xlsx> "<Sheet>!A1:T60" <out.png> [scale]
"""
from __future__ import annotations

import os
import sys
import tempfile
from pathlib import Path


def snapshot(path: str, ref: str, out_png: str, scale: float = 2.0) -> str:
    import pypdfium2 as pdfium

    from .excel import ExcelSession

    path = str(Path(path).resolve())
    out_png = str(Path(out_png).resolve())
    sheet, rng = ref.split("!", 1)
    pdf_path = os.path.join(tempfile.gettempdir(), f"fmb_snap_{os.getpid()}.pdf")
    with ExcelSession(path, read_only=True) as xl:
        ws = xl.wb.Worksheets(sheet.strip("'"))
        ps = ws.PageSetup
        ps.PrintArea = rng
        ps.Zoom = False
        ps.FitToPagesWide = 1
        ps.FitToPagesTall = 1
        ps.Orientation = 2  # landscape
        ps.LeftMargin = ps.RightMargin = ps.TopMargin = ps.BottomMargin = 10
        ws.ExportAsFixedFormat(0, pdf_path)  # xlTypePDF
        ps = ws = None
    pdf = pdfium.PdfDocument(pdf_path)
    page = pdf[0]
    img = page.render(scale=scale).to_pil()
    img.save(out_png)
    try:
        os.remove(pdf_path)
    except OSError:
        pass
    return out_png


if __name__ == "__main__":
    p, ref, out = sys.argv[1:4]
    sc = float(sys.argv[4]) if len(sys.argv) > 4 else 2.0
    print(snapshot(p, ref, out, sc))
