# Agent 33: 33-web-EDGAR-raw-governance-DEF14A-Form4-8K

*Model: sonnet. Run 2026-10-11 02:48:43. Cost $0.71 (API-equivalent).*

**Assignment:** Close the governance and insider gaps by going to raw SEC EDGAR files, not search extracts. Use sec.gov/cgi-bin/browse-edgar and sec.gov/Archives/edgar/data/1110803/ (Illumina CIK 1110803) and fetch the primary documents directly. Prior agents 22, 26 and 30 got only summaries and 403s, so if a URL fails, try the filing index page, the -index.htm page, or the XML version of the Form 4 (the raw ownership XML).

1) Open the 2026 DEF 14A (filed about April-May 2026). Extract: annual bonus metrics and weights and any adjustments or discretion; the 2026 PSU design (EPS PSUs 'resumed in fiscal 2026', relative TSR peer group, performance ranges 0-200% vs 0-250%); changes to compensation metrics versus 2024 and 2025; clawback and hedging policy; Thaysen's 2025 Summary Compensation Table total vs equity grants ($11.0M vs $12.3M); CEO pay ratio; say-on-pay result from the 2025 proxy and the 2026 8-K Item 5.07.
2) List every Form 4 since 1 Jan 2025 for Thaysen, Dhingra (CFO), Goswami, Barnard, Meister, the general counsel and directors. For each, record date, transaction code (S, M, F, A, G), shares, price, whether it was under a 10b5-1 plan, and the holdings after. Compute net open-market selling in $ by person and by quarter, and flag clusters before or after earnings or guidance changes. Reconcile Meister's 44,500-share gap (look at swap termination and May-Jun 2026 filings).
3) Check 8-Ks since 2025 for Item 5.02 (executive departures, compensation changes), Item 4.01 (auditor change), and Item 2.02 exhibits showing non-GAAP definition changes. Check Corvex 13D/G, Schedule 13G holders over 5%, and the S&P index announcement date.
Quantify every figure and give accession numbers. Hard stop at 20 minutes; return a table of insider transactions and a list of compensation-metric changes with the filing citation.

## Key findings

Status: I stopped here. The 1.2MB proxy and the Meister Form 4 XMLs would not open, so those items stay unresolved. EDGAR browse pages, filing directories, small 8-Ks, small Form 4 XMLs and the proxy's XBRL file did open. WebFetch passes each page through a summarizer, so every number below is summarizer-extracted rather than read raw. Treat the details as unverified until checked against the filing.

1. **Thaysen's pay figures are now primary-sourced (XBRL, DEF 14A, 0001193125-26-149669, filed 2026-04-09).** FACT:
   - 2025 Summary Compensation Table (SCT) total is **$11,018,895**, and "compensation actually paid" (CAP) is **$12,832,816**.
   - 2024 was $14,802,924 SCT and $17,689,413 CAP. 2023 was $4,691,233 SCT and $4,439,576 CAP.
   - The "$12.3M" in the ledger is therefore not a SCT or CAP figure. I could not locate it. Only part of the 2025 grant was visible (see finding 2).
   - The company-selected measure in the pay-versus-performance table is revenue ($4,343M in 2025 vs $4,332M in 2024). That is not the net income line, and it matches the AIP's revenue metric.
   - Net income is reported as +$850M in 2025 against −$1,223M in 2024.
   - Illumina's TSR value in the table is 36.47% (2025), against the NASDAQ Biotech Index at 122.07%.

2. **2025 grant detail for Thaysen (search extract of the same DEF 14A; not verified from the filing itself).** FACT:
   - Cash incentive target was $1.5M with a $3.0M maximum.
   - Two PSU grants on 2025-03-05: 33,493 target shares, grant-date fair value (GDFV) $3,433,033, and 33,493 target shares, GDFV $2,870,015.
   - 28,709 RSUs, GDFV $2,460,074.
   - These three grants sum to about $8.76M. The remaining part of the $12.3M figure is not visible.
   - The PSU footnote reads: "three-year average consolidated non-GAAP earnings per share growth for fiscal years 2026-2028… 0% to 250%".

3. **The PSU payout range is 0–250% on both PSU types in 2026 grants. This resolves the 0–200% vs 0–250% question (Form 4 footnotes).** FACT:
   - The Aug–Sep 2026 grants to the new Chief Commercial Officer Michael C. Sullivan (0001110803-26-000169) and Chief Legal Officer Julie Coletti (0001110803-26-000177) each carry two PSU tranches: three-year EPS growth, and relative TSR. Both are 0–250% and vest 2028-12-31.
   - Sullivan received 5,254 target shares per tranche; Coletti received 5,307.
   - I did not find the 200% figure anywhere in the 2026 grants.

4. **The 2025 annual incentive plan paid 77% of target (search extract of the DEF 14A).** FACT:
   - Metrics were revenue (50%) and non-GAAP operating income (50%).
   - It was described as "fully formula-based", with no discretion.
   - Thaysen's payout was **$1,155,000** (77% × $1.5M).
   - The CEO's target rose from 125% to 150% of salary in FY25. This is a pay increase on top of a below-target payout, which is fair to note.
   - I did not obtain the 2026 AIP design, the clawback or hedging language, or the CEO pay ratio.

5. **Say-on-pay support was about 91% in 2025 and about 93.5% in 2026. This closes the "attendance only" gap.**
   - 2026 (8-K Item 5.07, 0001110803-26-000124, filed 2026-05-26, meeting 2026-05-21): For 121,746,792; Against 8,464,596; Abstain 404,097; broker non-votes 10,428,546. FACT. Support is 93.5% of for-plus-against (my calculation).
   - 2025 (0001110803-25-000051, filed 2025-05-23): For about 115.6M; Against about 11.5M. FACT. Support is about 91%.
   - Auditor ratification in 2026: 133.17M for and 7.76M against. This is the largest auditor opposition I saw (about 5.5% against).
   - Director opposition ranged up to 8.42M against in 2026. In 2025, Epstein drew 13.7M against, and he retired in 2026.

6. **The ledger's Thaysen holdings conflict (E152) is resolved, and the correction runs against the ledger's note.** FACT:
   - Thaysen's Form 4 of 2026-10-02/07 (0001110803-26-000183) shows a Code F withholding of 1,303 shares at $293.69 on 2026-10-05, leaving **107,770 shares** direct.
   - So the "107,770" in F15 is the October 2026 balance, not an error. The May 2025 figure of 83,390 is also right for its date.
   - Only the "100 shares" purchase version remains doubtful.
   - The summarizer labelled Code F as a "10b5-1 sale" and quoted a "$382.8 million" value. Both are wrong: F is tax withholding, and 1,303 × $293.69 is about $383K. The 10b5-1 flag is 0.

7. **Meister's holdings after the sales: 770,350 shares indirect (Corvex funds) plus 6,887 direct (0001110803-26-000181, 2026-09-30).** FACT:
   - The direct balance includes a Code A grant of 107 shares at $219.8037, which is 100% of his Q3 retainer taken in stock.
   - This is an exact post-selling holding, but I could not reconcile the 44,500-share gap, because the three August–September Meister XMLs returned 404:
     - 0001193125-26-361476 (filed 2026-08-21, period 2026-08-19)
     - 0001193125-26-371756 (filed 2026-08-27, period 2026-08-25)
     - 0001193125-26-383924 (filed 2026-09-04)
   - Their file sizes are about 54KB each, so they are large multi-line reports.

8. **The Chief Commercial Officer turned over, and this is not in the ledger.**
   - Everett Cunningham gave notice on 2026-01-04 and resigned effective 2026-01-16. The 8-K Item 5.02 gave no severance or terms (0001110803-26-000006, filed 2026-01-08). FACT.
   - It was filed the same day the ledger says Cunningham terminated a 10b5-1 plan on 2026-02-09, which is after he had already left.
   - Michael C. Sullivan appears as Chief Commercial Officer in an Aug 2026 new-hire grant: 4,503 RSUs at $199.87, plus the two PSU tranches (0001110803-26-000169, signed 2026-08-07). FACT.
   - Coletti is titled Chief Legal Officer and received a large grant on 2026-09-08: 4,549 RSUs, 14,214 RSUs and two 5,307-share PSU tranches (0001110803-26-000175 is Barnard, so Coletti is 0001110803-26-000177). The ledger refers to "Davies (GC)". I did not verify whether Davies left. OPINION: this is a possible GC turnover worth confirming.

9. **Board changes (Item 5.02 8-Ks).** FACT:
   - 2025-03-25 (0001110803-25-000032): Stephen MacMillan resigned effective 2025-03-28. Keith Meister joined the board, and Scott Gottlieb became non-executive Chair. Meister joined the board as Corvex was already building its position.
   - 2026-04-02 (0001110803-26-000082): Arnold, Epstein and Guthart gave notice of retirement effective 2026-05-21, and David King was nominated.
   - 2026-06-23 (0001110803-26-000138, effective 2026-06-16): Daniel Skovronsky was added, expanding the board from 9 to 10.
   - All three filings say the departures were not from disagreements.

10. **Item 2.02 and Item 4.01 checks.**
    - No Item 4.01 (auditor change) appeared in the 8-K list from May 2024 through Aug 2026. EY was ratified in both 2025 and 2026. FACT.
    - I did not open the earnings-release exhibits for non-GAAP definition changes.

11. **Other officers' Form 4s in September 2026 (small).** FACT: Barnard's Code F on 2026-09-05 was 408 shares at $211.06 (about $86K), leaving 40,927 shares, with no 10b5-1 plan flagged (0001110803-26-000175). Director Ullem received 113 shares at $219.8037 for his retainer, leaving 11,143 (0001110803-26-000180). Both are routine.

12. **Schedule 13G list.** The EDGAR listing surfaced only 2024 filings (accessions 0000932471-24-001320, 0001422849-24-000110 and others). No 2025–2026 13G/13D rows came back, and I did not identify the holders. This remains a gap.

## Insider transactions captured (new vs ledger)

| Person | Date | Code | Shares | Price | 10b5-1 | After | Accession |
|---|---|---|---|---|---|---|---|
| Thaysen | 2026-10-05 | F | 1,303 | $293.69 | No | 107,770 | 0001110803-26-000183 |
| Meister (direct) | 2026-09-30 | A | 107 | $219.80 | No | 6,887 direct; 770,350 indirect | 0001110803-26-000181 |
| Ullem | 2026-09-30 | A | 113 | $219.80 | No | 11,143 | 0001110803-26-000180 |
| Coletti | 2026-09-08 | A | 4,549 + 14,214 RSUs; 2×5,307 PSU | $0 | No | 18,763 | 0001110803-26-000177 |
| Barnard | 2026-09-05 | F | 408 | $211.06 | No | 40,927 | 0001110803-26-000175 |
| Sullivan | 2026-08-05 | A | 4,503 RSUs; 2×5,254 PSU | $199.87 | No | 4,503 | 0001110803-26-000169 |

I verified no net open-market sales for these people. All six are grants or tax withholding.

## Compensation-metric changes (filing citations)
- **FY25 AIP:** revenue 50% / non-GAAP operating income 50%; the CEO target was raised from 125% to 150% of salary (DEF 14A 0001193125-26-149669; search extract).
- **PSUs (2025 and 2026 grants):** the 2025 grants (3 March) used three-year (FY2026–28) non-GAAP EPS growth, 0–250%. The 2026 hire grants add a relative-TSR tranche, also 0–250%. I found nothing to confirm whether the TSR peer group changed.
- **Pay-versus-performance table:** the company-selected measure is revenue.

## Contradictions and stale data
- E152: the 107,770 holdings figure is correct as of October 2026, so F15's version is not wrong. Update the ledger. The summarizer tool also mislabels Code F, so earlier searched summaries of Code F as "10b5-1 sales" may be unreliable.
- The ledger names the GC as "Davies". Coletti now signs as Chief Legal Officer (Sept 2026). Confirm Davies's status.
- E150/E151: Meister's sales trail 12 May–4 Sep. Retained position is 770,350 shares indirect plus 6,887 direct, which is the current base.

## Gaps / what I could not find
- The proxy CD&A, SCT detail, pay ratio, clawback, hedging and the 2026 AIP design. The fetcher truncated at about page 37 of the proxy, before the compensation sections.
- A full Form 4 list from 1 January 2025 by person. Only the 10 most recent filings and the 40-row 8-K table came back. The August–September Meister reports returned 404 at ownership.xml, the .txt submission and CIK-path variants.
- The 44,500-share reconciliation.
- Corvex 13D/13G filings after 2024, the 5%+ holders, and the S&P 500 announcement date.
- Item 2.02 exhibit non-GAAP definition changes.
- Next step I'd suggest: have the analyst download `d13789ddef14a.htm` and the three Meister `ownership.html` pages by hand into Inbox, since the fetcher cannot render them.

Sources: [DEF 14A XBRL](https://www.sec.gov/Archives/edgar/data/1110803/000119312526149669/d13789ddef14a_htm.xml), [DEF 14A](https://www.sec.gov/Archives/edgar/data/1110803/000119312526149669/d13789ddef14a.htm), [2026 meeting 8-K](https://www.sec.gov/Archives/edgar/data/1110803/000111080326000124/ilmn-20260521.htm), [2025 meeting 8-K](https://www.sec.gov/Archives/edgar/data/1110803/000111080325000051/ilmn-20250521.htm), [Jan 2026 8-K](https://www.sec.gov/Archives/edgar/data/1110803/000111080326000006/ilmn-20260108.htm), [Apr 2026 8-K](https://www.sec.gov/Archives/edgar/data/1110803/000111080326000082/ilmn-20260402.htm), [Jun 2026 8-K](https://www.sec.gov/Archives/edgar/data/1110803/000111080326000138/ilmn-20260616.htm), [Mar 2025 8-K](https://www.sec.gov/Archives/edgar/data/1110803/000111080325000032/ilmn-20250325.htm), [Sullivan Form 4](https://www.sec.gov/Archives/edgar/data/0001110803/000111080326000169/form4.xml), [Thaysen Form 4](https://www.sec.gov/Archives/edgar/data/0001110803/000111080326000183/form4.xml), [Meister Form 4](https://www.sec.gov/Archives/edgar/data/0001110803/000111080326000181/form4.xml), [Ullem Form 4](https://www.sec.gov/Archives/edgar/data/0001110803/000111080326000180/form4.xml), [Coletti Form 4](https://www.sec.gov/Archives/edgar/data/0001110803/000111080326000177/form4.xml), [Barnard Form 4](https://www.sec.gov/Archives/edgar/data/0001110803/000111080326000175/form4.xml).
