This slice came up thin: only 6 cores have public prices I confirmed, and most NY and New England cores publish nothing public. Cores I could not find (or open) public NovaSeq X, AVITI or Ultima prices for:
- Gated or request-only: UMass Chan, Tufts, UVM, Columbia, NYU, Mount Sinai, Einstein, Rochester and Buffalo. Their pricing pages are login-gated or say "contact us", and some pages returned 403 or 404.
- Not in my results: Stony Brook (only a per-sample Sanger-type rate, no NGS lane prices), Syracuse/SUNY Upstate and Albany. MSK IGO and the Broad Genomics Platform also had no public lane prices.
- Not confirmed: Yale Center for Genome Analysis (YCGA) is in the JSON, but its page returned a 404 when I opened it, so its prices come only from search-result text.

Notes on the six cores:
- **MIT BioMicro Center:** Prices sit on openwetware wiki pages. The FY2025b page (last edited 2025-01-24) lists NovaSeq X 10B 300nt at $1,850 for core labs and $2,000 for MIT. Its Non-MIT column shows NA. It also lists AVITI prices. The main page (last edited 2025-04-15) lists NovaSeq X as "pricing in iLab" and says NovaSeq X runs happen at a sister shared resource, but it still shows AVITI prices. I saw no FY2024 or FY2026 versions. The FY2022 and FY2021 pages appeared in search results but were not opened.
- **Yale (YCGA):** Search-result text, not the page itself, gave NovaSeq X Plus 25B 2x150 at $2,936 for Yale users and $3,825 for non-Yale users, and AVITI at $1,428 and $1,864. The page header said FY2024-25 but another line said "7/1/2022 - 6/30/2023", so the dating is unclear.
- **Cornell BRC (Ithaca):** The price list shows only AVITI24 re-sequencing: a 400M lane costs $799 internal and $999 external. NovaSeq runs are contracted out and the pricing page lists no NovaSeq prices (the spotlight post, dated 2024-05-14, gives no prices either). The `/price-list/404` page itself has no date, so I set `as_of` to null for it.
- **BU Microarray and Sequencing Resource:** It publishes NextSeq 2000 and NextSeq 500 prices only, for example P1 100 cycles at $1,300 internal and $1,775 external. The page has no date.
- **UNH Hubbard Center for Genome Studies (HCGS):** NovaSeq X Plus 1.5B shared runs cost $3.00 per million read pairs at 2x150 and $5.00 at 2x300. It also lists PacBio Vega. Dedicated 5B, 10B and 25B flow cells are quote-only. The page shows a 2026 copyright but no price date.
- **Rockefeller Genomics Resource Center:** A FY27 price list PDF is linked from the pricing page, but I could not see its URL, so I list only the rate page. Search results showed an older FY2024 version covering NovaSeq 6000 and NextSeq, for example SP 2x50 at $4,300 for Rockefeller users. The core added an AVITI in Nov 2024 (announcement on the news page). Whether the FY27 list includes AVITI is unconfirmed.
- **Brown:** The FY26 rate table (effective 2025-12-10) lists only NextSeq 2000 assisted use at $554 internal and $980 external per run, plus variable supply fees. NovaSeq and AVITI are not listed, so it is a weak fit.

Harvard Bauer Core and UConn CGI are already on your known list. In search results I saw Bauer FY26 and FY27 NGS pages, and a UConn service-rates page updated January 2025. I list them below as extra URLs for those two cores.

```json
{"cores": [
{"institution":"Massachusetts Institute of Technology","core":"BioMicro Center","country":"US","kind":"university","platforms":["NovaSeq X","NovaSeq 6000","AVITI"],
"urls":[
{"url":"https://openwetware.org/wiki/BioMicroCenter:Pricing","type":"rate_page","current":true,"public":true,"verified":true,"as_of":"2025-04"},
{"url":"https://openwetware.org/wiki/BioMicroCenter:PricingFY2025b","type":"rate_page","current":false,"public":true,"verified":true,"as_of":"2025-01"},
{"url":"https://openwetware.org/wiki/BioMicroCenter:PricingFY2025","type":"rate_page","current":false,"public":true,"verified":false,"as_of":null},
{"url":"https://openwetware.org/wiki/BioMicroCenter:PricingFY2023b","type":"rate_page","current":false,"public":true,"verified":false,"as_of":null},
{"url":"https://openwetware.org/wiki/BioMicroCenter:PricingFY2023","type":"rate_page","current":false,"public":true,"verified":false,"as_of":null},
{"url":"https://openwetware.org/wiki/BioMicroCenter:PricingFY2022","type":"rate_page","current":false,"public":true,"verified":false,"as_of":null},
{"url":"https://openwetware.org/wiki/BioMicroCenter:PricingFY2021","type":"rate_page","current":false,"public":true,"verified":false,"as_of":null}],
"notes":"Wiki-hosted. FY2025b: AVITI 150 PE one lane (~400M reads) core lab $1,375 / MIT $1,513 / non-MIT $1,925; NovaSeq X 10B 300nt core lab $1,850 / MIT $2,000 (non-MIT NA). Main page says NovaSeq X pricing is in iLab only. No FY2024 or FY2026 page linked; main page last edited 2025-04-15, so a newer price list may exist elsewhere."},
{"institution":"Yale University","core":"Yale Center for Genome Analysis (YCGA)","country":"US","kind":"university","platforms":["NovaSeq X","NovaSeq 6000","AVITI"],
"urls":[
{"url":"https://medicine.yale.edu/genetics/research/ycga/service-fees","type":"rate_page","current":true,"public":true,"verified":false,"as_of":null}],
"notes":"Page returned HTTP 404 when I fetched it, but it appeared in two search results. The search snippet showed NovaSeq X Plus 25B 2x150 flow cell $2,936 Yale / $3,825 non-Yale and AVITI $1,428 / $1,864. Header said FY2024-25 but also had a stale '7/1/2022 - 6/30/2023' line, so verify the dating."},
{"institution":"Cornell University (Ithaca)","core":"Biotechnology Resource Center (BRC) Genomics / Epigenomics Facility","country":"US","kind":"university","platforms":["AVITI","NovaSeq X","NovaSeq 6000"],
"urls":[
{"url":"https://www.biotech.cornell.edu/core-facilities-brc/price-list/404","type":"rate_page","current":true,"public":true,"verified":true,"as_of":null},
{"url":"https://biotech.cornell.edu/core-facilities-brc/price-list","type":"rate_page","current":true,"public":true,"verified":false,"as_of":null},
{"url":"https://www.biotech.cornell.edu/core-facilities-brc/services/element-aviti24-sequencing-cytoprofiling-situ-rna-seq-atlas-antibody","type":"rate_page","current":true,"public":true,"verified":false,"as_of":null},
{"url":"https://biotech.cornell.edu/spotlight/new-services-brc-genomics-facility-lower-cost-novaseqx-novaseq6000-sequencing-runs-udi","type":"announcement","current":false,"public":true,"verified":true,"as_of":"2024-05"}],
"notes":"AVITI24 re-sequencing lane (400M) $799 internal / $999 external; flow cell (800M) $1,598 / $1,998. NovaSeq runs are outsourced and no dollar amounts are shown publicly (order via portal). The price list page has no date."},
{"institution":"Boston University","core":"Microarray and Sequencing Resource (BUMSR)","country":"US","kind":"academic_medical_center","platforms":["NextSeq 2000","NextSeq 500"],
"urls":[
{"url":"https://www.bumc.bu.edu/microarray/pricing/","type":"rate_page","current":true,"public":true,"verified":true,"as_of":null}],
"notes":"No NovaSeq/AVITI/UG; NextSeq 2000 P1-P4 only. NextSeq 2000 XLEAP P1 100 cycles $1,300 internal / $1,775 external (per run). The page has no date."},
{"institution":"University of New Hampshire","core":"Hubbard Center for Genome Studies (HCGS)","country":"US","kind":"university","platforms":["NovaSeq X"],
"urls":[
{"url":"https://hcgs.unh.edu/services-pricing","type":"rate_page","current":true,"public":true,"verified":true,"as_of":"2026"}],
"notes":"NovaSeq X Plus 1.5B shared run 2x150: $3.00 per million read pairs (internal); 2x300: $5.00. Dedicated 5B/10B/25B are quote-only. PacBio Vega is also listed. Prices reviewed annually."},
{"institution":"Rockefeller University","core":"Genomics Resource Center","country":"US","kind":"university","platforms":["NovaSeq 6000","NextSeq 2000","AVITI"],
"urls":[
{"url":"https://www.rockefeller.edu/genomics/pricing/","type":"rate_page","current":true,"public":true,"verified":true,"as_of":"2026-07"},
{"url":"https://www.rockefeller.edu/genomics/news/","type":"announcement","current":true,"public":true,"verified":true,"as_of":"2024-11"}],
"notes":"Page links a 'Genomics Resource Center Price List FY27' PDF (I did not see its URL; get it from the pricing page). Search results showed the earlier FY2024 list (e.g. NovaSeq SP 2x50 $4,300 RU / $5,800 external academic). AVITI added 2024-11-26 (news post, no prices). Whether the FY27 list has AVITI prices is unconfirmed."},
{"institution":"Brown University","core":"Genomics Core Facility","country":"US","kind":"university","platforms":["NextSeq 2000"],
"urls":[
{"url":"https://biomedcorefacilities.brown.edu/genomics-facility","type":"rate_page","current":true,"public":true,"verified":true,"as_of":"2025-12"}],
"notes":"Weak fit: only NextSeq 2000 assisted-use run fee ($554 internal / $980 external academic, FY26, effective 12/10/2025) plus variable supply fees. NovaSeq and AVITI are not listed."},
{"institution":"Harvard University","core":"Bauer Core Facility (FAS)","country":"US","kind":"university","platforms":["NovaSeq X","NextSeq 1000"],
"urls":[
{"url":"https://bauercore.fas.harvard.edu/fy27-ngs-sequencing","type":"rate_page","current":true,"public":true,"verified":false,"as_of":"2026-07"},
{"url":"https://bauercore.fas.harvard.edu/fy26-ngs-sequencing","type":"rate_page","current":false,"public":true,"verified":false,"as_of":"2025-07"}],
"notes":"Already known; extra URLs only. From search snippets: FY27 25B 300-cycle lane about $2,426 (Harvard account) / $3,396 (PO); FY26 about $2,059 / $2,883."},
{"institution":"University of Connecticut","core":"Center for Genome Innovation","country":"US","kind":"university","platforms":["NovaSeq X","NovaSeq 6000"],
"urls":[
{"url":"https://genome.center.uconn.edu/?p=891","type":"rate_page","current":false,"public":true,"verified":false,"as_of":"2025-01"}],
"notes":"Already known; extra URL only (service rates updated January 2025; S1 v1.5 100-cycle kit $4,431, plus a shipping surcharge)."}
]}
```

Sources:
- [MIT BioMicro Center pricing](https://openwetware.org/wiki/BioMicroCenter:Pricing)
- [MIT FY2025b](https://openwetware.org/wiki/BioMicroCenter:PricingFY2025b)
- [UNH HCGS](https://hcgs.unh.edu/services-pricing)
- [Cornell BRC price list](https://www.biotech.cornell.edu/core-facilities-brc/price-list/404)
- [BU pricing](https://www.bumc.bu.edu/microarray/pricing/)
- [Brown genomics facility](https://biomedcorefacilities.brown.edu/genomics-facility)
- [Rockefeller pricing](https://www.rockefeller.edu/genomics/pricing/)
- [Rockefeller news](https://www.rockefeller.edu/genomics/news/)
- [Yale service fees](https://medicine.yale.edu/genetics/research/ycga/service-fees)