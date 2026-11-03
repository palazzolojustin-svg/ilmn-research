"""Regression test: rebuild the Spotify reference model from its own inputs.

Usage:  python spot_regression.py <path to spot template .xlsx> <output dir>

Reads every hardcode, driver input and side-build cell out of the reference workbook,
expresses the model as an engine spec, builds it, recalculates in Excel and compares
the main outputs with the reference workbook's cached values.
"""
from __future__ import annotations

import datetime as dt
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "scripts"))

from openpyxl import load_workbook  # noqa: E402
from openpyxl.utils import get_column_letter  # noqa: E402

from fmb import styles as S  # noqa: E402
from fmb.build_model import build  # noqa: E402
from fmb.engine import BS, CFS, IS, MARGIN, REV  # noqa: E402
from fmb.periods import PeriodAxis  # noqa: E402
from fmb.verify import verify  # noqa: E402

HIST_COLS = ["D", "E", "F", "G", "I", "J", "K", "L", "N", "O", "P", "Q", "S", "T"]
HIST_PIDS = ["1Q23", "2Q23", "3Q23", "4Q23", "1Q24", "2Q24", "3Q24", "4Q24", "1Q25", "2Q25", "3Q25", "4Q25", "1Q26", "2Q26"]
EST_COLS = {"U": "3Q26", "V": "4Q26", "W": "FY2026", "X": "1Q27", "Y": "2Q27", "Z": "3Q27", "AA": "4Q27", "AB": "FY2027",
            "AC": "1Q28", "AD": "2Q28", "AE": "3Q28", "AF": "4Q28", "AG": "FY2028", "AH": "FY2029", "AI": "FY2030"}
DRV_COLS = {"D": "1Q26", "E": "2Q26", "F": "3Q26", "G": "4Q26", "H": "FY2026", "I": "1Q27", "J": "2Q27", "K": "3Q27",
            "L": "4Q27", "M": "FY2027", "N": "1Q28", "O": "2Q28", "P": "3Q28", "Q": "4Q28", "R": "FY2028", "S": "FY2029", "T": "FY2030"}
CELL_REF = re.compile(r"(?<![A-Za-z_])\$?[A-Z]{1,3}\$?\d+")

DATA_ROWS = {
    REV: {23: "prem_rev", 31: "prem_subs", 37: "prem_arpu", 44: "ab_rev", 51: "ab_subs", 52: "ab_pct", 59: "ab_rpu",
          61: "nonab_rev", 86: "ad_rev", 94: "ad_mau", 100: "ad_arpu"},
    MARGIN: {47: "prem_cogs", 78: "ad_cogs", 97: "rd", 103: "sbc_rd", 110: "sm", 116: "sbc_sm", 123: "ga", 129: "sbc_ga",
             146: "total_sbc", 150: "op_inc", 25: "bop_mau"},
    IS: {14: "is_prem_rev", 15: "is_ad_rev", 19: "cogs", 23: "is_rd", 24: "is_sm", 25: "is_ga", 32: "fin_inc", 33: "fin_cost",
         37: "tax", 44: "dep", 45: "amort", 49: "sbc", 54: "shares_basic", 55: "shares_dil", 56: "eps_basic", 57: "eps_dil"},
    CFS: {19: "wc_recv", 20: "wc_pay", 21: "wc_defrev", 22: "wc_prov", 23: "wc_tax", 24: "other_op", 27: "capex", 28: "st_inv_chg",
          29: "other_inv", 34: "opt_proceeds", 35: "buybacks", 36: "lease_principal", 37: "rsu_tax", 38: "notes_debt",
          39: "other_fin", 41: "fx", 44: "beg_cash"},
    BS: {15: "cash", 16: "st_inv", 17: "receivables", 18: "tax_recv", 19: "other_ca", 23: "rou", 24: "ppe", 25: "goodwill",
         26: "intangibles", 27: "lt_inv", 28: "restricted_other", 29: "fin_lease_recv", 30: "dta", 36: "payables", 37: "tax_payable",
         38: "deferred_rev", 39: "accrued", 40: "exch_notes_cur", 41: "provisions", 42: "deriv_liab", 46: "lease_liab",
         47: "accrued_nc", 48: "provisions_nc", 49: "dtl", 50: "exch_notes_nc", 56: "paid_in", 57: "treasury", 58: "other_reserves",
         59: "retained"},
}

DRIVER_MAP = {  # (section, title) -> (id, fmt, cased, extra)
    ("Revenue Drivers", "Premium ARPU Growth y/y Ex. Add-ons"): ("prem_arpu_g", "pct_plain"),
    ("Revenue Drivers", "Premium Subs Growth y/y "): ("prem_subs_g", "pct_plain"),
    ("Revenue Drivers", "% of Audiobook+ Premium Subs QoQ Change"): ("ab_pct_bps", "bps"),
    ("Revenue Drivers", "% Uptake of Audiobooks + Adoption for Other Add-ons"): ("ab_uptake", "pct_plain"),
    ("Revenue Drivers", "Ads Supported MAU y/y Growth"): ("ad_mau_g", "pct_plain"),
    ("Revenue Drivers", "Ads Supported ARPU y/y Growth"): ("ad_arpu_g", "pct_plain"),
    ("Revenue Drivers", "Peak Add-on Pxing "): ("peak_px", "price"),
    ("Cost Drivers", "Premium Gross Margin "): ("prem_gm", "pct_plain"),
    ("Cost Drivers", "Ad Gross Margin "): ("ad_gm", "pct_plain"),
    ("Cost Drivers", "G&A % of Revenue"): ("ga_pct", "pct_plain"),
    ("Cost Drivers", "S&M % of Revenue"): ("sm_pct", "pct_plain"),
    ("Cost Drivers", "R&D % of Revenue"): ("rd_pct", "pct_plain"),
    ("Income Statement Drivers", "Finance Income"): ("fin_inc", "amount_s"),
    ("Income Statement Drivers", "Finance Costs"): ("fin_cost", "amount_s"),
    ("Income Statement Drivers", "Tax Rate"): ("tax_rate", "pct_s"),
    ("Income Statement Drivers", "Depreciation"): ("dep", "amount_s"),
    ("Income Statement Drivers", "Amortization (Pre-Cap)"): ("amort", "amount_s"),
    ("Income Statement Drivers", "Stock-Based Compensation"): ("sbc", "amount_s"),
    ("Income Statement Drivers", "Basic Weighted Avg Shares"): ("shares_basic", "shares"),
    ("Income Statement Drivers", "Diluted Weighted Avg Shares"): ("shares_dil", "shares"),
    ("Balance Sheet Drivers", "Short-Term Investments"): ("st_inv", "amount_s"),
    ("Balance Sheet Drivers", "Income Tax Payable"): ("tax_payable", "amount_s"),
    ("Balance Sheet Drivers", "Trade & Other Receivables % of Qtr. Revenue"): ("recv_pct", "pct_s"),
    ("Balance Sheet Drivers", "Other Current Assets % of Qtr. Revenue"): ("other_ca_pct", "pct_s"),
    ("Balance Sheet Drivers", "Trade & Other Payables % of Qtr. (CoR + Opex)"): ("pay_pct", "pct_s"),
    ("Balance Sheet Drivers", "Deferred Revenue % of Qtr. Revenue"): ("defrev_pct", "pct_s"),
    ("Balance Sheet Drivers", "Accrued Expenses & Other % of Qtr. Cost of Revenue"): ("accrued_pct", "pct_s"),
    ("Balance Sheet Drivers", "ROU Asset Share of Depreciation"): ("rou_share", "pct_s"),
    ("Cash Flow Drivers", "Capital Expenditures"): ("capex", "amount_s"),
    ("Cash Flow Drivers", "Option Proceeds"): ("opt_proceeds", "amount_s"),
    ("Cash Flow Drivers", "Share Repurchases"): ("buybacks", "amount_s"),
    ("Cash Flow Drivers", "Lease Principal Payments"): ("lease_principal", "amount_s"),
    ("Cash Flow Drivers", "RSU Tax Withholding"): ("rsu_tax", "amount_s"),
}
UNCASED_FY = {"fin_inc": "sum", "fin_cost": "sum", "tax_rate": "last", "dep": "sum", "amort": "sum", "sbc": "sum",
              "shares_basic": "avg", "shares_dil": "avg", "st_inv": "last", "tax_payable": "last", "recv_pct": "last",
              "other_ca_pct": "last", "pay_pct": "last", "defrev_pct": "last", "accrued_pct": "last", "rou_share": "last",
              "capex": "sum", "opt_proceeds": "sum", "buybacks": "sum", "lease_principal": "sum", "rsu_tax": "sum"}
TARGETS = {
    "prem_arpu_g": ("prem_arpu_ex", "pct_yoy"), "prem_subs_g": ("prem_subs", "pct_yoy"), "ab_pct_bps": ("ab_pct", "bps_qoq"),
    "ad_mau_g": ("ad_mau", "pct_yoy"), "ad_arpu_g": ("ad_arpu", "pct_yoy"), "prem_gm": ("prem_gp", "pct_of"),
    "ad_gm": ("ad_gp", "pct_of"), "ga_pct": ("ga", "pct_of"), "sm_pct": ("sm", "pct_of"), "rd_pct": ("rd", "pct_of"),
    "fin_inc": ("fin_inc", None), "fin_cost": ("fin_cost", None), "tax_rate": ("tax_rate", None), "dep": ("dep", None),
    "amort": ("amort", None), "sbc": ("sbc", None), "shares_basic": ("shares_basic", None), "shares_dil": ("shares_dil", None),
    "st_inv": ("st_inv", None), "tax_payable": ("tax_payable", None), "capex": ("capex", None),
    "opt_proceeds": ("opt_proceeds", None), "buybacks": ("buybacks", None), "lease_principal": ("lease_principal", None),
    "rsu_tax": ("rsu_tax", None),
}


def cell_value(wf, wv, sheet, coord):
    """Value for data: numbers as-is, ref-free formulas as text, formulas with refs -> cached value."""
    v = wf[sheet][coord].value
    if v is None:
        return None
    if isinstance(v, str) and v.startswith("="):
        if "!" in v or CELL_REF.search(v):
            cv = wv[sheet][coord].value
            return cv if isinstance(cv, (int, float)) else None
        return v
    if isinstance(v, (int, float)) and not isinstance(v, bool):
        return v
    return None


def extract_data(wf, wv) -> dict:
    data = {}
    for sheet, rows in DATA_ROWS.items():
        for r, lid in rows.items():
            series = {}
            for col, pid in zip(HIST_COLS, HIST_PIDS):
                v = cell_value(wf, wv, sheet, f"{col}{r}")
                if v is not None:
                    series[pid] = v
            if lid == "beg_cash":
                series = {"1Q23": series.get("1Q23")}
            data[lid] = series
    # consensus rows (estimate columns)
    cons = {}
    for sheet, r, key in [(REV, 108, "cons_prem_rev_g"), (REV, 111, "cons_prem_arpu_g"), (REV, 114, "cons_total_rev_g"),
                          (MARGIN, 159, "cons_gm"), (MARGIN, 162, "cons_opm"), (MARGIN, 165, "cons_prem_gm"), (MARGIN, 168, "cons_inc_prem_gm")]:
        cons[key] = {pid: wf[sheet][f"{col}{r}"].value for col, pid in EST_COLS.items() if isinstance(wf[sheet][f"{col}{r}"].value, (int, float))}
    data["_consensus"] = cons
    return data


def extract_drivers(wf) -> list:
    ws = wf["Drivers & Casing"]
    drivers = []
    section = None
    r = 11
    cases = ["Disaster", "Bear", "Base", "Bull", "Blowout"]
    while r <= 190:
        b = ws[f"B{r}"].value
        if isinstance(b, str) and b.strip() in ("Revenue Drivers", "Cost Drivers", "Income Statement Drivers", "Balance Sheet Drivers", "Cash Flow Drivers"):
            section = b.strip(); r += 1; continue
        if isinstance(b, str) and (section, b) in DRIVER_MAP:
            did, fmt = DRIVER_MAP[(section, b)]
            nxt = ws[f"B{r + 1}"].value
            if nxt in cases:  # cased block
                vals = {}
                for i, case in enumerate(cases):
                    rr = r + 1 + i
                    assert ws[f"B{rr}"].value == case, (r, rr, ws[f"B{rr}"].value)
                    cv = {}
                    for col, pid in DRV_COLS.items():
                        v = ws[f"{col}{rr}"].value
                        if v is None:
                            continue
                        if isinstance(v, str) and v.startswith("=") and CELL_REF.search(v.replace("'ARPU Bridge'!", "").replace("'Margin Bridge'!", "")) and "!" not in v:
                            continue
                        cv[pid] = v
                    vals[case] = cv
                d = {"id": did, "label": b, "section": _sec(section), "fmt": fmt, "cased": True, "values": vals}
                if did == "peak_px":
                    d["single"] = True
                if did in TARGETS:
                    d["target"] = {"line": TARGETS[did][0], "sub": TARGETS[did][1]}
                drivers.append(d)
                r += 7
                continue
            else:  # uncased: values on the next row
                rr = r + 1
                cv = {}
                for col, pid in DRV_COLS.items():
                    v = ws[f"{col}{rr}"].value
                    if isinstance(v, (int, float)) and not isinstance(v, bool):
                        cv[pid] = v
                d = {"id": did, "label": b, "section": _sec(section), "fmt": fmt, "cased": False, "values": cv,
                     "fy": UNCASED_FY.get(did, "sum")}
                if did in ("shares_basic", "shares_dil"):
                    d["annual_dsl"] = "={drv:" + did + "@py}+({drv:" + did + "@4Q28$}-{drv:" + did + "@4Q27$})"
                if did in TARGETS:
                    d["target"] = {"line": TARGETS[did][0], "sub": TARGETS[did][1]}
                drivers.append(d)
                r += 3
                continue
        r += 1
    return drivers


def _sec(section: str) -> str:
    return {"Revenue Drivers": "revenue", "Cost Drivers": "cost", "Income Statement Drivers": "is",
            "Balance Sheet Drivers": "bs", "Cash Flow Drivers": "cf"}[section]


def extract_side_build(wf, name: str) -> dict:
    ws = wf[name]
    cells = []
    for row in ws.iter_rows():
        for c in row:
            if c.value is None:
                continue
            v = c.value
            if isinstance(v, str) and v.startswith("="):
                v = v.replace("'Revenue Build'!R23", "{Revenue Build!prem_rev@FY2025}")
            col = None
            if c.font and c.font.color is not None and c.font.color.type == "rgb" and c.font.color.rgb not in ("FF000000",):
                col = c.font.color.rgb
            fill = None
            if c.fill and c.fill.fill_type:
                fill = c.fill.fgColor.rgb if c.fill.fgColor.type == "rgb" else S.GREY_BAND
                if fill == "00000000":
                    fill = None
            entry = {"cell": c.coordinate, "value": v, "fmt": c.number_format if c.number_format != "General" else None,
                     "bold": bool(c.font.bold), "italic": bool(c.font.italic), "color": col if isinstance(col, str) and col != "FF000000" else None,
                     "fill": fill}
            if isinstance(v, dt.datetime):
                entry["value"] = v.date().isoformat(); entry["fmt"] = entry["fmt"] or "mmm-yy"
            cells.append(entry)
    widths = {k: v.width for k, v in ws.column_dimensions.items() if v.width}
    return {"name": name, "zoom": ws.sheet_view.zoomScale or 70, "widths": widths, "cells": cells,
            "merge": [str(m) for m in ws.merged_cells.ranges]}


def consensus_items(cons: dict) -> dict:
    return {
        REV: [
            {"label": "Premium Revenue", "line": "prem_rev", "sub": "pct_yoy", "values": cons["cons_prem_rev_g"]},
            {"label": "Premium ARPU", "line": "prem_arpu", "sub": "pct_yoy", "values": cons["cons_prem_arpu_g"]},
            {"label": "Total Revenue", "line": "total_rev", "sub": "pct_yoy", "values": cons["cons_total_rev_g"]},
        ],
        MARGIN: [
            {"label": "Total Gross Margin %", "line": "total_gp", "sub": "pct_of", "measure": "margin", "values": cons["cons_gm"]},
            {"label": "Total Operating Margin %", "line": "op_inc", "sub": "pct_of", "measure": "margin", "values": cons["cons_opm"]},
            {"label": "Premium Gross Margin %", "line": "prem_gp", "sub": "pct_of", "measure": "margin", "values": cons["cons_prem_gm"]},
            {"label": "Incremental Premium Gross Margin", "line": "prem_inc_gm", "measure": "margin", "values": cons["cons_inc_prem_gm"]},
        ],
    }


def L(**k):  # shorthand for a line block
    return {"line": k}


def revenue_blocks(cons) -> list:
    amt = ["pct_yoy", "pct_2y", "usd_yoy", "pct_qoq", "usd_qoq"]
    return [
        {"section": "Revenue Build"},
        {"subtitle": "Totals:", "marker": True},
        L(id="total_rev", label="Total Revenue", bold=True, dsl="={prem_rev}+{ad_rev}", fy="sum", subs=amt),
        {"band": "Premium:"},
        L(id="prem_rev", label="Premium Revenue", bold=True, hist="prem_rev", proj_dsl="={ab_rev}+{nonab_rev}+{prem_rev_ex}", fy="sum",
          subs=amt + ["pct_total"]),
        L(id="prem_subs", label="Period Average Premium Subscribers ", kind="count", bold=True, hist="prem_subs",
          proj_dsl="={prem_subs@py}*(1+{prem_subs.pct_yoy})", fy="avg", subs=["net_adds_yoy", "pct_yoy", "net_adds_qoq", "pct_qoq"],
          driver={"id": "prem_subs_g", "sub": "pct_yoy"}),
        L(id="prem_arpu", label="Premium ARPU", kind="price", bold=True, hist="prem_arpu", proj_dsl="={prem_rev}/({prem_subs}*{months})",
          fy="avg", subs=amt),
        L(id="ab_rev", label="Audiobook+ Revenue", bold=True, hist="ab_rev", proj_dsl="={ab_subs}*{ab_rpu}*{months}", fy="sum", subs=amt),
        L(id="ab_subs", label="Audiobook+ Paying Subscribers", kind="count", bold=True, hist="ab_subs", proj_dsl="={ab_pct}*{prem_subs}",
          fy="last", subs=["net_adds_yoy", "net_adds_qoq"]),
        L(id="ab_pct", label="% of Premium Subs", kind="pct", italic=True, hist="ab_pct", proj_dsl="={ab_pct@pq}+{ab_pct.bps_qoq}/10000",
          annual_dsl="={ab_pct@py}+{ab_pct.bps_qoq}/10000", fy="last",
          subs=["bps_yoy", "bps_2y", "bps_qoq"], sub_labels={"bps_yoy": "yoy change in % of subs", "bps_qoq": "qoq change in % of subs (FY29E-FY30E: yoy)"},
          driver={"id": "ab_pct_bps", "sub": "bps_qoq"}),
        L(id="ab_rpu", label="Audiobook+ Blended RPU ", kind="price", bold=True, hist="ab_rpu",
          proj_dsl="={ab_rpu@pq}+({ab_rpu@4Q27$}-{ab_rpu@2Q26$})/6", fy="avg",
          values={"4Q27": "={drv:peak_px@1Q26$}", "1Q28": "={ab_rpu@pq}", "2Q28": "={ab_rpu@pq}", "3Q28": "={ab_rpu@pq}", "4Q28": "={ab_rpu@pq}",
                  "FY2029": "={ab_rpu@py}+1", "FY2030": "={ab_rpu@py}+1"}),
        L(id="nonab_rev", label="Non Audiobook+ Add-on Revenue", bold=True, hist="nonab_rev",
          proj_dsl="={nonab_uptake}*{ab_pct@-6}*{prem_subs}*{ab_rpu@2Q26$}*{months}", fy="sum", subs=amt,
          sub_start={"pct_yoy": "1Q28", "usd_yoy": "1Q28", "pct_2y": "FY2029", "pct_qoq": "2Q27", "usd_qoq": "2Q27"},
          values={**{q: "={nonab_uptake}*{ab_pct@-6}*{prem_subs}*{ab_rpu@1Q27$}*{months}" for q in ["1Q28", "2Q28", "3Q28", "4Q28"]},
                  "FY2029": "={nonab_uptake}*AVERAGE({ab_pct@3Q27$},{ab_pct@4Q27$},{ab_pct@1Q28$},{ab_pct@2Q28$})*{prem_subs}*{ab_rpu@2Q27$}*{months}",
                  "FY2030": "={nonab_uptake}*(({ab_pct@3Q28$}+{ab_pct@4Q28$}+2*{ab_pct@FY2029$})/4)*{prem_subs}*{ab_rpu@2Q27$}*{months}"}),
        L(id="nonab_uptake", label="% of Audiobook+ Uptake ", kind="pct", italic=True, hist={"kind": "blank"}, proj_dsl="={drv:ab_uptake}",
          annual_dsl="={drv:ab_uptake}", fy="blank"),
        L(id="prem_rev_ex", label="Premium Revenue Ex. Add Ons", bold=True, hist={"kind": "formula", "dsl": "={prem_rev}-{ab_rev}-{nonab_rev}"},
          proj_dsl="={prem_arpu_ex}*{prem_subs}*{months}", fy="sum", fy_hist="formula", fy_dsl="={prem_rev}-{ab_rev}-{nonab_rev}", subs=amt),
        L(id="prem_arpu_ex", label="Premium ARPU Ex. Add Ons", kind="price", bold=True, hist={"kind": "formula", "dsl": "={prem_arpu}*({prem_rev_ex}/{prem_rev})"},
          proj_dsl="={prem_arpu_ex@py}*(1+{prem_arpu_ex.pct_yoy})", fy="avg", subs=amt, driver={"id": "prem_arpu_g", "sub": "pct_yoy"}),
        L(id="arpu_addon_contrib", label="Premium ARPU Growth Contribution from Add Ons yoy", kind="bps", bold=True, fmt="bps",
          dsl="=(({prem_arpu}-{prem_arpu_ex})-({prem_arpu@py}-{prem_arpu_ex@py}))/{prem_arpu@py}*10000", needs="py", fy="formula"),
        {"band": "Ads"},
        L(id="ad_rev", label="Ad-Supported Revenue", bold=True, hist="ad_rev", proj_dsl="={ad_arpu}*AVERAGE({ad_mau@pq},{ad_mau})*{months}",
          annual_dsl="={ad_arpu}*{ad_mau}*{months}", fy="sum", subs=amt + ["pct_total"]),
        L(id="ad_mau", label="Avg Ad-Supported MAUs", kind="count", bold=True, hist="ad_mau", proj_dsl="={ad_mau@py}*(1+{ad_mau.pct_yoy})",
          fy="avg", subs=["net_adds_yoy", "pct_yoy", "net_adds_qoq", "pct_qoq"], driver={"id": "ad_mau_g", "sub": "pct_yoy"}),
        L(id="ad_arpu", label="Ad-Supported ARPU", kind="price", bold=True, hist="ad_arpu", proj_dsl="={ad_arpu@py}*(1+{ad_arpu.pct_yoy})",
          fy="avg", subs=amt, driver={"id": "ad_arpu_g", "sub": "pct_yoy"}),
        {"blank": 1},
        {"deltas": cons[REV]},
    ]


def margin_blocks(cons) -> list:
    amt = ["pct_yoy", "pct_2y", "usd_yoy", "pct_qoq", "usd_qoq"]
    inc = {"key": "inc_ratio", "label": "Incremental Opex/Incremental Revenue (y/y)", "dsl": "=({id}-{id@py})/({m_total_rev}-{m_total_rev@py})",
           "fmt": "pct", "italic": True, "needs": "py"}
    return [
        {"section": "Revenue", "marker": False},
        L(id="m_prem_rev", label="Premium Revenue", bold=True, dsl="={Revenue Build!prem_rev}", fy="sum", subs=["pct_yoy"]),
        L(id="m_ad_rev", label="Ad-Supported Revenue", bold=True, dsl="={Revenue Build!ad_rev}", fy="sum", subs=["pct_yoy"]),
        L(id="m_total_rev", label="Total Revenue", bold=True, dsl="={m_prem_rev}+{m_ad_rev}", fy="sum", subs=["pct_yoy"]),
        L(id="m_prem_subs", label="Avg Premium Subscribers", kind="count", bold=True, dsl="={Revenue Build!prem_subs}", fy="formula"),
        L(id="m_ad_mau", label="Avg Ad-Supported MAUs", kind="count", bold=True, dsl="={Revenue Build!ad_mau}", fy="avg", gap=False),
        L(id="bop_mau", label="BOP Ad-Supported MAUs", kind="count", hist="bop_mau", proj_dsl="={eop_mau@pq}", annual_dsl="={eop_mau@py}", fy="first", gap=False),
        L(id="eop_mau", label="EOP Ad-Supported MAUs", kind="count", dsl="=2*{m_ad_mau}-{bop_mau}", fy="last"),
        {"section": "Cost of Revenue", "marker": False},
        L(id="total_cogs", label="Total COGS", bold=True, dsl="={prem_cogs}+{ad_cogs}", fy="sum",
          subs=[{"key": "pct_of", "label": "% of Total Revenue", "dsl": "={id}/{m_total_rev}", "fmt": "pct", "italic": True}] + amt),
        L(id="total_gp", label="Total Gross Profit", bold=True, dsl="={m_total_rev}-{total_cogs}", fy="sum",
          subs=[{"key": "pct_of", "label": "GM %", "dsl": "={id}/{m_total_rev}", "fmt": "pct", "italic": True}] + amt),
        {"band": "Premium:"},
        L(id="prem_cogs", label="Premium COGS", bold=True, hist="prem_cogs", proj_dsl="={m_prem_rev}*(1-{drv:prem_gm})", fy="sum",
          subs=[{"key": "pct_of", "label": "% of Premium Revenue", "dsl": "={id}/{m_prem_rev}", "fmt": "pct", "italic": True}] + amt),
        L(id="prem_gp_chg", label="y/y $ change in premium gross profit", italic=True, dsl="={prem_gp}-{prem_gp@py}", needs="py", fy="formula", gap=False),
        L(id="prem_rev_chg", label="y/y $ change in premium revenue", italic=True, dsl="={m_prem_rev}-{m_prem_rev@py}", needs="py", fy="formula", gap=False),
        L(id="prem_cogs_inc", label="Incremental premium COGS", italic=True, dsl="={prem_cogs}-{prem_cogs@py}", needs="py", fy="formula", gap=False),
        L(id="prem_inc_gm", label="Incremental Premium Gross Margin", kind="pct", bold=True, dsl="={prem_gp_chg}/{prem_rev_chg}", needs="py", fy="formula",
          subs=["bps_yoy", "bps_qoq"], sub_labels={"bps_yoy": "bps y/y ", "bps_qoq": "bps q/q"}),
        L(id="prem_cogs_base", label="Existing Premium COGS Base", bold=True, dsl="={prem_cogs}-{prem_cogs_inc}", needs="py", fy="formula", subs=amt),
        L(id="prem_gp", label="Premium Gross Profit", bold=True, dsl="={m_prem_rev}-{prem_cogs}", fy="sum",
          subs=[{"key": "pct_of", "label": "Premium GM %", "dsl": "={id}/{m_prem_rev}", "fmt": "pct", "italic": True}] + amt),
        {"band": "Ads:"},
        L(id="ad_cogs", label="Ad-Supported COGS", bold=True, hist="ad_cogs", proj_dsl="={m_ad_rev}*(1-{drv:ad_gm})", fy="sum",
          subs=[{"key": "pct_of", "label": "% of Ad-Supported Revenue", "dsl": "={id}/{m_ad_rev}", "fmt": "pct", "italic": True},
                {"key": "per_mau", "label": "COGS/Avg Ad MAU/Month", "dsl": "={id}/{m_ad_mau}/{months}", "fmt": "price", "italic": True},
                "pct_yoy", "usd_yoy", "pct_qoq", "usd_qoq"]),
        L(id="ad_gp", label="Ad-Supported Gross Profit", bold=True, dsl="={m_ad_rev}-{ad_cogs}", fy="sum",
          subs=[{"key": "pct_of", "label": "Ad-Supported GM %", "dsl": "={id}/{m_ad_rev}", "fmt": "pct", "italic": True}] + amt),
        {"section": "Operating Expenses", "marker": False},
        {"subtitle": "Research & Development:"},
        L(id="rd", label="R&D", bold=True, hist="rd", proj_dsl="={m_total_rev}*{drv:rd_pct}", fy="sum",
          subs=["pct_of", "pct_yoy", "usd_yoy", "pct_qoq", "usd_qoq"], base="m_total_rev", gap=False),
        L(id="sbc_rd", label="SBC - R&D", hist="sbc_rd", proj_dsl="={total_sbc}*{sbc_rd@py}/{total_sbc@py}", fy="sum", gap=False),
        L(id="rd_ex", label="R&D ex-SBC", dsl="={rd}-{sbc_rd}", fy="sum", base="m_total_rev",
          subs=["pct_of", "pct_yoy", "usd_yoy"], sub_labels={"pct_of": "ex-SBC % of Revenue", "pct_yoy": "ex-SBC % yoy", "usd_yoy": "ex-SBC $ yoy"}),
        {"subtitle": "Sales & Marketing:"},
        L(id="sm", label="Sales & Marketing", bold=True, hist="sm", proj_dsl="={m_total_rev}*{drv:sm_pct}", fy="sum",
          subs=["pct_of", "pct_yoy", "usd_yoy", "pct_qoq", "usd_qoq"], base="m_total_rev", gap=False),
        L(id="sbc_sm", label="SBC - S&M", hist="sbc_sm", proj_dsl="={total_sbc}*{sbc_sm@py}/{total_sbc@py}", fy="sum", gap=False),
        L(id="sm_ex", label="Sales & Marketing ex-SBC", dsl="={sm}-{sbc_sm}", fy="sum", base="m_total_rev",
          subs=["pct_of", "pct_yoy", "usd_yoy"], sub_labels={"pct_of": "ex-SBC % of Revenue", "pct_yoy": "ex-SBC % yoy", "usd_yoy": "ex-SBC $ yoy"}),
        {"subtitle": "General & Administrative:"},
        L(id="ga", label="G&A", bold=True, hist="ga", proj_dsl="={m_total_rev}*{drv:ga_pct}", fy="sum",
          subs=["pct_of", "pct_yoy", "usd_yoy", "pct_qoq", "usd_qoq"], base="m_total_rev", gap=False),
        L(id="sbc_ga", label="SBC - G&A", hist="sbc_ga", proj_dsl="={total_sbc}*{sbc_ga@py}/{total_sbc@py}", fy="sum", gap=False),
        L(id="ga_ex", label="G&A ex-SBC", dsl="={ga}-{sbc_ga}", fy="sum", base="m_total_rev",
          subs=["pct_of", "pct_yoy", "usd_yoy"], sub_labels={"pct_of": "ex-SBC % of Revenue", "pct_yoy": "ex-SBC % yoy", "usd_yoy": "ex-SBC $ yoy"}),
        L(id="total_opex", label="Total Opex", bold=True, dsl="={rd}+{sm}+{ga}", fy="sum", base="m_total_rev",
          subs=["pct_of", "pct_yoy", "usd_yoy", "pct_qoq", "usd_qoq", inc], gap=False),
        L(id="total_opex_ex", label="Total Opex ex-SBC", bold=True, dsl="={rd_ex}+{sm_ex}+{ga_ex}", fy="sum",
          subs=["pct_yoy", "usd_yoy", dict(inc, label="Incremental Opex ex-SBC/Incremental Revenue (y/y)")], gap=False),
        L(id="total_sbc", label="Total SBC", bold=True, hist="total_sbc", proj_dsl="={drv:sbc}", fy="sum",
          subs=[{"key": "cor", "label": "SBC - Cost of Revenue (implied)", "dsl": "={id}-{sbc_rd}-{sbc_sm}-{sbc_ga}", "fmt": "amount", "italic": True}]),
        {"subtitle": "Operating Income:"},
        L(id="op_inc", label="Operating Income", bold=True, hist="op_inc", proj_dsl="={total_gp}-{total_opex}", fy="sum", base="m_total_rev",
          subs=[{"key": "pct_of", "label": "% margin", "dsl": "={id}/{m_total_rev}", "fmt": "pct", "italic": True},
                {"key": "bps", "label": "bps y/y", "dsl": "=({id.pct_of}-{id.pct_of@py})*10000", "fmt": "bps", "italic": True, "needs": "py"},
                "pct_yoy", "usd_yoy",
                {"key": "inc_y", "label": "Incremental Operating Margin (y/y)", "dsl": "=({id}-{id@py})/({m_total_rev}-{m_total_rev@py})", "fmt": "pct", "italic": True, "needs": "py"},
                {"key": "inc_q", "label": "Incremental Operating Margin (q/q)", "dsl": "=({id}-{id@pq})/({m_total_rev}-{m_total_rev@pq})", "fmt": "pct", "italic": True, "needs": "pq", "q_only": True},
                {"key": "check", "label": "Check", "dsl": "=ROUND({total_gp}-{total_opex}-{id},6)", "fmt": "amount", "italic": True}]),
        {"deltas": cons[MARGIN]},
    ]


def is_blocks() -> list:
    return [
        {"section": "Income Statement", "marker": False},
        L(id="is_prem_rev", label="Premium Revenue", hist="is_prem_rev", proj_dsl="={Revenue Build!prem_rev}", fy="sum", gap=False),
        L(id="is_ad_rev", label="Ad-Supported Revenue", hist="is_ad_rev", proj_dsl="={Revenue Build!ad_rev}", fy="sum", gap=False),
        L(id="total_rev", label="Total Revenue", bold=True, top=True, dsl="={is_prem_rev}+{is_ad_rev}", fy="sum", fmt="amount_s",
          subs=[{"key": "pct_yoy", "label": "% YoY Growth", "dsl": "={id}/{id@py}-1", "fmt": "pct_s", "italic": True, "needs": "py"}]),
        L(id="cogs", label="Cost of Revenue", hist="cogs", proj_dsl="={Margin Build!total_cogs}", fy="sum", fmt="amount_s", gap=False),
        L(id="gp", label="Gross Profit", bold=True, top=True, dsl="={total_rev}-{cogs}", fy="sum", fmt="amount_s",
          subs=[{"key": "pct_of", "label": "% Gross Margin", "dsl": "={id}/{total_rev}", "fmt": "pct_s", "italic": True}]),
        L(id="is_rd", label="Research & Development", hist="is_rd", proj_dsl="={Margin Build!rd}", fy="sum", fmt="amount_s", gap=False),
        L(id="is_sm", label="Sales & Marketing", hist="is_sm", proj_dsl="={Margin Build!sm}", fy="sum", fmt="amount_s", gap=False),
        L(id="is_ga", label="General & Administrative", hist="is_ga", proj_dsl="={Margin Build!ga}", fy="sum", fmt="amount_s", gap=False),
        L(id="total_opex_is", label="Total Operating Expenses", bold=True, top=True, dsl="={is_rd}+{is_sm}+{is_ga}", fy="sum", fmt="amount_s",
          subs=[{"key": "pct_of", "label": "% of Revenue", "dsl": "={id}/{total_rev}", "fmt": "pct_s", "italic": True}]),
        L(id="op_inc_is", label="Operating Income", bold=True, dsl="={gp}-{total_opex_is}", fy="sum", fmt="amount_s",
          subs=[{"key": "pct_of", "label": "% Margin", "dsl": "={id}/{total_rev}", "fmt": "pct_s", "italic": True}]),
        L(id="fin_inc", label="Finance Income", hist="fin_inc", proj_dsl="={drv:fin_inc}", fy="sum", fmt="amount_s", gap=False),
        L(id="fin_cost", label="Finance Costs", hist="fin_cost", proj_dsl="={drv:fin_cost}", fy="sum", fmt="amount_s", gap=False),
        L(id="fin_net", label="Finance Income/(Costs), Net", bold=True, top=True, dsl="={fin_inc}+{fin_cost}", fy="sum", fmt="amount_s"),
        L(id="pretax", label="Pre-Tax Income", bold=True, dsl="={op_inc_is}+{fin_net}", fy="sum", fmt="amount_s", gap=False),
        L(id="tax", label="Income Tax Expense", hist="tax", proj_dsl="={pretax}*{tax_rate}", fy="sum", fmt="amount_s", gap=False),
        L(id="tax_rate", label="% Tax Rate", kind="pct", italic=True, fmt="pct_s", hist={"kind": "formula", "dsl": "={tax}/{pretax}"},
          proj_dsl="={drv:tax_rate}", annual_dsl="={drv:tax_rate}", fy="formula", fy_dsl="={tax}/{pretax}"),
        L(id="ni", label="Net Income", bold=True, top=True, dsl="={pretax}-{tax}", fy="sum", fmt="amount_s",
          subs=[{"key": "pct_of", "label": "% Net Margin", "dsl": "={id}/{total_rev}", "fmt": "pct_s", "italic": True}]),
        {"subtitle": "memo"},
        L(id="dep", label="Depreciation", hist="dep", proj_dsl="={drv:dep}", fy="sum", fmt="amount_s", gap=False),
        L(id="amort", label="Amortization", hist="amort", proj_dsl="=MIN({amort_pre},{Balance Sheet!intangibles@pq})", fy="sum", fmt="amount_s", gap=False),
        L(id="amort_pre", label="Amortization (Pre-Cap)", italic=True, hist={"kind": "blank"}, proj_dsl="={drv:amort}", fy="sum", fmt="amount_s", gap=False),
        L(id="ebitda", label="EBITDA", bold=True, top=True, dsl="={op_inc_is}+{dep}+{amort}", fy="sum", fmt="amount_s",
          subs=[{"key": "pct_of", "label": "% Margin", "dsl": "={id}/{total_rev}", "fmt": "pct_s", "italic": True}], gap=False),
        L(id="sbc", label="Stock-Based Compensation", hist="sbc", proj_dsl="={drv:sbc}", fy="sum", fmt="amount_s", gap=False),
        L(id="ebitda_ex", label="EBITDA ex. SBC", bold=True, top=True, dsl="={ebitda}+{sbc}", fy="sum", fmt="amount_s",
          subs=[{"key": "pct_of", "label": "% Margin", "dsl": "={id}/{total_rev}", "fmt": "pct_s", "italic": True}]),
        {"subtitle": "Per Share data"},
        L(id="shares_basic", label="Basic Weighted Avg Shares", kind="shares", hist="shares_basic", proj_dsl="={drv:shares_basic}", fy="avg", gap=False),
        L(id="shares_dil", label="Diluted Weighted Avg Shares", kind="shares", hist="shares_dil", proj_dsl="={drv:shares_dil}", fy="avg", gap=False),
        L(id="eps_basic", label="Basic EPS", kind="eps", hist="eps_basic", proj_dsl="={ni}/{shares_basic}", fy="formula", gap=False),
        L(id="eps_dil", label="Diluted EPS", kind="eps", hist="eps_dil", proj_dsl="={ni}/{shares_dil}", fy="formula"),
    ]


def cfs_blocks() -> list:
    A = "amount_s"
    carry = lambda i: {"values": {"FY2029": "={" + i + "@py}", "FY2030": "={" + i + "@py}"}}
    def plug(i, label, bottom=False):
        return L(id=i, label=label, hist=i, fy="sum", fmt=A, gap=False, bottom=bottom,
                 values={**{p: 0 for p in ["3Q26", "4Q26", "1Q27", "2Q27", "3Q27", "4Q27", "1Q28", "2Q28", "3Q28", "4Q28"]},
                         "FY2029": "={" + i + "@py}", "FY2030": "={" + i + "@py}"}, input_fill=True, input_color=S.BLUE)
    return [
        {"section": "Cash Flow Statement", "marker": False},
        L(id="cf_ni", label="Net Income", bold=True, dsl="={Income Statement!ni}", fy="sum", fmt=A),
        L(id="cf_dep", label="(+) Depreciation", dsl="={Income Statement!dep}", fy="sum", fmt=A, gap=False),
        L(id="cf_amort", label="(+) Amortization", dsl="={Income Statement!amort}", fy="sum", fmt=A, gap=False),
        L(id="cf_sbc", label="(+) Stock-Based Compensation", dsl="={Income Statement!sbc}", fy="sum", fmt=A, gap=False),
        L(id="wc_recv", label="(+/-) Change in Trade Receivables & Other Assets", hist="wc_recv", fy="sum", fmt=A, gap=False,
          proj_dsl="=-(({Balance Sheet!receivables}-{Balance Sheet!receivables@pq})+({Balance Sheet!other_ca}-{Balance Sheet!other_ca@pq})+({Balance Sheet!restricted_other}-{Balance Sheet!restricted_other@pq})+({Balance Sheet!fin_lease_recv}-{Balance Sheet!fin_lease_recv@pq}))"),
        L(id="wc_pay", label="(+/-) Change in Trade & Other Liabilities", hist="wc_pay", fy="sum", fmt=A, gap=False,
          proj_dsl="=({Balance Sheet!payables}-{Balance Sheet!payables@pq})+({Balance Sheet!accrued}-{Balance Sheet!accrued@pq})+({Balance Sheet!accrued_nc}-{Balance Sheet!accrued_nc@pq})+({Balance Sheet!deriv_liab}-{Balance Sheet!deriv_liab@pq})"),
        L(id="wc_defrev", label="(+/-) Change in Deferred Revenue", hist="wc_defrev", fy="sum", fmt=A, gap=False,
          proj_dsl="=({Balance Sheet!deferred_rev}-{Balance Sheet!deferred_rev@pq})"),
        L(id="wc_prov", label="(+/-) Change in Provisions", hist="wc_prov", fy="sum", fmt=A, gap=False,
          proj_dsl="=({Balance Sheet!provisions}-{Balance Sheet!provisions@pq})+({Balance Sheet!provisions_nc}-{Balance Sheet!provisions_nc@pq})"),
        L(id="wc_tax", label="(+/-) Change in Taxes, Net", hist="wc_tax", fy="sum", fmt=A, gap=False,
          proj_dsl="=({Balance Sheet!tax_payable}-{Balance Sheet!tax_payable@pq})+({Balance Sheet!dtl}-{Balance Sheet!dtl@pq})-({Balance Sheet!tax_recv}-{Balance Sheet!tax_recv@pq})-({Balance Sheet!dta}-{Balance Sheet!dta@pq})"),
        plug("other_op", "(+/-) Other Operating Items (plug for actuals)", bottom=True),
        L(id="cfo", label="CFO", bold=True, top=True, dsl="=SUM({cf_ni}:{other_op})", fy="sum", fmt=A),
        L(id="capex", label="(-) Capital Expenditures", hist="capex", proj_dsl="={drv:capex}", fy="sum", fmt=A, gap=False),
        L(id="st_inv_chg", label="(+/-) Net (Purchases)/Sales of Short term Investments", hist="st_inv_chg", fy="sum", fmt=A, gap=False,
          proj_dsl="=-({Balance Sheet!st_inv}-{Balance Sheet!st_inv@pq})"),
        plug("other_inv", "(+/-) Other Investing", bottom=True),
        L(id="cfi", label="CFI", bold=True, top=True, dsl="=SUM({capex}:{other_inv})", fy="sum", fmt=A),
        L(id="fcf", label="FCF", bold=True, top=True, dsl="={cfo}+{capex}", fy="sum", fmt=A),
        L(id="opt_proceeds", label="(+) Option Proceeds", hist="opt_proceeds", proj_dsl="={drv:opt_proceeds}", fy="sum", fmt=A, gap=False),
        L(id="buybacks", label="(-) Share Repurchases", hist="buybacks", proj_dsl="={drv:buybacks}", fy="sum", fmt=A, gap=False),
        L(id="lease_principal", label="(-) Lease Principal Payments", hist="lease_principal", proj_dsl="={drv:lease_principal}", fy="sum", fmt=A, gap=False),
        L(id="rsu_tax", label="(-) RSU Tax Withholding", hist="rsu_tax", proj_dsl="={drv:rsu_tax}", fy="sum", fmt=A, gap=False),
        plug("notes_debt", "(+/-) Exchangeable Notes/Debt"),
        plug("other_fin", "(+/-) Other Financing", bottom=True),
        L(id="cff", label="CFF", bold=True, top=True, dsl="=SUM({opt_proceeds}:{other_fin})", fy="sum", fmt=A, gap=False),
        plug("fx", "(+/-) FX Effect on Cash"),
        {"blank": 1},
        L(id="net_change", label="Net Change in Cash", bold=True, top=True, dsl="={cfo}+{cfi}+{cff}+{fx}", fy="sum", fmt=A, gap=False),
        L(id="beg_cash", label="Beginning Cash", hist={"kind": "formula", "dsl": "={end_cash@pq}"}, proj_dsl="={end_cash@pq}", annual_dsl="={end_cash@py}",
          fy="first", fmt=A, values={"1Q23": "={data:beg_cash}"}),
        L(id="end_cash", label="Ending Cash", bold=True, top=True, dsl="={net_change}+{beg_cash}", fy="formula", fmt=A),
        L(id="cash_check", label="check", bold=True, dsl="={end_cash}-{Balance Sheet!cash}", fy="formula", fmt=A),
    ]


def bs_blocks() -> list:
    A = "amount_s"
    def flat(i, label, gap=False):
        return L(id=i, label=label, hist=i, proj_dsl="={" + i + "@pq}", fy="last", fmt=A, gap=gap)
    def plug(i, label, gap=False):
        return L(id=i, label=label, hist=i, fy="last", fmt=A, gap=gap, input_fill=True, input_color=S.BLUE,
                 values={**{p: 0 for p in ["3Q26", "4Q26", "1Q27", "2Q27", "3Q27", "4Q27", "1Q28", "2Q28", "3Q28", "4Q28"]},
                         "FY2029": "={" + i + "@py}", "FY2030": "={" + i + "@py}"})
    wk = "*13/{weeks}"
    return [
        {"section": "Balance Sheet", "marker": False},
        {"subtitle": "Current Assets"},
        L(id="cash", label="Cash & Cash Equivalents", hist="cash", proj_dsl="={Cash Flow Statement!end_cash}", fy="last", fmt=A, gap=False),
        L(id="st_inv", label="Short-Term Investments", hist="st_inv", proj_dsl="={drv:st_inv}", fy="last", fmt=A, gap=False),
        L(id="receivables", label="Trade & Other Receivables", hist="receivables", proj_dsl="={drv:recv_pct}*{Income Statement!total_rev}" + wk, fy="last", fmt=A, gap=False),
        flat("tax_recv", "Income Tax Receivable"),
        L(id="other_ca", label="Other Current Assets", hist="other_ca", proj_dsl="={drv:other_ca_pct}*{Income Statement!total_rev}" + wk, fy="last", fmt=A, gap=False),
        L(id="total_ca", label="Total Current Assets", bold=True, top=True, dsl="=SUM({cash}:{other_ca})", fy="formula", fmt=A),
        {"label": "Non-Current Assets"},
        L(id="rou", label="Lease Right-of-Use Assets", hist="rou", proj_dsl="={rou@pq}-{Income Statement!dep}*{drv:rou_share}+{new_leases}", fy="last", fmt=A, gap=False),
        L(id="ppe", label="Property & Equipment", hist="ppe", proj_dsl="={ppe@pq}-{Cash Flow Statement!capex}-{Income Statement!dep}*(1-{drv:rou_share})", fy="last", fmt=A, gap=False),
        flat("goodwill", "Goodwill"),
        L(id="intangibles", label="Intangible Assets", hist="intangibles", proj_dsl="={intangibles@pq}-{Income Statement!amort}", fy="last", fmt=A, gap=False),
        flat("lt_inv", "Long-Term Investments"),
        flat("restricted_other", "Restricted Cash & Other Non-Current Assets"),
        flat("fin_lease_recv", "Finance Lease Receivables"),
        flat("dta", "DTAs"),
        L(id="total_nca", label="Total Non-Current Assets", bold=True, top=True, dsl="=SUM({rou}:{dta})", fy="formula", fmt=A),
        L(id="total_assets", label="Total Assets", bold=True, top=True, dsl="={total_ca}+{total_nca}", fy="formula", fmt=A),
        {"label": "Current Liabilities"},
        L(id="payables", label="Trade & Other Payables", hist="payables", proj_dsl="={drv:pay_pct}*({Income Statement!cogs}+{Income Statement!total_opex_is})" + wk, fy="last", fmt=A, gap=False),
        L(id="tax_payable", label="Income Tax Payable", hist="tax_payable", proj_dsl="={drv:tax_payable}", fy="last", fmt=A, gap=False),
        L(id="deferred_rev", label="Deferred Revenue", hist="deferred_rev", proj_dsl="={drv:defrev_pct}*{Income Statement!total_rev}" + wk, fy="last", fmt=A, gap=False),
        L(id="accrued", label="Accrued Expenses & Other Liabilities", hist="accrued", proj_dsl="={drv:accrued_pct}*{Income Statement!cogs}" + wk, fy="last", fmt=A, gap=False),
        plug("exch_notes_cur", "Exchangeable Notes"),
        flat("provisions", "Provisions"),
        flat("deriv_liab", "Derivative Liabilities"),
        L(id="total_cl", label="Total Current Liabilities", bold=True, top=True, dsl="=SUM({payables}:{deriv_liab})", fy="formula", fmt=A),
        {"label": "Non-Current Liabilities"},
        L(id="lease_liab", label="Lease Liabilities", hist="lease_liab", proj_dsl="={lease_liab@pq}+{Cash Flow Statement!lease_principal}+{new_leases}", fy="last", fmt=A, gap=False),
        flat("accrued_nc", "Accrued Expenses & Other (non-current)"),
        flat("provisions_nc", "Provisions (Non-Current)"),
        flat("dtl", "DTLs"),
        plug("exch_notes_nc", "Exchangeable Notes (Non-Current)"),
        L(id="total_ncl", label="Total Non-Current Liabilities", bold=True, top=True, dsl="=SUM({lease_liab}:{exch_notes_nc})", fy="formula", fmt=A),
        L(id="total_liab", label="Total Liabilities", bold=True, top=True, dsl="={total_cl}+{total_ncl}", fy="formula", fmt=A),
        {"subtitle": "Shareholders Equity"},
        L(id="paid_in", label="Other Paid-In Capital", hist="paid_in", proj_dsl="={paid_in@pq}+{Cash Flow Statement!opt_proceeds}", fy="last", fmt=A, gap=False),
        L(id="treasury", label="Treasury Shares", hist="treasury", proj_dsl="={treasury@pq}+{Cash Flow Statement!buybacks}", fy="last", fmt=A, gap=False),
        L(id="other_reserves", label="Other Reserves", hist="other_reserves", proj_dsl="={other_reserves@pq}+{Income Statement!sbc}+{Cash Flow Statement!rsu_tax}", fy="last", fmt=A, gap=False),
        L(id="retained", label="Retained Earnings", hist="retained", proj_dsl="={retained@pq}+{Income Statement!ni}", fy="last", fmt=A, gap=False),
        L(id="total_equity", label="Total Equity", bold=True, top=True, dsl="=SUM({paid_in}:{retained})", fy="formula", fmt=A),
        L(id="total_le", label="Total Liabilities & Equity", bold=True, top=True, dsl="={total_liab}+{total_equity}", fy="formula", fmt=A),
        L(id="bs_check", label="check", bold=True, dsl="={total_assets}-{total_le}", fy="formula", fmt=A),
        {"subtitle": "memo"},
        L(id="new_leases", label="new non-cash leases", hist={"kind": "blank"}, proj_dsl="={Income Statement!dep}*{drv:rou_share}", fy="sum", fmt=A),
    ]


def build_spec(wf, wv, data, drivers) -> dict:
    ts = wf["Tearsheet"]
    tv = wv["Tearsheet"]
    dcf = wf["DCF"]
    mult = lambda c: tv[c].value
    cases = ["Disaster", "Bear", "Base", "Bull", "Blowout"]
    multiples = {"Base": {"YE2027": mult("E56"), "YE2028": mult("E57")}, "Bull": {"YE2027": mult("E59"), "YE2028": mult("E60")},
                 "Bear": {"YE2027": mult("E62"), "YE2028": mult("E63")}, "Blowout": {"YE2027": mult("E65"), "YE2028": mult("E66")},
                 "Disaster": {"YE2027": mult("E68"), "YE2028": mult("E69")}}
    metric = {"Base": {"YE2027": ts["E5"].value, "YE2028": ts["J5"].value}, "Bull": {"YE2027": ts["E12"].value, "YE2028": ts["J12"].value},
              "Bear": {"YE2027": ts["E19"].value, "YE2028": ts["J19"].value}, "Blowout": {"YE2027": ts["E26"].value, "YE2028": ts["J26"].value},
              "Disaster": {"YE2027": ts["E33"].value, "YE2028": ts["J33"].value}}
    exit_m = {"Disaster": dcf["G50"].value, "Bear": dcf["G51"].value, "Base": dcf["G52"].value, "Bull": dcf["G53"].value, "Blowout": dcf["G54"].value}
    cons = consensus_items(data["_consensus"])
    return {
        "company": {"name": "Spotify Technology S.A.", "ticker": "SPOT", "exchange": "NYSE", "reporting_currency": "EUR",
                    "trading_currency": "USD", "fx_rate": dcf["D65"].value, "units": "mm", "fiscal_year_end_month": 12,
                    "fiscal_year_end_day": 31, "author": "Palazzolo, Justin J", "cover_tab": "Cover"},
        "horizon": {"first_hist_quarter": "1Q23", "last_actual_quarter": "2Q26", "last_quarterly_estimate": "4Q28",
                    "annual_only_years": [2029, 2030],
                    "report_dates": {pid: wf[REV][f"{col}10"].value.date().isoformat() for col, pid in zip(HIST_COLS, HIST_PIDS)
                                     if isinstance(wf[REV][f"{col}10"].value, dt.datetime)}},
        "cases": cases, "active_case": "Base",
        "sheets": {REV: {"blocks": revenue_blocks(cons)}, MARGIN: {"blocks": margin_blocks(cons)},
                   IS: {"blocks": is_blocks()}, CFS: {"blocks": cfs_blocks()}, BS: {"blocks": bs_blocks()}},
        "drivers": drivers,
        "dcf": {"opex_lines": [["is_rd", "R&D"], ["is_sm", "S&M"], ["is_ga", "G&A"]], "da_lines": ["dep", "amort"],
                "nwc_lines": ["wc_recv", "wc_pay", "wc_defrev", "wc_prov"], "capex_line": "capex",
                "valuation_date": dcf["D40"].value.date().isoformat(), "tax_rate": dcf["D41"].value, "rfr": dcf["D42"].value,
                "beta": dcf["D43"].value, "erp": dcf["D44"].value, "kd_after_tax": dcf["D46"].value, "equity_weight": dcf["D47"].value,
                "exit_multiples": exit_m, "diluted_shares": dcf["D67"].value,
                "bridge": {"cash_lines": ["cash", "st_inv", "lt_inv", "fin_lease_recv"], "debt_lines": ["lease_liab"],
                           "debt_label": "(-) Lease Liabilities",
                           "other_adjustments": [{"label": "(-) Current Lease Liabilities", "value": -62}]}},
        "tearsheet": {"metric_label": "Adj. EBITDA", "metric_line": "ebitda", "multiple_label": "NTM Multiple",
                      "blocks": [{"label": "YE2027", "target_date": "2027-12-31", "metric_period": "FY2028", "blended_label": "Near Term Setup"},
                                 {"label": "YE2028", "target_date": "2028-12-31", "metric_period": "FY2029"}],
                      "multiples": multiples, "case_metric_values": metric,
                      "weights": {"Blowout": 0.1, "Bull": 0.2, "Base": 0.4, "Bear": 0.2, "Disaster": 0.1},
                      "current_multiple_period": "FY2027",
                      "price": {"source": "hardcode", "value": dcf["D69"].value, "date": "2026-10-01"}},
        "side_builds": [extract_side_build(wf, "ARPU Bridge"), extract_side_build(wf, "Margin Bridge")],
    }


def compare(template: str, rebuilt: str) -> list:
    wt = load_workbook(template, data_only=True)
    wr = load_workbook(rebuilt, data_only=True)
    checks = [(REV, "Total Revenue", ["U", "W", "AB", "AG", "AH", "AI"]), (REV, "Premium Revenue", ["U", "AB", "AI"]),
              (REV, "Ad-Supported Revenue", ["U", "AB", "AI"]), (MARGIN, "Total Gross Profit", ["U", "AB", "AI"]),
              (MARGIN, "Operating Income", ["U", "AB", "AI"]), (IS, "EBITDA", ["W", "AB", "AG", "AH", "AI"]),
              (IS, "Net Income", ["W", "AB", "AG", "AI"]), (IS, "Diluted EPS", ["W", "AB", "AG", "AI"]),
              (BS, "Total Assets", ["U", "AB", "AI"]), (CFS, "FCF", ["W", "AB", "AI"]), (BS, "check", ["U", "AB", "AI"]),
              (CFS, "check", ["U", "AB", "AI"])]
    out = []
    for sheet, label, cols in checks:
        rt = _find_row(wt[sheet], label)
        rr = _find_row(wr[sheet], label)
        for col in cols:
            a = wt[sheet][f"{col}{rt}"].value if rt else None
            b = wr[sheet][f"{col}{rr}"].value if rr else None
            out.append((sheet, label, col, a, b))
    for sheet, cells in [("DCF", {"Implied Share Price": "D68"}), ("Tearsheet", {"Base PT YE27": "E7", "Blended YE27": "Q10", "Base PT YE28": "J7"})]:
        for name, c in cells.items():
            a = wt[sheet][c].value
            rrow = None
            if sheet == "DCF":
                rrow = _find_row(wr["DCF"], "Implied Share Price (USD)")
                b = wr["DCF"][f"D{rrow}"].value if rrow else None
            else:
                b = wr[sheet][c].value
            out.append((sheet, name, c, a, b))
    return out


def _find_row(ws, label):
    for r in range(1, ws.max_row + 1):
        v = ws[f"B{r}"].value
        if isinstance(v, str) and v.strip() == label.strip():
            return r
    return None


def main():
    template, out_dir = sys.argv[1], Path(sys.argv[2])
    out_dir.mkdir(parents=True, exist_ok=True)
    wf = load_workbook(template)
    wv = load_workbook(template, data_only=True)
    data = extract_data(wf, wv)
    drivers = extract_drivers(wf)
    spec = build_spec(wf, wv, data, drivers)
    (out_dir / "spot_spec.json").write_text(json.dumps(spec, indent=1, default=str), encoding="utf-8")
    (out_dir / "spot_data.json").write_text(json.dumps(data, indent=1, default=str), encoding="utf-8")
    series = {k: v for k, v in data.items() if not k.startswith("_")}
    out = out_dir / "spot_rebuild.xlsx"
    build(spec, series, str(out))
    print("built", out)
    rep = verify(str(out), recalc=True)
    print(json.dumps({k: rep[k] for k in rep if k != "static"}, indent=1, default=str)[:4000])
    print("static issues:", rep["static"]["issues"][:10], "| fingerprints:", rep["static"]["fingerprints"][:5],
          "| colour:", rep["static"]["colour_violations"][:5])
    print("\nTEMPLATE vs REBUILD")
    for sheet, label, col, a, b in compare(template, str(out)):
        diff = None
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            diff = round((b - a) / a * 100, 2) if a else round(b - a, 4)
        print(f"  {sheet:20s} {label:28s} {col:3s} template={a!s:>20} rebuilt={b!s:>20} diff%={diff}")


if __name__ == "__main__":
    main()
