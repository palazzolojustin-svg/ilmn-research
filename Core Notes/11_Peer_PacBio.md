# Peer: Pacific Biosciences (PACB)

*Core Notes section 11. Synthesized from 10 source extracts as of 2026-10-10. Bracketed tags cite the source; full detail is in Working Notes (see INDEX.md).*

## Business overview

### What PacBio does

Pacific Biosciences of California (PacBio, ticker PACB) makes long-read DNA sequencers. These instruments read continuous stretches of DNA, often tens of thousands of letters at a time. Illumina's short-read machines instead read fragments of a few hundred letters and stitch them together. PacBio was founded in 2000 and is based in Menlo Park, California. It reports three revenue lines [UBS, 2026-02-13]:

- **Instruments:** the sequencers themselves.
- **Consumables:** the reagent kits and chips customers must buy for every sequencing run, which makes this revenue recurring.
- **Service and other.**

PacBio's signature data type is **HiFi** (high-fidelity) sequencing, which produces long reads that are also highly accurate. Sequencing runs on a disposable chip called a **SMRT Cell**, using a chemistry kit. The product line is:

- **Revio:** the high-throughput system. Throughput means how much DNA data a machine produces per run. Revio's average selling price (ASP) was about $482k in Q4 2025 [UBS, 2026-02-13]. Cumulative shipments reached 346 by Q1 2026 and 366 by Q2 2026.
- **Vega:** a lower-priced benchtop system for smaller labs and new customers, launched in late 2024. Cumulative shipments were 147 at end-2025, 174 after Q1 2026 and 200 after Q2 2026.
- **SPRQ and SPRQ-Nx chemistries:** SPRQ-Nx replaces SPRQ. It raises SMRT Cell yield and, with the **multi-use SMRT Cell**, lets one chip run up to three times. It launched on Revio at the end of May 2026 and on Vega in August 2026.
- **Other products:** **Kinnex** (RNA sequencing kits), **PureTarget** (targeted panels used for carrier screening) and **DeepConsensus** (an AI accuracy algorithm built with Google). The older Sequel II/IIe line is still used clinically in China.
- **A high-throughput (HT) platform:** an unnamed, higher-capacity next-generation sequencer targeted for 2027.

PacBio also had a short-read sequencer, **Onso**. The short-read business had been meant to address "the piece of oncology that long reads can't really go after very well" [Van Oene, Morgan Stanley conf., 2026-09-15].

In January 2026, PacBio closed the sale of its high-throughput short-read intellectual property and assets **to Illumina** for about $48.1M in net cash. In Q1 2026 it also resolved litigation with Personal Genomics of Taiwan. Then-CEO Christian Henry said these steps "sharpen our focus" on long reads, which the company calls its true competitive advantage [Q1 2026 call].

A key metric is **pull-through**: annual consumables revenue per installed Revio. Management targeted "low-to-mid $200k" for 2025 and $225k–$250k for 2026. In August 2026 it cut the 2026 range to $200k–$225k.

### How PacBio competes with Illumina

The core trade-off is quality versus cost. Barclays said long reads beat short reads on quality, but "from a cost, speed, and ease-of-use perspective they have never been on par," and "it [takes] a lot to dethrone the entrenched technologies" [Barclays, 2025-11-05]. UBS said PacBio's "unique capabilities" struggle "in the face of persistently unfavorable relative cost and throughput differentials vs. Illumina," which "will remain a challenge" [UBS, 2026-02-13].

**Cost per genome is the main battleground.** In its own opinion, Barclays argued that "the true Dx opportunity unlocks when PACB gets the cost of sequencing down close to ILMN's $200" per genome. Dx means diagnostics. At that price, "the economics work for larger scale vols of HiFi + SBS for a Dx test," where SBS (sequencing by synthesis) is Illumina's chemistry. Barclays called this "not a biochemistry issue" but "an engineering problem around the chip and the supporting system." The team had worked on it for two to three years, and "engineering issues tend to be more easily solved than chemistry issues" [Barclays, 2025-08-07].

SPRQ-Nx is PacBio's answer to that problem, and the cost claims sharpened over time:

- Management first promised a human whole genome (WGS, reading a person's entire DNA) below $300 at scale [Q3 2025 call].
- Barclays then described it as $300 per genome, on par with high-throughput peers [Barclays, 2026-02-12].
- At launch, the U.S. list price for a 20x HiFi human genome fell 30%, to **$345**. "20x" means each DNA position is read about 20 times on average [Q2 2026 call].

**PacBio's clinical argument** is that HiFi is "the only commercially available sequencing technology that we believe can comprehensively characterize substantially all classes of variants in a single assay." Short-read approaches need several tests to match it, so HiFi should give a faster answer at lower total testing cost [Henry, Q1 2026 call]. Barclays framed PacBio as a "substitution model for an already existing market," where just 2% share "would essentially double revenues from here" [Barclays, 2025-11-05].

**Illumina is now a long-read competitor.** Illumina tried to buy PacBio in 2020, but the FTC blocked the deal. Barclays calls Illumina's TruPath launch "the third iteration/name change of ILMN's push into long-read sequencing." Given that history, it wants more community data before concluding Illumina will win share. Near term, though, "ILMN's launch could freeze part of the long-read market," and Barclays expects it to draw more investor attention than Roche [Barclays, 2026-03-06].

**Roche** is coming with Axelios, "a relatively long-ish read technology that may freeze some of the market for PACB" [Barclays, 2026-02-12]. Its reads are longer than Illumina's SBS reads "but no where close to PACB." Even so, budget-constrained researchers who use both technologies may spend scarce capital on it. Barclays expects a modest headwind to Revio in 2026 [Barclays, 2026-03-06].

PacBio management named no competitors on the Q2 2026 call or at Morgan Stanley. The only competitive language was that SPRQ-Nx lets PacBio "compete for substantially larger projects where competitive economics are crucial to winning" [Van Oene, Q2 2026 call].

### Customers and end markets

Demand comes from three groups:

- **Academic and government (A&G) labs:** the historical core, especially for plant, animal and other non-human research. U.S. A&G demand has been weak through 2025–2026 because of uncertain NIH (National Institutes of Health) funding.
- **Clinical and hospital customers:** the growth engine. They use HiFi for rare disease diagnosis, newborn screening, pharmacogenomics and **carrier screening** (testing healthy prospective parents for gene variants they could pass on).
- **Newer buyers:** population-scale programs, commercial service providers, biopharma, and AI companies building **foundation models** (large AI models trained broadly on biological data).

Van Oene expects "AI therapeutic companies and nontraditional customers" to "likely replace academic and government in many ways" over three to five years [Morgan Stanley conf., 2026-09-15].

## Results and commentary, in chronological order

### Quarterly results

The table below gathers quarterly results. Revenue is in $ millions, and "consensus" is the Bloomberg Street average cited by Barclays. Gross margin is the share of revenue left after the direct cost of products. Q1 and Q2 2025 figures come from year-ago comparisons on the 2026 calls. The Q2 2025 gross margin is Barclays' 38.2%; the later call gave 38% non-GAAP.

The pattern is clear. Consumables grew steadily to records, while instrument sales were volatile. Gross margin peaked at 42.1% in Q3 2025 and then fell to the mid-30s.

| Quarter | Revenue | Consensus | Instruments | Consumables | Service/other | Revio units | Vega units | Gross margin | Pull-through (annualized) | Adj. EPS |
|---|---|---|---|---|---|---|---|---|---|---|
| Q1 2025 | 37.2 | n/a | 11.0 | 20.1 | 6.0 | 12 | 28 | 40% | n/a | -0.15 |
| Q2 2025 | ~39.8–40 | 37 | 14.2 | 18.9 | 6.7 | 15 | 38 | 38.2% | n/a | -0.13 |
| Q3 2025 | 38.4 | 40.2 | 11.3 | 21.3 | 5.8 | 13 | 32 | 42.1% | $236k | -0.12 |
| Q4 2025 | 44.6 | 42.1 | 17.3 | 21.6 | 5.7 | 21 | 42 | 39.9% | ~$240k | -0.12 |
| Q1 2026 | 37.2 | 39.8 | 9.7 | 21.8 | 5.6 | 15 | 27 | 37% | ~$229k | -0.12/-0.13 |
| Q2 2026 | 39.0 | ~40.1–40.6 | 12.8 | 20.1 | 6.1 | 20 | 26 | 36% | ~$202k | -0.14 |

On a full-year basis [UBS, 2026-02-13; Barclays, 2026-02-12]:

- **Revenue:** 2025 revenue was about $160.0M, up 3.9% from $154.0M in 2024. That followed a 23.2% decline in 2024 from $200.5M in 2023.
- **Gross margin:** 2025 gross margin was 40.1–40.2%, up from 33.2% in 2024 and 27.4% in 2023.

### Guidance over time

The next table tracks management's guidance. It shows expectations being narrowed and then cut:

- FY2026 revenue fell from $165–180M in February to $155–165M by August.
- Cash-flow breakeven slipped a year.

| Item | Aug 2025 (Q2'25) | Nov 2025 (Q3'25) | Feb 2026 (Q4'25) | May 2026 (Q1'26) | Aug 2026 (Q2'26) |
|---|---|---|---|---|---|
| Revenue | FY25 $155–165M (from $150–170M) | FY25 $155–160M | FY26 $165–180M | FY26 $165–175M | FY26 $155–165M |
| Gross margin | FY25 37–40% (from 35–40%) | Exit 2025 above 40% | FY26 41–44% | 41–44% kept; +100 to +400 bps improvement, toward the low end | FY26 35–37% |
| Non-GAAP opex | FY25 $235–240M (from $240–250M) | n/a | FY26 below $230M | $220–225M | $215–220M |
| Revio pull-through | Low-to-mid $200k | n/a | $225–250k | $225–250k | $200–225k |
| Cash-flow breakeven | Positive exiting 2027 | End of 2027 | End of 2027 | End of 2027 | 2028 |

### Q2 2025 (reported early August 2025)

Revenue of about $40M beat the Street's $37M by 8.9%. Instruments ($14M versus $12M, +20.0%) and service ($7M versus $5M, +34.2%) drove the beat. Consumables slightly missed ($19M versus $20M, -4.2%).

Other results also beat expectations [Barclays, 2025-08-07]:

- **Placements:** Revio placed 15 units versus Barclays' 13, and Vega 38 versus 24.
- **Gross margin:** 38.2%, beating the Street's 34.5% by 375 basis points. A basis point (bp) is a hundredth of a percentage point, so 100 bps equals one point.
- **EPS:** earnings per share, here a loss, was -$0.13, versus -$0.16 expected by Barclays and -$0.17 by consensus.

Asia-Pacific (APAC) plus Europe, Middle East and Africa (EMEA) grew 45% year over year and drove the beat. U.S. A&G demand was soft, as expected.

Guidance changes:

- **FY2025 revenue** narrowed to $155–165M with an unchanged midpoint, against consensus of $156M and Barclays' $154M.
- **Gross margin** guidance rose 100 bps to 37–40%, against consensus of 37.3%.
- **Product mix:** consumables were guided up mid-teens percent and instruments down mid-teens percent.
- **Costs and share count:** opex fell to $235–240M. Interest and other expense rose to $6–8M from $5–7M. The share count was trimmed to 298M from 299M.
- **Q3 2025 revenue** was guided at about $40M, flat sequentially and year over year. APAC would rise year over year but fall sequentially, because demand had been pulled into the first half.
- **Unchanged:** the exit gross margin above 40% and positive cash flow exiting 2027.

Barclays summarized: "Trends consistent with rest of peers on US A&G side. Strength in APAC/EMEA drove the beat. Strong demand for Vega highlights the interest in HiFi. Dx and translational demand starting to pick up." Translational means research aimed at clinical use. Barclays said Vega brought HiFi to budget-constrained customers "just at a more approachable price point." It called clinical traction "the most notable update on the print."

Barclays' diagnostics lab checks and a WGS non-deal roadshow (an investor marketing trip) found more long-read use in carrier screening and targeted panels, including an ataxia panel with Quest Diagnostics. Barclays tied this to the many large long-read projects of recent years. Management highlighted a large global ALS study. Barclays came away "incrementally more positive" on a "relatively strong" quarter given the macro environment [Barclays, 2025-08-07].

### Q3 2025 (reported 5 November 2025)

Barclays headlined its note "For Every 2 Steps Forward in Consumables, Instruments Take a Step Back." Revenue of $38.4M missed the Street's $40.2M by 4.4%. The line items:

- **Instruments:** $11.3M versus $13.7M, a 17.5% miss.
- **Service:** $5.8M versus $6.2M, a 7.0% miss.
- **Consumables:** $21.3M versus $20.0M, a 6.3% beat.
- **Placements:** Revio was in line at 13 units. Vega missed at 32 versus Barclays' 42, a sequential decline within Vega's first launch year.
- **Gross margin:** 42.1%, beating the Street's 37.8% by 430 bps on a high-margin consumables mix.
- **EPS:** -$0.12, beating -$0.15 from both Barclays and consensus.

Management's explanations [Q3 2025 call, via Barclays]:

- **Vega:** the miss was mainly in Europe, where procurement ran past quarter-end. Some delayed orders had already arrived for Q4.
- **Revio:** one unit with a "much higher ASP" failed installation testing, shifting its revenue to Q4.
- **New customers:** about 75% of Revio and 60% of Vega placements went to new customers.
- **Pricing:** instrument ASPs dipped because of discounted **strategic placements** at key institutions meant to drive consumable use. Management expected a recovery.
- **Pull-through:** Revio pull-through of $236k was at the high end of the range.

By region, EMEA grew 18% on 50% consumables growth. The Americas fell 10% year over year but grew 2% sequentially. APAC fell 11%, though China beat management's expectations.

Guidance and outlook:

- **FY2025 revenue** guidance fell to $155–160M, cutting $5M from the top.
- **Q4 2025** revenue was guided up about 10% sequentially, with Revio and Vega placements at yearly highs.
- **2026:** no formal guidance, but management said revenue should grow on a larger installed base, a better funnel, steady placements and strong utilization.
- **Cash:** 2025 cash burn of $115M and positive cash flow by end-2027 were both reiterated.
- **SPRQ-Nx:** more than 100 customers showed interest in a paid beta that began in November 2025. Early access was planned for early 2026, with broad rollout in 2026.

Barclays credited the pull-through to "all the market education and marketing the team has done over the past 2 years." It cited an EU consortium paper showing HiFi is "much better than standard testing technologies for carrier screening and hard to sequence genes," giving PacBio "a good foothold in the clinical market."

The remaining hurdles, in Barclays' view, were up-front workflows and costs and simpler data analysis: "we are still at the early days and the story will take time to play out." It expected margin to keep improving from the low-40s and possibly expand materially "when vols reach critical capacity utilization" [Barclays, 2025-11-05]. On 15 December 2025, with the stock at $2.17, Barclays raised its target to $2.00 from $1.50.

### Q4 2025 and initial 2026 guidance (reported 12 February 2026)

PacBio had pre-announced a beat in January. The final figures [Barclays, 2026-02-12; UBS, 2026-02-13]:

- **Revenue:** $44.6M versus the Street's $42.1M, a 6.0% beat.
- **Instruments:** $17.3M versus $14.3M (+20.8%), helped by European Vega shipments that had slipped from Q3.
- **Consumables:** a record $21.6M, in line with the Street.
- **Service:** $5.7M versus $6.0M, a slight miss.
- **Placements:** Revio's 21 units beat Barclays' 13, and Vega's 42 matched its estimate.
- **Gross margin:** 39.9%, missing the Street's 40.7% by 81 bps.

Other details:

- **Clinical growth:** hospital and clinical consumables sales grew 55% in 2025.
- **Vega:** about 65% of 2025 placements went to new customers, and ASPs were flat.
- **Revio pricing:** Revio was again discounted into key accounts expected to generate "above-average consumable pull-through."
- **Pull-through:** UBS cited full-year Revio pull-through of about $242k, slightly below the prior year. Its note labeled this "2026," but it most likely means 2025.
- **Channel focus:** management de-emphasized A&G and highlighted clinical momentum, especially in EMEA.
- **SPRQ-Nx:** the product was moving from beta (about 4–5 users) to early access (about 15). It would expand to EMEA "in several weeks," then APAC, with full launch later in 2026.

2026 guidance and the analyst reaction:

- **Revenue:** guided to $165–180M, against consensus of $178M. Barclays modeled $178M, though its guidance table showed $175M without reconciliation. UBS modeled $173.3M.
- **Gross margin:** guided to 41–44%, against consensus of 42.4%.
- **Placements and pull-through:** Revio placements flat to slightly up, with pull-through of $225–250k. Vega placements up, with pull-through of $25–40k.
- **Costs:** cash burn to "slightly tick up," and opex below $230M.
- **Q1 2026:** revenue up year over year but below Q4, with gross margin at the low end, around 41%. Instrument seasonality is stronger than consumables seasonality.
- **Growth drivers:** clinical HiFi adoption, with SPRQ-Nx and multi-use cells driving clinical growth and, eventually, margins.

Barclays called Vega "the big headline in the Q," opening doors that "could eventually help drive broader HiFi adoption w/in the clinic," since "the more researcher's hands HiFi is in, the better chances of making the shift to clinical applications." It said SPRQ-Nx "resets long-read economics at $300/genome," with launch "by 2H."

Barclays was "not expecting the funding floodgates to open" and predicted "another knife-fight of a 1H." It praised management for continuing to "keep hammering away at the opportunities." It planned checks at AGBT (the Advances in Genome Biology and Technology conference) to test for "an inflection point over the next 12-18mos" [Barclays, 2026-02-12].

Barclays also listed clinical adoption examples:

- **Rare disease and oncology:**
  - Berry Genomics won approval from China's regulator (the NMPA) for Sequel II thalassemia testing. Possible expansions are fragile X, spinal muscular atrophy (SMA) and Duchenne muscular dystrophy (DMD).
  - Children's Mercy adopted HiFi as a first-line diagnostic.
  - Radboud UMC consolidated several standard-of-care tests into one HiFi test.
  - Stanford uses Revio for pharmacogenomics.
  - Ambry Genetics is validating improved diagnostic yields.
  - The HiFi Solves consortium passed 15 members.
- **Carrier screening:** HiFi assays are being validated alongside short-read tests, with launches expected in 2026.
- **Population sequencing:**
  - All of Us, which published its first data in October 2025.
  - The Long Life Family Study, with about 8,000 samples.
  - The Asian Pan-Genome Consortium, with more than 10,000 samples.
  - Pipeline projects planning for hundreds of thousands of samples.

UBS called the print "incrementally positive but [it does] not change our view." The guide "seems conservative but faces an unfavorable academic/government end market." UBS questioned whether PacBio has the capacity to meet SPRQ-Nx volume, even though the product should lift sales and **incremental margins** (profit on each extra dollar of sales) [UBS, 2026-02-13].

### The March 2026 Barclays sector note and the PacBio downgrade

On 6 March 2026, in a sector note titled "The Bullet Train to the Singularity is Broken – Grab the Tools Train to Reality Instead," Barclays downgraded PacBio to Underweight from Equal Weight. Underweight means the stock is expected to underperform Barclays' coverage over 12 months. It cut the target to $1.50 from $2.00.

PacBio had fallen 26% between Anthropic's Claude clinical-research plug-in announcement on 3 February and 5 March, versus a 2% drop for the S&P 500. Barclays blamed "competition beginning to enter on long-read," not AI.

The reasoning [Barclays, 2026-03-06]:

- **Competition:** Roche's Axelios and Illumina's TruPath launches could cause a demand pause.
- **Consumables:** Barclays expected a first-half "air pocket" as customers wound down work ahead of SPRQ-Nx, which alone "could freeze PACB's market near term until customers burn off inventories."
- **Cost:** lower cost could be a "meaningful shift/inflection." Barclays heard less concern than in prior years about the multi-wash step in research. It could be a bigger hurdle clinically, where PacBio must win to unlock a larger **TAM** (total addressable market).
- **Timing:** population-sequencing wins would not reach the P&L until later years.
- **Stock appeal:** Barclays "debated a lot internally," but concluded "an illiquid stock with a 2H-weighted catalyst path is not likely to garner much investor interest."

The new target applied 4x EV/revenue to FY2026E revenue of $167M, down from 5x on $178M. EV/revenue is enterprise value (equity value plus net debt) divided by sales. FY2026 EPS moved to -$0.50 from -$0.53. On 14 April 2026, with the stock at $1.45, Barclays cut its target further to $1.00.

### Q1 2026 (reported 7 May 2026)

Revenue was $37.2M, flat year over year and $2.80M (6.7%) below consensus of $39.8M. Sources recorded EPS differently. Seeking Alpha recorded -$0.12, a $0.01 beat. Barclays recorded -$0.13, against its own -$0.12 and consensus of -$0.14. The line items [Q1 2026 call; Barclays, 2026-05-08]:

- **Instruments:** $9.7M, down 12% and 16.2% below the Street's $11.6M.
- **Consumables:** a third straight record at $21.8M, up 9%, but 2.4% below the Street's $22.3M.
- **Service:** $5.6M, down 7%.
- **Placements:** Revio's 15 units (versus 12) beat Barclays' 11. Vega's 27 (versus 28) missed Barclays' 36.
- **Gross margin:** non-GAAP margin fell to 37% from 40%, 400 bps below the Street's 41%. Non-GAAP figures exclude certain items, though PacBio keeps stock compensation in them.

CFO Jim Gibson gave three reasons for the margin drop:

- Higher memory (DRAM) and computing component costs.
- A one-time Vega promotion.
- One-time inventory and warranty charges.

Management explained the instrument weakness:

- **Funding:** U.S. academic funding pressure weighed on demand.
- **Vega promotion:** a "substantial portion" of the 27 Vegas sold under a limited-time promotion, mostly in price-sensitive APAC. Few U.S. buyers took it, which management read as a sign of funding constraints. More than 85% of Vega placements went to new customers.
- **Middle East:** conflict blocked shipments to the region. Management did not quantify this. Barclays put it at $1.5M of hardware, noting "$1.5m moves the needle" on a roughly $40M quarter.
- **Revio:** half of placements went to new customers, and clinical accounts kept placing multi-system orders.

Clinical shipments more than doubled, reaching a mid-teens share of consumable shipments, double the year-ago share. Some customers, including the largest Chinese accounts, delayed orders ahead of SPRQ-Nx. Barclays said the launch "froze some of the market on Revio consumables."

By region:

- **EMEA:** $10.8M, up 17%, as clinical customers moved from pilots to production.
- **Americas:** $16.7M, up 2%, led by commercial service providers and clinical labs.
- **APAC:** $9.7M, down 16%.

Operating figures, compared with a year earlier:

- **Opex:** fell 19% to $49.9M. Stock compensation was $3.8M versus $8.0M.
- **Net loss:** non-GAAP net loss was $35.9M versus $44.4M.
- **Cash:** about $276M, versus $280M at year-end, helped by the Illumina proceeds.
- **Headcount:** 492 versus 485.

Guidance changes:

- **Revenue:** the top of the FY2026 range fell $5M, to $165–175M, a 1.4% cut at the midpoint, against consensus of $174M. The guide assumes no meaningful A&G recovery, especially in the Americas.
- **Gross margin:** improvement was now expected toward the low end of +100 to +400 bps, because compute costs would "temper the pace." Barclays recorded the 41–44% range as maintained, with consensus at 42.2%. Margin was expected to improve in Q2.
- **Opex:** moved to $220–225M.
- **Vega pricing:** ASPs should normalize, with no further discounting.

Henry said Revio and Vega trends should "somewhat balance out," keeping the company within its February range. He said "perhaps as much as more than half of our consumable revenue over time will be clinically driven," without giving a date. Most of the consumables guide rests on the existing installed base, with SPRQ-Nx "the one variable."

Henry described three platforms for different customer scales: Vega, Revio and the coming ultra-high-throughput system. Mid-throughput customers would stay on Revio, and large clinical accounts would move to the new system. He did not address whether Revio orders might slow ahead of its launch.

Clinical programs cited on the call:

- **Ambry:** the ONCE study of 1,000 patients.
- **Ultra-rare disease:** work with n-Lorem and EspeRare.
- **University of Washington:** a study of sudden unexplained death in childhood across 200 families.
- **DNAstack:** a collaboration announced in late February to federate HiFi genomes through HiFi Solves. **Federated** data stay at their home sites but can be analyzed together. The consortium now has nearly 30 institutions in 15 countries and more than 10,000 genomes connected or committed.
- **Babies in Focus:** a newborn-screening study led by Eurofins Genomics UK, covering at least 2,000 samples. Of these, 1,000 will be sequenced on PacBio between April and September 2026. Henry called it foundational evidence for possibly including long reads in a UK national newborn screening program.
- **Market size:** about 300 million people live with a rare disease, and Henry said the market is in "early innings."

**The Basecamp Research deal** was the quarter's strategic headline. It was first press-released in mid-March 2026. PacBio will deeply sequence about **100,000 metagenomic samples**, meaning mixed environmental DNA, mostly from soil bacteria. Henry called it the largest HiFi project in company history and the first scaled use of HiFi to build a biological foundation model.

The samples feed Basecamp's "Trillion Gene Atlas." The atlas aims to grow Basecamp's dataset from 10 billion to 1 trillion genes and expand known genetic diversity up to 100-fold by sequencing up to 100-plus million species. The other partners are Anthropic and Ultima Genomics (a short-read rival), on NVIDIA infrastructure. The data train Basecamp's EDEN model, which designs therapeutics such as gene-insertion systems, antimicrobial peptides and cell therapies.

Barclays called it "the biggest deal in the company's history." It estimated $10–20M of revenue over 18 months, mainly in 2027, based on 100,000 samples at $100–200 each. It admitted it had "clearly underappreciated" the March release. It saw possible future deals in which AI companies get discounted sequencing in exchange for shared downstream economics: "the frontier is open." But "it is still very early... we look for more proof points before diving in both feet."

Barclays kept Underweight but raised its target 50%, to $1.50, "on the AI foundational biology model opportunities." The new target applied 4x to 2027E revenue of $187M, versus 3x on $190M before. Outside Basecamp, it called the quarter "unsurprisingly difficult," "a waiting game" [Barclays, 2026-05-08].

### Q2 2026 and the CEO change (reported 5 August 2026)

On 5 August 2026, Christian Henry stepped down as President and CEO after nearly six years. He stays on the board and advises his successor. Chief Operating Officer **Mark Van Oene** became CEO immediately. He joined in 2021 and led the R&D teams that built Revio, Vega and SPRQ-Nx before running commercial operations.

Van Oene's priorities are to scale the EMEA clinical model globally, drive SPRQ-Nx adoption, and expand HiFi throughput and data access. He summed up the plan as to "sharpen our execution, and run a leaner, more focused organization."

Analysts praised Henry. Canaccord's Kyle Mikson said "There's been the highs and the lows, but it's been overall a really impressive job." Barclays said his tenure "wasn't always smooth sailing, but he always made it fun" [Q2 2026 call; Barclays, 2026-08-05].

A reorganization begun in late July cut about 40 jobs. It folded marketing into the commercial organization and removed management layers, affecting "none of our key R&D platform projects." Quarter-end headcount was 492, versus 491 a year earlier.

Results, with year-ago comparisons:

- **Revenue:** $39.0M, down about 2% from $39.8M and $1.57M below consensus.
- **Instruments:** $12.8M, down 9%, on lower ASPs from strategic Revio pricing and fewer Vega units.
- **Consumables:** $20.1M, up 6% but flat sequentially. Customers were using up old reagent inventory and validating SPRQ-Nx.
- **Service:** $6.1M, down from $6.7M, as a population sequencing program ended.
- **Pull-through:** about $202k per Revio.
- **Clinical shipments:** up 67%, still a mid-teens share of consumables.
- **Revio:** 20 units versus 15, beating Barclays' 15. Of these, 60% went to new customers and 45% came in multi-instrument orders. This included a significant order from a new, unnamed population-scale customer starting in Q3.
- **Vega:** 26 units versus 38, below Barclays' 32. 81% went to new customers, and ASPs normalized. U.S. public health labs bought units, including for wastewater testing.

By region:

- **EMEA:** $14.4M, up 52%, on clinical production and a multi-system Revio order for a national genomics initiative.
- **Americas:** $17.6M, down slightly.
- **APAC:** $7.0M, down 45%. A large population program ended, academic funding weakened and customers burned down inventory.

Margins, costs and cash:

- **Gross margin:** non-GAAP margin was 36%, down from 38%. Barclays read it as 35.6%, versus about 38.9% for the Street. The causes were compute inflation, lower volumes and $1.1M of costs to bring Vega manufacturing in-house. Gibson said PacBio had bought enough memory through end-2026.
- **Opex:** $56.1M, down 3%.
- **Net loss:** $41.9M, or $0.14 per share, versus $0.12 expected by Barclays and $0.13 by consensus.
- **Cash:** $236.9M.

**SPRQ-Nx rollout.** More than a third of the installed base adopted the enabling software in June. Management expects more than half by end-Q3 and the vast majority by year-end. HiFi yield was "near identical across the first two uses with a slight decline on the third." On Vega, SPRQ-Nx raises output to 90 gigabases per run from 60 and lowers DNA input requirements.

Two papers supported the clinical case:

- **New England Journal of Medicine** (13 June 2026, Bitter et al.): long-read genome sequencing showed 96.4% concordance with standard care. Long reads improved diagnoses in 3.4% of cases, while standard care caught misses in only 0.2%.
- **Nature Genetics** (Sabbagh et al.): the paper proposed "near-perfect genome sequencing."

A HiFi Solves study of subfertility also appeared; subfertility affects about one in six couples. For Basecamp, hundreds of samples were being sequenced weekly, with most to come in 2027.

**Guidance was cut again.** The new FY2026 figures:

- **Revenue:** $155–165M.
- **Gross margin:** 35–37%, including about $2.5M of Vega transition costs.
- **Opex:** $215–220M.
- **Year-end cash:** about $175–185M.
- **Pull-through:** $200–225k.

Management cited slower SPRQ-Nx adoption, compute costs, strategic Revio pricing, no A&G recovery and a slower China rebound. **Cash-flow breakeven moved to 2028.** For 2027, management expects $15–20M of compensation savings, plus another $15–20M as HT platform development spending ends. Gibson said existing cash funds the business through breakeven and the HT launch. Van Oene called the outlook "a really balanced view."

Barclays kept Underweight and cut its target 17%, to $1.25, at 4x 2026E revenue of $159M (from $167M). The stock was at $1.30. Barclays argued the cut reflects an SPRQ-Nx "air pocket" bottoming in Q3–Q4 2026, not weak demand: "not as bad as it looks."

The hardest task, in Barclays' view, is converting U.S. and smaller clinical labs to production. The U.S. market is "very different and more fragmented." Labs there face data-analysis limits, the need for automated sample preparation and a "legacy bias toward short-read," which makes the work "more hand-to-hand." Barclays expects the stock is "likely to lag peers given all of the moving pieces," and an "extended demand pause on capex" is possible [Barclays, 2026-08-05].

### Morgan Stanley conference (15 September 2026)

Van Oene told Morgan Stanley's Michael Podoll that "this is not me making a wholesale change on the strategy. It really is... the execution." His priorities for the next 12–18 months:

1. **Land the restructuring.** Van Oene expects about **$40M of 2027 savings** from headcount and non-recurring expenses. "We've had to go through 3 restructurings in 3 years, and we've exited the short-read business."
2. **Complete the SPRQ-Nx transition.** The goal is to exit 2026 with consumable and margin growth. Pull-through is "closer to $200,000" and should stay there through Q3 in "a 2-quarter transition," recovering by year-end.
3. **Launch the HT platform in 2027.** The platform was spared from the cuts and is the largest R&D cost. Van Oene described it as end-to-end: the sequencer plus data software ("precision health intelligence"). Other R&D includes Kinnex updates and library-preparation automation. All Vega manufacturing is moving in-house to Menlo Park.

The multi-use SMRT Cell was Van Oene's "most underappreciated" point. The chip is "the majority of the cost of our sequencing." Spreading it over two or three uses, and eventually four or five, changes both price and margin. "For the first time, I'm staring at a product line that will have the gross margin that will actually make us a sustainable company."

Van Oene named three indicators to watch:

- Gross margin back above 40% through 2027.
- Clinical consumables growth of "50-plus percent" over the next couple of years.
- A successful HT launch setting up 2028 breakeven: "Not many labs have ever run 10,000 genomes a year."

**Regional strategy.** Europe has moved HiFi to a frontline rare-disease test, meaning the first test ordered rather than a follow-up (reflex) test, with volumes in the "thousands of samples." The U.S. will start with carrier screening, such as Quest's ataxia panels. Revio can handle "hundreds of thousands" of targeted samples but not yet that many whole genomes.

**Partners, biopharma and software.** PacBio will partner for interpretation and clinical reporting, and it sees biopharma interest in HiFi for target discovery. Its software covers:

- **Phasing:** assigning variants to each parent's copy.
- **Structural variants and copy number.**
- **Paralogs:** near-duplicate gene copies.
- **Methylation:** chemical tags on DNA.
- **HiFi Solves:** a sovereign, federated data network.

**Funding.** Van Oene said "I haven't seen a budget flush," the usual year-end spending burst. He expects no NIH improvement and said U.S. revenue is flat because clinical growth only offsets academic declines. Basecamp-style AI deals are "not... in our base case model" for margins or breakeven [Morgan Stanley conf., 2026-09-15].

## Analyst views

### Barclays (Luke Sergott, with Salem Salem and Anna Kruszenski)

Barclays is the most frequent voice in this material. It consistently says it likes "the underlying technology, revamped business & story, strong management team, and innovative launches." Through February 2026 it stayed on the sidelines because the stock traded "at a 20% premium to peers" and multiples could contract. Its industry view on U.S. Life Science & Diagnostic Tools was Neutral in 2025 and Positive from February 2026.

The table below traces Barclays' rating and target. It shows a steady markdown from $14 in 2023 as the shares collapsed, followed by small moves around $1–2. The May 2026 note wrongly implies the downgrade happened in 2025; it occurred on 6 March 2026.

| Date | Share price | Rating | Price target |
|---|---|---|---|
| 10 May 2023 | $12.03 | Equal Weight (initiation) | $14.00 |
| 28 Sep 2023 | $8.36 | Equal Weight | $9.00 |
| 31 Oct 2023 | $7.11 | Equal Weight | $8.00 |
| 9 Apr 2024 | $3.45 | Equal Weight | $3.00 |
| 9 May 2024 | $1.68 | Equal Weight | $2.00 |
| 24 Jun 2025 | $1.27 | Equal Weight | $1.50 |
| 15 Dec 2025 | $2.17 | Equal Weight | $2.00 |
| 6 Mar 2026 | $1.52 | Underweight | $1.50 |
| 14 Apr 2026 | $1.45 | Underweight | $1.00 |
| 8 May 2026 | $1.65 | Underweight | $1.50 |
| 5 Aug 2026 | $1.30 | Underweight | $1.25 |

Barclays' target methods and scenarios changed as follows:

- **August 2025:** $1.50 at 4x 2026E revenue of $173M (up from about $165M), with an upside case of $3.00 and a downside case of $1.00.
- **November 2025:** $1.50 at 4x $169M (from $172M). Barclays held the target "given the volatility in shares due to the illiquidity of the stock."
- **February 2026:** $2.00 at 5x $178M.
- **August 2026:** $1.25, with the upside case cut to $2.50.

The scenario logic never changed. The upside rests on easing macro conditions, better funding, or scientists "flock[ing] to PACB as the premier provider of long-read tech." The downside rests on prolonged macro pressure, a guidance miss or tighter budgets.

The next table compares Barclays' long-range models. It shows three trends:

- Revenue estimates drifting down.
- Losses narrowing sharply in 2027.
- Modeled cash running out, which implies new financing.

| Note | 2026E revenue | 2027E revenue | 2027E gross margin | 2027E EPS | Cash, end-2026E / 2027E |
|---|---|---|---|---|---|
| Aug 2025 | $173M | $192M | 48.9% | -$0.27 | $68M / $12M |
| Nov 2025 | $169M | $188M | 49.1% | -$0.24 | $92M / $46M |
| Feb 2026 | $178M | $192M | 47.6% | -$0.24 | $56M / $7M (-$68M 2028) |
| Mar 2026 | $167M | $191M | 47.5% | -$0.24 | $66M / $17M |
| May 2026 | $166M | $187M | 47.7% | -$0.23 | $62M / $15M (-$57M 2028) |
| Aug 2026 | $159M | $186M | 47.8% | -$0.23 | $15M / -$28M (-$98M 2028) |

Other model points:

- **2027 EPS:** Barclays' estimate of about -$0.23 is far better than consensus of -$0.41 to -$0.43. The gap comes from modeled cuts that bring SG&A (selling, general and administrative costs) to 55% of sales and R&D to 30%.
- **Balance sheet:** shareholders' equity turns negative in 2026, at about -$146M to -$157M. Debt is modeled at $585M to $747M across the notes.
- **Unexplained gap:** Barclays' 2025 free-cash-flow estimate of -$181M (November 2025) did not match management's $115M burn guidance.
- **Market value:** market capitalization was $378M (August 2025), $575M (November 2025), $555M (February 2026), $512M (May 2026) and $403M (August 2026).
- **Per-share figures:** the 52-week low rose to $1.09 by August 2026, and book value per share fell from $0.30 to $0.01.

### UBS (Dan Leonard, Lu Li, Nathan Bolanos)

UBS rates PacBio Neutral with a $1.50 target, set on 13 February 2025 and kept on 13 February 2026. The target rests on about 5x next-twelve-months EV/sales. With the stock at $1.73, it implied a -13.1% return.

Because the stock is volatile, UBS widens its rating bands to ±25% around its 8.5% market return assumption, versus the normal ±6%. As a result, even a -21.6% expected excess return remains a "core banding exception" Neutral.

UBS's rating history:

- Neutral in 2023, with $12–13 targets.
- Buy from November 2023 to March 2024, with $10.00–12.50 targets.
- No rating from 28 March 2024, at $3.75.
- Neutral since November 2024, with a $2.00 target, later $1.50.

UBS's EPS estimates, against consensus:

| Year | UBS estimate | Prior UBS estimate | Consensus |
|---|---|---|---|
| 2026 | -$0.46 | -$0.50 | -$0.52 |
| 2027 | -$0.38 | n/a | -$0.49 |
| 2028 | -$0.31 | -$0.29 | -$0.42 |

UBS's long-range model:

- **Revenue:** $173.3M (2026E), $198.7M (2027E), $243.8M (2028E), $310.6M (2029E) and $348.0M (2030E).
- **Gross margin:** rising from 41.8% to 53.8% over the same period.
- **Operating cash flow:** turns positive in 2029, at $1.4M.
- **Cash:** $235.7M at end-2026, then held at $200M by assumed new debt of $26.0M, $47.4M and $13.0M in 2027–2029.
- **Equity:** $5.3M at end-2025, negative thereafter.

UBS's short-term quantitative views:

- **Industry structure:** deteriorating (2 of 5).
- **Regulatory environment:** improving (4 of 5).
- **Next EPS:** in line with consensus.
- **Risks:** skewed to the downside.
- **Catalysts:** none expected in the next three months.

UBS's listed risks are technology delays, field reliability, the macro environment, China and tariffs, pharma and academic budgets, new entrants, financing and currency.

### The Barclays life-science-tools sector note (6 March 2026)

**Tools** companies sell instruments, consumables and software to labs. **Contract research organizations (CROs)** run clinical trials for drug makers. Both groups sold off in early 2026 after Anthropic launched its Claude life-science plug-in and, on 3 February, its clinical-research plug-in. Barclays argued this "Claude crash" was largely overblown.

**AI will create more lab work, not less.** Barclays' main argument is that AI will create more wet-lab work (physical experiments), not less. Biology "is incomplete at best and wrong at worst. This is why we do experiments." Faster AI-driven design frees scientists for lab time and drives more experiment iterations that feed back into models. Twist's AI-driven drug discovery boom is the evidence. AI should also raise pharma's return on R&D, so pharma will not cut R&D.

**CRO fears are overblown, for four reasons:**

- **Regulation moves slowly:** "the FDA only started allowing PDFs or digital submission of data in 2016/2017."
- **Outsourcing will persist.**
- **Data access matters:** ICON once sourced 70 datasets per trial.
- **Big CROs will build better AI:** large CROs will build better tools than "a model vibe-coded by a pharma company."

**Top picks.** Barclays has the most conviction in 10x Genomics, Twist, Charles River and Danaher. 10x and Twist are "clear winners." Danaher is the near-term favorite after a penalty for its Masimo deal. Thermo Fisher "will... be an AI winner somehow," with value to unlock once fears about its PPD CRO unit fade.

The table below shows returns from 3 February to 5 March 2026 with Barclays' explanations. It shows that most large drops had non-AI causes.

| Stock | Return | Barclays' explanation |
|---|---|---|
| Fortrea | -40% | AI plus bookings weakness |
| ICON | -34% | AI plus accounting investigation |
| PacBio | -26% | Long-read competition |
| Avantor | -21% | Underperformance, weak 2026 guide |
| Guardant / Natera | -20% / -14% | Multi-cancer early detection failure noise, diagnostics competition, AI, valuation |
| Repligen | -18% | Guidance |
| Medpace / IQVIA / Charles River / Thermo Fisher | -17% / -13% / -11% / -10% | AI (Medpace also cancellations) |
| Sotera | -16% | Secondary offering |
| Waters | -16% | Becton Dickinson deal |
| Agilent / Qiagen | -11% / -11% | M&A fears / fading deal hopes |
| Certara | -10% | AI and guidance |
| Bruker | -9% | Lowered omics target, fading academic recovery trade |
| Mettler-Toledo | -8% | China and Iran fears |
| Danaher | -8% | Masimo deal |
| Illumina | -5% | Short covering on better-than-feared EPS |
| Revvity | -5% | Roche pricing news offset by AI |
| S&P 500 | -2% | Benchmark |
| Exact Sciences / Labcorp | +1% / +1% | Abbott deal approved / defensive positioning |
| Twist | +5% | AI drug discovery |
| West Pharmaceutical | +6% | Strong EPS |
| Quest | +10% | Volume and guidance beat |
| 10x Genomics | +12% | 10x Claude plug-in and Roche Axelios kit |

Several rating actions in the note use EV/EBITDA. EBITDA is earnings before interest, taxes, depreciation and amortization. The actions:

- **IQVIA:** upgraded to Overweight, with a $210 target (12.5x EV/EBITDA on $3.98B of 2026E EBITDA). Management put AI exposure at about 5% of revenue. Barclays estimates that equals 15–20% of Technology & Analytics Solutions revenue and under 3% of EBITDA. Upside case $250, downside $160.
- **Medpace:** upgraded to Equal Weight, with a $500 target (23x on $620M). It "closed the gap" on valuation, but Barclays wants to understand rising cancellations first.
- **Avantor:** downgraded to Underweight, with the target cut to $8.50 from $9 (10x 2027E EPS of $0.83). Its problems are company-specific: share losses and a multi-year turnaround.
- **Certara:** downgraded to Equal Weight, with an $8 target (10.5x on $131M). Barclays "did not appreciate how much of a fixer-upper the business was." The new CEO is Jon Resnick, and short interest is about 18% of float.
- **PacBio:** downgraded to Underweight, as described above.
- **ICON:** kept at Equal Weight, with the target cut to $120 from $200 (9x on $1.57B). The risk is a possible backlog restatement after 2% revenue overstatements in 2023–2024. Barclays leans toward the 30 April update being "a nothing burger."
- **Fortrea:** stays at Equal Weight.

Illumina was not rated in this note. It matters here for its modest 5% decline and for TruPath as a threat to PacBio.

## Key tensions to keep in mind

The sources agree on three points:

- Clinical demand, especially in Europe, and consumables are real bright spots.
- U.S. academic funding is not recovering.
- The SPRQ-Nx transition caused a temporary consumables dip.

They differ on outlook. Management calls SPRQ-Nx a margin breakthrough and says current cash funds the company to breakeven. Barclays sees an illiquid, cash-burning stock with a second-half-weighted catalyst path. Its own models show a funding gap by 2027–2028.

Timing has repeatedly slipped:

- SPRQ-Nx moved from "early 2026" early access to a late-May launch.
- Breakeven moved from 2027 to 2028.
- Gross margin guidance fell from 41–44% to 35–37%.

Van Oene's comments are also slightly inconsistent. He calls SPRQ-Nx "a 2-quarter transition," yet says the company must succeed "through 2027" to get margin back above 40%. Basecamp and other AI deals are upside that management deliberately excludes from its base case.
