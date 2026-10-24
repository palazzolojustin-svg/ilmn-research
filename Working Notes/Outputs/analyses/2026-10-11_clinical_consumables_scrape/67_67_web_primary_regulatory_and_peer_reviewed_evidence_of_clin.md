# Agent 67: 67-web-primary-regulatory-and-peer-reviewed-evidence-of-clinical-6000-to-X-migration-and-c

*Model: sonnet. Run 2026-10-11 03:50:43. Cost $0.88 (API-equivalent).*

**Assignment:** Close open gap 6 with primary-database checks, not web-search absence. Pursue: (1) openFDA device 510(k)/PMA/De Novo records and FDA Summary of Safety and Effectiveness PDFs for FoundationOne CDx, FoundationOne Liquid CDx, Guardant360 CDx, Guardant Shield, Tempus xT CDx, Natera Signatera (breakthrough designation), GeneDx, Caris MI Cancer Seek, and Illumina TSO Comprehensive. Record which sequencer is named (NovaSeq 6000 versus X) and any supplemental or PMA-supplement filings for a sequencer change, which indicate a 6000-to-X migration. (2) The Wagner et al. Providence/ISB 78-gene clinical WGS paper (PMC12554564, Frontiers in Molecular Biosciences, Oct 2025): sequencer, cost per genome, Gb per sample. (3) PubMed, medRxiv and bioRxiv from 2025-2026 for clinical-lab NovaSeq X validation papers (NIPT, MRD, WGS, rare disease, newborn screening) and for Roche AXELIOS, Element AVITI24 and Ultima UG100/UG200 clinical validations. Capture the cost per sample, the reagent cost per Gb they quote and the concordance with Illumina. (4) ASHG 2026 (20-24 Oct) and AMP 2026 abstract and poster listings, and any pre-announced vendor talks. (5) CAP and NYS CLEP notices and Illumina or Roche or Element press releases dated after 1 Oct 2026. Quantify: sequencer-change evidence count by lab, per-genome costs, Gb per sample and any 'runs in parallel on 6000 and X' statements, which bear directly on the Jefferies parallel-running question. Cite PMIDs, URLs and dates.

## Key findings

1. **FoundationOne CDx has never moved to the NovaSeq X, and the one sequencer change on record took 11 months to approve. [FACT]** openFDA PMA record P170019/S045 was received 2023-05-19 and approved 2024-04-25 as a "Normal 180 Day Track" supplement. Its approval statement reads "approval for the migration of the F1CDx from the HiSeq 4000 to NovaSeq 6000 configuration" (api.fda.gov/device/pma.json, pulled 2026-10-11).
   - I found no later F1CDx supplement for a sequencer change. The 2024-2026 supplements I could see are S046 (2023-08), S052 (2024-08), S054 (2025-01) and S060 (2026-05), and all are labeling changes.
   - Foundation Medicine, a high-volume FDA-approved lab, therefore moved to the 6000 as recently as April 2024 and shows no X filing through 2026-10-11.
   - This directly supports the E016, E027 and E250 logic that regulated assays anchor part of the 6000 tail.
   - It does not prove F1CDx never moves. A change-control plan, a lab-site notification or a pending PMA supplement would not show up in these records.

2. **No FDA-approved CDx PMA supplement I could find names a NovaSeq X. [FACT, absence in a primary database, not web search.]** This is a database check, which E250 lacked.
   - I looked at Guardant360 CDx (P200010), FoundationOne Liquid CDx (P190032), Tempus xT CDx (P210011) and Guardant Shield (P230009).
   - For Guardant360 CDx, supplements S016 (2024-03), S025 (2026-05), S028 (2025-12) and S029 (2026-09) are bioinformatics, labeling and manufacturing-room changes. One more (S0xx) was not shown.
   - Foundation's Liquid CDx supplements S018, S026, S028 and S032 are labeling or manufacturing changes.
   - Tempus xT CDx supplements S001-S004 are supplier, stability, algorithm and site changes.
   - Shield's S001-S020 are supplier, QC and classifier changes.
   - Caveat: openFDA gives short approval statements, not the full summary PDFs. I did not open the original SSED PDFs, so the sequencer named in each original approval is not confirmed here.

3. **Guardant moved the LDT (lab-developed test) Guardant360 Liquid to the X in May 2026 (E043), but the FDA-approved Guardant360 CDx shows no matching supplement.** [FACT absence + OPINION]
   - The PMA supplement trail through 2026-09-18 (S029) has no sequencer or instrument change.
   - Either the CDx still runs on the 6000, or the change was handled outside these records.
   - This sharpens Q1: the LDT version captured the X saving (~$200 per test), but the regulated version has not visibly done so.
   - Check this at the next Guardant call.

4. **Tempus xT CDx got an FDA-approved change-control plan on 2026-09-02 (S002).** [FACT]
   - The approval is "to modify the use of the device at a single laboratory to multiple laboratories."
   - This is a Tempus capacity and site expansion, not a sequencer change. The record does not mention a sequencer.
   - It is mildly relevant to E022, where Tempus lists both the 6000 and the X in a job posting.

5. **The Wagner et al. Providence/ISB paper (PMC12554564) is a 6000 study, not an X study. [FACT]**
   - It is titled "Design and validation of a clinical whole genome sequencing-based assay for patient screening in a large healthcare system" and was received 2025-07-18 and accepted 2025-09-16.
   - It uses the Illumina NovaSeq 6000 with "24 libraries loaded per S4 flow cell."
   - Target depth was 30X, and median coverage was 35.2-41.9X across validation groups.
   - It reports 100% sensitivity and specificity against orthogonal methods, 98.7% sensitivity versus whole exome sequencing, and 100% pharmacogenomics concordance.
   - More than 2,000 patients have been sequenced in the Geno4ME implementation study.
   - The paper gives no cost per genome and no parallel-instrument statement.
   - Implication: a large-system clinical WGS program validated as late as mid-2025 on S4 flow cells, not the X. (Calc: an S4 gives roughly 3,000 Gb, so about 125 Gb per sample at 24 per flow cell, in line with ~35-42X coverage.)
   - This is evidence that new clinical WGS was still being validated on the 6000 in 2025, which supports the sticky-tail view. It is one lab and one design.

6. **PathoNext (Leipzig molecular pathology lab) runs a NovaSeq 6000 and an Element AVITI24 side by side. [FACT]**
   - It has run the AVITI24 since October 2025 and validated its OncoDEEP panel on it (OncoDNA user-meeting deck, Dec 2025, ugm.oncodna.com).
   - Its published observations: AVITI24 Q30 92.7-94.95 versus 90.6 on the NovaSeq, mapping above 99% versus 96-98%, duplicates 28-35% versus ~50%, and ~1.5x coverage at comparable reads.
   - I could not extract the PDF text directly. These numbers come from a search summary, so treat them as unverified until the slide is read.
   - It is a clinical-lab case of adding a cheaper competitor next to a 6000. It is not a 6000-to-X move. It bears on the parallel-running question but not the X conversion path.

7. **A June 2026 peer-reviewed comparison finds Element AVITI and NovaSeq X Plus "highly comparable" for WGS. [FACT]**
   - It is in NAR Genomics and Bioinformatics, June 2026, by Höjer, Alneberg et al. from Swedish institutions (bioRxiv 10.1101/2025.10.10.681584; SciLifeLab publications entry).
   - It ran PCR-free WGS on four tumor cell lines.
   - AVITI showed low duplication rates and higher base quality, with a "minor improvement" on indels at low coverage. It was superior in high-GC regions and inferior in GC homopolymers.
   - Its read 2 error rate was higher on short fragments.
   - It is research-grade, not clinical, and quotes no cost. It gives independent, non-Illumina evidence that Element is analytically adequate for short-read WGS, which weakens the quality moat.
   - I could not open the full text because of a 429 error.

8. **An independent 96-exome study validated the NovaSeq 6000 RUO with automated library prep against the NovaSeq 6000Dx. [FACT]**
   - It is Pasquinelli et al., Computational and Structural Biotechnology Journal, 2025-11-01 (PMC12639258).
   - SNV agreement was 100%. CNV positive percent agreement was 79% for events above 150 kb and 91.7% above 900 kb.
   - The relevance is that a lab was still doing CE-IVD-equivalence work on 6000-generation hardware in late 2025, which suggests regulated labs are extending the 6000 rather than migrating. It does not mention the X.

9. **The only IVD whole-genome kit I could surface is EU-only.** TruSight Whole Genome (IVDR) appeared in a search summary as validated on more than 450 clinical samples across more than 150 runs, and its page title references the NovaSeq X Series. [FACT, unverified]
   - The Illumina EMEA page I fetched did not mention it, so the platform, status and date are unconfirmed. It is not in the ledger.
   - If it is X-labelled and IVDR-compliant, it would contradict the E250 inference that no regulated pathway exists on the X. Verify before using.

10. **I found no Illumina or Roche press releases dated after 1 Oct 2026, and no ASHG 2026 abstracts. [FACT, absence]**
    - The latest Illumina release surfaced is the Feb 23, 2026 roadmap (illumina.com press release 7b4175f1-a13f-401e-9335-3e5eadbb1fe0).
    - ASHG 2026 begins 20 Oct. The only listings indexed are ASHG 2025 recaps.

## Sequencer-change evidence count by lab (primary sources only)

| Lab | Change documented | Source and date | Direction |
|---|---|---|---|
| Foundation Medicine (F1CDx) | HiSeq 4000 → NovaSeq 6000, FDA-approved | openFDA P170019/S045, 2024-04-25 | Not to X |
| Guardant (360 CDx) | No sequencer supplement | openFDA P200010 through S029, 2026-09-18 | None visible |
| Guardant (360 Liquid LDT) | → X, May 2026 | E043 (already in ledger) | To X, LDT only |
| Foundation Liquid CDx, Tempus xT CDx, Shield | No sequencer supplement | openFDA | None visible |
| Providence/ISB (Geno4ME) | Validated on 6000 S4 | PMC12554564, accepted 2025-09-16 | 6000 |
| PathoNext | 6000 + AVITI24 in parallel | OncoDNA deck, Dec 2025 | Competitor added |

Net: the count of labs with FDA-documented 6000-to-X migration is **zero**. The count with FDA-documented moves to the 6000 is **one** (Foundation, April 2024).

## Contradictions and stale data

- **E250:** the absence is now confirmed in the FDA PMA database for the CDx products checked. It is still unchecked for 510(k) and De Novo records, and a possible EU IVDR TruSight WGS listing needs verification (finding 9).
- **E043 versus the FDA record:** Guardant's X move applies to the LDT. The approved CDx shows no supplement, so a "Guardant moved to X" read-through should not extend to its regulated tests.
- **E022 (Tempus lists both the 6000 and X):** the only regulatory change on xT CDx in 2026 is site expansion, so the dual-running posting is not matched by any FDA sequencer filing.

## Gaps / what I could not find

- **Not run or not opened:** the SSED PDFs themselves, the 510(k) and De Novo searches (openFDA full-text search for "NovaSeq X" is not available), Natera Signatera, GeneDx, Caris MI Cancer Seek, and Illumina TSO Comprehensive. TSO Comprehensive was probably approved as a kit on the NextSeq 550Dx, which E250 already notes from the EU page.
- **Missing papers:** PubMed, medRxiv and bioRxiv 2025-26 clinical-lab X validations for NIPT, MRD, rare disease and newborn screening, and for Roche AXELIOS or Ultima UG200 clinical validations. Searches returned no such paper. This is a search-tool limit, not proof of absence.
- **No cost per genome** came from any item above. Wagner reports none, and Pasquinelli and Höjer report none.
- **Not covered:** CAP and NYS CLEP notices, AMP 2026 listings (AMP is in November), and ASHG 2026 listings. Re-run after 20 Oct.
