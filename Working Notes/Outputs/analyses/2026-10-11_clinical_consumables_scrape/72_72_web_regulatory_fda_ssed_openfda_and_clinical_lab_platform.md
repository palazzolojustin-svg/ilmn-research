# Agent 72: 72-web-regulatory-FDA-SSED-openFDA-and-clinical-lab-platform-migration-primary-evidence

*Model: sonnet. Run 2026-10-11 08:14:54. Cost $1.77 (API-equivalent).*

**Assignment:** Closes open gap 6 and the read-through on clinical lock-in versus switching. Use openFDA (api.fda.gov/device/510k.json, /pmn, De Novo and PMA endpoints), accessdata.fda.gov SSED PDFs, FDA CDRH databases and lab web pages. Not repeated in earlier waves: the SSED PDFs and PMA supplements for the original sequencer-based companion diagnostics and IVDs. Check which sequencer is named (NovaSeq 6000, NovaSeq X, NextSeq 550Dx, MiSeqDx or non-Illumina) and whether any supplement adds NovaSeq X or a non-Illumina platform. Cover: Foundation Medicine FoundationOne CDx and Liquid CDx, Guardant360 CDx, Natera Signatera, Tempus xT CDx, Caris MI Cancer Seek, Illumina TSO Comprehensive, Pillar, Myriad MyChoice CDx and the Illumina TruSight Oncology Comprehensive. Check the 510(k) and PMA records for platform changes (a PMA supplement for a sequencer change takes months and gives a measure of switching cost). Also check: the EU IVDR page for 'TruSight Whole Genome' and its NovaSeq X link, CAP or CLIA proficiency or validation notes, and NY State approvals that name a platform. Read in full the OncoDNA/PathoNext poster/deck (NovaSeq 6000 and AVITI24 run in parallel, Dec 2025) and the NAR Genomics & Bioinformatics paper by Höjer et al. (AVITI vs NovaSeq X). Quantify the time and cost of revalidation where documented (months, number of samples, $), the platform named for each test, and any lab explicitly running the 6000 and the X in parallel. Also search for published clinical-lab validation of Ultima UG100 or Roche AXELIOS (for example the Broad, Natera or BillionToOne claims, medRxiv or bioRxiv preprints, 2026). Return a table: test or lab, platform, document, date, URL, and what it implies for how fast the 6000 base converts or churns.

## Key findings

**Net result: little that is new, but four items matter.** Most of gap 6 is still open. The FDA SSED PDFs are FlateDecode binaries, and WebFetch can't read them. There is also no shell, so I couldn't extract the text. The items below are either new to the ledger or sharpen E250 and E043. File 67 already covers the F1CDx and Pasquinelli (the 96-exome NovaSeq 6000 RUO vs 6000Dx study, PMC12639258) items, so I don't repeat them.

1. **Caris MI Cancer Seek (PMA P240010) is on the NovaSeq 6000. [FACT]**
   - The record shows initial approval on 2024-11-05, after a 2024-04-01 filing (about 7 months). There have been 10 supplements through S010 (2026-07-02), and none names a sequencer. The openFDA statements are short, so a sequencer change could still hide in an unlisted supplement.
   - The sequencer is named in the SSED as the "Illumina NovaSeq 6000".
   - Run validity needs ">16 billion reads passing filters" and Q30. Key genes need ">100x" depth.
   - It is a "sole-location FDA PMA test". It covers 228 genes plus MSI, TMB and one copy-number gene.
   - Sources: openFDA api.fda.gov/device/pma.json (pulled 2026-10-11); Discoveries in Health Policy, 2024-12-30 (discoveriesinhealthpolicy.com/2024/12/caris-pma-test-fda-documents-now-online.html); CLP Magazine, which says "Sequencing is performed on qualified Illumina NovaSeq 6000 instruments".
   - **Implication:** The largest-volume WES/WTS clinical customer (E092: 114K+ WES/WTS per quarter) has an FDA-approved flagship locked to the 6000. A switch to the X would need a PMA supplement. Caris also has the Open Offer price clause (E255), so its price per Gb falls without any sequencer change.
   - **Caveat:** The LDT volume at Caris may run elsewhere. I couldn't check this.

2. **Guardant360 Liquid CDx (PMA P250027) is a new PMA, not a supplement, and earlier agents missed it. [FACT]**
   - It was received 2025-07-31, amended 2026-02-17, and approved 2026-05-19. That is about 9.7 months from filing.
   - It has 741 genes (SNV/indel) plus 2 copy-number genes. The 7 CDx indications of the legacy Guardant360 CDx (P200010) transfer to it. It is a "100X wider footprint".
   - Management says the Liquid CDx adds genomic and epigenomic content, and it expects ADLT designation in 1H27 (Q2'26 call, 2026-08-07, fool.com transcript).
   - File 67 said the Guardant CDx trail through S029 shows no sequencer change. That is true, but it misses that regulated content moved to a new PMA filed in July 2025.
   - Guardant's May 2026 NovaSeq X completion (E043) and this approval fall in the same month.
   - **I could not read the SSED (P250027B) to see which sequencer it names.** This is the single most valuable open check. If it names the X, the regulatory pathway to the X exists for large panels and E250 is wrong. If it names the 6000, E043 applies only to the LDT.
   - **Do not conclude either way from the timing alone.** A PMA filed in July 2025 would normally have validated the sequencer in use then.
   - Sources: openFDA P250027; 360Dx/GenomeWeb (the page returned 403; I got only the search summary); fool.com Guardant Q2'26 transcript, 2026-08-07. The transcript quotes "completed the Guardant360 Liquid transition to NovaSeq X in May" and "reducing cost per test by approximately $200".

3. **TruSight Oncology Comprehensive (P230011) is NextSeq 550Dx only, and its PMA trail shows no sequencer expansion. [FACT]**
   - Original approval was 2024-08-21, after a 2023-03-20 filing (about 17 months).
   - Supplements S001–S008 run through 2026-09-04. They cover raw-material and supplier changes, MSI reporting (S002, filed 2025-01-30, approved 2026-06-26, about 17 months) and thyroid RET (S006, filed 2025-11-18, approved 2026-08-14, about 9 months).
   - **Implication:** Illumina's own FDA-approved CGP kit has not been extended to a high-throughput instrument in over 2 years. That is consistent with E077, where the ex-manager said TSO Comprehensive is the only FDA-approved CGP kit.
   - Cross-check: the same TSO 500 family page lists the NovaSeq 6000Dx.
   - Sources: openFDA P230011 (pulled 2026-10-11); FDA recently-approved-devices page.

4. **Switching cost in PMA time, from openFDA. [FACT]**
   - FoundationOne CDx S045, HiSeq 4000 to NovaSeq 6000 (the file 67 item): received 2023-05-19, approved 2024-04-25, about 11 months, on the "Normal 180 Day Track".
   - A like-for-like comparison is Ventana ALK (P140025/S024), an instrument migration from BenchMark ULTRA to ULTRA PLUS. It took 15 months (2023-12-08 to 2025-03-12).
   - Other PMA timings: Caris initial about 7 months; Guardant Liquid CDx about 9.7 months; TSO new-indication supplements 9–17 months.
   - **Inference [OPINION]:** For an FDA-approved sequencer-based test, a platform move takes about 11–15 months and a supplement fee, and must be filed in advance. This supports the 12–18 month validation framing in E031. It also means a lab filing for the X would show in these records before the revenue shift.
   - The F1CDx record also shows a lag. HiSeq 4000 to NovaSeq 6000 was approved in April 2024, about 5.5 years after the NovaSeq 6000 launched in January 2018.

## Competitor clinical-validation read-through

5. **AXELIOS, Hartwig/Cuppen data (ESP Congress, article dated 2026-09-24): ~99% concordance across 1,229 reported cancer events vs Illumina. [FACT per Cuppen's presentation; sample count not disclosed.]**
   - Modelled cost per tumor/normal WGS at 90×/30× is about 29% lower on AXELIOS than on NovaSeq X 25B. [FACT, as presented; this is a model, not invoice data.]
   - The events span SNV, indel, CNA, fusion, TMB, MSI, HRD/HRP and HLA typing.
   - Source: Oncodaily, "Highlights From the European Society of Pathology Annual Congress", 2026-09-24 (oncodaily.com/science/svetlana-nikic-593041). GenomeWeb 645931 was blocked (403).
   - **Implication:** This is the first quantified cost gap on a comparable-depth oncology WGS workload. It is 29%, far smaller than the headline $150 vs $200 per genome (about 25%, E059) would suggest once you add duplex and deep tumor-normal coverage. It is also not the 11x of the $0.06/M-read comparison (E060).
   - It is a research partner (Hartwig), not a CLIA/IVD lab. A 99% concordance claim alone is not a CLIA validation.
   - Sample counts, runtime and the matching Illumina mode are all undisclosed.

6. **Illumina NovaSeq X vs NovaSeq 6000 concordance, from Illumina's own app note (M-US-00201). [FACT, vendor source]**
   - Whole genome: 10B X vs S4 v1.5, same libraries, 2×151.
   - Exome: 753 samples on the X, Twist Comprehensive Exome Panel, 2×101.
   - SNP/indel precision and recall deviation is under 0.2% between platforms, and SNP similarity is above 95%.
   - **Implication:** Illumina supplies the sample-level comparison that lowers a lab's X verification burden. This supports the idea that laboratory-developed-test (LDT) conversion is a business decision (E031: "validation cost outweighs the savings"), not a data-quality problem.
   - Source: Illumina app note via search summary; I did not open the PDF.

7. **Ultima UG 100 clinical-services preprint (Health 2030 Genome Center): the E252 finding stands.** I could not retrieve the full text (429 errors). No new numbers.

8. **Höjer et al. (AVITI vs NovaSeq X Plus), NAR G&B 2026: no new numbers.** The bioRxiv full text returned 429 twice. Nothing beyond file 67 finding 7.

## Lab / test table

| Test or lab | Platform | Document and date | Implication for 6000 conversion or churn |
|---|---|---|---|
| Caris MI Cancer Seek (P240010) | NovaSeq 6000 | SSED via Discoveries in Health Policy, 2024-12-30; CLP Magazine; openFDA | Flagship exome/transcriptome CDx is locked to the 6000, with 10 supplements and none for a sequencer. Conversion needs a supplement of about 11–15 months. |
| FoundationOne CDx (P170019) | HiSeq 4000 → NovaSeq 6000 (S045) | openFDA, approved 2024-04-25 | One FDA-documented sequencer migration; 11 months. No X filing. |
| Guardant360 Liquid CDx (P250027) | Not confirmed (SSED unreadable) | openFDA; Q2'26 call 2026-08-07 | New PMA approved 2026-05-19; the platform it names decides whether E250 holds. |
| Guardant360 CDx (P200010) | Not confirmed | openFDA through S029 | The legacy version's indications transfer to the new Liquid CDx. |
| TSO Comprehensive (P230011) | NextSeq 550Dx | openFDA; FDA page | Illumina's own CGP kit is not on a high-throughput instrument. |
| Tempus xT CDx (P210011) | Not confirmed | openFDA S002, 2026-09-02 | Multi-site change-control plan; nothing on the sequencer. |
| TruSight Whole Genome (IVDR) | Unconfirmed: search results point to the NovaSeq 6000Dx; the page title reads "NovaSeq X Series ordering" | emea.illumina.com URL title only | Unresolved; the page fetch returned no usable text. |
| Hartwig (AXELIOS) | AXELIOS 1 | Oncodaily, 2026-09-24 | 99% concordance, 29% lower modelled cost; a research partner, not CLIA. |

I didn't read the OncoDNA/PathoNext deck text directly; it is a PDF of images. Agent 67's numbers (E-summary: Q30, mapping, duplicates) remain search-summary only. The same applies to the NovaSeq 6000-plus-AVITI24 parallel running claim.

## Contradictions and stale data

- **E250:** The absence of an X pathway for regulated assays is still unproven. The Guardant Liquid CDx SSED is the live test, and the TruSight Whole Genome page title mentions the X but search results point to the 6000Dx.
- **File 67 finding 3:** The Guardant CDx supplement trail alone misses P250027 (new PMA, 2026-05-19), so "no matching supplement" is incomplete.
- **E059 vs the AXELIOS 29% figure:** The first is list-vs-list per genome and the second is a modelled WGS tumor/normal workflow. They are not like-for-like, and the second is likely closer to the real clinical picture.

## Gaps / what I could not find

- **SSED text:** None of the SSED PDFs (P200010B, P250027B, P170019 etc.) can be read with WebFetch (FlateDecode, no PDF tool, no shell). Someone with a shell needs to run pdftotext on P250027B, P200010B and P190032B.
- **openFDA 510(k)/De Novo:** The 510(k) search URL returned 404. No De Novo search done. Natera Signatera has no PMA and no 510(k) record found. GeneDx and Myriad MyChoice CDx PMA records were not checked beyond the Myriad BRACAnalysis site-change list (P140020).
- **Pillar:** not searched.
- **Cost, months and sample counts for lab revalidation:** nothing documented beyond E116 and the PMA clocks above.
- **Labs explicitly running 6000 and X in parallel:** none new. Tempus and Natera job-posting evidence (E022) stands.
- **Höjer and Ultima preprint full texts:** blocked (429).

Sources: openFDA PMA database (api.fda.gov/device/pma.json), pulled 2026-10-11; [Oncodaily, 2026-09-24](https://oncodaily.com/science/svetlana-nikic-593041); [Discoveries in Health Policy, 2024-12-30](https://www.discoveriesinhealthpolicy.com/2024/12/caris-pma-test-fda-documents-now-online.html); [CLP Magazine MI Cancer Seek](https://clpmag.com/diagnostic-technologies/molecular-diagnostics/sequencing-systems/fda-approved-mi-cancer-seek-test-enhances-tumor-profiling-precision-oncology/); [Guardant Q2'26 call, fool.com, 2026-08-07](https://www.fool.com/earnings/call-transcripts/2026/08/07/guardant-health-gh-q2-2026-earnings-call-transcript/); [FDA TSO Comprehensive P230011](https://www.fda.gov/medical-devices/recently-approved-devices/trusight-oncology-comprehensive-p230011).
