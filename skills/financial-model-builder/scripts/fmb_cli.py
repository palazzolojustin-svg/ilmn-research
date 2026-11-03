"""Command line for the financial-model-builder skill. Run from any working folder:

  python <skill>/scripts/fmb_cli.py detect  [folder]                     list data files found in the folder (and this repo's consensus notes)
  python <skill>/scripts/fmb_cli.py parse   <files...> --out data.json   normalise Bloomberg / CapIQ exports
  python <skill>/scripts/fmb_cli.py inputs1 data.json --out inputs.xlsx [--set key=value ...]   write the stage-1 inputs workbook (pre-filled)
  python <skill>/scripts/fmb_cli.py inputs2 inputs.xlsx data.json         add the Driver Grid / Multiples / DCF tabs (stage 2)
  python <skill>/scripts/fmb_cli.py spec    inputs.xlsx data.json --out spec.json --data-out model_data.json
  python <skill>/scripts/fmb_cli.py build   spec.json model_data.json --out model.xlsx
  python <skill>/scripts/fmb_cli.py verify  model.xlsx [--no-recalc]
  python <skill>/scripts/fmb_cli.py snapshot model.xlsx "Sheet!A1:T60" out.png
  python <skill>/scripts/fmb_cli.py cases   model.xlsx spec.json          snapshot each case's valuation metric into the Tearsheet (Excel needed)
  python <skill>/scripts/fmb_cli.py summary model.xlsx                    key outputs after a recalc (for the review step)
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from fmb import parse_data  # noqa: E402


VALUE_FLAGS = ("--out", "--data-out", "--set")


def _split(args):
    """(positionals, options, --set values); accepts --flag=value and --flag value."""
    pos, opts, sets = [], {}, []
    i = 0
    while i < len(args):
        a = args[i]
        if a.startswith("--"):
            if "=" in a:
                flag, val = a.split("=", 1)
            elif a in VALUE_FLAGS and i + 1 < len(args) and not args[i + 1].startswith("--"):
                flag, val = a, args[i + 1]
                i += 1
            else:
                flag, val = a, True
            if flag == "--set":
                sets.append(val)
            else:
                opts[flag] = val
        else:
            pos.append(a)
        i += 1
    return pos, opts, sets


def _arg(args, flag, default=None):
    return _split(args)[1].get(flag, default)


def _pos(args):
    return _split(args)[0]


def cmd_doctor(args):
    """Check the environment: Python packages, Excel, and the skill's own test."""
    import importlib.util
    import platform
    report = {"python": sys.version.split()[0], "platform": platform.platform()}
    for mod in ("openpyxl", "win32com", "pypdfium2", "pdfplumber", "xlrd"):
        report[mod] = importlib.util.find_spec(mod) is not None
    if sys.platform.startswith("win"):
        try:
            from fmb.excel import find_excel
            report["excel"] = find_excel()
        except Exception as e:
            report["excel"] = f"not found ({e})"
    else:
        import shutil
        report["libreoffice"] = shutil.which("soffice") or "not found"
    report["can_build"] = report["openpyxl"]
    report["can_verify_in_excel"] = bool(report.get("excel")) and report.get("win32com", False) and "not found" not in str(report.get("excel"))
    report["can_snapshot"] = report["can_verify_in_excel"] and report.get("pypdfium2", False)
    missing = [m for m in ("openpyxl", "pywin32", "pypdfium2") if not report.get({"pywin32": "win32com"}.get(m, m))]
    if missing:
        report["install"] = "python -m pip install --user " + " ".join(missing)
    print(json.dumps(report, indent=1))


def cmd_detect(args):
    folder = Path(args[0]) if args else Path.cwd()
    hits = []
    exts = {".xlsx", ".xls", ".xlsm", ".csv", ".md"}
    for p in folder.rglob("*"):
        if p.suffix.lower() not in exts or any(part.startswith(".") or part in ("_Build", "node_modules", "skills") for part in p.parts):
            continue
        name = p.name.lower()
        if any(k in name for k in ("consensus", "capiq", "capital_iq", "capitaliq", "bloomberg", "income", "balance", "cash", "key_stats", "keystats", "estimates", "financials")):
            hits.append(str(p))
    print(json.dumps(hits, indent=1))


def cmd_parse(args):
    parse_data.main(args)


def cmd_inputs1(args):
    from fmb.inputs_workbook import propose_inputs, write_stage1
    pos, opts, sets = _split(args)
    data = json.loads(Path(pos[0]).read_text(encoding="utf-8"))
    out = opts.get("--out", "model_inputs.xlsx")
    overrides = {}
    for val in sets:   # --set key=value (or key:value)
        if "=" in val:
            k, v = val.split("=", 1)
        elif ":" in val:
            k, v = val.split(":", 1)
        else:
            continue
        overrides[k.strip()] = v.strip()
    files = [{"path": f, "type": "Bloomberg consensus" if f.lower().endswith(".md") else "", "notes": ""} for f in data.get("files", [])]
    inputs = propose_inputs(data, overrides, files)
    write_stage1(inputs, out)
    print("wrote", out)


def cmd_inputs2(args):
    from fmb.build_model import make_axis
    from fmb.inputs_workbook import read_inputs, write_stage2
    from fmb.spec_builder import build_spec
    inputs_path, data_path = _pos(args)[:2]
    data = json.loads(Path(data_path).read_text(encoding="utf-8"))
    inputs = read_inputs(inputs_path)
    spec, model_data = build_spec(inputs, data)
    axis = make_axis(spec)
    # realised history of each driver (where the target line has history) for the grey columns
    hist = {}
    for d in spec["drivers"]:
        t = d.get("target") or {}
        s = model_data.get(t.get("line") or "", {})
        if s and not t.get("sub"):
            hist[d["id"]] = s
    write_stage2(inputs_path, inputs, axis, hist, spec["dcf"].get("bridge"))
    print("stage 2 added to", inputs_path)


def cmd_spec(args):
    from fmb.inputs_workbook import read_inputs
    from fmb.spec_builder import build_spec
    inputs_path, data_path = _pos(args)[:2]
    data = json.loads(Path(data_path).read_text(encoding="utf-8"))
    inputs = read_inputs(inputs_path)
    spec, model_data = build_spec(inputs, data)
    out = _arg(args, "--out", "model_spec.json")
    dout = _arg(args, "--data-out", "model_data.json")
    Path(out).write_text(json.dumps(spec, indent=1, default=str), encoding="utf-8")
    Path(dout).write_text(json.dumps(model_data, indent=1, default=str), encoding="utf-8")
    print("wrote", out, "and", dout, "| drivers:", len(spec["drivers"]), "| sheets:", list(spec["sheets"]))


def cmd_build(args):
    from fmb.build_model import build_from_files
    out = _arg(args, "--out", "model.xlsx")
    pos = _pos(args)
    build_from_files(pos[0], pos[1] if len(pos) > 1 else None, out)
    print("built", out)


def cmd_verify(args):
    from fmb.verify import verify
    rep = verify(_pos(args)[0], recalc="--no-recalc" not in args)
    print(json.dumps(rep, indent=1, default=str))


def cmd_snapshot(args):
    from fmb.snapshot import snapshot
    pos = _pos(args)
    print(snapshot(pos[0], pos[1], pos[2], float(pos[3]) if len(pos) > 3 else 2.0))


def cmd_cases(args):
    from fmb.cases import snapshot_cases
    pos = _pos(args)
    print(json.dumps(snapshot_cases(pos[0], pos[1]), indent=1, default=str))


def cmd_summary(args):
    from fmb.verify import cached_values
    from openpyxl import load_workbook
    wb = load_workbook(_pos(args)[0], data_only=True)
    out = {}
    for sheet in ("Income Statement", "Revenue Build"):
        ws = wb[sheet]
        hdr = {ws.cell(row=7, column=c).value: c for c in range(4, ws.max_column + 1) if ws.cell(row=7, column=c).value}
        for r in range(12, ws.max_row + 1):
            label = ws.cell(row=r, column=2).value
            if label in ("Total Revenue", "EBITDA", "Net Income", "Diluted EPS", "Adjusted Diluted EPS", "Adjusted EBITDA", "Operating Income"):
                out.setdefault(sheet, {})[label] = {h: ws.cell(row=r, column=c).value for h, c in hdr.items() if "E" in str(h)}
    print(json.dumps(out, indent=1, default=str))


COMMANDS = {"doctor": cmd_doctor, "detect": cmd_detect, "parse": cmd_parse, "inputs1": cmd_inputs1, "inputs2": cmd_inputs2, "spec": cmd_spec,
            "build": cmd_build, "verify": cmd_verify, "snapshot": cmd_snapshot, "cases": cmd_cases, "summary": cmd_summary}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        print(__doc__)
        sys.exit(1)
    COMMANDS[sys.argv[1]](sys.argv[2:])
