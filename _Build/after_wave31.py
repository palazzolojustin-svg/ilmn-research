"""One-off watcher (2026-10-11): once every agent of research wave 31 has started, set the job's stop flag so
no wave 32 is planned; wave 31 finishes and the job proceeds to the model, red team, fact-check and write-up."""
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOG = ROOT / "_Build" / "clinical_scrape.log"
TARGET = 31


def note(msg):
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] [after_wave31] {msg}\n")


deadline = time.time() + 4 * 3600
while time.time() < deadline:
    text = LOG.read_text(encoding="utf-8", errors="replace")
    if re.search(r"Saturation:|ending research loop|Synthesis \(opus\) start", text):
        note("research loop already ended before wave 31 completed starting; nothing to do")
        sys.exit(0)
    m = None
    for m in re.finditer(rf"^\[[^\]]+\] Wave {TARGET}: (.*)$", text, re.M):
        pass
    if m:
        ids = re.findall(r"(?:^|; )(\d+) ", m.group(1))
        after = text[m.end():]
        started = [i for i in ids if re.search(rf"Agent {i} (start|done|FAILED|skipped)", after)]
        if ids and len(started) == len(ids):
            subprocess.run([sys.executable, str(ROOT / "_Build" / "clinical_scrape.py"), "stop"], cwd=ROOT)
            note(f"all wave {TARGET} agents started ({', '.join(ids)}); stop flag set so no wave {TARGET + 1} "
                 f"is planned; write-up follows")
            sys.exit(0)
    time.sleep(5)
note("timed out waiting for wave 31")
