# Former Roche Principal Software Engineer on AI in Genomics, Sequencing Hardware Moats and Roche SBX vs. Illumina

*Source file: `Working Notes/Sources/ILMN/expert_call/Expert_2026-07-27_Former_Principal_Software_Engineer_at_Roche_Holding_Ltd_Believes_AI_Is_Revolutionizing_Gen.md` · Date: 2026-07-27 · AlphaSense expert call (company deep-dive); expert is a former Principal Software Engineer / Principal AI Researcher at Roche (left February 2025); interviewer is an investor-led buy-side analyst. Published 2026-07-30. · expert call*

**Summary.** A former Roche deep-learning engineer who worked on the base caller for Roche's SBX sequencer says sequencing hardware is an extremely hard-to-disrupt moat, that Roche's SBX offers throughput and data-cleanliness advantages but will not replace Illumina, and that no winner-takes-all outcome is likely. He argues AI is transforming the software layer (base calling, variant calling, interpretation, possibly with less data) and helps small and large firms alike, while hardware remains the moat. He sees routine, cheap whole genome sequencing as the long-term vision, still years away.

# Expert call notes: Former Roche Principal Software Engineer on AI, Genomics and Sequencing Moats

## Expert background and relationship to Illumina

**Relationship.** The expert is a former employee of a competitor (Roche), not of Illumina. AlphaSense tags the perspective as "Competitor" and the analyst perspective as "Investor-Led (Buy-Side)". Primary company: ILMN. The call took place 2026-07-27 and was published 2026-07-30.

**Role and recency.** The expert was a Principal Software Engineer (also described as Principal AI Researcher and Consultant in generative AI, agentic AI, bioinformatics and robotics) at Roche, leaving in February 2025. They say they spent four years at Roche, on the deep learning team building the base caller algorithm for Roche's sequencer. (A base caller turns the raw signals a sequencer measures into the letters A, G, T and C of DNA.) Their Roche experience is therefore about 17 months old at the time of the call, and they were not at Roche when its product moved further toward market. They note Roche's SBX work was presented publicly by their supervisor "last year" (2025).

**Earlier career (all direct experience).**
- About 2008: on the research team for Siri when it was a research project at Stanford Research Institute.
- PhD in robotics and AI/ML.
- Around 2016: post-doc at UC San Diego (UCSD) in the Sebat Lab, working on the genomics of the neurodevelopmental basis of autism, including modeling the mutation rate of the genome and predicting the pathogenicity (disease-causing potential) of genomic variants. Used Illumina, array and other sequencing data. "When I was at UCSD, everybody was using Illumina sequencing."
- Bionano Genomics (optical imaging of genomes, good for structural variation, meaning large rearrangements of DNA).
- Roswell Biotech (a sequencing company with novel chemistries).
- Roche: base-calling neural network architectures and data-cleaning strategies for training data.
- Says they have worked about 10 years in bioinformatics and AI/ML applications to it. Currently works with several small players and uses AI coding agents heavily.

**Limits of the expert's knowledge.** They have direct experience of sequencer hardware, base calling and research genomics. They say they have not tried AI on variant-calling or confidence-interval problems in genomics ("I haven't really tried for genomics per se"; "I have heard some success stories"). Their comments on GeneDx's business, Roche's current commercial progress and Illumina's market position are opinion or inference. They did not give figures on Illumina's financials, pricing or market share.

## Durable moats in sequencing: hardware is the barrier

**Core view [Expert, Jul 2026].** It is "very difficult" for anyone to enter the sequencer market from scratch. The expert says that even with their experience, starting their own sequencer company would be very difficult because of the capital needed. A sequencer needs a lot of electronics and sophisticated chemistries, so "it's fundamentally a hardware problem," needing far more capital than bioinformatics or AI/ML software on top. "There's only a handful of companies that can even touch that."

**Timelines (direct experience at Roche).**
- Roche spent around 15-20 years building its sequencer; the expert was there for four of them.
- The SBX chemistry (the sequencing chemistry Roche acquired) had been in development since about 2010-2011, and was researched for "at least 10-20 years" before it went to Roche. One person in a lab worked on it for many years, with many teams prototyping it, and it had extensive validation before being spun out.
- Getting a mature sequencer off the ground has "easily" been a 10-year process or more. The downstream clinical applications are probably another 10 years.
- Getting a sequencer to do basic sequencing at all is "at least a couple-of-years process" in itself; the expert has seen early-stage companies struggle to produce basic sequencing data.
- Building a robust sequencer with a low false positive rate, accurate variant calling and an accurate human genome is a large effort. Linking detected variants to health and clinical studies (pathogenicity of variants) is "an even larger can of worms."
- Teams need many specialties; the expert worked alongside PhDs who often had 10 years in industry.
- Overall, matching incumbents like Roche and Illumina "has been a 20-year process."

**Manufacturing.** The expert says it is even harder to get a sequencer manufactured, and "that's actually where Roche stumbled." The big question that "shook the market at that time" was who would manufacture it. They add that Roche "might have wind people up by now" (the transcript is unclear; they appear to mean Roche may have since resolved this). Hardware prototyping takes years, and this "is going to be a big problem for every sequencing company."

**Conclusion on moat.** Because of this, "places like Roche and Illumina are fairly safe from the hardware disruption, unless something helps there." The expert is exploring whether AI "CADing agents" (computer-aided design) could make hardware design as easy as coding, but notes hardware still has to be built or manufactured, so it remains "much more difficult to disrupt." Right now "that's still the moat."

**Does AI shorten the 20-year path?** The expert is unsure ("I don't know if new innovations like AI will speed that up"). Expertise is accelerated by AI, which "maybe closes the gap," but the capital and the burden of proving the sequencing works remain "very challenging."

## Roche SBX versus Illumina

**Roche advantages [Expert, direct experience plus opinion].**
- The SBX chemistry (sequencing by synthesis, which Roche "pioneered" in its SBX form) has advantages in throughput (more genomes at once, efficient bulk sequencing) and speed.
- The base caller the expert worked on was "one of the best that I had": extremely fast, ran on GPUs, and the data was "much cleaner than anything I'd ever previously worked on."
- Every effort at Roche aimed at making sequencing faster and cheaper.
- Better data quality might help research on complicated disorders such as neurodevelopmental conditions.
- Throughput is "the big one" for Roche; data quality in complicated regions is second.

**Roche challenges and unknowns.**
- Cost per genome: "they were still trying to figure that out." The expert notes cost, speed and efficiency are what matter to a clinician.
- Accuracy was "pretty good" overall, but achieving accuracy in edge cases (highly repetitive regions, structural variation, complex variation) "has been the challenge."
- Roche was earlier-stage than Illumina on go-to-market: starting to form partnerships with clinicians and get technology to hospitals.

**Illumina's strengths [Expert opinion].**
- Illumina has been the incumbent for a long time and has "a very strong moat with all the clinicians and the people already in the field."
- Short-read sequencing "still has lots of advantages." Long-read sequencing can be more accurate for very complicated regions, but the expense may remain. Roche was trying to bring cost down and extend read length.
- "Illumina probably will still remain strong in other aspects," and "Illumina will probably still have a strong moat."

**No winner-takes-all.** Having multiple technologies is useful because one can validate the variants called by another. "There won't really be a winner takes all, from my perspective." Asked whether Roche can replace Illumina: "No, I don't think anybody's going to replace anyone. That's not the way genomics works." Instead there are trade-offs by application, and he lists Roche, Illumina, GeneDx and Ultima as systems with trade-offs (and compares this to trade-offs between AI models). Asked if Illumina is going away soon: "I don't think so." He concedes a market shift in particular applications is possible and that some things could advantage Roche, but says "I don't have a clear understanding of what exactly." Roche's advances are described as higher throughput and potentially faster and cheaper, with more players and options for consumers, who will "try everything as much as they can."

## Whole genome sequencing, discovery and the neurodevelopmental landscape

- **Discovery versus known variants [Expert].** For variants already known to cause a disorder, targeted assays (tests designed for specific known variants) are cheaper and potentially more reliable than whole genome sequencing (WGS). That is "more GeneDx's business": testing a new patient for something well implicated. WGS is useful for discovering new variation, which is where Roche and Illumina "have a lot of value for the scientific edge."
- **Exome versus genome.** Whole exome sequencing (only protein-coding regions) helps, but non-coding variation also matters; WGS helps find enhancer-promoter effects. The client noted the non-coding part is the roughly 80% of the genome that is poorly understood; the expert agreed AI could help.
- **Environment.** For neurodevelopmental disorders, environment matters greatly, sometimes "potentially more environment than genetics," though genetics is still important (the expert has seen bipolar disorder and autism pass through generations). Expert quote: "genomics loads the gun... the actual firing mechanism is the environment." Environmental and clinical data are less public than large WGS datasets and are often proprietary to clinics.
- **Client's point (not the expert's).** The client noted in diagnostic odysseys the cause is often unknown and multiple causes are possible, hence multi-gene panels and then exome testing.

## How AI changes genomics (software layer)

**Base calling and false positives [Expert, direct experience].** The expert has had "a lot of success with base calling algorithms that have much lower false positive rates than I ever could" before. AI is "very good at designing data processing pipelines."

**Case-based reasoning.** LLMs can decide on each individual data point using its specific context rather than a general rule set. A rule-based filter with 15-20 rules cannot easily handle cases where only some rules apply. The expert says AI can "dramatically lower false positive rates" this way. The reasoning can be complicated yet more accurate than codified rules or statistical analyses, and the expert sees it as "a new form of representation that's potentially more powerful" than classical ML statistics, which "seems a little bit archaic now."

**Interpretability.** AI can explain why it classified a data point a certain way, which was historically a pain point for data scientists. The Roche base caller work had nothing like this; the expert says today every base or variant could have a context-specific decision and explanation.

**Ambition.** The expert is "very excited" by LLMs and future AI creating "zero false positive rate solutions" in variant and base calling, which "could not be achieved earlier." Genomics will see AI performance gains like everything else.

**Less data needed (opinion/speculation).**
- Classical deep learning and statistics were "a data game": more data, better system. LLMs, being generally intelligent and pre-trained on lots of data, can make good decisions on small datasets, "potentially better" than expert humans.
- Example: a variant seen three times in a population might be implicated in disease with the help of phenotype, genotype and symptom data, whereas the statistical approach (GWAS, a genome-wide association study) would need more hits (e.g. 10) for significance. The client summarized that a rare disease sequenced 5-50 times might be enough to start predicting; the expert said "potentially," depending on orthogonal metadata (physician notes, symptoms, environment, downstream clinical data). He speculated 3-5 or even 20 counts might suffice for a clinician. AI cannot decide without the right data.
- Rare disorders may benefit most.
- The expert says this could disrupt the conventional statistical-hypothesis-testing view, which remains the incumbent viewpoint in healthcare. He said it is "100% fair" that healthcare wants more data to confirm hypotheses and that the more-data-more-confidence model is still how it works today; his point is AI might allow implicating cases with less data given good metadata.

**Confidence.** Classical confidence depends on data size. LLMs can estimate their own confidence, which could yield complex "non-parametric" confidence intervals; those scores are "sometimes... not terrible" in his non-health applications, but need far more validation for health use. He said he has not tried this in genomics and does not want to overstep.

**Evidence of clinical impact.** He says AI has been reported to solve "at least hundreds" of complicated cases that doctors struggled with, by suggesting biological mechanisms that clinicians then tested and confirmed. Whether this works at population scale is unknown, so healthcare will remain "data conservative." A doctor would review AI output.

## Business implications

**GeneDx and AI.** Asked whether AI helps or hurts GeneDx (which competes with Labcorp and Natera, per the client), the expert said AI "helps everything" and "helps everyone." The client's hypothesis that cheap interpretation could spur interest and investment that helps Illumina and hurts GeneDx was not directly endorsed; the expert replied that for already-implicated variants, targeted tests are cheaper than WGS and described that as GeneDx's business (also compared to 23andMe).

**AI and company size [Expert opinion].**
- AI is "a danger not to use." Roche did not allow AI for two of the four years the expert was there, which they called "a bit of a crutch" that "a big company can do."
- AI helps smaller companies compete because they can do much more with fewer resources; "it's a huge boon for the start-up world."
- Personal productivity: about three "vibe coding" (AI-assisted coding) projects per week in 2026, each of which would previously have taken years; a patent draft per week versus about a year traditionally.
- "I am more efficient than I ever was." He sees an "open playing field" and "a lot of opportunities for everyone."

**Does AI create more genetic-testing companies?** AI disrupts the software layer; "the hardware layer is the moat for WGS," so AI does not lower the barrier to making sequencers.

## Throughput: why it matters and when

- **Why throughput matters [Expert].** WGS at higher throughput and lower cost lets the field collect far more genomes, which is how new variation is implicated and how confidence in decisions (by AI or humans) is built. He calls this "in a nutshell the disruption" Roche brings. He referenced public databases such as gnomAD that held hundreds of thousands of genomes when he worked with them and may have reached millions; he speculated about eventually reaching billions.
- **Tipping point.** The client gave an illustration: GeneDx at roughly 100,000 genomes or tests a year, over about 250 days, is about 400 a day, and asked where throughput becomes a no-brainer (400, 1,000, tens of thousands a day?). The expert gave no numeric threshold. He said throughput matters when sequencing a genome is not a cost consideration for a clinician, and everyone can get their genome very inexpensively, "just like taking a blood pressure test or a temperature."
- **Timing.** The client said this is far from today's reality (not standard of care); the expert agreed ("It feels like it's"). Importance will rise as understanding of complex diseases (brain disorders, cancer) grows. He expects "a huge breakthrough in health... sooner rather than later, probably next five, 10 years," and, with AI, more difficult conditions getting treated.

## Key takeaways and caveats

- Hardware is the durable moat in sequencing; AI mostly strengthens the software layer and benefits challengers and incumbents alike.
- Roche's SBX edge is throughput and clean data, with unresolved questions on cost per genome, edge-case accuracy, manufacturing and clinical adoption; the expert expects coexistence with Illumina, not displacement.
- The expert's AI-reduces-data-needs views are speculative and not tested by them in genomics; clinical adoption would be slow and cautious.
- The expert's Roche knowledge is dated to early 2025, and no financial, pricing or market-share figures for Illumina were provided.
