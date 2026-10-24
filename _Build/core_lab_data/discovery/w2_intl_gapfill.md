Only one new non-US core is confirmed, and I stopped short of the 15–30 target. Searches mostly returned US cores. Many European and Asian cores either don't publish prices or gate them behind a login.

- **Confirmed new:** Utrecht Sequencing Facility (USEQ, Netherlands). Its fee page shows NovaSeq X (1.5B, 10B and 25B) and NextSeq 2000 (P1–P4) run prices in € ex-VAT, dated 01-08-2026. It has no AVITI, UG100 or NovaSeq 6000. The full price list is a SharePoint link for UMCU clients only, and I found no PDF or older versions.
- **Unconfirmed:** The Warsaw CENT, Lleida and SAMRC pages below returned 404 or unreadable PDFs, so I could not check their contents.
- **Not usable:** HKU Genomics Core and Chulalongkorn publish no NGS prices (HKU quotes via iLab). NTOU (Taiwan) lists only Nanopore. Copenhagen GeoGenetics has prices behind a KU login. UMC Utrecht, Oslo, Bergen, NTNU and Ramaciotti give no figures.
- **Not found:** I found no published sequencing price lists for UK cores (Oxford, Crick, Earlham and others), German cores other than FAU, Nordic, Israeli, Latin American or Asian cores. The Oxford Kennedy page returned 403 and is single-cell only.
- **Extra history URLs for known cores:** seen in search results and not opened. They cover EPFL (five dated lists), CNAG, Calgary CHGI, TCAG, INCLIVA and FISABIO. The EPFL list dated 09 September 2026 appears to be the newest.

```json
{"cores": [
{"institution": "Utrecht University Medical Center (UMC Utrecht)", "core": "Utrecht Sequencing Facility (USEQ)", "country": "Netherlands", "kind": "academic_medical_center", "platforms": ["NovaSeq X", "NextSeq 2000"],
 "urls": [
  {"url": "https://useq.nl/service-fees/", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": "2026-08"},
  {"url": "https://research.umcutrecht.nl/technologies/utrecht-sequencing-facility/services-fees/", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": null}],
 "notes": "Runs priced per run in EUR ex-VAT: NovaSeq X 1.5B/10B/25B at 100/200/300 cycles, single-lane 10B, NextSeq 2000 P1-P4. Page says published 01-08-2026 and prices update quarterly. The full internal list is a SharePoint link for UMCU clients only. No older versions found."},
{"institution": "University of Warsaw", "core": "CENT sequencing (Internal Users Pricelist / Sequencing runs)", "country": "Poland", "kind": "university", "platforms": ["unknown"],
 "urls": [
  {"url": "https://cent.uw.edu.pl/en/?p=10138", "type": "rate_page", "current": false, "public": true, "verified": false, "as_of": null},
  {"url": "https://cent.uw.edu.pl/en/?p=10133", "type": "rate_page", "current": false, "public": true, "verified": false, "as_of": null}],
 "notes": "Titled 'Sequencing runs' in search results. Both URLs returned 404 when fetched. Needs a re-check via the CENT site. Platforms and prices unknown."},
{"institution": "Universitat de Lleida", "core": "SCTS Proteomics and Genomics service", "country": "Spain", "kind": "university", "platforms": ["unknown"],
 "urls": [
  {"url": "https://www.recercaitransferencia.udl.cat/export/sites/Recerca/ca/.galleries/SCTS/Tarifas_Proteomica_i_Genomica_20260714.pdf", "type": "pdf", "current": true, "public": true, "verified": false, "as_of": "2026-07"}],
 "notes": "Tariff PDF modified 2026-07-14. The fetch tool could not read the PDF text, so I don't know whether it has NGS run prices."},
{"institution": "South African Medical Research Council", "core": "SAMRC Genomics Platform", "country": "South Africa", "kind": "government", "platforms": ["unknown"],
 "urls": [
  {"url": "https://www.samrc.ac.za/sites/default/files/attachments/2023-10/GenomicsPlatformPrices.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2024-04"}],
 "notes": "Price PDF with creation date 2024-04-22. Text unreadable by the fetch tool, so the platforms are unconfirmed."},
{"institution": "IRB Barcelona", "core": "Genomics and bioinformatics tariffs 2026", "country": "Spain", "kind": "nonprofit_institute", "platforms": ["unknown"],
 "urls": [
  {"url": "https://www.irbbarcelona.org/sites/default/files/2026-03/71 - Tarifas Bioestadistica 2026 _WEB.pdf", "type": "pdf", "current": true, "public": true, "verified": false, "as_of": "2026-03"}],
 "notes": "Seen in search results only. The visible items were bioinformatics (QC and alignment per sample or per GB), not run prices. Probably not useful for $/Gb."},
{"institution": "University of Copenhagen", "core": "GeoGenetics Sequencing Core", "country": "Denmark", "kind": "university", "platforms": ["NovaSeq X", "NextSeq 2000"],
 "urls": [
  {"url": "https://globe.ku.dk/infrastructure-and-facilities/seqcenter", "type": "rate_page", "current": true, "public": false, "verified": false, "as_of": null}],
 "notes": "Per the search summary, prices are behind a KU-ID login on the order form. Skip."},
{"institution": "EPFL (KNOWN CORE: extra history URLs)", "core": "Gene Expression Core Facility (GECF)", "country": "Switzerland", "kind": "university", "platforms": ["NovaSeq 6000", "NovaSeq X", "AVITI"],
 "urls": [
  {"url": "https://www.epfl.ch/research/facilities/gene-expression-core-facility/wp-content/uploads/2026/09/GECF-price-list-for-EPFL-users-09-September-2026.pdf", "type": "pdf", "current": true, "public": true, "verified": false, "as_of": "2026-09"},
  {"url": "https://www.epfl.ch/research/facilities/gene-expression-core-facility/wp-content/uploads/2025/07/GECF-price-list-for-EPFL-users-01-July-2025.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2025-07"},
  {"url": "https://www.epfl.ch/research/facilities/gene-expression-core-facility/wp-content/uploads/2025/03/GECF-price-list-for-EPFL-users-01-March-2025.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2025-03"},
  {"url": "https://epfl.ch/research/facilities/gene-expression-core-facility/wp-content/uploads/2024/11/GECF-price-list-for-EPFL-users-01-November-2024.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2024-11"},
  {"url": "https://epfl.ch/research/facilities/gene-expression-core-facility/wp-content/uploads/2024/07/GECF-price-list-for-EPFL-users-01-July-2024.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2024-07"},
  {"url": "https://www.epfl.ch/research/facilities/gene-expression-core-facility/page-154614-en-html/", "type": "announcement", "current": true, "public": true, "verified": false, "as_of": null}],
 "notes": "Extra history for a known core. Price lists in CHF. The changelog page mentions a strong NovaSeq price decrease (March 2026 update)."},
{"institution": "CNAG (KNOWN CORE: extra history URLs)", "core": "CNAG Sequencing Unit", "country": "Spain", "kind": "nonprofit_institute", "platforms": ["NovaSeq X"],
 "urls": [
  {"url": "https://www.cnag.eu/sites/default/files/CNAG PRICES 2025_R1.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2025"},
  {"url": "https://www.cnag.eu/sites/default/files/CNAG PRICES 2025.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2025"}],
 "notes": "Extra history for a known core, seen in search results only."},
{"institution": "University of Calgary (KNOWN CORE: extra history URLs)", "core": "CHGI NGS", "country": "Canada", "kind": "university", "platforms": ["NovaSeq X", "NovaSeq 6000", "NextSeq 2000"],
 "urls": [
  {"url": "https://cumming.ucalgary.ca/sites/default/files/teams/97/2025%20CHGI%20Internal%20Price%20List.pdf", "type": "pdf", "current": true, "public": true, "verified": false, "as_of": "2025"},
  {"url": "https://live-cumming.ucalgary.ca/sites/default/files/teams/97/CHGI%20Internal%20UofC%20Price%20List%20with%20sales%202024-2025.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2024"},
  {"url": "https://cumming.ucalgary.ca/sites/default/files/teams/97/CHGI%20Internal%20Price%20List%20June%202024.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2024-06"},
  {"url": "https://cumming.ucalgary.ca/sites/default/files/teams/97/CHGI%20Internal%20Library%20%26%20Seq%20Price%20List%202022-2023.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2022"}],
 "notes": "Extra history for a known core. Sample line from search summaries: NovaSeq X 25B lane 300 cycles PE150 is CAD $4,100 (2025 and June 2024 lists)."},
{"institution": "Hospital for Sick Children (KNOWN CORE: extra URL)", "core": "TCAG", "country": "Canada", "kind": "academic_medical_center", "platforms": ["NovaSeq X"],
 "urls": [
  {"url": "https://www.tcag.ca/documents/facilities/TCAG-NGS-Price-List April 2025.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2025-04"}],
 "notes": "Extra history for a known core. Sample line from search summaries: 25B 300-cycle lane $3,470 (April 2025)."},
{"institution": "INCLIVA (KNOWN CORE: extra URL)", "core": "Precision Medicine / Genomics", "country": "Spain", "kind": "nonprofit_institute", "platforms": ["NovaSeq X"],
 "urls": [
  {"url": "https://www.incliva.es/wp-content/uploads/2026/03/Tarifas_Web_MP_2026.pdf", "type": "pdf", "current": true, "public": true, "verified": false, "as_of": "2026-03"}],
 "notes": "Sample line from search summaries: NovaSeq X 25B 2x100 lane EUR 2,141.08 at tier A."},
{"institution": "FISABIO (KNOWN CORE: extra URL)", "core": "Sequencing & Bioinformatics Platform", "country": "Spain", "kind": "nonprofit_institute", "platforms": ["Illumina"],
 "urls": [
  {"url": "https://fisabio.san.gva.es/media/upload/arxius/servicios/plataformas-cientifico-tec/servicios-cientifico-tec/secuenciacion/tarifas-secuenciacion-2023.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2023"}],
 "notes": "Older 2023 tariff for a known core."},
{"institution": "FAU Erlangen-Nürnberg (KNOWN CORE: extra URL)", "core": "Core Unit NGS", "country": "Germany", "kind": "university", "platforms": ["NovaSeq X"],
 "urls": [
  {"url": "https://www.med.fau.de/files/2024/11/NGS.pdf", "type": "announcement", "current": false, "public": true, "verified": false, "as_of": "2024-10"}],
 "notes": "Price-reduction notice dated 7 Oct 2024, effective 1 Jan 2025. Bulk RNA-seq fell from EUR 395 to 245."}
]}
```

Sources:
- [USEQ service fees](https://useq.nl/service-fees/)
- [UMC Utrecht USEQ services and fees](https://research.umcutrecht.nl/technologies/utrecht-sequencing-facility/services-fees/)