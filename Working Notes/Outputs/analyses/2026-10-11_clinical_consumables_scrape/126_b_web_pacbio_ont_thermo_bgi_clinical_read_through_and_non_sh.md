# Agent 126: B-web-PacBio-ONT-Thermo-BGI-clinical-read-through-and-non-short-read-substitution

*Model: sonnet. Run 2026-10-11 11:48:00. Cost $0.41 (API-equivalent).*

**Assignment:** Look at competitors not yet covered in depth (prior agents 14, 23, 56, 100 focused on Roche AXELIOS, Element, Ultima; 86 and 89 covered MGI/ONT H1 China). Pursue: (1) PacBio Q2 2026 results, 10-Q and call (Revio/Vega/Sequel IIe clinical placements, SPRQ pricing, per-genome cost, clinical customers such as GeneDx, Children's Mercy, Radboud, Mayo, PerkinElmer/Revvity, and any statement on rare-disease long-read as a complement or substitute to Illumina WGS); (2) Oxford Nanopore H1 2026 results, London Calling 2026 and clinical program announcements (UK NHS, Genomics England, Cancer Research UK, Epi2me clinical, MRD or methylation workflows), price per Gb on PromethION; (3) Thermo Fisher Ion Torrent Genexus / Oncomine Dx Express Test 2026 placements and read-through to targeted CGP at labs that could move off Illumina; (4) BGI / Complete Genomics / MGI US-ex-China clinical placements and the US BIOSECURE Act status. Quantify price per Gb or per genome, instrument price, installed base or placements, named clinical labs, and any statements about Illumina share loss or pricing. Report whether any named clinical lab with Illumina volume has moved production volume, not just validation. Cite URL, publisher and date for each item; mark FACT, MGMT or OPINION; flag anything contradicting that Illumina clinical share loss is minimal.

## Key findings

Almost all of what I found is already in the ledger (E069, E070, E131, E133, E134). The additions below are small and mostly quantify or qualify those items. Nothing I found contradicts "Illumina clinical share loss is minimal."

- **No named clinical lab moved production volume (FACT, negative finding).** I found no 2026 report of a lab shifting clinical production sequencing from Illumina to PacBio, ONT, Complete Genomics, Element, Ultima or Roche. One search targeted this and returned only generic platform news. Treat it as "not found", not proof that none exists. [WebSearch, 2026-10-11; GenomeWeb ASHG roundup, date not captured]
- **BIOSECURE Act is law but does not reach private clinical labs (FACT).** It passed in the FY2026 NDAA. It names no companies and relies on the DoD 1260H list, which currently includes BGI Group, BGI Genomics and MGI Tech. Complete Genomics is not on that list.
  - The OMB list of designated companies is due by December 2026.
  - FAR (federal procurement rules) revisions follow within one year. Effective dates are 60 days (1260H entities) or 90 days (others) after that.
  - Contracts signed before the effective date are grandfathered for five years.
  - The restriction applies to federal contracts and grants, not to private labs buying sequencers.
  - Implication (OPINION): any BGI/MGI-driven switching in US clinical labs is unlikely before 2027–28. This adds detail to E131's "low threat" view. [Arnold & Porter, Dec 2025, https://www.arnoldporter.com/en/perspectives/advisories/2025/12/the-biosecure-act-becomes-law-in-the-united-states; Mondaq, https://www.mondaq.com/unitedstates/healthcare/1725294/the-biosecure-act-becomes-law-in-the-united-states]
- **Complete Genomics now sits outside the BGI/MGI group (FACT).** Swiss Rockets AG agreed to acquire it (announced Feb 2026), and it says it will stay a US-based organisation. This fits the ledger's E131 "$50M" figure and may partly insulate it from BIOSECURE. At AGBT 2026 it launched the DNBSEQ-T7+ (multi-flowcell, PE150). [levinassociates, 2026-02-23, https://healthcare.levinassociates.com/2026/02/23/swiss-rockets-ag-acquires-complete-genomics/; Complete Genomics Q1'26 newsletter, https://www.completegenomics.com/newsletter-q1-2026/]
- **PacBio Q2'26 details beyond E131 (FACT/MGMT).** [PacBio press release, 2026-08-05, https://www.pacb.com/press_releases/pacbio-announces-second-quarter-2026-financial-results/]
  - Revenue was $39.0M. Consumables were $20.1M, against $18.9M a year earlier (+6%), so the +67% clinical shipments sit inside slow overall consumables growth.
  - Non-GAAP gross margin was 36%, down from 38%. Management attributed it to compute and memory costs and "multi-system pricing concessions". That is evidence of price pressure, not pricing power.
  - FY26 revenue guidance is $155–165M.
  - Vega placements fell to 26, from 38 a year earlier. Revio placements were 20 (15 a year earlier). 60% of Revio placements went to new customers and 45% were multi-instrument orders.
- **Rare-disease long-read evidence points to complement, not substitute (FACT/OPINION).** PacBio cites an NEJM paper, "Clinical Long-Read Genome Sequencing for Rare-Disease Diagnostics" (Radboud UMC). It models HiFi WGS as a first-tier test, with diagnostic yield rising from 16.4% to 18.9% (more than 500 extra patients a year).
  - PacBio frames this as "first-tier", which is a substitute claim for Illumina WGS in rare disease. That is the one competitive claim worth watching.
  - Price is the barrier: $345 per 20x genome list, against Illumina short-read costs well below that (OPINION).
  - [PacBio press release, 2026-08-05; PacBio blog on Radboud, https://www.pacb.com/blog/radboud-umc-research-highlights-promise-of-hifi-long-read-sequencing-to-match-standards-of-care-in-rare-disease-genomics/]
- **ONT / Genomics England (FACT).** [Genomics England L&C26 talk, https://nanoporetech.com/resource-centre/long-read-sequencing-at-genomics-england-lc26; UK Find a Tender notice, https://www.find-tender.service.gov.uk/Notice/039504-2024]
  - A contract for long-read WGS instruments and consumables was awarded to ONT on 6 Dec 2024, worth £5.23M.
  - Genomics England has run more than 15,000 PromethION flow cells since 2019.
  - The cancer project covers about 2,000 germline:tumour pairs, moving next to haemato-oncology, sarcoma and brain tumours.
  - ONT also announced a UK partnership including pathogen surveillance across 30 NHS sites.
  - Scale is tiny against Illumina's NHS short-read base. This is a research-to-clinical pilot (OPINION).
- **ONT H1'26 context (FACT).** Revenue was £116.7M (+11%), below internal expectations because of China and the Middle East. Gross margin was 62.2% (+400bp). Clinical was £17.6M, 15% of revenue (matches E131). [ONT H1 RNS via directorstalkinterviews.com, Aug 2026]
- **Thermo Fisher (FACT).** The Oncomine Dx Express Test on Genexus Dx has FDA approval, announced February 2026. It is a companion diagnostic for ZEGFROVY and for tumor profiling, with results in about 24 hours. Biodesix is the first lab offering it. This is small-panel, fast-turnaround testing, not the high-throughput sequencing that drives NovaSeq consumables. I found no placement counts. [MLO Online / CLP Magazine, Feb 2026, https://www.mlo-online.com/diagnostics/news/55301480/thermo-fishers-ngs-assay-receives-fda-approval-as-a-companion-diagnostic-for-zegfrovy-and-for-tumor-profiling]

## Contradictions and stale data

- E131 says PacBio pull-through is about $202K per system. The press release confirms this as annualized Revio pull-through.
- E131 cites 20 Revios "mostly clinical". The release says "majority" of Q2 placements were clinical, with no exact count.

## Gaps / what I could not find

- I could not fetch the PacBio call transcript or the marketbeat summary (the URL returned an unrelated page), so there are no verbatim management quotes on Illumina or on WGS substitution.
- The ONT GenomeWeb page was blocked (403). I found no ONT price per Gb on PromethION and no ONT methylation or MRD clinical detail.
- I found no Genexus placement counts and no named labs moving off Illumina to Ion Torrent.
- I found no US-ex-China placement counts for MGI or Complete Genomics.
- I did not verify PacBio's named clinical customers (GeneDx, Children's Mercy, Mayo) for 2026.
