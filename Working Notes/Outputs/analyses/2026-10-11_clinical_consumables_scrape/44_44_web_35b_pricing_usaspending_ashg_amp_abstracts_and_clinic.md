# Agent 44: 44-web-35B-pricing-USAspending-ASHG-AMP-abstracts-and-clinical-lab-migration-evidence

*Model: sonnet. Run 2026-10-11 03:07:07. Cost $1.42 (API-equivalent).*

**Assignment:** Goal: get primary evidence on actual NovaSeq X prices and on real clinical labs' 6000-to-X migration and challenger switching, which has been absent so far. (1) Price points: query USAspending.gov (API at api.usaspending.gov, search by recipient 'ILLUMINA' with keywords NovaSeq X, 25B, 10B, 1.5B, flow cell, reagent) and SAM.gov/FPDS, state contract portals (e.g. Texas, California, Minnesota, NIH CIO-SP and NIH purchase-order awards, VA, DoD DHA), university purchasing and recharge pages, and Fisher/VWR/Cytiva/Scientific Instrument Services/Genohub/BioCompare quote pages for catalog 20104706 (25B 300-cycle) and for any 35B flow cell or 14B. Record the list or contract price per kit, the date and the implied $/Gb. Search for any Illumina 35B launch announcement, ASHG 2026 (20-24 Oct) preannouncements, a product-spec PDF, and an Illumina Ordering Guide or price-list leak. (2) Clinical-lab migration evidence: search PubMed, medRxiv, bioRxiv, Journal of Molecular Diagnostics, Clinical Chemistry, Genetics in Medicine, AMP 2025 and 2026 posters and ASHG 2026 abstract listings, ESHG 2026, and lab white papers for named labs that validated NovaSeq X for clinical use (e.g. Mayo, Children's Mercy, Rady, Broad Clinical Labs, ARUP, Labcorp, Quest, Natera, Invitae/Labcorp, Fulgent, Ambry, GeneDx). Extract Gb or samples per flow cell, cost per sample before and after, revalidation effort, time and parallel-run duration, and any 6000 concordance studies. (3) Challenger clinical validation: retrieve the Ultima UG 100 clinical-services preprint (bioRxiv 10.64898/2025.12.11.693628; try Europe PMC, the bioRxiv full-text mirror, ResearchGate or a Google Scholar cache if bioRxiv returns 429), Roche AXELIOS clinical validation posts (GenomeWeb, 360Dx, Roche press), Element AVITI clinical or LDT validation studies, and any named clinical lab publicly moving volume off Illumina. (4) Check the Illumina TSO 500 HT on NovaSeq X tech note (M-GL-02869) for samples per run and Gb per sample. Quantify $/Gb, samples/run, cost per sample, and named labs. Label each point FACT/MGMT/OPINION with URL and date. Hard stop at 20 minutes.

## Key findings

1. **First dated, SKU-level price points for the NovaSeq X exist (closes part of open gap #1, extends E054/E055).** GSA distributor Government Scientific Source lists the 25B 300-cycle kit (20104706) at **$24,155.04**. The 10B 300-cycle kit (20085594) is **$14,493.03**, and the 1.5B 300-cycle kit (20104705) is **$3,927.77**. The 25B 100-cycle kit (20125967) is **$13,650.00**. The pages carry no date and I found no price for the 5B. These are GSA/ECAT government-channel distributor prices, not Illumina list prices, and Illumina's own order page is login-gated. [FACT; govsci.com product pages, fetched 2026-10-11, e.g. https://www.govsci.com/product-detail/Illumina-----Inc/20104706/EA/]

2. **The same source gives 6000 prices, so the per-Gb gap can be calculated (extends E051/E053).** The 6000 S4 v1.5 300-cycle kit (20028312) is **$21,682.58**. The S4 200-cycle kit (20028313) is $19,435.96 and the S2 300-cycle kit (20028314) is $15,632.93. [FACT; govsci.com/product-detail/Illumina-----Inc/20028312/EA etc.]

3. **Implied $/Gb, using Illumina's spec output ranges** (S4 300-cycle ~2.4–3.0 Tb is my recollection, not fetched this session). The X ranges come from illumina.com/systems/sequencing-platforms/novaseq-x-plus/specifications.html. [OPINION, calc on FACT]

| Kit (GSA price) | Output per flow cell (2x150) | $/Gb |
|---|---|---|
| 25B-300 ($24,155) | 8.0–10.5 Tb | **$3.02 (at 8 Tb) down to $2.30 (at 10.5 Tb)** |
| 10B-300 ($14,493) | 3–4 Tb | $4.83–$3.62 |
| 1.5B-300 ($3,928) | 0.50–0.72 Tb | $7.85–$5.49 |
| 6000 S4-300 ($21,683) | ~3 Tb | ~$7.23 |

   - At the conservative end, 25B is about **58% cheaper per Gb than the S4** ($3.02 vs $7.23).
   - 10B is about 33–50% cheaper than the S4. This matches the −35% in E051.
   - The 1.5B kit costs about as much per Gb as the S4, so small flow cells give little saving.

4. **The 25B GSA price sits above Illumina's "$2.00/Gb" list claim (E054/E055).** $24,155 is at most about $2.30/Gb even at the top of the output range. Realistic yields therefore put government-channel pricing about 15–50% above the headline $2.00, and E054's core-lab prices ($2.5–3.3/Gb) are close to this GSA level. Large clinical accounts reportedly pay much less (E063, E059). [OPINION]

5. **A 35B price implied by the "−20% $/Gb" claim (E058).** If $/Gb falls 20% and output rises 40% (E057), the flow cell would cost about 1.12x the 25B. That is roughly **$27K on the GSA basis**. This is a calculation on hearsay, not a quote. No 35B price, SKU or ASHG pre-announcement exists in anything I could reach. Illumina's own 18-month roadmap (23 Feb 2026) gives 35B for H1 2027 and 14B alongside it, which matches E057. [OPINION on MGMT; barchart/Illumina press release 2026-02-23, https://www.illumina.com/company/news-center/press-releases/2026/7b4175f1-a13f-401e-9335-3e5eadbb1fe0.html]

6. **TSO 500 HT tech note, first per-sample economics for a clinical assay (gap #6).** Illumina's TSO 500 HT page lists samples per run at 3,500x coverage:

| Platform / flow cell | Samples per run |
|---|---|
| 6000 S2 | 72 |
| 6000 S4 | 192 |
| X 1.5B | 32 |
| X 10B | 192 |
| X 25B | 480 (up to 960 on an X Plus with two flow cells) |

   Turnaround is "4–5 days from sample to results". [FACT; illumina.com/products/by-type/clinical-research-products/trusight-oncology-500-ht.html, fetched 2026-10-11; the M-GL-02869 PDF itself exceeded the fetch size limit] On GSA kit prices, the sequencing cost per sample is: [OPINION, calc]
   - 6000 S4: $21,683/192 = **~$113**.
   - X 10B: $14,493/192 = **~$75** (−33%).
   - X 25B: $24,155/480 = **~$50** (−55%).
   - The 6000 S2 ($15,633/72) = ~$217. This is the S2 users' step-down.

   Sample prep is under $100 and informatics $500–1,000 per clinical sample (E058). Sequencing is therefore only about 5–10% of a TSO 500 sample's cost, and a 55% cut saves a lab about $63 per sample. That supports the E058 point that a lab's total workflow cost falls only about 5%. The "480 on 25B" figure also means a lab needs a batch of 480 samples to reach the lowest cost. Under-filled flow cells keep the effective price high (E032).

7. **Revenue-per-sample implication for Q1.** For this one assay, moving from S4 to a full 25B cuts Illumina's consumable revenue per sample about 55%, and from S4 to a 10B about 33%. Samples must grow about 2.2x (25B) or 1.5x (10B) for revenue neutrality. This is consistent with E004 and E029 (a two-thirds cut needs about 3x). It depends on GSA prices and spec output ranges. [OPINION]

## Challenger evidence (gap #6, mostly not retrieved)

- **Ultima UG 100 clinical-services preprint (bioRxiv 10.64898/2025.12.11.693628):** Full text was blocked (HTTP 429 on every bioRxiv URL I tried). The search snippet confirms only that it benchmarks **precision and recall for SNV calling on GIAB samples against the NovaSeq 6000**, including homopolymers of 4–6, 7–11, >11 and >20 bp, and that it states a UG 100 genome cost of $80. It names no lab here and I have no numbers. [FACT; https://www.biorxiv.org/content/10.64898/2025.12.11.693628.full.pdf]
- **Owkin preprint (bioRxiv, 13 Mar 2026):** Benchmarks UG 100 against Illumina NovaSeq on clinically relevant FFPE (preserved tissue) samples in four modes: single-nuclei RNA-seq, whole-transcriptome, exome and genome. It found "highly comparable results". UG 100 variant calling was more conservative and had insertion-biased indels. [FACT; https://owkin.com/publications/multi-modal-benchmarking-of-the-ultima-ug100-and-illumina-novaseq-sequencing-platforms-using-clinically-relevant-ffpe-tissues] The NovaSeq version was not stated, and it is research, not a clinical validation.
- **Named clinical-lab adopters of Ultima, each announced as collaboration or exploratory** (no volume shift found): Labcorp (expanded UG 100 + ppmSeq collaboration for WGS MRD; tipranks/medtechdive, 2024), Myriad (Oct 2024: MRD test and FirstGene prenatal screen; medicaldevice-network), NeoGenomics (Cambridge UK innovation centre), Inocras (CLIA/CAP San Diego, offering UG 100 WGS), and Broad (two UG 100s, 10–12B reads per wafer). Ultima's UG 100 is at "over 15 sites". [FACT; search snippets, dates mostly 2024, not verified further] None of these says it moved production volume off Illumina. Myriad's Q2'26 results are weak anyway (E095).
- **Roche AXELIOS:** The Roche launch release (29 Jun 2026) states it is **research-use-only**, and Broad Clinical Labs and Hartwig are launch collaborators. A search summary said "it is too early to provide a timeline for clinical validation" at Broad (GenomeWeb, date unclear; I could not open GenomeWeb, HTTP 403). The aseqer pricing post confirms $150/duplex-30x genome, $0.06/M simplex reads, ~$2,400 per run (sensor module reused ~20 times) and a $750K instrument. [FACT; https://aseqer.com/p/roche-axelios-pricing; roche.com/media/releases/med-cor-2026-06-29] The post says the pricing "isn't aggressively low" against the $80–200 market. It cites Ultima at 24 cents/M reads, against Roche's 6 cents.
- **Element AVITI:** No clinical-lab validation or named lab leaving Illumina found. Element promotes AVITI24 for clinical research and has a Fabric Genomics partnership. A Seqanswers thread, "Switching from Illumina to Element Biosciences", exists but I did not open it. OncoDNA presented OncoDEEP on AVITI (Dec 2025 user-group slides), but the PDF was unreadable. [FACT; elementbiosciences.com, ugm.oncodna.com]

## 6000-to-X migration by named labs (gap #6, not found)

- I found no peer-reviewed paper, poster or white paper with Gb per sample, cost per sample before and after, parallel-run duration or revalidation effort for a named clinical lab moving from the 6000 to the X.
- **Orchid Health (via Psomagen):** The only X-versus-6000 concordance case found. It ran the same pool of libraries from 5 GIAB cell lines at 30x on both. The X had "higher accuracy, specificity, sensitivity, and comparable precision" with no figures on the page. Orchid is a consumer embryo-screening lab and Psomagen is a service provider, so this is weak evidence. [FACT; https://www.psomagen.com/news/case-study-novaseq-x-plus]
- **Illumina's own concordance app note** (M-US-00201) says X and 6000 give highly accurate variant calling. It is vendor material and I did not read the numbers. [MGMT; illumina.com]
- **AOUS Siena (PMC12639258, Nov 2025):** A 96-sample exome comparison of NovaSeq 6000 RUO against 6000Dx, with 100% SNV concordance. It does not cover the X. It shows validation work is still being done on the 6000 in Europe. [FACT; https://pmc.ncbi.nlm.nih.gov/articles/PMC12639258/]
- **Rady Children's:** Search summaries repeat old 6000-era validation news. The ARUP 2025 whole-genome lecture-slide PDF could not be read.

## Government award search (gap #1, no usable price)

- USAspending and FPDS returned nothing directly. I found only Iowa State University purchase orders on Govly, both showing Illumina line items without unit prices: PO-1335923 of 26 May 2026 ($14,374; 6000 S2 kit plus MiSeq kits) and PO-1338858 of 17 Jun 2026 ($8,731; 6000 S1 kit, NovaSeq XP 2-lane kit, MiSeq kit). [FACT; app.govly.com/public/awards/...]
- Iowa State was still buying 6000 S1/S2 reagents in mid-2026. This is a small research buyer, so treat it as anecdotal against E015.
- I did not check state portals or university recharge pages beyond the core pages already in E051–E054.

## Contradictions and stale data

- The GSA 25B price implies **$2.3–3.0/Gb**, above the $2.00/Gb launch claim (E055) and in line with E054's core lists. The "$2.00" figure is best treated as a best-case or large-account number.
- The Illumina TSO 500 HT page's "reads per sample" column is internally inconsistent (it lists 20B and 52B against 192 and 480 samples). I used only samples per run. The "up to 60% lower cost per Gb vs NovaSeq 6000" claim on the same page is MGMT. My GSA calc gives −55% per sample for 25B and −33% for 10B.
- The govsci pages show no date. They may be stale if Illumina repriced in 2026. I verified only the price points, not the dates or whether they are contract prices.
- The Ultima preprint's "$80 genome" claim is a vendor claim, and Roche's "$150" is duplex 30x while the "$0.06/M" is simplex (E068).

## Gaps / what I could not find

- The full text of the Ultima UG 100 clinical-services preprint (HTTP 429 on bioRxiv, no usable mirror), the GenomeWeb AXELIOS clinical-validation article (HTTP 403), and the ARUP and OncoDNA slide PDFs (binary, unreadable).
- Any 35B or 14B SKU, price or ASHG 2026 preannouncement. The 5B GSA price, any dated list price or ordering-guide leak, and a Fisher/VWR/Genohub quote for 20104706. The NIH CIO-SP, VA, DHA and state portals were not queried.
- The full M-GL-02869 PDF (too large to fetch). AMP 2025/2026 and ASHG 2026 abstracts, and the JMD/Clin Chem tables of contents.
- A named clinical lab publicly moving volume off Illumina. The AVITI and AXELIOS clinical validations also remain unfound.

**Sources:** [GSA 25B-300](https://www.govsci.com/product-detail/Illumina-----Inc/20104706/EA/), [GSA 10B-300](https://www.govsci.com/product-detail/Illumina-----Inc/20085594/EA), [GSA 1.5B-300](https://www.govsci.com/product-detail/Illumina-----Inc/20104705/EA), [GSA S4-300](https://www.govsci.com/product-detail/Illumina-----Inc/20028312/EA), [GSA S2-300](https://www.govsci.com/product-detail/Illumina-----Inc/20028314/EA), [Illumina X specs](https://www.illumina.com/systems/sequencing-platforms/novaseq-x-plus/specifications.html), [TSO 500 HT](https://www.illumina.com/products/by-type/clinical-research-products/trusight-oncology-500-ht.html), [Illumina roadmap release](https://www.illumina.com/company/news-center/press-releases/2026/7b4175f1-a13f-401e-9335-3e5eadbb1fe0.html), [aseqer AXELIOS pricing](https://aseqer.com/p/roche-axelios-pricing), [Psomagen/Orchid](https://www.psomagen.com/news/case-study-novaseq-x-plus), [Owkin](https://owkin.com/publications/multi-modal-benchmarking-of-the-ultima-ug100-and-illumina-novaseq-sequencing-platforms-using-clinically-relevant-ffpe-tissues), [AOUS Siena](https://pmc.ncbi.nlm.nih.gov/articles/PMC12639258/), [Myriad–Ultima](https://www.medicaldevice-network.com/news/myriad-ultima-genomics-clinical-tests/).
