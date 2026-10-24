"""Rebuild the full addendum web page from Core Notes file 16 (run after editing the addendum)."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "_Build"))
from md_to_html import convert  # noqa: E402

md = (ROOT / "Core Notes" / "16_Addendum_Clinical_Consumables_Thesis.md").read_text(encoding="utf-8")
page = convert(md, "Clinical Consumables Thesis",
               "Is Illumina over-earning on clinical consumables as the NovaSeq 6000 converts to the X? "
               "Full evidence, as of 2026-10-11.")
out = ROOT / "Working Notes" / "Outputs" / "artifacts" / "2026-10-11_clinical_consumables_thesis.html"
out.write_text(page, encoding="utf-8")
print(f"wrote {out} ({len(page):,} chars)")
