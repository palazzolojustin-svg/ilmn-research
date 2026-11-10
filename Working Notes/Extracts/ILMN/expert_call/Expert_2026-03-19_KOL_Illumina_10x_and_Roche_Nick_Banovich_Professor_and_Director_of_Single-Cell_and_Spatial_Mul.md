# Guidepoint expert call with TGen's Nick Banovich on NIH funding, single-cell and spatial platforms, Roche Axelios, Element AVITI24 and Microsoft GigaTIME (Mar 2026)

*Source file: `Working Notes/Sources/ILMN/expert_call/Expert_2026-03-19_KOL_Illumina_10x_and_Roche_Nick_Banovich_Professor_and_Director_of_Single-Cell_and_Spatial_Mul.md` · Date: 2026-03-19 · Guidepoint expert network; moderator Andrew Carmen; expert Dr. Nicholas Banovich, Professor and Director of the Center for Single-Cell and Spatial Multiomics, TGen (City of Hope) · expert call*

**Summary.** An academic core-lab director and heavy 10x Genomics user explains that NIH grant success rates fell to 13% in 2025 and are likely to stay there in 2026, and that his lab has shifted spending from single-cell (about $50,000) to spatial (about $500,000) consumables. He sees Illumina's new spatial platform as promising but limited to fresh frozen tissue, and says Illumina's lower NovaSeq X flow-cell pricing makes him wait rather than buy a Roche Axelios or Element AVITI. He regards Roche's simplex mode (about $0.06 per million reads) as potentially transformative for very large single-cell experiments, but found Roche's workflow too slow for rapid clinical genomes, and he thinks Microsoft's GigaTIME is a net positive for spatial companies because AI models need much more measured data.

# Expert call notes: Nick Banovich (TGen), 19 March 2026

## Expert background and basis of views

- **Who:** Dr. Nicholas Banovich is Professor in the Integrated Cancer Genomics Division and Director of the Center for Single-Cell and Spatial Multiomics at TGen, the Translational Genomics Research Institute. TGen is a nonprofit research institute that is part of the City of Hope Medical Center (based in California). [Expert: Banovich, Mar 2026]
- **New role:** He has just taken on administrative duties as TGen's vice president for scientific development. He also runs his own research lab focused on pulmonary fibrosis (a non-cancerous lung disease), using single-cell, spatial and other "omics" methods (measurements of molecules across the whole cell or genome) to understand disease biology and find new treatments.
- **Relationship to Illumina and peers:** He is a customer and core-facility director, not a former employee. He buys from 10x Genomics, Illumina (sequencing), Element, Vizgen and others. He also sits on NIH study sections (panels of scientists who review grants). TGen runs a CLIA lab (a lab certified for clinical testing) doing rapid whole-genome tests for AML (acute myeloid leukemia) and multiple myeloma.
- **Recency:** Direct, current experience. He spoke with the same network a year earlier (about 2025) on NIH funding. He attended AGBT (the annual genomics technology conference) in early 2026.
- **Direct experience vs. speculation:** NIH funding, his lab's spend, Xenium, Visium HD, the Illumina spatial demo (presented by him at AGBT 2025) and his current NovaSeq X workflow are first-hand. Views on Roche pricing, Singular, Stellaromics, Element's in situ work and GigaTIME are based on AGBT presentations, publications and back-of-envelope math, and he flags several open questions.
- **Format note:** Guidepoint's standard compliance statement was read at the start (no commentary on stock prices or non-public information); the disclaimer at the end is boilerplate and omitted.

## NIH funding environment

### How the grant system works (expert's explanation)

A researcher writes a proposal, which goes to a study section. The study section scores grants and discusses roughly the top 50%. Each grant gets an aggregate score and a percentile rank within its study section. A second review, the council review, decides which grants are funded, historically by percentile. After approval the researcher receives an official notice of award. The cycle runs three times per year (February, June, October). A grant submitted in February is reviewed in June, goes to council in October, and typically gets its notice of funding between December and February, so about a year elapses from submission to funding.

### Success rates

The standard large grant mechanism is the R01 (typically five years of funding, paid one year at a time). Its success rate, per the expert [Expert, Mar 2026]:

| Year | R01 success rate |
|---|---|
| 2023 | 21% |
| 2024 | 18% |
| 2025 | 13% |

- **Cause of the 2025 drop:** Partly last year's turmoil, and partly heavier use of "multiyear funding." Under it the NIH records all five years of a grant's cost against one fiscal year. His illustration: with $5 million of appropriations, the NIH could fund five grants at $1 million a year, or one grant at $5 million a year. So it effectively funds five years of one grant instead of five one-year projects, which lowers the number of grants awarded.
- **2026 outlook:** There was a push to expand multiyear funding this year, but the budget bill restricted it to FY25 levels. He therefore expects 2026 success rates similar to 2025 (about 13%). He says that is very tough: "your grant has to score near perfect" to be funded.
- **Is it an accounting trick?** Asked by the moderator, he agreed: "It's fully an accounting trick. I don't see how it sort of helps them at all." Over a five-year period it would normalize as old year-by-year grants finish, but in the first two years of a full shift success rates would be "abysmal." Multiyear awards also do not let a researcher spend freely, as there appear to be guardrails on annual spend.

### Cash flow and award timing

- Money has flowed fairly consistently since about June 2025 for grants that already had notices of award.
- The bigger 2026 problem is that notices of award for new grants have been very slow, partly due to the government shutdown at the start of the fiscal year (which starts October 1) and partly because OMB (the White House budget office) had not released full funds to the NIH. He saw that morning (19 Mar 2026) that OMB had released the full funds, so awards may tick up.
- **New R01 awards since 1 October (data he pulled the morning of the call):** 496 so far in FY26, versus 1,099 over the comparable period last year. (He first phrased it as "400 this year" but gave 496 as the figure.)

### Effect on his lab versus the field

- His lab is an outlier: by luck it landed three fairly large NIH grants at the end of FY24, so it had funds in hand through the uncertainty, and its spending increased.
- For the field overall, he believes the uncertainty (lower success rates, harder money, longer waits for awards) has "really decreased the spend on consumables" (the reagent kits needed for each experiment). This is his opinion based on field observation, not measured data.

## Spending mix: single-cell versus spatial

- **His lab's 2025 consumable spend:** about $50,000 on single-cell consumables (the lowest ever, after a steady decline) versus about $500,000 on spatial consumables (a big increase). [Expert, Mar 2026]
- **Why single-cell is declining for his type of user:** He describes two groups. (1) "Tissue cell atlasing" users, like him, who profile primary patient tissue to find cellular and molecular changes in disease. For them spatial "offers such a tremendous advantage over single-cell," especially once single-cell insights already exist, so moving work to spatial "makes a ton of sense." (2) "Perturbation assay" users running large CRISPR or drug screens with a single-cell readout. He thinks this market is growing, and that much of it sits inside pharmaceutical companies, which keep work quiet until a project ends, so academics see less of it.
- **Platform mix in his lab:** Single-cell is still 100% 10x Genomics (never moved to other single-cell platforms). Spatial is primarily 10x, almost all Xenium: by budget and samples, about 90% Xenium and 10% Visium HD. TGen also owns a Vizgen MERSCOPE Ultra (barely used) and an Element AVITI24 (used for development work on in-tissue spatial with Element, which has presented on it at recent conferences).

## AGBT 2026 observations

- The single-cell and spatial side was a year of "platform maturation" with fewer new announcements and new companies than in past years. He suggests the field is stabilizing and that companies on the market today may be the ones with longevity.
- **Stellaromics:** Last year it only discussed the concept; this year it coupled the talk with its commercial release.
- **Illumina:** Gave updates on its spatial platform (demoed at AGBT 2025) but "nothing new."
- **10x Genomics:** No significant new announcements at AGBT.

## Single-cell competition

- **Parse Biosciences:** Appeals to the perturbation-assay group because combinatorial barcoding (labeling cells with unique combinations of barcodes so reads can be traced to cells) is needed to bring cost down for experiments of 100 million to a billion cells. This ties to "virtual cell" models: efforts to build AI/LLM-style models that learn the "language of biology" from huge perturbation data sets and predict what a perturbation would do.
- **10x Flex Apex:** Just released. His lab has tinkered with it and it "looks good," but they have not run it at scale. It pre-barcodes cells so that several cells share a droplet yet reads can still be traced back; he describes it as halfway between 10x's historical approach and the split-pool approach of Scale (which 10x acquired, per his remark) or Parse (cells put in wells at low concentration, barcoded, split, and pooled again).
- He says Parse and Flex Apex are the two technologies he would look at for big perturbation experiments.
- **Illumina PIPseq:** He has not seen compelling data that it is a contender here. Illumina had "one line" in its AGBT presentation saying it suits large CRISPR screens, but he does not see how that works without a combinatorial barcoding step, which PIPseq lacked. It "would have to have been a big update to the chemistry." He says some level of combinatorial barcoding is needed for massive-scale experiments.

## Spatial platforms

He divides spatial into two buckets and notes that for all platforms today, "you're either getting breadth or you're getting depth."

### Sequencing-based spatial (breadth, whole transcriptome)

Includes Visium HD, the Illumina spatial platform and Stereo-seq. RNA is moved from tissue onto a chip and sequenced.

- **Visium HD (10x):** "The product that I've probably been the most disappointed with" in the spatial portfolio. Sensitivity is too low; it gives full transcriptome coverage but "really, really low complexity data." TGen has stopped offering it as a service unless users strongly want it, because results were not consistent.
- **Illumina spatial platform:** He sees a lot of room for improvement in this bucket and says Illumina "could really capitalize on the market if they deliver a high-quality product." When he tested and presented it in 2025, it showed a significant sensitivity increase over Visium HD, and it has a much larger capture area than Visium HD. Colleagues who have used it more since AGBT 2025 are "very excited about the promise." He expects it to deliver an attractive alternative if Illumina operationalizes and prices it well. Key limitation: at launch it is planned only for fresh frozen tissue, whereas FFPE tissue (formalin-fixed, paraffin-embedded, the standard preserved clinical form) is "the vast bulk of biosamples in the world." For it to take hold, Illumina must move it to FFPE.
- **Element (in situ sequencing):** Element is trying to bring the sequencing reaction to RNA molecules inside the tissue (in situ, "in C2" in the transcript) while still doing whole transcriptome. This is why TGen bought the AVITI24. It is not commercially available and still in development, but it could bridge the sequencing-based and imaging-based buckets.

### Imaging-based spatial (depth, smaller gene panels, high sensitivity)

Includes Xenium (10x), CosMx (Bruker/NanoString), Singular, and Element to a degree. He personally prefers imaging approaches because seeing where molecules sit in the cell "builds a lot of confidence."

- **Xenium is his benchmark:** "It just works." Samples rarely fail, and the chemistry is very robust to degraded samples. His example is FFPE tissue that has sat in a paraffin block on a clinician's desk for five years, handled with bare hands, non-refrigerated. Any new technology is benchmarked against Xenium; its ease of use and data quality put it "far ahead of everybody else for us."
- **CosMx:** Has fans and a whole-transcriptome panel, but he says sensitivity is similarly low to Visium HD; most colleagues who have both systems still do the bulk of work on Xenium.
- **Singular:** Just starting to ship instruments (some at the Harvard spatial lab, which he saw designated a center of excellence for Singular the day before the call). It showed compelling AGBT data that the system runs consistently.
- **Capture area:** Singular and Element have much larger capture areas than other systems. If they mature, higher sample throughput will be necessary for the field, especially for clinical use; today's throughput "is just not sufficient" for clinical work.
- **Bottom line:** There is still competition and room for market share to be gained, but "I have not seen anything that has been of sufficient quality to push me off of the Xenium."

### Stellaromics Pyxa (3D spatial)

- As a researcher he finds 3D "incredibly exciting" and wants to generate data on it (his lab currently approximates 3D with serial sections and reconstruction). He told Stellaromics he would test it once boxes are available for shipping samples.
- As a core director he will not buy it: not enough users, and he thinks it is "quite expensive." It answers focused questions (for example five samples profiled very deeply), while his users ask about scaling, such as how to run a 400-patient cohort. A dedicated user base will exist, but "it's not the request that I'm getting from my core."

## Microsoft GigaTIME

- **What it is (expert's description):** An AI model trained on a roughly 40 million cell data set of histology images (stained tissue slides) matched with multiplexed immunofluorescence (protein imaging). Given only a histology image, it predicts the protein signal.
- **His assessment of the paper:** Average correlation across predicted proteins was only about 0.3, with some proteins predicted well and others poorly; representative images and aggregate statistics are "ok but not great." The paper focused on core cell-type markers and predictions were already not great; nuanced molecular markers are "a much, much tougher problem." The model was also applied to TCGA data.
- **Verdict:** Not "ready for prime time." He would not use such approaches for core research, "certainly not clinical decisions."
- **Is it a threat?** He sees it as a win for spatial companies: building accurate models requires an "immense amount more data," so the spatial companies benefit up front, and there will always be molecular information tissue imaging does not capture, a gap only direct measurement fills.
- **What would change his mind:** It depends on the ceiling. If ten times more data lifts average correlation from 0.3 to 0.4, it is not compelling; if from 0.3 to 0.8, "that becomes an approach that's really exciting." He expects users will still need to generate data for their own disease and tissue, since a generalizable model across all diseases and tissues will be very difficult.
- **Why cancer is hard (his reasoning):** On a UMAP plot (a 2D map where each dot is a cell), in diseases like pulmonary fibrosis, Alzheimer's or heart disease, each cell-type cluster contains an even mix of patients. In cancer, each patient forms their own cluster, so the molecular signature is "almost entirely unique" per patient even when histology looks similar. Histology alone may not capture that, because it is unclear that molecular changes map to histological changes.

## Sequencing: Roche Axelios, Element AVITI, Illumina NovaSeq X

### Context

He calls it "a crazy month and a half in the sequencing world": Element's AVITI (he was initially excited), then Illumina's new flow cells with lower pricing, then Roche's platform announcement (Axelios, based on the "Xpandomer" chemistry he references). He has had about a month to digest them.

### Roche Axelios

- **Clinical rapid genome: disappointing.** Before AGBT he was most excited about Roche as a clinical platform for TGen's rapid whole-genome testing. A Roche presenter who was operationalizing exactly that showed a workflow timeline that was actually slower than TGen's current NovaSeq X workflow. Although the sequencing itself is very fast, the Xpandomer step is slow with many steps and overnight incubations. It "kind of came off the table" for him for this use.
- **Simplex vs. duplex reads:** Roche offers duplex and simplex reads. Simplex reads are lower quality but fine for count-based applications like single-cell and spatial.
- **His back-of-envelope cost math:**

| Item | Cost |
|---|---|
| Current NovaSeq X 25B flow cell | about $0.40 to $0.60 per million reads |
| Roche simplex mode | about $0.06 per million reads (nearly an order of magnitude cheaper) |

- **Per-cell impact:** For huge single-cell experiments, he estimates total cost per cell could fall from about $0.30 to about $0.08-$0.09. Later he framed it as sequencing being about $0.20 of the $0.30 per cell today, falling to about $0.02 per cell. Over a billion cells that is "a huge difference in cost."
- **Open question:** It is unclear what throughput is needed to reach that pricing. Details from Roche still need to come out.
- **Point of care:** It could be compelling as an in-hospital whole-genome system. He understands the sensor can be reused for 20 runs and lasts about three months; if only 20 runs in three months are needed to hit Roche's quoted genome price, it could be compelling for diagnostics. His key test is whether it is flexible enough to give cheap genomes "without having to do the throughput of a NovaSeq X."
- **Who benefits most (his two cases):** (1) Organizations that bring whole-genome diagnostics in-house and capture the reimbursements rather than sending samples to a CRO or Tempus. (2) Groups running huge counting experiments. He notes groups in pharma, Parse's Tahoe data set of 100 million cells (announced at AGBT 2025), and companies thinking about virtual-cell models with 500 million plus cells; he does not know how many are doing billion-cell work.

### Illumina's response and TGen's purchase decision

- Illumina announced new flow cells with dropped pricing (referred to by the moderator and expert as a 35B flow cell, the expert also citing "13 billion read flow cells with lower pricing" on NovaSeq X, and TruPath mentioned by the moderator). [Transcript terms as spoken; the exact products are not fully clear from the call.]
- TGen's constraint: a mixed user base (whole genomes, single-cell and spatial, exomes, epigenetics) with different throughput needs. The 25B flow cell gives the lowest pricing, but non-genome users wait longer because enough work must accumulate to fill a lane.
- **Element AVITI (he writes "VITARI"):** A 10 billion read run split across 12 lanes would give moderate-output runs at a cheaper price than Illumina's current offering, which would address this. But lower-priced 13B flow cells on the NovaSeq X converge on a similar enough price that it raises the question of whether another $600,000-$700,000 instrument is worth it.
- **Decision:** TGen was considering buying a new instrument at the start of the calendar and fiscal year, but Illumina's response means "maybe wait and see rather than jump." Illumina is "accomplishing what they need to," i.e., reducing prices so TGen gets flexible run configurations without new capital equipment, in a period when capital equipment is harder to get. The moderator summarized that Illumina is making it unattractive to take the risk of a new system; the expert agreed: "Yes, exactly."
- **Break-even logic:** If the price difference is only about $20 per genome, one must ask how many genomes would need to be run to justify buying new capital equipment.
- His overall view: there are now good options that did not exist a year ago, but he does not see anyone offering enough to make TGen stop using its NovaSeq X and buy a new system.

## Closing outlook (expert)

- Spatial platforms continue to mature and become more robust; users have moved from "kick the tires" exploration to full-scale data production, and he expects more large cohort-style projects.
- On sequencing, over the next 12 months the AVITI and Roche systems will be in market and Illumina's pricing response will be visible, giving the information needed to judge whether these systems offer significantly different capabilities.

## Summary comparison from the call's AI-generated overview

The Guidepoint summary table (not the expert's words) characterized: 10x as robust but with limited recent innovation and strong market position; Illumina as having potential for a high-quality, large-capture-area spatial platform but limited to fresh frozen tissue; Roche as fast sequencing with potential cost savings but a slower-than-expected clinical workflow; Element as innovative in situ but not yet commercially available.
