"""Overnight research job: is Illumina over-earning on clinical consumables? (started 2026-10-11)

Runs 20 headless Claude agents (4 at a time, each with a hard timeout), then an Opus synthesis that
writes Core Notes/16_Addendum_Clinical_Consumables_Thesis.md, and a Sonnet pass that turns it into an
HTML artifact source. Progress lives in _Build/clinical_scrape_state.json so the job resumes after any
interruption. Usage limits are waited out. Spend is metered per call (API-equivalent USD reported by
the CLI) and capped at ~10% of the weekly plan, calibrated by the hourly self-check:

  python _Build/clinical_scrape.py start [--baseline PCT]  launch detached (records weekly % baseline)
  python _Build/clinical_scrape.py run                      run in the foreground
  python _Build/clinical_scrape.py status                   progress, spend and cap
  python _Build/clinical_scrape.py usage PCT                feed the current weekly % (calibrates the cap)
  python _Build/clinical_scrape.py published URL            record the published artifact URL
  python _Build/clinical_scrape.py stop                     ask the job to stop launching new agents
"""
import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build import find_claude  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "_Build"
WORK = ROOT / "Working Notes"
CORE = ROOT / "Core Notes"
EXTRACTS = WORK / "Extracts"
OUT_DIR = WORK / "Outputs" / "analyses" / "2026-10-11_clinical_consumables_scrape"
DATASETS = WORK / "Outputs" / "datasets"
ADDENDUM = CORE / "16_Addendum_Clinical_Consumables_Thesis.md"
ADDENDUM_COPY = WORK / "Outputs" / "analyses" / "2026-10-11_clinical_consumables_thesis.md"
HTML_OUT = WORK / "Outputs" / "artifacts" / "2026-10-11_clinical_consumables_thesis.html"
STATE = BUILD / "clinical_scrape_state.json"
LOG = BUILD / "clinical_scrape.log"
SANDBOX = BUILD / "sandbox"

CONCURRENCY = 4
CAP_PCT = 10.0              # share of the weekly plan this job may use
RESERVE_MIN_USD = 25.0      # held back from research for the model, red team, fact-check, write-up and HTML
PROVISIONAL_CAP_USD = 60.0  # ceiling until the hourly check has calibrated $ per weekly %
MAX_WAVES = 40              # safety stop for the iterative research loop
LEDGER = OUT_DIR / "00_evidence_ledger.md"
GAPS = OUT_DIR / "00_open_gaps.md"
TIMEOUT = {"haiku": 15 * 60, "sonnet": 22 * 60, "sonnet_web": 25 * 60, "opus": 45 * 60}
BUDGET = {"haiku": 3, "sonnet": 12, "opus": 30}

_lock = threading.RLock()
_pause_until = 0.0


def now():
    return dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def log(msg):
    line = f"[{now()}] {msg}"
    with _lock:
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    print(line, flush=True)


def _retry(fn, tries=40):
    """Windows/OneDrive can briefly lock a file during an atomic replace or sync: retry instead of crashing."""
    for i in range(tries):
        try:
            return fn()
        except (PermissionError, OSError, json.JSONDecodeError):
            if i == tries - 1:
                raise
            time.sleep(0.25 + 0.25 * i)


def _read_state():
    return json.loads(STATE.read_text(encoding="utf-8"))


def _write_state(st):
    tmp = STATE.with_suffix(".tmp")
    tmp.write_text(json.dumps(st, indent=1), encoding="utf-8")
    tmp.replace(STATE)


def load_state():
    with _lock:
        if STATE.exists():
            return _retry(_read_state)
    return {"agents": {}, "cost_usd": 0.0, "stage": "new", "cap_usd": PROVISIONAL_CAP_USD,
            "calibrated": False, "baseline_pct": None, "started": None, "samples": [], "stop": False}


def save_state(st):
    with _lock:
        _retry(lambda: _write_state(st))


def update_state(fn):
    with _lock:
        st = load_state()
        fn(st)
        st["heartbeat"] = time.time()
        st["heartbeat_human"] = now()
        _retry(lambda: _write_state(st))
        return st


def keep_awake(on=True):
    """Ask Windows not to idle-sleep while this process runs (released automatically on exit)."""
    if os.name != "nt":
        return
    import ctypes
    ES_CONTINUOUS, ES_SYSTEM_REQUIRED = 0x80000000, 0x00000001
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | (ES_SYSTEM_REQUIRED if on else 0))


# ------------------------------------------------------------------------------ headless calls

LIMIT_RX = re.compile(r"usage limit|limit reached|hit your limit|limit will reset|resets? (at|in)|"
                      r"rate.?limit|too many requests|\b429\b", re.I)
OVERLOAD_RX = re.compile(r"overloaded|\b529\b|api error|connection error|ECONNRESET", re.I)


def call_claude(prompt, model, tools, add_dirs, timeout, budget):
    """One headless call. Returns (text, cost_usd). Waits out usage limits."""
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
    for d in add_dirs:
        args += ["--add-dir", str(d)]
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
            log(f"  timeout after {timeout // 60} min ({model}); cost of the killed call is unknown")
            return None, 0.0
        cost, text = 0.0, ""
        try:
            j = json.loads(out)
            cost = float(j.get("total_cost_usd") or 0.0)
            text = j.get("result") or ""
            is_err = bool(j.get("is_error"))
        except Exception:
            text, is_err = out or "", True
        blob = (text or "") + "\n" + (err or "") + ("" if text else (out or ""))
        if "not logged in" in blob.lower():
            log("  CLI is not logged in. Run `claude setup-token` (or `claude` then /login) and restart.")
            raise SystemExit(2)
        if not is_err and text and len(text.strip()) > 200:
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
        if "budget" in blob.lower() and text and len(text.strip()) > 200:
            return text.strip(), cost
        log(f"  call failed rc={p.returncode} ({model}): {blob.strip()[:300]!r}")
        return (text.strip() if text and len(text.strip()) > 200 else None), cost


# ------------------------------------------------------------------------------ prompts

CONTEXT = f"""You are one of 20 research agents working overnight (date: 2026-10-11) for an equity analyst researching Illumina (ILMN). Your output feeds a final synthesis, so return organized findings, not prose essays and not copies of documents.

THE THESIS QUESTIONS
1. Is Illumina over-earning on clinical sequencing consumables today? The remaining NovaSeq 6000 business is still a large share of high-throughput (HT) consumables revenue. As of Q2 2026, NovaSeq X carried ~83% of HT gigabase (Gb) volume but only ~59% of HT consumables revenue, so the NovaSeq 6000 still carries ~17% of HT volume and ~41% of HT revenue. (These are TOTAL HT figures, research + clinical. Clinical-only: ~78% of clinical volume was on X in Q2 2026, target 80-85% by end-2026; research ~92%.) When that remaining volume converts to the X (management has said the per-Gb price decline across the transition is "easily more than 60% to 70%"), how much revenue is at risk, and is current clinical consumables revenue/margin inflated by the not-yet-converted 6000 base (and by labs running 6000s and Xs in parallel, a question Jefferies raised on the Q2 2026 call)?
2. What is the go-forward volume (Gb) growth for clinical consumables customers, and will it offset the price decline per Gb on the X versus the 6000? Consider test-volume growth (MRD, liquid biopsy/CGP, NIPT, rare disease, MCED), sequencing intensity (exome->genome ~15x data, deeper MRD, WGS-based MRD), competition (Roche AXELIOS, Ultima, Element), customer concentration and bargaining power, and further price cuts (e.g. the 35B flow cell, ~20% lower $/Gb, expected ~Jan 2027).
The analyst also wants: (a) anything "shady" or credibility-relevant in management behavior, in and outside calls (metric changes, definitions, dropped disclosures, guidance games, accounting choices, insider selling, compensation-metric changes, contradictions, dodged questions); (b) read-through from end customers (clinical labs) and from competitors. Breadth beyond these points is welcome if relevant.

KEY FACTS ALREADY KNOWN (do not spend time re-deriving; DO flag anything that contradicts them):
- FY25 pull-through (annual consumables $ per installed instrument): NovaSeq X ~$1.35M (FY26 guide $1.35-1.40M), installed base ~890 at end-FY25 (~970 by Q1'26); NovaSeq 6000 ~$670K (FY26 guide $600-650K), base ~1,360 after ~330 decommissions in FY25. NextSeq 1k/2k ~$90K.
- X share of HT revenue: ~27% (Q2'24) -> 35% (Q3'24) -> 40% (Q4'24) -> 43% (Q1'25) -> 44% (Q2'25) -> 51% (Q3'25) -> 55% (Q4'25) -> 55% (Q1'26) -> 59% (Q2'26). Volume share: ~45% -> 55% -> 65% -> 68% -> 69% -> 78% -> 80% -> 82% -> 83%.
- Ex-China clinical consumables growth: 7/5/11/8% (2024 quarters), 8/10/12/20% (2025), 20% Q1'26, 15% Q2'26; research & applied -7% Q2'26. Clinical >65% of sequencing consumables (management) though an ex-employee called the classification "very loose". FY25 sequencing consumables $2,939M; Q2'26 $775M.
- Gb output on connected instruments grows >30% y/y; management's long-term model: volume growth mid-20s %, price decline mid-teens % per year. CFO (Nov 2024): Q3'24 volume +40% vs consumables revenue +5%, "largely price"; price decline ~25%.
- Management stopped reporting transition metrics/cohort data at various points; "40 fully converted clinical customers" case study (volume offset price in year 1, then both accelerated).
- Roche AXELIOS: $150/genome list, $0.06/M reads, ~$750K instrument, RUO launch 29 Jun 2026, ~1/3 of ~100 first-year placements by Sept. JPM 62-customer survey (Jun 2026): planned volume growth 2.4-5.2 pts faster than planned spend.

CORPUS: Working Notes are at "{WORK}". INDEX.md lists every document. Readable extracts are under "{EXTRACTS}\\<COMPANY>\\<type>\\" and originals under "{WORK}\\Sources\\<COMPANY>\\<type>\\" (open originals when exact quotes, tables or numbers matter).

OUTPUT RULES
- Return Markdown. Start with "## Key findings" (8-15 bullets, most important first), then organized sections for your scope, then "## Contradictions and stale data", then "## Gaps / what I could not find".
- Every factual bullet carries a citation: for corpus items the file name and date (e.g. [ILMN Q2 2026 call, 2026-07-30, Extracts/ILMN/earnings_call/...]); for web items the publisher, date and URL.
- Label each point as FACT (reported number/document), MGMT (management claim), or OPINION (analyst/expert/your inference). Quote exact words when they matter (short quotes).
- Quantify wherever possible. Be concise: aim for 2,000-4,500 words. No filler.
- HARD STOP: you have about {{minutes}} minutes. Prioritize the highest-value material first and return what you have before time runs out. Never invent numbers, sources or URLs.
"""

INTERNAL = "Use Read/Grep/Glob on the corpus. Read the extracts in full for your files; open originals for exact numbers/quotes."
WEB = ("Use WebSearch and WebFetch. Prefer primary sources (company filings on sec.gov, earnings-call transcripts or "
       "prepared remarks, investor presentations, CMS/FDA/government data, company press releases), then reputable "
       "trade press (GenomeWeb, 360Dx, Fierce, Endpoints, STAT), then other sources. Record the date of every item. "
       "If a site blocks fetching, try another source; do not get stuck.")

AGENTS = [
    # ---- wave A/B: the corpus
    dict(id="01", name="ILMN calls and conferences 2023-2024", kind="internal", model="sonnet",
         task="Read every ILMN earnings call 2023-2024 (Extracts/ILMN/earnings_call) and every ILMN conference/investor event dated 2023-2024 (Extracts/ILMN/conference). Extract everything bearing on: the NovaSeq 6000->X economics (price per Gb, pull-through by platform, 'pricing transitions', 25B/10B pricing, validation timelines, clinical vs research conversion), the clinical customer base (growth, concentration, open offer letters, multi-year contracts, application mix), volume vs revenue statements, elasticity claims and how they aged, and every management statement later contradicted or quietly dropped (targets abandoned, metrics changed). Build a dated list of management's quantitative transition claims."),
    dict(id="02", name="ILMN calls, conferences and decks 2025-2026", kind="internal", model="sonnet",
         task="Read every ILMN earnings call 2025-2026, every conference dated 2025-2026, and all investor decks (Extracts/ILMN/earnings_call, conference, deck). Extract: every transition metric by quarter (X share of HT volume/revenue, clinical vs research conversion, placements, rental/lease share, multi-unit orders, capacity vs replacement placements), pull-through guides, clinical consumables growth by region/application, the '40 converted clinical customers' cohort slide (exact shape/labels), parallel 6000+X running, the 'over-earned' question (Jefferies, Q2'26) and the exact answer, pricing commentary (35B, volume discounts, application-specific pricing, passing on memory/freight costs), and what management said about where the remaining 6000 clinical volume sits (FDA-approved/validated assays, laggards). Also flag Q&A dodges and answers that changed between quarters."),
    dict(id="03", name="ILMN filings, consensus and insider data", kind="internal", model="sonnet",
         task="Read the ILMN SEC filings (Extracts/ILMN/filing: 10-K, 10-Qs, 8-Ks), the consensus sheets (Extracts/ILMN/consensus) and the insider-trading datasets (Extracts/ILMN/insider_data). Extract: consumables revenue by line and period, gross-margin drivers ('reduced pricing', consumables mix), risk-factor language on customer concentration ('small number of large, centralized laboratory customers'), pricing, reagent rental, contract terms, revenue recognition for rentals/leases, backlog/RPO, any change in disclosure wording between filings (diff the risk factors and MD&A language on pricing and customers), government incentives, non-GAAP adjustments trend, and every insider transaction pattern (who, when, size, 10b5-1 or not, timing vs news/guidance raises). Also what consensus assumes for sequencing consumables growth 2026-2032 and the implied price/volume."),
    dict(id="04", name="Expert calls (all 23)", kind="internal", model="sonnet",
         task="Read all 23 expert-call extracts (Extracts/ILMN/expert_call), opening originals for key quotes. Extract everything on: clinical labs' volumes and growth, conversion from NovaSeq 6000 to X and what keeps tests on the 6000, price per Gb/genome actually paid (by customer size), discounts and their withdrawal, reagent rental, parallel running, sample supply ('sequenced everything in the freezer'), validation/switching costs, which clinical labs are validating Ultima/Element/Roche, customer concentration and bargaining power, MRD/liquid biopsy/NIPT/rare disease volume growth, sequencing intensity per test, and allegations about Illumina conduct (Sunshine Act perks, broken discount promises, opaque quotes, support of competitor validation, 'clinical' classification). Weight each expert by recency and proximity (flag stale or competitor-employed experts)."),
    dict(id="05", name="Sell-side and independent research on ILMN", kind="internal", model="sonnet",
         task="Read all ILMN research notes (Extracts/ILMN/research: JPM, Barclays, UBS, Freedom, Ameriprise, BI, Seeking Alpha). Extract: every quantitative estimate of price vs volume (Barclays' X Gb-share vs revenue-share argument, BI 'trading price for volume', JPM survey details incl. spend vs volume, UBS 'counting' 16% exposure), clinical consumables growth forecasts, models of the transition, analysts' view on whether clinical growth is sustainable, pull-forward/placement debates, margin quality critiques (government incentives, restructuring absence), FCF misses, and estimate changes. Note where analysts disagree and what evidence each side uses."),
    dict(id="06", name="Competitor and peer corpus read-through", kind="internal", model="sonnet",
         task="Read the peer extracts: Roche (Extracts/ROCHE), Oxford Nanopore (Extracts/ONT), PacBio (Extracts/PACB), Thermo Fisher (Extracts/TMO), 10x Genomics (Extracts/TXG), MGI (Extracts/MGI), sector (Extracts/SECTOR). Extract read-through for Illumina clinical consumables: Roche AXELIOS clinical targets, pricing, Foundation Medicine/SAGA/Freenome plans to move volume, placements; ONT/PacBio clinical growth rates and pricing (proxy for clinical sequencing demand); 10x commentary on Ultima/Roche lowering price per read; MGI clinical growth and price deflation; Thermo funding read-through; any statements about clinical labs validating or switching platforms; market sizing for MRD/CGP/MCED and growth rates."),
    dict(id="07", name="Management credibility audit (corpus)", kind="internal", model="sonnet",
         task="Do a forensic audit of Illumina management credibility across ALL ILMN calls, conferences, decks, filings and research in the corpus. Build: (1) a guidance-vs-actual track record table 2023-2026 (initial guide, changes, actual); (2) a list of every KPI introduced, redefined or discontinued, with dates and the stated reason (e.g. transition metrics phased out after Q4'25, cohort reporting stopped, 2027 target redefined ex-China, installed base 'net' vs gross, pull-through definitions, 'clinical' classification >65% vs earlier ~40-56%, organic/ROW definitions); (3) statements later contradicted (e.g. 'no clinical cliff', 'no pull-forward', instrument revenue vs placements, rental/lease accounting, inflation 'fully offset'); (4) margin-quality items (government incentives, deferred comp, absent restructuring, tariff refunds); (5) capital-allocation inconsistencies (buyback pauses, debt); (6) leadership churn. Rate each item's severity (low/med/high) and say whether it bears on the clinical-consumables thesis."),
    dict(id="08", name="Transition and unit-economics dataset (corpus)", kind="internal", model="sonnet",
         task="Build the definitive quarter-by-quarter dataset (Q1 2023 - Q2 2026) from the corpus (calls, decks, filings, research) of: sequencing consumables $, ex-China consumables growth, clinical and research consumables growth, X share of HT Gb and HT revenue (total, clinical, research), NovaSeq X placements and installed base, NovaSeq 6000 installed base/decommissions, pull-through by platform (guides and actuals), gigabase growth, stated price declines per Gb, flow-cell list prices and $/genome mentions, clinical share of consumables, and HT consumables revenue if derivable. Present as Markdown tables with a source per cell (or per row). Then derive: implied HT consumables $ on X vs on 6000 per quarter (using any disclosed or estimated HT revenue base), implied revenue per Gb on X vs 6000 and the ratio, and implied 6000 revenue still to convert. State every assumption explicitly."),
    # ---- wave C/D: outside data (web)
    dict(id="09", name="Clinical customers I: Natera, Guardant, BillionToOne, Exact/Abbott", kind="web", model="sonnet",
         task="Research the latest (2025 to Q3 2026) disclosures of Natera, Guardant Health, BillionToOne and Exact Sciences (now Abbott): test volumes and growth by product (Signatera, Panorama/NIPT, Guardant360, Reveal/Shield, UNITY, Cologuard/Oncodetect), guidance, cost of revenue per test and gross margin trends, any comments on sequencing costs, sequencer platforms, suppliers (10-K supplier-dependence language naming Illumina), supply agreements, migrations to NovaSeq X, and validation of other platforms (Ultima, Element, Roche). Convert test growth into an estimate of sequencing-volume growth where possible (e.g. whole-genome/tumor-informed MRD needs more Gb per test). Note any statements that sequencing cost per test fell and by how much."),
    dict(id="10", name="Clinical customers II: Tempus, Caris, GeneDx, Myriad, NeoGenomics, Veracyte, Adaptive, Labcorp, Quest, Foundation", kind="web", model="sonnet",
         task="Research recent (2025 to Q3 2026) disclosures of Tempus AI, Caris Life Sciences, GeneDx, Myriad Genetics, NeoGenomics, Veracyte, Adaptive Biotechnologies (clonoSEQ), Labcorp and Quest genomics, Personalis and Foundation Medicine (via Roche): test volumes and growth, exome->genome shifts (GeneDx), MRD launches, sequencing COGS commentary, platform/supplier statements (Illumina dependence, NovaSeq X migrations and the cost savings they cite, e.g. Adaptive's NovaSeq X transition), validation of Ultima/Element/Roche, and any supply agreements. Summarize the implied 2026-2027 clinical sequencing volume growth across the group, and which customers have the most incentive and ability to switch."),
    dict(id="11", name="Pricing data: NovaSeq 6000 vs NovaSeq X price per Gb", kind="web", model="sonnet",
         task="Find public price data to quantify the per-Gb price decline from NovaSeq 6000 to NovaSeq X: (1) university/core-facility sequencing price lists (e.g. per-lane or per-flow-cell prices for NovaSeq 6000 S1/S2/S4 vs NovaSeq X 1.5B/10B/25B; many cores publish these, including internal vs external rates, and some show both platforms side by side or year over year); (2) Illumina list prices or quoted reagent kit prices for S4 300-cycle vs 10B/25B 300-cycle and their output in Gb; (3) commercial service providers' price per genome/Gb on each platform; (4) any 2026 price changes and the 35B flow cell. Compute $/Gb for each platform/flow cell and the implied decline (old vs new), noting dates, internal vs external rates and that core prices include labor/overhead. Aim for at least 10 distinct price points with URLs, and summarize the median decline."),
    dict(id="12", name="Reimbursement and test-volume data (CMS and payers)", kind="web", model="sonnet",
         task="Find public data on US clinical NGS test volumes and reimbursement trends: CMS Medicare Part B / Clinical Laboratory Fee Schedule utilization for key NGS codes (e.g. 81479, 0239U, 0340U Signatera, 0242U Guardant360, 0037U FoundationOne CDx, 81420/81507 NIPT, 81425-81427 genome, 81415-81417 exome, MRD PLA codes) by year; MolDX coverage decisions for MRD and CGP (2024-2026); ADLT rate changes; the Sept 2026 CMS PAMA proposal and its effect on NGS test prices; any NIPT penetration statistics; and state biomarker-testing laws. Translate into an evidence-based range for 2026-2028 US clinical NGS test-volume growth by category, and note pricing pressure that could push labs to demand cheaper sequencing."),
    dict(id="13", name="Sequencing intensity per test and clinical Gb growth inputs", kind="web", model="sonnet",
         task="Quantify data consumed per clinical test and how it is changing, from vendor specs, publications and company materials: NIPT (Gb per sample, low-pass WGS), CGP tissue panels (e.g. TSO 500, FoundationOne), liquid biopsy panels, tumor-informed panel MRD vs whole-genome MRD (e.g. Signatera exome+panel, Personalis NeXT, NeoGenomics RaDaR, Myriad Precise MRD, C2i/Veracyte WGS MRD, Illumina's WGS MRD workflow), rare disease exome vs genome, MCED (Galleri methylation), pharmacogenomics. Build a table: test type, Gb per test (range), trend, source. Then build a simple model: 2026-2028 clinical Gb growth = test growth x intensity change, by category, with low/base/high cases, and compare with management's >30% clinical data-growth claim."),
    dict(id="14", name="Competitor read-through and clinical switching evidence (web)", kind="web", model="sonnet",
         task="Research July-October 2026 (and relevant 2025-2026) news on Roche AXELIOS (placements, named customers, clinical/IVD plans, Foundation Medicine/SAGA migration, ASHG 2026 data, pricing), Ultima Genomics (UG 100 Solaris, clinical customers, deals with Natera/Guardant/others, $/genome), Element Biosciences (VITARI shipments, AVITI24 clinical use, clinical customers), MGI/Complete Genomics (Swiss Rockets), PacBio and ONT clinical wins, and any clinical lab publicly validating or moving tests off Illumina. Also Illumina's competitive responses (35B flow cell pricing, reagent rental, TruPath, Q70, price cuts). Rate each item by how directly it threatens Illumina's clinical consumables price or volume."),
    dict(id="15", name="Management conduct outside calls (web)", kind="web", model="sonnet",
         task="Research Illumina management and governance outside the earnings calls, 2024 to Oct 2026: SEC Form 4 insider sales/purchases by Thaysen, Dhingra and other officers/directors (use sec.gov EDGAR or openinsider-type sites; note 10b5-1 plans, timing vs guidance raises and stock run-up from ~$80 to ~$278), proxy statements (DEF 14A 2025 and 2026: changes to incentive metrics, e.g. EPS units reinstated, non-GAAP definitions used for pay), 8-Ks (executive departures e.g. CCO Everett Cunningham Jan 2026; new hires), SEC comment letters (CORRESP/UPLOAD) on Illumina's non-GAAP or segment disclosures, litigation (GRAIL securities suits, patent suits, any customer or competitor suits about pricing or exclusivity), employee sentiment (Glassdoor, Blind, Reddit, layoffs.fyi; layoffs or reorganizations in 2025-2026), and reports of aggressive commercial practices. Present as a dated list with severity ratings and relevance to the thesis."),
    dict(id="16", name="Latest ILMN commentary Aug-Oct 2026 and international clinical demand", kind="web", model="sonnet",
         task="Find Illumina management commentary after the Q2 2026 call (30 Jul 2026) through Oct 2026: investor conferences (e.g. Wells Fargo, Baird, Morgan Stanley, Goldman, Bank of America, UBS in Aug-Sept 2026), press releases, ASHG 2026, product/pricing announcements (35B flow cell, NovaSeq X roadmap), any pre-announcement or Q3 2026 preview, and analyst notes summarized in the press. Also research outside-US clinical sequencing demand: NHS Genomic Medicine Service volumes and tenders, European national genomics programs, NIPT/WGS adoption in Europe, Middle East programs, and any IVDR effects. Focus on clinical consumables volume, pricing and conversion statements."),
    # ---- wave E: analysis (needs 01-16)
    dict(id="17", name="Job postings and hiring signals", kind="web", model="sonnet",
         task="Paid scraping (Apify) was unavailable tonight, so gather job-posting evidence via WebSearch/WebFetch: search public job boards and company career sites (Greenhouse, Lever, Workday, LinkedIn public job pages, Indeed result snippets) for postings from roughly the last 90 days that mention 'NovaSeq X', 'NovaSeq 6000', 'Ultima' / 'UG 100', 'Element' / 'AVITI', 'AXELIOS' / 'SBX' at clinical labs (Natera, Guardant, Tempus, Caris, Exact, BillionToOne, GeneDx, Foundation Medicine, Myriad, NeoGenomics, Labcorp, Quest and others). Also Illumina's own hiring/layoff signals (functions, China, clinical market access, reagent rental/commercial finance) and Roche sequencing/Ultima/Element commercial and field-service build-outs. Record each posting (company, title, location, date, URL, platforms named). Write findings: counts by platform among clinical employers, notable validation/transition roles, and caveats about the small sample."),
    dict(id="18", name="Over-earning and price/volume model", kind="analysis", model="sonnet", needs="research",
         task="Using ALL findings files listed below, build an explicit, transparent model answering both thesis questions. (1) Over-earning: size the remaining NovaSeq 6000 consumables revenue (total HT and clinical-only; use pull-through x installed base, X-share data, and any HT revenue base), the per-Gb price ratio X/6000 (triangulate management's 60-70%, CFO's ~25% annual, price-list data), and the revenue lost if that volume converts at constant Gb, over what timeline (2026-2028). (2) Offset: required clinical Gb growth to offset conversion plus ongoing price declines (35B, competition), versus evidence-based Gb growth (test growth x intensity from agents 09-13). Produce low/base/high scenarios for 2026-2028 clinical sequencing consumables revenue growth and the 'excess earnings' at risk, with every assumption sourced or labeled. Include sensitivity tables (e.g. price ratio vs Gb growth). Compare with consensus sequencing consumables (+5.6% 2026, +8.8% 2027, +9.4% 2028) and management's clinical mid-teens guide. Be explicit about what is unknowable and which single numbers would change the answer."),
    dict(id="19", name="Red team: bull vs bear", kind="analysis", model="sonnet", needs="research",
         task="Using ALL findings files listed below, write the strongest evidence-based BEAR case and the strongest BULL case on the two thesis questions, then adjudicate: which evidence is strongest and most recent, which claims rest on stale/biased experts or management assertions, where consensus may be wrong, and which management-credibility issues actually matter for the clinical-consumables thesis versus noise. List the 10 KPIs/events to watch next (e.g. Q3 2026 call ~30 Oct: X revenue share if disclosed, clinical growth, pull-through, 35B pricing, Roche ASHG data) with what reading would confirm each side."),
    dict(id="20", name="Fact-check of key numbers", kind="internal", model="haiku", needs="research",
         task="You are a fact-checker. From the findings files listed below, pick the ~40 most decision-relevant numeric claims that cite the corpus (transition shares, pull-through, installed base, growth rates, prices, guidance, insider transactions) and verify each against the cited extract or original (use Grep/Read). Return a table: claim, cited source, verified value, status (OK / WRONG / UNVERIFIABLE / MIS-CITED), correction. Then list any claims that contradict each other across agents. Do not verify web claims except by checking internal consistency."),
]

SYNTH_PROMPT = """You are writing a new section of the Core Notes for an Illumina (ILMN) research folder: "16 Addendum: Is Illumina Over-Earning on Clinical Consumables?" (as of 2026-10-11). The Core Notes are a master briefing read at the start of every research chat, so this addendum must stand alone, be accurate, and be easy to learn from.

Inputs: the master evidence ledger (read it in full: it is the deduplicated list of every piece of evidence found across all research waves), the open-gaps list, and the agent findings files listed below (open them for detail and exact quotes; file 20 is a fact-check: apply its corrections; files 18 and 19 are the model and red team; files 21+ are follow-up waves that the planner targeted at gaps). You may consult the Core Notes in "{core}" (especially 01, 02, 05, 07, 08, 09) to check context, but do not repeat them at length.

The analyst's questions:
1. Is Illumina over-earning on clinical consumables once the remaining NovaSeq 6000 business (Q2 2026: ~17% of HT volume, ~41% of HT revenue; clinical ~22% of volume) converts to the NovaSeq X?
2. What is go-forward volume growth for clinical consumables customers, and will it offset the price decline on the X relative to the 6000?
Plus: management conduct and credibility in and outside calls ("shady things"), and read-through from end customers and competitors, with broad coverage beyond these points.

WRITE (Markdown, no front matter), following these rules:
- Full, well-written, simple sentences and short paragraphs. Lead with the answer, then explain. Assume a smart reader with little background; explain jargon in a few plain words the first time.
- Contextualize every number: what it measures, the period, the comparison, why it matters. Distinguish FACT, management claim and opinion, and say who said what and when with light citations like (Q2 2026 call) or (Natera Q2 2026 10-Q) or (Expert: ex-Illumina AD, Jul 2026). Point out disagreements and stale data.
- Tables are welcome for comparisons, always introduced with a sentence saying what to take from them.
- The analyst asked for "a readable, well-written list summary containing all evidence": so the core of the document is organized, numbered evidence lists, each item one to three sentences with its citation, grouped by theme.

STRUCTURE:
# 16 Addendum: Is Illumina Over-Earning on Clinical Consumables?
*As of 2026-10-11. Built from iterative waves of research agents (run until a wave found no new evidence or the usage cap was reached) covering every relevant Core Notes source plus outside data (customer filings, price lists, CMS and payer data, competitor news, insider filings, job postings). How it was built and its limits are at the end.*
## The answer in brief  (5-8 short paragraphs: verdict on Q1 and Q2 with confidence levels and the key numbers; what would change the view)
## How the NovaSeq 6000-to-X conversion hits revenue: the mechanics  (plain-English primer with the arithmetic)
## Question 1: Is clinical consumables revenue over-earning?  (numbered evidence list, then the sizing)
## Question 2: Will clinical volume growth offset the price decline?  (numbered evidence list by driver: test volumes by application, sequencing intensity, price per Gb data, competition, customer concentration)
## The model: scenarios for 2026-2028  (tables from agent 18, cleaned; assumptions; sensitivity)
## Management conduct and credibility  (numbered list with severity and relevance; separate 'material to the thesis' from 'noise')
## Read-through from clinical customers  (numbered list, customer by customer)
## Read-through from competitors  (numbered list)
## Alternative data  (price lists, CMS/payer data, job postings: what each shows and how reliable)
## Bull case vs bear case
## What to watch next  (KPIs and dated events with what each reading would mean)
## Where sources disagree, and stale or weak evidence
## How this addendum was built  (sources, agents, limits: e.g. Apify job-postings scrape unavailable; web-sourced data quality)

Length: as long as needed to cover every ledger item (merge near-duplicates into one item with multiple citations), typically 10,000-20,000 words; keep each evidence item to one to three sentences. Do not invent anything; if inputs conflict, say so. Output ONLY the Markdown document."""

HTML_PROMPT = """Convert the Markdown document below into ONE complete, self-contained HTML page that will be published as a private web artifact. Keep ALL of the content and wording; do not summarize or drop anything.

Requirements:
- <!doctype html>, <meta charset="utf-8">, <meta name="viewport" content="width=device-width, initial-scale=1">, and <title>Clinical Consumables Thesis</title>.
- Define colors as CSS custom properties on :root (light theme), then redefine them for dark mode under `@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ ... }} }}` and again under `:root[data-theme="dark"] {{ ... }}`. Give body an explicit background and text color from the tokens.
- Typography: a clean readable sans-serif stack (you may load one Google Fonts family via <link>, e.g. Inter or Source Sans 3; nothing else external). Max content width ~780px, comfortable line height, 16px side gutters on phones, no horizontal page scroll: wrap every table in a div with overflow-x:auto.
- A sticky or top table of contents linking to each ## section (give headings ids). Style numbered evidence lists clearly; tables with subtle borders and zebra rows; small muted citation styling is fine but keep citations visible as text.
- A small header block with the title, the as-of line, and a one-line description.
- No JavaScript except an optional tiny theme toggle. No other external resources.
Output ONLY the HTML, starting with <!doctype html>.

=== MARKDOWN ===
{md}"""


# ------------------------------------------------------------------------------ runner

def findings_files(exclude=()):
    """Agent findings files (not the ledger/gaps), sorted by agent id."""
    out = [p for p in OUT_DIR.glob("*.md") if not p.name.startswith("00_") and p.name.split("_")[0] not in exclude]
    return sorted(out, key=lambda p: int(p.name.split("_")[0]))


def research_ok(wait=True):
    """True while research may continue: spend below cap minus the write-up reserve.
    While the cap is still provisional, wait for the hourly check to calibrate it."""
    waited = 0
    while True:
        st = load_state()
        if st.get("stop"):
            return False
        reserve = max(RESERVE_MIN_USD, 0.15 * st["cap_usd"])
        if st["cost_usd"] < st["cap_usd"] - reserve:
            return True
        if st.get("calibrated") or not wait or waited >= 240:
            return False
        if waited % 15 == 0:
            log(f"Research paused: spend ${st['cost_usd']:.2f} at provisional cap ${st['cap_usd']:.2f} less reserve; "
                f"waiting for the hourly check to calibrate the cap")
        time.sleep(60)
        waited += 1


def run_agent(a, retry=False, final=False):
    st = load_state()
    rec = st["agents"].get(a["id"], {})
    if rec.get("status") == "done":
        return True
    if not final and not research_ok():
        log(f"Agent {a['id']} skipped: research budget reached or stop flag set")
        update_state(lambda s: s["agents"].setdefault(a["id"], {}).update(status="skipped_cap", name=a["name"]))
        return False
    tkey = "sonnet_web" if (a["kind"] == "web" and a["model"] == "sonnet") else a["model"]
    timeout = TIMEOUT[tkey]
    minutes = timeout // 60 - 3
    prompt = CONTEXT.replace("{minutes}", str(minutes))
    prompt += f"\nYOUR ASSIGNMENT (agent {a['id']}: {a['name']}):\n{a['task']}\n\n"
    prompt += (INTERNAL if a["kind"] == "internal" else WEB if a["kind"] == "web" else
               "Use Read/Grep/Glob on the findings files (and the corpus if needed to check a number).")
    if a.get("needs") == "ledger":
        prompt += (f"\n\nIMPORTANT: this is a follow-up research wave. Everything found so far is in the evidence ledger at "
                   f"{LEDGER} and the open gaps are in {GAPS}. Read both FIRST. Report ONLY evidence that is not already in "
                   f"the ledger, or that materially corrects, updates or quantifies a ledger item (cite its E-number). "
                   f"Do not restate known evidence. If you find nothing new and useful, say exactly 'NO NEW EVIDENCE' "
                   f"and explain briefly what you checked.")
    if a.get("needs") == "research":
        prompt += (f"\n\nEVIDENCE LEDGER (deduplicated master list of all evidence found): {LEDGER}\nOPEN GAPS: {GAPS}\n"
                   "FINDINGS FILES FROM ALL RESEARCH AGENTS (the ledger is the index; open these for detail):\n" +
                   "\n".join(f"- {p}" for p in findings_files(exclude={"18", "19", "20"})))
    if retry:
        prompt += "\n\nNOTE: a previous attempt timed out. Work faster: cover the highest-value items first and return sooner."
    tools = ["Read", "Grep", "Glob"] + (["WebSearch", "WebFetch"] if a["kind"] == "web" else [])
    log(f"Agent {a['id']} start ({a['model']}{', web' if a['kind'] == 'web' else ''}): {a['name']}")
    update_state(lambda s: s["agents"].setdefault(a["id"], {}).update(status="running", started=now(), name=a["name"]))
    text, cost = call_claude(prompt, a["model"], tools, [WORK, CORE, OUT_DIR], timeout, BUDGET[a["model"]])

    def upd(s):
        s["cost_usd"] = round(s["cost_usd"] + cost, 4)
        r = s["agents"].setdefault(a["id"], {})
        r["cost_usd"] = round(r.get("cost_usd", 0) + cost, 4)
        r["attempts"] = r.get("attempts", 0) + 1
        r.update(status="done", finished=now()) if text else r.update(status="failed")
    if text:
        slug = re.sub(r"[^a-z0-9]+", "_", a["name"].lower()).strip("_")[:60]
        (OUT_DIR / f"{a['id']}_{slug}.md").write_text(
            f"# Agent {a['id']}: {a['name']}\n\n*Model: {a['model']}. Run {now()}. Cost ${cost:.2f} (API-equivalent).*\n\n"
            f"**Assignment:** {a['task']}\n\n{text}\n", encoding="utf-8")
    st = update_state(upd)
    log(f"Agent {a['id']} {'done' if text else 'FAILED'} (${cost:.2f}; job total ${st['cost_usd']:.2f} of cap ${st['cap_usd']:.2f})")
    if not text and not retry and st["agents"][a["id"]]["attempts"] < 2:
        return run_agent(a, retry=True, final=final)
    return bool(text)


def run_pool(agents, final=False):
    with ThreadPoolExecutor(max_workers=CONCURRENCY) as ex:
        list(ex.map(lambda a: run_agent(a, final=final), agents))


def simple_call(label, prompt, model="sonnet", timeout=30 * 60):
    """A single non-agent helper call (ledger, planner, judge), metered against the job."""
    log(f"{label} ({model}) start")
    text, cost = call_claude(prompt, model, ["Read", "Grep", "Glob"], [WORK, OUT_DIR], timeout, BUDGET[model])
    st = update_state(lambda s: s.update(cost_usd=round(s["cost_usd"] + cost, 4)))
    log(f"{label} {'done' if text else 'FAILED'} (${cost:.2f}; job total ${st['cost_usd']:.2f})")
    return text


def extract_json(text, opener):
    closer = "]" if opener == "[" else "}"
    i, j = text.find(opener), text.rfind(closer)
    if i < 0 or j <= i:
        return None
    try:
        return json.loads(text[i:j + 1])
    except Exception:
        return None


LEDGER_PROMPT = """You are building the master EVIDENCE LEDGER for an overnight research job on Illumina (ILMN). The thesis questions and context are below.

{context}

Read EVERY findings file listed below in full (Read tool). Then output two Markdown sections and nothing else:

## Evidence ledger
One line per distinct, decision-relevant piece of evidence, deduplicated across files (merge duplicates; keep the best citation; note how many independent sources corroborate). Format each line exactly:
E### | THEME | claim with the key numbers and dates | FACT/MGMT/OPINION | source (publisher/file, date, URL if web) | corroboration: n
THEME is one of: Q1-OVEREARNING, Q2-VOLUME, PRICING, CUSTOMERS, COMPETITORS, MANAGEMENT, ALT-DATA, MARKET, OTHER. Number from E001. Include every useful item (expect 150-400 lines); omit trivia.

## Open gaps
A numbered list (10-25) of the most valuable unanswered questions, unresolved contradictions, missing quantifications and unexplored sources (corpus or web) that a further research wave could close, each with a suggested source or method.

FINDINGS FILES:
{files}"""

PLAN_PROMPT = """You are the research planner for an overnight job on Illumina (ILMN). Context and thesis questions:

{context}

Read the evidence ledger ({ledger}) and the open gaps ({gaps}). Previous agent assignments (do not repeat them; go to new sources, angles or deeper quantification):
{previous}

Design the next research wave: exactly 4 agents, each with a narrow, concrete, non-overlapping assignment aimed at the highest-value remaining gaps for the two thesis questions, management conduct, and customer/competitor read-through. Favor sources not yet used (specific filings, transcripts, price lists, government datasets, trade press, patents, court dockets, procurement records, conference posters, company websites). Each agent has ~20 minutes and either web tools ("web") or only the local corpus ("internal").
Output ONLY a JSON array of 4 objects: [{{"name": "...", "kind": "web" or "internal", "task": "detailed instructions naming the exact sources/queries to pursue and what to quantify"}}]"""

JUDGE_PROMPT = """You are a strict novelty judge for an overnight research job on Illumina (ILMN). Thesis questions: (1) is Illumina over-earning on clinical consumables as the remaining NovaSeq 6000 volume converts to the NovaSeq X; (2) will clinical volume growth offset the price decline per Gb; plus management conduct/credibility and read-through from clinical customers and competitors.

Read the current evidence ledger ({ledger}) and the open gaps ({gaps}), then read these new findings files from the latest wave:
{files}

Accept an item ONLY if it is (a) NOVEL: not already in the ledger in substance (a new source repeating a known claim adds at most a corroboration note, which is NOT novel), and (b) INCREMENTALLY USEFUL: it adds a new fact, a new number or quantification, a materially better or more recent source, a correction, or a new angle that could change or sharpen the answer to the thesis questions, management assessment, or read-through. Reject restatements, generic commentary, unsourced speculation, and items you cannot tie to a cited source.

Output ONLY a JSON object:
{{"new_items": ["THEME | claim with numbers and dates | FACT/MGMT/OPINION | source (publisher/file, date, URL) | corroboration: n", ...],
 "corrections": ["E### : what changes and why (source)", ...],
 "updated_gaps": ["numbered-list-ready gap text with suggested source", ...],
 "rationale": "one or two sentences on why the wave did or did not add value"}}
Use an empty list when there are no new items. Be strict: when in doubt, reject."""


def build_ledger():
    files = "\n".join(f"- {p}" for p in findings_files(exclude={"18", "19", "20"}))
    text = simple_call("Evidence ledger", LEDGER_PROMPT.format(context=CONTEXT.replace("{minutes}", "30"), files=files))
    if not text or "## Evidence ledger" not in text:
        return False
    led, _, gaps = text.partition("## Open gaps")
    LEDGER.write_text("# Evidence ledger\n\n" + led.replace("## Evidence ledger", "").strip() + "\n", encoding="utf-8")
    GAPS.write_text("# Open gaps\n\n" + gaps.strip() + "\n", encoding="utf-8")
    n = sum(1 for ln in LEDGER.read_text(encoding="utf-8").splitlines() if re.match(r"E\d+", ln.strip()))
    update_state(lambda s: s.update(ledger_items=n))
    log(f"Ledger built with {n} items")
    return True


def next_agent_id(st):
    used = [int(k) for k in st["agents"] if k.isdigit()] + [20]
    return max(used) + 1


def plan_wave(st):
    prev = "\n".join(f"- {k}: {r.get('name', '')}" for k, r in sorted(st["agents"].items(), key=lambda kv: int(kv[0])))
    text = simple_call("Wave planner", PLAN_PROMPT.format(context=CONTEXT.replace("{minutes}", "20"), ledger=LEDGER,
                                                          gaps=GAPS, previous=prev), timeout=20 * 60)
    plan = extract_json(text or "", "[")
    if not isinstance(plan, list) or not plan:
        return None
    start = next_agent_id(st)
    agents = []
    for i, p in enumerate(plan[:4]):
        kind = "web" if str(p.get("kind", "web")).lower().startswith("web") else "internal"
        agents.append(dict(id=str(start + i), name=str(p.get("name", f"Wave agent {start + i}"))[:90], kind=kind,
                           model="sonnet", needs="ledger", task=str(p.get("task", ""))))
    return agents


def judge_wave(ids):
    files = [p for p in findings_files() if p.name.split("_")[0] in ids]
    if not files:
        return 0, "no findings files produced"
    text = simple_call("Novelty judge", JUDGE_PROMPT.format(ledger=LEDGER, gaps=GAPS,
                                                            files="\n".join(f"- {p}" for p in files)), timeout=25 * 60)
    res = extract_json(text or "", "{")
    if not isinstance(res, dict):
        return None, "judge failed"
    items = [x for x in res.get("new_items", []) if isinstance(x, str) and x.strip()]
    led = LEDGER.read_text(encoding="utf-8")
    n0 = sum(1 for ln in led.splitlines() if re.match(r"E\d+", ln.strip()))
    add = "".join(f"E{n0 + i + 1:03d} | {x.strip()} | (wave agents {', '.join(ids)})\n" for i, x in enumerate(items))
    corr = res.get("corrections") or []
    if corr:
        add += "".join(f"CORRECTION ({', '.join(ids)}): {c}\n" for c in corr if isinstance(c, str))
    if add:
        LEDGER.write_text(led.rstrip() + "\n" + add, encoding="utf-8")
    gaps = res.get("updated_gaps") or []
    if gaps:
        GAPS.write_text("# Open gaps\n\n" + "\n".join(f"{i}. {re.sub(r'^[0-9]+[.)] *', '', g)}"
                                                      for i, g in enumerate(gaps, 1)) + "\n", encoding="utf-8")
    update_state(lambda s: s.update(ledger_items=n0 + len(items)))
    return len(items), str(res.get("rationale", ""))[:500]


def research_loop():
    if not LEDGER.exists():
        if not (build_ledger() or build_ledger()):
            log("Ledger could not be built; skipping the iterative loop")
            return
    fails = 0
    while True:
        st = load_state()
        if st.get("saturated"):
            return
        if len(st.get("waves", [])) >= MAX_WAVES:
            log("Max waves reached; ending research loop")
            return
        if not research_ok():
            log("Research budget reached (cap less reserve) or stop flag; ending research loop")
            update_state(lambda s: s.update(loop_end="budget"))
            return
        cur = st.get("current_wave")
        if not cur:
            agents = plan_wave(st)
            if not agents:
                fails += 1
                if fails >= 3:
                    log("Planner failed 3 times; ending research loop")
                    return
                continue
            n = len(st.get("waves", [])) + 1
            update_state(lambda s: s.update(current_wave={"n": n, "agents": agents}, stage=f"research wave {n}"))
            cur = {"n": n, "agents": agents}
        log(f"Wave {cur['n']}: " + "; ".join(f"{a['id']} {a['name']}" for a in cur["agents"]))
        run_pool(cur["agents"])
        ids = [a["id"] for a in cur["agents"]]
        if not any(load_state()["agents"].get(i, {}).get("status") == "done" for i in ids):
            # nothing ran (budget or failures): do not count as saturation
            update_state(lambda s: s.update(current_wave=None))
            fails += 1
            if fails >= 3:
                return
            continue
        new, why = judge_wave(ids)
        if new is None:
            new, why = judge_wave(ids)
        if new is None:
            new, why = -1, "judge failed twice"
        rec = {"n": cur["n"], "agents": ids, "new_items": new, "why": why, "t": now()}
        update_state(lambda s: (s.setdefault("waves", []).append(rec), s.update(current_wave=None)))
        log(f"Wave {cur['n']} added {new} new evidence items. {why}")
        if new == 0:
            update_state(lambda s: s.update(saturated=True, loop_end="saturated"))
            log("Saturation: a full wave found no new, incrementally useful evidence. Ending research loop.")
            return


PARTS_DIR = OUT_DIR / "addendum_parts"

SPEC = """THE ANALYST'S SPECIFICATIONS (the document must satisfy every one):
1. It answers both thesis questions directly, leading with the answer, then explaining: (Q1) is Illumina over-earning on clinical consumables once the remaining NovaSeq 6000 business (Q2 2026: ~17% of HT volume, ~41% of HT revenue; clinical ~22% of volume) converts to the NovaSeq X; (Q2) what is go-forward clinical volume growth and will it offset the price decline per Gb on the X versus the 6000.
2. It covers management conduct and credibility in and outside calls (the "shady things": changed or dropped metrics, definitions, guidance games, accounting choices, insider selling, pay-metric changes, contradictions, dodged questions), and read-through from end customers (clinical labs) and from competitors, plus all other relevant evidence found (broad, not just those topics).
3. It is "a readable, well-written list summary containing all evidence": organized, numbered evidence lists grouped by theme, each item one to three sentences, and EVERY item in the evidence ledger appears (near-duplicates merged into one item that cites all of their E-numbers).
4. Writing rules (the user's standing rules): full, well-written, simple sentences and short paragraphs; lead with the answer; contextualize every number (what it measures, the period, the comparison: prior period, guidance, consensus or peers, and why it matters); assume a smart reader with little background and explain each piece of jargon in a few plain words the first time it appears; primer-style explanations build from the basics and explain the why; distinguish facts, management claims and opinions, saying who said what and when with light citations like "(Q2 2026 call)" or "(Natera 10-Q, Aug 2026)"; point out where sources disagree and where information may be stale; tables are fine for comparisons but every table is introduced by prose saying what it shows and what to take from it. No word or number vomit.
5. Each evidence item carries its ledger tag(s) in square brackets at the end, e.g. [E041, E210], in addition to the light citation.
6. It is a Core Notes section: it starts with "# 16 Addendum: Is Illumina Over-Earning on Clinical Consumables?" and an as-of line, stands alone, and ends with how it was built and its limits."""


def ledger_ids():
    return set(re.findall(r"^E(\d{3,4})\b", LEDGER.read_text(encoding="utf-8"), re.M))


def assemble_parts():
    parts = sorted(PARTS_DIR.glob("part_*.md"), key=lambda p: int(re.findall(r"\d+", p.stem)[0]))
    return "\n\n".join(p.read_text(encoding="utf-8").strip() for p in parts).strip() + "\n", parts


def cited_ids(doc):
    ids = set()
    for grp in re.findall(r"\[(E\d[^\]]*)\]", doc):
        for a, b in re.findall(r"E(\d{1,4})(?:\s*[-–]\s*E?(\d{1,4}))?", grp):
            if b:
                ids.update(f"{i:03d}" for i in range(int(a), int(b) + 1))
            else:
                ids.add(f"{int(a):03d}")
    return ids


def opus_parts_call(label, prompt):
    log(f"{label} (opus) start")
    text, cost = call_claude(prompt, "opus", ["Read", "Grep", "Glob", "Write", "Edit"], [WORK, CORE, OUT_DIR],
                             8 * 3600, 150)
    st = update_state(lambda s: s.update(cost_usd=round(s["cost_usd"] + cost, 4)))
    log(f"{label} done (${cost:.2f}; job total ${st['cost_usd']:.2f}). Reply: {(text or '')[:120]!r}")
    return text


def write_addendum():
    st = load_state()
    if ADDENDUM.exists() and st.get("addendum_done"):
        return True
    PARTS_DIR.mkdir(parents=True, exist_ok=True)
    for p in PARTS_DIR.glob("part_*.md"):
        p.unlink()
    n_led = len(ledger_ids())
    files = "\n".join(f"- {p}" for p in findings_files())
    update_state(lambda s: s.update(stage="synthesis"))
    prompt = (SYNTH_PROMPT.format(core=CORE).replace("Output ONLY the Markdown document.", "") + "\n\n" + SPEC +
              f"\n\nMASTER EVIDENCE LEDGER ({n_led} numbered items, E001 onward; your evidence lists must cover ALL of "
              f"them, grouped and deduplicated, each tagged with its E-numbers): {LEDGER}\nOPEN GAPS: {GAPS}\n"
              f"Waves run: {json.dumps(st.get('waves', []))[:3000]}\n\nFINDINGS FILES (open for detail; 18 = model, "
              f"19 = red team, 20 = fact-check, 21+ = follow-up waves):\n" + files +
              f"\n\nHOW TO DELIVER (important): the document is long. Take the time you need. Write it to disk in order, "
              f"in parts, using the Write tool: {PARTS_DIR}\\part_01.md, part_02.md, part_03.md, ... Each part holds "
              f"one or more whole sections (never split a list mid-item) and at most about 4,000 words. Part 01 starts "
              f"with the title and the as-of line. Do not repeat content across parts. Before finishing, re-read the "
              f"ledger and confirm every E-number is cited somewhere. Then reply with exactly: DONE <number of parts>.")
    opus_parts_call("Synthesis (writing addendum in parts)", prompt)
    doc, parts = assemble_parts()
    if not parts or len(doc.split()) < 4000:
        log(f"Synthesis produced {len(doc.split())} words in {len(parts)} parts; treating as failed")
        return False
    # Up to 3 rounds: mechanical ledger-coverage check plus a specification review, then targeted revision.
    for rnd in range(1, 4):
        doc, parts = assemble_parts()
        missing = sorted(ledger_ids() - cited_ids(doc), key=int)
        review = simple_call(f"Spec review round {rnd}", f"""You are reviewing a draft research document against the analyst's specifications. Read every part file in order:
{chr(10).join(f'- {p}' for p in parts)}

{SPEC}

Grade strictly. Output ONLY a JSON object: {{"pass": true/false, "issues": ["specific, actionable issue with the part file and section it is in", ...]}}.
Fail it for any material violation: unexplained jargon, numbers without context, missing fact/claim/opinion distinction, untagged evidence items, tables without an introduction, a missing required topic, walls of text, sections that are not readable lists, or a weak or buried answer. Ignore trivial style nits. List at most 25 issues, most important first.""", timeout=40 * 60)
        res = extract_json(review or "", "{") or {}
        issues = [i for i in res.get("issues", []) if isinstance(i, str)]
        passed = bool(res.get("pass")) and not issues
        log(f"Review round {rnd}: {len(missing)} ledger items uncited; spec {'PASS' if passed else f'{len(issues)} issues'}")
        update_state(lambda s: s.update(review=dict(round=rnd, uncited=len(missing), issues=issues[:25], passed=passed)))
        if not missing and passed:
            break
        fix = "REVISION TASK. The draft addendum is in these part files (edit them in place with Edit/Write; keep the part structure):\n"
        fix += "\n".join(f"- {p}" for p in parts) + "\n\n" + SPEC + f"\n\nLedger: {LEDGER}\n"
        if missing:
            fix += (f"\n1. These {len(missing)} ledger items are not cited anywhere. Add each one to the right section as "
                    f"a well-written evidence item (or merge it into an existing item if it is a near-duplicate, adding "
                    f"its tag): " + ", ".join(f"E{m}" for m in missing) + "\n")
        if issues:
            fix += "\n2. Fix these specification issues:\n" + "\n".join(f"- {i}" for i in issues) + "\n"
        fix += "\nDo not delete correct content. When finished, reply with exactly: DONE."
        opus_parts_call(f"Revision round {rnd}", fix)
    doc, parts = assemble_parts()
    words = len(doc.split())
    uncited = len(ledger_ids() - cited_ids(doc))
    ADDENDUM.write_text(doc, encoding="utf-8")
    ADDENDUM_COPY.write_text(doc, encoding="utf-8")
    update_state(lambda s: s.update(addendum_done=True, addendum_words=words, addendum_uncited=uncited))
    log(f"Addendum written ({words:,} words in {len(parts)} parts; {uncited} ledger items still uncited)")
    return True


def write_html():
    from md_to_html import convert
    md = ADDENDUM.read_text(encoding="utf-8")
    page = convert(md, "Clinical Consumables Thesis",
                   "Is Illumina over-earning on clinical consumables as the NovaSeq 6000 converts to the X? "
                   "All evidence, as of 2026-10-11.")
    HTML_OUT.write_text(page, encoding="utf-8")
    update_state(lambda s: s.update(html_done=True))
    log(f"HTML written by converter ({len(page):,} chars)")
    return True


def cmd_finalize(args):
    """Redo the write-up and page from the finished research (used after a bad synthesis)."""
    keep_awake(True)
    try:
        update_state(lambda s: s.update(addendum_done=False, html_done=False, published=None, stage="synthesis",
                                        pid=os.getpid()))
        stop_hb = threading.Event()

        def heartbeat():
            while not stop_hb.wait(120):
                try:
                    update_state(lambda s: None)
                except Exception as e:
                    log(f"  heartbeat write failed (will retry): {e!r}")
        threading.Thread(target=heartbeat, daemon=True).start()
        ok = write_addendum() or write_addendum()
        if ok:
            write_html()
            finish_files()
        stop_hb.set()
        st = update_state(lambda s: s.update(stage="complete" if ok else "failed", finished=now()))
        log(f"Finalize {st['stage']}. Total API-equivalent spend ${st['cost_usd']:.2f}.")
    except BaseException:
        import traceback
        log("CRASH (finalize):\n" + traceback.format_exc())
        raise
    finally:
        keep_awake(False)


def finish_files():
    # 00_Start_Here: list the new file in the Core Notes table.
    start = CORE / "00_Start_Here.md"
    s = start.read_text(encoding="utf-8")
    row = ("| `16_Addendum_Clinical_Consumables_Thesis.md` | Addendum (2026-10-11): whether Illumina is over-earning on "
           "clinical consumables as the NovaSeq 6000 converts to the X, clinical volume growth versus price declines, "
           "management conduct, and customer and competitor read-through, with all evidence listed. |")
    if "16_Addendum" not in s:
        anchor = re.search(r"^\| `15_Peer_MGI_Tech\.md` \|.*$", s, re.M)
        if anchor:
            s = s[:anchor.end()] + "\n" + row + s[anchor.end():]
        start.write_text(s, encoding="utf-8")
    # INDEX.md: refresh the auto-generated Outputs section.
    idx = WORK / "INDEX.md"
    t = idx.read_text(encoding="utf-8")
    outs = sorted(p for p in (WORK / "Outputs").rglob("*") if p.is_file())
    block = "## Outputs\n\n" + "\n".join(f"- `{p.relative_to(WORK).as_posix()}`" for p in outs) + "\n"
    t = t[:t.index("## Outputs")] + block if "## Outputs" in t else t.rstrip() + "\n\n" + block
    idx.write_text(t, encoding="utf-8")


def cmd_run(args):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    keep_awake(True)
    st = load_state()
    if not st.get("started"):
        st["started"] = now()
        st["started_ts"] = time.time()
    st["stage"] = "research"
    st["pid"] = os.getpid()
    save_state(st)
    stop_hb = threading.Event()

    def heartbeat():
        while not stop_hb.wait(120):
            try:
                update_state(lambda s: None)
            except Exception as e:  # never let the heartbeat thread die
                log(f"  heartbeat write failed (will retry): {e!r}")
    threading.Thread(target=heartbeat, daemon=True).start()
    try:
        log(f"Job running (pid {os.getpid()}); cap ${st['cap_usd']:.2f} ({'calibrated' if st['calibrated'] else 'provisional'})")
        research = [a for a in AGENTS if not a.get("needs")]
        analysis = [a for a in AGENTS if a.get("needs")]
        run_pool(research)
        research_loop()
        update_state(lambda s: s.update(stage="analysis"))
        run_pool(analysis, final=True)
        if write_addendum():
            write_html()
        finish_files()
        st = update_state(lambda s: s.update(stage="complete" if s.get("addendum_done") else "failed",
                                             finished=now()))
        log(f"Job {st['stage']}. Total API-equivalent spend ${st['cost_usd']:.2f}.")
    except BaseException:
        import traceback
        log("CRASH:\n" + traceback.format_exc())
        raise
    finally:
        stop_hb.set()
        keep_awake(False)


def cmd_start(args):
    st = load_state()
    if args.baseline is not None and st.get("baseline_pct") is None:
        st["baseline_pct"] = args.baseline
        st["baseline_time"] = now()
        save_state(st)
    exe = Path(sys.executable)
    pyw = exe.with_name("pythonw.exe") if os.name == "nt" else exe
    if not pyw.exists():
        pyw = exe
    # Reset agents left "running" by a dead process so they rerun.
    def reset(s):
        for r in s["agents"].values():
            if r.get("status") == "running":
                r["status"] = "pending"
    update_state(reset)
    # Launch through WMI so the job is a child of the WMI service, not of the calling shell. Processes started
    # from an app/agent shell are killed with that shell's job object when the session goes idle.
    cmdline = f'"{pyw}" "{Path(__file__).resolve()}" run'
    ps = ("$r = Invoke-CimMethod -ClassName Win32_Process -MethodName Create -Arguments "
          f"@{{CommandLine='{cmdline}'; CurrentDirectory='{ROOT}'}}; "
          "Write-Output (\"rc=\" + $r.ReturnValue + \" pid=\" + $r.ProcessId)")
    out = subprocess.run(["powershell", "-NoProfile", "-Command", ps], capture_output=True, text=True)
    print(f"Launched via WMI: {out.stdout.strip()} {out.stderr.strip()[:200]}. "
          f"Check with: python _Build/clinical_scrape.py status")


def cmd_status(args):
    st = load_state()
    hb = st.get("heartbeat", 0)
    age = (time.time() - hb) / 60 if hb else None
    stalled = st.get("stage") not in ("complete", "failed", "new") and (age is None or age > 25)
    print(f"stage: {st.get('stage')}  started: {st.get('started')}  heartbeat: {st.get('heartbeat_human')}"
          f" ({'%.0f' % age if age is not None else '?'} min ago){'  STALLED' if stalled else ''}")
    print(f"spend: ${st['cost_usd']:.2f} of cap ${st['cap_usd']:.2f} ({'calibrated' if st['calibrated'] else 'provisional'});"
          f" baseline weekly {st.get('baseline_pct')}%; stop={st.get('stop')}; paused_until={st.get('paused_until')}")
    for k in sorted(st["agents"]):
        r = st["agents"][k]
        print(f"  {k} {r.get('status'):<12} ${r.get('cost_usd', 0):.2f}  {r.get('name', '')}")
    print(f"ledger items: {st.get('ledger_items')}  saturated: {st.get('saturated', False)}  loop_end: {st.get('loop_end')}")
    for w in st.get("waves", []):
        print(f"  wave {w['n']} ({', '.join(w['agents'])}): +{w['new_items']} new items. {w.get('why', '')[:150]}")
    print(f"addendum: {st.get('addendum_done', False)}  html: {st.get('html_done', False)}  published: {st.get('published')}")


def cmd_usage(args):
    """Calibrate the cap from the account-wide weekly % (the job ran alone for its first ~45 minutes)."""
    pct = args.pct

    def upd(s):
        s.setdefault("samples", []).append({"t": now(), "pct": pct, "cost": s["cost_usd"]})
        base = s.get("baseline_pct")
        if base is None:
            s["baseline_pct"] = pct
            return
        if s.get("calibrated"):
            return
        k = pct - base
        spent = s["cost_usd"]
        if spent < 5:
            return
        if k >= 1:
            # displayed delta k means the true delta lies in (k-1, k+1); use a mildly conservative k+0.5
            s["cap_usd"] = round(CAP_PCT * spent / (k + 0.5), 2)
            s["calibrated"] = True
            s["calibration_note"] = f"{now()}: weekly +{k} pts for ${spent:.2f} of job spend"
        else:
            # under 1 pt for this spend: 1% costs more than `spent`, so 10% > 10x spend; keep calibrating
            s["cap_usd"] = round(max(s["cap_usd"], 8 * spent), 2)
            s["calibration_note"] = f"{now()}: weekly +0 pts for ${spent:.2f}; provisional cap raised"
    st = update_state(upd)
    print(f"weekly {pct}% (baseline {st.get('baseline_pct')}%), job spend ${st['cost_usd']:.2f}, "
          f"cap ${st['cap_usd']:.2f} ({'calibrated' if st['calibrated'] else 'provisional'}). {st.get('calibration_note', '')}")
    if st["cost_usd"] >= st["cap_usd"]:
        print("CAP REACHED: no new agents will start.")


def cmd_check(args):
    """Fixed-text command for the hourly self-check: relaunch if stalled or failed, then print status."""
    st = load_state()
    hb = st.get("heartbeat", 0)
    age = (time.time() - hb) / 60
    pid = st.get("pid")
    alive = False
    if pid:
        out = subprocess.run(["tasklist", "/FI", f"PID eq {pid}", "/NH"], capture_output=True, text=True).stdout
        alive = str(pid) in out and "pythonw" in out.lower()
    if st.get("stage") == "complete":
        pass
    elif alive and age <= 90:
        print(f"Job process {pid} alive (last state write {age:.0f} min ago): no action.")
    elif st.get("stage") == "failed" or not alive or age > 90:
        if alive:
            print(f"Job process {pid} alive but silent for {age:.0f} min: treating as hung, killing it.")
            subprocess.run(["taskkill", "/T", "/F", "/PID", str(pid)], capture_output=True)
            time.sleep(3)
        print("Job stalled or failed: relaunching.")
        cmd_start(argparse.Namespace(baseline=None))
        time.sleep(10)
    cmd_status(args)
    st = load_state()
    if st.get("stage") == "complete":
        print("COMPLETE" + ("" if not st.get("published") else " AND PUBLISHED"))


def cmd_published(args):
    update_state(lambda s: s.update(published=args.url))
    print("recorded")


def cmd_stop(args):
    update_state(lambda s: s.update(stop=True))
    print("stop flag set; running agents finish, no new ones start, the write-up still runs")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("run").set_defaults(fn=cmd_run)
    p = sub.add_parser("start"); p.add_argument("--baseline", type=float); p.set_defaults(fn=cmd_start)
    sub.add_parser("status").set_defaults(fn=cmd_status)
    sub.add_parser("check").set_defaults(fn=cmd_check)
    sub.add_parser("finalize").set_defaults(fn=cmd_finalize)
    p = sub.add_parser("usage"); p.add_argument("pct", type=float); p.set_defaults(fn=cmd_usage)
    p = sub.add_parser("published"); p.add_argument("url"); p.set_defaults(fn=cmd_published)
    sub.add_parser("stop").set_defaults(fn=cmd_stop)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
