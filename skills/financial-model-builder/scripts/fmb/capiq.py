"""S&P Capital IQ "Financials" workbook export.

One workbook, one sheet per report: Key Stats, Income Statement, Balance Sheet, Cash Flow,
Multiples, Historical Capitalization, Capital Structure Summary / Details, Ratios,
Supplemental, Industry Specific, Pension OPEB, Segments. Every sheet has the same shape:

    row ~4    "Illumina, Inc. (NasdaqGS:ILMN) > Financials > Income Statement"
    rows 6-10 metadata pairs: "Template: | Standard", "Period Type: | Annual",
              "Currency: | US Dollar", "Order: | Latest on Right", ...
    title     "Income Statement" / "Key Financials" / "Business Segments"
    header    "For the Fiscal Period Ending" | "12 months\\nDec-31-2023A" | "LTM\\n12 months\\nSep-27-2026A" | ...
              or "Balance Sheet as of:" | <date cells>, or "For Quarter Ending" | <date cells>
    "Currency | USD | USD ..." then the labelled rows. A text row without numbers starts a
    sub-section ("Per Share Items", "ASSETS"); footnotes start with *, ¹, ², †, "Note".
    A sheet may hold several tables, each with its own header row (Key Stats, Segments).

Period columns: "12 months" -> fiscal year (FY pid), "3 months" -> quarter, LTM / 6 / 9
months -> skipped. "E" after the year marks an estimate (Key Stats consensus columns).
Date-cell headers use the sheet's Period Type: on an Annual sheet a date at the fiscal
year end is the fiscal year, any other date is the quarter it ends.

The section of a line is "<sheet> - <sub-section>" (sheet name alone before the first
sub-section), so statement lookups can prefer or exclude whole sheets by prefix.
"""
from __future__ import annotations

import datetime as dt
import re
from collections import Counter
from typing import Dict, List, Optional, Tuple

from .periods import pid_of

HEADER_STARTS = ("for the fiscal period", "balance sheet as of", "for quarter ending", "for the quarter ending",
                 "for the period ending", "as of")
SKIP_LABELS = {"currency", "exchange rate", "conversion method", "filing date", "restatement type", "calculation type",
               "inventory method", "pricing as of"}
FOOTNOTE = re.compile(r"^(\*|¹|²|³|†|‡|note\b|\(\d+\)|growth rates are|all results|all forward|for companies that|total liability|net liability|tev includes|total capital includes)", re.I)
HDR = re.compile(r"(\d+)\s*months?\W*(?:ending)?\W*([A-Za-z]{3})-(\d{1,2})-(\d{4})\s*([AE])?", re.I)
LTM = re.compile(r"LTM", re.I)
TICKER = re.compile(r"\(([A-Za-z]+):([A-Z0-9.\-]{1,10})\)")
MONTHS = {m: i for i, m in enumerate(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}
CURRENCIES = {"us dollar": "USD", "euro": "EUR", "british pound": "GBP", "pound sterling": "GBP", "japanese yen": "JPY", "swiss franc": "CHF",
              "canadian dollar": "CAD", "australian dollar": "AUD", "hong kong dollar": "HKD", "chinese yuan": "CNY", "danish krone": "DKK",
              "swedish krona": "SEK", "norwegian krone": "NOK", "indian rupee": "INR", "singapore dollar": "SGD", "korean won": "KRW",
              "new taiwan dollar": "TWD", "brazilian real": "BRL", "mexican peso": "MXN", "south african rand": "ZAR"}
US_EXCHANGES = ("nasdaq", "nyse", "amex", "otc", "bats", "arca")


def _text(c) -> str:
    return "" if c is None else str(c).replace("\n", " ").strip()


def _snap(d: dt.date) -> dt.date:
    """A period end a few days into a month (52/53-week calendars: Jan-02-2022) belongs to the previous month."""
    return d - dt.timedelta(days=7) if d.day <= 7 else d


def _as_date(c) -> Optional[dt.date]:
    if isinstance(c, dt.datetime):
        return c.date()
    if isinstance(c, dt.date):
        return c
    return None


def _number(c) -> Optional[float]:
    if c is None or isinstance(c, bool) or isinstance(c, (dt.date, dt.datetime)):
        return None
    if isinstance(c, (int, float)):
        return float(c)
    s = str(c).strip().replace(",", "")
    if s in ("", "-", "--", "NA", "NM", "N/A", "n/a", "n.m.", "."):
        return None
    neg = s.startswith("(") and s.endswith(")")
    s = s.strip("()").replace("$", "").replace("%", "").strip()
    if not re.fullmatch(r"-?\d*\.?\d+", s):
        return None
    v = float(s)
    return -v if neg else v


def looks_like_capiq(grids: List[Tuple[str, List[List[object]]]]) -> bool:
    for _, rows in grids:
        for r in rows[:40]:
            if r and _text(r[0]).lower().startswith(HEADER_STARTS[:3]):
                return True
    return False


def _metadata(rows: List[List[object]]) -> dict:
    """Ticker, currency and period type from the first rows of a sheet."""
    meta: Dict[str, Optional[str]] = {"ticker": None, "exchange": None, "currency": None, "period_type": None}
    for r in rows[:14]:
        cells = [_text(c) for c in r]
        for i, c in enumerate(cells):
            m = TICKER.search(c)
            if m and not meta["ticker"]:
                meta["exchange"], meta["ticker"] = m.group(1), m.group(2)
            low = c.lower().rstrip(":")
            nxt = next((x for x in cells[i + 1:] if x), "")
            if low == "currency" and nxt and not meta["currency"]:
                meta["currency"] = CURRENCIES.get(nxt.lower(), nxt.upper() if len(nxt) == 3 else None)
            if low in ("period type", "frequency") and nxt and not meta["period_type"]:
                meta["period_type"] = nxt.lower()
            m2 = re.search(r"\bin (?:millions|thousands|billions) of ([A-Z]{3})\b", c, re.I)
            if m2 and not meta["currency"]:
                meta["currency"] = m2.group(1).upper()
    return meta


def _fy_end_month(grids, fy_hint: Optional[int]) -> Tuple[int, bool]:
    months = []
    for _, rows in grids:
        for r in rows[:80]:
            for c in r:
                m = HDR.search(_text(c)) if isinstance(c, str) else None
                if m and int(m.group(1)) == 12 and not LTM.search(_text(c)):
                    mon = MONTHS.get(m.group(2).lower()[:3])
                    if mon:
                        try:
                            months.append(_snap(dt.date(int(m.group(4)), mon, int(m.group(3)))).month)
                        except ValueError:
                            pass
    if months:
        return Counter(months).most_common(1)[0][0], False
    if fy_hint:
        return fy_hint, False
    return 12, True


def _fy_of(d: dt.date, fy_end_month: int) -> int:
    ds = _snap(d)
    return ds.year + (1 if ds.month > fy_end_month else 0)


def _quarter_pid(d: dt.date, fy_end_month: int) -> Optional[str]:
    ds = _snap(d)
    after = (ds.month - fy_end_month) % 12
    if after % 3:
        return None
    return pid_of("Q", _fy_of(d, fy_end_month), 4 if after == 0 else after // 3)


def _col(c, period_type: Optional[str], fy_end_month: int) -> Optional[Tuple[str, bool, dt.date]]:
    """(pid, estimate, end date) for a header cell, or None for a column to skip."""
    d = _as_date(c)
    if d is not None:
        annual = (period_type or "").startswith("annual")
        if annual and _snap(d).month == fy_end_month:
            return pid_of("FY", _fy_of(d, fy_end_month)), False, d
        q = _quarter_pid(d, fy_end_month)
        return (q, False, d) if q else None
    s = _text(c)
    if not s or LTM.search(s):
        return None
    m = HDR.search(s)
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
    est = (m.group(5) or "").upper() == "E"
    if months == 12:
        return pid_of("FY", _fy_of(d, fy_end_month)), est, d
    if months == 3:
        q = _quarter_pid(d, fy_end_month)
        return (q, est, d) if q else None
    return None


def _clean_title(s: str) -> str:
    return re.sub(r"[¹²³†‡*]+", "", s).strip().rstrip(":").strip()


def parse_sheet(sheet: str, rows: List[List[object]], fname: str, fy_end_month: int, period_type: Optional[str],
                trust_dates: bool = True) -> Tuple[dict, List[dict]]:
    periods: Dict[str, dict] = {}
    lines: List[dict] = []
    cols: Optional[List[Optional[Tuple[str, bool, dt.date]]]] = None
    title: Optional[str] = None
    sub: Optional[str] = None
    pending_title: Optional[str] = None
    for r in rows:
        cells = list(r) + [None] * max(0, 2 - len(r))
        label = _text(cells[0])
        low = label.lower().rstrip(":")
        if low.startswith(HEADER_STARTS):
            cols = [None] + [_col(c, period_type, fy_end_month) for c in cells[1:]]
            for col in cols:
                if col:
                    periods.setdefault(col[0], {"end": col[2].isoformat() if trust_dates else None, "estimate": col[1]})
            title = pending_title or title or sheet
            sub = None
            continue
        nums = [_number(c) for c in cells[1:]]
        if cols is None:
            # above the first header: a text row without numbers and without a "key: value" pair is the table title
            if label and not any(v is not None for v in nums) and ":" not in label and not FOOTNOTE.match(label) and len(label) < 70:
                pending_title = _clean_title(label)
            continue
        if not label or low in SKIP_LABELS or FOOTNOTE.match(label):
            continue
        values, est = {}, {}
        for col, c in zip(cols, cells):
            if col is None:
                continue
            v = _number(c)
            if v is None:
                continue
            values[col[0]] = v
            est[col[0]] = bool(col[1])
        if not values:
            if any(_text(c) in ("-", "NA", "NM", "--") for c in cells[1:]):
                continue   # a real line with no data in any period
            if any(v is not None for v in nums) and sub and "current" in sub.lower():
                values = {"CUR": next(v for v in nums if v is not None)}   # current-capitalization snapshot, one value
            else:
                nxt = _clean_title(label)
                if nxt:
                    pending_title = nxt   # becomes the title if a header follows, the sub-section otherwise
                    sub = nxt
                continue
        elif sub and "current" in sub.lower() and len(values) == 1 and cols[1] is not None and list(values) == [cols[1][0]]:
            values = {"CUR": next(iter(values.values()))}   # single-column snapshot under the first period header
        qual = _text(cells[1]) if len(cols) > 1 and cols[1] is None and _number(cells[1]) is None else ""
        full_label = f"{label} ({qual})" if qual and qual.lower() not in ("usd", "eur", "gbp") else label
        section = " - ".join(x for x in (sheet, title if title and title.lower() != sheet.lower() else None, sub) if x)
        pct = label.endswith("%") or label.lower().startswith(("growth over", "compound annual growth", "margin %"))
        if pct:
            mags = sorted(abs(v) for v in values.values())
            if mags and mags[len(mags) // 2] > 1.5:
                values = {k: v / 100.0 for k, v in values.items()}
        lines.append({"file": fname, "sheet": sheet, "section": section, "label": full_label, "values": values, "pct": pct,
                      "suspect": False, "suspect_pids": [], "est": est})
    return periods, lines


def parse_workbook(grids: List[Tuple[str, List[List[object]]]], fname: str, fy_hint: Optional[int] = None) -> dict:
    fy_end_month, assumed = _fy_end_month(grids, fy_hint)
    out = {"periods": {}, "lines": [], "source": "capiq", "fy_end_month": fy_end_month, "fy_end_assumed": assumed,
           "ticker": None, "currency": None}
    for sheet, rows in grids:
        meta = _metadata(rows)
        if meta["ticker"] and not out["ticker"]:
            exch = (meta["exchange"] or "").lower()
            out["ticker"] = f"{meta['ticker']} US Equity" if exch.startswith(US_EXCHANGES) else meta["ticker"]
            out["exchange"] = meta["exchange"]
        if meta["currency"] and not out["currency"]:
            out["currency"] = meta["currency"]
        trust = sheet.strip().lower() not in ("multiples", "historical capitalization")
        periods, lines = parse_sheet(sheet, rows, fname, fy_end_month, meta["period_type"], trust)
        for pid, info in periods.items():
            cur = out["periods"].setdefault(pid, dict(info))
            cur["estimate"] = cur["estimate"] and info["estimate"]
            cur["end"] = cur.get("end") or info.get("end")
        out["lines"].extend(lines)
    return out
