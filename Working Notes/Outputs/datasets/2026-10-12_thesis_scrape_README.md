# Thesis scrape datasets (2026-10-12)

**What:** evidence and data sources from the overnight adaptive alternative-data scrape for the ILMN short thesis
(labels 1A-2B: NovaSeq 6000 mix shift, accelerating discounting, slowing volume, research price sensitivity,
research pricing). The readable summary is `Outputs/artifacts/2026-10-12_thesis_scrape_addendum.html`
(Markdown: `Outputs/analyses/2026-10-12_thesis_scrape_addendum.md`).

**Source:** open-web searches and fetches by headless Claude agents (scouts, probes, miners), plus Apify runs
executed by the hourly check; deduplicated against the existing corpus (Core Notes, prior evidence ledger) and
reviewed by a skeptical verifier. Built by `_Build/thesis_scrape.py`.

**Files**
- `2026-10-12_thesis_scrape_findings.json` / `.csv`: one row per evidence item. Columns: id (F = found, D = derived),
  status (verified / verified_unreviewed / unverified / rejected), label (1A-2B), direction (supports / against),
  strength, claim, detail, url, date, source_name, source_type, quote (15 words or fewer), why_new, verify_note,
  source_id (links to sources.json), task, link (URL check result), found (timestamp).
- `2026-10-12_thesis_scrape_sources.json`: the source registry: every data source considered, with status
  (productive / exhausted / dry / blocked / candidate), attempts, new items found and notes.

**Caveats:** web data quality varies; rejected rows are kept for transparency. Unverified rows were not reviewed.
