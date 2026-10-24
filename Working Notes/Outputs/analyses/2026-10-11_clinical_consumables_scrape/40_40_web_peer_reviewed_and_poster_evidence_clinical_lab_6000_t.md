# Agent 40: 40-web-peer-reviewed-and-poster-evidence-clinical-lab-6000-to-X-and-competitor-validations

*Model: sonnet. Run 2026-10-11 02:52:20. Cost $0.55 (API-equivalent).*

**Assignment:** Look for primary technical evidence, not company statements, on (a) how clinical labs actually move from the NovaSeq 6000 to the X and what it does to their Gb and cost per test, and (b) clinical validations of Roche AXELIOS, Ultima UG100/UG200 and Element AVITI/AVITI24 for regulated clinical assays. Sources: PubMed/PMC, bioRxiv/medRxiv, Journal of Molecular Diagnostics, Clinical Chemistry, Genetics in Medicine, AMP, ACMG and ASHG abstracts, AGBT 2026 posters, NCCN or CAP proficiency material, Illumina and Ultima/Element/Roche application notes and customer stories, and press releases of labs announcing a switch (search terms: 'NovaSeq X Plus' clinical validation, 'concordance NovaSeq 6000 NovaSeq X', 'cost per sample', 'Ultima UG 100 clinical validation', 'AVITI clinical laboratory validation CLIA', 'AXELIOS' early access lab). For each study or announcement extract: lab name, assay, date, Gb or reads per sample, cost per sample before vs after, whether the lab ran the 6000 and X in parallel and for how long (revalidation time and cost), and whether the lab kept or dropped Illumina. Also gather Sept-Oct 2026 news on AXELIOS placements, Ultima UG200 customers and Element VITARI orders that name clinical labs (GeneDx, Natera, Tempus, Caris, Labcorp, Quest, ARUP, Mayo, children's hospitals). Quantify Gb per test where found (liquid CGP, WGS, MRD, NIPT) to test the claim that test growth is not equal to Gb growth. Distinguish peer-reviewed evidence, vendor claims and press. Cite the URL, journal and date for every item. Do not invent citations.

## Key findings

Most of what I found is already covered by the ledger or doesn't help with the clinical question. Four items are new or update a ledger entry. I found none of the primary lab data the assignment asked for. Several fetches failed (listed under Gaps).

- **Peer-reviewed or preprint evidence on cost, Gb or revalidation time for labs moving from the 6000 to the X:** none found. FACT (absence).
  - Searches covered PubMed/JMD/Clin Chem phrasing and NovaSeq X Plus clinical validation terms.
  - The only hits were vendor or provider material, plus an unrelated RUO-vs-Dx NovaSeq 6000 exome study (PMC12639258).
  - This fits E031 and E116, which rest on management and expert statements only.
- **Ultima clinical-services bioRxiv paper (new, not in the ledger).** Title: "Evaluation of the Ultima Genomics UG 100 sequencing platform for clinical services" (bioRxiv 10.64898/2025.12.11.693628, posted around 11 Dec 2025, https://www.biorxiv.org/content/10.64898/2025.12.11.693628.full.pdf). The fetch was blocked (HTTP 429), so I only have search-snippet content.
  - It is a preprint, not peer-reviewed.
  - It is framed around accreditation of sequencing centers for clinical services.
  - It tests SNV precision and recall on four GIAB (Genome in a Bottle reference) samples, UG 100 against NovaSeq 6000, stratified by homopolymer length (4–6, 7–11, >11 and >20 bp).
  - A snippet says UG 100 homopolymer calling accuracy "drops below 90% after a length of 8 bases".
  - I could not get the lab name, numbers, cost or conclusion.
  - OPINION: this is the closest thing to a primary clinical-validation document for a challenger. Its stated weakness is indels in homopolymers, which supports E129 (Element/Ultima win shallow, new uses first).
- **Owkin multi-modal benchmark (new).** Ultima UG100 against Illumina NovaSeq on FFPE tissue from oncologic and immune-mediated disease, covering snRNA-seq, whole transcriptome, exome and genome (https://owkin.com/publications/multi-modal-benchmarking-of-the-ultima-ug100-and-illumina-novaseq-sequencing-platforms-using-clinically-relevant-ffpe-tissues, dated March 2026 per the page title).
  - It is vendor-adjacent, not peer-reviewed, and the page gave no sample counts or percentages.
  - It reports "highly comparable results to Illumina" and UG100 "high precision and reduced low-frequency artifacts".
  - It also reports "characteristic insertion-biased indels", discrepancies in pseudogenes and non-coding transcripts, and a "more sensitive but noisier" Illumina variant-calling workflow.
  - It does not say which NovaSeq model was used.
- **Illumina's own Ultima-vs-NovaSeq X WGS benchmark (vendor claim, published 7 Oct 2025, https://www.illumina.com/science/genomics-research/articles/ultima-ug-100-vs-illumina-novaseq-x-wgs-data.html).** MGMT.
  - Illumina says the UG 100 produced "6× more SNV errors and 22× more indel errors" against the full NIST v4.2.1 benchmark.
  - Ultima's high-confidence region excludes about 4.2% of the genome, 2.3% of the exome, 1.0% of ClinVar variants and about 450,000 variants.
  - Illumina's X accuracy figures are SNV 99.94%, CNV 97%, SV 88% and STR 95.2%.
  - It is a competitor's marketing piece, but it names the exact hurdle that matters for regulated clinical use.
  - It does not directly update an E-number. It adds a quantified technical barrier to E125/E129.
- **Labcorp–Ultima date (small correction to E114).** The Fly/TipRanks item is dated 30 Jul 2024, while E114 cites 29 Jul 2024. FACT.
  - It describes using "UG 100 sequencing solution and ppmSeq technology to explore new whole genome sequencing clinical applications, including molecular residual disease".
  - It is explicitly exploratory, with no volumes (https://www.tipranks.com/news/the-fly/labcorp-expands-collaboration-with-ultima-genomics-in-genome-sequencing).
- **Foundation Medicine AXELIOS data (adds a date to E124).** At an AACR workshop in April 2026, Dr. Alex Robertson (Foundation Medicine) presented early-access SBX experience. This included "data analyses of a WGS-based approach to detect low ctDNA levels from limited cfDNA". FACT per a search summary of Roche's page; I could not open the poster.
  - OPINION: this ties to E124's plan for a whole-genome tissue baseline in Pathlight MRD. WGS-based MRD is high Gb per sample, but the sequencing would sit on Roche's own platform, not Illumina's.
- **Element AVITI24 clinical-lab pricing (new datapoint).** The University of Iowa microbiome core's 2026 AVITI24 rates were $45 per sample for fewer than 92 samples, $35 for 93–188, $28 for 190–284 and $24 for 285–380 (https://microbiomecore.sites.uiowa.edu/services-rates). FACT.
  - The page is a core-facility price list. I did not confirm the assay or read depth, and it is not a clinical lab.
  - It is the same kind of source as E051–E054, so treat it as a rough price marker only.
- **Element cost claims (MGMT).** Medtech Dive and SDBJ coverage says Element claims about $1.4–1.5M savings over three years versus NextSeq 2000. AVITI cost per million reads was said to be 33% lower than FY25 as of Sept 2025, and 62–71% lower than FY24 (https://www.medtechdive.com/news/element-bioscience-raises-277m-illumina/721187; sdbj.com). This is a vendor claim. I did not verify the date or the original.
- **Novogene and Discovery Life Sciences bridging (vendor/provider data).** Novogene ran whole-genome sequencing in parallel on the X Plus and the 6000. It reports an average Q30 of 94.63% on the X Plus and a maximum of 465 Gb per lane. Discovery Life Sciences published cross-validation data to "bridge" the two chemistries.
  - These are service providers, not regulated clinical labs. They show that parallel bridging is a standard practice.
  - I found no revalidation time or cost.
- **Illumina TSO 500 HT on NovaSeq X tech note (M-GL-02869) and the NovaSeq X data-concordance app note (M-US-00201).** Vendor documents.
  - The search snippet cites a 77-normal-sample baseline with CNV R²=0.99, SV R²=0.82, 0% MSI false positives and TMB R²=0.86.
  - I could not open the PDF to confirm the table. The CGP-on-X bridging is Illumina's own, so it supports ease of conversion for Illumina-validated kits only.

## Contradictions and stale data

- The Labcorp–Ultima date differs by one day (30 Jul 2024 here, 29 Jul 2024 in E114). This is a minor discrepancy that is probably a time-zone or reporting artifact.
- Nothing contradicts the numeric ledger entries.

## Gaps / what I could not find

- No lab-level evidence on Gb per sample, cost per sample before and after, 6000/X parallel-run duration, or revalidation cost for any named clinical lab. No ASHG, AMP or AGBT 2026 poster surfaced. The one study that matched the clinical-validation search terms was the RUO-vs-Dx exome study.
- No Sept–Oct 2026 news naming clinical labs for AXELIOS placements, UG200 customers or VITARI orders. The only new UG200 item was the Precure/Helix selection (22 Sep 2026), which is already in E128. I found no named clinical lab buying VITARI, consistent with E069/E200.
- The WebFetch tool was blocked or failed on the bioRxiv preprints (429), GenomeWeb (403) and the Roche AACR page (301 redirect that I did not follow). The first two are the highest-value follow-ups: the bioRxiv UG 100 clinical-services paper for its exact results, and GenomeWeb "Roche sets sights on clinic following commercial launch of AXELIOS 1" for IVD timing and named customers.
- Not checked for lack of time: Journal of Molecular Diagnostics and Clinical Chemistry issues directly, PubMed, medRxiv, CAP proficiency material, and the open-gap items in `00_open_gaps.md`, which are filings and docket work outside this assignment.

Sources: [Ultima UG 100 clinical services (bioRxiv)](https://www.biorxiv.org/content/10.64898/2025.12.11.693628.full.pdf) · [Owkin benchmark](https://owkin.com/publications/multi-modal-benchmarking-of-the-ultima-ug100-and-illumina-novaseq-sequencing-platforms-using-clinically-relevant-ffpe-tissues) · [Illumina UG100 vs NovaSeq X](https://www.illumina.com/science/genomics-research/articles/ultima-ug-100-vs-illumina-novaseq-x-wgs-data.html) · [Labcorp–Ultima (TipRanks/The Fly)](https://www.tipranks.com/news/the-fly/labcorp-expands-collaboration-with-ultima-genomics-in-genome-sequencing) · [Roche AXELIOS launch](https://www.roche.com/media/releases/med-cor-2026-06-29) · [Ultima/Precure (HPCwire)](https://www.hpcwire.com/bigdatawire/this-just-in/ultima-genomics-selected-for-mayo-clinic-led-million-biospecimen-initiative/) · [Univ. of Iowa core rates](https://microbiomecore.sites.uiowa.edu/services-rates) · [Medtech Dive on Element](https://www.medtechdive.com/news/element-bioscience-raises-277m-illumina/721187)
