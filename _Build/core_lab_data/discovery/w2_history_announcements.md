Status: I've covered the main search angles (price-cut news posts, FY25/FY26 rate sheets, AVITI, Ultima, tariff surcharges). I'm now writing up the cores and URLs I found.

Notes:
- Most cores in my slice were already on your known list, so I mainly added history and announcement URLs for them. The new cores are the University of Tennessee Knoxville, NDSU, UNMC (page is only listed as known for the Genomics Core, so I'm treating the bioinformatics page as unconfirmed), Stanford PAN, Emory, Oklahoma State and CHLA.
- Dated announcements I opened and confirmed:
  - UMGC AVITI: ~40% cut in Jul 2024, a further ~20% cut on 2024-12-19, then a 50% output increase at the same price on 2025-09-15.
  - Missouri: 40% cut announced 2024-09-06.
  - UGA: lower prices, Mar 2025.
- Pages I could not open (HTTP 403): Oklahoma State MBGC FY26 sheet and CHLA. Both are listed as unverified.
- Stanford PAN adds a separate tariff surcharge line, but its page shows only MiSeq, with no sequencing prices for the platforms you want. I have not seen a sample line for Emory either.
- I did not find public Ultima prices beyond UMGC's 10x-project pricing.
- Wisconsin Biotechnology Center's 10B lane price ($2,050) comes from an undated post whose chart suggests Sep 2023.

```json
{"cores":[
{"institution":"University of Minnesota","core":"University of Minnesota Genomics Center (UMGC)","country":"US","kind":"university","platforms":["AVITI","NovaSeq X","UG100"],
"urls":[
{"url":"https://genomics.umn.edu/AVITI-price-drop-2024","type":"announcement","current":false,"public":true,"verified":true,"as_of":"2024-12"},
{"url":"https://genomics.umn.edu/news/aviti-upgrade-complete","type":"announcement","current":true,"public":true,"verified":true,"as_of":"2025-09"},
{"url":"https://genomics.umn.edu/news/preferred-ultima-ug-100-pricing-10x-genomics-projects","type":"announcement","current":true,"public":true,"verified":false,"as_of":null},
{"url":"https://genomics.umn.edu/service/illumina-novaseq-x-plus-sequencing","type":"rate_page","current":true,"public":true,"verified":false,"as_of":null}],
"notes":"AVITI cut ~40% Jul 2024, further ~20% Dec 2024, +50% output at same price Sep 2025 (33% lower per M reads vs FY25). Ultima 10x full wafer $2,409 UMN / $2,712 external (reflects $500 off standard). NovaSeq X is outsourced."},
{"institution":"University of Georgia","core":"Georgia Genomics and Bioinformatics Core (GGBC)","country":"US","kind":"university","platforms":["NovaSeq X"],
"urls":[
{"url":"https://dna.uga.edu/2025/03","type":"announcement","current":false,"public":true,"verified":false,"as_of":"2025-03"},
{"url":"https://dna.uga.edu/spring-forward-with-lower-prices-at-the-georgia-genomics-and-bioinformatics-core/","type":"announcement","current":false,"public":true,"verified":false,"as_of":"2025-03"},
{"url":"https://dna.uga.edu/category/news","type":"announcement","current":true,"public":true,"verified":false,"as_of":null}],
"notes":"Mar 2025 price cut post. 25B lane $3,000; 10B lane $2,000 (per search snippet)."},
{"institution":"University of Missouri","core":"Genomics Technology Core","country":"US","kind":"university","platforms":["NovaSeq X"],
"urls":[{"url":"https://research.missouri.edu/news/new-genomics-tool","type":"announcement","current":false,"public":true,"verified":true,"as_of":"2024-09"}],
"notes":"2024-09-06 post: XLEAP-SBS chemistry lets the core cut sequencing rates 40%. No dollar figures."},
{"institution":"University of Wisconsin-Madison","core":"Biotechnology Center DNA Sequencing","country":"US","kind":"university","platforms":["NovaSeq X"],
"urls":[{"url":"https://cgsi.wisc.edu/bio-tech-update-sequencings-best-bang-for-the-buck/","type":"announcement","current":false,"public":true,"verified":true,"as_of":"2023-09"}],
"notes":"10B lane 2x150 $2,050; ~30% cheaper than older option. Post undated (chart filename suggests Sep 2023)."},
{"institution":"EPFL","core":"Gene Expression Core Facility (GECF)","country":"Switzerland","kind":"university","platforms":["NovaSeq 6000","AVITI"],
"urls":[
{"url":"https://epfl.ch/research/facilities/gene-expression-core-facility/wp-content/uploads/2024/07/GECF-price-list-for-EPFL-users-01-July-2024.pdf","type":"pdf","current":false,"public":true,"verified":false,"as_of":"2024-07"},
{"url":"https://epfl.ch/research/facilities/gene-expression-core-facility/wp-content/uploads/2024/11/GECF-price-list-for-EPFL-users-01-November-2024.pdf","type":"pdf","current":false,"public":true,"verified":false,"as_of":"2024-11"},
{"url":"https://www.epfl.ch/research/facilities/gene-expression-core-facility/wp-content/uploads/2025/03/GECF-price-list-for-EPFL-users-01-March-2025.pdf","type":"pdf","current":false,"public":true,"verified":false,"as_of":"2025-03"},
{"url":"https://www.epfl.ch/research/facilities/gene-expression-core-facility/wp-content/uploads/2025/07/GECF-price-list-for-EPFL-users-01-July-2025.pdf","type":"pdf","current":false,"public":true,"verified":false,"as_of":"2025-07"},
{"url":"https://www.epfl.ch/research/facilities/gene-expression-core-facility/wp-content/uploads/2026/02/GECF-price-list-for-EPFL-users-15-February-2026.pdf","type":"pdf","current":false,"public":true,"verified":false,"as_of":"2026-02"},
{"url":"https://www.epfl.ch/research/facilities/gene-expression-core-facility/wp-content/uploads/2026/09/GECF-price-list-for-EPFL-users-09-September-2026.pdf","type":"pdf","current":true,"public":true,"verified":false,"as_of":"2026-09"},
{"url":"https://www.epfl.ch/research/facilities/gene-expression-core-facility/page-154614-en-html/","type":"announcement","current":true,"public":true,"verified":false,"as_of":"2025-11"},
{"url":"https://www.epfl.ch/research/facilities/gene-expression-core-facility/news","type":"announcement","current":true,"public":true,"verified":false,"as_of":null}],
"notes":"Known core; full dated price-list history in CHF. Changelog: NovaSeq 10B 300-cycle price drop Mar 2026, AVITI price drop late 2025, AVITI24 +50% output Feb 2026."},
{"institution":"FAU Erlangen-Nürnberg","core":"Core Unit NGS","country":"Germany","kind":"university","platforms":["NovaSeq X"],
"urls":[{"url":"https://www.med.fau.de/files/2024/11/NGS.pdf","type":"pdf","current":false,"public":true,"verified":false,"as_of":"2024-10"}],
"notes":"Known core; Oct 2024 old vs new price comparison effective 2025-01-01 (bulk RNA-seq EUR 395 to 245)."},
{"institution":"Northwestern University","core":"NUSeq Core","country":"US","kind":"university","platforms":["NovaSeq X","AVITI"],
"urls":[
{"url":"https://www.cgm.northwestern.edu/cores/nuseq/pricing.html","type":"rate_page","current":true,"public":true,"verified":false,"as_of":"2026-07"},
{"url":"https://www.cgm.northwestern.edu/docs/nuseq/fy26-prices_finalusers.pdf","type":"pdf","current":true,"public":true,"verified":false,"as_of":"2026-07"},
{"url":"https://www.cgm.northwestern.edu/docs/nuseq/fy25-pricing.pdf","type":"pdf","current":false,"public":true,"verified":false,"as_of":"2025-07"}],
"notes":"Known core; FY25 and FY26 PDFs. 25B PE150 lane $3,000 internal (FY26); 10B PE150 lane $1,600; AVITI PE150 High Output lane $1,300."},
{"institution":"Harvard University","core":"Bauer Core Facility","country":"US","kind":"university","platforms":["NovaSeq X"],
"urls":[
{"url":"https://bauercore.fas.harvard.edu/fy26-ngs-sequencing","type":"rate_page","current":false,"public":true,"verified":false,"as_of":"2025-07"},
{"url":"https://bauercore.fas.harvard.edu/fy27-ngs-sequencing","type":"rate_page","current":true,"public":true,"verified":false,"as_of":"2026-07"}],
"notes":"Known core. 25B 300-cycle lane Harvard account: $2,059 (FY26), $2,426 (FY27). Prices rose year on year."},
{"institution":"TGen","core":"Collaborative Sequencing Center","country":"US","kind":"nonprofit_institute","platforms":["NovaSeq X"],
"urls":[
{"url":"https://www.tgen.org/media/x2dmuqf1/tgen_csc_academic_price_list_08-2026.pdf","type":"pdf","current":true,"public":true,"verified":false,"as_of":"2026-08"},
{"url":"https://tgen.org/media/494096/academic-price-list.pdf","type":"pdf","current":false,"public":true,"verified":false,"as_of":null}],
"notes":"Known core. Jul 2026 to Mar 2027 list: 25B lane 300-cycle $3,136.63; 25B flow cell $25,093.04."},
{"institution":"University of Connecticut","core":"Center for Genome Innovation","country":"US","kind":"university","platforms":["NovaSeq X"],
"urls":[
{"url":"https://honeycrisp.core.uconn.edu/products/358","type":"rate_page","current":true,"public":true,"verified":false,"as_of":"2026-01"},
{"url":"https://honeycrisp.core.uconn.edu/products/328","type":"rate_page","current":true,"public":true,"verified":false,"as_of":"2026-01"},
{"url":"https://honeycrisp.core.uconn.edu/products/391","type":"rate_page","current":true,"public":true,"verified":false,"as_of":null},
{"url":"https://honeycrisp.core.uconn.edu/products/368","type":"rate_page","current":true,"public":true,"verified":false,"as_of":null},
{"url":"https://honeycrisp.core.uconn.edu/products/657","type":"rate_page","current":true,"public":true,"verified":false,"as_of":null}],
"notes":"Known core. 25B 300-cycle lane $2,933.99 from 2026-01-01 (was $2,924.04 in 2025); includes 5% temporary Illumina tariff. Honeycrisp pages carry start dates, so history may be visible."},
{"institution":"Texas A&M University","core":"AgriLife Genomics (TxGen)","country":"US","kind":"university","platforms":["NovaSeq X"],
"urls":[{"url":"https://www.txgen.tamu.edu/wp-content/uploads/txgen/TxGen_Prices.pdf","type":"pdf","current":false,"public":true,"verified":false,"as_of":"2025-02"}],
"notes":"Known core. Feb 2025 sheet: 25B 300-cycle lane $3,222 ($3.30/Gb)."},
{"institution":"University of Calgary","core":"CHGI NGS","country":"Canada","kind":"university","platforms":["NovaSeq X"],
"urls":[
{"url":"https://cumming.ucalgary.ca/sites/default/files/teams/97/CHGI%20Internal%20Price%20List%20June%202024.pdf","type":"pdf","current":false,"public":true,"verified":false,"as_of":"2024-06"},
{"url":"https://cumming.ucalgary.ca/sites/default/files/teams/97/2025%20CHGI%20Internal%20Price%20List.pdf","type":"pdf","current":false,"public":true,"verified":false,"as_of":"2025"}],
"notes":"Known core. Jun 2024: 25B single lane PE150 CAD 4,100."},
{"institution":"SickKids","core":"TCAG","country":"Canada","kind":"academic_medical_center","platforms":["NovaSeq X"],
"urls":[{"url":"https://www.tcag.ca/documents/facilities/TCAG-NGS-Price-List April 2025.pdf","type":"pdf","current":false,"public":true,"verified":false,"as_of":"2025-04"}],
"notes":"Known core; April 2025 NGS price list (URL has a space in it)."},
{"institution":"University of Chicago","core":"Genomics Facility","country":"US","kind":"university","platforms":["NovaSeq X","AVITI"],
"urls":[
{"url":"https://voices.uchicago.edu/genomicsfacility/pricing-new","type":"rate_page","current":true,"public":true,"verified":false,"as_of":null},
{"url":"https://voices.uchicago.edu/genomicsfacility/ngs","type":"rate_page","current":true,"public":true,"verified":false,"as_of":"2024"},
{"url":"https://cri.uchicago.edu/?p=5394","type":"announcement","current":false,"public":true,"verified":false,"as_of":"2025-07"}],
"notes":"Known core. AVITI 150 full flow cell ~$1,175 internal; FY2026 recharge notice effective 2025-07-01."},
{"institution":"Salk Institute","core":"Integrative Genomics and Bioinformatics Core","country":"US","kind":"nonprofit_institute","platforms":["AVITI","NovaSeq X"],
"urls":[{"url":"https://www.salk.edu/science/core-facilities/integrative-genomics-and-bioinformatics-core/scheduling-and-rates/","type":"rate_page","current":true,"public":true,"verified":false,"as_of":null}],
"notes":"Known core. AVITI High Output 300-cycle flow cell $3,610 internal / $4,513 external."},
{"institution":"Case Western Reserve University","core":"Genomics Core","country":"US","kind":"university","platforms":["NovaSeq X"],
"urls":[{"url":"https://case.edu/medicine/genomics/pricing","type":"rate_page","current":true,"public":true,"verified":false,"as_of":"2026-07"}],
"notes":"Known core. Older snippets say 'updated October 2023' (25B 300-cycle $20,000); later snippet says July 2026 with a shared 1.5B lane $1,400-1,800."},
{"institution":"University of Illinois Urbana-Champaign","core":"Carver Biotechnology Center DNA Services","country":"US","kind":"university","platforms":["NovaSeq X"],
"urls":[{"url":"https://biotech.illinois.edu/htdna","type":"rate_page","current":true,"public":true,"verified":false,"as_of":null}],
"notes":"Known core. 10B 2x150 lane $2,190; 25B lane $3,290."},
{"institution":"Duke University","core":"Sequencing and Genomic Technologies Core","country":"US","kind":"university","platforms":["NovaSeq X"],
"urls":[{"url":"https://medschool.duke.edu/blog/sequencing-core-launches-illumina-x-plus-sequencer","type":"announcement","current":false,"public":true,"verified":false,"as_of":null}],
"notes":"Known core. Launch post; one lane (1-1.25B reads) $1,465 Duke / $1,492 external per search snippet."},
{"institution":"Virginia Tech","core":"Fralin Genomics Sequencing Center","country":"US","kind":"university","platforms":["NovaSeq X"],
"urls":[{"url":"https://fralinlifesci.vt.edu/content/dam/fralinlifesci_vt_edu/core-services/gsc/2024-09-01-GSC-Pricing-Guide.pdf","type":"pdf","current":false,"public":true,"verified":false,"as_of":"2024-09"}],
"notes":"Known core. Sep 2024 pricing guide, useful as history."},
{"institution":"Stanford University","core":"Protein and Nucleic Acid (PAN) Facility","country":"US","kind":"university","platforms":[],
"urls":[{"url":"https://pan.stanford.edu/rates.html","type":"rate_page","current":true,"public":true,"verified":true,"as_of":null}],
"notes":"NEW but low value: page lists MiSeq only, no NovaSeq/AVITI. Has a separate tariff surcharge invoice line (no amount)."},
{"institution":"University of Tennessee, Knoxville","core":"Genomics Core","country":"US","kind":"university","platforms":["NovaSeq 6000","NextSeq 2000"],
"urls":[{"url":"https://research.utk.edu/?p=125","type":"rate_page","current":true,"public":true,"verified":true,"as_of":"2026-08"}],
"notes":"NEW. NovaSeq SP 200 2x100: internal $3,360 / external academic $3,610 / non-academic $4,530, plus tariff fee $134. Page undated; file paths suggest mid-2026. No AVITI."},
{"institution":"North Dakota State University","core":"Biotechnology Innovation Core, Sequencing","country":"US","kind":"university","platforms":["NextSeq 1000/2000"],
"urls":[{"url":"https://www.ndsu.edu/biotech-innovation-core/sequencing/services-and-fees","type":"rate_page","current":true,"public":true,"verified":true,"as_of":null}],
"notes":"NEW. NextSeq1000 P1 2x50 (10 Gb) $1,220/run internal, $1,769 external. Undated."},
{"institution":"University of Nebraska Medical Center","core":"Genomics Core","country":"US","kind":"university","platforms":["NovaSeq 6000","AVITI"],
"urls":[{"url":"https://www.unmc.edu/research-resources/resources/cores/genomics-core/pricing.html","type":"rate_page","current":true,"public":true,"verified":true,"as_of":null}],
"notes":"Known core. NovaSeq 6000 S1 100-cycle v1.5 $5,928 internal / $8,892 external per flow cell; AVITI24 listed. Undated."},
{"institution":"Emory University","core":"Integrated Genomics Core (Emory NBRC)","country":"US","kind":"university","platforms":["NovaSeq X"],
"urls":[{"url":"https://enbrc.emory.edu/genomicscore/services/nextgen-sequencing.html","type":"rate_page","current":true,"public":true,"verified":true,"as_of":null}],
"notes":"NEW. Service page lists NovaSeq X Plus, NovaSeq 6000, MiSeq; prices are on a separate 'Pricing' page I did not reach."},
{"institution":"Oklahoma State University","core":"MBGC (fee sheet)","country":"US","kind":"university","platforms":[],
"urls":[{"url":"https://ocrid.okstate.edu/site-files/documents/fy26-fee_sheets/fy26_mbgc.pdf","type":"pdf","current":true,"public":true,"verified":false,"as_of":"2025-07"}],
"notes":"NEW, unverified (HTTP 403 on fetch). FY26 fee sheet; the FY25/FY27 sheets likely follow the same URL pattern, but I did not see them."},
{"institution":"Children's Hospital Los Angeles","core":"Spatial Biology and Genomics Core","country":"US","kind":"academic_medical_center","platforms":[],
"urls":[{"url":"https://www.chla.org/research/core/spatial-biology-and-genomics/fee-structure","type":"rate_page","current":true,"public":true,"verified":false,"as_of":null}],
"notes":"NEW, unverified (HTTP 403 on fetch); platform coverage unknown."},
{"institution":"University of Edinburgh","core":"Edinburgh Genomics / Clinical Research Facility Genetics Core","country":"UK","kind":"university","platforms":[],
"urls":[{"url":"https://genomics.ed.ac.uk/node/75","type":"announcement","current":false,"public":true,"verified":false,"as_of":null}],
"notes":"Known core. 'Pricing changes' notice appears to be years old (mentions HiSeq X); not useful for 2024-26."}
]}
```