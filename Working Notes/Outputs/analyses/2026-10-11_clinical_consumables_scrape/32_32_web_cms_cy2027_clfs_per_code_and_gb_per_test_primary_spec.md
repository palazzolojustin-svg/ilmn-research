# Agent 32: 32-web-CMS-CY2027-CLFS-per-code-and-Gb-per-test-primary-specs

*Model: sonnet. Run 2026-10-11 02:42:57. Cost $1.09 (API-equivalent).*

**Assignment:** Goal: close open gaps 9, 11 and 12 with government data and primary technical specs, to turn the test-volume growth and reimbursement picture into Gb numbers.
(1) CMS CY2027 Clinical Laboratory Fee Schedule: download the preliminary rate file and the ADLT and PLA files from cms.gov (Clinical Lab Fee Schedule page, Annual Public Meeting and preliminary determinations, Sept 2026) and the PAMA data-reporting results. Extract preliminary CY2027 rates against CY2026 for the codes that drive sequencing: 81415, 81416, 81417, 81425, 81426, 81427 (exome and genome), 81479, 81455, 81445, 81450, 0340U (Signatera), 0239U, 0326U, 81420/81507/81420 (NIPT), 0414U and the MRD PLA codes. Also check the CMS 15% cap mechanics, the ADLT carve-outs, and the Nov 2026 final timing. Note the Medicare share of revenue for Natera, Guardant, Tempus, Caris, GeneDx and Exact, and compute the revenue-at-risk per company if rates fall by the preliminary amounts. Drop the old '$597 vs $1,759.60-$4,375' snippet. Also check the MolDX and Palmetto LCDs, the NCD 90.2 changes, and payer policies on MRD and WGS from Aug to Oct 2026.
(2) Gb per test from primary technical sources: FDA 510(k), PMA and De Novo summaries and package inserts (TSO Comprehensive, Guardant360 CDx, Guardant Shield, FoundationOne CDx and Liquid CDx, Illumina TSO 500 ctDNA, Signatera, Panorama, Haystack) and peer-reviewed analytical-validation papers or bioRxiv. These give reads or depth per sample, panel size and samples per flow cell. Calculate Gb per test for each, and the flow cells per 1,000 tests on a NovaSeq X 10B or 25B. Also gather published lab statements on samples per flow cell for NIPT, exome (about 8 Gb) and genome (more than 100 Gb), and Illumina's own run-spec table (output per flow cell, reads, Gb).
(3) Test the equal-price-ratio assumption in the ledger: use customer COGS per test (Natera, Guardant Shield about $410, GeneDx, BillionToOne) to estimate what share of the COGS is sequencing consumables. Estimate the Gb-per-test share against the per-test price that Illumina would implicitly receive.
Return tables with exact numbers, file names and dates, and URLs. Label FACT, MGMT or OPINION. Flag anything inconsistent with the ledger's Gb-per-test table (NIPT 1-2, exome 8, tissue CGP 15, liquid CGP 120, genome 100-120+). Hard stop at 20 minutes.

## Key findings

Most of what I could reach turned out to be already in the ledger. I found four useful items, plus one dated claim that needs a correction.

1. **TSO 500 ctDNA's per-sample read requirement confirms the ledger's ~120 Gb for liquid CGP (E082).** Illumina's knowledge-base page (illumina.com, fetched 2026-10-11) says ~800M paired-end reads and 35,000x raw coverage per sample before read collapsing. Pooling is 4 libraries on a NovaSeq 6000 S1, 8 on S2 and 24 on S4. Those counts multiply back to flow-cell capacity (24 × 800M = 19.2B, against ~20B reads on an S4). So 800M is a per-sample figure. A search summary I got first mistook it for a per-flow-cell figure. At 151 bp reads, 800M reads is ~121 Gb per sample (OPINION, my calculation; read length is my assumption). FACT for the reads and pooling; the Gb conversion is my arithmetic.
2. **Tissue TSO 500 is ~15 Gb per sample, matching the ledger.** The search summary quotes 192 samples per S4 at 100M reads and 3,500x. That is ~15 Gb at 151 bp, matching "tissue CGP 15" (E082). Source: Illumina TSO 500 pages via search summary, not opened directly. FACT for the quoted specs; the Gb figure is my arithmetic.
3. **CY2027 preliminary CLFS category cuts are confirmed from the CMS fact sheet (2026-09-21).** Genomic sequencing is −23%, molecular pathology −22%, microbiology and immunology −19.3%, chemistry −16%, and PLA −2.4%. The 15% annual per-test cap applies in 2027–2029. Final rates are due in November 2026, after a 30-day comment period. This agrees with E097. FACT (cms.gov).
4. **The ACLA says 775 tests would hit the full 15% cut in 2027, with further cuts in 2028–29.** This is new. FACT, as reported by HFMA (https://www.hfma.org/payment-reimbursement-and-managed-care/2027-medicare-lab-fee-schedule-cuts/). Together with the −23% category average, it implies most sequencing codes are capped at −15% in 2027 and then cut further.
5. **Code-level preliminary rates exist only from one vendor blog, so treat them as unverified.** See the table below. The most relevant for Illumina:
   - 0543U (TruSight Oncology) goes from $2,989 to $1,337 (−55%), which is an Illumina-owned test.
   - 81455 (51+ gene tumor panel) is nearly flat (−2%).
   - 0364U (clonoSEQ) goes from $2,007 to $337 (−83%). That looks implausible. It may be a data artifact or a different code, so do not use it without checking the CMS file.
6. **The 15% cap would limit the near-term 0543U cut.** If the cap binds, 0543U would be paid ~$2,541 in 2027 (0.85 × $2,989), not $1,337 (OPINION, my calculation from the blog's numbers).
7. **No per-company Medicare revenue share is available.** Natera's FY25 10-K does not give a Medicare percentage. It says Medicare matters "as a large proportion of these patients" in oncology and organ health are covered (search summary of sec.gov). Guardant says Medicare was ">10% of total revenue" in each of 2023–25 (search summary of the FY25 10-K). I did not open the Tempus, Caris, GeneDx or Exact filings. The revenue-at-risk calculation therefore cannot be done from what I have.

## CMS CY2027 preliminary CLFS

Dollar rates for the specific codes you listed (81415–81427, 81479, 81445, 81450, 0340U, 0239U, 0326U, NIPT, 0414U) are not in any page I could fetch. The CMS fact sheet states that code-level data exist only in the downloadable files, for codes reported by 10 or more entities. Those files are on the CMS Clinical Lab Fee Schedule page and I could not retrieve them.

| Code | Test | CY2026 | CY2027 prelim | Change | Source and reliability |
|---|---|---|---|---|---|
| 81455 | 51+ gene tumor panel | $2,919 | $2,861 | −2% | screenmygene.com, vendor blog |
| 0543U | TruSight Oncology | $2,989 | $1,337 | −55% | same |
| 0364U | clonoSEQ MRD | $2,007 | $337 | −83% | same; suspect |
| 0211U | MI Cancer Seek | $8,455 | $8,455 | 0% | same |
| 0485U | Caris liquid biopsy | — | $5,250 | new (+44% per source) | same |

The blog's own framing is that code-level swings "hide enormous code-by-code variations," with the cap phasing most reductions through 2028. URL: https://www.screenmygene.com/resources/clfs-2027-preliminary-rates-molecular-pathology (OPINION and unverified).

Other CMS context:
- HFMA and Becker's say 1,171 of ~1,500 codes fall, and Medicare pays ~16% above commercial rates on average. Roughly 6,400 labs reported. Savings figures differ by source, and the fact sheet gives none.
- Most PLA codes would not hit the cap.
- The ADLT treatment is not specified in any source I could read.

## Gb per test from primary specs

All conversions assume 2×151 bp reads, and the read length is my assumption. NovaSeq X reads per flow cell come from Illumina's NovaSeq X specifications page (illumina.com/systems/sequencing-platforms/novaseq-x-plus/specifications.html): 10B gives 20–26B paired-end reads and 25B gives 52–70B.

| Assay | Reads per sample | Gb per sample | Samples on X 10B | Samples on X 25B | Flow cells per 1,000 tests, 10B | Flow cells per 1,000 tests, 25B |
|---|---|---|---|---|---|---|
| TSO 500 ctDNA | ~800M | ~121 | ~25–32 | ~65–87 | ~31–40 | ~11–15 |
| TSO 500 tissue | ~100M | ~15 | ~200–260 | ~520–700 | ~3.8–5 | ~1.4–1.9 |

I derived the sample counts by dividing flow-cell reads by reads per sample. They are my calculations. They ignore dead capacity, failed samples and controls, so real counts would be somewhat lower.

Two further reference points:
- The 25B 2×150 output is ~8–10.5 Tb per flow cell and the 10B is ~3–4 Tb. A ~8 Gb exome therefore fits ~375–500 per 10B and ~1,000–1,300 per 25B. The ledger's exome figure of 8 holds (FACT for flow-cell output; the sample counts are my arithmetic).
- Signatera uses ~100,000x depth on patient-specific amplicons, with 16 variants and 20K genome equivalents input (Natera white paper and patent text via search summary). Reads per sample are not disclosed, so I cannot compute Gb. The ledger's "<1 Gb per plasma draw" (E082) remains unverified.

## Assays I could not reach

- **Guardant360 Liquid CDx (P250027, FDA approval 19 May 2026).** The SSED (P250027B) and the Guardant spec sheet downloaded as binary PDFs. I could not render them because poppler is missing, so I got no depth figures. The files are saved in the sandbox tool-results folder for a rerun.
- **FoundationOne CDx and Liquid CDx, Panorama and Haystack.** Not searched; no figures.
- **Guardant Shield and the COGS-share test (assignment item 3).** No new data, and I did not test the equal-price-ratio assumption.

## Contradictions and stale data

- E097 says Medicare finals are "due Nov 2026." That is consistent with the fact sheet, and nothing changes.
- E203 says ~77% of priced codes fall. Secondary sources agree (1,171 of ~1,500, which is ~78%).
- I found no contradiction to the ledger's Gb-per-test table for exome, tissue CGP or liquid CGP. NIPT (1–2 Gb), genome and Signatera remain unchecked against primary sources.

## Gaps / what I could not find

- The actual CMS preliminary rate, ADLT and PLA files, so no rates for 81415–81427, 81479, 81445, 81450, 0340U, 0239U, 0326U, 0414U or the NIPT codes. Next step: download the files from the CMS CLFS page.
- Medicare revenue shares for Natera, Tempus, Caris, GeneDx and Exact, so the revenue-at-risk table is not built.
- Payer policies on MRD and WGS for Aug–Oct 2026, the NCD 90.2 changes, and the Palmetto LCD text. I did not search these.
- Customer COGS-share estimates for Natera, GeneDx and BillionToOne. The ledger already has Shield COGS of ~$410 (E090).
- The Guardant SSED and spec-sheet contents (see above), and the Signatera and Panorama read counts.

**Overall:** this is mostly NO NEW EVIDENCE beyond the four items above (the TSO 500 per-sample figures, the 775-test cap count, the unverified code-level rates, and the Guardant Medicare >10% statement).

Sources:
- CMS fact sheet: https://www.cms.gov/newsroom/fact-sheets/preliminary-calendar-year-cy-2027-medicare-clinical-laboratory-fee-schedule-payment-rates
- HFMA: https://www.hfma.org/payment-reimbursement-and-managed-care/2027-medicare-lab-fee-schedule-cuts/
- Forvis Mazars: https://www.forvismazars.us/forsights/2026/10/cms-releases-preliminary-2027-clinical-lab-fee-schedule-rates
- screenmygene.com blog: https://www.screenmygene.com/resources/clfs-2027-preliminary-rates-molecular-pathology
- Illumina TSO 500 ctDNA knowledge base: https://knowledge.illumina.com/library-preparation/trusight-oncology-tumor-library-prep/library-preparation-trusight-oncology-tumor-library-prep-reference_material-list/000002931.md
- Illumina NovaSeq X specifications: https://www.illumina.com/systems/sequencing-platforms/novaseq-x-plus/specifications.html
