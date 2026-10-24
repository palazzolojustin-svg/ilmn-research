# Agent 89: 94-web-GRAIL-Galleri-FDA-briefing-10K-Gb-per-test-and-MCED-Precure-volumes

*Model: sonnet. Run 2026-10-11 10:13:28. Cost $1.03 (API-equivalent).*

**Assignment:** Close open gap 1 (MCED sequencing depth and volume). (a) Decode the already-saved FDA briefing PDF (webfetch-1791731164668-sx6n5b.pdf, from fda.gov/media/195032/download; find it on disk under the tool-results or temp folder, or re-download it) with pdftotext. Extract the Galleri assay design (targeted methylation panel size, read depth, reads per sample, platform named), plus any test-volume and clinical-validation numbers. (b) Pull the GRAIL FY25 10-K and the Q2'26 10-Q from sec.gov and find the Illumina supply agreement text, the NovaSeq X migration, cost of revenue per test, and the number of tests sold. (c) Search for Exact Cancerguard, Guardant Shield MCD and the NHS-Galleri final results, plus the Precure and GUARDIAN/BabySeq genome counts and depth. Compute Gb per test and the implied Gb per year at 1M, 3M and 10M tests/yr, with each source cited. State clearly whether the earlier 5-15 Gb/test scenarios look too high. Do not repeat agents 84/85. Quantify everything. Label every point FACT, MGMT or OPINION.

## Key findings

Net: new evidence is thin but useful. I could not decode the FDA briefing PDF, because this session has no pdftotext and the Read tool needs poppler. The method details below come from the published CCGA paper and GRAIL's own statements.

1. **Galleri depth is public, from the CCGA paper.**
   - FACT: the targeted bisulfite panel covered "103 456 distinct regions (17.2 Mb) and 1 116 720 [CpGs]", with "150-bp paired-end sequencing on Illumina NovaSeq".
   - FACT: libraries were "sequenced to a median depth of 113 million fragments (median unique on-target depth: 139X)".
   - Source: Liu et al., Annals of Oncology 2020, PMC8274402, via Europe PMC full-text XML.
   - This confirms the ledger's "more than 100,000 regions" snippet and gives the depth the ledger lacked (gap 1).
2. **That depth is about 34 Gb per sample (OPINION, my calculation).** 113M fragments × 2 reads × 150 bp = 33.9 Gb raw. This is the CCGA-era design, with 150-bp reads assumed from the paper. The earlier 5–15 Gb/test scenarios are therefore too low for the legacy assay, not too high.
3. **The commercial assay is now much cheaper per sample.**
   - MGMT: GRAIL's Q4'24 call, per search summaries, said an enhanced Galleri with a "reduced panel size" and fully automated workflow gives "4×" sample throughput. The panel is cut "to the most informative regions", allowing four times the samples per flow cell, with no near-term capex (MarketBeat Q4'24 call, 2025-02-20; 503 on fetch, so the wording is from search summaries only).
   - OPINION: if the 4x all comes from fewer reads, the post-2024 figure is about 34 ÷ 4 ≈ 8.5 Gb per test. Part of the 4x may come from better flow-cell fill, so 8.5 Gb is a floor-to-midpoint, not a measurement.
   - So 5–15 Gb is a reasonable range for today's test. It is too high only if GRAIL cut reads by far more than 4x.
4. **Cost per test fits that picture.**
   - FACT: the FY25 10-K says cost of screening revenue rose $10.0M (16%), driven by a 36% rise in Galleri volume, "partially offset by a reduction in variable costs of Galleri testing performed on our automated platform."
   - FACT: more than 185,000 tests were sold in 2025, and more than 475,000 commercial tests cumulatively (GRAIL FY25 10-K, sec.gov/Archives/edgar/data/1699031/000162828026017319/gral-20251231.htm).
   - OPINION: $10.0M ÷ 16% implies a ~$62.5M base and ~$72.5M for FY25, or about $390 per test all-in. This matches E178 (~$382). If sequencing is a fraction of that, a large-scale assay like this is not a high-Gb workload.
   - The 10-K does not disclose platform, depth or flow-cell counts.
5. **New terms for the Illumina supply agreement, refining E279.**
   - FACT: the 10-K says the initial term "is scheduled to expire on February 28, 2027", with automatic two-year renewals unless either party gives notice at least 120 days before the end of the term.
   - FACT: the royalty is 9% in oncology, with anti-stacking down to a floor of 7%.
   - FACT: GRAIL can buy under Illumina's Open Offer pricing or its pre-acquisition terms.
   - The non-renewal notice window (about 31 Oct 2026) is a near-term watch item. I did not find these dates in the ledger, but I only grepped for them and did not check all 440+ lines.
6. **FDA panel outcome (Targeted Oncology, 2026-09-24, https://www.targetedonc.com/view/fda-panel-galleri-multi-cancer-early-detection-test).**
   - FACT: the 23 Sep 2026 panel voted 7-2-1 on benefit-risk, 6-4 on effectiveness and 10-0 on safety.
   - FACT: in PATHFINDER 2, specificity was 99.85%, PPV 77.0%, sensitivity 35.0% (12-month), and the number needed to screen was 202.
   - FACT: in NHS-Galleri, specificity was 99.74%, PPV 66.2% and sensitivity 31.6%.
   - FACT: 73% of those with a cancer signal underwent invasive procedures.
   - FACT: GRAIL submitted its PMA on 29 Jan 2026 (search summary).
   - This is not in the ledger as far as I saw. A positive FDA outcome would strengthen the case for volume growth, but E320 (NHS-Galleri missed its primary endpoint) remains.

## Gb per test and implied Gb per year (OPINION, calculated)

These are my calculations, not company figures.

| Scenario | Gb per test | 1M tests/yr | 3M tests/yr | 10M tests/yr |
|---|---|---|---|---|
| Legacy CCGA design (113M fragments × 300 bp) | ~34 | 34M Gb | 102M Gb | 340M Gb |
| Post-"4x" enhanced assay (34 ÷ 4) | ~8.5 | 8.5M Gb | 25.5M Gb | 85M Gb |
| Earlier ledger scenario (5–15 Gb) | 5–15 | 5–15M Gb | 15–45M Gb | 50–150M Gb |

- Current scale: 185K tests × 8.5 Gb ≈ 1.6M Gb for FY25 (about 6.3M Gb at 34 Gb per test).
- For scale, a 25B flow cell yields roughly 8,000 Gb per run (my assumption, not checked against the corpus). At 8.5 Gb per test, 1M tests need about 1,000 flow cells a year.
- Verdict: MCED is a modest Gb driver at today's volumes. It only matters at 3–10M tests a year, and the 4x efficiency gain cuts that by three-quarters.
- This supports E078: management says MCED is not visible in the numbers today.

## Peer MCED tests

- **Exact Cancerguard.** FACT: it combines methylation and protein markers. The methylation is detected by real-time PCR after bisulfite conversion, with a mutation reflex (search summary of the Exact Sciences test info page). That is a low-Gb workload. Exact no longer reports standalone (ledger correction to E177).
- **Guardant Shield MCD.** FACT: 98.5% specificity, 60% overall sensitivity and 74% across six aggressive cancers (BusinessWire, 2025-04-29). I found no depth figure. Search summaries say Guardant completed its NovaSeq X transition, but that is unverified.
- **GUARDIAN.** FACT: it aims to enroll 100,000 newborns for WGS covering 255 conditions, with 4,000 enrolled in the first report (BusinessWire, 2024-10-24). No depth was found in the results. A standard 30x genome is about 100 Gb raw (OPINION).
- **Precure.** FACT: 1M biospecimens on UG200 at up to 60,000 genomes per year per system, with Helix as the lab (HPCwire/Mayo, 2026-09-22). No depth was disclosed. The UG200 choice means this volume does not go to Illumina (E128).

## Contradictions and stale data

- The ledger scenarios of 5–15 Gb per test are too low for the legacy assay (about 34 Gb) but plausible for the enhanced assay (about 8.5 Gb).
- The "4x" claim comes from search summaries of the Q4'24 call, and the date is inferred. The Q4'24 call (20 Feb 2025) described a December rollout, so this is most likely Dec 2024. The 10-K also says the "late 2024 version" was rolled out.
- The FDA submission uses an "updated version" bridged to the trial version. Its panel and depth could differ from both figures above.

## Gaps / what I could not find

- I could not decode the FDA PDFs (media/195032, 194909, 195033). They are saved as binary in the tool-results folder, and WebFetch returned unreadable content. Someone with pdftotext should search them for "reads", "flow cell", "panel", "NovaSeq" and "CpG".
- The 10-K excerpts did not show the platform, the NovaSeq X migration or the supply-agreement flow-cell terms. WebFetch summarized rather than quoting the full filing, so these may exist unseen.
- I did not open the Q2'26 10-Q.
- The Annals of Oncology 2021 paper (Klein) is not in PMC and the publisher blocked the fetch.
- GenomeWeb returned 403 and MarketBeat returned 503.
- I found no figures for Saudi, Japan, Australia or BabySeq depth or counts, and no Precure genome depth.

Sources: [Europe PMC full text of Liu 2020](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8274402/fullTextXML), [GRAIL FY25 10-K](https://www.sec.gov/Archives/edgar/data/1699031/000162828026017319/gral-20251231.htm), [Targeted Oncology, 2026-09-24](https://www.targetedonc.com/view/fda-panel-galleri-multi-cancer-early-detection-test), [GRAIL Q4'24 call (MarketBeat)](https://www.marketbeat.com/earnings/reports/2025-2-20-grail-inc-stock), [BusinessWire GUARDIAN](https://www.businesswire.com/news/home/20241024902651/en/Groundbreaking-GUARDIAN-Study-Shows-Benefits-of-Adding-Genome-Sequencing-to-Newborn-Screening-Augments-and-Improves-Standard-Newborn-Screening), [BusinessWire Shield MCD](https://www.businesswire.com/news/home/20250429167731/en/guardant-health-presents-data-demonstrating-strong-performance-of-shield-multi-cancer-detection-test-across-10-tumor-types), [HPCwire Precure](https://www.hpcwire.com/bigdatawire/this-just-in/ultima-genomics-selected-for-mayo-clinic-led-million-biospecimen-initiative/)
