#!/bin/bash
# Full ILMN model pipeline: side builds -> spec -> build -> links -> case snapshots -> seed multiples -> rebuild -> links -> snapshots -> verify -> PNGs
set -e
S="/c/Users/palaz/AppData/Local/Temp/claude/C--Users-palaz-OneDrive-Documents-ILMN-Claude-Code-Local-Folder/e9c6ec81-c5dc-475c-9ef5-0cd8bd503e68/scratchpad/fmb"
cd "/c/Users/palaz/OneDrive/Documents/ILMN Claude Code Local Folder"
M="Working Notes/Outputs/models"
CLI="C:/Users/palaz/.claude/skills/financial-model-builder/scripts/fmb_cli.py"
FINAL="$M/ILMN_model_2026-11-03.xlsx"
MODEL="$S/work/ILMN_model_2026-11-03.xlsx"
mkdir -p "$S/work"
step() { echo; echo "##### $(date +%H:%M:%S) $1"; }
# the private safe-mode Excel sometimes disconnects right after the previous session closes: retry
retry() { local n=0; until "$@"; do n=$((n+1)); if [ $n -ge 3 ]; then echo "FAILED after 3 attempts: $*"; return 1; fi; echo "retrying ($n) after 10s"; sleep 10; done; }

step "side builds + spec + merge"
python -I "$S/make_side_builds.py" "$M/ILMN_side_builds.json"
python -I "$CLI" spec "$M/ILMN_model_inputs.xlsx" "$M/model_data_raw.json" "--out=$M/model_spec.json" "--data-out=$M/model_data.json" | tail -1 | cut -c1-80
python -I "$S/merge_side_builds.py" "$M/model_spec.json" "$M/ILMN_side_builds.json"
step "build 1 + link"
python -I "$CLI" build "$M/model_spec.json" "$M/model_data.json" "--out=$MODEL" | tail -1 | cut -c1-60
python -I "$S/link_multiples.py" "$MODEL" "$M/ILMN_side_builds.json"
step "cases 1"
retry python "$CLI" cases "$MODEL" "$M/model_spec.json" > "$S/cases_out1.txt" 2>&1; tail -2 "$S/cases_out1.txt" | cut -c1-80
step "case NI snapshots 1"
retry python "$S/cases_eps.py" "$MODEL" "$M/model_spec.json" "$M/ILMN_side_builds.json" "--out=$S/implied1.json" > "$S/eps_out1.txt" 2>&1; grep -A 22 '"implied"' "$S/eps_out1.txt"
step "seed spec multiples"
python -I "$S/seed_multiples.py" "$M/model_spec.json" "$S/implied1.json" "$MODEL"
step "build 2 + link"
python -I "$CLI" build "$M/model_spec.json" "$M/model_data.json" "--out=$MODEL" | tail -1 | cut -c1-60
python -I "$S/link_multiples.py" "$MODEL" "$M/ILMN_side_builds.json"
step "cases 2"
retry python "$CLI" cases "$MODEL" "$M/model_spec.json" > "$S/cases_out2.txt" 2>&1; tail -2 "$S/cases_out2.txt" | cut -c1-80
step "case NI snapshots 2"
retry python "$S/cases_eps.py" "$MODEL" "$M/model_spec.json" "$M/ILMN_side_builds.json" "--out=$S/implied2.json" > "$S/eps_out2.txt" 2>&1; grep -A 22 '"implied"' "$S/eps_out2.txt"
step "verify"
retry python "$CLI" verify "$MODEL" > "$S/verify_final2.json" 2>&1 || true
python - "$S/verify_final2.json" <<'PYEOF'
import json, sys, collections
t = open(sys.argv[1], encoding="utf-8").read(); v = json.loads(t[t.find("{"):])
print("ok:", v.get("ok"), "| static:", json.dumps(v.get("static"))[:200])
rc = v.get("recalc", {}); errs = rc.get("errors") or []
by = collections.Counter()
for e in errs:
    sheet, rest = e.split("!", 1); by[(sheet, rest.split(": ")[1])] += 1
print("error cells:", len(errs), dict(by))
print("checks:", {k: (max(abs(x) for x in val if isinstance(x, (int, float))) if val else None) for k, val in (rc.get("checks") or {}).items()})
print("warnings:", json.dumps(rc.get("warnings"))[:300])
PYEOF
step "snapshots"
retry python "$CLI" snapshot "$MODEL" "Multiples Build!A1:L28" "$S/snap_mult.png" | tail -1 | cut -c1-30
retry python "$CLI" snapshot "$MODEL" "Tearsheet!A1:R58" "$S/snap_ts2.png" | tail -1 | cut -c1-30
retry python "$CLI" snapshot "$MODEL" "DCF!A1:P70" "$S/snap_dcf2.png" | tail -1 | cut -c1-30
retry python "$CLI" snapshot "$MODEL" "Margin Build!A36:AB70" "$S/snap_mb.png" | tail -1 | cut -c1-30
step "copy back"
cp "$MODEL" "$FINAL" && cp "${MODEL%.xlsx}.map.json" "${FINAL%.xlsx}.map.json" && echo "model and map copied to $FINAL"
step "done"
