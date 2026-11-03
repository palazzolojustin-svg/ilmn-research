"""Period axis: fiscal quarters and years laid out as model columns.

Layout rule (from the reference model): for every fiscal year that has quarterly
columns, the four quarters come first and the fiscal-year column follows them.
Years beyond the quarterly horizon get one annual column each. Columns start at D;
A is a 2-wide marker column, B holds labels, C is a 2-wide spacer.
"""
from __future__ import annotations

import datetime as dt
import re
from dataclasses import dataclass, field
from typing import Dict, List, Optional

from openpyxl.utils import get_column_letter

FIRST_DATA_COL = 4  # column D


@dataclass
class Period:
    pid: str                 # canonical id: "1Q23", "FY2023", "FY2029"
    kind: str                # "Q" or "FY"
    fy: int                  # fiscal year
    q: int = 0               # 1..4 for quarters, 0 for FY
    estimate: bool = False   # True for estimate periods
    annual_only: bool = False  # FY column of a year that has no quarterly columns
    end: Optional[dt.date] = None  # period end date
    weeks: Optional[int] = None    # weeks in period (13/14 for quarters, 52/53 for years)
    col: int = 0             # worksheet column index (1-based)
    report_date: Optional[dt.date] = None

    @property
    def letter(self) -> str:
        return get_column_letter(self.col)

    @property
    def label(self) -> str:
        """Header label exactly as the reference model writes it."""
        yy = f"{self.fy % 100:02d}"
        if self.kind == "Q":
            return f"{self.q}Q{yy}{'E' if self.estimate else ''}"
        if self.annual_only:
            return f"FY{self.fy}{'E' if self.estimate else ''}"
        return f"FY {self.fy}{'E' if self.estimate else ''}"

    @property
    def months(self) -> int:
        return 3 if self.kind == "Q" else 12

    @property
    def is_q(self) -> bool:
        return self.kind == "Q"


def parse_pid(text: str) -> Optional[tuple]:
    """Parse '1Q23', '1Q2023', '2026Q3', 'FY2026', 'FY 2026E', '2026' -> (kind, fy, q)."""
    s = str(text).strip().upper().replace(" ", "")
    s = s.rstrip("E")
    m = re.fullmatch(r"([1-4])Q(\d{2}|\d{4})", s)
    if m:
        y = int(m.group(2)); y = y + 2000 if y < 100 else y
        return ("Q", y, int(m.group(1)))
    m = re.fullmatch(r"(\d{4})Q([1-4])", s)
    if m:
        return ("Q", int(m.group(1)), int(m.group(2)))
    m = re.fullmatch(r"(?:FY)?(\d{4})(?:Y)?", s)
    if m:
        return ("FY", int(m.group(1)), 0)
    return None


def pid_of(kind: str, fy: int, q: int = 0) -> str:
    return f"{q}Q{fy % 100:02d}" if kind == "Q" else f"FY{fy}"


def fiscal_quarter_end(fy_end_month: int, fy_end_day: int, fy: int, q: int) -> dt.date:
    """Quarter end for a fiscal calendar with month-end quarters (or a fixed day of the
    month when fy_end_day is before the 28th). Fiscal year `fy` is named by the calendar
    year in which it ends (FY ending June-2027 is FY2027)."""
    month = fy_end_month - 3 * (4 - q)
    year = fy
    while month <= 0:
        month += 12
        year -= 1
    if fy_end_day and fy_end_day < 28:
        return dt.date(year, month, fy_end_day)
    nxt = dt.date(year + (1 if month == 12 else 0), 1 if month == 12 else month + 1, 1)
    return nxt - dt.timedelta(days=1)


def _is_month_end(d: dt.date) -> bool:
    return (d + dt.timedelta(days=1)).month != d.month


def derive_end(prev_end: Optional[dt.date], fy_end_month: int, fy_end_day: int, fy: int, q: int) -> dt.date:
    """End of a period whose date the data did not give: thirteen weeks after the previous
    period end on a 52/53-week calendar (previous end not a month end), else the
    fiscal month end."""
    if prev_end is not None and not _is_month_end(prev_end):
        return prev_end + dt.timedelta(days=91)
    return fiscal_quarter_end(fy_end_month, fy_end_day, fy, q)


@dataclass
class PeriodAxis:
    periods: List[Period] = field(default_factory=list)
    by_id: Dict[str, Period] = field(default_factory=dict)

    @classmethod
    def build(cls, first_hist_q: str, last_actual_q: str, last_est_q: str,
              annual_only_years: List[int], period_ends: Optional[Dict[str, str]] = None,
              fy_end_month: int = 12, fy_end_day: int = 31,
              report_dates: Optional[Dict[str, str]] = None, start_col: int = FIRST_DATA_COL,
              annual_hist_years: Optional[List[int]] = None) -> "PeriodAxis":
        """Build the main axis. Quarter ids like '1Q23'. period_ends maps pid -> ISO date
        for any period whose end is known (actuals from data, estimates from consensus);
        missing ends are derived from the fiscal calendar."""
        _, y1, q1 = parse_pid(first_hist_q)
        _, y2, q2 = parse_pid(last_actual_q)
        _, y3, q3 = parse_pid(last_est_q)
        # every quarterly year is complete: history starts in Q1, the quarterly horizon ends in Q4,
        # so fiscal-year columns always sum four quarters
        q1, q3 = 1, 4
        ends = {k: dt.date.fromisoformat(v) for k, v in (period_ends or {}).items() if v}
        rdates = {k: dt.date.fromisoformat(v) for k, v in (report_dates or {}).items() if v}
        axis = cls()
        col = start_col
        y = y1
        prev_end: Optional[dt.date] = None
        # annual history columns before the quarterly history (typed from the annual statements)
        for ay in sorted(set(int(v) for v in (annual_hist_years or []))):
            if ay >= y1:
                continue
            pid = pid_of("FY", ay)
            end = ends.get(pid) or fiscal_quarter_end(fy_end_month, fy_end_day, ay, 4)
            axis._add(Period(pid, "FY", ay, 0, False, True, end, None, col))
            prev_end = end
            col += 1
        while y <= y3:
            for q in range(1, 5):
                est = (y, q) > (y2, q2)
                pid = pid_of("Q", y, q)
                end = ends.get(pid) or derive_end(prev_end, fy_end_month, fy_end_day, y, q)
                axis._add(Period(pid, "Q", y, q, est, False, end, None, col, rdates.get(pid)))
                prev_end = end
                col += 1
            pid = pid_of("FY", y)
            est = y > y2 or (y == y2 and q2 < 4)
            end = ends.get(pid) or prev_end or fiscal_quarter_end(fy_end_month, fy_end_day, y, 4)
            axis._add(Period(pid, "FY", y, 0, est, False, end, None, col))
            col += 1
            y += 1
        for y in sorted(set(int(v) for v in annual_only_years)):
            pid = pid_of("FY", y)
            if pid in axis.by_id:
                continue  # already covered by the quarterly horizon
            end = ends.get(pid) or (prev_end + dt.timedelta(days=364) if prev_end and not _is_month_end(prev_end) else fiscal_quarter_end(fy_end_month, fy_end_day, y, 4))
            axis._add(Period(pid, "FY", y, 0, True, True, end, None, col))
            prev_end = end
            col += 1
        axis._compute_weeks()
        return axis

    def _add(self, p: Period):
        self.periods.append(p)
        self.by_id[p.pid] = p

    def _compute_weeks(self):
        prev_q_end = None
        for p in self.quarters():
            if prev_q_end and p.end:
                p.weeks = int(round((p.end - prev_q_end).days / 7.0))
            else:
                p.weeks = 13
            prev_q_end = p.end
        prev_fy_end: Optional[dt.date] = None
        for p in self.fys():
            qs = self.quarters_of(p.fy)
            if len(qs) == 4 and all(q.weeks for q in qs):
                p.weeks = sum(q.weeks for q in qs)
            elif p.annual_only and p.end and prev_fy_end and 300 < (p.end - prev_fy_end).days < 400:
                p.weeks = int(round((p.end - prev_fy_end).days / 7.0))
            else:
                p.weeks = 52
            prev_fy_end = p.end

    # ---- queries -------------------------------------------------------------------
    def quarters(self) -> List[Period]:
        return [p for p in self.periods if p.kind == "Q"]

    def fys(self) -> List[Period]:
        return [p for p in self.periods if p.kind == "FY"]

    def quarters_of(self, fy: int) -> List[Period]:
        return [p for p in self.periods if p.kind == "Q" and p.fy == fy]

    def fy_of(self, p: Period) -> Optional[Period]:
        return self.by_id.get(pid_of("FY", p.fy))

    def has_quarters(self, fy: int) -> bool:
        return bool(self.quarters_of(fy))

    def prior_year(self, p: Period) -> Optional[Period]:
        if p.kind == "Q":
            return self.by_id.get(pid_of("Q", p.fy - 1, p.q))
        return self.by_id.get(pid_of("FY", p.fy - 1))

    def prior_period(self, p: Period) -> Optional[Period]:
        """Prior quarter for quarterly columns; prior fiscal year for FY columns."""
        if p.kind == "Q":
            if p.q > 1:
                return self.by_id.get(pid_of("Q", p.fy, p.q - 1))
            return self.by_id.get(pid_of("Q", p.fy - 1, 4))
        return self.by_id.get(pid_of("FY", p.fy - 1))

    def offset(self, p: Period, n: int) -> Optional[Period]:
        """n periods back (negative n) or forward in the same kind."""
        if p.kind == "Q":
            idx = p.fy * 4 + (p.q - 1) + n
            return self.by_id.get(pid_of("Q", idx // 4, idx % 4 + 1))
        return self.by_id.get(pid_of("FY", p.fy + n))

    def first(self) -> Period:
        return self.periods[0]

    def last(self) -> Period:
        return self.periods[-1]

    def last_col(self) -> int:
        return self.periods[-1].col

    def estimates(self) -> List[Period]:
        return [p for p in self.periods if p.estimate]

    def actual_quarters(self) -> List[Period]:
        return [p for p in self.quarters() if not p.estimate]

    def last_actual_quarter(self) -> Period:
        return self.actual_quarters()[-1]

    def last_actual_fy(self) -> Optional[Period]:
        f = [p for p in self.fys() if not p.estimate and not p.annual_only]
        return f[-1] if f else None

    def sub_axis(self, from_pid: str, start_col: int = FIRST_DATA_COL) -> "PeriodAxis":
        """A copy of this axis starting at `from_pid` with columns renumbered (used for
        the Drivers & Casing sheet, which starts at the first quarter of the last actual year)."""
        sub = PeriodAxis()
        col = start_col
        started = False
        for p in self.periods:
            if p.pid == from_pid:
                started = True
            if not started:
                continue
            sub._add(Period(p.pid, p.kind, p.fy, p.q, p.estimate, p.annual_only, p.end, p.weeks, col, p.report_date))
            col += 1
        return sub

    def drivers_start_pid(self) -> str:
        """First column of the drivers sheet: first quarter of the last actual fiscal year
        (falls back to the first estimate period)."""
        la = self.last_actual_quarter()
        qs = self.quarters_of(la.fy)
        return qs[0].pid if qs else self.estimates()[0].pid
