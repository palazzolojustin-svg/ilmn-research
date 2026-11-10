# Sequencing center director debriefs AGBT 2026: Roche AXELIOS, Illumina NovaSeq X upgrades and TruPath, and the pricing war

*Source file: `Working Notes/Sources/ILMN/expert_call/Expert_2026-03-06_Director_of_Sequencing_Center_at_University_Sees_Challenges_and_Opportunities_in_Roche_and.md` · Date: 2026-03-06 · Expert call (consultant expert, buy-side client); published 2026-06-04; interview 2026-03-06. Expert: Director of a university Sequencing and Technology Center, formerly Alliances & Partnership Ecosystems Manager at Complete Genomics (left Jan 2025) · expert call*

**Summary.** A university sequencing core director, who also worked at Complete Genomics until January 2025, reviews the AGBT 2026 conference. They see sequencing as fully commoditized, Roche's new platform (AXELIOS) as solid but with a long 19-20 hour upfront workflow and regulatory complexity around reusable flow cells, and Illumina as "back" with NovaSeq-centric launches that may push smaller labs out. They view TruPath (Illumina's synthetic long-read tech) as a credible clinical threat to PacBio and ONT, and Q70 accuracy as of little use.

## Expert background and how to weigh the views

- The expert is the current Director of the Sequencing and Technology Center (STC) at a university. Their lab runs both short-read platforms (Illumina; short reads are small DNA fragments sequenced in bulk) and long-read platforms (PacBio and Oxford Nanopore, "ONT"; long reads span much longer DNA stretches). [Expert bio]
- Before the university, they were Alliances & Partnership Ecosystems Manager at Complete Genomics (an Illumina competitor), responsible for market development strategy for the platform ecosystem. They left in January 2025, about 14 months before the interview. They were two levels removed from the C-suite, reporting to a Senior Director. [Expert bio]
- They can speak about Illumina and competitors including Aladdin Bioinformatics and Velsera. [Expert bio]
- Interview date was 2026-03-06, shortly after AGBT (the Advances in Genome Biology and Technology conference); published 2026-06-04. The perspective is consultant expert for an investor-led (buy-side) client. [Expert: university sequencing center director, Mar 2026]
- Direct experience: running a core lab, using an Illumina single-cell kit, PacBio Revio, ONT, Illumina rep interactions, talking to Roche salespeople, and prior Complete Genomics work. The lab does **not** own a NovaSeq; it outsources that work. Much of the commentary on Roche's AXELIOS is inference from conference presentations and conversations, not hands-on use, and the expert often flags "TBD" (to be determined).

## Overall AGBT takeaways

- Sequencing is now a commodity "if anyone thought it wasn't before," because prices keep falling. [Expert, Mar 2026]
- Several new high-throughput instruments were announced; the expert expects "a couple companies really struggle to move" them.
- Roche "didn't disappoint" and released most of the information people wanted. The expert expects questions about its upfront (sample prep) capabilities, but it "looks like it'll be a solid platform."
- Illumina, "the old Illumina, the one that's trying to take over the world again," looks "back" with new applications and markets it is pushing into.

## Competing platforms announced

- **Ultima**: announced an updated box, the "200," allegedly with higher throughput that will help drop cost. The expert says Ultima has placed a handful of boxes but "the economics around their platform still haven't proven themselves." Several sites with Ultima boxes cannot fill a run, partly because over 1,000 Illumina NovaSeqs are installed, creating a lot of spare capacity in the market.
- **Element**: announced a high-throughput box to complement its AVITI (the expert could not recall the name and said "Avantor"). The expert says it is basically the same box Complete Genomics launched a year earlier. It targets the medium-sized market, which "makes sense based on price and output." The expert says Element has a longer run time, "which isn't going to be great for them," and doubts how it fits when many labs already have NovaSeqs and Ultimas and are considering Roche.
- **Complete Genomics T1**: the same box as Element's, but faster, per the expert.
- Element appears to be pushing into application-specific roles, as Singular tried to do. The expert says that if a sequencing center's bread and butter is sequencing, that is not what you buy a box for.
- Complete Genomics is "easily in that ballpark" on price, "probably even better on scale," but "can't get into the conversation." [Expert, Mar 2026]
- "The war on pricing is getting brutal." [Expert, Mar 2026]

## Roche: pricing

- Roche's headline of a roughly $150 genome excludes capital expenditure (CapEx, the cost of buying the instrument) and other items. On base reagent cost alone, every platform lands around $100-$200. The expert expected this range and knew Roche was holding back its pricing for the conference.
- Expert expects Roche to cut further "in the next year or two" through iterative product cycles. Every major platform is now at that price point, so Roche had to at least match the industry.
- Real-world pricing for a 30x genome (30x means each DNA position is read about 30 times on average) on today's NovaSeq X, per the expert:

| Setting | Real-world price | Why |
|---|---|---|
| Research (big centers) | about $460 to $575 per 30x genome | Depends on overhead and costs |
| Clinical | about $1,000 or so | Added clinical costs, plus 100x or higher coverage |

The point: headline "$100 genome" figures are catchy, but once everything else is included, "it unfortunately is never that cheap."

## Roche: reusable flow cells (the "Rejuvenator")

- A flow cell is the consumable slide on which sequencing happens. Roche plans to sell the sequencer plus a box to refurbish flow cells, which the expert calls the "Rejuvenator." Whether Roche's headline price depends on reuse is a debate; the expert says efficacy is "TBD."
- The expert has seen preliminary data and spoke with people who have run it; they said flow cells reload well, with claims of 10 or 20 times reuse (the client says 20; the expert agrees "Twenty, yeah"). After about 10 uses, "some of the stuff starts to wear a little bit, because you're constantly re-adding pores," which becomes "a little pain." (The expert describes pores here; this is the expert's wording.) PacBio is doing the same on the long-read side. Open questions: will reused cells give the same amount and quality of data as the first run?
- **Regulatory difficulty** (FDA, the US regulator): the expert has worked with clinical labs and says validating a reused flow cell is "doable, but ... really tricky." Labs would have to show "without any shadow of a doubt, and then some" that reuse causes no degradation of sample or data and no process issues. They would likely need positive controls on each reuse run and assurance that rejuvenation worked 100%. Extra steps and checks would be built in, and "you're going to lose some flow cell space" to the extra material. Speed helps, but paperwork and checks would slow the process and make it somewhat more expensive.
- Controls are universal: every platform uses a control. PhiX (a small, well-characterized viral genome) has been Illumina's standard since early days, and in certain runs it is injected to help balance the color signal because of Illumina's SBS (sequencing by synthesis) chemistry. So controls are not a unique disadvantage of reusable flow cells.
- **Effect on adoption**: the expert thinks reuse will actually *increase* uptake because many labs value less waste. ONT touted the same strength almost five years ago: you replace the pores in the flow cell and can theoretically run as much as you want, stop and start, and so on. The catch is that the pores are artificial bacterial protein pores, "a protein, not DNA, so there's a lot of stability issues." The expert calls it "an easily solvable problem" that Roche, with money and bandwidth, will likely solve, and says it will probably help Roche.

## Roche: clinical adoption speed

- Adoption curves for technology have shortened. Roche has followed the normal approval sequence: whole genomes (easiest), then DNA applications, then RNA-seq, then specialized applications, and "so far, they've checked all those boxes" with "no problem" showing the platform works.
- Historically, research platforms needed five to 10 years to be stable enough for clinical use. Now clinical sequencing is well established, multiple competitors operate there, and Roche has resources, a clinical company and a research arm. The expert says Roche could push into the clinic "potentially as fast as any platform has gone." Roche salespeople told the expert this is exactly their plan. [Expert, from direct conversations with Roche sales]

## Roche: workflow, prep and infrastructure concerns

- **Upfront prep**: initially Roche's presentations referenced KAPA (Roche's library prep kits), but at AGBT it showed a roughly 19-20 hour upfront workflow, because the Xpandomers (the expanded molecules used in Roche's chemistry) were enlarged. The expert says this "is going to throw a wrench into" things and is their biggest question.
- Analogy: ONT's PromethION (its large instrument) offered 24 or 48 flow cells, yet labs could never prepare enough samples to fill a 48-sample run. A very fast sequencer forces labs to speed up prep and then handle the data.
- Roche's flow cell is very small; Roche hasn't said how many samples load at once, and the expert hasn't seen much on barcoding (tagging samples so several can be run together). The expert assumes several can run, which pressures prep ("you can only prep so many at a time"). The expert has "theoretically mapped it out" for a medium-sized lab and calls it "tough."
- **Back end**: analysis must speed up, requiring bigger servers, possibly GPUs. Much open-source software is written by labs or postdocs and often needs review, re-editing and parallelization. Roche appears to use fairly open-source analysis software, so no extra purchase is required, though this might change toward subscriptions. Servers would run around the clock.
- **Installing the instrument**: "You buy the box, you plug it in, once you get it validated, then you bend your operations around it." Liquid handlers (lab robots) would need reprogramming; some of Roche's upfront workflow may not be automatable and might need a new robot or manual steps, reducing time and cost savings. Standard QC (quality control) equipment should be fine. KAPA kits are very automatable and the lab uses them. The expert assumes Roche will incorporate KAPA over a year-cycle of product management.
- **Footprint**: clinical labs may be in tight quarters with walled-off pre- and post-PCR rooms (PCR is DNA amplification); the expert assumes Roche's sequencer plus Rejuvenator would sit in the post-PCR area. Research labs usually have plenty of space, so footprint is not a big deal. Element and Complete Genomics boxes are about the size of a mini fridge. Example of finicky equipment: the lab's PacBio Revio needs a dedicated, temperature-controlled room because the optics are sensitive; trouble starts above about "72°C" (as transcribed, likely meant °F), and they were "always fighting air coolers."
- **Timing**: the box goes on sale this year, the expert was told in Q2 2026. Watch who buys it and media releases. Expect steady data and product improvements and more early adopters; "by ASHG this time next year we'll have a whole different conversation."
- **Would the expert buy one?** "It's nice, but no." They have ONT and understand that workflow. They would consider it mainly if it were cheaper: if it is half the price of a NovaSeq and can do 80%-90% of what a NovaSeq does, "it makes more sense to buy something like that." They wouldn't run it full tilt or use the speed. (The reference to "half the price" is conditional, not a confirmed Roche price.)

## Illumina: overall reaction to AGBT announcements

- The expert calls the announcements "long overdue." Illumina was "so focused on just only sequencing and not innovating" that it fell behind, but its leadership "sounds like" they have ideas to move forward. [Expert, Mar 2026]
- Everything announced centers on the NovaSeq, "probably on purpose to push people up to that level." TruPath's Constellation technology must run on the NovaSeq, and more is becoming NovaSeq-exclusive. Illumina is "trying to push people to bigger boxes as usual."
- Expert's concern: small labs and users of medium-sized platforms "are going to see problems." "Some of that's going to backfire" as the expert sees market consolidation. Genomics cores (shared university sequencing labs) are under growing pressure, especially from NIH (US National Institutes of Health) funding problems. Peers on a text chat ahead of a core meeting reported that outside groups are "eating their lunch"; cores must either work with those groups or have institutional support "that most people don't have right now." Illumina's strategy may push some out of the market.
- Who is doing the eating: large sequencing operations running almost around the clock, such as Plasmidsaurus, Novogene and other CROs (contract research organizations), which can do this cheaply and fast.

## Illumina: higher-throughput NovaSeq flow cell

- The expert calls a 5 billion-read flow cell (reads are individual DNA sequences produced) "the next logical step" and a "nice intermediate point." There is a big gap between the 2 billion and 8 billion read flow cells; the expert's lab sometimes sends out projects that fill an entire 10 billion flow cell (single-cell work). Illumina added the top flow cell size "to really drop the price for single cell stuff." (Product naming in the transcript is garbled: "the 25 or the 35 after they added the top one too.")
- This will help keep NovaSeqs running and "stave off the Elements and the Ultimas for sure," and benefits existing owners, who are Illumina's biggest installed market. It should open the door to more single-cell and spatial work.

## Illumina: single cell versus 10x Genomics

- Single-cell and spatial markets "are really suffering." Illumina is now competing with 10x Genomics; "we'll see if they're going to overextend themselves."
- Expert has used Illumina's single-cell product (the Fluent kit, from Fluent BioSciences, per the expert's wording) and finds it "suboptimal compared to what 10x has." From head-to-head data the expert has seen, the Fluent kit did not produce as many annotated genes per sample as 10x. Illumina announced a new version with updated chemistry that is "a little more robust" and picks up more gene profiles.
- Illumina is gaining a foothold: for hard-to-dissociate tissue such as spinal neural samples, its kit "does a pretty good job."
- Illumina "can use it as a loss leader" (sold cheaply to win customers), since 10x "has been pricey." 10x recently cut prices in response. [Expert, Mar 2026]

## Illumina: TruPath / Constellation synthetic long reads

- TruPath is Illumina's name for Constellation, a synthetic long-read technology (infers long-read information from short reads). Illumina has tried this a couple of times before; the expert doesn't know what is different but thinks "this one is much better." The expert's Illumina rep doesn't know they've asked.
- The expert calls it "a pure clinical play," a direct response to PacBio and ONT growth in the clinic (long reads give more diagnostic information) and to long reads "eating into" Illumina's market share. It lets Illumina keep clinical NovaSeqs running and offer new clinical tests.
- The expert's reading of Illumina's last call: research is "falling off," and the only growth, "maybe steady at best," is clinical, so Illumina will push for clinical adoption. (Characterization by the expert, not a quote of management.)
- Quality: the first paper used clinical benchmarking data; "the numbers were very good," F1 scores (accuracy measure combining precision and recall) in the 99% range; calls crucial SNPs (single-letter DNA variants) better in the human standard samples used. It does phasing (working out which variants sit on which inherited copy), allowing haplotypes in a family trio. It is "pretty close to being as good as your long-read data."
- **Threat to long-read**: "Yes," a meaningful threat if it holds up head-to-head and improves. If you already have a NovaSeq, "there's no reason to buy a PacBio at this point." It may not be the longest read (ONT still holds that), but "long enough." The expert predicts "They will drive this to the clinic within five years."

## Illumina: Q70 accuracy

- The expert says Q70 is "not very" useful. Q scores (a measure of base-call accuracy) came out in the early, "wonky" days to aid comparison; now nearly everyone is at Q40, Q50 or higher. Q70 is nice, but "if anything, it'll probably hurt them a little bit in the long run, because you won't need as much sequencing" (higher accuracy means less redundant coverage is needed).

## Key risks and uncertainties noted by the expert

- Roche's flow cell reuse performance (wear after about 10 uses, pore protein stability) and FDA validation complexity are unproven.
- Roche's 19-20 hour prep may bottleneck labs and raise informatics and server costs.
- Ultima and Element may struggle to fill runs and place instruments amid NovaSeq overcapacity.
- Illumina's NovaSeq-centric strategy may alienate smaller cores and accelerate consolidation toward CROs and large centers; Illumina's single-cell product trails 10x on gene detection but is improving.
- Price compression across all platforms; Q70 may reduce sequencing demand per sample.
