I found only a few cores in my slice that publish sequencing prices, far short of the 15–30 target. Search was weak for institutes: Broad, Whitehead, JAX, Stowers, HudsonAlpha, Van Andel, Fred Hutch, St. Jude, MSK IGO, CSHL, NYGC, Wistar, Scripps, Gladstone, Sanger, Crick, EMBL, Garvan, WEHI, Max Planck, Pasteur, Curie and VBCF returned no public rate card. I stopped after the second round of searches and did not retry them with site-specific queries.

- **Verified rate pages (opened):**
  - NCI Frederick's FSGC page lists NovaSeq X Plus 1.5B–25B flow cells and NextSeq 2000. It has no AVITI or UG100, and no date or PDFs. Sample line: 1.5B 100-cycle $2,042 NCI, $4,084 non-NCI.
  - OICR's page prices the UG100 Solaris, with no NovaSeq X or AVITI. Sample line: 10B wafer CAD $5,130, minimum 2 wafers, academic use only. It has no date or PDFs.
  - La Jolla Institute lists NovaSeq 6000 flow cells with no date. Sample line: SP 100-cycle full flow cell $3,258 institute, $3,584 non-profit, $5,963 for-profit.
  - EPFL's Gene Expression Core Facility is a university, not in my slice. I included it because it keeps dated price-list PDFs and a news log of price cuts from 2025 to 2026. It covers NovaSeq and AVITI/AVITI24, priced in CHF.
- **Seen only in a search snippet, not opened:**
  - CRG Barcelona has a 2026 PDF, valid from 2026-01-01, with NovaSeq X Plus priced per million reads in EUR. The two price columns were unlabeled in the snippet. WebFetch could not read the PDF, so I could not confirm the platforms or the internal/external labels.
  - The EPFL PDFs from 2025-03, 2025-07, 2026-02 and 2026-09 and the Prices page appeared in search results only.
- **No public prices:**
  - Sanford Burnham Prebys runs an AVITI24 core, but its page has no prices.
  - Lerner (Cleveland Clinic) and Seattle Children's send you to iLab. The Seattle Children's page only prices NextSeq 2000 instrument time ($257.50 per day, internal, as of 2026-04-01).
  - IGE3 Geneva prices only NovaSeq fractions, with no platform named. The Genome Québec and Warsaw CeNT pages had no usable run prices; the CeNT URL returned 404.
  - HudsonAlpha's Genomic Services Lab may no longer be in service, per an RRID registry note.
  - Whitehead's Genome Technology Core pricing wiki appeared in results, but the fetch failed.
- **Other:** The Univ. of Minnesota UG100 pages are probably already covered, since UMGC is on your known list. Most other results were university cores, which are either on your known list or outside my slice.

```json
{"cores": [
{"institution": "National Cancer Institute (NIH), Frederick", "core": "Frederick Sequencing & Genomics Core (FSGC) NGS Production", "country": "US", "kind": "government",
 "platforms": ["NovaSeq X", "NextSeq 2000"],
 "urls": [
  {"url": "https://crtp.ccr.cancer.gov/fsgc/services/ngs-production/pricing", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": null},
  {"url": "https://crtp.ccr.cancer.gov/fsgc/?p=61", "type": "rate_page", "current": true, "public": true, "verified": false, "as_of": null}],
 "notes": "NovaSeq X Plus 1.5B 100 cycle $2,042 per flow cell NCI, $4,084 non-NCI. No AVITI or UG100. The page has a downloadable cost calculator but no file URL and no date."},
{"institution": "Ontario Institute for Cancer Research", "core": "OICR Genomics (Ultima sequencing)", "country": "Canada", "kind": "nonprofit_institute",
 "platforms": ["UG100"],
 "urls": [
  {"url": "https://genomics.oicr.on.ca/ultima-sequencing/", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": null},
  {"url": "https://genomics.oicr.on.ca/?p=5935", "type": "rate_page", "current": true, "public": true, "verified": false, "as_of": null}],
 "notes": "UG100 Solaris 10B wafer CAD $5,130 list, minimum 2 wafers, academic use only. The page footer is 2026 and has no price date."},
{"institution": "La Jolla Institute for Immunology", "core": "Sequencing Core", "country": "US", "kind": "nonprofit_institute",
 "platforms": ["NovaSeq 6000"],
 "urls": [
  {"url": "https://lji.org/research/research-services/sequencing", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": null},
  {"url": "https://www.lji.org/?p=12460", "type": "rate_page", "current": true, "public": true, "verified": false, "as_of": null}],
 "notes": "NovaSeq SP 100 cycle full flow cell $3,258.33 institute, $3,584.17 non-profit, $5,962.75 for-profit. The page is undated, has no PDFs, and uses NovaSeq 6000 only."},
{"institution": "Centre de Regulacio Genomica (CRG)", "core": "CRG Genomics Unit", "country": "Spain", "kind": "nonprofit_institute",
 "platforms": ["NovaSeq X"],
 "urls": [
  {"url": "https://www.crg.eu/sites/default/files/crg/genomic_service_fees2026_r0.pdf", "type": "pdf", "current": true, "public": true, "verified": false, "as_of": "2026-01"}],
 "notes": "Genomics Services Price List, valid from 01/01/2026 (R0). A search snippet showed NovaSeq X Plus (300 cycles, 10B) priced per million reads in EUR, with two unlabeled price columns. WebFetch could not read the PDF. Try the earlier editions (e.g. a 2025 equivalent) by changing the year in the filename, but I did not see those URLs."},
{"institution": "EPFL", "core": "Gene Expression Core Facility (GECF)", "country": "Switzerland", "kind": "university",
 "platforms": ["NovaSeq", "NovaSeq X", "AVITI", "AVITI24"],
 "urls": [
  {"url": "https://www.epfl.ch/research/facilities/gene-expression-core-facility/page-154614-en-html/", "type": "rate_page", "current": true, "public": true, "verified": false, "as_of": null},
  {"url": "https://www.epfl.ch/research/facilities/gene-expression-core-facility/news", "type": "announcement", "current": true, "public": true, "verified": true, "as_of": "2026-10"},
  {"url": "https://www.epfl.ch/research/facilities/gene-expression-core-facility/wp-content/uploads/2026/09/GECF-price-list-for-EPFL-users-09-September-2026.pdf", "type": "pdf", "current": true, "public": true, "verified": false, "as_of": "2026-09"},
  {"url": "https://www.epfl.ch/research/facilities/gene-expression-core-facility/wp-content/uploads/2026/02/GECF-price-list-for-EPFL-users-15-February-2026.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2026-02"},
  {"url": "https://www.epfl.ch/research/facilities/gene-expression-core-facility/wp-content/uploads/2025/07/GECF-price-list-for-EPFL-users-01-July-2025.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2025-07"},
  {"url": "https://www.epfl.ch/research/facilities/gene-expression-core-facility/wp-content/uploads/2025/03/GECF-price-list-for-EPFL-users-01-March-2025.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2025-03"}],
 "notes": "University core, outside my slice, kept because it has a dated history. Prices are in CHF, per run plus a per-sample reagent fee. Search snippets showed one AVITI 300-cycle run at 2,330 CHF in the 2025-07 list, but the table layout was unclear. The news page, which I opened, logs price cuts for 2025-03, 2025-07, 2025-09, 2025-10, 2025-11, 2026-03, 2026-09 and 2026-10. It also notes the AVITI upgrade to AVITI24 in November 2025."},
{"institution": "Sanford Burnham Prebys Medical Discovery Institute", "core": "Genomics and Spatial Transcriptomics core", "country": "US", "kind": "nonprofit_institute",
 "platforms": ["AVITI"],
 "urls": [
  {"url": "https://www.sbpdiscovery.org/medical-discovery/shared-resources/genomics", "type": "rate_page", "current": true, "public": true, "verified": false, "as_of": null}],
 "notes": "Describes AVITI24 sequencing (the cached copy says AVITI with 1B reads) but no prices were visible. Likely request-based or on a login-gated page. Low priority."},
{"institution": "Cleveland Clinic Lerner Research Institute", "core": "Genomics Core", "country": "US", "kind": "academic_medical_center",
 "platforms": ["NovaSeq 6000"],
 "urls": [
  {"url": "https://www.lerner.ccf.org/cores/genomics/", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": null}],
 "notes": "No prices on the page. Pricing is in iLab (ccf.ilab.agilent.com), which is login-gated. Skip unless an iLab show_external page exists."},
{"institution": "Seattle Children's Research Institute", "core": "Genomics and Spatial Biology CoLab", "country": "US", "kind": "nonprofit_institute",
 "platforms": ["NextSeq 2000"],
 "urls": [
  {"url": "https://www.seattlechildrens.org/research/resources/genomics-spatial-biology-colab/rates/", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": "2026-04"}],
 "notes": "Internal prices as of 2026-04-01, but only NextSeq 2000 instrument time ($257.50 per day) and prep and QC items. No per-flow-cell NovaSeq X, AVITI or UG100 prices. Marginal value."}
]}
```

Sources:
- [NCI FSGC pricing](https://crtp.ccr.cancer.gov/fsgc/services/ngs-production/pricing)
- [OICR Ultima sequencing](https://genomics.oicr.on.ca/ultima-sequencing/)
- [La Jolla Institute sequencing](https://lji.org/research/research-services/sequencing)
- [CRG 2026 genomics fees](https://www.crg.eu/sites/default/files/crg/genomic_service_fees2026_r0.pdf)
- [EPFL GECF news](https://www.epfl.ch/research/facilities/gene-expression-core-facility/news)
- [Seattle Children's CoLab rates](https://www.seattlechildrens.org/research/resources/genomics-spatial-biology-colab/rates/)
- [Lerner Genomics Core](https://www.lerner.ccf.org/cores/genomics/)
- [SBP Genomics](https://www.sbpdiscovery.org/medical-discovery/shared-resources/genomics)