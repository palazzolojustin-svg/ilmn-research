# Agent 143: C-web-clinical-lab-Gb-per-test-and-Q2-25-comparatives-S1-10K

*Model: sonnet. Run 2026-10-11 12:10:13. Cost $0.73 (API-equivalent).*

**Assignment:** Goal: close open gap 9, the Gb-per-test and Illumina-$-per-test side for clinical labs. Pursue: (1) BillionToOne S-1 and 424B4, and Foundation Medicine, Caris and Tempus S-1/S-4/10-K text, via sec.gov full-text or the filing indexes. Search for 'NovaSeq', 'sequencing reagents', 'cost of goods per test' and 'purchase commitment'. (2) Natera Panorama/Signatera, Guardant and GeneDx 10-K 'Cost of revenues per test' and 'Illumina' text, plus Q2'25 and Q2'26 per-test COGS from the earnings releases: Natera cost per test, Guardant COGS per sample, GeneDx cost per exome/genome, Caris cost per profile. (3) Q2'25 comparatives that are still missing: Caris Q2'25 profiles, Guardant360 Q2'25 and Q2'26 volumes, and Tempus MRD volumes. These give the y/y test-volume growth. (4) Peer-reviewed or poster sources on sequencing depth for NIPT (reads per sample, from about 10M to 30M+), WGS-based MRD (Natera Signatera genome, Personalis NeXT, Haystack), and exome vs genome in rare disease (GeneDx). Quantify per lab: tests per year, estimated Gb per test, implied Gb per year, y/y growth, and COGS per test trend (a falling COGS per test shows a pass-through of Illumina price cuts). Finish with a table of a bottom-up clinical Gb CAGR for 2026-2028 with each input sourced or labeled as an assumption, and say whether it reaches mid-20s% volume growth. Cite URL and date for everything. Hard stop at 20 minutes.

## Key findings

Most of what I checked was already in the ledger. I found a few numbers that sharpen it. The three main results:

- **Natera's cost per test is rising, not falling.** No clinical lab discloses Illumina cost per test, and BillionToOne's S-1 has no Illumina text, so I used reported total cost of revenues divided by tests as a proxy. It does not show a visible pass-through of Illumina price cuts (details below).
- **Guardant's proxy COGS per test fell about a third.** It is a crude figure and is driven mostly by mix.
- **GeneDx's proxy COGS per exome/genome fell about 14%.** Its price per test fell by more.

- **Natera cost of revenues per test is rising (OPINION, derived from FACT inputs).**
  - Total cost of revenues was $170.2M on 760.3K tests in Q2'24, about $224/test. It was $200.0M on 853.1K tests in Q2'25, about $234/test. [Natera Q2'25 8-K Ex.99.1, 2025-08-07, https://www.sec.gov/Archives/edgar/data/1604821/000110465925075189/tm2522162d1_ex99-1.htm]
  - Q2'26 revenue was $752.8M at a 64.5% gross margin on 1,043,900 tests. That implies cost of revenues of about $267M, or about $256/test. [Natera Q2'26 release, 2026-08-06, https://www.natera.com/company/news/natera-reports-second-quarter-2026-financial-results/] This is my arithmetic, because I could not parse the PDF's cost line.
  - So cost per test is up about 9% y/y in Q2'26 and about 14% over two years.
  - Cost of revenues includes labor, shipping, licensing and more, and the mix is shifting to Signatera. Signatera carries a tumor exome plus serial draws, so the rise is consistent with Gb intensity going up. It is not evidence of Illumina price pass-through.
  - This bears on E081 and the E082 correction. Natera's blended cost per test rises while volume grows, so per-Gb price cuts are not visibly shrinking its cost base.
- **Guardant's proxy COGS per test fell about 33%, mostly from mix (OPINION, derived from FACT).**
  - Cost of revenues was about $116.0M in Q2'26 ($335.0M revenue less $219.0M gross profit). It was about $81.2M in Q2'25 ($232.1M less $150.9M). [Guardant Q2'26 8-K, https://www.sec.gov/Archives/edgar/data/0001576280/000157628026000036/gh-06302026xexhibit991.htm]
  - Divided by oncology plus Shield tests, that is about $682/test in Q2'26 (about 104K plus 66K) against about $1,015/test in Q2'25 (about 64K plus 16K).
  - This is crude because COGS also covers biopharma and data samples. Shield is a cheaper test, so most of the drop is mix. It does not isolate the roughly $200 saving from moving G360 Liquid to the X (E043).
  - Gross margin was flat at 65% GAAP in both periods, so Guardant is not showing margin capture. Non-GAAP was 67% against 66%.
- **GeneDx's COGS per exome/genome fell about 14%, less than its price per test (OPINION, derived from FACT).**
  - Blended reimbursement fell from over $3,700 in Q2'25 to $3,258 in Q2'26. That is about -12%. [GeneDx Q2'25 release, https://www.sec.gov/Archives/edgar/data/1818331/000181833125000105/q22025pressrelease.htm; Q2'26 release, https://www.biospace.com/press-releases/genedx-reports-second-quarter-2026-financial-results]
  - Adjusted gross margin was 70% against 71% a year earlier. Q2'26 revenue was $114.4M, so adjusted COGS was about $34M. On 30,785 tests that is about $1,115/test.
  - For Q2'25 I back-solved revenue at about $103M ($114.4M ÷ 1.11), which gives adjusted COGS of about $30M. On 23,102 tests that is about $1,290/test.
  - The inputs include non-exome revenue, so treat the figure as approximate. It supports E091's "step improvements in 2027" wording, and cost per test fell about as fast as price.
- **Q2'25 comparatives (FACT).**
  - Caris: 50,032 clinical therapy-selection cases (+22.0% y/y), gross margin 62.7%. [Caris Q2'25 8-K, https://www.sec.gov/Archives/edgar/data/2019410/000201941025000011/cai_ex99-1.htm] The ledger's Q2'26 figures are 59.2K cases, +18%.
  - Guardant: oncology volume about 64,000 (+30%). Guardant360 Liquid grew over 20%. Shield was about 16,000 tests. [Guardant Q2'25 8-K, https://www.sec.gov/Archives/edgar/data/1576280/000157628025000245/gh-6302025xexhibit991.htm] The ledger's Q2'26 figures (about 104K, +63%; Shield about 66K) confirm the y/y.
  - GeneDx: 23,102 exome/genome results (+28% y/y). Q2'26 was 30,785, so +33% by my arithmetic; the company said +32%.
  - Natera: Q2'25 oncology tests 188,800 (+50.6%); total tests 853,100 (+12.2%). Q2'26 was 296.7K, which is +57% and consistent with E081.
  - Tempus: Q2'25 clinical NGS volume above 212,000 tests (+30%), oncology testing +26%. The xM MRD volume was kept low pending Medicare coverage, and I found no number. [Tempus Q2'25 release, https://www.tempus.com/news/pr/tempus-reports-second-quarter-2025-results/] So Tempus MRD y/y cannot be built.

## Section: BillionToOne
- The S-1 text I could fetch has no mention of Illumina, NovaSeq, sequencing reagents or purchase commitments. It describes proprietary smNGS (single-molecule NGS) technology only. [S-1, https://www.sec.gov/Archives/edgar/data/2070849/000119312525233697/d903739ds1.htm]
- It reports FY24 revenue of $152.6M and cost of revenue of $71.7M, a gross margin of about 53%. The company attributes margin gains to a lower cost per test.
- The fetch tool summarizes pages and may have truncated the document, so this is a negative result for the fetched text, not proof the filing is silent.

## Section: NIPT depth
- Peer-reviewed sources show the depth-versus-sensitivity trade-off. At a 10% fetal fraction, 20M reads detected microdeletions with 79.3% sensitivity (98.4% for deletions over 3 Mb). Below a 10% fetal fraction, sensitivity was 57%. [PMC7449492, https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7449492/]
- Standard NIPT is described as about 3M reads at 0.15x. NIPT-PLUS is about 8M reads at 0.4x (search-result snippet, not opened).
- Pushing NIPT toward microdeletion detection means roughly 20M+ reads, about 2–3x standard NIPT depth. At 150-bp paired-end reads that is roughly 6 Gb. Rough arithmetic: 20M read pairs × 300 bp = 6 Gb, which is above the ledger's "~1–2 Gb" for NIPT, if a lab adopts such panels.

## Bottom-up clinical Gb CAGR, 2026–2028 (illustrative)

Every input is an assumption, labeled as such, except where tied to ledger items. The Gb-share weights are mine because no lab discloses them.

| Segment | Share of clinical Gb, 2026 (assumption) | Annual Gb growth (assumption) | Basis |
|---|---|---|---|
| Tumor CGP (tissue and liquid) | 35% | 20% | Test growth +18–30% per E081, partly offset by Gb per test falling if the ~120 Gb liquid figure is overstated (E082 correction) |
| MRD | 20% | 35% | Test growth +45–60%, but most Gb sits in the one-off tumor exome (ledger correction); upside if mix shifts to genome-type tests |
| Rare disease | 20% | 30% | Test growth +32%, plus the exome-to-genome mix shift (genome cost "nearly double") (E091) |
| NIPT / reproductive | 15% | 8% | Natera non-MRD test growth is about 13% (ledger correction); upside if read depth rises |
| Other | 10% | 8% | Placeholder |
| **Weighted** | 100% | **~22%** (plausible range ~17–27%) | |

My read is that this does not clearly reach mid-20s% (OPINION). It gets there only if MRD tests move to genome-type assays and rare disease keeps tilting to genomes. Gb growth of about 22% against a mid-teens price decline per year implies consumables revenue growth of roughly 5–8%, in line with management's own model (volume mid-20s, price mid-teens). The one-time price drop across the 6000-to-X transition would sit on top of that.

## Contradictions and stale data
- Natera's cost per test is rising while Illumina price cuts are meant to cut cost. A mix shift to Signatera is the most likely explanation. This challenges any assumption that blended lab COGS visibly passes through per-Gb price declines.
- Guardant's gross margin was flat y/y, but GAAP COGS per test fell about a third on mix. The two readings do not conflict, because Shield has a lower cost per test.
- The Natera Q2'26 cost line is derived from the gross margin percentage, not read from the statement.

## Gaps / what I could not find
- Any Illumina dollars per test, or purchase obligations, for Natera, Guardant, Caris, FMI or Tempus. The Natera 10-K search returned only older 10-Ks (FY2015–FY2023). I did not retrieve the Guardant, Caris or FMI 10-K purchase-obligation text. Foundation Medicine and Tempus filings were not reached.
- Tempus MRD Q2'25 volume. Guardant360 Liquid Q2'25 absolute volume. Caris cost per profile.
- A primary read-count source for NIPT or MRD. The WGS-MRD depth sources (Signatera Genome, Personalis NeXT, Haystack) were not searched in this pass. The exome-versus-genome depth source for GeneDx was not retrieved either.
- Time ran short before I could open the Natera Q2'26 PDF (it came back as binary), so cost per test needs a local pdftotext check.
