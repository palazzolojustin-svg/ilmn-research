Only a few new cores turned up. Most cores that publish AVITI or Ultima prices were already on your known list. I stopped at about 7 minutes of searching, and the search tool kept returning the same known cores.

- **New cores with a verified AVITI price:** only the University of Iowa Holden Comprehensive Cancer Center Microbiome Core. Its AVITI24 rate is about $45 per sample internal for batches under 92 samples, and the page has a "2026 Prices" heading.
- **New cores with no usable price:**
  - Michigan's Advanced Genomics Core announced Ultima UG 100 service, but I found no public price. Its page returned a 403 when I opened it, so I haven't confirmed whether a rate sheet exists.
  - The University of Idaho item is a PDF I could not read. It is unverified and may not contain prices.
- **Known cores:** I added extra URLs for several of them, mainly older or dated versions for history. These come from search results, and I did not open them unless the notes say verified.
- **Ultima prices:** OICR and Minnesota are the only cores with public Ultima prices. Cornell's UG100 page says "pricing on request".
- **Price-change announcements:** the Minnesota AVITI posts (Jul 2024, Dec 2024, Sep 2025) and the EPFL news log. The EPFL log shows AVITI price cuts in Mar 2025 and Nov 2025, plus a Sep 2026 entry.
- **Not searched:** I did not search iLab, CoreSmart or similar portals, so I have nothing on login-gated pages. I also did not pursue the Vanderbilt VANTAGE iLab external page.

```json
{"cores":[
{"institution":"University of Michigan","core":"BRCF Advanced Genomics Core (AGC)","country":"US","kind":"university","platforms":["UG100","NovaSeq X","NextSeq 2000"],
"urls":[
{"url":"https://cores.research.umich.edu/core/brcf-advanced-genomics-core","type":"rate_page","current":true,"public":true,"verified":false,"as_of":null},
{"url":"https://medresearch.umich.edu/office-research/about-office-research/biomedical-research-core-facilities/advanced-genomics-core/technologies/next-generation-sequencing","type":"rate_page","current":true,"public":true,"verified":false,"as_of":null},
{"url":"https://medresearch.umich.edu/office-research/advanced-genomics-core-among-first-launch-ultima-genomics-ug-100-unlocking-affordable-high","type":"announcement","current":true,"public":true,"verified":false,"as_of":null}],
"notes":"One of the first UG 100 Certified Service Providers. No public prices found. The NGS page returned HTTP 403 when fetched, so I could not tell whether it links to a rate sheet."},
{"institution":"University of Iowa","core":"Holden Comprehensive Cancer Center Microbiome Core","country":"US","kind":"academic_medical_center","platforms":["AVITI"],
"urls":[{"url":"https://microbiomecore.sites.uiowa.edu/node/11","type":"rate_page","current":true,"public":true,"verified":true,"as_of":"2026-01"}],
"notes":"AVITI24 small batch (<92 samples) internal $45 per sample, library prep plus sequencing, '2026 Prices' heading. The page also shows a 2024-01-01 date. It is separate from the IIHG core already known."},
{"institution":"University of Idaho","core":"GBRC (Genomics and Bioinformatics Resources Core) facilities resources","country":"US","kind":"university","platforms":["unknown"],
"urls":[{"url":"https://iids.uidaho.edu/docs/GBRC_Facilities_Resources_2026.pdf","type":"pdf","current":true,"public":true,"verified":false,"as_of":"2026"}],
"notes":"Surfaced in an AVITI24 search. I could not read the PDF, so I don't know whether it has prices or which platforms it covers."},
{"institution":"Cornell University","core":"BRC Genomics Facility (known core, extra URLs)","country":"US","kind":"university","platforms":["AVITI","UG100"],
"urls":[
{"url":"https://www.biotech.cornell.edu/core-facilities-brc/price-list/404","type":"rate_page","current":true,"public":true,"verified":false,"as_of":null},
{"url":"https://www.biotech.cornell.edu/core-facilities-brc/services/element-aviti24-sequencing-cytoprofiling-situ-rna-seq-atlas-antibody","type":"rate_page","current":true,"public":true,"verified":false,"as_of":null},
{"url":"https://www.biotech.cornell.edu/core-facilities-brc/services/ultima-ug100-sequencing","type":"rate_page","current":true,"public":true,"verified":true,"as_of":null}],
"notes":"AVITI24 lane (400M reads) $799 internal, $999 external. The UG100 page gives no price, only a quote request and about $0.24 per million reads."},
{"institution":"University of Minnesota","core":"University of Minnesota Genomics Center (UMGC) (known core, extra URLs)","country":"US","kind":"university","platforms":["AVITI","UG100","NovaSeq X"],
"urls":[
{"url":"https://genomics.umn.edu/service/aviti24-sequencing","type":"rate_page","current":true,"public":true,"verified":false,"as_of":null},
{"url":"https://genomics.umn.edu/service/aviti-sequencing","type":"rate_page","current":true,"public":true,"verified":false,"as_of":null},
{"url":"https://genomics.umn.edu/service/ug-100-sequencing","type":"rate_page","current":true,"public":true,"verified":false,"as_of":null},
{"url":"https://genomics.umn.edu/service/human-whole-genome-sequencing","type":"rate_page","current":true,"public":true,"verified":false,"as_of":null},
{"url":"https://genomics.umn.edu/news/preferred-ultima-ug-100-pricing-10x-genomics-projects","type":"announcement","current":true,"public":true,"verified":false,"as_of":null},
{"url":"https://genomics.umn.edu/AVITI-price-drop-2024","type":"announcement","current":false,"public":true,"verified":false,"as_of":"2024-12"},
{"url":"https://genomics.umn.edu/news/aviti-upgrade-complete","type":"announcement","current":true,"public":true,"verified":false,"as_of":"2025-09"},
{"url":"https://genomics.umn.edu/news/ultima-ug-100-arrives","type":"announcement","current":false,"public":true,"verified":false,"as_of":"2024-11"}],
"notes":"UG100 wafer (10-12B reads) $2,909 UMN and $3,212 external. 10x preferred pricing is $2,409 and $2,712. AVITI price cuts: about 40% in Jul 2024, about 20% more in Dec 2024, and 33% lower per read in Sep 2025 (output +50%, price flat)."},
{"institution":"EPFL","core":"Gene Expression Core Facility (known core, extra URLs)","country":"Switzerland","kind":"university","platforms":["AVITI","NovaSeq"],
"urls":[
{"url":"https://www.epfl.ch/research/facilities/gene-expression-core-facility/wp-content/uploads/2026/02/GECF-price-list-for-EPFL-users-15-February-2026.pdf","type":"pdf","current":true,"public":true,"verified":false,"as_of":"2026-02"},
{"url":"https://www.epfl.ch/research/facilities/gene-expression-core-facility/wp-content/uploads/2025/07/GECF-price-list-for-EPFL-users-01-July-2025.pdf","type":"pdf","current":false,"public":true,"verified":false,"as_of":"2025-07"},
{"url":"https://www.epfl.ch/research/facilities/gene-expression-core-facility/wp-content/uploads/2025/03/GECF-price-list-for-EPFL-users-01-March-2025.pdf","type":"pdf","current":false,"public":true,"verified":false,"as_of":"2025-03"},
{"url":"https://www.epfl.ch/research/facilities/gene-expression-core-facility/news","type":"announcement","current":true,"public":true,"verified":false,"as_of":"2026-09"}],
"notes":"Dated price-list PDFs (Mar 2025, Jul 2025, Feb 2026). News log shows AVITI price cuts in Mar 2025 and Nov 2025."},
{"institution":"Northwestern University","core":"NUSeq Core (known core, extra URLs)","country":"US","kind":"university","platforms":["AVITI","NovaSeq X"],
"urls":[
{"url":"https://www.cgm.northwestern.edu/cores/nuseq/pricing.html","type":"rate_page","current":true,"public":true,"verified":false,"as_of":null},
{"url":"https://www.cgm.northwestern.edu/docs/nuseq/fy26-prices_finalusers.pdf","type":"pdf","current":true,"public":true,"verified":false,"as_of":"2025-09"},
{"url":"https://www.cgm.northwestern.edu/docs/nuseq/fy25-pricing.pdf","type":"pdf","current":false,"public":true,"verified":false,"as_of":"2024-09"},
{"url":"https://www.cgm.northwestern.edu/docs/nuseq/sg_elements_aviti_overview.pdf","type":"pdf","current":false,"public":true,"verified":false,"as_of":null}],
"notes":"FY26 NovaSeq X Plus 25B PE150 lane $3,000 internal, versus $2,800 in FY25. AVITI PE150 high-output lane $1,300 internal in FY26."},
{"institution":"Arizona","core":"Arizona Genetics Core (known core, extra URL)","country":"US","kind":"university","platforms":["AVITI"],
"urls":[
{"url":"https://azgc.arizona.edu/sites/default/files/2024-07/AZGC%20Rates_Effective%201Aug2024.pdf","type":"pdf","current":false,"public":true,"verified":false,"as_of":"2024-08"},
{"url":"https://azgc.arizona.edu/services/services/element-aviti-24","type":"rate_page","current":true,"public":true,"verified":false,"as_of":null},
{"url":"https://cores.arizona.edu/facilities/news/new-technology-introduction-az-genetics-core-sept-7-2024","type":"announcement","current":false,"public":true,"verified":false,"as_of":"2024-09"}],
"notes":"AVITI is listed as 'varies, contact core', so it has no fixed price."},
{"institution":"Michigan State University","core":"RTSF Genomics (known core, extra URLs)","country":"US","kind":"university","platforms":["AVITI"],
"urls":[
{"url":"https://rtsf.natsci.msu.edu/genomics/pricing.aspx","type":"rate_page","current":true,"public":true,"verified":false,"as_of":null},
{"url":"https://rtsf.natsci.msu.edu/_assets/files/genomics/100924_SG_Elements_AVITI_and_24_Overview_Michigan_State_University.pdf","type":"pdf","current":false,"public":true,"verified":false,"as_of":"2024-10"}],
"notes":"Oct 2024 overview: 2x150 high-output flow cell $2,089 (about $6.96/Gb)."},
{"institution":"UC Riverside","core":"IIGB Genomics Core (known core, extra URL)","country":"US","kind":"university","platforms":["AVITI"],
"urls":[{"url":"https://genomics.iigb.ucr.edu/rates","type":"rate_page","current":true,"public":true,"verified":false,"as_of":"2024"}],
"notes":"FY24-25 AVITI 300-cycle flow cell $2,000 for UC internal users."},
{"institution":"UC Davis","core":"DNA Technologies Core (known core, extra URLs)","country":"US","kind":"university","platforms":["AVITI"],
"urls":[
{"url":"https://dnatech.genomecenter.ucdavis.edu/element-bio-aviti-sequencing/","type":"rate_page","current":true,"public":true,"verified":false,"as_of":null},
{"url":"https://dnatech.ucdavis.edu/element-biosciences-aviti-sequencing","type":"rate_page","current":false,"public":true,"verified":false,"as_of":null}],
"notes":"UC-rate AVITI PE150 run $2,100 and PE75 run $1,400 on the newer page. The older page showed $2,000 for PE150."},
{"institution":"UC San Diego","core":"IGM Genomics Center (known core, extra URL)","country":"US","kind":"university","platforms":["NovaSeq X"],
"urls":[{"url":"https://igm.ucsd.edu/sites/default/files/docs/IGM%20Rates%202025%20New%20IDC.pdf","type":"pdf","current":false,"public":true,"verified":false,"as_of":"2025"}],
"notes":"2025 rate PDF; I did not check its contents."},
{"institution":"University of Nebraska Medical Center","core":"Genomics Core (known core, extra URL)","country":"US","kind":"academic_medical_center","platforms":["AVITI","NovaSeq 6000"],
"urls":[{"url":"https://www.unmc.edu/research-resources/resources/cores/genomics-core/pricing.html","type":"rate_page","current":true,"public":true,"verified":false,"as_of":null}],
"notes":"AVITI24 2x150 UltraQ $3,763 internal and $5,645 external. 2x150 high output $2,601 internal."},
{"institution":"University of Chicago","core":"Genomics Facility (known core, extra URL)","country":"US","kind":"university","platforms":["AVITI","NovaSeq X"],
"urls":[
{"url":"https://voices.uchicago.edu/genomicsfacility/pricing-new","type":"rate_page","current":true,"public":true,"verified":false,"as_of":null},
{"url":"https://voices.uchicago.edu/genomicsfacility/ngs","type":"rate_page","current":true,"public":true,"verified":false,"as_of":null}],
"notes":"AVITI flow cell 150 bp $1,175 and 300 bp $1,475, per the 2024 example costs."},
{"institution":"Salk Institute","core":"Integrative Genomics and Bioinformatics Core (known core, extra URLs)","country":"US","kind":"nonprofit_institute","platforms":["AVITI","NovaSeq X"],
"urls":[
{"url":"https://www.salk.edu/science/core-facilities/integrative-genomics-and-bioinformatics-core/scheduling-and-rates/","type":"rate_page","current":true,"public":true,"verified":false,"as_of":null},
{"url":"https://salk.edu/science/core-facilities/omics/scheduling-and-rates","type":"rate_page","current":false,"public":true,"verified":false,"as_of":null},
{"url":"https://salk.edu/science/core-facilities/next-generation-sequencing/scheduling-and-rates","type":"rate_page","current":false,"public":true,"verified":false,"as_of":null}],
"notes":"AVITI high output 300-cycle flow cell $3,610 (internal rate). The page is undated. Two older URL paths may be superseded."},
{"institution":"Harvard University","core":"Bauer Core Facility (known core, extra URL)","country":"US","kind":"university","platforms":["NovaSeq X"],
"urls":[{"url":"https://bauercore.fas.harvard.edu/fy26-ngs-sequencing","type":"rate_page","current":true,"public":true,"verified":false,"as_of":"2025-07"}],
"notes":"FY26 NovaSeq X Plus 25B 300-cycle lane $2,059 on a Harvard account code, $2,883 by PO."},
{"institution":"Ontario Institute for Cancer Research","core":"OICR Genomics (known core, extra URLs)","country":"Canada","kind":"nonprofit_institute","platforms":["UG100"],
"urls":[
{"url":"https://genomics.oicr.on.ca/ultima-sequencing/","type":"rate_page","current":true,"public":true,"verified":false,"as_of":null},
{"url":"https://genomics.oicr.on.ca/?p=5935","type":"rate_page","current":true,"public":true,"verified":false,"as_of":null}],
"notes":"Wafer (10B) CAD $5,130, minimum 2 wafers. 30X WGS CAD $435."}
]}
```

Sources:
- [Cornell price list](https://www.biotech.cornell.edu/core-facilities-brc/price-list/404)
- [Salk rates](https://www.salk.edu/science/core-facilities/integrative-genomics-and-bioinformatics-core/scheduling-and-rates/)
- [EPFL Feb 2026 price list](https://www.epfl.ch/research/facilities/gene-expression-core-facility/wp-content/uploads/2026/02/GECF-price-list-for-EPFL-users-15-February-2026.pdf)
- [UMN AVITI upgrade post](https://genomics.umn.edu/news/aviti-upgrade-complete)
- [UMN Ultima pricing for 10x projects](https://genomics.umn.edu/news/preferred-ultima-ug-100-pricing-10x-genomics-projects)
- [Iowa Microbiome Core](https://microbiomecore.sites.uiowa.edu/node/11)
- [Northwestern FY26 prices](https://www.cgm.northwestern.edu/docs/nuseq/fy26-prices_finalusers.pdf)
- [UNMC pricing](https://www.unmc.edu/research-resources/resources/cores/genomics-core/pricing.html)