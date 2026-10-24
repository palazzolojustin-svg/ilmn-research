# Agent 53: 53-web-ILMN-SEC-EDGAR-shell-10Q-DEF14A-CDA-and-8Ks

*Model: sonnet. Run 2026-10-11 03:30:55. Cost $0.35 (API-equivalent).*

**Assignment:** This agent needs a shell (Bash or PowerShell). Download the primary Illumina documents from EDGAR (CIK 1110803) into a local temp folder and grep them. Use a descriptive User-Agent header. (1) Fetch the Q2'26 10-Q main document. Grep Item 1A and Part II for Element, Munich, the SEC investigation or subpoena, the EC fine, and the 10x and Roche suits. Quote the exact text and the dollar amounts. (2) Fetch the 2026 DEF 14A. Extract the AIP design and funding, the PSU metric definition (operating margin vs EPS vs revenue), the rTSR peer group, any change in compensation metrics vs the 2025 proxy, the $11.0M SCT vs $12.3M grants reconciliation, the AIP revenue figure ($4,369M vs $4,343M reported), the 77% funding vs 103% op-income attainment, the pay ratio, CIC and clawback terms. (3) Read the unread 8-Ks: 17 Aug 2026 (8.01), 30 Jan 2026 (2.01, 8.01), 8 Jan 2026 (5.02, 7.01). (4) Build the 24-month Form 4 table (insider, date, shares, price, 10b5-1 flag, adoption date) and close the Meister 44,500-share gap. Give each item as a table with accession numbers and URLs. Flag anything that looks credibility-relevant. Do not repeat the secondary summaries in the ledger. Report the shell-fetched facts only.

## Key findings

**NO NEW EVIDENCE on the core assignment.** I had no Bash or PowerShell tool in this session, and the assignment depends on downloading and grepping filings locally. WebFetch returns only a truncated, summarized excerpt of each filing, so I couldn't read the 10-Q legal sections or the proxy CD&A. Gaps 5 and 6 stay open and need an agent with a real shell.

I checked the ledger and gaps first. Only the 17 Aug 8-K was readable, and it is already covered in the ledger.

## What I checked

| Target | Result | Evidence |
|---|---|---|
| Q2'26 10-Q main document (`.../000111080326000160/ilmn-20260628.htm`) | The fetch returned the financial statements, SomaLogic acquisition details and revenue policies. It returned no litigation or risk-factor text. Element, Munich, SEC, EC fine and the 10x/Roche suits all came back "no mention found". | This is a truncation artifact, not proof the filing is silent. Do not treat it as evidence. |
| 2026 DEF 14A (`0001193125-26-149669`, [d13789ddef14a.htm](https://www.sec.gov/Archives/edgar/data/1110803/000119312526149669/d13789ddef14a.htm)) | Both `.htm` and the full `.txt` cut off at about page 45, where the CD&A begins. The AIP, PSU, rTSR peer group, pay ratio, clawback and CIC terms were not retrievable. | FACT: the excerpt re-confirms 2025 revenue of $4.34B (flat), non-GAAP EPS of $4.84 (+16%) and non-GAAP operating margin of 23.1% (vs 21.3%). |
| 17 Aug 2026 8-K (`0001193125-26-354010`, [d51146d8k.htm](https://www.sec.gov/Archives/edgar/data/0001110803/000119312526354010/d51146d8k.htm)) | An underwriting agreement for $300M of 4.950% notes due 2029, closing 17 Aug. The proceeds, with cash on hand, repay the 4.650% notes due 9 Sep 2026. The filing was an S-3 takedown (Reg. No. 333-281921) with Ex. 4.2 and Ex. 5.1. | FACT. Already in the ledger as trivia (E154/E222 correction). The filing is Item 8.01/9.01, so it is not a disclosure event. |
| 30 Jan 2026 (2.01, 8.01) and 8 Jan 2026 (5.02, 7.01) 8-Ks | I could not locate these. The EDGAR browse page showed only filings from 30 Jul to 17 Aug. | The 8-K I did fetch, `000111080326000009`, is dated 13 Jan 2026 (Item 2.02, preliminary Q4/FY25 results, issued around JPM). It is not one of the three requested filings. |
| Form 4 table and the Meister 44,500-share gap | Not attempted, because the Form 4 XML needs bulk fetching. | The ledger already has the six Meister Form 4s: about 3.02M shares and about $586M (E150/E151 correction). |

## Filings in the August cluster

These are accession numbers from the EDGAR listing, for the next agent.

| Date | Accession | Items | Status |
|---|---|---|---|
| 2026-07-30 | 0001110803-26-000155 | 2.02, 9.01 | Q2 earnings release; already used |
| 2026-08-07 | 0001110803-26-000168 | 8.01, 9.01 | Not read by me |
| 2026-08-12 | 0001193125-26-345802 | 8.01, 9.01 | Not read by me; the ledger's "12–13 Aug 8-Ks" note covers it |
| 2026-08-13 | 0000950157-26-000888 | 1.01, 1.02, 2.03, 9.01 | Revolver and debt; the ledger notes a $1.0B revolver to Aug 2031 |
| 2026-08-17 | 0001193125-26-354010 | 8.01, 9.01 | Read (see above) |

OPINION: the 7 Aug 8.01 (`ilmn-20260807.htm`) is the only August filing not yet accounted for in the ledger, so it is worth a look.

## Contradictions and stale data

None found. I did not read enough text to test any ledger item.

## Gaps / what I could not find

- **Shell handoff for gaps 5 and 6.** Run the following with a User-Agent header, then grep locally:
  - 10-Q: `https://www.sec.gov/Archives/edgar/data/1110803/000111080326000160/ilmn-20260628.htm`. Grep for `Element|Munich|Unified Patent|subpoena|Securities and Exchange Commission|European Commission|10x|Roche|Ultima`.
  - DEF 14A: `https://www.sec.gov/Archives/edgar/data/1110803/000119312526149669/d13789ddef14a.htm`, from page 45 on. A lighter option is the ARS PDF, [d78939dars.pdf](https://www.sec.gov/Archives/edgar/data/1110803/000119312526149693/d78939dars.pdf), but it probably omits the CD&A.
  - The 2025 proxy for comparing compensation metrics: [d910798ddef14a.htm](https://www.sec.gov/Archives/edgar/data/1110803/000119312525076900/d910798ddef14a.htm).
- A search summary repeats the 77% AIP funding and the pre-established revenue plus non-GAAP operating income goals (Source: sec.gov DEF 14A, via WebSearch, 11 Oct 2026). This matches E197 and adds nothing.
- Not retrieved: the 8 Jan 2026 (5.02, 7.01) and 30 Jan 2026 (2.01, 8.01) 8-Ks, the 24-month Form 4 table with 10b5-1 flags, and the Meister 44,500-share gap. The shell agent can use the EDGAR submissions JSON (`data.sec.gov/submissions/CIK0001110803.json`) to find the two January 8-Ks.
