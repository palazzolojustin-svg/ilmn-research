# Agent 119: C-web-clinical-lab-sequencer-capacity-build-evidence-instrument-counts-and-facility-filing

*Model: sonnet. Run 2026-10-11 11:14:37. Cost $0.83 (API-equivalent).*

**Assignment:** Estimate physical sequencing capacity at the largest clinical customers and whether 6000s are being run in parallel with Xs, using sources not used before: (1) lab-expansion press releases, state/local economic-development and tax-incentive filings, building permits, CLIA/CAP lab-facility news and earnings-call remarks for Natera (Austin, TX; Sunnyvale), Guardant (Palo Alto/Redwood City, Lake Forest), Tempus (Chicago), Caris (Irving TX), GeneDx (Stamford, Durham), BillionToOne (Menlo Park), GRAIL (Durham), Exact/Abbott (Madison), Myriad (Salt Lake City), Labcorp/Quest/Natera/Invitae legacy sites, Foundation Medicine (Cambridge/Morrisville), Adaptive, Veracyte, Personalis, Ambry, Fulgent, Eurofins, plus Ultima/Element/Roche customer-lab announcements. Search for numbers of NovaSeq X/6000 instruments, 'NovaSeq X Plus', 'fleet', 'sequencers', 'capacity', 'utilization', 'decommission', 'retire NovaSeq 6000'. (2) 10-K/10-Q property & capex text and investor-presentation slides that state sequencer counts, utilisation or Gb capacity (e.g. Natera/Guardant/Tempus/Caris investor decks 2025-26, Caris S-1, Tempus S-1, BillionToOne S-1 'sequencing capacity' sections). (3) Illumina press releases or customer case studies (illumina.com/company/news-center, customer stories) naming clinical labs that bought X systems and the instrument counts. Quantify: instruments per lab, implied annual Gb capacity (use ~ 8 Tb/day class X Plus figures only if cited) versus stated volumes, and an estimate of how many of the ~1,360 remaining 6000s sit at clinical labs. Cite publisher, date, URL; label FACT/MGMT/OPINION; flag where numbers are my inference.

## Key findings

Only a few items are new, and the 10-K wording on Caris's 6000-versus-X mix is unverified. I checked Natera, Caris, Tempus, GeneDx, BillionToOne and Guardant. Only Caris and Natera yielded capacity figures.

- **Caris ran "over 50" NovaSeq systems and "over one trillion reads per day"** across four labs totalling "over 275,000 square feet". The S-1/A is from 2025, and an earlier S-1 search snippet says 50 systems as of 31 Mar 2025. FACT. [Caris S-1/A, 2025, https://www.sec.gov/Archives/edgar/data/2019410/000110465925059635/tm2415719-23_s1a.htm]. This is the only hard clinical-lab instrument count I found. It is not in the ledger.
- **Caris's 10-K FY25 reportedly says its Arizona labs use "NovaSeq 6000 and NovaSeq X".** This comes from a search-engine summary only. A direct fetch of the 10-K returned nothing on NovaSeq, so treat it as unverified. If it holds, it is a company statement that 6000s and Xs run in parallel at Caris. It would support E022's anecdotal job-posting evidence with a filing. [Caris 10-K FY25, https://www.sec.gov/Archives/edgar/data/2019410/000201941026000016/cai-20251231.htm]
- **Natera announced the Austin build on 21 May 2026.** It is a "dedicated sequencing facility" expected to have "the largest sequencing capacity in the world", plus space in a second building, with "up to 400 new jobs". No sequencer count, model, investment or incentive is stated. FACT. [Natera release, https://www.natera.com/company/news/natera-announces-expansion-in-austin-creating-what-is-believed-to-be-the-largest-sequencing-facility-in-the-world/]
  - MGMT: John Fesko (President and Chief Business Officer) said they are "expanding our lab space and sequencing capacity".
  - The release ties the build to oncology volume growth of 54% in Q1 2026.
  - The ledger's Natera items (E081, E089, E109) cover volume, ASP and the supply agreement, not this build.
  - One WebFetch summary of the Q4 copy of the release said "San Antonio, $150M, 500 jobs, Texas Enterprise Fund, operational 2028". That contradicts the Natera-site copy and the trade-press copy. I discarded it as probably a hallucination or a mis-summary. Do not use it.
- **A Texas permit filing puts a number on the Austin build.** The project is "Natera Pista – Level 3 South", owner 13011 McCallen Pass LLC. It converts existing office space into "24,000 sf of new lab space" (30,000 sq ft total) at an estimated cost of $9.9M. Work ran 15 Apr 2025 to 15 Dec 2025. FACT. [Texas Dept of Licensing and Regulation, registered 21 Feb 2025, https://www.tdlr.texas.gov/TABS/Search/Print/TABS2025012493]
  - Natera's Austin lease was about 94,000 sq ft per its 10-K (search snippet, extended to March 2033).
  - I cannot say whether this permit is part of the "dedicated sequencing facility". That link is my inference.
  - $9.9M is a fit-out cost, not equipment spend.
- **Tempus's Chicago lab:** the S-1 and 10-K snippets give about 217,000 sq ft (lease to Feb 2029). Its older sequencing-lab material says "current capacity of over 100,000 patients annually" (the 2018 PDF at tempus.com/wp-content/uploads/2018/06/Lab_052418.pdf). It has no instrument count. This is stale, and I did not open the 10-K FY25.
- **Illumina placements (corroborates the known "multi-unit" colour, adds dates).** The Q1'26 call quoted "more than 80" X placements. The Q2'26 call quoted "more than 95", with "several multi-unit capacity expansion orders" from clinical customers (search summaries of the nasdaq.com and fool.com transcripts).
- **Non-US clinical X purchases (Jan 2026):** Agilus Diagnostics (Fortis) installed an X in Mumbai, and Metropolis Healthcare launched a genomics centre on the X Series. Both are small and carry no counts. [biospectrumindia.com, Jan 2026]

## Capacity maths (OPINION, my inference)

- **Caris reads per instrument.** More than 1 trillion reads/day over more than 50 systems is about 20B reads/day per system, or about 7 trillion reads/year per system at full utilisation. That is roughly one 25B-read flow-cell-equivalent per system per day. This shows an installed-capacity ceiling, not Caris's actual use.
- **Caris Gb.** Cost per case is about $1,300–1,425 (existing ledger item, Caris Q2'26 10-Q). Its comment that it can "increase our capacity and decrease our cost of goods simultaneously" (E092) fits a fleet being re-based onto X. I cannot size how much of the fleet is still 6000.
- **How many of the ~1,360 6000s sit at clinical labs.** Not resolvable from public sources. The only counts are Caris (50+, mixed generations) and Discovery Life Sciences' target of five X Plus systems (April 2023, 256today.com), which was not a clinical-scale example. The top five labs (Natera, Guardant, Tempus, Caris, GeneDx) might hold on the order of 150–250 6000-class systems combined. That is a pure guess with no source behind it.

## Contradictions and stale data

- The Natera Q4-copy summary (San Antonio, $150M, 500 jobs) conflicts with the primary release, as noted above. Use the Natera-site release.
- Caris's S-1 count (50 as of Mar 2025) is 18 months old. Caris likely added X units since, and I have no current count.
- The Tempus capacity figure is 2018-era.
- The earlier ledger (E022) lists only job-posting evidence for parallel running. The Caris 10-K wording, if verified, would be the first filing-level support.

## Gaps / what I could not find

- No sequencer counts for Natera, Guardant, GeneDx, BillionToOne, GRAIL, Exact, Myriad, Foundation, Veracyte or Fulgent. The searches returned nothing, and the Natera 10-K Item 2 was not in the fetch excerpt.
- No incentive filings: the Texas Enterprise Fund and Chapter 380/313 agreements for Natera, and Durham or NC economic-development (JDIG) filings for GRAIL and GeneDx.
- No 10-K text on retiring or decommissioning 6000s at any named lab.
- The BillionToOne S-1 sequencing section was not located. Its job pages mention a new Austin lab opening in 2027, and the S-1 itself was not fetched.
- Ultima, Element and Roche customer-lab announcements were not covered. Another agent (files 100–105) already took the Novogene phase-out and Discovery Life Sciences.
- Next step: fetch the full Natera and Caris FY25 10-Ks on EDGAR (Item 1 and Item 2) and Caris's Q2'26 transcript, and search the EDGAR full-text index for "NovaSeq X" in 2026 10-Qs.

Sources:
- [Caris S-1/A](https://www.sec.gov/Archives/edgar/data/2019410/000110465925059635/tm2415719-23_s1a.htm)
- [Caris 10-K FY25](https://www.sec.gov/Archives/edgar/data/2019410/000201941026000016/cai-20251231.htm)
- [Natera Austin release](https://www.natera.com/company/news/natera-announces-expansion-in-austin-creating-what-is-believed-to-be-the-largest-sequencing-facility-in-the-world/)
- [TDLR permit filing](https://www.tdlr.texas.gov/TABS/Search/Print/TABS2025012493)
- [Trade & Industry Development](https://www.tradeandindustrydev.com/region/texas/news/tx-natera-announces-expansion-austin-creating-what-35889.md)
