# Agent 46: 46-web-ILMN-primary-filings-CDA-10Q-note8-and-8Ks

*Model: sonnet. Run 2026-10-11 03:12:56. Cost $0.91 (API-equivalent).*

**Assignment:** Previous agents (22, 26, 30, 33, 38, 42) failed to read the primary text of key Illumina filings. Fetch raw documents from sec.gov/Archives (CIK 1110803; try the EDGAR JSON API data.sec.gov/submissions/CIK0001110803.json for accession lists, then the primary htm files; use a browser-like User-Agent with contact string if needed; fall back to the filing index, the .txt full submission, or secondary mirrors such as stocktitan, last10k, sec.report if sec.gov blocks). Targets: (a) 2026 DEF 14A (CD&A, filed ~Apr 2026): 2026 annual incentive plan metrics and weights vs 2025 (any metric changes, adjustments or exclusions, e.g. use of non-GAAP, operating margin vs EPS, revenue, NovaSeq X placement or clinical metrics), PSU design and TSR peer group, payout percentages for 2025 and how they compare to results, clawback, hedging and pledging policies, pay ratio, severance/CIC terms, CEO Jacob Thaysen total comp (SCT vs grant-date value), say-on-pay result; (b) Q2 2026 10-Q (period ending 28 Jun 2026, acc. 0001110803-26-000160): Note on legal proceedings/commitments (Element, EC fine, GRAIL divestiture residuals), purchase obligations, restructuring, inventory and the revenue disaggregation by consumables/instruments/region/clinical, any change in how revenue categories or 'clinical' are defined versus FY25 10-K, and risk-factor language changes; (c) all 8-Ks from Jan to Oct 2026 (executive appointments such as Coletti, departures, Reg FD, guidance, auditor changes, 10b5-1 notes); (d) Form 4s and 10b5-1 plan disclosures for the 24 months to Oct 2026 for Thaysen, CFO Ankur Dhingra, and other Section 16 officers: dates, shares, price, net dollars, and whether sales were under a plan. Quantify everything and quote exact wording of any changed metric or definition. Flag items that look like credibility issues. Stop after about 20 minutes and return what you have.

## Key findings

Little here is new, and the CD&A is still unread. WebFetch truncates the proxy before the compensation sections.

- **The CD&A (the proxy's compensation discussion) is still not read.**
  - I tried `d13789ddef14a.htm` and its `_htm.xml` XBRL file. Both returned only the table of contents, the introduction or the pay-versus-performance table.
  - A search snippet adds one fact for E197/E149. FACT/MGMT (search summary, not the CD&A text): the 2025 annual incentive was "a formula-based annual incentive plan with pre-established revenue and non-GAAP operating income goals", and funded at 77% for every named executive.
  - The same snippet describes the PSUs as "an equal portion vesting based on an average Operating Margin goal measured over a 3-year performance period and a portion vesting based on 3-year TSR performance relative to select companies in the Nasdaq Biotechnology Index", with payout of "0% to a maximum of 200%".
  - That description matches the 2025 proxy (accession 0001193125-25-076900) as much as the 2026 one, and I could not tell which year it came from.
  - The 2025 incentive metrics are therefore revenue plus non-GAAP operating income. The ledger did not previously state that. The 0-200% PSU range is unverified for the 2026 document.
  - The 2026 grants to Sullivan and Coletti are 0-250% EPS plus relative-TSR PSUs (E197/CORRECTION 264), so the PSU design or payout range appears to have changed between the 2025 and 2026 grants. This is OPINION until the CD&A is read.
- **Q2'26 10-Q Note 8 is Legal Proceedings and covers GRAIL shareholder litigation only.** FACT (XBRL R14, acc. 0001110803-26-000160, period ended 28 Jun 2026; read through a summarizer, not verbatim).
  - It covers derivative suits, one settled at "no payment by any party", and federal and state securities class actions. The state class was certified in May 2026.
  - It also covers two shareholder demands, which the board deferred in Feb 2026 pending the lawsuits.
  - The summarizer reported no dollar accrual and no Element, EC fine or SEC-investigation text in Note 8. This corrects the open-gaps expectation that Note 8 would cover Element and the EC fine. Element appears to be absent from the financial-statement notes, and the SEC investigation (E159) must sit elsewhere in the 10-Q, probably Item 1A or Part II.
- **Other Q2'26 10-Q notes (XBRL, via summarizer):**
  - R13 (Note 7): restructuring was nil in Q2'26 vs $39M in YTD'25. The GRAIL-divestiture indemnification liability is $1M. Government incentives recognized YTD'26 were $28M (consistent with E147). Inventory is $655M net, including $26M non-current. Accounts receivable is $773M gross with a $9M allowance.
  - R10 (Note 4): contingent consideration for SomaLogic and GRAIL sits in the investments and fair-value note.
  - R16 (Note 10): there is one reportable segment, and the note has no clinical or region disaggregation. The "clinical" label therefore exists only in earnings materials and calls, not in audited filings. This supports E077.
- **New financing filings (not in the ledger beyond E154's brief mention).** FACT, acc. 0001193125-26-345802 (filed 12 Aug 2026), -354010 (17 Aug) and 0000950157-26-000888 (13 Aug); fetched through summarizers.
  - Illumina issued $300M of 4.950% senior notes due 19 Sep 2029. The agreement was signed 10 Aug and closed 17 Aug.
  - The proceeds "together with cash on hand" repay the 4.650% notes due 9 Sep 2026. $500M was outstanding at 28 Jun, so about $200M comes from cash. The new coupon is 30 bp higher.
  - On 13 Aug 2026 the company signed a new $1,000M senior unsecured five-year revolver with Bank of America as agent. It carries a $50M swingline sublimit, a $75M letter-of-credit sublimit, an accordion or term-loan option of up to $500M, and a maximum total-leverage covenant. It matures 13 Aug 2031 with three one-year extension options. The 8-K carries Items 1.01, 1.02 and 2.03, so an older facility was terminated (not identified).
  - This shows no liquidity stress. The company issued $300M and refinanced $500M while buying back stock at an average of $124 in H1'26.
- **Jan 30, 2026 8-K (Item 2.01) records completion of the SomaLogic ("Standard BioTools proteomics") acquisition at $350M.** FACT (autobound.ai listing, secondary). It matches E146 and is not new.
- **8-K list for Jan–Oct 2026 (complete as of 11 Oct).** The EDGAR atom feed shows 13 filings:
  - 8 Jan: 5.02 and 7.01 (Cunningham resigns).
  - 13 Jan: 2.02.
  - 30 Jan: 2.01.
  - 5 Feb: 2.02.
  - 2 Apr: 5.02 and 7.01.
  - 30 Apr: 2.02 and 8.01.
  - 26 May: 5.07.
  - 23 Jun: 5.02.
  - 30 Jul: 2.02.
  - 7 Aug: 8.01 (Icahn notice).
  - 12 Aug: 8.01.
  - 13 Aug: 1.01, 1.02 and 2.03.
  - 17 Aug: 8.01.

  There is no Item 4.01 (auditor change) and no Item 5.02 for Sullivan or Coletti. They surface only through Form 4 and PSU-grant filings (accessions -169 and -177). Neither was announced by 8-K. FACT (absence, inferred from the list). A CLO and a CCO are not necessarily "named executive officers", so this is not a violation, but it is thin disclosure for the new CLO, who signed the 7 Aug 8-K.
- **Form 4s: one more officer sale confirmed, plus the Meister sales volume.**
  - Jakob Wedel Christensen (SVP Strategy/Corporate Development) sold 1,033 shares at $191.52 on 18 Aug 2026 under a 10b5-1 plan. He held 14,023 afterwards, so about $198K. FACT (Form 4 acc. 0001110803-26-000173).
  - Meister's 19–21 Aug Form 4 (acc. 0001193125-26-361476) shows 30 sales totalling about 628K shares at $201.59–$220.43. The 10b5-1 box is unchecked. This refines the E150 and E165 corrections, which already include 25–27 Aug and 2–4 Sep.
  - The Form 4 index shows no accession filed by an officer on 2026-06-01 (0001011438-26-000371, an agent filing) beyond what the ledger holds. I did not open it.

## Contradictions and stale data

- **Open-gaps item 4 and the 10-Q Note 8 expectation.** Note 8 contains no Element, EC-fine or SEC-investigation text. The Element dispute is not in the financial notes, which implies the company treats it as immaterial. FACT, from a summarizer, unverified verbatim.
- **PSU range and metrics (E197 vs E149).** The search snippet (operating margin plus relative TSR, 0-200%) matches the ledger's "op margin + rTSR" reading. The August–September 2026 grants (EPS plus relative TSR, 0-250%) match the 10-Q statement that EPS PSUs "resumed in fiscal 2026". Both can be true if the design changed for 2026 grants. Nothing here resolves which metric governs the March 2025 grant.

## Gaps / what I could not find

- **The CD&A text** is unavailable because WebFetch truncates the proxy. To fix it, download `d13789ddef14a.htm` locally with a tool that can save files, then grep for "Annual Incentive", "clawback", "pledg", "pay ratio" and "Change in Control". The needed items are:
  - the 2025 and 2026 AIP weights and thresholds;
  - adjustments or exclusions;
  - the rTSR peer group;
  - the $11.0M SCT vs $12.3M grants reconciliation;
  - severance and change-in-control multiples;
  - the pay ratio.
- **Q2'26 10-Q:** I could not read the purchase-obligation note, Item 1A risk-factor changes or the revenue-by-clinical disaggregation.
  - R pages for Notes 4, 6, 7, 8, 9 and 10 are mapped. R11, R12 and R17 onward are unread; commitments may be in R11.
  - Note 8 should be re-read verbatim. The summaries above are paraphrased.
- **Form 4s:**
  - I did not build a 24-month table.
  - The Form 4 filing list is mapped by date and accession, but only 0001110803-26-000173 and 0001193125-26-361476 were opened.
  - Thaysen's and Dhingra's discretionary sales, if any, and 10b5-1 adoption dates (in 10-Q Item 5) were not checked. Both look like Code F withholding only, per E152.
- **Not checked:** the 30 Apr 2026 8-K Item 8.01 content, the older credit facility terminated on 13 Aug, and the Apr 2 Reg FD exhibit.

No credibility red flags emerged from these filings beyond what the ledger already has. The nearest is the absence of 8-Ks for the new CCO and CLO.

Sources: SEC EDGAR filings and listings cited above (sec.gov/Archives/edgar/data/1110803/…); autobound.ai Illumina 8-K summary (secondary).
