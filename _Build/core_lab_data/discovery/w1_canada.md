Few Canadian cores publish NGS prices publicly. I found about 4 usable ones, well short of the 15–30 target, so the slice looks thin rather than under-searched. I did not find public prices for McGill Genome Centre, UHN Princess Margaret, Lunenfeld-Tanenbaum, BC Cancer Genome Sciences Centre, IRIC, Laval, Dalhousie, Manitoba, Saskatchewan, Queen's, Western or Sherbrooke. Their price lists are probably quote-only or behind a login.

- **Calgary CHGI** is the best source. It has dated internal price lists back to 2022–23 (CAD). The 2025 list shows NovaSeq X 25B, one lane, PE150, at $4,100. That price was unchanged from the June 2024 list, which is useful for a $/Gb time series. The same lists price NovaSeq 6000, NextSeq 2000 and MiSeq.
  - The lists are PDFs I could not read directly. I saw their content only through search snippets, so they are marked unverified.
  - The CHGI pricing page is `https://cumming.ucalgary.ca/research/cat/health-genomics/pricing`. I did not open it, so it is not in the JSON.
- **OICR Genomics** publishes Ultima UG100 prices for academics (CAD), with no date on the page. A 10B wafer is $5,130 (2-wafer minimum) and 30X WGS is $435 per sample (20-sample minimum). I did not find NovaSeq X prices for OICR.
- **UBC Biomedical Research Centre (Next-Gen Sequencing Core)** has dated NextSeq 2000 price sheets: Jan 2024, Nov 2024 and Feb 2025. The sheets say NovaSeq is available on request, and I saw no AVITI. All three URLs returned 404 when I opened them, though they appeared in search results. They are marked unverified, and I listed them as non-public since I couldn't confirm they are reachable.
- **Génome Québec (CES, CHU Sainte-Justine)** publishes per-sample all-inclusive CAD prices on a NovaSeq X workflow. Human WGS is $525, Exome 100X is $316, and mRNA at 25M reads is $172. The page is undated and has no per-lane prices.
- **University of Guelph AAC** has an NGS fee page. It prices only a NextSeq 1000 P1 25M-read cartridge at $1,425 for internal users, from mostly 2018 prices. NovaSeq X is "contact facility", with installation expected June 2026. It is not useful for the time series.
- **Ottawa StemCore (OHRI), McMaster Farncombe and Sherbrooke RNomics** have service pages with no prices. Sherbrooke's page is MiSeq only. StemCore uses Infinity, a login system. I left all three out of the JSON.
- **The Lunenfeld-Tanenbaum NGS page** is `https://nbcc.lunenfeld.ca/facilities/next-gen-sequencing`. It appeared only in a search summary and I did not open it. I saw no rates and left it out of the JSON.

```json
{"cores": [
{"institution": "University of Calgary (Cumming School of Medicine)", "core": "Centre for Health Genomics and Informatics (CHGI) NGS", "country": "Canada", "kind": "university", "platforms": ["NovaSeq X", "NovaSeq 6000", "NextSeq 2000"],
 "urls": [
 {"url": "https://cumming.ucalgary.ca/sites/default/files/teams/97/2025%20CHGI%20Internal%20Price%20List.pdf", "type": "pdf", "current": true, "public": true, "verified": false, "as_of": "2025-01"},
 {"url": "https://live-cumming.ucalgary.ca/sites/default/files/teams/97/CHGI%20Internal%20UofC%20Price%20List%20with%20sales%202024-2025.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2024-04"},
 {"url": "https://cumming.ucalgary.ca/sites/default/files/teams/97/CHGI%20Internal%20Price%20List%20June%202024.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2024-06"},
 {"url": "https://cumming.ucalgary.ca/sites/default/files/teams/97/CHGI%20Internal%20Library%20%26%20Seq%20Price%20List%202023-2024%20v2_0.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2023-04"},
 {"url": "https://cumming.ucalgary.ca/sites/default/files/teams/97/CHGI%20Internal%20Library%20%26%20Seq%20Price%20List%202022-2023.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2022-04"}
 ],
 "notes": "Internal CAD prices per search snippets; PDFs not readable via fetch. Sample: NovaSeq X 25B one lane 300cyc PE150 $4,100 (June 2024 and 2025 lists, same price; run in partnership with BC Genome Sequencing Centre). NovaSeq 6000 S4 300cyc $22,420 (2025). Possibly a newer 2026 list exists; not found."},
{"institution": "Ontario Institute for Cancer Research", "core": "OICR Genomics (Ultima sequencing)", "country": "Canada", "kind": "nonprofit_institute", "platforms": ["UG100"],
 "urls": [
 {"url": "https://genomics.oicr.on.ca/ultima-sequencing/", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": null}
 ],
 "notes": "Academic-only list prices in CAD, undated. Sample: UG100 10B wafer $5,130 (min 2 wafers); 30X WGS $435 (min 20 samples). A search snippet suggested an older page version with a different table; no archived versions found, so the Wayback Machine may help for history. No NovaSeq X prices found."},
{"institution": "University of British Columbia", "core": "Biomedical Research Centre Next-Gen Sequencing Core (SBME price sheets)", "country": "Canada", "kind": "university", "platforms": ["NextSeq 2000"],
 "urls": [
 {"url": "https://bme.ubc.ca/wp-content/uploads/2025/02/2025-Feb-SBME-Seq-Price-Sheet.pdf", "type": "pdf", "current": true, "public": false, "verified": false, "as_of": "2025-02"},
 {"url": "https://bme.ubc.ca/wp-content/uploads/2024/11/2024-Nov-SBME-Seq-Price-Sheet.pdf", "type": "pdf", "current": false, "public": false, "verified": false, "as_of": "2024-11"},
 {"url": "https://bme.ubc.ca/wp-content/uploads/2024/01/2024-Jan-SBME-Seq-Price-Sheet.pdf", "type": "pdf", "current": false, "public": false, "verified": false, "as_of": "2024-01"},
 {"url": "https://brc.ubc.ca/?p=2723", "type": "rate_page", "current": true, "public": true, "verified": false, "as_of": null}
 ],
 "notes": "All three PDFs returned 404 when opened but appeared in search results; they may have moved. brc.ubc.ca/?p=2723 appeared in a search result and was not opened. Sample from snippet: NextSeq 2000 P3 300cyc $8,200 (Nov 2024 academic). NovaSeq is 'available upon request'. No AVITI seen."},
{"institution": "Genome Québec", "core": "Centre d'expertise et de services Génome Québec (CES)", "country": "Canada", "kind": "nonprofit_institute", "platforms": ["NovaSeq X"],
 "urls": [
 {"url": "https://genomequebec.com/en/technological-services/promotions/", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": null}
 ],
 "notes": "Per-sample all-in CAD prices, not per lane, undated. Sample: Human WGS $525; Exome 100X $316; mRNA 25M reads $172. Page says prices reflect NovaSeq X and the 25B flow cell. Useful only as a per-sample proxy."},
{"institution": "University of Guelph", "core": "Advanced Analysis Centre (AAC) Genomics Facility", "country": "Canada", "kind": "university", "platforms": ["NextSeq"],
 "urls": [
 {"url": "https://www.uoguelph.ca/aac/print/facilities/genomics/fees/next-generation-sequencing", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": null},
 {"url": "https://uoguelph.ca/aac/node/260", "type": "rate_page", "current": true, "public": true, "verified": false, "as_of": null}
 ],
 "notes": "Low value. NextSeq 1000 P1 600cyc 25M reads $1,425 internal (prices largely from 2018). NovaSeq X listed as 'contact facility' with installation expected June 2026. This may change once NovaSeq X goes live."}
]}
```

Sources:
- [CHGI 2025 internal price list](https://cumming.ucalgary.ca/sites/default/files/teams/97/2025%20CHGI%20Internal%20Price%20List.pdf)
- [OICR Ultima sequencing](https://genomics.oicr.on.ca/ultima-sequencing/)
- [Génome Québec NGS services](https://genomequebec.com/en/technological-services/promotions/)
- [UBC Feb 2025 sequencing price sheet](https://bme.ubc.ca/wp-content/uploads/2025/02/2025-Feb-SBME-Seq-Price-Sheet.pdf)
- [University of Guelph NGS fees](https://www.uoguelph.ca/aac/print/facilities/genomics/fees/next-generation-sequencing)