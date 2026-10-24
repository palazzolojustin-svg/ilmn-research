I found a handful of dated documents. Most of the cores returned nothing new.

- **Verified by opening:** none of the candidates below. I confirmed no document's dates and prices by opening it.
  - The TGen and UConn entries are confirmed only from search-result text.
  - The EPFL PDFs opened as compressed binary that the fetch tool couldn't read. I took their dates from the filenames and from the PDF metadata for November 2024. I did not see their sequencing prices.
  - The TGen `tgen.org/media/494096/...` and `tgen_csc_academic_price_list_09_13_24.pdf` URLs returned 404 when I fetched them. The search results showed their text, so they may be fetchable at other URLs.
- **ASU:** The ASU rates page we already have points to TGen sequencing runs, so I used TGen's Collaborative Sequencing Center lists as the older documents. Per the search text:
  - The April 2024 to March 2025 academic list shows a NovaSeq X Plus 25B lane at $2,883.17 and a 10B lane at $1,678.74.
  - The revised 09/13/2024 list shows the 25B lane at $2,883.16 and a PacBio Onso flow cell price cut.
  - The July 2026 to March 2027 list shows the 25B lane at $3,136.63 and the 10B lane at $1,413.47. I could only read its file metadata, not its prices.
- **UConn:** The honeycrisp booking pages are dated product listings with start and end dates. The `dxdev` mirror shows different, expired prices, such as $2,924.04 for a 25B 300-cycle lane ending 2025-12-31. These are snapshots of the same products we already have under different URLs. `products/329` is a product page we don't have yet.
- **No new dated documents** for these cores:
  - UTK
  - LJI
  - ECU
  - MSU (only the pages we already have)
  - Penn
  - SickKids (only the April 2025 list we already have)
  - UNH
  - Wisconsin (the 2024-06-27 research.wisc.edu post is the same article as `?p=57818`, with no rate sheet)
  - Colorado
  - IU
  - Genome Québec
  - SBP
  - AGRF
  - MOseq
  - Emory
  - SAMRC
- **Genome Québec:** The 2023-03-29 post announcing the NovaSeq X Plus and NextSeq 2000 states no prices.
- **Skipped as off-target:** The Calgary, Texas A&M and Northwestern lists, and other cores' price lists that came up in the searches.

```json
{"documents": [
{"core_id": "arizona-state-university--genomics-core-ngs-tgen-sequenc", "url": "https://tgen.org/media/494096/academic-price-list.pdf", "as_of": "2024-04", "kind": "pdf", "note": "TGen Collaborative Sequencing Center academic price list, Apr 1 2024 to Mar 31 2025; NovaSeq X Plus 25B lane $2,883.17, 10B lane $1,678.74. Seen in search text only; fetch returned 404."},
{"core_id": "arizona-state-university--genomics-core-ngs-tgen-sequenc", "url": "https://tgen.org/media/494312/tgen_csc_academic_price_list_09_13_24.pdf", "as_of": "2024-09", "kind": "pdf", "note": "TGen CSC academic price list revised 09/13/2024 for the Apr 2024 to Mar 2025 period; 25B lane $2,883.16, PacBio Onso flow cell price cut. Seen in search text only; fetch returned 404."},
{"core_id": "arizona-state-university--genomics-core-ngs-tgen-sequenc", "url": "https://www.tgen.org/media/x2dmuqf1/tgen_csc_academic_price_list_08-2026.pdf", "as_of": "2026-07", "kind": "pdf", "note": "TGen CSC academic list valid Jul 22 2026 to Mar 31 2027; per search text 25B lane $3,136.63, 10B lane $1,413.47. File metadata dated 2026-07-22; I could not read the prices. This is the current list, not an older one."},
{"core_id": "epfl--gene-expression-core-facility-", "url": "https://epfl.ch/research/facilities/gene-expression-core-facility/wp-content/uploads/2024/07/GECF-price-list-for-EPFL-users-01-July-2024.pdf", "as_of": "2024-07", "kind": "pdf", "note": "GECF internal price list effective 1 July 2024; date from filename, and the PDF text did not open."},
{"core_id": "epfl--gene-expression-core-facility-", "url": "https://epfl.ch/research/facilities/gene-expression-core-facility/wp-content/uploads/2024/11/GECF-price-list-for-EPFL-users-01-November-2024.pdf", "as_of": "2024-11", "kind": "pdf", "note": "GECF internal price list effective 1 November 2024; PDF metadata dated 2024-11-03, and the PDF text did not open."},
{"core_id": "university-of-connecticut--center-for-genome-innovation", "url": "https://honeycrisp.dxdev.core.uconn.edu/products/657", "as_of": "2025-07", "kind": "rate_page", "note": "dxdev mirror of NovaSeq Xplus 25B 300-cycle lane listing; $2,924.04 for 2025-07-01 to 2025-12-31 (differs from the main-site listing). Includes tariff and shipping."},
{"core_id": "university-of-connecticut--center-for-genome-innovation", "url": "https://honeycrisp.core.uconn.edu/products/329", "as_of": "2025-07", "kind": "rate_page", "note": "Additional honeycrisp NovaSeq X listing in search results (not in our list); dates and prices unverified, check start and end dates."},
{"core_id": "university-of-connecticut--center-for-genome-innovation", "url": "https://honeycrisp.dxdev.core.uconn.edu/products/358", "as_of": "2025-07", "kind": "rate_page", "note": "dxdev mirror listing, expired end date 2025-12-31 (e.g. 1.5B 100-cycle lane $1,452.20, 10B 200-cycle $1,576.76 per search text)."}
]}
```