# Expert call with Daisy Lab co-founder/CSO and former university genomics core lead on Illumina's position, competition (MGI, Nanopore, Roche SBX), long-read vs short-read, switching barriers, DRAGEN, and strategy

*Source file: `Working Notes/Sources/ILMN/expert_call/Expert_2026-07-23_Co-Founder_and_Chief_Scientific_Officer_at_Daisy_Lab_Believes_Illumina_Will_Maintain_Leade.md` · Date: 2026-07-23 · AlphaSense expert interview (investor-led, buy-side analyst perspective); expert is Co-Founder and Chief Scientific Officer at Daisy Lab and former Lead of Auckland Genomics, University of Auckland (published 2026-07-27) · expert call*

**Summary.** A customer-side expert who ran a New Zealand university sequencing core facility for about five years says Illumina remains the gold standard and will likely keep dominating for roughly the next five years absent a disruptive technology. He sees growing price and flexibility competition from MGI, Oxford Nanopore and eventually Roche's SBX, says validated diagnostic users are very unlikely to switch, and criticizes Illumina's steep small-scale pricing and its diversification into new areas, advising a focus on lowering the cost of core sequencing.

## Expert background and how to weigh the views

**Who the expert is.** The expert is Co-Founder and Chief Scientific Officer of Daisy Lab, a pre-revenue, development-stage company working on precision fermentation (using microbes to make food ingredients) and molecular biology for sustainable food systems. They report to Daisy Lab's board. [Expert: Daisy Lab co-founder/CSO, Jul 2026]

**Relationship to Illumina: customer.** The interview is tagged "Customer" for expert perspective and "Investor-Led (Buy-Side)" for analyst perspective. The expert was previously Lead of Auckland Genomics at the University of Auckland, reporting to the Dean of Science. They headed the genomics core facility (a shared university lab that sells sequencing services), oversaw high-throughput sequencing and drove primary research. They left in January 2021. In the call they said they "run a genomics facility" and had run the core for "about five years", with close to 25 years in molecular biology as researcher and at various companies. The bio lists a further 6 years as a researcher. [Expert: Daisy Lab co-founder/CSO, Jul 2026]

**Recency caveat.** The bio says the expert left the University of Auckland core in January 2021, yet the expert speaks in the present tense ("we use", "I run") about facility operations and pricing. Their direct hands-on knowledge may therefore be several years old. The call does not resolve this, so treat the facility details as possibly dated. The expert also refers to a local provider that is shifting to MGI, which suggests some ongoing knowledge of the New Zealand market.

**Platforms used.** The expert has used Illumina sequencers, Oxford Nanopore sequencers and MGI sequencers. The bio says they primarily focus on Illumina and Nanopore. They can speak to sequencing (including the "Midnight Method"), pathogen evolution, antibiotic resistance, GMO regulation and precision fermentation.

**Direct experience versus speculation.** Statements on Nanopore and Illumina economics, tech support, the facility's revenue mix and the 100x small-scale pricing are firsthand. MGI observations are partly firsthand (they have access to MGI in New Zealand) and partly about a local provider. Statements on Roche SBX, Element, Ultima, MGI's bioinformatics, DRAGEN interoperability, circulating tumor DNA and Illumina's diversification are explicitly hedged ("from what I understand", "I'm not as familiar"). The expert declines to say what Illumina's best strategy is. The advice given is labeled speculation by the interviewer's framing.

## Illumina's market position

- The expert calls Illumina "the leading technology, the gold standard" and says that when most people think of sequencing, they think of Illumina. Some customers of a core facility simply ask for "Illumina sequencing" without knowing alternatives exist: "Almost it's becoming like Kleenex or something."
- Illumina is "definitely the major player", but many competitors now produce "pretty similar short-read data", which "is going to maybe be a challenge for them".
- Outlook: absent a big change, Illumina "will continue to dominate" for "the next five years maybe". Competitors are gaining some advantages, but "it's going to take a major shift" for them to enter Illumina's market, and they "need to do something really different." The expert sees no one doing something "absolutely dramatically different" and no "disruptor coming just yet".
- Why Illumina holds: its data is "really good", it is "still the gold standard for everything", and it has validated kits and assays that many customers already use. The expert expects the market to "be cut away a little bit", not lost.
- A disruptor would have to be a technology "so dramatically different at a price point that is dramatically lower" that it could change the whole market. SBX is cited as an example of a candidate.
- Illumina does not meaningfully compete in long-read. The expert has seen a few things Illumina is bringing out, but they "don't seem to be anywhere near the same level of technology" as PacBio or Oxford Nanopore. Illumina's "long-read" technology is "very basic" by comparison, "from what I understand" (hedged).

## Long-read sequencing: why it matters and how big it is

**Definitions the expert used.** Short-read sequencing (Illumina's approach) reads tiny DNA fragments. Long-read sequencing (PacBio, Oxford Nanopore) reads much longer pieces. Generally, "long read" means Oxford Nanopore, then PacBio.

**Puzzle analogy.** Assembling a genome is like a puzzle with many "blue sky" pieces (featureless parts). Illumina gives "thousands of tiny little blue sky pieces" that are very hard to assemble. Nanopore gives "big pieces", which are "fuzzy" but make it "much more easily" possible to assemble a genome.

**Other advantages of long-read (not only repeats).**
- Methylation information (chemical marks on DNA that affect gene activity) comes "for free", with no extra chemical treatment.
- RNA sequencing: full-length transcripts can be read; the expert says there are many Nanopore advantages in RNA that they consider better than Illumina.
- Genomic rearrangements can be detected. The expert stressed that solving repetitive elements is "definitely not the only advantage."
- Long-read can be used across a huge range of applications and "provides answers that short read can't".
- Nanopore flexibility at low scale: you can stop a run partway and reuse the flow cells (the consumable cartridge), adjusting output, which "can be a cost saving".

**Current disadvantages of Nanopore.** (1) Accuracy: historically lower than Illumina at the single-molecule level, though "getting better and better". (2) Price at scale: price per base (cost per unit of DNA read) at very high scale is "exorbitantly expensive" with Nanopore. By contrast, Illumina with the NovaSeq X (its newest high-throughput instrument) is "so cheap" at huge scale; Nanopore can do "bespoke" work but "can't do that at scale yet."

**Direction of travel.** The expert thinks accuracy (base calling, the software that converts signal to letters, and the pores used) is improving. If long-read's disadvantages disappear, it would have "a long list of advantages relative no disadvantages", so people would choose it and "the market for long read... will grow".

**MGI in long-read.** The expert says MGI "has basically, from what it looks like, completely copied Nanopore, in some regard", with very similar technology, and is "approaching the long-read market at scale", so cost at scale is coming down. (Expert's characterization, not verified.)

**Long-read share of work at the expert's facility.** The interviewer said he generally hears that roughly 10% of sequencing skews toward long-read. The expert said at their facility it is higher: "probably closer to 20% or 30%" of the work by revenue is Nanopore, and "definitely growing". This is one facility, not the market.

**Structural variants.** Structural variants are DNA rearrangements such as inversions or translocations (a piece moved elsewhere), seen more often in cancers than in inherited conditions. Long reads identify them far more easily because most reads span the breakpoint and show both sides in one read. With short reads, it is harder to have enough reads covering the breakpoint to evidence the event. The expert was not familiar with circulating cell-free DNA (liquid biopsy) or the "fragmentomics" idea the interviewer raised and spoke only about structural variants generally.

## Instrument cost and accessibility (Nanopore vs Illumina)

- Large Illumina instruments cost about NZD 1.5 million to NZD 2 million in New Zealand dollars (later described loosely as "$1 million" for a big box in a core facility). Nanopore devices cost about $10,000 or $20,000 depending on device, "now it's increasing a little bit". [Expert, Jul 2026]
- The expert, as a provider, can get Nanopore machines "much cheaper than I can buy a huge Illumina instrument". It is "much easier to get in", to buy your own equipment and run it in your own lab, and Nanopore is "getting a lot more uptake in that way too".
- Nanopore for a long time "literally" gave out free sequencers while customers bought reagents (the expert's description). This, especially during COVID, let Nanopore "explode into the market" as every small lab sequenced small viruses. Nanopore's sequencer is "candy bar-sized" and its motto was "democratizing sequencing, anyone, anywhere, anytime."
- Contrast: Illumina's model is "a big box in a big core facility", which the expert says "has been a disadvantage for them in the past few years, to be honest."

## Short-read competition

**General.** The debate is no longer just short-read versus long-read: "It's really like what kind of short read." Growing short-read competitors named by the expert: MGI, Roche (new technology coming) and others. For validated diagnostics such as cancer, short read is "enough and very useful and great", but "even in that space, I think Illumina is facing some competition as well."

**MGI (China-based; most familiar to the expert).**
- Offers equipment at small, medium, large and extra-large output scales. Price is "very competitive" and read quality "very good". MGI does "very, very similar things" to Illumina at all scales, "pretty well".
- Using an MGI sequencer and kits is "definitely much less expensive". MGI kits are "fairly compatible with Illumina kits", so switching from Illumina (or even Nanopore) is "pretty easy". They are "off-brand equivalents that work just as well", producing "the same data and at lower cost".
- Obstacle: brand. Today people say "I want Illumina data or Nanopore data" because of brand confidence. The expert expects that "as time goes on, MGI will potentially have that brand name".
- Geography: the expert has access to MGI in New Zealand; "in the U.S., it may be more difficult to get MGI sequencing" (speculation).
- Agriculture: sequencing is heavily used in agriculture (domesticated plants and animals), which the expert knows better than diagnostic cancer. One New Zealand provider doing large-scale agricultural sequencing is shifting to MGI "just because of cost of the equipment", with data "just as good". They are "ditching their very large Illumina sequencers for MGI. That's a major shift."
- MGI does not appear to have a DRAGEN-like integrated bioinformatics tool, per the expert (hedged: "I'm not as familiar").

**Roche SBX.** The expert said it is "so new" that it "remains to be seen" whether there are real limitations. What Roche says it can do is "pretty amazing", and if it works at a low enough price it "could be a major market shift". Price per gigabase and how the platform is integrated decide uptake. If it is a $2 million machine, only huge institutes such as the Broad might adopt it, which would limit the share impact on Illumina. As the expert understands it, SBX pricing is "still quite expensive to even get into", which may hinder adoption. The interviewer noted SBX may involve a nanopore element; the expert did not confirm.

**Element and Ultima.** The interviewer asked about them; the expert said they are more familiar with MGI and did not comment further.

## Switching barriers

- Established diagnostic labs: with a large Illumina instrument and a validated protocol (a test whose procedure is formally verified), there is "huge hesitation to shift". Assays are "really entrenched". The expert sees "very little reason" to move unless the alternative were "dramatically cheaper... several times maybe" (they said they do not know the economics). Validation takes "so much time and effort", and "if you've got a piece of equipment already, there's no reason to change if it's working."
- This is described as a "huge advantage of Illumina": it has "a lot of that diagnostic market already established, and so people won't move away from that for a long time."
- Flexible buyers: universities, government-funded public research institutes (including "crown research institutes" in New Zealand) and core facilities lack validated assays and are "much more flexible". Research-only (non-clinical) sequencing is "still a huge part of the market".
- Start-ups: the expert pushed back on the interviewer's framing that start-ups drive new demand: start-ups are "a very small space" because sequencing is expensive to enter. The people doing "the majority of the sequencing" are major academic research institutes. Even the Broad Institute and the Wellcome (Sanger) institute have "all of the new machines" and are testing and validating them. (Expert's view; no data given.)

## Market growth

- The expert says the whole sequencing market is "definitely growing": "The cost per base is coming down."
- Drivers cited: academic publishing increasingly requires sequencing; whole genome sequencing is now done by default for unexplained genetic disorder cases where cost used to be prohibitive; microbial work has moved from 16S sequencing (targeting one gene) to whole-genome metagenomic data ("no one wants that anymore").
- Long-term: "There's so much that we haven't sequenced"; with personalized medicine and lower prices "everything will get sequenced."
- No market-size figures or growth rates were given.

## Bioinformatics, DRAGEN, service and support

- With cheaper sequencing, "the issue now is not getting the data, it's analyzing the data." The expert thinks Illumina is "doing a good job" with DRAGEN (Illumina's integrated analysis system), helping researchers and clinicians analyze data and produce validated reports and consistent pipelines. They believe the market is moving to end-to-end offerings, "starting from even cells to all the way to the end of the analysis", and see this as a competitive advantage because analysis can be "a huge barrier".
- Competitors: as far as the expert knows, MGI lacks such a tool and Illumina is "one of the few" integrating bioinformatics this way.
- Interoperability: DRAGEN is not interoperable. Reads carry a barcode identifying the Illumina machine used, so, as the expert understands it, data must come from an Illumina sequencer to be used in DRAGEN (hedged understanding).
- Service and support: Illumina is "head and shoulders above" others, "amazing": they will send someone to fix instruments and customers can call them directly. The expert qualifies "at least in the past". Oxford Nanopore "historically have been incredibly poor" on support but are "getting a lot better", and the expert thinks many ex-Illumina people moved to Nanopore and use the same service model.

## Illumina strategy and the expert's advice

**Diversification.** The interviewer listed Illumina's moves into MRD (minimal residual disease testing), genomic profiling, liquid biopsy, multiomics, proteomics (including SomaLogic) and single-cell (Fluent). The expert has most experience with single-cell: the market "has exploded", 10x Genomics "used to be the major player", Illumina has entered, and the niche is "now flooded". Illumina is "trying to do what everyone else does" and "getting into places where there are already strong existing providers". The expert said they do not know if that is a good strategy, then later said it "seems like what they're doing is trying to do too many things".

**Pricing criticism (firsthand).** Illumina's pricing structure is "a little bit wild". For a smaller provider, price per base at small scale is, "I don't even know, 100X more expensive than at the larger scale, something like that." The expert asked why, since "it's all the same technology", and called small-scale Illumina sequencing "exorbitant". The expert said pricing is "all structured towards the large end of things" and believes small-scale niche sequencing is "also a big market". The figure is a rough estimate, stated twice.

**Capex.** Buying a large Illumina sequencer is "more and more... out of reach", and company capital-expenditure approval "can take several years even".

**Advice (speculative).**
1. Even out pricing so smaller providers can use Illumina.
2. Either develop a brand-new technology doing long and short read at high accuracy for very little money (which "everyone is trying to do", and "seems hard"), or
3. Focus on the core business and do "something really innovative" in lowering the cost of sequencing.

The interviewer mentioned another expert who suggested a tabletop device for locations like doctors' offices. The expert replied that this is what Nanopore did.

## Other discussion (Daisy Lab and Ginkgo)

- Daisy Lab is pre-revenue and in the development stage.
- On Ginkgo Bioworks, the expert said they mostly did synthetic-biology strain development and, as they understand, "historically" that "is where it stopped", selling strains afterward. The interviewer noted Ginkgo is moving into robotics and automation. This is not relevant to Illumina.

## Key quotes

- "Almost it's becoming like Kleenex or something." [Expert, Jul 2026, on Illumina's brand]
- "They're still the gold standard for everything." [Expert, Jul 2026]
- "It seems for the next five years maybe... Illumina will continue to dominate." [Expert, Jul 2026]
- "They're ditching their very large Illumina sequencers for MGI. That's a major shift." [Expert, Jul 2026, on a New Zealand agricultural provider]
- "They produce the same data and at lower cost." [Expert, Jul 2026, on MGI]
- "Head and shoulders above in terms of service and just tech support." [Expert, Jul 2026, on Illumina]
- "Their pricing structure is a little bit wild." [Expert, Jul 2026]
- "Their model is we're going to put a big box in a big core facility." [Expert, Jul 2026, on Illumina vs Nanopore]
