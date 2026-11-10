# GeneDx (WGS): all evidence in the corpus (2026-10-31)

*GeneDx is a US rare-disease lab that sequences exomes (the protein-coding ~2% of the genome) and whole genomes, mostly for children and NICU (neonatal intensive care) patients. It is an Illumina clinical customer. This note combines two agent sweeps: the primary sources (expert calls, Illumina calls and broker notes) and our own scrape work (GeneDx filings, reimbursement, Gb modeling). The Q2'26 release numbers were re-checked against the SEC exhibit.*

## Bottom line

- **No primary GeneDx document is in `Sources/`.** All hard GeneDx data comes from our scrapes of its SEC filings and Q2'26 call.
- **GeneDx supports the short only modestly.**
  - *For the short:* its revenue per test is falling faster than Illumina's bull case allows. Its genome mix fell in mid-2026. Its CFO is openly planning on lower reagent costs in 2027.
  - *Against the short:* test volume is still growing about 30%. It has no validated alternative sequencer, and no filing or expert shows it leaving Illumina.
- **It is small for Illumina.** On our assumed Gb per test, GeneDx is about 0.5% of Illumina's ~800M Gb a year of high-throughput output.

## 1. Hard data (GeneDx filings)

**Q2'26 results** (8-K Ex. 99.1, 3 Aug 2026; verified):
- Exome/genome volume was **30,785, +32%** y/y.
- Exome/genome revenue was **$100.3M, +17%**. Total revenue was $114.4M (+11%).
- Revenue per test works out to about **$3,258, down ~12%** from ~$3,700. That is our division; the company does not report it.

**Guidance:**
- Q3'26: 33,200 tests, exome/genome revenue of $110–112M, total revenue of $122–124M.
- FY26 (cut in May, reiterated in Aug): revenue of $475–490M, volume growth of at least 30%, exome/genome revenue growth of at least 20%.
- The guide floors imply revenue per test falls about 7.7% for the year (our calc).
- **Q3'26 results are not out as of 31 Oct.** They are expected in early November, before the pitch.

**Genome mix** (Q2'26 call, 3 Aug 2026):
- In the insurance outpatient channel, genomes fell from ~40% (Q1) to **32%** (Q2), with ~30% "maybe slightly lower" expected in H2.
- Reflex exomes (exome first, genome only if the exome is negative) passed genome volume in July 2026.
- The whole-portfolio genome share in Q1 was ~45%. That is a different series, so don't mix the two.
- Per a MarketBeat call summary, the CFO tied the y/y gap between volume and revenue to a higher genome share at lower contracted rates. So genome share is up y/y but down q/q.

**Costs:**
- Cost of services was $36.2M vs $31.8M (+14%). Cost per test is roughly $1,176 vs $1,364 (−14%, our calc).
- The CFO said a genome costs "nearly twice as much to produce than exome… almost entirely higher reagent costs." He expects cost per test "relatively flat" in H2'26, with **"step improvements in 2027"** as "manufacturers advance their technology."

**Suppliers** (FY25 10-K, Note R9):
- One unnamed supplier was **20% of purchases in 2025**, up from 13% (2024) and 11% (2023). The risk factors name Illumina among limited suppliers, but the 20% supplier itself is not named.
- The Q2'26 10-Q shows that supplier at ~14% of quarterly spend vs ~20% a year earlier. That came from a fetch summary, so spot-check it.
- $41.5M of purchase commitments run through 2030 ($16.3M in 2027), with no vendor named.
- No Illumina supply agreement, minimum or price schedule has been found.

**Reimbursement:**
- Coverage is widening: commercial genome coverage rose from 47% to 87% of covered lives, 39 state Medicaid programs now cover exome or genome, and Medi-Cal, Texas, Mississippi and Carelon added coverage in mid-2026.
- Outpatient genome collection rates are weak at **32%, down from 43%**.
- CMS's 2027 proposed fee schedule (21 Sep 2026) cuts genomic sequencing codes about 23%, capped at 15% a year. That covers GeneDx's codes 81415–81427. GeneDx's Medicare revenue share is unknown.

**Governance:** Keith Meister (Corvex) sits on both the Illumina and GeneDx boards and owns ~16.1% of GeneDx (13D/A, May 2026). Corvex bought GeneDx shares in May while selling Illumina.

## 2. Expert calls (weak evidence: the interviewer supplied most of the GeneDx facts)

- **Former Illumina staff scientist, 30 Jul 2026** (L291–293):
  - The interviewer asked "You would not be surprised if GeneDx adopts an alternate platform in the 2020s. Maybe confidence level on that." The expert answered: "I would say 98.5%."
  - His reasoning was about academic long-read projects, not clinical labs. The question was leading, and "adopts" could mean adding a long-read machine rather than replacing Illumina.
  - The same expert says to stay on Illumina for fast NICU work (L273).
  - Do not cite the 98.5% as a switching estimate.
- **PacBio global segment lead (ex-Illumina), 3 Aug 2026** (L103):
  - Names "NICU testing where it's all sent to big centralized reference labs, Labcorp, GeneDx, Quest". There, "it's really down to high throughput technology and then which lab adopts which instrument… When Roche announced… they're focused on these really high throughput testing centers."
  - Same call (L147): "If you're validating an assay on a NovaSeq X, you're probably not going to switch for a while… Illumina is very sticky."
- **Former Roche principal software engineer, 27 Jul 2026:**
  - The interviewer asserted GeneDx "filings talk about how they rely on Illumina" (L363), and gave "100,000 genomes or test volume a year… 400 a day" (L395). Neither figure is verified.
  - The expert: "I don't think anybody's going to replace anyone" (L367).

## 3. Illumina management on GeneDx's market (rare disease; GeneDx is not named)

- **Thaysen, CEO, Q1'26 call, and the JPM conference (Jan 2026):** exome to genome means "15x more sequencing intensity" and is "driving clinical sequencing volume growth above 30%." The JPM deck assumes ">120 Gb per genome vs ~8 Gb for exomes" and calls the model "directional."
- **Dhingra, CFO, JPM (Jan 2026):** whole genome "still makes a smaller fraction of the overall volumes… it's still much, much smaller."
- **Thaysen, Q1'26:** in exome-to-genome conversations Illumina is happy to "continue to lower their cost per gigabase for them." That is the price half of the trade.
- **Q4'25 and Q2'26 calls:** oncology is the main driver, and rare disease is "growing on a healthy speed" but behind it.

## 4. How it nets for the pitch

**Supports the short:**
- Revenue per test is falling (−12%), and CMS proposes about −23% on genomic codes. The genome mix is slipping toward cheaper exomes, so +30% test growth means much less Gb growth. On our assumed depths, roughly +7–18% Gb.
- The CFO is budgeting for reagent cost "step improvements in 2027." A large customer expects Illumina's price per Gb to fall.
- Illumina's own "15x" exome-to-genome story is not showing up in GeneDx's mix this year.

**Cuts against it:**
- Volume is still up ~30%, and coverage is widening into 2027.
- There is no validated second sequencer. Experts on both sides call Illumina sticky for validated clinical work.
- GeneDx is ~0.5% of Illumina's Gb, so it illustrates the rare-disease story rather than measuring it.

## Gaps

- Which sequencer GeneDx runs (NovaSeq X or 6000), and its fleet size.
- Any Illumina contract, price per Gb or rebate terms.
- Sourced Gb per test, including the trio share (child plus both parents).
- GeneDx's Medicare share of revenue.
- Any evaluation of Roche, Ultima, Element or PacBio.
- The Q3'26 results (due early November).
- The final CMS 2027 rates (due November).

## Contradictions to avoid

- **Genome share:** 45% (whole portfolio, Q1) is a different series from 40% and 32% (insurance outpatient).
- **Gross margin:** our files variously say 74% to 70.4%, 71% to 70%, and 56% to 70%. Use the company's ~70% guide and drop the 56% figure.
- **Supplier alternatives:** the 10-K says "some or all" while the 10-Q says "the majority." The "not validated a viable alternative" quote was not re-fetched.

## Sources

- GeneDx Q2'26 8-K Ex. 99.1 (sec.gov, accession 0001628280-26-051852)
- GeneDx Q2'26 10-Q
- GeneDx FY25 10-K (Note R9)
- GeneDx Q2'26 call (Webull transcript, 3 Aug 2026)
- Corvex 13D/A
- CMS CY2027 CLFS proposal
- Expert calls of 27 Jul, 30 Jul and 3 Aug 2026 (`Sources/ILMN/expert_call/`)
- Illumina JPM Jan 2026 conference and deck; Q1'26, Q4'25, Q2'26 and Q3'26 calls
- Our files:
  - `analyses/2026-10-12_lab_peers_vs_genedx_reimbursement_and_data_per_test.md`
  - `analyses/2026-10-12_thesis_scrape_addendum.md`
  - `analyses/2026-10-11_clinical_consumables_scrape/` files 10, 12, 25, 34, 52, 66, 78_81, 100_105, 143_c
  - `Core Notes/16` and `Core Notes/18`
