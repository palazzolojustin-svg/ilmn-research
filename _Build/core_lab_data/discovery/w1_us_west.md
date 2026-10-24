Only a handful of cores in this slice publish usable sequencing prices: UC San Diego IGM, UCLA TCGB, UC Riverside, UCSF CAT, UC Davis and the University of Oregon GC3F. I found 8 cores in total, short of the 15–30 target. Several candidates either have no public sequencing prices or I couldn't reach their pages.

- **Not verified by me:** UCSF CAT and UC Davis returned HTTP 403 when I fetched them. Their pricing content comes from search-result snippets only. The UC Davis and Oregon State fee pages did not surface a NovaSeq X or NextSeq row, so I haven't confirmed their coverage.
- **Platform coverage:** I found no public AVITI or Ultima prices in this slice. Scripps runs an AVITI but posts no prices. GC3F lists NovaSeq 6000 and NextSeq 2000 only.
- **No public sequencing price page found:** Stanford, UCSB, UC Santa Cruz, USC, Caltech, City of Hope, Cedars-Sinai, UW Northwest Genomics Center, Washington State, University of Hawaii, OHSU MPSSR and UC Irvine GRT Hub. UC Irvine and OHSU most likely price through iLab, which is login-gated. The WSU page redirected to a URL that returned 404.
- **Search-tool figures to treat with caution:**
  - The search summaries gave UCLA's 10B and 25B 300-cycle lanes as $1,962 and $3,168, but those same figures appear for UC Riverside's internal rate. Check which core they belong to.
  - UCLA's 2024 sheet (Mar 2024, rev. Jun 2024) shows 25B 300-cycle at $3,168 internal.
  - UCLA's July 2026 page shows external rates only, and its internal rates sit in a Box link.
- **UCSD IGM:** The 2025 PDF lists NovaSeq X Plus 25B 300-cycle at $2,800 UC and $3,836 outside. The 2026 PDF and a 2026 image rate card are on the IGM rates page, but I couldn't read their prices.
- **UC Riverside:** The page is FY24-25, effective 2025-04-17, and lists NovaSeq X Plus, NextSeq 2000 and AVITI.

```json
{"cores": [
{"institution": "UC San Diego", "core": "IGM Genomics Center", "country": "US", "kind": "university",
 "platforms": ["NovaSeq X"],
 "urls": [
  {"url": "https://igm.ucsd.edu/genomics/rates", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": "2026-01"},
  {"url": "https://igm.ucsd.edu/sites/default/files/docs/IGM%20Rates%202026%20New%20IDC%20Chloes%20edits_0.pdf", "type": "pdf", "current": true, "public": true, "verified": false, "as_of": "2026-01"},
  {"url": "https://igm.ucsd.edu/sites/default/files/docs/2026%20rates%20flow%20cell%20fix.png", "type": "rate_page", "current": true, "public": true, "verified": false, "as_of": "2026-01"},
  {"url": "https://igm.ucsd.edu/sites/default/files/docs/IGM%20Rates%202025%20New%20IDC.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2025-01"},
  {"url": "https://igm.ucsd.edu/node/123", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": "2026-01"}],
 "notes": "2025 PDF (seen in search): NovaSeq X Plus 25B 300-cycle lane UC $2,800 / outside $3,836. The 2026 PDF and image were not read. The node/123 page shows the NovaSeq X Plus pricing as an image, labelled 'proposed, subject to rates committee'."},
{"institution": "UCLA", "core": "Technology Center for Genomics & Bioinformatics (TCGB)", "country": "US", "kind": "academic_medical_center",
 "platforms": ["NovaSeq X", "NovaSeq 6000"],
 "urls": [
  {"url": "https://www.uclahealth.org/departments/pathology/research-services/technology-center-genomics-bioinformatics-tcgb/pricing", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": "2026-07"},
  {"url": "https://uclahs.app.box.com/s/ger1oivcyn9c1or940dsjha2pvtz1tnn", "type": "pdf", "current": true, "public": true, "verified": false, "as_of": "2026-07"},
  {"url": "https://uclahealth.org/sites/default/files/documents/48/ucla-tcgb-rates-publication-revised-6-18-2024.pdf?f=d042f1b9", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2024-06"},
  {"url": "https://www.uclahealth.org/sites/default/files/documents/0f/ucla-tcgb-rates-publication-revised-3-12-2024-1.pdf?f=b82588c6", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2024-03"},
  {"url": "https://www.uclahealth.org/sites/default/files/documents/9e/ucla-tcgb-rates-publication-8-1-23-final-version.pdf?f=df27dbc8", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2023-08"},
  {"url": "https://www.uclahealth.org/sites/default/files/documents/UCLA%20TCGB%20rates%20for%20publication%207-1-22.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2022-07"},
  {"url": "https://www.uclahealth.org/sites/default/files/documents/NewApprovedRatesEffective11012019.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2019-11"}],
 "notes": "Gives history across 2019-2026 sheets. The July 2026 page shows NovaSeq X Plus 1.5B/5B/10B/25B flow cells at external rates; it does not list NovaSeq 6000, AVITI or Ultima. Internal rates are in the Box link. 2024 sheets (search snippet): 25B 300-cycle lane $3,168 internal, $3,538 external non-profit, $3,933 for-profit; the 2024 sheets carry internal, JCCC and external columns."},
{"institution": "UC Riverside", "core": "Genomics Core Facility, Institute for Integrative Genome Biology (IIGB)", "country": "US", "kind": "university",
 "platforms": ["NovaSeq X", "NextSeq 2000", "AVITI"],
 "urls": [
  {"url": "https://genomics.iigb.ucr.edu/rates", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": "2025-04"}],
 "notes": "FY24-25 schedule, effective 2025-04-17. Sample line (fetched): MiSeq 150bp lane $1,388 internal UC / $1,787.74 external educational / $2,514.02 commercial. The page also lists NovaSeq X Plus 10B and 25B lanes (search snippet: 25B 300-cycle $3,168 internal UC), plus AVITI, Revio and Nanopore. No older versions are linked, and the page may be stale for FY26."},
{"institution": "UC San Francisco", "core": "Center for Advanced Technology (CAT)", "country": "US", "kind": "university",
 "platforms": ["NovaSeq X", "AVITI"],
 "urls": [
  {"url": "https://cat.ucsf.edu/sequencing", "type": "rate_page", "current": true, "public": true, "verified": false, "as_of": null},
  {"url": "https://cat.ucsf.edu/node/706", "type": "rate_page", "current": true, "public": true, "verified": false, "as_of": null},
  {"url": "https://cat.ucsf.edu/node/36", "type": "rate_page", "current": true, "public": true, "verified": false, "as_of": null}],
 "notes": "Both fetches returned 403 to me, so everything here is from search snippets. A snippet showed 25B 300-cycle lane $2,551 UC rate and 10B 300-cycle $1,439 UC rate. An older snapshot showed 10B 300-cycle at $1,724 internal (Sep 2024). Surcharges for non-UC and for-profit users appear to have changed between snapshots (+26%/+38.6% older, +33%/+46.3% newer). Check whether an AVITI listing exists."},
{"institution": "UC Davis", "core": "Genome Center DNA Technologies and Expression Analysis Core", "country": "US", "kind": "university",
 "platforms": ["NovaSeq X", "AVITI"],
 "urls": [
  {"url": "https://dnatech.ucdavis.edu/uc-prices/", "type": "rate_page", "current": true, "public": true, "verified": false, "as_of": "2026-03"},
  {"url": "https://dnatech.ucdavis.edu/academicnon-profit-prices", "type": "rate_page", "current": true, "public": true, "verified": false, "as_of": null},
  {"url": "https://dnatech.genomecenter.ucdavis.edu/?p=150", "type": "rate_page", "current": true, "public": true, "verified": false, "as_of": null},
  {"url": "https://dnatech.genomecenter.ucdavis.edu/?p=4468", "type": "rate_page", "current": true, "public": true, "verified": false, "as_of": null},
  {"url": "https://dnatech.ucdavis.edu/faq/what-are-you-prices", "type": "rate_page", "current": true, "public": true, "verified": false, "as_of": null}],
 "notes": "Fetches returned 403, so I could not confirm NovaSeq X rows. The UC price page says 'new prices as of March 2026'. Three tiers: UC, academic/non-profit, industry. The ?p= URLs are search hits and their content is unconfirmed. This core is the most likely to carry older dated versions and the platforms most worth chasing, so check manually."},
{"institution": "University of Oregon", "core": "Genomics & Cell Characterization Core Facility (GC3F)", "country": "US", "kind": "university",
 "platforms": ["NovaSeq 6000", "NextSeq 2000"],
 "urls": [
  {"url": "https://gc3f.uoregon.edu/rates", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": null},
  {"url": "https://research.uoregon.edu/sites/research1.uoregon.edu/files/2020-10/GC3F%20FY21%20Rate%20Memo%20(4.16.20).pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2020-04"},
  {"url": "https://uoresearch.uoregon.edu/files/2023-07/GC3%20Core%20Facility.docx", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2024-09"}],
 "notes": "NovaSeq 6000 S4 300-cycle PE150 lane: $5,070 internal / $6,903 external. NextSeq 2000 P4 300-cycle: $4,228 internal / $5,496 external. The page shows no NovaSeq X or AVITI. A search snippet showed older S4 prices ($4,852 internal), so the page has changed over time and the page date is not stated. A 2022 announcement (S4 300-cycle $4,612 internal, effective 2022-07) was seen in a search snippet, but I did not get its URL. The FY21 memo is the oldest document I found. The .docx is dated 2024-09."},
{"institution": "Oregon State University", "core": "Center for Quantitative Life Sciences (CQLS) Genomics Core", "country": "US", "kind": "university",
 "platforms": ["NextSeq 2000"],
 "urls": [
  {"url": "https://cqls.oregonstate.edu/cqls-service-fees", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": "2026-11"},
  {"url": "https://cqls.oregonstate.edu/cqls-service-fees/csv?page&_format=csv", "type": "spreadsheet", "current": true, "public": true, "verified": false, "as_of": "2026-11"},
  {"url": "https://cqls.oregonstate.edu/cqls-service-fees/xlsx?page&_format=xlsx", "type": "spreadsheet", "current": true, "public": true, "verified": false, "as_of": "2026-11"},
  {"url": "https://blogs.oregonstate.edu/cqls/category/sequencing/", "type": "announcement", "current": true, "public": true, "verified": false, "as_of": null}],
 "notes": "The fee table is public; genomics fees are labelled 'effective November 1, 2026'. Page 1 shows no sequencing rows, and the filter lists NextSeq and MiSeq i100 sequencing. The CSV/XLSX download URLs are inferred from the page's links on the same site, so their output wasn't checked. The core runs NextSeq 2000 (P1-P3) and MiSeq i100, with no NovaSeq X or AVITI seen. The blog category may carry price-change posts."},
{"institution": "Scripps Research", "core": "Genomics Core (La Jolla)", "country": "US", "kind": "nonprofit_institute",
 "platforms": ["AVITI", "NextSeq 2000"],
 "urls": [
  {"url": "https://www.scripps.edu/science-and-medicine/cores-and-services/genomics-ca/index.html", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": null}],
 "notes": "The page lists the Element AVITI and an Illumina NextSeq 2000 but posts no prices (only a $125 external AWS account fee). The order form is login-gated ELAN. Low priority."}
]}
```

Sources:
- [UCSD IGM Rates 2025 PDF](https://igm.ucsd.edu/sites/default/files/docs/IGM%20Rates%202025%20New%20IDC.pdf)
- [UCLA TCGB pricing](https://www.uclahealth.org/departments/pathology/research-services/technology-center-genomics-bioinformatics-tcgb/pricing)
- [UCR IIGB rates](https://genomics.iigb.ucr.edu/rates)
- [UCSF CAT service rates](https://cat.ucsf.edu/node/706)
- [UC Davis UC prices](https://dnatech.ucdavis.edu/uc-prices/)
- [UO GC3F rates](https://gc3f.uoregon.edu/rates)
- [OSU CQLS service fees](https://cqls.oregonstate.edu/cqls-service-fees)
- [Scripps Genomics Core](https://www.scripps.edu/science-and-medicine/cores-and-services/genomics-ca/index.html)