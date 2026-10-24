# Agent 138: B-web-clinical-Gb-baseline-and-MRD-CGP-volume-bottom-up

*Model: sonnet. Run 2026-10-11 12:03:50. Cost $0.82 (API-equivalent).*

**Assignment:** Close open gaps 3 and 9 (thesis Q2) by building a SOURCED total clinical Gb baseline. Per-test sequencing intensity and volume are the targets, not test counts. Use primary documents. Quantify per company: tests or samples per quarter (Q2'26 and Q2'25), Gb per test with the source of that estimate, implied Gb per year, and growth. Natera: Signatera tumor-informed WES or WGS depth, plasma depth (reads or 'x' coverage in the Signatera Genome and Signatera classic validation papers, bioRxiv/medRxiv, the FDA SSED if any, and the Natera 10-K, S-3 or investor deck); Panorama read count; Prospera and Horizon. Guardant: Guardant360 Liquid, Reveal and Shield read depth from the SSEDs (P200010, P230001) and its technical papers; the 10-K Item 1 on 'platform' and 'sequencing capacity'. Tempus xT/xF/xM. Caris, which sequences WES/WTS on each tumor (the Caris S-1 and 10-K state tests and the sequencing platform). Foundation Medicine FoundationOne CDx and Liquid CDx (SSEDs P170019 and P190032 list depth of about 500x and 5,000x). GeneDx (exome versus genome counts, with the Q2'26 release and 10-Q). Adaptive clonoSEQ (the 10-K gives depth or reads per sample). Personalis NeXT Personal depth (the 10-K, S-4 and Tempus merger documents). BillionToOne UNITY (the S-1 and 10-Q). For each lab, read the Illumina sequencer, flow-cell type and reagent-spend commitment from the 10-K or 10-Q (purchase obligations; cost of revenue per test), and compute the implied Illumina consumables dollars per test. Then sum to an implied top-10 clinical-lab Gb per year and a share of Illumina's clinical consumables (roughly $1.9B at 65% of FY25's $2,939M). Compare with Illumina's 'Gb output grows over 30%' claim. Cite the filing, section and date. Flag every Gb/test figure that is your own estimate. Deliver a table with columns: lab, Q2'26 tests, Gb/test, source, implied annual Gb, y/y growth.

## Key findings

**Verdict: partial.** I found new Q2'26 volumes for five labs that the ledger lacks. I could not get a primary-source Gb per test for any of them, because every FDA SSED and Natera/Guardant PDF I opened came back as unreadable binary. The Gb figures below are my own estimates and are not a sourced baseline. Gap 3 stays mostly open. Gap 9 is only partly closed: the volumes are sourced, the intensities are not.

- **FACT, Natera Q2'26:** about 1,043,900 tests processed, versus about 853,100 in Q2'25 (+22%). Clinical MRD was 283,000 units, up about 56% y/y and +34,000 vs Q1. Revenue was $752.8M (+37.7%). [Natera Q2'26 release, 2026-08-06, https://www.businesswire.com/news/home/20260806933033/en/ ; https://www.sec.gov/Archives/edgar/data/0001604821/000160482126000015/ntra-20260630xex991.htm]
  - Total tests grew 22% while MRD grew 56%. Non-MRD volume (Panorama, Horizon, Prospera and others, about 761K tests) grew only about 11% (my arithmetic).
  - Because MRD volume is a growing share of the mix, Natera's Gb growth depends on the mix of classic and Genome tests (E082, E432 in the ledger).
- **FACT, Guardant Q2'26:** oncology test volume +63% y/y. Reveal volume more than doubled, Guardant360 Liquid grew over 30%, and Guardant360 Tissue accelerated. Shield was about 66,000 tests vs about 16,000 in Q2'25 (about 4x), with screening revenue of $52.9M. [Guardant Q2'26 release/call, 2026-07-30, https://www.sec.gov/Archives/edgar/data/0001576280/000157628026000036/gh-06302026xexhibit991.htm ; https://www.marketbeat.com/instant-alerts/guardant-health-q2-earnings-call-highlights-2026-07-30/]
  - Shield is the largest new volume source. Its read depth is not in anything I could open.
  - Guardant says the NovaSeq X transition for its liquid portfolio is complete (call summary, not verified in a transcript). That is a read-through for the X conversion.
- **FACT, Caris Q2'26:** about 59,200 clinical cases (+18% vs 52,800). That comprised over 114,000 whole-exome (WES) and whole-transcriptome (WTS) tests and over 345,000 total oncology tests. Revenue was $263.7M (+45%). [Caris Q2'26 release, https://www.carislifesciences.com/about/news-and-media/caris-life-sciences-reports-second-quarter-2026-financial-results-and-increases-2026-revenue-guidance/]
  - Cases grew 18% while revenue grew 45%, so revenue per case is rising.
  - Caris sequences every tumor on WES plus WTS, so this is the only lab in the set with a hard, high-intensity Gb count.
- **FACT, GeneDx Q2'26:** 30,785 exome and genome tests (49% of results), versus about 23,246 (40%) in Q2'25, which is +32%. [GeneDx Q2'26 10-Q, https://www.sec.gov/Archives/edgar/data/0001818331/000162828026051878/wgs-20260630.htm]
  - The 10-Q does not split exome from genome in what I could retrieve. I also found no mention of NovaSeq or Illumina in the part I could see.
  - The 10-Q says "One supplier accounted for approximately 14% and 20% of spend" in Q2'26 and Q2'25, for reagents, equipment and supplies. The supplier is not named. The fall from 20% to 14% is consistent with falling Illumina $/Gb, but that is my inference.
  - Purchase commitments are $41.5M through 2030 (2026 remainder $9.4M, 2027 $16.3M). They are not attributed to a vendor.
  - Cost of services was $36.2M, or about $323 per diagnostic test on $111.9M of diagnostic revenue (that division is my calculation, from the 10-Q figures).
- **FACT, Adaptive clonoSEQ Q2'26:** 36,111 tests delivered (+43% y/y), ASP $1,382 (+7% y/y, +11% q/q). [Adaptive Q2'26 release, 2026-07-29, https://www.biospace.com/press-releases/adaptive-biotechnologies-reports-second-quarter-2026-financial-results ; https://www.marketbeat.com/instant-alerts/adaptive-biotechnologies-q2-earnings-call-highlights-2026-07-29/]
  - clonoSEQ is a low-Gb test per sample, so it is volume-rich but Gb-light.
- **FACT, Tempus Q2'26:** MRD volume was 9,000 tests, up from 6,500 in Q1. Oncology volume grew 31% y/y and hereditary revenue grew 5%. Revenue was $382.5M (+22%). [Tempus Q2'26 release, 2026-07-30, https://www.businesswire.com/news/home/20260730328545/en/Tempus-Reports-Second-Quarter-2026-Results]
  - Hereditary revenue at +5% is a sign that germline volume is not a major Gb driver.
- **FACT, depth specs that I did confirm (secondary pages only):**
  - Guardant360 sequences "to an average depth of coverage of greater than 10,000X" (Guardant spec sheet, search snippet).
  - Standard Signatera reaches "100,000X average depth of coverage of each target" (Natera 2025-04-24 release).
  - Personalis NeXT Personal uses tumor/normal whole-genome sequencing (WGS) to select up to about 1,800 variants. It reports a 1.67 ppm detection threshold and a 3.45 ppm limit of detection (LOD95) (Oncotarget/Personalis, medRxiv 2024).
  - None of these gives a Gb per sample.

## Table (Q2'26 volumes sourced; Gb per test is my estimate unless noted)

| Lab | Q2'26 tests | y/y | Gb/test | Source of Gb/test | Implied Gb/quarter |
|---|---|---|---|---|---|
| Natera, all tests | 1,043,900 | +22% | not available | none | not computable |
| Natera Signatera plasma draws | 283,000 | +56% | ~0.2 (classic) | ledger E082/E596; Genome ~2–3 | ~60K Gb if all classic; a Genome share raises it about 10x per draw |
| Guardant, Shield | ~66,000 | ~4x | unknown | none | not computable |
| Caris, WES/WTS tests | 114,000 | n/a | ~5–10 | **my estimate** (50 Mb exome at ~100–150x, plus RNA) | ~0.6–1.1M Gb |
| GeneDx exome and genome | 30,785 | +32% | ~8 exome, ~100 genome | ledger E082 (OPINION) | exome-only ~0.25M Gb, genome-only ~3M Gb; the real figure depends on a split I could not find |
| Adaptive clonoSEQ | 36,111 | +43% | not available | none | not computable |
| Tempus MRD | 9,000 | +38% q/q | unknown | none | not computable |

## Analysis (OPINION)

- **Concentration looks small.** If Illumina clinical consumables were about $1.9B/yr at an assumed $5–8/Gb, that would be roughly 240–380M Gb/yr. The labs I could size (Caris, GeneDx, Natera MRD) add up to roughly 10–15M Gb/yr on the estimates above. That is a few percent of the total. The $/Gb and the clinical dollar base are the ledger's assumptions and my inference, not sourced.
- **Implication.** The named top labs probably do not explain most clinical Gb. The bulk may sit in NIPT, other CGP, and non-US or lab-developed-test (LDT) volume. A top-10 share cannot be stated from this work.
- **Possible overstatement in the ledger (E082).** It gives "liquid CGP ~120 Gb". At >10,000x unique coverage of a panel of roughly 0.7–2 Mb, unique-molecule Gb is about 7–20 Gb. Even allowing 3–5x for duplicates and overhead, 120 Gb looks high. This needs a read-count source before it is used.
- **Test growth versus Gb growth.** MRD test growth of 43–56% (Natera, Adaptive) is the fastest in the set. It is a low-Gb test unless the mix shifts to Genome/WGS-based MRD. This supports the existing ledger correction at lines 586 and 596.

## Contradictions and stale data

- Caris reports cases (+18%) and tests (345K) separately. Test counts and case counts must not be mixed when sizing Gb.
- E082 says exome is about 8 Gb and tissue CGP about 15 Gb. Caris WES plus WTS at about 5–10 Gb combined is lower than that. This is unresolved.
- The Adaptive and Tempus figures come from search summaries and a marketbeat/biospace pass. I did not open the filings.

## Gaps / what I could not find

- **Unreadable PDFs.** WebFetch could not read these: FDA SSEDs P260004D (Signatera) and P200010S026B (Guardant360), the Guardant360 Liquid CDx technical document LBL-000496, and the Natera Signatera white paper. All of them, plus P250027B/D and the Guardant spec sheets, need a local pdftotext or Python run.
- **Not reached.** Foundation Medicine SSEDs (P170019, P190032), the BillionToOne S-1/10-Q, the Personalis 10-K or Tempus merger documents, and the Natera 10-K purchase obligations were not reached.
- **No Q2'25 comparatives.** I did not find Q2'25 figures for Caris, Guardant360 or Tempus MRD.
- **Illumina dollars per test** cannot be computed for any lab. No filing I could read states per-lab Illumina spend (GeneDx's unnamed 14% supplier is the nearest).
- **Illumina's ">30% Gb growth" comparison** is not testable from this data. The labs I sized grew 22–63% in tests, but I have no Gb series.
