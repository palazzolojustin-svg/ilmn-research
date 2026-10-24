Only 4 new cores in states A–M are confirmed, short of the 15–30 target. Search results were dominated by cores already on your list, and many other cores publish no public prices.

**Confirmed new cores**
- **Arizona State University:** the page shows NovaSeq X 10B and NextSeq 2000 P1–P4 prices but no AVITI. It has no date and no PDFs. Sample: "NovaSeq X 10B 300-cycle $1,950/run (ASU and nonprofit/academic); NextSeq 2000 P1 2x150 $1,530 ASU / $2,204 nonprofit".
- **UCLA Broad Stem Cell Research Center Sequencing Core:** this is a different core from the UCLA TCGB you already have. It has a public table with no date shown. Sample: "NovaSeq X Plus 10B 2x150 internal $1,962 / ext non-profit $2,234 / ext $2,524".
- **University of Florida ICBR NextGen DNA Sequencing:** the lab-services page showed "Rates Updated: 07/01/2026" and lists NovaSeq X prices. I could not tell which of the three price columns is which. Sample: "1.5B 2x50 full flow cell $2,546.27 / $3,055.52 / $3,310.15". The page is very long (284K characters), and I did not read the first 100K characters.
- **Mass General Brigham NextGen Core:** the search result says the page covers NextSeq 2000 P1–P4, with internal, external academic and industry columns (P3 SR100 about $3,666 internal). I could not open the page (HTTP 404), so it is unverified. The URL came from a search result.

**Found but poor fit**
- **UAB Heflin Genomics Core:** public per-million-read pricing, but only NextSeq500/MiSeq, so no target platform. Sample: "SE75 $4.50/M reads".
- **Georgia Tech:** pricing is on sums.gatech.edu and covers older platforms only. I did not open it.
- **K-State CEZID:** per-sample pricing with no instrument named (updated 1/29/26).
- **University of Kentucky:** the 2022–23 NovaSeq handout appeared in search but returned 404 when opened. It is historical only.
- **University of Miami, Mayo, UAMS, Stanford, Emory, Tufts, Purdue, Iowa State, City of Hope, Jackson Laboratory, Van Andel, Broad, WashU GTAC, UMass Chan and Maryland IGS:** I found no public prices. Miami says "contact us" and Mayo returned 403.
- **UMass Boston:** its pricing page returned 404.

```json
{"cores": [
{"institution": "Arizona State University", "core": "Genomics Core (NGS, TGen sequencing runs)", "country": "US", "kind": "university", "platforms": ["NovaSeq X", "NextSeq 2000"],
 "urls": [{"url": "https://cores.research.asu.edu/genomics/rates", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": null}],
 "notes": "NovaSeq X 10B 300-cycle $1,950/run (ASU and nonprofit/academic); NextSeq 2000 P1 2x150 $1,530 ASU / $2,204 nonprofit. No AVITI. Undated page (images suggest Sep 2025 upload), no PDFs; use Wayback for history."},
{"institution": "University of California, Los Angeles", "core": "Broad Stem Cell Research Center Sequencing Core (High-Throughput Sequencing Core; distinct from TCGB)", "country": "US", "kind": "university", "platforms": ["NovaSeq X"],
 "urls": [
  {"url": "https://cores.ucla.edu/cores/cellular-molecular-analysis/sequencing-core", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": null},
  {"url": "https://stemcell.ucla.edu/high-throughput-sequencing", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": null}],
 "notes": "NovaSeq X Plus 10B 2x150 lane internal $1,962 / ext non-profit $2,234 / ext $2,524; 1.5B 2x50 per lane $1,377 / $1,874 (stemcell.ucla.edu page, footer 2024). Undated pages."},
{"institution": "University of Florida", "core": "ICBR NextGen DNA Sequencing Shared Resource", "country": "US", "kind": "university", "platforms": ["NovaSeq X"],
 "urls": [
  {"url": "https://biotech.ufl.edu/lab-services/", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": "2026-07"},
  {"url": "https://biotech.ufl.edu/next-gen-dna/resources/", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": null},
  {"url": "https://biotech.ufl.edu/icbr-enhances-dna-sequencing-capabilities-with-the-illumina-novaseq-x-plus/", "type": "announcement", "current": false, "public": true, "verified": false, "as_of": null},
  {"url": "https://biotech.ufl.edu/new-instruments-in-the-icbr-ngs-shared-resource-will-lower-dna-sequencing-costs-for-uf-investigators/", "type": "announcement", "current": false, "public": true, "verified": false, "as_of": null}],
 "notes": "Rates Updated 07/01/2026. NovaSeq X 1.5B 2x50 full FC $2,546.27 / $3,055.52 / $3,310.15 (UF / non-profit / commercial; column mapping unclear). Announcements say X Plus cut fees by up to 40-60% (undated in my view). Page is very long (284K characters); I did not read its first 100K characters."},
{"institution": "Massachusetts General Hospital (Mass General Brigham)", "core": "MGH Next-generation Sequencing Core", "country": "US", "kind": "academic_medical_center", "platforms": ["NextSeq 2000"],
 "urls": [{"url": "https://nextgen.mgh.harvard.edu/Pricing.html", "type": "rate_page", "current": true, "public": true, "verified": false, "as_of": null}],
 "notes": "URL appeared in search results; my direct fetch returned 404 (may need retry or different casing). Search snippet: P3 SR100 about $3,666 internal / $5,279 external academic / $6,598 industry. Only NextSeq 2000/MiSeq, no NovaSeq."},
{"institution": "University of Alabama at Birmingham", "core": "Heflin Center for Genomic Science, Genomics Core Lab", "country": "US", "kind": "university", "platforms": ["NextSeq 500 (legacy)"],
 "urls": [{"url": "https://www.uab.edu/hcgs/hcgspricing", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": null}],
 "notes": "Single End 75bp $4.50/million reads. No NovaSeq/AVITI/NextSeq 2000, so likely out of scope; low priority."},
{"institution": "Georgia Institute of Technology", "core": "High Throughput DNA Sequencing Core", "country": "US", "kind": "university", "platforms": ["NextSeq", "MiSeq"],
 "urls": [{"url": "https://research.gatech.edu/bio/research/core-facilities/high-throughput-dna-sequencing-core/services", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": null}],
 "notes": "Services page links to pricing on sums.gatech.edu (DepartmentId=46 NextSeq-class, DepartmentId=31 HiSeq 2500); I did not open those links. Platforms appear to be older; no NovaSeq/AVITI found."},
{"institution": "Kansas State University", "core": "CEZID (Vet Med) NGS Services", "country": "US", "kind": "university", "platforms": [],
 "urls": [{"url": "https://www.k-state.edu/cezid/research-core-facilities/NGSservices.html", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": "2026-01"}],
 "notes": "Per-sample pricing (e.g. WGS $98 internal / $149 external) with no instrument named; updated 1/29/26. Weak fit for $/Gb tracking."},
{"institution": "University of Kentucky", "core": "UK HealthCare Oncogenomics Shared Resource Facility (NGS Illumina Sequencing)", "country": "US", "kind": "academic_medical_center", "platforms": ["NovaSeq 6000"],
 "urls": [{"url": "https://WWW.UKHEALTHCARE.UKY.EDU/sites/default/files/2022-11/OG%20SRF_NGS_Illumina%20Sequencing%202022-2023%20Handout.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2022-11"}],
 "notes": "Seen in search results only; a fetch returned 404. Per search snippet (not verified): S4 300-cycle $17,132 (10,000M reads), S1 300-cycle $6,346 (2022-23). Historical only; no current version located."}
]}
```

Sources:
- https://cores.research.asu.edu/genomics/rates
- https://cores.ucla.edu/cores/cellular-molecular-analysis/sequencing-core
- https://stemcell.ucla.edu/high-throughput-sequencing
- https://biotech.ufl.edu/lab-services/
- https://www.uab.edu/hcgs/hcgspricing
- https://research.gatech.edu/bio/research/core-facilities/high-throughput-dna-sequencing-core/services
- https://www.k-state.edu/cezid/research-core-facilities/NGSservices.html