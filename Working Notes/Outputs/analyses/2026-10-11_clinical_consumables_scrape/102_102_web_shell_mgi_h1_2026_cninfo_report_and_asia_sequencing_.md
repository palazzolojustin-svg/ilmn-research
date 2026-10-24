# Agent 102: 102-web-shell-MGI-H1-2026-cninfo-report-and-Asia-sequencing-service-provider-pricing-decod

*Model: sonnet. Run 2026-10-11 10:27:47. Cost $0.86 (API-equivalent).*

**Assignment:** Close open gap 2. Download the MGI Tech H1'26 report from cninfo (file 1225493542.PDF; search cninfo.com.cn or the SSE STAR Market site for '华大智造 2026年半年度报告' if the link fails). Decode it with pdftotext -layout, using a Chinese-capable tool or reading the extracted text directly. Extract: domestic vs overseas revenue split and the check against RMB 1.062B vs 1.10B; sequencer vs reagent revenue; T7+, T20 and T1+ placements and the 'over 40 installed' T7+ claim; any $/Gb or price-war commentary; the clinical share of use; gross margin; and any language on import substitution of Illumina, Illumina's China restrictions (the unreliable entity list) and customers. Then find H1'26 or Q2'26 results for Novogene (688315), BGI Genomics (300676), Macrogen (KOSDAQ) and Psomagen: sequencing-service revenue, data volume (Tb or Gb), price per Gb, platform mix (NovaSeq X, Illumina vs MGI vs Ultima) and any statement of capacity or Illumina consumable purchases. Quantify what the price per Gb among Asian service providers implies for the 35B price umbrella, and the China ex-clinical consumables share risk to Illumina. Label FACT, MGMT or OPINION and give exact page or section references. Hard stop at 20 minutes.

## Key findings

The MGI H1'26 primary PDF is still undecoded. This session had no Bash, pdftotext or pdftoppm, and WebFetch returned only PDF binary. I did not read page-level text, so I cannot give page or section references. The gain this round is mostly secondary data that closes part of the Novogene, Macrogen and MGI picture.

- **The real URL has a different date folder.** The PDF is `https://static.cninfo.com.cn/finalpage/2026-08-22/1225493542.PDF`, not the 08-28 or 08-29 paths. It is the file already saved as `webfetch-1791732358383-hb1gfc.pdf` (1.8 MB, WPS-created 21 Aug 2026). A session with Bash can run pdftotext on that saved file directly. [cninfo via WebSearch, 2026-08-22]
- **The RMB 1.062B vs 1.10B check is probably explained, but only from secondary sources.** This is an inference, not a verified reading of the report.
  - **FACT (secondary):** SEQ ALL, MGI's full-length sequencing line, is RMB 1.06B (+17.6%). Reagents and consumables grew 16.3% and instruments fell 6.4%. [search summary of the report, 2026-08-22]
  - **FACT (secondary):** More than 410 new sequencers were sold in H1'26. [same source]
  - **FACT (secondary):** GenomeWeb quotes "sequencing revenue RMB 1.10 billion, up 18%", with reagents +16% and instruments −6%. [genomeweb.com/node/657086 snippet; the page itself returned HTTP 403]
  - **OPINION:** 1.10B is likely a broader sequencing definition than SEQ ALL's 1.062B, for example including other sequencing-related revenue. Treat it as unreconciled until the segment note is read.
- **Intelligence on the "over 40 T7+ installed" claim.** GenomeWeb says "over 40 units of the T7+ are installed globally since its launch" and that 27 T7+ units were sold in 2025. [genomeweb snippet, via web search] This is a small base next to roughly 970 NovaSeq X units. It is also an installed count, not H1'26 placements. T20 and T1+ placement counts were not found. Only the T1+ NMPA approval was found, described as a clinical Tb-scale benchtop platform that runs PE150 in 24 hours with Q40 ≥ 90%. [search summary of the report, 2026-08-22]
- **MGI geography (partial).**
  - **FACT (secondary):** Americas revenue was RMB 243.4M, "up 21%", with sequencing revenue there of RMB 210.0M, also up 21% and "driven by consumable sales". [GenomeWeb snippet; the period is unclear and may be an earlier one]
  - **Contradiction:** the ledger (E131 correction) says Americas +95.8% and overseas RMB 483M (+33.8%). Treat the +21% figure as a possibly different period (FY25 or Q1) until checked.
- **MGI margin and cash.** Net loss was RMB −158M (loss narrowed 6.41%). Gross margin rose about 3 points. Operating cash flow was +RMB 300M (+218%). Period expenses fell 12.68%. The company claims the T7+ running cost is down 50% (plug-in reagent trays and room-temperature reagents). [search summary and weeklyonstock, 2026-08-21]. Ledger E131 already has the 57.0% gross margin.
- **Novogene H1'26 (new; not in the ledger).**
  - **FACT:** Revenue was RMB 1,113.83M (+7.09%). Mainland China was RMB 555.6M (+9.66%). Hong Kong, Macau, Taiwan and overseas were RMB 558.2M (+4.65%). [jiemian/search summary of the 25 Aug 2026 results call; news.qq.com/rain/a/20260826A0906E00]
  - **FACT:** Net profit was RMB 63.1M (−19.82%). Gross margin was 41.86%. Q2 revenue was RMB 557M (+3.59%) and Q2 net profit was RMB 33.7M (−24.9%). [news.qq.com/rain/a/20260827A02WHL00, 2026-08-27]
  - **FACT (new):** Q1'26 revenue was RMB 556M (+10.84%) and net profit RMB 29.5M (−13.06%). Q2 growth slowed sharply from Q1. [search summary, 2026-04]
  - **OPINION:** the slowdown to +3.6% in Q2, with falling profit, is consistent with price pressure that outpaces volume. The press attributes the profit decline to higher credit-loss provisions on receivables. [news.qq.com, 2026-08-27]
- **Novogene FY25 volume vs revenue (quantified, supports E070).**
  - **FACT:** FY25 revenue was RMB 2.210B (+4.66%) and gross margin 42.53% (−1.21 points). [gelonghui, 2026-05-08]
  - **FACT:** Data output was +33.19% and "销量" (data sales volume) was +28.19%. Sequencing platform service revenue was RMB 1.062B at a 32.5% gross margin. [gelonghui, 2026-05-08; jiemian]
  - **OPINION:** with sequencing volume up about 28% and total revenue up 4.7%, the implied per-Gb price decline is large. Sequencing service revenue growth was not found, so a clean $/Gb cannot be computed.
- **Novogene platform mix.**
  - **MGMT (FY25 report):** The company lists NovaSeq X Plus, NextSeq, MGI T7 and T7+, Ultima UG100, PacBio Revio and Singular Surfseq Q. It says NovaSeq and T7+ "showed notably increased adoption". [gelonghui, 2026-05-08]
  - **FACT:** The company site gives NovaSeq X Plus PE150 as 3 Tb/run (10B) and 8 Tb/run (25B). The T7 gives 1.75–7 Tb. [search summary]
  - This is the same large Asian service provider that Georgia core says takes 80–90% of lost work (E128). Its disclosed platform mix therefore shows Illumina still in use alongside MGI T7+ and Ultima. It does not show a switch away from Illumina.
- **Macrogen H1'26 (conflicts with the ledger).**
  - **FACT:** H1'26 revenue was KRW 54.1B (+13%), operating profit KRW 2.4B (+152%) and net income KRW 2.3B (+227%). The CEO credited "cost reduction optimization" and stable NGS growth. [kormedi.com/1228742, 2026-08-07]
  - **Contradiction with E352:** E352 gives Q1'26 revenue of KRW 45.3B. A search summary gives Q2 revenue of KRW 51.0B (+4.1%), and that does not reconcile with H1 of KRW 54.1B. The figures may mix consolidated and standalone numbers. Do not use them until the DART filing is checked.
  - **OPINION:** in either version Macrogen is barely profitable, which fits E352's "unit-cost decline" comment.
- **BGI Genomics (300676).** It held an investor call on 24 Aug 2026 with 8 institutions. FY25 precision-medicine testing revenue was RMB 1.588B. No H1'26 segment or sequencing numbers were retrievable. [search summary]
- **Psomagen H1'26.** Nothing found.

## What this means for the 35B price umbrella and China risk (OPINION)

- I found no disclosed $/Gb for any Asian service provider. The only quantified signal is Novogene's FY25 data volume +28–33% against revenue +4.7%. That is roughly a 20% or larger decline in revenue per unit of data. It matches management's "mid-teens" long-term price decline and E070, so it does not point to a faster break.
- On the China ex-clinical consumables share risk to Illumina, the new read-through is Novogene's Q2'26 growth of +3.6% and rising receivables stress. Even Illumina's largest research-sequencing customers there are seeing weak revenue.
- I found no MGI wording on import substitution or the unreliable entity list in the report text. The only entity-list facts are the Feb 2025 listing, taken from yicaiglobal and digitalpolicyalert and already known.

## Contradictions and stale data

- MGI sequencing revenue: RMB 1.062B (SEQ ALL, ledger) vs RMB 1.10B (GenomeWeb).
- MGI Americas growth: +21% (GenomeWeb) vs +95.8% (ledger).
- Macrogen: Q1'26 KRW 45.3B (E352) vs Q2 KRW 51.0B vs H1 KRW 54.1B. These cannot all be right.
- Novogene gross margin for H1'26: one source says +1.06 points y/y and another says +2.61%. The level of 41.86% is consistent across both.

## Gaps / what I could not find

- MGI page-level text: the domestic/overseas split, T20 and T1+ placements, clinical share, $/Gb and price-war wording, and Illumina and import-substitution language. Next step: in a Bash session, run `pdftotext -layout` on `webfetch-1791732358383-hb1gfc.pdf` and grep for 境内, 境外, 国产替代, 不可靠, T7+, T20, 价格.
- Novogene's sequencing-service segment for H1'26, data volume and price per Gb. The full report is probably at `cninfo.com.cn`, filed around 25 Aug 2026. The Novogene IR record (dataclouds.cninfo.com.cn/.../20260417/...PDF) was not opened.
- Psomagen and Macrogen platform mix and capacity: nothing found.

**Not reached:** the GenomeWeb article (HTTP 403) and the BGI Genomics half-year report.

Sources: [jiemian.com 14256855](https://www.jiemian.com/article/14256855.html), [news.qq.com 20260826](https://news.qq.com/rain/a/20260826A0906E00), [news.qq.com 20260827](https://news.qq.com/rain/a/20260827A02WHL00), [gelonghui 5230297](https://m.gelonghui.com/news/5230297), [kormedi 1228742](https://kormedi.com/1228742/), [weeklyonstock](https://static.weeklyonstock.com/26/0821/ABB2621301779398.html), [cninfo MGI H1'26](https://static.cninfo.com.cn/finalpage/2026-08-22/1225493542.PDF), [GenomeWeb](https://www.genomeweb.com/node/657086) (search snippet only).
