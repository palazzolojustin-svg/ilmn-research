# Agent 133: 132b-web-ILMN-Sept-2026-conferences-sell-side-and-10Q-MDA-gross-margin-DEF14A-CD&A

*Model: sonnet. Run 2026-10-11 11:59:27. Cost $0.60 (API-equivalent).*

**Assignment:** Close open gap 8 and the unresolved primary-filing gaps using routes earlier agents did not use. (a) Find any Illumina appearance or transcript from 1 Aug to 11 Oct 2026 (Citi, Morgan Stanley, Wells Fargo, Baird, Barclays and similar September healthcare conferences). Try Quartr, MarketScreener, stocktitan.net, investing.com, seekingalpha headlines, GuruFocus, Yahoo Finance, the illumina.com IR events page and webcast archive. Quote anything on the NovaSeq 6000 tail, the 35B flow cell, clinical growth, Q3 guidance or the Jan 2027 price cut. (b) Fetch the Q2'26 10-Q MD&A gross-margin and consumables paragraphs, and the Part II legal note, from sec.gov/Archives (filing index, then the primary htm). Extract the exact wording on consumables margin drivers, price/mix, tariffs and any new risk-factor language about NovaSeq 6000 end-of-life or customer concentration. (c) Fetch the 2026 DEF 14A CD&A. Quantify the FY25 and FY26 incentive metrics (revenue, non-GAAP op margin, EPS, any clinical or NovaSeq X metric), the changes from FY24, the payout percentages, CEO and CFO pay and any metric definition changes. (d) Collect any post-30-Jul sell-side notes or price-target changes that state an explicit 6000, $/Gb or 35B assumption. Report exact quotes and URLs, and flag what could not be retrieved.

## Key findings

**Mostly NO NEW EVIDENCE.** No Illumina September 2026 conference appearance, post-30-Jul sell-side note with a 6000, $/Gb or 35B assumption, or Q2'26 10-Q MD&A text could be retrieved. Three small items refine ledger entries. They come from search-engine summaries of the DEF 14A, not from my reading the CD&A.

1. **AIP metric label resolved, and the weights are still unread (refines E149/E197/E220).** The 2026 DEF 14A, as quoted in search snippets, describes a "formula-based annual incentive plan with pre-established revenue and non-GAAP operating income goals tied to the budget and forecasts and targeting increases over 2024 performance". It says this gave a below-target 77% funding for 2025. [FACT; sec.gov DEF 14A, 0001193125-26-149669, https://www.sec.gov/Archives/edgar/data/1110803/000119312526149669/d13789ddef14a.htm; retrieved via search snippet 2026-10-11]
   - So the AIP metrics are revenue and non-GAAP operating income (dollars), not operating margin. That settles the label question noted in the E220 correction.
   - There is no clinical or NovaSeq X metric in the snippets. The thresholds, actuals and weights remain unread.

2. **CEO AIP range (corroborates E197).** Thaysen's threshold, target and maximum are $563,000, $1,500,000 and $3,000,000. [FACT; same DEF 14A via search snippet]
   - A 77% payout on the $1.5M target equals the ledger's $1,155,000.
   - The "$1.5M target" is my reading of the snippet. Treat it as consistent with the ledger, not independently verified.

3. **PSU structure for 2025 grants (corroborates the E149 correction).** Each executive's PSUs vest half on 3-year average operating margin and half on 3-year relative TSR against Nasdaq Biotechnology Index companies. The performance period ends 2 Jan 2028 and payout ranges from 0% to 250%. [FACT; same DEF 14A via snippet]
   - The snippet says the operating-margin goals "will be disclosed after the end of the performance cycle". Investors cannot see the margin hurdle until 2028.
   - There is no EPS or revenue PSU in the 2025 grants. This again conflicts with the 10-Q's "EPS PSUs resumed in fiscal 2026". The 2026 grants (876K PSUs at $161.80) are still uncharacterised.

4. **Non-GAAP gross margin (secondary-source figures, likely already known).** Q2'26 non-GAAP gross margin was 68.2% against 69.4% in Q2'25, and GAAP was 66.4% against 65.6%. [FACT; search summary of the Q2'26 release, https://www.illumina.com/company/news-center/press-releases/2026/29026.html]
   - Non-GAAP gross margin fell about 1.2 points y/y while the ledger notes consumables mix shifting to the X. I could not get the cause from the 10-Q MD&A.
   - Check this against the ledger's gross-margin entries.

## What I checked

- **September conferences.** I found no Illumina press release, transcript or webcast after 30 Jul 2026. The latest conference item found was the TD Cowen fireside chat on 3 Mar 2026 (announced 17 Feb 2026).
  - The September calendar included Wells Fargo (8-10 Sep), Citi (9-10 Sep), Cantor (9-11 Sep), Morgan Stanley (14-16 Sep) and Baird (15-16 Sep). I found no confirmation that Illumina attended any of them. [The M&A Hunter, https://maandhunter.substack.com/p/september-2026-biotech-conference]
  - The investor.illumina.com events page returned 403. Quartr, MarketScreener, StockTitan and GuruFocus were not reached. Absence of evidence is not proof of absence.
- **Sell-side.**
  - The "Daiwa upgrade to Buy, PT $154" that surfaced in search is dated 16 Aug 2024, so it is stale. [TipRanks/The Fly, https://www.tipranks.com/news/the-fly/illumina-upgraded-to-buy-from-neutral-at-daiwa]
  - A Simply Wall St narrative page cites a "$206.65" analyst price target as of 30 Sep 2026, with no broker or explicit 6000/$/Gb/35B assumption. [OPINION; low reliability]
  - The Citi downgrade to Neutral surfaced without a retrievable date or text.
  - Nothing states a 6000, $/Gb or 35B assumption.
- **Q2'26 10-Q** (acc. 0001110803-26-000160, https://www.sec.gov/Archives/edgar/data/0001110803/000111080326000160/ilmn-20260628.htm). The fetch tool returns only the front part, ending at the financial-statement notes.
  - MD&A gross-margin wording, tariff language, new risk factors on 6000 end-of-life or customer concentration, and the Part II legal note were not retrievable.
  - The direct EDGAR viewer fetch returned only navigation.
- **DEF 14A CD&A.** The fetch truncates before the CD&A, which starts on page 45. The full CD&A, FY24-to-FY25 metric changes, FY26 AIP design, CFO pay and AIP weights and actuals remain unread.

## Contradictions and stale data

- The Daiwa PT of $154 is 2024 and should not be used as a current data point.
- The EPS-PSU conflict between the 10-Qs and the proxy persists (see E149).

## Gaps / what I could not find

- **CD&A and 10-Q MD&A text.** A different retrieval route is needed. The options are downloading the filing locally, or an agent with shell access running curl against sec.gov with a User-Agent header and reading the page ranges with the Read tool.
  - The 10-Q is 8 MB and the proxy htm is 1.2 MB. The proxy's R pages are XBRL data only.
- **Illumina's events page** (403 from sec.gov-style fetches) and the transcript aggregators (Quartr, MarketScreener, StockTitan) were not reached.
- **Sell-side notes.** Broker PT changes after 30 Jul 2026 with explicit 6000, $/Gb or 35B assumptions were not found. The next real test is the Q3'26 call (~29 Oct).
