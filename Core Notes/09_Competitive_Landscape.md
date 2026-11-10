# The Competitive Landscape in Sequencing

*Core Notes section 09. Synthesized from 8 Core Notes sections as of 2026-10-10. Bracketed tags cite the source; full detail is in Working Notes (see INDEX.md).*

Illumina still owns most of the sequencing market, but by autumn 2026 the debate had moved from *whether* rivals could dent it to *how fast* its share erodes and how much price it must give up. The pressure differs by arena:

- **High-throughput sequencing:** new entrants from Roche, Ultima and Element.
- **Mid-tier:** Element, plus contract labs (CROs, outside firms selling sequencing as a service).
- **Long reads:** PacBio and Oxford Nanopore (ONT).
- **China:** MGI.
- **Proteomics:** Thermo Fisher's Olink.
- **Spatial biology:** 10x Genomics' imaging instruments, which need no sequencer at all.

Most evidence below comes from about 90 expert calls held between January and October 2026, from sell-side research and from competitors' own disclosures. Treat single expert numbers as anecdotes. Many later calls are AI-run "channel checks" (scripted customer surveys), and several experts appear twice under different labels. Competitors and former insiders have obvious biases.

## High-throughput short-read sequencing

### The incumbent position

High-throughput short-read sequencing means large machines reading billions of short DNA fragments per run. It is Illumina's core franchise, built on the NovaSeq X. Illumina placed more than 100 NovaSeq X units in Q4 2025, its second-best quarter since launch, taking the installed base to about 890. It then placed more than 80 in Q1 2026, against a 50–60 quarterly framework, and more than 95 in Q2. About 70% of Q2 placements went to clinical labs, and up to half of those added capacity rather than replacing older machines [Q4 2025, Q1 2026 and Q2 2026 calls, via JPM and Barclays].

The move from the older NovaSeq 6000 is nearly complete. By Q2 2026 the X carried 92% of research volume and 78% of clinical volume [Q2 2026 call].

Customers explain the lock-in in terms of the whole ecosystem rather than the machine itself: validated workflows, trained staff, software and depreciation schedules.

- **Depreciation.** Sanofi depreciates instruments over eight years, so a NovaSeq X Plus bought in 2024 cannot be retired before about 2030 without a write-off [Expert: Sanofi head of genomics, Oct 2026].
- **Channel-check evidence.** Of roughly 25 customer channel checks in Q3 2026, nearly all still ran 100% of their short-read work on Illumina. Only three reported real displacement: two to Element and one to Ultima.
- **Brand.** "You never get fired for buying Illumina" [Expert: former Illumina senior director, Oct 2026]. One expert called it "almost… like Kleenex" [Expert: Daisy Lab CSO, Jul 2026].

### Share estimates

Share estimates come almost entirely from former Illumina staff and competitors, so they are opinion, not data. All agree on the direction but differ widely on pace. The table shows the range, from mild erosion to a fall toward half the market.

| Source | Share now | Where it is heading |
|---|---|---|
| Former Illumina commercial manager [Jun 2026] | ~70% "maybe a little less," from 92% (mid-2017, or 2021 elsewhere in the call) | Below 60% |
| Former Illumina AD [Jul 2026], citing DeciBio data used internally | Mid-60s%, from ~80%, losing ~3 points a year | "Flatline" near 50% |
| Former Illumina field application scientist (FAS), now SOPHiA [Jul 2026] | ~70%, from 80% | Loses "at least 30%" over 4–5 years |
| ONT EMEA sales director [Oct 2026] | ~80% in Europe (75–85%) | 55–60% in 3–5 years, revenue "overall stable" |
| Ivy League core director [Jul 2026] | n/a | Illumina loses ~10% of share (up to 20% counting new share); at most 70%, more likely 60%, of new placements from 2027 |
| California biotech director [Oct 2026] | n/a | 80–85% of short-read, Ultima 15–20% |
| Former Illumina AD, now Kailos [Aug 2026] | 80%+ of installed base | Bullish for 2–3 years |
| LifeStrands lab director [Jul 2026] | "something like 95%" (loose) | "always going to win" |

Two framings recur across these calls. First, each rival attacks one segment while Illumina must defend all of them [Expert: Kailos AD, Aug 2026]. Second, Illumina is better seen as a premium brand in a "race to the bottom" than as a technology laggard [Expert: former Illumina AD, Jul 2026].

The Complete Genomics (CG) CEO said "Illumina will definitely lose market share" because incumbents "have only one way to go," while conceding there was no evidence of share shifts yet [Mar 2026]. A Natera associate director expects erosion to be gradual: "It's not going to be in six months, they will lose 30%" [Jul 2026].

### Price, elasticity and Illumina's defense

Price elasticity is how much more sequencing customers do when the price falls. Experts say it has weakened. In the early years, halving the price might bring four times more sequencing. From the NovaSeq era onward, halving the price lifts sequencing only about 25% [Expert: former Illumina AD, Jul 2026].

The NovaSeq 6000 (about 2018) cut the price per gigabase (a billion DNA letters) from about $20 to $5. Once BGI/MGI and then Singular, Element and Ultima arrived in 2021–22, Illumina "just didn't have the ability to keep the price premium high," producing "real flat growth starting in about 2022." The same expert estimates blended high-throughput consumable prices (the reagent kits bought for every run) fell 30–40% since 2022. On core consumables, "flat would be a huge win."

The Broad Institute gives the clearest example. Its Illumina spend was "basically flat" from 2024 to 2025 while its data output doubled [Expert: Broad EVP, Apr 2026].

Illumina's defense is to cut price on big flow cells (the consumable chips runs happen on) and upgrade the NovaSeq X without asking customers for new capital.

- **Bigger and smaller flow cells.** A 35B flow cell (billions of reads) is expected around January 2027 and should cut cost from about $2.50 to $2 per gigabase, roughly 20% [Expert: former Illumina AD, Jul 2026]. A 5B flow cell fills the gap between 2B and 8B. Cheaper 5B and 10B kits are priced toward the 25B unit price [Ivy League core, Oct 2026].
- **Other upgrades.** These include Q70 accuracy (about one error per 10 million bases), staggered runs, 5-base (reading genetic variants and methylation, chemical tags that regulate genes, in one run) and TruPath (see Long reads).
- **Trade-ins and rental.** Trade-in credits of about 50% are offered on NovaSeq 6000s [NY core, Jul 2026], which one director called "a discount war" [academic medical center core, Oct 2026]. Reagent rental places an instrument free in return for multi-year reagent commitments. One former insider says it has "become a necessity" because Element and Ultima will discount instruments 90% [Jul 2026].

Owners largely accepted this approach. "If I had a NovaSeq, I'd be happy," said the University of Minnesota director [Feb 2026]. The same director also said Illumina is "not evolving their box much anymore… it's incremental."

List prices still rise on paper while net prices fall:

- **Annual increases.** February list increases are about 3–5% [Arizona core, Apr 2026; pharma core, Jul 2026]. X Plus consumables rose 2.5% in 2026 [UCSD, Mar 2026].
- **Surcharges.** Tariff surcharges run 5–6% [Ivy League core; cancer center core, Oct 2026]. Vanderbilt fought one and won a bigger discount.
- **Analyst read.** Barclays saw signs of quiet discounting. In Q1 2026 the NovaSeq X's share of gigabases rose to 76% while its share of consumables revenue stayed at 55% [Barclays, 2026-04-30]. Bloomberg Intelligence said Illumina was "in the early stages of trading price for volume" [BI, 2026-05-01].

### Roche Axelios (SBX)

Roche acquired its SBX technology (sequencing by expansion, which copies DNA into enlarged "Xpandomer" molecules read through a nanopore) with Stratos Genomics in 2020. It unveiled SBX at the AGBT conference in February 2025, priced it at AGBT in February 2026, and launched the research-use-only (RUO, not cleared for patient diagnosis) Axelios 1 on 29 June 2026 [Roche H1 2026 call].

Roche's published figures are below; they are Roche claims, not independent checks.

| Metric | Roche figure |
|---|---|
| Instrument | ~$750,000 (vs NovaSeq X ~$985K–1.2M per BI) |
| Duplex mode (both DNA strands read) | ~16 genomes per run, 1.8 terabases in 4 hours, Q38 (~99.98% accuracy) |
| Simplex mode (one strand) | 40B reads in 4 hours, reads up to 1,500 bases |
| Genome price | $150 per 30X genome (each position read ~30 times), assuming ~20 sensor reuses; "no volume-based discounting" |
| Counting price | $0.06 per million reads |
| Liquid-biopsy panel | ~$25 per sample (1.1 Mb panel) |

**How analysts read the price.** JPM put $150 about 25% below its ~$200 estimate for NovaSeq X [JPM, 2026-02-26]. UBS called it "relatively benign," because large Illumina customers already pay similar prices and Illumina's roadmap implies about $150. UBS saw the real exposure in "counting" applications such as RNA sequencing. There Roche's $0.06 per million reads compares with Illumina's roughly $0.68 list on the 25B flow cell, and counting is about 16% of Illumina's sequencing consumables [UBS, 2026-02-26]. Barclays instead saw a "well capitalized competitor" able to force "another round of pricing headwinds in 2027 and beyond" [Barclays, 2026-02-05]. A CG product director said Illumina's stock rose during the presentation, and that "$50 genome, that will be devastating" [May 2026].

**How customer sentiment moved.** Views went through three stages:

1. **Before AGBT (early 2026).** Experts doubted the accuracy claims. Roche compared a strand with its own fold-back copy rather than with a known reference [VCU, Jan 2026]. UIUC said released data degraded "after 100 bases" [UIUC, Feb 2026]. Experts did, however, fear Roche's diagnostics sales force.
2. **After AGBT (spring 2026).** Customers read the pricing as parity with Illumina, not disruption. Yale already gets $150 from Illumina and answered "Nope." Cedars-Sinai said only $50–75 would have triggered "massive adoption." Practical drawbacks emerged: no modularity (a partial run costs a full run) [UCSD, Mar 2026], an overnight amplification step and 19–20 hour prep [ex-CG director; TGen, Mar 2026], and reuse validation worries for clinical work [Natera, Mar 2026].
3. **Into Q3 2026.** Wait-and-see. Customers flagged carry-over on reusable sensors, a narrow assay menu, analysis weaker than DRAGEN (Illumina's analysis software), RUO status, and Roche's weak service reputation since it bought KAPA.

**Who is buying.** Near-hands-on users were most positive. The Broad, a beta site, will "most likely" put Axelios into production, starting with work Illumina does not do, such as same-day newborn-ICU genomes [Apr 2026]. Dana-Farber and Vanderbilt planned trials, and the largest academic genome center expects to buy "a couple" [Jul 2026].

**Roche's targets and progress.** Roche targets about 100 placements in year one and a $1bn-plus "blockbuster" over time. JPM compared this with first-year placements of earlier launches: PacBio Revio (173 in nine months of 2023), Element AVITI (112) and NovaSeq X (352) [JPM, 2026-05-13]. By 8 September, Schinecker said roughly one-third of the ~100 had been placed, with no "teaser offers" [JPM CEO call]. Barclays framed the 100 as orders [Barclays, 2026-09-28].

**JPM's customer survey** of 62 customers [JPM, 2026-06-10] found:

- 40% were unfamiliar with Axelios.
- Only 8% would buy within 6–12 months.
- About 11% of potential buyers would retire an Illumina instrument.
- 37–39% said a reagent-rental offer from Illumina would make them less likely to buy Axelios.

Survey caveat: only 37 respondents knew Axelios, and the source dates conflict.

**Share forecasts for Roche** span a wide range:

- "Maximum 5%" in two years [former Illumina AD, May 2026].
- 10–15 of 100 instruments bought in 2027 [former Illumina AD, Jul 2026].
- 5–10% in year one and 20–30% "in a couple of years" [CG product marketing, May 2026].
- 10–20% of Illumina's business in three years [ONT, ex-Illumina, Oct 2026].
- 20–30% [MD Anderson scientist, Jul 2026].

### Ultima Genomics

By Q3 2026 several customers named Ultima, not Roche, as the real cost threat.

- **Price.** Reagents run at about one-third to one-fifth of Illumina's cost, and genomes near $80, heading toward $50–60 on the UG200 [Ivy League core; Tennessee NGS manager, Oct 2026]. The UG200 lists at $1.25M [UCSD, Mar 2026].
- **Accuracy.** Ultima's ppmSeq chemistry reaches Q60–Q70 [former Illumina AD; Exact ML scientist, Jul 2026].
- **McGill's view.** McGill, an official Ultima service provider since early 2026, puts it at about half Illumina's cost but says it needs "at least another year" to approach Illumina's popularity [Jul 2026].
- **Natera's view.** The Natera AD recalls $80–110 per sample for shallow applications. Solaris chemistry needs about 50% less DNA and costs 30% less, at "below $0.40" per million reads. The UG200 is priced like Illumina [Jul 2026].
- **Adoption examples.** Tennessee is leasing an Ultima for over $1M: about 80% cheaper on reagents and 50% all-in. It will absorb 60% of the sequencing budget but only 8–10% of samples [Oct 2026]. A Georgia core saw Ultima's share of its outsourced work rise from about 10% to 20% in two years [Jul 2026]. Ultima will "pretty much put an instrument in my lab for free" in return for reagent commitments [Vanderbilt, Apr 2026].

Its limits are quality, thin analysis pipelines and turnaround (one lab quoted six months). A New York clinical lab rejected Ultima because it cannot read about 10% of the genome, including "almost every clinically relevant gene" [Oct 2026].

### Other high-throughput entrants

Element's VITARI was unveiled on 19 February 2026. Prices for it conflict:

- Minnesota put it at $689,000 [Feb 2026].
- UBS said it is about 40% cheaper than the X Plus's $689,000 list [UBS, 2026-02-19].
- Natera's AD put it at about $700,000 [Jul 2026].

UBS added that its consumables cost about one-tenth per run ($3,000 versus $32,000), about half per gigabase, for about one-fifth of the output, with shipping in the second half of 2026. Natera's AD called it "almost equal with NovaSeq X," and said it gives 50X genomes for "somewhere over $70." UCSD called it "not a truly high throughput box." Element owners felt betrayed because "they promised us they wouldn't come out with a new box."

**Complete Genomics** (CG) is owned by China's MGI and re-entered the US in 2023 after Illumina paid it over $300M in a cross-licensing settlement. CG's T1 is "easily in that ballpark" but "can't get into the conversation" [ex-CG director, Mar 2026]. MGI is selling CG to a Swiss company (see China).

## Benchtop and mid-throughput sequencing

The middle of the market is where Illumina is losing the most ground, mainly because its best per-gigabase economics require full high-output runs.

**How the squeeze works.**

- Several cores said Illumina discounts aggressively on its biggest machines but "not as aggressive with mid-size," which pushed them toward Element [South Carolina core, Mar 2026].
- Delaware became the first core to skip an Illumina flagship. Its cost of ownership is "far too high," because the advertised cost per gigabase holds only for runs it would fill 8–12 times a year [May 2026].
- Large customers pay a half or a quarter of what small labs pay per base, and five- to tenfold less than labs on smaller instruments [former Illumina AD, Jul 2026].
- Small-scale pricing may be "100X more expensive" per base [Daisy Lab CSO, Jul 2026].

**Illumina's mid-tier responses.** Illumina has cut selected prices. A California biotech saw an extra 30–40% discount on the NextSeq 2000's largest flow cell [Jul 2026]. Management's 2026 pull-through guidance (yearly consumables revenue per instrument) shows how much less a mid-tier box generates than a flagship [JPM, 2026-02-06]:

| Instrument | Annual consumables pull-through |
|---|---|
| NovaSeq X | $1.35–1.40M |
| NovaSeq 6000 | $600–650K |
| NextSeq 1000/2000 | $80–100K |
| NextSeq 500/550 | $90–110K |

**Element is the consensus mid-throughput winner.** Its AVITI24 adds spatial and cell-imaging features and loads Illumina libraries natively.

- **Pricing.** About $300,000 for the small box [Vanderbilt, Apr 2026], $350,000 with spatial [Vanderbilt, Jul 2026] and about $500,000 [former FAS, Jul 2026]. Upgrades cost $150,000 at list, about $100,000 negotiated [Delaware], or about $140,000 [Yale].
- **Installed base.** Experts recall "a couple hundred" IVD units and "several hundred" instruments.
- **Price history.** About two years ago Element undercut Illumina by "almost half," until a 30% Illumina consumables cut left a 10–15% gap. Illumina now sits 15–20% above alternatives on cost per gigabase, and some customers say "we are willing to pay the premium" [EpiCypher, Jun 2026]. One former insider says Element pushed Illumina's consumable margins "below 50% in some cases" [Jul 2026].
- **A switch example.** The South Carolina core bought an AVITI24 with a September 2026 NIH grant. It runs RNA-seq at about $1,100 versus $1,600–1,700 for an outsourced NovaSeq X lane, and expects 70–80% of its work to move [Oct 2026].
- **Where it does not fit.** Large centers such as the Broad, McGill and TCAG found little use for Element. Yale likes it but would need three or four boxes.

**The rest of Illumina's small-box range.** The MiSeq i100 is well liked; one pharma lab ranks it first among its purchase plans [Jul 2026]. The NextSeq is "losing favor." An ONT director called Illumina's MiSeq discontinuation "a huge disaster" [Oct 2026]. A former insider said the MiSeq tier is low-revenue and "dying," though dropping it risks ceding entry customers to Element.

**Contract labs are drawing work away from cores.** Low-cost providers such as Plasmidsaurus (about $50 per RNA-seq sample), Novogene, Zymo, Twist and QIAGEN undercut core labs, which must recover salaries. Louisville's director summarized the result as demand "rerouted," not lost [Sep 2026].

**Other mid- and low-throughput rivals.**

- **Thermo Fisher's Ion Torrent** wins on simple DNA-to-report workflows and small panels, but labs that scale move to Illumina [former Illumina market developer, Jan 2026]. An Abbott scientist gives Thermo at least 10–15% share [Jul 2026], while another calls Oncomine "losing the market so bad" [former FAS, Jul 2026]. Thermo's own 2026 disclosures did not discuss Ion Torrent at all, so its trajectory is undocumented here.
- **GeneMind** copied a prior Illumina box at "insanely low pricing," mainly in Asia [former Illumina AD, Jul 2026].
- **Singular's G4X** is "clearly lost in the sequencing space" [UCSD, Mar 2026].

## Long-read sequencing

Long-read sequencers read continuous stretches of thousands of DNA letters. Former insiders put long reads at about 10% of the market and calling them "a little too niche to support an independent company" [former Illumina AD, Jul 2026].

### PacBio

PacBio is shrinking and cash-constrained.

- **Revenue.** 2025 revenue was about $160M, up 3.9%. FY2026 guidance was cut from $165–180M (February) to $155–165M (August), gross margin guidance from 41–44% to 35–37%, and cash-flow breakeven was pushed to 2028 [PacBio Q2 2026 call].
- **Cost cuts.** Its SPRQ-Nx chemistry cut the list price of a 20X human genome 30%, to $345.
- **Clinical demand.** Clinical consumable shipments grew 67% in Q2.
- **Exiting short reads.** PacBio sold its short-read assets to Illumina for about $48.1M net in January 2026. The FTC had blocked Illumina's attempt to buy all of PacBio in 2020.
- **Analyst view.** Barclays rates it Underweight. It says a 2% share of the substitutable market "would essentially double revenues," but cost, speed and ease of use "have never been on par" with short reads [Barclays, 2025-11-05].

Customer views of PacBio split. UIUC called the Revio "the winner," with PacBio rising from about 10% to 20% of its revenue [Feb 2026]. Yale's Revio runs at about 30% utilization, because "short reads are actually answering 90% of the questions" [Apr 2026]. A Massachusetts institute sees long reads "losing share" [Mar 2026].

### Oxford Nanopore

ONT grows faster but is also resetting expectations.

- **Results.** FY2025 revenue was £223.9M, up 24% at constant currency. H1 2026 grew only 12%, to £116.7M, hurt by China (−16%) and the Middle East (−14%) [ONT Q2 2026 call].
- **Targets.** ONT targets organic revenue above $700M in 2030.
- **Genome cost.** Its consumable cost per genome is about $345 at two genomes per flow cell, with under $200 on the roadmap, against Illumina's $200 and Roche's $150 [JPM, 2026-05-13].
- **Publications.** ONT papers reached almost 1,900 in 2025, more than 30% of Illumina's count [DB, 2026-09-21].
- **Customer complaints.** UIUC's director calls ONT "my enemy" for selling MinIONs directly to researchers and cites runs yielding 1–2 Gb instead of 20 Gb [Feb 2026].
- **How brokers see it.** All three brokers frame ONT as more complementary to Illumina than a substitute.

### Illumina's TruPath

TruPath (formerly Constellation) produces "synthetic long reads," meaning long-range genome structure inferred from short reads, at about $395 list per sample. Management says it was launched in February 2026. Roughly $600 fully loaded (including all lab and data costs) [UCSD, Mar 2026].

Rivals dismiss it. Barclays calls it "the third iteration/name change" of Illumina's long-read push but warns it "could freeze part of the long-read market" [Barclays, 2026-03-06]. ONT calls it "stitching together… imputed. It's not direct" [ONT CFO, Mar 2026].

Customer verdicts diverged sharply:

| Expert | Verdict on TruPath |
|---|---|
| Yale [Apr 2026] | "Exceptionally good"; about $500 versus about $2,000 on PacBio |
| Delaware [May 2026] | "Not going to work" |
| Ivy League core [Oct 2026] | About $3,000 versus about $700 on PacBio |
| Tennessee [Oct 2026] | "Never going to be a $400 genome"; standard prep is under $300 |
| Vanderbilt [Jul 2026] | Moved from "not likely" to many orders |
| Colorado children's hospital [Oct 2026] | "Looks the winner" for unknown critical cases |

**Methylation is a separate front.** EpiCypher says long-read methylation now costs about the same as short-read methylation. It expects long reads to rise from 10–15% to about 50% of its methylation work in two to three years [Jun 2026]. Another epigenomics lab moved its consumables spend from 75/25 Illumina/PacBio to "closer to 50/50" on Fiber-seq, a long-read assay [Jul 2026]. Illumina's 5-base, by contrast, drew the most consistent praise of any Illumina launch [Delaware, May 2026; UCSD, Apr 2026].

## Clinical diagnostics

### Illumina's clinical strength

Clinical testing is Illumina's growth engine and its strongest moat. Clinical consumables grew 20% excluding China in Q4 2025 and Q1 2026, then eased to 15% in Q2. They now make up about 65% of sequencing consumables, up 10 points in two years [BI, 2026-07-31].

JPM upgraded to Overweight on 10 June 2026, arguing clinical customers are "stickier-than-appreciated." Its reasoning: clinical drives more than 40% of company revenue, and transition pricing headwinds are "largely gone exiting this year" [JPM, 2026-06-10].

Former staff dispute the size of the clinical claim. One calls the over-65% figure "a very loose statement," because "Illumina has been very generous… in classifying clinical use" [former market developer, Jan 2026]. Another recalls clinical at 52% of revenue on leaving in 2024 [Kailos AD, Aug 2026].

### Switching costs

Switching costs are what protect the clinical franchise:

- **Validation.** Validating a test on a new platform costs about $100,000–200,000 plus "hundreds of samples" per sample type [Colorado children's hospital; Texas reference lab, Oct 2026]. Cedars-Sinai puts it at $200,000–500,000 for academic labs and "millions" for private ones, taking months to over a year. Cedars' own genome validation used 120 genomes [Apr 2026].
- **Legacy example.** Adaptive's clonoSEQ cancer test still runs on the old NextSeq 550, at nearly ten times NovaSeq's cost per read, because revalidating is "incredibly hard" [former Illumina AD, Jul 2026].
- **FDA-approved tests.** Moving an FDA-approved test could cost "another $200 million of clinical trials" [Exact ML scientist, Jul 2026].
- **Trials.** "You cannot switch an assay or a sequencer middle of a trial," and MRD-guided trials run five to seven years [Natera AD, Jul 2026].

### Cheap genomes and tumor testing

Cheap genome headlines matter less for clinical cancer testing. Germline (inherited) genomes need about 30X coverage, but tumors need "easily more than 120" and sometimes 200X [former market developer, Jan 2026]. Tumor work at 1,000X would cost $5,000–7,500, so "I need a $20 genome" [Cedars-Sinai, Apr 2026].

Fully loaded genome costs dwarf headline prices:

- About $460–575 for research and about $1,000 for clinical work [ex-CG director, Mar 2026].
- Over CA$400 at TCAG [Apr 2026].
- Under $400 at the Broad.
- "Probably two thirds of the cost is not the sequencing" [Dana-Farber, Apr 2026].

### MRD

MRD (minimal residual disease) testing uses blood to look for cancer left after treatment. It is the main clinical growth driver.

- **Sensitivity bar.** A Natera AD says sensitivity below five parts per million will be required to stay in the market by 2030. Illumina's AGBT slide claimed below 5 ppm, recalled as 2.5 ppm, which they tie to Q70 [Mar 2026].
- **Market size.** The same expert recalls an MRD market of about $5bn today and $30bn by 2030 [Jul 2026]; treat this as a rough recollection.
- **Skeptics.** A former Illumina manager doubts MRD travels outside the US, where reimbursement is the obstacle [Jan 2026].

### Roche's clinical channel

Roche's diagnostics channel is the scenario that most worries clinical observers. "If I were Illumina, I'd actually be very scared" [UMN, Feb 2026].

Roche is building an end-to-end cancer-testing stack around Axelios:

- **Foundation Medicine (FMI).** FMI has delivered more than 1.5M comprehensive genomic profiles (CGP, large-panel tumor DNA tests). More than 40% of US oncologists ordered from it in the past year, and it holds over 100 companion diagnostics (tests required to choose a specific drug). FMI plans to move partner sites onto Axelios and showed better MRD detection at AACR 2026 [Roche DX Day, 2026-05-12].
- **Other pieces.** SAGA Diagnostics (MRD), the Freenome partnership and PathAI.

A former Illumina AD said Roche becomes a significant threat only if it moves Foundation's testing over [May 2026]. Others note that MRD and ctDNA players (circulating tumor DNA testing companies) such as Guardant and Natera want a "dumb" sequencer from a non-competitor [UMN].

Two signs of movement have appeared. Foundation, Guardant and Natera are validating Ultima and Roche, and NHS labs mirror their partners' setups, so if partners switch, NHS labs follow [Roche UK lead, Jul 2026]. A former FAS says some third-party-panel users "quietly placed Roche instruments" after Illumina price rises [Jul 2026].

### Prenatal testing

Commoditization is already visible in prenatal testing (NIPT, a maternal blood screen for fetal chromosome conditions). In Europe, lab-to-lab prices fell 40–50% over five to six years, from €350–400 to €220–250, in a market described as "capped." BGI sells slightly below Illumina at under €100. Element with Medicover runs about 284 samples per run. Illumina's VeriSeq NIPT has had no big update since 2019 [Veritas VP, Jan 2026].

## China

### Illumina's position

Illumina's China business has roughly halved since Beijing put the company on its "unreliable entity" list.

| Period | Greater China revenue | Change |
|---|---|---|
| Q4 2025 | $55M | −33% at constant currency |
| Q1 2026 | $52M | −29% organic |
| Q2 2026 | $56M | −19% organic |
| FY2026 guidance | $210–220M | About a 1-point drag on growth |

[Ameriprise; JPM; Q2 2026 call]

Freedom Broker expects renewed growth only after removal from the list [Freedom, 2026-02-10]. A former commercial manager put China at about 4–5% of revenue and said "the clear winner right now is MGI" [Jun 2026].

### MGI

MGI's evidence comes only from UBS notes, which never mention Illumina. Management says MGI's share of Chinese public tenders rose to about 70% in 2025, and that it shipped about 60% of the prior year's import-substitution orders (Chinese buyers replacing foreign products) [MGI mgmt via UBS, 2026-04-29].

The numbers are weaker than the share claims suggest:

- **2025.** Revenue fell 7.7% to Rmb2.78bn, China sequencing revenue fell 11%, and gross margin dropped to 52.9% amid "intensified competition."
- **H1 2026.** Revenue rose 18.9% to Rmb1.37bn, with China +8.5% and the Americas +126% [UBS, 2026-08-24].
- **Analyst view.** UBS rates MGI Neutral with a Rmb58 target.

MGI is cutting its US exposure. It licensed its CoolMPS chemistry outside Asia to Swiss Rockets ($20M upfront plus a $20M milestone). It agreed to sell its US subsidiary Complete Genomics for $50M and licensed its StandardMPS chemistry in North America [UBS, 2026-04-29]. It is also buying nanopore and spatial assets for Rmb365.7M, making it, per UBS, the only Chinese supplier with both short- and long-read capability.

Outside China, a New Zealand agricultural provider is "ditching their very large Illumina sequencers for MGI" [Daisy Lab CSO, Jul 2026]. A former FAS says MGI "lost its touch" [Jul 2026].

### Geopolitics

- **US restrictions.** BGI is held back in the US by restrictions and NIH grant rules [epigenomics lab, Jul 2026]. The US DoD 1260H list names Complete Genomics and Novogene [academic medical center core, Oct 2026]. A New York core expects NIH's "1271 list" to steer work away from some foreign providers [Jul 2026].
- **Peers' China problems.** ONT's China revenue fell about 16% in H1 2026 under export controls, with 7–8 local nanopore competitors pricing about 30% lower [Barclays, 2026-09-08]. PacBio's APAC revenue fell 45% in Q2 2026.

## Proteomics

Proteomics means measuring proteins rather than DNA. Illumina entered by acquiring SomaLogic, which closed in January 2026 for $350M upfront plus royalties and milestones; Barclays cites $363M net cash on 30 January. SomaLogic reads protein-binding aptamers out on Illumina sequencers. It costs about 100 basis points of 2026 margin and $0.18 of EPS [JPM; Barclays]. Management says multiomics plus the BioInsight data unit will add 1–2 points of growth in 2027; Barclays and Seeking Alpha call that unverifiable.

The rival is Thermo Fisher's Olink. A former Illumina market developer called the deal "absolutely the right strategy" and said Olink "sets up a new battleground," with SomaLogic easier to add for NovaSeq X owners [Jan 2026].

Customers showed interest but almost no adoption:

- **Upfront costs.** The assay requires a six-figure Tecan liquid-handling robot [pharma core, Jul 2026; Solvias, Jul 2026]. Starting probe sets cost $30,000–40,000 [UIUC, Feb 2026], and one expert cites $400,000–500,000 for 100 samples [VCU, Jan 2026].
- **Competitors chosen instead.** A pharma lab piloted Alamar instead. One core says Olink Reveal covers about 90% of its needs. The Massachusetts institute, Yale (which found SomaLogic "horrible to deal with") and McGill use Olink. Another Sanofi department bought its own X Plus specifically to run Olink.
- **Strategic doubts.** SomaLogic versus Olink is "a mountain and a sea level" [former FAS, Jul 2026], and integrating proteomics is like "water and oil" [ex-Illumina staff scientist, Jul 2026].

Thermo is pairing Olink with its own Orbitrap Astral mass spectrometer in a Singapore population-health study, not with sequencing [Thermo Q2 2026 call]. Roche lists Olink, Pixelgen and Alamar as Axelios partners. The Broad notes that Olink- and SomaLogic-style counting tolerates simplex errors, which makes it a natural Axelios use [Apr 2026].

## Single-cell and spatial biology

### 10x Genomics

Single-cell analysis (measuring gene activity cell by cell) and spatial biology (measuring it while preserving tissue location) feed sequencers, but they increasingly bypass them too. 10x Genomics is the incumbent.

**Q1 2026 results** [10x Q1 2026 call]:

- Revenue was $150.8M.
- Single-cell consumables grew 6% while reaction volumes grew double digits, so price per reaction fell.
- Spatial consumables grew 31%, but spatial instruments fell 32% as buyers waited for Atera.

10x CEO Saxonov credited Ultima and Roche, not Illumina, for cutting "price per read… hugely," which he called "a huge enabler" of mega-scale projects [BofA, 2026-05-13]. Relations with Illumina are strained. After Illumina launched single cell in 2025, 10x "broke off," recommended Ultima and dropped NovaSeqs from its brochures until cores "revolted" [UIUC, Feb 2026].

### Atera

10x launched Atera at AACR in April 2026 at about $495,000 [UCSD, Apr 2026]. It is an imaging-based whole-transcriptome instrument that needs no sequencer.

- **Economics.** About $9,000 per slide, 4 slides a week and about 200 slides a year (Xenium, the predecessor, handles about 100).
- **Supply.** About 40 units ship in the second half of 2026, mostly in Q4, and supply constrains deliveries into 2027 [10x Q1 2026 call].
- **Customer reactions.** UCSD: "If we don't buy an Atera, we're going to lose all of our spatial business." Duke: 10x single-cell consumables halved from about $1.2M to about $600,000 as work moved to spatial, and "ultimately we see less sequencing being done on the Illumina platforms" [Jun 2026]. A Massachusetts hospital core's output fell 15–20% as users moved to spatial [Jul 2026].
- **Dissent.** McGill says spatial "will not dent sequencing" given population genomics, MRD and proteomics growth, and was "very upset" Atera is a new box at about double Xenium's price [Jul 2026]. Yale says "the timing is wrong."

### Illumina's single-cell and spatial products

Illumina is late in both areas. A former insider estimates single cell at over $1bn (near $1.5bn) and spatial "probably not even a $500 million market." In a 10x workflow, Illumina captured about 25% of spend, and its own sequencing-based spatial revenue is at most "low eight figures" [former Illumina AD, Jul 2026].

**Fluent/PIPseq** (single-cell kits from the Fluent acquisition, closed early 2025) drew mixed reviews:

- Positive: cheap and low-labor [VCU, Jan 2026; Massachusetts institute, Mar 2026].
- Negative: fewer genes detected than 10x [ex-CG director, Mar 2026]; "not game-changing" [pharma, Jul 2026]; "doesn't seem like it's making much of a dent" [Louisville, Sep 2026].
- One mid-sized core does spend mid six figures a year on it [Vanderbilt, Apr 2026].

**StrataMap**, launched June 2026, is Illumina's spatial product and drew the most enthusiasm of its new launches. Specifications [Ivy League core, Jul 2026]:

| Feature | StrataMap | Visium HD |
|---|---|---|
| Resolution | ~1 µm | 2 µm |
| Capture area | 10×50 mm | 6.5×6.5 mm |
| Price | Over $2,000 per slide | Roughly double |
| Availability | Q4 2026 | Shipping |

StrataMap works only on fresh-frozen tissue, not the FFPE (formalin-fixed, paraffin-embedded) samples that make up most clinical material [TGen; McGill]. A former insider says it took four years and now overlaps Atera, leaving Illumina "scrambling to adjust their business cases" [Jul 2026].

### Other single-cell and spatial players

- **Parse** (now QIAGEN-owned) quotes about $300 against a true cost of about $2,000 [UIUC].
- **Singleron** is 5x cheaper than 10x [former FAS].
- **Bruker's CosMx** will "struggle" [UCSD].
- **Singular's G4X** is "still a bit niche."
- **Roche** has a 10x single-cell partnership.

## Where sources disagree

**How fast Illumina loses share.** Estimates run from "minimal" in 12 months [largest academic genome center, Jul 2026] to a fall toward 50% [former Illumina AD]. Former insiders increasingly blame strategy rather than technology: indecision between research and clinical, leadership churn and software. The ONT director's view that share falls while revenue stays "overall stable" splits the difference.

**Whether Roche's price is disruptive.** UBS, Yale and Cedars-Sinai see parity at best. Barclays, Natera's AD and the CG product director see a well-funded rival that could reset pricing. One expert said Roche can price flexibly because sequencing is small within its diagnostics arm; another said Roche may run 90%+ reagent margins. Cedars argues Illumina's own reagents carry "printer ink" margins and could go to $100. Roche's ~20-reuse assumption is accepted by the Broad, while Natera calls it "a major no" for MRD.

**Whether speed matters.** The Broad, Vanderbilt and TCAG say it matters for newborn-ICU, urgent and contract work. Cedars-Sinai, Yale, UCSD and a former Illumina senior director (8 hours versus 23) say prep time and clinical scheduling erase the gain. Cedars called Roche's speed claims, which start from a finished library, "cheating."

**Who Roche targets.** Candidates named include CROs and counting work (biopharma, Regeneron), clinical diagnostics (TCAG, EpiCypher, CG), Roche's own cost base ("an enabler, not a replacer," per the Exact ML scientist) and research cores. Sanofi expects the real contest around 2030, when NovaSeq X depreciation ends.

**Ultima versus Element as the nearer threat.** The South Carolina core said "the Illumina competitor is not Roche, but rather Ultima." Others call Element "the most real threat" [former Director of Commercial Excellence, Jul 2026]. A Yale expert calls Ultima's chemistry "basically flawed." The ONT strategist says "Ultima's doomed."

**DRAGEN's value.** Vanderbilt says "No way can beat the DRAGEN." A former Illumina bioinformatician says most people "just don't use it," and ONT says it is "not a reason why to stay." A Fluxus director dropped it as too expensive, and a former Illumina commercial leader argues it should be bundled rather than charged at about $40,000 on a ~$1M machine.

**Q70 and TruPath.** Natera sees Q70 as essential for MRD. UCSD ("I don't care because I mostly do counting") and the ex-CG director see it as irrelevant or even demand-reducing. TruPath verdicts span "exceptionally good" to "not going to work," as shown in the Long reads section.

**Price direction.** Several labs report 5–10% increases, a 6% tariff surcharge and 10–15% freight rises. Others say "Illumina reagent price has only one direction, that is to go down" [Ivy League core, Jul 2026]. Both are probably true at once: list prices rise while discounts deepen where competition bites.

**Analysts on valuation.** The underlying debate is clinical growth versus Roche-led price pressure, which has not been settled; the analyst disagreement is mainly about how much the stock already reflects.

| Firm | Rating and target | Reasoning |
|---|---|---|
| JPM | Overweight; $185 (10 Jun) → $230 | Clinical stickiness |
| Freedom Broker | Downgraded to Hold, $185 (5 Aug) | "Much of the upside is now priced in" |
| Barclays | Underweight; target raised to $160 | Mid-single-digit grower needing "continued price concessions"; "cannot justify" ~35x P/E |
| Seeking Alpha | Fair value $188 | Q2 margin gain mostly government incentives |

The stock reached about $278 by early October, above most targets.

**Data conflicts to watch.** Several sources contain errors or conflicts:

- Barclays (July 2026) and one former Illumina scientist call Axelios an Element product; it is Roche's.
- BI reports a 20% fall in Q1 service revenue, which conflicts with every other source.
- Reported VITARI prices conflict (see High-throughput section).
- Roche's 100-system target is framed as orders by Barclays and as placements by JPM.
- Several share figures come from interviewers, not experts, and dated insider views may be stale.
