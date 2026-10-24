#!/usr/bin/env python3
"""
ILMN research-folder builder.

Turns the raw source documents into:
  Working Notes/Sources/   originals, renamed and filed by company and type
  Working Notes/Extracts/  one exhaustive, readable note per source (every word read)
  Working Notes/INDEX.md   one entry per source, used by agents to find material
  Core Notes/              ~150K-token master briefing synthesized from the extracts

Model calls go through the Claude Code CLI in headless mode (`claude -p`), at most
4 at a time, each with a hard timeout. All progress is saved in _Build/state.json,
so the job can be stopped and restarted at any point and picks up where it left off.
When the account hits a usage limit, the script waits for the reset instead of failing.

Commands (run from anywhere):
  python _Build/build.py plan       dry run: show how every file would be classified
  python _Build/build.py selftest   one tiny Haiku call to check the CLI is logged in
  python _Build/build.py start      launch the full build detached (survives closing the chat)
  python _Build/build.py run        full build in the foreground (what `start` launches)
  python _Build/build.py ingest     process new files dropped into Inbox/
  python _Build/build.py status     show progress
  python _Build/build.py resynth K  force a rebuild of Core Notes section K (e.g. 07)
"""
import argparse
import datetime as dt
import glob
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "_Build"
CORE = ROOT / "Core Notes"
WORK = ROOT / "Working Notes"
SOURCES = WORK / "Sources"
EXTRACTS = WORK / "Extracts"
ARCHIVE = WORK / "_Archive"
OUTPUTS = WORK / "Outputs"
INBOX = ROOT / "Inbox"
OLD_ARCHIVE = ROOT / "_Archive (removed duplicates & low-value)"
STATE = BUILD / "state.json"
STATUS = BUILD / "status.json"
LOG = BUILD / "build.log"
SANDBOX = BUILD / "sandbox"          # empty cwd for sub-calls so they never load CLAUDE.md
PARTS = BUILD / "section_parts"

MAX_WORKERS = 4
TIMEOUT = {"haiku": 15 * 60, "sonnet": 20 * 60, "opus": 40 * 60}   # per-call hard stops
MAX_ATTEMPTS = 3
MAX_INPUT_CHARS = {"haiku": 450_000, "sonnet": 600_000, "opus": 500_000}
AS_OF = "2026-10-10"

_lock = threading.Lock()
_pause_until = 0.0
_progress = {"stage": "idle", "done": 0, "total": 0, "failed": 0, "note": ""}


# ----------------------------------------------------------------------------- utils
def log(msg):
    line = f"[{dt.datetime.now():%Y-%m-%d %H:%M:%S}] {msg}"
    with _lock:
        BUILD.mkdir(exist_ok=True)
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    try:
        print(line, flush=True)
    except Exception:
        pass


def read(p):
    return Path(p).read_text(encoding="utf-8", errors="replace")


def write_atomic(p, text):
    p = Path(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(p.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    for i in range(40):   # OneDrive (or antivirus) can briefly lock a file it is syncing; wait and retry
        try:
            os.replace(tmp, p)
            return
        except PermissionError:
            time.sleep(0.5 + i * 0.25)
    p.write_text(text, encoding="utf-8")   # last resort: overwrite in place
    tmp.unlink(missing_ok=True)


def load_state():
    if STATE.exists():
        return json.loads(read(STATE))
    return {"files": {}, "sections": {}}


def save_state(state):
    with _lock:
        write_atomic(STATE, json.dumps(state, indent=1, ensure_ascii=False))


def write_status(extra=None):
    s = dict(_progress)
    s["heartbeat"] = time.time()
    s["heartbeat_human"] = f"{dt.datetime.now():%Y-%m-%d %H:%M:%S}"
    s["pid"] = os.getpid()
    s["paused_until"] = (dt.datetime.fromtimestamp(_pause_until).strftime("%H:%M")
                         if _pause_until > time.time() else None)
    if extra:
        s.update(extra)
    write_atomic(STATUS, json.dumps(s, indent=1))


def heartbeat_loop(stop):
    while not stop.is_set():
        write_status()
        stop.wait(30)


def safe_name(s, n=110):
    s = re.sub(r"[^\w\-. ]+", "", s).strip().replace(" ", "_")
    s = re.sub(r"_+", "_", s)
    return s[:n].rstrip("_.")


MONTHS = {m: i for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}


def date_from_text(text):
    m = re.search(r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.? (\d{1,2}), (20\d\d)", text[:4000])
    if m:
        return f"{m.group(3)}-{MONTHS[m.group(1).lower()]:02d}-{int(m.group(2)):02d}"
    m = re.search(r"(\d{2}) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* (20\d\d)", text[:4000])
    if m:
        return f"{m.group(3)}-{MONTHS[m.group(2).lower()]:02d}-{int(m.group(1)):02d}"
    return ""


# ----------------------------------------------------------------------- classification
ROCHE_KEEP = (
    "20260917_JP_Morgan_ROP-SW_Roche-_Key_Takeaways_from_our_2026_CEO_Call",
    "20261002_Barclays_ROP-SW_Roche-_MedTech_-_Life_Sciences_Investor_Trip",
    "20260919_UBS_ROP-SW_First_Read-_Roche_-UBS_2026_Bus_Tour",
)
ARCHIVE_RX = [
    r"_NOVOB-DC_", r"_AZN-LN_", r"_SAN-FP_", r"_ALM-SM_", r"Slingshot_Insights",
    r"^20\d{6}_(GSK|Amgen|Abbvie|Roche-_Bristol|Roche_Polivy|Roche_Launch|Biotech|"
    r"European_Healthcare|Europe_Earnings|Health_Care_Growth|Upcoming_COL)",
    r"^roche investor day\.md$",      # Jun-2026 obesity-drug (ADA) call: pharma only
    r"^roche megatranscript\.md$",    # Sep-2026 Pharma Day: pharma only
]
DECKS = {"49": "ILMN_2026Q2_Earnings_Slides.md", "50": "ILMN_2026Q1_Earnings_Slides.md",
         "51": "ILMN_2025Q4_Earnings_Slides.md", "52": "ILMN_2026-01-13_JPM_Healthcare_Conference_Slides.md",
         "53": "ILMN_2025Q3_Earnings_Slides.md", "54": "ILMN_2025Q2_Earnings_Slides.md"}
PEER_TRANSCRIPT_PREFIX = {"Oxford Nanopore": "ONT", "Pacific Biosciences": "PACB", "Thermo Fisher": "TMO"}


def E(company, doctype, tier, model, newname=None):
    return {"company": company, "doctype": doctype, "tier": tier, "model": model, "newname": newname}


def clean_transcript_title(name):
    t = re.sub(r"\.md$", "", name)
    t = re.sub(r"^.*?\([A-Z]{2,6}\)\s*", "", t)
    t = re.sub(r"\s*_\s*Seeking Alpha.*$", "", t)
    t = re.sub(r"\(?Transcript\)?", "", t)
    t = t.replace("Presents at ", "").replace(" - ", " ")
    return safe_name(t, 80)


def filing_name(text):
    head = text[:3000]
    m = re.search(r"Quarterly Period Ended (\w+) (\d+), (20\d\d)", head, re.I)
    if m:
        # Illumina's fiscal quarters can end a few days into the next month (e.g. Q1 2022 ended Apr 3).
        mo = MONTHS[m.group(1)[:3].lower()] - (1 if int(m.group(2)) <= 7 else 0)
        return f"ILMN_10-Q_{m.group(3)}Q{(mo - 1) // 3 + 1}.md"
    m = re.search(r"fiscal year ended (\w+) (\d+), (20\d\d)", head, re.I)
    if m:
        yr = int(m.group(3)) - (1 if m.group(1).lower().startswith("jan") else 0)
        return f"ILMN_10-K_FY{yr}.md"
    return None


# Low-value or duplicate material, kept out of the analysis (decided with the user on 2026-10-10).
LOWVALUE_RX = [
    r"_Smart_Insider_", r"_Acquisdata_", r"_Financial_AI_", r"_PharmaBoardroom_",
    r"S-P_500", r"^20260723_Illumina_Charting_a_Path",   # BI timeline; byte-identical to the 20260731 file
    r"^TMO Q2\.md$", r"^tmo ms conference\.md$",         # re-saves of Thermo transcripts already filed
]


def classify(name, text):
    if any(re.search(rx, name) for rx in LOWVALUE_RX):
        return E("OTHER", "low_value", "archive", None)
    if any(re.search(rx, name) for rx in ARCHIVE_RX):
        return E("OTHER", "pharma", "archive", None)
    if "_ROP-SW_" in name:
        if name.startswith(ROCHE_KEEP):
            return E("ROCHE", "research", "core", "sonnet")
        return E("OTHER", "pharma", "archive", None)
    if name.startswith("0001110803-") or name == "Q2_2026_10Q.md":
        return E("ILMN", "filing", "working", "haiku", filing_name(text))
    m = re.match(r"Illumina, Inc\. \(ILMN\) Q(\d) (\d{4}) Earnings Call", name)
    if m:
        return E("ILMN", "earnings_call", "core", "sonnet", f"ILMN_{m.group(2)}Q{m.group(1)}_Earnings_Call.md")
    if name.startswith("Illumina, Inc. (ILMN)"):
        return E("ILMN", "conference", "core", "sonnet",
                 f"ILMN_{date_from_text(text) or 'undated'}_{clean_transcript_title(name)}.md")
    m = re.match(r"original \((\d+)\)\.md", name)
    if m and m.group(1) in DECKS:
        return E("ILMN", "deck", "core", "sonnet", DECKS[m.group(1)])
    if name.startswith(("ILMN - ExpertCall", "Former ", "Global Segment Lead", "Senior Director of",
                        "Single Cell Genomic")):
        h1 = re.search(r"#\s*\*\*(.+?)\*\*", text[:1500])
        if name.startswith("ILMN - ExpertCall") and h1:
            dates = re.findall(r"\d{2} (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) 20\d\d", text[:2500])
            d = date_from_text(dates[1] if len(dates) > 1 else (dates[0] if dates else ""))
            return E("ILMN", "expert_call", "core", "sonnet", f"Expert_{d or 'undated'}_{safe_name(h1.group(1), 90)}.md")
        return E("ILMN", "expert_call", "core", "sonnet", "Expert_Tegus_" + safe_name(name[:-3], 90) + ".md")
    if re.match(r"ILMN (Annuals|Quarterlies)", name):
        return E("ILMN", "consensus", "core", "sonnet", "ILMN_Consensus_" + safe_name(name[5:-3]) + ".md")
    if "OpenInsider" in name or "_ILMN-_Illumina_Meister" in name:
        return E("ILMN", "insider_data", "working", "haiku")
    if "Priced For Perfection" in name:
        return E("ILMN", "research", "core", "sonnet", "20260908_SeekingAlpha_ILMN_Priced_For_Perfection.md")
    if "_ONT-LN_" in name:
        if "Proactive_Investors" in name:
            return E("ONT", "news", "working", "haiku")
        return E("ONT", "research", "core", "sonnet")
    if "_PACB_" in name:
        return E("PACB", "research", "core", "sonnet")
    if "_688114-CH_" in name:
        return E("MGI", "research", "core", "sonnet")
    if "_MEDP_" in name:
        return E("SECTOR", "research", "core", "sonnet", name.replace("_MEDP_", "_SECTOR-Tools_"))
    if re.match(r"20\d{6}_", name) and re.search(r"ILMN|Illumina|Sequencing_Market", name):
        return E("ILMN", "research", "core", "sonnet")
    for prefix, tk in PEER_TRANSCRIPT_PREFIX.items():
        if name.startswith(prefix):
            return E(tk, "transcript", "core", "sonnet",
                     f"{tk}_{date_from_text(text) or 'undated'}_{clean_transcript_title(name)}.md")
    low = name.lower()
    if low == "roche q1.md":   # despite the filename, this is the Q2/H1 2026 results call
        return E("ROCHE", "transcript", "core", "sonnet", "ROCHE_2026-07-23_H1_2026_Results_Call.md")
    if low == "roche shareholder day.md":
        return E("ROCHE", "transcript", "core", "sonnet", "ROCHE_2026-05-12_Investor_Day_Diagnostics_AXELIOS.md")
    if low == "txg q1.md":
        return E("TXG", "transcript", "core", "sonnet", "TXG_2026-05-07_Q1_2026_Earnings_Call.md")
    if low == "txg bofa healthcare conference.md":
        return E("TXG", "transcript", "core", "sonnet", "TXG_2026-05-13_BofA_Global_Healthcare_Conference.md")
    if low == "txg shareholder stuff.md":
        return E("TXG", "annual_meeting", "working", "haiku", "TXG_2026-06-04_Annual_Shareholder_Meeting.md")
    cons = {"mgi financials.md": ("MGI", "MGI_Consensus_Annual.md"),
            "ont annuals.md": ("ONT", "ONT_Consensus_Annual.md"),
            "ont semi-annuals.md": ("ONT", "ONT_Consensus_Semiannual.md"),
            "pacb quarterlies.md": ("PACB", "PACB_Consensus_Quarterly_2025Q1-2027Q2.md"),
            "pacb quartlies 2.md": ("PACB", "PACB_Consensus_Quarterly_2026Q3-2028Q4.md"),
            "roche annuals.md": ("ROCHE", "ROCHE_Consensus_Annual.md"),
            "roche quartlies.md": ("ROCHE", "ROCHE_Consensus_Quarterly.md")}
    if low in cons:
        return E(cons[low][0], "consensus", "working", "haiku", cons[low][1])
    return None


def classify_with_haiku(name, text):
    """Fallback for unrecognized new files (used by ingest)."""
    prompt = ("Classify this research document for an Illumina (ILMN) research folder. Reply with ONLY a JSON "
              'object: {"company": ticker such as ILMN, PACB, ONT, ROCHE, TMO, TXG, MGI, SECTOR or OTHER, '
              '"doctype": one of earnings_call, conference, transcript, expert_call, research, consensus, filing, '
              'deck, news, insider_data, other, "relevant": true if it concerns genomics/sequencing/life-science '
              f'tools, else false}}.\nFilename: {name}\n\n{text[:6000]}')
    out = call_claude(prompt, "haiku")
    m = re.search(r"\{.*\}", out or "", re.S)
    if not m:
        return None
    j = json.loads(m.group(0))
    if not j.get("relevant", True):
        return E("OTHER", "other", "archive", None)
    company, doctype = j.get("company", "OTHER"), j.get("doctype", "other")
    core = (company == "ILMN" and doctype in ("earnings_call", "conference", "expert_call", "research", "consensus", "deck")) \
        or (company != "ILMN" and doctype in ("earnings_call", "transcript", "conference", "research"))
    return E(company, "transcript" if company != "ILMN" and doctype in ("earnings_call", "conference") else doctype,
             "core" if core else "working", "sonnet" if core else "haiku")


# ---------------------------------------------------------------------------- model calls
def find_claude():
    w = shutil.which("claude")
    if w:
        return w
    # The desktop app is a packaged Windows app: inside it, %APPDATA%\Claude is redirected to
    # %LOCALAPPDATA%\Packages\Claude_*\LocalCache\Roaming\Claude, so search both locations.
    cands = glob.glob(os.path.join(os.environ.get("APPDATA", ""), "Claude", "claude-code", "*", "*", "claude.exe"))
    cands += glob.glob(os.path.join(os.environ.get("LOCALAPPDATA", ""), "Packages", "Claude_*", "LocalCache",
                                    "Roaming", "Claude", "claude-code", "*", "*", "claude.exe"))
    if not cands:
        raise SystemExit("Could not find the Claude CLI (claude.exe). Install Claude Code or the desktop app.")

    def ver(p):
        v = Path(p).parent.parent.name
        return tuple(int(x) if x.isdigit() else 0 for x in v.split("."))
    return max(cands, key=lambda p: (ver(p), os.path.getmtime(p)))


class NotLoggedIn(Exception):
    pass


LIMIT_RX = re.compile(r"usage limit|limit reached|hit your limit|limit will reset|resets? (at|in)|"
                      r"rate.?limit|too many requests|\b429\b", re.I)
OVERLOAD_RX = re.compile(r"overloaded|\b529\b|\b5\d\d\b.*error|api error|connection error|ECONNRESET", re.I)


def call_claude(prompt, model, timeout=None, min_len=40):
    """One headless call. Returns text, or None on failure. Waits out usage limits."""
    global _pause_until
    exe = find_claude()
    SANDBOX.mkdir(parents=True, exist_ok=True)
    timeout = timeout or TIMEOUT[model]
    # Drop variables inherited from a desktop-app chat session so every sub-call is a plain,
    # independent CLI run that uses the saved login (~/.claude/.credentials.json).
    env = {k: v for k, v in os.environ.items() if not re.match(r"(CLAUDE|ANTHROPIC)", k)}
    env.update(CLAUDE_CODE_MAX_OUTPUT_TOKENS="64000", DISABLE_AUTOUPDATER="1")
    args = [exe, "-p", "--model", model, "--output-format", "text", "--tools", "",
            "--strict-mcp-config", "--no-session-persistence"]
    flags = 0x08000000 if os.name == "nt" else 0   # CREATE_NO_WINDOW
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
            return None
        blob = (out or "") + "\n" + (err or "")
        if "not logged in" in blob.lower() or "/login" in blob.lower() and len(out or "") < 300:
            raise NotLoggedIn(blob.strip()[:300])
        if p.returncode == 0 and out and len(out.strip()) >= min_len and not (len(out) < 400 and LIMIT_RX.search(out)):
            return out.strip()
        if LIMIT_RX.search(blob):
            with _lock:
                _pause_until = max(_pause_until, time.time() + 20 * 60)
            log(f"  usage limit hit; pausing all workers until {dt.datetime.fromtimestamp(_pause_until):%H:%M} "
                f"(then retrying). Detail: {blob.strip()[:160]!r}")
            continue
        if OVERLOAD_RX.search(blob) and transient < 6:
            transient += 1
            log(f"  transient API error, retry {transient} in 2 min: {blob.strip()[:160]!r}")
            time.sleep(120)
            continue
        log(f"  call failed rc={p.returncode} ({model}): {blob.strip()[:300]!r}")
        return None


# ------------------------------------------------------------------------------ prompts
STYLE = """Writing rules: Write for an intelligent reader with little background in genomics or finance. Use complete, well-written sentences and short paragraphs under clear headings; never dump bare numbers or sentence fragments. Every number must say what it measures, for what period, and what it compares to (prior year, guidance, consensus) whenever the material gives that comparison. The first time a technical or financial term appears, explain it in plain English in a few words, e.g. "consumables (the reagent kits customers must buy for every sequencing run)". Attribute every claim to who made it and when, using short bracketed tags such as [Q2 2026 call], [JPM, 2026-06-15] or [Expert: former Illumina associate director, Jul 2026]. Keep facts, management claims and opinions clearly distinguished. Tables are welcome for dense numeric comparisons, but always introduce a table with prose explaining what it shows."""

TYPE_HINTS = {
    "earnings_call": "Organize as: results and guidance → prepared remarks by speaker → Q&A, with one sub-heading per analyst (name and firm) giving the question and the substance of the answer. Capture every figure and every guidance item, including changes from prior guidance.",
    "conference": "Organize by topic in the order discussed, noting the host analyst and firm. Capture every figure and anything new versus prior earnings calls, plus the tone of management.",
    "transcript": "If this is an earnings call: results and guidance → prepared remarks → Q&A with one sub-heading per analyst. Otherwise organize by topic. Capture every figure and guidance item, and everything said about Illumina, sequencing, competitors, pricing and diagnostics in particular detail.",
    "expert_call": "Begin with the expert's background: their relationship to Illumina (former employee, customer, competitor, channel check), role, seniority, and how recent their experience is. Then organize by topic. Keep the expert's reasoning and every number (prices, market shares, volumes, switching behaviour, timelines, budgets). Note where the expert speaks from direct experience versus speculation.",
    "research": "Capture the rating, price target and any changes, estimate changes (old → new, with reasons), valuation method, the full thesis, risks, any channel checks or survey data, comparisons to consensus, and the firm and analyst names.",
    "consensus": "Explain what the sheet is (source, currency, units, which periods are actual vs. estimate), then reproduce EVERY line item for EVERY period as clean Markdown tables (split wide tables if needed), then add short prose noting implied growth rates, margin trends and anything unusual (for example an estimate that looks like an outlier).",
    "filing": "Focus on segment, product (consumables, instruments, services) and geographic revenue; margins; operating expenses; cash flow; balance sheet; share count and buybacks; legal and regulatory matters (for example GRAIL, China); customer concentration; changes in risk factors; and anything newly disclosed. Reproduce the key financial tables as clean Markdown. Skip generic boilerplate.",
    "deck": "Go slide by slide and capture every figure, chart label, footnote and guidance item.",
}
DEFAULT_HINT = "Capture every fact and figure, organized by topic."

EXTRACT_PROMPT = """You are building research notes on Illumina (ILMN) and its competitors. Below is ONE source document (type: {doctype}; primary company: {company}; file: "{name}"){part_note}.

Read every word. Produce exhaustive notes that capture EVERY distinct piece of information: all numbers (with units, periods and comparisons), guidance and changes to it, strategy, products, customers, pricing, competition, regulation and geography, every analyst question and the substance of every answer, ratings, price targets, estimate changes and their reasons, expert views with their reasoning, risks, and memorable verbatim quotes (short, exact, in quotation marks, attributed). Do not add outside knowledge and do not editorialize. Drop only true boilerplate: legal disclaimers, safe-harbor language, operator instructions, page headers and distribution notices.

{hint}

{style}

Length: as long as needed to lose nothing distinct, typically 20-35% of the source's length.

Begin your reply with this block, filled in:
<<<INDEX
title: <descriptive title>
company: <primary company ticker>
date: <YYYY-MM-DD of the event or publication; best estimate>
source: <publisher, bank or platform, and analyst/speaker names if given>
type: <earnings call | conference | expert call | sell-side research | independent research | consensus estimates | SEC filing | slides | news | insider data | other>
summary: <2-4 plain-English sentences: what this document is and its most important takeaways>
topics: <comma-separated keywords>
INDEX>>>
Then the notes in Markdown (use ## and ### headings). Output nothing else.

=== DOCUMENT ===
{content}"""

SECTION_PROMPT = """You are writing part of the Core Notes: the master briefing that is read first, before every research question about Illumina (ILMN). Section: "{title}".{part_label}

Purpose of this section: {brief}

Below are detailed notes extracted from {n} source documents. Write this section so that it preserves EVERY distinct fact, number, view and quote in these notes while merging repetition: when several sources make the same point, state it once, show how it changed over time, and say who said it. Nothing distinct may be dropped. Organize for understanding: {organize}

{style}

Target length: about {tokens:,} tokens (roughly {words:,} words). This is a firm budget: do not exceed it by more than 10%. Spend the space on substance, not filler.

Use ## and ### headings and do not repeat the section title. After the section text, append these two blocks exactly:
<<<TERMS
<every technical or financial term you used, one per line, as: term :: one-sentence plain-English definition>
TERMS>>>
<<<DATES
<every dated event worth a master timeline, one per line, as: YYYY-MM-DD :: event>
DATES>>>

=== SOURCE NOTES ===
{inputs}"""

OVERVIEW_PROMPT = """Below are the parts of the Core Notes section "{title}". Write a "Key takeaways" overview of about {tokens:,} tokens that orients a newcomer before they read the detail: the most important conclusions, where the sources agree and disagree, and what changed over time. Use a short intro paragraph followed by ## headings or a few well-written paragraphs. Do not add TERMS or DATES blocks.

{style}

=== SECTION PARTS ===
{inputs}"""

CONDENSE_PROMPT = """Below is one section of the Core Notes, the master briefing on Illumina (ILMN) that is read at the start of every research chat. It is currently about {cur:,} words, which is too long. Rewrite it to about {target:,} words (do not exceed {cap:,}).

Preserve every distinct fact, number, date, guidance figure, rating, price target, attribution tag and source citation, plus the most important verbatim quotes. Keep tables (they are dense), merging or trimming only where they repeat the prose. Achieve the cut by removing repetition, restated context, filler, hedging and over-long explanations, and by merging points made more than once into one statement that shows how they changed over time. Keep the heading structure, and keep the "Key takeaways" section if there is one, tightened.

{style}

Output only the rewritten section, starting directly with its first ## heading. Do not repeat the section title, and do not add TERMS or DATES blocks.

=== SECTION ===
{body}"""

START_PROMPT = """Write "00 Start Here", the first file of the Core Notes for an Illumina (ILMN) research folder (as of {as_of}). It must contain, under ## headings:

1. "How these notes are organized": a short guide to the folder (given below) and what each Core Notes file covers.
2. "Illumina and its market in one page": a plain-English orientation for someone with no background: what DNA sequencing is, what Illumina sells, who its customers are, how it makes money, who its competitors are, and the key debates right now. Base it on the primer and landscape text below.
3. "Master timeline": merge, de-duplicate and sort the dated events below into one chronological list, grouped by year, keeping every distinct event that matters for understanding Illumina and its competitors. Write each entry as a full, clear sentence.
4. "Glossary": merge the term lists below into one alphabetical glossary with one clear, plain-English definition per term (resolve duplicates into the best definition), grouped under ### Genomics and technology, ### Products and business, ### Finance and valuation.
5. "Source coverage and known gaps": present the coverage table and gaps given below as readable prose plus a table.

{style}

Target length: about {tokens:,} tokens.

=== FOLDER GUIDE ===
{folder}

=== CORE NOTES FILES ===
{files}

=== PRIMER TEXT (section 01) ===
{primer}

=== LANDSCAPE TEXT (section 09) ===
{landscape}

=== DATED EVENTS ===
{dates}

=== TERMS ===
{terms}

=== COVERAGE ===
{coverage}

=== KNOWN GAPS ===
{gaps}"""

KNOWN_GAPS = """- Expert calls: 23 distinct calls (4 others were the same call saved from both Tegus and AlphaSense; the duplicates are archived). The goal was 29.
- Illumina conference transcripts after the TD Cowen conference of 3 Mar 2026 are missing (likely Bernstein in May, Goldman in June, Morgan Stanley in Sep 2026).
- Research reacting to Illumina's Q2 2026 results (30 Jul 2026) is in hand from JPM, Barclays, Freedom Broker, Ameriprise and Bloomberg Intelligence, but not from UBS.
- Earnings call transcripts start at Q1 2023, while the SEC filings start at Q1 2022.
- Roche: only one recent results call (H1 2026); the Q1 2026 sales call is missing. Roche Q3 2026 sales are due around 22-23 Oct 2026.
- Thermo Fisher: Q1 2026 call, consensus estimates and research are missing. Q3 2026 results are due around 22 Oct 2026.
- 10x Genomics: Q2 2026 call, consensus estimates and research are missing.
- MGI Tech: no call transcripts (Shanghai-listed; English transcripts generally do not exist).
- Element Biosciences and Ultima Genomics are private, so they are covered only through expert calls and others' commentary."""


# ----------------------------------------------------------------------------- sections
def by_names(*prefixes):
    return lambda e: e["dest"].startswith(prefixes)


def yr(e):
    return (e.get("date") or "0000")[:4]


SECTIONS = [
    dict(key="01", file="01_ILMN_Company_Primer.md", title="Illumina: What the Company Does and How It Makes Money",
         tokens=9000,
         select=lambda e: e["company"] == "ILMN" and (e["doctype"] == "deck" or e["dest"].startswith(
             ("ILMN_10-K_FY2025", "ILMN_10-Q_2026Q2", "20251113_Illumina-s_Broad", "20251113_Illumina_Shifted"))),
         brief="Explain from scratch what Illumina does: the basics of DNA sequencing, its products (instruments, consumables, services, software, and newer multi-omics such as SomaLogic proteomics), its customers (research versus clinical), its geography (including China), its business model (an installed base of machines driving recurring consumable sales), recent corporate history (GRAIL, leadership, acquisitions), and how it reports segments.",
         organize="start from the basics and build up; finish with the current strategy."),
    dict(key="02", file="02_ILMN_Financial_History_and_Guidance.md", title="Illumina: Financial History and Guidance",
         tokens=13000, select=lambda e: e["company"] == "ILMN" and e["doctype"] in ("filing", "deck"),
         parts=lambda e: "2022-2023" if yr(e) <= "2023" else "2024-2026",
         brief="Quarterly and annual financial history from 2022 through the latest quarter: revenue by type, segment and region; margins; operating expenses; EPS; cash flow; balance sheet; buybacks; and every guidance figure issued and how it changed. Include clean tables of the key series.",
         organize="chronological, with summary tables of the key series followed by explanation of the drivers."),
    dict(key="03", file="03_ILMN_Consensus_Estimates.md", title="Illumina: What Wall Street Expects (Consensus Estimates)",
         tokens=7000, select=lambda e: e["company"] == "ILMN" and e["doctype"] == "consensus",
         brief="What consensus (the average of sell-side analysts' forecasts) expects for Illumina: every available line item by quarter and year, implied growth and margins, and how the latest actual results compare.",
         organize="explain what consensus is first; then annual, then quarterly, with tables plus commentary."),
    dict(key="04", file="04_ILMN_Earnings_Calls_2023-2024.md", title="Illumina Earnings Calls, 2023-2024",
         tokens=14000, select=lambda e: e["company"] == "ILMN" and e["doctype"] == "earnings_call" and yr(e) <= "2024",
         parts=lambda e: yr(e),
         brief="A quarter-by-quarter narrative of each earnings call: results against expectations, guidance, strategic messages, segment and regional commentary, and every distinct analyst Q&A point. Show how management's story evolved.",
         organize="one ## heading per quarter in chronological order."),
    dict(key="05", file="05_ILMN_Earnings_Calls_2025-2026.md", title="Illumina Earnings Calls, 2025-2026",
         tokens=16000, select=lambda e: e["company"] == "ILMN" and e["doctype"] == "earnings_call" and yr(e) >= "2025",
         parts=lambda e: yr(e),
         brief="A quarter-by-quarter narrative of each earnings call: results against expectations, guidance, strategic messages, segment and regional commentary, and every distinct analyst Q&A point. Show how management's story evolved, especially on clinical demand, China, pricing, competition and multi-omics.",
         organize="one ## heading per quarter in chronological order."),
    dict(key="06", file="06_ILMN_Conferences_and_Investor_Events.md", title="Illumina at Investor Conferences and Special Events",
         tokens=11000, select=lambda e: e["company"] == "ILMN" and e["doctype"] == "conference",
         parts=lambda e: "2023-2024" if yr(e) <= "2024" else "2025-2026",
         brief="Management's appearances at investor conferences and special events (including the 2024 strategy update and AGBT session): what they said beyond the earnings calls, new information, and changes in tone.",
         organize="chronological, one ## heading per event."),
    dict(key="07", file="07_ILMN_Expert_Calls.md", title="Expert Calls on Illumina and the Sequencing Market",
         tokens=20000, select=lambda e: e["doctype"] == "expert_call", parts="halves", overview=1800,
         brief="All expert-network calls (former employees, customers, competitors' employees and AI-run channel checks). For each call: who the expert is and their vantage point, then every distinct insight. Close each part with the themes that recur across its calls.",
         organize="one ## heading per call (expert role and date in the heading), then a closing ## Cross-call themes."),
    dict(key="08", file="08_ILMN_Equity_Research.md", title="Sell-Side and Independent Research on Illumina",
         tokens=16000, select=lambda e: e["company"] == "ILMN" and e["doctype"] == "research",
         parts=lambda e: "through April 2026" if (e.get("date") or "") < "2026-05" else "May 2026 onward",
         overview=1800,
         brief="All sell-side and independent research on Illumina: each firm's rating, price target, estimates and thesis and how they changed over time; the bull and bear debates; channel checks; and reactions to each event (for example the Roche sequencing launch).",
         organize="chronological by event, with a running scoreboard of firms' ratings and targets."),
    dict(key="10", file="10_Peer_Oxford_Nanopore.md", title="Peer: Oxford Nanopore Technologies (ONT, London)",
         tokens=10000, select=lambda e: e["company"] == "ONT" and e["tier"] == "core",
         parts=lambda e: "calls and management events" if e["doctype"] == "transcript" else "equity research",
         brief="Everything about Oxford Nanopore: what it sells, how its long-read nanopore technology competes with and complements Illumina, results and guidance from recent calls, management commentary at conferences, leadership changes, analyst ratings, targets and views.",
         organize="business overview, then chronological results and commentary, then analyst views."),
    dict(key="11", file="11_Peer_PacBio.md", title="Peer: Pacific Biosciences (PACB)",
         tokens=7000, select=lambda e: (e["company"] == "PACB" and e["tier"] == "core") or e["company"] == "SECTOR",
         brief="Everything about PacBio: products (HiFi long-read, short-read Onso), how it competes with Illumina, results and guidance from recent calls, conference commentary, leadership change, analyst ratings and views. Also cover the Barclays life-science-tools sector note.",
         organize="business overview, then chronological results and commentary, then analyst views."),
    dict(key="12", file="12_Peer_Roche.md", title="Peer: Roche (sequencing and diagnostics)",
         tokens=8000, select=lambda e: e["company"] == "ROCHE" and e["tier"] == "core",
         brief="Roche as a sequencing competitor: its sequencing-by-expansion (SBX) technology and AXELIOS platform, launch timing, pricing, target customers, the diagnostics division's results and outlook, what management and analysts say. Cover pharma only where it matters for diagnostics or the group's priorities.",
         organize="sequencing strategy first, then diagnostics results, then analyst views."),
    dict(key="13", file="13_Peer_Thermo_Fisher.md", title="Peer: Thermo Fisher Scientific (TMO)",
         tokens=4000, select=lambda e: e["company"] == "TMO" and e["tier"] == "core",
         brief="Thermo Fisher where it touches Illumina: Ion Torrent sequencing, Olink proteomics (competing with Illumina's SomaLogic), clinical NGS, life-science-tools demand trends, results and outlook from recent calls and conferences.",
         organize="relevance to Illumina first, then results and outlook."),
    dict(key="14", file="14_Peer_10x_Genomics.md", title="Peer: 10x Genomics (TXG)",
         tokens=4000, select=lambda e: e["company"] == "TXG" and e["tier"] == "core",
         brief="10x Genomics: single-cell and spatial biology, how it relates to and competes with Illumina (single-cell sample prep, spatial), academic funding trends, results and outlook from recent calls and conferences.",
         organize="relevance to Illumina first, then results and outlook."),
    dict(key="15", file="15_Peer_MGI_Tech.md", title="Peer: MGI Tech (688114, Shanghai)",
         tokens=4000, select=lambda e: e["company"] == "MGI" and e["tier"] == "core",
         brief="MGI Tech: its sequencers, its position in China and abroad, its competition with Illumina (including China trade restrictions), results, and analyst views. Note that no call transcripts exist.",
         organize="business overview, then results, then analyst views."),
    dict(key="09", file="09_Competitive_Landscape.md", title="The Competitive Landscape in Sequencing",
         tokens=9000, derived=["07", "08", "10", "11", "12", "13", "14", "15"],
         brief="Synthesize across all sources: who competes with Illumina in each arena (high-throughput short-read, benchtop, long-read, clinical diagnostics, China, proteomics, single-cell and spatial), including private players such as Element Biosciences and Ultima Genomics; pricing and share shifts; technology comparisons; what experts, analysts and managements say; and where they disagree.",
         organize="one ## heading per arena, then ## Where sources disagree."),
]
SECTION_BY_KEY = {s["key"]: s for s in SECTIONS}
START_TOKENS = 12000

FOLDER_GUIDE = """- CLAUDE.md: the operating rules Claude Code follows in every chat opened on this folder.
- Core Notes/: this master briefing (read first in every chat).
- Working Notes/INDEX.md: one entry per source document, with a short summary and links.
- Working Notes/Extracts/: an exhaustive, readable note for every source document.
- Working Notes/Sources/: the original documents, renamed and filed by company and type.
- Working Notes/Outputs/: everything produced later (datasets, artifacts, primers, analyses).
- Working Notes/_Archive/: duplicates and off-topic files kept out of the analysis.
- Inbox/: drop new files here, then run `python _Build/build.py ingest`.
- _Build/: the build script, its state and its log."""


# ------------------------------------------------------------------------------ stages
def plan_files(names_dir):
    """Classify every .md file directly inside names_dir. Returns (entries, unclassified)."""
    entries, unknown = [], []
    for p in sorted(Path(names_dir).glob("*.md")):
        if p.name == "CLAUDE.md":
            continue
        text = read(p)
        c = classify(p.name, text)
        if c is None:
            unknown.append(p.name)
            continue
        c["src"] = p.name
        c["dest"] = c.pop("newname") or p.name
        if re.match(r"(20\d{6})_", c["dest"]):
            d = c["dest"][:8]
            c["date"] = f"{d[:4]}-{d[4:6]}-{d[6:8]}"
        else:
            m = re.search(r"(20\d\d)Q(\d)", c["dest"]) or re.search(r"(20\d\d)-(\d\d)-(\d\d)", c["dest"])
            if m and "Q" in m.group(0):
                c["date"] = f"{m.group(1)}-{int(m.group(2)) * 3:02d}-28"
            elif m:
                c["date"] = m.group(0)
            else:
                fy = re.search(r"FY(20\d\d)", c["dest"])
                c["date"] = f"{fy.group(1)}-12-31" if fy else (date_from_text(text) or "")
        entries.append(c)
    return entries, unknown


def cmd_plan(args):
    entries, unknown = plan_files(ROOT)
    from collections import Counter
    cnt = Counter((e["tier"], e["company"], e["doctype"]) for e in entries)
    print(f"{len(entries)} files classified, {len(unknown)} unclassified\n")
    for (tier, co, dtp), n in sorted(cnt.items()):
        print(f"  {tier:8} {co:7} {dtp:15} {n:3}")
    if unknown:
        print("\nUNCLASSIFIED:\n  " + "\n  ".join(unknown))
    if args.verbose:
        for e in entries:
            print(f"{e['tier']:8} {e['company']:6} {e['doctype']:14} {e['date']:10} {e['dest']}")


def dest_path(e):
    if e["tier"] == "archive":
        return ARCHIVE / e["dest"]
    return SOURCES / e["company"] / e["doctype"] / e["dest"]


def extract_path(e):
    return EXTRACTS / e["company"] / e["doctype"] / e["dest"]


def unpack_zips(folder):
    """Unpack .md files from any zip in `folder` (skipping names already present), then archive the zip."""
    import zipfile
    for z in list(Path(folder).glob("*.zip")):
        ARCHIVE.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(z) as zf:
            for member in zf.namelist():
                target = Path(folder) / Path(member).name
                if member.lower().endswith(".md") and not target.exists():
                    target.write_bytes(zf.read(member))
        shutil.move(str(z), str(ARCHIVE / z.name))
        log(f"Unpacked and archived {z.name}")


def organize(state, from_dir=ROOT, entries=None):
    unpack_zips(from_dir)
    if entries is None:
        entries, unknown = plan_files(from_dir)
        if unknown:
            log(f"Leaving {len(unknown)} unclassified file(s) in place: {unknown}")
    for d in (CORE, SOURCES, EXTRACTS, ARCHIVE, OUTPUTS, INBOX, PARTS):
        d.mkdir(parents=True, exist_ok=True)
    for sub in ("datasets", "artifacts", "primers", "analyses"):
        (OUTPUTS / sub).mkdir(exist_ok=True)
    if OLD_ARCHIVE.exists():
        for p in OLD_ARCHIVE.iterdir():
            shutil.move(str(p), str(ARCHIVE / p.name))
        try:
            OLD_ARCHIVE.rmdir()
        except OSError:   # OneDrive can briefly lock a just-emptied folder; harmless to leave it
            pass
    # Exact-content duplicates of anything already filed are archived too. (Only filed sources count:
    # comparing against the archive would wrongly discard the kept copy of an archived duplicate.)
    known = {}
    for p in SOURCES.rglob("*.md"):
        known.setdefault(hashlib.md5(p.read_bytes()).hexdigest(), p.name)
    moved = 0
    for e in entries:
        src = Path(from_dir) / e["src"]
        if src.exists() and e["tier"] != "archive":
            h = hashlib.md5(src.read_bytes()).hexdigest()
            if h in known:
                log(f"Duplicate of {known[h]}: archiving {src.name}")
                e.update(tier="archive", company="OTHER", doctype="duplicate")
            else:
                known[h] = src.name
        dst = dest_path(e)
        dst.parent.mkdir(parents=True, exist_ok=True)
        if dst.exists() and src.exists():
            stem, n = dst.stem, 2
            while dst.exists():
                dst = dst.with_name(f"{stem}_{n}{dst.suffix}")
                n += 1
            e["dest"] = dst.name
        if src.exists():
            shutil.move(str(src), str(dst))
            moved += 1
        if e["tier"] != "archive":
            fid = f"{e['company']}/{e['doctype']}/{e['dest']}"
            prev = state["files"].get(fid, {})
            e["status"] = prev.get("status", "pending")
            e["attempts"] = prev.get("attempts", 0)
            state["files"][fid] = e
    save_state(state)
    log(f"Organized {moved} file(s) into Working Notes.")
    return entries


def split_text(text, limit):
    if len(text) <= limit:
        return [text]
    chunks, cur = [], []
    size = 0
    for para in text.split("\n\n"):
        if size + len(para) > limit and cur:
            chunks.append("\n\n".join(cur))
            cur, size = [], 0
        cur.append(para)
        size += len(para) + 2
    if cur:
        chunks.append("\n\n".join(cur))
    return chunks


def extract_one(fid, e):
    src = SOURCES / e["company"] / e["doctype"] / e["dest"]
    text = read(src)
    model = e["model"]
    chunks = split_text(text, MAX_INPUT_CHARS[model])
    outs = []
    for i, ch in enumerate(chunks, 1):
        part_note = f" (this is part {i} of {len(chunks)} of the document)" if len(chunks) > 1 else ""
        prompt = EXTRACT_PROMPT.format(doctype=e["doctype"], company=e["company"], name=e["dest"],
                                       part_note=part_note, hint=TYPE_HINTS.get(e["doctype"], DEFAULT_HINT),
                                       style=STYLE, content=ch)
        out = call_claude(prompt, model)
        if not out or "<<<INDEX" not in out:
            return False
        outs.append(out)
    body = outs[0] + "".join(f"\n\n---\n## (Continued: part {i} of the document)\n\n" +
                             re.sub(r"<<<INDEX.*?INDEX>>>", "", o, flags=re.S).strip()
                             for i, o in enumerate(outs[1:], 2))
    m = re.search(r"<<<INDEX(.*?)INDEX>>>", body, re.S)
    meta = {}
    for line in m.group(1).strip().splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip().lower()] = v.strip()
    notes = body[m.end():].strip()
    header = (f"# {meta.get('title', e['dest'])}\n\n"
              f"*Source file: `Working Notes/Sources/{e['company']}/{e['doctype']}/{e['dest']}` · "
              f"Date: {meta.get('date', e.get('date', ''))} · {meta.get('source', '')} · {meta.get('type', '')}*\n\n"
              f"**Summary.** {meta.get('summary', '')}\n\n")
    write_atomic(extract_path(e), header + notes + "\n")
    e["meta"] = meta
    if re.match(r"\d{4}-\d{2}-\d{2}$", meta.get("date", "")) and not e.get("date"):
        e["date"] = meta["date"]
    e["extract_hash"] = hashlib.md5((header + notes).encode()).hexdigest()
    return True


def run_extractions(state):
    todo = [(fid, e) for fid, e in state["files"].items()
            if e["status"] != "done" and e["attempts"] < MAX_ATTEMPTS]
    _progress.update(stage="extracting source documents", done=0, total=len(todo), failed=0)
    log(f"Extraction: {len(todo)} document(s) to process, {MAX_WORKERS} at a time.")
    order = {"sonnet": 0, "haiku": 1}
    todo.sort(key=lambda t: (order.get(t[1]["model"], 2), t[0]))
    with ThreadPoolExecutor(MAX_WORKERS) as ex:
        futs = {ex.submit(extract_one, fid, e): (fid, e) for fid, e in todo}
        for f in as_completed(futs):
            fid, e = futs[f]
            try:
                ok = f.result()
            except NotLoggedIn:
                raise
            except Exception as exc:
                log(f"  error on {fid}: {exc!r}")
                ok = False
            e["attempts"] += 1
            e["status"] = "done" if ok else "failed"
            _progress["done"] += 1
            _progress["failed"] += 0 if ok else 1
            log(f"  [{_progress['done']}/{len(todo)}] {'ok    ' if ok else 'FAILED'} {fid}")
            save_state(state)


def build_index(state):
    lines = ["# Working Notes Index", "",
             "One entry per source document. Each entry gives the date, title, a short summary, the "
             "readable extract (exhaustive notes) and the original file. Agents should use this index "
             "to pick the documents relevant to a question, read the extracts, and open the originals "
             "when exact wording, tables or figures matter.", "",
             f"*As of {AS_OF}. Documents: {sum(1 for e in state['files'].values() if e['status'] == 'done')} "
             f"extracted.*", ""]
    names = {"ILMN": "Illumina (ILMN)", "ONT": "Oxford Nanopore (ONT)", "PACB": "Pacific Biosciences (PACB)",
             "ROCHE": "Roche (ROG)", "TMO": "Thermo Fisher (TMO)", "TXG": "10x Genomics (TXG)",
             "MGI": "MGI Tech (688114)", "SECTOR": "Sector-wide research"}
    groups = {}
    for fid, e in state["files"].items():
        groups.setdefault(e["company"], {}).setdefault(e["doctype"], []).append(e)
    for co in sorted(groups, key=lambda c: (c != "ILMN", c)):
        lines += [f"## {names.get(co, co)}", ""]
        for dtp in sorted(groups[co]):
            lines += [f"### {dtp.replace('_', ' ').title()} ({len(groups[co][dtp])})", ""]
            for e in sorted(groups[co][dtp], key=lambda x: x.get("date") or ""):
                m = e.get("meta", {})
                tier = "core" if e["tier"] == "core" else "working only"
                lines.append(f"- **{e.get('date') or m.get('date', '')} — {m.get('title', e['dest'])}** "
                             f"({m.get('source', '')}; feeds {tier})  ")
                if m.get("summary"):
                    lines.append(f"  {m['summary']}  ")
                ex = extract_path(e).relative_to(WORK).as_posix()
                sr = dest_path(e).relative_to(WORK).as_posix()
                status = "" if e["status"] == "done" else " **(extract not yet built — read the original)**"
                lines.append(f"  Extract: `{ex}` · Original: `{sr}`{status}")
            lines.append("")
    outs = sorted(p for p in OUTPUTS.rglob("*") if p.is_file())
    lines += ["## Outputs", ""]
    lines += [f"- `{p.relative_to(WORK).as_posix()}`" for p in outs] or ["- (none yet)"]
    write_atomic(WORK / "INDEX.md", "\n".join(lines) + "\n")
    log("INDEX.md rebuilt.")


def strip_blocks(text):
    terms = re.search(r"<<<TERMS(.*?)TERMS>>>", text, re.S)
    dates = re.search(r"<<<DATES(.*?)DATES>>>", text, re.S)
    body = re.sub(r"<<<(TERMS|DATES).*?(TERMS|DATES)>>>", "", text, flags=re.S).strip()
    return body, (terms.group(1).strip() if terms else ""), (dates.group(1).strip() if dates else "")


def section_inputs(state, s):
    return sorted([e for e in state["files"].values() if e["status"] == "done" and s["select"](e)],
                  key=lambda e: (e.get("date") or "", e["dest"]))


def group_parts(s, ents):
    if s.get("parts") == "halves":
        h = (len(ents) + 1) // 2
        groups = [("first half of the calls", ents[:h]), ("second half of the calls", ents[h:])]
    elif callable(s.get("parts")):
        g = {}
        for e in ents:
            g.setdefault(s["parts"](e), []).append(e)
        groups = list(g.items())
    else:
        groups = [("", ents)]
    out = []   # split further if a group's text is too large for one call
    for label, grp in groups:
        cur, size, n = [], 0, 1
        for e in grp:
            sz = len(read(extract_path(e)))
            if cur and size + sz > MAX_INPUT_CHARS["opus"]:
                out.append((f"{label} (batch {n})".strip(), cur))
                cur, size, n = [], 0, n + 1
            cur.append(e)
            size += sz
        if cur:
            out.append((f"{label} (batch {n})".strip() if n > 1 else label, cur))
    return [g for g in out if g[1]]


def build_section(state, s):
    key = s["key"]
    if s.get("derived"):
        texts = [read(CORE / SECTION_BY_KEY[k]["file"]) for k in s["derived"] if (CORE / SECTION_BY_KEY[k]["file"]).exists()]
        groups = [("", None)]
        inputs_by_group = ["\n\n=====\n\n".join(texts)]
        n_src = len(texts)
        sig = hashlib.md5("".join(texts).encode()).hexdigest()
    else:
        ents = section_inputs(state, s)
        if not ents:
            log(f"Section {key}: no inputs yet; skipped.")
            return True
        groups = group_parts(s, ents)
        inputs_by_group = ["\n\n=====\n\n".join(read(extract_path(e)) for e in g) for _, g in groups]
        n_src = len(ents)
        sig = hashlib.md5("|".join(f"{e['dest']}:{e.get('extract_hash', '')}" for e in ents).encode()).hexdigest()
    rec = state["sections"].get(key, {})
    if rec.get("sig") == sig and rec.get("status") == "done" and (CORE / s["file"]).exists():
        return True
    if rec.get("sig") != sig:
        rec = {"sig": sig, "parts": {}}
    nparts = len(groups)
    per = max(1500, (s["tokens"] - s.get("overview", 0)) // nparts)
    jobs = []
    for i, ((label, g), inp) in enumerate(zip(groups, inputs_by_group), 1):
        if rec["parts"].get(str(i)) == "done" and (PARTS / f"{key}_{i}.md").exists():
            continue
        plabel = f" You are writing part {i} of {nparts}, covering: {label}." if nparts > 1 else ""
        prompt = SECTION_PROMPT.format(title=s["title"], part_label=plabel, brief=s["brief"],
                                       n=len(g) if g else n_src, organize=s["organize"], style=STYLE,
                                       tokens=per, words=int(per * 0.75), inputs=inp)
        jobs.append((i, prompt))
    for i, prompt in jobs:
        out = call_claude(prompt, "opus")
        if not out:
            log(f"Section {key} part {i}: failed.")
            state["sections"][key] = rec
            save_state(state)
            return False
        write_atomic(PARTS / f"{key}_{i}.md", out)
        rec["parts"][str(i)] = "done"
        state["sections"][key] = rec
        save_state(state)
    bodies, terms, dates = [], [], []
    for i in range(1, nparts + 1):
        b, t, d = strip_blocks(read(PARTS / f"{key}_{i}.md"))
        bodies.append(b)
        terms.append(t)
        dates.append(d)
    overview = ""
    if s.get("overview"):
        ov = PARTS / f"{key}_overview.md"
        if rec.get("overview") != "done" or not ov.exists():
            out = call_claude(OVERVIEW_PROMPT.format(title=s["title"], tokens=s["overview"], style=STYLE,
                                                     inputs="\n\n=====\n\n".join(bodies)), "opus")
            if not out:
                return False
            write_atomic(ov, out)
            rec["overview"] = "done"
        overview = "## Key takeaways\n\n" + re.sub(r"^#+ *Key takeaways\s*", "", read(ov).strip(), flags=re.I) + "\n\n"
    head = (f"# {s['title']}\n\n*Core Notes section {key}. Synthesized from {n_src} "
            f"{'Core Notes sections' if s.get('derived') else 'source extracts'} as of {AS_OF}. "
            f"Bracketed tags cite the source; full detail is in Working Notes (see INDEX.md).*\n\n")
    write_atomic(CORE / s["file"], head + overview + "\n\n".join(bodies) + "\n")
    write_atomic(PARTS / f"{key}_terms.txt", "\n".join(terms))
    write_atomic(PARTS / f"{key}_dates.txt", "\n".join(dates))
    rec["status"] = "done"
    state["sections"][key] = rec
    save_state(state)
    log(f"Section {key} written: {s['file']}")
    return True


def coverage_table(state):
    from collections import Counter
    c = Counter((e["company"], e["doctype"]) for e in state["files"].values() if e["status"] == "done")
    rows = ["| Company | Document type | Count |", "|---|---|---|"]
    rows += [f"| {co} | {dtp.replace('_', ' ')} | {n} |" for (co, dtp), n in sorted(c.items())]
    return "\n".join(rows)


def build_start(state):
    files = [s["file"] for s in sorted(SECTIONS, key=lambda s: s["key"]) if (CORE / s["file"]).exists()]
    # Keep hand-added Core Notes files (e.g. 16_Addendum_*.md written by chat jobs) listed in Start Here.
    known = {s["file"] for s in SECTIONS} | {"00_Start_Here.md"}
    files += sorted(p.name for p in CORE.glob("*.md") if p.name not in known)
    terms ="\n".join(read(p) for p in sorted(PARTS.glob("*_terms.txt")))
    dates = "\n".join(read(p) for p in sorted(PARTS.glob("*_dates.txt")))
    sig = hashlib.md5((terms + dates + "".join(files) + coverage_table(state)).encode()).hexdigest()
    rec = state["sections"].get("00", {})
    if rec.get("sig") == sig and (CORE / "00_Start_Here.md").exists():
        return True
    prompt = START_PROMPT.format(as_of=AS_OF, style=STYLE, tokens=START_TOKENS, folder=FOLDER_GUIDE,
                                 files="\n".join(f"- {f}" for f in files),
                                 primer=read(CORE / "01_ILMN_Company_Primer.md") if (CORE / "01_ILMN_Company_Primer.md").exists() else "",
                                 landscape=read(CORE / "09_Competitive_Landscape.md") if (CORE / "09_Competitive_Landscape.md").exists() else "",
                                 dates=dates, terms=terms, coverage=coverage_table(state), gaps=KNOWN_GAPS)
    out = call_claude(prompt, "opus")
    if not out:
        return False
    write_atomic(CORE / "00_Start_Here.md", f"# Start Here: Illumina Research Core Notes\n\n*As of {AS_OF}.*\n\n" +
                 strip_blocks(out)[0] + "\n")
    state["sections"]["00"] = {"sig": sig, "status": "done"}
    save_state(state)
    log("Section 00 written: 00_Start_Here.md")
    return True


def condense_section(state, s):
    """If a written section overshot its budget by more than 15%, have Opus tighten it to the target."""
    key = s["key"]
    rec = state["sections"].get(key, {})
    path = CORE / s["file"]
    if rec.get("status") != "done" or not path.exists() or rec.get("condensed") == rec.get("sig"):
        return True
    text = read(path)
    cut = text.find("\n## ")
    head, body = (text[:cut + 1], text[cut + 1:]) if cut > 0 else ("", text)
    cur, target = len(body.split()), int(s["tokens"] * 0.75)
    if cur > target * 1.15:
        out = call_claude(CONDENSE_PROMPT.format(cur=cur, target=target, cap=int(target * 1.1), style=STYLE,
                                                 body=body), "opus")
        new = len(out.split()) if out else 0
        if new < target * 0.6:   # empty or truncated: keep the longer original rather than lose content
            log(f"Section {key}: condense failed or came back too short ({new} words); kept original.")
            return False
        write_atomic(path, head + strip_blocks(out)[0] + "\n")
        log(f"Section {key} condensed: {cur:,} -> {new:,} words (target {target:,}).")
    rec["condensed"] = rec.get("sig")
    state["sections"][key] = rec
    save_state(state)
    return True


def run_sections(state, force=()):
    for k in force:
        state["sections"].pop(k, None)
    base = [s for s in SECTIONS if not s.get("derived")]
    derived = [s for s in SECTIONS if s.get("derived")]
    start = {"key": "00", "file": "00_Start_Here.md", "tokens": START_TOKENS}
    _progress.update(stage="writing and condensing Core Notes sections", done=0,
                     total=2 * len(SECTIONS) + 2, failed=0)

    def tally(ok):
        _progress["done"] += 1
        _progress["failed"] += 0 if ok else 1

    with ThreadPoolExecutor(MAX_WORKERS) as ex:
        for f in as_completed([ex.submit(build_section, state, s) for s in base]):
            tally(f.result())
        for f in as_completed([ex.submit(condense_section, state, s) for s in base]):
            tally(f.result())
    for s in derived:
        tally(build_section(state, s))
        tally(condense_section(state, s))
    tally(build_start(state))
    tally(condense_section(state, start))


# ------------------------------------------------------------------------------ commands
def acquire_lock():
    if STATUS.exists():
        try:
            s = json.loads(read(STATUS))
            if s.get("pid") != os.getpid() and time.time() - s.get("heartbeat", 0) < 300 \
                    and s.get("stage") not in ("complete", "stopped", "needs login"):
                log(f"Another build (pid {s.get('pid')}) is running; exiting.")
                sys.exit(0)
        except Exception:
            pass


def guarded(fn):
    def wrapper(args):
        acquire_lock()
        if os.name == "nt":   # keep the PC from idle-sleeping while this process runs (released on exit)
            import ctypes
            ctypes.windll.kernel32.SetThreadExecutionState(0x80000000 | 0x00000001)  # CONTINUOUS | SYSTEM_REQUIRED
        stop = threading.Event()
        threading.Thread(target=heartbeat_loop, args=(stop,), daemon=True).start()
        try:
            fn(args)
        except NotLoggedIn as exc:
            _progress.update(stage="needs login", note=str(exc))
            log("The Claude CLI is not logged in. Run `claude setup-token` (or `claude` then /login), then restart.")
        except BaseException:
            import traceback
            _progress.update(stage="crashed", note=traceback.format_exc()[-500:])
            log("CRASH:\n" + traceback.format_exc())
            raise
        finally:
            stop.set()
            write_status()
    return wrapper


@guarded
def cmd_run(args):
    state = load_state()
    organize(state)
    for _ in range(2):   # second pass retries failures
        run_extractions(state)
    build_index(state)
    run_sections(state)
    build_index(state)
    failed = [fid for fid, e in state["files"].items() if e["status"] != "done"]
    bad_sections = [k for k, r in state["sections"].items() if r.get("status") != "done"]
    _progress.update(stage="complete" if not failed and not bad_sections else "complete with failures",
                     note=f"failed extracts: {failed}; failed sections: {bad_sections}")
    log(f"BUILD FINISHED. Failed extracts: {len(failed)}. Failed sections: {bad_sections or 'none'}.")


@guarded
def cmd_ingest(args):
    state = load_state()
    INBOX.mkdir(exist_ok=True)
    unpack_zips(INBOX)
    entries, unknown = plan_files(INBOX)
    for name in unknown:
        c = classify_with_haiku(name, read(INBOX / name))
        if c:
            c.update(src=name, dest=c.pop("newname") or name, date=date_from_text(read(INBOX / name)))
            entries.append(c)
        else:
            log(f"Could not classify {name}; left in Inbox.")
    if not entries:
        log("Inbox is empty; nothing to ingest.")
        return
    organize(state, from_dir=INBOX, entries=entries)
    run_extractions(state)
    build_index(state)
    run_sections(state)      # only sections whose inputs changed are rebuilt
    build_index(state)
    _progress.update(stage="complete", note=f"ingested {len(entries)} file(s)")
    log(f"INGEST FINISHED: {len(entries)} file(s).")


@guarded
def cmd_resynth(args):
    state = load_state()
    run_sections(state, force=args.keys)


def cmd_selftest(args):
    exe = find_claude()
    print(f"CLI: {exe}")
    try:
        out = call_claude("Reply with exactly the word OK.", "haiku", timeout=180, min_len=1)
    except NotLoggedIn as exc:
        print(f"NOT LOGGED IN: {exc}")
        sys.exit(1)
    print(f"Response: {out!r}")
    sys.exit(0 if out and "OK" in out else 1)


def cmd_status(args):
    if not STATUS.exists():
        print("No build has run yet.")
        return
    s = json.loads(read(STATUS))
    age = time.time() - s.get("heartbeat", 0)
    alive = age < 300 and s.get("stage") not in ("complete", "complete with failures", "needs login")
    print(f"Stage: {s.get('stage')} | progress {s.get('done')}/{s.get('total')} | failed {s.get('failed')}")
    print(f"Last heartbeat: {s.get('heartbeat_human')} ({int(age // 60)} min ago) -> "
          f"{'RUNNING' if alive else 'NOT RUNNING'}")
    if s.get("paused_until"):
        print(f"Paused for usage limit until {s['paused_until']}")
    if s.get("note"):
        print(f"Note: {s['note']}")
    if STATE.exists():
        st = json.loads(read(STATE))
        from collections import Counter
        print("Extracts:", dict(Counter(e["status"] for e in st["files"].values())))
        print("Sections done:", sorted(k for k, r in st["sections"].items() if r.get("status") == "done"))


def cmd_start(args):
    exe = Path(sys.executable)
    pyw = exe.with_name("pythonw.exe") if os.name == "nt" else exe
    if not pyw.exists():
        pyw = exe
    argv = [str(pyw), str(Path(__file__).resolve()), args.what] + list(args.rest)
    if os.name == "nt":
        base = 0x00000008 | 0x00000200 | 0x08000000   # DETACHED | NEW_PROCESS_GROUP | NO_WINDOW
        try:
            p = subprocess.Popen(argv, cwd=ROOT, creationflags=base | 0x01000000, close_fds=True)  # + BREAKAWAY_FROM_JOB
        except OSError:
            p = subprocess.Popen(argv, cwd=ROOT, creationflags=base, close_fds=True)
    else:
        p = subprocess.Popen(argv, cwd=ROOT, start_new_session=True, close_fds=True)
    print(f"Launched `{args.what}` detached (pid {p.pid}). Follow with: python _Build/build.py status")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("plan"); p.add_argument("-v", "--verbose", action="store_true"); p.set_defaults(fn=cmd_plan)
    sub.add_parser("run").set_defaults(fn=cmd_run)
    sub.add_parser("ingest").set_defaults(fn=cmd_ingest)
    sub.add_parser("status").set_defaults(fn=cmd_status)
    sub.add_parser("selftest").set_defaults(fn=cmd_selftest)
    p = sub.add_parser("resynth"); p.add_argument("keys", nargs="+"); p.set_defaults(fn=cmd_resynth)
    p = sub.add_parser("start"); p.add_argument("what", nargs="?", default="run", choices=["run", "ingest", "resynth"])
    p.add_argument("rest", nargs="*"); p.set_defaults(fn=cmd_start)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
