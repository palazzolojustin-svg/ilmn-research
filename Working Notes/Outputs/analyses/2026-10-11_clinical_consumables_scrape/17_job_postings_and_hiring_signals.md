# Agent 17: Job postings and hiring signals

*Model: sonnet. Run 2026-10-11 02:06:04. Cost $0.60 (API-equivalent).*

**Assignment:** Paid scraping (Apify) was unavailable tonight, so gather job-posting evidence via WebSearch/WebFetch: search public job boards and company career sites (Greenhouse, Lever, Workday, LinkedIn public job pages, Indeed result snippets) for postings from roughly the last 90 days that mention 'NovaSeq X', 'NovaSeq 6000', 'Ultima' / 'UG 100', 'Element' / 'AVITI', 'AXELIOS' / 'SBX' at clinical labs (Natera, Guardant, Tempus, Caris, Exact, BillionToOne, GeneDx, Foundation Medicine, Myriad, NeoGenomics, Labcorp, Quest and others). Also Illumina's own hiring/layoff signals (functions, China, clinical market access, reagent rental/commercial finance) and Roche sequencing/Ultima/Element commercial and field-service build-outs. Record each posting (company, title, location, date, URL, platforms named). Write findings: counts by platform among clinical employers, notable validation/transition roles, and caveats about the small sample.

## Key findings

1. **The sample is very thin.** Paid scraping was unavailable, so I used WebSearch and WebFetch. I found about 12 usable postings in total, and only 3 clinical-lab postings name a specific sequencer. No posting reaches the "last 90 days, clinical employer, platform named" bar with a confirmed date. Treat everything below as anecdotal, not a count.
2. **Platform counts among clinical employers (n=3 postings naming a platform, 2 employers):** NovaSeq X / X Plus appears in 2 Natera Research Associate 2 postings (San Carlos, CA). Tempus names both "Novaseq6000 and NovaX" (Chicago). I found 0 clinical-lab postings naming Ultima UG 100, Element AVITI, or Roche AXELIOS/SBX. FACT for the postings. The zero is OPINION-weak, because search engines index job boards poorly and most postings say only "NGS."
3. **Parallel running of the 6000 and X is visible in at least one clinical lab.** Tempus's Molecular Technologist I/II (High Complexity, Chicago, third-shift differential) lists both "Illumina Novaseq6000 and NovaX platforms." That supports the Jefferies parallel-running question. The posting is dated only "6+ months ago," so it is probably roughly Q1 2026 or earlier. [Tempus via jobs.lightbank.com, fetched 2026-10-11](https://jobs.lightbank.com/companies/tempus/jobs/52994688-molecular-technologist-ii-high-complexity)
4. **Natera loads NovaSeq X Plus in its production sample-processing lab.** The search snippet for a Research Associate 2 (Sample Processing, San Carlos) says the role loads libraries on "NovaSeq and NovaSeq X Plus." A second 6-month contract RA2 on the RUO Oncology R&D team says "NovaSeq." Natera has not moved off Illumina in these postings. I could not confirm dates or full text, because the Greenhouse URLs redirected to the board index. [Natera RA2](https://job-boards.greenhouse.io/natera/jobs/6104899004), [Natera RA2 listing](https://startup.jobs/research-associate-2-natera-8820571), [Natera IVD Product Support RA1](https://job-boards.greenhouse.io/natera/jobs/5481489004), all via search snippet, 2026-10-11.
5. **Guardant postings name no platform.** Scientist II, Assay Development (Palo Alto, posted 2026-07-21, now closed) says only "NGS technologies" and "liquid biopsy sequencing technologies." [Guardant via Khosla jobs](https://jobs.khoslaventures.com/companies/guardant-health/jobs/86964588-scientist-ii-assay-development). This is not evidence for or against a switch.
6. **Ultima is building its field organization, with no clinical-validation roles visible.**
   - Senior Field Application Scientist, Fremont CA, posted 2026-04-23, with no clinical customers or platforms named. [Khosla](https://jobs.khoslaventures.com/companies/ultima-genomics-2/jobs/76000354-senior-field-application-scientist)
   - A remote Senior FAS ($120–140K) was reported as posted 2026-08-28; this date comes from a search snippet only.
   - Field Service Engineer II, Phoenix AZ (2026-08-07, $37–42/hr, snippet), and FSE II, Abu Dhabi. [Ultima Greenhouse](https://job-boards.greenhouse.io/ultimagenomics/jobs/5599289004)
   - FSE I development program, Fremont, and an Associate Strategic Accounts Director for Pharma and Biotech. [Ultima Greenhouse](https://job-boards.greenhouse.io/ultimagenomics/jobs/5821432004)
   - OPINION: this looks like a post-install support buildout for new US placements and the Gulf region. It is not a clinical-sales push.
7. **Roche is hiring for SBX/AXELIOS service and field applications in the US and EMEA.**
   - Field Service Engineer, Nordics, posted 2026-03-03 (closed), covering "SBX sequencing technology." [jobbsafari](https://jobbsafari.se/jobb/field-service-specialist-scsom-20051627)
   - Field Applications Scientist-Sequencing, US, posted 2026-05-22 ($90.3–167.7K, expired), about five weeks before the 29 Jun RUO launch. [jobRxiv](https://jobrxiv.org/job/field-applications-scientist-sequencing/)
   - A Field Applications Specialist NGS (Northeast, Boston/NY) and Field Application Specialist/Field Service Specialist roles appear on Hired/jobbsafari (undated).
   - An EMEA/LATAM Sequencing Service Support internship exists for "the introduction of the new AXELIOS 1 Sequencing Platform across the region." [Workingstudentjobs](https://www.workingstudentjobs.de/jobs/roche-internship-sequencing-service-support-emea-latam-1-e31cc257)
   - MGMT/OPINION: Roche hired field staff before the RUO launch, which fits the ~1/3 of ~100 first-year placements by September.
8. **Element is hiring commercial staff and promoting a cheaper system.** Element has an Inside Sales Representative posting tagged "Scale without the premium. Introducing VITARI™," with shipping planned for 2H 2026. [Element careers](https://www.elementbiosciences.com/careers/openings/6141076004) Element is also at ADLM 2026 and partnering with Revvity on newborn screening IVD (search snippets, 2026).
9. **No evidence found of a 2026 Illumina layoff.** The "10% of R&D / $100M cost cut / San Diego, Foster City, Madison, Singapore, UK" results are from June 2023, not 2026. [STAT, 2023-06-26](https://www.statnews.com/2023/06/26/illumina-to-lay-off-10-of-research-and-development-team-in-bid-to-cut-costs-by-100-million/) A search-engine summary presented them as 2026, so discount any recycled mention.
10. **Illumina WARN filings are small in 2026 and larger in 2025.**
    - 2026 San Diego WARN notices total 38 workers: 28 (5 Jan), 7 (19 Jan) and 3 (17 Feb). [LayoffTracker](https://www.layofftracker.us/layoffs/company/illumina/2026)
    - One further San Diego HQ notice affects 1 person (filed 14 Jan, effective 9 Mar). [WARNTracker](https://www.warntracker.com/layoff/illumina-2026-03-09)
    - The larger recent action was 172 employees (filed 17 Apr 2025, effective 16 Jun 2025), after 75 in July 2023. [Kadoa](https://www.kadoa.com/layoffs/company/illumina-worldwide-headquarters)
    - WARN covers only California sites at the 50+ threshold. It says nothing on China or other regions or on small cuts.
11. **Illumina is still posting commercial, clinical and market-access roles, which is not a contraction signal.**
    - Associate Director, Market Access & Value Evidence Strategy (US remote). [xtalks](https://xtalks.com/job/associate-director-market-access-and-value-evidence-strategy-remote/)
    - Clinical and Academic Senior Account Manager, South East UK (GLH, i.e. Genomic Laboratory Hub). [resumegeni](https://resumegeni.com/jobs/clinical-and-academic-senior-account-manager-south-east-glh-at-illumina-england-remote)
    - Senior Sequencing Sales Specialist (Boston/Cambridge), and a 2026 UK Business Finance placement. All are undated.
    - I found no "reagent rental" or "commercial finance" role of substance.
12. **The China context is documented, but I found no hiring or layoff data for China.** Illumina was added to China's Unreliable Entity List on 4 Feb 2025 and got an instrument-export ban on 4 Mar 2025. China allowed exports again from 10 Nov 2025, case by case (FACT, per FY2025 10-K). [10-K](https://www.sec.gov/Archives/edgar/data/1110803/000111080326000024/ilmn-20251228.htm)

## Postings log

| Company | Title | Location | Date | Platforms named | URL |
|---|---|---|---|---|---|
| Natera | Research Associate 2 (Sample Processing) | San Carlos, CA | undated | NovaSeq, NovaSeq X Plus | greenhouse.io/natera/jobs/6104899004 |
| Natera | RA2, 6-mo contract, RUO Oncology | San Carlos, CA | undated | NovaSeq | startup.jobs/research-associate-2-natera-8820571 |
| Natera | RA1, IVD Product Support | not recorded | undated | none confirmed | greenhouse.io/natera/jobs/5481489004 |
| Natera | RA / Sr RA (verification & validation) | Austin, TX | undated | none confirmed | ihirebiotechnology.com/jobs/view/478163629 |
| Tempus | Molecular Technologist I/II (High Complexity) | Chicago, IL | "6+ months ago" | NovaSeq 6000 and NovaSeq X | lightbank link above |
| Tempus | Sr. Research Associate (clinical NGS lab, new-test development) | not recorded | undated | none confirmed | via search snippet only |
| Guardant | Scientist II, Assay Development | Palo Alto, CA | 2026-07-21 | none ("NGS") | Khosla link above |
| Ultima | Sr FAS | Fremont, CA | 2026-04-23 | none | Khosla link above |
| Ultima | FSE II | Phoenix, AZ | 2026-08-07 (snippet) | none | Khosla |
| Roche | Field Service Engineer | Nordics | 2026-03-03 | SBX | jobbsafari link above |
| Roche | Field Applications Scientist-Sequencing | US | 2026-05-22 | none stated | jobRxiv link above |
| Element | Inside Sales Rep | not shown | undated | VITARI (marketing) | Element link above |

## Caveats

- **Sample size:** About 12 postings were found, against thousands that exist. The Natera and Tempus counts show only that these employers use Illumina. They don't measure share.
- **Dates:** Several postings are undated or "no longer accepting." Many boards (Greenhouse) redirect closed postings to the index, so full text was not verifiable.
- **Selection bias:** Search indexes favor aggregators, so absence of Ultima/Element/AXELIOS in clinical postings is weak evidence. Real clinical-lab migrations to non-Illumina platforms usually show first as validation or bioinformatics roles, which I did not find.
- **Corroborated adjacent fact:** Myriad bought an Ultima UG 100 for its South San Francisco "Lab of the Future" and is exploring ppmSeq for Precise MRD (press release, Oct 2024). NeoGenomics also has an Ultima collaboration (search snippet, date not captured). [Myriad release, via BioSpace](https://www.biospace.com/press-releases/myriad-genetics-and-ultima-genomics-to-explore-the-ug-100-sequencing-platform-to-advance-clinical-test-offerings-in-oncology-and-reproductive-genomics)

## Contradictions and stale data

- Search-engine summaries wrongly dated the June 2023 Illumina layoffs as "mid-2026" or "July 2026." The real 2026 WARN data show only about 38 California workers.
- The Tempus posting says "6+ months ago," and Roche's May 2026 and March 2026 postings are closed. None of these is a "current" signal.
- This corpus does not contradict the supplied key facts. The Tempus 6000-plus-X posting is directionally consistent with the "parallel running" and ~78% clinical X volume share.

## Gaps / what I could not find

- No dated postings at Caris, Exact, BillionToOne, GeneDx, Foundation Medicine, Myriad, NeoGenomics, Labcorp or Quest naming a specific sequencer.
- No clinical-lab job naming AVITI, UG 100 or AXELIOS/SBX.
- No Illumina China hiring or layoff data, and no 2026 non-California layoff data.
- No Illumina reagent-rental, commercial-finance or pricing-analyst postings.
- No Illumina headcount trend. The FY2025 10-K URL is above if someone wants the year-end employee count; I did not open it.
- I did not check Workday or LinkedIn directly. Fetching was blocked or returned index pages for most boards.
