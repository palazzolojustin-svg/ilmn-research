# Agent 51: 51-web-clinical-lab-6000-to-X-migration-evidence-35B-pricing-and-challenger-validation

*Model: sonnet. Run 2026-10-11 03:20:36. Cost $1.78 (API-equivalent).*

**Assignment:** Close gaps 1 and 7 with sources not yet tried. Prior agents hit core price lists, GSA and USAspending. New angles: (1) NIH RePORTER and grants.gov project abstracts and budget narratives, 2025-2026, that cite NovaSeq X cost per Gb, 25B or 35B, or per-genome cost, to get dated prices. Core-facility and sequencing-center announcements (Broad, Baylor, HudsonAlpha, Stanford, Genohub, Psomagen, Novogene, Macrogen, Azenta, GENEWIZ, CD Genomics, Admera, Medgenome) that mention 35B, 14B, 'NovaSeq X Plus' price reductions or 2027 price lists. Outsourced per-genome quotes and press releases. (2) Peer-reviewed or preprint papers 2025-2026 (PubMed, medRxiv, bioRxiv, JMD, Clinical Chemistry, Genetics in Medicine, JAMA Netw Open, Cancer Discovery) on clinical-lab validation of NovaSeq X Plus vs NovaSeq 6000 with Gb per sample, cost before and after, parallel-run duration or revalidation burden. Also validation of Roche AXELIOS (SBX), Ultima UG100/UG200 or Element AVITI/AVITI24 in clinical settings, for example at Mayo, ARUP, Baylor, Broad Clinical Labs, Children's Mercy, Rady, Labcorp, Quest and Natera. (3) Regulatory documents: FDA 510(k)/PMA/De Novo databases and recent clearances (Illumina TSO Comprehensive, TSO 500 HT, any NovaSeq X Dx claim); the Illumina TSO 500 HT tech note M-GL-02869 for Gb per sample and instrument claims; NYS CLEP and CAP notices on sequencer changes. (4) Conference programs: ASHG 2026 (20-24 Oct), AMP 2026 and ESHG 2026 abstract titles naming NovaSeq X migration, Ultima, Element or AXELIOS clinical use. (5) Illumina's own pages and press releases (illumina.com/company/news-center, product pages for NovaSeq X 35B/14B, 'Constellation', 'Q70', 'Illumina Connected Analytics') for dated claims about price per Gb or output. (6) Trade press (GenomeWeb, 360Dx, Fierce, STAT, Endpoints, Business Insider) for Aug-Oct 2026 on AXELIOS orders, Illumina discounting, or lab switching; retry the Ultima preprint (bioRxiv 10.64898/2025.12.11.693628) via the europepmc.org full-text API or a PMC mirror. Report every dated $/Gb, $/genome or Gb-per-sample figure with its source, and any named lab running 6000 and X in parallel. Quote exact words. Say 'not found' rather than guessing. Do not repeat the Salk, UConn, Calgary, CWRU or Dana-Farber price lists in the ledger.

## Key findings

Most of what I checked was already in the ledger or came back empty. These items are new:

1. **Rush University price list gives lane Gb, which closes the per-lane gap in open gap 1. FACT.** The June 2026 Rush fee schedule is the first I found that states Gb per lane. It lists these Illumina prices:
   - 10B lane, 100 cycle (125 Gb): $1,900 internal / $2,090 external, about $15.2/Gb internal.
   - 10B lane, 300 cycle (375 Gb): $2,400 / $2,640, about $6.40/Gb internal.
   - 25B lane, 300 cycle (930 Gb): $4,200 / $4,620, about $4.52/Gb internal and about $4.97/Gb external.
   - The same sheet still lists NovaSeq 6000 S4 2x150 at $6,615 internal / $6,945.75 external. It gives no Gb for S4, so no 6000 $/Gb can be derived.
   - Rush's own cover note says a 25B lane is cheaper per cluster than 2.5 x 10B lanes.
   - Source: Rush GMCF fee schedule dated 15 Jun 2026, https://www.rushu.rush.edu/sites/default/files/2026-06/GMCF%20Pricing%20June%202026.pdf
   - This is a $4.5–5.0/Gb data point for 25B, well above the $2.5–3.3/Gb range in E054. It is a small university core that includes labor and overhead. It supports E051's caveat that core prices run above Illumina's $2.00/Gb list.

2. **Two more dated lane prices with Gb attached. FACT.**
   - Novogene's spring 2026 promotion: $2,599 per 1,000 Gb lane (25B), about $2.60/Gb, and $1,599 per 375 Gb lane (10B), about $4.26/Gb. It applied to quotes issued on or before 30 Jun 2026 and needed discount codes. Source: https://web.novogene.com/Website_Premade_2026_Spring
   - The Utah Huntsman core, updated Jan 2026, lists these lanes (read-pairs, not Gb):

   | Flow cell | Internal | External |
   |---|---|---|
   | 10B | $1,250 | $1,500 |
   | 25B | $2,600 | $3,120 |

   - Utah's 25B lane is 3,000M read-pairs. Source: https://uofuhealth.utah.edu/huntsman/shared-resources/gcb/htg/pricing
   - A search snippet attributes $2,799 per 950 Gb lane (about $2.95/Gb) and WGS "as low as $488/sample" to Azenta/GENEWIZ. I did not open that page.

3. **Broad Clinical Labs publishes walk-up prices, including Ultima. FACT.** The page says "NovaSeq X Plus starting as low as $2,375 per 25B lane" and "Ultima Genomics UG 100 starting as low as $4,000 per wafer". It specifies at least 2.8B reads per 25B lane and at least 8B reads per UG100 wafer. It lists the NovaSeq 6000 as still offered (S4, S2, S1, SP). The page has no date. Source: https://broadclinicallabs.org/sequencing-of-customer-prepared-libraries/
   - Per-read, that is about $0.85 per million reads on X versus $0.50 per million on Ultima (my calculation, OPINION). The Ultima figure is a floor ("as low as") and the Gb per read is not stated.
   - It shows a clinical-grade lab, an early AXELIOS evaluator (E124), pricing Ultima capacity roughly 40% lower per read than X. That is read-through for Illumina price pressure.

4. **No NovaSeq X-labelled FDA assay exists, and the TSO Comprehensive approval is dated. This corroborates E250 with a primary FDA record.**
   - FDA lists TruSight Oncology Comprehensive as PMA P230011, approved 21 Aug 2024, with companion-diagnostic claims for VITRAKVI (NTRK fusions) and RETEVMO (RET-mutant NSCLC).
   - Search results describe the system as NextSeq 550Dx. I could not confirm the instrument from the FDA page text itself.
   - I found no 2026 clearance naming a NovaSeq X.
   - I did not query the PMA or 510(k) databases directly.
   - Source: https://www.fda.gov/medical-devices/recently-approved-devices/trusight-oncology-comprehensive-p230011

5. **Illumina's roadmap page adds a customer-reported 30% output gain with no price change. FACT/MGMT.**
   - Roadmap windows: 5B and 1.5B flow cells in H1 2026; "HT mode" in H2 2026 ("increase reads for better sequencing economics"); 35B, 14B, Q70/Q50 and 20–22 hour WGS in H1 2027; "40% yield improvement on 10B flow cells".
   - The page quotes Texas A&M AgriLife: "Since we purchased the NovaSeq X, the usable output per run has increased by roughly 30 percent thanks to the improvements Illumina continues to introduce."
   - A 30% yield gain on an unchanged flow cell price is a 23% cut in $/Gb. It is price deflation that never shows up as a list-price cut, and it is separate from the 35B event (E057, E058).
   - The HT mode in H2 2026 is a possible additional yield lever. I did not find its terms.
   - The page states no pricing. Source: https://www.illumina.com/systems/sequencing-platforms/novaseq-x-plus/applications/innovation-roadmap.html

6. **Illumina's transition page makes no revalidation claim. FACT.** It says the X narrows the WGS-to-WES cost gap "by over 2.5× compared to the NovaSeq 6000 System" and that it enables a "$200 USD genome". It does not mention revalidation or parallel running. Customer quotes are about usability only. Source: https://www.illumina.com/systems/sequencing-platforms/novaseq-x-plus/applications/transition.html, fetched 2026-10-11. This is consistent with E031's view that revalidation is a hidden friction Illumina does not address publicly.

## Clinical-lab validation evidence

- **No peer-reviewed or preprint paper (2025–26) reporting a clinical lab's 6000-to-X migration was found.** That means no Gb per sample, cost before and after, parallel-run length or revalidation burden. Searches covered JMD, Genetics in Medicine, Clinical Chemistry and medRxiv/bioRxiv through the search engine only. I did not browse tables of contents or PubMed.
- **Uppsala University Hospital Clinical Genetics (FACT).** It put the X Plus into operation in May 2024. The first clinical tests were rare-disease WGS and WGS plus whole-transcriptome sequencing for pediatric acute leukemia. Bondeson says the instrument "reduces the cost per sample" and lets previously outsourced work be analyzed internally. Rare-disease patients rose about 40% in 2024 versus 2023. No figures on Gb, cost or parallel running were given. Source: https://www.uu.se/en/research/clinical-genomics-uppsala/news/archive/2025-03-26-new-technology-enables-faster-diagnoses-of-genetic-health-conditions
  - This is a named clinical lab that moved volume in-house onto the X. The 40% patient growth is a volume data point for E083/E205, but it is one site and is not in Gb.
- **Orchid Health WGS concordance (FACT).** Orchid compared its proprietary 30x whole-genome assay on X Plus and 6000 using 5 GIAB cell lines. It observed "higher accuracy, specificity, sensitivity, and comparable precision" on X, with no numbers given. The dated source (17 Oct 2023) is old and Orchid's CLIA status is not stated. Source: https://www.psomagen.com/news/case-study-novaseq-x-plus
  - It shows revalidation of an LDT on X is feasible in a small N, but that N is 5 samples.
- **Discovery Life Sciences (FACT, Apr 2023).** It began cross-validating WGS, WES and RNA-seq libraries on X Plus "to help customers transition from NovaSeq 6000", with 2 systems and a plan for 5. This is old and is a commercial lab, not a clinical lab. Source: https://256today.com/discovery-hosts-largest-fleet-of-genomic-research-accelerators/
- **Illumina TSO 500 HT tech note M-GL-02869 and the TSO ctDNA v2 6000/X concordance note M-GL-03016 were not read.** The first PDF exceeded the fetch size cap and the second returned binary. A search snippet attributes this to M-GL-03016: it says a baseline analysis of 77 normal samples found CNV false-positive concordance R² = 0.99, SV R² = 0.82, MSI 0% false positives and TMB R² = 0.86. Another snippet says SNP/indel precision and recall differ by under 0.5% between platforms. Treat both as unverified snippets. If they hold, the X reproduces 6000 results with little revalidation risk for these assays.

## Challengers

- **Ultima preprint.** The identification matches E252. Europe PMC returns PPR1231843 and the abstract (Santuari, Kolpakov, Blin, Xenarios, Howald). Direct bioRxiv fetch returned 429 and the Europe PMC full-text XML returned 500, so full text is still not read.
  - The abstract says the UG100 "reduces genome sequencing costs to $80" but "technical limitations in resolving long homopolymer regions undermine the application of this technology to short variant calling in clinical settings". The comparator is the NovaSeq 6000. This is the authors' own abstract language, and it confirms the sign of E252's snippet-level finding. The abstract has no numbers.
- **Owkin preprint, bioRxiv, 13 Mar 2026 (FACT).** "Multi-modal benchmarking of the Ultima UG100 and Illumina NovaSeq sequencing platforms using clinically relevant FFPE tissues" covered snRNA-seq, WTS, WES and WGS. It reports comparable performance, with discrepancies "largely limited to pseudogene and non-coding transcripts, and did not affect pathway-level conclusions". It is a pharma/AI company, not a clinical lab, and I did not read the sample count. Source: https://www.owkin.com/publications/multi-modal-benchmarking-of-the-ultima-ug100-and-illumina-novaseq-sequencing-platforms-using-clinically-relevant-ffpe-tissues
  - This is the first third-party evidence that Ultima matches Illumina on FFPE exome and genome, which is the clinical oncology sample type. It partly offsets E252's negative homopolymer finding.
- **Roche AXELIOS (FACT, search-snippet level).** Roche says it "booked pre-orders" but declined further detail, and the launch is research use only. The GenomeWeb article "Roche Sets Sights on Clinic Following Commercial Launch of Axelios 1" returned 403. A snippet says early-access users compared AXELIOS and the NovaSeq 6000 on tumor-normal pairs. The Roche ADLM press release (22 Jul 2026) returned unreadable binary.
- **Element.** I found no named clinical lab running AVITI or AVITI24 in a CLIA or CAP setting. Element says clinical research was more than 25% of revenue in 2025, which is higher than the 20% in E129 (the two may use different definitions or periods). Element also says it achieved ISO 13485. Source: search snippet only, so treat it as unverified.
- **ASHG 2026 (20–24 Oct).** No ASHG or AMP 2026 abstract listing naming X migration, Ultima, Element or AXELIOS clinical use was found. Element lists an ASHG 2026 presence for VITARI and AVITI24. The abstract database is not indexed.

## Contradictions and stale data

- The Rush $4.52–4.97/Gb for 25B conflicts with the $2.5–3.3/Gb range in E054. The likely cause is a small core with labor and overhead included, and the sheet gives only a 930 Gb lane. It does not contradict Illumina's $2.00 list, which is consumables only.
- Novogene's $2.60/Gb is a time-limited promotion (to 30 Jun 2026), so it is not a stable list price.
- The Broad Clinical Labs and Texas A&M items are undated or unattributed in time. Do not use them as time-series points.
- Orchid (2023) and Discovery (2023) are old and do not describe the 2026 migration state.
- The Rush sheet's NovaSeq 6000 S4 price ($6,615) cannot be converted to $/Gb. S4 per-lane Gb was not on the sheet, and the S4 flow-cell output I recall is a general figure, not from the source.

## Gaps / what I could not find

- The 35B and 14B price and date. Illumina's roadmap has no pricing and gives H1 2027. No distributor or core announcement was found.
- Any named clinical lab with Gb per sample, cost before and after, parallel-run duration or revalidation cost for a 6000-to-X move.
- The TSO 500 HT tech note M-GL-02869 and the M-GL-03016 concordance note. Both PDFs failed, so Gb per sample and samples per flow cell are unknown. The saved binary copy of M-GL-03016 is in the tool-results folder, but PDF rendering is unavailable here.
- The Ultima preprint full text, and the GenomeWeb AXELIOS clinical article.
- Direct FDA 510(k)/PMA/De Novo database queries, and NYS CLEP/CAP notices on sequencer changes.
- Aug–Oct 2026 trade press on AXELIOS orders or lab switching. Searches returned only June–July 2026 launch coverage.
- Northwestern FY26 prices (PDF unreadable). Harvard and UCLA lane Gb are still missing.

Sources:
- [Rush GMCF fee schedule, 15 Jun 2026](https://www.rushu.rush.edu/sites/default/files/2026-06/GMCF%20Pricing%20June%202026.pdf)
- [Novogene spring 2026 premade-library promotion](https://web.novogene.com/Website_Premade_2026_Spring)
- [Utah Huntsman HTG pricing, Jan 2026](https://uofuhealth.utah.edu/huntsman/shared-resources/gcb/htg/pricing)
- [Broad Clinical Labs walk-up sequencing](https://broadclinicallabs.org/sequencing-of-customer-prepared-libraries/)
- [FDA P230011 TruSight Oncology Comprehensive](https://www.fda.gov/medical-devices/recently-approved-devices/trusight-oncology-comprehensive-p230011)
- [Illumina NovaSeq X innovation roadmap](https://www.illumina.com/systems/sequencing-platforms/novaseq-x-plus/applications/innovation-roadmap.html)
- [Illumina NovaSeq X transition page](https://www.illumina.com/systems/sequencing-platforms/novaseq-x-plus/applications/transition.html)
- [Uppsala University Clinical Genomics, 26 Mar 2025](https://www.uu.se/en/research/clinical-genomics-uppsala/news/archive/2025-03-26-new-technology-enables-faster-diagnoses-of-genetic-health-conditions)
- [Psomagen/Orchid case study, 17 Oct 2023](https://www.psomagen.com/news/case-study-novaseq-x-plus)
- [Discovery Life Sciences, 4 Apr 2023](https://256today.com/discovery-hosts-largest-fleet-of-genomic-research-accelerators/)
- [Owkin Ultima benchmarking preprint, 13 Mar 2026](https://www.owkin.com/publications/multi-modal-benchmarking-of-the-ultima-ug100-and-illumina-novaseq-sequencing-platforms-using-clinically-relevant-ffpe-tissues)
- [Ultima UG100 clinical-services preprint](https://www.biorxiv.org/content/10.64898/2025.12.11.693628.full.pdf)
