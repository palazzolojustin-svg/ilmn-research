# Agent 135: 134-web-MRD-plasma-depth-Gb-per-sample-NCCN-CIRCULATE-ADLT-and-CGP-WGS-coverage-2026

*Model: sonnet. Run 2026-10-11 11:59:16. Cost $0.91 (API-equivalent).*

**Assignment:** Close open gaps 1, 2 and 3 to quantify go-forward clinical Gb volume. (a) Find sequencing depth, plasma input or Gb per sample for Natera Signatera (and Signatera Genome / WGS-based), Guardant Reveal, NeXT Personal (Personalis; try bioRxiv, medRxiv mirrors, Europe PMC, the Personalis 10-K and investor decks), RaDaR (NeoGenomics/Inivata), clonoSEQ (Adaptive), Haystack (Quest), and Labcorp/Ultima MRD. Convert to Gb per test, with the assumptions shown. (b) Verify NCCN colon, rectal and other ctDNA/MRD guideline status through ASCO Post, Healio, OncLive or nccn.org 2026 updates. Find CIRCULATE-US, VEGA and DYNAMIC-III results and the implied surveillance cadence (tests per patient per year). (c) Pull the 2026 CMS ADLT list, MolDX/Palmetto DEX Z-code entries and coverage determinations for MRD, CGP and WGS, plus ACS Facts & Figures 2026 and SEER patient counts. Build a simple addressable-volume model: eligible patients x adoption x tests per year x Gb per test, to give a 2025 to 2028 clinical Gb CAGR range. Compare with management's mid-20s % volume growth. Cite every source with a URL and date.

## Key findings

1. **The CIRCULATE ASCO 2026 result is not CIRCULATE-US.** The "62% vs 19% recurrence" data (reported 31 May 2026) come from **CIRCULATE-AIO** (NCT04089631, Germany/Austria, about 140 centres). It used an academic tumor-informed assay tracking up to 71–78 genes, not Signatera, and tested only stage II MSS colon cancer. FACT [OncLive, 2026-05-31, https://www.onclive.com/view/ctdna-guided-adjuvant-chemotherapy-improves-dfs-reduces-disease-recurrence-in-stage-ii-colon-cancer]. A search-engine summary labelled these data as "CIRCULATE-US". Treat that label as wrong.
   - Key numbers: ctDNA positivity was only 2.9% of randomized patients, with a single post-op draw at a median of 21 days. Assay sensitivity was 31% and specificity 98%.
   - Per-protocol results (21 chemo vs 15 observation): 3-year recurrence 62%→19%, DFS 38%→77%.
   - The intention-to-treat primary analysis was formally negative because of under-enrollment.
   - **Implication:** this trial tested a single draw, not serial surveillance, so it adds no cadence support for Gb. A single draw also means a low-volume use case.

2. **CIRCULATE-US (NRG-GI008, Signatera) had not reported.** It was at 967 of 1,912 planned patients on 4 Sep 2025 [NRG Oncology/Duke listings via search; no results found]. It is the trial that would use serial Signatera monitoring in ctDNA-negative patients. I found no 2026 readout, and a readout is not yet a Gb driver.

3. **Signatera Genome plasma Gb per draw is about 10–15x the classic Signatera draw.**
   - Classic Signatera is 16 amplicons at about 100,000x average read depth, so about 1.6M reads [Natera white papers, https://www.natera.com/wp-content/uploads/2020/11/Oncology-Clinical-Seeing-beyond-the-limit-Detect-residual-disease-and-assess-treatment-response-SGN_AV_WP.pdf; NICE MIB307, https://www.nice.org.uk/advice/mib307/chapter/The-technology].
   - Signatera Genome is 64 clonal variants at up to 350,000x each, so about 22M reads (launched broadly 2025-04-24) [Natera/BusinessWire, 2025-04-24, https://www.businesswire.com/news/home/20250424920561/en/Natera-Announces-Broad-Clinical-Launch-of-Ultra-Sensitive-Signatera-Genome-MRD-Test].
   - Converting reads to Gb (my assumption: 100–150 bp read length, 350,000x read depth per variant):
     - Classic: about 0.16–0.24 Gb per draw.
     - Genome: about 2.2–3.4 Gb per draw.
   - This refines ledger E082 ("<1 Gb per plasma draw"). The classic figure holds and the Genome figure is roughly 10x higher. OPINION (derived).
   - The 350,000x and 64-variant figures come from a search snippet of the Natera launch release, not from the fetched page. The fetched page confirmed only mPCR-NGS and 1 ppm.

4. **The one-off tumor and normal sequencing dominates Gb per patient for WGS-designed assays.**
   - NeXT Personal tumor and normal are sequenced on Illumina NovaSeq to "at least 30x". A 30x human genome is about 90–100 Gb, my rule of thumb.
   - Panels carry up to about 1,800 variants. Of 118 patient panels, nearly half had more than 1,800 targets and 70% had more than 1,000 [Oncotarget, Mar 2024, PMC10939476, https://pmc.ncbi.nlm.nih.gov/articles/PMC10939476/]. FACT.
   - cfDNA input was up to 4.1 mL of plasma (median 3.5 mL), 3.4–420 ng yield, up to 30 ng in the library, modal about 15 ng. FACT.
   - Plasma depth is not stated; the paper says only that samples were "significantly over-sequenced". The ≥250 Gb figure in E082 therefore remains an estimate, not a disclosure.
   - Per-patient Gb: tumor plus normal WGS is roughly 200+ Gb once, against about 3 Gb per Genome draw. If Signatera Genome and NeXT Personal take mix, the Gb comes from new patient starts, not from more draws.

5. **NCCN status is unchanged from the ledger on the sources I could reach.**
   - Feb 2025: ctDNA recognised as prognostic only. "Insufficient evidence to recommend routine use outside clinical trials", and no de-escalation based on ctDNA. FACT [OncLive, https://www.onclive.com/view/nccn-updates-ctdna-stance-in-colon-rectal-and-mcc-guidelines; Natera/BusinessWire, 2025-02-10, https://www.businesswire.com/news/home/20250210708213/en].
   - Merkel cell carcinoma is the exception: ctDNA "often obtained every 3 months" for surveillance, citing a Signatera JCO 2024 paper.
   - I found no 2026 NCCN colon or rectal change in search results. nccn.org was not directly verified, so ledger gap 2 stays open for NCCN.

6. **DYNAMIC-III (Nature Medicine, Oct 2025) supports ctDNA-negative de-escalation.**
   - Recurrence-free survival was 85% (de-escalated) vs 88% (standard) in ctDNA-negative stage III patients, with less chemotherapy.
   - ctDNA-positive patients got no benefit from escalation [Ludwig Link, Apr 2026, https://www.ludwigcancerresearch.org/ludwig-link/april-2026/ctdna-predicts-post-surgical-recurrence-risk-for-stage-iii-crc/]. FACT.
   - The page gave no surveillance cadence. VEGA and ALTAIR (CIRCULATE-Japan) are described only as "ongoing".
   - Net read: the evidence is mostly about how to treat after the first post-op test, not about serial testing frequency.

7. **Medicare covers Signatera Genome under MolDX LCD L38779 for CRC, breast, bladder, ovarian and lung cancers and for pan-cancer immunotherapy monitoring.**
   - CRC monitoring is allowed "with the same frequency as CEA" [Natera/BusinessWire, 2025-06-04, https://www.businesswire.com/news/home/20250604942709/en; GenomeWeb]. FACT.
   - CEA surveillance in colorectal follow-up is typically every 3–6 months for 2–5 years (my background knowledge, not verified in this session). That implies about 2–4 draws a year in CRC.
   - This refines ledger E089 on reimbursement. It does not change the Medicare rate figures already there ($3,920 → $3,590).

8. **US patient counts (ACS Facts & Figures 2026):**
   - 2,114,850 new cancer cases and 626,140 deaths estimated for 2026 [cancer.org, 2026, https://www.cancer.org/content/dam/cancer-org/research/cancer-facts-and-statistics/annual-cancer-facts-and-figures/2026/mr6-leading-sites-2026-branded.pdf]. FACT.
   - Colorectal: 158,850 new cases, with 108,860 colon and 49,990 rectal [https://www.cancer.org/cancer/types/colon-rectal-cancer/about/key-statistics.html]. FACT.
   - I did not get stage splits. SEER was not queried, so stage II–III share and resection rates below are assumptions.

9. **Other assays' sequencing specs are largely unavailable.**
   - Haystack tracks up to 50 mutations, accepts up to 3 blood tubes, with an LoD95 of 0.063 mean ctDNA molecules/mL and a noise floor below 1 error per 1M cfDNA molecules. No depth or ng input is disclosed [haystackmrd.com, https://haystackmrd.com/dna-input-and-number-of-mutations-tracked-a-balancing-act]. FACT.
   - For clonoSEQ, RaDaR and Guardant Reveal I found no usable Gb or depth data.

## Addressable-volume model (OPINION; every input is an assumption)

I could not source an adoption curve, so this is a sensitivity table, not a forecast.

**Gb per patient-year (new MRD patient, year 1):**

| Assay type | One-off tumor and normal | Plasma draws per year | Gb per draw | Total Gb per patient-year |
|---|---|---|---|---|
| Classic amplicon (Signatera-type) | about 25 Gb (WES; assumed) | 4 | about 0.2 | about 26 Gb |
| Signatera Genome | about 200 Gb (WGS at 30x or more; assumed) | 4 | about 3 | about 212 Gb |
| NeXT Personal | about 200+ Gb (≥30x) | 4 | 5–60 (unknown) | about 220–450 Gb |

**Scenario growth in MRD Gb, 2025→2028:**
- Patients tested: +25% a year (low) to +45% a year (high). Natera volume growth is in the ledger. I did not re-derive it.
- Genome-type mix of new starts rising from 5% to 10–25%.
- Blended Gb per new patient rises from about 36 Gb to about 45 Gb (10% mix) or about 72 Gb (25% mix).

| Scenario | Patient growth | Mix shift | Gb per patient growth | MRD Gb CAGR |
|---|---|---|---|---|
| Low | 25% | 5%→10% | about 8% | about 35% |
| High | 45% | 5%→25% | about 26% | about 83% |

**Read-through (OPINION):** MRD Gb could grow faster than management's mid-20s % volume target, driven by mix shift to WGS-designed tests, not by more draws per patient. But MRD is a small slice of clinical Gb, and I could not size it against CGP, NIPT or exome volumes. I cannot give a defensible total clinical Gb CAGR from this work. Two limits on the mix assumption:
- Natera's tumor sequencing can run on Illumina (Natera has a supply agreement through August 2033, E109), but Personalis is being bought by Tempus.
- Ultima-based Labcorp and Quest MRD, which E114 covers, would divert exactly the WGS-heavy Gb.

## Contradictions and stale data

- **Mislabelled CIRCULATE trial.** Search engines blended CIRCULATE-AIO ASCO 2026 data into "CIRCULATE-US". If any ledger entry cites those figures as US or Signatera evidence, correct it.
- E082's "<1 Gb per draw" is right for classic Signatera and low for Signatera Genome (2–3 Gb).
- The NeXT Personal validation (Oncotarget, Mar 2024) is old. The commercial assay may have changed.
- ACS counts are estimates, not observed counts.

## Gaps / what I could not find

- **Directly verified NCCN 2026 colon and rectal text** (nccn.org not reachable via search).
- **CMS ADLT list and Palmetto DEX Z-code entries for 2026.** The search returned only the CMS ADLT landing page.
- **Surveillance cadence from guidelines or trials.** DYNAMIC-III and CIRCULATE-AIO do not state one.
- **Plasma depth or Gb for NeXT Personal, RaDaR, clonoSEQ, Guardant Reveal and Labcorp/Ultima MRD.** The FDA PDF P260004B was binary and unreadable (saved locally at `C:\Users\palaz\.claude\projects\C--Users-palaz-OneDrive-Documents-ILMN-Claude-Code-Local-Folder--Build-sandbox\9b412fe9-77d3-4c73-914d-7672e6dd8094\tool-results\webfetch-1791737839444-t0w5vr.pdf`; unidentified device).
- **SEER stage splits and resection rates.**
- **A sourced MRD adoption curve and total clinical Gb baseline.** Without these, the clinical Gb CAGR in thesis question 2 remains unanswered.
