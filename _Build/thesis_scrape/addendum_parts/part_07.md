## Where the evidence is thin, and what to look at next

The scrape is strong on posted prices and public data. It is weak in exactly the places that matter most for the short. There is almost no direct evidence on three things:

- **The clinical 6000 tail.** About 80% of remaining 6000 output is clinical, and clinical labs do not deposit data publicly.
- **Illumina's net price to its largest accounts.** Every price seen is a core resale rate, a government purchase or a published schedule.
- **Roche's AXELIOS.** It launched on 29 Jun 2026 and has not yet appeared in any price list, tender or public dataset.

The items below are the most useful next steps.

**Gaps that weaken each thesis leg**

- **1A (the clinical tail).**
  - GTR registry data is stale [D012]. Public databases are research-weighted and lag about two years [D052].
  - Untested sources that could count the regulated 6000Dx base directly:
    - European device-safety notices, which often state units in distribution (BfArM, MHRA).
    - External quality-assessment reports listing lab platforms (EMQN; PDF unreadable here).
    - UK lab accreditation schedules (UKAS; PDFs).
  - Job postings that name the 6000 versus the X would show labs mid-conversion. The Indeed scrape returned only two postings, so a broader scrape is needed.
- **1B (net prices).** The best untested lead is the Element v. Illumina amended antitrust complaint (N.D. Cal. 5:25-cv-08026). Because the first complaint was dismissed for lack of specifics, the amended version should name discount conditions and customers. Federal transaction-level kit purchases (USAspending) need a POST-capable tool.
- **1C (volume).**
  - The Natera, BillionToOne and GeneDx Q3 2026 results (early to mid November) will test three things: whether the NIPT re-acceleration holds, whether MRD adds slow as Natera guided, and whether GeneDx's genome mix keeps falling.
  - Natera's cost of goods implies Illumina spend of tens of petabytes (PB) a quarter at $2–4/Gb. That is far above the ~1–2 PB a quarter its test counts suggest. This inconsistency is unresolved.
- **2A and 2B (research).**
  - AXELIOS: look for ASHG 2026 abstracts (embargoed during the scrape) and the first core rate cards listing AXELIOS or the 35B flow cell. None existed as of 12 Oct.
  - The AAMC's September NIH brief will give final FY26 grant counts.
  - The ASCP 2026 lab vacancy survey results are due in late 2026 or 2027.

**Dated datapoints coming soon**

- **14 Oct 2026:** NHRI's Illumina outsourcing lot award, budget NT$8.80M (−37% vs 2023).
- **20 Oct 2026:** Taipei VGH's Illumina high-throughput maintenance tender opens. The model is not named.
- **After 16 Nov 2026:** Osaka University's 78-line award, covering X 25B/10B/1.5B kits, MGI kits and 10x kits. It would give realized Japanese prices.
- **Pending Apify jobs:**
  - A04: Japanese and Taiwanese award notices, plus any later Open Offer schedules.
  - A05: university pages publishing Illumina discount percentages, and cores that left Illumina over price.
  - A06: eBay sold prices for used 6000s and surplus S4 kits.
  - A07: archived Pitt price tables for a 2023–25 series.

**Documents already downloaded but unread.** The environment had no PDF text extractor, so a run with `pdftotext` or `python -I` plus pypdf should read these first:

- Element's JPM 2026 deck with speaker notes.
- Northwestern's "State of the Core 2024".
- UCLA's 2024 rate sheets.
- EPFL's 9 Sep 2026 price list.
- CMS's 2025 Part B national summary file (ZIP).
- William Blair's survey of 169 OB-GYNs on prenatal testing.
- OIG's top-25 Medicare lab test table.
- The Dutch RIVM NIPT monitor.
- Rush and Utah core updates.
- Kyoto University fee tables.
- Japanese PMDA package inserts.

**Conflicts to resolve**

- Element's 2025 revenue: $58M (Substack) vs ~$85M (GenomeWeb).
- The Open Offer top discount tier: ≥$50M or ≥$100M of annual spend.
- Whether NHRI's Dec 2023 S4 award really covers 16 kits (≈$2/Gb) [D067].
- Whether the Health Canada and Agriculture Canada C$405K instruments are one purchase [F510].
- The X software v1.4.0 release date: Mar 2026 or Jul 2026.
- UMGC's AVITI pricing sheet vs its live price page [F1067].

**Untested leads worth a single probe each**

- EPFL's dated log of "strong decrease" NovaSeq price entries (Oct 2025, Mar 2026).
- Element's JPM 2025 deck, for year-over-year comparisons.
- Michigan's core rate card, for a same-core Ultima vs X comparison.
- TxGen's 2019 S4 price, for a 6000-to-X series at one institution.
- Charles University (Prague) award reports with X kit bid prices.
- Leiden (LUMC)'s AVITI24 notice, which may say which Illumina boxes it replaces.
- NASA GeneLab's 2025 6000 reagent notice.
- University of Toronto's 6000 purchase notice.
- Victoria's genetics service (VCGS) 2026 clinical price changes.
- The run's own queue: Illinois Carver pricing history, Taipei VGH successor tenders, NHRI TSO500 direct buys, Illumina LIMS compatibility status for the 6000, and the X v1.4.0 release notes (for 35B and new-chemistry details).

## How this scrape was built

**Process.** The scrape ran overnight on 12 Oct 2026, from about 01:00 to 05:45. A Python orchestrator ran a "strategist" for 85 cycles. Each cycle queued narrow probe, mine and scout tasks to cheaper-model agents, at most four at a time. The run completed 618 tasks and catalogued 1,042 candidate sources. It logged 1,236 raw findings.

**Filtering.** Each finding was:

- deduplicated against the analyst's existing notes;
- checked by a skeptical reviewer, which rejected 79 findings outright and corrected many others (the corrections are reflected above);
- tagged by thesis label and direction.

What survived is about 300 verified source findings (F-tags) and 103 derived figures (D-tags). Spend was about $321. The run stopped at its planned budget wind-down, at an estimated 42% of the weekly allowance.

**Tools and their limits.** Agents had web search and a GET-only page fetcher. They had no shell, no PDF text extraction and no POST requests. Four consequences follow:

- Many key documents were downloaded but not read.
- Several figures rest on search-result snippets; those are flagged in the items.
- Archived page histories (Wayback Machine, archive.today) were blocked. So almost no core price history before the current page could be built, except where old PDFs were linked directly.
- Apify actors were tried:
  - an eBay sold-listings scrape (failed: zero sold 6000s);
  - an Indeed postings scrape (two postings);
  - a Google search scrape (done);
  - four more requests still pending.

**Sources that were productive (most items first)**

- Taiwan's government e-procurement API (49 items).
- NCBI GEO platform counts (26).
- Canada's proactive contract disclosure (20).
- NCBI SRA run counts (12).
- The NCBI Genetic Testing Registry (13).
- Natera filings and decks (11).
- University core rate cards: UCLA, UCSD, UCSF, Berkeley, UMGC, Salk, Pitt, KUMC, Calgary, UConn, Emory, MIT, TCAG, OICR, Fred Hutch, Carver and Iowa.
- AAMC NIH award briefs (7).
- Myriad filings (7).
- GeneDx filings and calls (9).
- CMS Medicare Part B provider data (7).
- Illumina's Open Offer appendices (5).
- Illumina support and LIMS pages (5).
- The ENA archive.
- Freenome filings (4).
- UK university frameworks.
- CDC birth data (7).

**Sources found blocked; do not retry without a different tool**

- The Wayback Machine and archive.today.
- Reddit.
- WhatDoTheyKnow.
- Harvard's Bauer core pages (403).
- Surplus Solutions resale listings (403).
- GovDeals.
- UK Contracts Finder and Find a Tender web pages (403). Their OCDS API works.
- UC Davis's core pages.
- Palmetto MolDX documents.
- Health Canada's device licence search.
- Korea's KONEPS (login).
- Japan's PMDA PDFs.
- USAspending and the TED search API (both POST-only).
- The NIH RePORTER API.
- SRA BigQuery (needs a Google account).
- Fed360.
- HigherGov, after its free views.

**Sources found dry; do not repeat**

- Used-equipment marketplaces: eBay, LabX, REUZEit, MSU Surplus and dealer listings. These are undated, so they cannot show retirement pace.
- SEC EDGAR full-text search, which returns metadata only.
- Customer filings for Illumina supply terms: Natera, Freenome, GRAIL, 10x and BillionToOne. All are redacted or absent.
- Distributor catalogs. Government Scientific Source shows only the known GSA prices; Fisher and VWR show none.
- GSA eLibrary.
- University and cooperative purchasing agreements: E&I, Sourcewell, Big Ten, Iowa State and Colorado. UC's agreement shows only 25% off service.
- NIH S10 and NSF instrument awards.
- Service-provider price pages beyond promotions: GENEWIZ, Eurofins, Psomagen, Macrogen and GenoHub.
- Roche AXELIOS launch materials. They give only the $750K instrument and $150 genome.
- Element and Ultima newsrooms and trade-in pages.
- Most job boards.
- Public procurement portals in Brazil, India, mainland China, Thailand, Colombia, Ukraine, Portugal, Poland, Czechia, Slovakia, Spain and France.
- GTR lab-level summaries.
- Extra ENA data-volume variants, which need scripting.
- ClinicalTrials.gov enrollment sums.
- ABRF surveys.
- Core annual reports.
- NHS trust spend files.

**Limits to keep in mind**

- Core recharge rates include labor and overhead, so they are not Illumina's net price [D019].
- Public databases lag and over-represent research [D052].
- Canadian federal and Taiwanese buyers are tiny in Illumina's revenue. They are useful for patterns, not totals.
- Every derived $/Gb figure depends on the stated output assumptions (see Derived figures).
