# Agent 115: 116-web-ILMN-governance-via-EDGAR-mirrors-and-IR-site-8K-Item-2.05-5.02-Q4-25-SGA-adjustme

*Model: sonnet. Run 2026-10-11 10:54:34. Cost $1.12 (API-equivalent).*

**Assignment:** Close open gaps 1 and 2 from 00_open_gaps.md, which many earlier agents could not complete because direct sec.gov access failed. Do NOT rely on sec.gov. Use mirrors and Illumina's own site: investor.illumina.com (press releases, the Q4'25 earnings release PDF with its non-GAAP reconciliation tables, and the SEC filings tab), stocktitan.net, sec.report, last10k.com, secdatabase.com, fintel.io, openinsider.com, secform4.com, quiverquant.com, marketscreener.com, tipranks, simplywall.st, gurufocus, Justia, and Wayback Machine copies of sec.gov URLs (web.archive.org). Also try the data.sec.gov JSON endpoint via a plain fetch with a User-Agent string if the tool allows.

Targets, in priority order: (1) Q4'25 earnings release reconciliation. Get the SG&A non-GAAP adjustment footnote behind the $0.30 per share (~$47M) item, against $0.04 in Q4'24: what was it (legal, restructuring, GRAIL-related, acquisition, litigation reserve, executive transition?). Also get the add-backs by category for Q4'23 to Q4'25. (2) The Item 2.05 (restructuring) 8-Ks from 2023-06-26 to 2025-01-14 and the Item 5.02 (officer changes) 8-Ks from 2023: the dollar charges, the headcount, and the dates, with any exec departures such as CFO or CEO transitions, severance and any 'performance-based award' changes. (3) The 7 Aug 2026 8-K (Items 8.01 and 9.01): what it announced. (4) Any Illumina Form 4 filings and 10b5-1 plan adoptions by Jacob Thaysen, Ankur Dhingra, and other Section 16 officers from Jan 2025 to Oct 2026: totals sold, price, % of holdings and timing relative to earnings or the 35B and X-share disclosures. (5) The 2026 DEF 14A: which compensation metrics changed from 2024 to 2025 to 2026 (revenue, non-GAAP operating margin, EPS, relative TSR, any new 'NovaSeq X transition' or 'clinical' metrics), and any non-GAAP adjustment to bonus payouts. Return exact figures, quotes and URLs. Say plainly what you could not access.

## Key findings

1. **The Q4'25 SG&A add-back of $0.30 per share (about $46M) is now itemized.** (FACT, from the Illumina Q4'25 press release, 2026-02-05, fetched via illumina.com.) GAAP SG&A was $310M and non-GAAP SG&A was $264M.
   - Acquisition-related: $21M.
   - Transformational initiatives: $6M.
   - Other: $19M, footnoted as a "$19 million donation to the Illumina Foundation".
   - The three items sum to $46M. This resolves open gap 1.

2. **The "Other" item is a charitable donation, not a legal reserve.** (FACT.) The $19M donation to the Illumina Foundation was excluded from non-GAAP SG&A in the quarter.
   - A web search summary of the 10-K called it "non-cash". That is unverified, because my 10-K fetch returned no MD&A text.
   - Excluding a recurring-style corporate cost adds about 1.6 points to non-GAAP operating margin on Q4 revenue of roughly $1.16B. That revenue is my inference from the 23.7% non-GAAP margin and $275M non-GAAP operating profit.
   - It is the first "Other" bucket in this series, and the add-back categories changed from Q4'24 (see finding 4).
   - OPINION: this is a quality-of-earnings flag. Non-GAAP margin, which is also a compensation metric, benefits from the exclusion. See the gaps section on whether bonus results were adjusted.

3. **The acquisition-related bucket is defined broadly.** (FACT.) The footnote reads: "Amortization of intangible assets, fair value adjustments on contingent consideration liabilities, and legal/other expenses for SomaLogic acquisition and GRAIL legal expenses." The Q4'25 acquisition-related add-back of $21M therefore bundles GRAIL legal costs with SomaLogic deal costs and contingent-consideration remeasurement.

4. **Further SG&A reconciliation figures, with one caveat.** (FACT, press release.)

   | Period | Acquisition-related | Transformational initiatives | Other | GAAP SG&A | Non-GAAP SG&A |
   |---|---|---|---|---|---|
   | Q4'25 | $21M | $6M | $19M | $310M | $264M |
   | Q4'24 | $7M (the reversed sign suggests a credit) | $15M | none | $279M | $271M |
   | FY25 | $16M | $39M | $22M | $1,086M | $1,009M |
   | FY24 | $227M (sign as shown) | $58M | none | $900M | $1,069M |

   - The FY25 "Other" of $22M is the $19M donation plus $3M for "board membership changes".
   - Transformational initiatives are defined as "Employee severance costs related to restructuring activities and ERP system upgrade implementation costs."
   - Treat the FY24 row and the Q4'24 acquisition-related sign with caution. GAAP SG&A of $900M below non-GAAP SG&A of $1,069M is implausible on its face. It most likely reflects the 2024 reversal of the European Commission fine and GRAIL items. The fetch tool summarized the table rather than reproducing it. Verify against the PDF before relying on those two items.

5. **The per-share table lists a separate "Legal contingency" line of $0.05 in Q4'25** (FACT, same release). It is separate from the SG&A line. I could not see its nature. The same summary showed an "Other income" item of $(1.25) per share, which probably relates to GRAIL or investment gains. GAAP diluted EPS was $2.16 against non-GAAP $1.35. Non-GAAP operating profit was $275M (23.7% margin), against GAAP $202M (17.4%).

6. **The 7 Aug 2026 8-K is a litigation settlement, not an operating event.** (FACT, Items 8.01 and 9.01, accession 0001110803-26-000168, https://www.sec.gov/Archives/edgar/data/0001110803/000111080326000168/ilmn-20260807.htm.)
   - The case is Icahn Partners LP et al. v. Francis deSouza et al. (Del. Ch., C.A. No. 2023-1045-PAF), over the GRAIL acquisition.
   - The release agreement is effective 21 Aug 2025. It provides mutual releases and "no payment from any party".
   - The action is dismissed with prejudice as to plaintiffs only. A court approval hearing is set for 2 Nov 2026 at 1:30 pm ET.
   - Defendants named are deSouza, Thompson, Arnold, Dorsa, Epstein, Gottlieb, Guthart, Schiller and Siegel, who deny the allegations.
   - Stating a settlement that took effect in Aug 2025 only in an Aug 2026 8-K is a timing point. I did not establish whether it was disclosed earlier.

7. **The "seven or more Item 2.05 8-Ks" are mostly amendments to two original events.** (FACT.)
   - **Original 2023 event:** 8-K filed 2023-06-26, report date 2023-06-21 (acc. 0001110803-23-000048).
     - Reduction-in-force charges were estimated at "approximately $25 - $35 million", mostly severance and benefits, with the majority in Q2'23.
     - Management said it would "reduce its annualized run rate expenses by more than $100 million in 2023". No headcount percentage appears in the filing.
     - A real-estate plan was approved on 22 Jun 2023 to exit the i3 campus in San Diego (about $60M of assets) and evaluate the Foster City campus (about $186M). No charge estimate was given at that point.
   - **Amendments to the 2023 event:** 8-K/A filings on 2023-11-13, 2024-01-09, 2024-05-03 (acc. 0001110803-24-000025) and 2025-01-14 (acc. 0001110803-25-000011).
     - The May 2024 amendment reports a $43M Q4'23 impairment on Foster City right-of-use assets and leasehold improvements.
     - It also reports Q1'24 impairments of $18M (right-of-use) and $14M (leasehold improvements), for $75M in total.
     - About $142M of related assets remained at 31 Mar 2024.
     - The Jan 2025 amendment gives Q1'24 impairments of $32M and a Q4'24 right-of-use impairment of $14M. It says the Foster City portion and another San Diego property were exited in Q1'24, with no assets left on that property.
     - The Jan 2025 amendment says "Both charges will be excluded from non-GAAP financial metrics."
     - Foster City options for the remaining space are still being evaluated.
     - The $43M, $32M and $14M figures sum to $89M of facility impairments across Q4'23 to Q4'24. The $75M-versus-$89M difference is the extra $14M Q4'24 charge, since the Q1'24 pieces tie ($18M + $14M = $32M).
   - **GRAIL spin event:** 8-K dated 2024-06-03 (acc. 0001193125-24-153239), Items 2.05 and 8.01, with an 8-K/A on 2024-06-27 (acc. 0001110803-24-000038).
     - Incremental charges were estimated at "$35 - $50 million, primarily comprised of cash expenditures relating to legal and advisory fees", mostly in Q2'24 and substantially all by Q3'24.
     - Possible goodwill impairment was flagged but not estimable. GRAIL balance-sheet items were goodwill of $1,466M, R&D of $561M and intangibles of $2,092M.
     - Terms: at least 85.5% of GRAIL distributed on 24 Jun 2024 at one GRAIL share per six ILMN shares (ticker GRAL).
   - This matches the ledger correction that no 8-K in the listed accession set carried a fresh Item 2.05. These are amendments, not new programs.

8. **The 2023 executive changes are confirmed from the filings.** (FACT, Item 5.02.)
   - **deSouza:** The 8-K for 2023-06-08 reports that his resignation, submitted 8 Jun, was accepted 11 Jun 2023 (acc. 0000950157-23-000666). He served as an adviser to 31 Jul 2023. The filing disclosed no severance or award terms. Interim CEO Charles Dadswell's arrangements were unchanged: "has not entered into, amended, or modified any plan, contract, agreement, grant or award".
   - **Thaysen:** The 8-K for 2023-09-05 (acc. 0000950157-23-000929) sets the CEO start date at 25 Sep 2023.
     - Pay terms: base salary $1,000,000; target bonus 125% of salary from 2024; annual equity $10M (70% PSUs, 30% RSUs).
     - Sign-on terms: $500,000 cash (clawback within two years); $3.5M replacement equity; and up to $1M of matching RSUs for stock he buys.
     - Change-in-control severance is two times base plus the greater of target or most recent bonus, with full equity vesting.
   - **CFO change:** Dhingra became CFO on 15 Apr 2024 (8-K 2024-04-09, acc. 0000950157-24-000591). Goswami moved to employee-adviser and left on 1 Jul 2024. His departure was stated as not the result of any disagreement.
     - Dhingra's package: $650K base, $500K one-time cash and $3.5M of equity.
   - **General counsel:** Dadswell was replaced on 3 Oct 2024 (acc. 0000950157-24-001364). Scott Davies became interim General Counsel and Secretary. Dadswell's terms: a lump sum equal to annual base salary, plus a separate $600,000 lump sum for completing adviser services through 31 Mar 2025. The adviser arrangement keeps his 2024 annual incentive award in place.
   - The CEO's target bonus rose from 125% to 150% of salary in FY25 (ledger E197 correction). That change is not in this 2023 8-K and was not re-verified here.

## Contradictions and stale data

- **Ledger E-numbers:** I found no contradiction with E152 or E164. I did not re-check the Form 4 data.
- **Ledger open gap 2 premise:** The seven or more "Item 2.05" filings are mostly 8-K/As on the 21 Jun 2023 event and the 3 Jun 2024 GRAIL event. There is no separate wave of new restructuring programs in that window.
- **SG&A reconciliation:** The FY24 and Q4'24 acquisition-related signs look odd. The figures came from a summarizing fetch tool, not a raw table. Treat them as unverified.
- **Foundation donation:** A web summary called it "non-cash". The press-release footnote says only "donation". Treat "non-cash" as unverified.

## Gaps / what I could not find

- **Q4'25 release PDF:** Both the s24.q4cdn PDF and the sec.gov Exhibit 99.1 path failed with 404 or 403 errors. The itemization above comes from the illumina.com press-release page via a summarizing fetch.
- **Add-backs by category for Q4'23 to Q3'24:** Not retrieved. Only Q4'24 and Q4'25 plus FY24 and FY25 totals are shown.
- **2026 and 2025 DEF 14A:** The Compensation Discussion and Analysis was truncated in both fetches.
  - I could not confirm the VCP metrics, weights, or any change to PSU design. A web-search summary says FY25 VCP had two equally weighted financial goals, with revenue named as one. The other is likely non-GAAP operating margin, but I did not see it stated.
  - A web-search summary also says a PSU grant uses 3-year relative TSR against Nasdaq Biotechnology Index peers, and another PSU uses three-year average operating margin for FY25–27.
  - I did not establish whether bonus results were adjusted for the $19M donation. That needs the raw proxy.
- **Form 4 and 10b5-1 data:** Not worked, beyond the ledger's existing data. Time was spent on the 8-Ks and the proxy.
- **Q4'25 DSO and receivables:** The 10-K fetch returned no MD&A, so no answer.
- **Headcount for the June 2023 reduction:** The 8-K gives no percentage. Press snippets say about 5% year-to-date, but I did not verify them.
- **"Legal contingency" $0.05 per share:** I could not see what it was.

Sources:
- [Illumina Q4'25 press release (illumina.com), 2026-02-05](https://www.illumina.com/company/news-center/press-releases/2026/5dc3da71-77d9-4286-8c21-70c83aacbcdc.html)
- [Illumina 8-K, 2026-08-07](https://www.sec.gov/Archives/edgar/data/0001110803/000111080326000168/ilmn-20260807.htm)
- [Illumina 8-K, 2023-06-26](https://www.sec.gov/Archives/edgar/data/1110803/000111080323000048/ilmn-20230621.htm)
- [Illumina 8-K/A, 2024-05-03](https://www.sec.gov/Archives/edgar/data/1110803/000111080324000025/form8-karestructuring5224.htm)
- [Illumina 8-K/A, 2025-01-14](https://www.sec.gov/Archives/edgar/data/1110803/000111080325000011/ilmn-20230621.htm)
- [Illumina 8-K, 2024-06-03](https://www.sec.gov/Archives/edgar/data/1110803/000119312524153239/d700243d8k.htm)
- [Illumina 8-K (deSouza), 2023-06-08](https://www.sec.gov/Archives/edgar/data/1110803/000095015723000666/form8-k.htm)
- [Illumina 8-K (Thaysen), 2023-09-05](https://www.sec.gov/Archives/edgar/data/1110803/000095015723000929/form8-k.htm)
- [Illumina 8-K (Dhingra/Goswami), 2024-04-09](https://www.sec.gov/Archives/edgar/data/1110803/000095015724000591/form8-k.htm)
- [Illumina 8-K (Dadswell), 2024-10-03](https://www.sec.gov/Archives/edgar/data/1110803/000095015724001364/form8-k.htm)
