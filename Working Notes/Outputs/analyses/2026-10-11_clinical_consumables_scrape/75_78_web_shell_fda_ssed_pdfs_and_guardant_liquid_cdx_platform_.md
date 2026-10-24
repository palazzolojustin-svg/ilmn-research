# Agent 75: 78-web-shell-FDA-SSED-PDFs-and-Guardant-Liquid-CDx-platform-claims

*Model: sonnet. Run 2026-10-11 09:52:44. Cost $0.53 (API-equivalent).*

**Assignment:** Only run if a shell with curl and pdftotext (or python PyPDF) works. Download and read the FDA SSED PDFs from accessdata.fda.gov/cdrh_docs/pdf25/P250027B.pdf (Guardant360 Liquid CDx), P200010B, P190032B and P240010, plus any Natera Signatera, GeneDx, Myriad MyChoice CDx or Pillar SSEDs you can locate through the FDA PMA database. Extract: the sequencer named (NovaSeq 6000 vs NovaSeq X vs NextSeq), reagent kit names, whether a sequencer change needs a PMA supplement (a switching-friction point), the validated input and read depth per sample (Gb or reads per sample), and the analytical-validation platform comparison. Also try: the openFDA device 510(k) and De Novo API for the TruSight Oncology Comprehensive, TruSight Whole Genome IVDR page claims, the Illumina Dx NovaSeq X Dx status, and the Höjer et al. AVITI-vs-NovaSeq X comparison (bioRxiv, retry or use the shell) for $/Gb and quality results. Quantify the regulatory lock-in: which marketed clinical IVD or LDT-adjacent assays are tied to NovaSeq 6000 and how long a re-validation takes. Return a table of assay, sequencer, kit, Gb per sample and source URL, with exact quotes. Hard stop at 20 minutes.

## Key findings

I did not run the full assignment. It was conditional on a shell with curl and pdftotext, and this session has no shell. I could only use WebFetch, WebSearch, Read and Grep.

- **The main check failed.** The Guardant360 Liquid CDx SSED (P250027B) is still unread, so E250/E288 stay unresolved. WebFetch returned only an "encoded stream data" refusal for these PDFs:
  - P250027B and P250027A
  - P240010B
  - Guardant's Technical Information Document
  - Read's `pages` option needs pdftoppm, which isn't installed here. Grep on the saved PDFs found no matches, because the text is compressed.
- **FACT (small update to E250/E288):** the FDA PMA database page for P250027 lists the device as "Next generation sequencing oncology panel, somatic or germline variant detection system", approved 19 May 2026. It shows one supplement, S001, and names no sequencer. [FDA PMA database, https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpma/pma.cfm?id=P250027, fetched 2026-10-11]
  - The page text was summarized by the fetch tool, so this is not a verbatim quote.
  - S001 matters. If it is an X-related change, it would contradict the "no X pathway" inference. I did not open it.
- **FACT (supports E043):** a search result for Guardant's Q2 2026 call says the liquid biopsy portfolio completed its NovaSeq X transition. This only repeats the E043 correction and does not settle which instrument P250027 names. [Motley Fool transcript, 2026-08-07, https://www.fool.com/earnings/call-transcripts/2026/08/07/guardant-health-gh-q2-2026-earnings-call-transcript/]
- **FACT (Höjer, helps gap 6):** bioRxiv 2025.10.10.681584 is titled "Whole genome sequencing with AVITI and NovaSeq X Plus reveals comparable performance with contextual biases". It sequenced four human cell lines on PCR-free libraries. [https://www.biorxiv.org/content/10.1101/2025.10.10.681584.full.pdf] Search summaries of the paper report:
  - AVITI had lower duplication rates and higher reported base qualities, which gave better mapping confidence and fewer spurious variant candidates.
  - AVITI was affected by G-quadruplex motifs.
  - The summaries say the paper does not centre on $/Gb. I did not fetch the full text, so there are no exact quotes or numbers.
  - The summary calls it a peer-reviewed NAR Genomics and Bioinformatics paper. That is unverified.
- **OPINION:** the Höjer result suggests that, on WGS quality, switching to Element is not blocked by data quality. That strengthens the threat in E116, where the barrier is re-validation cost, not data quality.

## Not completed

The table of assay, sequencer, kit and Gb per sample could not be built. That covers P200010B, P190032B and P240010. It also covers the openFDA 510(k) and De Novo checks, the TruSight Whole Genome IVDR page, and the Natera, GeneDx, Myriad and Pillar SSEDs. The regulatory lock-in could not be quantified, and I found no source for how long a PMA re-validation takes beyond E116.

## Contradictions and stale data

None new. GenomeWeb returned 403, so I could not read the article on the upgraded Guardant CDx.

## Gaps / what I could not find

Re-dispatch the following to an agent that has a shell:
- Run `curl -A "<UA>" -O https://www.accessdata.fda.gov/cdrh_docs/pdf25/P250027B.pdf`, then `pdftotext -layout`.
- Grep for `NovaSeq|NextSeq|S4|reagent|reads|Gb`.
- Apply the same steps to P200010B, P190032B, P240010B and the S001 summary.
