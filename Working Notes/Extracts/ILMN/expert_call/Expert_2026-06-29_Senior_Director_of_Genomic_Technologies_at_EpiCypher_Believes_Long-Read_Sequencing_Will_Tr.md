# Expert call with EpiCypher Senior Director of Genomic Technologies: Illumina NextSeq 2000 user experience, Element and Roche competition, long-read displacement of short-read DNA methylation, MRD and spatial

*Source file: `Working Notes/Sources/ILMN/expert_call/Expert_2026-06-29_Senior_Director_of_Genomic_Technologies_at_EpiCypher_Believes_Long-Read_Sequencing_Will_Tr.md` · Date: 2026-06-29 · Expert-network platform transcript (published 2026-07-01), AI interviewer; expert is a Senior Director of Genomic Technologies at EpiCypher (small biotech); name not given · expert call*

**Summary.** A hands-on, 15-year Illumina user at a small epigenomics biotech describes why they stay on Illumina's NextSeq 2000 despite paying roughly 15-20% more than alternatives: reliability, support, ecosystem and track record. The expert's main forward-looking view is that long-read sequencing (PacBio, Oxford Nanopore) will take over whole-genome DNA methylation work within 2-3 years because price per gigabase is now at parity. The expert names Roche as the scariest competitor and Illumina's biggest risk as being spread too thin across proteomics, spatial and MRD (minimal residual disease testing).

# Expert call notes: EpiCypher Senior Director of Genomic Technologies (interview 2026-06-29, published 2026-07-01)

## 1. Expert background and how to weigh the evidence

- **Role.** The expert is Senior Director of Genomic Technologies (in the interview, "senior director of genomics") at EpiCypher, which they describe as "a small biotech company." They oversee six scientists and research associates in the genomics lab and the genomics projects within R&D. Nearly all of those projects have a readout (final measurement) on the Illumina sequencing platform. [Expert: Senior Director, EpiCypher, 2026-06-29]
- **Relationship to Illumina.** The expert is a customer, not a former employee or competitor. They have used Illumina for about 15 years and have hands-on experience with the instruments. Their duties include output and quality control, running instruments to specification, bandwidth evaluation, consumables inventory (reagents and flow cells customers buy for each run) and relationship management with sequencing company representatives.
- **Decision-making power.** They are "one of the primary stakeholders" and one of the most senior people in R&D. They advise the C-suite, which makes the final decision on buying and retiring instruments. The other two key stakeholders are the chief scientific officer and the chief business officer.
- **Recency.** The experience is current (interview date June 2026). The Element evaluation took place "probably two years ago."
- **Limits of their view.** They are a research (R&D) user. They say they cannot speak to clinical genomics or reimbursement. On MRD, spatial, Roche and Ultima they speak from conference exposure and reading, not direct use. The interviewer is an AI, and the expert is classified as a Doctor/Medical Professional perspective.
- **Weighting.** Illumina and long-read comments on methylation are direct experience. The 2-3 year timeline, the spatial price outlook and the competitor ranking are the expert's opinion and speculation. The expert says explicitly that the spatial price trajectory is "just speculation."

## 2. How EpiCypher uses sequencing

- **Applications.** The two main applications are epigenomics (study of chemical marks and protein binding on DNA that control genes) and DNA methylation sequencing (reading the methylation marks on DNA).
  - Epigenomics work involves sequencing CUT&RUN and CUT&Tag enriched libraries, which answer where proteins bind in the genome.
  - Whole-genome DNA methylation work is done on both short-read Illumina platforms and long-read platforms (Oxford Nanopore, "ONT," and PacBio).
- **Volume.** The expert thinks of volume in Illumina cartridges. They use the P2 cartridge on the NextSeq 2000 (about 400 million-500 million clusters, or paired reads, per cartridge). They run four to six per month, equal to several hundred libraries per month.
- **Depth.** Their assays need medium sequencing depth, 10 million-15 million reads per reaction. About 400 million reads per run allows pooling of 40-60 libraries in one run. DNA methylation has lower throughput, which affects bandwidth.
- **Typical output.** An example run is about 30 gigabases of data, which takes about an hour to download.

## 3. Purchase criteria and why they stay on Illumina

- **Top two factors.** Usage and cost-effectiveness. A key metric is cost per gigabase (a gigabase is a billion DNA letters read) or cost per read.
- **Why they like the NextSeq 2000.** It has a broad range of cartridges giving different output levels.
- **Pricing position (opinion based on their evaluations).** Illumina's cost per gigabase is "middle of the road" and "pretty good." There are few short-read competitors, and Roche "hasn't quite hit the market yet." Illumina sits about 15%-20% above alternatives, on "the more expensive side of the gap."
- **Why they stay despite the premium.** The reasons are reliability, tech support, infrastructure and an ecosystem of reagents. It is logistically simpler to be on one platform. They say Illumina has a track record since it bought Solexa in 2006: "They're an easy bet. Even though they're a little more expensive, they're going to be around in five years." They add, "We are willing to pay the premium."
- **Process for new platforms.** First comes information gathering on strengths and weaknesses ("warts and all"). Then come meetings with sales reps or technical staff and requests for demo library runs to see the data, workflow and bioinformatics back end. Then the CSO, CBO and expert huddle to decide. The expert gives technical advice and the C-suite is not involved in technical evaluation. Time from awareness to a go/no-go decision is about three months. Because the company is small it moves quickly, and the slow step is interacting with the sequencing company.

## 4. Competition in short-read sequencing

### Element (direct evaluation)
- About two years ago the team seriously considered leaving Illumina for Element. This was just before the NextSeq 2000 launched. Element undercut Illumina's price per gigabase (or per million reads) by "almost half."
- Just before the decision, Illumina launched the NextSeq 2000, which cut consumables pricing by 30%. This made Illumina "much more competitive." The expert says this explains the roughly 20% difference cited above.
- A meaningful gap remains: about 10%-15% at medium throughput. The expert notes comparisons vary by throughput tier (low throughput is more expensive per gigabase, then medium, then high such as the NovaSeq) and that medium throughput is their reference.
- **What would win them over.** A track record of innovating and driving costs down, increasing throughput and reliability, and improving base-calling quality, or a "completely distinct technology that is unique to the platform."
- **Quality.** Q scores (accuracy of base calls) are "becoming increasingly important." Illumina typical runs are "easily Q30 to Q35"; Element is "slightly higher Q in the mid- to high-Q30s, but nothing significant."
- **What tipped the decision back to Illumina.** Legacy, technical support, history of working together, trust in reliability and innovation, beyond the pricing response.

### Ultima (not used; opinion)
- Ultima is cheaper and competes with the higher end of Illumina (NovaSeq-class) instruments, but is "really not as accessible." It is not accessible to academic cores or industry sequencing cores, and targets "mega scale sequencing consortiums" as its niche.

### BGI / MGI (not used)
- BGI Genomics is a Chinese sequencing company with a wide range of instruments and "very competitive" prices. The reluctance is U.S. government restrictions on collaborating with or using Chinese instrumentation.

### Roche (not yet launched; opinion)
- The expert calls Roche "probably the scariest competitor for Illumina right now." Reasoning: Roche is "hyper-focused on the clinical $100 genome," sequencing is "extremely fast," "extremely accurate" and "extremely cheap," and the focus is on the clinic where Illumina's emerging products (MRD) are also aimed. The expert thinks Roche "could out-compete Illumina in that space."

### Which competitor depends on the application
- Long-read can take away DNA methylation. For enrichment-based and RNA-based methods, the winner will be whoever sequences the most reads cheapest: ultra-high-throughput players like Ultima, high-end BGI instruments, Element and Roche.
- The expert also noted that last year EpiCypher onboarded a new short-read technology "moving towards commercialization" (kits and services), which ramped up their short-read output quite a bit. The vendor is not named.

## 5. Long-read displacement of short-read DNA methylation (key thesis)

- **Shift in customers.** The expert sees "a major shift" among customers interested in whole-genome DNA methylation toward long-read.
- **Price parity.** Price per gigabase is now relatively equal between short-read (30X whole genome bisulfite or EM-seq) and long-read. The expert's figure is "5-8 per gigabase" on short read, and ONT and PacBio are in the same 5-8 range (the dollar signs were lost in the transcript, so the currency is presumed US dollars).
- **Long-read advantages.** Long-read detects methylation natively. It needs no conversion library prep (bisulfite or EM-seq convert methylated versus unmethylated DNA) and no PCR; one simply sequences purified genomic DNA. Data quality is better and workflow is easier.
- **Implication (opinion).** "All things being equal," short-read methylation assays like bisulfite and EM-seq will "go away, because there's no reason to do short-read anymore."
- **Current and expected share.** Long-read is "probably 10%-15%" of EpiCypher's methylation work now, with an upward trend. The expert expects 50% in two to three years.
- **Impact on Illumina.** Illumina's share of their spend "will go down, barring any new short-read technologies." Customers are shown both options with pros and cons, and increasingly choose long-read "because of the additional value."
- **Platform split.** EpiCypher has a PacBio Revio internally and uses PacBio for its own long-read work. Among broader customers interested in long-read, the split between Oxford Nanopore and PacBio is about 50/50.
- **Why long-read is chosen.** The long-read assays are multi-omic (methylation, genetics and chromatin information together), and short-read assays are for customers who want only methylation.
- **Skeptic pushbacks.** (1) Customers interested only in certain locations: enrichment methods are less accessible on long-read. (2) Unfamiliarity: no bioinformatics pipelines or support. The expert's team taught itself long-read analysis in about four to six months, and says anyone who can do short-read analysis can learn long-read. EpiCypher gives customers training time and tech support.

## 6. NextSeq 2000 experience and operations (direct experience)

- **Onboarding.** "No workflow disruption. It was really amazing." Before the NextSeq 2000 they manually denatured libraries off the machine (turning double-strand DNA into single-strand with dilute sodium hydroxide), which adds variability and error. The NextSeq 2000 does it on the instrument. "That's one of the strengths of Illumina is just the simplicity of using the instruments." Time from delivery to independent production runs was "a week or two."
- **Steady state.** Largely smooth. About once a year an instrument error occurs (for example a laser or internal fault). Illumina's tech support usually comes out within a few days, "really quick," and Illumina compensates for lost reagents. Other friction is user-driven (wrongly assigned barcodes, which requires requeuing in analysis and happens fairly frequently; sample-sheet transpositions or name errors).
- **Data flow.** Sample sheets are prepared in BaseSpace (Illumina's online portal). The run is configured on the instrument (single- or dual-read). Data is stored locally on a hard drive on the instrument and simultaneously streamed to BaseSpace. EpiCypher has a BaseSpace Pro account with storage credits, where the FASTQ files (raw sequence files) live. The next day they manually download FASTQs to a local high-performance cluster and run analysis pipelines locally.
- **Bottleneck.** The download is "a bit of a bottleneck": about an hour per run (about 30 gigabases). "It's not too bad."
- **Bioinformatics capacity.** Not a limit. The expert helped write the initial pipelines, which are now automated, with a bioinformatics team for troubleshooting.
- **Quality control.** They check Q scores, contaminating DNA (bacterial, mitochondrial), adapter dimers, duplicated and multi-aligned reads, and alignment rate (expected 60%-80% of reads aligned for their assay; assay-specific). Only after quality passes do they invest manual effort in interpretation, often integrating RNA-Seq data or published data (for example Venn diagrams).
- **Reruns.** Ambiguity is rare. About half the time they rerun the experiment and half the time they triage and move on. Problems are "almost always a library preparation issue," from cell or library quality, not sequencing.
- **Decision speed.** One to two weeks from receiving data to starting the next experiment. The bottleneck is scientific decision-making (aligning schedules and input from parties), not bioinformatics.
- **Budget.** Budgets are set by project scope and deadline. They sequence what is needed. Sequencing is expensive but "not the major driving cost," and they sequence enough to be confident, with controls and replicates.

## 7. Minimal residual disease (MRD) testing

MRD is testing for traces of cancer remaining after treatment, here via cell-free DNA (DNA fragments in blood). Knowledge is from last week's AACR Lymphoma Conference, not direct experience.

- **Takeaway.** MRD is becoming "a critical part of the clinical toolkit," and the scientific community has growing confidence in cell-free DNA monitoring. The expert notes Illumina "just announced their first distributed whole genome sequencing for MRD detection" (distributed means run at the clinical site, not in a central lab) and finds it "pretty exciting."
- **Conference content.** Talks focused on therapy effectiveness (in lymphoma, the standard four-drug therapy CHOP) and on cell-free DNA including its methylation status, not distributed versus centralized. The expert guesses most speakers used centralized testing since it is more common and Illumina's offerings are recent. Illumina was not specifically recalled. Labcorp and Ultima were named as centralized options. Ultima was seen as "an emerging option for heavy sequencing users."
- **Illumina's offering (read about, not used).** Looks "fairly competitive." Specs highlighted: very high Q scores (Q70 mentioned) and sensitivity to single-digit parts per million in blood cell-free DNA. The expert assumes (as a non-clinician) that distributed testing simplifies logistics, lowers cost and speeds turnaround.
- **Biggest barrier.** Awareness.
- **Skeptic case.** Distributed testing requires on-site training, and clinical staff may lack bandwidth (busy with pathology and other sequencing). Institutions must judge whether efficiency, cost and turnaround gains justify the entry barrier of training, understanding and data interpretation.
- **Workflow bottleneck.** The workflow is essentially whole genome sequencing, but a patient-specific "fingerprint" of the tumor must first be built by sequencing the initial biopsy. Later cell-free DNA from blood is compared with it. Creating the reference is the hardest part. The bioinformatics is "already optimized and automated by Illumina."

## 8. Spatial and single-cell

- **View.** Spatial (sequencing that records where cells sit in tissue) is complementary to short-read workflows, though it "might replace the single-cell short-read workflow" since spatial is effectively single-cell plus X/Y coordinates, and is "better compared to solution-based single-cell." It would not displace other short-read assays.
- **Timing.** Routine in "maybe three to five years." Currently cutting-edge, many companies, most commonly RNA (transcriptomic) measurements, with others trying DNA methylation, chromatin accessibility and antibody-directed profiling.
- **Cost.** Expert's recollection: about $4,000-$6,000 per library for library prep plus sequencing, which is too expensive for mainstream use.
- **Why costly (opinion/speculation).** Sequencing cost is a major contributor, because 90%-95% of reads are thrown out of final analysis, requiring billions of reads. Either sequencing costs fall or capture of unique reads per cell becomes more efficient. The expert declined to estimate the path to $1,000 per library.

## 9. Risks to Illumina (expert opinion)

- **Biggest risk.** Illumina becoming "spread too thin to where it's not really the best at anything." The expert compares Illumina to Apple: not always first to market but strikes "the best balance of compromises" among cost, accuracy and cutting-edge technology.
- **Mechanism.** As Illumina pushes into multi-omic areas (proteomics, spatial, MRD), if it "forget[s] their foundation of short-read sequencing and cost effectiveness," hyper-focused competitors could supplant it.
- **Other threats named in the call.** Long-read in methylation (Section 5), Roche in clinical sequencing, Element on price, Ultima and BGI at ultra-high throughput.

## 10. Notable quotes

- "They're an easy bet. Even though they're a little more expensive, they're going to be around in five years." [Expert, 2026-06-29]
- "The price per gigabase is now at parity." (short-read versus long-read methylation) [Expert, 2026-06-29]
- "There's no reason to do short-read anymore if it's just as cheap and the data quality's better on long-read and the workflow is easier." [Expert, 2026-06-29]
- "Illumina's biggest risk is being spread too thin to where it's not really the best at anything." [Expert, 2026-06-29]
- "Roche probably is the scariest competitor for Illumina right now." [Expert, 2026-06-29]
- "We are willing to pay the premium." [Expert, 2026-06-29]

## 11. Gaps and caveats

- No reimbursement or clinical-setting visibility. Budgets are not a constraint for this customer.
- No exact dollar figures for Illumina cartridges, and the 5-8 per gigabase figures lost their currency symbols in the transcript.
- The expert's 50% long-read share forecast applies to EpiCypher's own methylation business, not the market.
- The Element price gap is given as almost half before the NextSeq 2000 and 10%-15% after, versus a 15%-20% gap to "alternatives" generally; the expert reconciled these as one 30% price cut (approximate, recollection-based).
