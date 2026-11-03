"""Every visual rule of the reference model, in one place.

Colour rule (user's convention): blue = hardcoded input, black = calculation,
green = link from a different sheet. Section headers are white-on-navy (003765),
delta-to-consensus rows are bold italic on yellow, key input cells sit on light
yellow (FFFFCC), estimate-period headers and sub-section bands are light grey
(E8E8E8), statement fiscal-year columns are very light grey (F2F2F2).
"""
from __future__ import annotations

from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

FONT_NAME = "Arial"
FONT_SIZE = 11

BLUE = "FF0000FF"
BLACK = "FF000000"
GREEN = "FF008000"
WHITE = "FFFFFFFF"
RED = "FFFF0000"
NAVY = "FF003765"
YELLOW = "FFFFFF00"
LIGHT_YELLOW = "FFFFFFCC"
GREY_BAND = "FFE8E8E8"      # estimate headers, sub-section bands (theme lt2 in the reference)
GREY_FY = "FFF2F2F2"        # statement FY columns, drivers FY headers
GREY_PT = "FFD9D9D9"        # price-target rows on the tearsheet
GREEN_TS = "FF19B350"       # tearsheet block headers and cover tab colour

NUMBER_FORMATS = {
    # builds
    "amount": r'#,##0;\(#,##0\)',
    "pct": r'0.0%;\(0.0%\);\-\%',
    "pct_plain": "0.0%",
    "bps": r'0"bps";\(0"bps"\)',
    "bps_delta": r'#,##0" bps";\(#,##0\)" bps";\-',
    "pct_cons": r'0.0%;\(0.0%\);\-',
    "kpi": r'0.0;\(0.0\)',
    "price": r'\$0.00;\(\$0.00\)',   # per-unit currency amount; currency symbol swapped at runtime
    # statements and drivers
    "amount_s": r'#,##0_);(#,##0)',
    "pct_s": r'0.0%_);\(0.0%\)',
    "shares": r'#,##0.00_);(#,##0.00)',
    "eps": r'0.00_);\(0.00\)',
    "number1": "0.0",
    "number2": "0.00",
    "number4": "0.0000",
    # dcf / tearsheet
    "amount_d": r'#,##0;\(#,##0\);"-"',
    "pct_d": r'0.0%;\(0.0%\);"-"',
    "mult": r'0.0\x',
    "px": r'"$"#,##0.00',
    "px_acct": r'_([$$-409]* #,##0.00_);_([$$-409]* \(#,##0.00\);_([$$-409]* "-"??_);_(@_)',
    "weight": "0%",
    "date": "mm-dd-yy",
    "int": "0",
    "general": "General",
}

CURRENCY_SYMBOLS = {"USD": "$", "EUR": "€", "GBP": "£", "JPY": "¥", "CNY": "¥", "CHF": "CHF ", "CAD": "C$",
                    "AUD": "A$", "SEK": "kr", "DKK": "kr", "NOK": "kr", "HKD": "HK$", "INR": "₹", "KRW": "₩"}


def price_format(currency: str) -> str:
    sym = CURRENCY_SYMBOLS.get((currency or "USD").upper(), "$")
    if len(sym) == 1:
        return rf'\{sym}0.00;\(\{sym}0.00\)'
    return rf'"{sym}"0.00;\("{sym}"0.00\)'


def px_format(currency: str) -> str:
    sym = CURRENCY_SYMBOLS.get((currency or "USD").upper(), "$")
    return rf'"{sym}"#,##0.00'


def font(color: str = BLACK, bold: bool = False, italic: bool = False, size: int = FONT_SIZE) -> Font:
    return Font(name=FONT_NAME, size=size, bold=bold, italic=italic, color=color)


def fill(rgb: str) -> PatternFill:
    return PatternFill(fill_type="solid", fgColor=rgb, bgColor=rgb)


THIN = Side(style="thin")
NO_SIDE = Side(style=None)


def border(top: bool = False, bottom: bool = False, left: bool = False, right: bool = False) -> Border:
    return Border(top=THIN if top else NO_SIDE, bottom=THIN if bottom else NO_SIDE,
                  left=THIN if left else NO_SIDE, right=THIN if right else NO_SIDE)


def color_for(value) -> str:
    """Apply the colour rule to a cell value: formulas referencing another sheet are
    green, other formulas black, constants blue."""
    if isinstance(value, str) and value.startswith("="):
        return GREEN if "!" in value else BLACK
    if isinstance(value, (int, float)):
        return BLUE
    return BLACK


def style_cell(cell, value=None, *, fmt: str | None = None, bold: bool = False, italic: bool = False,
               color: str | None = None, fill_rgb: str | None = None, top: bool = False,
               bottom: bool = False, align: str | None = None, keep_fill: bool = False):
    """Write a value and apply the house style in one call. Colour defaults to the
    colour rule unless `color` is given."""
    if value is not None:
        cell.value = value
    c = color or (color_for(cell.value) if cell.value is not None else BLACK)
    cell.font = font(c, bold, italic)
    if fmt:
        cell.number_format = NUMBER_FORMATS.get(fmt, fmt)
    if fill_rgb:
        cell.fill = fill(fill_rgb)
    elif not keep_fill:
        pass
    if top or bottom:
        cell.border = border(top=top, bottom=bottom)
    if align:
        cell.alignment = Alignment(horizontal=align)
    return cell


def setup_period_sheet(ws, label_width: float = 54.0, data_width: float = 13.75, last_col: int = 36,
                       zoom: int | None = 70, freeze: str | None = "D11"):
    """Column widths, zoom, gridlines and freeze panes shared by every period sheet."""
    ws.sheet_view.showGridLines = False
    if zoom:
        ws.sheet_view.zoomScale = zoom
    ws.column_dimensions["A"].width = 2.0
    ws.column_dimensions["B"].width = label_width
    ws.column_dimensions["C"].width = 2.0
    for c in range(4, last_col + 1):
        ws.column_dimensions[get_column_letter(c)].width = data_width
    for c in range(last_col + 1, last_col + 4):
        ws.column_dimensions[get_column_letter(c)].width = 10.0
    if freeze:
        ws.freeze_panes = freeze
    ws.sheet_format.defaultRowHeight = 14.25
    ws.row_dimensions[2].height = 18.0
    ws.row_dimensions[3].height = 18.0


def set_row_heights(ws, rows: dict):
    for r, h in rows.items():
        ws.row_dimensions[r].height = h
