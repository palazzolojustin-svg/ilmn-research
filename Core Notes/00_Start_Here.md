# Start Here: Illumina Research Core Notes

*As of 2026-10-10.*

## How these notes are organized

This folder is a research workspace on Illumina (ILMN) and its publicly traded competitors. It has three layers. The **Core Notes** are a master briefing to read first. The **Working Notes** hold every source document plus a readable extract of each. The **Outputs** folder holds everything produced later in chats.

### The folder

| Location | What it holds |
|---|---|
| `CLAUDE.md` | The operating rules Claude Code follows in every chat opened on this folder. |
| `Core Notes/` | This master briefing, read first in every chat. |
| `Working Notes/INDEX.md` | One entry per source document, with a short summary and links. Start here to find material. |
| `Working Notes/Extracts/` | An exhaustive, readable note for every source document, filed by company and type. |
| `Working Notes/Sources/` | The original documents, renamed and filed by company and type. Use these when exact wording, tables or figures matter. |
| `Working Notes/Outputs/` | Everything produced later: datasets, artifacts, primers and analyses. |
| `Working Notes/_Archive/` | Duplicates and off-topic files kept out of the analysis. |
| `Inbox/` | Drop new files here, then run `python _Build/build.py ingest`. |
| `_Build/` | The build script, its state file and its log. |

### The Core Notes files

The Core Notes run in numeric order. Files 01 to 08 cover Illumina itself, file 09 compares the whole market, and files 10 to 15 cover one competitor each.

| File | What it covers |
|---|---|
| `00_Start_Here.md` | This file: folder guide, one-page orientation, master timeline, glossary, and source coverage and gaps. |
| `01_ILMN_Company_Primer.md` | What Illumina does and how it makes money: technology, products, customers, geography, business model, reporting, history and balance sheet. |
| `02_ILMN_Financial_History_and_Guidance.md` | Reported results over time and how management's guidance moved. |
| `03_ILMN_Consensus_Estimates.md` | What Wall Street analysts on average expect for future revenue, margins and earnings. |
| `04_ILMN_Earnings_Calls_2023-2024.md` | Quarterly earnings calls from Q1 2023 to Q4 2024: the GRAIL fight, the NovaSeq X launch and the guidance cuts. |
| `05_ILMN_Earnings_Calls_2025-2026.md` | Quarterly earnings calls from 2025 to mid-2026: China, tariffs, SomaLogic and the return to growth. |
| `06_ILMN_Conferences_and_Investor_Events.md` | Management remarks at investor conferences, such as J.P. Morgan, Evercore, Wolfe and TD Cowen, and at strategy days. |
| `07_ILMN_Expert_Calls.md` | Interviews with former employees, customers and competitors' staff, mostly from July and August 2026. |
| `08_ILMN_Equity_Research.md` | Analyst research and ratings from J.P. Morgan, Barclays, UBS, Freedom Broker, Ameriprise, Bloomberg Intelligence and others. |
| `09_Competitive_Landscape.md` | A cross-company view of the sequencing market, segment by segment. |
| `10_Peer_Oxford_Nanopore.md` | Oxford Nanopore (ONT), the nanopore long-read company listed in London. |
| `11_Peer_PacBio.md` | PacBio, the high-accuracy long-read company. |
| `12_Peer_Roche.md` | Roche, whose new AXELIOS sequencer entered the market in 2026. |
| `13_Peer_Thermo_Fisher.md` | Thermo Fisher, owner of the Ion Torrent sequencers and the Olink proteomics business. |
| `14_Peer_10x_Genomics.md` | 10x Genomics, the leader in single-cell and spatial biology. |
| `15_Peer_MGI_Tech.md` | MGI Tech, the Chinese sequencing company that dominates its home market. |
| `16_Addendum_Clinical_Consumables_Thesis.md` | Addendum (2026-10-11): whether Illumina is over-earning on clinical consumables as the NovaSeq 6000 converts to the X, clinical volume growth versus price declines, management conduct, and customer and competitor read-through, with all evidence listed. |
| `17_Addendum_Open_Offer_Pricing_Power.md` | Addendum (2026-10-11): what the Open Offer contracts let Illumina do on price with big US oncology customers (real-price freeze, most-favoured-customer terms), customer by customer. |
| `18_Addendum_Thesis_Scrape_Alt_Data.md` | Addendum (2026-10-12): new alternative-data evidence from the overnight web scrape on the short thesis: the 6000 mix shift, accelerating discounts, slowing volume and research pricing, with the main counter-evidence, gaps and a map of sources tried. |

## Illumina and its market in one page

### What DNA sequencing is

Every living cell carries instructions written in DNA, a long molecule built from four chemical "letters" (A, C, G and T). **DNA sequencing** means reading the order of those letters. A human genome, the full set of a person's DNA, is about three billion letters long. Cheap, fast sequencing lets scientists study disease and lets doctors find the mutations driving a patient's cancer. It also lets labs screen pregnancies for chromosomal problems and helps breeders improve crops and livestock.

Illumina leads the market for **next-generation sequencing (NGS)**, which reads millions of short DNA fragments in parallel. Its chemistry is called **sequencing by synthesis (SBS)**. The machine copies each fragment one letter at a time using chemically tagged building blocks, and a camera records which letter was added at each step. This approach is called **short-read** sequencing because each fragment is only a few hundred letters long. The technology came from Solexa, which Illumina bought for $480 million in 2007. Bloomberg Intelligence (BI) calls that deal possibly "one of the best health-care deals in history" [BI, 2025-11-13].

Costs have collapsed. In 2014 the HiSeq X Ten broke the $1,000-per-genome barrier. The current flagship, the NovaSeq X, can produce a human genome for as little as about $200 [10-K FY2025].

### What Illumina sells and how it makes money

Illumina sells four kinds of things:

- **Instruments**, the sequencing machines. They range from small benchtop MiSeq units to the factory-scale NovaSeq X.
- **Consumables**, the reagent kits and flow cells customers must buy for every run. A **flow cell** is the glass slide on which DNA is read.
- **Services**, such as sequencing done in Illumina's own labs and support contracts.
- **Software**, notably DRAGEN, which turns raw machine output into a list of genetic variants.

Illumina runs a "razor and razor blades" model. Each machine placed with a customer generates years of consumable purchases. Consumables were $3,227 million in FY2025, or 74% of revenue. That share was up from 68% in FY2023 [10-K FY2025].

The key operating measures are:

- the **installed base**, about 21,000 active instruments at FY2025 [JPM, 2026-01-13];
- **pull-through**, the yearly consumables revenue each machine generates.

A NovaSeq X pulls through about $1.35 million a year, roughly twice a NovaSeq 6000 and about 15 times a NextSeq [Q4 2025 deck].

FY2025 revenue was $4,343 million. That was flat against FY2024 on a "Core" basis, which excludes GRAIL, the cancer-test company Illumina was forced to divest. FY2025 **non-GAAP** earnings per share (EPS, profit per share after management's adjustments) were $4.84, up from $4.16 [Q4 2025 deck].

Growth returned in late 2025. Q2 2026 revenue of $1,159 million was up 6.5% **organically**, meaning excluding currency moves and acquisitions [Q2 2026 slides]. In July 2026 management raised its FY2026 guidance to:

- revenue of $4.60–4.64 billion;
- non-GAAP EPS of $5.30–5.40.

The analyst consensus snapshot of 2026-10-10 sits inside both ranges: revenue of $4,624.8 million and adjusted EPS of $5.36 [Bloomberg consensus, 2026-10-10].

### Who the customers are

Customers fall into two broad groups:

- **Research & Applied** customers include universities, government labs, genome centers, drug companies, agriculture and consumer genomics.
- **Clinical** customers are hospitals and diagnostic labs that test patients for cancer, inherited disease and pregnancy-related conditions.

The two groups are moving in opposite directions. Outside China, clinical consumables grew 12% in FY2025 and 15% in Q2 2026. Research & Applied fell 7% in both periods [Q4 2025 and Q2 2026 slides]. Much of the clinical growth comes from cancer blood tests, such as **minimal residual disease (MRD)** testing, which looks for traces of cancer left after treatment.

Sources disagree on clinical's size. Management put it at about 40% of sequencing consumables [JPM, 2026-01-13]. BI later said it was more than 65% [BI, 2026-07-31]. A former manager called the figure "a very loose statement" because Illumina classifies clinical generously [Expert: former Illumina senior manager, est. Jan 2026].

Clinical brings two features worth noting:

- **Concentration.** Clinical volume is concentrated in roughly 10–20 large labs, such as Natera, Guardant, Tempus and Caris. These labs have real bargaining power [Expert: ONT senior director, ~Oct 2026].
- **Stickiness.** Moving a validated clinical test to a new machine can take months to years and cost from $100,000 to tens of millions of dollars [Expert calls, Jul–Aug 2026].

### Who the competitors are

Illumina now faces a different rival in almost every part of its market:

- **High-volume short reads:** Roche's new AXELIOS 1, launched for research use on 29 June 2026 at a claimed $150 per genome [Roche DX Day, 2026-05-12], and privately held Ultima Genomics.
- **Mid-sized labs:** privately held Element Biosciences, with its AVITI and new VITARI machines.
- **Long reads (much longer continuous stretches of DNA):** Oxford Nanopore and PacBio.
- **China:** MGI Tech.
- **Single-cell and spatial biology:** 10x Genomics.
- **Proteomics (measuring proteins):** Thermo Fisher, through Olink.

A former Illumina associate director summarized the problem this way: "they're trying to compete with many companies, while these competitors are only competing with Illumina" [Expert: ex-Illumina AD now at Kailos, Aug 2026].

### The key debates right now

**Price versus volume.** Each cut in the price per gigabase (a billion DNA letters) now brings less extra volume than in the past. One former employee dated "real flat growth" in core sequencing to about 2022 [Expert: ex-Illumina AD, 23 Jul 2026]. Some analysts think Illumina is quietly "trading price for volume" [BI, 2026-05-01; Barclays, 2026-04-30]. Management calls that reading noise. J.P. Morgan's survey of 62 customers implied only modest price cuts [JPM, 2026-06-10].

**How dangerous Roche is.** Views range widely. UBS called Roche's pricing "relatively benign" [UBS, 2026-02-26]. Barclays sees "another round of pricing headwinds in 2027 and beyond." Experts range from "will just simply die out" to 10–20% market share within three years. Roche's CEO said about one-third of roughly 100 first-year placements had been made by September [JPM, 2026-09-15].

**Whether the recent strength lasts.** NovaSeq X placements beat Illumina's quarterly framework of 50–60 units, with more than 100 in Q4 2025 and more than 95 in Q2 2026. Barclays and Seeking Alpha ask whether customers pulled purchases forward ahead of AXELIOS. Management calls it "a very healthy market."

**China.** China placed Illumina on its "unreliable entities list" in February 2025. Greater China revenue fell 21% in FY2025, to $243 million, and management guides it to about $210–220 million in FY2026.

**New businesses.** Management's push into multiomics (measuring several biological layers, such as DNA, RNA and proteins, from one sample) includes:

- the SomaLogic proteomics acquisition, closed 30 January 2026;
- the BioInsight data and AI unit.

Experts like the strategy, but early customer uptake is thin [Expert calls, Jul–Aug 2026].

**The 2027 targets.** Management targets, by FY2027:

- high-single-digit revenue growth excluding China;
- a non-GAAP operating margin of about 26%;
- double-digit-to-teens EPS growth.

BI called the goal "increasingly visible" [BI, 2026-07-31].

**Analyst views.** As of the latest notes, analysts are split:

| Firm | Rating | Price target |
|---|---|---|
| J.P. Morgan | Overweight | $230 (2026-07-31) |
| Barclays | Underweight | $160 (2026-07-31) |
| Freedom Broker | Hold | $185 (2026-08-05) |
| Ameriprise | Buy | — |
| Seeking Alpha | Hold | $188 fair value (2026-09-08) |

## Master timeline

This timeline merges every dated event in the sources into one chronological list, grouped by year. Exact dates appear where the sources give them; "month only" or "approximate" means the sources give only a rough date. Where sources disagree, the entry says so. For 2026, Illumina events and peer events are interleaved by date so the competitive context is visible.

### Before 2020

- **2007:** Illumina bought Solexa for $480 million, acquiring the sequencing-by-synthesis technology that underpins its business today [BI, 2025-11-13].
- **Q3 2011:** The first MiSeq benchtop sequencer shipped [Q4 2025 deck].
- **2012:** U.S. budget sequestration (automatic federal spending cuts) and a federal shutdown temporarily capped Illumina's growth, showing its dependence on government research funding [BI, 2025-11-13].
- **2014:** The HiSeq X Ten became the first system to break the $1,000-per-genome barrier, and the NextSeq 500 first shipped in Q1 [BI; Q4 2025 deck].
- **Q1 2015:** The NextSeq 550 first shipped [Q4 2025 deck].
- **2015-08-18:** Illumina announced Helix, a consumer-genomics venture backed by $100 million from two venture investors [BI, 2025-11-13].
- **2016:** Illumina formed GRAIL to develop a blood test for early cancer detection, and the MiniSeq first shipped in Q1 [BI; Q4 2025 deck].
- **Q1 2017:** The NovaSeq 6000 high-throughput sequencer first shipped [Q4 2025 deck].
- **2018:** The iSeq 100 first shipped in Q1, and Illumina announced a plan to acquire PacBio [Q4 2025 deck; Barclays].
- **2019:** Illumina deconsolidated Helix, removing it from its financial statements; BI called this "a prudent step to tighten the portfolio" [BI, 2025-11-13].

### 2020

- **2020-02-05:** The board authorized a $750 million share repurchase, of which only $15 million later remained [10-K].
- **Q1 and Q4 2020:** The NextSeq 2000 (Q1) and NextSeq 1000 (Q4) first shipped [Q4 2025 deck].
- **2020:** Illumina abandoned its PacBio acquisition after U.S. Federal Trade Commission (FTC) opposition [Barclays], and Roche bought Stratos Genomics, the source of its later sequencing-by-expansion (SBX) chemistry [Roche sources].

### 2021

- **2021-03-08 and 2021-03-23:** Illumina entered a $750 million revolving credit facility and issued $500 million of notes due 2023 and $500 million due 2031 [10-K].
- **2021-05-20:** Ameriprise added Illumina to its Recommended List as a Buy at $385.31 [Ameriprise].
- **2021-08-18:** Illumina completed its reacquisition of GRAIL without first obtaining European Union approval, setting off a multi-year regulatory fight [10-K; BI].
- **Q3 2021:** Illumina's market capitalization peaked at $76 billion, against $1.8 billion when the Solexa deal was announced [BI, 2025-11-13].
- **2021-11-10:** J.P. Morgan initiated coverage of Oxford Nanopore at Overweight [JPM].

### 2022

- **2022-06-09:** CFO Sam Samad departed and Joydeep Goswami became interim CFO [10-Q].
- **2022-07-13:** The EU General Court ruled that the European Commission (EC) had jurisdiction over the GRAIL deal [10-Q].
- **2022-07-14:** Illumina settled patent litigation with BGI/Complete Genomics (MGI's parent and its U.S. unit) for $325 million, paid on July 25 [10-Q].
- **2022-07-19:** The EC issued a Statement of Objections (a formal charge) for closing GRAIL during review, and Illumina accrued a $453 million fine [10-Q].
- **July 2022:** GRAIL's NHS-Galleri trial completed enrollment of 140,000 participants [10-Q].
- **2022-09-01:** An FTC administrative law judge ruled in Illumina's favor on GRAIL [10-Q].
- **2022-09-06:** The EC prohibited the Illumina–GRAIL acquisition [10-Q].
- **~2022-09-29:** Illumina unveiled the NovaSeq X at its Genomics Forum, at its lowest-ever cost per gigabase and with 2.5x prior throughput [BI].
- **~October 2022:** Illumina's investor day set targets of mid-teens growth and a 25% operating margin, and sized its addressable markets at more than $125 billion with 34% research capture by 2027 [BI; 10-Q]. These targets were later abandoned.
- **2022-11-03:** Illumina recorded a $3,914 million impairment (write-down) of GRAIL goodwill and guided 2022 revenue flat to up 1% [Q3 2022 10-Q].
- **November 2022:** Illumina announced its first cost-cutting actions [10-Q].
- **2022-12-13:** Illumina issued $500 million of 5.80% notes due 2025 and $500 million of 5.75% notes due 2027 [10-K].

### 2023

- **2023-01-04:** Illumina replaced its credit line with a new $750 million revolving facility maturing in January 2028 [10-K].
- **2023-02-07:** Original 2023 guidance called for 7–10% consolidated revenue growth and non-GAAP EPS of $1.25–$1.50 [Q4 2022 call]; J.P. Morgan rated the stock Neutral with a $271 target on 2023-02-08.
- **2023-02-17:** The FY2022 10-K reported revenue of $4,584 million (up 1%) and a net loss of $4,404 million, driven by GRAIL impairments [10-K FY2022].
- **March 2023:** The first NovaSeq X Plus systems shipped to customers [Q4 2025 deck], and Illumina repaid its $500 million 2023 notes on March 23. Around this time Illumina announced its first long-read sequencing offering (month approximate) [conference transcripts].
- **2023-03-31:** The full FTC ordered Illumina to divest GRAIL [10-Q].
- **2023-04-25:** On the Q1 call, management reported 67 NovaSeq X shipments, raised its 2023 X target above 330 and announced more than $100 million of cost cuts [Q1 2023 call].
- **June 2023:** CEO Francis deSouza departed amid an activist proxy contest by Icahn, and Charles Dadswell became interim CEO; an 8-K disclosed headcount and real-estate reductions [Q2 2023 call; 8-K].
- **2023-07-12:** The EC fined Illumina €432 million for closing GRAIL during review [10-Q].
- **2023-08-09:** Management cut 2023 guidance to roughly flat Core revenue from 6–9% growth, despite 109 NovaSeq X shipments [Q2 2023 call; UBS summit, 2023-08-17].
- **2023-08-15:** Illumina repaid $750 million of convertible notes in cash [10-Q].
- **2023-09-25:** Jacob Thaysen became CEO [Q3 2023 call].
- **2023-10-12:** The EC adopted its GRAIL Divestment Decision [10-K].
- **2023-10-17:** Icahn Partners filed the first Delaware derivative suit (a shareholder suit brought on the company's behalf) against directors over GRAIL [10-K].
- **Late October 2023:** Illumina launched the 25B flow cell, the largest NovaSeq X consumable [Q3 2023 call]. Some sources say late November or Q4.
- **2023-11-09:** Management cut 2023 guidance a second time, lowered NovaSeq X shipments to 330–340, recorded an $821 million GRAIL impairment and formed a board special committee on GRAIL [Q3 2023 call; 10-Q].
- **2023-11-10:** Analysts slashed price targets after the stock collapsed: J.P. Morgan to $110, UBS to $111 and Barclays to $48.59 (adjusted) [research notes].
- **2023-11-11:** The first federal securities class action over GRAIL was filed [10-K].
- **2023-11-29:** New CEO Thaysen ruled out large acquisitions and said China was about 10% of revenue [Piper Sandler conference].
- **2023-12-15:** The U.S. Fifth Circuit vacated the FTC's GRAIL order and sent it back for reconsideration [10-K].
- **2023-12-17:** Illumina announced it would divest GRAIL [10-K].
- **Late 2023:** Illumina acquired Partek, a multiomics analysis software company [conference transcripts].
- **FY2023:** The year ended with consolidated revenue of $4,504 million (down 2%) and GAAP EPS of −$7.34 [10-K]. The FY2025 10-K gives FY2023 revenue of $4,438 million, apparently on a different basis.

### 2024

- **2024-01-09:** Illumina pre-announced a Q4 2023 beat, 352 NovaSeq X shipments for 2023 and $175 million of cost savings [JPM conference].
- **January 2024:** Illumina launched the NovaSeq X 1.5B kit, and a further workforce cut brought cumulative role reductions to about 12% [Q4 2023 call].
- **2024-02-02:** A California state class action was filed over GRAIL registration statements [10-K].
- **2024-02-08:** Management guided 2024 to flat Core revenue and about a 20% operating margin [Q4 2023 call]. Freedom Broker rated the stock Hold with a $150 target on 2024-02-09.
- **February to April 2024:** Further Delaware derivative suits were filed by the City of Omaha (February 26) and the City of Roseville (April 16) [10-K].
- **March 2024:** XLEAP-SBS chemistry and the P4 flow cell launched on the NextSeq 1000/2000, and the marketing and commercial teams merged [Q1 2024 call].
- **April 2024:** The EC approved Illumina's GRAIL divestment plan, and Ankur Dhingra joined as CFO [Q1 2024 call].
- **2024-06-20:** Illumina drew a $750 million term loan at 6.7% to fund GRAIL [10-Q].
- **2024-06-24:** Illumina spun off GRAIL, distributing 85.5% of its shares, keeping 14.5% and funding it with $974 million of cash [10-K].
- **Q2 2024:** Illumina recorded $1,886 million of GRAIL impairments and a $1,988 million quarterly net loss [10-Q].
- **2024-08-01:** The board authorized a $1.5 billion share repurchase [10-K].
- **2024-08-06:** Management cut FY2024 revenue guidance to −2% to −3%, raised its margin outlook to 20.5–21% and introduced EPS guidance of $3.80–3.95 [Q2 2024 call].
- **2024-08-13:** A strategy update set the FY2027 targets: high-single-digit growth, at least 500 basis points of operating-margin expansion and double-digit-to-teens EPS growth [strategy update]. Barclays rated the stock Equal Weight with a $125 target on 2024-08-14.
- **2024-09-03:** The EU Court of Justice ruled that the EC had lacked jurisdiction over the GRAIL deal [10-K].
- **2024-09-06:** The EC withdrew its €432 million fine, and Illumina booked a $481 million net gain [10-K].
- **2024-09-09:** Illumina issued $500 million of 4.65% notes due 2026 and repaid the term loan [10-K].
- **Q3 2024:** Illumina agreed to buy Fluent BioSciences (single-cell technology) and began buybacks [Q3 2024 call]. Experts recall the Fluent deal closing in early 2025.
- **September 2024:** Clinical was 52% of revenue when a former associate director left, according to that expert's recollection [Expert: ex-Illumina AD now at Kailos, Aug 2026].
- **2024-11-04:** Management cut FY2024 revenue to about −3% but raised EPS guidance to $4.05–4.15; analysts debated a "clinical cliff" as clinical labs moved to cheaper NovaSeq X runs [Q3 2024 call].
- **2024-11-20:** The CFO said Q3 volume rose about 40% while consumables revenue rose only about 5%, "largely price" [Wolfe conference].
- **2024-12-03:** Management reported 528 NovaSeq X installed and framed 2025 placements at 200–240 [Evercore conference].
- **December 2024:** The MiSeq i100 began shipping, with more than 70 placed by year-end, and a single-flow-cell NovaSeq X began shipping [Q4 2024 call].
- **2024-12-23:** The Pavers and Road Builders derivative suit was filed [10-K].
- **FY2024:** The year ended with consolidated revenue of $4,372 million (down 2.9%) and a net loss of $1,223 million [10-K].

### 2025

- **January 2025:** Illumina launched Single Cell 3' RNA Prep and announced NVIDIA and Truveta partnerships (January 13) [10-K; JPM conference].
- **2025-02-04:** China added Illumina to its Unreliable Entities List (UEL), a blacklist allowing trade and investment penalties [10-K].
- **2025-02-06:** Illumina reported Q4 2024 revenue of $1.1 billion (up 1%) and 91 NovaSeq X placements [Q4 2024 call]. Barclays downgraded the stock to Underweight ($100 target) on 2025-02-10, while Freedom moved to Buy ($130).
- **February 2025:** Roche unveiled its SBX sequencing chemistry at the AGBT conference [Roche sources], and Illumina previewed Constellation and a 5-billion-cell atlas with the Broad Institute [AGBT investor session, 2025-02-25].
- **2025-03-04:** China banned imports of Illumina sequencing instruments [10-K]. In the same quarter Illumina launched an extra $100 million cost-reduction program [Q1 2025 10-Q].
- **2025-04-02:** U.S. "Liberation Day" tariffs were announced, with Illumina estimating about $85 million of cost, mainly on Singapore-made products [Q1 2025 call].
- **2025:** NIH capped university indirect costs, sharply cutting academic instrument funding [Expert: PacBio segment lead, Aug 2026], and 10x Genomics withdrew its full-year guidance in May [10x Q1 2025 call].
- **2025-05-08:** Management cut FY2025 guidance to revenue of $4.18–4.26 billion and EPS of $4.20–4.30, and named Scott Gottlieb board chair [Q1 2025 call]. J.P. Morgan cut its target to $85 (May 9), near the stock's low of about $80, and UBS cut its target to $98 (May 13).
- **2025-06-22:** Illumina agreed to buy SomaLogic from Standard BioTools for $350 million upfront plus up to $75 million in milestones and royalties [Q2 2025 slides].
- **2025-07-04:** U.S. tax legislation let companies deduct R&D immediately, triggering a one-time tax valuation allowance [10-K].
- **2025-07-22:** Illumina settled a Department of Justice False Claims Act probe for $9.8 million [10-Q].
- **2025-07-31:** Illumina reported Q2 revenue of $1,059 million, announced the SomaLogic deal and raised FY2025 EPS guidance to $4.45–4.55 [Q2 2025 call].
- **August 2025:** Oxford Nanopore announced that co-founder and CEO Gordon Sanghera would step down [ONT sources].
- **September 2025:** Illumina launched Protein Prep, its sequencing-based proteomics assay [10-K].
- **September 2025 litigation:** A California court overruled Illumina's demurrer (motion to dismiss) in the state GRAIL class action on September 3. The Icahn derivative suit was dismissed after a no-payment settlement on September 19. A federal court dismissed the GRAIL securities suit with leave to amend on September 26 [10-K].
- **Q3 2025:** Illumina achieved its NovaSeq X transition targets of more than 75% of high-throughput gigabases and more than 50% of high-throughput revenue [Q3 2025 deck].
- **October 2025:** Illumina launched its 5-Base Solution at the ASHG conference and announced BioInsight, its data and AI business [Q3 2025 deck]. On 2025-10-13 MGI licensed its CoolMPS chemistry outside China and Asia-Pacific to Swiss Rockets [UBS].
- **2025-10-30:** Q3 results showed $1,084 million of revenue and EPS of $1.34; growth outside China returned (+2%), and FY2025 EPS guidance rose to $4.65–4.75 [Q3 2025 call]. UBS raised its target to $120 and J.P. Morgan set $105.
- **2025-11-05:** PacBio missed Q3 expectations and cut its FY2025 guidance [PacBio Q3 call].
- **2025-11-10:** China allowed Illumina instrument exports into China to resume "on a case-by-case basis," effective that day; the permission was granted November 5 [10-K].
- **2025-11-13:** Bloomberg Intelligence published its Illumina business profile [BI].
- **November 2025:** Illumina issued $500 million of 4.75% notes due 2030 [10-K]. Oxford Nanopore restructured, and Natera acquired Foresight Diagnostics, according to an expert.
- **2025-12-08:** ONT named Francis van Parys CEO, effective 2 March 2026 [ONT].
- **2025-12-12:** Illumina repaid its $500 million 5.80% notes at maturity [10-K].
- **2025-12-15:** J.P. Morgan raised its target to $130 and Barclays to $110 [research notes].
- **2025-12-28:** FY2025 ended with revenue of $4,343 million, GAAP net income of $850 million, non-GAAP EPS of $4.84, a 23.1% non-GAAP operating margin and free cash flow of $931 million [10-K; Q4 2025 deck].

### 2026

- **2026-01-12:** ONT reported FY2025 revenue of about £224 million, up 24% in constant currency [ONT trading update].
- **2026-01-13:** At the J.P. Morgan Healthcare Conference, Illumina pre-announced FY2025 EPS of $4.76–4.79, reaffirmed its FY2027 targets and introduced the Billion Cell Atlas with AstraZeneca, Merck and Eli Lilly [JPM, 2026-01-13].
- **2026-01-15:** PacBio sold its short-read (Onso) assets to Illumina for about $48.1 million net [PacBio].
- **2026-01-16:** Chief Commercial Officer Everett Cunningham departed [10-K].
- **January 2026:** Illumina reorganized into four new reporting regions (USCAN, EMEALA, APAC and Greater China) [Q1 2026 10-Q].
- **2026-01-30:** Illumina closed the SomaLogic acquisition. The accounting purchase price was $460 million, or $363 million of net cash [Q2 2026 10-Q].
- **2026-02-01:** MGI agreed to buy nanopore and spatial-omics platforms from BGI Tech for Rmb365.7 million [UBS].
- **2026-02-03:** Anthropic's Claude clinical-research plug-in set off a sell-off in tools and contract-research stocks, dubbed the "Claude crash" [research notes].
- **2026-02-05:** Illumina reported Q4 2025 revenue of $1,159 million and EPS of $1.35, and guided FY2026 to $4.50–4.60 billion revenue and $5.05–5.20 EPS [Q4 2025 deck]. UBS raised its target to $135 the same day. J.P. Morgan cut its target to $120 on February 6, and Freedom raised its target to $140 on February 10.
- **2026-02-11:** Illumina filed its FY2025 10-K.
- **February 2026:** The U.S. Supreme Court ruled that IEEPA tariffs were improper. On February 13 a Delaware court heard the motion to dismiss the GRAIL derivative suit [Q2 2026 10-Q].
- **2026-02-19:** Element Biosciences unveiled its VITARI sequencer for shipment in H2 2026 [UBS, 2026-02-19].
- **2026-02-24:** MGI agreed to sell its U.S. unit, Complete Genomics, for $50 million [UBS].
- **2026-02-26:** Roche priced AXELIOS at $150 per genome [JPM; UBS, 2026-02-26].
- **2026-03-02:** ONT reported FY2025 results, guided FY2026 growth to 21–25% and dropped its >30% growth target; shares fell 12%. Van Parys became CEO the same day [ONT].
- **2026-03-03:** Illumina launched TruPath at $395 per genome and put Q70 accuracy and a 35B flow cell on its roadmap [TD Cowen conference].
- **2026-03-06:** Barclays downgraded PacBio to Underweight, citing TruPath and AXELIOS [Barclays].
- **March 2026:** The Court of International Trade ordered IEEPA tariff refunds [Q2 2026 10-Q].
- **2026-04-28 and 2026-04-30:** The board authorized an additional $1.5 billion buyback (announced April 30). Q1 results showed revenue of $1,091 million (+1.2% organic) and EPS of $1.15, and FY2026 EPS guidance rose to $5.15–5.30 [Q1 2026 call]. Barclays set a $122 target (Underweight).
- **April 2026:** Illumina paid the $25 million 2025 SomaLogic milestone, and 10x Genomics launched its Atera spatial platform at AACR [Q2 2026 10-Q; 10x].
- **2026-05-01:** BI said Illumina was "in the early stages of trading price for volume," and J.P. Morgan set a $125 target (Neutral) [BI; JPM]. Freedom raised its target to $155 on May 6.
- **2026-05-07:** PacBio missed Q1 expectations and cut its guidance [PacBio Q1 call].
- **2026-05-12:** At its Diagnostics Day, Roche set a target of about 100 first-year AXELIOS placements and a "blockbuster" ambition [Roche DX Day].
- **2026-05-15:** A California court certified a class in the state GRAIL securities suit [Q2 2026 10-Q].
- **2026-06-10:** J.P. Morgan upgraded Illumina to Overweight with a $185 target, citing a 62-customer survey [JPM, 2026-06-10].
- **June 2026:** Illumina launched StrataMap, its spatial product. An expert said the 35B flow cell was announced the same month.
- **2026-06-26:** A California court denied Illumina's motion for judgment on the pleadings, and BI said the sequencing market had entered "a more competitive era" [Q2 2026 10-Q; BI].
- **2026-06-29:** Roche launched AXELIOS 1 for research use only [Roche]. An expert dated the launch to July.
- **2026-07-13:** ONT warned that H1 revenue was about 7% below consensus [ONT trading update].
- **2026-07-16:** J.P. Morgan raised its target to $220 [JPM].
- **22 July to 6 August 2026:** Most of the folder's expert calls took place, with customers, former Illumina staff and competitors' employees [Expert calls].
- **2026-07-23:** Roche reported H1 Diagnostics growth of 3%, with China down 15% [Roche H1 call]. Thermo Fisher raised its 2026 guidance without mentioning sequencing [TMO Q2 call].
- **2026-07-27:** Illumina paid $30 million to buy out its remaining SomaLogic milestone and royalty obligations [Q2 2026 10-Q].
- **2026-07-28:** Illumina sought appellate review of the class-certification order [Q2 2026 10-Q].
- **2026-07-30:** Q2 revenue was $1,159 million (+6.5% organic, the fastest growth under Thaysen), with EPS of $1.31 and more than 95 NovaSeq X placements. FY2026 guidance rose to $4.60–4.64 billion revenue and $5.30–5.40 EPS, and new executives and directors were named [Q2 2026 call].
- **2026-07-31:** Analysts reacted to Q2. J.P. Morgan raised its target to $230 and Barclays to $160 (still Underweight), and BI called the 2027 goal "increasingly visible" [research notes].
- **2026-08-05:** Freedom downgraded Illumina to Hold with a $185 target. The same day, PacBio cut its guidance and CEO Christian Henry stepped down [Freedom; PacBio Q2 call].
- **2026-08-19:** ONT cut its core growth guide to 16–20% but signed a $20 million cross-licence and set 2030 targets [ONT H1 results].
- **2026-08-24:** MGI reported H1 revenue up 18.9% [UBS].
- **2026-09-08:** Roche's CEO said about one-third of the first-year AXELIOS placements had been made [JPM, 2026-09-15]. Seeking Alpha reiterated Hold on Illumina with a $188 fair value.
- **2026-09-09:** Illumina's $500 million 4.65% notes were scheduled to mature; the sources do not confirm repayment [10-K].
- **2026-09-21:** CMS proposed PAMA cuts to Medicare lab-test prices [Roche sources].
- **2026-10-04:** Illumina's Q3 2026 ended, a 14-week quarter. Consensus expects revenue of $1,154 million and EPS of $1.36, against guidance of $1.14–1.16 billion and $1.33–1.38 [Bloomberg consensus, 2026-10-10].
- **Upcoming:** Roche and Thermo Fisher report Q3 around October 22–23. A hearing on amending Illumina's answer in the California GRAIL suit is set for October 30 [Q2 2026 10-Q].

### 2027 and later

- **2027-01-03:** Illumina's fiscal 2026 ends; it is a 53-week year. Consensus expects Q4 2026 revenue of $1,220 million [Bloomberg consensus].
- **January 2027:** A genome-center VP expects the 35B flow cell, which should cut price per gigabase about 20% [Expert, 31 Jul 2026].
- **H1 2027:** Illumina's ERP upgrade (its core business software) is due to go live [10-K]. ONT expects its full strategy update with FY2026 results in February 2027.
- **2027:** Several peer milestones fall in this year:
  - ONT targets adjusted EBITDA breakeven;
  - PacBio targets $40 million of savings and a new high-throughput platform;
  - SomaLogic is expected to be profitable on a non-GAAP operating basis [ONT; PacBio; Q4 2025 deck].
- **2027-12-13:** Illumina's $500 million 5.75% notes mature [10-K].
- **2028:** Illumina's fiscal 2027 ends on January 2. Consensus expects revenue of $4,918 million and EPS of $6.11 [Bloomberg consensus]. Illumina's revolving credit facility matures on January 4. PacBio and ONT target cash-flow breakeven, and SomaLogic is targeted to match Illumina's margin.
- **2030:** ONT targets more than $700 million of organic revenue and a margin above 15% [ONT H1 2026 results].
- **2033-08:** Illumina's GRAIL contingent value right payments end [10-K].
- **2035:** Illumina's Singapore tax holidays expire [10-K].

## Glossary

Each term below has one plain-English definition. Where the sources gave several versions, the clearest one has been kept. The terms are grouped into three sections and sorted alphabetically within each.

### Genomics and technology

- **5-base genome (5-Base Solution):** Illumina's product that reads DNA variants and methylation from one preparation, launched in October 2025.
- **Amplicon sequencing:** Targeted sequencing of specific, known DNA regions after copying them.
- **Aptamer / SOMAmer:** A short engineered DNA-like molecule that binds a specific protein. SOMAmer is SomaLogic's version.
- **Base calling (basecaller):** Software that converts a sequencer's raw signals into DNA letters.
- **Batching / multiplexing:** Pooling many samples into one run to fill a large flow cell and cut the cost per sample.
- **BeadArray:** Illumina's bead-based microarray technology.
- **Cell-free DNA (cfDNA) / ctDNA:** DNA fragments floating in the blood. ctDNA is the portion shed by tumors.
- **CMOS sensor:** A semiconductor chip, like a camera sensor, with millions of wells that detect molecules. Roche's AXELIOS uses one.
- **Comprehensive genomic profiling (CGP):** A large-panel tumor test covering hundreds of cancer genes to guide treatment.
- **Copy number:** How many copies of a DNA segment a genome contains.
- **Cost per gigabase / cost per genome:** What it costs to read a billion DNA letters, or one human genome. These are the industry's main price yardsticks.
- **Counting applications:** Uses such as RNA-seq and single-cell work that count molecules and are priced per million reads.
- **Coverage (depth, e.g. 30X):** How many times each DNA position is read on average. A 30X genome is about 100 gigabases.
- **CRISPR:** A gene-editing tool used to switch genes off or alter them in experiments.
- **De novo assembly:** Building a genome sequence from scratch without a reference.
- **Digital PCR:** A highly sensitive DNA-copying test that counts individual molecules. It is cheap for repeat cancer monitoring.
- **DNA sequencing:** Reading the order of the chemical letters (A, C, G, T) in DNA.
- **Duplex / simplex:** Reading both strands of a DNA molecule for accuracy (duplex), or one strand for more output (simplex).
- **Exome / whole-exome sequencing (WES):** The protein-coding 1–2% of the genome, and sequencing only that part (about 8 Gb per sample).
- **FFPE:** Formalin-fixed, paraffin-embedded tissue. This is the standard way hospitals preserve biopsies, and it fragments the DNA.
- **Flow cell:** The consumable glass chip on which sequencing happens. Names such as 1.5B, 25B or 35B indicate billions of reads.
- **Foundation model:** A large AI model trained on huge datasets that can be adapted to many tasks.
- **Gene panel (targeted panel):** A test that sequences only selected genes.
- **Genome:** The complete DNA of an organism, about three billion letters in a human.
- **Germline / somatic:** Inherited DNA present in every cell, versus mutations acquired by a tumor.
- **Gigabase (Gb), terabase, petabase:** A billion, a trillion and a quadrillion DNA letters. These are the units of sequencing output.
- **HiFi:** PacBio's long reads that are also highly accurate.
- **Homopolymer:** A run of one repeated letter, which some sequencers read poorly.
- **Hybrid capture:** Pulling out whole genes with probes before sequencing.
- **Imaging-based spatial:** Spatial methods read by a microscope instrument without a sequencer, such as 10x's Xenium and Atera.
- **Isoform:** One of several RNA versions a single gene can produce.
- **Library prep:** The lab steps that turn a raw DNA or RNA sample into fragments a sequencer can read.
- **Liquid biopsy:** A blood test that detects cancer from DNA shed into the bloodstream.
- **Long-read, short-read and mid-read sequencing:** Reads of thousands of letters or more (PacBio, ONT); a few hundred letters (Illumina); and in-between lengths of up to about 1,000 or more (claimed for Roche AXELIOS).
- **Methylation / methylome / epigenetics:** Chemical tags on DNA that switch genes on and off without changing the sequence. The methylome is the genome-wide pattern of these tags, and epigenetics is their study.
- **Metagenomics:** Sequencing all the DNA in a mixed sample to identify its organisms.
- **Microarray (array):** An older chip with DNA probes that checks for a preset list of known variants. It is cheaper but less complete than sequencing.
- **MCED (multi-cancer early detection):** Blood tests that screen healthy people for many cancers at once, such as GRAIL's Galleri.
- **MRD (minimal residual disease):** Testing for traces of cancer left after treatment. Tumor-informed tests use the patient's own tumor profile; tumor-naive tests do not.
- **Multiomics:** Measuring several biological layers, such as DNA, RNA, proteins and methylation, from the same samples.
- **Nanopore sequencing:** Reading native DNA or RNA by pulling it through a tiny pore and measuring changes in electrical current. This is ONT's method.
- **Native protein sequencing:** Reading proteins directly rather than through DNA-based proxies.
- **Next-generation sequencing (NGS):** Technology that reads millions of DNA fragments in parallel.
- **NIPT (noninvasive prenatal testing):** A blood test of a pregnant person that screens fetal DNA for chromosomal conditions.
- **Perturb-Seq:** Experiments that switch genes off in many cells and sequence each cell to see what every gene does.
- **Phasing (haplotyping):** Working out which parent's chromosome copy each variant sits on.
- **Primary, secondary and tertiary analysis:** Turning signals into letters; aligning reads and calling variants; and interpreting the results into reports.
- **Proteomics:** Large-scale measurement of proteins. It can be affinity-based (binding reagents, as with SomaLogic and Olink) or done by mass spectrometry.
- **Q score:** A logarithmic accuracy scale. Q30 means one error per 1,000 letters, Q60 one per million, and higher numbers mean fewer errors.
- **Read / paired reads:** A single stretch of sequence produced by a sequencer, and a fragment read from both ends.
- **Reference genome / pangenome:** A standard genome used for comparison, and a reference built from many people's genomes.
- **Repeat expansion:** An abnormally lengthened stretch of repeated DNA that causes diseases such as Huntington's.
- **RNA-seq / transcriptome:** Sequencing RNA to measure which genes are active. The transcriptome is all the RNA a cell expresses.
- **SBS (sequencing by synthesis):** Illumina's chemistry, which reads DNA as a copy is built one tagged letter at a time.
- **SBX (sequencing by expansion) / Xpandomer:** Roche's chemistry, which converts DNA into a stretched surrogate molecule (the Xpandomer) read on a sensor.
- **Single-cell sequencing:** Measuring gene activity cell by cell rather than averaged across tissue.
- **SNP / SNV / SNP genotyping:** A single-letter DNA variant, and testing which version a sample carries.
- **Spatial biology (spatial transcriptomics):** Measuring gene activity while preserving its location in tissue.
- **Structural variant:** A large DNA rearrangement, deletion or duplication, which short reads often miss.
- **Synthetic long reads:** Long-range information reconstructed by stitching short reads together, as in Illumina's TruPath.
- **T2T genome:** A complete "telomere-to-telomere" genome with no gaps.
- **Throughput tiers (low, mid, high):** Sequencer classes by data output per run, from benchtop MiSeq to the NovaSeq X.
- **UMI / cell barcode:** Molecular tags that let individual molecules be counted accurately, or that record which cell a read came from.
- **Variant calling:** Identifying where a sample's DNA differs from the reference.
- **Whole-genome sequencing (WGS):** Reading a person's entire DNA, more than 120 Gb per sample.
- **XLEAP-SBS:** Illumina's newest, faster and cheaper SBS chemistry, with reagents shipped at room temperature.

### Products and business

- **10x Genomics products:** Chromium (single-cell, including Flex and Flex Apex assays), Visium (sequencing-based spatial), Xenium (imaging spatial with targeted panels) and Atera (whole-transcriptome imaging spatial, launched April 2026).
- **AGBT / ASHG / AACR / AMP / J.P. Morgan Healthcare Conference:** The major annual genomics, human-genetics, cancer, molecular-pathology and investor meetings where products and guidance are unveiled.
- **AVITI / AVITI24 / VITARI:** Element Biosciences' benchtop and new higher-output sequencers.
- **AXELIOS 1:** Roche's SBX-based sequencer, launched for research use in June 2026.
- **Backlog / remaining performance obligations (RPO):** Firm orders not yet shipped, and contracted revenue not yet recognized.
- **BaseSpace / Illumina Connected Analytics / Connected Insights / Connected Multiomics / Emedgene:** Illumina's cloud run-management, data-platform, interpretation, multiomics-analysis and AI rare-disease software.
- **BioInsight / Billion Cell Atlas:** Illumina's data and AI unit, launched in late 2025, and its first product. The Atlas is a gene-perturbation single-cell dataset sold to pharma partners.
- **Budget flush:** Year-end buying by customers spending leftover annual budgets.
- **Channel checks:** Analyst interviews with customers and distributors to gauge demand.
- **Clinical vs. Research & Applied (A&G):** Patient-testing customers versus academic, government, pharma and industrial customers. A&G means academic and government.
- **Clinical cliff:** The 2024 worry that clinical labs moving to the cheaper NovaSeq X would sharply cut consumables revenue.
- **CLIA / CAP:** U.S. certification and accreditation required to run clinical labs.
- **Companion diagnostic (CDx):** A test required to choose patients for a specific drug.
- **Consumables:** Reagent kits and flow cells customers must buy for every run. They are Illumina's main recurring revenue.
- **Core lab / genome center:** A shared facility that sequences for many researchers.
- **CRO / CDMO:** Contract research organizations, which run trials for drug companies, and contract manufacturers.
- **DRAGEN:** Illumina's fast secondary-analysis software, accelerated on FPGA chips and now GPUs.
- **Elasticity:** How much extra sequencing customers buy when prices fall.
- **Galleri / GRAIL:** GRAIL is the cancer-screening company Illumina formed, reacquired in 2021 and spun off in June 2024. Galleri is its multi-cancer blood test.
- **Helix:** The consumer-genomics venture Illumina launched in 2015 and deconsolidated in 2019.
- **HiSeq / HiSeq X Ten:** Older high-throughput lines. The X Ten broke the $1,000 genome in 2014.
- **Illumina Protein Prep / SomaScan:** Illumina's sequencing-based protein assay of about 9,500 proteins, launched September 2025, and SomaLogic's protein platform.
- **Import substitution:** Chinese buyers replacing foreign products with domestic ones.
- **Installed base / placement:** Instruments in active use at customers, and a newly installed instrument, whether sold, leased or rented.
- **Instruments:** The sequencers and array scanners themselves, sold as capital equipment.
- **Ion Torrent / Genexus:** Thermo Fisher's sequencing platforms, used mainly for small panels.
- **IVD / IVDR / CE mark:** A regulated diagnostic test; the EU regulation governing such tests; and the EU marketing approval mark.
- **ISO 13485:** The international quality standard for medical-device makers.
- **Key opinion leader (KOL):** An influential expert whose adoption shapes a field.
- **LDT (laboratory-developed test):** A test designed and validated by a single lab rather than sold as an approved kit.
- **MiSeq / MiSeq i100 / iSeq / MiniSeq:** Illumina's low-throughput benchtop sequencers. The i100 (2024) uses room-temperature reagents.
- **NextSeq 550 / 1000 / 2000:** Illumina's mid-throughput sequencers, workhorses in clinical labs.
- **NovaSeq 6000:** Illumina's 2017 high-throughput flagship, now being replaced.
- **NovaSeq X / X Plus / X Dx:** Illumina's flagship since 2023, with a much lower cost per gigabase. The Dx version is cleared for clinical use.
- **NovaSeq X transition:** Customers' shift from the NovaSeq 6000 to the NovaSeq X. It cut revenue per gigabase in 2023–2024 and was declared complete in late 2025.
- **OEM partner:** A company selling Illumina-made instruments under its own brand or channels.
- **Olink:** Thermo Fisher's proteomics business, SomaLogic's main rival.
- **Open offer letter:** Illumina's multi-year customer pricing arrangements, not tied to one instrument.
- **PacBio products:** Revio (high-throughput) and Vega (benchtop) long-read sequencers; SMRT Cells, the run chips, now reusable up to three times; and SPRQ-Nx chemistry, launched May 2026.
- **PIPseq / Fluent:** Illumina's instrument-free single-cell technology, from the Fluent BioSciences acquisition.
- **PMA / 510(k):** The FDA's long, costly approval pathway, and its shorter clearance pathway based on equivalence to an existing device.
- **PromethION / GridION / MinION / Flongle:** ONT's large, mid-sized, portable and small-flow-cell products. PromethION is now more than half of revenue.
- **Pull-through:** Yearly consumables revenue generated per installed instrument.
- **Reagent rental:** Placing an instrument free or cheaply in exchange for multi-year consumable commitments.
- **Recurring revenue:** Consumables plus service and other. Illumina puts this at about 90% of revenue.
- **Reimbursement / PAMA:** Payment by insurers for a test, and the U.S. law setting Medicare lab prices.
- **RUO (research use only):** A label meaning a product is not cleared for diagnosing patients.
- **Service and other:** Revenue from support contracts, sequencing and genotyping services, licensing and, since 2026, SomaLogic services.
- **Solexa:** The company whose technology underpins Illumina sequencing, bought for $480 million in 2007.
- **StrataMap:** Illumina's sequencing-based spatial product, launched June 2026.
- **Switching cost / validated assay:** The time and money needed to requalify a clinical test on a new platform.
- **Technology transfer:** A test company training a hospital lab to run its test locally, as in the UK's NHS.
- **Tender:** A government or hospital competitive bidding process.
- **Total cost of workflow:** The full cost of a result, including prep, sequencing, analysis and downtime.
- **TruPath (Constellation):** Illumina's synthetic long-read genome product, which skips most library prep. It launched in 2026 at $395 per genome.
- **TSO 500 / TSO Comprehensive:** Illumina's 500-gene tumor-profiling kit and its FDA-approved version.
- **Unreliable Entities List (UEL) / MOFCOM:** China's blacklist allowing penalties on foreign firms, which includes Illumina, and China's Ministry of Commerce, which administers it.
- **Win rate:** The share of competitive deals a company wins.

### Finance and valuation

- **10-K / 10-Q / 8-K / Form 10:** U.S. annual, quarterly and event filings, and the registration used for spin-offs.
- **Basis point (bp):** One hundredth of a percentage point; 100 bp equals 1 point.
- **Beat / miss / beat-and-raise:** Results above or below consensus; a beat followed by raised guidance.
- **Beta:** How much a stock moves relative to the market.
- **Bolt-on (tuck-in) acquisition:** A small purchase adding a technology to the existing business.
- **Breakeven / cash burn:** The point where a profit or cash measure reaches zero, and the pace at which a loss-maker uses cash.
- **CAGR:** Compound annual growth rate, the smoothed yearly growth over a period.
- **Capital expenditures (capex):** Spending on equipment and facilities.
- **Clearing event:** A guidance reset that removes investor doubt.
- **COGS:** Cost of goods sold, the direct cost of making products.
- **Consensus (Street):** The average forecast of sell-side analysts.
- **Constant currency (CC):** Growth with exchange-rate effects removed.
- **Contingent consideration:** Future acquisition payments that depend on targets being met.
- **Contingent value right (CVR):** A security paying holders based on a future outcome. Illumina's pays a share of GRAIL revenue through August 2033.
- **Core Illumina vs. consolidated:** Results excluding GRAIL versus whole-company totals. The two have been identical since the June 2024 spin-off.
- **Deconsolidate:** Remove a business from a company's financial statements.
- **Derivative suit / demurrer:** A shareholder suit on the company's behalf against directors, and a California motion arguing a complaint fails legally.
- **Dilutive / accretive:** Lowering or raising a metric such as EPS.
- **Discounted cash flow (DCF) / WACC / terminal growth:** Valuing a company from discounted future cash flows. WACC is the discount rate, and terminal growth is the long-run rate assumed after the forecast period.
- **EBIT / EBITDA:** Operating profit, and earnings before interest, taxes, depreciation and amortization, a rough proxy for operating cash earnings.
- **Effective tax rate:** Tax expense as a share of pre-tax profit.
- **Enterprise value (EV), EV/sales, EV/EBITDA:** Market value plus net debt, and valuation multiples built on it.
- **EPS (diluted, adjusted):** Profit per share. Diluted EPS counts potential shares; adjusted EPS uses non-GAAP profit.
- **ERP:** Enterprise resource planning, a company's core business software.
- **Fiscal year (52/53-week):** Illumina's year ends on a Sunday near December 31. FY2026 has 53 weeks and Q3 2026 has 14 weeks.
- **Fixed-cost absorption / operating leverage:** Margins rising as fixed costs spread over more volume.
- **Free cash flow (FCF), FCF conversion, FCF yield:** Operating cash flow minus capex; FCF as a share of non-GAAP net income; and FCF divided by market value.
- **GAAP / non-GAAP (adjusted):** Official U.S. accounting results, and management-adjusted figures excluding items such as amortization, acquisition costs, restructuring and investment gains. Illumina's non-GAAP still includes stock-based compensation, while some analysts' "adjusted" figures exclude it.
- **Goodwill / intangible assets / amortization:** The acquisition premium over identifiable assets; non-physical assets such as technology; and the gradual expensing of those assets.
- **Gross / operating margin:** Revenue left after direct costs, and after all operating costs, each as a share of revenue.
- **Gross leverage / net debt:** Total debt divided by trailing EBITDA, and debt minus cash.
- **Guidance:** Management's own forecast of results.
- **Impairment / IPR&D:** A write-down when an asset is worth less than its book value, and acquired unfinished research projects carried as assets.
- **Inventory step-up:** Acquired inventory revalued to fair value and expensed as it is sold.
- **Investment-grade rating:** A credit rating signalling low default risk.
- **LSD / MSD / HSD / DD:** Low-, mid-, high-single-digit and double-digit percentage growth.
- **Market capitalization:** The total stock-market value of a company.
- **Monte Carlo simulation:** Valuing an uncertain payment by simulating many outcomes.
- **NPV / ROIC / ROE:** Net present value; return on invested capital; and return on equity.
- **NTM / TTM; YoY / sequential:** Next and trailing twelve months; versus the same period a year earlier, and versus the prior quarter.
- **Organic growth / ROW organic:** Growth excluding currency and acquisitions, and that measure further excluding Greater China.
- **P/E:** Share price divided by earnings per share.
- **Pre-announcement:** Preliminary results released before the formal report.
- **Price target / ratings:** An analyst's 12-month share-price estimate. Overweight or Buy means expected to outperform; Neutral, Equal Weight or Hold means in line; Underweight means expected to underperform.
- **Pro forma:** Results restated as if an acquisition had happened earlier.
- **Proxy contest:** A shareholder campaign to elect its own board nominees, as Icahn ran in 2023.
- **Pull-forward:** Customers buying early, borrowing demand from later periods.
- **R&D capitalization (Section 174):** A tax rule requiring R&D to be deducted over years. The July 2025 U.S. law ended it for domestic R&D.
- **R&D / SG&A:** Research and development; selling, general and administrative expenses.
- **Restructuring charges / transformational initiatives:** Layoff and facility-exit costs, and Illumina's label for restructuring and ERP costs excluded from non-GAAP.
- **Revolving credit facility / term notes / delayed-draw term loan / convertible notes:** A standing bank credit line; fixed-rate bonds with set maturities; a loan drawn after signing; and bonds exchangeable into shares.
- **Sell-side / buy-side / independent research:** Bank analysts who publish for clients; investors; and research firms that do not trade the stock, such as BI.
- **Sequestration / continuing resolution:** Automatic U.S. federal spending cuts, and stopgap funding at prior-year levels.
- **Share repurchase (buyback) / anti-dilutive buyback:** A company buying its own stock, and buybacks sized to offset employee share issuance.
- **Spin-off / Disposal Funding:** Distributing a business's shares to the parent's shareholders, and the $974 million Illumina gave GRAIL at spin-off.
- **Stock-based compensation (SBC):** The non-cash cost of paying employees in shares.
- **Tariffs / IEEPA:** Import taxes, and the emergency-powers law used to impose tariffs that the Supreme Court ruled improper in February 2026.
- **Tax holiday / valuation allowance:** A temporary tax exemption, here for Singapore manufacturing to 2035, and a write-down of tax assets unlikely to be used.
- **Total addressable market (TAM):** The total revenue opportunity for a product category.

## Source coverage and known gaps

The folder holds 187 source documents. Illumina dominates the collection, with 115 documents (about 60% of the total). These include:

- 14 earnings-call transcripts and 16 conference transcripts;
- 18 SEC filings and 6 investor decks;
- 31 research notes and 3 consensus sheets;
- 23 expert calls and 4 insider-trading datasets.

Oxford Nanopore is the best-covered peer, with 43 documents, mostly research notes. The other peers are much thinner. PacBio has 11 documents, Roche 7, MGI 5, 10x Genomics 3 and Thermo Fisher 2, plus one sector-wide note. Conclusions about Illumina rest on deep, multi-source evidence. Conclusions about Roche, Thermo Fisher, 10x and MGI rest on only a handful of documents each and should be treated as provisional.

The table below shows the count of documents by company and type.

| Company | Document types (count) | Total |
|---|---|---|
| Illumina (ILMN) | Research 31; expert calls 23; filings 18; conferences 16; earnings calls 14; decks 6; insider data 4; consensus 3 | 115 |
| Oxford Nanopore (ONT) | Research 30; news 6; transcripts 5; consensus 2 | 43 |
| PacBio (PACB) | Research 6; transcripts 3; consensus 2 | 11 |
| Roche | Research 3; transcripts 2; consensus 2 | 7 |
| MGI Tech | Research 4; consensus 1 | 5 |
| 10x Genomics (TXG) | Transcripts 2; annual meeting 1 | 3 |
| Thermo Fisher (TMO) | Transcripts 2 | 2 |
| Sector | Research 1 | 1 |
| **Total** | | **187** |

### Known gaps

The main gaps below could affect conclusions.

**Expert calls.** The folder holds 23 distinct expert calls against a goal of 29. Four further files were the same calls saved from both Tegus and AlphaSense, and the duplicates are archived. Several experts' knowledge of Illumina is three to five years old, and many now work for competitors. Their views should be weighed with that in mind.

**Illumina conferences.** No conference transcript is in hand after the TD Cowen conference of 3 March 2026. The likely missing events are Bernstein (May), Goldman Sachs (June) and Morgan Stanley (September 2026). Management's commentary between earnings calls is therefore missing for most of 2026.

**Q2 2026 research.** Reaction notes to Illumina's Q2 2026 results (30 July 2026) are in hand from J.P. Morgan, Barclays, Freedom Broker, Ameriprise and Bloomberg Intelligence, but not from UBS. UBS's latest Illumina view in the folder dates from February 2026.

**Uneven history.** Earnings-call transcripts start at Q1 2023, while SEC filings start at Q1 2022. Management's spoken commentary on 2022 is therefore missing.

**Roche.** There is only one recent results call (H1 2026), and the Q1 2026 sales call is missing. Roche reports Q3 2026 sales around 22–23 October 2026.

**Thermo Fisher.** The Q1 2026 call, consensus estimates and research are all missing. Thermo reports Q3 2026 around 22 October 2026.

**10x Genomics.** The Q2 2026 call, consensus estimates and research are missing.

**MGI Tech.** There are no call transcripts, because MGI is listed in Shanghai and English transcripts generally do not exist. Coverage relies on UBS research, whose segment figures in some notes appear to be swapped.

**Element Biosciences and Ultima Genomics.** Both are private and publish no financials. They appear only through expert calls and other companies' commentary, so claims about their prices, quality and adoption are unverified.
