# Agent 58: 58-web-shell-GRAIL-and-Natera-supply-agreements-10K-raw-text-take-or-pay-pricing

*Model: sonnet. Run 2026-10-11 03:36:37. Cost $0.46 (API-equivalent).*

**Assignment:** Use a real shell (curl or Invoke-WebRequest with a SEC-compliant User-Agent header) and grep the raw filing text. If no shell is available, say so first. (1) GRAIL (CIK via EDGAR company search 'GRAIL, Inc.'): download the latest 10-K and the Q2'26 10-Q. Grep for 'Illumina', 'supply agreement', 'minimum', 'take-or-pay', 'purchase commitment', 'royalty', 'renewal', 'NovaSeq', 'flow cell' and 'price'. Report the contract term, renewal and non-renewal notice mechanics (notice falls about 31 Oct 2026), whether the royalty resumes 24 Dec 2026, annual Illumina purchases in $ and any Gb or volume figures. Also report GRAIL sequencing cost per test or COGS commentary, and the NHS-Galleri and PATHFINDER 2 sample volumes, which imply Gb per test. Look for any 8-K from 1 Oct to 11 Oct 2026. (2) Natera: Q2'26 10-Q Ex. 10.1-10.4 (acc. 0001628280-26-054525), where the 2014-2016 amendment chain was re-filed. Read the cover or explanatory note and the FY25 10-K contractual-obligations and 'Illumina' risk-factor text. Find whether the refiling was driven by the Third Amendment's ten-year term or by an SEC confidential-treatment expiry. Also report Natera's Illumina purchase obligations in $, remaining term, any exclusivity or price-protection clause, and any NovaSeq X migration language ('NovaSeq X', 'transition', 'cost per sample', 'sequencing cost'). (3) Repeat the grep for Guardant, Tempus, GeneDx, Caris, BillionToOne and Exact FY25 10-Ks and Q2'26 10-Qs for the phrases 'NovaSeq X', 'sequencing cost per', 'decrease in the cost of sequencing', 'Ultima', 'Element', 'AVITI', 'AXELIOS' and 'parallel'. Return a table by company: quote, filing, date, and what it implies for Gb growth, price pass-through and switching. Do not repeat the generic contract summaries from agents 29, 34, 41, 47, 50 and 54 unless you are adding raw quotes or numbers.

## Key findings

I had no shell, so there was no curl or grep of raw filings. I used WebFetch, which truncates long 10-Ks. Items (1) GRAIL contract mechanics and (3) the other six companies are therefore NOT done. Item (2) is partly done through the four Natera exhibits.

- **The Natera Ex. 10.1–10.4 refiling reason is not stated in any text I could reach.**
  - [Natera Q2'26 10-Q, 2026-08-07, sec.gov/Archives/edgar/data/1604821/000162828026054525/] has no explanatory note in any of the four exhibits.
  - The 10-Q main document and the FY25 10-K came back truncated, so I did not see the exhibit index or its footnotes.
  - FACT: Ex. 10.1 is the original "Supply Agreement (TG Consumables)" dated 16 Aug 2013, "as amended September 18, 2014". Ex. 10.2 is the Second Amendment (signed 23 Sep 2015). Ex. 10.3 is the Third Amendment (signed 3–8 Jun 2016). Ex. 10.4 is the Fourth Amendment (undated in the fetch). These are the 2013–2016 documents, so the ledger's "2014–2016" label should read 2013–2016, with the base agreement refiled alongside.
- **Third Amendment term, quoted (Ex. 10.3, via WebFetch summary):** "ten (10) years after the Third Amendment Date unless otherwise terminated early." Counted from June 2016, that is about June 2026.
  - FACT: the refiling came in the 10-Q covering the quarter in which that date fell.
  - OPINION: this timing supports a link to the ten-year term, but it is still an inference. I did not find or rule out a confidential-treatment expiry.
  - The current term is August 2033 (E109), presumably set by later amendments such as the Eleventh. The ten-year clause is therefore historical.
- **The exhibits show the early contract was non-exclusive on later terms but exclusive in 2015.**
  - FACT (Ex. 10.2, 2015): Natera had to use "exclusively… Illumina TG Consumables and Temporary Consumables and Illumina Hardware for all NIPT Uses". Pricing was tied to quarterly "Consumable Spend" volume discounts, with minimum discount floors.
  - FACT (Ex. 10.3, 2016): the IVD-kit rights are "non-exclusive". Illumina may terminate the NIPT/Additional Clinical Use rights on 2 years' notice, not before the 5th anniversary. The rights exclude clustering and sequencing consumables.
  - FACT (Ex. 10.4): "beginning in calendar year 2019 and through the end of the Term, Illumina may adjust base prices in accordance with Section 7(a)." This is a price-adjustment right for Illumina. It sits with the ledger's E212 view that the later §7(l) is a ceiling.
  - Whether the 2015 exclusivity survives in the current agreement is unverified. The Eleventh Amendment keyword read (ledger corrections) found no MFN language.
- **The base agreement has forecast mechanics.** FACT (Ex. 10.1, as summarised by WebFetch): monthly forecasts six months ahead, the fourth month binding with ±25% variance. The customer can terminate for convenience on 4 months' notice. Illumina can terminate on a Natera change of control. There is no take-or-pay in the early documents (minimums are "[*]" redacted for Temporary Consumables). Treat these as 2013–2016 terms that later amendments may have changed.
- **The "$11.6M Natera purchase commitments" figure is still unverified; do not add it.**
  - A search returned "non-cancellable purchase commitments total $11,559 thousand ($5,310K in 2026, $5,310K in 2027, $939K in 2028)".
  - The source link was app.edgar.tools/companies/NEO. NEO is NeoGenomics, so the figure probably belongs to that company. The ledger's CORRECTION on E109 stands.
  - Even if it were Natera's, the amount is immaterial against Natera's sequencing spend.
- **GRAIL FY25 10-K ([gral-20251231.htm], acc. 0001628280-26-017319, sec.gov/Archives/edgar/data/1699031/):** the fetch showed no term, renewal, minimum or take-or-pay language, and no dollar purchase figures. That does not prove the 10-K lacks them.
  - FACT: GRAIL calls Illumina "a sole supplier for our next-generation sequencers and associated reagents".
  - FACT: the fourth amendment suspends the royalty until 24 Dec 2026 or an earlier change of control, resuming "without retroactive effect". This confirms what the ledger already holds.
  - FACT: the royalty is 9% in perpetuity, with an anti-stacking floor of 7% and a step-down to 5% after $1B of cumulative payments. GRAIL's 10-K says "high single-digit".
  - FACT: the supply-agreement product list includes NovaSeq 6000, NovaSeq X Plus and NovaSeq reagent kits and flow cells, so GRAIL can buy both generations.
- **Trial sizes for Gb-per-test work (FACT, GRAIL FY25 10-K):** NHS-Galleri "over 140,000 individuals". PATHFINDER 2 is about 35,000 participants, with about 25,000 in the initial ESMO results. I found no sequencing depth or Gb per test, so the Gb-per-test inference is still blocked (ledger E178).
- **No GRAIL 8-K for 1–11 Oct 2026 was found.** I did not check EDGAR's filing list directly, only web search. The renewal-notice date of about 31 Oct is not confirmed in any text I read.

## Table for item (3): not done

I did not reach the Guardant, Tempus, GeneDx, Caris, BillionToOne or Exact 10-Ks and 10-Qs. WebFetch returns only the front matter of these filings. I did not run the phrase searches ("NovaSeq X", "sequencing cost per", "Ultima", "AXELIOS", "parallel").

## Contradictions and stale data

- The ledger's "2014–2016 amendment chain" should read 2013 base agreement plus 2014–2016 amendments. The First Amendment (18 Sep 2014) is referenced in Ex. 10.1 but is not a separate exhibit.
- The $11.6M commitment is probably NeoGenomics, not Natera (see above).
- The 2015 exclusivity (Ex. 10.2) may be stale. Ex. 10.3 describes non-exclusive IVD rights, and Natera now has other platforms in job postings (E022, E166).

## Gaps / what I could not find

- **Needs a real shell:** the exhibit index and footnotes in the Natera 10-Q and 10-K, the 10-K contractual-obligations note, GRAIL 10-K contract-term, renewal-notice and purchase-dollar text, and all six item (3) companies' filings. Use curl with a User-Agent header and grep, for example against the accession paths above.
- **Not checked:** the GRAIL Q2'26 10-Q, any GRAIL 8-K by direct EDGAR listing, and GRAIL cost-per-test commentary (ledger E178 stands).
