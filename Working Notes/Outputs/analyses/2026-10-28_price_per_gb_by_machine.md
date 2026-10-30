# Price per Gigabase by Sequencing Machine

*Prepared 2026-10-28. Sources: the core-lab price dataset (`Outputs/datasets/2026-10-13_core_lab_price_per_gb/`), the Open Offer and tender scrape (`Outputs/datasets/2026-10-12_thesis_scrape_findings.csv`), the 6000-vs-X revenue-per-Gb dataset, prior pricing analyses, expert calls, sell-side notes and peer transcripts. Every figure below cites its source.*

## The short answer

Price per gigabase (Gb, a billion DNA letters read) depends far more on **flow-cell size** than on the machine itself. On the same Illumina platform, bigger flow cells (the consumable glass chip each run uses) are much cheaper per Gb. Across Illumina's range, the cheapest output, the NovaSeq X 25B flow cell, costs about **$2–3 per Gb**. The most expensive, a NextSeq 2000 P1 run, costs about **$50 per Gb**, roughly 20 times as much.

Three conclusions stand out:

1. **NovaSeq X versus NovaSeq 6000.** Per Gb, the old 6000 costs **about 2–2.6 times** as much as the X at list and core-lab prices. On revenue, Illumina's own disclosures imply the 6000 now earns **about 3.4 times** as much per Gb as the X, up from about 2.2 times in 2024. The gap between those two figures suggests large customers pay well below list on the X.
2. **Mid-throughput is expensive per Gb.** A NextSeq 2000 P4 Gb costs about 4.5 times a 25B Gb, and the small P1 and P2 flow cells cost 11–20 times as much.
3. **Competitors claim roughly half of Illumina's best price or less.** Ultima (about $0.80/Gb at three core labs), Roche AXELIOS (about $1.3–1.5/Gb at its $150-genome list) and Element VITARI (about $1/Gb, announced) all undercut the X 25B list of about $2/Gb. Most of these figures are vendor claims or come from thin samples.

## How to read the numbers

There is no clean public price list. Illumina's catalogue is behind a login, and management has never given a $/Gb figure for each instrument. Each figure below comes from one of three kinds of source:

- **Illumina list (Open Offer catalogue).** These are prices from Illumina's Open Offer contract appendices, which surfaced in the web scrape (Feb 2024 to Jan 2025). They are the best list evidence available, but have not been checked against Illumina's own site.
- **Core-lab medians (Oct 2026).** These are what university sequencing cores charge their own researchers, at about 38 cores for the 25B. They include labor and overhead, so they sit above what Illumina charges the core. Internal rates are shown; external rates run about 13% higher.
- **Ratio to the 25B.** This is the median of each core's own price for that flow cell divided by its own 25B price. Comparing within the same lab removes differences between labs, so it is the cleanest relative measure.

$/Gb is calculated at the manufacturer's maximum output per run, so real-world $/Gb is somewhat higher. The 25B is rated at 8,000–10,500 Gb per run, which explains why its list $/Gb ranges from $1.57 to $2.06.

## Illumina instruments

The table runs from the cheapest to the most expensive Gb within each platform. The ratio column shows how many times a 25B Gb each flow cell costs.

| Machine and flow cell | Illumina list $/Gb | Core-lab median $/Gb (cores) | × NovaSeq X 25B | Notes |
|---|---|---|---|---|
| **NovaSeq X 25B** | ~$2.00–2.06 ($16,000–16,480 per kit) | $2.81 (38) | 1.0× | Cheapest Illumina output. Management claims a genome for "as little as ~$200" (10-K FY2025), or about $2/Gb |
| NovaSeq X 10B | ~$3.20 ($9,600 per kit) | $4.16 (39) | 1.5× | Cores cut 10B prices about 8–11% on a same-core basis in 2026 |
| NovaSeq X 5B | n/a | $4.89 (7) | ~2.1× | New in H1 2026; thin sample |
| NovaSeq X 1.5B | ~$5.5 (distributor price) | $8.72 (22) | 2.9× | Wide spread across cores |
| **NovaSeq 6000 S4** | ~$5.31–5.53 ($15,900–16,600 per kit) | $6.30 (25) | 2.1× | The regulated 6000Dx S4 lists at about $4.63/Gb |
| NovaSeq 6000 S2 | ~$8.8–11.1 | $10.57 (22) | 3.8× | |
| NovaSeq 6000 S1 | ~$11.5 (one university contract) | $15.60 (21) | 5.6× | |
| NovaSeq 6000 SP | ~$13.8–17.3 | $19.20 (23) | 7.0× | |
| **NextSeq 2000 P4** (XLEAP) | Not found | $10.80 (18) | 4.5× | An analyst recalled a "$9/Gb" XLEAP figure in Aug 2024 (unverified) |
| NextSeq 2000 P3 | Not found | $14.37 (19) | 5.7× | |
| NextSeq 2000 P2 | Not found | $28.46 (24) | 11.3× | |
| NextSeq 2000 P1 | Not found | $49.61 (23) | 20.4× | |
| NextSeq 550, MiSeq / MiSeq i100, iSeq, MiniSeq | Not found | Not in dataset | n/a | A real gap in the folder |
| NovaSeq X 35B (planned, about H1 2027) | Not priced | n/a | n/a | Management declined to discuss pricing (Q1 2026 call). One expert expects about 20% lower $/Gb; UBS sees about $150 per genome if priced like the 25B |

*Sources: list prices are from the Open Offer appendices (scrape rows D048, D049, D054, F538, F479) and the distributor price list (evidence ledger E234). Core medians and ratios are from `summary_by_table_month.csv` and the per-table CSVs, Oct 2026.*

## The NovaSeq X versus NovaSeq 6000 gap

This gap matters most for the investment debate, because the customer move from the 6000 to the X has cut Illumina's revenue per Gb. The measures below disagree in instructive ways.

| Measure | 6000 S4 vs X 25B | What it tells you |
|---|---|---|
| Illumina list, 2024 | 2.76× ($5.53 vs $2.00) | The X is about 64% cheaper per Gb at list |
| Illumina list, 2025–26 | 2.58× ($5.31 vs $2.06) | The list gap narrowed slightly: 6000 list was trimmed about 4% and 25B list rose about 3% |
| Core-lab medians, Oct 2026 | 2.06–2.24× | Flat against Oct 2024 (2.21×) |
| **Revenue implied by Illumina's disclosures, Q2 2026** | **3.39×** (range 3.2–3.6×) | Up from 2.2× in 2024. The X earns about 70% less per Gb than the 6000 |

The revenue-implied ratio comes from Illumina's quarterly disclosures of the X's share of high-throughput gigabases (83% in Q2 2026) and of high-throughput revenue (59%). It is therefore a fact-based calculation, though the rounded shares add about ±0.2× of error.

**Why the revenue gap is wider than the list gap.** The revenue gap grew from about 2.2× to about 3.4× while the list and core-lab gaps stayed flat. Something other than list price must be driving it. An earlier decomposition (`2026-10-12_6000_vs_X_ratio_widening_decomposition.md`) found two causes:

- **Most of the widening (60–100%, depending on assumed Gb growth):** X revenue per Gb fell as big customers converted on deep discounts.
- **The rest:** the remaining 6000 base shifted toward smaller, pricier flow cells.

Management itself said in Aug 2024 that the X is "easily more than 60% to 70%" cheaper per Gb (CFO, Q2 2024 call). Treat the split between these two causes as an estimate.

**Discounts on the X.** Expert evidence on discounts is consistent but thin:

- **List:** about $200 per genome (JPM, Mar 2026).
- **Typical discounted price:** about $175, per a UBS expert (Mar 2026).
- **Largest users:** about $125, in that expert's belief.

A former Illumina associate director (Jul 2026) said the largest genome centers and clinical labs may pay half to a quarter of what a small core pays per base on the same instrument. The same person said the gap can reach five to tenfold on low-throughput machines.

## Competitor machines

These figures are much less comparable. Most are vendor headline claims, priced per genome at different depths, often excluding library prep (the lab steps that prepare a sample for sequencing). Conversions to $/Gb assume about 100 Gb per 30X human genome.

| Machine | $/Gb | Basis | Source |
|---|---|---|---|
| **Ultima UG100** | ~$0.80 (3 cores: Cornell, Minnesota, OICR); ~0.2× the 25B at the same cores | Core-lab rate | Core dataset, Oct 2026 |
| Ultima, company target | ~$0.8–1.0 ($80–100 per genome) | Company target | JPM, May 2026 |
| **Roche AXELIOS 1** (duplex, full genome) | ~$1.3–1.5 ($150 per genome) | List, excluding library prep; assumes the sensor module is reused 20 times | JPM, Mar 2026; Roche Diagnostics Day, May 2026 |
| Roche AXELIOS (simplex, for "counting" uses) | ~$0.34 ($0.06 per million reads) | List | Roche, 2026 |
| **Element VITARI** (shipping H2 2026) | ~$1.0 (~$3k consumables per 3 Tb run). UBS puts the X Plus at ~$2.0 on the same basis | Company-announced economics, relayed by UBS | UBS, Feb 2026 (extract partly garbled) |
| Element AVITI (High Output) | $8.29 core median (7 cores); ~2× the 25B at the same cores | Core-lab rate | Core dataset, Oct 2026 |
| Oxford Nanopore PromethION | ~$3.5 (~$345 per genome); company roadmap to below $200 | Analyst figures | JPM, May 2026 |
| PacBio Revio | ~$5.5 ($345 per 20X HiFi genome) | List | PacBio Q2 2026 call |
| MGI / Complete Genomics DNBSEQ-T7+ | ~$1.0 (claimed) | Vendor claim of $1/Gb and a "$100 genome"; no list price disclosed. Experts call MGI "a little cheaper than Illumina" | Thesis scrape F204, F251; expert calls, Jul 2026 |
| Thermo Ion Torrent | No figures in the folder | n/a | n/a |

Long-read platforms (PacBio, Nanopore) cost more per Gb by design. They sell read length and accuracy, not cheap bases, so they are not direct price competitors for high-volume short-read work.

## Caveats and contradictions

- **The core-lab data is a proxy.** Core labs mark up, reprice about once a year (so a price can be 6–12 months old), and lag Illumina's own price moves. 10 of the 25 current NovaSeq 6000 S4 prices are carried forward from earlier observations rather than freshly seen. Ultima (3 cores), AVITI (7) and the 5B (7) are thin samples.
- **Different denominators.** The 25B list figure is $2.00/Gb at 8 Tb of output but about $1.57/Gb at the 10.5 Tb ceiling. Real lane yields can be lower.
- **Some figures are unverified.** The Open Offer list prices are from Feb 2024 to Jan 2025 and were not checked against Illumina's site. The $9/Gb XLEAP figure is an analyst's recollection from 2024. Every 35B price is hearsay.
- **"$150 per genome" is Roche's list, not Illumina's.** Experts who quote $150 for Illumina mean an expected 35B outcome or a discounted price.
- **The X Plus instrument price:** about $985k–1.2M (Bloomberg Intelligence) or "just above $1M" (expert). The $689k in a garbled UBS line is more likely Element VITARI's price, per the evidence ledger's correction.
- **Gaps:** there is no data for MiSeq, MiSeq i100, NextSeq 550 or Ion Torrent, and only a vendor claim for MGI. Illumina's 2024 Open Offer catalogue appendices are the best place to close the low-throughput gap.
