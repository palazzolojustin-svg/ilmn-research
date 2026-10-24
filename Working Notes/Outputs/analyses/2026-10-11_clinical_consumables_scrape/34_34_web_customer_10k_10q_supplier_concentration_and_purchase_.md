# Agent 34: 34-web-customer-10K-10Q-supplier-concentration-and-purchase-commitments

*Model: sonnet. Run 2026-10-11 02:47:09. Cost $0.71 (API-equivalent).*

**Assignment:** Read the raw text of customer filings to test whether clinical customers are locked into Illumina consumables purchases and how exposed they are. Use the EDGAR Archives direct document URLs (find them through sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=...&type=10-K, then the index page) and the XBRL company-facts API at data.sec.gov/api/xbrl/companyfacts/CIK##########.json for tags such as PurchaseObligation, PurchaseObligationDueInNextTwelveMonths and ConcentrationRiskPercentage.

Companies not yet checked: Exact Sciences, BillionToOne, Adaptive, Veracyte, Myriad, NeoGenomics, Caris (Note 8), Labcorp, Quest. Also finish Tempus (tem-20251231.htm) and GeneDx (wgs-20251231.htm), and the Q2 2026 10-Qs for Natera, Guardant, Tempus and GeneDx.
For each, search for: 'Illumina' by name in risk factors, supply agreements and the commitments note; 'sole source' or 'single source' sequencer or reagents; the purchase obligation amounts and the period they cover (the Natera figures $261.4M vs $256.9M with $171.3M due within a year need resolving by opening the 10-K commitments note); the supplier concentration percentages of COGS or purchases and any change from year to year; any statement that they are evaluating or have qualified alternative sequencers (Element, Ultima, Roche AXELIOS, PacBio, MGI/Complete Genomics); any language on NovaSeq X transition, instrument purchases, reagent rental, or capex for sequencers; the cost per test and COGS per test and how it moved y/y (to infer $/Gb pass-through); and Medicare share of revenue.
Quantify and give filing, section and accession number. Quote short exact phrases. Hard stop at 20 minutes. Return a table by company: names Illumina (Y/N), purchase commitment $, supplier concentration %, alternative-platform language, COGS per test trend.

## Key findings

1. **Tempus names Illumina.** This corrects the "one unnamed supplier" treatment in open gap 5.
   - FACT (search-engine extract of the Tempus FY25 10-K, not the full text): "Purchases from Illumina accounted for approximately 33%, 39% and 33% of total vendor payments" for 2025, 2024 and 2023.
   - FACT: amounts due to Illumina were "approximately $15.9 million at December 31, 2025". The ledger's $15.9M payable is therefore Illumina.
   - FACT: Tempus "relies on Illumina as the sole supplier of the sequencers and as the sole provider of maintenance and repair services". This is the strongest lock-in language found so far.
   - Source: Tempus AI Form 10-K FY2025, https://www.sec.gov/Archives/edgar/data/1717115/000119312526066961/tem-20251231.htm, accession 0001193125-26-066961. I got this from two WebSearch extracts on 2026-10-11.
   - I could not open the sections myself, so the exact section (risk factors vs. concentration note) is not confirmed.
   - OPINION: Tempus's spend with Illumina is 33–39% of all vendor payments. That is a very high dependence for a lab, and it was volatile (39% in 2024, 33% in 2025).

2. **GeneDx names Illumina, but not as the 20% supplier.**
   - FACT (direct fetch of wgs-20251231.htm): "We rely on a limited number of suppliers, including Illumina, Inc., Life Technologies Corporation, Twist Biosciences Corporation, Path-Tec LLC and Agilent Technologies for certain laboratory reagents, as well as sequencers and other equipment and materials."
   - FACT, same fetch: "only a few other manufacturers outside of those listed above … are currently capable of supplying and servicing the equipment necessary for our operations, including sequencers and various associated reagents and enzymes." This is the only "alternatives" language found. It does not name Element, Ultima or Roche.
   - A search extract says one supplier was about 20% of 2025 purchases, up from 13% in 2024. Five suppliers are named, so the 20% supplier is not identified as Illumina. Keep it "unnamed".
   - Source: GeneDx 10-K FY2025, accession 0001818331-26-000015.

3. **Natera: the $261.4M vs $256.9M question is still unresolved.**
   - FACT: the XBRL company-facts API for CIK 1604821 has no `PurchaseObligation` or `PurchaseObligationDueInNextTwelveMonths` tags. The answer therefore sits only in the narrative commitments note of the 10-K (accession 0001104659-26-020881).
   - The "$11.6M" figure came from an app.edgar.tools page for ticker NEO, which is NeoGenomics, not Natera. That page reports $11,559K of purchase commitments for 2026–2028. This confirms the E109 caution: do not attribute it to Natera.
   - The page returned 403 on a direct fetch, so the NEO attribution rests on the search snippet.

4. **Caris runs a very large Illumina fleet, per press.**
   - Trade press via search extracts (360Dx and GenomeWeb, no dates seen): about 50 NovaSeq instruments, the largest single-customer installed base. Both NovaSeq 6000 and NovaSeq X are in use at its Arizona labs.
   - The 10-K Note 8 and the supplier language were not retrievable.

## Table by company

| Company | Names Illumina? | Purchase commitment $ | Supplier concentration | Alternative-platform language | COGS per test trend |
|---|---|---|---|---|---|
| Tempus | Y, sole sequencer and service supplier (extract) | Not found; $15.9M payable | 33/39/33% of vendor payments (2025/24/23) | None found | Not checked |
| GeneDx | Y, one of five named suppliers | Not found | One unnamed supplier at 20% vs 13% | "only a few other manufacturers" | Not checked |
| Natera | Y (from prior ledger) | Unresolved; no XBRL tag | Not found | Not found | Not checked |
| Caris | Not verified in text; press says 50 NovaSeq | Not found | Not found | Not found | Not checked |
| Exact, BillionToOne | Not verified | Not found | Not found | Not found | Not checked |
| Adaptive, Veracyte, Myriad, NeoGenomics, Labcorp, Quest | Not checked | NeoGenomics $11.6M (2026–28, snippet) | Not checked | Not checked | Not checked |

## Contradictions and stale data

- Gap 5 says the Tempus and GeneDx 33/39/33% and 20/13/11% figures are "one unnamed supplier". The Tempus extract says the 33/39/33% supplier is Illumina. The GeneDx supplier stays unnamed.
- Search-engine summaries are a weak source. Several of my WebFetch calls returned only the business section of long filings, so every "not found" above means "not retrievable", not "absent".
- The Exact Sciences extract says earlier 10-Ks had MRD and MCED tests built on Illumina, and that Exact "has invested significant capital, time and expertise to procure Illumina and Hamilton machines". This is a switching-cost statement. I could not tie it to the FY25 10-K text or a date.

## Gaps / what I could not find

- WebFetch truncates large 10-Ks. I could not read the commitments notes for Natera, Tempus, GeneDx, Caris, Exact or BillionToOne, and I did not reach the Q2'26 10-Qs. The BillionToOne 10-K URL is https://www.sec.gov/Archives/edgar/data/2070849/000207084926000017/blln-20251231.htm and the Exact one is https://www.sec.gov/Archives/edgar/data/1124140/000112414026000011/exas-20251231.htm.
- I did not reach Adaptive, Veracyte, Myriad, Labcorp or Quest, or any COGS-per-test or Medicare-share data.
- Recommended workaround: download the 10-K HTML files into Inbox or a local folder and grep them. XBRL R-pages (R#.htm) from each accession may also fetch cleanly.

**Verdict: partial.** The one new, useful finding is that Tempus names Illumina as its sole sequencer supplier and puts Illumina at 33–39% of vendor payments. Everything else is confirmation, or not retrievable.

Sources:
- [Tempus AI 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1717115/000119312526066961/tem-20251231.htm)
- [GeneDx 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1818331/000181833126000015/wgs-20251231.htm)
- [Natera 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1604821/000110465926020881/ntra-20251231x10k.htm)
- [Caris 10-K FY2025](https://www.sec.gov/Archives/edgar/data/2019410/000201941026000016/cai-20251231.htm)
