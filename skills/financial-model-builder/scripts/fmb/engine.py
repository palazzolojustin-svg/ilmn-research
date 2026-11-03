"""Core engine: sheet builders, the line registry and the formula mini-language.

A model is a set of period sheets that share one column axis. Every row of substance
is a *line* with an id. Formulas are written in a small template language whose
tokens resolve to cell references for the column being written:

    {id}            same period, line `id` (local sheet first, then other sheets -> green link)
    {id@py}         prior year (same quarter last year; prior FY for annual columns)
    {id@pq}         prior period (prior quarter; prior FY for annual columns)
    {id@-2}         n periods back (quarters for quarterly columns, years for annual ones)
    {id@4Q25}       a specific period's column
    {id@4Q25$}      ... as an absolute reference ($T$59)
    {id.pct_yoy}    a variance sub-row of a line
    {Sheet Name!id} an explicit cross-sheet reference
    {sumq:id} {avgq:id} {lastq:id} {firstq:id}   the four quarters of this FY column
    {drv:id}        the Active row of driver `id` on Drivers & Casing (same period)
    {months} {weeks} {case} {col} {row:id}

Two passes: `line()` lays rows out and registers ids; `finalize()` writes every
cell, so forward and cross-sheet references always resolve.
"""
from __future__ import annotations

import datetime as dt
import re
from typing import Any, Callable, Dict, List, Optional

from openpyxl import Workbook
from openpyxl.comments import Comment
from openpyxl.styles import Alignment
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

from . import styles as S
from .periods import Period, PeriodAxis, parse_pid, pid_of

DRIVERS = "Drivers & Casing"
REV = "Revenue Build"
MARGIN = "Margin Build"
IS = "Income Statement"
BS = "Balance Sheet"
CFS = "Cash Flow Statement"
DCF = "DCF"
TEARSHEET = "Tearsheet"

LOOKUP_ORDER = [REV, MARGIN, IS, BS, CFS, DRIVERS, DCF]

TOKEN_RE = re.compile(r"\{([^{}]+)\}")

# Variance sub-rows. `needs` says which prior column must exist for the row to be
# written in a column; `q_only` rows are left blank in fiscal-year columns.
SUB_DEFS: Dict[str, Dict[str, Any]] = {
    "pct_yoy":      dict(label="% yoy", dsl="={id}/{id@py}-1", fmt="pct", italic=True, needs="py"),
    "pct_2y":       dict(label="% 2y stack", dsl="={id.pct_yoy}+{id.pct_yoy@py}", fmt="pct", italic=True, needs="py2"),
    "usd_yoy":      dict(label="$ yoy", dsl="={id}-{id@py}", fmt=None, italic=False, needs="py"),
    "pct_qoq":      dict(label="% qoq", dsl="={id}/{id@pq}-1", fmt="pct", italic=True, needs="pq", q_only=True),
    "usd_qoq":      dict(label="$ qoq", dsl="={id}-{id@pq}", fmt=None, italic=False, needs="pq", q_only=True),
    "pct_total":    dict(label="% total", dsl="={id}/{total}", fmt="pct", italic=True),
    "bps_yoy":      dict(label="bps yoy", dsl="=({id}-{id@py})*10000", fmt="bps", italic=True, needs="py"),
    "bps_2y":       dict(label="bps 2y stack", dsl="={id.bps_yoy}+{id.bps_yoy@py}", fmt="bps", italic=True, needs="py2"),
    "bps_qoq":      dict(label="bps qoq", dsl="=({id}-{id@pq})*10000", fmt="bps", italic=True, needs="pq", q_only=True),
    "net_adds_yoy": dict(label="yoy net adds", dsl="={id}-{id@py}", fmt="kpi", italic=False, needs="py"),
    "net_adds_qoq": dict(label="qoq net adds", dsl="={id}-{id@pq}", fmt="kpi", italic=False, needs="pq", q_only=True),
    "pct_of":       dict(label="% of Revenue", dsl="={id}/{base}", fmt="pct", italic=True),
}

# Default variance rows by line kind (order matters: it is the order on the sheet)
DEFAULT_SUBS = {
    "amount": ["pct_yoy", "pct_2y", "usd_yoy", "pct_qoq", "usd_qoq"],
    "count": ["net_adds_yoy", "pct_yoy", "net_adds_qoq", "pct_qoq"],
    "price": ["pct_yoy", "pct_2y", "usd_yoy", "pct_qoq", "usd_qoq"],
    "pct": ["bps_yoy", "bps_2y", "bps_qoq"],
    "none": [],
}

KIND_FMT = {"amount": "amount", "count": "kpi", "price": "price", "pct": "pct", "bps": "bps",
            "shares": "shares", "eps": "eps", "mult": "mult", "number1": "number1", "number2": "number2",
            "int": "int", "date": "date"}


class ModelContext:
    """Workbook-wide state shared by all sheet builders."""

    def __init__(self, spec: dict, axis: PeriodAxis, data: dict):
        self.spec = spec
        self.axis = axis
        self.data = data or {}
        self.wb = Workbook()
        self.wb.remove(self.wb.active)
        self.sheets: Dict[str, "SheetBuilder"] = {}
        self.registry: Dict[tuple, int] = {}         # (sheet, id) -> row
        self.line_defs: Dict[tuple, dict] = {}       # (sheet, id) -> line def
        self.drv_rows: Dict[str, int] = {}           # driver id -> Active row on Drivers
        self.drv_axis = axis.sub_axis(axis.drivers_start_pid())
        self.notes: List[tuple] = []                 # (sheet, cell, text)
        self.dcf_cells: dict = {}
        company = spec.get("company", {})
        self.reporting_ccy = company.get("reporting_currency", "USD")
        self.trading_ccy = company.get("trading_currency", self.reporting_ccy)
        self.units = company.get("units", "mm")
        self.author = company.get("author", "")
        self.cases = spec.get("cases") or ["Bear", "Base", "Bull"]
        self.active_case = spec.get("active_case", "Base")
        S.NUMBER_FORMATS["price"] = S.price_format(self.reporting_ccy)
        S.NUMBER_FORMATS["px"] = S.px_format(self.trading_ccy)

    # ---- registry ----------------------------------------------------------------
    def register(self, sheet: str, line_id: str, row: int, line_def: dict):
        if (sheet, line_id) in self.registry and self.registry[(sheet, line_id)] != row:
            raise ValueError(f"duplicate line id {line_id!r} on {sheet} (rows {self.registry[(sheet, line_id)]} and {row})")
        self.registry[(sheet, line_id)] = row
        self.line_defs[(sheet, line_id)] = line_def

    def find(self, line_id: str, prefer: Optional[str] = None, exclude: Optional[str] = None) -> Optional[tuple]:
        """Return (sheet, row) for a line id; local sheet first, then the lookup order."""
        if prefer and (prefer, line_id) in self.registry and prefer != exclude:
            return prefer, self.registry[(prefer, line_id)]
        for sh in LOOKUP_ORDER + [s for s in self.sheets if s not in LOOKUP_ORDER]:
            if sh == exclude:
                continue
            if (sh, line_id) in self.registry:
                return sh, self.registry[(sh, line_id)]
        return None

    def sheet_axis(self, sheet: str) -> PeriodAxis:
        sb = self.sheets.get(sheet)
        return sb.axis if sb else self.axis

    def title_line(self) -> str:
        c = self.spec.get("company", {})
        name, ticker, exch = c.get("name", ""), c.get("ticker", ""), c.get("exchange", "")
        return f"{name} ({exch}: {ticker})" if exch else f"{name} ({ticker})"

    def units_line(self) -> str:
        sym = S.CURRENCY_SYMBOLS.get(self.reporting_ccy.upper(), self.reporting_ccy + " ")
        unit = {"mm": "mm", "m": "mm", "millions": "mm", "k": "000s", "thousands": "000s", "bn": "bn", "billions": "bn"}.get(
            str(self.units).lower(), str(self.units))
        return f"{sym.strip()} in {unit} except per share data"

    def finalize(self):
        for sb in self.sheets.values():
            sb.flush()
        for sheet, cell, text in self.notes:
            if not text:
                continue
            c = self.wb[sheet][cell]
            c.comment = Comment(str(text), self.author or "Analyst")
        self.notes = []


class SheetBuilder:
    """One period sheet: lays out lines and writes them on flush()."""

    @classmethod
    def resolver(cls, ctx: "ModelContext", title: str) -> "SheetBuilder":
        """A worksheet-less instance used to resolve tokens for free-form sheets
        (side builds): only tokens with explicit periods or row lookups make sense there."""
        self = cls.__new__(cls)
        self.ctx, self.title, self.axis = ctx, title, ctx.axis
        self.pending, self.fy_fill, self.last_col = [], False, ctx.axis.last_col()
        return self

    def __init__(self, ctx: ModelContext, title: str, axis: Optional[PeriodAxis] = None,
                 label_width: float = 54.0, zoom: Optional[int] = 70, freeze: Optional[str] = "D11",
                 fy_fill: bool = False, header: bool = True):
        self.ctx = ctx
        self.title = title
        self.axis = axis or ctx.axis
        self.ws = ctx.wb.create_sheet(title)
        self.row = 1
        self.pending: List[dict] = []
        self.fy_fill = fy_fill
        self.last_col = self.axis.last_col()
        ctx.sheets[title] = self
        S.setup_period_sheet(self.ws, label_width=label_width, last_col=self.last_col, zoom=zoom, freeze=freeze)
        if header:
            self.header_block()

    # ---- layout helpers ----------------------------------------------------------
    @property
    def letter_last(self) -> str:
        return get_column_letter(self.last_col)

    def cols(self):
        return range(4, self.last_col + 1)

    def header_block(self):
        ws, ctx, ax = self.ws, self.ctx, self.axis
        S.style_cell(ws["B2"], ctx.title_line(), bold=True, color=S.BLACK)
        ws["B2"].font = S.font(S.BLACK, True, False, 14)
        S.style_cell(ws["B3"], ctx.units_line(), italic=True, color=S.BLACK)
        if self.title == DRIVERS:
            S.style_cell(ws["B5"], ctx.active_case, bold=True, color=S.BLACK, top=True, bottom=True, align="center")
            dv = DataValidation(type="list", formula1='"' + ",".join(ctx.cases) + '"', allow_blank=False)
            ws.add_data_validation(dv)
            dv.add(ws["B5"])
        else:
            S.style_cell(ws["B5"], f"='{DRIVERS}'!B5", bold=True, color=S.BLACK, top=True, bottom=True, align="center")
        S.style_cell(ws["B7"], "Fiscal Year", bold=True, color=S.BLACK, top=True)
        S.style_cell(ws["C7"], None, top=True)
        S.style_cell(ws["B8"], "Period Ending", color=S.BLACK)
        S.style_cell(ws["B9"], "Weeks in Period", color=S.BLACK)
        drivers = self.title == DRIVERS
        if not drivers:
            S.style_cell(ws["B10"], "Earnings Report", color=S.BLACK)
        # hidden helper date before the first column (white font), as in the reference
        prev = ax.first()
        prev_end = None
        if prev.end:
            prev_end = prev.end - dt.timedelta(days=91)
            S.style_cell(ws["C8"], prev_end, fmt="date", color=S.WHITE)
        for p in ax.periods:
            L = p.letter
            hdr = ws[f"{L}7"]
            band = (p.estimate and not drivers) or (drivers and p.kind == "FY")
            fill_rgb = (S.GREY_FY if drivers else S.GREY_BAND) if band else None
            S.style_cell(hdr, p.label, bold=True, color=S.BLACK, top=True, fill_rgb=fill_rgb, align="center")
            if p.end:
                S.style_cell(ws[f"{L}8"], p.end, fmt="date", color=S.BLACK, fill_rgb=fill_rgb, align="center")
            if p.kind == "Q":
                S.style_cell(ws[f"{L}9"], p.weeks or 13, color=S.BLACK, fill_rgb=fill_rgb, fmt="general", align="center")
            elif p.annual_only or not ax.quarters_of(p.fy):
                S.style_cell(ws[f"{L}9"], p.weeks or 52, color=S.BLACK, fill_rgb=fill_rgb, fmt="int", align="center")
            else:
                qs = ax.quarters_of(p.fy)
                S.style_cell(ws[f"{L}9"], f"=SUM({qs[0].letter}9:{qs[-1].letter}9)", color=S.BLACK, fill_rgb=fill_rgb, align="center")
            if not drivers and p.report_date and not p.estimate:
                S.style_cell(ws[f"{L}10"], p.report_date, fmt="date", color=S.BLACK, align="center")
        # the reference puts a thin top border on row 7 across the width
        for c in range(2, self.last_col + 1):
            cell = ws.cell(row=7, column=c)
            cell.border = S.border(top=True)
        if drivers:
            S.set_row_heights(ws, {5: 15.0, 6: 4.5, 7: 15.0, 8: 15.0, 9: 15.0, 10: 4.5})
            self.row = 11
        else:
            S.set_row_heights(ws, {5: 15.0, 7: 15.0, 8: 15.0, 9: 15.0, 10: 15.0, 11: 4.5})
            self.row = 12

    def section(self, title: str, marker: bool = True) -> int:
        """Navy section header across the width (white bold label in B, 'x' marker in A)."""
        r = self.row
        if marker:
            S.style_cell(self.ws[f"A{r}"], "x", color=S.BLACK, align="center")
        S.style_cell(self.ws[f"B{r}"], title, bold=True, color=S.WHITE, fill_rgb=S.NAVY)
        for c in range(3, self.last_col + 1):
            self.ws.cell(row=r, column=c).fill = S.fill(S.NAVY)
        self.ws.row_dimensions[r].height = 15.0
        self.row += 2
        return r

    def band(self, title: str, marker: bool = True) -> int:
        """Grey sub-section band ('Premium:' style)."""
        r = self.row
        if marker:
            S.style_cell(self.ws[f"A{r}"], "x", color=S.BLACK)
        S.style_cell(self.ws[f"B{r}"], title, bold=True, color=S.BLACK, fill_rgb=S.GREY_BAND)
        for c in range(3, self.last_col + 1):
            self.ws.cell(row=r, column=c).fill = S.fill(S.GREY_BAND)
        self.row += 1
        return r

    def subtitle(self, title: str, marker: bool = False) -> int:
        """Bold label row without fill ('Totals:' / 'Research & Development:')."""
        r = self.row
        if marker:
            S.style_cell(self.ws[f"A{r}"], "x", color=S.BLACK)
        S.style_cell(self.ws[f"B{r}"], title, bold=True, color=S.BLACK)
        self.row += 1
        return r

    def blank(self, n: int = 1):
        self.row += n

    def label_only(self, text: str, bold: bool = False, italic: bool = False, fill_rgb: str | None = None) -> int:
        r = self.row
        S.style_cell(self.ws[f"B{r}"], text, bold=bold, italic=italic, color=S.BLACK, fill_rgb=fill_rgb)
        self.row += 1
        return r

    # ---- lines ---------------------------------------------------------------------
    def line(self, line: dict, with_subs: Optional[bool] = None) -> int:
        """Lay out a line (and its variance sub-rows) and register it. Cells are
        written on flush()."""
        line = dict(line)
        line.setdefault("kind", "amount")
        line.setdefault("bold", False)
        line.setdefault("italic", False)
        line.setdefault("fy", "sum")
        if line["fy"] == "formula" and not line.get("fy_dsl") and not line.get("dsl") and "{drv:" in (line.get("proj_dsl") or ""):
            raise ValueError(f"{line['id']}: fy='formula' needs fy_dsl (the fiscal-year cells of cased drivers are blank)")
        r = self.row
        line["row"] = r
        self.ctx.register(self.title, line["id"], r, line)
        self.pending.append(line)
        self.row += 1
        subs = line.get("subs")
        if subs is None and with_subs:
            subs = DEFAULT_SUBS.get(line["kind"], [])
        for sub in subs or []:
            sdef = dict(SUB_DEFS[sub] if isinstance(sub, str) else sub)
            key = sub if isinstance(sub, str) else sub["key"]
            labels = line.get("sub_labels", {})
            sid = f"{line['id']}.{key}"
            sline = {
                "id": sid, "label": labels.get(key, sdef["label"]), "kind": "sub",
                "fmt": sdef.get("fmt") or line.get("fmt") or KIND_FMT.get(line["kind"], "amount"),
                "italic": sdef.get("italic", False), "bold": False,
                "dsl": sdef["dsl"].replace("{id", "{" + line["id"]).replace("{total}", "{" + str(line.get("total", "total_rev")) + "}")
                       .replace("{base}", "{" + str(line.get("base", "total_rev")) + "}"),
                "needs": sdef.get("needs"), "q_only": sdef.get("q_only", False), "fy": "formula",
                "parent": line["id"], "sub_key": key, "row": self.row,
            }
            # driver-fed sub-row: projections link to the driver's Active row
            drv = line.get("driver") or {}
            if drv and drv.get("sub") == key:
                sline["proj_dsl"] = "={drv:" + drv["id"] + "}"
                sline["annual_dsl"] = "={drv:" + drv["id"] + "}"
            if sdef.get("needs") == "py2":
                sline["needs"] = "py2"
            sub_start = (line.get("sub_start") or {}).get(key)
            if sub_start:
                sline["start"] = sub_start
            self.ctx.register(self.title, sid, self.row, sline)
            self.pending.append(sline)
            self.row += 1
        return r

    # ---- resolution ----------------------------------------------------------------
    def _col_for(self, sheet: str, p: Period) -> Optional[int]:
        ax = self.ctx.sheet_axis(sheet)
        q = ax.by_id.get(p.pid)
        return q.col if q else None

    def _shift(self, ax: PeriodAxis, p: Period, off: Optional[str]) -> Optional[Period]:
        if not off:
            return ax.by_id.get(p.pid)
        base = ax.by_id.get(p.pid)
        if base is None:
            return None
        if off == "py":
            return ax.prior_year(base)
        if off == "pq":
            return ax.prior_period(base)
        if off == "fy":
            return ax.fy_of(base)
        if re.fullmatch(r"[+-]\d+", off):
            return ax.offset(base, int(off))
        parsed = parse_pid(off)
        if parsed:
            k, y, q = parsed
            return ax.by_id.get(pid_of(k, y, q))
        raise ValueError(f"unknown offset {off!r}")

    def ref(self, token: str, p: Period, cur_line: Optional[str] = None) -> Optional[str]:
        """Resolve one token (without braces) for period p. Returns None when the
        reference does not exist (the cell is then left blank)."""
        ctx = self.ctx
        t = token.strip()
        if t == "months":
            return str(p.months)
        if t == "weeks":
            return f"{p.letter}$9"
        if t == "case":
            return f"'{DRIVERS}'!$B$5"
        if t == "col":
            return p.letter
        if t.startswith("row:"):
            found = ctx.find(t[4:], prefer=self.title)
            return str(found[1]) if found else None
        if t.startswith("data:"):
            v = (ctx.data.get(t[5:]) or {}).get(p.pid)
            if v is None:
                return None
            self._typed_input = True
            return str(v) if not (isinstance(v, str) and v.startswith("=")) else v[1:]
        absolute = t.endswith("$")
        if absolute:
            t = t[:-1]
        fn = None
        m = re.fullmatch(r"(sumq|avgq|lastq|firstq):(.+)", t)
        if m:
            fn, t = m.group(1), m.group(2)
        sheet_hint = None
        if "!" in t:
            sheet_hint, t = t.split("!", 1)
        off = None
        if "@" in t:
            t, off = t.split("@", 1)
        if t.startswith("drv:"):
            did = t[4:]
            row = ctx.drv_rows.get(did)
            if row is None and ":" in did:
                row = ctx.registry.get((DRIVERS, "drv:" + did))   # a case row: drv:<driver>:<Case>
            if row is None:
                raise KeyError(f"driver {did!r} not found on {DRIVERS}")
            sheet, ax = DRIVERS, ctx.drv_axis
        elif sheet_hint:
            # an explicit sheet must hold the line; never fall back to another sheet
            if (sheet_hint, t) not in ctx.registry:
                raise KeyError(f"line {t!r} is not on sheet {sheet_hint!r} (token {token!r} from {self.title})")
            sheet, row = sheet_hint, ctx.registry[(sheet_hint, t)]
            ax = ctx.sheet_axis(sheet)
        else:
            # a plain {id} inside the formula of line `id` means the same-named line on
            # another sheet (a link); with an offset it is a local lag of itself
            exclude = self.title if (t == cur_line and off is None) else None
            found = ctx.find(t, prefer=self.title, exclude=exclude)
            if not found:
                raise KeyError(f"line {t!r} not found (from {self.title}, token {token!r})")
            sheet, row = found
            ax = ctx.sheet_axis(sheet)
        if fn:
            fyp = ax.by_id.get(p.pid)
            if fyp is None or fyp.kind != "FY":
                return None
            qs = ax.quarters_of(fyp.fy)
            if len(qs) == 0:
                return None
            prefix = "" if sheet == self.title else f"'{sheet}'!"
            if fn == "lastq":
                return f"{prefix}{qs[-1].letter}{row}"
            if fn == "firstq":
                return f"{prefix}{qs[0].letter}{row}"
            func = "SUM" if fn == "sumq" else "AVERAGE"
            return f"{func}({prefix}{qs[0].letter}{row}:{qs[-1].letter}{row})"
        q = self._shift(ax, p, off)
        if q is None:
            return None
        cell = f"${q.letter}${row}" if absolute else f"{q.letter}{row}"
        return cell if sheet == self.title else f"'{sheet}'!{cell}"

    def formula(self, dsl: str, p: Period, cur_line: Optional[str] = None) -> Optional[str]:
        """Expand a template into an Excel formula for period p; None if any token is unresolvable."""
        missing = False

        def sub(m):
            nonlocal missing
            r = self.ref(m.group(1), p, cur_line)
            if r is None:
                missing = True
                return "#MISSING"
            return r

        out = TOKEN_RE.sub(sub, dsl)
        if missing:
            return None
        if not out.startswith("="):
            out = "=" + out
        return out

    # ---- writing -------------------------------------------------------------------
    def _value_for(self, line: dict, p: Period):
        """Decide what goes in the cell of `line` for period p (number, formula or None)."""
        ax = self.axis
        lid = line["id"]
        kind = line.get("kind")
        needs = line.get("needs")
        if needs == "py" and ax.prior_year(p) is None:
            return None
        if needs == "pq" and ax.prior_period(p) is None:
            return None
        if needs == "py2":
            py = ax.prior_year(p)
            if py is None or ax.prior_year(py) is None:
                return None
        if line.get("q_only") and p.kind == "FY" and not (p.annual_only and line.get("annual_dsl")):
            return None
        start = line.get("start")
        if start and ax.by_id.get(start) and p.col < ax.by_id[start].col:
            return None

        # explicit per-period values override everything else (driver inputs, consensus rows,
        # per-period formula overrides); periods without an override fall through
        vals = line.get("values") or {}
        if p.pid in vals:
            v = vals[p.pid]
            if isinstance(v, str) and v.startswith("=") and "{" in v:
                return self.formula(v, p, lid)
            return v
        if line.get("values_only"):
            return None

        if kind == "sub":
            dsl = line["dsl"]
            if p.kind == "Q" and p.estimate and line.get("proj_dsl"):
                dsl = line["proj_dsl"]
            elif p.annual_only and line.get("annual_dsl"):
                dsl = line["annual_dsl"]
            elif needs in ("py", "pq", "py2"):
                # only where the parent has a value in this period and in the comparison period
                parent = self.ctx.line_defs.get((self.title, line["parent"]))
                if parent is not None:
                    saved = self._typed_input   # nested evaluations must not recolour this cell
                    other = ax.prior_year(p) if needs in ("py", "py2") else ax.prior_period(p)
                    blank = self._value_for(parent, p) is None or (other is not None and self._value_for(parent, other) is None)
                    if not blank and needs == "py2":
                        other2 = ax.prior_year(other) if other is not None else None
                        blank = other2 is not None and self._value_for(parent, other2) is None
                    self._typed_input = saved
                    if blank:
                        return None
            return self.formula(dsl, p, lid)

        if p.kind == "Q":
            if not p.estimate:
                return self._hist_value(line, p)
            dsl = line.get("proj_dsl") or line.get("dsl")
            return self.formula(dsl, p, lid) if dsl else None
        # FY columns
        if p.annual_only:
            dsl = line.get("annual_dsl") or line.get("proj_dsl") or line.get("dsl")
            if dsl:
                return self.formula(dsl, p, lid)
            hv = self._hist_value(line, p)
            return hv
        agg = line.get("fy_hist", line.get("fy")) if not p.estimate else line.get("fy")
        if agg == "blank":
            return None
        if agg == "formula":
            dsl = line.get("fy_dsl") or (line.get("dsl") if (not p.estimate or not line.get("proj_dsl")) else line.get("proj_dsl"))
            if not dsl:
                dsl = line.get("proj_dsl") or line.get("dsl")
            return self.formula(dsl, p, lid) if dsl else None
        qs = ax.quarters_of(p.fy)
        if not qs:
            return self._hist_value(line, p)
        if not p.estimate and isinstance(line.get("hist"), (str, dict)) and (line["hist"] if isinstance(line["hist"], dict) else {"kind": "data"}).get("kind", "data") == "data":
            # a historical year with no quarterly data stays blank instead of summing to zero
            saved = self._typed_input
            empty = all(self._hist_value(line, q) is None for q in qs)
            self._typed_input = saved
            if empty:
                return None
        r = line["row"]
        if agg == "sum":
            return f"=SUM({qs[0].letter}{r}:{qs[-1].letter}{r})"
        if agg == "avg":
            return f"=AVERAGE({qs[0].letter}{r}:{qs[-1].letter}{r})"
        if agg == "last":
            return f"={qs[-1].letter}{r}"
        if agg == "first":
            return f"={qs[0].letter}{r}"
        raise ValueError(f"unknown fy aggregation {agg!r} for {lid}")

    def _hist_value(self, line: dict, p: Period):
        h = line.get("hist")
        if h is None:
            dsl = line.get("dsl")
            return self.formula(dsl, p, line["id"]) if dsl else None
        if isinstance(h, str):
            h = {"kind": "data", "key": h}
        k = h.get("kind", "data")
        if k == "blank" or k == "none":
            return None
        if k == "formula":
            return self.formula(h["dsl"], p, line["id"])
        if k == "data":
            series = self.ctx.data.get(h.get("key", line["id"])) or {}
            v = series.get(p.pid)
            if v is None and p.kind == "FY":
                return None
            if isinstance(v, str) and v.startswith("="):
                if "{" in v:
                    return self.formula(v, p, line["id"])
                self._typed_input = True
                return v
            return v
        raise ValueError(f"unknown hist kind {k!r}")

    def flush(self):
        ws = self.ws
        for line in self.pending:
            r = line["row"]
            fmt = line.get("fmt") or KIND_FMT.get(line.get("kind"), "amount")
            if line.get("kind") == "sub":
                fmt = line.get("fmt") or "amount"
            S.style_cell(ws[f"B{r}"], line["label"], bold=line.get("bold", False), italic=line.get("italic", False),
                         color=S.BLACK, top=line.get("top", False), fill_rgb=line.get("fill"))
            # label indents as in the reference: variance rows one step in on the builds; on the
            # statements ordinary lines one step, their ratio rows two, totals none
            indent = line.get("indent")
            if indent is None:
                if line.get("kind") == "sub":
                    indent = 2 if self.fy_fill else 1
                elif self.fy_fill and not line.get("bold") and not line.get("top"):
                    indent = 1
                else:
                    indent = 0
            if indent:
                ws[f"B{r}"].alignment = Alignment(horizontal="left", indent=indent)
            if line.get("top") or line.get("bottom"):
                for c in range(2, self.last_col + 1):
                    ws.cell(row=r, column=c).border = S.border(top=bool(line.get("top")), bottom=bool(line.get("bottom")))
            for p in self.axis.periods:
                self._typed_input = False
                try:
                    v = self._value_for(line, p)
                except KeyError as e:
                    raise KeyError(f"{self.title} row {r} ({line['id']}): {e}") from e
                cell = ws[f"{p.letter}{r}"]
                if v is None:
                    cell.font = S.font(S.BLACK, line.get("bold", False), line.get("italic", False))
                    cell.number_format = S.NUMBER_FORMATS.get(fmt, fmt)
                    if line.get("fill"):
                        cell.fill = S.fill(line["fill"])
                    continue
                color = line.get("color")
                if color is None:
                    color = S.color_for(v)
                    if self._typed_input and color == S.BLACK:
                        color = S.BLUE        # a typed expression such as =9.3%-0.6% is an input
                    if color == S.BLUE and line.get("input_color"):
                        color = line["input_color"]
                fill_rgb = line.get("fill")
                if line.get("input_fill") and p.estimate and not isinstance(v, str):
                    fill_rgb = S.LIGHT_YELLOW
                S.style_cell(cell, v, fmt=fmt, bold=line.get("bold", False), italic=line.get("italic", False),
                             color=color, fill_rgb=fill_rgb, top=line.get("top", False))
                note = (line.get("notes") or {}).get(p.pid)
                if note:
                    self.ctx.notes.append((self.title, f"{p.letter}{r}", note))
            if line.get("label_note"):
                self.ctx.notes.append((self.title, f"B{r}", line["label_note"]))
        self.pending = []
        if self.fy_fill:
            for p in self.axis.fys():
                if p.annual_only:
                    continue
                for rr in range(7, self.row + 1):
                    c = ws[f"{p.letter}{rr}"]
                    if c.fill is None or c.fill.fill_type is None:
                        c.fill = S.fill(S.GREY_FY)

    # ---- block renderer ------------------------------------------------------------
    def blocks(self, blocks: List[dict]):
        """Render a list of layout blocks:
        {"section": title} {"band": title} {"subtitle": title} {"blank": n}
        {"label": text, "bold":.., "italic":..} {"line": {...line def...}}
        {"deltas": [...delta items...]}"""
        for b in blocks:
            if "section" in b:
                self.section(b["section"], marker=b.get("marker", True))
            elif "band" in b:
                self.band(b["band"], marker=b.get("marker", True))
            elif "subtitle" in b:
                self.subtitle(b["subtitle"], marker=b.get("marker", False))
            elif "blank" in b:
                self.blank(int(b["blank"] or 1))
            elif "label" in b:
                self.label_only(b["label"], bold=b.get("bold", False), italic=b.get("italic", False), fill_rgb=b.get("fill"))
            elif "line" in b:
                self.line(b["line"], with_subs=b.get("with_subs"))
                if b.get("gap", True):
                    self.blank()
            elif "deltas" in b:
                self.delta_block(b["deltas"])
            else:
                raise ValueError(f"unknown block {b!r}")

    # ---- delta blocks --------------------------------------------------------------
    def delta_block(self, items: List[dict]):
        """Rows comparing a model line (or its growth sub-row) with an external series.
        item = {label, source, line, sub (optional), values {pid: number}, measure}
        measure: 'growth' (sub-row vs series, bps), 'margin' (line vs series, bps),
        'level' (line vs series, % delta)."""
        for it in items:
            src = it.get("source", "Consensus")
            measure = it.get("measure", "growth")
            label = it["label"]
            if measure == "growth":
                ext_label = f"{src} {label} % YoY "
                fmt = "pct_cons"
            elif measure == "margin":
                ext_label = f"{src} {label} "
                fmt = "pct_cons"
            else:
                ext_label = f"{src} {label} "
                fmt = it.get("fmt", "amount")
            ext_id = f"ext.{src.lower()}.{it['line']}.{it.get('sub') or 'level'}"
            r_ext = self.line({"id": ext_id, "label": ext_label, "kind": "none", "fmt": fmt, "bold": True,
                               "values": it.get("values", {}), "fy": "blank"})
            ref = "{" + it["line"] + ("." + it["sub"] if it.get("sub") else "") + "}"
            if measure == "level":
                dsl = "=" + ref + "/{" + ext_id + "}-1"
                dlabel = f"∆ to {src} (%)"
                dfmt = "pct_cons"
            else:
                dsl = "=(" + ref + "-{" + ext_id + "})*10000"
                dlabel = f"∆ to {src} (bps)"
                dfmt = "bps_delta"
            # the delta exists only where the external value exists
            vals = {p.pid: dsl for p in self.axis.periods if it.get("values", {}).get(p.pid) is not None}
            self.line({"id": ext_id + ".delta", "label": dlabel, "kind": "none", "fmt": dfmt, "bold": True, "italic": True,
                       "fill": S.YELLOW, "fy": "formula", "bottom": True, "values": vals})
            self.blank()
