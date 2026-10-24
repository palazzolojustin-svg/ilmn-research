# Agent 13: Sequencing intensity per test and clinical Gb growth inputs

*Model: sonnet. Run 2026-10-11 02:04:25. Cost $0.99 (API-equivalent).*

**Assignment:** Quantify data consumed per clinical test and how it is changing, from vendor specs, publications and company materials: NIPT (Gb per sample, low-pass WGS), CGP tissue panels (e.g. TSO 500, FoundationOne), liquid biopsy panels, tumor-informed panel MRD vs whole-genome MRD (e.g. Signatera exome+panel, Personalis NeXT, NeoGenomics RaDaR, Myriad Precise MRD, C2i/Veracyte WGS MRD, Illumina's WGS MRD workflow), rare disease exome vs genome, MCED (Galleri methylation), pharmacogenomics. Build a table: test type, Gb per test (range), trend, source. Then build a simple model: 2026-2028 clinical Gb growth = test growth x intensity change, by category, with low/base/high cases, and compare with management's >30% clinical data-growth claim.

## Key findings

1. **Intensity per test varies by roughly 1,000x, so test-count growth is a weak proxy for Gb growth.** Rough Gb per test: NIPT ~1–2, tissue CGP ~15, exome ~8, 30x genome ~100, liquid CGP ~120, WGS-style plasma MRD ~250. Clinical Gb growth depends on mix. Rare-disease genomes and WGS MRD matter far more per test than NIPT or amplicon MRD.
2. **Most of the fastest-growing clinical tests are not Gb-hungry.** Natera's clinical MRD units were 283K in Q2'26 (+56% y/y). Signatera is built on multiplex-PCR deep sequencing of ~16 patient-specific variants, which uses very little data per plasma draw. Test growth of 50%+ therefore does not mean Gb growth of 50%.
   - FACT: Natera reports 283K units, +56% y/y [Natera Q2'26 call via [Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/08/13/natera-ntra-q2-2026-earnings-call-transcript/), 2026-08-13; [MedPath](https://trial.medpath.com/news/natera-reports-record-signatera-volumes-in-q2-2026-raises-guidance-on-mrd-market-momentum)].
   - FACT: Signatera uses 16 variants at ~100,000x, "up to 350,000x" per target in newer material [Natera white papers](https://www.natera.com/wp-content/uploads/2020/11/Oncology-Clinical-Seeing-beyond-the-limit-Detect-residual-disease-and-assess-treatment-response-SGN_AV_WP.pdf).
   - OPINION: this works out to well under 1 Gb per plasma sample. That is my estimate, not a disclosed figure.
3. **The heavy-Gb MRD designs are the whole-genome and exome-plus designs, and they are still small.**
   - FACT: Personalis NeXT Personal Dx spec is ≥250 Gb per sample, ~5,000x on boosted genes and ~2,000x exome-wide. My search tool read this from a Personalis filing page but did not name the document. I tried to open the original and failed (the PDF would not parse), so verify before relying on it. Source: [Personalis 10-Q search result, 2026](https://www.sec.gov/Archives/edgar/data/0001527753/000119312526332817/psnl-20260630.htm).
   - FACT: Personalis' Q2'26 clinical test revenue was only $2.6M.
   - FACT: Illumina's WGS MRD kit entered early access on 2026-05-28, with global launch in 2027. Its sensitivity is 10 ppm now, with a single-digit ppm goal using duplex reads. Illumina has not disclosed its depth or Gb per sample [Diagnostics World News, 2026-06-08](https://www.diagnosticsworldnews.com/news/2026/06/08/illumina-launches-first-tool-in-wgs-oncology-portfolio).
   - MGMT: Illumina said the workflow is meant to cut assay-development cost and time.
4. **Deep-sequencing oncology is the segment competitors can't easily take.** A current Natera associate director said Element at 30–50x cannot do CGP (which "usually needs 150X or deeper, plus you need RNA") or Signatera/ctDNA. They said shallow tests like NIPT, transplant and infectious disease are where Ultima/Element/Roche will take share. Ultima prices at "$80–$110" per sample, with a Solaris "$50 genome" (the expert's recollection). See [Expert call, Natera, 2026-07-22, Extracts/ILMN/expert_call/Expert_2026-07-22_Associate_Director_at_Natera...]. This matters for the thesis: the competition lands on the low-intensity, price-sensitive segments, while the high-Gb segments are stickier.
5. **Test growth is strong at the main oncology customers.** The table below shows the latest quarter.

| Company | Metric (Q2'26) | Growth | Source |
|---|---|---|---|
| Natera | Clinical MRD units 283K | +56% y/y | Natera Q2'26 call |
| Guardant | Oncology tests ~104K | +63% y/y | [MarketBeat, 2026-07-30](https://www.marketbeat.com/instant-alerts/guardant-health-q2-earnings-call-highlights-2026-07-30/) |
| Guardant | Reveal (MRD) volume | >100% y/y | same |
| Guardant | Guardant360 Liquid volume | >30% y/y | same |
| Guardant | Shield (blood CRC screen) ~66K | +22K q/q | same |
| GRAIL | Galleri volume >61K | +35% y/y | [GRAIL Q2'26 release, 2026-08-05](https://www.biospace.com/press-releases/grail-reports-second-quarter-2026-financial-results) |

6. **Base case: clinical Gb grows ~23% a year in 2026–28, versus management's ">30%".** The range is ~10% (low) to ~35% (high). The model is below. It rests on my assumed clinical mix, which no source gives. Treat it as a framework.
7. **The >30% claim is not a clinical-only number.** MGMT: "Total gigabase output on connected high and mid-throughput instruments grew more than 30%" [ILMN Q2'26 call, 2026-07-30; [MarketBeat](https://www.marketbeat.com/instant-alerts/illumina-q2-earnings-call-highlights-2026-07-30/)]. That includes research, which Illumina says is declining in revenue (-7%). The clinical Gb figure is therefore not directly disclosed.
8. **A reconciliation puzzle favors the high case.** If Gb is +30% and price falls mid-teens, revenue would be about +10% (1.30 × 0.85). Yet ex-China clinical consumables revenue is +15% (Q2'26) and +20% (Q1'26). Either clinical Gb growth is well above 30%, price erosion is less than the "mid-teens" model, or mix and pricing (such as the shorter-shelf-life X pack) help. This is OPINION and an inference from known facts. It is worth asking management whether clinical Gb growth is ~35–40%.
9. **The sequencing share of a test's cost is small for the high-growth tests.**
   - FACT: GRAIL's Q2'26 cost of screening revenue was $23.3M on ~61K tests, ~$382 per test. Screening revenue of $42.6M implies ~$698 per test (my arithmetic).
   - OPINION: Galleri's sequencing depth is not public in what I found. Targeted methylation at 100–1,000x is far lighter than WGBS at 30x.
10. **Price cuts matter more than intensity for the revenue outcome.** At a ~20% cut in $/Gb (the 35B flow cell), a revenue-neutral result needs +25% Gb. The base case at ~23% is barely neutral. So a 6000→X conversion with a >60–70% per-Gb decline relies on volume from new tests or the exome→genome shift.

## Data per clinical test

Gb figures are either vendor-spec (S), derived from flow-cell yield (D) or my estimate (E). Flow-cell yields: the 25B flow cell gives ~8–10.5 Tb at 2×150, the 10B ~3–4 Tb, and the 1.5B ~0.5–0.7 Tb [Illumina NovaSeq X specs](https://www.illumina.com/systems/sequencing-platforms/novaseq-x-plus/specifications.html).

| Test type | Gb per test (range) | Trend | Source / basis |
|---|---|---|---|
| NIPT (genome-wide low-pass) | ~1–2 (E) | Flat to down; shallower or targeted designs favored | Literature recommends ~16–17M reads, ~0.35x (2×35 bp) [search result, undated]. Natera's Panorama is SNP-targeted (E: <1 Gb). |
| Exome (germline) | ~8 | Flat; being displaced by genome | ILMN Core Notes glossary, `00_Start_Here.md` |
| 30x genome (germline / rare disease) | ~100 (up to >120) | Up: genome replacing exome | Expert call 2026-07-23 (~100 Gb); Core Notes glossary (>120 Gb) |
| Tissue CGP (TSO 500 v2) | ~15 (D) | Up modestly: bigger panels, RNA | Illumina spec: 480 samples per 25B flow cell, 100M reads, 3,500x [Illumina](https://www.illumina.com/products/by-type/clinical-research-products/trusight-oncology-500-ht.html). I derived 15 Gb as 100M reads × 150 bp; if the spec means 100M read pairs it is 30 Gb, but 480 × 30 Gb would exceed a 25B flow cell's yield. |
| FoundationOne CDx | Not found in Gb | n/a | Spec: >500x median coverage, 324 genes ([FDA PMA](https://www.accessdata.fda.gov/cdrh_docs/pdf17/P170019S043B.pdf)) |
| Liquid CGP (TSO 500 ctDNA v2) | ~120 (D) | Up if panels grow | Illumina spec: 64 samples per 25B flow cell, 800M reads, 35,000x [Illumina](https://www.illumina.com/products/by-type/clinical-research-products/trusight-oncology-500-ctdna.html) |
| Tumor-informed amplicon MRD (Signatera) | <1 per plasma draw (E), plus a one-off tumor exome or WGS | Per-test intensity flat; frequency of draws rising | Natera white paper (16 variants, 100,000x) |
| Signatera Genome | Tumor + normal WGS (E: 200+ Gb one-off), plasma mPCR | Rising: WGS-designed assays | Natera release, [BusinessWire 2025-04-24](https://www.businesswire.com/news/home/20250424920561/en/Natera-Announces-Broad-Clinical-Launch-of-Ultra-Sensitive-Signatera-Genome-MRD-Test): "designed from a whole genome sequence" of tumor and matched normal, 1 ppm |
| Whole-genome MRD (Personalis NeXT Personal Dx) | ≥250 | Up if the model spreads | Personalis spec (see finding 3) |
| Illumina WGS MRD kit | Not disclosed | New (2027 launch) | Diagnostics World News, 2026-06-08 |
| MCED (Galleri) | Not found (E: tens of Gb or less, targeted methylation) | Flat | Targeted methylation 100–1,000x vs WGBS 20–50x (general literature) |
| Pharmacogenomics | Not found | n/a | n/a |

Observations from the table:
- The jump from an exome to a genome is ~12–15x in data. This is the single biggest intensity lever in germline.
- Liquid CGP uses about 8x the data of tissue CGP, because 35,000x is needed for low-frequency variants.
- Roche's illustration of a 1.1 Mb panel at 2,000x costs $25 per sample on AXELIOS [JPM, 2026-03-03, Extracts/ILMN/research/20260303_JP_Morgan_ILMN...]. That is a competitor-pricing data point for deep panels.

## Model: clinical Gb growth, 2026–28

Annual growth ≈ test growth × intensity change per year, weighted by each category's share of 2026 clinical Gb. **The category weights are my assumptions (OPINION)**; no source gives them. Tests and intensity are annual rates.

| Category | Weight | Low (tests / intensity) → Gb | Base → Gb | High → Gb |
|---|---|---|---|---|
| Rare disease / germline | 25% | +12% / +3% → +15% | +20% / +10% → +32% | +25% / +15% → +44% |
| Tissue CGP | 20% | +6% / 0 → +6% | +10% / +5% → +16% | +14% / +10% → +25% |
| Liquid CGP | 15% | +20% / -5% → +14% | +30% / 0 → +30% | +35% / +5% → +42% |
| Amplicon MRD | 7% | +30% / -10% → +17% | +45% / -5% → +38% | +55% / 0 → +55% |
| WGS-based MRD | 3% | +40% / 0 → +40% | +80% / 0 → +80% | +120% / 0 → +120% |
| NIPT / reproductive | 20% | +3% / -8% → -5% | +6% / -3% → +3% | +9% / 0 → +9% |
| MCED / screening | 5% | +15% → +15% | +30% → +30% | +45% → +45% |
| Other (PGx, infectious) | 5% | +5% | +10% | +15% |
| **Weighted clinical Gb growth** | | **~+9–10%** | **~+23%** | **~+35%** |

What the scenarios imply for revenue:
- At a mid-teens price decline (management's long-term model), revenue growth is roughly -7% (low), +5% (base) and +14% (high).
- Hitting management's ">30%" requires the high case. That means rare-disease genome conversion plus fast uptake of whole-genome MRD, both of which depend on tests still early or not yet launched.
- Mix drift (faster categories gaining share) adds roughly 1–2 points to each case, which I haven't included.
- Sensitivity: if NIPT is 30% of Gb rather than 20%, the base case falls by about 2 points. If rare disease is 35%, it rises by about 2 points.

## Read-through on the original thesis questions

- **Volume offsetting price:** I'd frame it as "plausible but not assured." The offset holds only if clinical Gb grows 25–30% or more, and the base case here sits just below that. This is OPINION.
- **Competition:** Per the Natera expert, Ultima/Element/Roche threaten the shallow, price-sensitive uses (NIPT, transplant, screening, large-scale WGS) first. These are also the lowest-Gb tests, so share loss there costs less volume than the revenue-per-test comparison suggests. The deep-oncology segment is stickier because switching mid-trial is "a no-no" (the same expert).
- **Customer power:** Natera and Guardant are the largest oncology volume drivers. Both are growing 50%+ in MRD units but use targeted sequencing, so they buy relatively little Gb per test. This is OPINION.

## Contradictions and stale data

- The Natera expert said "The big four, plus Natera, they're just using Illumina" and earlier said Natera also uses Element for ctDNA. These are inconsistent within the transcript [Extracts/ILMN/expert_call/Expert_2026-07-22...].
- The same expert said "last year" Illumina had a 2–3% revenue loss. This is unverified and from recollection.
- Genome size varies by source: ~100 Gb (expert, 2026-07-23) vs ">120 Gb" (Core Notes glossary). The difference is coverage target and read length.
- The TSO 500 reads-to-Gb conversion depends on whether "100M reads" means reads or read pairs (see table).
- Personalis' ≥250 Gb/sample figure came through a search summary of a filing page. I could not open the original.
- Natera's disclosure that Signatera Genome is WGS-designed with mPCR monitoring could be read as high-Gb. The Gb sits in the one-off tumor and normal WGS, not the repeat plasma draws.
- Reconciliation puzzle in finding 8 (clinical consumables revenue +15–20% vs >30% Gb with mid-teens price decline).

## Gaps / what I could not find

- Gb per sample for Galleri, Guardant Reveal/Shield/Guardant360, Veracyte TrueMRD, Myriad Precise MRD, NeoGenomics RaDaR, and commercial NIPT (Natera, Labcorp, Quest, BillionToOne). No vendor publishes these.
- Illumina's own clinical Gb breakdown by application. The whole-genome MRD kit's depth and Gb per sample are undisclosed.
- The actual clinical share of total Gb (the >30% claim covers all connected HT and MT instruments).
- Peer-reviewed data on what share of rare-disease labs are moving from exome to genome. I only found the meta-analysis (diagnostic yield of 0.38 exome vs 0.34 genome) and Germany's model project, not lab-mix data.
- I did not search Quest/Labcorp/Tempus/Myriad/BillionToOne volumes. I also did not open Roche's AXELIOS per-test economics beyond the JPM $25/sample illustration.

Sources:
- [Natera white paper](https://www.natera.com/wp-content/uploads/2020/11/Oncology-Clinical-Seeing-beyond-the-limit-Detect-residual-disease-and-assess-treatment-response-SGN_AV_WP.pdf)
- [Natera Q2'26 transcript](https://www.fool.com/earnings/call-transcripts/2026/08/13/natera-ntra-q2-2026-earnings-call-transcript/)
- [MedPath, Natera Q2'26](https://trial.medpath.com/news/natera-reports-record-signatera-volumes-in-q2-2026-raises-guidance-on-mrd-market-momentum)
- [BusinessWire, Signatera Genome, 2025-04-24](https://www.businesswire.com/news/home/20250424920561/en/Natera-Announces-Broad-Clinical-Launch-of-Ultra-Sensitive-Signatera-Genome-MRD-Test)
- [MarketBeat, Guardant Q2'26, 2026-07-30](https://www.marketbeat.com/instant-alerts/guardant-health-q2-earnings-call-highlights-2026-07-30/)
- [GRAIL Q2'26 release, 2026-08-05](https://www.biospace.com/press-releases/grail-reports-second-quarter-2026-financial-results)
- [MarketBeat, Illumina Q2'26, 2026-07-30](https://www.marketbeat.com/instant-alerts/illumina-q2-earnings-call-highlights-2026-07-30/)
- [Diagnostics World News, 2026-06-08](https://www.diagnosticsworldnews.com/news/2026/06/08/illumina-launches-first-tool-in-wgs-oncology-portfolio)
- [Illumina TSO 500 HT](https://www.illumina.com/products/by-type/clinical-research-products/trusight-oncology-500-ht.html)
- [Illumina TSO 500 ctDNA v2](https://www.illumina.com/products/by-type/clinical-research-products/trusight-oncology-500-ctdna.html)
- [Illumina NovaSeq X specs](https://www.illumina.com/systems/sequencing-platforms/novaseq-x-plus/specifications.html)
- [FDA PMA, FoundationOne CDx](https://www.accessdata.fda.gov/cdrh_docs/pdf17/P170019S043B.pdf)
- [Personalis 10-Q, 2026](https://www.sec.gov/Archives/edgar/data/0001527753/000119312526332817/psnl-20260630.htm)
