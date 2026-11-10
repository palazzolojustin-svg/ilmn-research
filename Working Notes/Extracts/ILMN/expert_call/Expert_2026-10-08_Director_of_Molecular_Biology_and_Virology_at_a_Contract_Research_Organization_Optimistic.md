# Channel check with a Director of Molecular Biology and Virology at a clinical/CRO sequencing lab (Illumina customer): Q3 2026 volumes, MRD growth, Roche AXELIOS and Element evaluation

*Source file: `Working Notes/Sources/ILMN/expert_call/Expert_2026-10-08_Director_of_Molecular_Biology_and_Virology_at_a_Contract_Research_Organization_Optimistic.md` · Date: 2026-10-08 · AI-interviewer channel check on an expert-network platform (published 13 Oct 2026; interview 8 Oct 2026); expert is a customer, unnamed Director of Molecular Biology and Virology at a contract research organization · expert call*

**Summary.** A customer lab (about 70% CLIA clinical diagnostics, 30% biopharma/clinical-trial work) that runs 100% of its short-read sequencing on Illumina reports sample volume up about 18% year over year in Q3 2026, driven by biopharma contract wins and better MRD (minimal residual disease) reimbursement. It expects about 15% growth in 2027, and is evaluating Element Biosciences (cost) and Roche AXELIOS (speed) for possible additions around December 2026, while saying it is not worried about Roche taking share in the short term. Pricing, discounts, lead times and support were all unchanged, and reagent spend rose about 20%, all from volume.

## Expert background and how to read this call

- **Who the expert is.** The speaker is a Director of Molecular Biology and Virology at a contract research organization (CRO, a company that runs studies and tests on behalf of drug developers). They are a **customer** of Illumina, not a former employee or competitor. The expert-network platform describes them as having visibility into technical and strategic oversight of sequencing [Expert: CRO molecular biology director, 8 Oct 2026].
- **Recency.** The interview took place on 8 October 2026 and was published on 13 October 2026. The expert speaks about the current year, including Q3 2026, and about their 2027 plans, so the experience is current.
- **Format.** An AI interviewer asked a standard channel-check questionnaire. Most answers are direct experience of the lab's own operations. Statements about Roche AXELIOS (Roche's new short-read sequencer), competitor pricing, and the 2027 outlook are partly second-hand (market price quotes, publications, colleagues at other labs) or forecasts, and are flagged below.
- **Caveat on a few figures.** Some numbers the expert gave are internally inconsistent, noted where they occur (for example the percentage breakdowns and the long-read split).

## The lab and its customers

- **Volume.** The lab sequences about 3,000 NGS (next-generation sequencing, high-volume DNA reading) samples per year. The expert said that at roughly 90 gigabases (Gb, billions of DNA letters) per whole genome sample, this is about 270 TB per year. The interviewer restated this as about 270,000 Gb. (The expert mixed gigabase and terabyte units while calculating; this is the expert's own rough estimate.) The expert later said the lab tracks **sample counts, not gigabases**, because targeted assays produce far less data than whole genomes [Expert, Oct 2026].
- **Business mix.** About 70% of revenue comes from clinical diagnostics performed as a CLIA laboratory (CLIA is the US certification regime for clinical labs). The other 30% is research use, mainly running clinical trial samples for biopharma and biotech clients, some of whom require a CLIA lab, plus R&D and translational research.
- **Clinical customers.** Hospitals and clinics send patient samples directly to the lab, which acts as their reference laboratory (an outside lab that performs a specialized test) for a very specialized NGS test.

## Demand drivers and constraints

The expert listed the forces that move sequencing volume, in no particular order [Expert, Oct 2026]:

1. **Clinical guidelines.** When a guideline is approved supporting testing of a biomarker for an indication, oncologists and clinicians use the lab's test.
2. **Reimbursement.** High reimbursement from private or public payers is described as the main way to be cash-flow positive on a test, and has a "huge influence" on volume. Reimbursable tests have notably higher volume than non-reimbursable ones.
3. **Large biopharma projects.** A clinical trial needing a few thousand samples in a year raises volume, with the lab's test used to screen and identify patients for the trial.

**Capacity.** The expert sees no throughput constraint. The lab has enough instruments for extremely high volume and can scale staff quickly, including hiring short-term contractors.

**Supply chain.** A minor factor is sequencing suppliers restricting a workflow product. The lab keeps two or three alternative vendors at each workflow step (for reagents, flow cells, magnetic beads and so on). Occasionally only one or two OEMs (original equipment manufacturers) make a given plastic or reagent worldwide, so several vendors share the same source and delays can occur. The expert said they ran into similar shortages during COVID.

## Clinical application mix and growth outlook

The expert's breakdown of clinical sequencing (the numbers add to roughly 100% only with an R&D remainder):

| Application | Share of lab output | Expected growth next 12 months |
|---|---|---|
| MRD (minimal residual disease, testing for leftover cancer cells after treatment) | about 30% | 15%-20% year over year (fastest) |
| Oncology tumor profiling | about 30% | about 6%-7% (slowest) |
| Rare disease whole genome sequencing | about 33% | about 8%-9% |
| Internal R&D feasibility and validation | about 7% | not discussed |
| Reproductive health and infectious disease | none | not applicable |

**Why each is growing at its pace** [Expert, Oct 2026]:
- **MRD:** Many new guidelines for leukemia and other blood cancers use NGS as an orthogonal (independent, complementary) method to monitor patients before and after treatment. Repeated testing across the patient journey multiplies volume.
- **Rare disease whole genome:** Payer reimbursement has risen "slowly but steady" year over year. It was "pretty tough to get reimbursed a few years ago", helped by new publications and guidelines, but the lab still does not get full reimbursement.
- **Tumor profiling:** Many competitors offer similar platforms and tests, and reimbursement criteria are stringent and unclear unless a primary test has already indicated profiling is needed. The expert said the lab is not seeing double-digit or accelerated growth.

## Instrument fleet and short-read versus long-read split

**Fleet.** The lab runs:
- Illumina short-read (reads short DNA fragments, good for small changes) instruments: MiSeq i100 (newest, bought at the start of 2026), NextSeq 1000, NextSeq 2000, NovaSeq 6000 and NovaSeq X.
- Oxford Nanopore (ONT) GridION, used for research and rare disease applications.
- A first-generation PacBio HiFi long-read instrument.

**Split.** About 70% of output is short-read and 30% is long-read, with the long-read work focused on rare disease whole genome sequencing.

**Reasoning.** Short-read is used to find short insertions/deletions (indels) and mutations. Long-read is used for fusions, chimeric and more complex variants, detected with better resolution and lower error rate.

**Outlook for the split.** It should stay about the same absent a new biopharma or pharma contract favoring long-read whole genome work, a major reimbursement change, or a new guideline showing long-read whole genome raises rare disease diagnostic rate [Expert, Oct 2026].

**Which instruments carry the volume.** Most samples run on the NovaSeq 6000 and NovaSeq X because of throughput. Some whole genomes run on long-read machines and some on NovaSeq, NovaSeq X and NextSeq (mid-throughput). Choice depends on batch size, turnaround time and target mutation. The lab sometimes splits a sample in half and runs it in parallel on short-read and long-read to raise diagnostic yield.

## Q3 2026 results, utilization and outlook

- **Versus expectations.** Q3 2026 output "definitely met" expectations.
- **Utilization.** Instruments are at about 75%-80% utilization, leaving roughly 20%-25% of capacity untapped, so growth can be handled without new instruments.
- **Growth.** Total volume rose about **18%** in Q3 2026 versus Q3 2025. Drivers: (1) winning contracts with a few biopharma companies, and (2) a slight improvement in reimbursement for one of the lab's MRD tests. (The expert said "three elements" but named two.)
- **Full-year 2026.** Sample output is up by a similar, about 18%. Biopharma clients are willing to spend somewhat more than in 2025 and the lab landed a few bigger projects. On the clinical side, MRD grew because of better guidelines, reimbursement and clinician adoption, which the expert credits partly to marketing effort over the past few years.
- **Sentiment.** The expert is "pretty optimistic", saying the lab is exceeding its revenue target and expects the tailwind to last through the end of 2026.
- **2027 forecast.** About **15%** growth. Drivers: a few biopharma clinical trials near the end of the sales funnel with a high chance of closing in 2027, plus continued MRD clinician education and reimbursement improvement.
- **Why 15% is below 18%.** The expert said the lab is "conservative" and 2026 may be an anomaly from a couple of one-time contracts. The last five years' trend was 10%-15% growth.

## Competitive landscape: short-read

- **Current share.** **100%** of the lab's short-read output is on Illumina.
- **Evaluations.** The lab is considering evaluating Element Biosciences and the new Roche sequencer (launched earlier in 2026), possibly in **late Q4 2026 (around December)**, and possibly bringing in one of them.
- **Element rationale (cost).** The expert believes Element could give a lower cost per gigabase. Throughput is a little lower, but reagent and total cost might be lower.
- **Roche rationale (speed).** Publications indicate **one-day turnaround** for whole genome sequencing. The lab could use this to offer whole genome sequencing for NICU (neonatal intensive care) babies in hospitals to diagnose rare diseases, which could drive growth in that segment.
- **Share impact.** If either is purchased, it would take share from the NovaSeq X, NovaSeq 6000 or NextSeq, via shorter turnaround or lower price. It would be a **net addition** to the fleet, not a replacement.
- **Stability.** There was no change in vendor share between 2025 and 2026.

## Competitive landscape: long-read

- **Split.** The expert said about 65%-70% runs on PacBio and "the other 40%" on Oxford Nanopore (arithmetically inconsistent; the interviewer restated it as 65%-70% and 30%-35%).
- **Role of each.** Both are used for complex variants. The lab currently runs **no research samples on PacBio**, only clinical. Research samples that need long-read for structural or complex variants go to Oxford Nanopore.
- **Outlook.** The lab expects to expand PacBio throughput rather than Nanopore, and to reduce Nanopore use a little as research samples decline and the focus shifts to clinical diagnostics and clinical trials, which do not run on Nanopore.

## Roche AXELIOS: evaluation detail

- **Stage.** Still evaluating. Over the next three months the lab is talking to colleagues at other labs who already use the Roche instrument about workflow, turnaround time, optimal throughput, bioinformatics integration, and the end-to-end process from extraction to reporting.
- **Reusable sensor.** The washable flow cell is "attractive, but that's not unique", since Oxford Nanopore flow cells can be washed too (the expert said up to four or five times). The expert's understanding is that nanopores can plug, become less robust after washing, and risk cross-contamination.
- **Price (market hearsay).** The expert heard about **$600,000-$700,000** per instrument, depending on relationship and discount. The lab expected under **$500,000** and was "taken by surprise"; the price is "still relatively high".
- **Main concern: bioinformatics.** The worry is not sequencing capability but downstream integration, ease of use of analysis and automated report generation. The expert said Roche lacks the whole bioinformatics ecosystem that Illumina has with its **DRAGEN platform** (Illumina's analysis software) and other tools.
- **Threat to Illumina.** Roche has a heavily penetrated clinical channel through years of selling instruments to hospitals and clinics, which may help adoption in high-throughput hospital labs and take some clinical diagnostic share. But Illumina is well known in clinical, and the expert is "not too worried about Roche taking share" in the short term; adoption "is going to take many years". The expert said commercialization execution matters more than the technology.
- **RUO versus CLIA.** AXELIOS launched research-use-only (RUO). The expert said most clinical assays are lab-developed tests (LDTs), so an RUO instrument is acceptable under CLIA if the full end-to-end assay is validated for performance, sensitivity and specificity. A diagnostic (Dx) version is needed only for clinical trial samples, where everything must be locked down.
- **Validation effort.** About **four to six months** to fully validate a clinical test if all goes smoothly. Bottlenecks: obtaining enough samples (about 50 clinical samples per validation, and 50-60 is hard for rare biomarkers; cell lines can supply positive controls) and retraining technicians who are trained on Illumina workflows.
- **Decision status.** Wait and see. The lab wants more users and publications first, and will look for value beyond genomics, such as methylation and single-cell spatial sequencing, in multi-omics (combining several types of molecular measurement).

## Illumina products and corporate actions

- **NovaSeq X roadmap.** The interviewer said Illumina committed to raising NovaSeq X flow cell output by up to 40% and speeding whole genome sequencing by about 30%. The expert said the lab (which has adopted the NovaSeq X) could use it more if actually implemented, but pricing matters, since the new chemistry and flow cells may cost more.
- **TruPath Genome.** The interviewer said it launched February 2026, removes library preparation from the whole genome workflow, and lists at about $395 per sample. The lab has not adopted it but is validating it, with early data "positive", validation expected to finish in **Q1 2027** and commercial launch in Q1 2027. It has not shifted any long-read work to Illumina, since short-read still cannot identify complex structural variants and the lab uses both technologies for diagnostic yield.
- **SomaLogic.** The interviewer said Illumina closed the acquisition in January 2026. It has had no effect on the lab, which does not offer proteomics (protein measurement).

## Instrument purchases and capital spending

- **Plans.** Over the next 12 months the only candidates are Roche and Element (decision around Q4 2026), as additions.
- **Q3 2026.** No instrument placement plans were accelerated, delayed or canceled.
- **CapEx.** Sequencing capital spending in 2026 is flat versus 2025. The only new sequencer was the Illumina MiSeq i100 bought early in 2026 (other non-sequencing instruments were also bought).
- **Vendor terms.** Instrument discounts, incentives and placement terms in Q3 2026 were unchanged versus the prior quarter.

## Consumables, pricing, inventory and support

- **Reagent spend.** Up about **20%** in Q3 2026 versus 2025 (reagent expense for the year). The expert said it was **all volume**, including validation work, with no price effect.
- **Pricing.** Prices for comparable consumables are the same in 2026 as in 2025.
- **Contracts.** Discounts and commitments were unchanged in Q3. "We have contracts for three years, so they cannot change the price."
- **Inventory and lead times.** Inventory is "sufficient"; lead times stayed about the same.
- **Support.** No standout positive or negative vendors. The lab gets "pretty good support" because it is a high-volume, high-priority customer, and support levels were unchanged in Q3.

## Other points

- **Emerging technology.** The expert is not tracking any new sequencing technology.
- **Closing flag.** The expert highlighted upstream workflow tools, such as nucleic acid extraction machines, automation and liquid handlers, particularly for cell-free DNA in liquid biopsy, as the space they are watching now.

## Notable quotes

- On Roche's short-term threat: "In a short time, I'm not too worried about Roche taking share. It's going to take many years."
- On Roche's price: "We were taken by surprise that it still costs $600,000-$700,000 for the machine."
- On Roche's gap: "The main concern for the Roche instrument is not the sequencing capability, but the downstream integration for bioinformatics."
- On pricing: "We have contracts for three years, so they cannot change the price."
- On 2027: "We try to be a little bit conservative… 2026 is an anomaly."
