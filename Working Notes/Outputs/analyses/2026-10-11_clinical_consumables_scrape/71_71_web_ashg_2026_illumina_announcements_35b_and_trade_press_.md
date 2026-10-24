# Agent 71: 71-web-ASHG-2026-Illumina-announcements-35B-and-trade-press-since-Oct-1

*Model: sonnet. Run 2026-10-11 03:55:30. Cost $1.37 (API-equivalent).*

**Assignment:** Closes open gaps 1, 2 and 6, focusing on live news and pricing not yet found. Searches (web search plus fetch of company and trade-press pages; if archive.org is blocked, say so and move on): (a) Illumina newsroom (investor.illumina.com and illumina.com/company/news-center) for any release dated after 2026-10-01: NovaSeq X 35B, 14B or 5B flow cell, 'HT mode', 'constellation', 'Q3 2026 earnings date', ASHG booth and launch announcements, price statements and ship dates. (b) Trade press: GenomeWeb, 360Dx, Fierce Biotech, Genetic Engineering News and BioSpace for 'NovaSeq X' 'flow cell' price or '$/Gb' and 'January 2027' in Aug-Oct 2026. (c) Core-facility and vendor rate cards or catalogs showing NovaSeq X 25B, 10B and 1.5B flow cell prices against NovaSeq 6000 S4 and S2 on the same page or date: Broad Genomics Platform, Stanford SGTC, Baylor HGSC, HudsonAlpha, Garvan, UMich Advanced Genomics, Vanderbilt VANTAGE, Duke GCB, NYU Genome Technology Center, TCAG Toronto, plus distributor listings (Fisher Scientific, VWR, Cytiva, Thermo) for part numbers 20104704, 20083470 and 20085594. Quote $/flow cell, Gb per flow cell and computed $/Gb, and the date of each. (d) Competitor price points: Roche AXELIOS list price per genome and what '$0.06/M reads' implies per Gb at 150bp paired-end (show the math), Element AVITI24 and AVITI High-Output $/Gb, Ultima UG100 Solaris and UG200 $/Gb and $100 or $80 genome claims, MGI T20 and T7+ tender prices in China, India or Europe. (e) ASHG 2026 (20-24 Oct) program pages and abstracts listing NovaSeq X vs AVITI or AXELIOS or UG100 comparisons from clinical labs. Return a dated table of price points with URLs and clearly say which are list vs realized.

## Key findings

Little here is new. I found no 35B, 14B or HT-mode price or ship date. There is also no new Illumina release or trade-press item on a "January 2027" list-price change.

1. **Illumina's newsroom has only two items after 1 Oct 2026 (FACT).** Both are dated 8 Oct 2026. One announces Q3'26 results on Thu 29 Oct 2026 (the ledger's gap 3 date is now confirmed). The other releases SpliceAI2, a rare-disease splice-variant AI model. Neither mentions NovaSeq X, flow cells or pricing. [illumina.com/company/news-center, fetched 2026-10-11]
2. **The Illumina ASHG 2026 page has no NovaSeq X or 35B content (FACT).** It lists booth 701, three Industry Education sessions (long-range/epigenetic, multiomics, population-scale learning systems), two CoLab sessions (proteomics, epigenetic mapping), a DRAGEN user group on 22 Oct and 11 posters. The silence is informative, not proof. Illumina launched the 25B flow cell at ASHG 2024, but the pre-show page shows no comparable launch this year. [illumina.com/events/conferences/2026/ashg-2026.html, fetched 2026-10-11]
3. **CNAG (Barcelona) lists X 25B and 6000 S4 on one 2026 rate card, a same-page pair the ledger lacks (FACT, search-snippet level).** It lists the X 25B at €3.77/Gb (regular tier), €4.22 (mid) and €4.52 (premium), both 2x100. It lists the S4 at €10.07, €11.28 and €12.08. The X is therefore 63% cheaper per Gb on the same card, a 0.37 ratio, in every tier. This is steeper than E051's unpaired median (−53%) and its Calgary pair (−41%). It sits close to the −60% Salk pair and to management's "60–70%". The PDF would not parse, so it is unconfirmed against the original. [cnag.eu/sites/default/files/CNAG PRICES 2026_R1.pdf]
4. **Roche AXELIOS $/Gb is now computable (E068, E060).** At the 175 bp insert quoted for simplex mode, 1 Gb is about 5.7M reads. At $0.06/M reads that is about $0.34/Gb. This is calc on FACT. It is simplex, and Roche's $150 duplex 30x genome is a separate price.
   - 175 bp is the insert size Roche quoted, which may not be the sequenced read length. The $/Gb moves with whatever length is used.
   - Roche's "$0.06 × 40B reads = $2,400 per run" matches the per-run figure in the aseqer analysis (27 Feb 2026), which supports the definition.
   - That analysis also cites Ultima at $0.24/M reads. Illumina's 25B list is $0.64–0.68/M reads (E060), so on a per-read basis Roche is roughly 10x cheaper.
5. **Ultima's own claim is $0.80/Gb reagent cost (MGMT).** Ultima says UG 100 with Solaris gives "$80 / genome and $0.80 / Gb pricing". Solaris 2.0 Max, due in 2H26, doubles output to 20B reads per wafer. This quantifies E069 and gives a vendor-claimed Ultima $/Gb. [ultimagenomics.com whole-genome-sequencing page; GenomeWeb, via search 2026-10-11]
6. **UMGC's AVITI24 lane price converts to about $2.6–3.6/Gb (E290).** The Element JPM 2026 deck and catalog are in the search results but unread.
7. **Catalog numbers resolve part of gap 2 (FACT).** [illumina.com NovaSeq X Series Reagent Kits page, fetched 2026-10-11]
   - The earlier part-number list was off. 20104704 is the 1.5B 200-cycle kit, not a 25B kit.
   - 20085594 is the 10B 300-cycle kit.
   - The 25B 300-cycle kit is 20104706. The 100- and 200-cycle kits are 20125967 and 20125968.
   - The 5B kits are 20145965/66/67 and the 1.5B 600-cycle kit is 20145964.
   - The page lists no 14B or 35B kits yet. List prices need a login. No Fisher, VWR or Cytiva price was found.
8. **Rate-card dates (UCLA, TCAG).**
   - UCLA TCGB: the page effective 1 Jul 2026 gives per-lane 1.5B, 5B, 10B and 25B prices (table below). E275 had only the 25B row.
   - TCAG April 2025 (snippet): X 25B lane $2,500 (100-cycle), $3,085 (200-cycle) and $3,470 (300-cycle). This is dated, but no S4 price was extracted.
9. **A UCLA rate card dated 1 Aug 2023 also appeared in the results (snippet only).** It lists X 25B 300-cycle at $3,168 internal and $3,933 external, against S4 300-cycle at $4,817 internal and $5,313 external.
   - The 1 Jul 2026 external 25B-300 price is $3,512, down 11% from $3,933.
   - If the 2023 snippet is right, the X-to-S4 gap there was only about 25–26% per lane then. The snippet is unverified, because a 25B kit before 2024 is implausible.
   - Do not use it until the PDF is read. I could not open the PDF.

## Dated price table

| Date | Source | Item | Price | List or realized | URL |
|---|---|---|---|---|---|
| 2026 (Rev 1) | CNAG | X 25B 2x100 / S4 2x100, per Gb | €3.77–4.52 / €10.07–12.08 | Core rate (service price) | cnag.eu/sites/default/files/CNAG PRICES 2026_R1.pdf |
| 1 Jul 2026 | UCLA TCGB (external) | X 1.5B 100/200/300/600-cycle lane | $1,874 / $2,189 / $2,339 / $3,473 | Core rate | uclahealth.org (TCGB pricing page) |
| 1 Jul 2026 | UCLA TCGB (external) | X 5B 100/200/300-cycle lane | $1,210 / $1,352 / $1,463 | Core rate | same |
| 1 Jul 2026 | UCLA TCGB (external) | X 10B 100/200/300-cycle lane | $1,457 / $1,666 / $1,766 | Core rate | same |
| 1 Jul 2026 | UCLA TCGB (external) | X 25B 100/200/300-cycle lane | $2,165 / $3,202 / $3,512 | Core rate | same |
| FY27 (undated) | Harvard Bauer (snippet) | X 25B 100/200/300-cycle lane, Harvard code | $1,403 / $2,143 / $2,426 | Core rate | bauercore.fas.harvard.edu/fy27-ngs-sequencing |
| FY27 (undated) | Harvard Bauer (snippet) | X 25B 100/200/300-cycle lane, PO | $1,964 / $3,001 / $3,396 | Core rate | same |
| Undated | Missouri Genomics Technology Core (snippet) | X 25B 300-cycle lane | $2,317 | Core rate | mugenomicscore.missouri.edu/ngs.html |
| Undated | TxGen (snippet) | X 25B 300-cycle lane | $3,222 | Core rate | txgen.tamu.edu |
| Apr 2025 | TCAG (snippet) | X 25B 100/200/300-cycle lane | $2,500 / $3,085 / $3,470 | Core rate | tcag.ca/documents/facilities/TCAG-NGS-Price-List April 2025.pdf |
| Undated | Calgary CHGI (snippet) | S4 v1.5 300-cycle flow cell / lane | $22,420 / $5,820 | Core rate | cumming.ucalgary.ca (CHGI price list) |
| Undated | Calgary CHGI (snippet) | X 25B 300-cycle lane | $4,100 | Core rate | same |
| 27 Feb 2026 | Roche (via aseqer analysis) | AXELIOS simplex, ~$0.06/M reads | ≈$0.34/Gb at 175 bp (calc) | List | aseqer.com/p/roche-axelios-pricing |
| 27 Feb 2026 | Roche (via aseqer analysis) | AXELIOS duplex 30x genome | $150 | List | same |
| Feb 2026 | Ultima | UG 100 Solaris | $0.80/Gb, $80 genome | Vendor claim | ultimagenomics.com |
| Feb 2026 | Ultima | UG200 instrument | $850K; $1.25M (Ultra) | List | GenomeWeb, 649716 |

The Harvard, Missouri, TxGen, Calgary and CNAG rows come from search snippets. Their original PDFs and pages were not opened, so treat them as unverified. Per-Gb figures need Gb per lane, which the ledger puts at about 1,000 Gb for a 25B 300-cycle lane (E259 and its correction).

## Not new
Roche $750K and $150/genome, Illumina's Feb 2026 roadmap (no price, no dates), UCLA's 25B-300 price (E275), Rush, Broad and Novogene (E259, E260), and Harvard's FY26 to FY27 move (E274).

## Contradictions and stale data
- The CNAG pair (−63% for the X vs S4, same card) is steeper than E051's unpaired median (−53%) and Calgary's (−41%). The spread between cores is wide, so one number should not be taken as "the" price gap.
- The 2023 UCLA snippet conflicts with the idea that the X launched at roughly 50–60% below the S4 (E055). Its 25B label for a 2023 document looks suspect.
- Part number 20104704 in the task brief is the 1.5B 200-cycle kit, not a 25B kit.
- GenomeWeb returned 403 for the pages I tried.

## Gaps / what I could not find
- **Archive.org:** not attempted, and the earlier waves found it blocked.
- **Not found:** any 35B, 14B or HT-mode price, ship date, or release-note mention (checked: Illumina newsroom, ASHG page, kit catalog, web search); any trade-press "January 2027" item; Stanford SGTC, Baylor, HudsonAlpha, Garvan, UMich, Vanderbilt, Duke and NYU rate cards; Fisher, VWR and Cytiva list prices; MGI T20 and T7+ tender prices.
- **Not read:** The TCAG, CNAG, UCLA-2023 and Rush PDFs came back as binary, and Bash and PDF rendering were disabled for me. To confirm the CNAG, TCAG and UCLA figures and extract the S4 prices, someone needs to read those PDFs from a shell.
- **Not opened:** AVITI24 and AVITI High Output $/Gb from Element's own catalog, and ASHG 2026 abstracts.
