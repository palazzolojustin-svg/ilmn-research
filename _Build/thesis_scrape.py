"""Overnight adaptive alt-data scrape for the ILMN pricing / research thesis (started 2026-10-12).

An adaptive queue runner. Headless Claude agents (up to 5 at once, each with a hard timeout) SCOUT for
web data sources, PROBE them cheaply, MINE the productive ones and VERIFY the evidence. An Opus STRATEGIST
re-plans the queue every 5 completed tasks or 30 minutes, dropping dry sources and pivoting to new ones.
All strategy lives in data files (sources.json, queue.json), never in this code.

Usage is capped at +20 points of the weekly all-models plan over the baseline taken at launch; wind-down
(no new research, last verify, write-up) starts at +17. The hourly self-check feeds the real weekly % in
(`usage PCT`), which calibrates the % per $ rate the job uses between checks.

Apify is not visible to headless calls, so agents queue Apify requests and the hourly check (which runs
inside the desktop app) executes them and hands the datasets back (`apify_pending` / `apify_done`).

  python _Build/thesis_scrape.py start --baseline PCT   launch detached
  python _Build/thesis_scrape.py run                    run in the foreground
  python _Build/thesis_scrape.py status                 progress, budget, sources, findings
  python _Build/thesis_scrape.py check                  hourly check: relaunch if stalled, then status
  python _Build/thesis_scrape.py usage PCT              feed the current weekly % (calibrates the budget)
  python _Build/thesis_scrape.py apify_pending          list Apify requests waiting for the hourly check
  python _Build/thesis_scrape.py apify_done ID PATH     hand back a saved Apify dataset (JSON file)
  python _Build/thesis_scrape.py apify_failed ID WHY    mark an Apify request as failed
  python _Build/thesis_scrape.py published URL          record the published artifact URL
  python _Build/thesis_scrape.py stop                   stop new research; verify and write up
"""
import argparse
import csv
import datetime as dt
import json
import os
import re
import subprocess
import sys
import threading
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build import find_claude  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "_Build"
CORE = ROOT / "Core Notes"
WORK = ROOT / "Working Notes"
OUTPUTS = WORK / "Outputs"
JOB = BUILD / "thesis_scrape"
SANDBOX = JOB / "sandbox"
RESULTS = JOB / "results"
APIFY_DIR = JOB / "apify"
PARTS = JOB / "addendum_parts"
STATE = JOB / "state.json"
SOURCES = JOB / "sources.json"
QUEUE = JOB / "queue.json"
FINDINGS = JOB / "findings.json"
BUDGET_F = JOB / "budget.json"
APIFY_Q = JOB / "apify_requests.json"
KNOWN = JOB / "known_evidence.md"
STRAT_LOG = JOB / "strategy_log.md"
LOG = JOB / "thesis_scrape.log"
PRIOR_LEDGER = OUTPUTS / "analyses" / "2026-10-11_clinical_consumables_scrape" / "00_evidence_ledger.md"

DATE = "2026-10-12"
MD_OUT = OUTPUTS / "analyses" / f"{DATE}_thesis_scrape_addendum.md"
HTML_OUT = OUTPUTS / "artifacts" / f"{DATE}_thesis_scrape_addendum.html"
DS = OUTPUTS / "datasets"

CONCURRENCY = 5
BUDGET_PTS, WINDDOWN_PTS = 20.0, 17.0
PROVISIONAL_RATE = 1.0 / 3.0            # weekly % per API-equivalent $ until calibrated (1% per $3)
STRAT_EVERY_N, STRAT_EVERY_S = 5, 30 * 60
VERIFY_BATCH = 12
MAX_APIFY_PENDING = 4
TIMEOUT = {"SEED": 18, "SCOUT": 20, "PROBE": 10, "MINE": 25, "VERIFY": 20, "APIFY_MINE": 15,
           "STRATEGIST": 15, "MERGE": 8, "KNOWN": 45, "WRITE": 240}
MAXBUD = {"haiku": 1.5, "sonnet": 8, "opus": 20}
TIMEOUT_COST_GUESS = {"haiku": 0.2, "sonnet": 1.5, "opus": 5.0}

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
    """Windows/OneDrive can briefly lock a file during a replace or sync: retry instead of crashing."""
    for i in range(tries):
        try:
            return fn()
        except (PermissionError, OSError, json.JSONDecodeError):
            if i == tries - 1:
                raise
            time.sleep(0.25 + 0.25 * i)


def jload(path, default):
    with _lock:
        if not path.exists():
            return default
        return _retry(lambda: json.loads(path.read_text(encoding="utf-8")))


def jsave(path, obj):
    with _lock:
        def w():
            tmp = path.with_suffix(".tmp")
            tmp.write_text(json.dumps(obj, indent=1, ensure_ascii=False), encoding="utf-8")
            tmp.replace(path)
        _retry(w)


def load_state():
    return jload(STATE, {"stage": "new", "cost_usd": 0.0, "tasks_done": 0, "running": {}, "history": [],
                         "cycles": [], "next_task": 1, "next_src": 1, "next_item": 1, "next_apify": 1,
                         "stop": False, "since_strat": 0, "last_strat": 0})


def update_state(fn):
    with _lock:
        st = load_state()
        fn(st)
        st["heartbeat"] = time.time()
        st["heartbeat_human"] = now()
        jsave(STATE, st)
        return st


def keep_awake(on=True):
    if os.name != "nt":
        return
    import ctypes
    ctypes.windll.kernel32.SetThreadExecutionState(0x80000000 | (0x00000001 if on else 0))


# ------------------------------------------------------------------------------ budget

def load_budget():
    return jload(BUDGET_F, {})


def est_pct():
    b, st = load_budget(), load_state()
    if not b:
        return None
    return b["latest_pct"] + (st["cost_usd"] - b.get("cost_at_latest", 0.0)) * b["pct_per_usd"]


def budget_mode():
    """ok | pause (provisional estimate over wind-down: wait for calibration) | winddown | hardcap."""
    b = load_budget()
    if not b:
        return "ok"
    e = est_pct()
    if e >= b["hard_cap"]:
        return "hardcap"
    if e >= b["winddown"]:
        if not b.get("calibrated"):
            first = b.get("pause_started") or time.time()
            if not b.get("pause_started"):
                b["pause_started"] = first
                jsave(BUDGET_F, b)
            return "pause" if time.time() - first < 80 * 60 else "winddown"
        return "winddown"
    if b.get("pause_started"):
        b.pop("pause_started")
        jsave(BUDGET_F, b)
    return "ok"


# ------------------------------------------------------------------------------ headless calls

LIMIT_RX = re.compile(r"usage limit|limit reached|hit your limit|limit will reset|resets? (at|in)|"
                      r"rate.?limit|too many requests|\b429\b", re.I)
OVERLOAD_RX = re.compile(r"overloaded|\b529\b|api error|connection error|ECONNRESET", re.I)


def call_claude(prompt, model, tools, timeout_min, budget=None, add_dirs=()):
    """One headless call from the empty sandbox. Returns (text, cost_usd). Waits out usage limits."""
    global _pause_until
    exe = find_claude()
    SANDBOX.mkdir(parents=True, exist_ok=True)
    env = {k: v for k, v in os.environ.items() if not re.match(r"(CLAUDE|ANTHROPIC)", k)}
    env.update(CLAUDE_CODE_MAX_OUTPUT_TOKENS="64000", DISABLE_AUTOUPDATER="1")
    args = [exe, "-p", "--model", model, "--output-format", "json", "--strict-mcp-config",
            "--no-session-persistence", "--max-budget-usd", str(budget or MAXBUD[model])]
    if tools:
        args += ["--tools", ",".join(tools), "--allowedTools", " ".join(tools)]
    else:
        args += ["--tools", ""]
    for d in (JOB,) + tuple(add_dirs):
        args += ["--add-dir", str(d)]
    flags = 0x08000000 if os.name == "nt" else 0
    timeout = timeout_min * 60
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
            log(f"  timeout after {timeout_min} min ({model}); charging an estimated ${TIMEOUT_COST_GUESS[model]}")
            return None, TIMEOUT_COST_GUESS[model]
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
        if not is_err and text and len(text.strip()) > 20:
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
        if text and len(text.strip()) > 200:
            return text.strip(), cost
        log(f"  call failed rc={p.returncode} ({model}): {blob.strip()[:300]!r}")
        return None, cost


def extract_json(text, opener="{"):
    if not text:
        return None
    m = re.search(r"```(?:json)?\s*(.*?)```", text, re.S)
    cands = [m.group(1)] if m else []
    cands.append(text)
    closer = "]" if opener == "[" else "}"
    for c in cands:
        i, j = c.find(opener), c.rfind(closer)
        if i >= 0 and j > i:
            try:
                return json.loads(c[i:j + 1])
            except Exception:
                continue
    return None


def charge(cost):
    return update_state(lambda s: s.update(cost_usd=round(s["cost_usd"] + cost, 4)))


# ------------------------------------------------------------------------------ prompts

THESIS = """THESIS (an equity analyst's short thesis on Illumina, ILMN; today is 2026-10-12). Every finding must map to one label:
1A. Mix shift on the 6000 is not done. The street and the buy-side assume "no substantial pricing headwinds post 2026." We believe that can't be squared with 17% of consumables volume but 41% of consumables revenue still sitting on the NovaSeq 6000. The customers still on the 6000 are less volume-elastic than those who already converted. We expect about 5 more points of mix shift in 2027. We doubt management's claim that the remaining 6000 volume stays there permanently.
1B. Discounting will speed up. The street holds discounting flat. We think it will accelerate because of the 35B flow cell and heavy new short-read competition (Ultima, Element) with much lower $/genome. Future consumables prices offered to large accounts will carry bigger extra discounts, because those customers have huge negotiating leverage.
1C. Volume will slow. The near-term volume levers are used up. MRD and WGS aren't big enough to stop volume growth slowing from about 30% to about 25%, and at minimum we don't see the speed-up needed to reach the street's 2027E consumables revenue growth. Sequencing cost is no longer the constraint; volumes face growing limits elsewhere. NIPT maturing will drag on volume. The technology is too far out, and NTRA and the other big public labs aren't seeing MRD or WGS become a meaningful share of their mix. So: volume growth slows slightly and pricing keeps falling.
2A. Research customers are very price-sensitive. They demand "insane discounts," are less volume-elastic, and will fight on price because funding is tight.
2B. The street models research consumables flat year over year. We think volume stays the same but pricing gets worse, because of Roche's Axelios (SBX) and large labs pushing for bigger discounts. Research is about 35% of revenue, so this drives misses.
"""

GOAL = """GOAL: find NEW evidence that supports the thesis. Priority 1 (what the analyst cares about most): creative ALTERNATIVE DATA and FORENSIC evidence scraped from the open web (procurement records, price lists, archived web pages, filings exhibits, forums, job postings, claims/utilization data, public datasets, conference materials, resale markets, etc.). Priority 2: earnings calls and filings of competitors and customers (Natera and the other big labs first). Evidence ALREADY KNOWN (listed below) is worthless unless you materially update or quantify it; never resurface it. Strong evidence that CUTS AGAINST the thesis should also be reported (direction "against"), so the analyst can see the watch-outs.
RULES: no logins, no paywalls, no account creation, never enter credentials. Sources from Jan 2025 onward unless older data establishes a trend. Never invent numbers, sources or URLs: every item needs a real URL you actually opened (or a search-result snippet you saw, marked as such). Quotes must be 15 words or fewer.
"""

ITEM_SCHEMA = """Each evidence item is a JSON object:
{"label": "1A|1B|1C|2A|2B", "direction": "supports|against", "claim": "one sentence", "detail": "the evidence with numbers, period and context (2-4 sentences)", "url": "...", "date": "publication or data date", "source_name": "publisher / dataset", "source_type": "procurement|price_list|archive|filing|forum|jobs|claims_data|dataset|conference|press|earnings_call|other", "quote": "<=15 words or empty", "strength": "strong|medium|weak", "why_new": "one line: why this is not already known"}"""


def known_block():
    k = KNOWN.read_text(encoding="utf-8") if KNOWN.exists() else "(not built)"
    return f"=== EVIDENCE ALREADY KNOWN (exclusion list) ===\n{k}\n=== END KNOWN ===\n"


def found_block(limit=400):
    f = jload(FINDINGS, {"items": []})["items"]
    lines = [f"{i['id']} [{i['label']}] {i['claim'][:160]}" for i in f if i.get("status") != "rejected"][-limit:]
    return "=== FOUND SO FAR IN THIS SCRAPE (also not new) ===\n" + ("\n".join(lines) or "(none yet)") + "\n=== END ===\n"


def sources_brief(limit=300):
    srcs = jload(SOURCES, {"sources": []})["sources"]
    return "\n".join(f"{s['id']} [{s['status']}; items {s.get('new_items', 0)}; attempts {s.get('attempts', 0)}] "
                     f"{s['name']}: {s.get('access', '')[:80]}" for s in srcs[-limit:]) or "(empty)"


APIFY_NOTE = ("APIFY: you cannot call Apify directly, but if a source clearly needs a heavy scraper (e.g. job boards, "
              "LinkedIn public posts, Reddit history, eBay sold listings, Google results at scale), you may request up "
              "to 2 Apify actor runs in \"apify_requests\": [{\"actor\": \"actor id if known, else a description\", "
              "\"input\": {...}, \"why\": \"...\", \"max_items\": 200}]. Results arrive within 1-2 hours and are mined "
              "by a later agent. Only request runs with a clear payoff.")

HEADER = "You are a research agent in an overnight, adaptive web scrape. Return ONLY the JSON requested (no prose outside it).\n\n"


def p_seed(t):
    return (HEADER + THESIS + "\n" + GOAL + "\n" + known_block() +
            f"\nYOUR TASK (SEED PROBE {t['id']}): {t['title']}\n{t['instructions']}\n\n"
            "Quickly test each named data source (and obvious close variants) with WebSearch/WebFetch: does it exist, is "
            "it reachable without a login, does it contain data relevant to the thesis labels, and is that data new versus "
            "the known list? Spend at most ~20 tool calls in total and about 15 minutes. Do not mine exhaustively; capture "
            "up to 3 sample items per productive source.\n" + APIFY_NOTE + "\n\n" + ITEM_SCHEMA +
            "\n\nReturn JSON: {\"sources\": [{\"name\": \"...\", \"url\": \"...\", \"access\": \"how to get the data\", "
            "\"labels\": [\"1B\"], \"status\": \"productive|dry|blocked\", \"notes\": \"what is there / why dry\", "
            "\"how_to_mine\": \"specific instructions for a deeper extraction\", \"difficulty\": \"hard (needs "
            "interpretation: contracts, tenders, implied pricing, archived price histories) | easy (plain extraction)\", "
            "\"items\": [ ... ]}], "
            "\"new_candidates\": [{\"name\": \"...\", \"url\": \"...\", \"access\": \"...\", \"labels\": [...], "
            "\"rationale\": \"...\"}], \"apify_requests\": []}")


def p_scout(t):
    return (HEADER + THESIS + "\n" + GOAL + "\n" + known_block() +
            f"\nSOURCES ALREADY IN THE REGISTRY (do not repeat; dry/blocked ones failed):\n{sources_brief()}\n\n"
            f"YOUR TASK (SCOUT {t['id']}): {t['title']}\n{t['instructions']}\n\n"
            "Think creatively and laterally like a forensic short-seller analyst: where on the open web could hard evidence "
            "for this thesis label exist that the street has not looked at? Consider procurement and tender databases "
            "worldwide, price lists and their archived versions (Wayback Machine), SEC exhibits and full-text search, "
            "government datasets (CMS, CDC, NIH RePORTER, USAspending), court dockets, patents, conference abstracts and "
            "posters, job boards, resale/auction markets, forums and social media, university core-facility pages, "
            "distributor catalogs, app/website changes, customer press releases, non-US regulators and stock-exchange "
            "filings. You may run up to ~12 quick searches to confirm candidates are real and reachable. Propose 5-10 "
            "candidate sources, ranked by expected payoff, each concrete enough that another agent can test it.\n"
            + APIFY_NOTE +
            "\n\nReturn JSON: {\"candidates\": [{\"name\": \"...\", \"url\": \"...\", \"access\": \"exact method: queries, "
            "URLs, filters\", \"labels\": [...], \"rationale\": \"why it could hold evidence and what it would show\", "
            "\"expected_payoff\": \"high|medium|low\"}], \"apify_requests\": []}")


def p_probe(t, src):
    return (HEADER + THESIS + "\n" + GOAL + "\n" + known_block() +
            f"\nYOUR TASK (PROBE {t['id']}): test ONE candidate source cheaply.\nSource {src['id']}: {src['name']}\n"
            f"URL: {src.get('url', '')}\nAccess: {src.get('access', '')}\nWhy: {src.get('rationale', '')}\n"
            f"Extra instructions: {t.get('instructions', '')}\n\n"
            "Use at most ~10 tool calls and about 8 minutes. Decide: productive (relevant, reachable, new data), dry "
            "(nothing relevant or nothing new) or blocked (login/paywall/bot-blocked). Capture up to 2 sample items.\n"
            + APIFY_NOTE + "\n\n" + ITEM_SCHEMA +
            "\n\nReturn JSON: {\"status\": \"productive|dry|blocked\", \"notes\": \"...\", \"how_to_mine\": \"specific "
            "instructions for a deep extraction\", \"difficulty\": \"hard|easy\", \"items\": [...], "
            "\"new_candidates\": [...], \"apify_requests\": []}")


def p_mine(t, src):
    return (HEADER + THESIS + "\n" + GOAL + "\n" + known_block() + found_block() +
            f"\nYOUR TASK (MINE {t['id']}): extract the evidence from this productive source thoroughly.\n"
            f"Source {src['id']}: {src['name']}\nURL: {src.get('url', '')}\nAccess: {src.get('access', '')}\n"
            f"Probe notes: {src.get('notes', '')}\nHow to mine: {src.get('how_to_mine', '')}\n"
            f"Strategist instructions: {t.get('instructions', '')}\n\n"
            "Use up to ~40 tool calls and about 22 minutes. Go for numbers, time series, named entities and dated changes; "
            "derive figures where the data allows (show the arithmetic in 'detail'). Return at most 15 items, strongest "
            "first. Also list leads to adjacent sources you noticed.\n" + APIFY_NOTE + "\n\n" + ITEM_SCHEMA +
            "\n\nReturn JSON: {\"items\": [...], \"source_status\": \"productive|exhausted|dry|blocked\", \"notes\": "
            "\"what remains to mine, if anything\", \"leads\": [{\"name\": \"...\", \"url\": \"...\", \"access\": \"...\", "
            "\"labels\": [...], \"rationale\": \"...\"}], \"apify_requests\": []}")


def p_apify_mine(t, req):
    return (HEADER + THESIS + "\n" + GOAL + "\n" + known_block() + found_block() +
            f"\nYOUR TASK (APIFY_MINE {t['id']}): an Apify scraper run was executed for this purpose: {req.get('why', '')}\n"
            f"Actor: {req.get('actor')}  Input: {json.dumps(req.get('input'))[:600]}\n"
            f"The dataset is saved at: {req.get('result_path')}\nRead it (Read tool; it may be large, read in chunks) "
            "and extract evidence. Aggregate where useful (counts, shares, price distributions, trends) and show the "
            "arithmetic. You may use WebFetch to open a few item URLs for confirmation. Return at most 15 items.\n\n"
            + ITEM_SCHEMA + "\n\nReturn JSON: {\"items\": [...], \"notes\": \"...\", \"leads\": [...]}")


def p_verify(t, items):
    return (HEADER + THESIS + "\n" + known_block() +
            f"\nYOUR TASK (VERIFY {t['id']}): you are a skeptical reviewer. For each item below decide:\n"
            "- Is it truly new versus the known list (and not a restatement of a known fact from a new outlet)?\n"
            "- Does it actually support (or, if marked 'against', actually cut against) the label it was assigned?\n"
            "- Are the numbers read correctly and in context (period, units, list vs net price, research vs clinical)?\n"
            "You may open URLs (WebFetch) to check the most important numbers; spend at most ~20 tool calls. Then look "
            "across ALL items (including previously verified ones below) for combinations that yield a derived figure "
            "(e.g. an implied discount rate, a $/Gb trend, a share or growth rate) and add those as derived items with "
            "the working shown.\n\nITEMS TO VERIFY:\n" + json.dumps(items, ensure_ascii=False, indent=0) +
            "\n\nPREVIOUSLY VERIFIED (context for derived figures):\n" + verified_brief() +
            "\n\nReturn JSON: {\"verdicts\": [{\"id\": \"F012\", \"verdict\": \"accept|reject\", \"strength\": "
            "\"strong|medium|weak\", \"label\": \"1A|1B|1C|2A|2B\", \"direction\": \"supports|against\", \"note\": "
            "\"correction or reason\"}], \"derived\": [" + ITEM_SCHEMA.split("\n", 1)[1] +
            " plus \"based_on\": [\"F003\", \"F017\"]]}")


def verified_brief():
    f = jload(FINDINGS, {"items": []})["items"]
    v = [x for x in f if x.get("status") == "verified"]
    return "\n".join(f"{x['id']} [{x['label']}/{x.get('direction', 'supports')}] {x['claim'][:150]} | "
                     f"{x.get('detail', '')[:220]}" for x in v[-120:]) or "(none yet)"


def p_merge(new_items):
    return ("You are a deduplication clerk. Compare each NEW item with the KNOWN list and the FOUND list. Mark an item "
            "'known' if the known list already holds the same fact or number (a new outlet repeating it is still "
            "known), 'dup' if an item in the found list already holds it (give that id), else 'new'. Be strict but do "
            "not reject items that add a materially new number, date, entity or source type.\n\n" + known_block() +
            found_block(600) + "\nNEW ITEMS:\n" +
            "\n".join(f"N{i}: [{x.get('label')}] {x.get('claim', '')} | {x.get('detail', '')[:300]} | {x.get('url', '')}"
                      for i, x in enumerate(new_items)) +
            "\n\nReturn ONLY JSON: {\"results\": [{\"n\": 0, \"status\": \"new|known|dup\", \"of\": \"F012 or empty\"}]}")


def p_strategist(st):
    srcs = jload(SOURCES, {"sources": []})["sources"]
    q = jload(QUEUE, {"tasks": []})["tasks"]
    f = jload(FINDINGS, {"items": []})["items"]
    live = [x for x in f if x.get("status") != "rejected"]
    by_label = {lab: sum(1 for x in live if x.get("label") == lab and x.get("strength") in ("strong", "medium")
                         and x.get("direction", "supports") == "supports") for lab in ["1A", "1B", "1C", "2A", "2B"]}
    hist = "\n".join(f"{h['id']} {h['type']} ({h['model']}) {h['title'][:90]} -> {h.get('outcome', '')[:140]}"
                     for h in st.get("history", [])[-25:])
    latest = "\n".join(f"{x['id']} [{x['label']}/{x.get('strength')}/{x.get('status')}] {x['claim'][:150]}"
                       for x in live[-30:])
    b = load_budget()
    apq = jload(APIFY_Q, {"requests": []})["requests"]
    ap = "\n".join(f"{r['id']} [{r['status']}] {r.get('actor')}: {r.get('why', '')[:100]}" for r in apq[-20:])
    running = "\n".join(f"{k}: {v.get('type')} {v.get('title', '')[:80]}" for k, v in st.get("running", {}).items())
    return (THESIS + "\n" + GOAL +
            "\nYou are the STRATEGIST of an adaptive overnight scrape (5 agents run at once). Your job: keep the search "
            "pivoting toward the highest-yield NEW evidence. Re-plan the pending queue now.\n\n"
            f"BUDGET: estimated weekly usage {est_pct() or 0:.1f}% (baseline {b.get('baseline')}, wind-down at "
            f"{b.get('winddown')}, hard cap {b.get('hard_cap')}; calibrated={b.get('calibrated')}). Job spend so far "
            f"${st['cost_usd']:.2f}. As budget runs down, put the highest expected-yield tasks first.\n\n"
            f"STRONG+MEDIUM SUPPORTING ITEMS BY LABEL: {json.dumps(by_label)}  (total items incl. weak: {len(live)})\n\n"
            f"SOURCE REGISTRY (id [status; new items; attempts] name: access):\n{sources_brief(400)}\n\n"
            f"RECENT TASK OUTCOMES:\n{hist or '(none)'}\n\nRUNNING NOW:\n{running or '(none)'}\n\n"
            f"LATEST ITEMS:\n{latest or '(none)'}\n\nAPIFY REQUESTS (run hourly by the app):\n{ap or '(none)'}\n\n"
            f"CURRENT PENDING QUEUE ({len(q)} tasks):\n" +
            "\n".join(f"{t['id']} {t['type']} {t.get('model')} {t.get('source_id', '')} {t['title'][:90]}" for t in q[:80]) +
            "\n\nRULES:\n- Task types: SCOUT (opus; brainstorm new sources for a label/angle), PROBE (sonnet; test one "
            "candidate source by source_id), MINE (opus if 'hard' interpretation is needed: contracts, tenders, implied "
            "pricing, Wayback price histories, reading between the lines; else sonnet; needs a productive source_id).\n"
            "- A source with 2 attempts and no new medium/strong items is dry: never queue it again. Never re-try dry or "
            "blocked sources. Go deeper on productive sources (more years, geographies, entities) with new MINE tasks.\n"
            "- Send SCOUTs to the thinnest labels and to angles nobody has tried. Keep at least 8 tasks queued so 5 can "
            "run at all times. Priority 1 is creative alternative data; priority 2 is competitor/customer calls and filings.\n"
            "- You may mark sources dry/blocked/productive and add new candidate sources.\n"
            "- 'queue' holds only NEW tasks to add, in priority order; they are interleaved 1:1 with the pending tasks "
            "listed above. Remove pending tasks you judge low-value by listing their ids in 'drop' (SEED tasks, the "
            "analyst's 20 starting probes, cannot be dropped). PROBEs of fresh candidates and MINEs of newly productive "
            "sources are queued automatically as results arrive; do not duplicate them.\n"
            "- exhausted=true ONLY if you judge that no untried source has a plausible chance of producing new "
            "medium/strong evidence.\n\n"
            "Return ONLY JSON: {\"source_updates\": [{\"id\": \"S004\", \"status\": \"dry|blocked|productive\", "
            "\"notes\": \"...\"}], \"new_sources\": [{\"name\": \"...\", \"url\": \"...\", \"access\": \"...\", "
            "\"labels\": [...], \"rationale\": \"...\"}], \"queue\": [{\"type\": \"SCOUT|PROBE|MINE\", \"model\": "
            "\"opus|sonnet\", \"source_id\": \"S004 or a new_sources name for PROBE\", \"label\": \"1B\", \"title\": "
            "\"short\", \"instructions\": \"specific\"}], \"drop\": [\"T031\"], \"exhausted\": false, \"note\": \"one "
            "paragraph: what you changed and why\"}")


KNOWN_PROMPT = f"""You are building an EXCLUSION LIST for an overnight web scrape on Illumina (ILMN). Agents will use it to avoid resurfacing evidence the analyst already holds.

{THESIS}
Read, in full (Read tool, in chunks where long):
1. Every file in "{CORE}" (the master briefing, including the addenda numbered 16 and 17).
2. The prior scrape's evidence ledger: "{PRIOR_LEDGER}".
3. The top-level analyses in "{OUTPUTS / 'analyses'}" whose names start with 2026-10-11_ (skim; ignore subfolders except the ledger above).

Then write a compact bullet list of every fact, number and source already held that bears on labels 1A-2B, grouped under headings: ## 1A, ## 1B, ## 1C, ## 2A, ## 2B, ## Sources already used (named datasets, price lists, websites, tenders, filings, surveys, forums and other alt-data sources the corpus already drew on). One line per item with the key number and date, e.g. "- NovaSeq X carried ~83% of HT Gb but ~59% of HT revenue (Q2 2026 call)". Merge duplicates. Aim for 250-500 lines in total; be dense, no prose. Output ONLY the Markdown list."""


WRITE_PROMPT = """You are writing the final deliverable of an overnight alternative-data scrape for an equity analyst: "Thesis Scrape Addendum: New Evidence for the ILMN Pricing and Research Thesis" (as of {date}). Only evidence that is NEW to the analyst's corpus is included: it has been deduplicated against their notes and verified by a skeptical reviewer.

{thesis}
INPUT: read "{inp}" in full. It holds the verified items (id, label, direction, strength, claim, detail, url, date, source), derived figures, the sources tried and found dry or blocked, productive sources and leads still unexplored, and run statistics.

WRITE a readable, well-written list summary, following the analyst's standing rules:
- Full, well-written, simple sentences and short paragraphs. Lead with the answer, then explain. Assume a smart reader with little background: explain each piece of jargon in a few plain words the first time it appears (e.g. flow cell, $/Gb, MRD, NIPT, WGS, recharge rate, tender, RUO).
- Contextualize every number: what it measures, the period, what it compares to and why it matters for the thesis. Distinguish facts, management claims and opinions; say who said what and when with light citations like (USAspending, Mar 2026). Point out where sources disagree and where data may be stale or weak.
- Tables are fine for comparisons but every table is introduced by a sentence saying what it shows and what to take from it.
- Each evidence item is one to three sentences, ends with a markdown link to its source and its tag in square brackets, e.g. [F012] (derived items: [D003]). Every verified item and every derived item must appear (merge near-duplicates into one item citing all tags).

STRUCTURE:
# Thesis Scrape Addendum: New Evidence for the ILMN Pricing and Research Thesis
*As of {date}. One line on how it was built.*
## The most powerful new evidence  (5-8 short paragraphs or bullets: the findings that most strengthen the thesis, including derived figures)
## 1A. The NovaSeq 6000 mix shift is not done  (numbered evidence list, strongest first)
## 1B. Discounting will speed up
## 1C. Volume growth will slow
## 2A. Research customers fight hardest on price
## 2B. Research pricing gets worse from flat volume
## Derived figures  (the arithmetic, plainly explained)
## Watch-outs: evidence that cuts against the thesis
## Where the evidence is thin, and what to look at next
## How this scrape was built  (agents, sources tried, sources found dry or blocked, so they are not repeated; limits)

Write it to disk in parts with the Write tool: {parts}\\part_01.md, part_02.md, ... Each part holds one or more whole sections and at most ~4,000 words. Part 01 starts with the title. Then reply with exactly: DONE <number of parts>."""


# ------------------------------------------------------------------------------ registry / queue / findings

def add_source(cand, origin, status="candidate"):
    """Add a candidate source unless one with the same name or URL exists. Returns its id."""
    with _lock:
        reg = jload(SOURCES, {"sources": []})
        name = str(cand.get("name", "")).strip()[:160]
        url = str(cand.get("url", "")).strip()
        key = re.sub(r"[^a-z0-9]", "", name.lower())
        for s in reg["sources"]:
            if (key and re.sub(r"[^a-z0-9]", "", s["name"].lower()) == key) or (url and url == s.get("url")):
                return s["id"]
        st = load_state()
        sid = f"S{st['next_src']:03d}"
        update_state(lambda s: s.update(next_src=s["next_src"] + 1))
        reg["sources"].append(dict(id=sid, name=name or sid, url=url, access=str(cand.get("access", ""))[:600],
                                   labels=cand.get("labels", []), rationale=str(cand.get("rationale", ""))[:500],
                                   payoff=cand.get("expected_payoff", ""), status=status, attempts=0, new_items=0,
                                   notes="", how_to_mine="", origin=origin, added=now()))
        jsave(SOURCES, reg)
        return sid


def update_source(sid, **kw):
    with _lock:
        reg = jload(SOURCES, {"sources": []})
        for s in reg["sources"]:
            if s["id"] == sid:
                for k, v in kw.items():
                    if k in ("attempts", "new_items"):
                        s[k] = s.get(k, 0) + v
                    elif v not in (None, ""):
                        s[k] = v
                # automatic dry rule: 2 attempts with nothing new
                if s.get("attempts", 0) >= 2 and s.get("new_items", 0) == 0 and s["status"] in ("candidate", "productive"):
                    s["status"] = "dry"
                    s["notes"] = (s.get("notes", "") + " | auto-dry: 2 attempts, no new medium/strong items").strip(" |")
        jsave(SOURCES, reg)


def get_source(sid):
    for s in jload(SOURCES, {"sources": []})["sources"]:
        if s["id"] == sid:
            return s
    return None


def new_task(**kw):
    st = update_state(lambda s: s.update(next_task=s["next_task"] + 1))
    kw["id"] = f"T{st['next_task'] - 1:03d}"
    kw.setdefault("model", "sonnet")
    kw.setdefault("instructions", "")
    kw.setdefault("title", kw["type"])
    return kw


def enqueue(tasks, front=False):
    with _lock:
        q = jload(QUEUE, {"tasks": []})
        q["tasks"] = (tasks + q["tasks"]) if front else (q["tasks"] + tasks)
        jsave(QUEUE, q)


def pop_task(allowed):
    with _lock:
        q = jload(QUEUE, {"tasks": []})
        for i, t in enumerate(q["tasks"]):
            if t["type"] in allowed:
                q["tasks"].pop(i)
                jsave(QUEUE, q)
                return t
        return None


def link_check(url):
    if not url or not url.startswith("http"):
        return "none"
    try:
        req = urllib.request.Request(url, method="GET", headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            return "ok" if r.status < 400 else f"http{r.status}"
    except urllib.error.HTTPError as e:
        return "dead" if e.code in (404, 410) else f"http{e.code}"
    except Exception:
        return "unreachable"


def merge_items(items, task, source_id):
    """Dedupe new items with Haiku, link-check them, append to findings. Returns # new medium/strong supporting-or-against."""
    items = [x for x in (items or []) if isinstance(x, dict) and x.get("claim")]
    if not items:
        return 0
    res = None
    text, cost = call_claude(p_merge(items), "haiku", [], TIMEOUT["MERGE"])
    charge(cost)
    res = extract_json(text or "", "{")
    marks = {r.get("n"): r for r in (res or {}).get("results", []) if isinstance(r, dict)}
    kept = 0
    for i, x in enumerate(items):
        m = marks.get(i, {"status": "new"})
        if m.get("status") in ("known", "dup"):
            continue
        x["link"] = link_check(x.get("url", ""))
        if x["link"] == "dead":
            continue
        with _lock:
            st = update_state(lambda s: s.update(next_item=s["next_item"] + 1))
            x.update(id=f"F{st['next_item'] - 1:03d}", task=task["id"], source_id=source_id or "",
                     status="unverified", found=now(), dedupe="haiku" if res else "unchecked")
            x.setdefault("direction", "supports")
            f = jload(FINDINGS, {"items": []})
            f["items"].append(x)
            jsave(FINDINGS, f)
        if x.get("strength") in ("strong", "medium"):
            kept += 1
    return kept


def queue_apify(reqs, task):
    reqs = [r for r in (reqs or []) if isinstance(r, dict) and r.get("actor")][:2]
    if not reqs:
        return
    with _lock:
        q = jload(APIFY_Q, {"requests": []})
        pending = sum(1 for r in q["requests"] if r["status"] == "pending")
        for r in reqs:
            if pending >= MAX_APIFY_PENDING:
                break
            st = update_state(lambda s: s.update(next_apify=s["next_apify"] + 1))
            q["requests"].append(dict(id=f"A{st['next_apify'] - 1:02d}", actor=str(r.get("actor"))[:200],
                                      input=r.get("input", {}), why=str(r.get("why", ""))[:400],
                                      max_items=min(int(r.get("max_items", 200) or 200), 500), task=task["id"],
                                      source_id=task.get("source_id", ""), status="pending", requested=now()))
            pending += 1
        jsave(APIFY_Q, q)


# ------------------------------------------------------------------------------ task execution

def run_task(t):
    typ, model = t["type"], t.get("model", "sonnet")
    tools = ["WebSearch", "WebFetch", "Read"]
    src = get_source(t.get("source_id", "")) if t.get("source_id") else None
    if typ == "SEED":
        prompt = p_seed(t)
    elif typ == "SCOUT":
        prompt = p_scout(t)
    elif typ == "PROBE":
        if not src:
            return "skipped: unknown source"
        if src["status"] in ("dry", "blocked"):
            return f"skipped: source {src['id']} is {src['status']}"
        prompt = p_probe(t, src)
    elif typ == "MINE":
        if not src:
            return "skipped: unknown source"
        if src["status"] in ("dry", "blocked"):
            return f"skipped: source {src['id']} is {src['status']}"
        prompt = p_mine(t, src)
    elif typ == "APIFY_MINE":
        req = next((r for r in jload(APIFY_Q, {"requests": []})["requests"] if r["id"] == t.get("apify_id")), None)
        if not req:
            return "skipped: unknown apify request"
        prompt = p_apify_mine(t, req)
    elif typ == "VERIFY":
        f = jload(FINDINGS, {"items": []})["items"]
        ids = set(t.get("item_ids", []))
        items = [{k: x.get(k) for k in ("id", "label", "direction", "claim", "detail", "url", "date", "source_name",
                                         "quote", "strength")} for x in f if x["id"] in ids]
        if not items:
            return "skipped: nothing to verify"
        prompt = p_verify(t, items)
        tools = ["WebFetch", "WebSearch", "Read"]
    else:
        return f"skipped: unknown type {typ}"
    text, cost = call_claude(prompt, model, tools, TIMEOUT.get(typ, 20))
    charge(cost)
    if text:
        (RESULTS / f"{t['id']}_{typ}.json").write_text(text, encoding="utf-8")
    res = extract_json(text or "", "{")
    if not isinstance(res, dict):
        if src:
            update_source(src["id"], attempts=1)
        return f"failed (no JSON; ${cost:.2f})"

    if typ == "SEED":
        n_new, summary = 0, []
        for s in res.get("sources", []):
            if not isinstance(s, dict):
                continue
            stt = s.get("status") if s.get("status") in ("productive", "dry", "blocked") else "candidate"
            sid = add_source(s, t["id"], status=stt)
            k = merge_items(s.get("items"), t, sid)
            n_new += k
            update_source(sid, attempts=1, new_items=k, notes=str(s.get("notes", ""))[:500],
                          how_to_mine=str(s.get("how_to_mine", ""))[:800], status=stt)
            summary.append(f"{sid}:{stt}")
            if stt == "productive":
                hard = s.get("difficulty") == "hard"
                enqueue([new_task(type="MINE", model="opus" if hard else "sonnet", source_id=sid,
                                  title=f"mine {str(s.get('name', sid))[:60]}")], front=True)
        for c in res.get("new_candidates", []) or []:
            if isinstance(c, dict):
                add_source(c, t["id"])
        queue_apify(res.get("apify_requests"), t)
        return f"{len(summary)} sources ({', '.join(summary)[:150]}); {n_new} new med/strong items; ${cost:.2f}"
    if typ == "SCOUT":
        ids = [add_source(c, t["id"]) for c in res.get("candidates", []) or [] if isinstance(c, dict)]
        queue_apify(res.get("apify_requests"), t)
        # make the best candidates testable right away
        enqueue([new_task(type="PROBE", model="sonnet", source_id=i, title=f"probe {i}") for i in ids[:4]])
        return f"{len(ids)} candidates ({', '.join(ids)}); ${cost:.2f}"
    if typ == "PROBE":
        stt = res.get("status") if res.get("status") in ("productive", "dry", "blocked") else "dry"
        k = merge_items(res.get("items"), t, src["id"])
        update_source(src["id"], attempts=1, new_items=k, status=stt, notes=str(res.get("notes", ""))[:500],
                      how_to_mine=str(res.get("how_to_mine", ""))[:800], difficulty=res.get("difficulty", ""))
        for c in res.get("new_candidates", []) or []:
            if isinstance(c, dict):
                add_source(c, t["id"])
        queue_apify(res.get("apify_requests"), t)
        if stt == "productive":
            hard = res.get("difficulty") == "hard"
            enqueue([new_task(type="MINE", model="opus" if hard else "sonnet", source_id=src["id"],
                              title=f"mine {src['name'][:60]}")], front=True)
        return f"{src['id']} {stt}; {k} new med/strong items; ${cost:.2f}"
    if typ in ("MINE", "APIFY_MINE"):
        sid = src["id"] if src else t.get("source_id", "")
        k = merge_items(res.get("items"), t, sid)
        if src:
            ss = res.get("source_status", "productive")
            update_source(src["id"], attempts=1, new_items=k, notes=str(res.get("notes", ""))[:500],
                          status=ss if ss in ("dry", "blocked") else ("exhausted" if ss == "exhausted" else None))
        for c in res.get("leads", []) or []:
            if isinstance(c, dict):
                add_source(c, t["id"])
        queue_apify(res.get("apify_requests"), t)
        return f"{k} new med/strong items; ${cost:.2f}"
    if typ == "VERIFY":
        acc = rej = 0
        with _lock:
            f = jload(FINDINGS, {"items": []})
            byid = {x["id"]: x for x in f["items"]}
            for v in res.get("verdicts", []) or []:
                x = byid.get(v.get("id"))
                if not x:
                    continue
                if v.get("verdict") == "accept":
                    acc += 1
                    x["status"] = "verified"
                    for k2 in ("strength", "label", "direction"):
                        if v.get(k2):
                            x[k2] = v[k2]
                else:
                    rej += 1
                    x["status"] = "rejected"
                x["verify_note"] = str(v.get("note", ""))[:500]
            for i, x in enumerate(f["items"]):
                if x["id"] in set(t.get("item_ids", [])) and x["status"] == "unverified":
                    x["status"] = "verified_unreviewed"   # reviewer skipped it; keep but mark
            nd = 0
            for d in res.get("derived", []) or []:
                if isinstance(d, dict) and d.get("claim"):
                    nd += 1
                    n = sum(1 for x in f["items"] if str(x["id"]).startswith("D")) + 1
                    d.update(id=f"D{n:03d}", status="verified", task=t["id"], found=now(), derived=True)
                    d.setdefault("direction", "supports")
                    f["items"].append(d)
            jsave(FINDINGS, f)
        return f"accepted {acc}, rejected {rej}, derived {nd}; ${cost:.2f}"
    return "done"


def worker(t):
    update_state(lambda s: s["running"].__setitem__(t["id"], {**t, "started": now()}))
    log(f"{t['id']} start {t['type']} ({t.get('model')}): {t.get('title', '')[:100]}")
    try:
        outcome = run_task(t)
    except SystemExit:
        raise
    except Exception as e:
        import traceback
        log(f"{t['id']} ERROR: {traceback.format_exc()[-800:]}")
        outcome = f"error: {e!r}"[:200]
    log(f"{t['id']} done: {outcome}")

    def upd(s):
        s["running"].pop(t["id"], None)
        s["history"].append({"id": t["id"], "type": t["type"], "model": t.get("model"), "title": t.get("title", ""),
                             "source_id": t.get("source_id", ""), "outcome": outcome, "t": now()})
        if not outcome.startswith("skipped"):
            s["tasks_done"] += 1
            s["since_strat"] += 1
    update_state(upd)
    return outcome


def run_strategist():
    st = load_state()
    snap = {t["id"] for t in jload(QUEUE, {"tasks": []})["tasks"]}
    log("STRATEGIST start (opus)")
    text, cost = call_claude(p_strategist(st), "opus", ["Read"], TIMEOUT["STRATEGIST"])
    charge(cost)
    res = extract_json(text or "", "{")
    if not isinstance(res, dict):
        log(f"STRATEGIST failed to return JSON (${cost:.2f})")
        update_state(lambda s: s.update(last_strat=time.time(), since_strat=0,
                                        strat_fails=s.get("strat_fails", 0) + 1))
        return False
    for u in res.get("source_updates", []) or []:
        if isinstance(u, dict) and u.get("id"):
            update_source(u["id"], status=u.get("status") if u.get("status") in ("dry", "blocked", "productive") else None,
                          notes=str(u.get("notes", ""))[:400])
    name2id = {}
    for c in res.get("new_sources", []) or []:
        if isinstance(c, dict):
            name2id[str(c.get("name", ""))] = add_source(c, "strategist")
    tasks = []
    for q in res.get("queue", []) or []:
        if not isinstance(q, dict) or q.get("type") not in ("SCOUT", "PROBE", "MINE"):
            continue
        sid = q.get("source_id", "") or ""
        sid = name2id.get(sid, sid)
        if q["type"] in ("PROBE", "MINE"):
            s = get_source(sid)
            if not s or s["status"] in ("dry", "blocked"):
                continue
        model = "opus" if q["type"] == "SCOUT" else ("opus" if q.get("model") == "opus" else "sonnet")
        if q["type"] == "PROBE":
            model = "sonnet"
        tasks.append(new_task(type=q["type"], model=model, source_id=sid, label=q.get("label", ""),
                              title=str(q.get("title", ""))[:120], instructions=str(q.get("instructions", ""))[:1500]))
    drop = {str(d) for d in (res.get("drop") or [])}
    queued = len(tasks)
    with _lock:
        old = jload(QUEUE, {"tasks": []})["tasks"]
        system = [t for t in old if t["type"] in ("VERIFY", "APIFY_MINE")]
        # pending tasks survive unless explicitly dropped (seeds can't be dropped); new tasks interleave 1:1
        rest = [t for t in old if t["type"] not in ("VERIFY", "APIFY_MINE")
                and (t["id"] not in drop or t["type"] == "SEED" or t["id"] not in snap)]
        mixed = []
        while tasks or rest:
            if tasks:
                mixed.append(tasks.pop(0))
            if rest:
                mixed.append(rest.pop(0))
        jsave(QUEUE, {"tasks": system + mixed})
    f = jload(FINDINGS, {"items": []})["items"]
    st = load_state()
    prev_mark = st["cycles"][-1]["item_mark"] if st["cycles"] else 1
    new_ms = sum(1 for x in f if str(x["id"]).startswith("F") and int(x["id"][1:]) >= prev_mark
                 and x.get("strength") in ("strong", "medium") and x.get("status") != "rejected")
    cyc = {"n": len(st["cycles"]) + 1, "t": now(), "new_ms": new_ms, "item_mark": st["next_item"],
           "queued": queued, "exhausted": bool(res.get("exhausted")), "cost": round(cost, 2)}
    update_state(lambda s: (s["cycles"].append(cyc), s.update(last_strat=time.time(), since_strat=0, strat_fails=0)))
    with open(STRAT_LOG, "a", encoding="utf-8") as fh:
        fh.write(f"\n## Cycle {cyc['n']} ({now()}): +{cyc['new_ms']} new medium/strong items since last cycle; "
                 f"{queued} tasks queued; exhausted={cyc['exhausted']}\n\n{str(res.get('note', '')).strip()}\n")
    log(f"STRATEGIST cycle {cyc['n']}: +{cyc['new_ms']} new med/strong; queued {queued}; "
        f"exhausted={cyc['exhausted']} (${cost:.2f})")
    return True


def saturated():
    c = load_state()["cycles"]
    return len(c) >= 3 and c[-1]["new_ms"] == 0 and c[-2]["new_ms"] == 0 and c[-1]["exhausted"]


def maybe_queue_verify(force=False):
    with _lock:
        f = jload(FINDINGS, {"items": []})["items"]
        q = jload(QUEUE, {"tasks": []})["tasks"]
        st = load_state()
        pending_ids = {i for t in q if t["type"] == "VERIFY" for i in t.get("item_ids", [])}
        pending_ids |= {i for t in st["running"].values() if t.get("type") == "VERIFY" for i in t.get("item_ids", [])}
        todo = [x["id"] for x in f if x.get("status") == "unverified" and x.get("strength") in ("strong", "medium")
                and x["id"] not in pending_ids]
        made = 0
        while len(todo) >= VERIFY_BATCH or (force and todo):
            batch, todo = todo[:VERIFY_BATCH], todo[VERIFY_BATCH:]
            enqueue([new_task(type="VERIFY", model="opus", item_ids=batch, title=f"verify {batch[0]}..{batch[-1]}")],
                    front=True)
            made += 1
        return made


def check_apify_returns():
    """Queue an APIFY_MINE for each Apify dataset the hourly check has handed back."""
    with _lock:
        q = jload(APIFY_Q, {"requests": []})
        changed = False
        for r in q["requests"]:
            if r["status"] == "done" and not r.get("mined_task"):
                t = new_task(type="APIFY_MINE", model="sonnet", apify_id=r["id"], source_id=r.get("source_id", ""),
                             title=f"mine Apify dataset {r['id']} ({r['actor'][:40]})")
                enqueue([t], front=True)
                r["mined_task"] = t["id"]
                changed = True
        if changed:
            jsave(APIFY_Q, q)


# ------------------------------------------------------------------------------ seeds

SEEDS = [
    ("Core-lab recharge rates", "University and institute core-facility sequencing rate sheets: NovaSeq 6000 vs NovaSeq X per lane / per flow cell / per Gb, internal vs external rates, changes 2024-2026 (use the Wayback Machine for old versions), which cores still run 6000s or have retired them, and any cores adding Element AVITI, Ultima or MGI."),
    ("Government tenders and awards", "SAM.gov, USAspending.gov (award descriptions mentioning NovaSeq, Illumina, flow cell, Element, Ultima), GSA Advantage contract prices, EU TED tenders, UK Contracts Finder / Find a Tender, AusTender, Canadian Buy and Sell, China government procurement (ccgp.gov.cn). Look for unit prices, discounts, sole-source justifications, 35B flow cell, and wins by Element/MGI/Ultima."),
    ("Used NovaSeq 6000 resale market", "NovaSeq 6000 listings and sold prices on eBay, LabX, BioSurplus, Liquidity Services / GovDeals, university surplus auctions, refurbished-equipment dealers. Trend in asking/sold prices and number of units being retired (evidence on whether the 6000 base is really permanent)."),
    ("Sequencing service provider price lists", "Public price lists of sequencing service providers (Novogene, Azenta/GENEWIZ, Psomagen, Admera, Macrogen, BGI/MGI Tech services, Eurofins, CD Genomics, university-adjacent providers, Ultima-based providers): $/Gb and $/30x genome by platform (NovaSeq 6000, NovaSeq X, AVITI, UG100, DNBSEQ), and how fast they have fallen (Wayback)."),
    ("Ultima and Element pricing and wins", "Ultima Genomics (UG 100 / Solaris) and Element Biosciences (AVITI, AVITI24, AVITI LT) pricing, $/genome claims, placements, named customer wins and switches from Illumina, AGBT 2026 and ASHG 2026 materials, press releases, customer case studies."),
    ("Forums and social media on Illumina pricing", "Reddit (r/bioinformatics, r/labrats, r/genomics), SEQanswers, Biostars, X/Twitter, Bluesky, public LinkedIn posts: Illumina quotes, discount negotiations, 'switching to Element/Ultima', 6000 end-of-service, 35B pricing, budget cuts forcing platform changes."),
    ("Job postings as an adoption proxy", "Public job postings (Indeed, LinkedIn public pages, Greenhouse/Lever/Workday boards, university HR sites) mentioning AVITI, Ultima/UG100, DNBSEQ, AXELIOS/SBX vs NovaSeq: counts and trends; Illumina's own sales, pricing, deal-desk and contract-renewal postings."),
    ("EDGAR supply agreements and pricing terms", "SEC EDGAR full-text search (efts.sec.gov/LATEST/search-index?q=...) for Illumina supply agreements and exhibits at customers (Natera, GeneDx, Guardant, Exact/Abbott, Grail, BillionToOne, Tempus, Caris, Personalis, Twist, 10x): tiered pricing, most-favored pricing, minimum purchase commitments, price-reduction mechanics, 2025-2026 amendments."),
    ("Roche SBX/Axelios, MGI and new entrants", "Roche Axelios/SBX launch pricing, early-access and RUO customer sites, academic targeting and placement counts; MGI/Complete Genomics US expansion and pricing; any other short-read entrants. Evidence they pressure research pricing."),
    ("Clinical lab calls and filings 2026", "Q1-Q3 2026 earnings calls, 10-Qs and investor decks of Natera, GeneDx, Guardant, Exact/Abbott, Myriad, Caris, Tempus, BillionToOne, Labcorp, Quest, Grail: MRD and WGS volumes as a share of mix, NIPT growth, sequencing cost per test, statements that cost is no longer the constraint, what limits volume (reimbursement, ordering, staffing)."),
    ("NIPT maturation data", "CDC/NCHS births data 2025 and 2026 (provisional), NIPT adoption and payer-coverage saturation, average-risk coverage status, Natera Panorama and peer NIPT volume growth trends, China and Europe NIPT saturation."),
    ("MRD adoption limits", "MolDX MRD coverage decisions and LCDs, CMS Clinical Lab Fee Schedule and Part B utilization for MRD PLA codes (e.g. 0340U Signatera and peers), ADLT rates, prior-authorization friction, commercial payer coverage for MRD in 2025-2026."),
    ("Clinical WGS scale", "Newborn sequencing programs (GUARDIAN, BabySeq, Genomics England Generation Study, others), rapid WGS coverage by Medicaid/payers, actual clinical WGS test volumes, hospital adoption barriers."),
    ("Constraints other than sequencing cost", "Surveys and reports on what limits clinical/research sequencing volume: bioinformatics and data storage, staffing (genetic counselors, lab technologists), sample prep/library prep throughput, reimbursement, turnaround; 2025-2026 lab surveys (CAP, AMP, NSGC, ACMG, industry surveys)."),
    ("NIH funding data", "NIH RePORTER awards FY2025 vs FY2026 year-to-date (count and $, especially NHGRI and genomics-related), the 15% indirect-cost cap litigation status, Grant Witness / grant-termination trackers, FY2027 appropriations and President's budget, multi-year funding policy; NSF too."),
    ("Academic buying behavior", "University purchasing bid awards and consortium contracts for sequencing reagents (E&I Cooperative, UC system, Big Ten Academic Alliance, Texas/state contracts), core facility closures, consolidations and platform switches 2025-2026, evidence of steep academic discounts."),
    ("International research funding and buying", "China (Illumina unreliable-entity-list status, export controls, domestic-preference procurement), EU Horizon and national programs, UKRI budgets, academic tenders in Europe/Asia won by Element or MGI vs Illumina."),
    ("Tools-peer read-through Q2-Q3 2026", "Q2 and Q3 2026 earnings calls/decks of Thermo Fisher, Danaher, Agilent, Bio-Techne, Azenta, Qiagen, 10x Genomics, Twist, PacBio, Revvity: academic and government demand, pricing pressure, NIH budget comments, customer discount demands."),
    ("Illumina list-price forensics", "Illumina public list prices (illumina.com product pages, quotes), GSA Advantage schedule prices for Illumina flow cells and kits, distributor catalogs (Fisher, VWR, regional distributors), and their history in the Wayback Machine: price changes, promotions, NovaSeq X vs 6000 kit price per Gb."),
    ("Illumina promotions forensics", "Wayback Machine snapshots of Illumina promotion pages: trade-in/upgrade offers for 6000-to-X, reagent rental, 35B flow cell launch terms, rebates, academic pricing programs; webinar and conference claims; signs of escalating incentives."),
]

SCOUT_SEEDS = [
    ("1A", "Find unconventional evidence on how much NovaSeq 6000 volume/revenue remains, how elastic the remaining 6000 customers are, the pace of 2026-2027 conversion, and whether the 6000 tail is really permanent (service end-of-life, parts, refurbished market, validated-assay migrations, lab announcements)."),
    ("1B", "Find unconventional evidence of accelerating discounting: large-account pricing, 35B economics, Ultima/Element/Roche/MGI price undercuts, quotes, tenders, contracts, customer leverage and bundling."),
    ("1C", "Find unconventional evidence that sequencing volume growth will slow: test-volume data, NIPT saturation, MRD/WGS adoption limits, non-cost bottlenecks, claims data, lab capacity and hiring."),
    ("2A/2B", "Find unconventional evidence on research customers: funding stress, discount demands, platform switching, Axelios/SBX adoption in academia, core-facility economics, and research consumables pricing."),
    ("wildcard", "Wild card: think of the most creative, non-obvious alternative-data angles on Illumina pricing and volume that a hedge fund would use (e.g. shipping/import records, app/web traffic, patent filings, regulatory submissions, satellite-of-data like conference poster counts, GitHub/bioinformatics pipeline adoption, citation counts by platform, SRA/ENA public sequence-archive submissions by instrument model)."),
]


def seed_queue():
    tasks = []
    scouts = [new_task(type="SCOUT", model="opus", label=lab, title=f"scout {lab}", instructions=ins)
              for lab, ins in SCOUT_SEEDS]
    seeds = [new_task(type="SEED", model="sonnet", title=f"seed {i + 1}: {name}", instructions=ins)
             for i, (name, ins) in enumerate(SEEDS)]
    # interleave: a scout, then four seeds
    while scouts or seeds:
        if scouts:
            tasks.append(scouts.pop(0))
        for _ in range(4):
            if seeds:
                tasks.append(seeds.pop(0))
    jsave(QUEUE, {"tasks": tasks})


# ------------------------------------------------------------------------------ final write-up

def final_input():
    f = jload(FINDINGS, {"items": []})["items"]
    srcs = jload(SOURCES, {"sources": []})["sources"]
    st = load_state()
    keep = [x for x in f if x.get("status") in ("verified", "verified_unreviewed")]
    # if the budget stopped verification early, include unverified medium/strong items, clearly marked
    unv = [dict(x, status="unverified") for x in f if x.get("status") == "unverified"
           and x.get("strength") in ("strong", "medium")]
    q = jload(QUEUE, {"tasks": []})["tasks"]
    data = {
        "verified_items": keep, "unverified_medium_strong_items": unv,
        "sources_dry_or_blocked": [{k: s.get(k) for k in ("id", "name", "url", "status", "notes", "attempts")}
                                   for s in srcs if s["status"] in ("dry", "blocked")],
        "sources_productive_or_exhausted": [{k: s.get(k) for k in ("id", "name", "url", "status", "new_items", "notes")}
                                            for s in srcs if s["status"] in ("productive", "exhausted")],
        "candidates_never_tested": [{k: s.get(k) for k in ("id", "name", "url", "rationale")}
                                    for s in srcs if s["status"] == "candidate"][:60],
        "unexplored_queue": [{k: t.get(k) for k in ("type", "title", "source_id")} for t in q][:40],
        "stats": {"tasks_done": st["tasks_done"], "strategist_cycles": len(st["cycles"]),
                  "sources_total": len(srcs), "items_total": len(f), "items_rejected":
                  sum(1 for x in f if x.get("status") == "rejected"), "spend_usd": st["cost_usd"],
                  "stop_reason": st.get("stop_reason"), "budget": load_budget(),
                  "apify": jload(APIFY_Q, {"requests": []})["requests"]},
    }
    p = JOB / "final_input.json"
    jsave(p, data)
    return p, keep + unv


def write_up():
    PARTS.mkdir(parents=True, exist_ok=True)
    for p in PARTS.glob("part_*.md"):
        p.unlink()
    inp, items = final_input()
    update_state(lambda s: s.update(stage="writing"))
    prompt = WRITE_PROMPT.format(date=DATE, thesis=THESIS, inp=inp, parts=PARTS)
    for attempt in range(2):
        log(f"WRITE-UP start (opus), attempt {attempt + 1}")
        text, cost = call_claude(prompt, "opus", ["Read", "Write", "Edit", "Glob"], TIMEOUT["WRITE"], budget=60)
        charge(cost)
        parts = sorted(PARTS.glob("part_*.md"), key=lambda p: int(re.findall(r"\d+", p.stem)[0]))
        doc = "\n\n".join(p.read_text(encoding="utf-8").strip() for p in parts).strip()
        if len(doc.split()) > 800:
            break
    else:
        log("WRITE-UP failed twice")
        return False
    # coverage check: every item tag cited; one revision if not
    cited = set(re.findall(r"\b([FD]\d{3})\b", doc))
    missing = [x["id"] for x in items if x["id"] not in cited]
    if missing:
        log(f"WRITE-UP: {len(missing)} items uncited; revision pass")
        fix = (f"REVISION TASK. The addendum is in these part files (edit them in place):\n" +
               "\n".join(f"- {p}" for p in parts) +
               f"\nThe input is {inp}. These items are not cited anywhere; add each to the right section as a "
               f"well-written evidence item with its link and tag (or merge into an existing item, adding the tag): "
               f"{', '.join(missing)}\nKeep the writing rules (plain English, context for every number). Reply DONE.")
        text, cost = call_claude(fix, "opus", ["Read", "Write", "Edit", "Glob"], 90, budget=25)
        charge(cost)
        parts = sorted(PARTS.glob("part_*.md"), key=lambda p: int(re.findall(r"\d+", p.stem)[0]))
        doc = "\n\n".join(p.read_text(encoding="utf-8").strip() for p in parts).strip()
    doc += "\n"
    MD_OUT.write_text(doc, encoding="utf-8")
    from md_to_html import convert
    page = convert(doc, "Thesis Scrape Addendum",
                   "New, verified alternative-data evidence for the ILMN pricing and research thesis, as of 2026-10-12.")
    HTML_OUT.write_text(page, encoding="utf-8")
    log(f"WRITE-UP done: {len(doc.split()):,} words; HTML {len(page):,} chars")
    return True


def write_datasets():
    DS.mkdir(parents=True, exist_ok=True)
    f = jload(FINDINGS, {"items": []})["items"]
    (DS / f"{DATE}_thesis_scrape_findings.json").write_text(json.dumps(f, indent=1, ensure_ascii=False), encoding="utf-8")
    cols = ["id", "status", "label", "direction", "strength", "claim", "detail", "url", "date", "source_name",
            "source_type", "quote", "why_new", "verify_note", "source_id", "task", "link", "found"]
    with open(DS / f"{DATE}_thesis_scrape_findings.csv", "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for x in f:
            w.writerow({k: x.get(k, "") for k in cols})
    (DS / f"{DATE}_thesis_scrape_sources.json").write_text(SOURCES.read_text(encoding="utf-8"), encoding="utf-8")
    (DS / f"{DATE}_thesis_scrape_README.md").write_text(f"""# Thesis scrape datasets ({DATE})

**What:** evidence and data sources from the overnight adaptive alternative-data scrape for the ILMN short thesis
(labels 1A-2B: NovaSeq 6000 mix shift, accelerating discounting, slowing volume, research price sensitivity,
research pricing). The readable summary is `Outputs/artifacts/{DATE}_thesis_scrape_addendum.html`
(Markdown: `Outputs/analyses/{DATE}_thesis_scrape_addendum.md`).

**Source:** open-web searches and fetches by headless Claude agents (scouts, probes, miners), plus Apify runs
executed by the hourly check; deduplicated against the existing corpus (Core Notes, prior evidence ledger) and
reviewed by a skeptical verifier. Built by `_Build/thesis_scrape.py`.

**Files**
- `{DATE}_thesis_scrape_findings.json` / `.csv`: one row per evidence item. Columns: id (F = found, D = derived),
  status (verified / verified_unreviewed / unverified / rejected), label (1A-2B), direction (supports / against),
  strength, claim, detail, url, date, source_name, source_type, quote (15 words or fewer), why_new, verify_note,
  source_id (links to sources.json), task, link (URL check result), found (timestamp).
- `{DATE}_thesis_scrape_sources.json`: the source registry: every data source considered, with status
  (productive / exhausted / dry / blocked / candidate), attempts, new items found and notes.

**Caveats:** web data quality varies; rejected rows are kept for transparency. Unverified rows were not reviewed.
""", encoding="utf-8")


def refresh_index():
    idx = WORK / "INDEX.md"
    t = idx.read_text(encoding="utf-8")
    outs = sorted(p for p in OUTPUTS.rglob("*") if p.is_file())
    block = "## Outputs\n\n" + "\n".join(f"- `{p.relative_to(WORK).as_posix()}`" for p in outs) + "\n"
    t = t[:t.index("## Outputs")] + block if "## Outputs" in t else t.rstrip() + "\n\n" + block
    idx.write_text(t, encoding="utf-8")


# ------------------------------------------------------------------------------ main loop

def build_known():
    if KNOWN.exists() and KNOWN.stat().st_size > 2000:
        return True
    log("KNOWN-EVIDENCE list start (sonnet)")
    text, cost = call_claude(KNOWN_PROMPT, "sonnet", ["Read", "Glob", "Grep"], TIMEOUT["KNOWN"], budget=12,
                             add_dirs=(CORE, OUTPUTS))
    charge(cost)
    if not text or len(text) < 2000:
        log(f"KNOWN-EVIDENCE list failed (${cost:.2f})")
        return False
    KNOWN.write_text(text, encoding="utf-8")
    log(f"KNOWN-EVIDENCE list written: {len(text.splitlines())} lines (${cost:.2f})")
    return True


def cmd_run(args):
    for d in (JOB, SANDBOX, RESULTS, APIFY_DIR, PARTS):
        d.mkdir(parents=True, exist_ok=True)
    keep_awake(True)
    stop_hb = threading.Event()

    def heartbeat():
        while not stop_hb.wait(120):
            try:
                update_state(lambda s: None)
            except Exception as e:
                log(f"  heartbeat write failed (will retry): {e!r}")
    threading.Thread(target=heartbeat, daemon=True).start()
    try:
        st = load_state()
        # tasks left "running" by a dead process go back to the front of the queue
        if st.get("running"):
            orphans = list(st["running"].values())
            enqueue([{k: v for k, v in t.items() if k != "started"} for t in orphans], front=True)
            update_state(lambda s: s.update(running={}))
            log(f"Requeued {len(orphans)} orphaned tasks")
        update_state(lambda s: s.update(pid=os.getpid(), started=s.get("started") or now()))
        if st["stage"] in ("complete",):
            log("Job already complete")
            return
        if st["stage"] not in ("final", "writing"):
            if not (build_known() or build_known()):
                log("Could not build the known-evidence list; continuing with the prior ledger as the exclusion list")
                KNOWN.write_text(f"(Fallback) Read the prior evidence ledger at {PRIOR_LEDGER} as the exclusion list.\n",
                                 encoding="utf-8")
            if not QUEUE.exists():
                seed_queue()
                update_state(lambda s: s.update(last_strat=time.time()))
            update_state(lambda s: s.update(stage="research"))
            log(f"Research loop running (pid {os.getpid()}), concurrency {CONCURRENCY}")
            research_loop()
        final_phase()
    except BaseException:
        import traceback
        log("CRASH:\n" + traceback.format_exc())
        raise
    finally:
        stop_hb.set()
        keep_awake(False)


def research_loop():
    futures = {}
    strat_future = None
    with ThreadPoolExecutor(max_workers=CONCURRENCY + 1) as ex:
        while True:
            for k in [k for k, f in futures.items() if f.done()]:
                futures.pop(k)
            if strat_future and strat_future.done():
                strat_future = None
            st = load_state()
            mode = budget_mode()
            busy = len(futures) + (1 if strat_future else 0)
            check_apify_returns()
            maybe_queue_verify()
            if st.get("stop") or mode in ("winddown", "hardcap"):
                reason = "stop flag" if st.get("stop") else f"budget {mode} (est {est_pct():.1f}%)"
                update_state(lambda s: s.update(stop_reason=s.get("stop_reason") or reason))
                log(f"Ending research: {reason}. Waiting for {len(futures)} running tasks.")
                break
            if saturated():
                update_state(lambda s: s.update(stop_reason="saturation"))
                log("Saturation: two strategist cycles with no new medium/strong items and no plausible untried source.")
                break
            q = jload(QUEUE, {"tasks": []})["tasks"]
            cyc = st["cycles"]
            if (len(cyc) >= 2 and cyc[-1]["queued"] == 0 and cyc[-2]["queued"] == 0 and not q and not futures
                    and not strat_future):
                update_state(lambda s: s.update(stop_reason="strategist queued nothing twice: search exhausted"))
                log("Strategist queued nothing in two cycles and nothing is running; ending research.")
                break
            due = (st["since_strat"] >= STRAT_EVERY_N or time.time() - st.get("last_strat", 0) >= STRAT_EVERY_S
                   or (not q and not futures))
            if due and not strat_future and busy < CONCURRENCY:
                if st.get("strat_fails", 0) >= 3 and not q and not futures:
                    update_state(lambda s: s.update(stop_reason="strategist failed 3 times with an empty queue"))
                    log("Strategist keeps failing and the queue is empty; ending research.")
                    break
                strat_future = ex.submit(run_strategist)
                time.sleep(2)
                continue
            if mode == "pause":
                time.sleep(60)
                continue
            if busy < CONCURRENCY:
                t = pop_task({"SEED", "SCOUT", "PROBE", "MINE", "VERIFY", "APIFY_MINE"})
                if t:
                    futures[t["id"]] = ex.submit(worker, t)
                    time.sleep(3)
                    continue
                if not futures and not strat_future and not q:
                    # empty: wait for strategist timing
                    time.sleep(20)
                    continue
            time.sleep(10)
        for f in list(futures.values()):
            try:
                f.result()
            except Exception:
                pass
        if strat_future:
            try:
                strat_future.result()
            except Exception:
                pass


def final_phase():
    update_state(lambda s: s.update(stage="final"))
    # last verification of anything still unverified, unless the hard cap is hit
    if budget_mode() != "hardcap" and maybe_queue_verify(force=True):
        with ThreadPoolExecutor(max_workers=CONCURRENCY) as ex:
            vt = []
            while True:
                t = pop_task({"VERIFY"})
                if not t:
                    break
                vt.append(ex.submit(worker, t))
            for f in vt:
                f.result()
    ok = write_up()
    write_datasets()
    refresh_index()
    st = update_state(lambda s: s.update(stage="complete" if ok else "failed", finished=now()))
    log(f"Job {st['stage']}. Spend ${st['cost_usd']:.2f}; est weekly {est_pct() or 0:.1f}%.")


def cmd_start(args):
    JOB.mkdir(parents=True, exist_ok=True)
    if args.baseline is not None and not BUDGET_F.exists():
        jsave(BUDGET_F, {"baseline": args.baseline, "winddown": args.baseline + WINDDOWN_PTS,
                         "hard_cap": args.baseline + BUDGET_PTS, "latest_pct": args.baseline,
                         "measured_at": now(), "cost_at_latest": 0.0, "pct_per_usd": PROVISIONAL_RATE,
                         "calibrated": False, "samples": []})
    exe = Path(sys.executable)
    pyw = exe.with_name("pythonw.exe") if os.name == "nt" else exe
    if not pyw.exists():
        pyw = exe
    # Launch through WMI so the job is not a child of the calling shell (which the app may kill when idle).
    cmdline = f'"{pyw}" "{Path(__file__).resolve()}" run'
    ps = ("$r = Invoke-CimMethod -ClassName Win32_Process -MethodName Create -Arguments "
          f"@{{CommandLine='{cmdline}'; CurrentDirectory='{ROOT}'}}; "
          "Write-Output (\"rc=\" + $r.ReturnValue + \" pid=\" + $r.ProcessId)")
    out = subprocess.run(["powershell", "-NoProfile", "-Command", ps], capture_output=True, text=True)
    print(f"Launched via WMI: {out.stdout.strip()} {out.stderr.strip()[:200]}")


def cmd_status(args):
    st = load_state()
    hb = st.get("heartbeat", 0)
    age = (time.time() - hb) / 60 if hb else None
    stalled = st.get("stage") not in ("complete", "failed", "new") and (age is None or age > 25)
    b = load_budget()
    print(f"stage: {st.get('stage')}  started: {st.get('started')}  heartbeat: {st.get('heartbeat_human')} "
          f"({'%.0f' % age if age is not None else '?'} min ago){'  STALLED' if stalled else ''}")
    e = est_pct()
    print(f"budget: spend ${st['cost_usd']:.2f}; est weekly {e if e is None else round(e, 1)}% (baseline "
          f"{b.get('baseline')}, wind-down {b.get('winddown')}, cap {b.get('hard_cap')}; rate {b.get('pct_per_usd', 0):.3f} "
          f"%/$; calibrated={b.get('calibrated')}; mode={budget_mode() if b else '?'}); paused_until={st.get('paused_until')}")
    srcs = jload(SOURCES, {"sources": []})["sources"]
    by = {}
    for s in srcs:
        by[s["status"]] = by.get(s["status"], 0) + 1
    running = ", ".join(f"{k} {v.get('type')}" for k, v in st["running"].items()) or "none"
    nq = len(jload(QUEUE, {"tasks": []})["tasks"])
    print(f"tasks done: {st['tasks_done']}; running: {running}; queued: {nq}; strategist cycles: {len(st['cycles'])}")
    print(f"sources: {len(srcs)} {json.dumps(by)}")
    f = jload(FINDINGS, {"items": []})["items"]
    labs = {}
    for x in f:
        if x.get("status") != "rejected" and x.get("strength") in ("strong", "medium"):
            labs[x.get("label")] = labs.get(x.get("label"), 0) + 1
    print(f"items: {len(f)} total; medium/strong (not rejected) by label: {json.dumps(labs)}; verified: "
          f"{sum(1 for x in f if x.get('status') == 'verified')}; rejected: {sum(1 for x in f if x.get('status') == 'rejected')}")
    for c in st["cycles"][-4:]:
        print(f"  cycle {c['n']} {c['t']}: +{c['new_ms']} new med/strong; queued {c['queued']}; exhausted={c['exhausted']}")
    ap = jload(APIFY_Q, {"requests": []})["requests"]
    print(f"apify requests: {len(ap)} ({sum(1 for r in ap if r['status'] == 'pending')} pending)")
    print(f"stop_reason: {st.get('stop_reason')}  published: {st.get('published')}")


def cmd_check(args):
    st = load_state()
    hb = st.get("heartbeat", 0)
    age = (time.time() - hb) / 60 if hb else 999
    pid = st.get("pid")
    alive = False
    if pid:
        out = subprocess.run(["tasklist", "/FI", f"PID eq {pid}", "/NH"], capture_output=True, text=True).stdout
        alive = str(pid) in out and "python" in out.lower()
    if st.get("stage") == "complete":
        pass
    elif alive and age <= 30:
        print(f"Job process {pid} alive (last state write {age:.0f} min ago): no action.")
    else:
        if alive:
            print(f"Job process {pid} alive but silent for {age:.0f} min: treating as hung, killing it.")
            subprocess.run(["taskkill", "/T", "/F", "/PID", str(pid)], capture_output=True)
            time.sleep(3)
        print("Job stalled or failed: relaunching.")
        if st.get("stage") == "failed":
            update_state(lambda s: s.update(stage="final"))
        cmd_start(argparse.Namespace(baseline=None))
        time.sleep(10)
    cmd_status(args)
    if load_state().get("stage") == "complete":
        print("COMPLETE" + (" AND PUBLISHED" if load_state().get("published") else f" - publish {HTML_OUT}"))


def cmd_usage(args):
    pct = args.pct
    b = load_budget()
    st = load_state()
    if not b:
        print("no budget.json; start the job with --baseline first")
        return
    spend = st["cost_usd"]
    b.setdefault("samples", []).append({"t": now(), "pct": pct, "cost": spend})
    delta = pct - b["baseline"]
    if spend >= 5:
        if delta >= 1:
            # displayed delta k means the true delta lies in (k-1, k+1): use k+0.5 (mildly conservative)
            b["pct_per_usd"] = (delta + 0.5) / spend
            b["calibrated"] = True
            b["calibration_note"] = f"{now()}: weekly +{delta:g} pts for ${spend:.2f} of job spend"
        else:
            b["pct_per_usd"] = min(b["pct_per_usd"], 1.0 / spend)
            b["calibration_note"] = f"{now()}: weekly +0 pts for ${spend:.2f}; rate capped at {1.0 / spend:.4f}"
    b.update(latest_pct=pct, measured_at=now(), cost_at_latest=spend)
    jsave(BUDGET_F, b)
    print(f"weekly {pct}% (baseline {b['baseline']}%), job spend ${spend:.2f}, rate {b['pct_per_usd']:.4f} %/$ "
          f"({'calibrated' if b.get('calibrated') else 'provisional'}); est now {est_pct():.1f}%; "
          f"wind-down {b['winddown']}, cap {b['hard_cap']}. {b.get('calibration_note', '')}")


def cmd_apify_pending(args):
    q = jload(APIFY_Q, {"requests": []})
    pend = [r for r in q["requests"] if r["status"] == "pending"]
    if not pend:
        print("NO PENDING APIFY REQUESTS")
        return
    for r in pend[:3]:
        print(json.dumps({k: r[k] for k in ("id", "actor", "input", "why", "max_items")}, ensure_ascii=False))
        print(f"  -> save dataset items as JSON to: {APIFY_DIR / (r['id'] + '.json')}")


def cmd_apify_done(args):
    with _lock:
        q = jload(APIFY_Q, {"requests": []})
        for r in q["requests"]:
            if r["id"] == args.id:
                r.update(status="done", result_path=str(Path(args.path).resolve()), done=now())
        jsave(APIFY_Q, q)
    print("recorded")


def cmd_apify_failed(args):
    with _lock:
        q = jload(APIFY_Q, {"requests": []})
        for r in q["requests"]:
            if r["id"] == args.id:
                r.update(status="failed", why_failed=args.why[:300], done=now())
        jsave(APIFY_Q, q)
    print("recorded")


def cmd_published(args):
    update_state(lambda s: s.update(published=args.url))
    print("recorded")


def cmd_stop(args):
    update_state(lambda s: s.update(stop=True))
    print("stop flag set; running tasks finish, then the last verify and the write-up run")


def main():
    for s in (sys.stdout, sys.stderr):   # Windows consoles default to cp1252; never crash on printing
        try:
            s.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("run").set_defaults(fn=cmd_run)
    p = sub.add_parser("start"); p.add_argument("--baseline", type=float); p.set_defaults(fn=cmd_start)
    sub.add_parser("status").set_defaults(fn=cmd_status)
    sub.add_parser("check").set_defaults(fn=cmd_check)
    p = sub.add_parser("usage"); p.add_argument("pct", type=float); p.set_defaults(fn=cmd_usage)
    sub.add_parser("apify_pending").set_defaults(fn=cmd_apify_pending)
    p = sub.add_parser("apify_done"); p.add_argument("id"); p.add_argument("path"); p.set_defaults(fn=cmd_apify_done)
    p = sub.add_parser("apify_failed"); p.add_argument("id"); p.add_argument("why"); p.set_defaults(fn=cmd_apify_failed)
    p = sub.add_parser("published"); p.add_argument("url"); p.set_defaults(fn=cmd_published)
    sub.add_parser("stop").set_defaults(fn=cmd_stop)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
