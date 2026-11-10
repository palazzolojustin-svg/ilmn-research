# Channel check with a pharma genomics scientist (customer): ~50% sequencing growth in 2026, 100% Illumina short-read, Roche AXELIOS as a future threat

*Source file: `Working Notes/Sources/ILMN/expert_call/Expert_2026-10-18_Scientist_of_Genomics_at_Pharmaceutical_Company_Optimistic_About_Sequencing_Technology_Adv.md` · Date: 2026-10-18 · AlphaSense AI Channel Checks (AI interviewer); expert is a Senior Principal Scientist / Head of Genomics at a large pharmaceutical company; interview 2026-10-18, published 2026-10-21 · expert call*

**Summary.** A customer at a large pharma's internal research-use-only omics lab says their sequencing output rose about 50% in 2026, helped by perturb-seq adoption and a rebound from an unusually weak 2025. All short-read work runs on Illumina (NovaSeq X Plus), and an eight-year capital depreciation rule means they cannot realistically replace it before 2030. Roche's AXELIOS is seen as a serious future threat on cost per read, but is limited by capital budgets and the lab's own data infrastructure. The lab is exploring in-house long-read (PacBio or Oxford Nanopore) and expects only 10-20% output growth in 2027.

# Expert call: pharma genomics scientist on sequencing demand, platform choice and competition

## Expert background and how to weigh the evidence

- **Who:** The expert is a Scientist of Genomics at a large pharmaceutical company, described in the bio as Senior Principal Scientist and Head of Genomics, with visibility into sequencing consumables (the reagent kits needed for every run) and purchasing. [Expert: pharma head of genomics, customer, Oct 2026]
- **Relationship to Illumina:** Customer. The expert is not a former Illumina employee or competitor. The call was run by an AI interviewer (AlphaSense channel check) on 2026-10-18 and published 2026-10-21.
- **Lab:** An internal preclinical omics lab inside pharma research. It generates high-dimensional data (many measurements per sample) to support preclinical drug discovery, validation and mechanistic modeling. It is strictly research use only (not a clinical diagnostic lab). Funding is 100% internal biopharma money from the expert's own company, with no federal, institutional or philanthropic funding.
- **Recency and basis:** The expert speaks from direct, current experience about their own lab: Q3 2026 and full-year 2026. Statements about Roche AXELIOS's specs, Illumina's roadmap and other vendors' strategies are opinion or partial knowledge, and the expert flags this several times ("I believe," "if I'm not mistaken," "I don't know what they're working on"). This is one lab, not a market-wide sample.

## Scale and type of work

- The expert does not track gigabases (a unit of sequencing output). The primary data type is 10x Genomics single-cell data (measuring gene activity cell by cell). Experiments are typically 1 to 4 million cells, with four large experiments per year plus some smaller ones.
- The AI interviewer estimated that 20,000-30,000 reads per cell across 1 million cells would mean tens to hundreds of terabases per year. This was the interviewer's estimate, not the expert's figure.
- The lab is "so single-cell centric" that even a quick QC (quality control) sequencing run needs about one billion reads on a 4-8 million cell library prep.

## Demand drivers: tailwinds and headwinds

### Tailwind: perturb-seq
- The biggest recent positive for output is that a functional genomics team in the department standardized on perturb-seq (a method combining genetic perturbations such as CRISPR knockouts with single-cell readouts). This team previously used arrayed screens and more traditional readouts and moved to perturb-seq "this past year," working closely with the expert's lab. The expert says this "significantly increased our sequencing rate."
- Q3 2026 output also benefited from "a couple of extra development projects."
- The expert is slightly optimistic. Two large perturb-seq experiments are already scheduled for 2027.

### Potential headwind: Atera spatial system
- The lab is adopting the new Atera system (an in situ spatial platform; the expert refers to its whole-transcriptome readout). Currently, for each Xenium spatial experiment (10x Genomics' in situ platform), the lab runs a same-block single-cell FFPE-seq (single-cell sequencing from preserved tissue blocks).
- If Atera's whole-transcriptome readout proves sufficient, it could displace that FFPE-seq use. It could also displace the GeoMx digital spatial profiling whole-transcriptome readout, which also ends in sequencing. Atera would have to displace both for the volume impact to be meaningful.
- This is a bar yet to be cleared: the expert says it would take "at least a year of validation" before arguing for an abrupt pivot.
- Later, the expert again names Atera's whole-transcriptome capability as something that "might potentially cannibalize some of the short-read sequencing."

### Budget
- Q3 2026 funding levels were the same as before, but "this is the first year we went over budget." The cause was adding sequencing to functional genomics work on top of routine sequencing.

## Output trends

The table below summarizes the expert's reported and expected sequencing output.

| Period | Expert's statement | Reason |
|---|---|---|
| Q3 2026 vs expectations | "Exceeded my expectations" | Perturb-seq plus extra development projects |
| Q3 2026 vs Q3 2025 | About +50% | Q3 2025 was unusually low; mix of recovery to baseline and acceleration above it |
| Full-year 2026 vs 2025 | "50% basically holds" | Same drivers |
| 2027 vs 2026 | Modest increase, about 10-20% "at the most" | "Cruising altitude," no longer correcting a 2025 capacity reduction |

- **Why Q3 2025 was low:** Internal reorganizations, reprioritizations and "political ambiguity." The expert calls it an "idiosyncratic organizational situation," not a demand problem. The expert cautioned they did not want to give "the impression that that is this giant jump compared to baseline."
- **Consumables:** Q3 2026 consumables and reagent spending was also up about 50% over the weak 2025 comparison, and the increase was volume-driven (accelerated single-cell perturb-seq profiling). The expert was not watching price and does not know how much is inflation.

## Instrument fleet and short-read share

- **Fleet:** The workhorse is the NovaSeq X Plus (Illumina's high-throughput sequencer). The lab also has two legacy NovaSeq 6000s. It has moved almost exclusively to high throughput. It formerly had NextSeq 500s, MiSeq and MiniSeq, but dropped them because there was little demand for quick QC-style runs, smaller kits on current sequencers cover that, and single-cell volumes make small instruments unsuitable. The lab does no amplicon sequencing or other "modest sequencing loads," which "lost its justification."
- **Share:** Short-read is "100% Illumina," unchanged throughout Q3 2026. The lab has been in a technology access program with Element, but not for traditional short-read; it was looking at direct CT sequencing.
- **Next 12 months:** Illumina stays dominant "almost exclusively on the basis of depreciation of the X Plus."

### Why switching is hard
- The expert says established pipelines and workflows and capital depreciation make leaving Illumina challenging "even if there are very compelling metrics that alternatives can offer."
- The X Plus was bought around 2024 at close to seven figures. The company requires an eight-year depreciation cycle for significant investments, and the expert says it would have to be at least six years after purchase. Finance would not realistically accept a replacement until 2030.
- No short-read capex in 2025 or 2026. The last was the X Plus in 2024.
- No short-read replacement or upgrade is planned in the next 12 months. Other planned purchases are spatial (the Atera).

## Long-read

- **Current state:** Long-read (sequencing much longer DNA/RNA fragments) is currently outsourced. It covers two to three projects out of a normal 12, each with a handful (8-24) of long-read samples, versus 60-192 samples for a bulk RNA project. The interviewer characterized this as low single-digit percent of output at most (interviewer's inference).
- **Why demand is rising:** Historically requests were just counting genes, where short-read sufficed. Now several programs want isoform profiling (identifying the different versions of a gene's transcript), and the expert sees "a whole new avenue of target discovery within the isoform space." This makes the case for in-house long-read compelling for the first time.
- **Vendors:** The lab is engaging PacBio and Oxford Nanopore Technologies and would probably buy the highest-throughput offering. It will be "on the wish list in the next 12 months," and the decision depends on factors not yet visible. The expert describes capex cycles as "a mixture of very vague forecasting and improvisational purchases."
- **Choosing between them:** Still researching, with meetings planned. The expert has learned that some community prejudices about each company rest on "apples to oranges comparisons." The criterion will be "how many samples can I fit in a run that meet the minimum accuracy requirements."
- **Not a substitute for short-read:** Long-read is used for isoform ontology (cataloguing which isoforms exist), while short-read is still used for differential isoform splice-junction measurements. Each long-read sample may be paired with short-read, so short-read's percentage could fall while absolute short-read volume rises. The expert stressed this point.
- **Whole genome:** The lab would use long-read for whole genome only if it needed high fidelity in hard-to-sequence regions, which "hasn't come up as a requirement yet."

## Roche AXELIOS

- **Expert's view of the product (partly uncertain):** The expert finds the cost-per-run case "very compelling," notes it is compatible with 10x, and could help with more aggressive cell numbers. It looks cheaper and more accurate, and approaches Illumina's read counts ("about 40 billion reads, if I'm not mistaken").
- **Why it differs from past challengers:** Previously, rivals offered cheaper kits or better base-calling fidelity but could not match Illumina's brute read numbers. AXELIOS has "way cheaper cost per read" and comparable depth of read, so "that is a serious threat to Illumina as is."
- **Qualifiers:** The X Plus and AXELIOS are not the same generation. Illumina benefits from capex inertia. The expert sees AXELIOS as competing with whatever succeeds the X Plus around 2030. If Illumina diversifies and does not iterate on the X Plus, AXELIOS becomes a much more compelling next-generation short-read choice once capital is freed. If Illumina has a successor, the lab would compare it with AXELIOS in 2030. The expert says "I don't know what they're working on."
- **Obstacles to the lab adopting it:** (1) capex, and (2) the lab's pipeline for processing, ingesting and annotating data cannot yet absorb exponentially more single-cell data despite big AI initiatives and data lakes. "If we just blindly crank up the pressure on the pipeline, that's not necessarily going to be productive."

## Illumina roadmap and products

- **NovaSeq X improvements:** The interviewer said Illumina committed to raising NovaSeq X flow cell output by up to 40% and speeding whole genome sequencing by about 30%. The expert says speed is "fine," but cost per read is what matters because single-cell volumes keep growing. "That's the big argument in favor of AXELIOS." If several AXELIOS runs match the reads of one run on a newer X Plus chemistry, that is "a harder argument to make at the end of the decade."
- **TruPath Genome:** The interviewer said it launched in February 2026, removes library prep from whole genome workflows, and lists at about $395 per sample. The expert has not adopted it, did not know it was out, and has exactly one whole genome project this year (profiling mutated cell lines, where short-read is fine). The expert will look into it for that project. The lab orders from legacy lists unless the Illumina contact flags a newer kit.
- **SomaLogic acquisition (closed January 2026, per interviewer):** It has not caused the lab to shift work to Illumina. The lab uses Nomic Bio for secretome panels. The expert sees Illumina building a one-stop-shop ecosystem (gene, protein and neighborhood counting, including its Fluent acquisition and spatial solution, now secretome), which "makes sense on paper."
- **Cloud barrier:** Illumina pushes cloud-based solutions, which run "headlong into our IT security limitations." The lab has found no easy way to use vendor cloud solutions to centralize data because of hard negotiations with institutional IT security. "We're not allowed to use that."
- **Library prep:** The expert flags library-prep reduction, including Illumina's own efforts, as a compelling change for gene counting. Otherwise nothing is "fundamentally changing the act of gene counting," only shortcuts.

## Other vendors and emerging technology

- **Element AVITI:** The lab had earmarked it for optical pooled screening to support functional genomics. Element pivoted its chemistry from Teton to Cytos, disrupting the lab's technology access program. The expert is "seriously considering shelving it" and says it "left a bad taste in our mouth," adding "It's not their fault." The expert also says experience with AVITI means direct CT sequencing "may have some challenges."
- **Singular:** Not looked at deeply. The lab has some for spatial, but the expert thinks Singular is "going into very specific niches due to constraints on the flow cells."
- **Vendor pricing and support:** No sense of coupons or price arguments in Q3 2026, only performance literature. The expert is satisfied "across the board" with sales, technical and informatics support, with no major complaints and no outstanding standouts, and support was unchanged vs the prior quarter.

## Consumables, pricing and inventory

- The lab now buys larger bulk kits instead of smaller kits, which gives some per-sample savings through pricing scale. The expert had no clear view on like-for-like price inflation because kit composition differs year to year and 2025 is an awkward baseline. They could not say whether vendor discounts or reagent commitment terms changed.
- Inventory is "sufficient": some backup reagents, with large bulk kits ordered proactively once a big experiment is locked in. Lead times were unchanged as far as the expert knows.

## Longer-term view: clinical adoption

- The expert calls the clinical side "the big sleeping giant." Previously it was "a heavy uphill battle" to get clinical and development groups to run single-cell and spatial assays on patient samples, because clinicians wanted actionable biomarkers rather than a list of 27,000 genes.
- The expert has recently seen a cultural shift: development-side colleagues are expressing more interest in high-dimensional readouts, helped by AI training and reverse translation (using human data to inform preclinical work). If this becomes standardized, even for large-scale trials, it "would vastly accelerate the demand for gene counting in general."
- The expert's familiarity covers research, development, translation and diagnostics, not agriculture.

## Notable quotes
- "It was just the idiosyncratic organizational situation" on the weak Q3 2025 (paraphrase of the explanation given; the exact phrase appears in the transcript as shown).
- "We're at cruising altitude and not correcting a reduction in capacity from 2025" (on 2027 growth).
- "That is a serious threat to Illumina as is" (on AXELIOS, with caveats above).
- "The big sleeping giant is the clinical side."
