# Expert call – Single-cell genomics specialist at Brigham and Women's Hospital on Roche's AXELIOS sequencer versus Illumina, switching costs and adoption timeline

*Source file: `Working Notes/Sources/ILMN/expert_call/Expert_Tegus_Single_Cell_Genomic_Technology_Specialist_at_Brigham_and_Womens_Hospital_Illumina_Inc.md` · Date: 2026-10-10 · Tegus expert interview; Single-Cell Genomic Technology Specialist at Brigham and Women's Hospital (Harvard-affiliated); interviewer is an unnamed Tegus client. The transcript carries no date, so the date given is a best estimate (the folder's rules are dated 2026-10-10). · expert call*

**Summary.** A core-facility (shared-service lab) specialist who runs libraries on Illumina NovaSeq X Plus describes Roche's new AXELIOS sequencer as faster, cheaper, more flexible and easier to run. They have analysed AXELIOS-sequenced single-cell data and saw no substantial quality difference from Illumina. They argue Illumina's ecosystem and researcher conservatism create high switching costs, that Roche's real wins will come from new, large-scale clinical, biopharma and biotech projects, and that building trust will take roughly 5 years (2-3 years for first publications). They expect a more fragmented market and lower sequencing prices, and that an Illumina price cut to match Roche could push Roche's timeline out to about 5-7 years.

# Expert call: Roche AXELIOS versus Illumina, seen from a hospital sequencing core

## Expert background and how much weight to give it

**Role and employer.** The expert is a Single-Cell Genomic Technology Specialist at a cellular profiling core at Brigham and Women's Hospital, a Harvard-affiliated hospital. A "core" is a shared-service lab that sequences samples for many outside users in academia, biotech and biopharma. The expert has been in the core role for around five years [Expert: single-cell specialist, Brigham and Women's, undated]. Their duties, per the Tegus profile, include helping bring single-cell sequencing and genomic solutions to communities, advising labs on which assays to use, running quality checks before experiments, and using 10x Genomics technology to produce preliminary analysis of single-cell data before delivery.

**Relationship to Illumina and peers.** The expert is a customer and user, not a former employee of any vendor.
- *Illumina:* Hands-on and theoretical experience. At the core, single-cell and spatial libraries are sequenced on Illumina platforms, using the larger NovaSeq X Plus (a high-capacity Illumina sequencer), which "gives you better pricing."
- *Oxford Nanopore:* Hands-on experience with the MinION (a small portable nanopore sequencer) in previous labs, including library analysis, troubleshooting and training by Oxford Nanopore staff.
- *PacBio:* Extensive use in another lab for long-read sequencing of microbial genomes, especially plasmids (small circular DNA molecules), because long reads were good enough to give the whole plasmid structure.
- *Roche AXELIOS:* **No hands-on experience.** The expert knows the theory, advantages and disadvantages, sees Roche advertising AXELIOS at nearly every conference and biotech meeting, and **has analysed data sequenced on AXELIOS** (single-cell libraries). Anything about operating the machine is therefore second-hand or based on Roche's advertising ("as it is advertised").

**Reading guide.** Observations on Illumina workflows, turnaround, batching, researcher behaviour and the 10x Genomics marketing playbook come from direct experience. AXELIOS claims on speed, flow cell sizes, price and ease of use come from Roche's marketing and the expert's assumptions. The adoption odds, the 5-10 year timeline and the market-fragmentation view are the expert's opinions and rough estimates.

## Overall view

The expert is "optimistic" about AXELIOS because it adds another major player, which is competitive and should push sequencing prices down. They think Roche will first be a "second platform" in cores and labs, and later become a significant player in large-scale clinical, biopharma and biotech work. They expect the market to become more fragmented over roughly the next five years and doubt Illumina will remain the dominant player [Expert, undated].

## Roche AXELIOS: advantages (as advertised, plus the expert's analysis of data)

- **Speed and real-time data.** Runs take only a few hours, data is generated in real time, and turnaround is "a lot shorter." The expert says users can get data back "the same day or next day," and later that Roche says data can arrive in one day. Fast data is "a major concern" for core users, labs, biotech and biopharma.
- **Scalability.** The expert is unsure of AXELIOS's biggest flow cell (the consumable slide where sequencing happens) but thinks it is comparable to Illumina, perhaps 25 billion reads or more in one run. They also say four different experiments can run in parallel, which Illumina cannot do. This appeals to large diagnostics and large biopharma/biotech projects.
- **Lower cost.** Better cost per sample and per gigabyte of data. Roche is "offering more competitive prices compared to Illumina in the market." Cost matters especially for pilot studies, where people look for the lowest price when starting a project.
- **Flexibility of flow cell size.** Per the expert, Roche has multiple flow cell sizes, so it can run from one library to 300 libraries and keep its cost advantage over Illumina. The expert says they do not know the smallest flow cell size, and the interviewer's framing (a roughly $100-$200 genome) was the interviewer's assumption, not a number the expert supplied.
- **Ease of use and maintenance.** Only a few colour-coded reagents that load easily. One person can run the machine, download data and generate FASTQs (the standard text files of sequencing reads) on a laptop and deliver them. One or two people are enough. The machine "is not huge," is easy to clean and maintain, and Roche offers customer support.

## Roche AXELIOS: disadvantages and hurdles

- **It is new.** At this price point people are skeptical: will core users trust it, or will they ask for Illumina instead? "People need to find confidence in this platform." The expert says this is "not impossible," it just needs time and cross-platform comparison data.
- **Lack of public comparison data.** The expert could not find freely available data sequencing the same sample on multiple platforms. They especially want to verify Roche's advertised low background noise. Such data would assure researchers they are "not compromising on the quality."
- **Entrenched Illumina ecosystem** (see below). "It is hard to break that ecosystem."
- **Chemistry-driven artifacts** (see below), which matter for long projects.

## Data quality: the expert's hands-on comparison

The expert analysed single-cell libraries sequenced on AXELIOS and said it "was great," with no major or substantial differences from Illumina. The quality checks they use, and what they saw:

| Metric (plain-English meaning) | What the expert found on AXELIOS vs Illumina |
|---|---|
| Sequencing depth: reads per cell. If you request 30,000 reads per cell, you expect roughly 20,000-25,000 back; less raises questions about configuration. | Very similar |
| Sequencing saturation: how fully the sample's diversity has been captured. Depends on sample type (uniform cell culture saturates faster than multi-cell-type tissue). | Very similar for the same tissue on Roche and Illumina |
| Number of genes detected | Very similar, so "you are not losing anything" |
| Error rate: how often a base is misread, e.g. a T read as a C | Approximately the same, 0.1% (1 in 1,000), at Q30 (a standard accuracy score) for both |

Caveat: this is a small number of datasets in the expert's hands, not a formal published comparison, and the expert says new users still need a proper same-sample comparison.

## Why cross-platform comparability matters (reproducibility and artifacts)

**The expert's argument.** Researchers need reproducibility. If an experiment ran on Illumina five years ago and new data come from Roche today, the researcher must know both are correct and similar. Otherwise they cannot tell whether a difference is technology-related or truly biological.

**Examples given:**
- Single-cell data where Smart-seq (a different single-cell method) cells formed their own cluster separate from Illumina-based cells. The paper's authors interpreted it as biology, but the expert says it was a platform difference.
- Bulk RNA sequencing where re-sequencing the same libraries on Roche suddenly shows overexpression of certain genes that have no biological meaning.
- Whole-exome sequencing (DNA sequencing of the protein-coding regions) of 1,000 samples, starting on Illumina and switching to Roche, then merging with public datasets and clustering by variants (SNPs, single-letter DNA differences). Patients may cluster by sequencing platform rather than biology, introducing artifacts.

**Why it matters for timelines.** Academic studies often run four to five years; biopharma drug studies run five to 10 years. Data at different time points must stay consistent.

**Cause and severity.** Each method has different chemistry: the expert describes Roche's as "SBX" ("kind of long polymeric"), Illumina's as SBS (sequencing by synthesis, "a kind of amplification"), Nanopore using nanopore channels, and Thermo Fisher using hydrogen ion detection. Each introduces some artifacts. "It is not critical. It is just something that people have to be aware of." Changing chemistry brings some batch effect (systematic technical shift), which every researcher accepts. It does **not** mean old samples must be re-sequenced: "There's nothing to be resequenced." Switching is "kind of switching from Windows to Mac."

**Comparability guidance.** Compare short-read methods: Illumina and Thermo Fisher's Ion Torrent are the closest to Roche. The expert does not recommend mixing long-read (PacBio, Oxford Nanopore) with Roche in the same project: "too many artifacts."

## Illumina's ecosystem and switching costs

The expert calls the ecosystem "the biggest competitive advantage of Illumina." It includes:
- machine installation, reagents and flow cells bought as one system;
- customer support and well-established, easy library preparation workflows with solutions to nearly any issue, thanks to many years of use;
- bioinformatic support from Illumina after data generation;
- compatibility with other applications, e.g. 10x Genomics single-cell sequencing and Takara's Trekker barcodes (a spatial transcriptomics technology);
- a large user community.

To switch, labs must rebuild this gradually: the machine, trained personnel on a new protocol, troubleshooting, Roche customer support (including when "the machine breaks in the middle of the night"), and a larger community. "It will not happen overnight." Illumina's long history also creates trust: "We sequenced it on Illumina, meaning I can trust this data."

**Expert's estimate of the timeline.** Roche "needs some time to build this ecosystem. It could take five years. It could take 10 years." Not within one or two years of launch. The expert stresses five years is "just a rough number."

**What could shorten it:**
- a well-established, error-minimising workflow;
- publications, abstracts and available multi-platform comparisons, plus greater presence in the field;
- incentives: companies sometimes offer promotions such as 50% off reagents for a new project, which makes people willing to try; if they like it they tend to stay;
- entering through large hospitals and clinical labs. If a hospital's pathology lab uses Roche, it creates confidence and a presence; one machine would likely lead to another.

**What could lengthen it:** targeting smaller labs or individuals instead of large clinical settings. Also an Illumina price cut (below).

## Who is likely to switch (expert's estimates)

**Switching behaviour of existing projects.** Someone one or two years into a five-year project has a low likelihood of switching. The expert has seen a "conserved mindset" throughout their career: "If this technology and this data is working for me... I don't want to switch. I will pay more, but I will not switch."

**New projects and new labs.** A biotech building a new sequencing lab and buying new machines would find Roche "great": cheaper, faster, starting fresh.

The expert rated likelihood of using Roche (own scales, out of five):

| Customer type | Expert's likelihood of using Roche | Notes |
|---|---|---|
| Large biotech / biopharma | 4-5 out of 5 | Highly likely; they can build their own ecosystem and are not tied to other labs |
| Smaller academic labs (PI-led) | 2-3 out of 5 | New pilot project may go to Roche; established projects stay conservative |

The interviewer summarised this as roughly 50/50 for a new project and about 1 out of 5 for an existing project, and the expert agreed ("Yes"). This summary was the interviewer's, endorsed by the expert.

**Why small labs are more conservative.** They resist anything needing new optimisation or methods. With a couple of grants the risk is high, and they do not want to put money into something new.

**Why big players are more willing.** They have larger budgets and are aware the market is changing. As an example, a large company working with the core invested about **$2 million** just to run quality checks on a large number of samples and compare QC results before committing a larger amount. They expect Illumina "will not probably be the major player anymore in the next five, 10 years."

**Role of cores.** Small researcher labs come to a core, which can offer both: "You have Illumina, you have Roche, you choose." Cores can offer Roche as a second platform. The expert assumes "a lot of people would say yes" to a faster, cheaper trial, while others who already sequenced everything on Illumina will decline.

## Where the expert sees Roche winning: large-scale clinical and commercial use

- **Large-scale clinical and commercial use.** If a hospital decides to do whole-genome sequencing for all incoming patients, speed, low cost and thousands of samples matter. The expert says the Brigham and Women's direction is to make sequencing available for all patients, similar to the UK, where every hospital patient reportedly has a full genome sequenced and stored. They say a similar trend is happening in the US, and Roche "could be a good player here." (Claims about the UK and US trend are the expert's characterisation.)
- **Single-cell demand eroding.** Single-cell sequencing has been a major service for the core, but the expert says it is "being replaced by spatial transcriptomics." Current spatial methods use fluorescent-encoded probes and "do not use sequencing," so they bypass it. That removes a customer segment from sequencers, leaving clinical samples in large numbers, where the expert sees more competition for Illumina and Roche as a "major player." (The expert's view; note also that they say 10x single-cell and Takara Trekker spatial are Illumina-compatible.)
- **High throughput, lower cost** drives demand for alternatives, including Roche.

The expert's closing summary: Roche's role is as a major contributor in clinical and biopharma/biotech, in large projects rather than small researcher projects.

## Turnaround time and batching

**Illumina experience at the core (direct experience).** The core batches libraries from different users to fill a flow cell, which takes "a couple of weeks." The sequencing turnaround is about another two weeks, so users wait at least four weeks. Downloading large data can take a week, then FASTQ generation and analysis. Total: **six to eight weeks** from library to analysable data, which academia accepts for grant preliminary data, paper revisions or new projects. If the flow cell is not full the wait is longer.

**Why batching happens.** Larger flow cells are cheaper per read: the expert says a 10-billion-read flow cell is more cost-effective than a 500-million-read one. The core batches to get better pricing.

**Where Roche saves time.** Not in data download or analysis (similar data volumes, online FASTQ platforms user-friendly for both). The saving comes from machine run time (Illumina "could be several days"), the ability to run four parallel runs, and the ability to skip batching because reagent costs are lower and flow cells come in multiple sizes. The expert estimates roughly **a week saved per run**. They agree with the interviewer that Illumina's headline run time might be 24 hours but real-world turnaround is about a week because of batching. Even a single library finishes faster on Roche. Smaller batches, e.g. 5-10 rather than 20-30, suffice to reach full cost efficiency (interviewer's framing, which the expert confirmed with "It is, yes"). The interviewer noted Illumina also has smaller flow cells but at a much higher per-genome cost.

**Importance of turnaround by customer type.** Time matters everywhere. The month-long wait in academia is accepted "just for now because everybody is following Illumina"; the first question users ask is the turnaround time. The expert ranks:

| Customer | Turnaround importance (expert's score) | Why |
|---|---|---|
| Clinical/pathology labs | 5/5 | Treatment decisions, e.g. a child with cancer; one or two days can be decisive, and some might run other assays or skip sequencing if too slow |
| Biotech/pharma | 4/5 | Major financial and trial-planning decisions depend on the data |
| Academic labs | 2-3/5 | Less pressure ("more chill"), can wait a couple of weeks, though still wanted for revisions and grants |

The expert says AXELIOS's major marketing advantage is turnaround time, and the second is lower cost.

## Building confidence: publications and the 10x Genomics example

- Cost of reagents is "a major driver" of whether Roche can compete. For now it is cheaper, which attracts trial. Speed is second. Confidence comes with time.
- Publications are of "major importance," especially because Roche competes with an established environment. Roche's website and LinkedIn posts look "great," but the expert asks "can I trust the data if it's not in a scientific abstract or paper?" and answers "Probably not." The scientific community needs well-cited publications.
- **10x Genomics as a model.** The expert says 10x leads in single-cell and spatial transcriptomics (the core uses many of its products), partly because of how it markets data: investing in projects that compare its products with others (e.g. against Smart-seq), publishing comparisons of 10 methods, and funding researchers to use its methods on clinical tissue and present at conferences. Each presentation naming 10x chemistry is indirect advertising.
- **Timing.** About two to three years might be enough for a couple of good publications to reach the scientific community. The interviewer suggested a critical-mass effect (one or two papers is not enough, but momentum builds), and the expert agreed.

## Price competition and Illumina's response

- The expert says Roche's presence "would drive the sequencing prices lower" and that Illumina may lower prices to compete with AXELIOS in the existing market.
- The interviewer asked if Illumina dropping to $100-$200 per genome would be enough. The expert: "it should be enough. If they just lower it a little bit... They don't have to really go down too low." If Illumina matches Roche, "it will be very hard for researchers to choose between Roche and Illumina," given Illumina's long market presence. (The $100-$200 figure was the interviewer's; the expert did not independently give a price.)
- Effect on Roche's timeline: it would be harder to build an ecosystem within five years; the expert estimates a push-out to **five to seven years**, because Roche would need to show why to switch if price is the same and turnaround only slightly faster, or if customer support is not "extensively better."
- Price is "a very big important component."
- Interviewer's closing summary, which the expert endorsed: prices go down, Illumina is not out of moves, but Roche is a viable competitor that could establish itself as a true contender over about five years, mainly for large organisations and new projects rather than individual researchers.

## Key quotes

- "I will pay more, but I will not switch." (on the researcher mindset)
- "It is hard to break that ecosystem." (on Illumina)
- "It could take five years. It could take 10 years." (on Roche building an ecosystem)
- "It's kind of switching from Windows to Mac." (on moving platforms)
- "Illumina will not probably be the major player anymore in the next five, 10 years." (on how large biopharma views the market)
- "Can I trust the data if it's not in a scientific abstract or paper or publication? Probably not." (on publication importance)

## Contradictions and caveats

- The expert has no hands-on AXELIOS experience; speed, flow cell size and price claims are Roche's marketing or assumptions, and the expert admits uncertainty about Roche's largest and smallest flow cell sizes.
- The "five years" timeline is described as a rough number and varies in the conversation: 5-10 years for a solid ecosystem, 2-3 years for first publications, 5-7 years if Illumina cuts prices.
- Small-lab willingness to try Roche is mixed: unlikely to switch existing projects, but open to trial for new pilots, especially via cores.
- The call is undated; the point of view is from a single academic-hospital core, so it may not represent clinical diagnostic or biopharma purchasing behaviour directly.
