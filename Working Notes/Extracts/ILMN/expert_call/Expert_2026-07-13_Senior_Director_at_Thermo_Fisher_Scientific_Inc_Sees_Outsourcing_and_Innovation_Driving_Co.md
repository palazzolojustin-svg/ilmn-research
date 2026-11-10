# Thermo Fisher Senior Director on Outsourcing, Value Splits and Competitive Pressure on Illumina in Cancer Diagnostics Hardware (Expert Call, 13 Jul 2026)

*Source file: `Working Notes/Sources/ILMN/expert_call/Expert_2026-07-13_Senior_Director_at_Thermo_Fisher_Scientific_Inc_Sees_Outsourcing_and_Innovation_Driving_Co.md` · Date: 2026-07-13 · Expert call transcript (interview 13 Jul 2026, published 11 Oct 2026); expert is a Senior Director, Strategic Program Management at Thermo Fisher Scientific; client analyst unnamed · expert call*

**Summary.** A Thermo Fisher senior director describes how the hardware behind cancer tests (multi-cancer early detection, minimal residual disease, companion diagnostics) is built and how much of it is outsourced. They say Illumina's razor-blade model gives it a very high consumables attach rate, but that its dominant position is being eroded by Element, long-read players, 10x/Parse and especially Roche's new lower-cost sequencing platform. They say Illumina has cut prices and is likely to use more outsourcing to lower costs and to widen its ecosystem (single-cell, spatial, sample prep, AI software).

## Expert background and how to read this call

- **Who:** Senior Director, Strategic Program Management at Thermo Fisher Scientific, reporting to the Vice President of Strategic Programs. The expert leads enterprise-wide strategic initiatives, manages a high-value project portfolio and runs the profit and loss (P&L) of large integration and optimisation programs [Expert: Thermo Fisher senior director, Jul 2026].
- **Experience:** About 25 years across life sciences, in vitro diagnostics (IVD, tests run on lab instruments) and liquid biopsy (cancer testing from blood), including multi-cancer early detection (MCED), molecular residual disease (MRD, detecting leftover cancer after treatment) and companion diagnostics (CDx, tests that match a patient to a drug). They also know testing hardware, analytical instruments and what device makers (OEMs) expect from contract manufacturers.
- **Earlier role:** Director, Strategic Business Development and Marketing at Waters Corporation (liquid chromatography and mass spectrometry), leaving in 2018.
- **Relationship to Illumina:** Not an Illumina employee or direct customer. The expert is a sector and competitor-adjacent voice (Thermo Fisher is also an Illumina peer) and a customer of ERP and LIMS software. Many statements about Illumina are the expert's understanding of the industry ("my understanding is...") rather than first-hand knowledge. One item is direct contact: the expert chatted with Illumina at a trade show about AI.
- **Framing:** The client is an investor-type analyst looking at the hardware supply chain (the call is business-led, and the client mentions contract manufacturers and EMS companies, i.e. electronics manufacturing services firms). Several questions are about contract-manufacturing opportunity, not Illumina itself. The published title says the expert "sees outsourcing and innovation driving competitiveness."

## Cancer-diagnostic workflows: overlaps and differences

- The expert says the three areas (MCED, MRD, CDx) have "more overlaps than differences." MCED and MRD overlap most in technology and hardware. CDx overlaps less [Expert, Jul 2026].
- **CDx today:** Mostly still uses immunohistochemistry (IHC, staining of tissue to show protein biomarkers) and in situ hybridization (ISH). The reason: many CDx tests are tied to tissue biopsies, and IHC on tissue is the "gold standard" because it keeps spatial information.
- **Growth:** Current practice is still mainly IHC, but "the growth for PCR and NGS are higher," driven by more biomarkers and by liquid biopsy that detects mutations in cell-free DNA to guide drug choice.
- **Convergence:** CDx is converging toward liquid biopsy and next-generation sequencing (NGS) gene panels, plus qPCR and digital PCR. Today many CDx still look at one gene or a few mutations, which is targeted and used to choose drugs.
- **Technology split inside CDx:** All three (IHC, PCR, NGS) are used. Well-defined targets such as EGFR mutations can be detected by qPCR. More mutations are being found, which drives multiplex NGS panels, and some panels are approved as CDx.
- **Reimbursement quirk:** Even when a panel covers thousands of genes, CDx reimbursement usually applies to the one or few targeted mutations that match the drug. The same panel can also be used for broader cancer genomic profiling.
- **MCED status:** An emerging, early field. No FDA-approved MCED test exists yet. Most insurers do not reimburse it. Many players are still in R&D gathering evidence to convince payers. MCED relies on liquid biopsy looking at circulating tumor DNA.

## Value split of a high-value test

The client used a GRAIL-style example (an MCED test priced at about $1,000) and asked how the price divides among equipment, consumable hardware (plastics such as flow cells and plates), reagents (chemicals and enzymes) and the testing service (the lab company's own service and margin).

- The expert said reagents and the lab service make up the majority of value. Reagents are critical, used in every test, recurring, innovative and complex. Lab service margins are significant.
- Equipment is capital equipment used over many years, so per test it is a small share. OEMs with closed systems accept lower equipment margins to earn recurring reagent revenue.
- The client proposed: equipment 10%-15%, plastic consumables 25%-30%, the remaining ~60% reagents plus service margin. The expert disagreed on plastics: plastic consumables are "less than the 25%-30%" and reagents are worth more than plastics.
- The expert's estimate: reagents plus lab service margin "probably account for 70% of the test."

## Margins by component (gross margin)

| Component | Expert's gross margin estimate |
|---|---|
| Reagents, enzymes (also proteins, antibodies) | About 90% |
| Plastic consumables | About 80% (OEM level) |
| Instruments | 50%-60% |

- The expert also gave "70%-80% to the OEM, but it may be lower for the contract manufacturer" for consumables.
- Operating margin: for many companies in this space it is around 20%, but it is hard to assign to one component because shared costs must be allocated. This is why the expert prefers gross margin for component comparisons.

## Outsourcing maturity by area (client scale: low <20%, medium 20%-40%, high >40%)

| Area | Expert's grade | Reasoning |
|---|---|---|
| NGS (sequencers, overall) | Low to medium | Some modules outsourced, e.g. photonics; flow cells and some reagents in-house |
| Nucleic acid extraction | Moderate (higher than NGS) | Established technology (magnetic beads, columns) can be outsourced unless differentiated; integrated platforms and custom sample-prep modules favor in-house |
| Liquid handling | High | Many capable vendors: Tecan, Hamilton, Opentrons, HighRes, Labtech, Agilent, Beckman Coulter |
| Library prep | Low to medium (moderate overall) | R&D in-house, but enzymes and reagents bought from third parties |
| PCR | Not graded explicitly | Mature technology, many manufacturers can make it reliably |

### NGS sequencer hardware (expert's understanding)

- **Imaging:** Illumina instruments need very high-resolution imaging to capture millions of tiny reaction sites. "Illumina is not an imaging equipment company." It typically obtains imaging and photonics modules from vendors such as Hamamatsu or IonOptix (the expert's wording).
- **Sample prep modules:** Often outsourced to contract manufacturers.
- **Flow cells and enzymes:** Flow cells (the consumable slide on which sequencing happens) and some enzymes are in-house for quality and performance. Some enzymes come from third parties with enzyme expertise.
- **IP:** "IP is a significant concern": high-IP components favor in-house work; components needing special technology that would take long to develop in-house are outsourced.
- **Electronics:** Boards are often outsourced. Design may be collaborative, but manufacturing typically goes to firms like Jabil. The client noted Jabil is an Illumina supplier and has called out optical detection systems as a support area.
- **Development partners:** Invetech and Stratasys provide contract development and small-scale manufacturing. Commercial-scale production tends to go to large contract manufacturers like Jabil.
- **Microfluidics:** Increasingly used because it miniaturizes reagent use and delivers throughput. Manufacturing is typically outsourced to foundries; development is a mix of in-house and co-development. Outsourcing is common because of economies of scale for single-use consumables. "Those are opportunities for contract manufacturers."
- **Compute:** The expert understands Illumina outsources the compute hardware (GPU) while keeping bioinformatics and software development in-house. The cloud is still big for Illumina's bioinformatics, but compute is increasingly embedded in instruments for customers needing on-premises capability. Delivery is multi-approach (cloud, on-instrument, customer servers or private cloud).
- **Instrument generations:** Higher-throughput platforms need better photonics; smaller, lower-throughput platforms need less resolution and can be cheaper. Photonics and electronics change with each generation. With more competition, Illumina must do this more.

### IHC stainers (CDx hardware): who builds what

- **Roche (Ventana):** Makes instruments in-house, outsources components such as metal frames and some detection and liquid handling modules, and assembles in-house.
- **Leica (part of Danaher):** Similar, with some components outsourced.
- **Dako (Agilent):** Mostly in-house manufacturing with some outsourced components. Its latest instrument, Omnis, was co-developed with Tecan, which continues to support automation and liquid handling, while manufacturing is now in-house at Agilent.
- **Sakura:** In-house development over many years, strong in hardware engineering, but reagents came from a third party. It acquired a San Francisco Bay Area company to get its IHC reagent menu, now in-house.
- **Biocare:** Recently acquired by Agilent. It had a platform and many reagents and previously supplied reagents to others such as Dako. Agilent bought it to enhance its assay menu.
- **Pattern the expert drew:** Companies often start by outsourcing a capability and, if it proves critical, bring it in-house through acquisition for control, reliability and differentiation.

## Attach rate and business model

- The expert said the consumables attach rate (how often customers buy the maker's own consumables with its instruments) is "really high" because of the IP and platform design. Illumina's model is a "razor blades business model": initial capital sale, then most revenue from recurring consumables and reagents, though instruments are also high-value and expensive.
- Flow cells are unique to the platform, so customers must buy them from Illumina.
- Library construction kits can come from other vendors. The expert sees "a lot of opportunities" to raise attachment, but says it is "a balancing act": if too exclusive, customers wanting to launch certain assays may not use the platform. With many competitors, customers have more choices, so Illumina needs more openness to keep its installed base while maximizing consumables attachment.
- The client suggested companies like GRAIL and Guardant now have vendor choices and pushes Illumina to open library prep and extraction.

## Competitive erosion of Illumina's position

Statements here are the expert's opinions, not verified data.

- "Illumina's dominant position is being eroded because of the alternatives" coming to market. The expert said Illumina "has been reducing pricing to try to maintain its market share."
- More outsourcing is one strategy to lower cost: contract manufacturers with scale and expertise can make some components more cheaply than Illumina can in-house, helping it lower consumable and reagent costs to compete with new entrants.
- **Element Biosciences:** Offers lower-cost options and is an alternative sequencer for single-cell workflows.
- **Long-read players (PacBio, Oxford Nanopore):** "Still relatively low market share," but long-read has an advantage for some applications (mutations, rearrangements, translocations), so an opportunity to take share.
- **10x Genomics and Parse (now acquired by QIAGEN):** Dominant in single-cell transcriptomics (measuring gene activity in individual cells rather than in bulk), which the expert says has "really high growth." Previously they used Illumina instruments, with Illumina as partner, but now other sequencers can serve those workflows. NGS is only one component; sample prep is highly customized.
- **Illumina's response:** It bought Fluent (single-cell capability) to offer a complete workflow. The expert said it is increasingly important for Illumina to diversify into the ecosystem to "build a moat," since the analyzer is where Illumina is "still dominating" but upstream technologies give new entrants a way to take share.
- **Hardware and front-end investment:** Illumina must keep investing in front-end sample prep for single-cell, spatial and MCED/MRD (the latter need greater sensitivity for liquid biopsy).
- **Over the next several years:** "an increased competitive pressure on Illumina in the next-gen sequencing market." The expert said Illumina no longer has as much technological leadership as before, so it will explore lowering cost and increasing differentiation.

## GRAIL, Guardant and Illumina

- The expert confirmed the client's understanding that GRAIL and Guardant have no manufacturing of their own hardware or reagents and buy from suppliers.
- GRAIL was acquired by Illumina, and because of a regulatory issue Illumina had to divest it. GRAIL does not own a sequencer, uses Illumina, but there is "no tie-up to stay with Illumina," and it can use other sequencers.

## Roche's Axelios platform

- Roche recently launched a new NGS platform (named AXELIOS in the client's question). It is currently research use only (RUO), with a plan to seek approval as an IVD device.
- It is third-generation NGS using sequencing by expansion, which the expert said is "lower cost than Illumina's short-read sequencer," which relies on sequencing by synthesis.
- Because "Roche is a strong incumbent in the clinical labs" with a strong IVD presence, the expert expects it to take share from Illumina in clinical testing once approved, and in a few years to "definitely change the landscape" for clinical NGS.
- The expert's reasoning on price: Roche wants a healthy margin from the platform, but the lower-cost technology "should translate into lower cost for the lab."
- The client asked whether Axelios is qPCR-based; the expert answered that it is a new NGS platform (not qPCR).

## AI, software and automation

- **Penetration:** AI embedded on instruments is "probably low right now"; much AI is in downstream bioinformatics packages. Illumina has a very large installed base of legacy machines, so new AI-embedded versions have low penetration. The client's 10%-15% on-instrument figure was not endorsed. Instrument-level AI is "starting, but relatively modest"; downstream use "is already quite significant."
- **Illumina statement (direct contact):** At a trade show, Illumina told the expert AI is "really big" in the company and that half of its software organization is doing something related to AI [Expert recounting Illumina conversation, Jul 2026].
- **Uses:** Improving imaging and data output, optimizing sequencer operation and sample prep, and analysis downstream.
- **Outsourcing opportunity:** Continued outsourcing for automation (end-to-end sample-to-result) and software development, including AI/ML, plus PCR from contract manufacturers for front-end prep.
- **IVD instruments generally:** Imaging is increasingly important, especially with spatial biology, and AI makes image analysis more powerful. There is also innovation in non-imaging detection (electrochemical readouts), focused on sensitivity, signal-to-noise, reproducibility and throughput. Culture readers (such as Thermo Fisher's APAS Independence, raised by the client) are commonly image readers, with other readout technologies, including microplate readers, under active development.

## Contract manufacturing trends

- Differentiation for a contract manufacturer would be offering reagent deposition (filling, spotting, lyophilization) on top of plastics. Today many OEMs outsource the plastic consumables but fill reagents in-house to control critical elements (enzymes, antibodies, affinity reagents). The expert sees an end-to-end offering as "probably a trend," confirmed as an increasing trend.

## Companion diagnostics development

- Most pharma companies do not develop the diagnostic themselves; they co-develop CDx with an IVD partner such as Guardant or Roche. Roche is an exception, having both pharma and diagnostics divisions that collaborate, though they remain separate divisions. Most other pharma companies have no diagnostic division.

## Reagent sourcing for library prep

- Enzymes (polymerases, nucleases, ligases) are broadly available from New England Biolabs, MilliporeSigma, Thermo Fisher, Takara and Promega, so OEMs typically outsource those reagents. For critical reagents, OEMs like Illumina also run intensive in-house R&D on novel, higher-performing reagents (sensitivity, specificity, reproducibility) and manufacture reagents for library prep and sequencing themselves. The expert grades this overall as moderate.

## Caveats

- The expert is an industry observer, not an Illumina insider. Margin percentages, outsourcing grades and statements about Illumina's pricing and supplier relationships are the expert's estimates or understanding, not company disclosures.
- Interview was 13 Jul 2026 and was published 11 Oct 2026, so the information may be stale on Roche's platform status and regulatory timing.
