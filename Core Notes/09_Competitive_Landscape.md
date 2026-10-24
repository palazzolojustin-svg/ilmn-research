# The Competitive Landscape in Sequencing

*Core Notes section 09. Synthesized from 8 Core Notes sections as of 2026-10-10. Bracketed tags cite the source; full detail is in Working Notes (see INDEX.md).*

Illumina remains the default supplier of DNA sequencing almost everywhere, but it now faces a different rival in nearly every part of its market. Ultima Genomics and Roche attack the high-volume end. Element Biosciences attacks mid-sized labs. Oxford Nanopore (ONT) and PacBio hold the long-read niche. MGI dominates China. 10x Genomics leads single-cell and spatial biology, and Thermo Fisher owns Olink in proteomics. A former Illumina associate director summarized the problem: "they're trying to compete with many companies, while these competitors are only competing with Illumina" [Expert: ex-Illumina AD now at Kailos, Aug 2026].

Most sources describe gradual erosion rather than collapse. Clinical customers are sticky, switching is slow, and rivals are usually added alongside Illumina instruments rather than replacing them.

No source gives an audited market-share figure. The expert estimates below differ widely and none cites a firm source.

| Source | Illumina share claim |
|---|---|
| Former Illumina AD, product management [24 Jul 2026, citing DeciBio] | Fell from ~80% to the mid-60s%, losing ~3 points a year; should "flatline" near 50% |
| Former Illumina field application scientist [24 Jul 2026] | Fell from 80% to 70%; "at least 30%" more to lose by 2029–30 |
| Former Illumina AD, now at Kailos [Aug 2026] | 80%+ of installed instruments, "depending on whose number you look at" |
| LifeStrands Australia lab director [25 Jul 2026] | "Something like 95%" (a loose guess) |
| Abbott senior scientist [29 Jul 2026] | Thermo Fisher still holds "at least 10%-15%" (unsourced) |

The experts named three sources of Illumina's stickiness:

- an end-to-end system of instrument, sample-prep kits and DRAGEN analysis software;
- a workforce trained on Illumina;
- clinical tests already validated on its machines.

Illumina was called "the gold standard" [Expert: Roche UK lead, Jul 2026], "the workhorse of the industry" [Expert: ONT senior director, ~Oct 2026], "almost the IBM" of sequencing [Kailos expert, Aug 2026] and "becoming like Kleenex" [Expert: Daisy Lab co-founder, Jul 2026].

## High-throughput short-read sequencing

### Why the core business stalled

Short-read sequencing reads DNA in fragments of a few hundred letters at very high volume. It is Illumina's core business.

Former employees explain why growth stopped. In earlier product generations, halving the price led customers to sequence four times as much. NovaSeq 6000 (about 2018) cut price from about $20 to about $5 per gigabase (a billion DNA letters), and pent-up demand drove 5X–10X more sequencing. From NovaSeq onward the pattern broke: halving price might bring only 25% more volume. The cause was competition, first from BGI/MGI and then from Singular, Element and Ultima in 2021–22. The result was "real flat growth starting in about 2022 and to the present day" [Expert: ex-Illumina AD, multi-omic assays, 23 Jul 2026].

The blended high-throughput price has fallen from about $5 toward $2.50 per gigabase, roughly 30–40% since 2022. Volume gains have only offset that decline. For core sequencing consumables (the reagent kits bought for every run, which the client put at 60–70% of revenue), "flat would be a huge win."

NovaSeq X, launched in 2022, worsened this. It cost about the same as a NovaSeq 6000 but delivered the output of four 6000s at "almost half, if not 1/3" the run cost. Customers "sequenced everything in the freezer" and then ran out of samples [Kailos expert, Aug 2026].

The same expert estimated per-genome costs for a 30X genome (each DNA position read about 30 times, roughly 100 gigabases):

- sequencing on NovaSeq X at list price, about $250;
- sample preparation at scale, under $100;
- clinical data processing, $500–1,000;
- research data processing, $50–200.

As a result, cutting the sequencing price from $100 to $80 changes a clinical lab's total cost by only about 5%. Another former employee put the threshold at about a $100 genome or $1 per gigabase. Below that, sequencing is only 5–10% of workflow cost and cheaper reads barely matter [Expert: ex-Illumina AD, 24 Jul 2026].

### Illumina's response: cheaper flow cells, rental and an ecosystem

Illumina is extending NovaSeq X with new flow cells rather than new boxes. Flow cells are the consumable chips, labelled by billions of reads. The X launched with 1.5B, 10B and 25B flow cells; 5B, 14B and 35B followed or are on the 18-month roadmap, along with staggered runs and Q70 accuracy [Q1 2026 call]. A Q score is a log measure of accuracy: Q30 is one error in 1,000 bases and Q60 one in a million.

The 35B flow cell should cut price from about $2.50 to about $2 per gigabase, roughly 20% [23 Jul 2026 expert]. A genome center expected it in January 2027 [Expert: genome center VP, 31 Jul 2026]. UBS said Illumina's roadmap implies about $150 per genome if the 35B is priced like the 25B [UBS, 2026-02-26]. Barclays doubted competitive pricing is possible given "inherent technological barriers" [Barclays, 2026-07-31].

Reagent rental means placing an instrument free or cheaply in exchange for multi-year consumable commitments. One expert said Illumina refused it while they were there (to mid-2025) but it had "become a necessity," because cash-burning rivals "will absolutely" discount instruments 90%. Another said Illumina now offers it, with free Hamiltons, NextSeq 2000s, training and a year of ICI software at threatened sites such as Memorial Sloan Kettering [Expert: ex-Illumina FAS, 24 Jul 2026]. The Q1 2026 call confirmed some NovaSeq X deals carried reagent-rental, lease or volume-discount terms.

### Placement momentum surprised analysts

NovaSeq X placements repeatedly beat Illumina's quarterly framework of 50–60 units:

- more than 100 in Q4 2025 (installed base about 890);
- more than 80 in Q1 2026 (base about 970);
- more than 95 in Q2 2026, about 70% clinical, with up to half adding capacity rather than replacing older machines.

The transition to NovaSeq X is nearly complete. Its share of high-throughput consumables revenue rose from 44% (Q2 2025) to 55% (Q4 2025 and Q1 2026) and 59% (Q2 2026). In Q2 2026 it carried 83% of gigabases, 92% of research volume and 78% of clinical volume.

Management's 2026 pull-through guide is $1.35–1.40 million a year per NovaSeq X and $600–650 thousand per NovaSeq 6000 [4Q25 call, via JPM]. Pull-through means yearly consumables revenue per installed instrument. In Q1, management said about $1.3 million "or higher."

### Pricing: a race to the bottom, with opaque quotes

Short-read pricing was called "a race to the bottom" by the PacBio segment lead [Aug 2026] and by the former product director [24 Jul 2026]. Element pushed Illumina's consumable margins "below 50% in some cases" [24 Jul 2026].

The Broad Institute gets "insane" discounts across its "10+" Illumina sequencers and uses Ultima's "crazy pricing" as leverage. Academic contracts "can very quickly become null and void" when rivals undercut by 25–50% [23 Jul 2026 expert]. Customers complained of three things:

- **Opaque quotes:** Illumina gives individualized quotes rather than unified price lists [Expert: South Carolina core, Jul 2026].
- **Broken promises:** promised discounts were not honored [Georgia core, Jul 2026], or were withdrawn after a year [Expert: Sr. Staff ML scientist, Jul 2026].
- **Annual price rises,** in contrast to Element's prices, which do not change over a product's life [Arizona core, Jul 2026].

A Natera manager agreed that many uses need only "good enough" data at about 30% of the cost.

Barclays suspected quiet discounting. In Q1 2026, NovaSeq X's share of gigabases rose 500 basis points to 76% (Barclays' figure) while its revenue share stayed at 55%. Management called that reading "a frivolous exercise" because flow-cell mix creates noise [Barclays, 2026-04-30]. BI said Illumina was "in the early stages of trading price for volume" [BI, 2026-05-01].

The counter-evidence comes from customers. JPM's survey of 62 customers found planned volume growing only 2.4–5.2 points faster than planned spend, implying much smaller price cuts than the recent double-digit declines [JPM, 2026-06-10].

### Ultima Genomics

Ultima is private and attacks the high end. The Kailos expert called that "probably the biggest space where there is lack of competition."

**Product and pricing:**

- Ultima's first generation was "terrible," needing an on-site engineer eight hours a day plus new cooling and floor reinforcement [24 Jul 2026].
- Its UG 200 claims a sub-$100 list genome. One expert recalled $80–110 per sample for low-depth uses such as oncology, prenatal, transplant and local labs, while saying UG200 pricing is "comparable with Illumina" [Natera expert, Jul 2026].
- The expert recalled that Solaris chemistry needs about 50% less DNA input, cuts cost 30%, brings cost below $0.40 per million reads and supports a "somewhere $50 genome."
- JPM listed an $80–100 target genome [JPM, 2026-05-13].

**Accuracy:** Ultima's ppmSeq library prep reaches Q60 [ML scientist] or Q70 [24 Jul 2026 expert]. At one start-up the ML scientist chose Ultima for a laboratory-developed test because it was 2X–3X cheaper even before a "really good discount." Base quality sets "your ceiling" in liquid biopsy, where tumor DNA may be one read in a million.

**Wins:** Ultima is pulling projects from a Georgia academic core. Its share of that core's lost volume rose from about 10% two years ago to about 20%, with 80–90% still going to low-cost service centers such as Novogene. The core expects the pressure to "Accelerate" [Georgia core, 31 Jul 2026]. Some population projects are "secretly validating" Ultima [ex-FAS]. The Roche UK lead heard Foundation, Guardant and Natera are talking to Ultima, and that cutting Guardant's cost this way would be "a huge competitive advantage." 10x's CEO credited Ultima and Roche, not Illumina, with a "huge" drop in price per read that makes mega-scale single-cell projects possible [BofA, 2026-05-13].

**Doubts:** read quality "is still questionable" [South Carolina core]. Some labs hesitate over Ultima's size [Abbott scientist]. The ONT director said "Ultima's doomed in the long run" and nobody chases it "to the bottom."

### Element Biosciences

Element is private and attacks the mid-range.

**VITARI (unveiled 19 February 2026).** UBS's partly garbled comparison with the NovaSeq X Plus showed:

- an instrument about 40% cheaper than the X Plus's $689,000 list;
- consumables about one-tenth the cost per run (about $3,000 versus $32,000);
- about half the cost per gigabase;
- about one-fifth the output per run (3T versus 16T);
- shipping in the second half of 2026 [UBS, 2026-02-19].

Experts recalled VITARI at about $700,000 versus more than $1 million for NovaSeq X, with 50X genomes for "somewhere over $70" [Natera expert], or "about half" an X's price with similar capacity [ex-FAS].

**Technology and positioning:**

- AVITI's quality was "simply better." Element's sequencing-by-binding avoids the "unnatural bases" that make enzymes struggle on longer reads [24 Jul 2026 expert].
- Element has pursued an ecosystem "from day one." It moved from AVITI to AVITI24 with single-cell and spatial, and bundles SOPHiA or SeqOne software, automation scripts, five years of free cloud storage and dedicated staff.
- It lacks NIPT, oncology and infectious-disease panels [ex-FAS].

**Adoption:** the Abbott scientist named Element the threat with the best chance. But the PacBio lead said Element and Ultima drew "a lot of hype" three years ago "and now we're not seeing as much adoption," with Roche displacing them as the main concern.

### Roche AXELIOS 1 (SBX)

**Technology and timeline.** Roche's sequencing-by-expansion (SBX) chemistry came from its 2020 purchase of Stratos Genomics. It copies DNA into a stretched "Xpandomer" read through an 8-million-well reusable CMOS sensor. Roche unveiled it at AGBT in February 2025, priced it on 26 February 2026 and launched it for research use only (RUO) on 29 June 2026.

**Roche's claims:**

- **Duplex mode** (reading both strands): 1.8 terabases and about 16 genomes in four hours, at Q38 (about 99.98%).
- **Simplex mode:** 40 billion reads averaging 175 bases, with long reads up to 1,500 bases [H1 2026 call].
- **Prices:** $150 per genome "with no volume-based discounting," $0.06 per million reads, and about $25 per sample for a 1.1-megabase liquid-biopsy panel [Roche DX Day, 2026-05-12].
- **Reuse and price:** the sensor module can be reused up to 20 times; the instrument costs about $750,000.
- **Ambition:** "blockbuster" sales of more than $1 billion, with about 100 systems in year one. By September, roughly one-third of placements were made with no "teaser offers" [JPM, 2026-09-15]. Barclays called progress "well" against 100 orders [Barclays, 2026-09-28].

**How Roche's price compares.** JPM put Roche's $150 genome roughly 25% below the ~$200 it estimated for NovaSeq X [JPM, 2026-02-26].

UBS called the pricing "relatively benign." Large Illumina customers already pay similar prices. UBS saw more exposure in "counting" uses such as RNA-seq, where $0.06 per million reads compares with Illumina's $0.68 list on the 25B flow cell. It put counting at about 16% of Illumina's consumables [UBS, 2026-02-26].

Experts heard by UBS were split. One already paid $175 per genome after Illumina discounts and believed large users pay $125. Pathologists called sensor reuse "a nonstarter" for MRD.

**Analyst views:** Barclays saw a "well capitalized competitor" and "another round of pricing headwinds in 2027 and beyond." BI said disruption "is unlikely to be immediate" but Roche "could still chip away" [BI, 2026-06-26]. JPM upgraded Illumina to Overweight on 10 June, partly because its survey showed:

- 40% of customers had not heard of AXELIOS;
- only 8% would buy within 6–12 months;
- about 11% of potential buyers would retire an Illumina instrument;
- 37–39% said an Illumina reagent-rental offer would deter them from buying AXELIOS.

**Expert views evolved over the year:**

- **Early 2026:** speed matters little in oncology, saving about 12 hours on a long chain [Tegus expert, est. Jan 2026].
- **July:** "the main disruptor," but switching is impractical. The four-hour deep run needs 150 ng of DNA, "nearly impossible from a real patient" [Natera, Jul]. AXELIOS is "not ready," with perhaps "10, 15 tops" of every 100 instruments bought in 2027 [23 Jul]. It is "an enabler, not a replacer," aimed mainly at cutting Roche's own cost of goods [ML scientist].
- **August onward:** "a lot of hype without a lot of data" [PacBio lead]. Minimal impact in a year but more pressure than smaller rivals later; the genome center will likely buy "a couple" boxes [genome center VP]. It will "just simply die out" [South Carolina core]. It could take 10–20% over about three years and $1–2 billion of revenue in 10 years, "a complete dart at the wall" [ONT director]. Its single-cell data were "very similar" to Illumina's, but an ecosystem needs five to ten years, or five to seven if Illumina cuts to $100–200 genomes [Brigham specialist].

The former Roche software engineer called SBX data "much cleaner" than anything they had seen but said "there won't really be a winner takes all." Some of Illumina's third-party-panel users "quietly placed Roche" after price rises [ex-FAS].

### MGI and other short-read rivals in the West

The Daisy Lab expert called MGI's kits "off-brand equivalents" producing "the same data and at lower cost." One New Zealand agricultural provider is "ditching their very large Illumina sequencers for MGI" purely on cost.

Other experts were less impressed. MGI has "lost its touch," and the UAE's M42 site "kicked out" MGI "in less than 48 hours" [ex-FAS]. It "rarely shows up in deals" [24 Jul]. Complete Genomics has "very limited presence in the U.S." [Abbott]. The Roche UK lead heard MGI is "not quite as accurate."

## Benchtop and lower-throughput sequencing

This is where Illumina appears most exposed.

Arizona's core said lower-output Illumina systems are losing favor "because the cost per base is no longer competitive" [Arizona core, 22 Jul 2026]. Low throughput is "dying because sequencing has gotten so cheap," yet abandoning it lets Element win early relationships, especially in developing countries [24 Jul]. Illumina never "really worked that hard" in this segment [Tegus].

Small labs pay much more per letter. The gap was put at up to "100X" between small and large users [Daisy Lab]. Even on the same box, the Broad, Natera, Guardant and Foundation may pay a half or a quarter of a small contract lab's price, a gap reaching "five or tenfold" on low-throughput instruments [24 Jul].

**Product changes.** Legacy MiSeq, NextSeq 550 and iSeq are being retired in favor of the MiSeq i100, a two-color XLEAP system needing no engineer install [ex-FAS]. The i100 is "really turnkey" with on-instrument analysis [ex-Illumina scientist now at Roche, Aug 2026]. Over $100,000 for the i100 Plus limits adoption, though the Georgia core will buy one within 12 months.

NextSeq remains a "workhorse" for clinical labs too small to fill an X. Its 2026 pull-through guide is $80–100 thousand (NextSeq 1k/2k) and $90–110 thousand (500/550). Hospitals that cannot batch samples want small machines to backfill the retired MiSeq for targeted panels, still the largest low-throughput market [PacBio lead]. The ONT director estimated NextSeq-class revenue at about $500 million to $1 billion, an eighth to a quarter of Illumina's total.

**Element is the main mid-range winner.**

- Arizona's core runs AVITI as its primary sequencer.
- South Carolina's core is buying an AVITI24 with NIH money and hopes "at least 80%" of in-house work moves to it, even though its Illumina output rose about 40% in Q2 2026 on outsourced NovaSeq X runs.
- An AVITI at about $500,000 (one billion reads per flow cell) beats a NovaSeq 6000 site on price but loses to an X Plus site [ex-FAS].
- Smaller cores switch to Element on capital cost, which the Georgia director, an NIH equipment-grant reviewer, considers overpriced.
- The Abbott scientist relayed Element's claim of a $100 genome later in 2026.

**Other benchtop rivals:**

- **GeneMind** copied an older Illumina box "down to the exterior" at "insanely low pricing" and is spreading in China, Southeast Asia, the Middle East and the US, though limited to small panels.
- **Thermo's Ion Torrent and Genexus** win on a seamless sample-to-report workflow for small panels. Labs often start there and graduate to Illumina [Tegus]. Genexus "sometimes falls over" [LifeStrands] and cannot do whole genomes beyond 1X–5X coverage. Its Oncomine line is "losing the market" [ex-FAS].
- **Singular Genomics** machines are expected to lose share [Arizona].
- **Roche** argues its one-to-four-pool loading gives mid-throughput users high-throughput economics. The Brigham specialist said this would save about a week of batching on a six-to-eight-week library-to-data cycle.

Capital cost is the biggest friction in this segment. "An outright purchase of a machine that's over $500,000 is just much less feasible" for non-profit cores with "very, very thin" margins [Arizona]. Lease-to-own options matter [Abbott]. Experts disagree on whether lab-by-lab instrument buying will return. 10x's CEO argued the era when "every single lab" bought its own instrument is over.

## Long-read sequencing

### A valuable but specialized niche

Long-read sequencing reads continuous stretches of thousands of letters or more. Nearly every expert sees it as about 10% of demand, a figure usually offered by interviewers.

Its main uses are:

- rare disease and repeat disorders such as Huntington's and Fragile X;
- structural variants (large DNA rearrangements, which short reads miss "almost 1/3" of in MRD, per the Natera expert);
- phasing (assigning variants to each parent);
- native methylation (chemical tags on DNA, read "for free");
- pathogens, full-length RNA isoforms and HLA typing.

Its barriers are cost, missing population databases, short-read-based software and immature clinical workflows. The PacBio lead said accuracy for inherited-DNA uses "is basically there."

The Kailos expert gave a rare-disease yield framework, shown below. It explains why many labs stop at a short-read genome: they accept "I did my best and got 90%."

| Test | Share of cases answered |
|---|---|
| Gene panel | ~20% |
| Exome | 40–60% |
| Genome | ~80% |

The same expert said PacBio's reference-genome business is "plummeting," because only the first one to three genomes of a species need long reads.

Outliers expect more. The ex-Illumina staff scientist is "98.5%" confident a large lab such as GeneDx adopts an alternative platform around January 2027. The Natera expert called a combined cancer-profiling-plus-MRD long-read test "the very distant future."

### Oxford Nanopore (ONT)

ONT's nanopores read native DNA and RNA as it passes through a pore. Reads can be any length, methylation is detected directly, and devices range from the $5,000 MinION to the PromethION, which is now more than half of revenue [MS conf, 2026-09-15].

**Results and guidance:**

- **FY2025:** revenue £223.9m, up 24.2% at constant currency. Clinical grew about 60% and Research 15%.
- **March 2026:** ONT dropped its target of more than 30% annual growth and guided FY2026 to 21–25%.
- **H1 2026:** revenue £116.7m, up 12.3%. China fell about 16% and the Middle East 14%. Consumables grew only 2.7% while devices rose 32.6%.
- **August 2026:** core growth guided at 16–20%, or 23–27% including a $20m cross-licence fee from an undisclosed diagnostics company. Gross margin guided at 64%.
- **Targets:** adjusted EBITDA breakeven in 2027 and 2030 organic revenue above $700m.

**Price per genome.** J.P. Morgan's comparison shows ONT as the premium option. ONT argues its "fully loaded" genome includes methylation.

| Platform | Cost per genome |
|---|---|
| ONT, 2 genomes per flow cell (early access) | ~$345 |
| ONT, 4 genomes per flow cell (roadmap) | <$200 |
| Illumina | $200 |
| Roche AXELIOS | $150 |
| Ultima (target) | $80–100 |

The ONT expert put Illumina at about $150 per genome and Nanopore at "at least double."

**Competitive position.** Deutsche Bank found ONT "complementary to short reads in many applications, not a broad substitute." ONT papers reached almost 1,900 in 2025, more than 30% of Illumina's [DB, 2026-09-21].

Expert views of ONT varied:

- Its devices took sequencing "out into the wild," including bedside COVID strain-typing, and NHS validation for whole genomes and MRD is drawing "a lot of positive noise" [Roche UK lead].
- Accuracy tops out near Q30–35, "very, very unlikely" for MRD [ML scientist].
- Support was "incredibly poor" but is improving, partly through ex-Illumina staff [Daisy Lab].
- At the Daisy expert's former facility, Nanopore was "closer to 20% or 30%" of revenue.

ONT also discontinued the PromethION 2 Solo and dropped Flongle, which complicated logistics for the South Carolina core.

**ONT on its rivals:**

- On Illumina's long-read push: "the fourth one, I think. So good luck with that" [Sanghera, Q4 2025 call]. CFO Keher called TruPath "stitching together... imputed. It's not direct."
- On Roche: AXELIOS is "adjacent," "a short read focused platform" [van Parys, Q2 2026 call]. It cannot read native RNA [Barclays, 2026-03-25].

### PacBio

PacBio's HiFi reads are long and highly accurate. Its instruments are the Revio (about $482k average price) and the benchtop Vega ($175,000 at the Georgia core).

**2025:** revenue was about $160.0M, up 3.9%. Hospital and clinical consumables grew 55%.

**2026:** quarters were weak.

- **Q1:** revenue $37.2M, flat year on year.
- **Q2:** revenue $39.0M, down about 2%. APAC fell 45% while EMEA rose 52% on clinical production.
- **Guidance:** cut from $165–180M (February) to $155–165M (August). Gross margin guidance fell from 41–44% to 35–37%, and cash-flow breakeven slipped to 2028.

The new SPRQ-Nx chemistry and multi-use SMRT Cell (up to three runs per chip) cut the US list price of a 20x HiFi genome 30%, to $345. Customers paused consumables orders during the transition. CEO Christian Henry stepped down on 5 August, succeeded by Mark Van Oene.

PacBio's largest deal is with Basecamp Research: about 100,000 metagenomic samples for an AI biology model, alongside Anthropic and Ultima. Barclays estimates $10–20M of revenue, mainly in 2027.

**Analyst ratings:** Barclays downgraded PacBio to Underweight on 6 March 2026, citing long-read competition from AXELIOS and TruPath. Its target is $1.25. UBS rates it Neutral at $1.50.

**Illumina history:** Illumina tried to buy PacBio in 2020, but the deal was blocked. In January 2026 PacBio sold Illumina its high-throughput short-read assets for about $48.1M net. The ONT director gave PacBio about $150 million of revenue ("not long for this world"). The Roche UK lead cited "question marks on the reliability of PacBio." The staff scientist expects PacBio to lead long reads.

### Illumina's TruPath (Constellation) and Roche's middle ground

TruPath is Illumina's synthetic long-read product. It stitches short reads together to recover long-range information and cuts whole-genome hands-on time to about 10 minutes [Q1 2026 call]. Barclays called it the third rebranding of Illumina's long-read push and said it "could freeze part of the long-read market" [Barclays, 2026-03-06]. A Broad expert called it "a direct shot at PacBio and ONT."

Experts' adoption estimates diverged:

- 5–6% of the South Carolina core's volume by end-2026 for structural variants in tumors;
- 1–2% at the genome center ("an expensive, different version of Illumina sequencing");
- "not at all likely" at the Georgia and Arizona cores. Georgia's director said short reads cannot "adequately or efficiently resolve complex areas."

The ONT director said it "probably threatens Oxford's long-read clinical... position a bit." An earlier Illumina product, Illumina Complete Long Reads, "failed drastically" [ex-FAS].

AXELIOS sits between short and long reads. Its reads average 175–600 bases depending on source, with peaks of 1,000–1,500. Experts called this "a nice middle ground" [ONT director] or "an exciting middle ground" that may link variants over distance [Abbott]. ONT says Roche "will really struggle" to add native epigenetics.

## Clinical diagnostics

### The growth engine, and a concentration risk

Clinical sequencing (DNA tests used to diagnose and treat patients) is now Illumina's growth engine.

**Share of the business:**

- Clinical was 52% of revenue when the Kailos expert left in September 2024, up from a historical research-heavy split.
- It is more than 65% of sequencing consumables, up 10 points in two years, which BI says "adds ballast" [BI, 2026-07-31].
- It is more than 40% of company revenue [JPM, 2026-06-10].
- A former Illumina manager said the 65% figure "has always been a very loose statement," since Illumina classifies clinical "very generous[ly]," and most volume is laboratory-developed tests (LDTs, tests a single lab designs and validates itself) [Tegus].

**Growth of clinical consumables outside China:**

- 16% in the second half of 2025;
- 20% in Q4 2025 and Q1 2026;
- 15% in Q2 2026, above 20% in the US and Canada but softer in the Middle East and Latin America.

Guidance moved from "double-digit to mid-teens" to mid-teens. JPM expects low-to-mid-teens annual growth through 2030.

**The main growth areas** are liquid biopsy (cancer tests on blood) and MRD (minimal residual disease) testing, which looks for trace cancer after treatment. Large US labs such as Natera, Tempus, Caris and Foundation drive them [Tegus]. MRD wins over one-time cancer profiling because patients are tested three to four times a year [Kailos].

The Natera expert sized MRD at about $5 billion today and $30 billion by 2030, citing consultant projections of $30–50 billion. Roche projects monitoring growing 32% a year to CHF 5 billion by 2030 and multi-cancer early detection growing 35% a year to CHF 5.3 billion. The Tegus expert was skeptical MRD goes global beyond the US and Japan.

**Concentration.** The risk is that clinical revenue comes from roughly 10–20 large labs: Natera, Guardant, Tempus, Caris, BillionToOne and Exact [ONT director; Kailos]. These labs earn bigger margins than Illumina and hold bargaining power. A rival pitching "cut your cost by half" could have "a really big impact," leaving Illumina "only a supplier." The ONT director noted the pattern has "inverted" since 2008–14, when genome centers drove volume.

### Why clinical customers are sticky

Switching estimates rise with the stakes:

- one to two months of side-by-side tests at a start-up [Abbott];
- $100,000–200,000 to revalidate a clinical test [LifeStrands];
- $2 million just for quality checks at one large company [Brigham];
- four to five years to convert an established lab, and six to ten years for a new lab to reach accreditation [ONT director];
- up to $200 million in worst-case clinical trials to move an FDA-approved test [ML scientist].

Five-to-seven-year MRD trials cannot switch sequencer midstream ("It's a no-no") [Natera]. Adaptive's clonoSEQ still runs on the NextSeq 550, about 10X NovaSeq's per-read cost, after about a decade. Natera, Caris and Guardant run "a factory floor full of Illumina systems." The Natera expert said that in the US "the big four, plus Natera, they're just using Illumina" for MRD, though Natera uses aspects of Element for ctDNA. The ex-Illumina scientist now at Roche: "I don't think anyone is really going to move away from Illumina" in the clinic.

JPM's June upgrade rested on this. All large CLIA-certified labs have moved or are moving to NovaSeq X. Diagnostics executives showed "general intrigue" about Roche but no urgency, and mid-sized clinical labs expect Illumina's share of their work to rise from 50% to 57%. A PacBio lead, describing labs that validated on NovaSeq X, said they are "probably not going to switch for a while."

### Where the clinical defense could crack

**NHS technology transfer.** In technology transfer, a test company trains a hospital lab to run its test locally on the partner's equipment. Manchester runs a Foundation Medicine liquid-biopsy lab on an Illumina instrument; London has the same arrangement with Guardant; Natera was discussed for an NHS MRD lab. About 11 such UK labs exist or are possible. If Natera or Guardant revalidated on a cheaper sequencer, those labs would have to follow. "There is validation ongoing with some of the other platforms," the Roche UK lead said, though success is "up in the air."

**Roche's vertical integration.** Roche's oncology stack includes:

- Foundation Medicine, an AXELIOS early-access site that plans to move its partner sites to AXELIOS and showed better MRD detection at AACR 2026;
- SAGA Diagnostics for MRD, which sequences the tumor on AXELIOS and monitors it with digital PCR;
- a Freenome partnership, with Freenome evaluating AXELIOS;
- PathAI digital pathology.

The Tegus expert warned that tying sequencing to Roche drugs could repeat FoundationOne's experience, when other drugmakers grew wary. Adoption by Foundation "would be a powerful marketing tool" [24 Jul].

**Other cracks:**

- Illumina tells TSO users it won't support Element validation [ex-FAS].
- Illumina is "a little bit behind the ball" in liquid biopsy versus Natera, being "a technology company" without its own lab [LifeStrands].
- Its regulated TSO Comprehensive test is "a manual workflow."
- Experts saw GRAIL and Pillar as missteps.

### Illumina's clinical assets

Illumina's main clinical asset is TSO Comprehensive, the FDA-approved version of TSO 500 covering about 500 genes, versus FoundationOne's roughly 300. A savvy pathologist might favor it, but oncologists favor FoundationOne's brand and evidence [Tegus]. Its US reimbursement "helps expand access," meaning market expansion more than cannibalization.

Illumina also launched a whole-genome, tumor-agnostic MRD research kit, which needs heavy sequencing. The Abbott scientist thinks the approach "makes sense." Element cannot do cancer profiling, which needs 150X depth plus RNA, or tissue-informed MRD, which needs more than 80–120X [Natera].

## China

China has collapsed as an Illumina market. Beijing's "unreliable entity" designation, a government listing that restricts a foreign company, roughly halved China's contribution [BI, 2025-10-31].

| Period | Illumina Greater China revenue | Change |
|---|---|---|
| Q4 2025 | $55M | −33% cc |
| Q1 2026 | $52M | −29% organic |
| Q2 2026 | $56M | −19% organic |
| FY2026 guidance | $210–220M | about a 1-point drag on growth |

Shipments resumed, but growth is "not yet in sight" without removal from the list [Freedom, 2026-02-10]. JPM models China declining by mid-teens a year.

**MGI fills the gap.** Management, via UBS, claims MGI's share of Chinese public tenders rose to about 70% in 2025 as "import substitution" (buyers replacing foreign products with domestic ones) spread. It shipped about 60% of the prior year's import-substitution orders by end-2025.

MGI's numbers are weaker:

- **2025:** revenue fell 7.7% to Rmb2.78bn, with sequencing down 8%. China sequencing revenue fell 11%. Gross margin slid to 52.9%, and the net loss was Rmb222m.
- **Units versus price:** sequencer units rose to more than 1,470 from 1,260, but average prices fell on competition and a shift to cheaper machines.
- **H1 2026:** revenue rose 18.9% to Rmb1.37bn. Clinical customers grew 36.6% and the Americas 126%.
- **Rating:** UBS rates MGI Neutral with a Rmb58 target, while the stock traded around Rmb70–75 in August. The UBS notes never mention Illumina.

**MGI is also exiting direct US exposure:**

- It licensed its CoolMPS chemistry outside APAC and China to Swiss Rockets for $20m upfront plus a $20m milestone and royalties (13 October 2025).
- It agreed to sell its US unit, Complete Genomics, for $50m and licensed StandardMPS in North America for royalties (24 February 2026).
- It bought nanopore and spatial-omics platforms from BGI Tech for Rmb365.7m (1 February 2026). UBS says this makes MGI China's only, and one of two global, suppliers with both short- and long-read capability.

A South Carolina expert recalled, unverified, that MGI products now belong to a Swiss company that is "aggressively offering" them.

**Other China evidence:**

- GeneMind won Chinese approval for an infectious-disease instrument.
- ONT faces 7–8 local nanopore rivals pricing about 30% lower and expects China to keep declining.
- PacBio's largest Chinese accounts delayed orders, though Berry Genomics won NMPA approval for thalassemia testing on PacBio.
- Thermo Fisher's China business (about 7.5% of revenue) returned to low-single-digit growth on commercial biotech, while government science stays weak.
- The ONT director: "China is lost to Western vendors."

## Proteomics

Proteomics is the measurement of proteins. Illumina entered by closing its SomaLogic acquisition in January 2026: $350M upfront plus royalties and milestones, or $363M net cash, with a $25M milestone paid after Q1.

SomaLogic costs about 100 basis points of 2026 margin and $0.18 of EPS. It adds 1.5–2 points of growth and tracked at the high end of expectations in Q2, when microarrays rose 21% [Q1–Q2 2026 calls]. Management says multiomics and the BioInsight data unit will add 1–2 points of growth in 2027. Barclays said this cannot be verified, and Seeking Alpha called it a "major unsolved mystery."

**Experts like the strategy** of more applications per box:

- "absolutely the right strategy" [Tegus];
- "pretty clever, especially SomaLogic" [Kailos].

A NovaSeq X owner can add SomaLogic more easily than Olink. Thermo's Olink purchase "sets up a new battleground" [Tegus] and was "a really direct response" [Kailos].

**But customers have barely responded:**

- The genome center chose Olink first, so SomaScan had "no effect."
- Small cores find it too costly per sample.
- The Georgia director did not know what it does.
- One ex-FAS called the SomaLogic-versus-Olink gap "a mountain and a sea level."

**The science draws doubts.** A former staff scientist said Illumina's offering is "not strong enough," shallow, and like "mixing water and oil." The Kailos expert warned that sequencing-based proteomics is like microarrays, "you don't see what you don't see," and that native protein sequencing could "easily just kill that market in one day." The PacBio lead said clinical proteomics is "both near and far away."

**Rivals:** Thermo pairs Olink with its Orbitrap mass spectrometers, for example in a Singapore population study, rather than with sequencing. Roche cites proteomics collaborations on AXELIOS with Olink, Pixelgen and Alamar. ONT is developing peptide sequencing, with full protein sequencing 3–5 years away.

## Single-cell and spatial biology

Single-cell analysis measures gene activity cell by cell. Spatial biology measures it while preserving location in tissue. 10x Genomics leads both, and Illumina is widely seen as late: "late to the game, definitely" [Roche UK lead]; "just not going to compete with 10x" [ex-Illumina scientist now at Roche]. The former product director said "Illumina has no bargaining or leverage over 10x at all." They sized single-cell at more than $1 billion, "approaching $1.5 billion," and true spatial at under $500 million.

### Illumina's entries

**Single-cell.** Illumina bought Fluent BioSciences (PIPseq), closing in early 2025. In a typical 10x workflow, Illumina captured only about 25% of spend. Fluent needs no instrument and is cheaper per cell, but "really struggled" [24 Jul]. The genome center sees PIPseq as having "some potential competitive advantage against 10x."

**Spatial.** Illumina launched StrataMap, a sequencing-based spatial product, in June 2026, with interest above plan [Q2 2026 call]. It runs on existing sequencers with no new capital spending, but the former product manager expects Illumina's spatial revenue to be "not more than maybe low eight figures."

**Data services.** BioInsight's Billion Cell Atlas has delivered more than 300 million cells to six pharma partners, including AstraZeneca, Merck and Eli Lilly.

The Tegus expert saw Illumina ahead on transcripts per cell and spatial, and able to "close it really, really quickly." A former staff scientist would pick "Not the Illumina one."

### 10x Genomics and the imaging shift

10x reported Q1 2026 revenue of $150.8M, up 9% excluding a one-time patent settlement. Consumables rose 13%, while spatial instruments fell 32% as buyers waited for Atera. 10x guides 2026 revenue to $600–625M.

Single-cell reaction volumes grow double digits while prices fall. Flex and Flex Apex unlock whole-cohort projects, and pricing should stabilize by 2027.

**Why this matters for Illumina.** Single-cell growth pulls sequencing demand, but 10x credits Ultima and Roche for cheaper reads. 10x is also moving to closed imaging systems, which need no sequencer:

- **Xenium** today;
- **Atera**, launched at AACR in April 2026 as whole-transcriptome imaging, with about 40 units expected in late 2026.

10x's CEO said spatial "will increasingly become the default approach." The former product manager said Atera now overlaps Illumina's spatial product, so Illumina is likely "scrambling to adjust their business cases right now down." They are "cautiously pessimistic" on Atera's ~$500,000 boxes, citing "instrument fatigue." The genome center said Atera could "eat away at some of the activities that people use sequencing readouts for," but "it'll take a while." The Brigham specialist said single-cell demand is "being replaced by spatial transcriptomics" that uses fluorescent probes.

**Other rivals:** Singleron is almost 5X cheaper than 10x in single-cell [ex-FAS]. Roche's 10x partnership on AXELIOS copies Illumina's add-applications playbook [Tegus]. Element's AVITI24 adds in-cell sequencing.

**AI-driven data generation is the shared demand case.** 10x cites the Chan Zuckerberg Biohub's $500 million Virtual Biology Initiative. Thermo's CEO says AI-scale experiments "consume many reagents." PacBio's Basecamp deal points the same way.

## Where sources disagree

**Illumina's share and its floor.** Estimates range from a 95% guess to 80%+, 70% and the mid-60s. Forecasts range from a floor near 50% to "at least 30%" more loss by 2030. Customers in JPM's survey expect Illumina's share to rise 1–3 points (academic) or reach 57% (mid-sized clinical). Academic cores and the genome center expect little or no loss over 12 months; the South Carolina core expects losses to Element, Ultima "and most probably MGI."

**How dangerous Roche is.** Views span "die out" and "enabler, not replacer" to "main disruptor" and 10–20% share within three years. Sell-side views split the same way: UBS ("benign"), Barclays ("well capitalized competitor"), and JPM (stickier than feared).

Specific facts conflict:

- **Accuracy:** Q38 (Roche, and one expert's "best case") versus duplex 45–52 (ML scientist) versus Q50 with consensus reads (Roche). It is "maybe not quite as good as Illumina" [Abbott] or higher [PacBio lead].
- **Read length:** 175–250 bases average, 400–600, or up to 1,000–1,500.
- **Instrument cost:** $750,000 versus "less than a NovaSeq X" or a "$2 million machine" [Daisy].
- **Year-one measure:** about 100 placements [JPM] versus 100 orders [Barclays].

One expert and Barclays' July note wrongly attributed AXELIOS to Element.

**Whether Illumina is discounting.** Barclays and BI see price traded for volume. Management calls the data noise, and JPM's survey implies modest price cuts.

**Whether placements are sustainable.** Seeking Alpha and Barclays raised the possibility of pull-forward ahead of AXELIOS. Management called it "a very healthy market." Freedom moved from calling guidance "conservative" (May) to "priced in" (5 August Hold downgrade).

**NovaSeq X price and pricing assumptions.** List price was put at $689,000 (X Plus, UBS), $985K–1.2M (BI), "just above $1 million, like $1.2" and "almost $1 million" (experts). Genome prices quoted range from $100 to $250, and it is unclear whether headline figures include analysis and storage.

**DRAGEN.** DRAGEN is Illumina's variant-calling software. Some call it "a very important aspect of the strategy" and the standard for secondary analysis [Tegus; Daisy]. Others say it is "definitely not a decisive differentiator," and that "most of the people just don't use it" [ML scientist]. The Roche UK lead partly agreed that labs build their own pipelines.

**Long reads.** Most see a stable ~10% niche. One staff scientist is 98.5% sure big clinical labs adopt them. TruPath adoption estimates range from 1–2% to 5–6% to "not at all likely." Its launch timing is disputed: end-2024 at JPM [staff scientist] versus early 2026 [ONT director]. Constellation was still listed as a 1H26 launch on the 4Q25 call.

**Element and Ultima.** Element is ranked second by installed base [ex-FAS] and called the best-placed rival [Abbott]. The PacBio lead says adoption disappointed relative to hype. Ultima's data are "spot on" [ex-FAS] or "questionable" [South Carolina]; its future is "Increase" share [Georgia] or "doomed" [ONT director].

**Proteomics.** Experts call the strategy clever, but customer uptake is near zero and its long-term durability is doubted.

**Stale or unreliable data.** Several experts' Illumina knowledge is three to five years old, and many work for competitors (Roche, PacBio, ONT, SOPHiA). Interviewers supplied several figures, including the 10% long-read share and the 20% and 65% clinical statistics. Other data problems:

- BI's reported 20% fall in Q1 service revenue conflicts with all other sources.
- Firms disagree on the 2025 operating margin (23.1% versus 23.6%).
- JPM's survey dates conflict (May versus 10 June).
- UBS's MGI segment figures appear swapped.
