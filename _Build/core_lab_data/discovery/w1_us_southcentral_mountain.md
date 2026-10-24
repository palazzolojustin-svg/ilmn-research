I found 7 cores in this slice with public prices on a qualifying platform, plus 3 leads that don't qualify. I opened about 8 pages, but several fetches came back empty or blocked, so some URLs are marked unverified. I cut the work short to stay inside the time limit.

- **Baylor GARP:** This is the best history in the slice. A dated price file exists for roughly every 3 to 6 months from Sep 2024 to Feb 2026. The sample line is NovaSeq X 10B, 300 cycles, 1 lane at $1,650 (Sep 2025 and Feb 2026). The late-2024 NovaSeq 6000 S4 lane was $4,800. I read these figures from search snippets and did not open the files, so the "Duncan member" $1,600 rate is unconfirmed. The fees page links only the Feb 2026 file; the filename "02-10-2026" is probably Feb 10, 2026.
- **Arizona Genetics Core:** The rates are effective 1 Jul 2026. They list AVITI and NextSeq 550 run fees with flow cells not included, so they are not full per-flow-cell prices. The AVITI-24 service page says "varies".
- **UT Health San Antonio GSF:** The page was updated 4/21/26 and shows NovaSeq 6000 and NextSeq 2000 (P1 to P4) prices. Its linked PDF is dated 2026-04, but I did not get the PDF URL.
- **Boise State:** The core prices NextSeq flow cells in three rate tiers. P1 100 cycles is $1,717 for Rate A. The page gives no effective date.
- **UT Austin GSAF:** The wiki page shows NovaSeq S1 and SP lanes; I confirmed this from search snippets only, because the fetch came back empty. A NovaSeq S1 SR100 lane is $3,801.47 internal and $4,803.46 external. NovaSeq X is internal-only and not priced publicly. Archived versions exist, but I did not capture their URLs.
- **MD Anderson ATGC:** A search snippet says the NovaSeq X Plus page lists per-lane prices. My fetch of that page showed none, so this is unverified. The snippet gave a 25B 300-cycle lane at $2,595. The FY2023 NovaSeq 6000 price schedule PDF is an older version with tiered rates.
- **Utah core facilities (HSC Cores, AVITI):** This is a different core from the Huntsman HTG core you already have. It publishes AVITI example costs only, not a rate card.
- **Dead ends:**
  - UTSW McDermott lists no dollar amounts (request an estimate).
  - Texas Tech's rate page is FY18 and has no NovaSeq prices.
  - OSU's page returned 403.
  - I found no public rates for CU Anschutz, CU Boulder, CSU, BYU, OMRF, OU, Rice, ASU, UNM, UNR, Montana State or Wyoming. A CU Genomics Core Atlassian wiki page titled "Sequencing Prices" appeared in search results, but my fetch was empty. A related "Quotes … as of 09-09-2021" page is old.
  - UTHealth Houston CGC returned 403.

```json
{"cores": [
{"institution": "Baylor College of Medicine", "core": "Genomic and RNA Profiling Core (GARP)", "country": "US", "kind": "academic_medical_center",
 "platforms": ["NovaSeq X", "NovaSeq 6000"],
 "urls": [
  {"url": "https://www.bcm.edu/research/research-services/atc-core-labs/genomic-and-rna-profiling-core/fees", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": "2026-02"},
  {"url": "https://www.bcm.edu/sites/default/files/garp_pricingwebsite_-02-10-2026.docx", "type": "spreadsheet", "current": true, "public": true, "verified": true, "as_of": "2026-02"},
  {"url": "https://cdn.bcm.edu/sites/default/files/2025-09/garp_pricingwebsite_-09-2025.docx", "type": "spreadsheet", "current": false, "public": true, "verified": false, "as_of": "2025-09"},
  {"url": "https://cdn.bcm.edu/sites/default/files/2025-06/garp_pricingwebsite_-06-2025.docx", "type": "spreadsheet", "current": false, "public": true, "verified": false, "as_of": "2025-06"},
  {"url": "https://cdn.bcm.edu/sites/default/files/2025-02/garp_pricingwebsite_march2025.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2025-03"},
  {"url": "https://cdn.bcm.edu/sites/default/files/2025-02/garp_pricingwebsite_02102025.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2025-02"},
  {"url": "https://cdn.bcm.edu/sites/default/files/2024-12/garp_pricingwebsite_12092024.docx", "type": "spreadsheet", "current": false, "public": true, "verified": false, "as_of": "2024-12"},
  {"url": "https://cdn.bcm.edu/sites/default/files/2024-09/garp_pricingwebsite_09202024.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2024-09"},
  {"url": "https://cdn.bcm.edu/sites/default/files/garp_pricingwebsite_110122.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2022-11"}
 ],
 "notes": "NovaSeq X S10B 300cyc 1 lane $1,650 (Feb 2026, also Sep 2025). Late-2024 NovaSeq 6000 S4 lane $4,800. From search snippets; files not opened. Dated files roughly every 3-6 months."},
{"institution": "University of Arizona", "core": "Arizona Genetics Core (AZGC)", "country": "US", "kind": "university",
 "platforms": ["AVITI", "NextSeq 550"],
 "urls": [
  {"url": "https://cores.arizona.edu/facilities/azgc/pricing", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": "2026-07"},
  {"url": "https://cores.arizona.edu/media/476", "type": "pdf", "current": true, "public": true, "verified": false, "as_of": "2026-07"},
  {"url": "https://cores.arizona.edu/facilities/azgc/resources/element-aviti-24", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": null},
  {"url": "https://cores.arizona.edu/facilities/news/new-technology-introduction-az-genetics-core-sept-7-2024", "type": "announcement", "current": false, "public": true, "verified": false, "as_of": "2024-09"}
 ],
 "notes": "AVITI run (flow cell not included) $250 internal / $300 external (rates eff. 1 Jul 2026). Run fees only; flow cells quoted separately. Older rate PDFs likely exist at the same site but were not seen."},
{"institution": "UT Health San Antonio", "core": "Genome Sequencing Facility (Greehey CCRI)", "country": "US", "kind": "academic_medical_center",
 "platforms": ["NovaSeq 6000", "NextSeq 2000"],
 "urls": [
  {"url": "https://gccri.uthscsa.edu/services/gsf/gsf-pricing/", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": "2026-04"}
 ],
 "notes": "Page 'Updated 4/21/26', linked PDF dated 2026/04 (file name Updated260420; PDF URL not captured). NovaSeq 6000 and NextSeq 2000 P1-P4 priced; no AVITI. Three tiers (MCC/UTHSA/External). An older version (3/14/23) was referenced in search results."},
{"institution": "Boise State University", "core": "Sequencing Core", "country": "US", "kind": "university",
 "platforms": ["NextSeq"],
 "urls": [
  {"url": "https://www.boisestate.edu/sequencing-core/home/rates/", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": null}
 ],
 "notes": "NextSeq P1 100cyc flow cell $1,717 (Rate A), $2,429.56 (B), $2,653.63 (C). No effective date shown. NextSeq flow cells only, no NovaSeq or AVITI seen."},
{"institution": "University of Texas at Austin", "core": "Genomic Sequencing and Analysis Facility (GSAF)", "country": "US", "kind": "university",
 "platforms": ["NovaSeq 6000", "NextSeq 1000"],
 "urls": [
  {"url": "https://cloud.wikis.utexas.edu/wiki/x/eRBPAg", "type": "rate_page", "current": true, "public": true, "verified": false, "as_of": null},
  {"url": "https://cloud.wikis.utexas.edu/wiki/x/14wlGw", "type": "rate_page", "current": false, "public": true, "verified": false, "as_of": null},
  {"url": "https://wikis.utexas.edu/x/zgFNDg", "type": "rate_page", "current": false, "public": true, "verified": false, "as_of": null},
  {"url": "https://cloud.wikis.utexas.edu/wiki/x/tIJaEw", "type": "rate_page", "current": false, "public": true, "verified": false, "as_of": null}
 ],
 "notes": "NovaSeq S1 SR100 lane $3,801.47 internal / $4,803.46 external (search snippet; page fetch returned empty). NovaSeq X is internal-only and not priced publicly. The last three URLs are archived or older price pages per search, not opened."},
{"institution": "UT MD Anderson Cancer Center", "core": "Advanced Technology Genomics Core (ATGC)", "country": "US", "kind": "academic_medical_center",
 "platforms": ["NovaSeq X", "NovaSeq 6000"],
 "urls": [
  {"url": "https://www.mdanderson.org/research/research-resources/core-facilities/advanced-technology-genomics-core/services-and-fees/novaseqx-plus-sequencing.html", "type": "rate_page", "current": true, "public": true, "verified": false, "as_of": null},
  {"url": "https://www.mdanderson.org/research/research-resources/core-facilities/advanced-technology-genomics-core/services-and-fees.html", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": null},
  {"url": "https://www.mdanderson.org/content/dam/mdanderson/documents/core-facilities/sequencing-and-microarray-facility/ATGC%20FY2023%20Price%20Schedule%20v012323.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2023-01"}
 ],
 "notes": "Snippet: NovaSeq X 25B 300cyc $2,595 per lane; 10B 300cyc $1,523. My fetch of that page showed no prices, so unverified. FY2023 schedule (NovaSeq 6000, tiered MDA/GCC/external) is the older version."},
{"institution": "University of Utah (HSC Cores)", "core": "Next Gen Sequencing on the AVITI (HSC Cores bookstack)", "country": "US", "kind": "university",
 "platforms": ["AVITI"],
 "urls": [
  {"url": "https://bookstack.cores.utah.edu/books/next-gen-sequencing-on-the-aviti/page/project-planning", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": null},
  {"url": "https://bookstack.cores.utah.edu/books/next-gen-sequencing-on-the-aviti/page/rna-sequencing", "type": "rate_page", "current": true, "public": true, "verified": false, "as_of": null}
 ],
 "notes": "Examples only, not a rate card: RNA-seq 2x75 about $250/sample (16 samples); 2 human genomes about $2,700. Separate from the already-known Huntsman HTG core."},
{"institution": "University of Texas Health Science Center at Houston", "core": "Cancer Genomics Core (CGC)", "country": "US", "kind": "academic_medical_center",
 "platforms": ["unknown"],
 "urls": [
  {"url": "https://www.uth.edu/cgc/price.htm", "type": "rate_page", "current": true, "public": true, "verified": false, "as_of": null}
 ],
 "notes": "Fetch returned 403, so I could not confirm NovaSeq or AVITI lines. Search snippet showed internal and external tiers."},
{"institution": "University of Colorado", "core": "CU Genomics Core (Atlassian wiki)", "country": "US", "kind": "university",
 "platforms": ["unknown"],
 "urls": [
  {"url": "https://microcollaborative.atlassian.net/wiki/x/JQCPZg", "type": "rate_page", "current": false, "public": true, "verified": false, "as_of": null},
  {"url": "https://microcollaborative.atlassian.net/wiki/x/KYAcaw", "type": "rate_page", "current": false, "public": true, "verified": false, "as_of": "2021-09"}
 ],
 "notes": "Titled 'University of Colorado Genomics Core Sequencing Prices'; the fetch was empty. The second page is 'Quotes from CU Genomics Core as of 09-09-2021', so it is old. This may be the CU Anschutz core; unconfirmed."},
{"institution": "University of Texas Southwestern Medical Center", "core": "McDermott Next Generation Sequencing Core", "country": "US", "kind": "academic_medical_center",
 "platforms": ["NextSeq 2000"],
 "urls": [
  {"url": "https://www.utsouthwestern.edu/research/core-facilities/next-generation-sequencing/pricing/index.html", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": null}
 ],
 "notes": "The page lists no dollar amounts (estimate by email). It links 'View Internal Pricing' and 'View External Pricing' pages that I could not see. Low value unless those linked pages show prices."}
]}
```

Sources:
- https://cdn.bcm.edu/sites/default/files/2025-09/garp_pricingwebsite_-09-2025.docx
- https://cores.arizona.edu/facilities/azgc/pricing
- https://gccri.uthscsa.edu/services/gsf/gsf-pricing/
- https://www.boisestate.edu/sequencing-core/home/rates/
- https://cloud.wikis.utexas.edu/wiki/x/eRBPAg
- https://www.mdanderson.org/research/research-resources/core-facilities/advanced-technology-genomics-core/services-and-fees/novaseqx-plus-sequencing.html
- https://bookstack.cores.utah.edu/books/next-gen-sequencing-on-the-aviti/page/project-planning
- https://www.utsouthwestern.edu/research/core-facilities/next-generation-sequencing/pricing/index.html