I found 6 cores in states N–W with public NGS prices that aren't on your known list, well short of the 15–30 target. Searches mostly returned cores you already have, and many sites that fit my slice (UNC, WashU GTAC, Mount Sinai, NYU, Vanderbilt, OHSU, Rochester) publish no prices.

**Public prices found (none show NovaSeq X, AVITI or Ultima prices):**
- **UT Knoxville Genomics Core** lists NovaSeq 6000 and NextSeq 1000/2000 flow cell prices. Sample line: P1 100-cycle internal $1,120, external academic $1,270, plus a $36 tariff fee. The page has no date. It says "NextSeq 1000" in the text, so the platform needs rechecking.
- **UTHSC Memphis Molecular Resource Center** lists AVITI and NextSeq 2000 prices, effective 2025-07-01 (FY26), rising 3% per fiscal year. Sample line: AVITI HIGH 2x75 1B reads $1,000 to $1,300, and NextSeq 2000 P3 $1,900. An earlier search result suggested a 2024 version of the same list exists, but I found no URL for it.
- **East Carolina University Genomics Core** lists NextSeq 2000 prices, effective 2025-07-01. Sample line: P1 internal $936 and up. Search results also showed a June 2024 PDF and a 2020 PDF. The June 2024 PDF returned 404 when I opened it, so I haven't verified it.
- **Utah State University Genomics** lists NextSeq 2000 kits with internal and external prices (about $1,080–$5,880 internal). The page has no date.
- **North Dakota State University Biotechnology Innovation Core** lists NextSeq 1000 prices. Sample line: P2 2x150 internal $3,222, external $4,671.90. The page has no date.
- **Texas Tech Center for Biotechnology and Genomics** has only old, thin pricing. Its MiSeq sheet is dated FY18 and it lists NovaSeq 6000 as "contact." FY21 and FY23 PDFs exist but I haven't confirmed they hold NovaSeq prices.

**Login-gated or no public prices:**
- UNC HTSF has a fee page behind an ONYEN login.
- Oklahoma OUHSC has a pricing page behind a login.
- WashU GTAC says quotes only.
- Mount Sinai says custom estimates only.
- Vanderbilt VANTAGE and the Northwest Genomics Center list NovaSeq X Plus or AVITI but no prices.
- Purdue Bindley (AVITI and NovaSeq X) has no prices on its iLab page, and neither does Cincinnati Children's.
- VCU and Clemson show no prices.
- Rochester, Penn State and OHSU show no prices either.

**Not checked:** Oklahoma State and several others returned 403 or no usable results: Stanford (its pages list only older platforms), Fred Hutch, Wake Forest, UVA, Temple/Jefferson, Jackson Laboratory, Cold Spring Harbor, Wistar, Van Andel, and the University of Wyoming.

```json
{"cores": [
{"institution": "University of Tennessee, Knoxville", "core": "Genomics Core", "country": "US", "kind": "university", "platforms": ["NovaSeq 6000", "NextSeq 1000/2000"],
 "urls": [{"url": "https://research.utk.edu/research-facilities/core-facilities/genomics-core/", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": null},
          {"url": "https://research.utk.edu/oried/core-facilities/genomics-core/", "type": "rate_page", "current": true, "public": true, "verified": false, "as_of": null}],
 "notes": "P1 100-cycle internal $1,120 / external academic $1,270 / non-academic $1,420 + $36 tariff fee. A search snippet also showed NovaSeq 6000 S4 300 internal $15,700. No NovaSeq X or AVITI listed."},
{"institution": "University of Tennessee Health Science Center", "core": "Molecular Resource Center of Excellence (MRC)", "country": "US", "kind": "academic_medical_center", "platforms": ["AVITI", "NextSeq 2000"],
 "urls": [{"url": "https://www.uthsc.edu/research/institutional-cores/mrc/price-list.php", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": "2025-07"},
          {"url": "https://uthsc.edu/research/institutional-cores/mrc/price-list.php", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": "2025-07"},
          {"url": "https://www.uthsc.edu/research/institutional-cores/documents/price-list-mrc.pdf", "type": "pdf", "current": null, "public": true, "verified": false, "as_of": null}],
 "notes": "FY26 list effective 2025-07-01, +3% each fiscal year. AVITI HIGH 2x75 1B reads $1,300; NextSeq 2000 P3 $1,900. $100 flat consumables fee per project. A search snippet said a 2024 version also exists, but I found no URL for it."},
{"institution": "East Carolina University", "core": "Genomics Core (Big Core), Dept. of Pathology and Laboratory Medicine", "country": "US", "kind": "university", "platforms": ["NextSeq 2000"],
 "urls": [{"url": "https://pathology.ecu.edu/genomics-core/?p=389", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": "2025-07"},
          {"url": "https://biology.ecu.edu/wp-content/pv-uploads/sites/26/2023/07/GC-Pricelist.June2024.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2024-06"},
          {"url": "https://biology.ecu.edu/wp-content/pv-uploads/sites/26/2020/05/GC-Pricelist5-2020.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2020-05"}],
 "notes": "Four tiers (internal, federal, non-profit, profit). NextSeq 2000 P1 internal from $936; P4 up to $6,318. Effective 2025-07-01. The June 2024 PDF returned 404 when fetched, so it may have moved."},
{"institution": "Utah State University", "core": "Center for Integrated BioSystems Genomics Core", "country": "US", "kind": "university", "platforms": ["NextSeq 2000", "MiSeq i100"],
 "urls": [{"url": "https://qanr.usu.edu/biosystems/core-labs/genomics", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": null},
          {"url": "https://biosystems.usu.edu/core-labs/genomics/dna-sequencing", "type": "rate_page", "current": null, "public": true, "verified": false, "as_of": null}],
 "notes": "NextSeq 2000 kits internal about $1,080-$5,880, external about $1,580-$8,585. A snippet showed P2 100-cycle at $1,465 / $2,140. No date on page."},
{"institution": "North Dakota State University", "core": "Biotechnology Innovation Core - Sequencing", "country": "US", "kind": "university", "platforms": ["NextSeq 1000"],
 "urls": [{"url": "https://www.ndsu.edu/biotech-innovation-core/sequencing/services-and-fees", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": null}],
 "notes": "P2 2x150 internal $3,222 / external $4,671.90 per run. Kit prices float with Illumina pricing. No date on page."},
{"institution": "Texas Tech University", "core": "Center for Biotechnology and Genomics (CBG) Core", "country": "US", "kind": "university", "platforms": ["NovaSeq 6000", "MiSeq"],
 "urls": [{"url": "https://www.depts.ttu.edu/biotechnologyandgenomics/corelabfacility/Rates/Rates_FY23.php", "type": "rate_page", "current": false, "public": true, "verified": true, "as_of": "2023"},
          {"url": "https://www.depts.ttu.edu/biotechnologyandgenomics/corelabfacility/Rates/CBG_Rates_FY23.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2023"},
          {"url": "https://www.depts.ttu.edu/biotechnologyandgenomics/corelabfacility/Rates/CBG_All_Rates_FY21.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2021"},
          {"url": "https://www.depts.ttu.edu/biotechnologyandgenomics/rates/CBG_Genomics_Rate.html", "type": "rate_page", "current": false, "public": true, "verified": true, "as_of": "2020-01"}],
 "notes": "Low value. The rate page links only the FY23 fee schedule (page updated 2025-10). The FY18 genomics page prices MiSeq only and says 'contact' for NovaSeq 6000. The FY21 PDF reportedly has NovaSeq 6000 SP/S1/S2 prices, unverified."}
]}
```

Sources:
- [UT Knoxville Genomics Core](https://research.utk.edu/research-facilities/core-facilities/genomics-core/)
- [UTHSC Memphis MRC price list](https://www.uthsc.edu/research/institutional-cores/mrc/price-list.php)
- [ECU Genomics Core](https://pathology.ecu.edu/genomics-core/?p=389)
- [Utah State Genomics](https://qanr.usu.edu/biosystems/core-labs/genomics)
- [NDSU Biotechnology Innovation Core](https://www.ndsu.edu/biotech-innovation-core/sequencing/services-and-fees)
- [Texas Tech CBG rates](https://www.depts.ttu.edu/biotechnologyandgenomics/corelabfacility/Rates/Rates_FY23.php)