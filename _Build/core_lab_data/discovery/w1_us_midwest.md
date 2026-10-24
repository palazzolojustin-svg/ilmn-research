I found six cores in my slice that publish sequencing prices publicly. Five are new and one, Michigan State, is already on your list. Many other cores in the slice publish nothing, and I'm out of time.

- **Verified by opening the page:** Illinois Carver, UChicago, KUMC, Wayne State and Iowa IIHG.
- **Seen only in search results:** Indiana CMG. Its old URL redirects, so the working URL still needs checking.
- **Dates and history:** Only Illinois (Aug 2026) and Iowa (Apr 2026) show an effective date. UChicago, KUMC and Wayne State show none. I found no older dated versions or price-change announcements for any of them, so the history will need the Wayback Machine.
- **Nothing public found:** Michigan AGC (the page returned 403 Forbidden), Cincinnati and Cincinnati Children's (email for pricing), Cleveland Clinic, Purdue, Medical College of Wisconsin (pricing set at consultation), Ohio State (partner lab), and Kansas State.
- **WashU GTAC, UIC, Loyola, Saint Louis U:** My searches returned no price page. SLU's schedule is a PDF I couldn't open.
- **Not a sequencing price page:** The Notre Dame Genomics & Bioinformatics Core (MiSeq and NextSeq 2000 only) is a facility statement, not a price list. Kansas State's page covers NextSeq and has no prices.
- **Older Ohio State price sheet:** Nationwide Children's has a 2021 per-sample sheet at `coms.osu.edu/sites/default/files/2022-10/NCH-2021-Sequencing-Pricing.pdf`. It is a pre-NovaSeq X historical document, so I left it out of the JSON.

The Michigan State and UW-Madison searches turned up pages beyond the AVITI pricing you already have. I added the MSU URLs as extras in the JSON. For UW-Madison, the 2023 post quoting $2,050 per 10B lane is a dated data point, but it isn't a rate card.

```json
{"cores": [
{"institution": "University of Illinois Urbana-Champaign", "core": "Roy J. Carver Biotechnology Center DNA Services", "country": "US", "kind": "university",
 "platforms": ["NovaSeq X", "NovaSeq 6000"],
 "urls": [
  {"url": "https://biotech.illinois.edu/dna-services-core/dna-services-pricing/", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": "2026-08"},
  {"url": "https://biotech.illinois.edu/dna-services-core/dna-services-instruments/", "type": "rate_page", "current": true, "public": true, "verified": false, "as_of": null}
 ],
 "notes": "Page states 'All pricing is updated, effective Aug. 1, 2026.' Sample: Nova X 1.5B 2x300 per lane $3,100. Search snippets of the instruments page also showed 10B 2x150 $2,190 and 25B 2x150 $3,290 per lane. No AVITI. No older versions seen."},
{"institution": "University of Chicago", "core": "Genomics Facility", "country": "US", "kind": "university",
 "platforms": ["NovaSeq X", "NovaSeq 6000", "AVITI"],
 "urls": [
  {"url": "https://voices.uchicago.edu/genomicsfacility/pricing-new", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": null},
  {"url": "https://voices.uchicago.edu/genomicsfacility/fees", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": null}
 ],
 "notes": "Per-lane NovaX plus AVITI flow cells; internal/affiliated/academic/startup/commercial tiers. Sample: NovaX-10B-200 (PE100) lane internal $1,475; AVITI 150bp flow cell internal $1,175 (industry $1,855.69). Neither page is dated. The 'fees' page may be the older version (it still carries NovaSeq 6000 SP items), so the two likely differ over time. Capture both and use Wayback for history."},
{"institution": "University of Kansas Medical Center", "core": "Genome Sequencing Facility", "country": "US", "kind": "academic_medical_center",
 "platforms": ["NovaSeq X"],
 "urls": [
  {"url": "https://www.kumc.edu/research/genome-sequencing-facility/services/illumina-services/pricing.html", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": null}
 ],
 "notes": "NovaSeq X Plus only; full flow cell and single lane, internal vs external academic. Sample: 1.5B 100-cycle internal $3,600 full flow cell / $1,800 per lane. A search snippet showed 25B 300-cycle full flow cell at $23,872 internal and $37,002 external. No effective date shown. No AVITI."},
{"institution": "Wayne State University", "core": "Genome Sciences Core", "country": "US", "kind": "university",
 "platforms": ["NovaSeq 6000"],
 "urls": [
  {"url": "https://genomesciencescore.wayne.edu/pricing", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": null}
 ],
 "notes": "NovaSeq 6000 SP/S1/S2/S4 flow cells and MiSeq, tiers internal/non-profit/commercial. Sample: S4 300-cycle internal $17,000. No NovaSeq X or AVITI listed. Undated; page footer says 2026. Requests go through iLab."},
{"institution": "University of Iowa", "core": "Institute of Human Genetics (IIHG) Genomics Division", "country": "US", "kind": "university",
 "platforms": ["AVITI", "NovaSeq X"],
 "urls": [
  {"url": "https://humangenetics.medicine.uiowa.edu/genomics-division/genome-sequencing/library-prep-genome-sequencing-fees", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": "2026-04"}
 ],
 "notes": "AVITI24 prices effective April 1, 2026. Sample: AVITI24 300-cycle Cloudbreak FS-High UI $1,042/lane ($2,083 flow cell), external $1,245/lane. NovaSeq X shows 'Please Inquire for Pricing'. Related fee pages (not opened): .../genomics-division/sanger-sequencing/sequencing-fees"},
{"institution": "Indiana University School of Medicine", "core": "Center for Medical Genomics", "country": "US", "kind": "academic_medical_center",
 "platforms": ["NovaSeq X", "NovaSeq 6000"],
 "urls": [
  {"url": "https://geneticslab.medicine.iu.edu/service-cores/facilities/medical-genomics/pricing", "type": "rate_page", "current": false, "public": true, "verified": false, "as_of": null}
 ],
 "notes": "Seen in search results only. Fetch returned a 301 redirect to medicine.iu.edu/genetics/genetic-testing-laboratories; the working URL is not confirmed. Prices are per sample (12-sample batches), not per lane; a snippet showed WGS 400M reads 2x150 at $611 IU / $693 external university / $914 industry. Needs follow-up."},
{"institution": "Michigan State University", "core": "Research Technology Support Facility (RTSF) Genomics", "country": "US", "kind": "university",
 "platforms": ["AVITI", "NovaSeq X"],
 "urls": [
  {"url": "https://rtsf.natsci.msu.edu/rtsf-core-facilities/genomics/pricing.aspx", "type": "rate_page", "current": true, "public": true, "verified": false, "as_of": null},
  {"url": "https://rtsf.natsci.msu.edu/genomics/pricing.aspx", "type": "rate_page", "current": true, "public": true, "verified": false, "as_of": null},
  {"url": "https://rtsf.natsci.msu.edu/sites/_rtsf/assets/File/How_much_sequencing_November_2021.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2021-11"},
  {"url": "https://rtsf.natsci.msu.edu/_assets/files/genomics/100924_SG_Elements_AVITI_and_24_Overview_Michigan_State_University.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2024-10"}
 ],
 "notes": "Already known; extra URLs only, seen in search results. AVITI bundled flat rate seen: $76/sample for SparQ library plus 3 Gbp."}
]}
```

Sources:
- [Illinois DNA Pricing](https://biotech.illinois.edu/dna-services-core/dna-services-pricing/)
- [UChicago pricing](https://voices.uchicago.edu/genomicsfacility/pricing-new)
- [KUMC pricing](https://www.kumc.edu/research/genome-sequencing-facility/services/illumina-services/pricing.html)
- [Wayne State pricing](https://genomesciencescore.wayne.edu/pricing)
- [Iowa IIHG fees](https://humangenetics.medicine.uiowa.edu/genomics-division/genome-sequencing/library-prep-genome-sequencing-fees)