"""The inputs workbook: the analyst's UI for a model build.

Stage 1 (`write_stage1`): Setup, Data Files, Revenue Tree, Cost Tree, Drivers, Variance &
Deltas, Side Builds, Guidance, Buyside, KPI History, Statement Mapping. Pre-filled with
proposals from the parsed data; dropdowns for every choice.
Stage 2 (`write_stage2`): after the definitions are confirmed, adds Driver Grid (periods
across, cases down, one block per driver), Multiples and DCF Inputs tabs.
`read_inputs` turns the whole workbook back into the dict that spec_builder consumes;
cell notes on grid cells become notes on the model's driver cells.
"""
from __future__ import annotations

import datetime as dt
import re
from pathlib import Path
from typing import Dict, List, Optional

from openpyxl import Workbook, load_workbook
from openpyxl.comments import Comment
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

from . import canon
from .parse_data import _norm, series, series_pref
from .periods import PeriodAxis, parse_pid, pid_of

NAVY = "FF003765"
INPUT = "FFFFFFCC"
GREY = "FFF2F2F2"
HDR_FONT = Font(name="Arial", size=10, bold=True, color="FFFFFFFF")
FONT = Font(name="Arial", size=10)
BOLD = Font(name="Arial", size=10, bold=True)
HELP = Font(name="Arial", size=9, italic=True, color="FF595959")

SETUP_FIELDS = [  # key, label, default, help, dropdown options (or None)
    ("company_name", "Company name", "", "As it should appear in the model title, e.g. Illumina, Inc.", None),
    ("ticker", "Ticker", "", "Short ticker used in the title and file name", None),
    ("exchange", "Exchange", "", "NASDAQ / NYSE / LSE ... (shown in the title as EXCHANGE: TICKER)", None),
    ("ticker_code", "Price feed ticker code", "", "Bloomberg: 'ILMN US Equity'; CapIQ: 'ILMN'; FactSet: 'ILMN-US'", None),
    ("price_source", "Current price source", "Bloomberg", "Live formula in the Tearsheet; falls back to the typed price when the add-in is absent", ["Bloomberg", "CapIQ", "FactSet", "Hardcode"]),
    ("current_price", "Current price (fallback)", "", "Typed share price in the trading currency", None),
    ("price_date", "Price as-of date", "", "YYYY-MM-DD", None),
    ("reporting_currency", "Reporting currency", "USD", "Currency of the financial statements", ["USD", "EUR", "GBP", "CHF", "JPY", "CNY", "CAD", "AUD", "SEK", "DKK", "NOK", "HKD"]),
    ("trading_currency", "Trading currency", "USD", "Currency the shares trade in (price targets are in this currency)", ["USD", "EUR", "GBP", "CHF", "JPY", "CNY", "CAD", "AUD", "SEK", "DKK", "NOK", "HKD"]),
    ("fx_rate", "FX rate (reporting -> trading)", 1, "1.0 when both currencies are the same", None),
    ("units", "Units", "mm", "mm = millions", ["mm", "000s", "bn"]),
    ("fiscal_year_end_month", "Fiscal year end month", 12, "Detected from the data; 12 = December", None),
    ("first_hist_quarter", "History starts (quarter)", "", "e.g. 1Q23 (three full years before the first estimate is the default)", None),
    ("last_actual_quarter", "Last reported quarter", "", "Detected from the data, e.g. 2Q26", None),
    ("last_quarterly_estimate", "Last quarterly estimate", "", "e.g. 4Q28; later years are annual columns", None),
    ("annual_only_years", "Annual-only years", "", "e.g. 2029, 2030", None),
    ("annual_hist_years", "Annual history years (before the quarterly history)", "", "e.g. 2021, 2022, 2023, 2024: one annual column each, typed from the CapIQ annual statements (the Bloomberg annual printout fills lines CapIQ lacks); blank for none", None),
    ("case_set", "Cases", "Disaster/Bear/Base/Bull/Blowout", "Three or five cases", ["Bear/Base/Bull", "Disaster/Bear/Base/Bull/Blowout"]),
    ("comments_policy", "Cell comments", "From this workbook", "Notes you type on grid cells are copied to the model; or none at all", ["From this workbook", "I will add my own"]),
    ("author", "Author name (file properties and notes)", "", "Stamped as the workbook creator and the author of every note", None),
    ("cover_tab", "Cover tab name", "Cover", "Left blank for you to design", None),
    ("model_file", "Model file name", "", "Default: <TICKER>_model_<date>.xlsx in the models folder", None),
    ("valuation_metric", "Valuation metric", "EV/EBITDA", "Multiple used on the Tearsheet", ["EV/EBITDA", "EV/Adj. EBITDA", "P/E (Adj. EPS)", "P/E (GAAP EPS)", "EV/Sales", "EV/EBIT", "P/FCF"]),
    ("adjusted_block", "Non-GAAP reconciliation block", "Auto", "Auto = include when the company reports adjusted figures", ["Auto", "Yes", "No"]),
    ("incremental_blocks", "Incremental margin blocks on the Margin Build", "Y", "Y/N", ["Y", "N"]),
    ("sbc_split", "Split SBC by function on the Margin Build", "Auto", "Auto = when the data has SBC by line", ["Auto", "Yes", "No"]),
    ("adj_sbc_addback", "Add back SBC in the non-GAAP block", "Y", "Y = adjusted figures exclude SBC (most companies); N = the company keeps SBC in its non-GAAP results", ["Y", "N"]),
]

DRIVER_TYPES = ["yoy_pct", "qoq_pct", "net_adds", "bps_qoq", "bps_yoy", "pct_level", "pct_of_base", "gm_pct", "cost_per_unit", "absolute", "flat", "single", "custom"]
TREE_KINDS = ["sum", "volume_price", "growth", "share", "direct", "kpi", "custom"]
SECTIONS = ["Revenue", "Cost", "Income Statement", "Balance Sheet", "Cash Flow"]
NON_REVENUE = re.compile(r"adjusted|margin|eps|ebitda|income|cash|capex|capital expenditure|debt|shares|dividend|tax|gross profit|opex|expense", re.I)
FORMATS = ["%", "bps", "amount", "price", "shares", "x"]
FY_RULES = ["sum", "avg", "last", "first", "formula"]
DATA_TYPES = ["Bloomberg consensus", "CapIQ Income Statement", "CapIQ Balance Sheet", "CapIQ Cash Flow", "CapIQ Key Stats", "KPI history", "Guidance", "Buyside", "Other"]
MEASURES = ["growth", "margin", "level"]
SOURCES = ["Consensus", "Guidance", "Buyside"]


# ----------------------------------------------------------------------------- styling helpers
def _sheet(wb: Workbook, title: str, headers: List[str], widths: List[float], help_text: str, start_row: int = 3):
    ws = wb.create_sheet(title)
    ws.sheet_view.showGridLines = False
    ws["A1"].value = help_text
    ws["A1"].font = HELP
    ws["A1"].alignment = Alignment(wrap_text=False)
    for i, h in enumerate(headers, 1):
        c = ws.cell(row=start_row, column=i, value=h)
        c.font = HDR_FONT
        c.fill = PatternFill("solid", fgColor=NAVY)
        ws.column_dimensions[get_column_letter(i)].width = widths[i - 1] if i - 1 < len(widths) else 14
    ws.freeze_panes = ws.cell(row=start_row + 1, column=1)
    return ws


def _dv(ws, options: List[str], cell_range: str):
    dv = DataValidation(type="list", formula1='"' + ",".join(options) + '"', allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(cell_range)


def _write_rows(ws, rows: List[List], start_row: int, input_cols: Optional[List[int]] = None):
    for r_i, row in enumerate(rows):
        for c_i, v in enumerate(row, 1):
            c = ws.cell(row=start_row + r_i, column=c_i, value=v)
            c.font = FONT
            if input_cols and c_i in input_cols:
                c.fill = PatternFill("solid", fgColor=INPUT)


# ----------------------------------------------------------------------------- proposals
def propose_inputs(data: dict, overrides: Optional[dict] = None, files: Optional[List[dict]] = None) -> dict:
    ov = overrides or {}
    tick = (data.get("ticker") or "").split()
    last_actual = data.get("last_actual_quarter")
    last_est = data.get("last_estimate_quarter")
    first_q = data.get("first_quarter")
    if last_actual:
        _, y, q = parse_pid(last_actual)
        default_first = pid_of("Q", y - 3, 1)
        # history: three full years, but not earlier than the data (always from a first quarter)
        if first_q and parse_pid(first_q)[1] > y - 3:
            default_first = pid_of("Q", parse_pid(first_q)[1], 1)
        if not last_est:
            # exports with actuals only (CapIQ): two full estimate years by default
            last_est = pid_of("Q", y + 2, 4)
    else:
        default_first = first_q
    est_year = parse_pid(last_est)[1] if last_est else None
    setup = {k: d for k, _, d, _, _ in SETUP_FIELDS}
    setup.update({"ticker": tick[0] if tick else "", "ticker_code": data.get("ticker") or "", "reporting_currency": data.get("currency") or "USD",
                  "trading_currency": data.get("currency") or "USD", "fiscal_year_end_month": data.get("fy_end_month") or 12,
                  "first_hist_quarter": default_first or "", "last_actual_quarter": last_actual or "", "last_quarterly_estimate": last_est or "",
                  "annual_only_years": f"{est_year + 1}, {est_year + 2}" if est_year else ""})
    capiq_fy = sorted({int(pid[2:]) for l in data["lines"] if l.get("source") == "capiq" and (l.get("section") or "").lower().startswith("income statement")
                       and _norm(l["label"]) in ("total revenue", "revenue", "revenues", "net sales")
                       for pid, v in l["values"].items() if pid.startswith("FY") and v is not None and not (l.get("est") or {}).get(pid)})
    if capiq_fy and default_first:
        y0 = parse_pid(default_first)[1]
        setup["annual_hist_years"] = ", ".join(str(y) for y in [y for y in capiq_fy if y < y0][-5:])
    setup.update({k: v for k, v in ov.items() if v is not None})
    # revenue tree: segment lines first, business-breakdown lines as candidates
    # Bloomberg's "Segment Revenue" page runs on into highlight items (adjusted income, cash); keep revenue lines only
    seg = [l for l in data["lines"] if (l.get("section") or "").lower().startswith("segment revenue") and not l["pct"] and not NON_REVENUE.search(l["label"])]
    seen, tree = set(), []
    for l in seg:
        if l["label"] in seen:
            continue
        seen.add(l["label"])
        al, asec = _annual_match(data, l["label"])
        tree.append({"id": _slug(l["label"]), "label": l["label"], "parent": "", "kind": "growth", "data_label": l["label"], "data_section": l.get("section") or "",
                     "annual_data_label": al, "annual_data_section": asec})
    candidates = []
    for l in data["lines"]:
        sec = (l.get("section") or "").lower()
        if sec.startswith("business breakdown") and not l["pct"] and l["label"] not in seen and l["label"] not in candidates and not NON_REVENUE.search(l["label"]):
            candidates.append(l["label"])
    # cost tree (data sections come from the matched line, whatever the export's naming)
    cost = []
    cogs_label, cogs_sec = _first_label_section(data, ["Cost of Revenue", "Cost of Goods Sold", "Cost of Sales"], prefer_section="GAAP Results")
    al, asec = _annual_match(data, cogs_label or "Cost of Revenue")
    cost.append({"id": "cogs_total", "label": "Cost of Revenue", "section": "COGS", "segment": "", "data_label": cogs_label or "Cost of Revenue", "data_section": cogs_sec or "",
                 "annual_data_label": al, "annual_data_section": asec})
    for lab, lid in (("Selling, General & Administrative", "sga"), ("Research & Development", "rd"), ("Sales & Marketing", "sm"), ("General & Administrative", "ga"), ("Other Operating Expenses", "other_opex_line")):
        hit, sec = _first_label_section(data, [lab], prefer_section="GAAP Results")
        if hit:
            al, asec = _annual_match(data, hit)
            cost.append({"id": lid, "label": lab, "section": "Opex", "segment": "", "data_label": hit, "data_section": sec or "", "sbc_data_label": "",
                         "annual_data_label": al, "annual_data_section": asec})
    # drivers
    drivers = []
    for n in tree:
        drivers.append({"id": n["id"] + "_g", "label": f"{n['label']} Growth y/y", "section": "Revenue", "target": n["id"], "type": "yoy_pct", "cased": "Y", "format": "%",
                        "represented": f"% yoy row under {n['label']}; level = prior year x (1 + growth)", "fy": "", "target_sub": "pct_yoy"})
    for c in cost:
        if c["section"] == "COGS":
            drivers.append({"id": "gm_pct", "label": "Gross Margin %", "section": "Cost", "target": c["id"], "type": "gm_pct", "cased": "Y", "format": "%",
                            "represented": "COGS = revenue x (1 - GM%)", "fy": "", "target_sub": None})
        else:
            drivers.append({"id": c["id"] + "_pct", "label": f"{c['label']} % of Revenue", "section": "Cost", "target": c["id"], "type": "pct_of_base", "cased": "Y", "format": "%",
                            "represented": f"{c['label']} = revenue x %", "fy": "", "target_sub": "pct_of"})
    for did, label, section, fmt, fy, tgt in canon.DEFAULT_DRIVERS:
        drivers.append({"id": did, "label": label, "section": {"is": "Income Statement", "bs": "Balance Sheet", "cf": "Cash Flow"}[section], "target": tgt[0] if tgt else "",
                        "type": "absolute" if fmt != "pct_s" else "pct_level", "cased": "N", "format": {"amount_s": "amount", "pct_s": "%", "shares": "shares"}[fmt],
                        "represented": "", "fy": fy, "target_sub": tgt[1] if tgt else None})
    # deltas: consensus on the headline lines
    deltas = [{"sheet": "Revenue Build", "line": "total_rev", "label": "Total Revenue", "measure": "growth", "source": "Consensus", "data_label": _first_label(data, ["Revenue", "Total Revenue"]) or "Revenue", "data_section": "Highlights"}]
    for n in tree:
        deltas.append({"sheet": "Revenue Build", "line": n["id"], "label": n["label"], "measure": "growth", "source": "Consensus", "data_label": n["data_label"], "data_section": n["data_section"]})
    for lab, line, sheet, measure in (("Gross Margin (%)", "total_gp", "Margin Build", "margin"), ("Adjusted Operating Margin (%)", "op_inc", "Margin Build", "margin")):
        if _first_label(data, [lab]):
            deltas.append({"sheet": sheet, "line": line, "label": lab.replace(" (%)", " %"), "measure": measure, "source": "Consensus", "data_label": lab, "data_section": ""})
    mapping = []
    for lid, label, syns, _ in canon.IS_LINES:
        # D&A and SBC are memo lines read from the cash flow or adjustments blocks, as build_spec does
        hit, sec = _map_hit(data, syns, "memo" if lid in ("dep", "amort", "da", "sbc") else "is")
        al, asec = _annual_match(data, hit, syns, "memo" if lid in ("dep", "amort", "da", "sbc") else "is")
        mapping.append({"id": lid, "label": label, "statement": "Income Statement", "data_label": hit or "", "data_section": sec, "keep": "Y" if hit else "N",
                        "annual_data_label": al, "annual_data_section": asec})
    for lid, label, syns, grp, role in canon.BS_LINES:
        if role == "plug":
            continue
        hit, sec = _map_hit(data, syns, "bs")
        al, asec = _annual_match(data, hit, syns, "bs")
        mapping.append({"id": lid, "label": label, "statement": "Balance Sheet", "data_label": hit or "", "data_section": sec, "keep": "Y" if hit else "N",
                        "annual_data_label": al, "annual_data_section": asec})
    for lid, label, syns, grp, role in canon.CFS_LINES:
        if role == "plug":
            continue
        hit, sec = _map_hit(data, syns, "cf")
        al, asec = _annual_match(data, hit, syns, "cf")
        mapping.append({"id": lid, "label": label, "statement": "Cash Flow", "data_label": hit or "", "data_section": sec, "keep": "Y" if hit else "N",
                        "annual_data_label": al, "annual_data_section": asec})
    return {"setup": setup, "files": files or [], "revenue_tree": tree, "revenue_candidates": candidates, "cost_tree": cost, "drivers": drivers,
            "variance": [], "deltas": deltas, "side_builds": [], "guidance": [], "buyside": [], "kpi_history": {}, "mapping": mapping}


def _slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")


def _first_label(data: dict, syns: List[str], section: Optional[str] = None) -> Optional[str]:
    for s in syns:
        if series(data, s, section):
            return s
    return None


def _annual_match(data: dict, label: Optional[str], syns: Optional[List[str]] = None, stmt: str = "is"):
    """(label, section) of the line in the CapIQ export that holds the annual history of a
    quarterly label: the label itself and its synonyms, looked up in the statement's preferred
    sections first and never in the sections it excludes (same rule as DataView.annual_series)."""
    cands = []
    for s in ([label] if label else []) + list(syns or []) + (canon.synonyms_of(label) if label else []):
        if s and s not in cands:
            cands.append(s)
    prefs, excl = canon.PREFER_SECTIONS.get(stmt, []), canon.EXCLUDE_SECTIONS.get(stmt, [])
    secs = []
    for l in data["lines"]:
        if l.get("source") == "capiq" and l.get("section") and l["section"] not in secs:
            secs.append(l["section"])

    def ok(s):
        return bool(s) and any(pid.startswith("FY") for pid in s)

    for pref in prefs:
        for sec in secs:
            if _norm(sec).startswith(_norm(pref)):
                for lab in cands:
                    if ok(series(data, lab, sec, None, source="capiq")):
                        return lab, sec
    for lab in cands:
        if ok(series(data, lab, None, excl, source="capiq")):
            key = _norm(lab)
            sec = next((l.get("section") or "" for l in data["lines"] if l.get("source") == "capiq" and _norm(l["label"]) == key and l["values"]
                        and not any(_norm(l.get("section") or "").startswith(_norm(e)) for e in excl)), "")
            return lab, sec
    return "", ""


def _map_hit(data: dict, syns: List[str], stmt: str):
    """(label, section) for a statement line: the first synonym found, read from the statement's
    preferred sections first so the proposal names the section the spec will use."""
    prefs, excl = canon.PREFER_SECTIONS.get(stmt, []), canon.EXCLUDE_SECTIONS.get(stmt, [])
    for s in syns:
        vals, sec = series_pref(data, s, prefs, excl)
        if vals:
            return s, (sec or "")
    return None, ""


def _first_label_section(data: dict, syns: List[str], prefer_section: Optional[str] = None):
    """(label, section) of the first line matching one of the synonyms; a preferred section wins."""
    for s in syns:
        if prefer_section and series(data, s, prefer_section):
            return s, prefer_section
    for s in syns:
        key = _norm(s)
        for l in data["lines"]:
            if _norm(l["label"]) == key and l["values"]:
                return s, (l.get("section") or "")
    return None, None


# ----------------------------------------------------------------------------- stage 1
def write_stage1(inputs: dict, path: str):
    wb = Workbook()
    wb.remove(wb.active)
    # Setup
    ws = _sheet(wb, "Setup", ["Key", "Field", "Value", "Help"], [26, 44, 30, 90], "Fill the yellow cells. Dropdown cells offer the allowed choices.")
    r = 4
    for key, label, default, help_text, options in SETUP_FIELDS:
        val = inputs.get("setup", {}).get(key, default)
        _write_rows(ws, [[key, label, val, help_text]], r, input_cols=[3])
        if options:
            _dv(ws, options, f"C{r}")
        r += 1
    ws.column_dimensions["A"].hidden = True
    # Data files
    ws = _sheet(wb, "Data Files", ["Path", "Type", "Notes"], [90, 26, 50], "Files found in the working folder; add paths of Bloomberg and CapIQ exports (xlsx, csv or md).")
    rows = [[f.get("path", ""), f.get("type", ""), f.get("notes", "")] for f in inputs.get("files", [])] or [["", "", ""]] * 5
    _write_rows(ws, rows, 4, input_cols=[1, 2, 3])
    _dv(ws, DATA_TYPES, f"B4:B{3 + max(len(rows), 30)}")
    # Revenue tree
    ws = _sheet(wb, "Revenue Tree", ["ID", "Label", "Parent ID", "Kind", "Volume line ID", "Price line ID", "Price basis", "Data label (history)", "Data section", "Format (KPI)", "FY rule (KPI)", "History formula", "Notes", "Annual data label", "Annual data section"],
                [18, 36, 16, 14, 16, 16, 12, 34, 24, 12, 12, 40, 40, 30, 30],
                "One row per revenue line or KPI. Kind: sum (children add up), volume_price (volume x price), growth (y/y driver), share (% of parent), direct, kpi (a volume/price/mix line), custom.")
    rows = [[n.get("id", ""), n.get("label", ""), n.get("parent", ""), n.get("kind", ""), n.get("volume_id", ""), n.get("price_id", ""), n.get("price_basis", ""), n.get("data_label", ""), n.get("data_section", ""), n.get("format", ""), n.get("fy_rule", ""), n.get("hist_formula", ""), n.get("notes", ""), n.get("annual_data_label", ""), n.get("annual_data_section", "")]
            for n in inputs.get("revenue_tree", [])]
    rows += [[""] * 15] * 20
    _write_rows(ws, rows, 4, input_cols=list(range(1, 16)))
    n = 3 + len(rows)
    _dv(ws, TREE_KINDS, f"D4:D{n}"); _dv(ws, ["per month", "per period"], f"G4:G{n}"); _dv(ws, ["count", "price", "pct", "amount"], f"J4:J{n}"); _dv(ws, FY_RULES, f"K4:K{n}")
    if inputs.get("revenue_candidates"):
        ws.cell(row=n + 2, column=1, value="Other revenue lines in the data (candidates):").font = BOLD
        for i, c in enumerate(inputs["revenue_candidates"]):
            ws.cell(row=n + 3 + i, column=1, value=c).font = HELP
    # Cost tree
    ws = _sheet(wb, "Cost Tree", ["ID", "Label", "Section", "Segment (revenue line ID)", "Data label (history)", "Data section", "SBC data label", "Volume line ID", "Notes", "Annual data label", "Annual data section"],
                [18, 36, 12, 24, 34, 24, 24, 16, 40, 30, 30], "COGS lines (one per segment or a single total) and operating expense lines. The driver for each line is defined on the Drivers tab.")
    rows = [[c.get("id", ""), c.get("label", ""), c.get("section", ""), c.get("segment", ""), c.get("data_label", ""), c.get("data_section", ""), c.get("sbc_data_label", ""), c.get("volume_id", ""), c.get("notes", ""), c.get("annual_data_label", ""), c.get("annual_data_section", "")]
            for c in inputs.get("cost_tree", [])] + [[""] * 11] * 15
    _write_rows(ws, rows, 4, input_cols=list(range(1, 12)))
    _dv(ws, ["COGS", "Opex", "Other"], f"C4:C{3 + len(rows)}")
    # Drivers
    ws = _sheet(wb, "Drivers", ["ID", "Label (as shown on Drivers & Casing)", "Section", "Target line ID", "Type", "Cased (Y/N)", "Format", "Represented on the build as", "FY aggregation", "Notes"],
                [18, 44, 18, 20, 14, 12, 10, 60, 14, 40],
                "One row per driver. Type decides the formula (see the skill's model-logic reference); 'Represented on the build as' is your description or an explicit formula for custom types. Keep adding rows until every driver is listed.")
    rows = [[d.get("id", ""), d.get("label", ""), d.get("section", ""), d.get("target", ""), d.get("type", ""), d.get("cased", "Y"), d.get("format", "%"), d.get("represented", ""), d.get("fy", ""), d.get("notes", "")]
            for d in inputs.get("drivers", [])] + [[""] * 10] * 25
    _write_rows(ws, rows, 4, input_cols=list(range(1, 11)))
    n = 3 + len(rows)
    _dv(ws, SECTIONS, f"C4:C{n}"); _dv(ws, DRIVER_TYPES, f"E4:E{n}"); _dv(ws, ["Y", "N"], f"F4:F{n}"); _dv(ws, FORMATS, f"G4:G{n}"); _dv(ws, FY_RULES, f"I4:I{n}")
    # Variance & deltas
    ws = _sheet(wb, "Variance & Deltas", ["Line ID", "% yoy", "% 2y stack", "$ yoy", "% qoq", "$ qoq", "% total", "Start period"], [20, 8, 10, 8, 8, 8, 8, 12],
                "Variance rows: leave empty for the default set on every line; list a line to choose its rows (Y/N). Delta rows start further down.")
    rows = [[v.get("id", ""), v.get("pct_yoy", ""), v.get("pct_2y", ""), v.get("usd_yoy", ""), v.get("pct_qoq", ""), v.get("usd_qoq", ""), v.get("pct_total", ""), v.get("start", "")] for v in inputs.get("variance", [])] + [[""] * 8] * 12
    _write_rows(ws, rows, 4, input_cols=list(range(1, 9)))
    d0 = 4 + len(rows) + 2
    ws.cell(row=d0 - 1, column=1, value="DELTA ROWS (consensus / management guidance / buyside), written at the bottom of the builds").font = BOLD
    for i, h in enumerate(["Sheet", "Line ID", "Label", "Measure", "Source", "Data label", "Data section", "From period", "To period"], 1):
        c = ws.cell(row=d0, column=i, value=h); c.font = HDR_FONT; c.fill = PatternFill("solid", fgColor=NAVY)
    rows = [[d.get("sheet", ""), d.get("line", ""), d.get("label", ""), d.get("measure", ""), d.get("source", ""), d.get("data_label", ""), d.get("data_section", ""), d.get("from", ""), d.get("to", "")] for d in inputs.get("deltas", [])] + [[""] * 9] * 15
    _write_rows(ws, rows, d0 + 1, input_cols=list(range(1, 10)))
    _dv(ws, ["Revenue Build", "Margin Build", "Income Statement"], f"A{d0 + 1}:A{d0 + len(rows)}"); _dv(ws, MEASURES, f"D{d0 + 1}:D{d0 + len(rows)}"); _dv(ws, SOURCES, f"E{d0 + 1}:E{d0 + len(rows)}")
    ws["J1"].value = f"deltas_start={d0}"
    ws["J1"].font = HELP
    # Side builds
    ws = _sheet(wb, "Side Builds", ["Name (tab)", "Linked driver ID", "Describe the build and its layout"], [26, 20, 120], "One row per side-build tab. The Base case of the linked driver will link to the tab's output cells.")
    _write_rows(ws, [[s.get("name", ""), s.get("driver", ""), s.get("description", "")] for s in inputs.get("side_builds", [])] + [[""] * 3] * 8, 4, input_cols=[1, 2, 3])
    for r_i in range(4, 12):
        ws.cell(row=r_i, column=3).alignment = Alignment(wrap_text=True, vertical="top")
    # Guidance / buyside
    ws = _sheet(wb, "Guidance", ["Line ID", "Measure", "Period", "Low", "High", "Mid", "Source / date"], [20, 10, 10, 10, 10, 10, 40], "Management guidance by metric and period. Mid is computed. Used for the 'delta to guide' rows when a delta row names source = Guidance.")
    rows = [[g.get("line", ""), g.get("measure", ""), g.get("period", ""), g.get("low", ""), g.get("high", ""), None, g.get("source", "")] for g in inputs.get("guidance", [])] + [[""] * 7] * 15
    _write_rows(ws, rows, 4, input_cols=[1, 2, 3, 4, 5, 7])
    for i in range(len(rows)):
        ws.cell(row=4 + i, column=6, value=f'=IF(AND(D{4 + i}<>"",E{4 + i}<>""),AVERAGE(D{4 + i}:E{4 + i}),"")').font = FONT
    _dv(ws, MEASURES, f"B4:B{3 + len(rows)}")
    ws = _sheet(wb, "Buyside", ["Line ID", "Measure", "Period", "Value", "Source"], [20, 10, 10, 12, 40], "Buyside numbers (typed from a screenshot) for 'delta to buyside' rows.")
    _write_rows(ws, [[b.get("line", ""), b.get("measure", ""), b.get("period", ""), b.get("value", ""), b.get("source", "")] for b in inputs.get("buyside", [])] + [[""] * 5] * 15, 4, input_cols=[1, 2, 3, 4, 5])
    _dv(ws, MEASURES, "B4:B30")
    # KPI history
    kpi = inputs.get("kpi_history") or {}
    pids = sorted({p for vals in kpi.values() for p in vals}, key=lambda s: (parse_pid(s)[1], parse_pid(s)[2]) if parse_pid(s) else (0, 0))
    heads = pids + [""] * max(0, 20 - len(pids))
    ws = _sheet(wb, "KPI History", ["Data label"] + heads, [34] + [11] * len(heads), "Historical KPIs that are not in the data files: one row per KPI, quarters across (headers like 1Q23). Reference the label from the Revenue Tree's 'Data label' column.")
    r = 4
    for k, vals in kpi.items():
        ws.cell(row=r, column=1, value=k).font = FONT
        for i, p in enumerate(pids):
            if p in vals:
                c = ws.cell(row=r, column=2 + i, value=vals[p]); c.font = FONT; c.fill = PatternFill("solid", fgColor=INPUT)
        r += 1
    # Statement mapping
    ws = _sheet(wb, "Statement Mapping", ["Model line ID", "Model label", "Statement", "Data label", "Data section", "Keep (Y/N)", "Annual data label", "Annual data section"], [20, 40, 18, 40, 28, 10, 34, 34],
                "How the condensed statements map to the data. Change a data label or set Keep = N to drop a line; lines without data are dropped anyway. "
                "Annual data label/section: the CapIQ line that types the annual history columns (blank = same label or a synonym in the CapIQ export).")
    rows = [[m.get("id", ""), m.get("label", ""), m.get("statement", ""), m.get("data_label", ""), m.get("data_section", ""), m.get("keep", ""), m.get("annual_data_label", ""), m.get("annual_data_section", "")]
            for m in inputs.get("mapping", [])]
    _write_rows(ws, rows, 4, input_cols=[4, 5, 6, 7, 8])
    _dv(ws, ["Y", "N"], f"F4:F{3 + len(rows)}")
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    wb.save(path)
    return path


# ----------------------------------------------------------------------------- stage 2
def write_stage2(path: str, inputs: dict, axis: PeriodAxis, hist_values: Optional[Dict[str, Dict[str, float]]] = None,
                 blocks: Optional[List[dict]] = None):
    """Add Driver Grid, Multiples and DCF Inputs tabs to the stage-1 workbook. Existing
    estimates, notes, multiples, weights and DCF inputs survive a re-run (a driver added or
    the horizon extended keeps everything already typed)."""
    prior = {}
    try:
        prior = read_inputs(path)
    except Exception:
        prior = {}
    wb = load_workbook(path)
    for name in ("Driver Grid", "Multiples", "DCF Inputs"):
        if name in wb.sheetnames:
            wb.remove(wb[name])
    cases = ["Bear", "Base", "Bull"] if str(inputs["setup"].get("case_set", "")).startswith("Bear") else ["Disaster", "Bear", "Base", "Bull", "Blowout"]
    hist = [p for p in axis.actual_quarters()][-4:]
    est = [p for p in axis.periods if p.estimate and (p.kind == "Q" or p.annual_only)]
    headers = ["Driver ID", "Case"] + [p.label for p in hist] + [p.label for p in est] + ["Comment"]
    ws = _sheet(wb, "Driver Grid", headers, [22, 12] + [11] * (len(hist) + len(est)) + [40],
                "Type your estimates in the yellow cells (numbers or formulas; a note on a cell is copied to the model). Grey columns show the realised history. "
                "Percent inputs as decimals (0.05 = 5%) or with the % sign. Annual-only columns (FY2029E, FY2030E ...) take full-year amounts for flows "
                "(D&A, SBC, capex, buybacks) and year-end levels for rates; leave them empty to carry the prior year forward.")
    ws.freeze_panes = "C4"
    r = 4
    fmt_map = {"%": "0.0%", "bps": '0"bps"', "amount": "#,##0.0", "price": "0.00", "shares": "#,##0.00", "x": "0.0x"}
    for d in inputs.get("drivers", []):
        if not d.get("id"):
            continue
        ws.cell(row=r, column=1, value=d["id"]).font = BOLD
        ws.cell(row=r, column=2, value=d.get("label", "")).font = BOLD
        r += 1
        rows_for = cases if str(d.get("cased", "Y")).upper().startswith("Y") else ["Active"]
        if str(d.get("type", "")).lower() == "single":
            rows_for = cases
        for case in rows_for:
            ws.cell(row=r, column=1, value=d["id"]).font = FONT
            ws.cell(row=r, column=2, value=case).font = FONT
            col = 3
            hv = (hist_values or {}).get(d["id"], {})
            for p in hist:
                c = ws.cell(row=r, column=col, value=hv.get(p.pid))
                c.font = Font(name="Arial", size=10, color="FF808080")
                c.fill = PatternFill("solid", fgColor=GREY)
                c.number_format = fmt_map.get(d.get("format", "%"), "General")
                col += 1
            pg = ((prior.get("driver_grid") or {}).get(d["id"]) or {}).get(case) or {}
            pn = ((prior.get("driver_grid_notes") or {}).get(d["id"]) or {}).get(case) or {}
            for p in est:
                c = ws.cell(row=r, column=col)
                c.fill = PatternFill("solid", fgColor=INPUT)
                c.number_format = fmt_map.get(d.get("format", "%"), "General")
                c.font = FONT
                if str(d.get("type", "")).lower() == "single" and p is not est[0]:
                    c.fill = PatternFill("solid", fgColor=GREY)
                if p.pid in pg:
                    c.value = pg[p.pid]
                if p.pid in pn:
                    c.comment = Comment(pn[p.pid], inputs["setup"].get("author") or "Analyst")
                col += 1
            cc = ws.cell(row=r, column=col)
            cc.fill = PatternFill("solid", fgColor=INPUT)
            if pn.get("_row"):
                cc.value = pn["_row"]
            r += 1
        r += 1
    # Multiples
    ws = _sheet(wb, "Multiples", ["Case"] + ["Block 1", "Block 2"] + ["Comment"], [14, 14, 14, 50],
                "Target blocks (right): label, basis (NTM or YE), target date, the fiscal period of the metric the multiple applies to. Then one multiple per case and block.")
    r = 4
    pts = prior.get("tearsheet") or {}
    prior_blocks = pts.get("blocks") or []
    for case in cases:
        ws.cell(row=r, column=1, value=case).font = FONT
        for j, c in enumerate((2, 3)):
            cell = ws.cell(row=r, column=c)
            cell.fill = PatternFill("solid", fgColor=INPUT)
            cell.number_format = "0.0x"
            if j < len(prior_blocks):
                v = (pts.get("multiples") or {}).get(case, {}).get(prior_blocks[j]["label"])
                if v is not None:
                    cell.value = v
                note = (pts.get("multiple_notes") or {}).get(case, {}).get(prior_blocks[j]["label"])
                if note:
                    cell.comment = Comment(note, inputs["setup"].get("author") or "Analyst")
        ws.cell(row=r, column=4).fill = PatternFill("solid", fgColor=INPUT)
        r += 1
    r += 1
    ws.cell(row=r, column=1, value="Weights (blended price target)").font = BOLD
    r += 1
    wdef = {"Blowout": 0.1, "Bull": 0.2, "Base": 0.4, "Bear": 0.2, "Disaster": 0.1} if len(cases) == 5 else {"Bull": 0.25, "Base": 0.5, "Bear": 0.25}
    wdef.update(pts.get("weights") or {})
    for case in cases:
        ws.cell(row=r, column=1, value=case).font = FONT
        c = ws.cell(row=r, column=2, value=wdef.get(case)); c.fill = PatternFill("solid", fgColor=INPUT); c.number_format = "0%"
        r += 1
    r += 1
    ws.cell(row=r, column=1, value="Current implied multiple on (metric period)").font = BOLD
    c = ws.cell(row=r, column=2, value=_next_fy(axis)); c.fill = PatternFill("solid", fgColor=INPUT)
    # block table
    for i, h in enumerate(["Block", "Label", "Basis", "Target date", "Metric period", "Blended label"], 1):
        cc = ws.cell(row=3, column=6 + i, value=h); cc.font = HDR_FONT; cc.fill = PatternFill("solid", fgColor=NAVY)
    la = axis.last_actual_quarter()
    for i in range(2):
        yr = la.fy + 1 + i
        fy_end = axis.by_id.get(f"FY{yr}")
        end_s = fy_end.end.isoformat() if fy_end and fy_end.end else f"{yr}-12-31"
        vals = [f"Block {i + 1}", f"YE{yr}", "YE", end_s, f"FY{yr + 1}", "Near Term Setup" if i == 0 else ""]
        if i < len(prior_blocks):
            pb = prior_blocks[i]
            vals = [f"Block {i + 1}", pb.get("label") or vals[1], pb.get("basis") or "YE", pb.get("target_date") or end_s, pb.get("metric_period") or vals[4], pb.get("blended_label") or ""]
        for j, v in enumerate(vals, 1):
            c = ws.cell(row=4 + i, column=6 + j, value=v); c.font = FONT
            if j > 1:
                c.fill = PatternFill("solid", fgColor=INPUT)
    _dv(ws, ["NTM", "YE"], "I4:I5")
    for col in "GHIJKL":
        ws.column_dimensions[col].width = 16
    # DCF inputs
    ws = _sheet(wb, "DCF Inputs", ["Key", "Input", "Value", "Comment"], [18, 40, 16, 50], "Discount-rate and bridge inputs for the DCF tab. Exit multiples by case below.")
    pdcf = prior.get("dcf") or {}
    pnotes = pdcf.get("notes") or {}
    r = 4
    for key, label, default in (("valuation_date", "Valuation date (YYYY-MM-DD)", dt.date.today().isoformat()), ("tax_rate", "Tax rate (DCF)", ""), ("rfr", "Risk-free rate", ""),
                                ("beta", "Beta", ""), ("erp", "Equity risk premium", ""), ("kd_after_tax", "After-tax cost of debt", ""), ("equity_weight", "Equity weight", ""),
                                ("diluted_shares", "Diluted shares (mm)", ""), ("cash_lines", "Balance sheet lines counted as cash (IDs, comma-separated)", ", ".join((blocks or {}).get("cash_lines", []) if isinstance(blocks, dict) else [])),
                                ("debt_lines", "Balance sheet lines counted as debt/leases (IDs)", ", ".join((blocks or {}).get("debt_lines", []) if isinstance(blocks, dict) else []))):
        ws.cell(row=r, column=1, value=key).font = HELP
        ws.cell(row=r, column=2, value=label).font = FONT
        val = pdcf.get(key)
        if isinstance(val, list):
            val = ", ".join(val)
        c = ws.cell(row=r, column=3, value=val if val not in (None, "") else default); c.fill = PatternFill("solid", fgColor=INPUT); c.font = FONT
        cc = ws.cell(row=r, column=4); cc.fill = PatternFill("solid", fgColor=INPUT)
        if pnotes.get(key):
            cc.value = pnotes[key]
        r += 1
    r += 1
    ws.cell(row=r, column=2, value="Exit EV/EBITDA multiple by case").font = BOLD
    r += 1
    for case in cases:
        ws.cell(row=r, column=1, value="exit_" + case.lower()).font = HELP
        ws.cell(row=r, column=2, value=case).font = FONT
        c = ws.cell(row=r, column=3); c.fill = PatternFill("solid", fgColor=INPUT); c.number_format = "0.0x"
        pv = (pdcf.get("exit_multiples") or {}).get(case)
        if pv is not None:
            c.value = pv
        cc = ws.cell(row=r, column=4); cc.fill = PatternFill("solid", fgColor=INPUT)
        pn = (pnotes.get("exit_multiples") or {}).get(case)
        if pn:
            cc.value = pn
        r += 1
    wb.save(path)
    return path


def _next_fy(axis: PeriodAxis) -> str:
    la = axis.last_actual_quarter()
    return f"FY{la.fy + 1}"


# ----------------------------------------------------------------------------- read back
def _rows(ws, start_row: int = 4, ncols: Optional[int] = None) -> List[List]:
    out = []
    for row in ws.iter_rows(min_row=start_row, values_only=False):
        vals = [c.value for c in row[:ncols]] if ncols else [c.value for c in row]
        if ncols and len(vals) < ncols:
            vals += [None] * (ncols - len(vals))
        if all(v is None or str(v).strip() == "" for v in vals):
            continue
        out.append(vals)
    return out


def _s(v) -> str:
    return "" if v is None else str(v).strip()


def read_inputs(path: str) -> dict:
    wb = load_workbook(path)
    out: dict = {}
    ws = wb["Setup"]
    setup = {}
    for r in range(4, ws.max_row + 1):
        key = _s(ws.cell(row=r, column=1).value)
        if key:
            setup[key] = ws.cell(row=r, column=3).value
    out["setup"] = {k: ((v.date().isoformat() if isinstance(v, dt.datetime) else v.isoformat()) if isinstance(v, (dt.date, dt.datetime)) else v) for k, v in setup.items()}
    if "Data Files" in wb.sheetnames:
        out["files"] = [{"path": _s(r[0]), "type": _s(r[1]), "notes": _s(r[2])} for r in _rows(wb["Data Files"], 4, 3) if _s(r[0])]
    if "Revenue Tree" in wb.sheetnames:
        out["revenue_tree"] = []
        for r in _rows(wb["Revenue Tree"], 4, 15):
            if not _s(r[0]) or _s(r[0]).startswith("Other revenue lines"):
                if _s(r[0]).startswith("Other revenue lines"):
                    break
                continue
            out["revenue_tree"].append({"id": _s(r[0]), "label": _s(r[1]), "parent": _s(r[2]), "kind": _s(r[3]) or "sum", "volume_id": _s(r[4]), "price_id": _s(r[5]),
                                        "price_basis": _s(r[6]), "data_label": _s(r[7]), "data_section": _s(r[8]), "format": _s(r[9]), "fy_rule": _s(r[10]), "hist_formula": _s(r[11]), "notes": _s(r[12]),
                                        "annual_data_label": _s(r[13]), "annual_data_section": _s(r[14])})
    if "Cost Tree" in wb.sheetnames:
        out["cost_tree"] = [{"id": _s(r[0]), "label": _s(r[1]), "section": _s(r[2]), "segment": _s(r[3]), "data_label": _s(r[4]), "data_section": _s(r[5]), "sbc_data_label": _s(r[6]), "volume_id": _s(r[7]), "notes": _s(r[8]),
                             "annual_data_label": _s(r[9]), "annual_data_section": _s(r[10])}
                            for r in _rows(wb["Cost Tree"], 4, 11) if _s(r[0])]
    if "Drivers" in wb.sheetnames:
        out["drivers"] = []
        for r in _rows(wb["Drivers"], 4, 10):
            if not _s(r[0]):
                continue
            rep = _s(r[7])
            out["drivers"].append({"id": _s(r[0]), "label": _s(r[1]), "section": _s(r[2]), "target": _s(r[3]), "type": _s(r[4]) or "flat", "cased": _s(r[5]) or "Y",
                                   "format": _s(r[6]) or "%", "represented": rep, "formula": rep if rep.startswith("=") else "", "fy": _s(r[8]), "notes": _s(r[9]),
                                   "target_sub": _default_sub(_s(r[4]))})
    if "Variance & Deltas" in wb.sheetnames:
        ws = wb["Variance & Deltas"]
        d0 = None
        m = re.search(r"deltas_start=(\d+)", _s(ws["J1"].value))
        if m:
            d0 = int(m.group(1))
        out["variance"], out["deltas"] = [], []
        for r in range(4, (d0 or ws.max_row + 1) - 2):
            v = [ws.cell(row=r, column=c).value for c in range(1, 9)]
            if _s(v[0]):
                out["variance"].append({"id": _s(v[0]), **{k: str(x).upper().startswith("Y") for k, x in zip(["pct_yoy", "pct_2y", "usd_yoy", "pct_qoq", "usd_qoq", "pct_total"], v[1:7])}, "start": _s(v[7])})
        if d0:
            for r in range(d0 + 1, ws.max_row + 1):
                v = [ws.cell(row=r, column=c).value for c in range(1, 10)]
                if _s(v[1]):
                    out["deltas"].append({"sheet": _s(v[0]) or "Revenue Build", "line": _s(v[1]), "label": _s(v[2]), "measure": _s(v[3]) or "growth", "source": _s(v[4]) or "Consensus",
                                          "data_label": _s(v[5]), "data_section": _s(v[6]), "from": _s(v[7]), "to": _s(v[8])})
    if "Side Builds" in wb.sheetnames:
        out["side_builds"] = [{"name": _s(r[0]), "driver": _s(r[1]), "description": _s(r[2])} for r in _rows(wb["Side Builds"], 4, 3) if _s(r[0])]
    if "Guidance" in wb.sheetnames:
        out["guidance"] = [{"line": _s(r[0]), "measure": _s(r[1]), "period": _s(r[2]), "low": r[3], "high": r[4], "source": _s(r[6]) if len(r) > 6 else ""} for r in _rows(wb["Guidance"], 4, 7) if _s(r[0])]
    if "Buyside" in wb.sheetnames:
        out["buyside"] = [{"line": _s(r[0]), "measure": _s(r[1]), "period": _s(r[2]), "value": r[3], "source": _s(r[4])} for r in _rows(wb["Buyside"], 4, 5) if _s(r[0])]
    if "KPI History" in wb.sheetnames:
        ws = wb["KPI History"]
        heads = [_s(ws.cell(row=3, column=c).value) for c in range(2, ws.max_column + 1)]
        kpi = {}
        for r in range(4, ws.max_row + 1):
            lab = _s(ws.cell(row=r, column=1).value)
            if not lab:
                continue
            vals = {}
            for i, h in enumerate(heads):
                p = parse_pid(h) if h else None
                v = ws.cell(row=r, column=2 + i).value
                if p and isinstance(v, (int, float)):
                    vals[pid_of(*p)] = float(v)
            kpi[lab] = vals
        out["kpi_history"] = kpi
    if "Statement Mapping" in wb.sheetnames:
        out["mapping"] = [{"id": _s(r[0]), "label": _s(r[1]), "statement": _s(r[2]), "data_label": _s(r[3]), "data_section": _s(r[4]), "keep": _s(r[5]) or "Y",
                           "annual_data_label": _s(r[6]), "annual_data_section": _s(r[7])} for r in _rows(wb["Statement Mapping"], 4, 8) if _s(r[0])]
    if "Driver Grid" in wb.sheetnames:
        ws = wb["Driver Grid"]
        heads = [_s(ws.cell(row=3, column=c).value) for c in range(1, ws.max_column + 1)]
        pcols = {}
        for i, h in enumerate(heads):
            p = parse_pid(h) if h and h not in ("Driver ID", "Case", "Comment") else None
            if p:
                pcols[i + 1] = pid_of(*p)
        comment_col = heads.index("Comment") + 1 if "Comment" in heads else None
        grid, notes = {}, {}
        # map of grid rows -> (driver, case) so formulas that reference other grid cells can be
        # re-expressed as engine tokens (the same A1 address means another cell in the model)
        row_map = {}
        for r in range(4, ws.max_row + 1):
            did, case = _s(ws.cell(row=r, column=1).value), _s(ws.cell(row=r, column=2).value)
            if did and case and not ws.cell(row=r, column=1).font.bold:
                row_map[r] = (did, case)
        col_letters = {get_column_letter(col): pid for col, pid in pcols.items()}
        grey_cols = {get_column_letter(col) for col, pid in pcols.items() if ws.cell(row=4, column=col).fill is not None and ws.cell(row=4, column=col).fill.fgColor is not None and ws.cell(row=4, column=col).fill.fgColor.rgb == GREY}
        ref_re = re.compile(r"(?<![A-Za-z_!'])\$?([A-Z]{1,3})\$?(\d+)(?![\d(])")
        warnings = []

        def translate(formula: str, here: tuple) -> str:
            def repl(m):
                colL, rown = m.group(1), int(m.group(2))
                pid = col_letters.get(colL)
                if pid is None or rown not in row_map:
                    warnings.append(f"{here[0]}/{here[1]}: {formula} refers to {m.group(0)} outside the grid; left as typed")
                    return m.group(0)
                drv, cs = row_map[rown]
                if colL in grey_cols:
                    return "{drv:" + drv + "@" + pid + "}"          # realised history on the Active row
                return "{drv:" + drv + ":" + cs + "@" + pid + "}"   # another typed estimate
            return ref_re.sub(repl, formula)

        for r in range(4, ws.max_row + 1):
            if r not in row_map:
                continue
            did, case = row_map[r]
            for col, pid in pcols.items():
                c = ws.cell(row=r, column=col)
                if c.value is None or str(c.value).strip() == "":
                    continue
                if c.fill is not None and c.fill.fgColor is not None and c.fill.fgColor.rgb == GREY:
                    continue  # realised history, not an input
                v = c.value
                if isinstance(v, str):
                    vs = v.strip()
                    if vs.endswith("%") and re.fullmatch(r"-?[\d.]+%", vs):
                        v = float(vs[:-1]) / 100
                    elif re.fullmatch(r"-?[\d,]*\.?\d+", vs):
                        v = float(vs.replace(",", ""))
                    elif vs.startswith("=") and "!" not in vs:
                        v = translate(vs, (did, case))
                grid.setdefault(did, {}).setdefault(case, {})[pid] = v
                if c.comment is not None and c.comment.text:
                    notes.setdefault(did, {}).setdefault(case, {})[pid] = c.comment.text.strip()
            if comment_col:
                txt = _s(ws.cell(row=r, column=comment_col).value)
                if txt:
                    notes.setdefault(did, {}).setdefault(case, {})["_row"] = txt
        out["driver_grid"], out["driver_grid_notes"] = grid, notes
        if warnings:
            out["driver_grid_warnings"] = warnings
    if "Multiples" in wb.sheetnames:
        ws = wb["Multiples"]
        blocks = []
        for r in (4, 5):
            label = _s(ws.cell(row=r, column=8).value)
            if label:
                td = ws.cell(row=r, column=10).value
                blocks.append({"label": label, "basis": _s(ws.cell(row=r, column=9).value) or "YE", "target_date": td.date().isoformat() if isinstance(td, dt.datetime) else _s(td),
                               "metric_period": _s(ws.cell(row=r, column=11).value), "blended_label": _s(ws.cell(row=r, column=12).value) or label})
        mults, mnotes, weights = {}, {}, {}
        r = 4
        while _s(ws.cell(row=r, column=1).value) and not _s(ws.cell(row=r, column=1).value).startswith("Weights"):
            case = _s(ws.cell(row=r, column=1).value)
            for j, b in enumerate(blocks):
                c = ws.cell(row=r, column=2 + j)
                if isinstance(c.value, (int, float)):
                    mults.setdefault(case, {})[b["label"]] = float(c.value)
                if c.comment is not None and c.comment.text:
                    mnotes.setdefault(case, {})[b["label"]] = c.comment.text.strip()
            rc = ws.cell(row=r, column=4)
            if _s(rc.value):
                for b in blocks:
                    mnotes.setdefault(case, {}).setdefault(b["label"], _s(rc.value))
            r += 1
        for rr in range(r, ws.max_row + 1):
            k = _s(ws.cell(row=rr, column=1).value)
            v = ws.cell(row=rr, column=2).value
            if k in ("Disaster", "Bear", "Base", "Bull", "Blowout") and isinstance(v, (int, float)):
                weights[k] = float(v)
            if k.startswith("Current implied multiple"):
                cur_period = _s(v)
        out["tearsheet"] = {"blocks": blocks, "multiples": mults, "multiple_notes": mnotes, "weights": weights,
                            "current_multiple_period": locals().get("cur_period")}
    if "DCF Inputs" in wb.sheetnames:
        ws = wb["DCF Inputs"]
        dcf, notes, exits, enotes = {}, {}, {}, {}
        for r in range(4, ws.max_row + 1):
            key = _s(ws.cell(row=r, column=1).value)
            val = ws.cell(row=r, column=3).value
            note = _s(ws.cell(row=r, column=4).value)
            if not key:
                continue
            if key.startswith("exit_"):
                case = _s(ws.cell(row=r, column=2).value)
                if isinstance(val, (int, float)):
                    exits[case] = float(val)
                if note:
                    enotes[case] = note
            elif key in ("cash_lines", "debt_lines"):
                dcf[key] = [x.strip() for x in _s(val).split(",") if x.strip()]
            else:
                dcf[key] = val.date().isoformat() if isinstance(val, dt.datetime) else val
                if note:
                    notes[key] = note
        dcf["exit_multiples"] = exits
        notes["exit_multiples"] = enotes
        dcf["notes"] = notes
        out["dcf"] = dcf
    return out


def _default_sub(dtype: str) -> Optional[str]:
    # gm_pct is resolved by spec_builder to the gross-profit line's GM % row
    return {"yoy_pct": "pct_yoy", "qoq_pct": "pct_qoq", "net_adds": "net_adds_qoq", "bps_qoq": "bps_qoq", "bps_yoy": "bps_yoy", "pct_of_base": "pct_of"}.get(dtype.lower())
