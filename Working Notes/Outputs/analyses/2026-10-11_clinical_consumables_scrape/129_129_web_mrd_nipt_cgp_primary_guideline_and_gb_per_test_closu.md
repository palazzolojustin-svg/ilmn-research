# Agent 129: 129-web-MRD-NIPT-CGP-primary-guideline-and-Gb-per-test-closure

*Model: sonnet. Run 2026-10-11 11:52:58. Cost $0.59 (API-equivalent).*

**Assignment:** Close open gaps 10 and 11, which are the main inputs that convert clinical test growth into Gb growth (thesis Q2). Use primary sources only, and label each point FACT, MGMT or OPINION with URL and date. (1) NCCN: check whether the 2026 colon/rectal/other ctDNA guidance went beyond 'prognostic only'. Try nccn.org and OncLive, ASCO Post and Healio coverage. (2) Pull primary abstracts or papers for IMvigor011 (serial ctDNA draw schedule, number of draws per patient-year, ESMO/NEJM), DYNAMIC-III, CIRCULATE-Japan (VEGA/ALTAIR), CIRCULATE-US, and GALAXY. Use PubMed, ClinicalTrials.gov, ASCO and ESMO abstract sites. Extract headline results and the tests-per-patient-year implied by each protocol. (3) Find Gb or sequencing-depth per test for tumor-informed MRD (Signatera, RaDaR, clonoSEQ, Haystack) vs tumor-naive and WGS-based MRD (Personalis NeXT Personal, Natera WGS, Labcorp/Ultima). Sources: FDA SSEDs, analytical-validation papers, bioRxiv/medRxiv, Natera/Guardant white papers. Report reads per sample and the Gb/test range, and show the arithmetic that turns test growth into Gb growth. (4) NIPT: find the latest ACOG, SMFM and ACMG statements (the ledger has only ACOG PB 226 from 2020), including any 2024-26 update on average-risk screening, microdeletions or single-gene NIPT. Add category patient counts and CAGRs from American Cancer Society, CDC or SEER for cancers eligible for MRD and CGP. (5) Check 2026 CMS ADLT, MolDX or Palmetto DEX actions for MRD, CGP and WGS (new Z-codes, LCD changes, ADLT rate resets). Quantify per-test coverage changes. Output a table of test-volume driver, tests per patient-year, Gb/test, and the resulting Gb multiplier.

## Key findings

1. **NCCN colon/rectal: no 2026 upgrade found.** Colon ctDNA language is still "prognostic, not predictive" (Feb 2025 update). This confirms E419 and adds no new colon evidence. The only 2026 NCCN change I found is bladder, which is already E418. [OnCLive/OncNursingNews 2025-02-22, https://www.onclive.com/view/nccn-updates-ctdna-stance-in-colon-rectal-and-mcc-guidelines] (FACT, secondary). I could not open nccn.org itself.
2. **IMvigor011 draw schedule (new quantification).** About 761 post-cystectomy patients had Signatera drawn every 6 weeks for up to 12 months. [Natera release 2025-08-18, https://www.natera.com/company/news/imvigor011-bladder-cancer-trial-achieves-positive-results-with-signatera-strongly-predicting-adjuvant-immunotherapy-benefit/; Targeted Oncology 2025-08-18] (FACT, company release plus trade press)
   - That implies up to ~8–9 draws per patient-year, including the post-op baseline (OPINION: 52/6 ≈ 8.7).
   - Results: median DFS 9.9 vs 4.8 months (HR 0.64); OS 32.8 vs 21.1 months (HR 0.59).
   - ctDNA-negative patients: 95% disease-free at 1 year and 88% at 2 years.
   - Real-world use will probably draw less often than the trial protocol.
3. **GALAXY/CIRCULATE-Japan: 4 draws per year.** Draws are preoperative, then every 3 months for 2 years. [ESMO Asia 2020 GALAXY TiP abstract, https://oncologypro.esmo.org/meeting-resources/esmo-asia-virtual-congress-2020/prospective-observational-study-monitoring-circulating-tumour-dna-in-resectable-colorectal-cancer-patients-undergoing-radical-surgery-galaxy-study] (FACT)
   - Updated Natera release: 2,625 patients, 24-month DFS 88.3% vs 89.9% for ctDNA-negative patients with vs without adjuvant chemo (p=0.156). [Natera ESMO 2023 release, https://s201.q4cdn.com/354493536/files/doc_news/Updated-Data-from-CIRCULATE-Japan-Presented-at-ESMO-2023-Reinforces-Signateras-Prognostic-and-Predictive-Value-in-Analysis-of-2500-Co-BL36W.pdf]
4. **DYNAMIC-III (ESMO Oct 2025, Nature Medicine 2025-10-20).** 1,002 patients with stage III colon cancer were randomized. [Queen's CCTG release, https://www.ctg.queensu.ca/cctg_media_releases/dynamic-iii-trial-results-ctdna-blood-test-powerful-tool-guide-treatment; ecancer 2025-10, https://ecancer.org/en/news/27168-esmo-2025-dna-shed-by-colon-cancers-may-help-personalise-postsurgical-treatment] (FACT)
   - 3-year RFS was 87% for ctDNA-negative vs 49% for ctDNA-positive patients.
   - De-escalation worked: oxaliplatin use fell from 88.6% to 34.8%.
   - Escalation did not work: HR 1.11 for RFS.
   - The test is a single post-op draw at 5–6 weeks. This is a low tests-per-patient driver (~1–2 in year 1), and the escalation failure weakens the "positive result → more therapy" pull.
5. **ALTAIR (CIRCULATE-Japan) missed its endpoint, published 2026-06-08 (Nature Medicine; NCC release 2026-06-12).** [https://www.ncc.go.jp/jp/information/pr_release/2026/0612/index.html] (FACT)
   - 243 patients with ctDNA positivity after surgery and no imaging recurrence.
   - DFS 9.3 vs 5.6 months, HR 0.79, p=0.107, "did not achieve statistical significance".
   - This is a negative read for "treat on ctDNA positivity alone" in colorectal, so colorectal MRD growth leans on prognosis and surveillance rather than treatment-driven demand. (OPINION)
6. **ACMG Dec 2025 prenatal cfDNA statement (new; the ledger only had ACOG PB 226 from 2020).** [ACMG, Prenatal-cfDNA-Screening-Final-122025, https://www.acmg.net/ACMG/UploadedPDFS/PDFDocuments/Prenatal-cfDNA-Screening-Final-122025.aspx; the page returned 403, so this is from the search summary] (FACT, secondary)
   - ACMG recommends cfDNA as first-line screening for all pregnant patients (singleton and twin) for trisomies 21, 18 and 13.
   - It also says to offer sex-chromosome aneuploidy screening.
   - That is stronger than ACOG's stance that conventional screening remains first line for average-risk patients. If ACOG and SMFM moved toward ACMG, average-risk NIPT would expand.
7. **ACOG and SMFM have not changed (the latest I could find is 2022–23).**
   - ACOG, SMFM and ISPD do not endorse routine microdeletion screening. ACMG supports 22q11.2 screening after counseling. [Santoli 2025 overview, https://starlegacyfoundation.org/wp-content/uploads/Santoli-2025-An-overview-of-current-prenatal-genetic-screening-and-diagnosis-guidelines.pdf]
   - Single-gene cfDNA is treated as investigational. [payer policy citing ACOG Practice Advisory Feb 2019, reaffirmed Oct 2022 and Sep 2023, https://cms.radmd.com/sites/default/files/2025-04/Prenatal%20Cell-free%20DNA%20Testing%20for%20Single-gene%20Disorders_2025.2.pdf]
   - Most prenatal volume is already shallow, so a guideline shift would add tests, not much Gb (~1–2 Gb/test per E082).
8. **Gb per test: new spec anchors.**
   - Signatera: a bespoke assay of 16 tumor-specific variants at ~100,000x average depth, LoD 0.01% VAF. [Natera white paper, https://www.natera.com/wp-content/uploads/2020/11/Oncology-Clinical-Seeing-beyond-the-limit-Detect-residual-disease-and-assess-treatment-response-SGN_AV_WP.pdf] (FACT)
   - Arithmetic (OPINION): 16 amplicons × ~100 bp × 100,000x ≈ 0.16 Gb of target bases. With duplicates and overhead this is sub-1 Gb per draw, which supports E082's "<1 Gb". The tumor/normal exome is a one-off of roughly 8–15 Gb, my estimate from E082's ~8 Gb exome.
   - NeXT Personal: WGS of tumor and normal to identify up to ~1,800 variants, then a personalized panel on plasma. Analytical LOD95 is 3.45 ppm. [Personalis release 2024-03-26, https://www.businesswire.com/news/home/20240326574824/en/Personalis-Announces-Publication-Validating-NeXT-Personal-Test-for-Ultra-sensitive-MRD-Detection-and-Cancer-Treatment-Response-Monitoring] (FACT)
   - The ≥250 Gb/sample, ~5,000x boosted-gene and ~2,000x exome-wide figures belong to NeXT Liquid Biopsy, not NeXT Personal. [Personalis spec via search summary] (FACT)
   - E082's "≥250" for NeXT Personal may therefore be a different product's spec (see Contradictions).
9. **MolDX MRD LCD L38814 was revised effective 2026-02-05.** The Noridian notice describes it only as consolidating JE and JF into one policy number. No coverage expansion is evident. [Noridian, https://med.noridianmedicare.com/web/jea/article-detail/-/view/10521/policy-revision-s-for-moldx-local-coverage-determinations-and-associated-billing-and-coding-articles-effective-february-5-2026] (FACT)
   - Other MolDX LCDs are effective 2026-08-10 and 2026-10-12. The snippets name hereditary thrombophilia and non-NGS targeted panels, which are not relevant to sequencing volume.

## Table: volume driver → Gb multiplier

All Gb/test and tests/year figures are estimates (OPINION) built on the cited specs, not reported. Where the multiplier for a driver rests on a one-off tumor exome, I amortize it over the draws.

| Driver | Tests per patient-year | Gb/test | Gb per patient-year | Notes |
|---|---|---|---|---|
| Signatera, trial-style serial (IMvigor011) | up to ~8–9 draws + 1 tumor exome | <1 per draw; ~8–15 one-off | ~15–25 | The draws cost almost no Gb; the exome dominates |
| Signatera, GALAXY-style | 4 | <1; one-off exome | ~12–19 | |
| DYNAMIC-III-style (single post-op draw) | ~1 | <1; one-off exome | ~9–16 | |
| WGS-based MRD (NeXT Personal) | not found (the Gb/draw figure is unconfirmed) | tumor/normal WGS of ~100+ Gb each (30x ≈ 90–120 Gb per E316/E082) | >200 (OPINION) | Multiplier vs Signatera is ≥10x per patient |
| NIPT | 1 | ~1–2 | ~1–2 | Guideline-driven, shallow |
| Tissue CGP / exome / 30x genome / liquid CGP | 1 | ~15 / ~8 / ~100–120 / ~120 (E082) | as left | Unchanged from E082 |

Arithmetic takeaway (OPINION): amplicon MRD growth of +45–60% in tests (E099) lifts Gb far less than test growth. Roughly 10–20% of the Gb per patient comes from the repeated draws; the one-off exome carries the rest. Only a shift to WGS-based MRD gives a real Gb step-up (≥10x per patient). So MRD volume growth supports >30% Gb growth only if the WGS share rises (see E083, E087).

## Contradictions and stale data

- **E082** gives "≥250 Gb" for NeXT Personal. The only primary spec I found with ≥250 Gb, ~5,000x and ~2,000x is NeXT Liquid Biopsy, a different product. I could not find NeXT Personal's plasma depth. Treat that E082 figure as unverified.
- **E419 (colon, "no 2026 upgrade found")** is still true as far as I could check, but it rests on 2025 sources. ALTAIR's miss (2026-06) and DYNAMIC-III's escalation failure (2025-10) both lower the odds of a near-term upgrade. (OPINION)
- **ACMG vs ACOG/SMFM:** the societies now disagree, with ACMG at "first-line for all" and ACOG at "conventional screening for most average-risk patients". I did not find any 2024–26 ACOG or SMFM update, so the ledger's ACOG PB 226 may be stale, but I could not verify that. The ACMG details come from a search summary because the page returned 403.

## Gaps / what I could not find

- **nccn.org:** not opened, so the colon verdict is secondary-sourced.
- **CIRCULATE-US:** nothing retrieved.
- **VEGA:** no results found. The design is observation vs CAPOX in ctDNA-negative patients, n=1,240 per the search summary.
- **DYNAMIC-III serial surveillance cadence:** not confirmed.
- **medRxiv NeXT Personal paper:** blocked (403), so no plasma depth.
- **Other Gb/test depths:** none found for RaDaR, clonoSEQ, Haystack, Natera WGS or Labcorp/Ultima, and no FDA SSEDs.
- **Cancer patient counts and CAGR (ACS, CDC, SEER):** not retrieved.
- **ADLT, Z-code and CGP/WGS coverage changes in 2026:** only the L38814 consolidation was found. No per-test coverage or ADLT rate changes beyond E089.
