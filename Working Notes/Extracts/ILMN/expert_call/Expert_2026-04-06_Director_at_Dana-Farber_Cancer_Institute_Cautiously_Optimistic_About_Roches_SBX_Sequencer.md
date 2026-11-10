# Dana-Farber core facility director on Roche's SBX sequencer versus Illumina (customer expert call, interview 6 Apr 2026)

*Source file: `Working Notes/Sources/ILMN/expert_call/Expert_2026-04-06_Director_at_Dana-Farber_Cancer_Institute_Cautiously_Optimistic_About_Roches_SBX_Sequencer.md` · Date: 2026-04-06 · Third-party expert network transcript (published 20 Apr 2026); interview by a buy-side investor; expert is Director, Molecular Biology Core Facilities at Dana-Farber Cancer Institute (unnamed) · expert call*

**Summary.** A long-time Illumina customer who runs a research sequencing core (about 800-1,000 samples a month, mainly on a NovaSeq X Plus) explains how he would evaluate Roche's new SBX nanopore-based sequencer. He is cautiously optimistic: he expects Roche to cost roughly the same as the NovaSeq X to about 20% less in his real-world usage, to cut turnaround from roughly two weeks to about one week, and to offer better accuracy (duplex mode) and longer reads (simplex mode). He would likely add or switch to Roche over 12-18 months once commercial units ship and look good, and he views Element as more relevant for smaller labs and Ultima as a poor fit. He reports his Illumina spend is growing modestly.

# Expert call: Dana-Farber core facility director on Roche SBX vs. Illumina

## Expert background and relationship to Illumina

- The expert is Director of Molecular Biology Core Facilities at Dana-Farber Cancer Institute, a cancer research institute. A "core facility" is a shared lab that runs sequencing for other researchers. The perspective is that of a **customer** (an investor-led, buy-side interview). [Expert: Dana-Farber core director, interview 2026-04-06; published 2026-04-20]
- They have worked in the sequencing core for over 20 years and been director for the last five. The lab has run Illumina sequencers for about 15 years. Experience is current.
- The core supports cancer and basic-disease research for external clients and also has experience in upfront sample treatment, sequencing and informatics.
- Roche exposure (direct experience): several meetings with Roche technical and sales staff, attendance at conference showcases, and a demo where they saw the SBX instrument running real samples in a lab setting. They have not run it in their own lab. They also recalled seeing a Roche presenter a couple of months before the call.
- The lab is **not** CLIA/CAP-certified (the regulatory certifications needed for clinical diagnostics) and does no clinical diagnostics. Some work is translational (patient-derived samples) but all is for research.

## The expert's lab and Illumina fleet

- Illumina instruments: five MiSeqs (small benchtop sequencers), a MiniSeq and a NextSeq (both rarely used), and a NovaSeq X Plus, now the primary platform. Almost all samples run on the NovaSeq X Plus.
- Volume: roughly 800-1,000 samples a month, covering single-cell sequencing, bulk RNA-seq, target capture, exomes, genomes, and functional assays such as ChIP-seq, CUT&RUN and ATAC-seq.
- The NovaSeq X Plus is two years old. The expert plans equipment on a three-to-five-year horizon of use.
- Utilization: the lab pools and multiplexes several projects per run to hit the best price per data point. It runs mostly 10B flow cells (smaller, to get faster turnaround) rather than 25B ones, running as soon as enough samples accumulate. The expert estimates actual volume is about half of the machine's full capacity, though this depends on how it is calculated. The cadence is a couple of runs per week.

## Are there credible alternatives to Illumina? ("yes and no")

The expert's view is that it depends on lab size and needs. [Expert opinion]

- **Element (AVITI) and Singular:** short-read sequencers like Illumina. Their appeal is competitive per-sample or per-read cost on lower-throughput instruments, so smaller labs can get a cheap price without filling a NovaSeq. For a lab that can fill a NovaSeq there is little incentive, since they "don't really do anything very different than Illumina." Element has some differences: higher accuracy than Illumina and the ability to handle somewhat larger library fragments, though not as large as Roche. The expert would be excited to buy a couple of Element AVITIs if running a smaller lab, starting a new core, or running a departmental core.
- **Ultima:** the opposite extreme, very high throughput. The expert's lab lacks the sample volume to fill it, and the price tag and physical space are also issues. The expert has never been excited by it, calling the method "cool" but not a fit for a lab with diverse applications. It suits high-volume labs doing a handful of sequencing-intensive applications such as whole genomes or single cell.
- **Roche SBX:** the expert is "maybe a little bit excited" because the throughput sits in their range, pricing looks attractive so far, and the data differ from Illumina's. They are more excited about Roche than they were about Element, for the same reasons plus flexibility and throughput fit.

## How SBX differs technically (expert's understanding)

- SBX (Roche's sequencing technology) converts DNA into "expandomers," enlarged molecules that are read through a nanopore (a tiny hole that reads DNA as it passes). Illumina uses SBS (sequencing by synthesis).
- The expert called the expandomer a "pretty cool solution to a nanopore sequencing problem." Their explanation: in conventional nanopore sequencing (Oxford Nanopore), DNA passes through the pore so fast (about 400 nucleotides per second) and four or five native nucleotides are in the pore at once, so the software must deconvolute a mixed signal, which was hard. Expandomers put only one nucleotide in the pore at a time, spread out the signal and boost the signal-to-noise ratio.
- Open risk: how efficiently and accurately expandomers are incorporated. Any bias or error there is unknown until systems are in the wild. For counting applications this matters less. From what Roche has presented "it looks good." The expert does not want to be among the very first users but would want to be on the early end.

### Error rates (Roche's published specs as recalled by the expert)

- Simplex mode (single pass, longer reads): about Q20, one error in 100. Illumina is Q30, one in 1,000. Duplex mode: about Q40, one in 10,000. (Q scores are a log measure of base-call accuracy.)
- Expert's view: Q20 is acceptable for counting applications, and Q40 is better than Illumina and acceptable for variant calling, "if those numbers are real and there's not issues with the expandomer conversion." They think duplex is "about an order of magnitude more sensitive than Illumina."

## Applications that could benefit

- **Duplex (accuracy):** liquid biopsy using cell-free DNA (DNA fragments in blood), where labs want the lowest allele frequencies (rarest variants) detectable. The expert's lab is working on this now.
- **Simplex (longer reads):** RNA-seq for transcript-level expression and isoform quantification; fragmentomics (analysing the size distribution of cell-free DNA, which has clinical implications).
- **Counting applications:** RNA-seq is a counting application "99% of the time"; accuracy matters less than cost per read, so simplex's lower Q scores are tolerable. ChIP-seq and CUT&RUN are the other big counting applications and the lab does a fair amount of them. Calling variants from RNA is possible but challenging.
- Expert's takeaway: duplex is higher quality and simplex gives longer reads, so "maybe we can do some new things or maybe we can do some old things better," though gains depend on designing experiments to exploit those features.

## Workflow and operational impact

- **Library prep** (preparing DNA/RNA for sequencing) stays essentially the same. SBX adds an expandomer incorporation step of about four hours (roughly half a day), but the expert says that time is recouped by faster sequencing.
- **Cadence:** the NovaSeq is run as batches (accumulating enough inventory to fill a flow cell). The Roche would be fed continuously, daily. A challenge is triaging which runs are simplex versus duplex. The expert says that until it is in a lab like theirs, the real workload is hard to judge.
- **Turnaround:** the expert imagined moving the whole operation from Illumina to Roche and concluded turnaround would be consistently about one week for a reasonably sized project, versus typically one to two weeks now and sometimes three weeks for involved library preps (they also said "two weeks" in most cases). Very large projects would take longer to prep.
- **Speed anecdote:** the expert recalled a presenter citing a Guinness World Record for fastest sample collection to whole genome, just under four hours, "which is wild. You could never do that with an Illumina sequencer." They say clinical folks are excited by this.
- **Reagents and automation:** the lab uses two Biomek i7 automated liquid handlers for library prep, which the expert believes Roche explicitly supports with automated methods. They stock few reagents (mostly just-in-time ordering, apart from adapters). The lab already uses Roche KAPA reagents for RNA-seq prep, and Roche already makes Illumina-compatible sequencing reagents, so switching would mean a different part number. The interviewer suggested Roche could incentivize adoption by discounting library-prep reagents; the expert agreed it would help and said they would raise it with their sales rep.
- **Transition:** expected to take about a year to move everything over. Some legacy projects could not switch platforms, and some applications will not be developed or appropriate for SBX for a while.

## Data output and informatics

- The instrument ships with its own large computer (a big black box under the bench); the expert believes it is a substantial share of the instrument's cost [speculation: "pretty sure"].
- It outputs standard FASTQ files (the standard raw sequence file format), usable in any open-source pipeline, and also has built-in alignment and variant calling.
- A feature the expert has asked Roche about (not yet supported, Roche is thinking about it): real-time alignment and read counting so a run can "sequence until" a target such as 50 million reads per sample, then stop.
- Concern: SBX data differ from Illumina's. Illumina reads are typically paired-end (e.g., about 150 bases from each end of a fragment) with usable fragment sizes of roughly 200-800 bases ("probably being a little generous"). Roche simplex reads go up to about 1,500, maybe 2,000 bases. Roche is still shorter-read than Oxford Nanopore and PacBio. Existing tools optimized for Illumina may not handle simplex reads efficiently or may leave useful information unused. It is unclear how many reads are lost in duplex mode if not fully duplex, or what filtering applies. The expert said there is even less information about this analysis side. Combining simplex and duplex reads in analysis is an interesting possibility.
- The expert expects a while before open-source tools are optimized for SBX, but thinks Roche will support it well in the interim. The back-end analysis ecosystem and reliance on Roche compute are called "one of the bigger unknowns."

## Pricing and economics

- **Roche cost per read:** Roche says full-capacity whole-genome runs cost about $0.06 per million reads ("something crazy," expert's recollection). The expert is "pretty sure" their real-world mix would not reach that. Their estimate [expert speculation]: close to Illumina's cost, maybe 10% lower; later "somewhere around NovaSeq X to maybe 20% less," because their work has variable output needs.
- **Unclear pricing mechanics:** price depends on throughput and on how many uses the nanopore chip gives (Roche suggests about 20 uses). Unknowns: whether it is always 20 or sometimes 10 or 30, and the chip's cost (Roche has not been clear, which the interviewer suggested was by design). Chip life is like Oxford Nanopore's flow cell issue of pores dying or clogging. The instrument tells users when a chip is done after a percentage of pores drop out. The expert says they will not know until shipping begins.
- **Decision logic:** if comparable or cheaper, plus better data for specific uses, that is "enough for me to seriously consider either adding or switching."
- **Skepticism of cheap-genome marketing:** the expert dislikes "the marketing race to the cheapest genome." Reagents for a genome are not the most expensive part; library prep, QC and labor exceed $100. Data storage is a real cost for very high-throughput sequencers, "the X is no exception." Other costs: capital (a "$1-million instrument"), and a service contract, which the expert believes is list priced in the low six figures per year for a NovaSeq X. These make "$100 genomes" meaningless in their view.
- **Floor on prices:** "There's only so low we can go." For a given project on the NovaSeq 6000 and especially the X, probably two-thirds of cost is not sequencing but other items, mostly reagents and labor. The expert sees this starting already.

## Demand and spending trends

- Illumina spend at the lab is "modestly increasing." A year earlier "everyone was freaked out" (a reference to NIH funding worries) and there was a small drop-off that has come back; projects at the institute seem well funded and the lab is growing year over year. The expert flagged this is a first-person view, not the whole market.
- Elasticity: "every time sequencing costs go down, people do more sequencing," spending about the same as before for more data.
- Sequencing services is a competitive field; commercial providers compete mostly on price, while the core adds value through collaboration and development projects.

## Switch scenario and timing

- The Roche instrument would likely replace the NovaSeq X rather than the smaller Illumina machines.
- The expert would wait for commercial shipments (SBX is already at the Broad and some genome centers, but not commercially shipping as of the call). If it looks good with no issues, they would look to transition or add Roche, with a switch or dual-platform run taking 12-18 months.
- Illumina has said it plans to augment NovaSeq X capabilities rather than require a new million-dollar purchase for new features; the expert said "I'll believe it when I see it." Such an upgrade-path change could complicate the decision.
- Capacity: moving everything to SBX would fill it to about 80-90% capacity. The expert calculated that last year's volume would run at about 85% capacity, not counting single-cell work, so they might need two instruments. Ramp: three to six months before comfort with the workflow, perhaps 50% utilization within six months.
- Capacity comparison: the interviewer cited a Roche statistic that annual output of one SBX running full time equals a NovaSeq X running 25B flow cells around the clock; the expert said they believe this but only if running solely whole genomes. In their configuration the box does not have the annual capacity of a NovaSeq X Plus.

## Memorable quotes

- "I think the answer is yes and no." (on credible Illumina alternatives)
- "The Q20 is acceptable for counting and Q40 is better than Illumina."
- "I really dislike the marketing race to the cheapest genome."
- "Probably two thirds of the cost is not the sequencing, it's the other stuff."
- "Every time sequencing costs go down, people do more sequencing."
- On Illumina's upgrade pledge: "I'll believe it when I see it."

## Key uncertainties the expert flagged

- Real-world cost per read and chip reuse count (about 20 uses) are unproven.
- Expandomer incorporation bias or error is unproven outside Roche's data.
- Analysis tools and duplex read filtering are not mature.
- No commercial shipments yet as of April 2026.
