# Agent 55: 55-web-35B-flow-cell-pricing-ASHG-AMP-posters-and-clinical-lab-migration-evidence

*Model: sonnet. Run 2026-10-11 03:31:23. Cost $0.57 (API-equivalent).*

**Assignment:** Find new public evidence on (1) NovaSeq X 35B, 14B and 5B flow cell pricing and dates. Sources: Illumina's NovaSeq X Series reagent kit product pages and the support site (catalog 20104706), Fisher/VWR/Genohub/Cambridge Genomic Services/core-facility rate cards (check Rush S4 lane Gb, Harvard FY26, UCLA 1 Jul 2026), the GSA 25B-300 price date, Broad Clinical Labs, the H2 2026 'HT mode' terms, and any ASHG 20-24 Oct 2026 announcements. Compute $/Gb for each. (2) Primary clinical-lab evidence of 6000-to-X migration: AMP 2026 and ASHG 2026 abstract listings, conference posters (bioRxiv/medRxiv/ResearchGate) from named labs (e.g. Mayo, ARUP, Labcorp, Quest, Broad, Children's Mercy, Baylor, Invitae/Labcorp, Ambry, Fulgent) giving Gb per sample, cost per sample before and after, parallel-run length or revalidation cost. Also: Illumina TSO 500 HT notes M-GL-02869 and M-GL-03016, FDA PMA/510(k) databases (P230011 TSO Comprehensive instrument), NYS CLEP and CAP notices. Also: the Ultima UG 100 Solaris preprint and the GenomeWeb or 360Dx AXELIOS clinical articles (try web search snippets or archive.org if blocked). Quantify cost-per-genome or per-test deltas and flag any lab that stayed on the 6000 and why. Return a table of named labs, evidence, date and URL.

## Key findings

Most of the assignment came back empty. Three items add something to the ledger.

- **Illumina's roadmap page confirms the dates.** [FACT] The 35B and 14B flow cells and Q70/Q50 quality are all "H1 2027". The 5B flow cell was listed for "H1 2026". The 14B is a 10B with "40 percent increased yield… 14 billion reads", 20–22 hour runs, and "32 WGS samples in about 20 hours". The page gives no 35B output and no price for any flow cell. ([Illumina innovation roadmap](https://www.illumina.com/systems/sequencing-platforms/novaseq-x-plus/applications/innovation-roadmap.html), fetched 2026-10-11.)
  - This updates E057: the 14B is H1 2027 on Illumina's own page. It fits the ~Jan 2027 hearsay in E058 only at the very start of the window. A January list-price change would still need the 35B to ship that early.
  - I found no mention of an ASHG (20–24 Oct) flow-cell announcement.
- **TSO 500 HT now gives a first per-sample cost conversion.** [FACT: spec page; the cost numbers are my calculation] The Illumina product page lists the assay's throughput. ([Illumina TSO 500 HT page](https://www.illumina.com/products/by-type/clinical-research-products/trusight-oncology-500-ht.html), fetched 2026-10-11.)

| Flow cell | Samples per run | Paired-end reads | Reads per sample |
|---|---|---|---|
| NovaSeq 6000 S4 | 192 | ~100M per sample (the page states no run total) | ~100M |
| X 10B | 192 | 20B | ~104M |
| X 25B | 480 | 52B | ~108M |

  - Reads per sample are essentially identical across platforms, at 3,500× coverage. At 2×150, that is roughly 30 Gb per sample (my calculation).
  - The X 10B matches an S4 sample for sample. The 25B holds 2.5 times as many samples.
  - Using the Salk prices already in E052/E053: an S4-300 at $39,701 comes to about $207 per sample, and a 25B-300 at $42,560 comes to about $89 per sample. That is a 57% cut in flow-cell cost per sample for a lab that fully fills the 25B. [OPINION: calc]
  - Fill rate is the key sensitivity. A lab running 192 samples on a 25B pays $222 per sample, which is more than on the S4. This ties to E032 (under-filled flow cells carry a price premium) and shows why a low-volume tail may stay on the 6000 or the 10B.
  - Library prep, hybrid capture and bioinformatics are excluded.
- **Another Roche data point (E124).** [FACT, via search snippet; GenomeWeb returned 403 on fetch] GenomeWeb says Broad Clinical Labs had a prototype AXELIOS "for about a year and a half" and "plans to validate it for clinical use" once it gets the commercial version. Roche is launching it research-use-only, with "a clear strategic intent" to go clinical. So no clinical-lab AXELIOS validation exists yet, and no cost data. ([GenomeWeb](https://www.genomeweb.com/sequencing/roche-sets-sight-clinic-following-commercial-launch-axelios-1-sequencer), snippet only, date not seen.)
- **Illumina vs Ultima comparison (E069).** [MGMT] Illumina published its own comparison on 2025-10-07. It claims NovaSeq X makes "6× fewer SNV errors and 22× fewer indel errors" than UG 100 on the full NIST v4.2.1 benchmark. It says Ultima's "high-confidence region" excludes 4.2% of the genome, including 793 disease genes such as BRCA1 and FMR1. There are no cost figures. This is a vendor-run comparison, not an independent preprint. ([Illumina](https://www.illumina.com/ko-kr/science/genomics-research/articles/ultima-ug-100-vs-illumina-novaseq-x-wgs-data.html))
- **TGen August 2026 list (E054).** [FACT, via search snippet] The 25B-300 flow cell is $25,093 per flow cell. This is a different number from the $3.14/Gb the ledger cites for TGen, so check which unit the earlier figure used. ([TGen price list](https://www.tgen.org/media/x2dmuqf1/tgen_csc_academic_price_list_08-2026.pdf))

## Named labs and evidence

| Lab | Evidence | Date | URL |
|---|---|---|---|
| Broad Clinical Labs | Plans clinical validation of AXELIOS. This is not a 6000-to-X migration. | 2026 (date not seen) | genomeweb.com (above) |
| Illumina (not a lab) | TSO 500 HT throughput by platform | 2026-10-11 fetch | illumina.com (above) |
| UW–Madison core | Replaced a NovaSeq 6000 with an X Plus, citing "expanded capacity and lower consumable costs". No numbers. | 2024-06-27 | research.wisc.edu/?p=57818 |

I found no named clinical lab with Gb per sample, cost before and after, parallel-run length, or revalidation cost. I also found no lab that said it stayed on the 6000 and gave a reason.

## Contradictions and stale data

- No contradiction of known facts found.
- The ledger's "window H1 2027" for the 35B (gap 1) and E058's "~January 2027" hearsay are not the same. Illumina's own page says H1 2027, so a January list-price change is unconfirmed.

## Gaps / what I could not find

- **Blocked or empty sources.**
  - PMC and GenomeWeb returned bot walls or 403.
  - A bioRxiv paper surfaced, "Validation of the NovaSeq6000 platform… CE-IVD equivalence" (2025-08-19; doi 10.1101/2025.08.19.671033). It compares the 6000 RUO with the 6000Dx on 96 exomes, so it is not about migration to the X. I could not open it.
  - No M-GL-02869 or M-GL-03016 notes surfaced.
  - No FDA P230011 instrument confirmation, NYS CLEP or CAP notices, or AMP/ASHG 2026 abstract listings surfaced.
  - No Ultima Solaris preprint with clinical data surfaced.
- **Pricing items still open.**
  - Rush S4 lane Gb, Harvard FY26, UCLA 1 Jul 2026, the GSA 25B-300 price date, Fisher/VWR/Genohub quotes for catalog 20104706, the Broad Clinical Labs rate page, and the H2 2026 "HT mode" terms.
  - The Novogene "443 Gb/lane average, 465 max" figure (NovaSeq X Plus, PhiX validation) is undated and has no flow-cell type. It cannot be used for $/Gb.
- Searches return summaries, not full pages. The next agent should try archive.org copies and direct downloads with a shell.
