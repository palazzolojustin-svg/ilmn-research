# Agent 64: 64-web-clinical-migration-and-challenger-evidence-FDA-CAP-NYS-AMP-ASHG-Roche-Element-Ultim

*Model: sonnet. Run 2026-10-11 03:41:18. Cost $0.68 (API-equivalent).*

**Assignment:** Find primary evidence of what clinical labs are doing with sequencers, which earlier agents (40, 44, 48, 51, 55, 56) did not find. Pursue: (1) Regulators and accreditors: FDA 510(k)/PMA/De Novo databases for NovaSeq X Dx (or 'NovaSeq X Plus Dx') and any P230011-related supplement; FDA approval summaries of NGS companion diagnostics listing the sequencer (FoundationOne CDx, Guardant360 CDx, Tempus xT CDx, Caris, MI Cancer Seek) and whether they name the NovaSeq X, 6000, or a challenger; CMS/CLIA and CAP checklists; NYS CLEP approvals and public test listings that cite 'NovaSeq X'; MolDX technical assessments and Palmetto/MolDX LCD documents that name platform changes. (2) Conference abstracts and posters: AMP 2026 (Nov) and ASHG 2026 (Oct) abstract listings, ESHG 2026, AACR 2026, ASCO 2026, ACMG 2026, ISPD 2026, and bioRxiv or medRxiv preprints that report clinical-lab validation on NovaSeq X, Roche AXELIOS (SBX), Element AVITI/AVITI24, Ultima UG100/UG 100 Solaris, MGI T20 or Singular, including concordance, cost per sample and sequencing cost per Gb. Include MRD, NIPT, newborn and rare-disease WGS labs (Rady, GeneDx, Broad Clinical Labs, Genomics England, Our Future Health, NHS GMS, Singapore, Saudi, Emirati programs). (3) Trade press and company releases Aug-Oct 2026 (GenomeWeb, 360Dx, Fierce, STAT, Endpoints, company IR sites) on: Roche AXELIOS placements and named clinical customers; Element or Ultima clinical-lab wins (named labs, volumes, Gb); Natera, Guardant, Tempus, BillionToOne, GeneDx or Caris statements on platform mix or sequencing cost per test; Q3'26 pre-announcements and the Roche nine-month sales release if published. Quantify: named labs, run counts, Gb, cost per genome or sample, and the percent of volume moved off Illumina. Cite publisher, date and URL, and say plainly where nothing was found.

NO NEW EVIDENCE

I searched for this and found nothing that is not already in the ledger. Several targets could not be checked at source, so the gaps below are open, not closed.

**What I checked**
- **FDA, NovaSeq X Dx:** I found no NovaSeq X Dx, NovaSeq X Plus Dx or P230011-related filing. The only hits were old MiSeqDx clearances (2013). This matches E250, but I did not query the FDA 510(k), De Novo or PMA databases directly, so it is still an absence in web search and not a database check.
- **Companion diagnostics:** I searched FoundationOne CDx, Guardant360 CDx and Tempus xT CDx for the sequencer named in the approval summaries. The results covered only the approvals themselves (Tempus xT CDx, May 2023) and did not name a sequencer. I did not open the FDA summary documents, so this is unresolved.
- **Regulators and accreditors:** I did not reach any NYS CLEP, CAP, MolDX or CLIA documents that cite "NovaSeq X". Search returned nothing relevant.
- **ASHG, AMP, AACR, ASCO and other abstracts:** I found no abstract listings for ASHG 2026, which runs 20–24 Oct and has not happened yet. The only comparison results were already known:
  - Illumina's NovaSeq X vs Ultima UG 100 benchmarking page (E273).
  - The Ultima UG 100 bioRxiv preprint (E252).
  - Siena (E251).
- **Trade press on AXELIOS:** The GenomeWeb and 360Dx snippets only re-state what is already in E123, E124, E126 and E253. That covers the CNAG purchase, Broad Clinical Labs, Centogene, Hartwig and Foundation Medicine, the 100-unit year-one goal, and the RUO label. I found no new named clinical customer, run count, Gb figure or percent of volume moved off Illumina. GenomeWeb returned HTTP 403, so full articles were unreadable.
- **Element and Ultima clinical wins:** I found only the Precure/UG200 selection (22 Sep 2026), Hartwig, NeoGenomics, Quest and Labcorp. All are in E114, E128, E272 or E291-type items. No volumes, Gb or lab names are new.
- **Natera, Guardant, Tempus, GeneDx or Caris platform statements:** I found no statements about moving to Ultima, Element or Roche, and no sequencing cost per test beyond E043, E090, E091 and E092.
- **Roche nine-month sales:** I found no nine-month release. Search returned only the H1 release (sales +6% CER, CHF 30.4B, Axelios launched), which is already covered. It is probably not out yet, so re-check in late October.
- **NovaSeq X preprints:**
  - The Providence/ISB clinical-WGS paper (Wagner et al., Frontiers in Molecular Biosciences, 13 Oct 2025, PMC12554564, medRxiv 10.1101/2025.07.16.25331598) could be relevant. It validates a 78-gene heritable-disease and PGx screening WGS test.
  - I could not tell which sequencer it used, because medRxiv and Frontiers returned 403. Check it if a shell or PMC fetch works.

**Recommended follow-up (not done)**
- Re-run after ASHG (20–24 Oct), the Illumina Q3 results (29 Oct) and the Roche nine-month release.
- Read the Wagner paper in PMC to get the sequencer and cost per genome.
- Use a real shell to query openFDA and the 510(k) and PMA databases for "NovaSeq", and to open the CDx summary PDFs.
