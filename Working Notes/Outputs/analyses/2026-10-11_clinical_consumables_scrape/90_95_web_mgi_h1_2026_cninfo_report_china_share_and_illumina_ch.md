# Agent 90: 95-web-MGI-H1-2026-cninfo-report-China-share-and-Illumina-China-FY25-10K-reconciliation

*Model: sonnet. Run 2026-10-11 10:12:51. Cost $0.80 (API-equivalent).*

**Assignment:** Close open gaps 2 and 3. (a) Fetch the MGI Tech H1'26 report (static.cninfo.com.cn/finalpage/2026-08-22/1225493542.PDF). If WebFetch fails, save the PDF to disk with curl and run pdftotext. Extract sequencing instrument and reagent revenue (reconcile RMB 1.06B vs 1.10B), China share, clinical, NIPT and oncology adoption comments, T7+/T20 placements, overseas share, gross margin and price per Gb commentary. (b) Open the Illumina FY25 10-K from sec.gov (segment and geographic note, MD&A China discussion, unverified-entity-list and export-control risk factors). Reconcile total FY25 revenue ($4,343M vs $4,398M, and the source of each figure). Get China/Greater China revenue in dollars and as a percentage for FY23, FY24 and FY25, plus any China-specific consumables or clinical commentary. (c) Estimate the ex-China flattery on clinical consumables growth: the reported total clinical growth versus the ex-China growth, under 3 assumptions of China's share of clinical consumables. Cite filings and give quotes. Do not repeat agent 89. Label every point FACT, MGMT or OPINION.

## Key findings

**Coverage.** Two of the three pieces are only partly done. I could not read the MGI H1'26 PDF or the 10-K's geographic note, because Bash and pdftotext are disabled in this session and WebFetch returns raw binary for PDFs. The Illumina China dollar series is confirmed, but the MGI sequencing detail is not.

- **China revenue series is confirmed (E145 is partly corrected).**
  - Greater China is $384M in FY23, $308M in FY24 and $243M in FY25. It includes China, Taiwan and Hong Kong.
  - The FY25 and FY24 figures come from the FY25 and FY24 10-K text. FY25: "Our revenue from the Greater China region, which includes China, Taiwan, and Hong Kong, was $243 million in 2025" [Illumina FY25 10-K, risk factors, https://www.sec.gov/Archives/edgar/data/1110803/000111080326000024/ilmn-20251228.htm]. FY24: "was $308 million in 2024" [Illumina FY24 10-K, https://www.sec.gov/Archives/edgar/data/1110803/000111080325000019/ilmn-20241229.htm]. FACT.
  - The FY23 $384M comes from a search snippet of the 10-K and the consensus sheet [Extracts/ILMN/consensus/ILMN_Consensus_Annuals.md, line 96]. I did not read it in the filing text. FACT, lower confidence.
- **The $4,343M vs $4,398M conflict:**
  - FACT: $4,343M is FY25 revenue [Q4'25 deck, Extracts/ILMN/deck/ILMN_2025Q4_Earnings_Slides.md, line 132].
  - FACT: the FY24 comparatives in the same deck are $4,332M for "core Illumina" and $4,372M consolidated. Consolidated includes GRAIL until its 24 Jun 2024 spin-off.
  - I found no $4,398M in the FY25 10-K excerpt I could read, or anywhere in the corpus. The fetched excerpt did not include the financial statements, so this is not a full negative.
  - OPINION: $4,398M matches neither FY24 base. It is probably a third-party data field or a typo. Treat $4,343M as the FY25 figure and do not use $4,398M until someone finds its source.
- **China as a share of total revenue (computed from FACT inputs):**

| Year | Greater China | Total revenue used | China share |
|---|---|---|---|
| FY23 | $384M | $4,504M (consolidated; my recollection, not verified in the corpus) | ~8.5% |
| FY24 | $308M | $4,372M consolidated, or $4,332M core | ~7.0–7.1% |
| FY25 | $243M | $4,343M | ~5.6% |

  - Ex-China revenue was $4,100M in FY25 against $4,024M in FY24, up 2% [Q4'25 deck line 132].
  - Total revenue was flat while China fell 21%.
- **Consumables mix (FACT).** Consumables were 74% of FY25 revenue, against 72% in FY24 and 68% in FY23 [FY25 10-K, via WebFetch summary]. The 10-K gave no China-specific consumables or clinical breakdown in the text I could read. This confirms gap 2: China's share of clinical consumables is undisclosed.
- **The export-control risk factor is confirmed.**
  - The Unreliable Entity List (UEL) listing was announced 4 Feb 2025.
  - A notice on 4 Mar 2025 said Illumina would no longer be permitted to export sequencing instruments to China.
  - On 5 Nov 2025 regulators decided that, effective 10 Nov 2025, Illumina could export instruments to Chinese companies again, but "case-by-case" [FY25 10-K risk factors]. This matches E159. FACT.
- **International share (FACT).**
  - International shipments were $2,100M (48%) in FY25, $2,084M (48%) in FY24 and $2,145M (48%) in FY23 [FY25 10-K]. FY22 was $2,294M (50%) [FY24 10-K].
  - Greater China was about 11.6% of international shipments in FY25 ($243M of $2,100M), against about 14.8% in FY24.

## Ex-China flattery on clinical consumables growth (OPINION, my model)

Reported ex-China clinical consumables growth is 15% for Q2'26 and 20% for Q1'26 (E073). Total clinical growth including China is not disclosed.

**Formula.** Total growth = (1 − s) × ex-China growth + s × China growth. Here s is China's share of prior-year clinical consumables.

**China growth assumptions.** I used Greater China total revenue growth as a proxy for China clinical consumables growth, because no clinical-specific figure exists.
- Q1'26: −29% organic [Q1'26 deck summary, Extracts/ILMN/deck/ILMN_2026Q1_Earnings_Slides.md, line 5].
- Q2'26: about −11% reported, from $56M against $63M in Q2'25 [consensus sheet and Q2'25 deck line 27].

**Choosing s.** Greater China revenue is about $60M a quarter and most of it is probably consumables. Clinical is more than 65% of global sequencing consumables, but China's clinical share is unknown. My rough sizing puts China clinical consumables at $25–30M a quarter, or about 5–6% of the global clinical base. The three cases below bracket that.

| China share of clinical consumables | Q2'26 total clinical (ex-China 15%, China −11%) | Flattery | Q1'26 total clinical (ex-China 20%, China −29%) | Flattery |
|---|---|---|---|---|
| 3% (low) | ~14.2% | ~0.8 pt | ~18.5% | ~1.5 pt |
| 6% (mid) | ~13.4% | ~1.6 pt | ~17.1% | ~2.9 pt |
| 10% (high) | ~12.4% | ~2.6 pt | ~15.1% | ~4.9 pt |

- **Takeaway.** The ex-China framing flatters clinical growth by roughly 1–3 points in the middle case, and up to about 5 points in the worst quarter (Q1'26) at the high share. Growth is still double-digit under every assumption, so the clinical volume story survives.
- **Larger effect.** The ex-China framing matters more for the headline. Q1'26 total organic growth was only 1.2% (E145).
- **Direction of error.** If China's clinical share were higher, say because China is mostly consumables on a legacy installed base, the flattery would be larger.
- **Test for the Q3'26 call (29 Oct).** Ask for clinical consumables growth including China, or China's share of clinical consumables.

## MGI Tech H1'26 (partial; secondary snippets only)

I could not decode the cninfo PDF (1225493542.PDF). The binary is saved at `C:\Users\palaz\.claude\projects\C--Users-palaz-OneDrive-Documents-ILMN-Claude-Code-Local-Folder--Build-sandbox\5a6436f7-d4f7-4f33-ab0c-bc32d299168b\tool-results\webfetch-1791731429000-kbhew5.pdf`. Please run `pdftotext -layout` on it manually.

- **Group revenue (FACT).** The search summary and the 10jqka and weeklyonstock pages give "13.66亿" RMB, up 18.91% year on year (https://stock.10jqka.com.cn/20260822/c679192132.shtml; https://static.weeklyonstock.com/26/0821/ABB2621301779398.html, 2026-08-21/22). The search tool mistranslated 亿 as "billion". It is RMB 1.366B.
- **Margin and loss.** Main-business revenue was up 19.01%. A quote reads "毛利率同比提升约3个百分点" (gross margin up about 3 points year on year). Net loss attributable to the parent was RMB 158M (loss narrowed 6.41%). Operating cash flow was +RMB 300M.
- **Sequencing and reagent revenue (FACT, from a search-tool summary; the same mistranslation applies).**
  - Full read-length sequencing (SEQ ALL) was RMB 1.062B, up 17.64%. This is the "10.62亿" figure.
  - Reagents were RMB 645M, up 16.28%, or 60.77% of SEQ ALL. 645/1,062 = 60.7%, so the figures are internally consistent.
  - The implied instrument revenue is about RMB 417M. This is an OPINION computed by subtraction.
- **Reconciling RMB 1.06B vs 1.10B.** The 1.06B is SEQ ALL as reported in the H1 report. I found nothing reconciling the 1.10B GenomeWeb figure. It likely includes other sequencing-related lines or different scope, which is an inference. It stays unresolved until the PDF is read.
- **Not obtained:** China/domestic vs overseas split, clinical, NIPT and oncology comments, T7+/T20 placements, per-product gross margin, and price per Gb. The 10jqka and weeklyonstock articles state these are not covered.
- **Gross margin outlook.** One search summary says "projected gross margins are estimated at 60.5% for 2026" for SEQ ALL. I could not verify this and it is probably garbled.

## Contradictions and stale data

- **$4,398M** has no source in the corpus. Likely the conflict arises from the core/consolidated and GRAIL-timing bases ($4,332M vs $4,372M). See above.
- **FY23 China $384M** is not read from filing text. It comes from a search snippet plus the consensus sheet.
- **Mistranslation risk.** The search-tool MGI figures use "billion" where RMB 100M units (亿) apply. All MGI numbers above are secondary until the PDF is read.

## Gaps / what I could not find

- MGI H1'26 detail: the domestic/overseas split, China share, clinical, NIPT and oncology adoption, T7+/T20 placements, and price per Gb.
- The 10-K segment note table (revenue by region), and China-specific consumables or clinical commentary in the MD&A. The WebFetch excerpts ended before the financial statements.
- China's share of clinical consumables, and China clinical growth. Both are undisclosed.
- Illumina's Q4'25 press release returned 403 and the Q4'25 IR PDF returned 404.

**Sources:**
- [Illumina FY25 10-K](https://www.sec.gov/Archives/edgar/data/1110803/000111080326000024/ilmn-20251228.htm)
- [Illumina FY24 10-K](https://www.sec.gov/Archives/edgar/data/1110803/000111080325000019/ilmn-20241229.htm)
- [10jqka, MGI H1'26, 2026-08-22](https://stock.10jqka.com.cn/20260822/c679192132.shtml)
- [weeklyonstock, MGI H1'26, 2026-08-21](https://static.weeklyonstock.com/26/0821/ABB2621301779398.html)
- [MGI H1'26 report PDF (cninfo)](https://static.cninfo.com.cn/finalpage/2026-08-22/1225493542.PDF)
