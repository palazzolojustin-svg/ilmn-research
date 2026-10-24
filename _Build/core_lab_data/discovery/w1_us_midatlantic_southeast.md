Seven cores in my slice have public prices I could confirm or partly confirm. Most of the rest of the slice has no usable public rate card.

- **Confirmed by opening the page:**
  - Pitt: NovaSeq X Plus and NovaSeq 6000, internal prices effective 2025-06-01.
  - Penn PGSC: NovaSeq X Plus plus PacBio Revio, with no date on the page.
  - UGA GGBC: a March 2025 announcement of NovaSeq X Plus lane prices.
  - NC State GSL: NextSeq 2000 prices for NC State users, effective 2026-04-24, plus a $149 fee on outsourced NovaSeq X runs.
  - Tulane: a 2026 internal calculator, NextSeq 2000 only.
- **Johns Hopkins GRCF:** I could not open it, because both GRCF and IGC return 403 to fetches. Search snippets showed NovaSeq X flow-cell prices and an older version on `?p=796`. I marked these `verified: false`.
- **Virginia Tech GSC:** I could not read the September 2024 price guide PDF, which returned binary data. I don't know whether it lists NovaSeq X or AVITI, so it is unverified.
- **No public prices found:**
  - UNC HTSF: the fee table needs an ONYEN login.
  - Emory EIGC: no price list online. Its facilities document lists only MiSeq and NextSeq 2000 for Illumina.
  - Clemson, Princeton and Moffitt: the pages describe services but give no rates.
  - Rutgers: only a 2022 MiSeq/NovaSeq 6000 list, which predates the NovaSeq X.
  - UF ICBR: only percentage-savings posts (up to 40%, and up to 60% on another page).
  - UAB: the Heflin pricing page showed Sanger and fragment analysis only.
- **Not found at all:** I found nothing public for UMD IGS, Georgetown, UVA, VCU, Wake Forest, MUSC, Miami, USF, CHOP, Penn State, Kentucky, Louisville, LSU, Georgia Tech, Augusta, Vanderbilt VANTAGE, UD or UAB's NGS prices. Search results for these were thin, and I ran out of time before checking each core's own site.
- **Platforms:** none of the cores I confirmed lists AVITI or UG100 pricing.

```json
{"cores": [
{"institution": "Johns Hopkins University", "core": "Genetic Resources Core Facility (GRCF) High Throughput Sequencing Center", "country": "US", "kind": "university",
 "platforms": ["NovaSeq X"],
 "urls": [
  {"url": "https://grcf.jhmi.edu/?p=14200", "type": "rate_page", "current": true, "public": true, "verified": false, "as_of": "2026"},
  {"url": "https://igc.jhmi.edu/?p=14200", "type": "rate_page", "current": true, "public": true, "verified": false, "as_of": null},
  {"url": "https://grcf.jhmi.edu/?p=796", "type": "rate_page", "current": false, "public": true, "verified": false, "as_of": null}],
 "notes": "Fetch returned 403, so these were seen only in search snippets. Snippets show per-flow-cell NovaSeq X prices, e.g. 25B 100-cycle $13,100 (older) / $13,800 (2026 reference) and 10B single lane 300-cycle $1,200-1,400. The three URLs show different prices, so they may be different versions."},
{"institution": "University of Pittsburgh", "core": "Health Sciences Sequencing Core / Genomics Research Core (genomics.pitt.edu)", "country": "US", "kind": "university",
 "platforms": ["NovaSeq X", "NovaSeq 6000"],
 "urls": [
  {"url": "https://www.genomics.pitt.edu/about/pricing", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": "2025-06"},
  {"url": "https://genomics.pitt.edu/about/pricing", "type": "rate_page", "current": true, "public": true, "verified": false, "as_of": null}],
 "notes": "Internal (Pitt/UPMC) prices effective 6/01/2025. Sample line: NovaSeq X Plus 1.5B 200-cycle (2 lanes at 750M each) $2,554 in the first price column of the search snippet; the column headers are unclear. Covers 1.5B/10B/25B, lane, full flow cell and 2+ flow cells. External prices are on request. No older versions or news posts on the page. Also covers NovaSeq 6000 S2/S4/SP and MiSeq. Equipment pages exist at sharedfacilities.pitt.edu but I did not check them."},
{"institution": "University of Pennsylvania", "core": "Penn Genomics and Sequencing Core (PGSC)", "country": "US", "kind": "university",
 "platforms": ["NovaSeq X"],
 "urls": [{"url": "https://genetics.med.upenn.edu/penn-genomics-and-sequencing-core", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": null}],
 "notes": "NovaSeq X Plus full-service price per lane and ready-to-sequence price per flow cell, plus PacBio Revio. Sample line: 1.5B 100-cycle full-service lane $1,319.56; 10B 100-cycle $1,228.59 / $1,087.50 (two price columns in the snippet). NextSeq 2000 and MiSeq say 'contact us'. No date, PDF, or older versions on the page."},
{"institution": "University of Georgia", "core": "Georgia Genomics and Bioinformatics Core (GGBC)", "country": "US", "kind": "university",
 "platforms": ["NovaSeq X"],
 "urls": [
  {"url": "https://dna.uga.edu/2025/03", "type": "announcement", "current": true, "public": true, "verified": true, "as_of": "2025-03"},
  {"url": "https://dna.uga.edu/category/news", "type": "announcement", "current": true, "public": true, "verified": false, "as_of": null},
  {"url": "https://spa.uga.edu/research-facility-rates", "type": "rate_page", "current": true, "public": true, "verified": false, "as_of": null}],
 "notes": "Post dated 2025-03-12, 'Announcing New Price Reductions and Sequencing Options at the GGBC'. Sample line: NovaSeq X Plus one 25B lane PE150 $3,000 and 10B lane $2,000 (UGA rate). The spa.uga.edu page is a facility rate index that I did not open. I did not find the core's own current rate page."},
{"institution": "North Carolina State University", "core": "Genomic Sciences Laboratory (GSL)", "country": "US", "kind": "university",
 "platforms": ["NextSeq 2000", "NovaSeq X"],
 "urls": [
  {"url": "https://research.ncsu.edu/gsl/pricing/", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": "2026-04"}],
 "notes": "NextSeq 2000 prices for NC State users, effective 2026-04-24. Sample line: NextSeq 2000 P1 100SE/50PE $1,277.41. An older snippet showed P1 150PE $1,641.40, so history exists, but I have no URL for older versions. NovaSeq X is outsourced, with a $149 GSL fee added and no price listed. The detailed sheet is a Unity ID-gated Google Doc. External prices are on request. The URLs research.ncsu.edu/gsl/?p=266 and ?p=1622 also appeared in search but were not opened."},
{"institution": "Tulane University", "core": "CTRII NextGen Sequencing Core", "country": "US", "kind": "university",
 "platforms": ["NextSeq 2000"],
 "urls": [
  {"url": "https://medicine.tulane.edu/centers-institutes/ctrii/nextgen-sequencing-core/calculator", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": "2026"},
  {"url": "https://medicine.tulane.edu/centers-institutes/ctrii/nextgen-sequencing-core/illumina-sequencing-pricing", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": "2025-10"}],
 "notes": "The 2026 internal-rate calculator is NextSeq 2000 only. Sample line: standard DNA-Seq prep $95/sample. Run prices appear only in the calculator output. The Illumina pricing page holds prices in an image I could not read, and its upload date of about 2025-10 is inferred from the file path. The core uses iLab."},
{"institution": "Virginia Tech", "core": "Fralin Life Sciences Genomics Sequencing Center (GSC)", "country": "US", "kind": "university",
 "platforms": [],
 "urls": [{"url": "https://fralinlifesci.vt.edu/content/dam/fralinlifesci_vt_edu/core-services/gsc/2024-09-01-GSC-Pricing-Guide.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2024-09"}],
 "notes": "The PDF is dated 2024-09-01 and gives per-sample rates for VT and non-VT users. The fetch returned unreadable binary, so I could not confirm which platforms it covers. This is a good candidate for the PDF extraction step. A newer guide probably exists, but I did not find its URL."},
{"institution": "Rutgers University (NJMS)", "core": "NJMS Genomics Center", "country": "US", "kind": "university",
 "platforms": ["NovaSeq 6000"],
 "urls": [{"url": "https://research.njms.rutgers.edu/genomics/clinical/docs/Genomics%20Pricing%202022.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2022"}],
 "notes": "A 2022 internal price list covering MiSeq and NovaSeq 6000 kits (SP 500-cycle $4,620 up to S4 300-cycle over $15,000), per a search summary. It predates the NovaSeq X and is too old for the Oct 2024+ window. I found no current Rutgers list."}
]}
```

Sources:
- [Pitt pricing](https://www.genomics.pitt.edu/about/pricing)
- [Penn PGSC](https://genetics.med.upenn.edu/penn-genomics-and-sequencing-core)
- [UGA GGBC March 2025 post](https://dna.uga.edu/2025/03)
- [NC State GSL pricing](https://research.ncsu.edu/gsl/pricing/)
- [Tulane calculator](https://medicine.tulane.edu/centers-institutes/ctrii/nextgen-sequencing-core/calculator)
- [Tulane Illumina pricing](https://medicine.tulane.edu/centers-institutes/ctrii/nextgen-sequencing-core/illumina-sequencing-pricing)
- [Johns Hopkins GRCF](https://grcf.jhmi.edu/?p=14200)
- [Virginia Tech GSC pricing guide](https://fralinlifesci.vt.edu/content/dam/fralinlifesci_vt_edu/core-services/gsc/2024-09-01-GSC-Pricing-Guide.pdf)
- [Rutgers NJMS 2022 price list](https://research.njms.rutgers.edu/genomics/clinical/docs/Genomics%20Pricing%202022.pdf)