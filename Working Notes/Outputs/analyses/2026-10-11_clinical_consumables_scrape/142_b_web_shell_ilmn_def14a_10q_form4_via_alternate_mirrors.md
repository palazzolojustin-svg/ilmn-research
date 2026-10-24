# Agent 142: B-web-shell-ILMN-DEF14A-10Q-Form4-via-alternate-mirrors

*Model: sonnet. Run 2026-10-11 12:10:28. Cost $0.42 (API-equivalent).*

**Assignment:** Shell-capable agent. Open gap 8 is still unresolved after about 12 attempts, so use routes not yet tried. Try these in order and stop at the first that works. (a) PowerShell Invoke-WebRequest or curl.exe with the header 'User-Agent: Research palazzolojustin@gmail.com' against https://www.sec.gov/Archives/edgar/data/1110803/000119312526149669/ (DEF 14A, accession 0001193125-26-149669) and the 10-Q folder for ilmn-20260628. (b) data.sec.gov/submissions/CIK0001110803.json for the filing list, then the primary documents. (c) The Illumina IR site (investor.illumina.com) proxy PDF and the 10-Q PDF. (d) Mirrors: last10k, stocklight, secform4.com, openinsider.com, and sec.report. Save the files to Outputs/datasets and grep them locally. Extract and quantify: AIP metrics, weights, thresholds and payout percentages for FY25 and FY26, and any change from FY24 (for example a revenue, EPS or free-cash-flow swap, or exclusion of tariff or China effects). FY26 PSU design (876K at $161.80) and the performance metric and TSR comparator group. CEO and CFO realized pay, clawback and hedging policy. The Q2'26 10-Q: gross margin wording, the consumables margin driver, the tariff and China risk-factor changes versus the Q1'26 and Q2'25 10-Qs, Note 8 or legal contingencies, and customer concentration. All Form 4s since 2026-01-01: insider name, date, code (S, F, M, A), shares, price, and whether a 10b5-1 plan is noted. Output a table of the sales and total dollars sold by insider, and a table of metric changes with exact quotes. Hard stop at 20 minutes.

Status: I have no shell in this session, only WebFetch and WebSearch, so I couldn't run the curl route. I tried the SEC, mirror and IR-site routes through WebFetch instead. The Form 4 data came back, but the proxy and 10-Q text did not.

## Key findings

1. **Form 4 sales since 2026-01-01 were retrieved from secform4.com.** I found no Form 4 transactions between 2026-01-01 and 2026-03-05. That is the site's coverage, not proof that none exist. The ledger already notes a Cunningham plan termination on 9 Feb 2026 and a Leckman sale on 18 Feb 2026. The site's earliest listed entry is 2026-03-05, so it probably omits those. FACT [secform4.com/insider-trading/1110803.htm, fetched 2026-10-11].
2. **Meister's six sales total about 3.06M shares and $591.1M.** This corrects E150/E165. The ledger's recomputed figure was ~3.02M shares and ~$586M. Summing secform4's six sale rows gives $591.1M. That matches the earlier $591M figure and is not a different number. FACT (my arithmetic on mirror data).
3. **Meister's sales ran on a stepped price ladder, from $145 in May to $227 in late August.** Table below. FACT.
4. **The only officer sales are small, and the CEO and CFO made none.** Thaysen's only 2026 entry is tax withholding of 1,303 sh at $293.69 on 2026-10-05, which matches the ledger. FACT.
5. **The Q2'26 10-Q confirms two items already in the ledger (E149).** The gross margin is 66.4% versus 65.6% in Q2 2025, and the PSU wording is unchanged. The quote: "resumed issuing PSU for which the number of shares issuable is based on our performance relative to specified earnings per share targets (EPS PSU)". FACT [10-Q ilmn-20260628, acc. 0001110803-26-000160].
6. **The exact "consumables" line in the 10-Q is $852M versus $811M (+4.8%).** I did not find it in the ledger. It is not the same as the $775M sequencing consumables figure. It is probably the whole consumables line including non-sequencing products. Cost of product revenue was $291M versus $276M. FACT.
7. **Greater China revenue was $56M in Q2'26 versus $63M in Q2'25 (−11%).** The 10-Q footnote says the region "includes revenue from China, Taiwan, and Hong Kong". FACT.
8. **Julie Coletti appears as the new Chief Legal Officer.** Her Form 3 and a 29,377-share award at $0 were filed 2026-09-08. Davies appears as the prior Chief Legal Officer, with his last sale on 2026-07-30. This is consistent with the ledger's Form 3 note, but I did not find the role change documented there. FACT.

## Form 4 sales by insider (2026)

| Insider | Dates | Shares sold | Total $ | Notes |
|---|---|---|---|---|
| Meister (director, Corvex) | 13 May to 2 Sep | 3,059,258 | ~$591.1M | Six sale rows; prices $145 to $227 |
| Ericksen (Chief Accounting Officer) | 28 May | 2,000 | $305,150 | at $152.57 |
| Wedel (SVP Strategy) | 6 May, 18 Aug | 1,733 | ~$295,168 | $139.04 and $191.52 |
| Davies (Chief Legal Officer) | 29 May, 25 Jun, 30 Jul | 1,845 | $332,100 | 615 sh each at $160, $180, $200 |
| Leckman (Chief People Officer) | 2 Jun, 5 Jun | 1,567 | ~$254,373 | $162.08 and $162.59 |

The Davies sales are a price ladder at round numbers ($160, $180, $200), which looks like a standing limit-order plan. That is OPINION. The 10b5-1 flags were not shown on the mirror. The ledger already records that Meister's 10b5-1 box was unchecked.

Meister's individual sales:

| Date | Shares | Price | Proceeds |
|---|---|---|---|
| 13 May | 329,460 | $145.49 | $47.9M |
| 28 May | 669,596 | $159.86 | $107.0M |
| 4 Aug | 741,127 | $199.91 | $148.2M |
| 19 Aug | 679,574 | $214.19 | $145.6M |
| 25 Aug | 375,941 | $226.74 | $85.2M |
| 2 Sep | 263,560 | $217.03 | $57.2M |

- Meister also had option exercises and "Other" rows on 7 May, 11 May, 12 May and 28 May. The 12 May and 28 May exercises were paired with equal-size "Other" rows, which look like cash settlement of options at $102.82 strike. The ledger's 12 May equity-swap termination is consistent with this.
- The ledger's E165 says the peak sale price was $231.23 on 27 Aug. That is an intraday price on a Form 4 I did not see. Secform4 shows the 25 Aug sale at $226.74 as the highest weighted average, so the two are not in conflict.
- Director grants are routine: 2,072 options each on 21 May and small quarterly grants. Barnard received option awards on 5 Mar, and Sullivan, the Chief Commercial Officer, received awards on 5 Aug. These are not discretionary trades.

## Contradictions and stale data

- **E150 and E165 total:** use ~3.06M shares and ~$591M. The "~$586M" correction looks like a slight undercount.
- **E149 PSU conflict:** the Q2'26 10-Q again says EPS PSUs "resumed". The proxy extract says the 2025 grants had no EPS PSUs. These are consistent if the resumption applies only to 2026 grants. Whether that is true is unverified.
- **Filing list:** data.sec.gov's list is not reliable for form types. The fetch returned 0001011438-26-000553 as a 10-Q dated 2026-08-20. The ledger already warns that accession prefixes and labels are unreliable. The same fetch also said "no DEF 14A in 2026", which is wrong because the proxy is accession 0001193125-26-149669.

## Gaps / what I could not find (gap 8 remains open)

- **DEF 14A CD&A:** I fetched `d13789ddef14a.htm` and the `.txt` file. WebFetch truncated both before the CD&A, which starts around proxy page 45. The AIP weights, thresholds, payout curve, FY26 PSU design and TSR peer group, clawback and hedging policy, and CFO realized pay are all still unread. The 77% payout and the "revenue and non-GAAP operating income" wording were already in the ledger from search snippets.
- **FY24 comparison:** I did not retrieve the FY24 proxy (`000119312525076900`) either, so I can't say whether the metrics changed.
- **10-Q narrative:** WebFetch truncated the 10-Q before the MD&A and risk factors. I could not get the consumables margin driver wording, the risk-factor changes against Q1'26 and Q2'25, the legal contingency note, or customer concentration. The tariff and China language I saw is only the forward-looking-statements boilerplate: "unreliable entities list" and tariffs "announced... beginning in April 2025". I found nothing on customer concentration.
- **SomaLogic and CVR items:** the 10-Q shows a $40M GRAIL CVR liability at 28 Jun 2026, and up to $75M of SomaLogic contingent payments ($25M for 2025 performance, $50M for 2026). It also mentions a $30M early buyout after quarter-end. I did not check whether the ledger has these. They are not about consumables.
- **Untried routes:**
  - The IR site returned 403 for the one static file I tried.
  - openinsider.com refused the connection.
  - I did not try sec.report or stocklight.
  - I did not open the individual Form 4 XML files, so I couldn't confirm the 10b5-1 checkbox or the transaction codes (S, F, M, A).
- **Next step:** a shell-capable run is still needed. The command would be `curl.exe -A "Research palazzolojustin@gmail.com" -o proxy.htm https://www.sec.gov/Archives/edgar/data/1110803/000119312526149669/d13789ddef14a.htm`, followed by grepping for "Annual Incentive", "threshold" and "rTSR".
