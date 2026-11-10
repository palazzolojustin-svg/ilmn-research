# Broad Institute Executive VP on Roche's Axelios (SBX) sequencer as a potentially disruptive platform for rapid and counting applications

*Source file: `Working Notes/Sources/ILMN/expert_call/Expert_2026-04-06_Executive_VP_at_Broad_Institute_Sees_Roches_Sequencing_Platform_as_Potentially_Disruptive.md` · Date: 2026-04-06 · Expert-call platform transcript (published 20 Apr 2026; interview 6 Apr 2026); expert is an Executive VP at the Broad Institute (consultant perspective); interviewer is a buy-side investor, unnamed · expert call*

**Summary.** A senior executive at the Broad Institute, which has run a pre-commercial Roche Axelios sequencer as one of two beta sites, says Roche will most likely enter Broad's production use, first for incremental, speed-sensitive work such as same-day NICU genomes and for "counting" applications. Roche's announced pricing (about $150 per genome versus about $200 on Illumina's list price) and fast runtime could be disruptive, but data flow, validation and commercial availability (expected later in 2026) remain open. The expert says Element and Ultima are used only at low volume, and that Broad's Illumina spend was flat in 2024-2025 while data output doubled, with NIH grant funding a key risk.

## Expert background and basis of knowledge

- The expert is an Executive VP at the Broad Institute, a large genomics research center that runs many sequencers, including Illumina, Element and Ultima systems. The expert is a customer of Illumina and an evaluator of competitors, not a former employee. The interview took place 6 April 2026, so the experience is very recent. [Expert: Executive VP, Broad Institute, Apr 2026]
- Direct experience: Broad received a pre-commercial (beta) Roche Axelios, one of the first two placed. The other went to the Hartwig Medical Foundation in the Netherlands. The expert has run whole genome and counting samples on it.
- Direct experience: Broad also runs Element and Ultima instruments, but at low volume (see below).
- Speculation or secondhand understanding: Roche's commercial launch timing, how much longer Roche reads could get, how larger clinical labs will behave, and whether the market will decentralize. The expert flags these as uncertain ("I don't know").
- The interviewer says they are not a scientist by training, so several explanations are basic.

## Bottom line on Roche

- The expert says Broad will "most likely" have the Roche system in production. It offers more of an advantage than the other competing platforms, because of its very fast runtime and low cost. [Expert, Apr 2026]
- Most of Broad's current work does not need speed. Roche would first be adopted for incremental work not currently done on Illumina, such as a rapid genome for the NICU (neonatal intensive care unit) with a same-day result.
- Over time there is "a good chance" Broad puts more on Roche, because fast runs mean less batching (waiting to fill an instrument run) to reach a low price. Broad does that batching today on the NovaSeq X Plus (Illumina's high-throughput sequencer).
- Pricing is "potentially disruptive," but "the devil's in the details." The box is not commercial yet. The expert understands it will not be out until later in 2026. Implementation details remain undetermined: running it in production, data flow, and the analysis pipeline.

## Where Roche fits: counting applications and speed

- Counting applications (experiments that quantify short barcodes or tags rather than reading a whole genome) include single-cell RNA sequencing (quantifying transcripts in individual cells) and plasma proteomics assays such as Olink and SomaLogic (which read a barcode and count the relative amounts of different barcodes).
- Barcodes are designed to tolerate small errors; a read that does not match a valid barcode is simply discarded. So counting does not need very high accuracy, and Roche would run these in simplex mode (single-strand reads, lower accuracy than duplex, which reads both strands).
- Roche has been "pretty aggressive on pricing," announced at AGBT (a major genomics conference) in March 2026. For counting applications the expert says the cost "could be 1/2-1/3" of Illumina's list price. [Expert, Apr 2026]
- The value of speed depends on the application. In the NICU, clinicians want data the same day, tests are reimbursed at "a pretty high rate," and customers will pay more. The expert expects a market but says it is incremental and not the size of Broad's current Illumina business.
- For many applications, such as a big single-cell RNA experiment, speed does not matter; the 44-hour Illumina runtime "is not an impediment right now."

## Technology: SBX and expandomers versus Illumina

- Illumina uses sequencing by synthesis, which needs fluorescently labeled nucleotides (the DNA letters A, G, C, T in different colors) and a camera-like optical system. The flow cell (a highly engineered slide with tiny grooves where DNA clusters form) is also expensive. Both are cost drivers. [Expert]
- Roche's SBX converts the DNA template into large "expandomer" molecules that code for A, G, C and T. These pass through a nanopore (a tiny hole) that records a signal for each letter. There is no fluorescence, no camera, no labeled nucleotides and no highly engineered flow cell, so the expert says it has the potential to be "much cheaper" and is "likely to be cheaper actually than Illumina."
- Difference from Oxford Nanopore: Oxford passes native DNA directly through the pore, which is much harder to detect. Roche makes the pore easier to use by passing expandomers instead. The expert says there is "a pretty big difference."
- Read length: Roche appears to have headroom to read longer than it does now, but the expert does not expect Roche to match Oxford's very long reads, and does not know how long Roche can get.

## Workflow and runtime

- Roche workflow has three parts: library prep (attaching adapters to DNA), making the expandomers, and detection. Library prep and expandomer making happen on a separate machine from the sequencer. The result is loaded into the detection unit with the nanopore cartridge.
- Sequencing on the detection unit can take four hours, is tunable and can be shorter. Because expandomer making is on a different box, it can run in parallel, so the next batch is always being prepared.
- On Illumina, cluster generation (binding DNA fragments to the flow cell and amplifying them into spots, or clusters) and sequencing both happen on the sequencer. A NovaSeq X Plus run with the 25B flow cell takes about 44 hours.
- The expert agrees that, even if Roche's prep takes longer, in practice it will be "considerably faster than Illumina" at generating data.

## Throughput and batching

- Both the Roche and Illumina boxes can do about 20,000 whole genomes per year. [Expert, Apr 2026]
- On Illumina's 25B flow cell, Broad gets 64 genomes per 44-hour run. On Roche the expert estimates about five or six genomes per four-hour run, so roughly equivalent throughput over time, but with runs loaded about 10 times as often.
- The practical advantage: on Illumina, to reach the lowest cost you must fill the flow cell completely ("airplanes want to have all the seats full"), so labs wait and batch. With Roche's announced pricing and speed, labs could reach the low Illumina-like cost with much smaller batches.
- Market effect (speculation): this could further decentralize sequencing, letting more labs sequence in-house rather than outsource. Smaller labs would still need to build DNA preparation, data analysis and bioinformatics workflows, so uptake will take time. The expert thinks it "has potential to change the market a bit."

## Likely customers

- Interviewer hypothesis: clinical applications and mid-sized labs on the fence about buying an X Plus. Expert: possible.
- Smaller or decentralized clinical labs (for example in Europe) may be attractive.
- Large specialty diagnostics labs (Caris, Guardant, Tempus) are "more questionable" Roche adopters: they are tuned to Illumina, own many machines, always have samples so batching is not an issue, and cutting a run from two days to four hours saves little in a process that also includes sample registration and result return. They would also have to redo clinical validation and possibly go to the FDA depending on the product.

## Consumables and lock-in

- On Illumina, the flow cell and sequencing kit come bundled and must be used on Illumina machines. Broad buys library prep kits from many vendors (Roche, Watchmaker, Kapa); Illumina sells them too but does not capture that step.
- On Roche, the Roche sequencing kit is required, and the expert says library prep on the Roche machine must use Roche reagents (while noting that, in front of Roche, Broad "will probably use the Roche kit or we can use other kits"; the answer is somewhat inconsistent). The expert was "not quite sure" about the interviewer's suggestion that Roche could discount a bundle of prep consumables for Illumina workflows; they confirmed Illumina's flow cell and sequencing chemistry remain Illumina-only.

## Accuracy, data and software

- Roche has presented Broad's data at conferences and the expert says it is correct. With duplex reads Broad sees about a Q40 error rate (about 1 error in 10,000 bases), "very good"; simplex is less accurate but fine for most applications.
- No systematic bias seen "right now," but Broad has not done deep analysis of every sequence context. It has done whole genome sequencing and some counting applications, and "the data is quite good."
- Output format is "pretty standard" and runs through Broad's pipelines, though Broad will need to build custom quality control and may tune variant detection (finding DNA differences) once it has much more data.
- Broad would not run Roche data through Illumina's DRAGEN (Illumina's analysis software and infrastructure, which does both infrastructure and variant detection): the expert says files could be arranged to fit, but Broad would not, to avoid breaching the license; read lengths also differ. Roche will provide its own data processing with the box, and running two processing systems is "not a big deal."
- Open question: because so much data is generated so quickly, Broad is still working out data transfer rates and how to feed data to the cloud or its processing. This will be learned once the commercial box and bioinformatics pipeline arrive.

## Price per genome comparison

- The expert first recalled Roche's announced genome price as "a few hundred dollars," then corrected: Roche announced $150 at AGBT. [Expert, Apr 2026]
- Comparable Illumina figure: about $200 per genome at list price on the 25B flow cell, which the expert equates to $2 per gigabase (a billion DNA letters). This covers flow cell and sequencing consumables only. The expert says to compare Roche's $150 against Illumina's $150-$200 (the transcript says "150 − 200").
- Fully loaded cost (labor, all reagents and initial variant calling): Broad sells its Illumina genome for under $400.
- The interviewer noted that the $200 excludes sample prep, so it is not apples to apples, and that Roche would be unlikely to launch at a higher price than Illumina.

## Other platforms at Broad

- Element (mid-throughput benchtop sequencer): "hasn't honestly found much of a place with us." Broad has a strong Illumina discount on mid-throughput machines, Element has not differentiated itself, and utilization is low.
- Ultima (high-throughput, single-read, no duplex, good accuracy): at AGBT 2026 Ultima announced a workflow without the second box for its amplification step (usable on off-the-shelf automation), no emulsion PCR (a new way to get DNA onto beads), and chemistry improvements. The expert says people are happy with the data quality and Ultima is releasing a new box (model name not remembered, "UG200 or UG2000").
- Broad's Ultima use is low throughput and limited to a couple of projects: sequencing ancient fragmented human DNA (about 40,000 years old; thousands of samples, a funded researcher doing whole genomes), and some Olink plasma proteomics for one user (also run on Illumina).
- Reason users chose Ultima: "Special pricing," which Broad passes through to researchers. For the ancient DNA project, Ultima also built custom analysis software for the unusual error pattern of fragmented DNA. The expert says it could be done on Illumina but would need that vendor attention.
- Element and Ultima are not production level, are not used just to give vendors feedback, and are not displacing Illumina production volume.

## Research demand, NIH funding and Broad's Illumina spend

- Concern: NIH (US National Institutes of Health) is funding existing awards but very few new grants. The expert says this will likely hurt growth over the next couple of years unless it turns around. Congress has bipartisan support to keep the NIH budget flat though the Trump administration proposes cuts; the problem is money is not getting out as it used to. The expert saw a number over the weekend showing far fewer new awards nationally this year than usual at this point.
- Broad is diversifying toward industry-sponsored projects (pharma, biotech) and philanthropy (disease foundations). Growth is "hard to really count on," but demand is decent.
- Key datapoint: comparing 2024 and 2025, Broad's Illumina spend was basically flat year over year while it generated twice as much data. The expert attributes this mostly to the transition to the NovaSeq X Plus 25B and lower Illumina prices; in 2024 some projects were still on the NovaSeq 6000, and by 2025 it was fully off. "People are still hungry for sequence data."
- Possible growth areas: multi-omics (RNA, methylation) and single-cell RNA sequencing, as lower prices make large projects feasible; pharma is being approached, and tech companies want data for AI models. Little has materialized yet.
- 2026 outlook: Illumina spend growth is unlikely because Broad has added no machines and utilization is in the "upper double digit percentage." More spend would require buying machines, unlikely unless major new funding arrives. Current forecast: fine with existing machines. Unknowns in the second half of 2026: if big projects are cut due to NIH, spending could fall, but "too soon to tell."

## Clinical work at Broad

- Broad does small amounts of clinical sequencing, including back-end sequencing for some commercial labs and custom assays from local investigators (such as Dana-Farber) under a clinical framework. It does not compete with Caris, Guardant or Tempus, lacking the sales force and physician ordering channels. Hospitals use those labs rather than Broad.

## Notable quotes

- "Potentially disruptive" on Roche's pricing, with the caveat that implementation details remain to be determined. [Expert, Apr 2026]
- "Airplanes want to have all the seats full on an airplane." (on Illumina batching) [Expert]
- "Our Illumina spend was basically flat year over year, but we generated twice as much data." [Expert]
- "People are still hungry for sequence data." [Expert]
- Element "hasn't honestly found much of a place with us." [Expert]
- Ultima pricing was the reason users chose it: "Special pricing." [Expert]
