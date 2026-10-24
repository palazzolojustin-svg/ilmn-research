# Long reads vs short reads, and why the move from exome to genome matters

Prepared 11 Oct 2026 in answer to: "Why would one use long read versus short read, why does the shift to WGS exist, and why do I care about moving from the exome to the genome?" Sources: Core Notes 00, 01, 09; two research agents over the Working Notes (expert calls, ONT/PacBio/ILMN extracts, the clinical-consumables evidence ledger). Labels in brackets say who said it.

## The short answer

- **Short reads (Illumina) are the cheap, accurate workhorse.** They read DNA in fragments of a few hundred letters, in enormous volume. They handle about 90% of what labs need, including nearly all cancer testing.
- **Long reads (Oxford Nanopore, PacBio) see what short reads can't.** They read continuous stretches of thousands to millions of letters. That lets them see large rearrangements, long repeats and which parent a variant came from. They cost more and run slower, so they are a roughly 10% niche that sits beside Illumina rather than replacing it.
- **The shift from exome to genome matters most for you.** An exome reads only the 1–2% of DNA that codes for proteins. A genome reads all of it, finds more diagnoses and replaces several tests with one, and it became affordable once sequencing got cheap. For Illumina, each switch multiplies the sequencing per patient by roughly 10–15 times. That "intensity" is the main reason management can promise 30%+ clinical volume growth. The catch is that the price per gigabase keeps falling, so 15 times the data is not 15 times the revenue.

## 1. Background: what sequencing actually does

Picture a person's DNA as a 3-billion-letter book. No machine can read it end to end. So labs shred many copies into pieces, read each piece, and use software to work out where each piece belongs by matching it to a reference copy of the book. The key design choice is how big the pieces are.

## 2. Short reads vs long reads

**Short reads** (Illumina, Element, Ultima, MGI, Roche's AXELIOS in between) read pieces of about 150–500 letters. Billions are read at once, so they are cheap and highly accurate. Illumina will not launch below Q30, one error in 1,000 letters, and it has Q55–70 on its roadmap.

**Long reads** read pieces of about 10,000 letters (PacBio's "HiFi" reads) up to millions (Oxford Nanopore).

The problem short reads cannot solve is repetition. About half the genome is repeated text. If a 150-letter piece reads "the cat sat on the mat" and that sentence appears in 500 places, the software cannot tell where it goes. A 10,000-letter piece spans the repeat and anchors itself in unique text on either side. That is why long reads win in five situations:

| What you need to see | Why short reads struggle | Example use |
|---|---|---|
| **Structural variants** (big chunks deleted, duplicated, flipped or moved) | The break points sit in repeats; one expert says short reads miss "almost 1/3" in some settings | Rare disease, some cancers |
| **Repeat expansions** (a stretch like CAG-CAG-CAG grown too long) | A repeat longer than the read can't be measured; experts call short reads "completely blind" here | Huntington's, Fragile X, ataxias |
| **Phasing** (which parent each variant came from) | Two variants far apart never land on the same short piece | Recessive disease, HLA transplant matching, drug-response genes |
| **Native methylation** (chemical on/off tags on DNA) | Needs a separate chemical treatment; Nanopore reads it "for free" from untouched DNA | Epigenetics, cancer, ageing research |
| **Whole RNA molecules (isoforms)** | Short pieces can't show which version of a gene's RNA was made | Research, drug discovery |

Short reads win on everything else:
- **Cost.** An Illumina genome lists at about $200, and large customers pay $125–175. A PacBio 20X genome costs $345 and a Nanopore genome about $345 today [JPM; PacBio].
- **Throughput and speed.** Illumina's management says its TruPath product runs 16 genomes in 24 hours, against about 3 genomes for PacBio and about 3 days per sample for Nanopore. That is a management claim.
- **Accuracy where it matters most.** Cancer blood tests hunt for one tumour fragment in a million. The DNA in blood is already broken into short pieces, so long reads add nothing there. Nanopore's accuracy (roughly Q20–35) is "very, very unlikely" to work for MRD (minimal residual disease) testing, according to an Abbott/Exact scientist.
- **Infrastructure.** Validated clinical tests, reference databases and analysis software are all built on short reads.

**Size of the long-read market.** Oxford Nanopore had £224M of revenue in 2025 and PacBio about $160M, together roughly $0.5B. That is about 11–12% of Illumina's $4.3B, which matches the "~10% niche" figure, although interviewers usually supplied that 10% rather than the experts.
- **Both are struggling.** Nanopore cut its 2026 growth guide twice. PacBio cut its revenue and margin guides, pushed cash-flow breakeven to 2028, and its CEO left in August.
- **Clinical use is growing from a small base.** PacBio's clinical consumables rose 55% in 2025, at Children's Mercy, Radboud and Stanford. Nanopore's clinical revenue rose about 35%, with NHS validation underway. Long reads are typically a "reflex" test: they are run after a short-read test comes back inconclusive.

**Why it matters for Illumina.** Long reads are a complement and a small threat, not a big one.
- **Most sources call long reads complementary.** That includes Deutsche Bank and most of the expert panel. One former Illumina scientist is an outlier: he is "98.5%" sure that big labs such as GeneDx adopt long reads. His view of Illumina is dated.
- **Illumina's response is TruPath.** It is a "synthetic long-read" genome that uses short reads plus positional tricks to recover long-range information. It is priced at $395, roughly double a standard genome, so it raises revenue per genome on existing NovaSeq X machines.
  - **Reception is sceptical.** Barclays calls it Illumina's third rebrand of a long-read product; the 2023 version "failed drastically," per one expert. Nanopore calls it "stitching together... not direct."
  - **Expected uptake is small.** Experts expect 0–6% of a core lab's volume.
  - **Its real value may be defensive.** It keeps rare-disease labs, the clinical beachhead for long-read rivals, on Illumina machines.

## 3. Exome vs genome

**What each reads.**
- **Exome (WES):** the protein-coding 1–2% of DNA, where most known disease-causing mutations sit. It needs about 8–11 Gb of sequencing (a Gb is a billion letters).
- **Genome (WGS):** everything, at about 30 reads per letter. That is more than 120 Gb by management's figure, or roughly 100–125 Gb in other sources.

Management's slides say a genome uses about 15 times the data of an exome. Illumina's own spec page implies about 10.6 times, so think "10–15 times."

**Why the shift is happening.**

1. **A genome finds more answers.**
   - It catches what an exome misses: mutations outside genes, missing or duplicated chunks, repeat expansions, mitochondrial DNA, and the reading frame around genes.
   - **Rough yield in rare disease** (one former Illumina associate director's rule of thumb): a gene panel diagnoses about 20% of cases, an exome 40–60%, a genome about 80%.
   - **Be careful with those numbers.** Published studies outside the folder generally find a smaller gain, several percentage points rather than 20–40, and one unsourced figure in the folder even shows the exome slightly ahead. The direction is agreed; the size is not.
2. **One test replaces many.** A child with developmental delay might otherwise get a chromosome microarray, then a gene panel, then an exome, then a repeat test, often over months. A genome can do all of these in one test. Illumina says rare-disease customers use TruPath to "consolidate several tests into one workflow" [Q1'26 call]. From 1 April 2026, England's NHS made the genome the first test for children with developmental delay and restricted microarrays.
3. **Sequencing got cheap enough.**
   - **The X cut the price.** The NovaSeq X cut the sequencing cost of a genome to roughly $200, with $150 coming from Roche and from Illumina's 35B flow cell.
   - **The extra data barely raises the lab's total cost.** Most of a clinical test's cost is interpretation ($500–1,000 a case), and that is similar for an exome and a genome. GeneDx, the largest US rare-disease lab, says its genome costs "nearly double" its exome, not 15 times as much.
4. **Insurers started paying.**
   - **Commercial coverage:** GeneDx says commercial insurance coverage of genomes rose from 47% to 87% of covered lives.
   - **Medicaid:** 39 US states now cover exome or genome testing through Medicaid [GeneDx Q2'26].
5. **The same logic is spreading beyond rare disease.**
   - **Newborns:** England's Generation Study has recruited 52,000 of 100,000 planned babies for genome screening.
   - **Cancer recurrence:** genome-based MRD tests (Natera's Signatera Genome, Personalis, which Tempus is buying for about $1.5B, and Illumina's own MRD kit due in 2027) read the whole tumour genome instead of a 16-mutation panel.
   - **Tumour profiling:** tumour-plus-normal genomes are replacing panels in some centres.

## 4. Why you should care: the economics for Illumina

**This is the volume engine.** Illumina's revenue is gigabases sold times price per gigabase.
- **Each conversion multiplies volume.** Every patient who moves from an exome to a genome multiplies Illumina's volume for that patient by 10–15 times. Moving an MRD test from a small panel to a genome multiplies it more.
- **It explains management's growth claim.** The CEO says exome-to-genome movers are among the "absolutely the largest" clinical customer groups. Intensity is the main reason management says clinical volume will grow "above 30%" for a while.
- **It fits a pattern.** Expert calls say patient counts are maturing: prenatal screening already reaches 70–80% of US pregnancies, and tissue cancer profiling is "quite saturated." More data per patient is how volume keeps growing.

**The shift is better for Illumina than for the lab.** Sequencing is a much bigger share of a genome's cost than of an exome's. Illustratively, at today's X pricing (about $2–3 per Gb):
- an exome generates perhaps $25–50 of sequencing revenue for Illumina;
- a genome generates $200–300.

So the lab's cost roughly doubles, while Illumina's revenue per patient rises roughly six to ten times. This is my illustrative arithmetic, not a disclosed figure.

**Three catches.**
1. **The price per gigabase keeps falling.**
   - **A 15x data jump does not mean 15x revenue.** Labs move to genomes partly because the price fell, and Illumina's revenue per gigabase fell about 19% in the past year.
   - **Converted labs show the lag.** For the 40 fully converted clinical customers, the CFO said the first year after conversion was roughly flat in revenue and growth returned in year two.
   - **The next cut is coming.** The 35B flow cell in 2027 cuts the price per gigabase by about another 20%.
2. **The pace is slower than the story.** Management itself said in January that whole-genome volume is still "much, much smaller" than exome volume, and it gives no genome share. In J.P. Morgan's June survey of clinical labs, exomes and genomes together were 21% of samples, with no change expected in three years.
3. **Bottlenecks outside sequencing.**
   - **Interpretation and storage:** a genome produces far more data to analyse and keep.
   - **Reimbursement:** Medicare has proposed cutting generic genomic-sequencing codes 23% from 2027, capped at 15% a year. One expert says adoption is limited by reimbursement "even if sequencing is free."
   - **Some genome work may go to rivals:** Ultima in some large labs and MRD programmes, Roche, or long reads in rare disease.

## 4b. Follow-up: does "one test replaces many" mean the 15x is overstated?

Partly, but less than it first appears. The right comparison is all the sequencing a patient used to get against the genome that replaces it, not a genome against an exome.

**Most of what a genome replaces is not Illumina sequencing.** In a typical rare-disease workup:
- the chromosome test is usually a microarray, a market led by Thermo Fisher and Agilent rather than Illumina [general knowledge, outside the folder];
- the repeat-expansion test is usually PCR on a capillary instrument, not sequencing [general knowledge].

Losing those tests costs Illumina's sequencing business almost nothing. The two sequencing tests it replaces, the gene panel and the exome, are small in data terms: about 1–3 Gb and about 8–11 Gb.

**So the uplift depends on what the patient used to get.** The table shows the gigabase (Gb) uplift per patient for different prior workups. The ~120 Gb genome figure is management's.

| What the patient used to get | Illumina Gb before | Gb uplift from a genome |
|---|---|---|
| Gene panel only (common in community hospitals) | ~1–3 | ~40–100x |
| Exome only | ~8–11 | ~11–15x |
| Panel, then exome | ~10–14 | ~9–12x |
| Full workup: microarray, panel, exome, repeat PCR | ~10–14 (the microarray and PCR are not sequencing) | ~9–12x |
| Exome, then a follow-up genome if the exome was negative | ~130 | ~1x, no uplift |

Against a full workup, the honest uplift is nearer 9–12x than 15x. Against the many patients who only ever got a panel, it is far higher. The case where cannibalisation truly eats the uplift is the last row: patients who would have received both an exome and a genome anyway.

**Where the real overstatement sits.** The 15x is a data ratio, and three things make the revenue ratio smaller:
1. **Price per Gb.** Genomes run on the biggest, cheapest flow cells, about $2–3 per Gb. Panels and exomes often run on smaller flow cells or benchtop machines at a higher price per Gb. Illumina's revenue uplift per patient is therefore roughly 6–10x, not 15x (illustrative arithmetic).
2. **Lost kit revenue.** A genome needs no exome or panel enrichment kit. Some of those kits are Illumina's, though Twist and IDT are large suppliers [general knowledge]. A small share of Illumina's microarray sales goes to clinical cytogenetics labs.
3. **Reanalysis.** A stored genome can be re-read for free as science advances, so the patient may never need a second test. Under the old model, a negative exome often led to more sequencing later.

**What this means for modelling.**
- **Don't multiply test counts by 15.** In rare disease, consolidation can shrink the number of tests while gigabases rise. Lab test volumes are therefore a poor proxy for Illumina's volume.
- **Model per patient, net of price per Gb.** The useful figure is gigabases per patient across the whole workup, multiplied by the price per Gb on the flow cell actually used.
- **Management's 15x is a per-test ratio, not a forecast.** Management has never said what share of tests convert.

## 4c. Follow-up: when the two key data points come out

**GeneDx's genome-versus-exome mix and revenue per test.** GeneDx is the largest US rare-disease testing lab and a large Illumina customer.
- **Mix:** it reports exomes and genomes as one combined volume and does not disclose the genome share. An unverified search summary of its Q4'25 call says management was tilting the mix toward exomes because genomes face more reimbursement hurdles.
- **Volume:** combined volume was 30,785 tests in Q2'26, up 32%. Exome/genome revenue rose 17% to $100.3M. Q3'26 guidance is 33,200 tests and $110–112M.
- **Revenue per test:** the blended average reimbursement was $3,258 in Q2'26, down about 12% from about $3,700 a year earlier. The Q1'26 figure is unverified.
- **Collections:** the outpatient genome collection rate was 32%, against 43% a year earlier.
- **Coverage:** commercial genome coverage rose from 47% to 87% of insured lives.
- **Next report:** Q3'26 results are expected in the last week of October 2026. Aggregators say 27 or 29 October; nothing is confirmed. Last year's Q3 came on 28 Oct 2025.

**The 35B flow cell price.** Illumina has declined to give a price three times: at Stifel, at TD Cowen in March 2026 and on the Q1'26 call. Management says the price will come closer to launch.
- **Launch:** H1 2027, according to Illumina's roadmap page. One expert expects January 2027.
- **Most likely venues for the price:** a launch press release, the JPM Healthcare Conference in mid-January 2027, Q4 results in early February, or AGBT in February. This is our inference.
- **Expectations:** about $2.00 per Gb from about $2.50, roughly −20% [ex-Illumina expert]. UBS has about $150 per genome if the 35B is priced like the 25B.

Sources: GeneDx Q2'26 release (BioSpace copy); evidence ledger E081 and E091; Illumina Q1'26 call and TD Cowen 3 Mar 2026; expert call of 31 Jul 2026; UBS 3 Mar 2026.

## 5. What to watch

- Illumina disclosing any whole-genome share of clinical volume. It has not so far.
- GeneDx's genome-versus-exome mix and revenue per test.
- The 35B flow cell price in 2027.
- Final Medicare 2027 rates, due in November.
- TruPath revenue or customer counts.
- Whether genome-based MRD tests (Illumina's kit, Personalis under Tempus, Signatera Genome) win reimbursement and volume.
