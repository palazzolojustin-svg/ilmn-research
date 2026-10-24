# 02b. Expert calls (11 transcripts): what customers, ex-employees and competitors say

Prepared 2026-10-11 for the ILMN buy-side primer. Every statement below is an expert claim unless marked otherwise. Tag key: **[X]** = expert claim (not verified); **[X-direct]** = expert describes their own direct experience; **[X-hearsay]** = expert is repeating what others said or guessing; **[Analyst]** = my own note or arithmetic, not from the expert. Question tags: Q1 = clinical Gb growth and why it may plateau; Q2 = over-earning / NovaSeq 6000 tail / pricing; Q3 = multiomics uptake; Q4 = competition, switching costs, China; Q5 = variance to Wall Street.

All 11 transcripts were read in full (extract first, then the original in `Sources/ILMN/expert_call/`). Short quotes are under 20 words.

## How to weigh the panel (read this first)

The 11 experts are not 11 independent datapoints. They fall into five groups with different biases:

| Group | Calls | Typical bias |
|---|---|---|
| Academic core / research-center customers | 2, 4, 5, 11 | See only the research (RUO) market, which is the weak part of ILMN's business. Little clinical visibility. Three of the four are buying or trialling a competitor. |
| Pharma / clinical-adjacent customer | 1 | Self-declared non-expert on almost everything that matters (X, MRD, spatial). Treat as low signal. |
| Former Illumina staff | 3, 7, 8, 9 | Knowledge ranges from about 2020-2021 (call 7) to Sep 2024 (call 8). Two now work for rivals (call 7 at Roche) or pharma (call 9). |
| Competitor employees | 6 (PacBio), 10 (Oxford Nanopore), 7 (Roche, also ex-ILMN) | Incentive to describe Illumina as sticky and slow, or Roche as weak. |
| Call-date uncertainty | 9, 10, 11 | The three Tegus files carry no date; estimates are given in each header. |

Nobody on the panel gave a clean number for clinical gigabase (Gb) growth. The only hard clinical growth figure (about 20% clinical consumables growth ex-China for two quarters) came from an interviewer, not an expert. The panel is much better on switching costs, Roche, and academic-market weakness than on Q1 and Q3.

---

## (a) Call-by-call summaries

### Call 1. Senior Scientist, Abbott Laboratories (customer)
- **Date:** interview 29 Jul 2026 (published 31 Jul). AlphaSense, buy-side interviewer.
- **Role / credibility:** Senior Scientist at Abbott; formerly at Zafrens; about 13 years in the industry. A customer of Illumina for 23 years, mainly NextSeq and MiSeq. **Has not used NovaSeq X** and says repeatedly they are not an expert on MRD, spatial, large core labs, or insurance. Most answers are labelled "hunch" or "guess". **Low-signal call on Illumina's key franchises.**

Key claims:
1. **Clinical mix guess [X-hearsay, Q1].** The expert guesses prenatal/neonatal screening is "maybe 10%-20% of the market" and oncology "another 50%-60% at least, maybe higher actually now." No source. Rare disease has "a big push" but is "not a very large growing market." "I don't see a large, new area of growth beyond those general areas." (Read: clinical growth is concentrated in oncology and NIPT, with nothing new behind them.)
2. **Switching cost, quantified [X-direct, Q4].** Moving from Illumina means evaluating read length, quality scores, lease-to-own financing, bench space and FASTQ compatibility. Revalidation: "it could take a month or two just to really do side-by-side comparison studies." Capital cost is "the biggest friction." This is from a start-up perspective, not a large clinical lab, so it is the light end of switching cost.
3. **Which rival matters [X-hearsay, Q4].** Element "has a good opportunity to really capture a little more share"; Ultima is promising but "very large scale" and young, so slower traction; PacBio and Nanopore "may not change a lot". Thermo Fisher share guessed at "at least 10%-15%" (unsourced).
4. **NovaSeq X economics [X-hearsay, Q2].** Labs that need scale choose X because "the cost per reads are lower than any of the other platforms," and budget is the main reason others have not moved. NovaSeq X could pull volume from NextSeq at labs with multiple NextSeqs. Expert has no unit-economics view vs Ultima.
5. **$100 genome [X, Q2/Q4].** Interviewer says Element claims a $100 genome later in 2026. Expert thinks it "might open up new avenues of really preventive medicine" but does not know how reimbursement works out.
6. **MRD [X-hearsay, Q1].** Expert says a whole-genome MRD approach "would say yes" makes sense versus fixed panels, but "I don't know what it would take" to beat Natera's Signatera and declines to go further. No evidence behind it.
7. **AXELIOS (Roche) [X-hearsay, Q4].** "Very exciting" mid-length reads; library prep "doesn't seem too hard"; quality "maybe not quite as good as Illumina." Cost and instrument capex will decide adoption.
8. **Large vs small centers [X-hearsay, Q4].** Biggest centers more willing to add modalities; start-ups switch when a lease ends without penalty; smaller centers resist retraining.

### Call 2. Director, genomics core facility, South Carolina (customer)
- **Date:** interview 30 Jul 2026 (published 3 Aug). AlphaSense channel check with an AI interviewer. Associate professor and core director with purchasing authority.
- **Role / credibility:** Current customer. Owns an old NextSeq 500 and MiSeq plus Oxford Nanopore; buys **most high-volume Illumina sequencing from outside providers** (MedGenome, one other) running NovaSeq X. So the direct Illumina footprint is small and most Illumina exposure is third-party. Is buying an Element AVITI24 with NIH money.

Key claims:
1. **Volume [X-direct, Q1/Q5].** Illumina-instrument output is up "approximately 40%" year over year in Q2 2026 vs Q2 2025, "mainly due to demand for single-cell applications," and above expectations. The expert says spending on outside provider orders rose about 40% last year and "at least 40%" this year, vs about 15% for 2024 to 2025 (the wording is ambiguous on which year is which). This is one academic core riding the cheap outsourced NovaSeq X channel, not a market number.
2. **Single-cell driver [X-direct, Q1/Q3].** Single-cell demand is rising because of funding/publication value, the core's own investment, and "commercialization of several technologies which are competing with 10X" that cut library-prep cost, "which results the increase of the depth and sequencing demands." (Read: cheaper single-cell prep is raising sequencing depth per cell. That is a Gb tailwind for any sequencer vendor.)
3. **Price per lane [X-direct, Q2].** Outside providers charge per lane. Quotes: MedGenome "under $1,800 per lane," the other provider "under $2,000" (transcribed oddly), and "under $4,000 per lane" for a 10B or 25B flow cell lane. Prices "didn't change" and "even decreased a bit" when switching providers. Many providers now use the 25B flow cell. [Analyst: if a 25B lane is roughly 1 Tb at 2x150 this implies about $2/Gb all-in service pricing; unverified, check against Core Notes.]
4. **Illumina's own pricing [X-direct, Q2/Q5].** No change in the last 90 days. "I'm feeling that Illumina prefers to work with customers and to provide individualized quotes rather than show unified pricing policies." The expert says Illumina offers "huge discounts" on NovaSeq X quotes but has not tested it (speculation: big commercial buyers).
5. **Equipment [X-direct, Q4/Q5].** The Element system "cost us less than we proposed a year ago." Illumina reps offered discounts on NextSeq 2000 systems.
6. **Share outlook [X-hearsay, Q4].** "Illumina will lose some share but it won't be a significant loss." Gainers: "Element. Maybe Ultima and most probably MGI." Expert plans to move "at least 80%" of in-house sequencing from Illumina to AVITI24 ("I hope"; a hope, not a plan).
7. **MGI [X-hearsay, Q4].** Says MGI has been "logistic demerge[d]" from BGI into a Swiss-owned entity that is "aggressively offering their instruments." Unverified recollection (see section c).
8. **TruPath [X-direct, Q3].** "Very likely" to use native synthetic long reads on NovaSeq X; could be "roughly 5%-6%" of the lab's volume by end of 2026, from two or three cancer-biology labs. "Not a replacement" for long-read; premium add-on.
9. **SomaLogic [X, Q3].** "Potentially a good move" but "not feasible for the small cores" at the current price per sample; does not make the expert use more Illumina overall.
10. **Macro [X-direct, Q5].** NIH/federal funding is the dominant swing factor. Short-term rush-to-spend and longer-term cuts; a "huge reduction of NSF and NIH" in 2027 would mean "significantly less demand."
11. **AXELIOS [X-hearsay, Q4].** Predicts it "will just simply die out" (long reads of about 1,000 bases are not enough, cost unknown, Illumina and Element offer 600 bp reads, TruPath covers synthetic long reads). A prediction without hands-on data.

### Call 3. Former Staff Scientist, Illumina (now CRISPR QC)
- **Date:** interview 30 Jul 2026 (published 3 Aug). AlphaSense, buy-side.
- **Role / credibility:** Former Illumina staff scientist, helped with the early development of two platforms; about 5 years of experience on the bio; lived through a layoff (team cut from 12 to 3). Tenure years not given; he says "personal opinion" and that he "really like[s]" Illumina. Statements on Illumina's current products are "what I've seen," not inside knowledge. **Low-to-moderate signal; narrative-driven; several invented-sounding numbers.**

Key claims:
1. **Business model [X-direct, Q2].** "I'm selling you a car, but I'm the only one that can provide you with the gas" (instrument, then consumables). That model "was fantastic" until new entrants.
2. **Competitors ahead outside sequencing [X, Q3/Q4].** On spatial: asked which platform to use today, "Not the Illumina one"; he would choose 10x Genomics or BGI. 10x is "way ahead" on single-cell and spatial capability and resolution. Illumina is "still the pioneers" in single cell and should focus there.
3. **Roche is the long-term threat [X-hearsay, Q4].** "The one that I will be seriously concerned about." Evidence: Roche's push is "obvious" from LinkedIn and GenomeWeb, and Illumina's former VP of consumables is now at Roche. He calls NovaSeq X "fantastic" and says Roche "is getting close." Caveat: "Maybe I'm completely wrong."
4. **Long-read in clinical rare disease [X, Q1/Q4].** For isoform-driven rare disease he "would definitely" build on long reads. Short-read is better for SNPs. Asked if a large rare-disease lab like GeneDx moves to another platform: "I would say 98.5%." He admits some of his numbers are made up (the 98.5% is an illustrative confidence, not data). For an NICU needing answers in two to three days he would still pick Illumina.
5. **Proteomics [X, Q3].** Illumina's multiomics is "early stage" and "not strong enough," weak on "depth and reproducibility." Marrying nucleic-acid and protein biochemistry is "like mixing water and oil." Based on colleague anecdotes and no hands-on data.
6. **GRAIL and IVD [X-opinion, Q5].** Calls spinning up GRAIL a misstep and says the clinical/IVD push exposed gaps in upstream sample handling. Illumina "lost focus."
7. **Market structure [X, Q4].** Expects the market to resemble PCR machines: "six, seven, up to 10 companies," with Illumina "not going to disappear" but sharing the pie; "not as bright as back then" (2001).
8. **Automation lessons [X-direct, Q4].** Moving a long-read workflow to automation took about nine months and a second platform; error fell from about 40% to 1.8%. Relevant only as an illustration of how long switching a validated clinical workflow can take.

### Call 4. Scientific Director, genomics core, Georgia (customer)
- **Date:** interview 31 Jul 2026 (published 4 Aug). AlphaSense channel check, AI interviewer.
- **Role / credibility:** Founded the core about 15 years ago, about 10-12 staff, mostly academic and HIV/primate research customers. Runs NovaSeq X Plus, NovaSeq 6000 (to be sunset), an old 2015 MiSeq, and a PacBio Vega. Reviews NIH equipment grants. Has never run Ultima. **A good read on what is happening to a research core; not a clinical lab.**

Key claims:
1. **Volume falling underneath a contract [X-direct, Q1/Q5].** Core output is "slightly increased" only because of a long-term HIV-community contract; without it "we would be down." 2023 and 2024 were the biggest years; 2025 was "a slight decrease of about 20%"; 2026 about flat. Spending on Illumina reagents is up but "mostly volume-driven" and the expert has "not had great success in negotiating volume-related discounts."
2. **Where the lost work goes [X-direct, Q2/Q4].** Of volume the core lost, "about 80%-90%" went to big low-cost providers such as Novogene, and Ultima's share of that lost work "started maybe two years ago at about 10%" and has "creep[t] up to about 20%." The expert expects Ultima pressure to "accelerate."
3. **Why lost: price gap on NovaSeq 6000 vs X [X-direct, Q2].** The core waited about 12-18 months to get its NovaSeq X Plus, kept using the NovaSeq 6000, and customers left to vendors with X Plus pricing. (A concrete example of the 6000-to-X price gap pushing customers to cheaper outside capacity.)
4. **Ultima mechanics [X-direct, Q4].** Ultima has approached principal investigators with large program grants and persuaded them to send RNA-seq and single-cell libraries as proofs of principle; another campus outsourcing core is beta-testing Ultima. Reason for adoption: "vastly superior sequencing cost."
5. **Share outlook [X, Q4].** Ultima up; Illumina instruments "maintain current share"; Element flat; PacBio flat. Small cores moving to Element on capital cost; the expert reviews NIH equipment grants and sees Element proposals but "not seen proposals for Ultima."
6. **Sales / support [X-direct, Q5].** "Slightly disappointed": the core took delivery of instruments on Illumina's quarter-end schedule against promised discounts that "haven't [been] honored." Longstanding rep left a year ago; newer reps "less ability to work out deals." Support about 6.5/10 (a guess about managers' view), maintenance about 8.5/10.
7. **Equipment pricing [X-direct, Q5].** NovaSeq X Plus "reasonable" at about $1 million. MiSeq i100 Plus at "over $100,000" will "stop it being more widespread"; PacBio Vega $175,000 is "okay." No equipment price concessions in 90 days.
8. **TruPath [X-direct, Q3].** "Not at all likely": complex immunoglobulin loci need real long reads, and "short-read data without long-read coverage over repetitive regions" cannot resolve them. No Illumina product currently excites him.
9. **AXELIOS [X-direct, Q4].** Roche presented to his campus with a "fairly persuasive pitch" focused on speed; could matter for clinical newborn labs; "very early to tell"; significance within a year unlikely unless FDA-validated assays follow.

### Call 5. Vice President, large academic genome center, Massachusetts (customer)
- **Date:** interview 31 Jul 2026 (published 5 Aug). AlphaSense channel check, AI interviewer.
- **Role / credibility:** Runs "the largest academic genome center in the world"; 25 years in genomics. Predominantly Illumina (NovaSeq X Plus, NovaSeq 6000s, NextSeq, iSeq) plus Ultima, Element, PacBio and a beta AXELIOS. **High-quality customer with real scale and current data; research-market view.**

Key claims:
1. **Flat volume, down in 2026 [X-direct, Q1/Q5].** Q2 2026 Gb and consumables spend "basically the same" as Q2 2025; full-year 2026 "might end up maybe 5% down, but not more than that." Biggest cause: a large federal award "smaller than it was last year by a couple million" and slower project inflow. Outlook "probably less optimistic" than 90 days earlier because NIH summer supplement spending has not appeared. Utilization "about 70%."
2. **Pricing [X-direct, Q2/Q5].** List prices and negotiated volume price unchanged in 90 days. Illumina "typically" changes prices at the start of the calendar year, not mid-year. (Read: the next real price signal is January 2027.)
3. **35B flow cell [X-direct, Q2].** Interested because "it may further reduce the price of sequencing," expected "in January" (2027 by context); no price yet.
4. **AXELIOS pricing and fit [X-hearsay + beta access, Q2/Q4].** "Aggressive pricing basically on par, if not a little bit cheaper than Illumina sequencing"; fast runs and flexible run sizing help labs that struggle to fill a NovaSeq X Plus (the "batching" problem). "It should be very cheap given the sequencing chemistry." Plans to buy "a couple AXELIOS boxes" and upgrade a beta unit; could buy more NovaSeq X Plus "if more volume appears" but no plan now.
5. **Roche share [X, Q4].** First-year impact on Illumina "minimal"; "Illumina still maintains a dominant position"; over time AXELIOS could "exert more pressure than perhaps the other smaller companies" because of speed, price, and Roche's sales reach.
6. **Multiomics interest [X-direct, Q3].** Evaluating Illumina's PIPseq single-cell offering with Illumina ("potential competitive advantage against 10x in some scenarios"); interested in the five-base genome for methylation; "potentially interested" in SomaScan but has used Olink and "may have opportunity to switch" if projects appear; SomaLogic so far "no effect," "unlikely" to raise Illumina usage unless a project demands it.
7. **TruPath [X-direct, Q3].** "Somewhat likely in some scenarios" (rare/developmental disease structural variants). Adoption "limited because of price"; "an expensive, different version of Illumina sequencing"; "Maybe one or 2%" of volume by end of 2026.
8. **Rivals in single-cell / spatial [X, Q3/Q4].** 10x Flex "really lowering the cost of single-cell prep"; 10x Atera now whole transcriptome and could "eat away at some of the activities that people use sequencing readouts for," though "it'll take a while."
9. **Funding backdrop [X, Q5].** "NIH funding situation is not good"; expects fewer large biobank-style programs and a shift toward biopharma-driven demand.

### Call 6. Global Segment Lead, Human Genomics, PacBio (competitor; ex-Illumina)
- **Date:** interview 3 Aug 2026 (published 5 Aug). AlphaSense, buy-side.
- **Role / credibility:** Currently PacBio; was Senior Health Analytics Manager at Illumina (market access/reimbursement for pediatric rare disease), **left June 2021**, so inside Illumina knowledge is about five years old. Self-labelled "anecdotal" on Illumina's reputation. Germline only; says no expertise on proteomics, oncology or MRD. Employer sells long-read, so there is a pro-long-read slant, though much of the call is balanced.

Key claims:
1. **Clinical replaces academic [X, Q1/Q5].** The NIH indirect-cost cap in 2025 "fundamentally" changed academic demand; clinical revenue is "much more consistent" and reimbursement growth in oncology and rare disease has "made up for the reduction in academic funding." "Overall, I think we've seen growth this year."
2. **Short-read is a race to the bottom [X, Q2].** On short read, with Illumina and Roche, "it's a race to the bottom in terms of cost." But the expert says pricing marketing is incomplete: whether a "$150, $200 genome" includes analytics (Illumina Connected Analytics) and storage is "not well-captured," and "all of the ancillary costs are either staying the same or going up across the board." Reagent and consumable costs are falling with throughput.
3. **Illumina stickiness [X, Q4].** "Illumina's had a monopoly in the sequencing field for quite a while now, they're very sticky in clinical markets." A lab that validates an assay on NovaSeq X "is probably not going to switch for a while." Customers have built bioinformatics and EHR connections around the Illumina workflow. Some larger customers are "buying instruments in multiple competitor instruments" to compare, not defecting.
4. **Switching costs by type [X, Q4].** Illumina to another short-read vendor is "much more interchangeable" and "a lighter lift"; Illumina to long-read is "a much bigger lift" (different workflow, no clinical reference materials, no population frequency databases, immature clinical software).
5. **Roche AXELIOS [X-direct (workshop) + hearsay, Q2/Q4].** Launched RUO in July 2026. Data shown is "pretty good" and "up to the spec"; reads up to about 1,000 bp; accuracy "seems higher than Illumina's." Roche says a duplex 30X genome is about **$150**; simplex "could be cheaper but less accurate" and no simplex data published. Instrument announced at **$750,000** ("almost $1 million as well" as a NovaSeq X). Excitement strong in Europe; "a lot of hype without a lot of data." Roche targets high-throughput, time-critical clinical (4 hours vs 24 hours for Illumina, per Roche). Pre-orders "focused on these really high throughput testing centers."
6. **Illumina's competitive concern [X, Q4].** Competition is "hyper-regional" and "comes down to cost"; Illumina should worry most about Roche in clinical because Illumina has "shifted so much of their install base and so much of their strategy to clinical customers." Other start-ups: "a lot of hype, and now we're not seeing as much adoption."
7. **Low-throughput [X, Q5].** States "Illumina retired their MiSeq" and that buyers want to backfill panels volume (this conflicts with the MiSeq i100 launch described in calls 4, 7, 9; see section c).
8. **Reputation [X-hearsay, Q3/Q5].** Illumina "has slowed down quite a bit" as an innovator, new launches "an iteration of something that somebody else is already working on," and there is a "maybe negative feeling" among some customers about Illumina absorbing 10x-style adjacencies. On SomaLogic: "still waiting to see"; saw "not a big emphasis on proteomics" after the deal; will watch ASHG.
9. **Guidance [X-inference, Q5].** Says Illumina "raised their guidance this year" because clinical is picking up. No numbers.

### Call 7. Former Scientist, Medical & Scientific Affairs, Illumina (now Roche Diagnostics)
- **Date:** interview 5 Aug 2026 (published 10 Aug). AlphaSense, buy-side.
- **Role / credibility:** Eight years in clinical sequencing; joined Illumina via the 2020 ARUP spin-out acquisition (the expert does not name the company); then Thermo Fisher clinical sequencing; **now Scientific Affairs Manager for sequencing at Roche Diagnostics (US)**. So a current Roche employee. Repeatedly says "I'm not helpful right now" on long-read, core labs, proteomics, pricing. **Strong on how a clinical lab decides; weak on market numbers. Roche bias is real but this expert still argues Illumina is hard to displace.**

Key claims:
1. **Clinical share and oncology [X-hearsay, Q1].** Clinical sequencing "has been getting more and more market share"; roughly "50%" of the growth is oncology; MRD is a "buzzword," moving from heme to solid tumors, "starting to pick up" and "a competitive space." U.S. sequencing market "around probably $4 billion" with Europe "half that" (no year or source).
2. **Switching in clinical is rare [X-direct, Q4].** "I don't think anyone is really going to move away from Illumina because it is just tried and true." A clinical lab asks whether it knows every wet-lab component, whether it can handle different bioinformatics files, and "Is it really going to be worth it?" Rivals are not "displacing"; they are "opening, having some sort of differentiation to even consider bringing in this other instrument."
3. **Core-lab pattern [X-hearsay, Q4].** A core adds one Element, Ultima or AXELIOS "versus maybe six NovaSeq Xes"; some researchers "never convert."
4. **Pricing and capital [X-hearsay, Q2/Q5].** "Everyone is at around the same price point"; rivals "have to" come down. NovaSeq X list "just above $1 million, like $1.2 or something," but "I doubt that anyone ever pays that list price." Newer entrants need a lower capital cost incentive plus another incentive. (No discount percentage given.)
5. **AXELIOS selling points (a Roche employee, so marketing) [X, Q4].** One sensor module instead of four flow cells; run time selectable from 30 minutes to four hours; smaller reagent footprint ("four freezers" comment). Note: the Extracts file mislabels AXELIOS as Element's; the transcript is clear the expert works for Roche and AXELIOS is Roche's.
6. **NovaSeq 6000 [X-hearsay, Q2].** NovaSeq 6000 "is supposed to become obsolete," and that is "where some of the other players could come in." "I don't know what's going on with their NovaSeq 6000, but it does seem like that is going to create an opportunity for a lot of other companies." Core claim for Q2: the 6000 tail is Illumina's most exposed pocket.
7. **Illumina's roadmap [X-hearsay, Q5].** At AGBT, Illumina reportedly said it would keep improving current products, "especially NovaSeq X," not launch a new box; large core/reference labs like that.
8. **Workflow gaps [X-direct, Q4/Q5].** Clinical labs find it "a pain" to cobble together liquid handling, PCR and quantification around Illumina; rivals with whole-workflow offerings (Thermo Genexus-type turnkey) could "chip away." Thermo is limited: no real whole genome ("maybe 1X-5X"), "few and far between."
9. **Long-read [X-hearsay, Q4].** Not a major threat; niche complement; expert says they have not worked with it.

### Call 8. Former Associate Director, Precision Health & Population Genomics, Illumina (now Kailos Genetics)
- **Date:** interview 6 Aug 2026 (published 19 Aug). AlphaSense, buy-side.
- **Role / credibility:** About 5.5 years at Illumina, **left Sep 2024** (so about two years stale); now a consultant and at Kailos Genetics (an Illumina customer). Still partly owns ILMN stock (disclosed). Strong opinions; many numbers are recollections. **The most strategically useful call for Q1/Q2 mechanism, but the NovaSeq X story pertains to 2023-24.**

Key claims:
1. **The "IBM" moat [X, Q4].** "No one got fired for buying IBM." Estimates **80%+ of installations** are Illumina. Illumina is "not the cheapest" but "your dependable partner"; it is trying to avoid a race to the lowest dollar per base because it "can't win in that space" with a "bigger burn rate" than rivals.
2. **Segment attacks [X, Q4].** Ultima attacks the high end (NovaSeq-class, "hundreds of genomes a day"); MGI/BGI also high end; Element the NextSeq-class middle; Roche expected to target "pure clinical." Rivals fight only Illumina, "while they are fighting many"; newcomers "can definitely go below cost" to build installed base.
3. **NovaSeq X cannibalization and sample saturation [X-direct, Q1/Q2].** NovaSeq X "delivered the output of four NovaSeq 6000s" for a run cost of "almost half, if not 1/3," and "replaced a lot of NovaSeq 6000s... cannibalized the business." The problem was not price: customers "ran out of samples," so instruments ran below capacity. "We actually did sequence everything in the freezer. There's nothing left." (Strong support for the idea that falling price per Gb does not create unlimited volume, i.e. elasticity fades once the backlog is cleared. Experience is 2023-24.)
4. **Clinical mix [X-direct, Q1].** Clinical was **52% of revenue** when he left (Sep 2024), research "50-some and 40-some" before; "now it's becoming predominantly clinical."
5. **NIPT penetration [X-hearsay, Q1].** Recollects **70%-80%** of pregnancies tested ("if I remember correctly"), "one pregnancy out of five" not tested despite coverage. Cancer testing penetration is "really, really low." (This is the nearest clinical saturation point; growth there must come from price/mix and international, not volume.)
6. **MRD [X, Q1].** MRD is preferred over early detection as nearer to penetration; repeat testing means "three to four times in one year" per patient vs one-off CGP. Ultima has said it will tackle MRD.
7. **Customer concentration and margin [X, Q1/Q5].** Illumina is "just the supplier" to BillionToOne, Natera, Guardant, Exact; clinical revenue is "very top-heavy"; those customers have "big bargaining potential" and capture more margin. A rival pitching "cut your cost by half" is a real risk. Counterweight: "An executive making that decision and failing will lose big."
8. **Multiomics [X, Q3].** "Is it a short-term strategy? 100%": it exists because genomics hit a sample-saturation point and Illumina needs new things to sequence. Long-term doubt: proteomics via DNA readout is "what microarray is for DNA"; a native protein sequencer could "kill that market in one day."
9. **Long-read [X, Q4].** "A false statement" that long reads would replace short reads; will stay "stuck" in a niche (rare disease yield: panels 20%, exomes 40-60%, genomes about 80%). Calls PacBio "plummeting."
10. **Horizon [X, Q5].** Bullish for "two to three years at most," more cautious beyond.

### Call 9. Former Senior Manager, Global Market Development, Illumina (now Astellas) (Tegus)
- **Date:** not stated in the file; **estimate roughly Feb-Jun 2026** (my estimate, low confidence). Clues: refers to SomaLogic as completed, AXELIOS being marketed but not launched, "Illumina is coming out with" an MRD kit (call 1 on 29 Jul 2026 says it had "just launched"), and sub-$100 genomes from Element/Ultima. The Extracts file guesses 2026-01-15, which is not supportable.
- **Role / credibility:** About seven years at Illumina (sales specialist, oncology specialist, market development, global market development); before that 10x Genomics and Thermo. Now at Astellas (pharma), says that may bias him. **Years at Illumina are not dated; assume dated by 1-3 years.** The "20%" and ">65% clinical" figures were supplied by the interviewer; the expert at first did not recognise the 20% number and then agreed.

Key claims:
1. **Clinical growth is concentrated [X, Q1/Q5].** On the interviewer's statistic (clinical consumables about 20% ex-China for two straight quarters), the expert agreed it "has a lot to do with the big accounts," naming Natera, Tempus, Caris and Foundation, and he guesses rising MRD uptake explains it. He expects those accounts to "continue to sustain and be increased." But internally "we were relying on the big accounts, basically" and getting broad, "democratized" clinical use was "always the tough question."
2. **Bottleneck is not cost or speed [X, Q1].** The binding constraints are reimbursement, regulation and physician ordering behaviour. "Even if sequencing is free," regulation and reimbursement take time. A $100 genome is "a very nice, sexy number" but tumor sequencing needs "easily more than 120" X depth, and library prep, biopsy, FFPE handling and bioinformatics dominate cost. Impact in somatic oncology "very limited." (Directly answers the price-elasticity question for oncology: cost per Gb is not the constraint.)
3. **"Clinical" is loosely defined [X, Q5].** "Illumina has been very generous and very broad in terms of classifying clinical use"; the only FDA-approved CGP assay is TSO Comprehensive, so "most of it will be run as LDTs" at the large companies.
4. **Roche speed and sales force [X, Q4].** Cutting sequencing from 24-36 hours to under half saves about 12 hours across a workflow that includes biopsy and bioinformatics: "not worth that much" for oncology, more relevant to NICU. Roche's diagnostics sales force is "a big advantage," but converting non-NGS labs needs a "push-button system." Pharma wariness of tying tests to Roche drugs (Foundation precedent).
5. **Thermo vs Illumina [X-direct, Q4].** Thermo wins on simple workflow, small panels and a bit faster; Illumina on technology and capacity. Labs that scale move to Illumina.
6. **10x [X, Q3/Q4].** "10x is ahead for now" in single cell and spatial; Illumina is ahead on transcripts per cell, 10x on cells per sample; Illumina "can close it really, really quickly" because customers can try it at low initial cost.
7. **MRD skepticism [X, Q1].** Skeptical outside the US (reimbursement); in-house MRD LDTs "quite difficult"; MRD de-escalation trials "did not pan out." Illumina's agnostic MRD kit needs "a lot of sequencing... high cost," hard to see adoption but "good for revenue" if adopted.
8. **Instruments [X, Q5].** Illumina is loading new applications onto NovaSeq X first and customers see X as "the pinnacle," the opposite of a new box every few years. Smaller instruments: Illumina "[hasn't] really worked that hard to grow that segment."
9. **SomaLogic [X, Q3].** "Absolutely the right strategy" to put more analytes on one box; a lab with a NovaSeq X can add a SomaLogic workflow instead of Olink; NGS-based protein detection in the clinic "is going to be quite some time" away.
10. **Core risk [X, Q5].** Illumina "has not decided whether it wants to be a technology company or... a clinical company," with very few IVD/CDx assays.

### Call 10. Senior Director, Strategic Product Management, Oxford Nanopore (ex-Illumina, Adaptive, 10x) (Tegus)
- **Date:** not stated; **estimate Sep-Oct 2026** (matches the Extracts estimate of about 1 Oct 2026). Basis: refers to the latest earnings round where "Illumina had a great quarter," Nanopore's half-year report (+10-12%), AXELIOS as launched, and pitching Roche at AMP "last November" (Nov 2025).
- **Role / credibility:** At Illumina 2008-2014 (so very old); three years at Adaptive (an Illumina customer running MRD on NovaSeq); four years at 10x; 2.5 years at ONT. A competitor to both Illumina and Roche. States he is "not privy" to Illumina's numbers. Most commercial claims are own math. **Strong on switching mechanics and MRD workflows; weak on Illumina's current economics. Competitor bias against Roche, Ultima and PacBio.**

Key claims:
1. **Growth is diagnostics, research has collapsed [X, Q1/Q5].** "Research-use market has fallen off a cliff"; "Illumina had a great quarter"; the core-lab market "has really been struggling for the last couple of years"; R01 pay line "below 10%" (unchecked). Clinical diagnostic samples in the "low millions... could have been up to double-digit millions" (dated, rough).
2. **Customer concentration [X-hearsay, Q1/Q5].** Illumina's growth is "dominated by roughly 10 or so large sequencing houses" (Natera, Guardant, Tempus, Caris), "maybe 20" drive the bulk of sample volume and revenue. In his Illumina days the 80/20 rule was inverted (genome centers like Broad/Sanger/WashU).
3. **Pricing marks [X-hearsay, Q2].** "Illumina's now at $150 or so per genome," Oxford "at least double that." Roche has said **$150 per human genome**; Roche's reagent footprint is "already... competitive with Illumina." "Nobody's trying to chase Ultima to the bottom of the barrel on pricing"; "Ultima's doomed in the long run anyway"; people are "maintaining their margins for now."
4. **Roche is slow and cumbersome [X, Q4].** Chemistry is "the weakest link": "cumbersome and probably more expensive"; two-box workflow raises capex (though both boxes together cost less than a NovaSeq X); extra operator labor could "offset their pricing advantage." Roche "talking a lot and not saying much... for about two years." Can't do long reads or epigenetics.
5. **Switching mechanics, quantified [X-direct/inference, Q4].** Adaptive's move from NovaSeq 6000 to NovaSeq X took "years"; Adaptive said turning on X made clonoSEQ profitable "a year and a half or two years" after first instruments shipped. Switching an existing LDT entity to another vendor is "a four- or five-year project." A new diagnostic entity takes "six to 10 years (six minimum)" to a CLIA/CAP-ready LDT. Incumbents such as Natera/Guardant have "dozens of instruments per institution or maybe hundreds."
6. **Where Roche could win [X, Q4].** Liquid biopsy and tag-counting (RNA-seq, cfDNA) where read density matters more than length; MRD in T/B-cell cancers is a "slam dunk" fit. Opportunistic entries where an Illumina service contract lapses; reagent-rental placement is possible but capital heavy and fixed reimbursement caps what labs can pay.
7. **Share and size [X, Q4/Q5].** Roche "could probably pick away 10%-20% relatively easily" within about three years, but "I don't think of Roche in the next three years as displacing more than that." Roche sequencing at "$1 billion-$2 billion in a 10-year time horizon isn't crazy" (a "dart at the wall"). Industry perhaps around $5 billion in 10 years; doubling "might be considered a win." Mid-throughput platforms about $500 million-$1 billion of Illumina revenue (an eighth to a quarter), "not the driver"; NovaSeq X "$1 million or more per instrument at pull-through" (period and measure unclear).
8. **Reimbursement caps volume growth [X, Q1].** "The entire industry slows in its growth" because fixed reimbursement per sample has to pay for everything; "hard to see a dramatic increase in the numbers of applications" beyond known ones. Upside case is population-scale epigenetics, needing a funding "renaissance."
9. **Illumina long-read response [X, Q3/Q4].** Illumina launched "Constellation" (he is unsure of the name) at "the beginning of this year": "a bit of a trick," likely worse than Nanopore but could "threaten Oxford's long-read clinical sequencing position a bit." China: "losing the Chinese market" is a headwind for the industry.

### Call 11. Single-Cell Genomic Technology Specialist, Brigham and Women's Hospital core (customer) (Tegus)
- **Date:** not stated; **estimate Aug-Oct 2026** (after the July 2026 AXELIOS launch; weak evidence; the Extracts file's 2026-10-10 date is an assumption).
- **Role / credibility:** About five years running a cellular profiling core; sequences single-cell and spatial libraries on NovaSeq X Plus; hands-on with Nanopore and PacBio; **no hands-on AXELIOS** but has analyzed AXELIOS-sequenced single-cell data. A single academic-hospital core; several statements are about science generally, not Illumina's markets.

Key claims:
1. **AXELIOS data looks equivalent [X-direct, Q4].** On single-cell libraries: reads per cell, saturation, genes detected and error rate (about 0.1% at Q30 for both) were "very similar." Small sample, no public side-by-side data found.
2. **Roche advantages [X-hearsay from advertising, Q2/Q4].** Few-hour runs, same/next-day data, "more competitive prices compared to Illumina," several flow cell sizes (one library to 300 libraries), four parallel runs, easy to run with one or two people.
3. **Illumina's ecosystem is the moat [X-direct, Q4].** "The biggest competitive advantage of Illumina": installation, flow cells, library-prep workflows, bioinformatics, compatibility with 10x and Takara Trekker, community. Researchers: "I will pay more, but I will not switch." Switching is "kind of switching from Windows to Mac." Existing projects (one to two years into a five-year study) have a low chance of switching.
4. **Timeline [X-opinion, Q4].** Roche needs "five years... could take 10 years" to build a real ecosystem; 2-3 years for a couple of good publications; **push out to five to seven years if Illumina cuts price "a little bit"** to match. Large biopharma likelihood to use Roche "four or five out of five"; small academic PI labs "two or three"; interviewer summarized about 50/50 for new projects and 1 in 5 for existing (expert agreed).
5. **Where Roche wins [X, Q1/Q4].** New, large-scale clinical, biopharma and biotech projects; hospital WGS-for-all trends. A large biopharma spent about **$2 million** on a QC study to compare platforms and "will not probably be the major player anymore in the next five, 10 years" (expert's paraphrase of what customers believe). Expects the market to be "more fragmented."
6. **Turnaround and batching [X-direct, Q2].** Her core batches Illumina libraries to fill a flow cell (a couple of weeks), plus about two weeks sequencing, total six to eight weeks to analyzable data. Batching exists because "a 10 billion flow cell is more cost-effective than a 500 million reads flow cell." Smaller Roche flow cells with lower reagent cost remove the need to batch (saves "maybe a week per run").
7. **Single-cell displaced by imaging-based spatial [X, Q3].** Says single-cell sequencing demand at her core "is being replaced by spatial transcriptomics" that "do[es] not use sequencing"; she sees large clinical sample volumes as what remains. (Only partly right; see section c.)
8. **Price response [X-opinion, Q2].** Roche's presence "would drive the sequencing prices lower"; a small Illumina cut "should be enough."

---

## (b) Cross-call synthesis by question

### Q1. Clinical Gb growth and the "plateau" explanations

**What the panel can and cannot tell us.** No expert gave a clinical Gb growth rate. The nearest number is "about 20% clinical consumables growth ex-China for two straight quarters" (call 9), which came from the interviewer, was confirmed loosely by an ex-employee, and describes revenue, not Gb. Treat the panel as a test of the *reasons* given for deceleration, not as a source for the number.

**Where experts agree.**
- Growth is clinical, and clinical growth is concentrated in a small set of large US labs. Call 9 names Natera, Tempus, Caris and Foundation; call 10 says "roughly 10 or so," "maybe 20" sequencing houses drive the bulk of sample volume and revenue; call 8 names BillionToOne, Natera, Guardant and Exact and calls Illumina "just the supplier." Oncology is about half of clinical (calls 1, 7: both guesses at 50% to 60%).
- Academic/RUO demand is weak and not coming back soon (calls 4, 5, 6, 10). Call 5 sees 2026 down about 5% and "less optimistic" than 90 days earlier; call 4 sees its core's underlying volume down about 20% in 2025 and flat in 2026 only because of one contract. The one exception (call 2, +40%) is outsourced NovaSeq X work and single-cell.
- Reimbursement is the clinical gate. Call 6 credits reimbursement for "mak[ing] up for the reduction in academic funding"; call 9 says reimbursement, regulation and physician ordering behaviour (not cost or speed) are the binding constraint; call 10 says fixed reimbursement per sample caps how much the industry can grow.

**Testing the management reasons for volume deceleration.**
| Reason offered | Panel evidence | Verdict from the calls |
|---|---|---|
| Price elasticity fading | Call 8 (ex-ILMN): when X cut the cost per run to "almost half, if not 1/3," customers "ran out of samples"; the backlog of freezer samples was exhausted. Call 9: cost per Gb is not the oncology bottleneck; a $100 genome ignores 120x+ tumor depth, library prep, biopsy and bioinformatics. | **Supported for research and for existing clinical menus.** The claim is that demand per test is not price-elastic once a test is reimbursed. But the evidence on elasticity for *new* tests (whole-genome MRD, population screening) is untested by the panel. |
| NovaSeq X conversion "done" | Call 8: X "replaced a lot of NovaSeq 6000s." Call 4: core waited 12-18 months for X, lost customers on price. Call 7: 6000 "supposed to become obsolete." Call 5: still runs 6000s. Call 10 (Adaptive): conversion at a clinical lab took about two years from first instrument shipment. Call 7: "everyone is going to have a NovaSeq X." | **Partly supported.** No call says the 6000 is gone; several say the remaining tail sits in clinical (long validation cycles) and in labs not yet converted. Conversion lowers revenue per Gb (the same Gb at about a third of the price per Gb), so the Gb-to-revenue relationship matters more than Gb growth alone. |
| Reimbursement | Calls 6, 9, 10: reimbursement is both the engine and the cap. Call 9: outside the US, MRD reimbursement "very, very challenging." | **Supported as a cap on *new* volume; not a reason for plateau on existing tests.** |
| Test-volume growth | Call 8: NIPT penetration 70%-80% (near saturation); cancer "really, really low." Call 10: clinical samples in "low millions" up to double-digit millions. Call 9: community oncology CGP is "the billion-dollar question." Call 8: MRD brings "three to four" tests per patient-year. | **Mixed.** NIPT is mature (volume growth must come from price/mix and international); oncology/MRD is where unit growth lives. |
| Sequencing intensity per test | Call 9: tumors need more than 120x; MRD with an agnostic whole-genome method "needs a lot of sequencing... high cost." Call 8: MRD multiplies tests per patient. Call 6: ancillary costs are rising, not falling. | **Under-addressed by the panel.** The one real signal is that WGS-based MRD and tumor-normal pairs need far more Gb per test than panels, so mix toward WGS would add Gb; mix toward cheap panels and tumor-informed assays would subtract. Nobody gave a per-test Gb figure. |
| Competitors | Calls 10, 11, 7: switching takes years (four to ten); no credible clinical share loss near term; Roche 10-20% in three years at most. | **Not a 2026-27 volume driver for the largest clinical labs.** More relevant to price (Q2/Q4) than volume. |

**Best numbers.**
- NIPT penetration 70-80% [X-hearsay, call 8]; oncology about 50-60% of clinical mix [X-hearsay, call 1]; clinical 52% of ILMN revenue at Sep 2024 [X-direct, call 8].
- Top 10 to 20 labs drive the bulk of volume [X, call 10]; loose definition of "clinical" with most volume as LDTs not IVD [X, call 9].
- Research cores: -5% (call 5), about flat ex-contract with -20% in 2025 (call 4), +40% outsourced (call 2).

**Disagreements.** Call 2's 40% growth versus calls 4 and 5's flat-to-down is the clearest split; the likely reconciliation is that cheap outsourced NovaSeq X capacity (MedGenome, Novogene) is capturing the growth while in-house research cores lose. Call 8 is bullish for two to three years on clinical; call 9 is skeptical of MRD durability outside the US.

### Q2. Is Illumina over-earning? NovaSeq 6000 tail and pricing

**What the experts say about the price gap.** Call 8 gives the most direct number: X delivers four 6000s' output at "almost half, if not 1/3" run cost, consistent with the roughly 3x earn-per-Gb gap you describe. Call 4 gives a live example of the gap hurting an in-house core: customers left because the core was still on a 6000 and "the difference in price drove a lot of our customers to be seeking vendors that could provide X Plus prices."

**The 6000 tail.** Call 7 ("supposed to become obsolete... opportunity for a lot of other companies") and call 4 (core is sunsetting its 6000) point the same way: as the 6000 tail converts, the buyer is converted to a platform that earns Illumina roughly a third as much per Gb, and the window in which rivals can pick up those users is during the migration. No expert said what share of 6000 Gb is clinical; call 10's Adaptive example suggests clinical labs migrate slowly (two years), which supports the claim that the tail is mostly clinical and will convert gradually.

**Prices that rivals and providers are quoting.**
- Outsourced NovaSeq X lane pricing: "under $1,800" and "under $2,000" per lane, "under $4,000 per lane" for 10B/25B lanes, flat to slightly down (call 2).
- Genome pricing marks: Illumina "$150 or so" (call 10); Roche duplex 30X genome "$150" (calls 6, 10); Element and Ultima sub-$100 claims (calls 1, 9); Nanopore at least double (call 10).
- Capital: NovaSeq X "almost $1 million" (call 6), "$1.2 or something" list (call 7); AXELIOS $750,000 (call 6), two boxes cheaper than a NovaSeq X (call 10); MiSeq i100 Plus "over $100,000" (call 4); PacBio Vega $175,000 (call 4).

**What happens to consumables pricing.**
- Rivals at parity on price per genome, not below: calls 5 (AXELIOS "on par, if not a little bit cheaper"), 7 ("everyone is at around the same price point"), 10 (no one chasing Ultima to the bottom). That is consistent with a near-term pricing floor set by Roche/Element rather than a collapse.
- The deeper risk is Ultima for pure Gb economics (calls 4, 8, 2). Call 4 gives the only observed share-of-lost-work trend (Ultima 10% to about 20% of the lost work), but on a small base; Novogene is 80-90%.
- Illumina's response levers named: individualized quotes and "huge discounts" on NovaSeq X (call 2), broken promised discounts (call 4), and the expectation that a small price cut would neutralize Roche (call 11: five-to-seven year timeline if Illumina matches).
- The 35B flow cell (call 5, January 2027) "may further reduce the price of sequencing" with no pricing yet. That is the next visible event for price per Gb.
- Illumina's own stance (call 8): it will not chase the lowest dollar per base. Call 6 adds that ancillary software and storage costs are rising, so effective all-in price per genome is not falling as fast as the headline price.

**Where the experts disagree.** Call 10 and call 7 imply no price war; call 11 and call 8 imply price cuts are likely over time. Nobody quantified an expected price per Gb for the 25B or 35B flow cell, or the 6000 versus X pricing in dollars.

### Q3. Multiomics uptake (SomaLogic, single-cell, spatial, 5-base, TruPath, software)

**Actual or intended uptake in the calls.** All numbers below are stated intentions from academic cores, not purchases.
- **TruPath / synthetic long reads:** 5%-6% of one core's volume by end 2026, from two or three cancer biology labs (call 2, "very likely"); "Maybe one or 2%" and "somewhat likely" at the largest academic genome center, limited by price (call 5); "not at all likely" at a core that already uses PacBio for complex loci (call 4). So 0-6%, central estimate 1-2% of volume at two cores, not a revenue figure.
- **PIPseq (single-cell):** under evaluation at call 5's center with "potential competitive advantage against 10x in some scenarios." No volumes given.
- **SomaLogic / Illumina Protein Prep:** call 5 "potentially interested," currently on Olink; call 2 says price per sample too high for small cores; call 4 "unlikely to change our use"; call 6 sees little proteomics emphasis since the acquisition; call 9 says it is the right strategy but clinical use is a long way off; call 3 says depth and reproducibility are weak (hearsay). **No call reports an actual Soma purchase.**
- **5-base methylation:** call 5 "of interest"; call 2 likes the Illumina methylation kit; call 6 says Illumina is marketing itself as a five-base sequencer; call 10 argues Nanopore reads methylation natively and Roche cannot.
- **Spatial (StrataMap):** call 3 "Not the Illumina one"; call 1 "exploratory" and more expensive reads; call 9 says Illumina is ahead on transcripts per cell but 10x leads; call 5 sees 10x Atera as the thing to watch.
- **Single-cell sequencing demand:** call 2 says single-cell is driving +40% Gb at one core, boosted by cheaper 10x competitors; call 5 says 10x Flex is "really lowering the cost of single-cell prep"; call 11 says single cell is being replaced by imaging-based spatial.
- **Software (DRAGEN, Connected Analytics):** call 9 calls DRAGEN the de facto standard secondary-analysis tool and "very important" but under-marketed; call 5 says DRAGEN consolidation is a "value add" for labs without existing alternatives; call 6 questions whether $150-genome claims include analytics and storage cost.
- **Cloud / data:** call 2 praises the HIPAA-compliant integrated pipeline.

**Verdict on the "1-2 points of growth".** The calls give no purchase data that supports 1-2 points. They do show real interest from large academic centers, but those buyers are in the weakest part of the business, and the dollar value per customer is unknown. The most credible near-term contribution is sequencing-volume pull-through (TruPath at 1-6% of two cores' volume, single-cell depth), not Soma. Ex-employees (calls 8, 9) accept multiomics as a short-term strategic fit; call 8's reading is that multiomics exists because genomics hit sample saturation, which is a defensive rationale. Call 6 is the most negative on innovation momentum.

**Agreement / disagreement.** Agreement: the multiomics strategy is rational and customers like one-box convenience in principle (calls 5, 8, 9). Disagreement: whether customers will pay (call 2: price too high; call 5: TruPath is "expensive"), whether Illumina's single-cell and spatial offerings can beat 10x (call 3, 7: no; call 5, 9: maybe), and whether sequencing-based protein measurement is durable (call 8: no).

### Q4. Competition, switching costs, share shifts, China

**Agreement across nearly all calls.**
- Illumina is deeply entrenched and displacement is slow (calls 6, 7, 8, 10, 11 strongest). Reasons: validation, bioinformatics, EHR connections, support, staff training, risk aversion in clinical, and installed base 80%+ (call 8).
- Competitors win in niches: Ultima at high-throughput research providers (calls 4, 8), Element in small and mid-tier cores (calls 2, 4, 8), Roche in time-critical clinical and liquid biopsy (calls 5, 6, 10), Thermo in small panels (calls 7, 9), long reads in rare disease/complex loci (calls 3, 4, 6, 8).
- The most likely buyer behaviour is *adding* a rival box next to many Illumina boxes (calls 6, 7: "one versus maybe six NovaSeq Xes"), not replacing.

**Switching costs, best numbers.**
- Side-by-side comparison "a month or two" (call 1, start-up view).
- New LDT platform validation: NovaSeq 6000 to X took Adaptive "years"; changing vendor for an existing LDT "four or five years"; a new entity "six to 10 years (six minimum)" to a CLIA/CAP LDT (call 10).
- Roche to build a real ecosystem: five to ten years; five to seven if Illumina cuts price (call 11); three-year share capture 10%-20% at most (call 10).
- Large biopharma willing to spend about $2 million on a QC study to evaluate a platform (call 11).
- Short-read to short-read is a "lighter lift"; to long-read a "much bigger lift" (call 6).

**Share shifts.**
- Roche: 10%-20% of Illumina's *clinical mega-provider base* in three years at most (call 10); "minimal" first-year impact (call 5); "die out" (call 2); Illumina not major player in 5-10 years per a biopharma customer (call 11 hearsay). Wide range, no one has data.
- Ultima: 10% to 20% of one core's lost work (call 4), plus testing at the largest academic center (call 5). Call 10 disagrees ("doomed").
- Element: flat share (call 4) but gaining in small cores (calls 2, 4). One core intends to move 80% of in-house work (call 2).
- Overall: calls 2 and 5 say share loss is real but small; call 7 says no clinical lab leaves; call 11 and call 3 are the most bearish.

**China / MGI.** Little direct evidence. Call 2 claims MGI has been separated from BGI into a non-Chinese owner and is "aggressively offering" instruments (unverified). Call 3 names BGI as ahead in spatial. Call 10 lists "losing the Chinese market" as an industry headwind. There is no panel data on Illumina's China business.

**Disagreement on Roche.** Calls 5, 6 and 11 (users who have seen data) are impressed by the data and the economics, and call 11 and call 5 each plan to buy boxes or trial. Calls 10 and 2 (a competitor and a skeptical core) say the chemistry is complex or the product will not find space. Call 6 says "a lot of hype without a lot of data." The most precise common ground: data quality looks fine, speed is the differentiator, price is at parity-to-slightly-below, and the question is ecosystem and clinical validation time.

### Q5. Variance to Wall Street estimates

Because the experts are mostly research customers and competitors, the signals most relevant to variance are directional rather than quantitative.

- **Consumables growth.** Research is soft: call 5 (-5% 2026, outlook down vs 90 days ago), call 4 (flat, hidden decline), call 6 and call 10 (RUO "fallen off a cliff"). Clinical is strong: call 6 (reimbursement offsets), call 9 (+20% ex-China two quarters, big accounts, MRD), call 10 ("Illumina had a great quarter"). The aggregate depends on the mix; none of the experts attempted that. Call 2's +40% is the outlier and is Illumina-flow-cell volume sold through third parties.
- **Pricing.** No Illumina list or volume price changes in the last 90 days at three customers (calls 2, 4, 5); call 5 says price changes usually come at the start of the calendar year. Providers' per-lane prices flat to slightly lower (call 2). The January 2027 pricing round and the 35B flow cell launch are the two catalysts the panel points to.
- **Placements.** NovaSeq X Plus replacement/expansion appears limited in research (call 5: "no plans"). Smaller instruments: i100 Plus cost "over $100,000" limits adoption (call 4); Element picking up small cores (calls 2, 4). Roche AXELIOS: call 5 plans a couple of boxes, call 6 says pre-orders focused on high-throughput centers. No data on Illumina placement counts.
- **Margins.** Call 8's concern: the largest clinical customers have bargaining power and a rival could pitch "cut your cost by half"; Illumina cannot win a price race given a bigger burn rate. Call 6: ancillary costs rising. Call 4: sales execution slipping (rep turnover, unkept discounts) which could hurt instrument orders and goodwill.
- **Estimates risk, in plain words.** Upside to estimates would come from clinical oncology/MRD, X pull-through and early TruPath volume; downside from academic funding in 2027 (call 2, call 5), a 35B-flow-cell-driven price cut, Roche pricing in clinical tenders, and NovaSeq 6000 conversion at a third of the revenue per Gb.

---

## (c) Claims that look wrong, stale, or contradicted

1. **Call 6: "Illumina retired their MiSeq."** Contradicted by calls 4, 7 and 9, which describe the MiSeq i100 Plus (call 4 is buying one; call 7 calls it "the latest"; call 9 says "the new MiSeq is really, really fast"). Probably refers to the older MiSeq/MiSeqDx line. Stale or loosely stated.
2. **Call 8: "Thermo acquiring Olink was a really direct response" to Illumina's SomaLogic deal.** Chronology looks wrong. To my knowledge Thermo's Olink acquisition was announced in Oct 2023 and closed in 2024, well before Illumina's SomaLogic deal (2025) [Analyst: verify in Core Notes]. Call 9 handles it better ("sets up a new battleground").
3. **Call 8's "ran out of samples / sequenced everything in the freezer"** is a 2023-24 observation from an ex-employee who left Sep 2024. It conflicts with call 2 (+40% Gb at a core, single-cell driven) and with calls 9 and 10 (clinical at +20% consumables). Plausibly correct for research and for the 2023-24 transition, but should not be applied to 2026 clinical.
4. **Call 3: "98.5%" confidence that GeneDx adopts long-read.** The expert says he made up some numbers; the long-read thesis is also contradicted by calls 7, 8 and 6 (long-read stays a niche complement; clinical long-read lacks reference databases and software). Treat as colorful opinion, not a probability.
5. **Call 3: long reads "need less computing power" and "quality is as good" as short-read assembly; and "GRAIL was spun off to build IVD."** First two are generalizations not supported elsewhere (call 6 says long-read informatics is a "major bottleneck"); the GRAIL account is a simplified account.
6. **Call 3's claim that Roche tried to buy Illumina about 8 to 10 years ago** is explicitly rumor.
7. **Call 11: spatial transcriptomics "do[es] not use sequencing" and single-cell is being "replaced" by it.** Overgeneralized: imaging-based spatial (e.g. the probe/fluorescence systems the expert likely means, and 10x Atera per call 5) bypasses sequencing, but sequencing-based spatial (including Illumina's StrataMap and Visium-class assays) does not. It is a risk factor worth flagging for Q3, not a fact about the whole market. Same call: "single-cell sequencing has been around for the last two years" is wrong (more than a decade); the claim that hospitals in the UK sequence every patient's genome is also overstated.
8. **Call 2: MGI "demerge" into a Swiss company, Nanopore discontinuing PromethION 2 and Flongle, and Illumina having "lost several lawsuits."** All recollections that I cannot verify from the files; the MGI claim in particular runs against the usual understanding that MGI Tech remains a BGI-affiliated, China-listed company. Flag for checking before it is used in the China discussion.
9. **Call 2's +40% (one core) and the "at least 40%" spending line** should not be extrapolated: ambiguous year, outsourced provider pricing, a single-cell surge at one core.
10. **Call 2 calls AXELIOS "will die out"; call 11 expects Illumina not to be the major player in 5-10 years.** Both are extreme and unsupported by quantitative data; call 5's and call 10's middle view (small near-term share, larger long-term risk) is better grounded.
11. **TruPath is described inconsistently.** Calls 2, 4 and 5 describe it as native synthetic long reads / short reads plus additional data; call 6 calls it "a multiomic solution using a separate chemistry"; call 10 calls the long-read product "Constellation" (he is unsure of the name). Also call 3 dates the launch to JPM 2024 and call 10 to the start of 2026. The product naming and launch date need confirmation from Core Notes before use.
12. **Extracts error (not an expert error):** the Extract for call 7 says AXELIOS is "Element's." The transcript is explicit that the expert works at Roche and AXELIOS is Roche's. Also, the Extract dates for calls 9 and 11 (2026-01-15 and 2026-10-10) are assumptions; the transcripts are undated.
13. **Call 9: the "20%" and ">65% clinical consumables" figures are the interviewer's.** The expert asked what the 20% meant. These should not be cited as expert-confirmed company data.
14. **Call 6's inference that Illumina "raised their guidance" because clinical is picking up.** No numbers or period; an outside inference by a competitor employee.
15. **Call 1's Thermo "10%-15%" share, oncology "50%-60%" and NIPT "10%-20%" splits.** Unsourced guesses from an expert who says they are not an expert; use only as directional.
16. **Call 10's financial estimates** (PacBio about $150 million, Nanopore under $500 million, Illumina "$4+ billion," Roche $1-2 billion in ten years) are his own rough numbers; PacBio "not long for this world" is a competitor's opinion about another competitor.
17. **Call 7 (Roche employee) feature claims** (one sensor module vs four flow cells; 30 minute to four hour runs) are vendor marketing and unverified.
18. **Contradictions on AXELIOS capability:** call 8 says Roche claims it will pursue long reads and call 10 says its chemistry "is really not meant for" long reads or epigenetics; call 6 says reads up to about 1,000 bases (not long-read). Roche's claimed roadmap and the chemistry's real capabilities should not be assumed.
19. **Call 2: "Illumina and Element now offering 600 base pair reads"** presumably refers to paired-end 2x300; the comparison to AXELIOS' 1,000-base single reads is the expert's and not checked.

## Files

- Analysis: `C:\Users\palaz\OneDrive\Documents\ILMN Claude Code Local Folder\Working Notes\Outputs\analyses\2026-10-11_ilmn_primer_working\02b_expert_calls.md`
- Originals read: `Working Notes\Sources\ILMN\expert_call\` (the 11 files named in the brief); extracts read from `Working Notes\Extracts\ILMN\expert_call\`.
