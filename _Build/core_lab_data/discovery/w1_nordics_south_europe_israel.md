I found only a few cores in this slice with public NGS prices. Most of the Nordic, French, Italian, Portuguese, Greek and Israeli cores either price by quote or keep their rates on login pages (iLab) that I skipped. Searches for the cores below found no public rate card, so they are not in the JSON:
- Oslo NSC, Bergen, Copenhagen and Aarhus
- Lund, Gothenburg and Uppsala (apart from the NGI national pages)
- Oulu
- GenomEast/IGBMC, Genotoul, Curie, IGFL, Imagine and ICM
- CRG, IRB Barcelona, Santiago, Gulbenkian and i3S
- IIT, TIGEM, Padova, Milan and Rome
- Weizmann INCPM, Hebrew University and Tel Aviv (Tel Aviv's published prices are Sanger only)

The CNAG lists below are extra history URLs for a core you already have.

- **NGI Sweden (SciLifeLab):** This is the best find, and its page was updated 24 Jun 2026. It publishes SEK price examples and sells NovaSeq X in 600M read-pair units (5B = 1 unit, 10B = 2, 25B = 5). Sample line: "1 lane of NovaSeq 25B-300 (~3B read-pairs, ~25M/sample): 32,000 SEK". The 17 Nov 2025 announcement says Illumina harmonised cost per read across the 10B and 25B flow cells, which is a dated price-change event. It gives no per-unit price.
- **FISABIO (Valencia):** This is a Spanish public research foundation. It has a Spanish PDF of sequencing tariffs (NextSeq 2000/MiSeq) dated Feb 2026 and a 2023 version for history. I couldn't read the PDF text, so I haven't confirmed prices or platforms. The search result suggests NextSeq 2000 and MiSeq only.
- **FIMM Genomics (Helsinki):** The page lists NovaSeq X Plus, AVITI24 and MiSeq i100 sequencing-only services, but with no prices. Pricing is in iLab or by quote.
- **Technion Genome Center:** The page is marked "As of March 2020", so it is stale and covers older Illumina platforms only. NextSeq High Output 150 cycles is 15,000 NIS per run. The original URL redirects to atgc.net.technion.ac.il, which returned a 404.
- **INCLIVA (Valencia):** The 2026 PDF showed only extraction and quantification items in the search snippet. I haven't confirmed any NGS prices.
- **EPFL GECF (Switzerland, outside your slice):** I'm including it because it has a dated series of PDFs with big 2025–26 NovaSeq/AVITI price cuts. Prices are in CHF.

```json
{"cores": [
{"institution": "SciLifeLab / Uppsala University & Stockholm (National Genomics Infrastructure)", "core": "NGI Sweden", "country": "Sweden", "kind": "nonprofit_institute",
 "platforms": ["NovaSeq X"],
 "urls": [
  {"url": "https://ngisweden.scilifelab.se/resources/price-examples/", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": "2026-06"},
  {"url": "https://ngisweden.scilifelab.se/2025/11/exciting-update-from-illumina-sequencing-costs-now-aligned-across-flow-cells/", "type": "announcement", "current": true, "public": true, "verified": true, "as_of": "2025-11"},
  {"url": "https://ngisweden.scilifelab.se/technologies/illumina/novaseq-x-plus/", "type": "rate_page", "current": true, "public": true, "verified": false, "as_of": null}
 ],
 "notes": "SEK examples only, sold in 600M read-pair units. 'NovaSeq 25B-300 lane (~3B read-pairs): 32000 SEK' (page updated 2026-06-24). Nov 2025 post describes the unit-pricing change but gives no amounts. Per-unit SEK price not published."},
{"institution": "FISABIO Foundation (Valencia)", "core": "FISABIO Sequencing & Bioinformatics Platform", "country": "Spain", "kind": "nonprofit_institute",
 "platforms": ["NextSeq 2000"],
 "urls": [
  {"url": "https://fisabio.san.gva.es/media/upload/arxius/plataformas-cientifico-tecnicas/fs-for216-tarifas-secuenciacion-masiva-y-bioiformatica-es.pdf", "type": "pdf", "current": true, "public": true, "verified": false, "as_of": "2026-02"},
  {"url": "https://fisabio.san.gva.es/media/upload/arxius/servicios/plataformas-cientifico-tec/servicios-cientifico-tec/secuenciacion/tarifas-secuenciacion-2023.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2023"}
 ],
 "notes": "Spanish tariff PDFs (PDF created 2026-02-20). Text was not readable by the fetch tool, so prices and platforms are unconfirmed. The search result suggests NextSeq 2000 and MiSeq only, no NovaSeq X or AVITI."},
{"institution": "University of Helsinki (FIMM)", "core": "FIMM Genomics", "country": "Finland", "kind": "university",
 "platforms": ["NovaSeq X", "AVITI"],
 "urls": [
  {"url": "https://www.helsinki.fi/en/infrastructures/genome-analysis/infrastructures/fimm-genomics/fimm-genomics-services/ngs-sequencing-services/fimm-genomics-sequencing-only-services", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": null}
 ],
 "notes": "Page lists NovaSeq X Plus, AVITI24 and MiSeq i100 sequencing-only services but NO prices. Ordering is via iLab (gated). Low value unless an iLab public price page exists."},
{"institution": "Technion", "core": "Technion Genome Center", "country": "Israel", "kind": "university",
 "platforms": ["NextSeq 500/550", "HiSeq 2500", "MiSeq"],
 "urls": [
  {"url": "https://tgc.net.technion.ac.il/?p=1567", "type": "rate_page", "current": false, "public": true, "verified": true, "as_of": "2020-03"}
 ],
 "notes": "Stale ('As of March 2020'), NIS. 'NextSeq High Output 150 cycles 15000 NIS per run'. No NovaSeq, AVITI or Ultima. The page redirects to atgc.net.technion.ac.il, and that URL returned a 404. Check the site for a newer list."},
{"institution": "INCLIVA Health Research Institute (Valencia)", "core": "Precision Medicine / Genomics platform", "country": "Spain", "kind": "nonprofit_institute",
 "platforms": [],
 "urls": [
  {"url": "https://www.incliva.es/wp-content/uploads/2026/03/Tarifas_Web_MP_2026.pdf", "type": "pdf", "current": true, "public": true, "verified": false, "as_of": "2026-03"}
 ],
 "notes": "2026 tariff PDF (internal / external public / external private). Search snippet showed only nucleic acid extraction and quantification. NGS content unconfirmed, so low priority."},
{"institution": "CNAG (extra history URLs for known core)", "core": "CNAG Sequencing Unit", "country": "Spain", "kind": "nonprofit_institute",
 "platforms": ["NovaSeq 6000", "NovaSeq X"],
 "urls": [
  {"url": "https://www.cnag.eu/sites/default/files/CNAG PRICES 2025_R1.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2025"},
  {"url": "https://www.cnag.eu/sites/default/files/CNAG PRICES 2025.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2025"},
  {"url": "https://ccnagdev.cnag.cat/sites/default/files/CNAG PRICES.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": null}
 ],
 "notes": "EUR per Gb, 3 price columns. e.g. 'Large Scale Sequencing Gb (2x150, NovaSeq 6000 S4) 5.58 / 6.25 / 6.70 EUR' (undated version); the 2025_R1 version shows ~4.28/4.79/5.14 for 2x150 S4. 2025_R1 supersedes the plain 2025 version."},
{"institution": "EPFL (outside slice: Switzerland)", "core": "Gene Expression Core Facility (GECF)", "country": "Switzerland", "kind": "university",
 "platforms": ["NovaSeq X", "AVITI"],
 "urls": [
  {"url": "https://www.epfl.ch/research/facilities/gene-expression-core-facility/wp-content/uploads/2026/09/GECF-price-list-for-EPFL-users-09-September-2026.pdf", "type": "pdf", "current": true, "public": true, "verified": false, "as_of": "2026-09"},
  {"url": "https://www.epfl.ch/research/facilities/gene-expression-core-facility/wp-content/uploads/2026/02/GECF-price-list-for-EPFL-users-15-February-2026.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2026-02"},
  {"url": "https://www.epfl.ch/research/facilities/gene-expression-core-facility/wp-content/uploads/2025/07/GECF-price-list-for-EPFL-users-01-July-2025.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2025-07"},
  {"url": "https://www.epfl.ch/research/facilities/gene-expression-core-facility/wp-content/uploads/2025/03/GECF-price-list-for-EPFL-users-01-March-2025.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2025-03"},
  {"url": "https://www.epfl.ch/research/facilities/gene-expression-core-facility/wp-content/uploads/2023/09/GECF-price-list-for-EPFL-users-October-2023.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2023-10"},
  {"url": "https://www.epfl.ch/research/facilities/gene-expression-core-facility/page-154614-en-html/", "type": "announcement", "current": true, "public": true, "verified": false, "as_of": null}
 ],
 "notes": "CHF. Frequent dated price lists; the news page mentions NovaSeq/AVITI price decreases (2025, Sep-Nov 2025, Mar 2026). I did not open the PDFs, so the platforms and prices are unconfirmed. Outside the assigned slice, but strong for history."}
]}
```

Sources:
- [NGI Sweden price examples](https://ngisweden.scilifelab.se/resources/price-examples/)
- [NGI Sweden announcement, Nov 2025](https://ngisweden.scilifelab.se/2025/11/exciting-update-from-illumina-sequencing-costs-now-aligned-across-flow-cells/)
- [FIMM Genomics sequencing-only services](https://www.helsinki.fi/en/infrastructures/genome-analysis/infrastructures/fimm-genomics/fimm-genomics-services/ngs-sequencing-services/fimm-genomics-sequencing-only-services)
- [FISABIO tariffs, Feb 2026](https://fisabio.san.gva.es/media/upload/arxius/plataformas-cientifico-tecnicas/fs-for216-tarifas-secuenciacion-masiva-y-bioiformatica-es.pdf)
- [Technion Genome Center price list, Mar 2020](https://tgc.net.technion.ac.il/?p=1567)
- [EPFL GECF price list, Sep 2026](https://www.epfl.ch/research/facilities/gene-expression-core-facility/wp-content/uploads/2026/09/GECF-price-list-for-EPFL-users-09-September-2026.pdf)