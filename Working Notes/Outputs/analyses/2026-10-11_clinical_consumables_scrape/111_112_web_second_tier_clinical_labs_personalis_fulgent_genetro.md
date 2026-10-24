# Agent 111: 112-web-second-tier-clinical-labs-Personalis-Fulgent-Genetron-Berry-Eurofins-GenomicsPLC-A

*Model: sonnet. Run 2026-10-11 10:39:13. Cost $0.79 (API-equivalent).*

**Assignment:** Close open gap 5, the clinical customers not yet checked. (a) Read the Justia exhibits for the Personalis-Illumina agreements (contracts.justia.com/companies/personalis-inc-8225/contract/62420 and /62422) and extract the volume-tier pricing mechanics, minimum purchase commitments, price-reduction clauses, term, and any 'most favored customer' or platform-transition language. (b) Run SEC full-text search (efts.sec.gov/LATEST/search-index?q=...) for 'NovaSeq X' and for 'Illumina' with 'purchase commitment' in the latest 10-K and 10-Q of Personalis, Fulgent, Oncocyte, Revvity (Revvity/Variantyx/BioLegend are not relevant; focus on Revvity's genomics and NIPT business), Eurofins (H1'26 report), Genetron Health, Berry Genomics, Genomics plc, Ambry (private; use press), and Variant Bio. Extract: which sequencers they run, whether they have moved from NovaSeq 6000 to X or to AVITI/Ultima/Revio, the cost per test, the share of cost of revenue from Illumina, and the reagent price statements. Quantify any stated per-sample or per-Gb cost fall after the move to the X. Cite URL, filing date and quote. Stop at about 20 minutes.

## Key findings

**Mostly NO NEW EVIDENCE.** I found one item that adds to the ledger (Fulgent, below). Everything else I checked was empty or blocked.

- **Fulgent sequencing intensity (new, relevant to E082/E086 and to Q2 volume).** Fulgent said on its Q2'26 call (2026-07-30) that "our mean sequencing coverage increased from 40x to 60x to 70x" (FACT/MGMT). This came from implementing Illumina's TruePath system, described as "a short-read light technology that maintains high accuracy while providing long-range genomic insights." That is +50–75% more Gb per sample at one clinical lab, from a chemistry change rather than from test-volume growth. This supports the "intensity offsets price" argument at the margin.
  - Source: Fulgent Q2 2026 call transcript, webull.com/news/15364816053167104, 2026-07-30.
  - Limit: Fulgent did not state a sequencer model or a cost per test.
- **Fulgent's gross margin and customer loss (new context).** Q2'26 revenue was $85.4M, +4% y/y. GAAP gross margin was 30.1% and non-GAAP 31.3%. Management blamed "fixed costs spread over a lower revenue base, driven by the lower collection rate", not sequencing economics. FY26 revenue guidance was cut to $330–340M from $350M. The CFO said its largest customer is "moving its testing capabilities in-house" and cost the company $4.6M of quarterly revenue.
  - Source: the same transcript, plus marketbeat.com/instant-alerts/fulgent-genetics-q2-earnings-call-highlights-2026-07-30/.
  - OPINION: Fulgent is a weak read-through for Illumina clinical demand.
- **Fulgent's 10-K (FY25) names Illumina as supplier but gives no commitment figures.** It says the company relies on Illumina as "the sole supplier of the next generation sequencers" and "sole provider of maintenance and repair services." It notes that "several sequencer suppliers… could replace Illumina." It does not mention "NovaSeq" or any purchase-obligation dollar amount.
  - Source: sec.gov/Archives/edgar/data/1674930/000119312526079169/flgt-20251231.htm, filed 2026-03.
- **Personalis FY25 10-K confirms Illumina as sole supplier, with no terms.** It says "We have certain agreements and purchase arrangements in place with Illumina to satisfy the projected needs of our laboratory operations." It says it uses Illumina and other RUO (research-use-only) products for clinical tests and "intend[s] to evaluate" other platforms as they become available. It discloses no minimum commitments, tiers or pricing.
  - Source: sec.gov/Archives/edgar/data/1527753/000119312526076615/psnl-20251231.htm.
  - The Q2'26 10-Q does not name Illumina at all. It only says it relies on "a limited number of suppliers, or in some cases, a sole supplier" (sec.gov/Archives/edgar/data/0001527753/000119312526332817/psnl-20260630.htm).
- **Personalis Q2'26 results (context for E093).**
  - Revenue was $22.4M, +30% y/y.
  - Clinical tests were 10,384, +199%.
  - Gross margin was about 21%, hurt by "higher diagnostic test costs and lower reimbursement rates."
  - Guidance and calls are suspended because of the Tempus merger (quartr.com/events/personalis-inc-psnl-q2-2026_o08KfBpj, via search summary).
  - OPINION: Sequencing cost does not show up as a stated margin driver. A 21% gross margin on a high-Gb WGS-based MRD (minimal residual disease) test means Illumina's price per Gb is not the binding constraint for this lab.
- **Personalis–Illumina 2019 pricing agreement (partial, from a search snippet only).** A search result describes the agreement for NovaSeq 5000/6000 S4 reagent kits, dated 2019-03-26, with a "purchase commitment of $1.7 million by June 30, 2019" (Justia contract 62417 via search snippet). I could not open the page. The document is NovaSeq 6000-era, so it says nothing about the X.

## Gap 5 status

| Item | Result |
|---|---|
| Justia contracts 62420 and 62422 | **Blocked (HTTP 403).** Tier mechanics, MFN and price-reduction clauses are NOT extracted. 62420 is titled "Quotation and Supply Agreement for NovaSeq 6000 Sequencing Systems" and 62422 is a "Pricing Agreement… for NovaSeq 5000/6000 S4 Reagent Kits" (titles from search results). Both predate the X. |
| EDGAR full-text search | Not run. I had no working path to the efts endpoint through the tools available. The 10-K and 10-Q fetches above stand in for it. |
| Oncocyte, Revvity, Eurofins H1'26, Genetron, Berry, Genomics plc, Ambry, Variant Bio | Searches returned nothing on their sequencer choice, cost per test or Illumina share of cost of revenue. |

## Contradictions and stale data

- None contradict the ledger.
- The Berry/Illumina NextSeq CN500 co-development result is old (it dates from a 2014-era press release). It is not a current read.
- A "30.07 euros vs 7.21 euros per million raw reads" comparison (NovaSeq 6000 vs MGI G400RS) comes from a 2021 analysis. It is stale and does not apply to the X.

## Gaps / what I could not find

- **Justia exhibits.** The next step is to pull the original exhibits from the Personalis S-1 (2019), exhibits 10.x on sec.gov. Try the EDGAR index for CIK 1527753, filing year 2019.
- **Customer-level cost per test and per-Gb cost fall after the X move.** None of the second-tier labs disclose it. The only quantified ones remain Guardant (~$200 per test, E043) and Adaptive (gross margin 72% vs 64%, E044).
- **Illumina share of cost of revenue.** None of the 10-Ks I read give it.
- **Fulgent's sequencer fleet.** The 10-K text I could retrieve did not name NovaSeq models. The WebFetch tool summarises pages, so a direct read of the 10-K's Item 1 and Item 7 might still find mentions.
