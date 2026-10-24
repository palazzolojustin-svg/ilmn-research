# Agent 65: 65-web-ILMN-EDGAR-full-download-DEF14A-CDA-Form4-10Q-PartII-GRAIL-CVR

*Model: sonnet. Run 2026-10-11 03:50:16. Cost $0.53 (API-equivalent).*

**Assignment:** Close open gaps 5 and 8 on management conduct. Earlier agents were blocked by the fetch tool truncating long filings, so use Bash/PowerShell with curl and a declared SEC User-Agent (for example 'Research palazzolojustin@gmail.com'). Save full files to a temp folder and grep or read them locally by line range. Illumina's CIK is 1110803. Pull these in order: (1) DEF 14A, accession 0001193125-26-149669 (file d13789ddef14a.htm), from the CD&A onward. Extract the AIP (annual incentive plan) metrics, weights, thresholds, targets and actuals. Extract the 2026 PSU (performance share unit) metrics and the 2023-25 PSU payouts. Note any year-over-year metric changes: was a volume, pull-through, clinical or consumables metric dropped or added, and were any adjustments or discretion applied? Also extract the clawback and hedging policy, the CEO pay ratio and say-on-pay results, and related-party items. (2) Q2'26 10-Q, accession 0001110803-26-000160, Part II Items 1, 1A and 5. Capture the exact wording on the SEC investigation, the EC/Grail fine, Element, 10x and Roche litigation, and any 10b5-1 adoptions or terminations. Also reconcile the GRAIL CVR liability ($54M to $40M in Note 4) against the $32M favorable fair-value change cited in SG&A. (3) Form 4s filed 3 Aug to 7 Oct 2026 for Thaysen, Dhingra, Barnard, Sullivan, Meister and Corvex-related filers. Build a table with date, insider, transaction code (S/M/F/A), shares, price and 10b5-1 flag, plus a net-sold total in dollars. Also check for any Form 144. (4) 8-K Item 5.02 filings of 24-25 Mar 2025, 23 May 2025 and 2 Apr 2026, covering executive departures or changes and their stated reasons. Quantify everything and quote short phrases that matter. Label each point FACT, MGMT or OPINION and cite the accession number and URL. If a file cannot be downloaded, say so explicitly rather than guessing.

## Key findings

Most of the assigned filings could not be read in full. The fetch tool truncates long filings, and I had no shell or curl in this session, so I could not download and grep them. The items below are the new evidence I did get.

- **2026 PSUs include an EPS metric.** FACT: Michael Sullivan's Form 4 for 5 Aug 2026 shows two PSU lines of 5,254 shares each. One is EPS-based, with a payout of 0–250% on "three-year average consolidated non-GAAP EPS growth (2026-2028)", vesting 31 Dec 2028. The other is relative TSR (rTSR), 0–250%, for the year ending 31 Dec 2028 (acc. 0001110803-26-000169, https://www.sec.gov/Archives/edgar/data/0001110803/000111080326000169/form4.xml).
  - This settles the E149 conflict for 2026: EPS PSUs did resume in 2026, as the 10-Qs said. It also supports the ledger correction that 2025 PSUs were operating margin plus rTSR only.
  - The new EPS PSU rewards 3-year average EPS growth, not revenue, volume or pull-through. Buybacks and cost cuts lift EPS, so this metric does not tie pay to consumables volume.
  - The payout cap is 250%. The 2025 rTSR PSU cap was 175%. The 2026 rTSR cap also reads 250% in the Form 4, but that comes from a single new-hire filing.
- **Sullivan is a new Chief Commercial Officer.** FACT: His Form 3 has a 20 Jul 2026 event date and "no securities owned" (acc. 0001110803-26-000150). His 5 Aug grant is Code A: 4,503 RSUs at a $199.87 reference price, vesting 25% a year. The 10b5-1 flag is 0.
  - This is the replacement for Everett Cunningham, who resigned effective 16 Jan 2026. The commercial seat was empty for about six months.
  - Cunningham's departure is already in E164, but the Sullivan hire is not in the ledger.
- **Two Corvex Form 144s precede the Meister sales.** FACT, from Stocktitan (secondary source, https://www.stocktitan.net/sec-filings/ILMN/):

| Form 144 date | Shares proposed | Estimated value |
|---|---|---|
| 27 Aug 2026 | 200,000 | $44.97M |
| 4 Sep 2026 | 150,000 | $31.99M |

  - The matching Form 4s show larger sales: 375,941 shares on 27 Aug at $225.26–231.23, and 263,560 shares on 4 Sep at $213–221.55. That is 639,501 shares in total. The Form 4s do not tie to the Form 144 share counts.
  - This answers the ledger's open question on whether a Corvex Form 144 followed 4 Sep. The 144 was filed on 4 Sep itself.
  - The 10b5-1 flag is "No" on both Form 4s. That matches the ledger's "discretionary" label (E165).
- **Other insider filings, 3 Aug–7 Oct 2026.** FACT, from the same Stocktitan list. I did not see the raw XML, except for the Sullivan filing.
  - Thaysen, 7 Oct: Code F (tax withholding) of 1,303 shares at $293.69. No 10b5-1 plan, no discretionary sale.
  - Barnard, 9 Sep: Code F of 408 shares.
  - Coletti (Chief Legal Officer), 10 Sep: RSU and PSU grants totalling 23,377 shares.
  - Meister and Ullem, 2 Oct: Q3 director-retainer share receipts of 107 and 113 shares.
  - Dhingra: no filing appeared in this list. I could not confirm whether the 7 Aug filing in the gap list exists.
  - Net result: no discretionary open-market sale by any executive in this window. All discretionary selling was Corvex/Meister.
- **Say-on-pay support rose a little.** FACT, from the 8-K Item 5.07 vote results. Percentages are my calculation as for ÷ (for + against), excluding abstentions.

| Year | For | Against | Abstain | Support |
|---|---|---|---|---|
| 2025 (21 May 2025) | 115,560,563 | 11,450,964 | 3,517,311 | ~91.0% |
| 2026 (21 May 2026) | 121,746,792 | 8,464,596 | 404,097 | ~93.5% |

  - Sources: acc. 0001110803-25-000051 (https://www.sec.gov/Archives/edgar/data/1110803/000111080325000051/ilmn-20250521.htm) and acc. 0001110803-26-000124 (https://www.sec.gov/Archives/edgar/data/0001110803/000111080326000124/ilmn-20260521.htm).
  - The 2026 broker non-votes were 10,428,546.
  - Investors did not push back on pay, despite the AIP's 150% CEO target and the $11.0M CEO pay in E197.
- **The 2025 stock plan vote passed.** FACT: The Second Amended and Restated 2015 Stock and Incentive Plan was approved on 21 May 2025 with 124,234,469 for and 5,328,071 against (acc. 0001110803-25-000051).
  - The share-count increase is only in the 9 Apr 2025 proxy, which I did not read.
  - The 2026 share-based compensation line is rising: SG&A SBC was $41M in Q2'26 against $34M in Q2'25 (10-Q Note 7, acc. 0001110803-26-000160).
- **The 8-K 5.02s read as clean on their face.** FACT:
  - 25 Mar 2025 (acc. 0001110803-25-000032): Stephen MacMillan resigned as director effective 28 Mar. Keith Meister was elected the same day. The filing says the resignation "is not the result of any dispute or disagreement". It also says "no arrangement or understanding between Mr. Meister and any other person" governed his selection.
  - 2 Apr 2026 (acc. 0001110803-26-000082): Frances Arnold, Robert Epstein and Gary Guthart will retire as directors on 21 May 2026, with the same "not the result of any dispute" language. They are three of the directors who left the board that day. The 2026 vote shows nine nominees, against eleven in 2025.
  - 23 May 2025 (acc. 0001110803-25-000051): this 8-K was only the plan approval and vote results. It was not an executive departure.
  - OPINION: MacMillan left and Meister joined within three days. That is consistent with an activist-aligned board change, but the filing does not say so.
- **GRAIL CVR liability, partial check only.** FACT: Note 4 shows the liability falling from $54M (28 Dec 2025) to $40M (28 Jun 2026). That is a $14M decline. The CVRs pay 2.5% of the first $1B of GRAIL-related revenue each year and 9% above that, over 12 years to Aug 2033. The $32M favorable SG&A figure in E148 is still unreconciled.
  - Possible bridge (OPINION, unverified): the SG&A figure may combine the CVR with SomaLogic contingent consideration. SomaLogic contingent liabilities were $77M at 28 Jun 2026, and $30M was paid on 27 Jul 2026.
  - I could not read the MD&A to confirm this.

## Contradictions and stale data

- E149's PSU conflict is resolved for 2026 by the Sullivan Form 4: EPS PSUs plus rTSR. The "dropped from 2025" claim in F15 stays wrong.
- The ledger says Sullivan's role is unrecorded. He is the new CCO, with a Form 3 dated 20 Jul 2026.
- The Form 144 values (about $224.84 and $213.25 per share) are estimates from the notice. Realized Form 4 prices were $225.26–231.23 and $213–221.55, which are close.

## Gaps / what I could not find

- **DEF 14A CD&A:** the fetch tool returned only up to p.45, and the summary admitted the CD&A was not included. I got no AIP weights, thresholds or actuals beyond the 77% funding already in the ledger. I got no 2023-25 PSU payouts, no discretion or adjustment disclosure, and no clawback or hedging policy.
- **10-Q Part II:** Items 1, 1A and 5 were not in the fetched text. I found no SEC investigation wording, EC fine, Element, 10x or Roche text, and no 10b5-1 adoptions or terminations. The search snippets say Illumina's June 28 10-Q has a "Legal Proceedings" section (Note 8), but I did not read it.
  - From the earlier SEC probe (MedTech Dive, https://www.medtechdive.com/news/Illumina-SEC-ends-Grail-investigation-Q1/747691/): the SEC requested documents on the GRAIL acquisition and on "the conduct and compensation of certain members of Illumina and GRAIL management". The headline says the SEC ended that investigation in Q1. This is a secondary source, so confirm it.
  - The EC fine (€432M) was avoided after the Court of Justice ruling. I did not verify the 10-Q wording.
- **Form 4 table:** I have no per-row share totals for Thaysen (other than 1,303), Dhingra and Barnard beyond the Stocktitan summary. I could not build a net-sold dollar total for executives, because none sold discretionarily. The Corvex total is already in E150/E165.
- **Not read:** the 7 Oct Schedule 13G (0000315066-26-002340) and the CEO pay ratio detail (already in ledger).
- **Needed to finish:** a shell with curl and a declared SEC User-Agent for `d13789ddef14a.htm` and `ilmn-20260628.htm`.
