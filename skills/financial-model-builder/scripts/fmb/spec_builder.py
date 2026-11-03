"""Turn the analyst's inputs (from the inputs workbook) plus parsed data into an
engine spec. This is where driver *types* become formulas.

Driver types (column "Type" of the Drivers tab) and what they do to the line they drive:
  yoy_pct      level = prior-year level x (1 + driver); the "% yoy" variance row links the driver
  qoq_pct      level = prior-quarter level x (1 + driver); annual-only years use the driver as y/y
  net_adds     level = prior-period level + driver (absolute adds)
  bps_qoq      percentage line = prior quarter + driver/10000 (annual-only years: prior year + driver/10000)
  bps_yoy      percentage line = prior year + driver/10000
  pct_level    the line IS the driver (a margin %, a mix %, an uptake %)
  pct_of_base  line = base line x driver (e.g. R&D = revenue x %)
  gm_pct       cost line = revenue line x (1 - driver)   (gross-margin style)
  cost_per_unit  cost line = volume line x driver x months
  absolute     line = driver (a level typed directly)
  flat         line = prior period (no driver needed)
  single       one typed constant (a price point) referenced by custom formulas
  custom       the "Represented on build as" text is an engine formula
Revenue-tree kinds: sum, volume_price (per month or per period), growth, share, direct, kpi, custom.
"""
from __future__ import annotations

import re
from typing import Dict, List, Optional, Tuple

from . import canon
from . import styles as S
from .engine import BS, CFS, IS, MARGIN, REV
from .parse_data import _norm, series
from .periods import PeriodAxis, parse_pid, pid_of

AMT_SUBS = ["pct_yoy", "pct_2y", "usd_yoy", "pct_qoq", "usd_qoq"]
COUNT_SUBS = ["net_adds_yoy", "pct_yoy", "net_adds_qoq", "pct_qoq"]
PCT_SUBS = ["bps_yoy", "bps_2y", "bps_qoq"]
SUB_KEYS = {"% yoy": "pct_yoy", "% 2y stack": "pct_2y", "$ yoy": "usd_yoy", "% qoq": "pct_qoq", "$ qoq": "usd_qoq",
            "% total": "pct_total", "bps yoy": "bps_yoy", "bps 2y": "bps_2y", "bps qoq": "bps_qoq",
            "yoy net adds": "net_adds_yoy", "qoq net adds": "net_adds_qoq"}


def L(**k):
    return {"line": k}


def yn(v) -> bool:
    return str(v).strip().lower() in ("y", "yes", "true", "1", "x")


def clean_id(s: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "_", str(s).strip().lower()).strip("_")
    return s or "line"


# ----------------------------------------------------------------------------- data access
class DataView:
    """Lookup helper over the normalised data with period id translation."""

    def __init__(self, data: dict, kpi_history: Optional[dict] = None):
        self.data = data
        self.kpi = kpi_history or {}

    def series(self, label: Optional[str], section: Optional[str] = None, exclude: Optional[List[str]] = None) -> Dict[str, float]:
        if not label:
            return {}
        if label in self.kpi:
            return dict(self.kpi[label])
        return series(self.data, label, section or None, exclude_sections=exclude)

    def first_match(self, synonyms: List[str], section: Optional[str] = None, exclude: Optional[List[str]] = None) -> Tuple[Optional[str], Dict[str, float]]:
        for syn in synonyms:
            s = self.series(syn, section, exclude)
            if s:
                return syn, s
        return None, {}


# sections of a Bloomberg printout that must never feed a given statement
EXCLUDE = {
    "is": ["cash from", "changes in working capital", "condensed cash flow", "condensed balance sheet", "assets", "liabilities & equity"],
    "bs": ["cash from", "changes in working capital", "condensed cash flow", "company specific adjustments", "special company reference"],
    "cf": ["highlights", "income statement", "gaap results", "condensed balance sheet", "assets", "liabilities & equity", "segment revenue", "business breakdown"],
    "memo": [],
}


def hist_only(s: Dict[str, float], axis: PeriodAxis) -> Dict[str, float]:
    """Keep actual quarters of the model axis (FY totals are rebuilt from quarters)."""
    out = {}
    for pid, v in s.items():
        p = axis.by_id.get(pid)
        if p is not None and p.kind == "Q" and not p.estimate:
            out[pid] = v
    return out


# ----------------------------------------------------------------------------- revenue / cost trees
def driver_for(drivers: List[dict], target: str) -> Optional[dict]:
    for d in drivers:
        if d.get("target") == target:
            return d
    return None


def level_line(node: dict, d: Optional[dict], kind_fmt: str, hist_key: Optional[str], subs: List, extra: dict) -> dict:
    """A KPI or revenue level line driven by driver d (may be None)."""
    lid = node["id"]
    extra = dict(extra)
    bold = extra.pop("bold", True)
    line = dict(id=lid, label=node["label"], kind=kind_fmt, bold=bold, subs=subs, **extra)
    if hist_key:
        line["hist"] = hist_key
    dtype = (d or {}).get("type") or "flat"
    did = (d or {}).get("id")
    if not did and dtype not in ("flat", "custom"):
        dtype = "flat"   # no driver defined for this line: carry it forward
    if dtype == "yoy_pct":
        line["proj_dsl"] = "={" + lid + "@py}*(1+{" + lid + ".pct_yoy})"
        line["driver"] = {"id": did, "sub": "pct_yoy"}
        if "pct_yoy" not in subs:
            subs.insert(0, "pct_yoy")
    elif dtype == "qoq_pct":
        line["proj_dsl"] = "={" + lid + "@pq}*(1+{" + lid + ".pct_qoq})"
        line["annual_dsl"] = "={" + lid + "@py}*(1+{drv:" + did + "})"
        line["driver"] = {"id": did, "sub": "pct_qoq"}
        if "pct_qoq" not in subs:
            subs.append("pct_qoq")
    elif dtype == "net_adds":
        line["proj_dsl"] = "={" + lid + "@pq}+{" + lid + ".net_adds_qoq}"
        line["annual_dsl"] = "={" + lid + "@py}+{drv:" + did + "}"
        line["driver"] = {"id": did, "sub": "net_adds_qoq"}
        if "net_adds_qoq" not in subs:
            subs.append("net_adds_qoq")
    elif dtype == "bps_qoq":
        line["proj_dsl"] = "={" + lid + "@pq}+{" + lid + ".bps_qoq}/10000"
        line["annual_dsl"] = "={" + lid + "@py}+{" + lid + ".bps_qoq}/10000"
        line["driver"] = {"id": did, "sub": "bps_qoq"}
        if "bps_qoq" not in subs:
            subs.append("bps_qoq")
    elif dtype == "bps_yoy":
        line["proj_dsl"] = "={" + lid + "@py}+{" + lid + ".bps_yoy}/10000"
        line["driver"] = {"id": did, "sub": "bps_yoy"}
        if "bps_yoy" not in subs:
            subs.insert(0, "bps_yoy")
    elif dtype == "pct_level":
        line["proj_dsl"] = "={drv:" + did + "}"
        line["annual_dsl"] = "={drv:" + did + "}"
    elif dtype == "absolute":
        line["proj_dsl"] = "={drv:" + did + "}"
        line["annual_dsl"] = "={drv:" + did + "}"
    elif dtype == "custom" and d and d.get("formula"):
        line["proj_dsl"] = d["formula"] if d["formula"].startswith("=") else "=" + d["formula"]
    else:  # flat
        line["proj_dsl"] = "={" + lid + "@pq}"
        line["annual_dsl"] = "={" + lid + "@py}"
    line["subs"] = subs
    return line


def build_revenue_blocks(tree: List[dict], drivers: List[dict], dv: DataView, axis: PeriodAxis, variance: dict,
                         deltas: List[dict]) -> Tuple[List[dict], Dict[str, dict]]:
    """Revenue Build blocks from the revenue tree rows."""
    nodes = {clean_id(r["id"]): dict(r, id=clean_id(r["id"])) for r in tree if r.get("id")}
    for n in nodes.values():
        n["parent"] = clean_id(n["parent"]) if n.get("parent") else None
        n["kind"] = (n.get("kind") or "sum").strip().lower().replace(" ", "_")
    children: Dict[Optional[str], List[str]] = {}
    for nid, n in nodes.items():
        children.setdefault(n["parent"], []).append(nid)
    roots = children.get(None, [])
    blocks: List[dict] = [{"section": "Revenue Build"}]
    total_id = "total_rev"
    # Totals block
    top = [r for r in roots if nodes[r]["kind"] != "kpi"]
    blocks.append({"subtitle": "Totals:", "marker": True})
    blocks.append(L(id=total_id, label="Total Revenue", bold=True, dsl="=" + "+".join("{" + r + "}" for r in top) if top else "=0",
                    fy="sum", subs=sub_list(variance, total_id, AMT_SUBS)))
    line_index: Dict[str, dict] = {}

    def emit(nid: str, depth: int):
        n = nodes[nid]
        kids = children.get(nid, [])
        kind = n["kind"]
        d = driver_for(drivers, nid)
        hist_label = n.get("data_label")
        hist = hist_only(dv.series(hist_label, n.get("data_section")), axis) if hist_label else {}
        data_key = nid if hist else None
        if hist:
            DATA[nid] = hist
        if depth == 0 and kind != "kpi":
            blocks.append({"band": n["label"].rstrip(":") + ":"})
        rev_kids = [k for k in kids if nodes[k]["kind"] != "kpi"]
        subs = sub_list(variance, nid, AMT_SUBS + (["pct_total"] if depth == 0 else []))
        if kind == "sum" and rev_kids:
            line = dict(id=nid, label=n["label"], bold=True, dsl="=" + "+".join("{" + k + "}" for k in rev_kids), fy="sum", subs=subs)
            if data_key:
                line["hist"] = data_key
                line["proj_dsl"] = line.pop("dsl")
        elif kind == "volume_price":
            vol, price = clean_id(n.get("volume_id") or ""), clean_id(n.get("price_id") or "")
            per_month = str(n.get("price_basis") or "per month").lower().startswith("per m")
            line = dict(id=nid, label=n["label"], bold=True, hist=data_key, fy="sum", subs=subs,
                        proj_dsl="={" + vol + "}*{" + price + "}" + ("*{months}" if per_month else ""))
            if not data_key:
                line["dsl"] = line.pop("proj_dsl")
        elif kind == "growth":
            line = level_line(n, d or {"type": "yoy_pct", "id": f"{nid}_g"}, "amount", data_key, subs, {"fy": "sum"})
        elif kind == "share":
            parent = n["parent"] or total_id
            line = dict(id=nid, label=n["label"], bold=True, hist=data_key, fy="sum", subs=subs,
                        proj_dsl="={" + parent + "}*{" + nid + ".pct_total}")
            line["sub_labels"] = {"pct_total": "% of " + nodes[parent]["label"] if parent in nodes else "% total"}
            line["subs"] = [s for s in subs if s != "pct_total"] + ["pct_total"]
            line["total"] = parent
            line["driver"] = {"id": (d or {}).get("id"), "sub": "pct_total"}
        elif kind == "direct":
            line = level_line(n, d or {"type": "absolute", "id": f"{nid}_lvl"}, "amount", data_key, subs, {"fy": "sum"})
        elif kind == "custom":
            line = dict(id=nid, label=n["label"], bold=True, hist=data_key, fy="sum", subs=subs,
                        proj_dsl=(n.get("formula") or "=0"))
        elif kind == "kpi":
            kfmt = (n.get("format") or "count").strip().lower()
            kind_fmt = {"count": "count", "price": "price", "%": "pct", "pct": "pct", "amount": "amount"}.get(kfmt, "count")
            default_subs = COUNT_SUBS if kind_fmt == "count" else (PCT_SUBS if kind_fmt == "pct" else AMT_SUBS)
            fy_rule = {"count": "avg", "price": "avg", "pct": "last", "amount": "sum"}[kind_fmt]
            if n.get("fy_rule"):
                fy_rule = str(n["fy_rule"]).lower()
            hist_dsl = n.get("hist_formula")
            extra = {"fy": fy_rule, "italic": kind_fmt == "pct", "bold": kind_fmt != "pct"}
            if hist_dsl:
                extra["hist"] = {"kind": "formula", "dsl": hist_dsl if hist_dsl.startswith("=") else "=" + hist_dsl}
                if fy_rule == "formula":
                    extra["fy_dsl"] = extra["hist"]["dsl"]
            line = level_line(n, d, kind_fmt, data_key if not hist_dsl else None, sub_list(variance, nid, default_subs), extra)
            line["bold"] = kind_fmt != "pct"
        else:
            line = dict(id=nid, label=n["label"], bold=True, hist=data_key, fy="sum", subs=subs, proj_dsl="={" + nid + "@pq}")
        if n.get("sub_labels"):
            line["sub_labels"] = n["sub_labels"]
        line_index[nid] = line
        blocks.append({"line": line})
        for k in kids:
            emit(k, depth + 1)

    for r in roots:
        emit(r, 0)
    if deltas:
        blocks.append({"blank": 1})
        blocks.append({"deltas": deltas})
    return blocks, line_index


def sub_list(variance: dict, lid: str, default: List[str]) -> List:
    cfg = variance.get(lid)
    if not cfg:
        return list(default)
    out = []
    for key in ["pct_yoy", "pct_2y", "usd_yoy", "pct_qoq", "usd_qoq", "pct_total", "bps_yoy", "bps_2y", "bps_qoq", "net_adds_yoy", "net_adds_qoq"]:
        if cfg.get(key):
            out.append(key)
    return out or list(default)


DATA: Dict[str, Dict[str, float]] = {}


def build_cost_blocks(cost_rows: List[dict], drivers: List[dict], dv: DataView, axis: PeriodAxis, rev_index: Dict[str, dict],
                      variance: dict, deltas: List[dict], incremental: bool, sbc_by_function: bool) -> Tuple[List[dict], dict]:
    """Margin Build blocks: revenue links, COGS by segment, opex lines, operating income."""
    blocks: List[dict] = [{"section": "Revenue", "marker": False}]
    seg_rev_ids = [lid for lid, ln in rev_index.items() if ln.get("kind", "amount") == "amount" and lid in top_level_ids(rev_index)]
    for lid in seg_rev_ids:
        blocks.append(L(id="m_" + lid, label=rev_index[lid]["label"], bold=True, dsl="={" + REV + "!" + lid + "}", fy="sum", subs=["pct_yoy"]))
    blocks.append(L(id="m_total_rev", label="Total Revenue", bold=True, dsl="={" + REV + "!total_rev}", fy="sum", subs=["pct_yoy"]))
    rows = [dict(r, id=clean_id(r["id"])) for r in cost_rows if r.get("id")]
    cogs_rows = [r for r in rows if str(r.get("section", "")).lower().startswith("cogs")]
    opex_rows = [r for r in rows if str(r.get("section", "")).lower().startswith("opex")]
    other_rows = [r for r in rows if r not in cogs_rows and r not in opex_rows]
    info = {"cogs_ids": [], "opex_ids": [], "opex_labels": {}, "sbc_split": []}

    def cost_line(r: dict, base_id: str, subs_base_label: str) -> dict:
        lid = r["id"]
        d = driver_for(drivers, lid)
        dtype = (d or {}).get("type") or "pct_of_base"
        did = (d or {}).get("id")
        if not did and dtype != "custom":
            dtype = "flat"   # no driver defined: carry the line forward
        hist = hist_only(dv.series(r.get("data_label"), r.get("data_section")), axis)
        if hist:
            DATA[lid] = hist
        line = dict(id=lid, label=r["label"], bold=True, fy="sum", hist=lid if hist else None,
                    subs=[{"key": "pct_of", "label": f"% of {subs_base_label}", "dsl": "={id}/{" + base_id + "}", "fmt": "pct", "italic": True}]
                         + sub_list(variance, lid, ["pct_yoy", "usd_yoy", "pct_qoq", "usd_qoq"]))
        if dtype == "gm_pct":
            line["proj_dsl"] = "={" + base_id + "}*(1-{drv:" + did + "})"
        elif dtype == "pct_of_base":
            line["proj_dsl"] = "={" + base_id + "}*{drv:" + did + "}"
        elif dtype == "cost_per_unit":
            vol = clean_id(r.get("volume_id") or "")
            line["proj_dsl"] = "={" + REV + "!" + vol + "}*{drv:" + did + "}*{months}"
        elif dtype == "absolute":
            line["proj_dsl"] = "={drv:" + did + "}"
        elif dtype == "yoy_pct":
            line["proj_dsl"] = "={" + lid + "@py}*(1+{" + lid + ".pct_yoy})"
            line["driver"] = {"id": did, "sub": "pct_yoy"}
        elif dtype == "custom" and d and d.get("formula"):
            line["proj_dsl"] = d["formula"] if d["formula"].startswith("=") else "=" + d["formula"]
        else:
            line["proj_dsl"] = "={" + lid + "@pq}"
        if not hist:
            line["dsl"] = line["proj_dsl"]
        return line

    # ---- cost of revenue
    blocks.append({"section": "Cost of Revenue", "marker": False})
    cogs_ids = [r["id"] for r in cogs_rows]
    info["cogs_ids"] = cogs_ids
    # reported total cost of revenue vs the sum of the modelled COGS lines -> plug line so history foots
    seg_hist = {}
    for r in cogs_rows:
        for pid, v in hist_only(dv.series(r.get("data_label"), r.get("data_section")), axis).items():
            seg_hist[pid] = seg_hist.get(pid, 0) + v
    total_cogs_hist = hist_only(dv.first_match(["Cost of Revenue", "Cost of Goods Sold", "Cost Of Goods Sold", "Cost of Sales", "Total Cost of Revenue"])[1], axis)
    other_cogs = {pid: round(tv - seg_hist[pid], 4) for pid, tv in total_cogs_hist.items() if pid in seg_hist and abs(tv - seg_hist[pid]) > 0.01}
    if other_cogs and cogs_ids:
        DATA["other_cogs"] = other_cogs
        cogs_ids = cogs_ids + ["other_cogs"]
        info["other_cogs"] = True
    if len(cogs_ids) > 1:
        blocks.append(L(id="total_cogs", label="Total COGS", bold=True, dsl="=" + "+".join("{" + c + "}" for c in cogs_ids), fy="sum",
                        subs=[{"key": "pct_of", "label": "% of Total Revenue", "dsl": "={id}/{m_total_rev}", "fmt": "pct", "italic": True}] + AMT_SUBS))
        blocks.append(L(id="total_gp", label="Total Gross Profit", bold=True, dsl="={m_total_rev}-{total_cogs}", fy="sum",
                        subs=[{"key": "pct_of", "label": "GM %", "dsl": "={id}/{m_total_rev}", "fmt": "pct", "italic": True}] + AMT_SUBS))
    for r in cogs_rows:
        seg = clean_id(r.get("segment") or "")
        base = "m_" + seg if seg and ("m_" + seg) in [b["line"]["id"] for b in blocks if "line" in b] else "m_total_rev"
        base_label = rev_index[seg]["label"] if seg in rev_index else "Total Revenue"
        if len(cogs_ids) > 1:
            blocks.append({"band": (rev_index[seg]["label"] if seg in rev_index else r["label"]) + ":"})
        blocks.append({"line": cost_line(r, base, base_label)})
        gp_id = r["id"].replace("cogs", "gp") if "cogs" in r["id"] else r["id"] + "_gp"
        if incremental:
            blocks.append(L(id=gp_id + "_chg", label=f"y/y $ change in {base_label.lower()} gross profit", italic=True, dsl="={" + gp_id + "}-{" + gp_id + "@py}", needs="py", fy="formula", gap=False))
            blocks.append(L(id=base + "_chg", label=f"y/y $ change in {base_label.lower()}", italic=True, dsl="={" + base + "}-{" + base + "@py}", needs="py", fy="formula", gap=False))
            blocks.append(L(id=r["id"] + "_inc", label=f"Incremental {base_label.lower()} COGS", italic=True, dsl="={" + r["id"] + "}-{" + r["id"] + "@py}", needs="py", fy="formula", gap=False))
            blocks.append(L(id=gp_id + "_inc_gm", label=f"Incremental {base_label} Gross Margin", kind="pct", bold=True, dsl="={" + gp_id + "_chg}/{" + base + "_chg}", needs="py", fy="formula",
                            subs=["bps_yoy", "bps_qoq"], sub_labels={"bps_yoy": "bps y/y", "bps_qoq": "bps q/q"}))
        blocks.append(L(id=gp_id, label=f"{base_label} Gross Profit" if len(cogs_ids) > 1 else "Gross Profit", bold=True, dsl="={" + base + "}-{" + r["id"] + "}", fy="sum",
                        subs=[{"key": "pct_of", "label": (f"{base_label} GM %" if len(cogs_ids) > 1 else "GM %"), "dsl": "={id}/{" + base + "}", "fmt": "pct", "italic": True}] + AMT_SUBS))
    if info.get("other_cogs"):
        blocks.append({"band": "Other:"})
        blocks.append(L(id="other_cogs", label="Other Cost of Revenue (amortization, other items)", bold=True, hist="other_cogs",
                        proj_dsl="={other_cogs@py}", annual_dsl="={other_cogs@py}", fy="sum",
                        subs=[{"key": "pct_of", "label": "% of Total Revenue", "dsl": "={id}/{m_total_rev}", "fmt": "pct", "italic": True}, "pct_yoy", "usd_yoy"]))
    if len(cogs_ids) == 1:
        blocks.insert(len(blocks) - 1, {"blank": 0})
        info["total_cogs"] = cogs_ids[0]
        info["total_gp"] = cogs_ids[0].replace("cogs", "gp") if "cogs" in cogs_ids[0] else cogs_ids[0] + "_gp"
    elif cogs_ids:
        info["total_cogs"], info["total_gp"] = "total_cogs", "total_gp"
    else:
        info["total_cogs"], info["total_gp"] = None, None
    # ---- operating expenses
    blocks.append({"section": "Operating Expenses", "marker": False})
    opex_ids = []
    for r in opex_rows:
        lid = r["id"]
        opex_ids.append(lid)
        info["opex_labels"][lid] = r["label"]
        blocks.append({"subtitle": r["label"] + ":"})
        line = cost_line(r, "m_total_rev", "Revenue")
        line["subs"] = [{"key": "pct_of", "label": "% of Revenue", "dsl": "={id}/{m_total_rev}", "fmt": "pct", "italic": True}] + sub_list(variance, lid, ["pct_yoy", "usd_yoy", "pct_qoq", "usd_qoq"])
        sbc_label = r.get("sbc_data_label")
        sbc_hist = hist_only(dv.series(sbc_label, r.get("data_section")), axis) if (sbc_by_function and sbc_label) else {}
        blocks.append({"line": line, "gap": not sbc_hist})
        if sbc_hist:
            DATA["sbc_" + lid] = sbc_hist
            info["sbc_split"].append(lid)
            blocks.append(L(id="sbc_" + lid, label=f"SBC - {r['label']}", hist="sbc_" + lid, proj_dsl="={total_sbc}*{sbc_" + lid + "@py}/{total_sbc@py}", fy="sum", gap=False))
            blocks.append(L(id=lid + "_ex", label=f"{r['label']} ex-SBC", dsl="={" + lid + "}-{sbc_" + lid + "}", fy="sum",
                            subs=[{"key": "pct_of", "label": "ex-SBC % of Revenue", "dsl": "={id}/{m_total_rev}", "fmt": "pct", "italic": True},
                                  {"key": "pct_yoy", "label": "ex-SBC % yoy", "dsl": "={id}/{id@py}-1", "fmt": "pct", "italic": True, "needs": "py"},
                                  {"key": "usd_yoy", "label": "ex-SBC $ yoy", "dsl": "={id}-{id@py}", "fmt": "amount", "needs": "py"}]))
    # operating items reported but not modelled (restructuring, legal, impairments): plug so operating income foots
    oi_hist_pre = hist_only(dv.first_match(["Operating Income", "Operating Income (Loss)"], "GAAP Results")[1] or dv.first_match(["Operating Income"])[1], axis)
    rev_hist = hist_only(dv.first_match(["Revenue", "Total Revenue", "Total Revenues"])[1], axis)
    other_opex = {}
    if oi_hist_pre and total_cogs_hist and rev_hist:
        for pid, oi in oi_hist_pre.items():
            if pid not in rev_hist or pid not in total_cogs_hist:
                continue
            opex_sum = sum(DATA.get(o, {}).get(pid, 0) for o in opex_ids)
            plug = round(rev_hist[pid] - total_cogs_hist[pid] - opex_sum - oi, 4)
            if abs(plug) > 0.01:
                other_opex[pid] = plug
    if other_opex and opex_ids:
        DATA["other_opex"] = other_opex
        est_q = [p.pid for p in axis.quarters() if p.estimate]
        annual = [p.pid for p in axis.periods if p.annual_only]
        blocks.append({"subtitle": "Other Operating Items:"})
        blocks.append(L(id="other_opex", label="Other Operating Expenses (plug for actuals)", bold=True, hist="other_opex",
                        values={**{q: 0 for q in est_q}, **{a: "={other_opex@py}" for a in annual}}, input_fill=True, input_color=S.BLUE, fy="sum",
                        subs=[{"key": "pct_of", "label": "% of Revenue", "dsl": "={id}/{m_total_rev}", "fmt": "pct", "italic": True}]))
        opex_ids = opex_ids + ["other_opex"]
        info["other_opex"] = True
    info["opex_ids"] = opex_ids
    inc = {"key": "inc_ratio", "label": "Incremental Opex/Incremental Revenue (y/y)", "dsl": "=({id}-{id@py})/({m_total_rev}-{m_total_rev@py})", "fmt": "pct", "italic": True, "needs": "py"}
    if opex_ids:
        blocks.append(L(id="total_opex", label="Total Opex", bold=True, dsl="=" + "+".join("{" + o + "}" for o in opex_ids), fy="sum",
                        subs=[{"key": "pct_of", "label": "% of Revenue", "dsl": "={id}/{m_total_rev}", "fmt": "pct", "italic": True}, "pct_yoy", "usd_yoy", "pct_qoq", "usd_qoq", inc], gap=False))
        if info["sbc_split"]:
            blocks.append(L(id="total_opex_ex", label="Total Opex ex-SBC", bold=True, dsl="=" + "+".join("{" + o + "_ex}" for o in info["sbc_split"]) + "".join("+{" + o + "}" for o in opex_ids if o not in info["sbc_split"]),
                            fy="sum", subs=["pct_yoy", "usd_yoy", dict(inc, label="Incremental Opex ex-SBC/Incremental Revenue (y/y)")], gap=False))
    sbc_hist = hist_only(dv.first_match(["Stock-Based Compensation", "Stock Based Compensation"])[1], axis)
    if sbc_hist:
        DATA["total_sbc"] = sbc_hist
    subs_sbc = ([{"key": "cor", "label": "SBC - Cost of Revenue (implied)", "dsl": "={id}" + "".join("-{sbc_" + o + "}" for o in info["sbc_split"]), "fmt": "amount", "italic": True}]
                if info["sbc_split"] else [])
    blocks.append(L(id="total_sbc", label="Total SBC", bold=True, hist="total_sbc" if sbc_hist else None, proj_dsl="={drv:sbc}", dsl=None if sbc_hist else "={drv:sbc}", fy="sum", subs=subs_sbc))
    # ---- operating income
    blocks.append({"subtitle": "Operating Income:"})
    oi_hist = hist_only(dv.first_match(["Operating Income", "Operating Income (Loss)"], "GAAP Results")[1] or dv.first_match(["Operating Income"])[1], axis)
    if oi_hist:
        DATA["op_inc"] = oi_hist
    gp_ref = info["total_gp"] or "m_total_rev"
    blocks.append(L(id="op_inc", label="Operating Income", bold=True, hist="op_inc" if oi_hist else None,
                    proj_dsl="={" + gp_ref + "}-{total_opex}" if opex_ids else "={" + gp_ref + "}", dsl=None if oi_hist else ("={" + gp_ref + "}-{total_opex}" if opex_ids else "={" + gp_ref + "}"), fy="sum",
                    subs=[{"key": "pct_of", "label": "% margin", "dsl": "={id}/{m_total_rev}", "fmt": "pct", "italic": True},
                          {"key": "bps", "label": "bps y/y", "dsl": "=({id.pct_of}-{id.pct_of@py})*10000", "fmt": "bps", "italic": True, "needs": "py"},
                          "pct_yoy", "usd_yoy",
                          {"key": "inc_y", "label": "Incremental Operating Margin (y/y)", "dsl": "=({id}-{id@py})/({m_total_rev}-{m_total_rev@py})", "fmt": "pct", "italic": True, "needs": "py"},
                          {"key": "inc_q", "label": "Incremental Operating Margin (q/q)", "dsl": "=({id}-{id@pq})/({m_total_rev}-{m_total_rev@pq})", "fmt": "pct", "italic": True, "needs": "pq", "q_only": True},
                          {"key": "check", "label": "Check", "dsl": "=ROUND({" + gp_ref + "}" + ("-{total_opex}" if opex_ids else "") + "-{id},6)", "fmt": "amount", "italic": True}]))
    if deltas:
        # the proposal names the standard ids; a single-COGS model names its lines differently
        for it in deltas:
            if it.get("line") == "total_gp" and info.get("total_gp"):
                it["line"] = info["total_gp"]
            elif it.get("line") == "total_cogs" and info.get("total_cogs"):
                it["line"] = info["total_cogs"]
        blocks.append({"deltas": deltas})
    return blocks, info


def top_level_ids(rev_index: Dict[str, dict]) -> List[str]:
    return [lid for lid, ln in rev_index.items() if ln.get("_top")]


# ----------------------------------------------------------------------------- statements
def build_statement_blocks(dv: DataView, axis: PeriodAxis, rev_index: dict, cost_info: dict, drivers: List[dict],
                           setup: dict, mapping: Optional[List[dict]] = None) -> Tuple[dict, dict, dict, dict]:
    """IS, CFS and BS blocks plus the DCF configuration derived from them."""
    A = "amount_s"
    map_override = {m["id"]: m for m in (mapping or []) if m.get("id")}
    est_q = [p.pid for p in axis.quarters() if p.estimate]
    annual = [p.pid for p in axis.periods if p.annual_only]

    def mapped(lid: str, synonyms: List[str], section: Optional[str] = None, stmt: str = "is") -> Dict[str, float]:
        ov = map_override.get(lid)
        if ov and ov.get("keep") is not None and not yn(ov.get("keep", "Y")):
            return {}
        excl = EXCLUDE.get(stmt, [])
        if ov and ov.get("data_label"):
            return hist_only(dv.series(ov["data_label"], ov.get("data_section"), excl), axis)
        return hist_only(dv.first_match(synonyms, section, excl)[1], axis)

    has_drv = {d["id"] for d in drivers}

    # ---- income statement ------------------------------------------------------------
    is_blocks: List[dict] = [{"section": "Income Statement", "marker": False}]
    top_rev = [lid for lid in rev_index if rev_index[lid].get("_top")]
    for lid in top_rev:
        hist = DATA.get(lid, {})
        if hist:
            DATA["is_" + lid] = hist
        is_blocks.append(L(id="is_" + lid, label=rev_index[lid]["label"], hist="is_" + lid if hist else None, proj_dsl="={" + REV + "!" + lid + "}",
                           dsl=None if hist else "={" + REV + "!" + lid + "}", fy="sum", fmt=A, gap=False))
    is_blocks.append(L(id="total_rev", label="Total Revenue", bold=True, top=True, dsl="=" + "+".join("{is_" + l + "}" for l in top_rev) if top_rev else "={" + REV + "!total_rev}", fy="sum", fmt=A,
                       subs=[{"key": "pct_yoy", "label": "% YoY Growth", "dsl": "={id}/{id@py}-1", "fmt": "pct_s", "italic": True, "needs": "py"}]))
    cogs_hist = mapped("cogs", ["Cost of Revenue", "Cost of Goods Sold", "Cost Of Goods Sold", "Cost of Sales"], None)
    if cogs_hist:
        DATA["cogs"] = cogs_hist
    tc = cost_info.get("total_cogs")
    is_blocks.append(L(id="cogs", label="Cost of Revenue", hist="cogs" if cogs_hist else None, proj_dsl="={" + MARGIN + "!" + tc + "}" if tc else "=0",
                       dsl=None if cogs_hist else ("={" + MARGIN + "!" + tc + "}" if tc else "=0"), fy="sum", fmt=A, gap=False))
    is_blocks.append(L(id="gp", label="Gross Profit", bold=True, top=True, dsl="={total_rev}-{cogs}", fy="sum", fmt=A,
                       subs=[{"key": "pct_of", "label": "% Gross Margin", "dsl": "={id}/{total_rev}", "fmt": "pct_s", "italic": True}]))
    opex_is_ids = []
    for oid in cost_info.get("opex_ids", []):
        hist = DATA.get(oid, {})
        if hist:
            DATA["is_" + oid] = hist
        opex_is_ids.append("is_" + oid)
        label = cost_info["opex_labels"].get(oid, "Other Operating Expenses (plug for actuals)" if oid == "other_opex" else oid)
        is_blocks.append(L(id="is_" + oid, label=label, hist="is_" + oid if hist else None, proj_dsl="={" + MARGIN + "!" + oid + "}",
                           dsl=None if hist else "={" + MARGIN + "!" + oid + "}", fy="sum", fmt=A, gap=False))
    is_blocks.append(L(id="total_opex_is", label="Total Operating Expenses", bold=True, top=True, dsl="=" + "+".join("{" + o + "}" for o in opex_is_ids) if opex_is_ids else "=0", fy="sum", fmt=A,
                       subs=[{"key": "pct_of", "label": "% of Revenue", "dsl": "={id}/{total_rev}", "fmt": "pct_s", "italic": True}]))
    is_blocks.append(L(id="op_inc_is", label="Operating Income", bold=True, dsl="={gp}-{total_opex_is}", fy="sum", fmt=A,
                       subs=[{"key": "pct_of", "label": "% Margin", "dsl": "={id}/{total_rev}", "fmt": "pct_s", "italic": True}]))
    below = []
    for lid, label, syns, role in canon.IS_LINES:
        if lid in ("tax", "ni", "dep", "amort", "da", "sbc", "adj_oi", "adj_ni", "adj_eps", "shares_basic", "shares_dil", "eps_basic", "eps_dil"):
            continue
        hist = mapped(lid, syns, None, "is")
        if not hist and lid not in ("interest_income", "interest_expense"):
            continue
        if hist:
            DATA[lid] = hist
        if lid == "nci":
            continue
        below.append(lid)
        drv = lid if lid in has_drv else None
        proj = ("={drv:" + drv + "}") if drv else "={" + lid + "@py}"
        # a line with no reported history stays blank in actual columns (a driver link there
        # would be circular with the driver's own realised-history link)
        is_blocks.append(L(id=lid, label=label, hist=lid if hist else {"kind": "blank"}, proj_dsl=proj, annual_dsl=proj, fy="sum", fmt=A, gap=False))
    # everything else below operating income that the data reports in pre-tax income but the
    # model has no line for (FX, one-offs, equity income): a plug so pre-tax and net income foot
    pretax_hist = mapped("pretax", ["Pre-Tax Income", "Pretax Income", "Income Before Taxes", "EBT Incl. Unusual Items"], "GAAP Results", "is") or \
        mapped("pretax", ["Pre-Tax Income", "Pretax Income", "Income Before Taxes", "EBT Incl. Unusual Items"], None, "is")
    oi_hist = DATA.get("op_inc", {})
    nonop_plug = {}
    for pid, pt in pretax_hist.items():
        if pid not in oi_hist:
            continue
        known = oi_hist[pid] + sum(DATA.get(b, {}).get(pid, 0) for b in below)
        diff = round(pt - known, 4)
        if abs(diff) > 0.01:
            nonop_plug[pid] = diff
    if nonop_plug:
        DATA["other_nonop_plug"] = nonop_plug
        below.append("other_nonop_plug")
        is_blocks.append(L(id="other_nonop_plug", label="Other Non-Operating Items (plug for actuals)", hist="other_nonop_plug",
                           values={**{q: 0 for q in est_q}, **{a: "={other_nonop_plug@py}" for a in annual}}, input_fill=True, input_color=S.BLUE,
                           fy="sum", fmt=A, gap=False))
    is_blocks.append(L(id="nonop_net", label="Total Non-Operating Income (Expense)", bold=True, top=True, dsl="=" + ("+".join("{" + b + "}" for b in below) if below else "0"), fy="sum", fmt=A))
    is_blocks.append(L(id="pretax", label="Pre-Tax Income", bold=True, dsl="={op_inc_is}+{nonop_net}", fy="sum", fmt=A, gap=False))
    tax_hist = mapped("tax", ["Income Tax Expense", "Income Tax Expense (Benefit)", "Provision for Income Taxes", "Income Taxes"], "GAAP Results", "is") or mapped("tax", ["Income Tax Expense", "Provision for Income Taxes"], None, "is")
    if tax_hist:
        DATA["tax"] = tax_hist
    is_blocks.append(L(id="tax", label="Income Tax Expense", hist="tax" if tax_hist else None, proj_dsl="={pretax}*{tax_rate}", dsl=None if tax_hist else "={pretax}*{tax_rate}", fy="sum", fmt=A, gap=False))
    is_blocks.append(L(id="tax_rate", label="% Tax Rate", kind="pct", italic=True, fmt="pct_s", hist={"kind": "formula", "dsl": "={tax}/{pretax}"},
                       proj_dsl="={drv:tax_rate}", annual_dsl="={drv:tax_rate}", fy="formula", fy_dsl="={tax}/{pretax}"))
    nci_hist = mapped("nci", ["Minority Interest in Earnings", "Net Income Attributable to Noncontrolling Interest"])
    ni_dsl = "={pretax}-{tax}"
    if nci_hist:
        DATA["nci"] = nci_hist
        is_blocks.append(L(id="nci", label="(-) Net Income Attributable to Noncontrolling Interest", hist="nci", proj_dsl="={nci@py}", fy="sum", fmt=A, gap=False))
        ni_dsl = "={pretax}-{tax}-{nci}"
    is_blocks.append(L(id="ni", label="Net Income", bold=True, top=True, dsl=ni_dsl, fy="sum", fmt=A,
                       subs=[{"key": "pct_of", "label": "% Net Margin", "dsl": "={id}/{total_rev}", "fmt": "pct_s", "italic": True}]))
    # memo
    is_blocks.append({"subtitle": "memo"})
    # D&A and SBC are reported in the cash-flow block of a Bloomberg printout: the memo lines may read it
    dep_hist = mapped("dep", ["Depreciation Expense", "Depreciation"], None, "memo")
    amort_hist = mapped("amort", ["Amortization of Intangible Assets", "Amortization of Intangibles", "Amort. of Goodwill and Intangibles"], None, "memo")
    da_hist = mapped("da", ["Depreciation & Amortization", "Depreciation & Amort., Total", "Depreciation & Amort."], None, "memo")
    da_lines = []
    if dep_hist or amort_hist or not da_hist:
        if dep_hist:
            DATA["dep"] = dep_hist
        if amort_hist:
            DATA["amort"] = amort_hist
        is_blocks.append(L(id="dep", label="Depreciation", hist="dep" if dep_hist else {"kind": "blank"}, proj_dsl="={drv:dep}", annual_dsl="={drv:dep}", fy="sum", fmt=A, gap=False))
        is_blocks.append(L(id="amort", label="Amortization of Intangibles", hist="amort" if amort_hist else {"kind": "blank"}, proj_dsl="={drv:amort}", annual_dsl="={drv:amort}", fy="sum", fmt=A, gap=False))
        da_lines = ["dep", "amort"]
        da_expr = "{dep}+{amort}"
    else:
        DATA["da"] = da_hist
        is_blocks.append(L(id="da", label="Depreciation & Amortization", hist="da", proj_dsl="={drv:da}", annual_dsl="={drv:da}", fy="sum", fmt=A, gap=False))
        da_lines = ["da"]
        da_expr = "{da}"
    is_blocks.append(L(id="ebitda", label="EBITDA", bold=True, top=True, dsl="={op_inc_is}+" + da_expr, fy="sum", fmt=A,
                       subs=[{"key": "pct_of", "label": "% Margin", "dsl": "={id}/{total_rev}", "fmt": "pct_s", "italic": True}], gap=False))
    sbc_hist = DATA.get("total_sbc") or mapped("sbc", ["Stock-Based Compensation", "Stock Based Compensation"], None, "memo")
    if sbc_hist:
        DATA["sbc"] = sbc_hist
    is_blocks.append(L(id="sbc", label="Stock-Based Compensation", hist="sbc" if sbc_hist else {"kind": "blank"}, proj_dsl="={drv:sbc}", annual_dsl="={drv:sbc}", fy="sum", fmt=A, gap=False))
    is_blocks.append(L(id="ebitda_ex", label="EBITDA ex. SBC", bold=True, top=True, dsl="={ebitda}+{sbc}", fy="sum", fmt=A,
                       subs=[{"key": "pct_of", "label": "% Margin", "dsl": "={id}/{total_rev}", "fmt": "pct_s", "italic": True}]))
    # adjusted block
    adjusted = str(setup.get("adjusted_block", "auto")).lower()
    adj_oi_hist = mapped("adj_oi", ["Adjusted Operating Income", "Adj. Operating Income", "Non-GAAP Operating Income"])
    adj_ni_hist = mapped("adj_ni", ["Adjusted Net Income", "Adj. Net Income", "Non-GAAP Net Income"])
    adj_eps_hist = mapped("adj_eps", ["Adjusted Diluted EPS", "Adj. Diluted EPS", "Non-GAAP EPS", "Non-GAAP Diluted EPS"])
    include_adj = adjusted == "yes" or (adjusted == "auto" and bool(adj_oi_hist or adj_eps_hist))
    metric_line = "ebitda"
    if include_adj:
        is_blocks.append({"subtitle": "Non-GAAP Reconciliation"})
        DATA["adj_oi"] = adj_oi_hist
        is_blocks.append(L(id="adj_sbc", label="(+) Stock-Based Compensation", dsl="={sbc}", fy="sum", fmt=A, gap=False))
        if "amort" in da_lines:
            is_blocks.append(L(id="adj_amort", label="(+) Amortization of Acquired Intangibles", dsl="={amort}", fy="sum", fmt=A, gap=False))
        other_adj_hist = {}
        for pid, v in adj_oi_hist.items():
            base = (DATA.get("op_inc", {}).get(pid) if DATA.get("op_inc") else None)
            if base is None:
                continue
            other = v - base - sbc_hist.get(pid, 0) - (amort_hist.get(pid, 0) if "amort" in da_lines else 0)
            other_adj_hist[pid] = round(other, 4)
        DATA["adj_other"] = other_adj_hist
        is_blocks.append(L(id="adj_other", label="(+) Other Adjustments (restructuring, legal, other)", hist="adj_other" if other_adj_hist else None,
                           proj_dsl="={drv:adj_other}", dsl=None if other_adj_hist else "={drv:adj_other}", fy="sum", fmt=A, gap=False))
        is_blocks.append(L(id="adj_oi", label="Adjusted Operating Income", bold=True, top=True, dsl="={op_inc_is}+{adj_sbc}" + ("+{adj_amort}" if "amort" in da_lines else "") + "+{adj_other}", fy="sum", fmt=A,
                           subs=[{"key": "pct_of", "label": "% Adjusted Operating Margin", "dsl": "={id}/{total_rev}", "fmt": "pct_s", "italic": True}]))
        is_blocks.append(L(id="adj_pretax", label="Adjusted Pre-Tax Income", dsl="={adj_oi}+{nonop_net}", fy="sum", fmt=A, gap=False))
        is_blocks.append(L(id="adj_tax", label="(-) Adjusted Income Tax", dsl="={adj_pretax}*{adj_tax_rate}", fy="sum", fmt=A, gap=False))
        adj_rate_hist = {}
        for pid, ani in adj_ni_hist.items():
            aoi = adj_oi_hist.get(pid)
            non = sum(DATA.get(b, {}).get(pid, 0) for b in below)
            if aoi is not None and (aoi + non):
                adj_rate_hist[pid] = round(1 - ani / (aoi + non), 6)
        DATA["adj_tax_rate"] = adj_rate_hist
        is_blocks.append(L(id="adj_tax_rate", label="% Adjusted Tax Rate", kind="pct", italic=True, fmt="pct_s", hist="adj_tax_rate" if adj_rate_hist else None,
                           proj_dsl="={drv:adj_tax_rate}", annual_dsl="={drv:adj_tax_rate}", fy="formula", fy_dsl="={adj_tax}/{adj_pretax}", dsl=None if adj_rate_hist else "={drv:adj_tax_rate}"))
        is_blocks.append(L(id="adj_ni", label="Adjusted Net Income", bold=True, top=True, dsl="={adj_pretax}-{adj_tax}" + ("-{nci}" if nci_hist else ""), fy="sum", fmt=A,
                           subs=[{"key": "pct_of", "label": "% Adjusted Net Margin", "dsl": "={id}/{total_rev}", "fmt": "pct_s", "italic": True}]))
        is_blocks.append(L(id="adj_ebitda", label="Adjusted EBITDA", bold=True, top=True, dsl="={adj_oi}+" + ("{dep}" if "dep" in da_lines else "{da}"), fy="sum", fmt=A,
                           subs=[{"key": "pct_of", "label": "% Margin", "dsl": "={id}/{total_rev}", "fmt": "pct_s", "italic": True}]))
        metric_line = "adj_ebitda"
    is_blocks.append({"subtitle": "Per Share data"})
    for lid, label in (("shares_basic", "Basic Weighted Avg Shares"), ("shares_dil", "Diluted Weighted Avg Shares")):
        hist = mapped(lid, dict(canon.IS_LINES and [(x[0], x[2]) for x in canon.IS_LINES])[lid])
        if hist:
            DATA[lid] = hist
        is_blocks.append(L(id=lid, label=label, kind="shares", hist=lid if hist else None, proj_dsl="={drv:" + lid + "}", dsl=None if hist else "={drv:" + lid + "}", fy="avg", gap=False))
    eps_b = mapped("eps_basic", ["Basic EPS", "Basic EPS Excl. Extra Items"], "GAAP Results") or mapped("eps_basic", ["Basic EPS"])
    eps_d = mapped("eps_dil", ["Diluted EPS", "Diluted EPS Excl. Extra Items"], "GAAP Results") or mapped("eps_dil", ["Diluted EPS"])
    if eps_b:
        DATA["eps_basic"] = eps_b
    if eps_d:
        DATA["eps_dil"] = eps_d
    is_blocks.append(L(id="eps_basic", label="Basic EPS", kind="eps", hist="eps_basic" if eps_b else None, proj_dsl="={ni}/{shares_basic}", dsl=None if eps_b else "={ni}/{shares_basic}", fy="formula", fy_dsl="={ni}/{shares_basic}", gap=False))
    is_blocks.append(L(id="eps_dil", label="Diluted EPS", kind="eps", hist="eps_dil" if eps_d else None, proj_dsl="={ni}/{shares_dil}", dsl=None if eps_d else "={ni}/{shares_dil}", fy="formula", fy_dsl="={ni}/{shares_dil}", gap=False))
    if include_adj:
        if adj_eps_hist:
            DATA["adj_eps"] = adj_eps_hist
        is_blocks.append(L(id="adj_eps", label="Adjusted Diluted EPS", kind="eps", bold=True, hist="adj_eps" if adj_eps_hist else None, proj_dsl="={adj_ni}/{shares_dil}",
                           dsl=None if adj_eps_hist else "={adj_ni}/{shares_dil}", fy="formula", fy_dsl="={adj_ni}/{shares_dil}"))

    # ---- balance sheet -----------------------------------------------------------------
    bs_blocks: List[dict] = [{"section": "Balance Sheet", "marker": False}]
    groups = {"ca": [], "nca": [], "cl": [], "ncl": [], "eq": []}
    present = {}
    for lid, label, syns, grp, role in canon.BS_LINES:
        if role == "plug":
            continue
        hist = mapped(lid, syns, "Liabilities & Equity" if grp in ("cl", "ncl", "eq") else None, "bs") if syns else {}
        if not hist and syns:
            hist = mapped(lid, syns, None, "bs")
        if hist:
            DATA[lid] = hist
            present[lid] = (label, grp, role)
    totals = {}
    for key, (label, syns) in canon.BS_TOTALS.items():
        s = hist_only(dv.first_match(syns, None, EXCLUDE["bs"])[1], axis)
        if s:
            totals[key] = s
    # CapIQ exports have no non-current subtotals: derive missing group totals from the others
    def _derive(target, a, b, sign):
        if target in totals or a not in totals or b not in totals:
            return
        totals[target] = {pid: round(totals[a][pid] + sign * totals[b][pid], 4) for pid in totals[a] if pid in totals[b]}
    _derive("nca", "assets", "ca", -1)
    _derive("ca", "assets", "nca", -1)
    _derive("ncl", "liab", "cl", -1)
    _derive("cl", "liab", "ncl", -1)
    _derive("eq", "le", "liab", -1)
    _derive("liab", "le", "eq", -1)
    # plugs so reported subtotals tie
    for grp in ("ca", "nca", "cl", "ncl", "eq"):
        tot = totals.get(grp)
        plug_id = {"ca": "other_ca", "nca": "other_nca_plug", "cl": "other_cl_plug", "ncl": "other_ncl_plug", "eq": "other_eq_plug"}[grp]
        if not tot:
            continue
        plug = {}
        for pid, tv in tot.items():
            ssum = sum(DATA[l].get(pid, 0) for l, (_, g, _) in present.items() if g == grp)
            diff = round(tv - ssum, 4)
            if abs(diff) > 0.01:
                plug[pid] = diff
        if plug:
            DATA[plug_id] = plug
            present[plug_id] = (dict((x[0], x[1]) for x in canon.BS_LINES)[plug_id], grp, "plug")
    order = [x[0] for x in canon.BS_LINES]
    wc_drivers_needed = set()

    # which cash-flow lines exist decides the balance-sheet roll-forwards
    cf_present_pre = {}
    for lid_, label_, syns_, grp_, role_ in canon.CFS_LINES:
        if role_ == "plug" or not syns_:
            continue
        sec_ = {"op": "Changes in Working Capital" if role_.startswith("wc:") else "Cash from Operating Activities", "inv": "Cash from Investing Activities",
                "fin": "Cash from Financing Activities", "fx": None}[grp_]
        h_ = mapped(lid_, syns_, sec_, "cf") or (mapped(lid_, syns_, None, "cf") if grp_ != "op" else {})
        if h_:
            cf_present_pre[lid_] = True
    cf_has = lambda l: l in cf_present_pre

    def bs_line(lid: str) -> dict:
        label, grp, role = present[lid]
        line = dict(id=lid, label=label, hist=lid, fy="last", fmt=A, gap=False)
        if role == "cash":
            line["proj_dsl"] = "={" + CFS + "!end_cash}"
        elif role in ("pct_rev", "pct_cogs", "pct_costs"):
            did, base = canon.WC_DRIVER_FOR.get(lid, (None, None))
            if did:
                wc_drivers_needed.add(did)
                base_expr = {"rev": "{" + IS + "!total_rev}", "cogs": "{" + IS + "!cogs}", "costs": "({" + IS + "!cogs}+{" + IS + "!total_opex_is})"}[base]
                line["proj_dsl"] = "={drv:" + did + "}*" + base_expr + "*13/{weeks}"
            else:
                line["proj_dsl"] = "={" + lid + "@pq}"
        elif role == "ppe":
            line["proj_dsl"] = "={" + lid + "@pq}" + ("-{" + CFS + "!capex}" if cf_has("capex") else "") + "-{" + IS + "!" + ("dep" if "dep" in da_lines else "da") + "}"
        elif role == "intangibles" and "amort" in da_lines:
            line["proj_dsl"] = "={" + lid + "@pq}-{" + IS + "!amort}"
        elif role == "debt":
            line["proj_dsl"] = "={" + lid + "@pq}" + ("+{" + CFS + "!debt_change}" if cf_has("debt_change") else "") + ("+{" + CFS + "!debt_repaid}" if cf_has("debt_repaid") else "")
        elif role == "apic":
            # buybacks reduce equity through APIC when the company reports no treasury line
            line["proj_dsl"] = ("={" + lid + "@pq}+{" + IS + "!sbc}" + ("+{" + CFS + "!stock_issued}" if cf_has("stock_issued") else "")
                                + ("+{" + CFS + "!rsu_tax}" if cf_has("rsu_tax") else "")
                                + ("+{" + CFS + "!buybacks}" if cf_has("buybacks") and "treasury" not in present else ""))
        elif role == "treasury":
            line["proj_dsl"] = "={" + lid + "@pq}" + ("+{" + CFS + "!buybacks}" if cf_has("buybacks") else "")
        elif role == "retained":
            line["proj_dsl"] = "={" + lid + "@pq}+{" + IS + "!ni}" + ("+{" + CFS + "!dividends}" if cf_has("dividends") else "")
        elif role == "plug":
            line["proj_dsl"] = "={" + lid + "@pq}"
            if lid == "other_eq_plug":
                if cf_has("buybacks") and "treasury" not in present and "apic" not in present:
                    line["proj_dsl"] += "+{" + CFS + "!buybacks}"
                if "retained" not in present:
                    line["proj_dsl"] += "+{" + IS + "!ni}" + ("+{" + CFS + "!dividends}" if cf_has("dividends") else "")
        else:
            line["proj_dsl"] = "={" + lid + "@pq}"
        return line

    def emit_group(grp: str, title: str, total_id: str, total_label: str, subtitle_bold: bool):
        ids = [l for l in order if l in present and present[l][1] == grp]
        if subtitle_bold:
            bs_blocks.append({"subtitle": title})
        else:
            bs_blocks.append({"label": title})
        for l in ids:
            bs_blocks.append({"line": bs_line(l), "gap": False})
        if ids:
            bs_blocks.append(L(id=total_id, label=total_label, bold=True, top=True, dsl="=SUM({" + ids[0] + "}:{" + ids[-1] + "})", fy="formula", fmt=A))
        else:
            bs_blocks.append(L(id=total_id, label=total_label, bold=True, top=True, dsl="=0", fy="formula", fmt=A))
        return ids

    emit_group("ca", "Current Assets", "total_ca", "Total Current Assets", True)
    emit_group("nca", "Non-Current Assets", "total_nca", "Total Non-Current Assets", False)
    bs_blocks.append(L(id="total_assets", label="Total Assets", bold=True, top=True, dsl="={total_ca}+{total_nca}", fy="formula", fmt=A))
    emit_group("cl", "Current Liabilities", "total_cl", "Total Current Liabilities", False)
    emit_group("ncl", "Non-Current Liabilities", "total_ncl", "Total Non-Current Liabilities", False)
    bs_blocks.append(L(id="total_liab", label="Total Liabilities", bold=True, top=True, dsl="={total_cl}+{total_ncl}", fy="formula", fmt=A))
    emit_group("eq", "Shareholders Equity", "total_equity", "Total Equity", True)
    bs_blocks.append(L(id="total_le", label="Total Liabilities & Equity", bold=True, top=True, dsl="={total_liab}+{total_equity}", fy="formula", fmt=A))
    bs_blocks.append(L(id="bs_check", label="check", bold=True, dsl="={total_assets}-{total_le}", fy="formula", fmt=A))

    # ---- cash flow statement ---------------------------------------------------------------
    cf_blocks: List[dict] = [{"section": "Cash Flow Statement", "marker": False}]
    cf_present = {}
    for lid, label, syns, grp, role in canon.CFS_LINES:
        if role == "plug":
            continue
        sec = {"op": "Changes in Working Capital" if role.startswith("wc:") else "Cash from Operating Activities", "inv": "Cash from Investing Activities",
               "fin": "Cash from Financing Activities", "fx": None}[grp]
        hist = mapped(lid, syns, sec, "cf") if syns else {}
        if not hist and syns and grp != "op":
            hist = mapped(lid, syns, None, "cf")
        if lid in ("cf_ni", "cf_da", "cf_sbc") and not hist:
            hist = {"_link": True}
        if hist:
            cf_present[lid] = (label, grp, role)
            if "_link" not in hist:
                DATA[lid] = hist
    # treasury-style companies without a treasury line: buybacks must still hit equity
    if "buybacks" in cf_present and "treasury" not in present and "apic" in present:
        pass
    cf_totals = {k: hist_only(dv.first_match(v[1])[1], axis) for k, v in canon.CFS_TOTALS.items()}

    def plug_series(grp: str, total_key: str, plug_id: str):
        tot = cf_totals.get(total_key) or {}
        if not tot:
            return
        plug = {}
        for pid, tv in tot.items():
            ssum = sum(DATA.get(l, {}).get(pid, 0) for l, (_, g, r) in cf_present.items() if g == grp and l in DATA)
            # linked lines (NI, D&A, SBC) come from the IS history
            if grp == "op":
                ssum += sum(DATA.get(k, {}).get(pid, 0) for k in ("ni",) if "cf_ni" in cf_present and k in DATA)
                ni_hist = cf_totals.get("ni")
            diff = round(tv - ssum, 4)
            plug[pid] = diff
        DATA[plug_id] = plug
        cf_present[plug_id] = (dict((x[0], x[1]) for x in canon.CFS_LINES)[plug_id], grp, "plug")

    # NI history for the operating plug comes from the IS net income line
    ni_is = {}
    pre_vals = DATA.get("pretax")
    cf_ni_hist = mapped("cf_ni", ["Net Income"], "Cash from Operating Activities", "cf") or mapped("cf_ni", ["Net Income"], "GAAP Results", "is")
    if cf_ni_hist:
        DATA["cf_ni_hist"] = cf_ni_hist
    if cf_totals.get("op"):
        plug = {}
        for pid, tv in cf_totals["op"].items():
            ssum = cf_ni_hist.get(pid, 0)
            ssum += (DATA.get("da", {}).get(pid) if "da" in DATA else (DATA.get("dep", {}).get(pid, 0) + DATA.get("amort", {}).get(pid, 0)))
            ssum += DATA.get("sbc", {}).get(pid, 0)
            for l, (_, g, r) in cf_present.items():
                if g == "op" and l in DATA and l not in ("cf_ni", "cf_da", "cf_sbc"):
                    ssum += DATA[l].get(pid, 0)
            plug[pid] = round(tv - ssum, 4)
        DATA["other_op"] = plug
        cf_present["other_op"] = ("(+/-) Other Operating Items (plug for actuals)", "op", "plug")
    plug_series("inv", "inv", "other_inv")
    plug_series("fin", "fin", "other_fin")
    if cf_totals.get("net"):
        fx = {}
        for pid, tv in cf_totals["net"].items():
            ssum = (cf_totals.get("op", {}).get(pid, 0) + cf_totals.get("inv", {}).get(pid, 0) + cf_totals.get("fin", {}).get(pid, 0))
            fx[pid] = round(tv - ssum, 4)
        DATA["fx"] = fx
        cf_present["fx"] = ("(+/-) FX Effect on Cash", "fx", "plug")
    cf_order = [x[0] for x in canon.CFS_LINES]
    zero_est = {**{q: 0 for q in est_q}}
    carry = {a: None for a in annual}

    def cf_line(lid: str) -> dict:
        label, grp, role = cf_present[lid]
        line = dict(id=lid, label=label, fy="sum", fmt=A, gap=False)
        if role == "link_ni":
            line["dsl"] = "={" + IS + "!ni}"
        elif role == "link_da":
            line["dsl"] = "=" + "+".join("{" + IS + "!" + d + "}" for d in da_lines)
        elif role == "link_sbc":
            line["dsl"] = "={" + IS + "!sbc}"
        elif role.startswith("wc:"):
            bl = role[3:]
            line["hist"] = lid
            if bl in present:
                sign = "-" if present[bl][1] in ("ca", "nca") else ""
                line["proj_dsl"] = "=" + sign + "({" + BS + "!" + bl + "}-{" + BS + "!" + bl + "@pq})"
            else:
                line["values"] = {**zero_est, **{a: "={" + lid + "@py}" for a in annual}}
                line["input_fill"] = True; line["input_color"] = S.BLUE
        elif role == "investments":
            line["hist"] = lid
            inv_lines = [l for l in ("st_inv", "lt_inv") if l in present]
            if inv_lines:
                line["proj_dsl"] = "=-(" + "+".join("({" + BS + "!" + l + "}-{" + BS + "!" + l + "@pq})" for l in inv_lines) + ")"
            else:
                line["values"] = {**zero_est, **{a: "={" + lid + "@py}" for a in annual}}
                line["input_fill"] = True; line["input_color"] = S.BLUE
        elif role == "driver":
            line["hist"] = lid
            line["proj_dsl"] = "={drv:" + lid + "}"
        else:  # zero / plug: inputs of 0 in estimates (light yellow), carried in annual years
            line["hist"] = lid
            line["values"] = {**zero_est, **{a: "={" + lid + "@py}" for a in annual}}
            line["input_fill"] = True
            line["input_color"] = S.BLUE
        return line

    def emit_cf(grp: str, total_id: str, total_label: str):
        ids = [l for l in cf_order if l in cf_present and cf_present[l][1] == grp]
        for i, l in enumerate(ids):
            ln = cf_line(l)
            if i == len(ids) - 1:
                ln["bottom"] = True
            cf_blocks.append({"line": ln, "gap": False})
        if ids:
            cf_blocks.append(L(id=total_id, label=total_label, bold=True, top=True, dsl="=SUM({" + ids[0] + "}:{" + ids[-1] + "})", fy="sum", fmt=A))
        else:
            cf_blocks.append(L(id=total_id, label=total_label, bold=True, top=True, dsl="=0", fy="sum", fmt=A))
        return ids

    emit_cf("op", "cfo", "CFO")
    emit_cf("inv", "cfi", "CFI")
    cf_blocks.append(L(id="fcf", label="FCF", bold=True, top=True, dsl="={cfo}+{capex}" if "capex" in cf_present else "={cfo}", fy="sum", fmt=A))
    emit_cf("fin", "cff", "CFF")
    if "fx" in cf_present:
        cf_blocks.append({"line": cf_line("fx"), "gap": True})
        net_dsl = "={cfo}+{cfi}+{cff}+{fx}"
    else:
        net_dsl = "={cfo}+{cfi}+{cff}"
    cf_blocks.append(L(id="net_change", label="Net Change in Cash", bold=True, top=True, dsl=net_dsl, fy="sum", fmt=A, gap=False))
    beg = cf_totals.get("beg") or {}
    first_q = axis.actual_quarters()[0].pid
    if "cash" in DATA and first_q in DATA["cash"]:
        beg_first = (DATA["cash"].get(first_q, 0) - (cf_totals.get("net", {}).get(first_q, 0)))
    else:
        beg_first = beg.get(first_q)
    DATA["beg_cash"] = {first_q: beg_first} if beg_first is not None else {}
    cf_blocks.append(L(id="beg_cash", label="Beginning Cash", hist={"kind": "formula", "dsl": "={end_cash@pq}"}, proj_dsl="={end_cash@pq}", annual_dsl="={end_cash@py}",
                       fy="first", fmt=A, values={first_q: "={data:beg_cash}"} if beg_first is not None else {}))
    cf_blocks.append(L(id="end_cash", label="Ending Cash", bold=True, top=True, dsl="={net_change}+{beg_cash}", fy="formula", fmt=A))
    cf_blocks.append(L(id="cash_check", label="check", bold=True, dsl="={end_cash}-{" + BS + "!cash}", fy="formula", fmt=A))

    dcf_cfg = {"opex_lines": [[o, cost_info["opex_labels"].get(o.replace("is_", ""), "Other Operating Expenses")] for o in opex_is_ids],
               "da_lines": da_lines, "nwc_lines": [l for l in cf_order if l in cf_present and cf_present[l][2].startswith("wc:")],
               "capex_line": "capex" if "capex" in cf_present else None, "ebitda_line": metric_line,
               "bridge": {"cash_lines": [l for l in ("cash", "st_inv", "lt_inv") if l in present],
                          "debt_lines": [l for l in ("st_debt", "lt_debt", "lease_liab_cur", "lease_liab") if l in present]}}
    return {"blocks": is_blocks}, {"blocks": cf_blocks}, {"blocks": bs_blocks}, {"dcf": dcf_cfg, "metric_line": metric_line, "wc_drivers": sorted(wc_drivers_needed),
                                                                                "has_lines": {"cf": list(cf_present), "bs": list(present)}}


# ----------------------------------------------------------------------------- drivers
def build_driver_specs(driver_rows: List[dict], grid: dict, grid_notes: dict, cases: List[str], needed: dict,
                       setup: dict) -> List[dict]:
    out = []
    seen = set()
    for r in driver_rows:
        did = clean_id(r.get("id") or "")
        if not did or did in seen:
            continue
        seen.add(did)
        fmt = {"%": "pct_plain", "pct": "pct_plain", "bps": "bps", "amount": "amount_s", "price": "price", "shares": "shares", "x": "mult"}.get(
            str(r.get("format") or "%").strip().lower(), "pct_plain")
        section = {"revenue": "revenue", "cost": "cost", "income statement": "is", "is": "is", "balance sheet": "bs", "bs": "bs", "cash flow": "cf", "cf": "cf"}.get(
            str(r.get("section") or "revenue").strip().lower(), "revenue")
        cased = yn(r.get("cased", "Y"))
        d = {"id": did, "label": r.get("label") or did, "section": section, "fmt": fmt, "cased": cased,
             "values": grid.get(did) or {}, "notes": grid_notes.get(did) or {}, "fy": str(r.get("fy") or "sum").lower(),
             "type": str(r.get("type") or "").strip().lower(), "target": None}
        if r.get("target") and r.get("target_sub") is not None:
            d["target"] = {"line": clean_id(r["target"]), "sub": r.get("target_sub") or None}
        if d["type"] == "single":
            d["single"] = True
        if r.get("label_note"):
            d["label_note"] = r["label_note"]
        out.append(d)
    return out


# ----------------------------------------------------------------------------- assemble
def build_spec(inputs: dict, data: dict) -> dict:
    """inputs: dict of the inputs workbook tabs (see inputs_workbook.read_inputs)."""
    DATA.clear()
    setup = inputs.get("setup", {})
    dv = DataView(data, inputs.get("kpi_history"))
    cases = ["Bear", "Base", "Bull"] if str(setup.get("case_set", "5")).startswith("3") or "Bear/Base/Bull" == setup.get("case_set") else ["Disaster", "Bear", "Base", "Bull", "Blowout"]
    annual_years = [int(x) for x in re.findall(r"\d{4}", str(setup.get("annual_only_years") or ""))]
    period_ends = {pid: info.get("end") for pid, info in data.get("periods", {}).items() if info.get("end")}
    horizon = {"first_hist_quarter": setup.get("first_hist_quarter") or data.get("first_quarter"),
               "last_actual_quarter": setup.get("last_actual_quarter") or data.get("last_actual_quarter"),
               "last_quarterly_estimate": setup.get("last_quarterly_estimate") or data.get("last_estimate_quarter"),
               "annual_only_years": annual_years, "period_ends": period_ends, "report_dates": {}}
    company = {"name": setup.get("company_name") or (data.get("ticker") or "").split()[0], "ticker": (setup.get("ticker") or (data.get("ticker") or "").split()[0]),
               "exchange": setup.get("exchange") or "", "reporting_currency": setup.get("reporting_currency") or data.get("currency") or "USD",
               "trading_currency": setup.get("trading_currency") or setup.get("reporting_currency") or data.get("currency") or "USD",
               "fx_rate": float(setup.get("fx_rate") or 1.0), "units": setup.get("units") or "mm",
               "fiscal_year_end_month": int(setup.get("fiscal_year_end_month") or data.get("fy_end_month") or 12), "fiscal_year_end_day": 31,
               "author": setup.get("author") or "", "cover_tab": setup.get("cover_tab") or "Cover"}
    axis = PeriodAxis.build(horizon["first_hist_quarter"], horizon["last_actual_quarter"], horizon["last_quarterly_estimate"], annual_years, period_ends,
                            company["fiscal_year_end_month"])
    drivers_rows = inputs.get("drivers", [])
    driver_specs = build_driver_specs(drivers_rows, inputs.get("driver_grid", {}), inputs.get("driver_grid_notes", {}), cases, {}, setup)
    # expose driver type/target for the trees
    cost_ids = {clean_id(r["id"]) for r in inputs.get("cost_tree", []) if r.get("id")}
    for d in driver_specs:
        for r in drivers_rows:
            if clean_id(r.get("id") or "") == d["id"]:
                tgt = clean_id(r.get("target") or "")
                d["target"] = {"line": tgt, "sub": r.get("target_sub") or None} if tgt else d.get("target")
                d["formula"] = r.get("formula")
                dtype = str(r.get("type") or "").lower()
                if dtype == "gm_pct" and tgt in cost_ids:
                    # realised history of a gross-margin driver is the GM % row of the gross-profit line
                    gp_id = tgt.replace("cogs", "gp") if "cogs" in tgt else tgt + "_gp"
                    d["target"] = {"line": gp_id, "sub": "pct_of"}
                if dtype == "single":
                    # one typed constant lives in the first Drivers & Casing column
                    first = axis.drivers_start_pid()
                    for case, vals in list((d.get("values") or {}).items()):
                        if vals:
                            d["values"][case] = {first: list(vals.values())[0]}
                    for case, nts in list((d.get("notes") or {}).items()):
                        if nts:
                            d["notes"][case] = {first: list(nts.values())[0]}
    variance = {clean_id(v["id"]): v for v in inputs.get("variance", []) if v.get("id")}
    deltas = delta_items(inputs.get("deltas", []), dv, axis)
    rev_blocks, rev_index = build_revenue_blocks(inputs.get("revenue_tree", []), [dict(d, target=(d.get("target") or {}).get("line")) for d in driver_specs],
                                                dv, axis, variance, deltas.get(REV, []))
    roots = {clean_id(r["id"]) for r in inputs.get("revenue_tree", []) if r.get("id") and not r.get("parent")}
    for lid, ln in rev_index.items():
        ln["_top"] = lid in roots and ln.get("kind", "amount") == "amount"
    cost_blocks, cost_info = build_cost_blocks(inputs.get("cost_tree", []), [dict(d, target=(d.get("target") or {}).get("line")) for d in driver_specs],
                                               dv, axis, rev_index, variance, deltas.get(MARGIN, []),
                                               yn(setup.get("incremental_blocks", "Y")), str(setup.get("sbc_split", "auto")).lower() != "no")
    is_cfg, cf_cfg, bs_cfg, extra = build_statement_blocks(dv, axis, rev_index, cost_info, driver_specs, setup, inputs.get("mapping"))
    # drivers' realised-history targets for the Drivers sheet
    for d in driver_specs:
        if not d.get("target") and d["id"] in [x[0] for x in canon.DEFAULT_DRIVERS]:
            tgt = dict((x[0], x[5]) for x in canon.DEFAULT_DRIVERS)[d["id"]]
            if tgt and tgt[0] in {l for sheet in (is_cfg, cf_cfg) for b in sheet["blocks"] if "line" in b for l in [b["line"]["id"]]} and DATA.get(tgt[0]):
                d["target"] = {"line": tgt[0], "sub": tgt[1]}
    # drivers: drop unreferenced default (uncased) drivers and targets that point nowhere
    all_lines = set()
    for sheet_cfg in (rev_blocks, cost_blocks, is_cfg["blocks"], cf_cfg["blocks"], bs_cfg["blocks"]):
        for b in sheet_cfg:
            if "line" in b:
                all_lines.add(b["line"]["id"])
                for s in b["line"].get("subs") or []:
                    all_lines.add(b["line"]["id"] + "." + (s if isinstance(s, str) else s["key"]))
    referenced = set()
    for sheet_cfg in (rev_blocks, cost_blocks, is_cfg["blocks"], cf_cfg["blocks"], bs_cfg["blocks"]):
        for b in sheet_cfg:
            if "line" not in b:
                continue
            ln = b["line"]
            texts = [ln.get(k) for k in ("dsl", "proj_dsl", "annual_dsl", "fy_dsl") if ln.get(k)]
            texts += [v for v in (ln.get("values") or {}).values() if isinstance(v, str)]
            if ln.get("driver", {}).get("id"):
                referenced.add(ln["driver"]["id"])
            for t in texts:
                referenced.update(re.findall(r"\{drv:([a-z0-9_]+)", t))
    user_defined = {clean_id(r.get("id") or "") for r in drivers_rows if clean_id(r.get("id") or "") not in {x[0] for x in canon.DEFAULT_DRIVERS}}
    kept = []
    for d in driver_specs:
        if d["id"] not in referenced and d["id"] not in user_defined:
            continue
        t = d.get("target")
        if t and t.get("line"):
            key = t["line"] + ("." + t["sub"] if t.get("sub") else "")
            if key not in all_lines:
                d["target"] = None
        kept.append(d)
    driver_specs = kept
    # strip helper keys that the engine does not use
    for d in driver_specs:
        d.pop("type", None); d.pop("formula", None)
        if d.get("target") and not d["target"].get("line"):
            d["target"] = None
    for ln in rev_index.values():
        ln.pop("_top", None)
    dcf_in = inputs.get("dcf", {})
    dcf = dict(extra["dcf"])
    dcf.update({k: dcf_in.get(k) for k in ("valuation_date", "tax_rate", "rfr", "beta", "erp", "kd_after_tax", "equity_weight", "diluted_shares") if dcf_in.get(k) is not None})
    dcf["exit_multiples"] = dcf_in.get("exit_multiples") or {}
    dcf["notes"] = dcf_in.get("notes") or {}
    if dcf_in.get("cash_lines"):
        dcf["bridge"]["cash_lines"] = dcf_in["cash_lines"]
    if dcf_in.get("debt_lines"):
        dcf["bridge"]["debt_lines"] = dcf_in["debt_lines"]
    ts_in = inputs.get("tearsheet", {})
    metric_line = ts_in.get("metric_line") or extra["metric_line"]
    tearsheet = {"metric_label": ts_in.get("metric_label") or ("Adj. EBITDA" if metric_line == "adj_ebitda" else "EBITDA"), "metric_line": metric_line,
                 "multiple_label": ts_in.get("multiple_label") or "NTM Multiple", "blocks": ts_in.get("blocks") or [],
                 "multiples": ts_in.get("multiples") or {}, "multiple_notes": ts_in.get("multiple_notes") or {},
                 "weights": ts_in.get("weights") or default_weights(cases), "case_metric_values": ts_in.get("case_metric_values") or {},
                 "current_multiple_period": ts_in.get("current_multiple_period"),
                 "price": {"source": str(setup.get("price_source") or "bloomberg").lower(), "ticker_code": setup.get("ticker_code") or data.get("ticker") or "",
                           "value": setup.get("current_price"), "date": setup.get("price_date")}}
    spec = {"company": company, "horizon": horizon, "cases": cases, "active_case": "Base",
            "sheets": {REV: {"blocks": rev_blocks}, MARGIN: {"blocks": cost_blocks}, IS: is_cfg, CFS: cf_cfg, BS: bs_cfg},
            "drivers": driver_specs, "dcf": dcf, "tearsheet": tearsheet, "side_builds": inputs.get("side_builds_specs") or [],
            "comments_policy": setup.get("comments_policy") or "from_inputs"}
    if str(spec["comments_policy"]).lower().startswith("i will"):
        for d in spec["drivers"]:
            d["notes"] = {}
        spec["tearsheet"]["multiple_notes"] = {}
        spec["dcf"]["notes"] = {}
    return spec, dict(DATA)


def default_weights(cases: List[str]) -> Dict[str, float]:
    if len(cases) == 5:
        return {"Blowout": 0.1, "Bull": 0.2, "Base": 0.4, "Bear": 0.2, "Disaster": 0.1}
    return {"Bull": 0.25, "Base": 0.5, "Bear": 0.25}


def delta_items(rows: List[dict], dv: DataView, axis: PeriodAxis) -> Dict[str, List[dict]]:
    """Delta rows: {sheet, line, sub, measure, source, data_label, from, to} -> engine items."""
    out: Dict[str, List[dict]] = {}
    for r in rows:
        if not r.get("line"):
            continue
        sheet = r.get("sheet") or REV
        src = r.get("source") or "Consensus"
        measure = (r.get("measure") or "growth").lower()
        label = r.get("label") or r["line"]
        values = {}
        if r.get("values"):
            values = dict(r["values"])
        elif r.get("data_label"):
            s = dv.series(r["data_label"], r.get("data_section"))
            if measure == "growth":
                for pid, v in s.items():
                    p = axis.by_id.get(pid)
                    py = axis.prior_year(p) if p else None
                    if p and p.estimate and py and py.pid in s and s[py.pid]:
                        values[pid] = v / s[py.pid] - 1
            else:
                values = {pid: v for pid, v in s.items() if axis.by_id.get(pid) and axis.by_id[pid].estimate}
        frm, to = r.get("from"), r.get("to")
        if frm or to:
            keep = {}
            for pid, v in values.items():
                p = axis.by_id.get(pid)
                if not p:
                    continue
                if frm and axis.by_id.get(frm) and p.col < axis.by_id[frm].col:
                    continue
                if to and axis.by_id.get(to) and p.col > axis.by_id[to].col:
                    continue
                keep[pid] = v
            values = keep
        if not values:
            continue
        out.setdefault(sheet, []).append({"label": label, "line": clean_id(r["line"]), "sub": r.get("sub") or ("pct_yoy" if measure == "growth" else ("pct_of" if measure == "margin" else None)),
                                          "measure": measure, "source": src, "values": values})
    return out
