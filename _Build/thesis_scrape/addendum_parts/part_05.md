## Derived figures

The scrape produced 103 derived figures (tags D001–D103). They are our own arithmetic on verified source data. Each appears as evidence in the sections above or in the watch-outs below. This section explains how the most important ones were built, so the reader can judge how much weight they bear.

### How prices become $/Gb

Almost every price comparison here turns a posted price into dollars per gigabase (billion DNA letters). We divide the price by the output the flow cell, lane or wafer produces. We used these outputs:

- **NovaSeq X 25B, 300-cycle:** about 8,000 Gb per flow cell at spec, or roughly 940–1,000 Gb per lane. One user measured about 8,800 Gb [F146]. Berkeley says real output runs 25–30% above spec [D035].
- **NovaSeq X 10B, 300-cycle:** about 375 Gb per lane (3,000 Gb per flow cell).
- **NovaSeq 6000 S4, 300-cycle:** about 3,000 Gb per flow cell (750 Gb per lane). S2 is about 1,000–1,250 Gb, and SP about 200–240 Gb.
- **Ultima UG100 wafer:** 2.5–3.0 Tb at UMN's own realistic figure, not the 3.6 Tb maximum. Using the maximum overstated Ultima's advantage in the first draft [D003].
- **AVITI high-output, 2x150:** about 300–450 Gb, depending on the kit generation.

The level of any $/Gb figure moves with these assumptions. The direction of a change at one core usually does not, because the same output is used on both sides.

### The 6000-to-X price gap, and why it matters for 1A

The table below sets out every measure of the 6000-to-X per-Gb gap that the scrape found. The takeaway: like-for-like S4-versus-25B gaps at cores and on list sit at 1.6–3.1x. Illumina's reported revenue gap of 3.4x is higher, and small 6000 flow cells (4–10x) or deep X discounts would close the difference.

| Measure | Source and date | 6000 ÷ X per Gb | Tags |
|---|---|---|---|
| Core S4 vs 25B, low end | Calgary 2025, UConn 2026, Missouri 2024 ("40% rate cut") | 1.6–1.9x | D022, D063 |
| Core S4 vs 25B, high end | MD Anderson, UCSF, Emory, Salk (2024–25) | 2.4–3.1x (median ~2.5x) | D025, D027 |
| User-facing at MIT (core marks up the X more) | MIT, Jan 2025 | 2.2x (vs ~3.1x on list) | D097 |
| Illumina list, S4 vs 25B | Open Offer 2024; 2025–26 | 2.76x → 2.58x | D049 |
| Regulated 6000Dx S4 vs 25B, list | Open Offer, Feb 2024 | 2.31x | D054 |
| Academic net (NCI's ~71% of GSA) | NCI rate card, GSA | ~2.4x | D026, D029 |
| Small 6000 flow cells vs 25B | Salk 2025, Pitt 2025 | S2 3.6–4.7x; SP 6–9.8x | D028, D032 |
| Illumina reported revenue per Gb | Q2 2026 deck (known) | 3.4x | — |

Three calculations follow from the table.

- **The reconciliation [D029].** Price the S4 at the academic net rate: about $5.13/Gb. Illumina's 3.4x ratio then implies X revenue of about $5.13 ÷ 3.4 ≈ $1.51/Gb. That is about 30% below the matching academic net 25B price (~$2.15/Gb). It is close to a negotiated price estimate built separately: the $16,480 list less a ~15% discount, spread over measured output, gives ~$1.59/Gb [D011].
- **The trend test [D049].** List ratios narrowed from 2024 to 2026, yet Illumina's reported ratio widened from about 2.8x to 3.4x. So the widening must come from which customers are left on the 6000, and from discounts on the X. List prices did not drive it.
- **What a point of conversion costs [D022].** A known estimate assumes each clinical point of 6000 Gb moving to the X costs Illumina about $24M a year, based on a ~70% price step. If the true step for a tail lab paying near list is only 45–50%, a point costs about $15–17M. Five points would then cost about $75–85M rather than $112M. D025 argues the median core step is closer to 60%, so the truth likely sits between these figures.

### Ultima and Element versus Illumina

The following table compares rival prices with Illumina at matched units. It shows that Ultima's advantage is about 2–3x at core list rates. Against Illumina's best negotiated price, the advantage falls to 1.2–1.5x. AVITI wins only against the smaller X flow cells.

| Comparison | Result | Tags |
|---|---|---|
| Ultima wafer vs 25B lane, core internal rates (realistic output) | 2.3–2.7x cheaper (2.7–3.3x at external rates) | D003 |
| Ultima vs 25B in Canada (OICR vs TCAG) | 1.7–2.0x cheaper | D076 |
| Ultima vs negotiated 25B (~$1.59/Gb) | 1.2–1.5x cheaper | D011 |
| Ultima all-in genome vs Illumina sequencing-only cost at another core | 35–55% cheaper | D002 |
| Same-period genome price, OICR Ultima vs TCAG X | 33% cheaper | D075 |
| Ultima per read for 10x single-cell work (with 10x discount) | 3.2–3.8x cheaper | D004, D062 |
| AVITI full run vs X 10B lane | 30–40% cheaper | D096 |
| AVITI list vs 25B list | ~3x more expensive | D020 |

**The genome decomposition [D099].** UMGC prices Ultima genomes in batches that each fill about one wafer. Comparing the 30x batch (24 × $192 = $4,608) with the 90x batch (12 × $329 = $3,948) separates the fixed wafer cost from the per-sample cost. The difference is about $55 per sample for prep and analysis, leaving about $3,290 per wafer. That prediction matches the 60x batch to within $4, and it matches UMGC's stand-alone wafer list price of $3,204. So sequencing is about 71% of a research genome's price.

TCAG's X genome breaks down in a similar way [D043]. Of C$650, sequencing is about C$330 at the core's own 25B lane rate.

### Hidden deflation inside the X family

The 10B premium is the price per Gb of a 10B lane divided by the price per Gb of a 25B lane at the same core. In 2026 it ranges from 1.03x at KUMC to 1.50x at MD Anderson [D018, D034, D035].

- Where history exists, the premium shrank because cores cut the 10B by 16–21% while holding the 25B [D005, D092]. UCLA went from 1.58x to 1.26x and TGen from 1.45x to 1.13x.
- It is not universal. Carver, TCAG and Novogene sit at about 1.6x [D042, D045].
- At Harvard, the gap narrowed for the opposite reason: the 25B price rose 17% [D085].

To read core prices correctly, compare them with Illumina's per-lane list ($16,480 ÷ 8 ≈ $2,060).

- Cores charge 26–70% above that list [D019].
- At the two UC cores, the ratio fell from about 1.40x to 1.24x in one cycle while list rose about 3% [D093, D080]. That is a real but ambiguous signal: either a lower net price or less overhead.
- The "$24,155 list" used in several items is in fact the GSA distributor price, about 1.47x Illumina's catalog list [D048]. Once that is corrected, NCI pays roughly catalog list [D023].

### Taiwanese tenders as a window on service-lab reagent costs

An all-in genome at NT$12,800 (~US$410) works out to about $4.1/Gb including everything [D070]. If reagents are 45–60% of that, they cost $1.8–2.5/Gb. NHRI's NT$9,800 genome leaves at most $0.75–2.0/Gb for reagents plus margin [D072].

Prices fell in one step, from NT$24,000 in 2023 to NT$12,800, and then held flat [D073]. Single bidders on Illumina-only specifications settle within 0–0.02% of the buyer's reserve price, while multi-bidder tenders land 19–28% below it [D074]. Illumina's distributor settles at about 85% of its opening bid, year after year [D101, D103].

### Clinical sequencing in Gb terms, for 1C

Every clinical sizing here uses the same yardstick: about 800M Gb a year of Illumina high-throughput output, taken from the existing notes. The table below shows that none of the fast-growing named programs moves that total by even half a percent.

| Program | Annual Gb (approx.) | Share of HT base | Tags |
|---|---|---|---|
| Natera MRD draws at Q2 2026 run-rate (classic vs all-genome) | 0.2–3.8M | 0.02–0.5% | D039 |
| Adaptive clonoSEQ | 0.03–0.14M | 0.004–0.02% | D095 |
| GUARDIAN newborn genomes | ~1M | ~0.1% | D095 |
| GeneDx extra tests from new payer coverage | 0.25–3.7M | 0.03–0.5% | D102 |
| Taichung VGH genome contract | ~0.31M | ~0.04% | D069 |
| Taiwanese NIPT contracts | <0.006M | ~0.001% | D077 |
| Extra Dutch and German NIPT uptake | 0.13–0.26M | 0.02–0.03% | D094 |

**The GeneDx mix effect [D013].** Assume a genome is about 100 Gb and an exome about 10 Gb. Then Gb per average test falls from about 50.5 to 41.5 as the genome share drops from 45% to 35%. That is enough to cut 30% test growth to single-digit Gb growth.

**The NIPT pool [D014, D030, D086].**
- Netting Natera's gain against Myriad's loss gives +8.2% for the two labs.
- If NIPT already reaches 70–80% of pregnancies, full penetration adds at most 24–41% more tests (after the 1% birth decline), or about 5–9% a year.
- US birth counts are falling only about 0.5–1.5% a year. A faster drop in the fertility rate is partly offset by a growing population of women aged 15–44.

**Customer price-versus-volume splits.**
- BillionToOne's gross profit per test rose 30%, entirely from price [D006].
- GeneDx revenue per test fell 12% [D017].
- Myriad's prenatal revenue fall is −9% volume × −8% price [D021].
- Guardant's Medicare dollars rose 20% on 5–6% more tests [D038].
- Signatera's Medicare payment per service fell 8% [D040].

### Canadian federal contracts, cleaned

Canada's contract disclosure repeats amended contracts as extra rows, each carrying the cumulative value.

- Removing those rows changes the picture. PHAC's 2022 baseline falls from about C$9.6M to C$6.8M, so the 2022–25 decline is about −51%, not −65% [D050].
- Removing three instrument purchases from H1 2026 leaves consumable-type spend down about 54–67% [D046].
- Counting NRC's outsourced sequencing alongside its direct orders turns a 90% collapse into a 40–50% decline [D041].

### NIH grant counts

**Multiyear funding [D036].** Take the $1.6B of up-front multiyear funding. Assume each award covers 4–5 years, so about $1.2–1.3B pays for future years. Dividing that by about $586K per award gives roughly 2,000–2,200 awards. That is close to the 1,924-grant shortfall. The award length is our assumption.

### Public sequencing databases

- **Deposit lag [D052].** The X's share of GEO deposits (29.5% in Q3 2026) is below every research X share Illumina has reported since Q2 2024 (59–92%). So GEO lags real sequencing by about two years.
- **The X Plus fix [D065, D064].** Counting only the plain "NovaSeq X" platform misses 55–67% of X output, because the X Plus is filed separately. With the X Plus included, the X's share of large public runs went from 16% to 33% in a year.
- **Volume versus counts [D060].** Weighting by data volume, public NovaSeq output grew about 12%, against 42% by run count.
- **Rivals' share of growth [D056, D057, D089].** In SRA, rivals took about 23% of run growth. In GEO, they took only 6.5% of sample growth, and 10% of US series growth. The two databases disagree on direction.

### Smaller derived checks

- **Reagent rental [D053].** The rental surcharge adds about $520K a year per rented X box. With only about 5 of 100+ placements on rental, that lifts fleet-average consumables per box by just 1–3%.
- **Element's scale [D007].** At an assumed $290–500K per instrument, Element's non-instrument revenue is at most about $100K per average box. Illumina's X box averages about $1.24M.
- **Element at NTU [D084, D100].** NTU's AVITI reagent ceiling works out to about US$140K a year per box, about twice NTU's latest Illumina reagent ceiling.
- **Novogene [D044].** Its 25B lane price per Gb fell about 5.6% a year, against Illumina's blended revenue per Gb falling about 15–19% a year.
