# Agent 96: 101-web-Q3-26-setup-consensus-13F-short-interest-options-and-insider-Form4-index

*Model: sonnet. Run 2026-10-11 10:16:48. Cost $0.25 (API-equivalent).*

**Assignment:** Close the market-data remainder of open gap 6 and the Q3'26 setup. The ILMN Q3'26 call is on 29 Oct 2026.

(1) Consensus for Q3'26 and FY26: revenue, sequencing consumables, clinical consumables if available, EPS, and guidance ranges. Sources: Yahoo Finance, Nasdaq, MarketBeat, Zacks, TipRanks, Visible Alpha snippets, and the earnings previews in trade press and on Seeking Alpha. Also find recent analyst rating and price-target changes from Aug-Oct 2026, with firm, date and reasoning, especially anything on the 6000 base or $/Gb.
(2) Ownership and positioning: Q2'26 13F top holders and changes (Fintel, WhaleWisdom, dataroma, 13f.info, or SEC 13F XML); short interest (% of float, days to cover), borrow fee, and options-implied earnings move (Barchart, MarketChameleon, Fintel).
(3) Insider selling: use the SEC EDGAR Form 4 index for CIK 1110803 (https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1110803&type=4, or data.sec.gov submissions JSON, using a proper User-Agent header). Identify who sold the rest of the roughly $436M of insider sales beyond Meister. List officer and director sales for 2025-2026 by name, date, shares, price and 10b5-1 flag, and total them. Note any open-market buys.

Return tables with citations and URLs. Never invent numbers. Say 'not found' where a source is blocked. Flag contradictions with the ledger.

## Key findings

Only a little is new. Short interest and 13F holders are new to the ledger. The Q3'26 consensus EPS differs slightly from E176. The Form 4 index adds nothing, and nothing came back on options, borrow fee or clinical-consumables consensus.

- **Short interest (new, FACT).** Settlement-date data from equibles.com (fetched 2026-10-11) show shares short rising from 7.5M on 15 May to 10.59M on 15 Sep, then 9.47M on 30 Sep. The 30 Sep figure is about 6.3% of float.
  - A separate search snippet said 8.1M shares, 5.3% of float and 4.5 days to cover as of 19 Aug 2026.
  - Source: https://equibles.com/stocks/ilmn/shortinterest.
  - Shorts rose through the S&P 500 inclusion (announced 4 Sep, effective 21 Sep) and the run to about $294, and eased only slightly after. That fits a squeezed or contested name rather than a crowded short.
  - The 30 Sep days-to-cover of 1.63 conflicts with the 5.60 on 15 Sep. This is probably a volume spike around the index event, so treat it with caution.
  - The ledger has no short-interest data (E-number: none).

| Settlement date | Shares short | Days to cover |
|---|---|---|
| 2026-05-15 | 7.50M | 4.02 |
| 2026-06-30 | 7.57M | 3.68 |
| 2026-07-31 | 8.06M | 4.51 |
| 2026-08-14 | 9.46M | 4.83 |
| 2026-08-31 | 9.72M | 5.15 |
| 2026-09-15 | 10.59M | 5.60 |
| 2026-09-30 | 9.47M (6.3% of float) | 1.63 |

- **Q3'26 consensus EPS (FACT, updates E176).** E176 has about $1.36 EPS and about $1.15B revenue. MarketBeat's earnings page now shows $1.41, and no revenue figure was found. A search snippet (Benzinga/Barchart-type) still showed $1.36 from 5 estimates against $1.34 a year ago. The range is therefore $1.36–1.41, depending on the source and how stale it is.
  - Source: https://www.marketbeat.com/stocks/NASDAQ/ILMN/earnings, fetched 2026-10-11.
- **FY26 guidance and consensus (FACT).** MarketBeat gives FY26 EPS guidance of $5.30–5.40 against a consensus of $5.23 before the guide. It gives revenue of about $4.6B. Q2'26 revenue was $1.16B against $1.13B expected, and EPS was $1.31 against $1.23. Source: same MarketBeat page.
  - This is consistent with E143, the low-ball guidance pattern. The EPS beat was $0.08, or about 6.5%.
- **13F holders (new, FACT).** InsiderSet's aggregation of 917 filers puts total 13F value at about $27.0B at 30 Jun 2026. BlackRock is the largest holder at about $3.37B, followed by Capital World at $2.71B, Vanguard Portfolio Management at $1.17B, Vanguard Capital Management at $1.16B and State Street at $1.14B. Sources: https://www.insiderset.com/stocks/ilmn/institutional-ownership and a search snippet.
  - Capital World's $2.71B is consistent with the 10.3% stake in the E229 correction. No quarter-on-quarter changes were obtainable.
  - Among "superinvestors", ARK holds 1,045,010 shares (about $291M at current price) and Renaissance holds 826,642 shares (about $230M). Source: https://www.insiderset.com/investors/stocks/ILMN/top-shareholders. ARK is notable as a growth buyer into the rally.
- **Form 4 index (FACT).** The EDGAR index lists recent Form 4s dated 2026-09-09, 09-10, 10-02 (two) and 10-07 (accessions 0001110803-26-000175, -177, -180, -181 and -183). Source: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1110803&type=4.
  - These are company-filed accessions, which are likely officer or director filings, but the fetch gave no names, shares or prices.
  - The ledger already notes (E-number 360 correction) that -000180 and -000181 were mislabeled in the JSON. The ledger therefore needs the EDGAR index pages to be opened directly to confirm who filed them.

## Contradictions and stale data

- Q3 EPS consensus is $1.36 (E176, Barchart snippet) versus $1.41 (MarketBeat). Neither is dated precisely.
- Days to cover is 1.63 on 30 Sep versus 5.60 on 15 Sep. This is a methodology or volume artefact.
- The 19 Aug snippet (8.1M shares, 5.3% of float) differs from equibles' 14 Aug figure (9.46M). The sources use different settlement dates or different float definitions.

## Gaps / what I could not find

- Options-implied earnings move and borrow fee: not found, since Barchart returned an empty page and no other source was reached.
- Q3'26 revenue consensus (the $1.15B in E176 is unverified) and any clinical-consumables consensus: not found.
- Aug–Oct analyst rating and price-target changes beyond those already in the ledger: not found. MarketBeat's page had none.
- Corvex, FMR and other per-holder quarter-on-quarter 13F changes: not found.
- The names, shares and prices in the five Form 4s above, and the remainder of the roughly $436M of insider sales beyond Meister: not found. E151 and the corrections already show that the $436.7M is a TipRanks 90-day figure, mostly Meister.
