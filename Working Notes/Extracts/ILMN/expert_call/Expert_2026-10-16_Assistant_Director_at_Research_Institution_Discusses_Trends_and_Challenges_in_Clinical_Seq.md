# Channel check with a New York clinical genomics lab assistant director on sequencing demand, vendor mix and competition (interview 16 Oct 2026)

*Source file: `Working Notes/Sources/ILMN/expert_call/Expert_2026-10-16_Assistant_Director_at_Research_Institution_Discusses_Trends_and_Challenges_in_Clinical_Seq.md` · Date: 2026-10-16 · Channel check platform expert transcript (AI interviewer); expert is an assistant director at a New York research institution running a CLIA lab; published 20 Oct 2026 · expert call*

**Summary.** A customer of Illumina (a CLIA-certified clinical lab in New York doing about 5,000 30X whole genomes a year, mostly prenatal) says its short-read work is 100% Illumina NovaSeq X and will stay that way, because switching platforms means rebuilding all infrastructure. Volume is about 10% or more above Q3 2025 (a federal-funding trough) and about 5-10% above 2024. The main limits on growth are insurance reimbursement and a shortage of qualified report signers. The expert sees PacBio gaining a little share via carrier screening, rejects Ultima and Oxford Nanopore for clinical use, and is only evaluating Illumina's TruPath.

# Expert background and how to read this call

**Who the expert is.** The expert is an assistant director at a research institution in New York, with visibility into running sequencing platforms, including Illumina's, for clinical genetic testing. The platform labels the perspective as "Customer." The interviewer is an AI, so the questions follow a fixed template, and some questions embed facts supplied by the interviewer, not the expert (see "Interviewer-supplied context" below). [Expert: assistant director, NY research institution, interview 16 Oct 2026; published 20 Oct 2026]

**Relationship to Illumina.** The lab is a long-standing Illumina customer. The expert says Illumina short-read has been the lab's base sequencer "for as long as I've been there" (the lab ran HiSeq, then an earlier NovaSeq-class system, and now NovaSeq X). The expert also says they do not do the lab's budgeting, so they could not give pricing or spending figures. Their direct experience covers lab operations, validation and platform choice. Their views on Roche and the broader market are explicitly less informed.

**Recency.** The call covers Q3 2026 and was held on 16 Oct 2026, so the information is very fresh.

## The lab and its customers

- **Size.** The lab does on the order of 5,000 whole genomes a year, plus "a handful" of RNA transcriptomes (measurements of which genes are active) and long-read genomes. The expert did not know the output in gigabases (units of sequence data). The interviewer estimated about 400-500 terabases a year at roughly 30X coverage (each DNA position read about 30 times on average), and the expert called that "a reasonable estimate."
- **Type of work.** It is clinical testing in a CLIA-certified lab (CLIA is the US regulatory certification for clinical labs). Most testing is prenatal. Customers are a mix of people enrolled in research studies and people seeking clinical care for prenatal management, and pediatric and adult disorders.
- **Application mix.** About 70% of testing volume is prenatal (reproductive health), and the remaining roughly 30% is pediatric and adult hereditary and rare disease testing. The expert said 100% of the lab's work is hereditary disease, with prenatal testing carrying maternal and family implications. There is no oncology, infectious disease or residual disease monitoring today, though the expert said there are plans for the future.
- **Growth by application.** The expert expects prenatal to grow fastest over the next 12 months. Reasons given: patients increasingly want to understand their pregnancy and its possible outcomes, and demand rises as pricing becomes more affordable. Rare disease (defined by the expert as affecting fewer than 1% of the population) is a smaller pool of patients than general prenatal testing, so it grows more slowly.

## Demand drivers and bottlenecks

**Reimbursement is the dominant constraint.** The expert said "The most significant blocker of sequencing tests is insurance reimbursement." If insurers do not pay, uptake is "significantly less." The lab partly offsets this through research studies: it sets aside funds so that qualifying patients do not pay out of pocket. The expert's experience is that patients are willing to be sequenced if it is financially feasible. Asked about tailwinds, the expert said it is "primarily reimbursement." Reagent, computing and analysis costs keep falling, but "it's really the cost to the patient that is the primary barrier to uptake."

**Analyst workforce is the second bottleneck.** New York State requires that anyone signing out (approving) a test report be certified by the American Board of Medical Genetics and Genomics and hold a New York State license. The expert called the requirements "quite high," so the qualified pool is limited, which caps how many cases can be signed out. The expert said these two are "the primary bottlenecks as of today" and that this could change in future.

## Installed base and platform mix

- **Short-read (reads short DNA fragments; accurate and high-throughput).** The lab's primary platform is the Illumina NovaSeq X, which it has had for a number of years. Illumina short-read is also used for RNA sequencing.
- **Long-read (reads much longer DNA stretches).** The lab bought a PacBio HiFi Revio system, which the expert placed around the end of 2025, "maybe Q4 2025." The expert did not know the price paid.
- **Platforms evaluated and rejected.** The lab has looked at Ultima Genomics and Oxford Nanopore and judged them "not as useful for our clinical testing purposes." The expert has not, to their knowledge, tested Roche.
- **Split.** More than 99% of output is short-read, because that is the lab's base test. Long-read is used for confirmatory assays, research, or special cases. Short-read is 100% Illumina; long-read is 100% PacBio.
- **NovaSeq X replacement timing.** The expert said the NovaSeq X is "probably within two years" of its switchover date but did not remember the exact date. This answer was ambiguous. They said no new sequencer purchases are planned.

### Why long-read has not displaced short-read (direct operational experience)

The expert gave a throughput comparison. A 20X long-read genome basically takes one sample per lane, so eight samples fit on a PacBio chip. By contrast, the lab runs 20-30 trios (child plus both parents), "close to 100 samples per Illumina flow cell." The expert said "The throughput is just not there for the PacBio yet," though long-read lets users "do more with the data."

A regulatory point adds to this. As a New York State lab, any assay must be state-validated. The lab has not validated a long-read genome test because it "doesn't make sense from a cost-benefit standpoint" given the throughput gap. The expert does not see a meaningful shift in the next 12 months, and does not see long-read replacing short-read genomes as a standard test until it becomes more financially feasible. The expert expects PacBio and other long-read platforms to become more common if throughput rises and prices fall.

## Volume trends (the numbers)

The table below summarizes the expert's volume estimates. They are approximations, and the expert described them as such.

| Comparison | Expert's estimate | Context |
|---|---|---|
| Q3 2026 vs Q3 2025 | About 10% higher, "maybe a little bit more," in the 10-15% range | 2025 was a weak year |
| 2026 vs 2024 | About 5-10% higher | The expert called 2024 the cleaner baseline |
| Full-year 2026 vs 2025 | On pace for about 20% higher | Pace of output |
| Full-year 2026 vs 2024 | About 5% higher | Smaller gain than vs 2025 |
| 2027 vs 2026 | "At worst... flat," possibly "a little bit" up | No forecast given |

- **Why 2025 was weak.** Unexpected federal budget cuts, grant cancellations and funding reductions reduced the research samples sent to the lab (some cases are on research protocols), and disrupted general access to clinical care. The expert's framing is that 2024 was at a normal level, 2025 dipped, and 2026 recovered and added a couple of percentage points.
- **Versus expectations.** Q3 2026 output was "about meeting expectations, maybe exceeding slightly."
- **Outlook sentiment.** Q3 did not make the expert more optimistic or pessimistic. They believe reimbursement rates are slightly higher because the lab has been working with insurers, but said they lack the numbers.
- **2027.** The expert cannot forecast because some research protocols are ending and new ones start next year, but expects no significant change.

## Competitive landscape

### Illumina's position

The expert stated: "100% of our data is generated on Illumina short reads." Vendor share was stable in Q3 2026.

### Ultima Genomics (direct evaluation; rejected for clinical use)

The lab tested Ultima and found it unsuited to clinical testing. The expert's reason: Ultima's chemistry struggles with homopolymer tracts (runs of the same DNA base repeated). Ultima has identified these regions and carved out, in the expert's words, "basically 10% of the genome" that it admits cannot be sequenced well. The expert said "almost every clinically relevant gene has at least one region that cannot be assessed by Ultima." Because disease-causing genes cannot be fully covered, the lab decided not to use the platform.

### Oxford Nanopore (direct view; rejected for clinical use)

The expert said Oxford Nanopore has "admitted themselves" it is not ready for clinical testing because it updates firmware and hardware so often that stable builds do not stay stable long enough. Because the lab must keep assays validated with New York State (and other labs face California, Maryland and other states' requirements), it is "not practical to submit a validation update every three months or four months." The expert called PacBio "a much more stable system."

### Roche AXELIOS one (speculation; the expert is "not very familiar")

- **Adoption.** The lab has not adopted it and has not tested Roche. The expert said switching entirely to a new platform to replace Illumina "is quite a tall task" and not foreseeable soon. It would take "a significant difference in price, accuracy, efficiency," because all of the lab's pipelines and infrastructure are built on an "Illumina backbone."
- **Threat view.** The expert thinks Roche is a threat only "as sequencing needs change and sequencing technology changes." If Illumina stays in its current form (150 base paired-end reads, a 30X genome, or even 50X at the same cost), other platforms like Roche could gain a foothold in new labs that start up or as new tests looking for different kinds of genetic variation come online.
- **Switching cost.** The expert said the time and cost of validating under CLIA is "not that much of a concern" because the lab validates new assays continuously. The real obstacle is that the lab would not run two platforms in parallel, so a competitor would need a guarantee that it can fully replace Illumina. The cost is switching "all of the infrastructure": sequencer, pipelines, analysis and so on.

## Illumina products and roadmap

- **NovaSeq X roadmap.** The interviewer said Illumina has committed to raising NovaSeq X flow cell output by up to 40% and speeding whole genome sequencing by about 30%. The expert said this "doesn't change anything": more throughput "will be useful" but "doesn't fundamentally change anything about how we operate."
- **TruPath Genome.** The interviewer said Illumina launched it in February 2026 at a list price of about $395 per sample, removing library preparation (the step that readies DNA for sequencing) from the whole genome workflow. The expert said the lab is evaluating it but has run no clinical samples and is deciding whether to build a validation package for a TruPath-based test. The appeal is shared reagent and sequencing cost on the same machine, which are "very tangible benefits." The expert cannot judge until the final assay data are in.
- **SomaLogic acquisition.** The interviewer said Illumina closed the SomaLogic deal in January 2026. The expert said it is not relevant to their work and did not shift work to Illumina.

## Instruments, capital spending and vendor terms

- No plans to buy new sequencers in the next 12 months. No acceleration, delay or cancellation of instrument plans in Q3 2026.
- Sequencer capital spending in 2026 will be lower than 2025, because the PacBio system was bought in 2025 and no major system has been purchased this year. The gap equals the PacBio system's cost, which the expert did not know.
- Discounts, incentives and placement terms from Illumina and PacBio in Q3 2026 "remained the same" versus Q2 2026 (expert's belief).

## Consumables, pricing, inventory and support

- **Consumables (the reagent kits needed for each run).** The expert did not know negotiated prices with Illumina, only that a negotiated rate exists. Two research projects that began in spring 2026 have reagents supplied by Illumina at no cost, which the lab did not have last year. The expert agreed that this likely makes out-of-pocket consumable spending lower or flat despite higher volume.
- **Price changes.** The expert's understanding is that comparable Illumina and PacBio consumable prices are higher in 2026 than in 2025, but the expert does not do budgeting and gave no figure.
- **Terms.** Discounts, incentives and reagent commitment terms were unchanged in Q3 versus Q2 (expert's belief).
- **Inventory and lead times.** Inventory is "sufficient." No change in consumable lead times in Q3.
- **Support.** The expert is "fairly satisfied" with Illumina and PacBio, with no major issues. The lab needed no vendor support in Q3 2026.

## PacBio share gain (forward-looking, direct plan)

The expert expects PacBio to gain share and Illumina to lose share over the next 12 months. The reason is that the lab is validating a PacBio assay for carrier screening (testing healthy people for genes they might pass on) of genes well suited to long-read. The size of the shift is "to be determined" because it depends on insurance reimbursement, and the lab has never performed carrier screening, so it does not know what reimbursement will look like. The lab also plans to consider PacBio long-read genomes as a specialty test for specific patient or customer needs, not as a core test.

## Emerging technologies and longer-term views (expert opinion, not experience)

- **New platforms.** The expert has seen no specific new platforms to flag.
- **RNA and methylation.** The expert thinks RNA sequencing (on short- or long-read) and methylation-sensitive sequencing (detecting chemical tags on DNA that influence gene activity) "will become much more important in the very near future." This is mostly a library and sample prep issue, but the expert would watch sequencing volume. They are less focused on bisulfite-based methods and more on direct methylation detection by Oxford Nanopore and PacBio. Improving accuracy and confidence in that data across the field will be important if more clinical labs adopt it.
- **Carrier and newborn screening.** The expert predicts "massive increases in uptake" in the next few years. Some pilot programs have run whole genome sequencing and reported newborn screening results from it. Screening needs differ from diagnostic needs: diagnostic tests use about a 30X genome today, possibly moving to 50X in the near future if pricing allows, while screening could get by with a 10X-15X genome. Genome platforms are becoming more cost efficient for screening. Some large commercial labs are already shifting to win newborn screening business, since screening every newborn in a state is large. The expert expects this to shape the sequencing landscape over about five years, calling it "the next big market shift."
- **Long-read long term.** The expert expects long-read to grow as prices fall. Short-read cannot resolve some genome segments, while long-read can resolve the entire genome and certain structural variants (large rearrangements of DNA). With short-read, data are mapped onto a generic reference genome; long-read could build an individual's own map, yielding a "much more personalized genome product." This would require long-read pricing to come down to compete with short-read genomes.

## Interviewer-supplied context (not expert statements)

- Illumina's committed NovaSeq X flow cell output increase of up to 40% and whole genome speed-up of about 30%.
- TruPath Genome launch in February 2026 at about $395 list price per sample.
- Illumina's closing of the SomaLogic acquisition in January 2026.
- Roche AXELIOS launched as a research-use-only product, so clinical use would require CLIA validation.
- The 400-500 terabase estimate for the lab's annual output.

## Key takeaways for Illumina

- This customer shows strong lock-in: 100% Illumina short-read, with switching framed as full infrastructure replacement rather than a validation cost.
- Demand is recovering (about 10%+ year over year in Q3 2026, about 20% on a full-year pace against a depressed 2025) but is limited by reimbursement and by scarce licensed report signers, not by sequencing technology.
- Competitive erosion for this lab is limited to PacBio carrier screening, with size unknown.
- Illumina-funded research reagents reduce this lab's out-of-pocket consumable spending.
- TruPath is under evaluation only; the NovaSeq X roadmap changes nothing for this lab.
