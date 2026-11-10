# Cedars-Sinai molecular pathology director on genome-backbone testing, NovaSeq X economics and Roche's Axelios (SBX) adoption hurdles

*Source file: `Working Notes/Sources/ILMN/expert_call/Expert_2026-04-13_Director_of_Molecular_Pathology_at_Cedars-Sinai_Sees_Genome-Backbone_Testing_as_Future_of.md` · Date: 2026-04-13 · Expert-network transcript (interview 13 Apr 2026, published 27 Apr 2026); expert is a customer, Director of Molecular Pathology at Cedars-Sinai Medical Center; interviewer is an investor-led (buy-side) analyst, unnamed · expert call*

**Summary.** A clinical lab director who runs two NovaSeq X Plus systems explains how falling sequencing cost lets labs run one whole genome on every patient and "slice" out panels in software, and says he expects nearly every NGS assay to follow this "genome backbone" model within about 10 years. He is skeptical that Roche's new Axelios sequencer will win clinical labs already invested in Illumina, arguing Roche priced at $150 per genome when it needed to be $50-$100, and that validation costs make switching unattractive. He says his Illumina spend is rising because cheaper NovaSeq X sequencing let his lab launch new assays and volume that did not exist before.

## Expert background and relationship to Illumina

**Perspective:** The expert is a customer, interviewed for an investor-led (buy-side) client. The call took place on 13 April 2026 and was published 27 April 2026 [Expert: Director of Molecular Pathology, Cedars-Sinai, Apr 2026].

**Role and seniority:** The expert is the Director of the Molecular Pathology laboratory at Cedars-Sinai Medical Center. They are an MD who completed medical school, residency (APCP, anatomic and clinical pathology) and a molecular fellowship. They are responsible for long-term strategic planning of assay development and validation, operational troubleshooting, and support and management of clinical sign-out (the physician review and reporting of results). They oversee 2 fellows, 2 PhD-level lab genetics staff and 2 additional molecular genetic pathologists.

**Basis of knowledge:**
- Direct experience: daily use of Illumina and Thermo Fisher instruments, including internal use of the NovaSeq X Plus (Illumina's current high-throughput sequencer).
- Second-hand: the expert has had multiple conversations with Roche about its Axelios system and saw it showcased at the Association for Molecular Pathology (AMP) annual meeting in November 2025. They stress they have "zero material knowledge" of Roche's chemistry beyond what Roche told them, and that their cost views on Roche are inference rather than data.
- Disclosure: the expert consults for Natera, a competitor in liquid biopsy.
- Stated bias: "Obviously, I have a bias that I want things cheaper."

## The expert's lab and sequencer fleet

The lab was historically oncology-focused. In January 2026 it launched whole genome sequencing (reading a person's entire DNA, as opposed to selected regions) for constitutional disorders (inherited conditions), so it now has a broad inherited-disease service as well.

**Fleet (all of it, per the expert):**
- Illumina: one MiSeq, one MiSeq i100, one NextSeq 550, two NovaSeq X Plus, and one NovaSeq 6000 (the older model, being retired but still present). The lab has "the full fleet except for NextSeq 2000."
- Thermo Fisher: three Ion S5 Prime and three GeneXus systems.
- Planned: an Oxford Nanopore system for long-read confirmation work (long reads sequence much longer DNA strands than Illumina's short reads).

**Assays and volumes:**

| Assay | Platform | Volume |
|---|---|---|
| 500-gene DNA/RNA solid tumor cancer panel | Thermo Fisher | about 2,500 per year |
| 300-gene DNA/RNA pan-heme (blood cancer) panel, custom Archer kit | NovaSeq | almost 2,000 per year |
| Rapid heme panel for leukemia diagnosis | GeneXus | about 500-600 per year, maybe 700-800 |
| MPN (myeloproliferative neoplasm) sub-panels | GeneXus | not given |
| Archer solid tumor fusion panel | GeneXus | very low volume, about one run a week |
| Single-gene CFTR screening assay (cystic fibrosis) | MiSeq | not given |
| Whole genome sequencing with paneled-out analyses | NovaSeq X | about one run per week, about 50 samples (roughly 10 genomes and 10 panels a week depending on how many are trios, i.e. child plus both parents) |

Planned panels sliced from the genome: cardio (already running), hereditary hematologic malignancy, hereditary solid tumor, and neuro.

## The "genome backbone" model

**What it is.** The expert explains "paneling out" as a slice: every patient gets a whole genome, but the lab analyzes only the region of interest on the computer. Terms used are "exome slice" and "genome slice." Previously a panel was made by enriching chosen regions, either with PCR amplicons or with hybrid capture (targeted probes), and then sequencing only that enriched library. Now the lab sequences the whole genome and restricts analysis in the "dry lab" (bioinformatics).

**Why it works now.** Sequencing cost has fallen enough that the lab can "over sequence the hell out of everything," while library preparation is cheap and uniform because it is always just a genome with no probes. The expert credits the NovaSeq X with making this possible: "Getting the cost down near to where they are, we just run it on everything. We have no issue with that extra sequencing cost." Genomes were previously too expensive to do this; now it is cheaper than building a separate library per panel [Expert, Apr 2026].

**Advantages the expert lists:**
- Lower validation, training and regulatory cost, because one wet-lab assay replaces many (no separate validations, no training techs on multiple assays, less compliance burden).
- Panels can be changed instantly. Example: if a major journal paper shows a gene matters for cardiomyopathy, a bioinformatician can add it with a click. The expert's example panel has 150 genes.
- Expanded analysis is possible if the panel finds nothing: the lab can open the whole genome to look for other causes, and sees copy number changes and unexpected findings across the genome.
- A broader test menu for low-volume panels. For example 5 cardiomyopathy, 3 neuro and 17 cancer panel orders a week would not justify separate assays, but a single genome assay supports panels ordered only once or twice a week, which also serves populations that would otherwise have to send samples out.
- Batching: all orders (cardio, heme and others) run together because the wet-lab process is identical.

**Why somatic cancer testing is different.**
- Depth of coverage means how many times, on average, a position is read. The lab's genomes are 45X (each position covered about 45 times on average).
- Constitutional variants are essentially zero, 50% (heterozygous) or 100% (homozygous), apart from mosaicism. At 40X a half-present variant has about 20 supporting reads; at a weaker 30X region about 15, which is enough.
- Somatic (tumor) variants are generally under 30% and often 1-5% of reads in tissue. Circulating tumor DNA (ctDNA, tumor DNA in blood) is about a log (10x) lower, around 0.1%. With 1,000 reads, a 5% variant gives 50 reads and a 1% variant gives 10 reads. Sequencing has an inherent error rate, so high depth is needed for confident calls.
- Cost impact: the expert says Illumina markets a "$200 genome" but the real figure is probably around $250 for 45X after other costs. A somatic panel needs about 1,000X, which is 20-30 times more expensive, so a genome at that depth would cost about $5,000 or even $7,500, which is "non-sustainable in the current reimbursement area."
- Threshold for change: the expert says tissue-based testing needs another log of cost decline, "Instead of a $200 or $250 genome, I need a $20 genome." At a $20 constitutional genome, a somatic genome would be about $600, which the lab could absorb in a panel that reimburses $3,600, especially with minimal library costs.
- Exceptions: limited cases such as new hematologic diagnosis, which use around 100X genomes. "In general, we're not there yet from a cost perspective." This is why the lab keeps somatic panels on Thermo Fisher and Archer-based workflows.

**10-year view [Expert, opinion].** The expert expects "every single NGS assay to be a genome backbone assay" in 10 years, covering diagnostic, prognostic and predictive tests. The exception is MRD (minimal residual disease) assays, which are becoming more sensitive: at 10^-5 or 10^-6 sensitivity they would need 100,000X-500,000X coverage, which is not feasible this way.

**What gets us there.** No new sequencing paradigm is needed. Costs have fallen "multiple logs in the last 20 years" and "we're still on the asymptotic portion of the slope," not near leveling off [Expert, Apr 2026].

## Roche Axelios: pricing view

The client noted that falling costs invite new competition and that Roche is a key competitor, saying Roche did not price appropriately for its position.

**The expert's advice to Roche (direct experience).** At AMP in November 2025 the expert sat at Roche's booth with a senior U.S. executive (described as a U.S. president-level person, not Swiss, which matters because a Swiss executive could "call the shots"). The expert told them:
- Not to say $150 a genome, because labs heavily invested in Illumina would ignore a "mildly incremental change."
- Even $100 would draw a shrug because Chinese "knockoff clones" and other options can reach $100.
- To cause a splash, come in at $75 or $50, which would produce "massive adoption" and "push Illumina lower too."
- Roche "did exactly what I said not to do and they came in at $150. The juice is not worth the squeeze at this point."
- "The worst thing you can do is say $150."

**Could Roche have gone lower?** The expert says Roche could "for sure" have come in at $100 and probably lower, and speculates Roche's "bean counters" worried about their revenue curve. They add that Illumina could also reach $100 because reagents are "the printer ink thing" with "huge percentage profit."

**Cost of goods (speculation, stated as such).**
- The expert says Illumina does not come "anywhere near" $20,000-$25,000 to make one new 100B (10B/25B-class "100B") flow cell.
- Evidence offered: the largest NovaSeq flow cell has 8 lanes; a smaller product uses the same flow cell but gives access to only 2 lanes. The price difference is about $25,000 for the 8-lane version versus about $4,000 for the 2-lane version. The expert argues the flow cell cannot cost more than about $500, so "if you told me that the profit margins on those kits are 10,000%, I would not be surprised."
- On Roche: "I have no idea," but chemical costs are "logs cheaper than the cost of the kit." Roche's chip is "not $5, but it's not $5,000." Roche's reagents and consumables appear "decently significantly" cheaper than Illumina's, mainly because the chip is reusable and mostly involves seating nanopores, though it has built-in sensors. Illumina's flow cells are also probably not expensive given volumes built.

## Roche Axelios: technology

**How other platforms work (expert's explanation).**
- Thermo Fisher: short DNA fragments attach into wells with a pH sensor; each added base releases a proton that is sensed (sequencing by synthesis).
- Illumina: sequencing by synthesis using fluorescence, with a camera taking millions of images across the flow cell "lawn."
- Both read short fragments in parallel by adding bases.

**Conventional nanopore.** DNA passes through a pore in a membrane; each base (A, C, G, T, or methylated C) produces a different voltage, so the strand is read live with no synthesis or PCR errors, and methylation can be detected. Strands can be of any length. The problem is noise: base signals are very close (the expert's illustration: 1.1 millivolts vs 1.17 millivolts). Fidelity on single-letter changes may be about 95% rather than 99.999%.
- Good for: RNA fusion detection (only need to find the breakpoint) and methylation (only need a ballpark percentage, such as 50% vs 52%).
- Not good for: exact sequence calls. Example: an EGFR L858R lung cancer variant called wrongly 5% of the time would mean patients wrongly denied or given targeted therapy.

**What Roche did.** Roche bought a company with the technology rather than inventing it, and built in Xpandomers. The expert recommends watching Roche's video. As the expert and client describe it:
- Xpandomers expand each base "like 20 fold" with signal, so the signal lasts longer in the pore and is easier to distinguish. The expert says specificity goes from about 90-95% to 99.9999%, "what you need for large-scale sequencing."
- Elegant and not complicated, "not a space shuttle."
- It needs a special, highly engineered DNA polymerase that customers must buy from Roche, which the expert sees as good for Roche because it creates lock-in beyond the patent.
- Performance data: "there's actually not a huge amount of data." A few studies with the Broad, relayed by reps, are inherently biased. Roche's released information says the polymerase step does not introduce high error. Independent evidence will need a large user base.

**Turnaround claims.** The expert says Roche quotes timings starting from an already-prepared library, which "is cheating," so real time is a little longer. It is faster than NovaSeq, "but it's not like oh my God faster," saving perhaps a day. This might matter for rapid genomes but not for most use cases; the expert's tests have two- to three-week turnaround times.

## Roche Axelios: launch timing and clinical adoption

- Roche normally does not do LDTs (lab-developed tests) or RUO (research-use-only) products; it always has an FDA-cleared assay and platform plan. The expert's impression is Roche changed its playbook and released Axelios "on the earlier end of where a Roche product would get released" because breaking into the space is getting harder and it needs unbiased user experience. Roche products are usually like "a Swiss watch," but the expert "can't promise" that for this one because of the earlier release.
- Status: the client noted AGBT excitement a couple of months earlier and commercial availability supposedly not until Q3 or Q4. The expert says it is in the hands of key accounts (told by a Roche rep). A next recruiting round is "not quite pre-launch but not beta," then a real pre-launch for early launch customers, "now or very soon."
- Clinical labs with NovaSeq X: "I cannot imagine a laboratory with a NovaSeq X that would get rid of it to get this machine currently." Validation and regulatory work is huge, and Roche needs to make labs say "Whoa" to overcome the "activation energy."
- Expert's advice to Roche: target core labs, research labs and clinical-adjacent labs first, build a body of public experience, then clinical labs will feel confident. Research and core labs may "play with it for a few years." Adoption could grow if large centers (the Broad, Baylor) bring it in, clinical tools get built, and an ecosystem forms. The decision point would be for someone with a NovaSeq 6000 choosing between the X and Roche. For existing NovaSeq X owners, "minimal reason" to revamp workflows over about $50 per sample in cheaper sequencing cost.
- Client pushback: a smaller university lab told the client it has to batch samples for one to two weeks to fill a NovaSeq X, whereas Roche could run every two days. The expert replied that lab has a research NovaSeq X but not a clinical one; labs without a clinical NovaSeq X are the real target market of Roche's price structure. The NovaSeq X Plus has been out almost two years and "a lot of people have switched."

## Clinical validation and regulation

- Validation of an NGS assay for an academic lab (which has its own samples) is, by the expert's figure, in the range of $200,000-$500,000. Private labs that must source samples can spend millions. It takes months to over a year.
- Required for reporting on patients in the chart under CLIA (the U.S. lab quality regulation). For Medicare reimbursement in a "multi-X state" like the expert's, the validation must be submitted for technical assessment and meet a quality standard "significantly more stringent" than CLIA, though less than FDA or New York State. The expert thinks CLIA "undersells what you should do."
- The lab's genome validation used 120 genomes and included reproducibility and limit-of-detection studies, not just accuracy. Flow cells alone cost "six figures," reduced somewhat by Illumina discounts.

## Competitive landscape for the lab's tests

- No ctDNA assay currently. Guardant and Natera are mainly liquid biopsy players (including MRD monitoring).
- The lab's oncology tests compete with Tempus, Caris and Foundation (Foundation Medicine). On the constitutional side, competitors are Ambry, "the former husk of Invitae at Labcorp," and GeneDx.
- Sequencing is "in some ways a commodity"; interpretation and reporting expertise "is nowhere near that." Without access to raw data, "you don't know what you don't know." The expert dismisses AI claims: "AI, hooray AI is bullshit," saying manual interpretation has great value but "nobody wants to pay for that," and the industry standard is automated pipelines never reviewed. Academic centers allocate more resources to review.
- The expert respects Tempus, Caris, Foundation, Ambry and Invitae as run by good laboratorians; at hundreds of thousands of samples, rare errors occur statistically (a one-in-10,000 problem across 100,000 samples happens about 10 times). Where quality drops is at interpretation and local follow-up when things go wrong. The local value pitch is expertise and access, with "democratization" of testing as local capacity grows, though it needs volume and critical mass.
- Analogy: Quest and Labcorp have grown bigger in chemistry despite the expert's view that sending CBCs out is worse care; they win on being cheaper. "Usually you get what you pay for."

**MRD and ctDNA.**
- Cheaper sequencing could in theory enable a lab's own Guardant or Natera equivalent, but the expert says MRD is "a tricky beast," not of interest locally, and hard to assess outside clinical trials because each assay has different characteristics.
- Local tissue gives a lab an advantage (immediate access to blocks next door), while blood goes straight from the clinic to reference labs, so there is no local advantage. The lab lacks mobile phlebotomy.
- Possible future: a ctDNA predictive assay like Guardant360, Tempus xF or Foundation Blood, not an MRD assay. The lab has been out of space for five years and prioritizes constitutional work. Currently the lab partners with Tempus and sends all ctDNA to it.
- Reference labs' advantages are scale, resources, and salespeople; tissue access is a "huge" local advantage.

## Illumina spend and NovaSeq X migration

- The client noted Illumina has reported some consumables weakness attributed to clinical customers migrating to the X. The expert says their assays are only feasible on the X: on the NovaSeq 6000, sequencing would cost about double ("It's like halved at the sequencing cost" on the X).
- Spend with Illumina is up, because the lab launched new assays and increased volume: "everybody wins... by making sequencing cheaper, we were able to launch more assays, get more volume, and they make more money." The expert cannot quantify the increase but says it must be up because of the genome launch.
- Those assays did not exist the prior year: "we only launched these assays because we had access to the cheaper platform now."

## Key caveats

- The expert is a single customer lab; cost-of-goods and Roche-economics comments are speculation, not data.
- Interview facts on Roche status (key accounts, pre-launch timing) are second-hand from a Roche rep as of April 2026 and may be stale.
- Dollar figures such as the $250 real cost of a 45X genome and flow cell price points are the expert's estimates or recollections.
