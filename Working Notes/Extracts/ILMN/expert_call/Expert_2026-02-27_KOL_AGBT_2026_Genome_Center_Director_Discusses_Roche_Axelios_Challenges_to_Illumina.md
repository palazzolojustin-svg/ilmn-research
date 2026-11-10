# AGBT 2026 expert call: UMN Genomics Center director on Roche Axelios vs. Illumina, Ultima, and Element

*Source file: `Working Notes/Sources/ILMN/expert_call/Expert_2026-02-27_KOL_AGBT_2026_Genome_Center_Director_Discusses_Roche_Axelios_Challenges_to_Illumina.md` · Date: 2026-02-27 · Guidepoint expert call; expert Kenneth Beckman (Director, University of Minnesota Genomics Center); moderator Andrew Carmen · expert call*

**Summary.** A university core-lab director who attended AGBT 2026 (the genomics industry conference) explains why Roche's new Axelios sequencer is generating excitement, how its announced pricing ($750,000 instrument, about $150 per 30x genome) compares with Illumina, and why he thinks Roche is best positioned to dominate clinical sequencing. He views Illumina's response (35B flow cell, 5-base and mapped-read modes, no new instrument needed) as sensible and attractive to existing owners. He also discusses Ultima, Element VITARI, core-lab outsourcing, and the conservatism of core directors.

# AGBT 2026 expert call: Roche Axelios challenges to Illumina

## Expert background and context

- The call was run by Guidepoint on 2026-02-27, about 31 minutes long, with moderator Andrew Carmen (AC). The expert is Dr. Kenneth Beckman (KB), Director of the Genomics Center at the University of Minnesota (UMN). Guidepoint labels the viewpoint "Academic KOL - Physician Scientist" (KOL = key opinion leader).
- Primary companies tagged: Roche (ROG:SW) and Illumina (ILMN). Associated: PacBio, Ultima Genomics, Element Biosciences, Oxford Nanopore, Thermo Fisher, and a Chinese-listed name (300676:CH).
- Relationship to Illumina: he is a customer and competitor-adjacent user. His core lab owns Illumina instruments, an Ultima system, and about five Element sequencers. UMN scientists now use Element sequencers instead of Illumina because they trust the core to make that choice. His core has already outsourced some Illumina work to another core facility and to a company.
- He says this was "once again" a session with Guidepoint, so he has spoken before. His experience is recent: he attended AGBT 2026 (the Advances in Genome Biology and Technology conference) and describes the Roche session as "the most packed of all the sessions that I went to."
- He says he is unusually risk tolerant ("I'm a bit of a freak... I almost probably seek out risk") compared with his peers, and that he is close to the end of his career. He says he is "talking a little bit out of my area of expertise" when discussing MRD (minimal residual disease) testing strategy. The core-lab views are direct experience; the Roche clinical strategy and CMOS-chip-lock views are his speculation or reading between the lines.
- The call opened with Guidepoint compliance language asking the expert to avoid stock commentary and material nonpublic information.

## Roche Axelios: first impressions

- KB calls Axelios "fascinating" because, like Ultima a couple of years ago, it is "the shiny, new object," and "genomics loves shiny, new objects." He says there is substance behind the buzz because the technology is "a complete departure" from the other flow cell-based platforms.
- Output behaves a bit like Oxford Nanopore: it depends not on flow cell size but on how long you run it.
- Speed: Roche set a Guinness World Record for sequencing speed, and data can come off the instrument extremely quickly.
- Read mix: instead of "25 billion reads that are identical in terms of their length and distribution," Axelios gives a population of simplex reads and duplex reads (explained below), and reads can be much longer or shorter. He finds this "mind-bending."
- Improvement potential: new platforms typically improve most in their first few years, and since specs are "already pretty impressive out of the box," people are enticed.
- Rollout caveat: unlike scrappy start-ups (Element, Ultima) that must launch as soon as the product "doesn't light on fire all the time," Roche is "very methodical or, to say, uncharitably slow." He expects the launch product to be very polished, so it may improve less afterward. He is a little disappointed because Roche, unlike Element or Ultima in his experience, does not involve customers in R&D or its thought process; users get a fixed-way workflow.
- The platform uses Xpandomer synthesis (Roche's chemistry, in which synthesized molecules are read out by the chip). In a "fast mode" Roche runs synthesis faster and ends up with shorter Xpandomers. KB says most people will not use it, possibly some NICU (neonatal intensive care) cases, and "there are very few people who really need their data in 24, 48 hours."

## Early tester evidence

- The early tester is Dr. Keppa from the Hartwig (as transcribed). KB says this person is "not co-inventing... He's validating," assessing Axelios against Illumina in a structured clinical whole human genome workflow.
- The tester used five pillars of evaluation. KB recalls usability, turnaround time, and accuracy (he forgot the fifth); price was last. On all non-price metrics Axelios and Illumina were "basically equivalent, some better, some worse."
- At the talk, the tester flashed "get your cameras ready" followed by two question marks instead of a price. Roche announced pricing afterward. KB says Axelios is "equivalent to Illumina pretty much on" price.

## Pricing and economics

| Item | Figure (as stated by KB) | Context |
|---|---|---|
| Axelios instrument launch price | $750,000 | KB calls it "pretty nice" because seven figures is a psychological and capital-raising barrier; he wonders if Roche is losing money on it given "a lot of compute in that analysis box" |
| Cost per 30x human genome | about $150 (150 bp reads) | Roughly equivalent to NovaSeq X pricing per KB |
| Output | 40 billion reads | Compared with the 25 billion reads of a NovaSeq X 25B flow cell |
| Quoted per-base price | "$0.06 per base pair" (as transcribed; likely per-million-read style unit) | Assumes all 20 chip uses are consumed and each run uses 40 billion reads (800 billion reads total); at only 10 billion reads per run it would be "$0.24 a base pair" |

- KB was "maybe a little" disappointed at $150 but "not surprised." He says it would have been "stupid" for Roche to drive prices to the bottom because it has unique turnaround time and is aiming at the clinical market. Roche "needs a good margin to support the BMS of a company that it is" (as transcribed).
- He thinks Roche was "very clever" to split simplex versus duplex as "fast and good versus fast and cheap."
- He was "relieved" Axelios was not as cheap as Ultima, since otherwise he would face a conflict with his Ultima. Ultima gives "extremely low price for whole genome sequencing that the Roche won't be able to touch for a while."

### CMOS chip reuse (speculation)

- Axelios uses a reusable CMOS chip (the semiconductor sensor). Roche did not reveal everything about how it will price reuse. KB, reading between the lines, thinks there will be a fixed number of uses, perhaps 20, after which the chip is locked.
- He understood pricing assumed 20 reuses. Real-world per-run cost will be higher when runs need fewer than 40 billion reads, which he says is typical ("you don't usually need them all at once"). He says pricing for smaller runs "will all actually come out in the wash in the next couple of months."
- Chip degradation: he is not concerned. Roche showed data in its presentation that run 20 equals run 1. He says the chip is inorganic (plastic, metal, capacitors) and could probably be reused almost indefinitely, which is why Roche would need to lock it after a set number of uses.

## Simplex versus duplex modes

- Duplex mode is for cases where the exact sequence matters: de novo sequencing, resequencing individuals, mapping mutations. This is what the field considers "normal" sequencing, originating with the Human Genome Project.
- Simplex mode is for counting applications, where one only needs a read accurate enough to map to a genome and tally how often a sequence appears (single cell, spatial, ATAC-seq, and others). Simplex reads give about Q20 (Q-score = accuracy; Q20 is roughly one error in 100). Duplex reads sequence the same DNA twice to reach about Q38, as Roche claims.
- Library prep differs: there are two different library preps, one for each mode. Duplex gives much less output because it sequences each molecule twice, and it costs more.
- KB likes that Roche says boldly that Q20 is fine: "it's nice that somebody is saying like Q20 is fine." Historically, companies battled on quality and "would hit each other over the head," although high accuracy was never really needed for counting applications.

## Illumina's position and response

- KB says that for labs already owning Illumina, adding Axelios raises "what do I do with the Illuminas?" because "there's a limited amount of demand for next-gen sequencing." Smaller cores would not run both; displacement "might take a while."
- Illumina's response, which he calls smart: for existing owners, make the NovaSeq X progressively more attractive with more output and new modes: the 35B flow cell, 5-base sequencing on mapped reads, and Q70 (as stated). The message is "don't stop using our box" or you will miss expansions. He notes Roche has no clear path yet to native 5-base sequencing, though it can use library-based methods, and its reads can be longer.
- He thinks Illumina is acting "for the right reasons" (improving the platform and growing the market), "not to try to keep market share," and would do so with or without competition. He notes Illumina is "not evolving their box much anymore. There were no announcements really. And so it's incremental at this point." He found Illumina's case convincing: "If I had a NovaSeq, I'd be happy with what they're saying."
- Capex argument: Illumina does not require a new instrument. Ultima would need new capex to reach the $200,000 level (as stated), Axelios $750,000, and Element VITARI $689,000. Depreciation of purchases flows into operating costs, so avoiding new capex is attractive.
- He calls the new features "bona fide": mapping a genome and phasing haplotypes (assigning variants to the chromosome copy they sit on) was previously possible only with PacBio or similar. It is "a very innovative use of the technology they already have."
- Illumina has "farther ahead" capability and a "huge installed base." If he already owned an Illumina sequencer, switching "wouldn't be that obvious."
- Flow cell loading: he says the 35B (bigger than 25B) is hard to fill efficiently; "that's the main reason we've never gone for the platform because we couldn't fill it fast enough." The same issue slightly applies to Axelios's 40 billion reads. He notes Illumina charges so much for smaller flow cells that they don't help.

### Methylation and 5-base

- Xpandomer does not preserve methylation information the way PacBio or Oxford Nanopore do. KB says Illumina's future (constellation/TruPath with 5-base methylation) is simpler because everything happens on the flow cell: load high-molecular-weight DNA, hit go, and get phasing, methylation and the genome backbone at once. This is attractive for a basic clinical genome.
- On Roche, Ultima or Element, one can use TAPS, EM-seq, or bisulfite library methods, but that means making two libraries, sequencing both and merging the data.
- Tradeoff: running a flow cell in methylation-and-mapping mode uses the whole flow cell, so it is constraining for a core that mixes applications across lanes. Library-level methods allow pooling with methylation for only some samples. He says it is not obvious which is better; "it will really depend on the core or on the user." Facilities that crank out many human samples would find Illumina's all-in-one more attractive.

## Clinical market and Roche's strategy

- KB: clinical labs "take forever to make changes." His lab has been CLIA certified in the past and did clinical work during COVID. Displacing Illumina's clinical foothold would be hard for any other company, but "if there's any company that is just like pre-set up and in a great position to dominate the clinical market, it's Roche. And if I were Illumina, I'd actually be very scared of that."
- He expects a "Cobas NGS" (reference to Roche's Cobas diagnostics line) tied to drugs and other diagnostics, so "they have no reason to price it like as a research box."
- Internal tension (speculation): Roche's founder is "very research-y" and may want it everywhere, whereas clinical people may want to hold it back as a premium technology. If the box is opened to LDTs (lab-developed tests), labs doing their own LDTs may not switch to a pricier Roche-branded CE Mark or FDA kit.
- MRD/ctDNA players (e.g., Guardant, Natera, BRL as transcribed): attractive box, but many work with Ultima or Illumina, which do not compete with them at the test level, while Roche will. KB would want a "dumb" sequencer from a non-competitor; if Roche offers its own MRD test combined with Droplet Digital and its portfolio, those firms would be "very vulnerable." He flags this is outside his expertise.

## Core lab dynamics and adoption

- Outsourcing: KB's core encourages other cores to outsource sequencing to it rather than own instruments. He argues "you don't really need 1,000 machines, each of which can generate 40 billion reads in four hours," and that keeping such instruments full is "a pain." Alternatives for outsourcers are NovaSeq outsourcing or a friendly core versus Novogene (as transcribed). Some cores resist because ownership is part of their identity; some instrument makers also don't want it ("They want an Axelios in every core facility").
- If one's model is outsourcing with Axelios, "you do it early. You don't wait." He says the real sophistication is now in making libraries and communicating capabilities. At smaller institutes, $750,000 is still a lot.
- Workflow burden: Axelios library prep is no more complex than others (different molecules and enzymes; many labs automate it), and most workflow occurs on the flow cell. The burden is maintaining many workflows, each with SOPs, training, and kits. His staff just became adept at Element and Ultima, and adding another is "just more work." He uses a diner versus fine-dining analogy: with a huge menu, "none of them are going to be excellent."
- Conservatism: peers are "very suspicious," scientists "conservative weirdly," and many are reluctant to change. Core directors are gatekeepers who control technology choices because researchers struggling with grants want someone else to decide. That is why vendors "go out of their way" to build relationships with them. KB rarely attends ABRF (a core-lab society meeting), calling it "group think," and views other cores as competitors. He thinks many peers' mindset is "I don't want to be the business that makes a mistake."
- Vendor-support risk: midsize or small cores buying a $750,000 instrument could be hurt if it is not supported; Ultima is "even more that way." Past bad bets include the ADI (as transcribed) sequencer and Ion Torrent instead of Illumina. "You might not be able to get another shot on goal ever."

## Element VITARI and Ultima

- KB's lab has five Element instruments, about "1.5 VITARI's worth of output," so he probably will not buy VITARI. For mid-sized cores with one instrument, he thinks VITARI is "very attractive": Illumina libraries load natively, data "looks just like Illumina except better," and it is affordable. He credits Element with understanding what "State University X" might want.
- For NextSeq 2000 owners, VITARI is somewhat more expensive but discounts offer a path to more output. It lacks 5-base sequencing, but small cores mostly do RNA-seq and single cell, so that matters less. He expects it to improve with smaller and larger flow cells.
- Ultima: at AGBT it presented wafers sized 5, 10 and 20 (as transcribed) that can be used by quarter, half or whole, which he finds unique. He says his Ultima provides very low whole genome pricing.
- Guidepoint's summary table lists Axelios negatives as slow rollout and higher initial cost versus some competitors, Illumina's as a potential challenge from new entrants, Ultima's low-cost WGS, and VITARI's affordability without 5-base sequencing (these are the platform's summary, not direct quotes).

## Concluding views

- KB: "It's a great time to be a next-gen sequencing" user; competition is "great for the field" but stressful for companies and decision makers.
- Long-term: in about 10 years sequencing will be "embedded" in the background like computation in iPhones. It took about 30 years from early genomics and arrays to a mature technology, and the field is "five to ten years out from the point when it becomes boring."
