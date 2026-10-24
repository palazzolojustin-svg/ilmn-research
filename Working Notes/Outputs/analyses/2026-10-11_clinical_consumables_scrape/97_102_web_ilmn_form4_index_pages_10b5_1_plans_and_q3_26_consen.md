# Agent 97: 102-web-ILMN-Form4-index-pages-10b5-1-plans-and-Q3-26-consensus-options-short-interest

*Model: sonnet. Run 2026-10-11 10:22:57. Cost $0.55 (API-equivalent).*

**Assignment:** Close open gap 4 with primary pages, not search summaries. (1) Open the EDGAR filing index for Illumina (CIK 1110803) directly, for example https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1110803&type=4&dateb=&owner=include&count=40, or data.sec.gov/submissions/CIK0001110803.json. If a request is blocked, send a descriptive User-Agent, or use curl/Invoke-WebRequest or openinsider.com. Retrieve the Form 4s filed 2026-09-09, 09-10, 10-02 and 10-07, plus all Form 4s since 2026-01-01. For each one record: insider name and title, transaction code (S, M, F, A), shares, price, and whether it was under a 10b5-1 plan (footnote), with the date of plan adoption if stated. Also record post-transaction holdings. Total the open-market sales by insider (Thaysen, Dhingra, Goswami, Barnard and others) for 2026 against 2025. Note any 8-K Item 5.02 or Item 5.07 filings since July. (2) Find the Q3'26 setup before the 29 Oct call. Try Yahoo Finance analysis page, MarketChameleon, Fintel, Nasdaq/Zacks, TipRanks, Seeking Alpha earnings preview, and Stocktwits/Benzinga. Look for consensus Q3'26 revenue and EPS against the guide ($1.14-1.16B, EPS $1.33-1.38), the options-implied earnings move, short interest (shares and days to cover, latest FINRA date), borrow fee, and any post-July estimate changes or rating changes (Aug-Oct 2026), with price targets and the stated reasons. Quantify the average historical earnings-day move for the last 8 quarters. Flag anything you could not retrieve. Do not repeat agents 03, 33, 38, 42, 53, 57, 61, 65, 69, 77, 81 or 96 on high-level material; the aim is the missing transaction-level and market-implied numbers.

I've pulled the Form 4 filings, short interest and Q3 setup, and I'm now writing up the findings.

## Key findings

1. **FACT: The four Form 4s you named contain no open-market sales, and none was under a 10b5-1 plan.** Every filing has the 10b5-1 checkbox at 0 and no plan footnote. All come from the filing directories at sec.gov/Archives/edgar/data/1110803/. They are tax withholding (F), grants (A) or director fee shares (A). None is code S or M.
   - **9 Sep (filed 10 Sep, acc. 0001110803-26-000175):** Barnard Steven (SVP, CTO), code F, 408 sh at $211.06, 40,927 held after. No footnotes. The transaction date in the XML is 2026-09-05.
   - **8 Sep grants (filed 11 Sep, acc. -000177):** Julie Ann Coletti (CLO), code A, $0. She received two RSU grants (4,549 and 14,214 sh, 18,763 total) plus two PSU grants of 5,307 each. The RSUs vest 25% a year over four years, and a second RSU grant vests in thirds on 5 Sep 2027–2029. One PSU tranche pays on 2026–28 average non-GAAP EPS growth, vesting 31 Dec 2028. The other pays on relative total shareholder return (TSR) for the year ending 2028. Reading the XML through the fetch tool, the PSUs appear as a "derivative" table.
   - **2 Oct (filed 3 Oct, acc. -000180 and -000181):** Directors Ullem and Meister received 113 and 107 shares, code A, at $219.8037. These are Q3 board retainer fees taken in stock. Holdings after: Ullem 11,143; Meister 6,887 direct plus 770,350 indirect (the Corvex funds).
   - **5 Oct (filed 7 Oct, acc. -000183):** Thaysen (CEO), code F, 1,303 sh at $293.69, 107,770 held after. No footnotes.
   - The EDGAR company page and openinsider gave no extra detail. EDGAR listed only the filing dates 2026-10-08, 10-03 (two), 09-11 and 09-10. Those are one to two days later than the dates in the filing directories and in your assignment.

2. **FACT: Thaysen's 107,770-share holding is correct as of Oct 2026.** This updates E152. The "107,770" figure that the ledger called wrong for May 2025 (the "100 shares" purchase version) is the post-withholding count in the 5 Oct 2026 Form 4. Holdings were 82,089 (Oct 2025) and 83,339 (Feb 2026), so he gained roughly 24K shares between Feb and Oct 2026. That is consistent with vesting. The May 2025 purchase detail (12,350 sh at $80.86) is not contradicted.

3. **FACT: Blarkad's list of 2026 insider activity from May to October shows only five open-market sellers: Meister, Davies, Wedel, Leckman and Ericksen.** Source: blarkad.com/ticker/ILMN/insiders, fetched 2026-10-11. It lists no open-market sale by Thaysen, Dhingra, Goswami or Barnard in that window, and I did not check Jan–Apr. I did not total 2026 against 2025 by insider, because I could not retrieve the Jan–Apr 2026 or 2025 Form 4s at transaction level.
   - **Davies (Chief Legal Officer until Coletti, per E153):** 615 sh at $180.00 on 25 Jun and 615 sh at $200.00 on 3 Aug. Those round prices suggest limit-order plans.
   - **Wedel (SVP Strategy):** 933 sh at about $139 on 7 May and 1,033 sh at $191.52 on 20 Aug.
   - **Leckman (SVP People):** 784 sh on 4 Jun ($160.66–163.02) and 783 sh on 9 Jun ($161.79–167.88).
   - **Ericksen and Davies on 1 Jun:** the page says "multiple executives" sold on 1 Jun but gives no detail.
   - **Meister (Corvex, director):** the sale batches, which the ledger already has, are listed on Blarkad as 723,156 sh on 6 Aug, 611,248 on 21 Aug, 487,506 on 27 Aug and 370,118 on 4 Sep. Quantisnow gives average prices of $214.19, $226.74 and $217.03 for 679,574, 375,941 and 263,560 sh. Share counts do not match Blarkad batch for batch, probably because the filing dates differ. The fetch tool summarised these pages, so the figures are secondary.
   - **Sullivan (new CCO):** a code A grant of 15,011 sh on 7 Aug.
   - **Directors on 22 May:** eight directors each received 2,072 sh at $144.83.
   - **Skovronsky:** acquired 1,674 sh at $164.28 on 23 Jun.

4. **FACT: The options market implies a very large Q3 move.** Chartrow shows ±14.96% ($40.92). Unusual Whales shows ±14.14% ($39.33), "as of October 9, 2026". This is the first implied-move number for the ledger (gap 4). The earnings date and time (29 Oct after the close, call at 4:30 pm ET) are confirmed by a Finviz-listed press release.

5. **FACT: Short interest is falling.** MarketBeat and Equibles both show 9,471,310 shares short at FINRA settlement 30 Sep 2026. That is 6.3–6.46% of float and 1.6 days to cover, down 10.5% from 10,585,422 (the mid-September peak, 7.2% of float). Equibles projects about 9.0M for 15 Oct. A search snippet claimed 8.1M shares and 4.5 days to cover for August 2026. I did not verify it and it conflicts with the 1.6 days figure, so I would not use it. I did not find a borrow fee.

6. **FACT: Q3'26 consensus matches the ledger.** The Q3'26 EPS consensus is $1.36 on 5 estimates (Chartrow, Unusual Whales, a Finviz preview), against $1.34 a year ago. Revenue is about $1.15B, from a search snippet only. MarketBeat's $1.41 (E176 correction) is the outlier. Trailing figures from MarketBeat (2026-07-30 page): Q2'26 EPS $1.31 vs $1.23 consensus, revenue $1.16B vs $1.13B. Beats over the last four quarters were $0.08, $0.10, $0.09 and $0.18. FY26 guidance is $5.30–5.40 EPS and about $4.6B revenue. MarketBeat's $4.34B "annual revenue" is probably a trailing figure.

7. **FACT: Earnings-day history is thin and conflicting, so I cannot compute an 8-quarter average.**
   - **Oct 2025 (Q3'25):** Chartrow shows a +15.5% EPS surprise and a +24.8% stock surge. That is the largest reaction I found.
   - **Jul 2026 (Q2'26):** Chartrow and Unusual Whales both show "+0.0%" next-day move, which looks like a data-feed gap. A snippet from the TIKR blog (undated and unverified, so it may be from a different year) says shares "stumbled 10%" and cites "transition friction". I did not verify it.
   - MarketChameleon's historical table is paywalled.
   - The stock is up 33–36% since 30 Jul, so a 14–15% implied move is large against that run-up.

8. **FACT: Analyst actions in Aug–Oct 2026 from the web search were mostly stale.**
   - The TipRanks/The Fly items that surfaced are old: a TD Cowen downgrade on 4 Jan 2024 and a Piper cut to $275 on 15 Aug 2023.
   - These are not 2026 actions. Do not use them. I found no new 2026 rating changes beyond the ledger (E172, plus the Barclays $200 correction).

## Contradictions and stale data

- **E152:** the "107,770" Thaysen holdings number is valid for Oct 2026 but not for May 2025.
- **EDGAR dates:** the filing dates and the XML transaction dates differ by one to four days (for example Barnard: transaction 5 Sep, listed 9 Sep, filed 10 Sep).
- **Short interest:** 1.6 days to cover (FINRA 30 Sep) versus a 4.5-day snippet for August.
- **Q2 reaction:** +0.0% versus a possible −10% (see item 7).

## Gaps / what I could not find

- **Form 4s:** Thaysen/Dhingra/Goswami/other-insider sales for Jan–Apr 2026 and for 2025, so no 2026-vs-2025 totals. I also could not read the footnotes in the Davies, Wedel, Leckman and Ericksen Form 4s (10b5-1 adoption dates, post-sale holdings).
- **8-K Items 5.02 and 5.07:** the submissions-JSON summaries gave filing dates (2026-08-20, 08-21, 08-27, 09-04, 09-05) but no item numbers, and the ledger already flags those summaries as mislabelling form types. I did not open the 8-K indexes.
- **Options:** the implied move comes from two aggregators. I found no direct options chain, no expiry date and no skew.
- **Market data:** borrow fee, MarketChameleon and Fintel data, post-July estimate revisions and any 2026 rating-change reasons.
- **Yahoo analysis page:** it failed to load, and the Nasdaq short-interest page timed out.
- **Earnings-day moves:** the last 8 quarters.

Sources: the sec.gov Archives Form 4 XMLs listed above; blarkad.com/ticker/ILMN/insiders; quantisnow.com/insiders/ILMN; marketbeat.com/stocks/NASDAQ/ILMN/short-interest; equibles.com/stocks/ilmn/shortinterest; chartrow.com/quote/ilmn/earnings; unusualwhales.com/stock/ILMN/earnings; marketbeat.com/instant-alerts/illumina-nasdaqilmn-issues-quarterly-earnings-results-2026-07-30. All fetched 2026-10-11.
