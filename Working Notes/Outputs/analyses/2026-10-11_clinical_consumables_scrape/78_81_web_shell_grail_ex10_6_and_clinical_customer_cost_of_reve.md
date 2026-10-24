# Agent 78: 81-web-shell-GRAIL-Ex10.6-and-clinical-customer-cost-of-revenue-commitments

*Model: sonnet. Run 2026-10-11 09:56:46. Cost $0.77 (API-equivalent).*

**Assignment:** Needs a working shell (curl, pdftotext or Python); confirm it first and declare an SEC User-Agent. (A) Read in full the GRAIL-Illumina supply agreement, Ex. 10.6 (find it via GRAIL's 10-K/10-Q exhibit index on sec.gov). Extract §13 (term, termination, renewal, non-renewal notice dates), the Exhibit A discount or pricing table, the §3.4 binding forecast horizon, any minimum-purchase or take-or-pay terms, price-reduction or most-favored-customer language, and the NovaSeq X transition terms. Also check GRAIL's 8-Ks and 10-Q around Oct-Nov 2026 for a non-renewal notice, and the GRAIL royalty resumption date (Dec 2026). (B) For Caris Q2'26 10-Q, Tempus FY25 10-K ('exclusive use'), Exact FY25 10-K, Guardant Q2'26 10-Q, GeneDx, Myriad and Veracyte: pull the MD&A cost-of-revenue text, supplier-concentration notes and purchase-commitment notes, via the sec.gov R-pages or the full-text filings with grep for 'Illumina', 'sequencing', 'cost per', 'flow cell', 'reagent', 'purchase commitment', 'supplier'. Quantify cost of revenue per test or per sample and its change year over year. State whether it supports price-per-Gb deflation passing through to labs' unit costs (Adaptive and Guardant signals) or flat unit cost (Natera, Caris). Give any statements on migration from NovaSeq 6000 to X, parallel running, and share of Illumina in COGS. Cite accession numbers and quote short phrases.

## Key findings

1. **Part A is not done, and the ledger's E257 stays unverified.** I had no shell in this session, only WebFetch and WebSearch. Ex. 10.6 still truncates at §9.1(c), so §13 (term and renewal), Exhibit A and the §3.4 percentage were not read. Someone with curl and pdftotext needs to do this.
2. **GeneDx cost per test fell about 14% while volume grew 32%.** FACT. This is the cleanest new deflation signal.
   - Cost of services was $36.2M in Q2'26 vs $31.8M in Q2'25 (+13.8%). Six-month cost was $70.2M vs $60.4M (+16.2%).
   - I backed out the Q2'25 exome/genome volume at about 23.3K from the +32% growth to 30,785 (E081). That gives about $1,176 vs about $1,364 per exome/genome test.
   - This is my calculation (OPINION, directional). Cost of services includes other tests and labor. [GeneDx Q2'26 10-Q, acc. 0001628280-26-051878, https://www.sec.gov/Archives/edgar/data/0001818331/000162828026051878/wgs-20260630.htm]
3. **Caris unit cost is rising, which supports E092 and "deeper, not cheaper."** FACT plus calculation.
   - Molecular profiling cost of services was $81.3M vs $65.3M in Q2'25 (+24.5%). Six-month cost was $154.2M vs $126.2M (+22%).
   - Cases rose 18% to 59.2K (E081). That implies about $1,373 per case vs about $1,301 a year earlier, up about 5–6%. This is my calculation, and it uses total cases.
   - The 10-Q attributes the increase to the blood lab (+$10.4M) and tissue lab (+$5.5M). Blood-lab "materials and related testing costs" rose $8.6M. Tissue-lab materials rose $2.3M, and labor rose $3.6M.
   - Depreciation fell in both labs (−$0.8M and −$0.4M).
   - The blood-lab materials growth fits the double-sequencing blood assays in E092. [Caris Q2'26 10-Q, acc. 0002019410-26-000055, https://www.sec.gov/Archives/edgar/data/0002019410/000201941026000055/cai-20260630.htm]
4. **Guardant's 10-Q text confirms the deflation passes through.** FACT, via search snippet.
   - Six-month cost of revenue was $220.9M vs $155.9M (+42%).
   - The filing says the rise was "driven primarily by an increase in sample volume, partially offset by reduced cost per sample of oncology tests and Shield screening test."
   - This is 10-Q text that supports E043 and E090. It is not a ledger-level change. [Guardant Q2'26 10-Q, acc. 0001576280-26-000037, https://www.sec.gov/Archives/edgar/data/0001576280/000157628026000037/gh-20260630.htm]
5. **Veracyte's reagent spend fell while volume grew.** FACT. It is a weak Illumina read-through because Veracyte uses mixed platforms and I could not confirm any Illumina share.
   - Lab supplies and reagents were $13.8M vs $15.3M in Q2'25 (−9.8%).
   - Cost of testing revenue was $36.3M vs $32.4M (+12%). Compensation rose to $9.9M from $6.0M.
   - Decipher volume was +17% (E081). [Veracyte Q2'26 10-Q, acc. 0001384101-26-000044, https://www.sec.gov/Archives/edgar/data/0001384101/000138410126000044/vcyt-20260630.htm]
6. **GeneDx's supplier and commitment disclosures are new, but the supplier is unnamed.**
   - One supplier was about 14% of spend in Q2'26 vs 20% in Q2'25. For six months it was 23% vs 22%.
   - The filing says alternative suppliers exist "for the majority of these reagents and supplies."
   - Purchase commitments total $41.5M, of which $9.4M falls in the rest of 2026.
   - The filing does not name Illumina. Treat any Illumina attribution as unverified.
7. **Myriad shows no sequencing-driven deflation.**
   - Q2'26 cost of revenue was $63.7M vs $61.3M (+4%). Revenue was $190.7M vs $213.1M.
   - The implied cost ratio was 33.4% vs 28.8%, so gross margin fell to about 66.6% from about 71.2%. A fetch summary labeled 33.4% as "margin", which is inverted; I recomputed it.
   - The filing cites "increased fulfillment costs" and personnel costs, and gives no reagent or sequencing detail.
   - Revenue per test fell 9% (E095). The pressure is price, not unit-cost relief. [Myriad Q2'26 10-Q, acc. 0000899923-26-000072, https://www.sec.gov/Archives/edgar/data/0000899923/000089992326000072/mygn-20260630.htm]
8. **The GRAIL Oct–Nov 2026 non-renewal check cannot be done yet.** Today is 2026-10-11, and no Q3 10-Q or 8-K exists. GRAIL's royalty suspension runs to 24 Dec 2026 or an earlier change of control. This matches the ledger.

## Signal on unit-cost pass-through

| Company | Unit cost direction | Basis |
|---|---|---|
| Guardant | Down | 10-Q text on reduced cost per sample, plus the ~$200 X saving (E043) |
| GeneDx | Down ~14% (my calc) | Cost +14% vs exome/genome volume +32% |
| Veracyte | Reagents down ~10% | Volume up; platform mix unclear |
| Caris | Up ~5–6% (my calc) | Deeper sequencing, blood assays, labor |
| Myriad | Cost up 4% on lower revenue | Fulfillment and personnel; no sequencing detail |

OPINION: This supports a split. High-volume labs that moved to the X (Guardant) or have scale (GeneDx) are keeping the Gb deflation. Labs that reinvest in depth (Caris) show flat or rising unit cost. That fits the E092 and E115 switching-incentive picture.

## Contradictions and stale data

- No direct contradiction of the ledger. The Caris per-case figure here (~$1,373 for Q2'26, ~$1,301 for Q2'25) differs from the ledger's FY25-based ~$1,425 vs ~$1,340 under E092. These are different periods and calculations.
- Several figures are fetch-tool summaries of 10-Qs, not verbatim reads. The Veracyte reagent lines and GeneDx supplier percentages should be spot-checked against the filings.

## Gaps / what I could not find

- **GRAIL Ex. 10.6:** §13, the Exhibit A discount table, the §3.4 binding percentage (redacted as "[***]"), minimums and any X terms. Both the exhibit (https://www.sec.gov/Archives/edgar/data/1699031/000119312524132022/d556103dex106.htm) and the FY25 10-K (acc. 0001628280-26-017319) truncate. The visible §3.4 text says forecast is a binding commitment by GRAIL and its affiliates to take and pay for Products. The 10-K and 10-Q describe no term or renewal. Next step: pdftotext on the full exhibit, then check the GRAIL 8-K/10-Q after 31 Oct.
- **Tempus, Exact FY25 10-K, Guardant Q2'26 commitments note:** not retrieved this pass. Exact has no Q2 10-Q, since Abbott closed it in March 2026.
- **Illumina share of COGS and 6000-to-X migration or parallel running:** none of the 10-Qs I read state it. Caris's 10-Q excerpt did not mention Illumina or NovaSeq.
