"""Core-lab sequencing price dataset: $/Gb by core facility, month by month, Oct 2024 to Oct 2026 (started 2026-10-13).

Builds one table per flow cell (Illumina NovaSeq X 25B/10B/1.5B/5B, NovaSeq 6000 S4, NextSeq 2000, Element AVITI,
Ultima UG100) with core facilities as columns and months as rows, so discounting over time is visible.

Phases (resumable; progress in _Build/core_lab_pricing_state.json, log in _Build/core_lab_pricing.log):
  specs     one Sonnet web call confirms manufacturer output per flow cell (Gb at 2x150, lanes)
  discover  Sonnet web agents (4 at a time) find public core rate cards, old fiscal-year price lists and announcements
  harvest   pure Python: Wayback CDX history of every rate-card URL (Sep 2023 to now) plus a live fetch; linked PDFs
  extract   Haiku turns each distinct price-list text into structured price lines (cached by text hash)
  verify    Sonnet re-extracts pages with implausible, conflicting or missing results
  build     pandas/openpyxl/matplotlib: month grids (observed / document-dated / carried), Excel charts, PNGs,
            summary, sources, CSVs and README in Working Notes/Outputs/datasets/

  python _Build/core_lab_pricing.py start     launch detached (survives the chat)
  python _Build/core_lab_pricing.py run       run in the foreground
  python _Build/core_lab_pricing.py status    progress and spend
  python _Build/core_lab_pricing.py check     hourly self-check: relaunch if stalled, then status
  python _Build/core_lab_pricing.py build     rebuild the outputs from what has been collected
  python _Build/core_lab_pricing.py stop      stop launching new model calls (build still runs)
"""
import argparse
import datetime as dt
import hashlib
import html
import io
import json
import os
import re
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse

# Detached (WMI) launches may not see the per-user site-packages where pypdf/matplotlib live.
_parts = Path(__file__).resolve().parts
_home = Path(*_parts[:_parts.index("Users") + 2]) if "Users" in _parts else Path.home()
_usersite = _home / "AppData" / "Roaming" / "Python" / f"Python{sys.version_info[0]}{sys.version_info[1]}" / "site-packages"
if _usersite.exists() and str(_usersite) not in sys.path:
    sys.path.append(str(_usersite))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build import find_claude  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "_Build"
WORK = ROOT / "Working Notes"
DATA = BUILD / "core_lab_data"
DISC = DATA / "discovery"
SNAPS = DATA / "snaps"
EXTR = DATA / "extract"
VERI = DATA / "verify"
REGISTRY = DATA / "registry.json"
SNAPMETA = DATA / "snapmeta.jsonl"
URLDONE = DATA / "urls_done.json"
STATE = BUILD / "core_lab_pricing_state.json"
LOG = BUILD / "core_lab_pricing.log"
SANDBOX = BUILD / "sandbox"
STAMP = "2026-10-13"
TOPIC = "core_lab_price_per_gb"
OUT_DS = WORK / "Outputs" / "datasets"
OUT_DIR = OUT_DS / f"{STAMP}_{TOPIC}"
OUT_XLSX = OUT_DS / f"{STAMP}_{TOPIC}.xlsx"
OUT_README = OUT_DS / f"{STAMP}_{TOPIC}_README.md"

CONCURRENCY = 4
CAP_USD = 170.0            # whole job
DISCOVERY_CAP_USD = 95.0   # discovery waves stop launching beyond this
VERIFY_CAP_USD = 150.0
MAX_VERIFY = 80
TIMEOUT = {"haiku": 10 * 60, "sonnet": 20 * 60, "sonnet_web": 24 * 60}
BUDGET = {"haiku": 1.0, "sonnet": 3.0, "sonnet_web": 7.0}
WINDOW_START, WINDOW_END = "2024-10", "2026-10"
CDX_FROM = "20230901"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/128.0 Safari/537.36")

# Fixed approximate 2026 FX (USD per unit of local currency). Local prices are kept so anyone can reconvert.
FX = {"USD": 1.0, "EUR": 1.16, "GBP": 1.34, "CAD": 0.72, "CHF": 1.25, "AUD": 0.66, "NZD": 0.59, "SEK": 0.105,
      "NOK": 0.099, "DKK": 0.155, "ISK": 0.0081, "SGD": 0.78, "HKD": 0.128, "JPY": 0.0068, "CNY": 0.14,
      "KRW": 0.00072, "TWD": 0.032, "INR": 0.0115, "ILS": 0.29, "PLN": 0.27, "CZK": 0.047, "HUF": 0.0029,
      "BRL": 0.18, "MXN": 0.054, "ZAR": 0.056}

# Manufacturer output per flow cell at 2x150 (300 cycles); overwritten by the specs call where it finds better data.
SPECS = {
    "NSX_1.5B": {"gb": 500, "lanes": 2}, "NSX_5B": {"gb": 1500, "lanes": 2}, "NSX_10B": {"gb": 3000, "lanes": 8},
    "NSX_25B": {"gb": 8000, "lanes": 8}, "NSX_35B": {"gb": 11000, "lanes": 8},
    "NS6000_SP": {"gb": 400, "lanes": 2}, "NS6000_S1": {"gb": 1000, "lanes": 2}, "NS6000_S2": {"gb": 2000, "lanes": 2},
    "NS6000_S4": {"gb": 3000, "lanes": 4},
    "NS2000_P1": {"gb": 30, "lanes": 1}, "NS2000_P2": {"gb": 120, "lanes": 1}, "NS2000_P3": {"gb": 360, "lanes": 1},
    "NS2000_P4": {"gb": 540, "lanes": 1},
    "AVITI_HIGH": {"gb": 300, "lanes": 2}, "AVITI_MEDIUM": {"gb": 150, "lanes": 2}, "AVITI_LOW": {"gb": 75, "lanes": 2},
    "AVITI_ULTRAQ": {"gb": 300, "lanes": 2}, "AVITI_ULTRAHIGH": {"gb": 600, "lanes": 2}, "AVITI24": {"gb": 300, "lanes": 2},
    "UG100_WAFER": {"gb": 3000, "lanes": 1}, "UG200_WAFER": {"gb": 6000, "lanes": 1},
}
FC_LABEL = {
    "NSX_25B": "Illumina NovaSeq X 25B", "NSX_10B": "Illumina NovaSeq X 10B", "NSX_1.5B": "Illumina NovaSeq X 1.5B",
    "NSX_5B": "Illumina NovaSeq X 5B", "NSX_35B": "Illumina NovaSeq X 35B", "NS6000_S4": "Illumina NovaSeq 6000 S4",
    "NS6000_S2": "Illumina NovaSeq 6000 S2", "NS6000_S1": "Illumina NovaSeq 6000 S1", "NS6000_SP": "Illumina NovaSeq 6000 SP",
    "NS2000_P4": "Illumina NextSeq 2000 P4", "NS2000_P3": "Illumina NextSeq 2000 P3", "NS2000_P2": "Illumina NextSeq 2000 P2",
    "NS2000_P1": "Illumina NextSeq 2000 P1", "AVITI_HIGH": "Element AVITI High Output",
    "AVITI_MEDIUM": "Element AVITI Medium Output", "AVITI_LOW": "Element AVITI Low Output",
    "AVITI_ULTRAQ": "Element AVITI Cloudbreak UltraQ", "AVITI_ULTRAHIGH": "Element AVITI Ultra-High Output",
    "AVITI24": "Element AVITI24", "UG100_WAFER": "Ultima UG 100 wafer", "UG200_WAFER": "Ultima UG 200 wafer",
}
FC_ORDER = ["NSX_25B", "NSX_10B", "NSX_5B", "NSX_1.5B", "NSX_35B", "NS6000_S4", "NS6000_S2", "NS6000_S1", "NS6000_SP",
            "NS2000_P4", "NS2000_P3", "NS2000_P2", "NS2000_P1", "AVITI_HIGH", "AVITI_ULTRAQ", "AVITI_ULTRAHIGH",
            "AVITI_MEDIUM", "AVITI_LOW", "AVITI24", "UG100_WAFER", "UG200_WAFER"]
ALWAYS_MAIN = {"NSX_25B", "NSX_10B", "NS6000_S4", "AVITI_HIGH", "UG100_WAFER"}
# $/Gb outside these bands is flagged for verification; outside HARD it is excluded from the grids.
BAND = {"NSX": (0.8, 20), "NS6000": (1.5, 40), "NS2000": (3, 80), "AVITI": (0.8, 30), "UG": (0.2, 10)}
HARD = (0.1, 150)

KEYWORDS = re.compile(r"novaseq|nova seq|\bnsx\b|\bnovaseq ?x\b|\b(1\.5|5|10|25|35)\s?b\b|\bs4\b|\bs2\b|\bs1\b|\bsp\b|"
                      r"nextseq|\bp[1-4]\b|aviti|element|cloudbreak|ultraq|ultima|\bug ?100\b|\bug ?200\b|wafer|"
                      r"flow ?cell|flowcell|\blane|gigabase|per gb|\$/gb|2 ?x ?150|300[- ]cycle", re.I)
PRICEISH = re.compile(r"[$€£¥]|\b(usd|eur|gbp|chf|cad|aud|sek|dkk|nok)\b|\d[\d,.]*\s?(kr|€)", re.I)

_lock = threading.RLock()
_pause_until = 0.0
_wb_lock = threading.Lock()
_wb_last = 0.0


def now():
    return dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def log(msg):
    line = f"[{now()}] {msg}"
    with _lock:
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    print(line, flush=True)


def _retry(fn, tries=40):
    for i in range(tries):
        try:
            return fn()
        except (PermissionError, OSError, json.JSONDecodeError):
            if i == tries - 1:
                raise
            time.sleep(0.25 + 0.25 * i)


def _write_json(path, obj):
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(obj, indent=1, ensure_ascii=False), encoding="utf-8")
    tmp.replace(path)


def read_json(path, default):
    if not path.exists():
        return default
    return _retry(lambda: json.loads(path.read_text(encoding="utf-8")))


def write_json(path, obj):
    with _lock:
        _retry(lambda: _write_json(path, obj))


def load_state():
    with _lock:
        return read_json(STATE, {"stage": "new", "cost_usd": 0.0, "agents": {}, "stop": False, "specs": {},
                                 "started": None, "phases_done": []})


def update_state(fn):
    with _lock:
        st = load_state()
        fn(st)
        st["heartbeat"] = time.time()
        st["heartbeat_human"] = now()
        write_json(STATE, st)
        return st


def add_cost(c):
    return update_state(lambda s: s.update(cost_usd=round(s["cost_usd"] + c, 4)))["cost_usd"]


def keep_awake(on=True):
    if os.name != "nt":
        return
    import ctypes
    ctypes.windll.kernel32.SetThreadExecutionState(0x80000000 | (0x00000001 if on else 0))


def slug(s, n=60):
    return re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")[:n]


def sha(s):
    return hashlib.sha1(s.encode("utf-8", "ignore")).hexdigest()[:16]


def extract_json(text, opener="{"):
    if not text:
        return None
    m = re.search(r"```json\s*(.*?)```", text, re.S)
    cands = [m.group(1)] if m else []
    closer = "]" if opener == "[" else "}"
    i, j = text.find(opener), text.rfind(closer)
    if i >= 0 and j > i:
        cands.append(text[i:j + 1])
    for c in cands:
        try:
            return json.loads(c)
        except Exception:
            continue
    return None


# ------------------------------------------------------------------------------ headless calls

LIMIT_RX = re.compile(r"usage limit|limit reached|hit your limit|limit will reset|resets? (at|in)|"
                      r"rate.?limit|too many requests|\b429\b", re.I)
OVERLOAD_RX = re.compile(r"overloaded|\b529\b|api error|connection error|ECONNRESET", re.I)


def call_claude(prompt, model, tools, timeout, budget, min_len=40):
    """One headless call from the empty sandbox (so this folder's CLAUDE.md is not loaded). Returns (text, cost)."""
    global _pause_until
    exe = find_claude()
    SANDBOX.mkdir(parents=True, exist_ok=True)
    env = {k: v for k, v in os.environ.items() if not re.match(r"(CLAUDE|ANTHROPIC)", k)}
    env.update(CLAUDE_CODE_MAX_OUTPUT_TOKENS="64000", DISABLE_AUTOUPDATER="1")
    args = [exe, "-p", "--model", model, "--output-format", "json", "--strict-mcp-config",
            "--no-session-persistence", "--max-budget-usd", str(budget)]
    if tools:
        args += ["--tools", ",".join(tools), "--allowedTools", " ".join(tools)]
    else:
        args += ["--tools", ""]
    flags = 0x08000000 if os.name == "nt" else 0
    transient = 0
    while True:
        while time.time() < _pause_until:
            time.sleep(30)
        try:
            p = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                 cwd=SANDBOX, env=env, creationflags=flags, text=True, encoding="utf-8",
                                 errors="replace")
            out, err = p.communicate(prompt, timeout=timeout)
        except subprocess.TimeoutExpired:
            if os.name == "nt":
                subprocess.run(["taskkill", "/T", "/F", "/PID", str(p.pid)], capture_output=True)
            else:
                p.kill()
            p.communicate()
            log(f"  timeout after {timeout // 60} min ({model})")
            return None, 0.0
        cost, text, is_err = 0.0, "", True
        try:
            j = json.loads(out)
            cost = float(j.get("total_cost_usd") or 0.0)
            text = j.get("result") or ""
            is_err = bool(j.get("is_error"))
        except Exception:
            text = out or ""
        blob = (text or "") + "\n" + (err or "") + ("" if text else (out or ""))
        if "not logged in" in blob.lower():
            log("  CLI is not logged in. Run `claude setup-token` (or `claude` then /login) and restart.")
            raise SystemExit(2)
        if not is_err and text and len(text.strip()) >= min_len:
            return text.strip(), cost
        if LIMIT_RX.search(blob):
            with _lock:
                _pause_until = max(_pause_until, time.time() + 20 * 60)
            log(f"  usage limit hit; pausing until {dt.datetime.fromtimestamp(_pause_until):%H:%M}: {blob.strip()[:160]!r}")
            update_state(lambda s: s.__setitem__("paused_until", dt.datetime.fromtimestamp(_pause_until).isoformat()))
            continue
        if OVERLOAD_RX.search(blob) and transient < 6:
            transient += 1
            log(f"  transient API error, retry {transient} in 2 min: {blob.strip()[:160]!r}")
            time.sleep(120)
            continue
        if text and len(text.strip()) >= min_len:
            return text.strip(), cost
        log(f"  call failed rc={p.returncode} ({model}): {blob.strip()[:300]!r}")
        return None, cost


def stopped():
    st = load_state()
    return st.get("stop") or st["cost_usd"] >= CAP_USD


# ------------------------------------------------------------------------------ seeds and slices

SEEDS = [
    ("Harvard University", "Bauer Core Facility (FAS)", "US", ["https://bauercore.fas.harvard.edu/fy26-ngs-sequencing",
                                                              "https://bauercore.fas.harvard.edu/fy27-ngs-sequencing"]),
    ("Case Western Reserve University", "Genomics Core", "US", ["https://case.edu/medicine/genomics/pricing"]),
    ("Dana-Farber Cancer Institute", "Molecular Biology Core Facilities (MBCF)", "US",
     ["https://mbcf.dana-farber.org/pricing",
      "https://dfci.ilab.agilent.com/service_center/show_external/7607/core-mbcf-genomics"]),
    ("University of Connecticut", "Center for Genome Innovation", "US",
     ["https://draft.genome.center.uconn.edu/cgi_service_rates", "https://honeycrisp.core.uconn.edu/products/358"]),
    ("Dartmouth College", "Genomics Shared Resource", "US", ["https://geiselmed.dartmouth.edu/gsr/sequencing/"]),
    ("University of Minnesota", "University of Minnesota Genomics Center", "US",
     ["https://genomics.umn.edu/service/illumina-novaseq-x-plus-sequencing",
      "https://genomics.umn.edu/service/aviti24-sequencing", "https://genomics.umn.edu/AVITI-price-drop-2024",
      "https://genomics.umn.edu/news/aviti-upgrade-complete"]),
    ("Duke University", "Sequencing and Genomic Technologies Core", "US", ["https://medschool.duke.edu/node/8607"]),
    ("University of Missouri", "Genomics Technology Core", "US", ["https://mugenomicscore.missouri.edu/ngs.html"]),
    ("UC Berkeley", "QB3 Genomics", "US", ["https://qb3.berkeley.edu/?p=6524"]),
    ("Weill Cornell Medicine", "Genomics Resources Core Facility", "US",
     ["https://research.weill.cornell.edu/sites/default/files/full_price_list_wcm_genomics_core_fy2027.pdf"]),
    ("Salk Institute", "Integrative Genomics and Bioinformatics Core", "US",
     ["https://www.salk.edu/science/core-facilities/integrative-genomics-and-bioinformatics-core/scheduling-and-rates/",
      "https://salk.edu/science/core-facilities/omics/scheduling-and-rates"]),
    ("University of Utah", "Huntsman Cancer Institute High-Throughput Genomics", "US",
     ["https://uofuhealth.utah.edu/huntsman/shared-resources/gcb/htg/pricing"]),
    ("Northwestern University", "NUSeq Core", "US", ["https://www.cgm.northwestern.edu/docs/nuseq/fy26-prices_finalusers.pdf"]),
    ("CNAG (Centro Nacional de Analisis Genomico)", "CNAG Sequencing Unit", "Spain",
     ["https://www.cnag.eu/sites/default/files/CNAG%20PRICES%202026_R0.pdf",
      "https://www.cnag.eu/sites/default/files/CNAG%20PRICES%202026_R1.pdf"]),
    ("Rush University", "Genomics and Microbiome Core Facility", "US",
     ["https://www.rushu.rush.edu/sites/default/files/2026-06/GMCF%20Pricing%20June%202026.pdf",
      "https://www.rushu.rush.edu/sites/default/files/2026-01/gmcfupdates-boyd-122025.pdf"]),
    ("The Hospital for Sick Children (SickKids)", "The Centre for Applied Genomics (TCAG)", "Canada",
     ["https://www.tcag.ca/documents/facilities/TCAG-NGS-Price-List",
      "https://www.tcag.ca/documents/facilities/TCAG-NGS-Price-List%20April%202025.pdf"]),
    ("TGen (Translational Genomics Research Institute)", "Collaborative Sequencing Center", "US",
     ["https://www.tgen.org/media/x2dmuqf1/tgen_csc_academic_price_list_08-2026.pdf"]),
    ("Texas A&M University", "Texas A&M AgriLife Genomics (TxGen)", "US",
     ["https://www.txgen.tamu.edu/wp-content/uploads/txgen/TxGen_Prices.pdf",
      "https://www.txgen.tamu.edu/wp-content/uploads/2024/04/TxGen_Prices_v12_2024_05_04_v3.pdf"]),
    ("University of Nebraska Medical Center", "Genomics Core", "US",
     ["https://www.unmc.edu/vcr/cores/vcr-cores/genomics/pricing.html"]),
    ("University of Wisconsin-Madison", "Biotechnology Center Gene Expression / DNA Sequencing", "US",
     ["https://research.wisc.edu/?p=57818"]),
    ("Michigan State University", "Research Technology Support Facility Genomics", "US",
     ["https://rtsf.natsci.msu.edu/_assets/files/genomics/NovaSeq%206000%20Sequencing%20Available%20by%20the%20Lane_19July2023.pdf"]),
]

SLICES_W1 = [
    ("us_northeast", "US universities in MA, CT, RI, NH, VT, ME and NY (e.g. Harvard cores, MIT BioMicroCenter, BU, "
     "Tufts, UMass Chan, Yale Center for Genome Analysis, Brown, Columbia, Cornell (Ithaca and Weill), NYU, Rockefeller, "
     "Mount Sinai, Einstein, Rochester, Buffalo, Stony Brook, Albany, Syracuse/SUNY Upstate, UVM, UNH)."),
    ("us_midatlantic_southeast", "US universities in NJ, PA, DE, MD, DC, VA, WV, NC, SC, GA, FL, TN, KY, AL, MS, LA, AR "
     "(e.g. Princeton, Rutgers, Penn NGSC, CHOP, Pitt HSCRF, Penn State, Johns Hopkins GRCF, UMD IGS, Georgetown, UVA, "
     "VCU, Duke, UNC HTSF, NC State, Wake Forest, Emory, Georgia Tech, Augusta, UF ICBR, Miami, USF, Moffitt, "
     "Vanderbilt VANTAGE, UAB, Tulane, LSU, Kentucky, Louisville, Clemson, MUSC)."),
    ("us_midwest", "US universities in OH, MI, IN, IL, WI, MN, IA, MO, KS, NE, ND, SD (e.g. Michigan AGC, MSU RTSF, "
     "Wayne State, Ohio State, Cincinnati, Cleveland Clinic, Indiana CMG, Purdue, Notre Dame, UChicago, Northwestern, "
     "UIUC Roy J. Carver, UIC, Loyola, UW-Madison, Medical College of Wisconsin, Iowa IIHG, WashU GTAC/MGI, "
     "Saint Louis U, KU Medical Center, Kansas State)."),
    ("us_southcentral_mountain", "US universities in TX, OK, CO, UT, AZ, NM, NV, ID, MT, WY (e.g. UT Southwestern "
     "McDermott, MD Anderson, Baylor College of Medicine, UTHealth Houston, UT Austin GSAF, Rice, Texas Tech, UTSA, "
     "UT Health San Antonio, OU, OSU, OMRF, CU Anschutz Genomics Shared Resource, CU Boulder BioFrontiers, Colorado State, "
     "BYU, Arizona UAGC, ASU, Northern Arizona, UNM, Nevada Reno, Montana State)."),
    ("us_west", "US universities in CA, OR, WA, AK, HI (e.g. UCSF CAT, Stanford Genomics, UCLA TCGB, UC Davis Genome "
     "Center, UC Irvine GRT Hub, UC Riverside, UC San Diego IGM, UC Santa Cruz, UCSB, USC, Caltech, City of Hope, "
     "Cedars-Sinai, Scripps, OHSU MPSSR, Oregon State CQLS, Univ. of Oregon GC3F, UW Northwest Genomics Center, "
     "Washington State, Univ. of Hawaii)."),
    ("nonprofit_institutes", "Non-profit academic research institutes worldwide (e.g. Broad Institute, Whitehead, "
     "Jackson Laboratory, Stowers, HudsonAlpha, Van Andel, Fred Hutch, St. Jude, Memorial Sloan Kettering IGO, "
     "Cold Spring Harbor, New York Genome Center, Wistar, Sanford Burnham Prebys, La Jolla Institute, Scripps Research, "
     "Allen Institute, Gladstone, Lerner/Cleveland Clinic, Oklahoma Medical Research Foundation, CRG Barcelona, "
     "Wellcome Sanger, Francis Crick, EMBL GeneCore, Max Planck institutes, Institut Pasteur, Institut Curie, Garvan, "
     "WEHI, Hubrecht, IMP/IMBA Vienna (VBCF), Weizmann)."),
    ("canada", "Canadian universities and research hospitals (e.g. McGill Genome Centre, UHN Princess Margaret Genomics "
     "Centre, Lunenfeld-Tanenbaum, OICR, Canada's Michael Smith Genome Sciences Centre (BC Cancer), UBC Sequencing "
     "Centre, Calgary CHGI, Alberta, Ottawa StemCore, Queen's, Western, McMaster Farncombe, Laval CHU de Quebec, "
     "IRIC Montreal, Sherbrooke, Dalhousie, Manitoba, Saskatchewan)."),
    ("uk_ireland", "UK and Irish universities and institutes (e.g. Oxford Genomics Centre, Cambridge Genomic Services / "
     "CRUK Cambridge Institute, Edinburgh Clinical Research Facility / Edinburgh Genomics, Glasgow Polyomics, "
     "UCL Genomics, Imperial, King's, QMUL Genome Centre, Liverpool Centre for Genomic Research, Birmingham Genomics, "
     "Exeter Sequencing Service, Leeds, Manchester Genomic Technologies, Newcastle, Bristol Genomics, Cardiff, "
     "Nottingham DeepSeq, Sheffield, Dundee, Aberdeen, Trinity College Dublin, UCD Conway, Queen's Belfast)."),
    ("dach_benelux", "Universities and institutes in Germany, Austria, Switzerland, Netherlands, Belgium, Luxembourg "
     "(e.g. Functional Genomics Center Zurich, Lausanne GTF, Geneva iGE3, Basel/DBSSE, Bern NGS platform, VBCF Vienna, "
     "Medical University Vienna, Cologne Center for Genomics, Dresden DcGC, Tübingen, Heidelberg (DKFZ, EMBL), "
     "Munich (LMU, Helmholtz), Kiel IKMB, Berlin (MDC, BIH), Hamburg UKE, Leiden, Utrecht/UMC, Amsterdam UMC, "
     "Nijmegen, VIB Nucleomics Core, Ghent, Leuven, Luxembourg LCSB)."),
    ("nordics_south_europe_israel", "Universities and institutes in Sweden, Norway, Denmark, Finland, Iceland, France, "
     "Spain, Portugal, Italy, Greece and Israel (e.g. SciLifeLab NGI Stockholm/Uppsala, Lund, Gothenburg, Oslo NSC, "
     "Bergen, Copenhagen, Aarhus, FIMM/Helsinki, Turku, Oulu; GenomEast/IGBMC, Genotoul, Institut Curie, IGFL, "
     "Institut Imagine, ICM Paris; CRG, IRB Barcelona, CNIO, Valencia, Santiago; Gulbenkian, i3S Porto; "
     "IIT, Telethon TIGEM, Padova, Milan, Rome; Weizmann INCPM, Technion, Hebrew University, Tel Aviv)."),
    ("asia_pacific", "Universities and non-profit institutes in Australia, New Zealand, Singapore, Hong Kong, Japan, "
     "Korea, Taiwan, India and elsewhere in Asia (e.g. Ramaciotti Centre UNSW, AGRF (non-profit), Garvan, WEHI, "
     "QIMR Berghofer, UQ IMB, Monash, SAHMRI, Otago Genomics, Auckland, Duke-NUS, NUS, A*STAR GIS, HKU Centre for "
     "PanorOmic Sciences, CUHK, RIKEN, Kyoto, Tokyo, KAIST, Academia Sinica, NTU, IISc/NCBS)."),
    ("platform_ultima_element", "Academic cores ANYWHERE that offer Ultima Genomics UG 100 / UG 100 Solaris / UG 200 "
     "or Element Biosciences AVITI / AVITI24 (any flow cell, incl. Cloudbreak, UltraQ, Freestyle) sequencing with public "
     "prices, plus announcements of their adoption or price changes 2024-2026. Search e.g. 'core facility UG 100 price', "
     "'Ultima sequencing core rates', 'AVITI core facility pricing', 'AVITI24 rates core', 'Cloudbreak UltraQ core price', "
     "'price reduction AVITI core'."),
]

SLICES_W2 = [
    ("us_gapfill_a_m", "US universities and academic medical centers in states starting A through M that are NOT in "
     "the already-found list below. Think beyond flagship campuses: medical schools, land-grant universities, cancer "
     "centers, children's hospitals with academic cores."),
    ("us_gapfill_n_w", "US universities and academic medical centers in states starting N through W that are NOT in "
     "the already-found list below. Think beyond flagship campuses: medical schools, land-grant universities, cancer "
     "centers, children's hospitals with academic cores."),
    ("intl_gapfill", "International (non-US) universities and non-profit academic institutes NOT in the already-found "
     "list below, any country, including Latin America, Middle East and Africa."),
    ("history_announcements", "Dated announcements and archived documents of NovaSeq X, NovaSeq 6000, NextSeq 2000, AVITI "
     "and Ultima PRICE CHANGES at academic cores 2024-2026 (news posts, newsletters, 'price reduction', 'new lower rates', "
     "'FY25 rates', 'FY26 rates', 'rate increase', 'tariff surcharge'), and older fiscal-year price-list PDFs of cores "
     "already found, so we can build price history. Return the exact document URLs."),
]

DISCOVERY_PROMPT = """You are a research agent (today is 2026-10-13) helping an equity analyst build a dataset of the prices that academic DNA sequencing CORE FACILITIES charge their users, month by month from Oct 2024 to Oct 2026, to measure discounting in $/Gb over time.

YOUR SLICE: {slice}

GOAL: find as many cores in your slice as possible (target 15-30) that publish NGS sequencing prices publicly (no login) for ANY of these platforms:
- Illumina NovaSeq X / X Plus (1.5B, 5B, 10B, 25B flow cells; by lane or full flow cell)
- Illumina NovaSeq 6000 (SP, S1, S2, S4) and NextSeq 2000 (P1-P4)
- Element Biosciences AVITI / AVITI24 (any flow cell: High/Medium/Low output, Cloudbreak, UltraQ)
- Ultima Genomics UG 100 / UG 100 Solaris / UG 200 (wafers)
For each core return the exact URLs of: the public rate-card page(s); PDF/Excel price lists, INCLUDING older fiscal-year or dated versions (e.g. FY25, FY26, 2024, 2025 versions) because we need history; and dated news posts announcing price changes. Use WebSearch, then open candidate pages with WebFetch to confirm they show sequencing prices (a quick check is enough). Note which pages are login-gated (iLab, CoreSmart, PPMS, Stratocore): skip those unless a public page (e.g. iLab 'show_external') lists prices.

INCLUDE: universities, academic medical centers, and non-profit academic institutes (e.g. Broad, Salk, Dana-Farber, CNAG). EXCLUDE commercial providers (Novogene, Azenta/Genewiz, BGI, Psomagen, Macrogen, Admera, Eurofins, Novogene etc.).

ALREADY KNOWN (do not spend time re-finding these; you may add extra URLs for them, e.g. older price lists):
{known}

Do NOT transcribe whole price lists (a separate step extracts prices from the URLs). In "notes", give one sample line, e.g. "25B lane 2x150 internal $2,950 (FY26)".

OUTPUT: a few lines of notes, then ONE JSON object in a ```json fenced block, exactly this shape:
{{"cores": [{{"institution": "...", "core": "...", "country": "...", "kind": "university|academic_medical_center|nonprofit_institute|government",
  "platforms": ["NovaSeq X", "AVITI", "UG100", ...],
  "urls": [{{"url": "https://...", "type": "rate_page|pdf|spreadsheet|announcement", "current": true, "public": true, "verified": true, "as_of": "YYYY-MM or null"}}],
  "notes": "..."}}]}}
"current" means the page/document is the live, current rate card; set false for superseded documents. Never invent URLs: only list URLs you saw in search results or opened.
HARD STOP: you have about 18 minutes. Return what you have before time runs out."""

SPECS_PROMPT = """You are a research agent (today is 2026-10-13). Using Illumina, Element Biosciences and Ultima Genomics official specification pages/sheets (WebSearch + WebFetch), give the MAXIMUM specified output per flow cell (or wafer) and the number of lanes for each item below, at 2x150 bp (300 cycles) where applicable. For Ultima, give reads per wafer and average read length and compute Gb per wafer. For NextSeq 2000 P1-P4 give 2x150 output. For Element AVITI give per-flow-cell output at 2x150 for each flow-cell type (High/Medium/Low output, Cloudbreak UltraQ, any ultra-high output type, AVITI24).

Items: NSX_1.5B, NSX_5B, NSX_10B, NSX_25B, NSX_35B (if announced), NS6000_SP, NS6000_S1, NS6000_S2, NS6000_S4 (v1.5), NS2000_P1, NS2000_P2, NS2000_P3, NS2000_P4, AVITI_HIGH, AVITI_MEDIUM, AVITI_LOW, AVITI_ULTRAQ, AVITI_ULTRAHIGH, AVITI24, UG100_WAFER, UG200_WAFER.

Output ONLY a JSON object in a ```json block: {{"NSX_25B": {{"gb": 8000, "lanes": 8, "reads_per_unit_millions": 26000, "source": "url", "note": "..."}}, ...}}. Use null where a product does not exist or you cannot confirm it. HARD STOP: about 15 minutes."""

EXTRACT_PROMPT = """You extract DNA sequencing prices from the text of an academic core facility price list. The text may be a web page or PDF converted to text (table cells separated by " | "), possibly an archived version. Snapshot date: {snap}. URL: {url}. Core (as registered): {core}.

Return ONLY a JSON object:
{{"core_name_on_page": "...", "document_date": "YYYY-MM or null (date the list says it was updated/issued)", "effective_from": "YYYY-MM or null", "effective_to": "YYYY-MM or null", "fiscal_year_label": "e.g. FY26 or null",
 "lines": [{{"platform_fc": CODE, "flow_cell_raw": "...", "unit": "lane|flow_cell|wafer|run|per_gb|per_million_reads|per_sample|other", "quantity": 1, "read_config": "2x150", "total_cycles": 300,
   "tier": "internal|external_academic|commercial|unspecified", "tier_raw": "...", "price": 1234.5, "currency": "USD", "includes_library_prep": false,
   "stated_output_value": null, "stated_output_unit": "Gb|Tb|M_reads|B_reads|M_pairs|B_pairs|M_clusters|null", "line_quote": "short verbatim snippet"}}]}}

CODE is one of: NSX_1.5B, NSX_5B, NSX_10B, NSX_25B, NSX_35B (NovaSeq X / X Plus flow cells), NS6000_SP, NS6000_S1, NS6000_S2, NS6000_S4 (NovaSeq 6000), NS2000_P1, NS2000_P2, NS2000_P3, NS2000_P4 (NextSeq 1000/2000), AVITI_HIGH, AVITI_MEDIUM, AVITI_LOW, AVITI_ULTRAQ, AVITI_ULTRAHIGH, AVITI24 (Element), UG100_WAFER, UG200_WAFER (Ultima). Skip all other instruments (MiSeq, iSeq, NextSeq 500/550, PacBio, Nanopore, Sanger) and non-sequencing services.

RULES
- One line per distinct price: each tier column (internal / external academic / commercial) and each read configuration is a separate line.
- tier: "internal" = the institution's own users; "external_academic" = other academic/non-profit users; "commercial" = industry/for-profit; "unspecified" if the list has one price with no user category.
- unit: what ONE price buys. "lane" for a lane (quantity = number of lanes, e.g. 0.5 for half a lane, 8 for 8 lanes); "flow_cell" for a whole flow cell; "wafer" for an Ultima wafer; "per_gb" / "per_million_reads" for unit prices; "per_sample" when priced per sample (e.g. 30x genome).
- read_config like "2x150", "1x100", "2x300"; total_cycles is the kit cycles (2x150 = 300 cycles; "300 cycle kit" = 300). For Ultima use the stated read length or null.
- includes_library_prep = true only if the price explicitly bundles library preparation.
- SKIP lines for "machine use only" / instrument time / self-service runs where the user supplies the reagents or flow cell: they are not comparable sequencing prices.
- stated_output: only if the list itself states guaranteed or expected output for that unit (e.g. "~800M reads per lane", "3 Tb"). The flow-cell NAME (e.g. "10B", "25B", "1.5B reads") is NOT a stated output: leave null.
- currency as ISO code (USD, EUR, GBP, CAD, CHF, SEK, DKK, NOK, AUD, SGD, ...). Prices as numbers without symbols or commas.
- Never invent prices. If there are no qualifying prices, return "lines": [].

TEXT:
{text}"""

VERIFY_PROMPT = """You are checking an automated extraction of DNA sequencing prices from an academic core facility price list. The first extraction (by a smaller model) is below, followed by the source text and the reason this page was flagged. Re-read the source text carefully and return a CORRECTED, complete extraction in exactly the same JSON schema (fix wrong flow-cell codes, tiers, units, quantities, read configurations, currencies, library-prep flags or prices; add missed lines; delete invented lines). Pay special attention to: per-lane vs per-flow-cell pricing; half-lane or multi-lane quantities; which column is internal vs external academic vs commercial; NovaSeq X flow cell sizes (1.5B, 5B, 10B, 25B) vs NovaSeq 6000 (SP/S1/S2/S4); Element AVITI flow-cell types; Ultima wafers.

FLAG REASON: {reason}

SCHEMA AND CODE LIST (same as the first pass):
{schema}

FIRST EXTRACTION:
{first}

SOURCE TEXT (snapshot {snap}, {url}):
{text}

Return ONLY the corrected JSON object."""


# ------------------------------------------------------------------------------ registry

def load_registry():
    return read_json(REGISTRY, {"cores": {}, "urls": {}})


def add_core(reg, institution, core, country, kind, urls, source, notes=""):
    """urls: list of dicts {url,type,current,public,as_of}. Returns core_id. Dedupes by URL and by institution+domain."""
    urls = [u for u in urls if u.get("url", "").startswith("http")]
    cid = None
    for u in urls:
        if u["url"] in reg["urls"]:
            cid = reg["urls"][u["url"]]["core_id"]
            break
    inst = slug(institution, 40)
    if not cid and urls:
        dom = urlparse(urls[0]["url"]).netloc.lower().removeprefix("www.")
        for k, c in reg["cores"].items():
            if c["inst_slug"] == inst and dom in c.get("domains", []):
                cid = k
                break
    if not cid:
        cid = f"{inst}--{slug(core, 30)}" or sha(institution + core)
        n = 2
        while cid in reg["cores"]:
            cid = f"{inst}--{slug(core, 30)}-{n}"
            n += 1
        reg["cores"][cid] = {"institution": institution, "core": core, "country": country, "kind": kind,
                             "inst_slug": inst, "domains": [], "sources": [], "notes": []}
    c = reg["cores"][cid]
    if source not in c["sources"]:
        c["sources"].append(source)
    if notes:
        c["notes"].append(notes[:300])
    for u in urls:
        dom = urlparse(u["url"]).netloc.lower().removeprefix("www.")
        if dom not in c["domains"]:
            c["domains"].append(dom)
        if u["url"] not in reg["urls"]:
            reg["urls"][u["url"]] = {"core_id": cid, "type": u.get("type", "rate_page"), "current": bool(u.get("current", True)),
                                     "public": u.get("public", True) is not False, "as_of": u.get("as_of"), "via": source}
    return cid


def known_list(reg):
    lines = []
    for c in reg["cores"].values():
        lines.append(f"- {c['institution']} / {c['core']} ({c['country']})")
    return "\n".join(sorted(set(lines))) or "- (none yet)"


def seed_registry():
    reg = load_registry()
    for inst, core, country, urls in SEEDS:
        add_core(reg, inst, core, country, "nonprofit_institute" if any(k in inst for k in ("Salk", "Dana", "CNAG", "TGen", "SickKids"))
                 else "university", [{"url": u, "type": "pdf" if u.lower().endswith(".pdf") else "rate_page", "current": True}
                                     for u in urls], "seed:clinical_scrape")
    write_json(REGISTRY, reg)
    return reg


# ------------------------------------------------------------------------------ phase: specs

def phase_specs():
    st = load_state()
    if st.get("specs"):
        return
    log("specs: confirming manufacturer output per flow cell (sonnet web)")
    text, cost = call_claude(SPECS_PROMPT, "sonnet", ["WebSearch", "WebFetch"], TIMEOUT["sonnet_web"], BUDGET["sonnet_web"])
    total = add_cost(cost)
    (DATA / "specs_raw.md").write_text(text or "", encoding="utf-8")
    j = extract_json(text or "", "{") or {}
    specs = {}
    for k, v in SPECS.items():
        specs[k] = dict(v, source="default (pre-set from Illumina/Element/Ultima specs)", note="")
        w = j.get(k) if isinstance(j.get(k), dict) else None
        if w and isinstance(w.get("gb"), (int, float)) and w["gb"] > 0:
            specs[k]["gb"] = float(w["gb"])
            if isinstance(w.get("lanes"), (int, float)) and w["lanes"] > 0:
                specs[k]["lanes"] = int(w["lanes"])
            specs[k]["source"] = w.get("source") or "specs agent"
            specs[k]["note"] = (w.get("note") or "")[:300]
            specs[k]["reads_m"] = w.get("reads_per_unit_millions")
    update_state(lambda s: s.update(specs=specs))
    log(f"specs done (${cost:.2f}; job ${total:.2f}): " + ", ".join(f"{k}={v['gb']:.0f}Gb/{v['lanes']}L" for k, v in specs.items()))


# ------------------------------------------------------------------------------ phase: discovery

def run_discovery_agent(aid, slice_text):
    st = load_state()
    rec = st["agents"].get(aid, {})
    if rec.get("status") == "done":
        return
    if stopped() or st["cost_usd"] >= DISCOVERY_CAP_USD:
        log(f"discover {aid}: skipped (cap or stop)")
        return
    update_state(lambda s: s["agents"].__setitem__(aid, {"status": "running", "start": now()}))
    reg = load_registry()
    prompt = DISCOVERY_PROMPT.format(slice=slice_text, known=known_list(reg))
    log(f"discover {aid}: start")
    text, cost = call_claude(prompt, "sonnet", ["WebSearch", "WebFetch"], TIMEOUT["sonnet_web"], BUDGET["sonnet_web"])
    total = add_cost(cost)
    (DISC / f"{aid}.md").write_text(text or "", encoding="utf-8")
    j = extract_json(text or "", "{")
    n_new = 0
    if j and isinstance(j.get("cores"), list):
        with _lock:
            reg = load_registry()
            before = len(reg["cores"])
            for c in j["cores"]:
                try:
                    urls = [u for u in c.get("urls", []) if isinstance(u, dict) and u.get("public", True) is not False]
                    if not urls:
                        continue
                    add_core(reg, c.get("institution") or "?", c.get("core") or "Sequencing core", c.get("country") or "?",
                             c.get("kind") or "university", urls, f"discover:{aid}", c.get("notes") or "")
                except Exception as e:
                    log(f"  bad core entry in {aid}: {e}")
            write_json(REGISTRY, reg)
            n_new = len(reg["cores"]) - before
    ok = bool(j)
    update_state(lambda s: s["agents"].__setitem__(aid, {"status": "done" if ok else "failed", "end": now(),
                                                         "cost": cost, "new_cores": n_new}))
    log(f"discover {aid}: {'done' if ok else 'FAILED'} (+{n_new} cores, ${cost:.2f}; job ${total:.2f})")


def phase_discovery():
    seed_registry()
    with ThreadPoolExecutor(max_workers=CONCURRENCY) as ex:
        list(ex.map(lambda s: run_discovery_agent("w1_" + s[0], s[1]), SLICES_W1))
    # Retry failed wave-1 slices once.
    st = load_state()
    retry = [s for s in SLICES_W1 if st["agents"].get("w1_" + s[0], {}).get("status") == "failed"]
    for s in retry:
        update_state(lambda x, k="w1_" + s[0]: x["agents"].pop(k, None))
    if retry:
        with ThreadPoolExecutor(max_workers=CONCURRENCY) as ex:
            list(ex.map(lambda s: run_discovery_agent("w1_" + s[0], s[1]), retry))
    with ThreadPoolExecutor(max_workers=CONCURRENCY) as ex:
        list(ex.map(lambda s: run_discovery_agent("w2_" + s[0], s[1]), SLICES_W2))
    reg = load_registry()
    log(f"discovery complete: {len(reg['cores'])} cores, {len(reg['urls'])} URLs")


# ------------------------------------------------------------------------------ phase: harvest (no models)

class _Text(HTMLParser):
    BLOCK = {"p", "div", "br", "tr", "li", "h1", "h2", "h3", "h4", "h5", "h6", "table", "section", "article", "ul", "ol",
             "header", "footer", "dt", "dd", "caption", "thead", "tbody"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.skip, self.links = [], 0, []

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "noscript", "svg"):
            self.skip += 1
        if tag == "a":
            href = dict(attrs).get("href")
            if href:
                self.links.append(href)
        if tag in self.BLOCK:
            self.out.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript", "svg"):
            self.skip = max(0, self.skip - 1)
        if tag in ("td", "th"):
            self.out.append(" | ")
        if tag in self.BLOCK:
            self.out.append("\n")

    def handle_data(self, data):
        if not self.skip:
            self.out.append(data)


def html_to_text(raw):
    p = _Text()
    try:
        p.feed(raw)
    except Exception:
        pass
    t = "".join(p.out)
    t = re.sub(r"[ \t\r\f\v\xa0]+", " ", t)
    t = re.sub(r" *\n *", "\n", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip(), p.links


def pdf_to_text(data):
    from pypdf import PdfReader
    try:
        r = PdfReader(io.BytesIO(data))
        return "\n".join((pg.extract_text() or "") for pg in r.pages[:60]).strip()
    except Exception:
        return ""


def xlsx_to_text(data):
    try:
        import openpyxl
        wb = openpyxl.load_workbook(io.BytesIO(data), read_only=True, data_only=True)
        rows = []
        for ws in wb.worksheets[:10]:
            rows.append(f"## {ws.title}")
            for r in ws.iter_rows(values_only=True):
                cells = [str(c) for c in r if c is not None]
                if cells:
                    rows.append(" | ".join(cells))
        return "\n".join(rows)
    except Exception:
        return ""


def relevant_text(full, cap=32000):
    """Title/header lines plus +-10 line windows around price-list keywords. Empty if nothing relevant."""
    lines = [ln for ln in full.split("\n") if ln.strip()]
    hits = [i for i, ln in enumerate(lines) if KEYWORDS.search(ln)]
    if not hits or not any(PRICEISH.search(ln) or re.search(r"\d{2,}", ln) for ln in lines):
        return ""
    keep = set(range(min(25, len(lines))))
    for i in hits:
        keep.update(range(max(0, i - 10), min(len(lines), i + 11)))
    out = "\n".join(lines[i] for i in sorted(keep))
    return out[:cap]


_wb_pause = 0.0
_wb_strikes = 0           # consecutive 429s; the pause doubles each time (10, 20, 40, then 60 min)
WB_GAP = 6.0          # seconds between archive.org requests (~10/min)
WB_PAUSE = 120        # base global pause after a 429 (doubles per consecutive 429, max 30 min)


def wb_get(url, timeout=60, tries=5):
    """GET with retries. archive.org requests are serialized, spaced WB_GAP apart, and a 429 pauses ALL of them."""
    import requests
    global _wb_last, _wb_pause, _wb_strikes
    arch = "archive.org" in url
    for k in range(tries):
        if arch:
            with _wb_lock:
                while True:
                    wait = max(_wb_pause - time.time(), WB_GAP - (time.time() - _wb_last))
                    if wait <= 0:
                        break
                    time.sleep(min(wait, 30))
                _wb_last = time.time()
                try:
                    r = requests.get(url, headers={"User-Agent": UA}, timeout=timeout, allow_redirects=True)
                except Exception:
                    r = None
                if r is not None and r.status_code == 429:
                    _wb_strikes = min(_wb_strikes + 1, 6)
                    pause = min(WB_PAUSE * (2 ** (_wb_strikes - 1)), 1800)
                    _wb_pause = time.time() + pause
                    log(f"  429 from archive.org (strike {_wb_strikes}); pausing all archive requests {pause // 60} min")
                    update_state(lambda s: s.update(wb_paused_until=dt.datetime.fromtimestamp(_wb_pause).isoformat()))
                    continue
                if r is not None and r.status_code == 200:
                    _wb_strikes = 0
        else:
            try:
                r = requests.get(url, headers={"User-Agent": UA}, timeout=timeout, allow_redirects=True)
            except Exception:
                r = None
        if r is None:
            time.sleep(5 * (k + 1))
            continue
        if r.status_code in (503, 502, 504):
            time.sleep(20 * (k + 1))
            continue
        return r
    return None


def to_text(resp, url):
    ctype = (resp.headers.get("Content-Type") or "").lower()
    data = resp.content
    if "pdf" in ctype or url.lower().split("?")[0].endswith(".pdf") or data[:5] == b"%PDF-":
        return pdf_to_text(data), [], "pdf"
    if "spreadsheet" in ctype or url.lower().endswith((".xlsx", ".xlsm")):
        return xlsx_to_text(data), [], "xlsx"
    raw = resp.text
    t, links = html_to_text(raw)
    return t, links, "html"


def cdx(url):
    r = wb_get("https://web.archive.org/cdx/search/cdx?" + "&".join([
        "url=" + requests_quote(url), f"from={CDX_FROM}", "output=json", "filter=statuscode:200", "collapse=digest"]), timeout=90)
    if r is None or r.status_code in (429, 502, 503, 504):
        raise WaybackBlocked(url)
    if r.status_code != 200:
        return []
    try:
        rows = r.json()
    except Exception:
        return []
    return rows[1:] if rows else []


class WaybackBlocked(Exception):
    pass


WB_GIVE_UP_H = 8   # stop waiting for archive.org after this many hours of continuous blocking


def requests_quote(u):
    from urllib.parse import quote
    return quote(u.split("#")[0], safe="")


FAST_MODE = True   # 2026-10-13: archive history for one main rate page per core, one snapshot per quarter


def _bucket(ts):
    y, m = int(ts[:4]), int(ts[4:6])
    return f"{y}-Q{(m - 1) // 3 + 1}" if FAST_MODE else f"{y}-{m:02d}"


def pick_snapshots(rows, cap=12):
    """Latest capture before the window (seeds carry-forward) plus the last capture of each month in the window
    (each quarter in FAST_MODE)."""
    pre, by_month = None, {}
    for row in rows:
        ts = row[1]
        ym = f"{ts[:4]}-{ts[4:6]}"
        if ym < WINDOW_START:
            pre = row
        else:
            by_month[_bucket(ts)] = row
    picks = ([pre] if pre else []) + [by_month[k] for k in sorted(by_month)]
    if len(picks) > cap:
        step = len(picks) / cap
        picks = [picks[int(i * step)] for i in range(cap - 1)] + [picks[-1]]
    return picks


PRICE_LINK = re.compile(r"price|pricing|rate|fee|cost|recharge|tarif|preis|prijs|charges", re.I)


def save_snapshot(core_id, url, ts, source, text, extra=None):
    rel = relevant_text(text)
    h = sha(rel) if rel else ""
    if rel:
        p = SNAPS / f"{h}.txt"
        if not p.exists():
            p.write_text(rel, encoding="utf-8")
    rec = {"core_id": core_id, "url": url, "ts": ts, "source": source, "rel_hash": h, "chars": len(text), "rel_chars": len(rel)}
    if extra:
        rec.update(extra)
    with _lock:
        with open(SNAPMETA, "a", encoding="utf-8") as f:
            f.write(json.dumps(rec) + "\n")
    return rec


LIVE_DONE = DATA / "live_done.json"
ARCH_DONE = DATA / "arch_done.json"


def _seen_snaps():
    return {(m["url"], m["ts"]) for m in load_snapmeta()}


def _pdf_links(base, links, strip_wb=False):
    out = []
    for href in links:
        full = urljoin(base, href)
        if strip_wb:
            full = re.sub(r"^https?://web\.archive\.org/web/\d+(id_)?/", "", full)
        if re.search(r"\.(pdf|xlsx)(\?|$)", full, re.I) and PRICE_LINK.search(full):
            out.append(full.split("#")[0])
    return out


def live_fetch(url, cid):
    r = wb_get(url, timeout=45, tries=2)
    if r is None or r.status_code != 200 or len(r.content) < 200:
        return [], 0
    text, links, kind = to_text(r, url)
    extra = {"kind": kind}
    lm = r.headers.get("Last-Modified")
    if lm:
        try:
            extra["last_modified"] = dt.datetime.strptime(lm[5:16], "%d %b %Y").strftime("%Y-%m")
        except Exception:
            pass
    save_snapshot(cid, url, dt.datetime.now().strftime("%Y%m%d%H%M%S"), "live", text, extra)
    return [(l, True) for l in (_pdf_links(url, links) if kind == "html" else [])], 1


def archive_fetch(url, cid, seen):
    new_links, n = [], 0
    for row in pick_snapshots(cdx(url)):
        ts, orig = row[1], row[2]
        if (url, ts) in seen:
            continue
        rr = wb_get(f"https://web.archive.org/web/{ts}id_/{orig}", timeout=90, tries=4)
        if rr is None or rr.status_code != 200 or len(rr.content) < 200:
            continue
        text, links, kind = to_text(rr, orig)
        save_snapshot(cid, url, ts, "wayback", text, {"kind": kind})
        seen.add((url, ts))
        n += 1
        if kind == "html":
            new_links += [(l, False) for l in _pdf_links(orig, links, strip_wb=True)]
    if url.lower().split("?")[0].endswith(".pdf") and not FAST_MODE:
        d = url.rsplit("/", 1)[0] + "/"
        rr = wb_get("https://web.archive.org/cdx/search/cdx?" + "&".join([
            "url=" + requests_quote(d), "matchType=prefix", f"from={CDX_FROM}", "output=json", "filter=statuscode:200",
            "filter=mimetype:application/pdf", "collapse=urlkey", "limit=400"]), timeout=90)
        try:
            rows = rr.json()[1:] if rr is not None and rr.status_code == 200 and rr.text.strip() else []
        except Exception:
            rows = []
        for row in rows:
            if PRICE_LINK.search(row[2]) or re.search(r"ngs|seq|genom", row[2], re.I):
                new_links.append((row[2], False))
    return new_links, n


def _register_links(cid, links, via):
    with _lock:
        reg = load_registry()
        k = sum(1 for m in reg["urls"].values() if m["core_id"] == cid and str(m.get("via", "")).startswith("link:"))
        for lu, cur in links:
            if lu in reg["urls"] or k >= 12:
                continue
            k += 1
            reg["urls"][lu] = {"core_id": cid, "type": "pdf", "current": cur, "public": True, "as_of": None,
                               "via": f"link:{via[:80]}"}
        write_json(REGISTRY, reg)


def primary_urls(reg):
    """FAST_MODE: one main rate page per core: the URL (not a discovered link, if possible) whose live copy yielded the
    most extracted price lines; ties go to web rate pages over PDFs. Cores with no priced URL fall back to their first
    discovered rate page."""
    lines_by_url = {}
    for sm in load_snapmeta():
        if sm.get("source") != "live" or not sm.get("rel_hash"):
            continue
        ex = extraction_for(sm["rel_hash"])
        n = len(ex.get("lines") or []) if ex else 0
        lines_by_url[sm["url"]] = max(lines_by_url.get(sm["url"], 0), n)
    best = {}
    for u, m in reg["urls"].items():
        if not m.get("public", True):
            continue
        key = (lines_by_url.get(u, 0) > 0, not str(m.get("via", "")).startswith("link:"), lines_by_url.get(u, 0),
               m.get("type") == "rate_page", bool(m.get("current", True)))
        cid = m["core_id"]
        if cid not in best or key > best[cid][0]:
            best[cid] = (key, u)
    return {u for _, u in best.values()}


def extractor_loop(done_evt):
    """Runs Haiku extraction on new snapshot texts while the slow archive harvest continues."""
    while not done_evt.is_set():
        try:
            phase_extract(quiet=True)
        except Exception as e:
            log(f"  background extract error: {e!r}")
        done_evt.wait(120)


CC_DONE = DATA / "cc_done.json"
_cc_lock = threading.Lock()
_cc_last = 0.0


def cc_get(url, headers=None, timeout=90, tries=3):
    """Common Crawl index/data requests: request starts spaced >=1.2 s apart, backoff on 503/429 ('slow down')."""
    import requests
    global _cc_last
    for k in range(tries):
        with _cc_lock:
            wait = 1.2 - (time.time() - _cc_last)
            if wait > 0:
                time.sleep(wait)
            _cc_last = time.time()
        try:
            r = requests.get(url, headers=dict({"User-Agent": UA}, **(headers or {})), timeout=timeout)
        except Exception:
            time.sleep(10 * (k + 1))
            continue
        if r.status_code in (503, 429, 502, 504):
            time.sleep(30 * (k + 1))
            continue
        return r
    return None


def cc_crawls():
    """One Common Crawl crawl per quarter (the latest in each quarter), from Q3 2024 on."""
    r = cc_get("https://index.commoncrawl.org/collinfo.json", timeout=60)
    by_q = {}
    for c in (r.json() if r is not None and r.status_code == 200 else []):
        m = re.match(r"CC-MAIN-(\d{4})-(\d{2})", c.get("id", ""))
        if not m:
            continue
        y, w = int(m.group(1)), int(m.group(2))
        if (y, w) < (2024, 27):
            continue
        q = f"{y}-Q{min(4, (w - 1) // 13 + 1)}"
        if q not in by_q or c["id"] > by_q[q]:
            by_q[q] = c["id"]
    return sorted(by_q.values())


class _Resp:
    def __init__(self, headers, content):
        self.headers, self.content = headers, content
        self.text = content.decode("utf-8", "replace")


def _dechunk(body):
    out, i = b"", 0
    while True:
        j = body.find(b"\r\n", i)
        if j < 0:
            break
        try:
            n = int(body[i:j].split(b";")[0], 16)
        except ValueError:
            return body
        if n == 0:
            break
        out += body[j + 2:j + 2 + n]
        i = j + 2 + n + 2
    return out or body


def cc_record(j):
    import gzip
    import zlib
    off, ln = int(j["offset"]), int(j["length"])
    rr = cc_get("https://data.commoncrawl.org/" + j["filename"], headers={"Range": f"bytes={off}-{off + ln - 1}"})
    if rr is None or rr.status_code not in (200, 206):
        return None
    try:
        raw = gzip.decompress(rr.content)
    except Exception:
        return None
    parts = raw.split(b"\r\n\r\n", 2)
    if len(parts) < 3:
        return None
    head = parts[1].decode("latin-1", "replace")
    body = parts[2]
    hdrs = {}
    for line in head.split("\r\n")[1:]:
        if ":" in line:
            k, v = line.split(":", 1)
            hdrs[k.strip().title()] = v.strip()
    if "chunked" in hdrs.get("Transfer-Encoding", "").lower():
        body = _dechunk(body)
    if "gzip" in hdrs.get("Content-Encoding", "").lower():
        try:
            body = zlib.decompress(body, 16 + zlib.MAX_WBITS)
        except Exception:
            pass
    return _Resp(hdrs, body)


def cc_fetch(url, cid, crawls, seen):
    from urllib.parse import quote
    n = 0
    for cr in crawls:
        r = cc_get(f"https://index.commoncrawl.org/{cr}-index?url={quote(url.split('#')[0], safe='')}&output=json")
        if r is None or r.status_code != 200 or not r.text.strip():
            continue
        rows = []
        for line in r.text.strip().splitlines():
            try:
                rows.append(json.loads(line))
            except Exception:
                pass
        rows = [x for x in rows if str(x.get("status")) == "200"]
        if not rows:
            continue
        j = rows[-1]
        ts = j["timestamp"]
        if (url, ts) in seen:
            continue
        resp = cc_record(j)
        if resp is None or len(resp.content) < 200:
            continue
        text, _links, kind = to_text(resp, url)
        save_snapshot(cid, url, ts, "commoncrawl", text, {"kind": kind, "crawl": cr})
        seen.add((url, ts))
        n += 1
    return n


def cc_loop(stop_evt):
    """Second, independent history source (Common Crawl), run alongside the Wayback pass on the same main pages."""
    try:
        crawls = cc_crawls()
    except Exception as e:
        log(f"  common crawl unavailable: {e!r}")
        return
    log(f"common crawl: {len(crawls)} quarterly crawls ({', '.join(crawls)})")
    if not crawls:
        return
    done = set(read_json(CC_DONE, []))
    reg = load_registry()
    todo = [u for u in (primary_urls(reg) if FAST_MODE else reg["urls"]) if u not in done]
    log(f"common crawl: {len(todo)} URLs to check")
    seen = _seen_snaps()

    def one(u):
        if stop_evt.is_set() and False:
            return
        cid = reg["urls"][u]["core_id"]
        try:
            n = cc_fetch(u, cid, crawls, seen)
        except Exception as e:
            log(f"  cc error {u[:100]}: {e!r}")
            n = 0
        with _lock:
            done.add(u)
            write_json(CC_DONE, sorted(done))
        log(f"  [cc {len(done)}] {n} common-crawl snapshots: {u[:110]}")
        update_state(lambda s: s.update(cc_done=len(done)))

    with ThreadPoolExecutor(max_workers=3) as ex:
        list(ex.map(one, todo))
    log(f"common crawl complete: {len(done)} URLs")


def phase_harvest():
    live_done = set(read_json(LIVE_DONE, []))
    arch_done = set(read_json(ARCH_DONE, []))
    done_evt = threading.Event()
    ext = threading.Thread(target=extractor_loop, args=(done_evt,), daemon=True)
    ext.start()
    cct = threading.Thread(target=cc_loop, args=(done_evt,), daemon=True)
    cct.start()
    try:
        for rnd in range(3):
            reg = load_registry()
            urls = [u for u, m in reg["urls"].items() if m.get("public", True)]
            todo_live = [u for u in urls if u not in live_done]
            log(f"harvest round {rnd + 1}: live pass over {len(todo_live)} URLs")

            def lw(u):
                cid = load_registry()["urls"][u]["core_id"]
                try:
                    links, n = live_fetch(u, cid)
                except Exception as e:
                    log(f"  live error {u[:100]}: {e!r}")
                    links, n = [], 0
                if links and rnd < 2:
                    _register_links(cid, links, u)
                with _lock:
                    live_done.add(u)
                    write_json(LIVE_DONE, sorted(live_done))
            with ThreadPoolExecutor(max_workers=6) as ex:
                list(ex.map(lw, todo_live))
            reg = load_registry()
            todo_arch = [u for u, m in reg["urls"].items() if m.get("public", True) and u not in arch_done]
            if FAST_MODE:
                prim = primary_urls(reg)
                todo_arch = [u for u in todo_arch if u in prim]
                update_state(lambda s, n=len(prim): s.update(fast_mode=True, primary_urls=n))
            if not todo_arch and not [u for u in reg["urls"] if u not in live_done]:
                break
            log(f"harvest round {rnd + 1}: archive pass over {len(todo_arch)} URLs (serialized, ~10 req/min)")
            seen = _seen_snaps()
            blocked_since = None
            for i, u in enumerate(todo_arch):
                cid = reg["urls"][u]["core_id"]
                while True:
                    try:
                        links, n = archive_fetch(u, cid, seen)
                        blocked_since = None
                        break
                    except WaybackBlocked:
                        # Do not mark the URL done: wait out the block (wb_get's pause) and retry the same URL.
                        blocked_since = blocked_since or time.time()
                        if time.time() - blocked_since > WB_GIVE_UP_H * 3600:
                            break
                        update_state(lambda s: None)
                        continue
                    except Exception as e:
                        log(f"  archive error {u[:100]}: {e!r}")
                        links, n = [], 0
                        break
                if blocked_since and time.time() - blocked_since > WB_GIVE_UP_H * 3600:
                    log(f"archive.org blocked for {WB_GIVE_UP_H}h straight: giving up on archive history for the "
                        f"remaining {len(todo_arch) - i} URLs (current prices and dated documents still used)")
                    update_state(lambda s: s.update(archive_gave_up=now()))
                    break
                log(f"  [{i + 1}/{len(todo_arch)}] {n} archived snapshots: {u[:110]}")
                if links and rnd < 2 and not FAST_MODE:
                    _register_links(cid, links, u)
                arch_done.add(u)
                write_json(ARCH_DONE, sorted(arch_done))
                update_state(lambda s: s.update(harvest_done=len(arch_done), live_done=len(live_done)))
        log("wayback pass finished; waiting for common crawl to finish")
        while cct.is_alive():
            cct.join(timeout=300)
            update_state(lambda s: None)
    finally:
        done_evt.set()
        ext.join(timeout=1200)
    log(f"harvest complete: {len(live_done)} live, {len(arch_done)} archive URLs processed")


def load_snapmeta():
    out = []
    if SNAPMETA.exists():
        for ln in SNAPMETA.read_text(encoding="utf-8").splitlines():
            try:
                out.append(json.loads(ln))
            except Exception:
                pass
    return out


# ------------------------------------------------------------------------------ phase: extract

def extraction_for(h):
    v = VERI / f"{h}.json"
    if v.exists():
        return read_json(v, None)
    e = EXTR / f"{h}.json"
    return read_json(e, None) if e.exists() else None


def extract_one(item):
    h, snap, url, core = item
    out = EXTR / f"{h}.json"
    if out.exists() or stopped():
        return
    text = (SNAPS / f"{h}.txt").read_text(encoding="utf-8")
    prompt = EXTRACT_PROMPT.format(snap=snap, url=url, core=core, text=text)
    res, cost = call_claude(prompt, "haiku", [], TIMEOUT["haiku"], BUDGET["haiku"], min_len=10)
    add_cost(cost)
    j = extract_json(res or "", "{")
    if j is None:
        j = {"lines": [], "error": "unparseable", "raw": (res or "")[:2000]}
    j["_model"] = "haiku"
    write_json(out, j)
    update_state(lambda s: s.update(extract_done=s.get("extract_done", 0) + 1))


def phase_extract(quiet=False):
    reg = load_registry()
    seen, items = set(), []
    for sm in load_snapmeta():
        h = sm.get("rel_hash")
        if not h or h in seen:
            continue
        seen.add(h)
        c = reg["cores"].get(sm["core_id"], {})
        items.append((h, sm["ts"][:8], sm["url"], f"{c.get('institution')} / {c.get('core')}"))
    todo = [i for i in items if not (EXTR / f"{i[0]}.json").exists()]
    update_state(lambda s: s.update(extract_total=len(items)))
    if todo or not quiet:
        log(f"extract: {len(items)} distinct texts, {len(todo)} to do (haiku)")
    with ThreadPoolExecutor(max_workers=CONCURRENCY) as ex:
        list(ex.map(extract_one, todo))
    if not quiet:
        log("extract complete")


# ------------------------------------------------------------------------------ $/Gb maths

def specs_now():
    st = load_state()
    return st.get("specs") or {k: dict(v, source="default", note="") for k, v in SPECS.items()}


def fam(fc):
    return re.match(r"[A-Z]+", fc or "").group(0) if fc else ""


def to_gb(line, specs):
    """Returns (gb_per_price_unit, basis, cycle_bucket) or (None, reason, bucket)."""
    fc = line.get("platform_fc")
    unit = (line.get("unit") or "").lower()
    cyc = line.get("total_cycles")
    try:
        cyc = int(float(cyc)) if cyc not in (None, "") else None
    except Exception:
        cyc = None
    rc = str(line.get("read_config") or "")
    m = re.match(r"\s*(\d)\s*x\s*(\d+)", rc, re.I)
    if cyc is None and m:
        cyc = int(m.group(1)) * int(m.group(2))
    if fc and fc.startswith("UG"):
        bucket = "std"
    else:
        bucket = str(cyc) if cyc else "300?"
        if cyc and 290 <= cyc <= 320:
            bucket = "300"
    if bucket == "300?":
        bucket = "300" if not rc else "unk"
    qty = line.get("quantity") or 1
    try:
        qty = float(qty)
    except Exception:
        qty = 1.0
    if qty <= 0:
        qty = 1.0
    spec = specs.get(fc)
    scale = (cyc / 300.0) if (cyc and not fc.startswith("UG")) else 1.0
    # Core-stated output wins.
    v, u = line.get("stated_output_value"), (line.get("stated_output_unit") or "")
    try:
        v = float(v) if v not in (None, "") else None
    except Exception:
        v = None
    nominal = {"NSX_1.5B": 1.5, "NSX_5B": 5, "NSX_10B": 10, "NSX_25B": 25, "NSX_35B": 35}.get(fc)
    if v and nominal and u in ("B_reads", "B_pairs", "M_reads", "M_pairs") and abs(v * (1 if u[0] == "B" else 1e-3) - nominal) < 1e-6:
        v = None  # the flow-cell name, not a stated output
    if v and u and u != "null" and unit not in ("per_gb", "per_million_reads"):
        cyc_eff = cyc or 300
        if u == "Gb":
            return v, "core-stated output (Gb)", bucket
        if u == "Tb":
            return v * 1000, "core-stated output (Tb)", bucket
        mult = 1e6 if u.startswith("M_") else 1e9
        n = v * mult
        if u.endswith("pairs") or u.endswith("clusters"):
            return n * cyc_eff / 1e9, f"core-stated output ({u}, x{cyc_eff} bases)", bucket
        if u.endswith("reads"):
            half = n * (cyc_eff / 2) / 1e9
            full = n * cyc_eff / 1e9
            if spec:
                exp = spec["gb"] * scale * (qty / spec["lanes"] if unit == "lane" else 1)
                pick = half if abs(half - exp) <= abs(full - exp) else full
            else:
                pick = half
            return pick, f"core-stated output ({u}; read count interpreted {'as single reads' if pick == half else 'as pairs'})", bucket
    if unit == "per_gb":
        return 1.0, "listed per Gb", bucket
    if unit == "per_million_reads":
        bases = (cyc or 300) if not fc.startswith("UG") else 300
        return bases / 1000.0, f"listed per million reads (x{bases} bases)", bucket
    if not spec:
        return None, "no output spec", bucket
    if unit == "lane":
        return spec["gb"] * scale * qty / spec["lanes"], f"manufacturer spec {spec['gb']:.0f} Gb / {spec['lanes']} lanes", bucket
    if unit in ("flow_cell", "wafer", "run"):
        return spec["gb"] * scale * qty, f"manufacturer spec {spec['gb']:.0f} Gb per {unit}", bucket
    return None, f"unit '{unit}' not convertible", bucket


def ym(s):
    if not s or not isinstance(s, str):
        return None
    m = re.match(r"(\d{4})-(\d{1,2})", s.strip())
    if not m or not (1 <= int(m.group(2)) <= 12):
        return None
    return f"{m.group(1)}-{int(m.group(2)):02d}"


def months(a, b):
    y, m = map(int, a.split("-"))
    out = []
    while f"{y}-{m:02d}" <= b:
        out.append(f"{y}-{m:02d}")
        m += 1
        if m > 12:
            y, m = y + 1, 1
    return out


MONTHS = months(WINDOW_START, WINDOW_END)


def build_long():
    """Every extracted price line from every snapshot, with $/Gb and month observations."""
    import pandas as pd
    reg = load_registry()
    specs = specs_now()
    rows = []
    for sm in load_snapmeta():
        h = sm.get("rel_hash")
        if not h:
            continue
        ex = extraction_for(h)
        if not ex or not isinstance(ex.get("lines"), list):
            continue
        c = reg["cores"].get(sm["core_id"], {})
        snap_m = f"{sm['ts'][:4]}-{sm['ts'][4:6]}"
        eff_from, eff_to = ym(ex.get("effective_from")), ym(ex.get("effective_to"))
        doc_m = ym(ex.get("document_date")) or eff_from
        if sm.get("source") == "live" and sm.get("kind") == "pdf" and not doc_m and sm.get("last_modified"):
            doc_m = sm["last_modified"]
        for ln in ex["lines"]:
            if not isinstance(ln, dict) or ln.get("platform_fc") not in SPECS:
                continue
            try:
                price = float(str(ln.get("price")).replace(",", ""))
            except Exception:
                continue
            if price <= 0:
                continue
            cur = (ln.get("currency") or "USD").upper().strip()
            fx = FX.get(cur)
            gb, basis, bucket = to_gb(ln, specs)
            usd = price * fx if fx else None
            upg = (usd / gb) if (usd and gb) else None
            rows.append({
                "core_id": sm["core_id"], "institution": c.get("institution"), "core": c.get("core"), "country": c.get("country"),
                "kind": c.get("kind"), "url": sm["url"], "snapshot_ts": sm["ts"], "snapshot_month": snap_m,
                "source": sm["source"], "url_current": reg["urls"].get(sm["url"], {}).get("current", True),
                "doc_month": doc_m, "effective_from": eff_from, "effective_to": eff_to,
                "fiscal_year": ex.get("fiscal_year_label"), "extracted_by": ex.get("_model", "haiku"), "rel_hash": h,
                "platform_fc": ln["platform_fc"], "flow_cell_raw": ln.get("flow_cell_raw"), "unit": ln.get("unit"),
                "quantity": ln.get("quantity"), "read_config": ln.get("read_config"), "total_cycles": ln.get("total_cycles"),
                "cycle_bucket": bucket, "tier": (ln.get("tier") or "unspecified").lower(), "tier_raw": ln.get("tier_raw"),
                "price_local": price, "currency": cur, "fx_usd": fx, "price_usd": usd,
                "lib_prep_bundled": bool(ln.get("includes_library_prep")),
                "stated_output": f"{ln.get('stated_output_value')} {ln.get('stated_output_unit')}" if ln.get("stated_output_value") else "",
                "gb_per_unit": gb, "output_basis": basis, "usd_per_gb": upg, "line_quote": (ln.get("line_quote") or "")[:200],
            })
    df = pd.DataFrame(rows)
    if df.empty:
        return df
    df = df.drop_duplicates(subset=["core_id", "snapshot_ts", "platform_fc", "unit", "quantity", "cycle_bucket", "tier",
                                    "price_local", "currency", "lib_prep_bundled"])
    df["tier_group"] = df["tier"].map(lambda t: "internal" if t in ("internal", "unspecified") else
                                      ("external" if t == "external_academic" else "commercial"))
    lo_hi = df["platform_fc"].map(lambda f: BAND.get(fam(f), HARD))
    df["implausible"] = [(u is not None and u == u and not (b[0] <= u <= b[1])) for u, b in zip(df["usd_per_gb"], lo_hi)]
    df["excluded"] = [(u is None or u != u or not (HARD[0] <= u <= HARD[1])) for u in df["usd_per_gb"]]
    return df


def observation_months(r):
    """[(month, flag)] with flag O (seen in a snapshot that month) or D (inside the document's stated effective period)."""
    snap, ef, et = r["snapshot_month"], r["effective_from"], r["effective_to"]
    out = []
    if r["source"] == "live" and not r["url_current"]:
        # A superseded document still hosted today says nothing about today's price.
        snap = None
    if snap and et and snap > et:
        snap = None
    if snap:
        out.append((snap, "O"))
    if ef:
        end = snap or et or ef
        for m in months(ef, end):
            if m != snap:
                out.append((m, "D"))
    elif not snap and et:
        out.append((et, "D"))
    if not out and r.get("doc_month"):
        out.append((r["doc_month"], "D"))
    return out


UNIT_PREF = {"lane": 0, "flow_cell": 1, "wafer": 1, "run": 2, "per_gb": 3, "per_million_reads": 4}


def grids(df):
    """Returns {table_key: {"values": {core_id: {month: usd_per_gb}}, "flags": ..., "local": ...}}"""
    tables = {}
    use = df[~df["excluded"] & df["usd_per_gb"].notna() & (df["tier_group"] != "commercial")]
    for _, r in use.iterrows():
        key = (r["platform_fc"], r["tier_group"], bool(r["lib_prep_bundled"]), r["cycle_bucket"])
        q = r["quantity"]
        try:
            qpref = 0 if float(q or 1) == 1 else 1
        except Exception:
            qpref = 1
        rank_doc = r["doc_month"] or r["effective_from"] or r["snapshot_month"]
        for m, flag in observation_months(r):
            if m > WINDOW_END:
                continue
            cand = (rank_doc, 1 if flag == "O" else 0, -UNIT_PREF.get(r["unit"], 5), -qpref, r["snapshot_ts"])
            t = tables.setdefault(key, {})
            cell = t.setdefault(r["core_id"], {})
            if m not in cell or cand > cell[m][0]:
                cell[m] = (cand, r["usd_per_gb"], flag, f"{r['price_local']:,.0f} {r['currency']}/{r['unit']}"
                           f"{'' if qpref == 0 else ' x' + str(q)}", r["url"], r["output_basis"])
    out = {}
    for key, cores in tables.items():
        vals, flags, local, srcs = {}, {}, {}, {}
        for cid, cell in cores.items():
            seq = sorted(cell)
            last = None
            v, f, l = {}, {}, {}
            pre = [m for m in seq if m < WINDOW_START]
            if pre:
                last = cell[pre[-1]]
            for m in MONTHS:
                if m in cell:
                    last = cell[m]
                    v[m], f[m], l[m] = last[1], last[2], last[3]
                elif last is not None:
                    v[m], f[m], l[m] = last[1], "C", last[3]
            if v:
                vals[cid], flags[cid], local[cid] = v, f, l
                srcs[cid] = sorted({x[4] for x in cell.values()}), sorted({x[5] for x in cell.values()})
        if vals:
            out[key] = {"values": vals, "flags": flags, "local": local, "sources": srcs}
    return out


# ------------------------------------------------------------------------------ phase: verify

def phase_verify():
    st = load_state()
    if "verify" in st.get("phases_done", []):
        return
    df = build_long()
    reasons = {}
    if not df.empty:
        for h, g in df.groupby("rel_hash"):
            if g["implausible"].any():
                bad = g[g["implausible"]].iloc[0]
                reasons[h] = (f"implausible $/Gb {bad['usd_per_gb']:.2f} for {bad['platform_fc']} "
                              f"({bad['price_local']} {bad['currency']} per {bad['unit']} x{bad['quantity']})")
        # Same core, flow cell, tier, cycles, unit and snapshot month but prices that differ by >5% across documents.
        k = ["core_id", "platform_fc", "tier_group", "cycle_bucket", "unit", "snapshot_month", "lib_prep_bundled"]
        for _, g in df[df["usd_per_gb"].notna()].groupby(k):
            if g["rel_hash"].nunique() > 1 and g["usd_per_gb"].max() > 1.05 * g["usd_per_gb"].min():
                for h in g["rel_hash"].unique():
                    reasons.setdefault(h, "conflicts with another document from the same core in the same month")
    # Pages with many keyword+price lines but nothing extracted.
    extracted = set(df["rel_hash"]) if not df.empty else set()
    for sm in load_snapmeta():
        h = sm.get("rel_hash")
        if not h or h in extracted or h in reasons:
            continue
        ex = extraction_for(h)
        if ex is None:
            continue
        t = (SNAPS / f"{h}.txt").read_text(encoding="utf-8")
        strong = sum(1 for ln in t.split("\n") if re.search(r"novaseq|aviti|ultima|ug ?100|\b(10|25|1\.5|5)b\b", ln, re.I)
                     and PRICEISH.search(ln))
        if strong >= 3:
            reasons[h] = f"no prices extracted although {strong} lines mention a platform and a price"
    items = list(reasons.items())[:MAX_VERIFY]
    log(f"verify: {len(reasons)} pages flagged, re-checking {len(items)} with sonnet")
    schema = EXTRACT_PROMPT.split("TEXT:")[0]
    snapinfo = {}
    for sm in load_snapmeta():
        if sm.get("rel_hash"):
            snapinfo.setdefault(sm["rel_hash"], (sm["ts"][:8], sm["url"]))

    def one(it):
        h, reason = it
        if (VERI / f"{h}.json").exists() or load_state()["cost_usd"] >= VERIFY_CAP_USD or load_state().get("stop"):
            return
        first = (EXTR / f"{h}.json").read_text(encoding="utf-8") if (EXTR / f"{h}.json").exists() else "{}"
        snap, url = snapinfo.get(h, ("?", "?"))
        prompt = VERIFY_PROMPT.format(reason=reason, schema=schema, first=first[:12000], snap=snap, url=url,
                                      text=(SNAPS / f"{h}.txt").read_text(encoding="utf-8"))
        res, cost = call_claude(prompt, "sonnet", [], TIMEOUT["sonnet"], BUDGET["sonnet"], min_len=10)
        total = add_cost(cost)
        j = extract_json(res or "", "{")
        if j is not None and isinstance(j.get("lines"), list):
            j["_model"] = "sonnet-verified"
            j["_reason"] = reason
            write_json(VERI / f"{h}.json", j)
        log(f"  verified {h} ({'ok' if j else 'unparsed'}; ${cost:.2f}; job ${total:.2f})")

    with ThreadPoolExecutor(max_workers=CONCURRENCY) as ex:
        list(ex.map(one, items))
    update_state(lambda s: s["phases_done"].append("verify"))


# ------------------------------------------------------------------------------ phase: build outputs

def short_name(c):
    inst = c.get("institution") or "?"
    core = c.get("core") or ""
    inst = (inst.replace("University of ", "U ").replace("University", "U").replace("Institute", "Inst.")
            .replace("College", "Coll.").replace("  ", " "))
    s = inst if len(inst) <= 28 else inst[:27] + "."
    core_short = re.sub(r"\b(Core|Facility|Facilities|Center|Centre|Shared Resource|Laboratory|The)\b", "", core).strip(" -/,")
    if core_short and len(s) < 34:
        s += " - " + core_short[: 40 - len(s)]
    return s.strip()


def table_name(key):
    fc, tier, lp, bucket = key
    nm = FC_LABEL.get(fc, fc)
    parts = [nm, "internal/academic rate" if tier == "internal" else "external academic rate"]
    if lp:
        parts.append("library prep bundled")
    if bucket not in ("300", "std"):
        parts.append(f"{bucket} cycles")
    return ", ".join(parts)


def sheet_name(key, appendix):
    fc, tier, lp, bucket = key
    s = ("App_" if appendix else "") + ("LP_" if lp else "") + fc.replace("NSX_", "X").replace("NS6000_", "6000_") \
        .replace("NS2000_", "NS2K_").replace("_WAFER", "") + ("_int" if tier == "internal" else "_ext")
    if bucket not in ("300", "std"):
        s += f"_{bucket}c"
    return s[:31]


def phase_build():
    import pandas as pd
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from openpyxl import Workbook
    from openpyxl.chart import LineChart, Reference
    from openpyxl.styles import Alignment, Font, PatternFill
    from openpyxl.utils import get_column_letter

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "charts").mkdir(exist_ok=True)
    reg = load_registry()
    specs = specs_now()
    df = build_long()
    if df.empty:
        log("build: no price lines extracted; nothing to build")
        return
    df.to_csv(OUT_DIR / "long_all_price_lines.csv", index=False, encoding="utf-8-sig")
    G = grids(df)

    def n_obs(t):
        return sum(1 for cid in t["flags"] if any(f in ("O", "D") for f in t["flags"][cid].values()))

    keys = sorted(G, key=lambda k: (FC_ORDER.index(k[0]) if k[0] in FC_ORDER else 99, k[2], k[1] != "internal",
                                    k[3] not in ("300", "std"), k[3]))
    main, appendix = [], []
    for k in keys:
        n = len(G[k]["values"])
        std = k[3] in ("300", "std")
        if (not k[2]) and std and (n >= 8 or k[0] in ALWAYS_MAIN):
            main.append(k)
        elif k[2] and std and n >= 8:
            main.append(k)
        elif (not std) and n >= 8:
            main.append(k)
        elif std:
            appendix.append(k)
        # non-300-cycle series with fewer than 8 cores stay in Long_data only
    log(f"build: {len(main)} main tables, {len(appendix)} appendix tables")

    wb = Workbook()
    wsS = wb.active
    wsS.title = "Summary"
    wsR = wb.create_sheet("README")
    bold, grey = Font(bold=True), Font(italic=True, color="808080")
    hdr_fill = PatternFill("solid", fgColor="DDEBF7")
    summary_rows, coverage = [], []

    def write_table(k, appendix_flag):
        t = G[k]
        cids = sorted(t["values"], key=lambda c: short_name(reg["cores"].get(c, {})))
        names = [short_name(reg["cores"].get(c, {"institution": c})) for c in cids]
        # make names unique
        seen = {}
        for i, n in enumerate(names):
            if n in seen:
                seen[n] += 1
                names[i] = f"{n} ({seen[n]})"
            else:
                seen[n] = 1
        sname = sheet_name(k, appendix_flag)
        ws = wb.create_sheet(sname)
        fc = k[0]
        sp = specs.get(fc, {})
        thin = len(cids) < 8
        ws["A1"] = f"{table_name(k)}: $/Gb charged by academic core facilities, monthly" + ("  [THIN COVERAGE]" if thin else "")
        ws["A1"].font = Font(bold=True, size=13)
        ws["A2"] = (f"USD per Gb sequenced. Output basis: manufacturer max spec {sp.get('gb', '?')} Gb per "
                    f"{'wafer' if fc.startswith('UG') else 'flow cell'} ({sp.get('lanes', '?')} lane(s)) at "
                    f"{'standard read length' if fc.startswith('UG') else '2x150 / 300 cycles'}, unless the core states its own "
                    f"output (see Long data, column output_basis). Sequencing only" + (" incl. bundled library prep" if k[2] else "")
                    + f". Cores with data: {len(cids)}.")
        ws["A3"] = ("Cell style: BOLD = observed in a snapshot that month (O); normal = within the price list's stated "
                    "effective period (D); grey italic = carried forward from the last observation (C). Blank = no data yet. "
                    "Flags grid and local-currency prices are below the chart data.")
        for a in ("A2", "A3"):
            ws[a].alignment = Alignment(wrap_text=False)
        hr = 5
        ws.cell(hr, 1, "Month").font = bold
        for j, n in enumerate(names):
            c = ws.cell(hr, 2 + j, n)
            c.font = bold
            c.fill = hdr_fill
            c.alignment = Alignment(wrap_text=True, vertical="top")
        for i, m in enumerate(MONTHS):
            ws.cell(hr + 1 + i, 1, m)
            for j, cid in enumerate(cids):
                v = t["values"][cid].get(m)
                if v is None:
                    continue
                f = t["flags"][cid][m]
                c = ws.cell(hr + 1 + i, 2 + j, round(v, 3))
                c.number_format = "$#,##0.00"
                c.font = bold if f == "O" else (grey if f == "C" else Font())
        # flags grid and local prices
        r0 = hr + len(MONTHS) + 3
        ws.cell(r0, 1, "Flags (O observed, D document-dated, C carried)").font = bold
        r1 = r0 + len(MONTHS) + 3
        ws.cell(r1, 1, "Local-currency price and unit behind each value").font = bold
        for j, n in enumerate(names):
            ws.cell(r0 + 1, 2 + j, n).font = bold
            ws.cell(r1 + 1, 2 + j, n).font = bold
        for i, m in enumerate(MONTHS):
            ws.cell(r0 + 2 + i, 1, m)
            ws.cell(r1 + 2 + i, 1, m)
            for j, cid in enumerate(cids):
                f = t["flags"][cid].get(m)
                if f:
                    ws.cell(r0 + 2 + i, 2 + j, f)
                    ws.cell(r1 + 2 + i, 2 + j, t["local"][cid].get(m))
        rs = r1 + len(MONTHS) + 4
        ws.cell(rs, 1, "Sources (URLs) and output basis per core").font = bold
        for j, cid in enumerate(cids):
            urls, bases = t["sources"][cid]
            ws.cell(rs + 1 + j, 1, names[j])
            ws.cell(rs + 1 + j, 2, "; ".join(bases))
            ws.cell(rs + 1 + j, 3, " ; ".join(urls))
        ws.column_dimensions["A"].width = 12
        for j in range(len(cids)):
            ws.column_dimensions[get_column_letter(2 + j)].width = 16
        ws.row_dimensions[hr].height = 60
        ws.freeze_panes = ws.cell(hr + 1, 2)
        # native chart
        ch = LineChart()
        ch.title = table_name(k)
        ch.y_axis.title = "$/Gb"
        ch.x_axis.title = "Month"
        ch.height, ch.width = 13, 30
        data = Reference(ws, min_col=2, min_row=hr, max_col=1 + len(cids), max_row=hr + len(MONTHS))
        ch.add_data(data, titles_from_data=True)
        ch.set_categories(Reference(ws, min_col=1, min_row=hr + 1, max_row=hr + len(MONTHS)))
        ch.display_blanks = "gap"
        ws.add_chart(ch, f"{get_column_letter(len(cids) + 3)}5")
        # CSVs
        grid = pd.DataFrame({names[j]: [t["values"][cid].get(m) for m in MONTHS] for j, cid in enumerate(cids)}, index=MONTHS)
        grid.index.name = "month"
        flags = pd.DataFrame({names[j]: [t["flags"][cid].get(m) for m in MONTHS] for j, cid in enumerate(cids)}, index=MONTHS)
        flags.index.name = "month"
        grid.round(3).to_csv(OUT_DIR / f"{sname}_usd_per_gb.csv", encoding="utf-8-sig")
        flags.to_csv(OUT_DIR / f"{sname}_flags.csv", encoding="utf-8-sig")
        # PNG
        fig, ax = plt.subplots(figsize=(13, 6.5))
        x = list(range(len(MONTHS)))
        for j, cid in enumerate(cids):
            ys = [t["values"][cid].get(m) for m in MONTHS]
            ax.plot(x, [y if y is not None else float("nan") for y in ys], lw=1.1, alpha=0.75, label=names[j])
            ox = [i for i, m in enumerate(MONTHS) if t["flags"][cid].get(m) in ("O", "D")]
            ax.scatter(ox, [t["values"][cid][MONTHS[i]] for i in ox], s=12)
        med = grid.median(axis=1, skipna=True)
        ax.plot(x, med.values, color="black", lw=3, label="Median")
        ax.set_xticks(x[::2])
        ax.set_xticklabels(MONTHS[::2], rotation=45, ha="right")
        ax.set_ylabel("USD per Gb")
        ax.set_title(f"{table_name(k)} ({len(cids)} cores; dots = observed/document-dated, lines carry forward)")
        ax.grid(alpha=0.3)
        if len(cids) <= 30:
            ax.legend(fontsize=6.5, ncol=2, loc="center left", bbox_to_anchor=(1.0, 0.5))
        fig.tight_layout()
        fig.savefig(OUT_DIR / "charts" / f"{sname}.png", dpi=130)
        plt.close(fig)
        # summary
        for m in MONTHS:
            vals = grid.loc[m].dropna()
            obs = sum(1 for cid in cids if t["flags"][cid].get(m) in ("O", "D"))
            summary_rows.append({"table": sname, "description": table_name(k), "month": m, "cores_with_value": len(vals),
                                 "cores_observed_this_month": obs,
                                 "median": vals.median() if len(vals) else None, "p25": vals.quantile(.25) if len(vals) else None,
                                 "p75": vals.quantile(.75) if len(vals) else None, "min": vals.min() if len(vals) else None,
                                 "max": vals.max() if len(vals) else None})
        n_o = sum(1 for cid in cids for f in t["flags"][cid].values() if f == "O")
        n_d = sum(1 for cid in cids for f in t["flags"][cid].values() if f == "D")
        n_c = sum(1 for cid in cids for f in t["flags"][cid].values() if f == "C")
        first_last = []
        for cid in cids:
            v = t["values"][cid]
            ms = sorted(v)
            if len(ms) >= 2 and v[ms[0]]:
                first_last.append(v[ms[-1]] / v[ms[0]] - 1)
        coverage.append({"sheet": sname, "table": table_name(k), "appendix": appendix_flag, "cores": len(cids),
                         "observed_cells": n_o, "document_dated_cells": n_d, "carried_cells": n_c,
                         "cores_with_any_price_change": sum(1 for x in first_last if abs(x) > 0.005),
                         "median_change_first_to_last_pct": round(100 * float(pd.Series(first_last).median()), 1) if first_last else None})

    for k in main:
        write_table(k, False)
    for k in appendix:
        write_table(k, True)

    # Summary sheet
    sm = pd.DataFrame(summary_rows)
    sm.to_csv(OUT_DIR / "summary_by_table_month.csv", index=False, encoding="utf-8-sig")
    cov = pd.DataFrame(coverage)
    cov.to_csv(OUT_DIR / "coverage_by_table.csv", index=False, encoding="utf-8-sig")
    wsS["A1"] = "Core-facility $/Gb by flow cell: median across cores, monthly (main tables, internal/academic rates)"
    wsS["A1"].font = Font(bold=True, size=13)
    wsS["A2"] = (f"Built {now()}. Window {WINDOW_START} to {WINDOW_END}. Each value is the median of the cores that have a "
                 f"price that month (observed, document-dated or carried forward). See each sheet for core-level data, "
                 f"the Coverage table below for how much is observed versus carried, and README for method.")
    med_tables = [k for k in main if k[1] == "internal" and not k[2] and k[3] in ("300", "std")]
    hr = 4
    wsS.cell(hr, 1, "Month").font = bold
    for j, k in enumerate(med_tables):
        c = wsS.cell(hr, 2 + j, f"{FC_LABEL.get(k[0], k[0])} (median $/Gb)")
        c.font, c.fill = bold, hdr_fill
        c.alignment = Alignment(wrap_text=True, vertical="top")
    for i, m in enumerate(MONTHS):
        wsS.cell(hr + 1 + i, 1, m)
        for j, k in enumerate(med_tables):
            row = sm[(sm["table"] == sheet_name(k, False)) & (sm["month"] == m)]
            if len(row) and row["median"].notna().iloc[0]:
                c = wsS.cell(hr + 1 + i, 2 + j, round(float(row["median"].iloc[0]), 3))
                c.number_format = "$#,##0.00"
    wsS.row_dimensions[hr].height = 45
    for j in range(len(med_tables) + 1):
        wsS.column_dimensions[get_column_letter(1 + j)].width = 18
    if med_tables:
        ch = LineChart()
        ch.title = "Median core-facility $/Gb by flow cell"
        ch.y_axis.title = "$/Gb"
        ch.height, ch.width = 12, 26
        ch.add_data(Reference(wsS, min_col=2, min_row=hr, max_col=1 + len(med_tables), max_row=hr + len(MONTHS)), titles_from_data=True)
        ch.set_categories(Reference(wsS, min_col=1, min_row=hr + 1, max_row=hr + len(MONTHS)))
        ch.display_blanks = "gap"
        wsS.add_chart(ch, f"{get_column_letter(len(med_tables) + 3)}4")
        fig, ax = plt.subplots(figsize=(12, 6))
        for k in med_tables:
            s = sm[sm["table"] == sheet_name(k, False)].set_index("month")
            ax.plot(range(len(MONTHS)), [s["median"].get(m) for m in MONTHS], lw=2, label=FC_LABEL.get(k[0], k[0]))
        ax.set_xticks(range(0, len(MONTHS), 2))
        ax.set_xticklabels(MONTHS[::2], rotation=45, ha="right")
        ax.set_ylabel("Median USD per Gb")
        ax.set_yscale("log")
        ax.set_title("Median core-facility $/Gb by flow cell (internal/academic rates; log scale)")
        ax.grid(alpha=0.3, which="both")
        ax.legend(fontsize=8)
        fig.tight_layout()
        fig.savefig(OUT_DIR / "charts" / "Summary_medians.png", dpi=130)
        plt.close(fig)
    # range table under the medians
    r0 = hr + len(MONTHS) + 3
    wsS.cell(r0, 1, "Median, interquartile range and min-max by table and month").font = bold
    cols = ["table", "description", "month", "cores_with_value", "cores_observed_this_month", "median", "p25", "p75", "min", "max"]
    for j, cname in enumerate(cols):
        wsS.cell(r0 + 1, 1 + j, cname).font = bold
    for i, row in enumerate(sm[cols].itertuples(index=False)):
        for j, v in enumerate(row):
            c = wsS.cell(r0 + 2 + i, 1 + j, (round(v, 3) if isinstance(v, float) and v == v else (None if isinstance(v, float) else v)))
            if j >= 5:
                c.number_format = "$#,##0.00"
    # coverage on its own sheet
    wsC = wb.create_sheet("Coverage", 1)
    for j, cname in enumerate(cov.columns):
        wsC.cell(1, 1 + j, cname).font = bold
    for i, row in enumerate(cov.itertuples(index=False)):
        for j, v in enumerate(row):
            wsC.cell(2 + i, 1 + j, v)

    # Sources sheet
    wsSrc = wb.create_sheet("Sources")
    snaps = load_snapmeta()
    by_url = {}
    for s in snaps:
        if s.get("rel_hash"):
            by_url.setdefault(s["url"], []).append(s["ts"][:8])
    used_urls = set(df["url"])
    src_rows = []
    for u, meta in reg["urls"].items():
        c = reg["cores"].get(meta["core_id"], {})
        tiers = sorted(set(df[df["url"] == u]["tier"])) if u in used_urls else []
        bases = sorted(set(df[df["url"] == u]["output_basis"])) if u in used_urls else []
        src_rows.append({"core": short_name(c), "institution": c.get("institution"), "core_name": c.get("core"),
                         "country": c.get("country"), "kind": c.get("kind"), "url": u, "url_type": meta.get("type"),
                         "found_via": meta.get("via"), "snapshots_with_price_text": ";".join(sorted(set(by_url.get(u, [])))),
                         "price_lines_extracted": int((df["url"] == u).sum()), "tiers": ";".join(tiers),
                         "output_assumption": " | ".join(bases)})
    srcdf = pd.DataFrame(src_rows).sort_values(["core", "url"])
    srcdf.to_csv(OUT_DIR / "sources.csv", index=False, encoding="utf-8-sig")
    for j, cname in enumerate(srcdf.columns):
        wsSrc.cell(1, 1 + j, cname).font = bold
    for i, row in enumerate(srcdf.itertuples(index=False)):
        for j, v in enumerate(row):
            wsSrc.cell(2 + i, 1 + j, v)

    # Specs and FX
    wsP = wb.create_sheet("Output_specs_FX")
    wsP.append(["flow_cell_code", "label", "gb_per_unit_2x150", "lanes", "gb_per_lane", "source", "note"])
    for k in FC_ORDER:
        v = specs.get(k, {})
        wsP.append([k, FC_LABEL.get(k), v.get("gb"), v.get("lanes"),
                    (v.get("gb") or 0) / (v.get("lanes") or 1), v.get("source"), v.get("note")])
    wsP.append([])
    wsP.append(["currency", "USD per unit (fixed approx. 2026 rate)"])
    for k, v in FX.items():
        wsP.append([k, v])
    pd.DataFrame([{"flow_cell_code": k, **specs.get(k, {})} for k in FC_ORDER]).to_csv(OUT_DIR / "output_specs.csv",
                                                                                         index=False, encoding="utf-8-sig")

    # Long data sheet
    wsL = wb.create_sheet("Long_data")
    cols = list(df.columns)
    wsL.append(cols)
    for row in df.itertuples(index=False):
        wsL.append([(None if (isinstance(v, float) and v != v) else v) for v in row])

    readme = readme_text(df, main, appendix, cov, reg, specs)
    for i, ln in enumerate(readme.split("\n")):
        wsR.cell(1 + i, 1, ln)
    wsR.column_dimensions["A"].width = 160
    for ws in wb.worksheets:
        pass
    wb.save(OUT_XLSX)
    OUT_README.write_text(readme, encoding="utf-8")
    (OUT_DIR / "README.md").write_text(readme, encoding="utf-8")
    log(f"build: wrote {OUT_XLSX.name}, {len(list(OUT_DIR.glob('*.csv')))} CSVs, "
        f"{len(list((OUT_DIR / 'charts').glob('*.png')))} PNGs")


def readme_text(df, main, appendix, cov, reg, specs):
    n_cores = df["core_id"].nunique()
    n_ctry = df["country"].nunique()
    lines = [
        f"# Core-facility sequencing prices: $/Gb by flow cell, monthly, {WINDOW_START} to {WINDOW_END}",
        "",
        f"*Built {now()} by `_Build/core_lab_pricing.py`. Workbook: `{OUT_XLSX.name}`. CSVs and PNG charts: `{OUT_DIR.name}/`.*",
        "",
        "## What this is",
        "",
        "Academic DNA sequencing core facilities (university cores and non-profit institutes such as Broad, Salk, "
        "Dana-Farber and CNAG) publish rate cards that list what they charge for a lane or flow cell of sequencing. "
        "Converting those prices to US dollars per gigabase (Gb, a billion DNA bases read) makes cores and platforms "
        "comparable, and tracking them month by month shows how fast end-user prices are falling.",
        "",
        f"The dataset covers {n_cores} cores in {n_ctry} countries with at least one usable price line. "
        f"There are {len(main)} main tables and {len(appendix)} appendix tables (fewer than 8 cores, or non-standard read lengths).",
        "",
        "## Layout",
        "",
        "- **Summary**: median $/Gb by flow cell by month, plus median, interquartile range and min-max for every table.",
        "- **Coverage**: for each table, the number of cores and how many cells are observed, document-dated or carried forward.",
        "- **One sheet per table**: months down the rows, cores across the columns, values in USD per Gb, with a native "
        "Excel line chart. Below the chart data: a flags grid, the local-currency price and unit behind each value, and "
        "each core's source URLs and output basis. Sheet names: X25B = NovaSeq X 25B, 6000_S4 = NovaSeq 6000 S4, "
        "NS2K = NextSeq 2000, AVITI_* = Element, UG100 = Ultima; `_int` = internal/academic rate, `_ext` = external "
        "academic rate, `LP_` = library prep bundled into the price, `App_` = appendix.",
        "- **Sources**: every URL harvested, the core, the snapshot dates that contained price text, tiers and output assumption.",
        "- **Output_specs_FX**: manufacturer output assumptions and exchange rates.",
        "- **Long_data**: every extracted price line from every snapshot (also `long_all_price_lines.csv`).",
        "",
        "## Method",
        "",
        "1. **Finding cores.** Sonnet web agents searched region by region (US by region, Canada, UK/Ireland, Europe, "
        "Asia-Pacific, non-profit institutes) and by platform (Ultima, Element) for public rate cards, older fiscal-year "
        "price lists and price-change announcements. About 20 rate cards already in this folder seeded the list. "
        "Login-gated rate cards (iLab, CoreSmart, PPMS) were skipped. Commercial providers were excluded.",
        "2. **History.** Every URL was downloaded live (Oct 2026), and PDF price lists linked from live pages were added. "
        "Because the Wayback Machine (web.archive.org) throttled requests heavily, archive history was collected for one "
        "main rate page per core (the page whose live copy carried the most price lines): the last capture of each "
        "quarter since Oct 2024, plus the latest capture before the window. Older price lists found by the search agents "
        "or linked from live pages contribute history through the dates printed on them.",
        "3. **Extraction.** Claude Haiku turned each distinct price-list text into structured lines (flow cell, unit, "
        "read length, user tier, price, currency, library-prep bundling, stated output, effective dates). Claude Sonnet "
        "re-extracted pages whose results were implausible, conflicted with another document from the same core and "
        "month, or found no prices where prices were evident.",
        "4. **$/Gb.** Price in USD divided by the Gb that the price buys. Gb uses the manufacturer's maximum specified "
        "output at 2x150 (300 cycles), divided by lanes for per-lane prices; Ultima uses wafer output. Where the core "
        "states its own output (e.g. '~800M reads per lane'), that is used instead and flagged in `output_basis`. "
        "Main tables use 300-cycle runs only.",
        "5. **Months.** A cell is **O** (observed) if a snapshot from that month shows the price, **D** "
        "(document-dated) if the month falls inside the effective period printed on the price list, and **C** (carried) "
        "if neither, in which case the last observed price is carried forward. Months before a core's first observation "
        "are blank. When two documents disagree for the same month, the more recently dated document wins; snapshots "
        "beat document dates; per-lane prices beat whole-flow-cell prices.",
        "6. **Tiers.** Main tables use internal (own-institution) rates; a price list with a single, unlabelled price "
        "is treated as internal. External academic rates have their own tables. Commercial rates are kept in Long_data "
        "but not tabulated. Tariff surcharges are not added.",
        "",
        "## Caveats",
        "",
        "- **Carried cells are not observations.** Wayback captures some pages monthly and others once or twice a "
        "year, so many cells are carried. Use the flags (or the Coverage sheet) before reading a flat line as 'no "
        "price change'.",
        "- **Manufacturer output is a ceiling.** Real lane yields are often lower, so true $/Gb is somewhat higher than "
        "shown. The bias is similar across cores for the same flow cell, so trends and ranking hold better than levels.",
        "- **Extraction is automated.** Values come from model extraction of messy tables, checked by a second model "
        "only where flagged. Spot-check any value you rely on against the URL in the Sources sheet.",
        "- **Exchange rates are fixed** (approximate 2026 rates in Output_specs_FX), so non-US trends show local-price "
        "changes only. Local prices are kept for reconversion.",
        "- **Core rates are not Illumina's price.** Cores add labour, overhead and subsidy, and some are subsidised by "
        "their institutions. Changes in core prices lag and dampen changes in reagent prices.",
        "",
        "## Coverage by table",
        "",
        "| Sheet | Table | Cores | Observed cells | Document-dated | Carried | Cores with a price change | Median change first-to-last |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for r in cov.itertuples(index=False):
        lines.append(f"| {r.sheet} | {r.table}{' (appendix)' if r.appendix else ''} | {r.cores} | {r.observed_cells} | "
                     f"{r.document_dated_cells} | {r.carried_cells} | {r.cores_with_any_price_change} | "
                     f"{'' if r.median_change_first_to_last_pct is None else str(r.median_change_first_to_last_pct) + '%'} |")
    lines += ["", "## Columns in the CSVs", "",
              "- `<sheet>_usd_per_gb.csv`: month rows, one column per core, USD per Gb.",
              "- `<sheet>_flags.csv`: same shape, O / D / C flags.",
              "- `summary_by_table_month.csv`: table, month, cores with value, cores observed that month, median, p25, p75, min, max.",
              "- `coverage_by_table.csv`: as in the table above.",
              "- `sources.csv`: core, institution, country, kind, URL, URL type, how it was found, snapshot dates with price text, "
              "price lines extracted, tiers, output assumption.",
              "- `output_specs.csv`: flow-cell output assumptions.",
              "- `long_all_price_lines.csv`: one row per extracted price line per snapshot: core, URL, snapshot timestamp and month, "
              "live or Wayback, document date and effective period, flow cell, unit, quantity, read configuration, cycles, tier, "
              "local price, currency, FX, USD price, library-prep flag, stated output, Gb per unit, output basis, $/Gb, "
              "verbatim snippet, implausible and excluded flags.",
              ""]
    return "\n".join(lines)


# ------------------------------------------------------------------------------ commands

PHASES = [("specs", phase_specs), ("discover", phase_discovery), ("harvest", phase_harvest), ("extract", phase_extract),
          ("verify", phase_verify), ("build", phase_build)]


def cmd_run(args):
    for d in (DATA, DISC, SNAPS, EXTR, VERI, SANDBOX):
        d.mkdir(parents=True, exist_ok=True)
    keep_awake(True)
    update_state(lambda s: s.update(pid=os.getpid(), started=s.get("started") or now(), last_launch=now()))
    for mod in ("pypdf", "matplotlib", "openpyxl", "pandas", "requests"):
        try:
            __import__(mod)
        except ImportError:
            log(f"FATAL: module {mod} not importable by {sys.executable} (user site {_usersite})")
            update_state(lambda s, m=mod: s.update(stage="failed", error=f"missing module {m}"))
            return
    stop_hb = threading.Event()

    def heartbeat():
        while not stop_hb.wait(300):
            update_state(lambda s: None)
    threading.Thread(target=heartbeat, daemon=True).start()
    try:
        for name, fn in PHASES:
            st = load_state()
            if name in st.get("phases_done", []) and name != "verify":
                continue
            update_state(lambda s, n=name: s.update(stage=n))
            log(f"=== phase {name} ===")
            fn()
            if name != "verify":
                update_state(lambda s, n=name: s["phases_done"].append(n) if n not in s["phases_done"] else None)
        update_state(lambda s: s.update(stage="complete", finished=now()))
        log(f"JOB COMPLETE. Spend ${load_state()['cost_usd']:.2f}")
    except SystemExit:
        update_state(lambda s: s.update(stage="failed", error="CLI not logged in"))
        raise
    except Exception as e:
        import traceback
        log("FAILED: " + traceback.format_exc()[-1500:])
        update_state(lambda s: s.update(stage="failed", error=repr(e)[:300]))
    finally:
        stop_hb.set()
        keep_awake(False)


def cmd_start(args):
    for d in (DATA, DISC, SNAPS, EXTR, VERI, SANDBOX):
        d.mkdir(parents=True, exist_ok=True)
    exe = Path(sys.executable)
    pyw = exe.with_name("pythonw.exe") if os.name == "nt" else exe
    if not pyw.exists():
        pyw = exe

    def reset(s):
        for r in s["agents"].values():
            if r.get("status") == "running":
                r["status"] = "pending"
        if s.get("stage") == "failed":
            s["stage"] = "relaunching"
    update_state(reset)
    cmdline = f'"{pyw}" "{Path(__file__).resolve()}" run'
    ps = ("$r = Invoke-CimMethod -ClassName Win32_Process -MethodName Create -Arguments "
          f"@{{CommandLine='{cmdline}'; CurrentDirectory='{ROOT}'}}; "
          "Write-Output (\"rc=\" + $r.ReturnValue + \" pid=\" + $r.ProcessId)")
    out = subprocess.run(["powershell", "-NoProfile", "-Command", ps], capture_output=True, text=True)
    print(f"Launched via WMI: {out.stdout.strip()} {out.stderr.strip()[:200]}. "
          f"Check with: python _Build/core_lab_pricing.py status")


def cmd_status(args):
    st = load_state()
    reg = load_registry()
    snaps = load_snapmeta()
    distinct = len({s['rel_hash'] for s in snaps if s.get('rel_hash')})
    n_ex = len(list(EXTR.glob("*.json"))) if EXTR.exists() else 0
    n_ve = len(list(VERI.glob("*.json"))) if VERI.exists() else 0
    agents = st.get("agents", {})
    print(f"stage: {st.get('stage')} | started {st.get('started')} | heartbeat {st.get('heartbeat_human')} | pid {st.get('pid')}")
    print(f"spend: ${st.get('cost_usd', 0):.2f} of cap ${CAP_USD:.0f} | paused_until: {st.get('paused_until')}")
    print(f"discovery agents: {sum(1 for a in agents.values() if a.get('status') == 'done')} done, "
          f"{sum(1 for a in agents.values() if a.get('status') == 'failed')} failed, "
          f"{sum(1 for a in agents.values() if a.get('status') == 'running')} running (of {len(SLICES_W1) + len(SLICES_W2)})")
    print(f"registry: {len(reg['cores'])} cores, {len(reg['urls'])} URLs | live-fetched URLs: {st.get('live_done', 0)} | archive-harvested URLs: {st.get('harvest_done', 0)} | common-crawl URLs: {st.get('cc_done', 0)} | "
          f"archive paused until: {st.get('wb_paused_until')} | "
          f"snapshots: {len(snaps)} ({distinct} distinct price texts)")
    print(f"extracted: {n_ex}/{st.get('extract_total', '?')} | verified: {n_ve} | phases done: {st.get('phases_done')}")
    if st.get("error"):
        print(f"error: {st['error']}")
    if st.get("stage") == "complete":
        print(f"COMPLETE at {st.get('finished')}. Outputs: {OUT_XLSX}")


def cmd_check(args):
    st = load_state()
    age = (time.time() - st.get("heartbeat", 0)) / 60
    pid = st.get("pid")
    alive = False
    if pid:
        out = subprocess.run(["tasklist", "/FI", f"PID eq {pid}", "/NH"], capture_output=True, text=True).stdout
        alive = str(pid) in out and "python" in out.lower()
    if st.get("stage") == "complete":
        pass
    elif alive and age <= 40:
        print(f"Job process {pid} alive (last state write {age:.0f} min ago): no action.")
    else:
        if alive:
            print(f"Job process {pid} alive but silent for {age:.0f} min: killing it.")
            subprocess.run(["taskkill", "/T", "/F", "/PID", str(pid)], capture_output=True)
            time.sleep(3)
        print("Job stalled or failed: relaunching.")
        cmd_start(args)
        time.sleep(10)
    cmd_status(args)


def cmd_build(args):
    phase_build()


def cmd_stop(args):
    update_state(lambda s: s.update(stop=True))
    print("stop flag set: no new model calls; harvest and build still run")


def cmd_test(args):
    """Harvest + extract one URL end to end (for debugging)."""
    for d in (DATA, DISC, SNAPS, EXTR, VERI, SANDBOX):
        d.mkdir(parents=True, exist_ok=True)
    seed_registry()
    cid = load_registry()['urls'][args.url]['core_id']
    live_fetch(args.url, cid)
    archive_fetch(args.url, cid, _seen_snaps())
    done = set(read_json(URLDONE, []))
    done.add(args.url)
    write_json(URLDONE, sorted(done))
    reg = load_registry()
    hs = []
    for sm in load_snapmeta():
        if sm["url"] == args.url and sm.get("rel_hash") and sm["rel_hash"] not in [h[0] for h in hs]:
            c = reg["cores"].get(sm["core_id"], {})
            hs.append((sm["rel_hash"], sm["ts"][:8], sm["url"], f"{c.get('institution')} / {c.get('core')}"))
    print(f"{len(hs)} distinct texts")
    for it in hs[: args.n]:
        extract_one(it)
        print(json.dumps(extraction_for(it[0]), indent=1)[:3000])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name, fn in (("run", cmd_run), ("start", cmd_start), ("status", cmd_status), ("check", cmd_check),
                     ("build", cmd_build), ("stop", cmd_stop)):
        sub.add_parser(name).set_defaults(fn=fn)
    p = sub.add_parser("test")
    p.add_argument("url")
    p.add_argument("-n", type=int, default=1)
    p.set_defaults(fn=cmd_test)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
