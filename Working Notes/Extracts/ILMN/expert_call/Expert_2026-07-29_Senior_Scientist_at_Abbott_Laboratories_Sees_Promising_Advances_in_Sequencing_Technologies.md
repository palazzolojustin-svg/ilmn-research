# Expert call with a senior scientist at Abbott Laboratories (long-time Illumina customer) on sequencing competition, switching costs, NovaSeq X, clinical NGS and MRD

*Source file: `Working Notes/Sources/ILMN/expert_call/Expert_2026-07-29_Senior_Scientist_at_Abbott_Laboratories_Sees_Promising_Advances_in_Sequencing_Technologies.md` · Date: 2026-07-29 · AlphaSense expert call (published 31 Jul 2026; interview 29 Jul 2026); expert is a Senior Scientist at Abbott Laboratories, former scientist at Zafrens; investor-led (buy-side) interviewer · expert call*

**Summary.** A customer-side expert (23 years as an Illumina customer, mainly NextSeq and MiSeq user, with startup and diagnostics experience) gives views on new competitors (Roche AXELIOS, Element, Ultima, Thermo Fisher Ion Torrent, long-read players), what it takes to switch away from Illumina, the NovaSeq X upgrade cycle, clinical NGS growth, Illumina's WGS-based MRD kit and spatial products. The expert sees Element as the competitor with the best chance of taking share, says switching is slow and costly (a month or two of side-by-side testing, plus capital cost), and says clinical NGS growth is concentrated in oncology and prenatal screening. The expert repeatedly stresses limited direct knowledge of several topics (NovaSeq X, MRD, spatial, large core labs).

# Expert call: Senior Scientist at Abbott Laboratories on sequencing technologies and clinical applications (interview 29 Jul 2026)

## Expert background and how to weigh the views

- **Role and employer.** Senior Scientist at Abbott Laboratories. Formerly a scientist at Zafrens. Works across drug discovery, sequencing (next-generation and novel technologies), diagnostics and in vitro diagnostics (tests run on samples outside the body). Reports to the Head of R&D and sits two levels below the C-suite. About 13 years of experience in the industry [AlphaSense bio].
- **Relationship to Illumina.** A **customer**. Uses Illumina sequencers, mainly NextSeq (a mid-throughput instrument) and MiSeq (a small, lower-throughput instrument). The bio says they have been a customer for 23 years. Per the bio they can also speak about Danaher, Thermo Fisher, 10x Genomics, Agilent, Roche and Waters. The interviewer was an investor-led (buy-side) analyst.
- **Training.** PhD in chemistry and biophysics, undergraduate degree in biochemistry. Has worked "off and on" in tech, including sequencing directly and adjacent areas such as gene therapies and high-throughput drug screening. More recently has done diagnostics work, including at the current employer [Expert, Jul 2026].
- **Recency and reliability.**
  - Direct experience: NextSeq, MiSeq, evaluating instruments from a startup perspective (leasing, capital cost, bench space, data formats, side-by-side testing).
  - Self-declared gaps: has **not used NovaSeq X**; is "not an expert on large core centers" (their last frequent contact with core labs was in graduate school); is "not an expert on MRD", on immunohistochemistry, on spatial mapping, on insurance and reimbursement; and has not seen the latest AXELIOS quality data. These answers are mostly informed guesses, which the expert often labels as "hunch", "guess" or "I imagine".

## Roche AXELIOS (mid-read sequencing, SBX technology)

Background: the interviewer said Roche launched AXELIOS about one month before the call and that it uses SBX technology.

- **Expert view of the technology.** "I think it's a very exciting technology." It opens a new space of **middle-length reads**: a bit longer than Illumina reads and shorter than Oxford Nanopore reads. The expert suggests this could help with correlating SNPs (single-letter DNA variations) across longer distances, and with getting higher-confidence calls over sequences of that length or where information has to be preserved across that distance [Expert, Jul 2026]. Speculation, not direct experience; the expert has followed it since first announcements, roughly 1.5 to 2 years ago.
- **Library preparation.** Library prep (preparing DNA for the sequencer) "doesn't seem too hard", which the expert thinks could benefit users.
- **What Roche must prove to move volume from Illumina.**
  - Data quality: the expert understood AXELIOS quality scores to be "pretty high", "maybe not quite as good as Illumina currently". This matters, but may matter less given the benefit of longer reads. The full set of applications users will adopt it for is not yet clear to the expert.
  - Cost: "going to be a significant driver", along with **device cost**. Persuading core labs, startups or medium-sized companies to switch means one of the biggest capital expenditures (CapEx) they make. Lease options will probably exist ("we'll see").
  - Workflow integration: if the data can be rapidly adopted into clinical or R&D workflows, that is a big benefit. The expert credits Illumina's software and cloud capabilities with making adoption easy for many people. Clinical settings are different, and it will be interesting to see how this evolves as the rollout continues.
- **Mid-read vs very long reads.** The expert says mid-read length may offer enough benefit to make someone switch platforms without giving up much data quantity or quality, which the very-long-read technologies tend to do.

## Competitor landscape

### Element Biosciences (VITARI, $100 genome)

- The interviewer said Element claims a **$100 genome** (the cost to sequence one whole human genome) for later in 2026.
- Expert view on what the price enables: historically, for cancer screening or high-risk genetic and rare-disease screening, labs used focused panels (sequencing only selected genes), so a $100 genome was not needed. The expert thinks it "might open up new avenues of really preventive medicine".
- Open question: how this works out with insurance and reimbursement is unclear to the expert (self-described non-expert), though they see possible "win-wins" for patients and insurers. More genome-wide association study data could also make a $100 genome valuable.

### Which competitor should worry Illumina most

- **Element:** "Element has a good opportunity to capture more market share in terms of growth rates and other things." The expert repeated: "My guess is that Element has a good opportunity to really capture a little more share." (explicitly a guess).
- **Ultima:** promising, but it focuses on very large scale, so it "might take a longer time to get more market traction". It is also younger. Some labs may hesitate over Ultima because it is a smaller company. The expert does not know the unit economics of comparing it with a NovaSeq. On the high end, Ultima is a potentially significant competitor now and in the future.
- **PacBio and Oxford Nanopore:** "still up in the air"; more niche in application. Without new exploration, their market shares "may not change a lot at the moment."
- **Thermo Fisher (Ion Torrent, Genexus):** not to be discounted; the expert knows they have added new platforms and calls them "still a force". The expert is unsure of their share but thinks it is "at least 10%-15%" of the sequencing market (rough estimate, no source given).
- **Complete Genomics:** mentioned as another vendor offering the evaluation metrics, though with "a very limited presence in the U.S."

### Do large genome centers split volume across vendors?

Element, Ultima and Roche all now play in high throughput. The expert has not followed big core facilities recently, and the following is a hunch:
- The biggest centers are likely more willing to explore new sequencing modalities, especially if there is demand, and may have the resources and expertise to support them.
- Smaller centers may resist change because of retraining and new data formats, protocols and ways of working.
- In startups, people are more flexible and will change to get better data or a cheaper cost per run. Where an instrument is leased, once the lease ends without penalty, a startup might change platforms if it is financially and data-quality beneficial [Expert, drawing on startup experience].

## Long-read versus short-read

- **Long-read cost and quality.** The expert says long-read technologies trade quality for length. For Oxford Nanopore, the "cost per read is quite a bit higher". Data quality "goes down a little bit" and applications are more limited. Long-read is "usually somewhat more niche". The expert could not say when long-read would take real share from short-read (including in RNA sequencing): "I'm not sure, to put it that way."
- **PacBio selling its short-read assets to Illumina and becoming long-read only.** The expert knows PacBio had technology from an acquisition (thinks Omniome), but is not an expert. They think PacBio is "deciding to stay in one niche. Maybe it's a good strategy" and had no more to say.
- **Where long-read might be clearly better but labs stick with Illumina.** Possibly rare disease, where several SNPs act together at long distances; some labs may get short reads and reconstruct, possibly missing correlated-SNP information, also perhaps for certain cancer mutations. The expert does not know whether this is happening. In clinical use, adopting long-read would face more regulatory approval, which "might just take a long time" and gives labs pause [Expert, speculation].

## Switching costs and frictions when leaving Illumina

The expert says they speak mainly from a startup perspective; core labs may have other constraints.

1. **Technical fundamentals:** average read length and whether it suits the applications; quality scores; whether paired reads in both directions are offered (for example the standard 2x300 format common in the Illumina world). Element and Complete Genomics provide such metrics.
2. **Capital cost, the biggest friction:** whether a lease-to-own arrangement is available. Buying a sequencer is a large CapEx if sequencing in-house instead of sending samples to a core lab.
3. **Physical space:** benchtop room for the instrument.
4. **Data compatibility:** whether output arrives in a FASTQ file (the standard sequencing-data file format Illumina produces) and whether it can be plugged into existing bioinformatics platforms. The expert thinks this has become standardized among the main vendors.
5. **Revalidation time.** The expert's approach: review published literature or white papers comparing platforms, speak to other users, and judge how protocols could be adapted to reach similar quality. Then "it could take a month or two just to really do side-by-side comparison studies", using historical data or one-to-one comparisons, possibly with a core lab, before buying. "It's not an instantaneous decision... You shouldn't take it lightly."

## Illumina instruments and the NovaSeq X upgrade cycle

NovaSeq X is Illumina's high-throughput flagship sequencer. The expert has not used it and cannot speak from experience.

- **Adoption.** It "seems like the share has grown quite a bit" since release, which the expert thinks was four or five years ago (vague recollection).
- **Who upgrades.** Larger core labs typically choose larger sequencers and may run a mix of NextSeqs, MiSeqs and NovaSeqs. A startup scaling up might begin on MiSeq/NextSeq and port protocols to a NovaSeq when more data is needed. Those running multiple NextSeqs or MiSeqs that now need to scale will likely go to NovaSeq.
- **Why labs might not move.** Budget is "a perfectly valid concern". If a lab needs the scale, NovaSeq makes sense because "the cost per reads are lower than any of the other platforms." The decision depends on how many years of use are expected, whether demand will grow, and whether the lab has capital on hand or can arrange a lease with Illumina.
- **Cannibalization of NextSeq.** "It's possible": NovaSeq used at the low end could compete with NextSeq workflows, especially for labs with multiple NextSeqs, where one platform can pool libraries and save time and resources.
- **iSeq (Illumina's lowest-throughput instrument).** The expert is unsure whether the segment is growing or shrinking. The iSeq somewhat replaced the older MiniSeq and is a good first screening tool before scaling to NextSeq or NovaSeq. Some of that role may now be taken by the new MiSeq, which is a middle ground above the iSeq. The iSeq is useful but dedicating an instrument to low throughput raises cost per run; it fits protocol development or early drug discovery, "its own little niche that might be hard to grow from."

## Clinical adoption of next-generation sequencing

- **Where growth is.** The expert believes growth areas are in oncology and prenatal screening ("screening for pregnant people"), the latter described as a "common or not extremely growing area, but a constant one for Illumina" that other companies also address.
- **Rough market mix (expert's guesses, unsourced):** neonatal/pregnancy screening maybe 10%-20% of the clinical market; oncology "another 50%-60% at least, maybe higher actually now."
- **Other areas.** Rare disease diagnosis has a big push but is "not a very large growing market." Cell-free DNA approaches in cancer screening are interesting to follow. Pharmacogenomics panels (for example cytochrome P450 variants that affect drug response) exist but are not extremely large. "I don't see a large, new area of growth beyond those general areas."
- **Companion diagnostics (tests that guide cancer treatment).** Immunohistochemistry (IHC, a stain-based tissue test) still has big use and "I don't see it going away"; sequencing is becoming an extra tool and more prevalent as mutations are more granularly defined and measured. The expert is not an IHC expert and says it is "not clear", but expects sequencing to keep growing as practitioners learn about it and data quality and capabilities improve. PCR was in the question but not specifically addressed.

## MRD (minimal residual disease, detecting traces of cancer after treatment)

The interviewer said Illumina just launched a whole-genome-sequencing (WGS)-based MRD research kit, and that Natera's Signatera (a targeted-panel test) dominates MRD and just received a major NCCN guideline endorsement (interviewer statements).

- **Does WGS make sense vs targeted panels?** The expert answered "I would say yes." There is a movement toward alternatives to targeted panels. WGS gives a relatively straightforward way to screen trace amounts of cancer SNPs and other markers linked to treatment. Fixed panels such as Illumina's TruSight may miss things not currently seen. Whether Illumina builds the tests or others use the kit to build their own, more data will be gathered, and the expert thinks new mutations outside the exome (the protein-coding part of the genome) may be found that contribute to cancer formation.
- **What would let WGS gain share against Signatera?** "I don't know what it would take." The expert says evidence is needed that targeted panels miss things, and notes cancer mutation patterns may shift as some cancers become more or less prevalent. Some companies may already know this and be placing bets. The expert says they are "not an expert on MRD" and declined to go further.
- Summary tag also notes that panels like Signatera currently dominate due to established evidence and guidelines (AI-generated summary, not directly from the transcript).

## Spatial transcriptomics (Illumina StrataMap vs 10x Genomics Atera)

The expert says they are not an expert here. Spatial mapping of relationships ("constellations") has value: inferring genomic relationships, especially in cancers (chromosome abnormalities, possibly genomic organization correlated with pre-cancerous states). The expert thinks vendors are pursuing it because they see growth. The trade-off, as understood, is that these are **more expensive reads** and the area is "a little more exploratory". The expert did not directly say whether StrataMap and Atera address different needs.

## Future opportunities and challenges

- **Neoantigen vaccines (personalized medicine).** The one new growth area the expert offered, described as niche. A patient's tumor is sequenced to find SNPs that create neoantigens (tumor-specific markers); these are encoded "like tiles on a mosaic" into an mRNA that is delivered so T cells and other immune cells can pick them up. The approach has been tried for roughly a couple of decades, and early clinical trials suggest it works. The expert thinks sequencing companies can help build this capability and push personalized genomic medicine forward, with growth potential as efficacy is shown. "I can't think of any other applications at the moment."

## Summary of the expert's overall stance (from the AlphaSense summary and transcript)

- Emerging platforms (Roche AXELIOS, Element) are promising, but adoption depends on cost, data quality and workflow integration.
- Short-read platforms remain dominant, in the expert's view owing to cost, established workflows and regulatory considerations (the regulatory point was raised specifically for clinical long-read use).
- Clinical NGS growth is steady but concentrated in oncology and prenatal screening.
- No numbers on Illumina's financials, pricing of consumables or specific reagent costs were given; the quantified items are the $100 genome claim (interviewer-attributed to Element), the 10%-15% Thermo Fisher share guess, the 10%-20% prenatal and 50%-60%+ oncology clinical mix guesses, a one-to-two-month revalidation time and the 23-year customer tenure.
