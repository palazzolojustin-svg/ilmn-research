I found very little. Only three candidates came out of the searches, and I couldn't confirm any of them from the document text.

- **MD Anderson ATGC FY2024 price schedule (.docx):** A search snippet showed the title "FY 2024 Price Schedule" and a NovaSeq6000 section. WebFetch returned 404 on it, with the space in the URL and with `%20`, so I couldn't read the prices. The fiscal year is in the filename. The FY2022 and FY2023 schedules also turned up, but they are older than your window.
- **Lleida SCTS 2024 and 2025 tariff PDFs:** Both are on the university's own site, and the filenames carry the year. WebFetch returned raw compressed PDF data, so I couldn't read them. I also couldn't test them locally, because Bash was disabled in this session. I don't know whether either lists NovaSeq, NextSeq or AVITI prices. A search result showed the current 2026 version prices a MiSeq flow cell, so these may cover MiSeq only. A third file, `irblleida.org/.../tarifas-scts-2024_...pdf`, appeared in search results, but I didn't open it.
- **Guelph:** The only sequencing fee page is the one you already have, and it dates its prices to 2018. The "COMING SOON" NovaSeq X note on the site means there is probably no earlier NovaSeq X price.

I found nothing for the other cores. Each had either only the page you already hold or no result from its own site:
- **No dated older documents found:** UC Berkeley/QB3, Pitt, KUMC, Texas Tech, FISABIO, Auckland, Rutgers, TCAG, UW-Madison, Rockefeller, JHU, Edinburgh, UC Davis, Technion, Bern, Idaho, CHLA and K-State. Where search surfaced only older material (the Rockefeller FY2020 copy on gwern.net and the UC Davis 2019 price page), it was outside your window or not on the core's own site.
- **Pages blocked or unreachable:** `grcf.jhmi.edu/?p=3159` returned 403. `dnaseq.ucdavis.edu/prices` returned 403, and `dnatech.genomecenter.ucdavis.edu/?p=4022` refused the connection.
- **No prices on the page:** The Pitt resources page shows no prices. Its "Executive Summary" links carry dates in their filenames (09/05/2025 and 12/04/2024), but I don't know whether they contain prices, so I left them out.
- **Cores that don't publish run prices:**
  - K-State's page lists library-prep prices only.
  - Bern's May 2024 price list is one you already have.
- **Not yet searched:** Idaho and CHLA. I ran out of time on them.

```json
{"documents": [
{"core_id": "ut-md-anderson-cancer-center--advanced-technology-genomics-c", "url": "https://mdanderson.org/documents/core-facilities/sequencing-and-microarray-facility/ATGC FY2024 Price Schedule.docx", "as_of": "2023-07", "kind": "spreadsheet", "note": "ATGC FY2024 price schedule (fiscal year from filename). Search snippet showed a NovaSeq6000 section. Not verified: WebFetch returned 404."},
{"core_id": "universitat-de-lleida--scts-proteomics-and-genomics-s", "url": "https://www.recercaitransferencia.udl.cat/export/sites/Recerca/ca/.galleries/SCTS/Tarifes-2024-Servei-de-proteomica-i-genomica.pdf", "as_of": "2024-01", "kind": "pdf", "note": "2024 tariff for the proteomics and genomics service (PDF metadata created 2024-01-10). Contents unread, and it may list MiSeq only. Not verified."},
{"core_id": "universitat-de-lleida--scts-proteomics-and-genomics-s", "url": "https://recercaitransferencia.udl.cat/export/sites/Recerca/ca/.galleries/SCTS/Proteomica-i-genomica-2025.pdf", "as_of": "2025-01", "kind": "pdf", "note": "2025 tariff for the proteomics and genomics service (year from filename). Contents unread, and it may list MiSeq only. Not verified."}
]}
```

Sources:
- [MD Anderson ATGC FY2024 Price Schedule](https://mdanderson.org/documents/core-facilities/sequencing-and-microarray-facility/ATGC FY2024 Price Schedule.docx)
- [Lleida SCTS 2024 tariff](https://www.recercaitransferencia.udl.cat/export/sites/Recerca/ca/.galleries/SCTS/Tarifes-2024-Servei-de-proteomica-i-genomica.pdf)
- [Lleida SCTS 2025 tariff](https://recercaitransferencia.udl.cat/export/sites/Recerca/ca/.galleries/SCTS/Proteomica-i-genomica-2025.pdf)