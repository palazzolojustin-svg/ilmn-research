# Agent 98: 103-web-GRAIL-Galleri-FDA-briefing-PDFs-decode-and-GRAIL-Illumina-supply-term

*Model: sonnet. Run 2026-10-11 10:21:43. Cost $0.58 (API-equivalent).*

**Assignment:** Close open gap 1, since MCED is the largest speculative Gb driver. (1) Download the FDA Galleri advisory/briefing PDFs (fda.gov/media/195032, 194909, 195033, or search 'Galleri FDA advisory committee briefing document 2026 site:fda.gov'). Try Bash/PowerShell with curl.exe, then pdftotext -layout or Python pypdf/PyMuPDF. If the FDA site is blocked, try archive.org copies, GRAIL's investor site (grail.com/investors), the PMA submission summary, or trade-press summaries (STAT, Fierce, Endpoints, GenomeWeb). Extract: the test's read depth or sequencing description (reads per sample, flow cell type, panel size, CpG count, NovaSeq 6000 or X use), samples per flow cell or lane, the PATHFINDER 2 and NHS-Galleri numbers, the FDA decision timeline and the advisory vote. (2) From the GRAIL FY25 10-K and Q2'26 10-Q/call (sec.gov, CIK for GRAIL, gral-20251231): the Illumina supply agreement term, notice and renewal dates, minimum purchases and pricing mechanics (Ex. 10.x), cost per test, tests sold and guided volumes for 2026, and plans for the NovaSeq X or other platforms. (3) Convert to a Gb-per-test and Gb-per-year estimate for GRAIL at 1M, 3M and 10M tests per year, and state what share of Illumina's ~$3.1B sequencing consumables that would be at current $/Gb. Cite page numbers or line quotes. Do not repeat agents 89 and 93 conclusions unless you decode the actual PDFs; if the PDFs again fail to open, say so plainly and use the 10-K and 10-Q text.

## Key findings

**Status: the FDA PDFs could not be decoded.** Bash and PowerShell are disabled this session, and `pdftoppm` is not installed. WebFetch on `fda.gov/media/195032/download` returned a 281 KB binary, which is saved at `C:\Users\palaz\.claude\projects\...\tool-results\webfetch-1791732016812-s6dcuj.pdf`. The summariser could not read it, so I have no page-cited sequencing details. The 10-K text fetch and Ex. 10.16 were also redacted or truncated. Result: partly new evidence on the panel and PATHFINDER 2/NHS-Galleri numbers, and nothing new on depth, flow cell, or the supply term.

1. **FDA panel vote on 23 Sep 2026. FACT.** The Molecular and Clinical Genetics Devices Panel voted:
   - Benefit-risk: 7 yes, 2 no, 1 abstain.
   - Safety: 10-0.
   - Effectiveness: 6-4.

   This was the first advisory review of an MCED (multi-cancer early detection) PMA (premarket approval application). [TargetedOnc, 2026-09-24, https://www.targetedonc.com/view/fda-panel-galleri-multi-cancer-early-detection-test]. [Search summary of OncNursingNews, 2026-09-27, and GRAIL release, https://grail.com/?p=28484]. I could not confirm the vote tally against GRAIL's own release text. A pre-panel search summary was consistent with it. The effectiveness vote was close, and MDDI's headline called it "narrowly" backed "despite effectiveness concerns" (https://www.mddionline.com/ivd/fda-advisory-panel-narrowly-backs-multi-cancer-blood-test-despite-effectiveness-concerns). That page returned 403, so I have only the headline.

2. **FDA decision timing. MGMT.** GRAIL says the PMA remains under "iterative review", with a decision "still expected in early 2027" (search summary of GRAIL's panel-announcement release, https://grail.com/press-releases/grail-announces-fda-advisory-committee-meeting-to-review-premarket-approval-application-for-the-galleri-multi-cancer-early-detection-test/). A Q1 2026 PMA submission was previously flagged by Fierce (https://www.fiercebiotech.com/medtech/grails-third-quarter-sales-jump-medtech-eyes-q1-fda-galleri-pma-submission). Approval would not produce Gb volume before 2027.

3. **PATHFINDER 2 (303 cancer cases). FACT, as reported by TargetedOnc, 2026-09-24:**

   | Metric | Value |
   |---|---|
   | Sensitivity | 35.0% |
   | Specificity | 99.85% |
   | PPV | 77.0% |
   | NPV | 99.07% |
   | False-positive rate | 0.15% |
   | Number needed to screen | 202 |

   72.9% of positive results led to invasive procedures. Among positives with no cancer found, 47.8% still had a diagnostic workup.

4. **NHS-Galleri (820 cancer cases). FACT, TargetedOnc:**

   | Metric | Value |
   |---|---|
   | Sensitivity | 31.6% |
   | Specificity | 99.74% |
   | PPV | 66.2% |
   | NPV | 98.89% |
   | False-positive rate | 0.26% |
   | Number needed to screen | 196 |

   Sensitivity by cancer type was:
   - Lung 63.8%, colorectal 53.3%, breast 19.1%, prostate 10.7%.
   - Liver 80.0%, ovarian 75.0%, esophageal 65.4%.

   This adds detail to E320 (the primary-endpoint miss). Sensitivity of about a third means most cancers are missed. That caps the clinical case for annual mass screening and so the Gb ramp.

5. **Pricing and technical description. FACT.** Galleri's list price is $949, with a $799-or-less self-pay price through many providers. The assay is a targeted bisulfite methylation panel covering over 100,000 regions and more than 1,000,000 CpGs [galleri.com cost page and FAQs, via search summaries]. No source gave reads per sample, flow cell, or NovaSeq 6000 versus X. This keeps the 34 Gb legacy and about 8.5 Gb possible figures in E178 and its correction unresolved.

6. **Supply agreement mechanics. FACT. Refines E279.**
   - Ex. 10.16 (S-1 amended agreement, https://www.sec.gov/Archives/edgar/data/1699031/000162827920000227/ex1016-grailsx1xamende.htm) is redacted on term lengths (§13.1) and notice periods. Only the structure is visible.
   - §3.1(a) prices at "Illumina's then current List Price… subject to the discount table set forth in Exhibit A".
   - §3.4(a) makes the forecast "a binding commitment… to take receipt of and pay for" product. The binding portion is short-dated, not a multi-year take-or-pay. This is consistent with E279's "no take-or-pay".
   - The royalty is "high single-digit… in perpetuity", per the 10-K text. The suspension was extended by the 21 Jun 2024 amendment to the earlier of 2.5 years or a change of control. That implies roughly Dec 2026, and the older text says "until December 24, 2026". Royalties on GRAIL's net sales to Illumina therefore resume around year-end 2026, or earlier on a change of control. This is a GRAIL margin point, not an Illumina consumables one. It was a search summary, not a verified 10-K quote. I did not confirm the date in the 10-K.
   - GRAIL may buy under the Open Offer or Grandfathered Pricing, so the $/Gb GRAIL pays is unlikely to be Illumina's average.

7. **The "initial term ends 28 Feb 2027, 120-day notice" claim in open gap 1 stays unverified.** The 10-K fetch returned nothing on term, and the exhibit is redacted. Do not rely on it.

## Gb-per-test scenarios (OPINION; illustrative)

The inputs are unverified, so these are bracketing arithmetic. The depth figures are the legacy 34 Gb CCGA design (E178 correction) and a possible 8.5 Gb after the "4x" throughput change. The $/Gb figures of $3 to $6 are my assumption, not a sourced Illumina price. I also assume one sample per run's worth of Gb with no failure or re-run overhead.

| Tests per year | Gb per year at 8.5 Gb/test | Gb per year at 34 Gb/test |
|---|---|---|
| 1M | 8.5M | 34M |
| 3M | 25.5M | 102M |
| 10M | 85M | 340M |

Share of Illumina's about $3.1B sequencing consumables:

| Tests per year | At 8.5 Gb/test, $3/Gb | At 8.5 Gb/test, $6/Gb | At 34 Gb/test, $3/Gb | At 34 Gb/test, $6/Gb |
|---|---|---|---|---|
| 1M | $26M, 0.8% | $51M, 1.6% | $102M, 3.3% | $204M, 6.6% |
| 3M | $77M, 2.5% | $153M, 4.9% | $306M, 9.9% | $612M, 19.7% |
| 10M | $255M, 8.2% | $510M, 16.5% | $1,020M, 33% | $2,040M, 66% |

- **Calibration.** GRAIL ran about 61K screening tests in Q2'26, so roughly 0.25M tests a year (E178). At 1M tests a year, Galleri is a low-single-digit percentage of Illumina consumables, even at the legacy depth. Only 10M tests or more at legacy depth is material.
- **Upside gating.** Sensitivity of about a third, a split panel on effectiveness, and a missed NHS-Galleri primary endpoint (E320) mean the 3M and 10M scenarios depend on FDA approval, payer coverage, and screening guidelines. None of these is likely before 2027.
- **Price pressure.** GRAIL's own COGS is about $382 per test (E178), against a $949 list price. GRAIL has an incentive to push down sequencing cost per test through depth cuts and cheaper platforms. A fall in Gb per test from depth cuts would offset volume growth.

## Contradictions and stale data

- Open gap 1 says a search summary gave an initial term to 28 Feb 2027 with 120-day notice. The 10-K fetch says undisclosed, and Ex. 10.16 is redacted. Treat the date as unproven.
- GRAIL guided a decision in "early 2027". Panel-day press framed the effectiveness vote as narrow (6-4). Trade-press numbers rest on the FDA briefing, which I could not open. Treat PPV and sensitivity as secondary-source figures.

## Gaps / what I could not find

- The FDA briefing PDFs (195032, 194909, 195033) are still undecoded. Only 195032 was fetched, as unreadable binary. A Bash-enabled session needs `pdftotext -layout` on the saved file. The page-cited items are still missing: reads per sample, flow cell, samples per lane, and any NovaSeq 6000 versus X statement.
- 10-K and 10-Q text for the supply term, cost per test and the 2026 volume guide were not retrievable. WebFetch returned only excerpts. The MarketBeat call-highlights page returned unrelated content.
- No GRAIL statement on NovaSeq X adoption or an alternative platform.
