"""Parse Bloomberg consensus and CapIQ exports into one normalised data file.

Supported inputs
  * Bloomberg "Company Financials" printouts saved as Markdown (tables with a period
    header row such as `2025Q1 | 2026Q3 Est` or `2023 Y | 2026 Y Est`, period-end dates
    on the next row, section rows with no values, and `<br>`-merged rows)
  * Bloomberg Excel exports with the same table shape
  * CapIQ Excel exports (Income Statement, Balance Sheet, Cash Flow, Key Stats) whose
    headers read "12 months Dec-31-2023" / "3 months Mar-30-2025"
  * any xlsx/csv grid with recognisable period headers

Output (JSON)
  {"files": [...], "fy_end_month": 12, "periods": {pid: {"end": "2025-03-30", "estimate": false}},
   "lines": [{"file", "sheet", "section", "label", "values": {pid: number}, "pct": bool, "suspect": bool}],
   "last_actual_quarter": "2Q26", "last_estimate_quarter": "4Q28", "ticker": "ILMN US Equity", "currency": "USD"}

Period ids follow the model convention: 1Q25, FY2025.
"""
from __future__ import annotations

import csv
import datetime as dt
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from .periods import pid_of

BB_Q = re.compile(r"^(\d{4})\s*Q([1-4])(\s*Est)?$", re.I)
BB_Y = re.compile(r"^(\d{4})\s*Y(\s*Est)?$", re.I)
BB_H = re.compile(r"^(\d{4})\s*H([12])(\s*Est)?$", re.I)
DATE_US = re.compile(r"^(\d{1,2})/(\d{1,2})/(\d{4})$")
CAPIQ_HDR = re.compile(r"(\d+)\s*months?\s*(?:ending)?\s*([A-Za-z]{3})-(\d{1,2})-(\d{4})", re.I)
CAPIQ_LTM = re.compile(r"\bLTM\b", re.I)
MONTHS = {m: i for i, m in enumerate(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}
NUM = re.compile(r"^\(?-?\$?[\d,]*\.?\d+\)?%?$")
SECTION_HINTS = ("highlights", "segment revenue", "business breakdown", "regional breakdown", "income statement", "gaap results",
                 "company specific adjustments", "balance sheet", "assets", "liabilities & equity", "cash flow", "cash from",
                 "changes in working capital", "special company reference items", "prior disclosures")


# ----------------------------------------------------------------------------- helpers
def to_number(cell) -> Tuple[Optional[float], bool]:
    """Return (value, suspect). Suspect = an integer that looks like it lost its decimal point."""
    if cell is None:
        return None, False
    if isinstance(cell, bool):
        return None, False
    if isinstance(cell, (int, float)):
        return float(cell), False
    s = str(cell).strip()
    if "<br>" in s:
        parts = [p for p in s.split("<br>") if p.strip() not in ("", ".", ",")]
        s = parts[-1].strip() if parts else ""
    s = s.replace("−", "-").replace("—", "").replace("–", "-")
    if s in ("", "-", "--", "N/A", "NA", "n/a", "NM", "n.m.", "."):
        return None, False
    neg = s.startswith("(") and s.endswith(")")
    s = s.strip("()").replace("$", "").replace("%", "").replace(",", "").strip()
    if not re.fullmatch(r"-?\d*\.?\d+", s):
        return None, False
    v = float(s)
    if neg:
        v = -v
    suspect = "." not in s and len(s.lstrip("-")) >= 3
    return v, suspect


def period_from_label(label: str) -> Optional[Tuple[str, bool]]:
    s = str(label).strip()
    m = BB_Q.match(s)
    if m:
        return pid_of("Q", int(m.group(1)), int(m.group(2))), bool(m.group(3))
    m = BB_Y.match(s)
    if m:
        return pid_of("FY", int(m.group(1))), bool(m.group(2))
    m = BB_H.match(s)
    if m:
        return f"{m.group(2)}H{int(m.group(1)) % 100:02d}", bool(m.group(3))
    return None


def parse_us_date(s: str) -> Optional[dt.date]:
    m = DATE_US.match(str(s).strip())
    if not m:
        return None
    mo, d, y = int(m.group(1)), int(m.group(2)), int(m.group(3))
    try:
        return dt.date(y, mo, d)
    except ValueError:
        return None


# ----------------------------------------------------------------------------- markdown
def md_tables(text: str) -> List[List[List[str]]]:
    """Split markdown into tables (lists of rows of cells). `<br>` kept for later splitting."""
    tables, cur = [], []
    for line in text.splitlines():
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if all(re.fullmatch(r"-*", c) for c in cells):
                continue
            cur.append(cells)
        else:
            if cur:
                tables.append(cur); cur = []
    if cur:
        tables.append(cur)
    return tables


def split_br_rows(row: List[str]) -> List[List[str]]:
    """Rows whose cells contain `<br>` are two (or more) rows merged by the PDF export.
    Empty parts are dropped; when the label cell has more parts than the value cells
    (a section title printed above a data line) the values belong to the last labels."""
    if not any("<br>" in c for c in row):
        return [row]
    parts = [[x.strip() for x in c.split("<br>") if x.strip() not in ("", ".", ",")] for c in row]
    label_parts = parts[0]
    value_parts = parts[1:]
    n_vals = max((len(p) for p in value_parts), default=0)
    if len(label_parts) <= 1 and n_vals <= 1:
        return [[label_parts[0] if label_parts else ""] + [p[0] if p else "" for p in value_parts]]
    out = []
    n_lab = len(label_parts)
    # section titles come first in the label cell and carry no values
    lead = max(0, n_lab - n_vals)
    for i in range(lead):
        out.append([label_parts[i]] + [""] * len(value_parts))
    rows_n = max(n_vals, n_lab - lead)
    for j in range(rows_n):
        lab = label_parts[lead + j] if lead + j < n_lab else ""
        out.append([lab] + [(p[j] if j < len(p) else "") for p in value_parts])
    return [r for r in out if any(c for c in r)]


def parse_bloomberg_md(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    meta = {"ticker": None, "currency": None, "periodicity": None}
    m = re.search(r"Ticker:\s*([A-Z0-9 .]+?Equity)", text)
    if m:
        meta["ticker"] = m.group(1).strip()
    m = re.search(r"Currency:\s*([A-Z]{2,3})\|?([A-Z])?", text)
    if m:
        meta["currency"] = (m.group(1) + (m.group(2) or "")).strip()[:3]
    periods: Dict[str, dict] = {}
    lines: List[dict] = []
    cols: List[Optional[str]] = []   # pid per value column of the current table
    section = None
    for table in md_tables(text):
        for raw in table:
            for row in split_br_rows(raw):
                if not row:
                    continue
                label = row[0].strip()
                vals = row[1:]
                # header rows
                if label.lower().startswith("ticker:"):
                    continue
                pids = [period_from_label(v) for v in vals]
                if any(pids) and sum(1 for p in pids if p) >= max(2, len(vals) // 2):
                    cols = [p[0] if p else None for p in pids]
                    for p in pids:
                        if p:
                            periods.setdefault(p[0], {"end": None, "estimate": p[1]})
                            periods[p[0]]["estimate"] = p[1]
                    continue
                dates = [parse_us_date(v) for v in vals]
                if any(dates) and sum(1 for d in dates if d) >= max(2, len(vals) // 2) and cols:
                    for pid, d in zip(cols, dates):
                        if pid and d:
                            periods[pid]["end"] = d.isoformat()
                    continue
                if re.match(r"^(in (millions|thousands|billions)|multiple periods|i milli|n ons o)", label.lower()) or not cols:
                    continue
                nums = [to_number(v) for v in vals]
                has_vals = any(v is not None for v, _ in nums)
                if not has_vals:
                    # a section title has no values at all; a data line printed with dashes
                    # ("—" for not available) keeps the current section
                    raw_blank = all(str(v).strip() in ("", ".", ",") for v in vals)
                    if label and (raw_blank or label.lower().startswith(SECTION_HINTS)):
                        section = label
                    elif label:
                        lines.append({"file": path.name, "sheet": None, "section": section, "label": label, "values": {},
                                      "pct": False, "suspect": False, "suspect_pids": [], "est": {}})
                    continue
                if not label:
                    # values without a label (a split artefact): attach them to the previous line if it has none
                    if lines and not lines[-1]["values"] and lines[-1]["section"] == section:
                        label = lines.pop()["label"]
                    else:
                        continue
                pct = "(%)" in label or label.lower().startswith("as % of") or label.lower().endswith("(%)")
                values, est, suspect_pids = {}, {}, []
                for pid, (v, sus) in zip(cols, nums):
                    if pid is None or v is None:
                        continue
                    values[pid] = v / 100.0 if pct else v
                    est[pid] = bool(periods.get(pid, {}).get("estimate"))
                    if sus:
                        suspect_pids.append(pid)
                lines.append({"file": path.name, "sheet": None, "section": section, "label": label, "values": values,
                              "pct": pct, "suspect": bool(suspect_pids), "suspect_pids": suspect_pids, "est": est})
    meta["periods"] = periods
    meta["lines"] = lines
    meta["source"] = "bloomberg_md"
    return meta


# ----------------------------------------------------------------------------- grids (xlsx / csv)
def load_grids(path: Path) -> List[Tuple[str, List[List[object]]]]:
    if path.suffix.lower() == ".xls":
        try:
            import xlrd  # noqa: F401
        except ImportError:
            raise ValueError(f"{path.name} is a legacy .xls export; save it as .xlsx in Excel (or pip install xlrd) and parse again")
        import xlrd
        book = xlrd.open_workbook(str(path))
        out = []
        for sh in book.sheets():
            rows = [[sh.cell_value(r, c) for c in range(sh.ncols)] for r in range(sh.nrows)]
            out.append((sh.name, rows))
        return out
    if path.suffix.lower() in (".xlsx", ".xlsm"):
        from openpyxl import load_workbook
        wb = load_workbook(path, data_only=True, read_only=True)
        out = []
        for ws in wb.worksheets:
            rows = [list(r) for r in ws.iter_rows(values_only=True)]
            out.append((ws.title, rows))
        return out
    if path.suffix.lower() in (".csv", ".tsv"):
        with open(path, newline="", encoding="utf-8-sig", errors="replace") as f:
            dialect = csv.excel_tab if path.suffix.lower() == ".tsv" else csv.excel
            rows = [list(r) for r in csv.reader(f, dialect)]
        return [(path.stem, rows)]
    raise ValueError(f"unsupported file type {path.suffix}")


def capiq_period(header) -> Optional[Tuple[int, dt.date, bool]]:
    """'12 months Dec-31-2023' -> (12, date, is_ltm)"""
    if header is None:
        return None
    s = str(header).replace("\n", " ")
    if CAPIQ_LTM.search(s):
        return None
    m = CAPIQ_HDR.search(s)
    if not m:
        return None
    months = int(m.group(1))
    mon = MONTHS.get(m.group(2).lower()[:3])
    if not mon:
        return None
    try:
        d = dt.date(int(m.group(4)), mon, int(m.group(3)))
    except ValueError:
        return None
    return months, d, False


def _snap(d: dt.date) -> dt.date:
    """A period end a few days into a month (52/53-week calendars: Jan-03-2027) belongs to
    the previous month for fiscal-period arithmetic."""
    return d - dt.timedelta(days=7) if d.day <= 7 else d


def grid_fy_end_month(rows: List[List[object]]) -> Optional[int]:
    """Fiscal year end month from 12-month CapIQ headers on a grid, if any."""
    years = []
    for r in rows[:60]:
        for c in r:
            p = capiq_period(c)
            if p and p[0] == 12:
                years.append(_snap(p[1]).month)
    return Counter(years).most_common(1)[0][0] if years else None


def parse_grid(name: str, rows: List[List[object]], fname: str, fy_hint: Optional[int] = None) -> Optional[dict]:
    """Find a period header row in a grid and read the labelled rows under it. fy_hint is
    the fiscal year end month learnt from 12-month columns elsewhere (another sheet or file)."""
    header_idx, cols, fy_end_month = None, [], None
    # 1) Bloomberg-style labels
    for i, r in enumerate(rows[:40]):
        cells = ["" if c is None else str(c) for c in r]
        pids = [period_from_label(c) for c in cells]
        if sum(1 for p in pids if p) >= 3:
            header_idx = i
            cols = [(p[0], p[1]) if p else None for p in pids]
            break
    capiq = False
    if header_idx is None:
        # 2) CapIQ-style "12 months Dec-31-2023"
        best = None
        for i, r in enumerate(rows[:60]):
            per = [capiq_period(c) for c in r]
            n = sum(1 for p in per if p)
            if n >= 3 and (best is None or n > best[1]):
                best = (i, n, per)
        if best:
            header_idx, _, per = best
            capiq = True
            years = [p for p in per if p and p[0] == 12]
            if years:
                fy_end_month = Counter(_snap(p[1]).month for p in years).most_common(1)[0][0]
            elif fy_hint:
                fy_end_month = fy_hint
            else:
                # quarterly-only sheet with no fiscal year evidence anywhere: assume December and say so
                fy_end_month = 12
            cols = []
            for p in per:
                if not p:
                    cols.append(None); continue
                months, d, _ = p
                ds = _snap(d)
                fy = ds.year + (1 if ds.month > fy_end_month else 0)
                if months == 12:
                    cols.append((pid_of("FY", fy), False, d))
                elif months == 3:
                    after = (ds.month - fy_end_month) % 12
                    q = 4 if after == 0 else after // 3
                    if after % 3 != 0:
                        cols.append(None); continue
                    cols.append((pid_of("Q", fy, q), False, d))
                else:
                    cols.append(None)
    if header_idx is None:
        return None
    periods, lines, section = {}, [], None
    for c in cols:
        if c:
            periods[c[0]] = {"end": c[2].isoformat() if len(c) > 2 else None, "estimate": c[1]}
    # Bloomberg xlsx may carry a date row right under the header
    nxt = rows[header_idx + 1] if header_idx + 1 < len(rows) else []
    if not capiq and nxt:
        ds = [parse_us_date(str(c)) if c is not None and not isinstance(c, (dt.date, dt.datetime)) else (c.date() if isinstance(c, dt.datetime) else c) for c in nxt]
        if sum(1 for d in ds if d) >= 3:
            for col, d in zip(cols, ds):
                if col and d:
                    periods[col[0]]["end"] = d.isoformat()
            header_idx += 1
    label_col = 0
    for r in rows[header_idx + 1:]:
        if not r or all(c is None or str(c).strip() == "" for c in r):
            continue
        label = r[label_col]
        if label is None or str(label).strip() == "":
            continue
        label = str(label).strip()
        nums = [to_number(c) for c in r]
        values, est, suspect_pids = {}, {}, []
        for col, (v, sus) in zip(cols, nums):
            if col and v is not None:
                values[col[0]] = v
                est[col[0]] = bool(col[1])
                if sus and not capiq:
                    suspect_pids.append(col[0])
        if not values:
            section = label
            continue
        pct = "(%)" in label or label.lower().startswith("as % of") or label.lower().endswith("%")
        if pct and not capiq:
            values = {k: v / 100.0 for k, v in values.items()}
        lines.append({"file": fname, "sheet": name, "section": section, "label": label, "values": values, "pct": pct,
                      "suspect": bool(suspect_pids), "suspect_pids": suspect_pids, "est": est})
    return {"periods": periods, "lines": lines, "fy_end_month": fy_end_month, "source": "capiq" if capiq else "grid",
            "fy_end_assumed": capiq and not any(p and p[0] == 12 for p in (best[2] if best else [])) and not fy_hint}


# ----------------------------------------------------------------------------- driver
def parse_file(path: str, fy_hint: Optional[int] = None) -> dict:
    p = Path(path)
    if p.suffix.lower() in (".md", ".txt"):
        return parse_bloomberg_md(p)
    out = {"periods": {}, "lines": [], "source": None, "fy_end_month": None, "fy_end_assumed": False}
    grids = load_grids(p)
    # learn the fiscal year end from any 12-month columns in the workbook before keying quarters
    hint = fy_hint
    for name, rows in grids:
        hint = hint or grid_fy_end_month(rows)
    for name, rows in grids:
        g = parse_grid(name, rows, p.name, fy_hint=hint)
        if not g:
            continue
        out["periods"].update(g["periods"])
        out["lines"].extend(g["lines"])
        out["source"] = out["source"] or g["source"]
        out["fy_end_month"] = out["fy_end_month"] or g.get("fy_end_month")
        out["fy_end_assumed"] = out["fy_end_assumed"] or bool(g.get("fy_end_assumed"))
    return out


def parse_files(paths: List[str]) -> List[dict]:
    """Parse several files, sharing the fiscal-year-end evidence across them."""
    hint = None
    for f in paths:
        p = Path(f)
        if p.suffix.lower() in (".xlsx", ".xlsm", ".xls", ".csv", ".tsv"):
            try:
                for _, rows in load_grids(p):
                    hint = hint or grid_fy_end_month(rows)
            except Exception:
                pass
    return [parse_file(f, fy_hint=hint) for f in paths]


def fix_suspects(lines: List[dict]) -> Tuple[List[dict], List[dict]]:
    """Repair values whose decimal point the export dropped (7300 printed for 73.00) when
    the same label elsewhere gives an unambiguous scale; return (corrections, unresolved)."""
    by_label: Dict[str, List[dict]] = {}
    for l in lines:
        by_label.setdefault(_norm(l["label"]), []).append(l)
    corrections, unresolved = [], []
    for l in lines:
        if not l.get("suspect_pids"):
            continue
        refs = []
        for other in by_label.get(_norm(l["label"]), []):
            for pid, v in other["values"].items():
                if pid not in other.get("suspect_pids", []) and v:
                    # annual references are compared on a per-quarter basis
                    refs.append(abs(v) / (4.0 if pid.startswith("FY") and not l["values"] else 1.0) if pid.startswith("FY") else abs(v))
        ref = sorted(refs)[len(refs) // 2] if refs else None
        for pid in list(l["suspect_pids"]):
            v = l["values"].get(pid)
            if v is None:
                continue
            fixed = None
            if ref:
                for factor in (100.0, 10.0, 1000.0):
                    cand = v / factor
                    if 0.2 <= abs(cand) / ref <= 5.0:
                        fixed = cand
                        break
            if fixed is not None:
                corrections.append({"file": l["file"], "label": l["label"], "period": pid, "was": v, "now": fixed})
                l["values"][pid] = fixed
                l.setdefault("corrected_pids", []).append(pid)
            else:
                unresolved.append({"file": l["file"], "label": l["label"], "period": pid, "value": v})
    return corrections, unresolved


def merge(parsed: List[dict]) -> dict:
    periods: Dict[str, dict] = {}
    lines: List[dict] = []
    ticker = currency = None
    fy_end = None
    assumed = False
    for d in parsed:
        for pid, info in d.get("periods", {}).items():
            cur = periods.setdefault(pid, {"end": None, "estimate": info.get("estimate", False)})
            if info.get("end"):
                cur["end"] = info["end"]
            # an actual in any file wins over an estimate flag elsewhere
            cur["estimate"] = cur["estimate"] and info.get("estimate", False)
        lines.extend(d.get("lines", []))
        ticker = ticker or d.get("ticker")
        currency = currency or d.get("currency")
        fy_end = fy_end or d.get("fy_end_month")
        assumed = assumed or bool(d.get("fy_end_assumed"))
    if fy_end is None:
        ends = [_snap(dt.date.fromisoformat(v["end"])) for k, v in periods.items() if k.startswith("FY") and v.get("end")]
        fy_end = Counter(e.month for e in ends).most_common(1)[0][0] if ends else 12
    corrections, unresolved = fix_suspects(lines)
    qs = sorted([k for k in periods if "Q" in k], key=_qkey)
    actual_q = [k for k in qs if not periods[k]["estimate"]]
    est_q = [k for k in qs if periods[k]["estimate"]]
    return {"periods": periods, "lines": lines, "ticker": ticker, "currency": currency, "fy_end_month": fy_end,
            "fy_end_assumed": assumed,
            "last_actual_quarter": actual_q[-1] if actual_q else None,
            "first_quarter": qs[0] if qs else None,
            "last_estimate_quarter": est_q[-1] if est_q else None,
            "n_lines": len(lines), "corrections": corrections, "unresolved_suspects": unresolved}


def _qkey(pid: str):
    m = re.match(r"(\d)Q(\d{2})", pid)
    return (2000 + int(m.group(2)), int(m.group(1))) if m else (0, 0)


def find_line(data: dict, label: str, section: Optional[str] = None, prefer_file: Optional[str] = None) -> Optional[dict]:
    """First line whose label matches (case-insensitive, punctuation-insensitive)."""
    key = _norm(label)
    cands = [l for l in data["lines"] if _norm(l["label"]) == key and (section is None or _norm(l.get("section") or "") == _norm(section))]
    if prefer_file:
        cands.sort(key=lambda l: 0 if prefer_file in l["file"] else 1)
    return cands[0] if cands else None


def series(data: dict, label: str, section: Optional[str] = None, exclude_sections: Optional[List[str]] = None) -> Dict[str, float]:
    """Values for a label merged across files. Within one file only the first line with
    that label counts (Bloomberg repeats balance-sheet labels in the working-capital
    block, after the statement line), unless a section is named. Across files a value
    from an actual column beats one from an estimate column, whatever the file order."""
    key = _norm(label)
    excl = [_norm(s) for s in (exclude_sections or [])]
    out: Dict[str, float] = {}
    is_est: Dict[str, bool] = {}
    seen_files = set()
    for l in data["lines"]:
        if _norm(l["label"]) != key:
            continue
        sec = _norm(l.get("section") or "")
        if section and sec != _norm(section):
            continue
        if excl and any(sec.startswith(e) for e in excl):
            continue
        if not section:
            fkey = (l["file"], l.get("sheet"))
            if fkey in seen_files:
                continue
            seen_files.add(fkey)
        ests = l.get("est") or {}
        for pid, v in l["values"].items():
            e = ests.get(pid, data["periods"].get(pid, {}).get("estimate", False))
            if pid not in out or (is_est.get(pid, True) and not e):
                out[pid] = v
                is_est[pid] = e
    return out


def _norm(s: str) -> str:
    return re.sub(r"[^a-z0-9%]+", " ", str(s).lower()).strip()


def main(argv: List[str]):
    if len(argv) < 2:
        print(__doc__); return
    out_path = None
    files = []
    for a in argv:
        if a.startswith("--out="):
            out_path = a[6:]
        else:
            files.append(a)
    parsed = parse_files(files)
    merged = merge(parsed)
    merged["files"] = [Path(f).name for f in files]
    if out_path:
        Path(out_path).write_text(json.dumps(merged, indent=1, default=str), encoding="utf-8")
        print("wrote", out_path)
    print(json.dumps({k: merged[k] for k in ("ticker", "currency", "fy_end_month", "fy_end_assumed", "first_quarter",
                                             "last_actual_quarter", "last_estimate_quarter", "n_lines")}, indent=1))
    secs = Counter((l["section"] or "-") for l in merged["lines"])
    print("sections:", dict(secs.most_common(30)))
    if merged["corrections"]:
        print("corrected lost-decimal values (confirm with the analyst):")
        for c in merged["corrections"]:
            print(f"  {c['file']} | {c['label']} | {c['period']}: {c['was']} -> {c['now']}")
    if merged["unresolved_suspects"]:
        print("suspect values that could not be corrected (ask the analyst):")
        for u in merged["unresolved_suspects"]:
            print(f"  {u['file']} | {u['label']} | {u['period']}: {u['value']}")


if __name__ == "__main__":
    main(sys.argv[1:])
