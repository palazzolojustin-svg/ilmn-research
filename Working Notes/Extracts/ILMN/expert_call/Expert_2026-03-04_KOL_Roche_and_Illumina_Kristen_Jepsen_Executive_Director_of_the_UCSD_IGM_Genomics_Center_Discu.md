# Expert call with UCSD IGM Genomics Center director on Roche AXELIOS, Illumina pricing and TruePath, and academic sequencing demand (AGBT 2026 follow-up)

*Source file: `Working Notes/Sources/ILMN/expert_call/Expert_2026-03-04_KOL_Roche_and_Illumina_Kristen_Jepsen_Executive_Director_of_the_UCSD_IGM_Genomics_Center_Discu.md` · Date: 2026-03-04 · Guidepoint expert network; moderator Andrew Carmen (AC); expert Dr. Kristen Jepsen (KJ), Executive Director, IGM Genomics Center, University of California San Diego · expert call*

**Summary.** An academic core-facility director gives a customer's view of the Roche AXELIOS sequencer after seeing it at AGBT (the genomics industry meeting) in 2026. She finds it less modular, harder to adopt and not much cheaper than Illumina's NovaSeq X Plus, expects little share loss for Illumina in 2026, and says Illumina is discounting hard and launching TruePath (long reads) in response. She also reports weak academic demand in early 2026, roughly 10% down on reagent volume, from slow NIH grant funding and competition from outside service labs.

# Expert call notes: Roche AXELIOS, Illumina, and academic sequencing demand

## Expert background and how to weigh the evidence

- The expert is Dr. Kristen Jepsen, Executive Director of the IGM Genomics Center at the University of California, San Diego (UCSD). A "core facility" is a shared university lab that runs sequencing and related assays for many researchers on campus. [Expert: UCSD core facility director, Mar 2026]
- She is a customer and an academic key opinion leader (KOL), not a former Illumina employee. The call was hosted by Guidepoint (an expert network), moderated by Andrew Carmen, and recorded on 2026-03-04. Guidepoint classifies her as "Academic KOL - Physician Scientist".
- She is a repeat advisor ("once again"). She said her lab "held pretty steady this year... It wasn't really a year for new things."
- Her evidence is recent and mostly direct: she had just attended AGBT 2026 (the annual genomics technology conference), including a pre-meeting that Roche held only for core directors, Roche's lunch-and-learn, and an Illumina core-directors talk. She runs Illumina instruments, including NovaSeq X Plus (the "X Plus"; described as a high-throughput sequencer), plus a 10x Genomics Xenium (spatial instrument). She does not run Element, Ultima or Roche. She does not run the PacBio herself; another campus lab does.
- Her views on how Roche, Ultima, Element and Illumina will behave in the market are opinion and inference. Several details (Roche's real prices, the Illumina "35B" flow cell price, the UG200's size) she explicitly did not know or did not see.
- The advisor was asked to avoid commentary on stock prices, valuation and investment recommendations, and non-public information. None was given.

## Roche AXELIOS: what she learned at AGBT 2026

### Modularity was oversold

- Going into the meeting she was "pretty excited." At the 2025 launch, Roche gave few details on operating principles, and she and other core directors understood it as "super modular". Her example was sequencing for 30 minutes to get 300 million reads for customer one, then running another sample for an hour for customer two.
- In fact it is "not modular like that at all." A partial run is possible if you pay for a full run, but "from a pricing standpoint, it's not realistic to run it in a way that's modular." [Expert, direct, Mar 2026]
- Her broader frustration: she had hoped Roche would deliver a mid-throughput box with high-throughput per-base cost, as Element has. "That's clearly not the initial launch plan at least."
- The industry rule she cited: "the more you sequence, the cheaper it gets." Element's strength is giving a mid-throughput sequencer with a per-base cost close to a high-throughput one.

### Library prep is a high barrier for a core lab

- Switching to AXELIOS requires a different library prep (the step that converts DNA or RNA into a form the sequencer can read). It uses linear amplification rather than true PCR amplification.
- By contrast, switching to Element, Singular, or to some extent Ultima was easy. For those, library prep companies "only had to change their adapter sequence." For Roche, the amplification step changes, a "much longer step," and polymerase optimization will probably be needed.
- It also requires tuning. She said Roche was "a little light on the details," but that the Xpandomer synthesis step (the Roche chemistry step that creates the molecules the sensor reads) has to be tuned to the library type, mainly library size. It was unclear whether synthesis time becomes a bottleneck for long (~1 kb) libraries relative to sequencing on the sensor.
- Cores often mix libraries of very different sizes. At the pre-meeting, core directors asked how to mix short and long libraries; she said there was no clear answer. Her lab "run[s] hundreds of different types of samples," so "the barrier to entry is going to be pretty high for the eclectic offerings of a core facility."
- The fit is better for a genome center doing mostly whole genome sequencing, or a lab running a single type of single-cell prep. Example she gave: someone running 10x Flex at about 100 samples a week "should switch", though she doesn't know what share of the ecosystem that is.

### Read length, accuracy and applications

- Strength: longer reads than short-read sequencers. A talk showed isoform usage (which version of a gene's transcript a cell uses) in single-cell RNA sequencing, which short-read machines don't deliver. "The only thing that really sets it apart is the reads are a little longer."
- Simplex reads (one strand of the molecule read, giving more data) have pretty bad accuracy: "we would never pass data off an Illumina sequencer with that kind of quality score." Customers "want it" but "don't really need it" for counting applications (where reads are simply mapped to the genome or to probes). Counting is described as "low-hanging fruit" with cost savings only at very large scale and with many samples of the same type, which is a poor fit for cores.
- Duplex reads (both strands read, higher accuracy): Q30 (a standard accuracy score, about 1 error in 1,000 bases) may be a little higher, but Illumina is also pushing accuracy up, and Ultima's ppmSeq is pushing higher. "I'm not sure they have a huge advantage on accuracy."
- She noted a counterpoint: Roche is probably on a steeper improvement curve than a stable company like Illumina. "It's possible that this is just entry-level stuff, and they're going to accelerate and get much, much better very quickly."

### Pricing and economics

The table below summarizes the economics Roche presented (as relayed by the expert, with her comments).

| Item | Figure | Expert context |
|---|---|---|
| Cost per run (duplex) | $2,400, 16 whole genomes | Per-sample figure is $150 |
| Cost per duplex genome | $150 | "Not earth shattering"; with discounts, many are barely paying that now for Illumina; Ultima is clearly offering below it at list; Roche kept stressing this was list price |
| Simplex price | $0.06 per million reads | Only for the smallest libraries; up to 40 billion reads in one four-hour run |
| Sensor reuse | Up to 20 times (pricing assumes it works for "21") | Carryover (leftover material from a prior run) shown in Roche in-house data at 0.0015, which looked good, but needs independent confirmation |
| Upfront cost | ~$48,000 ("$50,000, $48,000") | Buying 20 uses at $2,400 a run; sensors sold as a separate line item from Xpander chemistry, so the price breakdown is unclear |
| Duplex output range | ~1.7 to 2.5 billion reads | A "really huge delta" for consistent data across 16 samples |
| Instrument price | $750,000 | Few will pay full price |

- The $150 price requires running the sensor all 20 times (she confirmed this to AC).
- The 40-billion-read simplex run is unrealistic for most users: "Who needs 40 billion reads of the same type of library, like you'd be waiting six months for your data." It would also take hundreds of pooled samples and run into barcoding (sample-tagging) issues. She doubts most people can realize the $0.06 price.
- Reuse is a concern especially for applications such as MRD (minimal residual disease, tracking tiny amounts of cancer DNA), where there is "a lot of hesitation to reuse."
- The upfront $48,000 and the wide output range make it "only applicable for really high throughput places."
- Roche's list price of $750,000: "I don't know who's going to pay full price for that." She expects early adopters, CROs (contract research organizations that sell sequencing as a service) and clinical labs to get strong deals, perhaps with reagent commitment agreements that lower capital cost.

### Speed and turnaround

- Not meaningfully faster in routine use. A customer at Roche's lunch-and-learn set a Guinness world record for the fastest rapid genome, but "they tweaked that a lot and optimized a lot." In regular use: "I don't think it's really that much faster than a standard Illumina box."
- Sample prep is long: an overnight amplification step, though hands-off. It would not speed up turnaround.
- She said the amplification step does not look like a bottleneck for instrument throughput, though details were thin.

### Target market, timing and adoption

- She believes Roche's early target is big genome centers. "They can't go clinical yet." Her own situation: "I'm going to have to raise the money and buy a new box, and I'm not feeling like I'm in a hurry to do that."
- Roche's plan, per her understanding: place about 20 boxes in the initial year, mostly with large players who need publications and data. She expects they will hit that.
- Share impact: "I don't think it's a huge share this year." Customers will "tinker," while X Plus machines continue to carry the bulk of throughput. Roche "might make a little dent in Illumina's market, but it won't make much of a dent."
- Roche's advantage: it is a stable company. Buyers do not worry about it going bankrupt, unlike Ultima or Element. She said this on the funding side.
- Her own decision rule: with an X Plus already installed, she is not looking at AXELIOS. She would shop around, possibly including AXELIOS, if she were buying a second X, replacing a retired X, or if Illumina launched a new box and stopped supporting the current one, "what they usually do."
- She noted that the cost of switching is not sensible for most projects for the ~900-1,000 X Plus boxes she says are installed.

### Support and service concerns

- Her main hesitation about Roche is support. Illumina has a strong reputation: effectively 24-hour tech support, remote-in help (such as a Friday 7 pm failure), and trained engineers and field application scientists (FAS, who help with sample prep). Cores do not know how quickly a Roche engineer or FAS would arrive.
- She said Illumina was short on trained engineers when the NovaSeq X first launched, which was hard even for her in San Diego, but Illumina then scaled and trained people. Support need drops as a technology matures: "they're such a mature technology that a lot of those kinks have been worked out over the last 10 years." Any new entrant faces this, since problems only show once the box is in the field (hard samples, IT issues).
- Her view on Roche's culture: at AGBT, "25%, 30% of the CEOs are there for the whole meeting. Roche, I don't even know if they have anyone in their top 50 there."
- On Roche's KAPA acquisition (library prep reagent brand): "they bought KAPA ruined it. We used to get such good support from KAPA... now like you can barely even get an order." She worries about access to senior management.
- She believes her San Diego location gives her slightly faster engineer support, but "I think most people enjoy good support from Illumina." Elements and Singular are also based in San Diego.
- She credits competition (Roche and others) for Illumina now "really paying attention to what their customer base is saying," which she called a good strategy.

## Illumina: pricing, products and positioning

### Pricing and discounting

- She said Illumina is lowering X Plus prices, now below the $750,000 level of Roche's box, "to try and solidify their market share," and is trying to place as many X Plus instruments as possible before the Roche box ramps. "Because of them [Roche], Illumina has come out with a lot of good offers."
- Illumina raised X Plus consumables prices by 2.5% this year (2026), which she found "interesting."
- She described a pricing cycle: companies set flat list prices, then outsized customers pressure them and discounts diverge. "No one pays a list price and some people pay significantly below list price," so Illumina "need[s] a reset." Illumina must be careful not to give CROs much better pricing than service providers or academics, or it risks putting service providers out of business.
- In short-read, Illumina is "already discounting down to the level to try and keep the business from like Ultima and Roche."

### TruePath (formerly "constellation")

- Illumina announced TruePath, the former constellation. It produces synthetic long reads (long reads stitched together from short reads), with no sample prep and about a two-day turnaround ("probably actually a one-day"). Currently only eight genomes per run, so low throughput.
- Pricing: list $395 per genome; she estimates about $600 fully loaded, since throughput is so low (amortized cost is "double"). It sits in the human long-read space, not as a short-read replacement. "It's not going to replace short reads if budgets is your main concern."
- Competition with PacBio: she thinks TruePath "chew[s] away a little bit more of what PacBio has." PacBio libraries alone nearly cost as much as a TruePath genome. She had a big structural variation project (neurological disease) done on PacBio Sequel at high cost per genome. If she had a big human PacBio project now, "I would be looking at switching that over." Throughput is about the same and it is cheaper.
- She noted that the read locations on the flow cell are available, so users with dedicated informatics staff could build their own pipelines and use other genomes (such as metagenomes, which her campus does on PacBio). "This is, let's be clear, Illumina's like third launch of synthetic long reads." Her view: "this has the best chance of any of the long-read technologies they've had at being competitive. And PacBio, they're struggling already."
- She said that for people doing a lot of human work, an Illumina instrument might keep them from buying a PacBio.
- Cores who tried TruePath in private meetings were "very happy."
- Illumina is pushing the message that it is an "end-to-end multiomics company," not just a sequencing company. She questioned "How true is that? I don't know."

### "35B" flow cell and Q70

- She was unsure what the 35B flow cell is. She understood it as a 35-billion-read flow cell versus the 25B flow cell, perhaps just software tuning to extract 35 billion reads from the 25B flow cell at the 25B price. Illumina did not disclose a price. She said her lab already gets about 30 billion reads from a 25B flow cell, so the change is "more incremental than you think, unless when they say 35, they really mean 40."
- Her behavior: extra data goes to customers via more sequencing per sample, not pooling more samples, "which is good for Illumina." Customers tend to buy full lanes. "Without price points, I don't even know what that 35 billion means."
- Q70 (a claimed accuracy score; Q30 is about 1 error in 1,000 bases, Q70 far fewer): "Whatever. I don't care because I mostly do counting." It does not matter much for whole genome work unless somatic or MRD. It might allow shallower sequencing. "These companies kind of play with these Q scores. What's the ground truth."
- Her lab runs three or four 25B flow cells a week and has no trouble filling them. The challenge is filling 10B flow cells for customers who want small increments of data, so the 5B flow cell Illumina has discussed would be attractive: "Our problem on our X isn't not having enough capacity. It's definitely filling runs." She had not seen a 5B price.

### Illumina spatial transcriptomics

- Illumina discussed it briefly; an early-access customer presented. The product works on fresh frozen tissue only, species-agnostic, poly(A) capture. People like the data: clearly better than Visium (10x's spatial product) poly(A) capture, with higher gene expression, and a much larger tissue area than Visium HD. Opinions on the protocol were mixed ("still a little bit of a challenging protocol"), but "Illumina is pretty good at protocol development."
- Limitation: most of her spatial work is FFPE (formalin-fixed, paraffin-embedded tissue, the common clinical format). Probe-based systems are needed for FFPE, which is why 10x went probe-based. Illumina has no significant spatial share yet. Rumor: it competes more with Visium than with Xenium (she runs very little Visium).

## Competitors

### Ultima (UG200)

- She attended the talk but will "never buy one." The box is too high-throughput. Existing Ultima boxes in the field "have a lot of spare capacity," so outsourcing is easy. A local San Diego service provider with an Ultima solicited her business because it is not full and wants to run around the clock to amortize cost. Early-generation owners had to build significant infrastructure.
- UG200 list: $1.25 million, significantly more than an X Plus or Roche box. She believes it needs less infrastructure but did not see it. Ultima is "betting on" applications arriving to match its output; she called that "a risk."
- Her view: Ultima is already below the Roche $150 genome at list. She mentioned the $80 genome and $150 genome in the context of the meeting's "race to the bottom."

### Element (AVITI and VITARI)

- Midsized San Diego cores run Element because its price per run beats a NextSeq (a mid-throughput Illumina box) when they cannot fill an X. Once you have an X, "Element doesn't make that much sense."
- VITARI (new Element box, announced the week before AGBT): higher throughput, reagent price likely lower, but "not a truly high throughput box." Amortized, an X run full time is still cheaper than a VITARI run full time.
- Existing Element owners were "very disappointed" and said "they promised us they wouldn't come out with a new box." They are small facilities that struggle with funds. She does not know whom VITARI targets and knows no one planning to upgrade. Academic excitement is about direct sequencing-based spatial on AVITI, which is not available on VITARI. There was little buzz.
- Many announcements now come before AGBT (Roche in 2025; Element in 2026), which she called "psychological decisions."

### PacBio

- The campus PacBio lab is "quite busy," running mostly metagenomic long-read work. Illumina's announcement will not hurt that lab much, but "PacBio continues to struggle. And this Illumina announcement is not going to help them globally."
- She does not think the Roche launch hurts PacBio "because it's not really long reads."

### 10x Genomics

- Business with 10x is "pretty flat" for her, with no loss to other platforms. Her lab spends over $1 million per year with 10x on single cell (reagents partly bought directly by customers, so she tracks it loosely). Xenium runs around the clock and weekly, so little room to grow.
- 10x had a small presence at AGBT (a meeting room, no suite or booth, no parties) but left chocolates dated 4/18/26. She says a big announcement is planned at AACR (a cancer research meeting), rumored to be a new Xenium version. She is "not at all happy" about that, since her Xenium may be only about three years old. She thinks 10x is "giving away Xeniums right now" and hopes for a trade-in.

### Singular Genomics (G4X) and Stellaromics

- Singular (San Diego): G4X panel sizes are getting large, with higher throughput than other spatial platforms and good tissue-on-slide methods. The company is now focused on spatial and "clearly lost in the sequencing space." Early adopters found it "actually pretty good." Concern: investor-funded startups spark "one year of funding left" rumors, creating longevity worries.
- Stellaromics (Pyxa): early access, niche, well received technically. It can image about 100-micron sections, allowing whole-cell, 3D-style analysis. A talk (a speaker she believed was from University of Washington, uncertain) showed serial 5-micron sections on CosMx, where expression looks very different depending on where a cell is sliced, with proteins more uniform than RNA. Serial sections are too expensive for grant-funded labs, so Stellaromics could be enabling (for example, developmental biology).
- She noted that spatial has a cell segmentation problem (assigning genes to cells) even with thin sections.

## Demand, funding and outsourcing trends

### Academic demand in 4Q25 and early 2026

- 4Q25 finished "pretty strong," as grant money "finally went out the door" and because people sequence everything before the holiday closure. She said even with a flat NIH budget, multiyear funding awards meant less money could be spent in 2025.
- Early 2026 is slow. "I think we'll be down this year. I'm kind of panicked, honestly." Her reagent purchasing is "maybe already like 10% down over last year for this first couple of months." This is mainly Illumina; 10x is flat.
- Causes she listed: (1) outside CROs doing things faster and cheaper as technology matures; (2) money flowing in slowly, "ridiculously low" grants funded in 2026, partly from reviews canceled during the government shutdown, and she suspects "they're just dragging their feet on purpose"; (3) researchers know funding rates are low and stretch awards (4-5 year awards turned into 5-6 years with non-competing extensions), spending less freely than when fund rates were 15% or 10%. PIs now scrutinize trainee "$10,000 experiments." "The creative gets crushed a little bit."
- Most of her customers are UCSD academics, so NIH exposure is high. She heard, unverified, that UCSD was hit harder than other UC campuses.
- She bought no new instruments in 2025 and hopes not to in 2026: "we just really don't have the funds." Universities are "very nervous and they're not encouraging capital spends." The "really fun purchases" are expensive new technology.

### Outsourcing and commoditization

- Over the last year, routine high-throughput work can be slightly cheaper to outsource. She outsources some Ultima sequencing to a local company. "It just doesn't make sense to buy capital equipment when you can't keep it full." Midsized cores cannot keep an X full, so they cannot match CRO prices.
- It is "a tenuous time for an academic core facility": sequencing is increasingly a commodity, though cores have specialized work. She wants to keep technical expertise to develop new assays. Whole genome and single-cell sequencing, if you just need to rent a sequencer, can be cheaper to outsource.

### Race to the bottom

- Her view of AGBT 2026: "It was the race to the bottom. Everyone is just trying to get the cheapest genome." Cheap genomes are great for some shops and maybe the clinic, but "it's not like paradigm shifting" until insurers reimburse and medical records become accessible to researchers. "$80 genome, $150 genome... it's not like changing the world."

## Qualitative summary table

The summary section of the transcript (a Guidepoint-generated overview) lists these positives and negatives.

| Company | Positives | Negatives |
|---|---|---|
| Roche | Longer reads, potential to improve | High entry barrier, complex library prep, uncertain support |
| Illumina | Established support, competitive pricing, mature technology | Pricing pressure from new entrants |
| Ultima | High throughput, competitive pricing | Large infrastructure, niche market |
| Element | Mid-throughput, competitive pricing | Limited appeal for high-throughput facilities |
| PacBio | Strong in long reads | Competitive pressure from Illumina's new offerings |

## Notable quotes

- "It's not modular like that at all." (KJ, on AXELIOS)
- "The barrier to entry is going to be pretty high for the eclectic offerings of a core facility." (KJ)
- "I'm not sure they have a huge advantage on accuracy." (KJ, on Roche duplex)
- "I can thank them for that because because of them, Illumina has come out with a lot of good offers." (KJ, on Roche)
- "It was the race to the bottom." (KJ, on AGBT 2026)
- "I think we'll be down this year. I'm kind of panicked, honestly." (KJ)
- "This has the best chance of any of the long-read technologies they've had at being competitive." (KJ, on TruePath)

## Caveats on the source

- Some transcription errors appear in the source (for example "Xpander" for Xpandomer-related terms, "VITARI," and "court records" for core directors). The "35B" flow cell and TruePath prices were not confirmed by Illumina in this call.
- Moderator AC's mention of 15,000-20,000 Illumina instruments in the field was explicitly marked as not exact. The expert's 900-1,000 installed X Plus figure is her estimate.
- The document header reads "11/04/2026"; the event date is Mar 4, 2026 per the cover.
