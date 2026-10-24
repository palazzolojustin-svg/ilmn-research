# Agent 99: 104-web-MGI-H1-2026-report-China-pricing-and-Asia-sequencing-service-providers-Novogene-Ma

*Model: sonnet. Run 2026-10-11 10:22:35. Cost $0.94 (API-equivalent).*

**Assignment:** Close open gap 2 and add the price-war read-through from Asia, which sets the global price floor for $/Gb. (1) Retrieve MGI Tech (688114.SS) H1 2026 report. Try cninfo, SSE (sse.com.cn), Eastmoney, Sina Finance or an English summary on GenomeWeb, 360Dx or Yicai Global. Extract: the domestic vs overseas revenue split, the sequencer revenue (SEQ ALL RMB 1.062B vs GenomeWeb's RMB 1.10B discrepancy), the T7+ and T20 placements, the reagent/consumable revenue and growth, gross margin, price commentary, clinical share and the Illumina import-substitution commentary. Use pdftotext -layout or Python pypdf if you can download the PDF. (2) Illumina's China status: the unreliable entity list, the import ban on sequencers (Mar 2025), any 2026 change, the FY25 10-K China revenue and the Q2'26 disclosure, and the effect on clinical growth ex-China. (3) Sequencing service providers' public data: Novogene (688315) H1 2026 report, Macrogen, Psomagen, Azenta/Genewiz, BGI Genomics. Look for revenue per Gb or per sample, price cuts, and which platforms they run (NovaSeq X, T7+, Ultima, Element). Quantify price per Gb or per genome and the y/y price change. (4) Any 2026 Chinese or Asian price per genome announcements ($100, $200 genomes), such as MGI T1+ or T20 claims. Report the numbers with sources and quote exact wording. Do not repeat agents 86 and 90 unless you actually open the primary report.

## Key findings

1. **Illumina's Greater China revenue is shrinking and ex-China framing hides it.** FACT: Greater China revenue was $243M in FY25 vs $308M in FY24, a $65M (−21%) drop that the 10-K attributes to the Unreliable Entity List ("UEL") listing. [Illumina FY25 10-K, sec.gov/Archives/edgar/data/1110803/000111080326000024/ilmn-20251228.htm; the search summary carried the $308M and $65M, the fetch confirmed the $243M]. Q2'26 was $56M vs $63M (−11%), and H1'26 was $108M vs $135M (−20%). [Illumina 10-Q for the period ended 2026-06-28, sec.gov/Archives/edgar/data/0001110803/000111080326000160/ilmn-20260628.htm]. China is still falling in 2026 even after the import ban was lifted. Extends E145 and E159, which show the ex-China framing but no China dollars.

2. **MGI's H1'26 growth is reagent-led and overseas-led.** FACT, from secondary summaries of the report (units checked, see Contradictions):
   - Revenue was RMB 1.366B, +18.91%.
   - Overseas revenue was RMB 483M, +33.77%, about 35% of the total. Implied domestic revenue is about RMB 883M (calc, ~65%).
   - Americas revenue was RMB 201M, +95.76%.
   - SEQ ALL revenue was RMB 1.062B, +17.64%. Reagent/consumable revenue grew +16.28% and instrument revenue fell −6.37%. The company reports "over 410" new sequencer sales.
   - Gross margin was 57.03%, up about 3 points y/y. Net loss was RMB 158M, 6.41% narrower. Operating cash flow was +RMB 300M.
   - [weeklyonstock.com/26/0821/ABB2621301779398.html (2026-08-21); wap.stockstar.com/detail/RB2026082500032745 (2026-08-25)]
   - This adds dollars and the overseas split to E131, which had only clinical +36.6% and reagent +16.3%.

3. **MGI cut T7+ running cost about 50%.** MGMT: the T7+ was redesigned with plug-in reagent trays and partly room-temperature reagents, and "运行成本较此前下降50%" (running cost down 50% vs before). [Chinese-language search summary of the H1'26 report, 2026-08-22; primary PDF not read]. This is a cost claim, not an observed price. It is a credible driver of the Asian price floor, but it comes with no $/Gb figure.

4. **Novogene's data show the price deflation Illumina's model assumes.** FACT/calc:
   - In FY25, Novogene's data output rose +33.19% and sales volume rose +28.19%. Its "sequencing platform services" revenue rose only +0.63%, to RMB 1.062B, at a 32.50% gross margin (−1.88 pts).
   - Implied revenue per unit of volume is about −22% (calc, 1.0063/1.2819−1; the volume measure is unclear, so treat as approximate).
   - That matches Illumina's own pattern of volume +30% vs revenue +5% (E048). It shows a large Illumina customer passing price declines through.
   - [cls.cn/detail/2344118; jiemian.com/article/14256855.html; m.gelonghui.com/news/5230297; FY25 report summaries, about 2026-04]

5. **Novogene says competition eased and runs a mixed fleet.** MGMT:
   - Q1'26 gross margin was 41.84% (+237 bps), attributed to "行业竞争压力减小" (reduced industry competitive pressure). FY25 gross margin was 42.5% (−121 bps) on "market competition and product mix adjustment". [gelonghui, 2026]
   - Stated platforms: "Illumina Novaseq XPlus、Ultima UG100、华大DNBSEQ-T7&T7+、真迈Surfseq Q、PacBio Revio".
   - It names Illumina, Thermo Fisher, PacBio and MGI as suppliers, so it is a live multi-vendor buyer. E128 already has the Georgia core quote that 80–90% of lost work goes to low-cost providers like Novogene.

6. **Novogene H1'26 was soft.** FACT:
   - Revenue was RMB 1.114B, +7.09%. Mainland China was RMB 556M (+9.66%) and HK/Taiwan/overseas was RMB 558M (+4.65%).
   - H1 gross margin was 41.86% (+1.06 pts y/y). Net profit was RMB 63.1M, −19.82%. R&D rose +45.7%.
   - [jiemian.com 14256855 search summary; stockstar RB2026082700056904 (2026-08-27)]
   - The FY25 segment split gave a sequencing platform gross margin of 32.5% vs 54.2% for research services. The H1 report did not itemize segments in the pages I could read.

7. **The ban timeline is confirmed from the filing, and the UEL listing remains.** FACT, from the 10-K and the Q2'26 10-Q:
   - UEL listing: 4 Feb 2025.
   - 4 Mar 2025 notice: Illumina "would no longer be permitted to export sequencing instruments into China."
   - 5 Nov 2025 decision, effective 10 Nov 2025: exports to Chinese companies permitted again, "subject to approval on a case-by-case basis."
   - The Q2'26 10-Q still lists "our inclusion on the 'unreliable entities list'" as a forward-looking uncertainty.
   - Consumables were 74% of FY25 revenue and instruments 11%. The filing does not split China by consumables vs instruments.
   - Adds exact filing wording to E159.

8. **Azenta and Macrogen offer little price read-through.** FACT:
   - Azenta fiscal Q3'26 (ended 2026-06-30): revenue was $161M, +12% (+9% organic). Multiomics was $73M, +8% organic, led by NGS and gene synthesis. China multiomics grew about 23% and Europe about 26%, but that is mostly oligo/synthesis. About $3M of clinical-services work was pulled into the quarter, and management said it does not show a broad recovery. [azenta q3 call highlights, via thestockobserver.com 2026-08-06; marketbeat page did not load]
   - Macrogen Q1'26: revenue was KRW 45.3B, of which sequencing was KRW 39.9B (88%), with an operating loss of KRW 0.5B. The company says sequencing faces unit-cost decline and "requir[es] volume expansion for viability." [en.edaily.co.kr/news/eda202606265099, 2026-06-26]
   - The older Macrogen plan of 5 NovaSeq X Plus units is from Illumina marketing material and is undated.

9. **No 2026 Asian "$100 genome" announcement found.** The only hit is MGI's T20×2 claim, dating from 2023: under $100 per 30x genome "including instrument depreciation", at up to 50,000 WGS a year. [news-medical.net 2023-02-09; sandiegomics.com]. Nothing from 2026 gives a $/Gb for the T1+ or T20, so the price floor is anchored by older claims. This is OPINION on the absence, not a finding.

## Contradictions and stale data

- **SEQ ALL RMB 1.062B vs GenomeWeb's RMB 1.10B.** The Chinese summaries I opened, weeklyonstock.com and stockstar, say 10.62亿 (RMB 1.062B), +17.64%. The GenomeWeb summary says RMB 1.10B, +18%. I could not open the primary PDF, so the gap is unresolved. A plausible but unverified reason is that GenomeWeb's "sequencing" includes extra lines. I would use 1.062B, because it matches the company-segment naming and the +17.64% growth.
- **Unit scale.** The WebFetch tool mislabeled 亿 as "billion", producing nonsense like "13.66 billion yuan". Correct scale is 亿 = 100M yuan, so RMB 1.366B. I corrected every figure above.
- **Coincidence to check.** Novogene's FY25 sequencing-platform revenue and MGI's H1'26 SEQ ALL both print as 10.62亿. They come from different companies and sources with different growth rates and margins, so I treat it as a coincidence. Re-check before citing either in the synthesis.
- **MGI "410 new units" vs E070.** E070's "MGI 2025 units 1,470 vs 1,260" is a different period and measure. MGI says the H1'26 unit count is down y/y, which would be consistent with instrument revenue −6.37%.
- **Search summaries disagreed on China.** One said Illumina's UEL status is not in the 10-Q. The fetched 10-Q text does contain it. I used the fetched text.
- **UEL ban lift and E159.** E159 says exports were allowed from 10 Nov 2025 "case by case". That is consistent, and the filing wording is now exact.

## Gaps / what I could not find

- **MGI primary report.** The cninfo PDFs (1225493311, 1225493542, 1225493342) and the dfcfw PDFs came back as binary or unreadable. Read tool PDF rendering failed because pdftoppm is not installed, and no shell was available. I could not get the T7+ and T20 placement split, an exact clinical share, price commentary or the Illumina import-substitution wording. A session with pdftotext should run it on the saved file `…\3abbc297-b52e-4773-b0ea-4daa84f64743\tool-results\webfetch-1791732026543-9x6sus.pdf`.
- **MGI T7+ install base.** The GenomeWeb/EQS snippet says "over 40 units installed globally" since the Sept 2025 launch. I did not open that EQS release, so this number is unverified.
- **Novogene H1'26.** No itemized segment split, no data-output or volume figures, and no $/Gb or per-sample price.
- **Macrogen and Psomagen.** No H1'26 numbers or $/genome. Psomagen has only a pitchbook trailing-12-month figure of $42.8M, which I did not open. BGI Genomics was not searched.
- **Azenta NGS.** The NGS-only growth rate and any price commentary are missing.
- **Illumina China.** No Q2'26 call disclosure of China as a share of clinical or of the consumables-versus-instrument split. The Q2'26 transcript, as fetched, has no MGI or Chinese-competitor discussion. Management's China comments at JPM26 (Fierce) were blocked (403).
- **Greater China % of revenue.** I did not verify total revenue to give an exact percent. $243M is roughly 5–6% of FY25 revenue (rough calc; the search summary said "about 7%" from older data).
