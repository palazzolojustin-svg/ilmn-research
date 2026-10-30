# Start Here: Illumina Research Core Notes

*As of 2026-10-10.*

# 00 Start Here

*Core Notes section 00. This is the orientation file for the Illumina (ILMN) research folder. It reflects material as of 2026-10-10. A few late-October 2026 events that arrived after that date, including the Q3 2026 earnings call, are added to the timeline and flagged. Bracketed tags cite the source, and full detail sits in the Working Notes (see `Working Notes/INDEX.md`).*

## How these notes are organized

This folder is a research workspace on Illumina and its publicly traded competitors: Oxford Nanopore, PacBio, Roche, Thermo Fisher, 10x Genomics and MGI Tech. It is built in layers. The original documents sit at the bottom. Above them are readable notes on each document, and on top is this master briefing, which synthesizes everything.

**Where things live:**

- **`CLAUDE.md`** holds the operating rules Claude Code follows in every chat opened on this folder.
- **`Core Notes/`** is this master briefing. It is read first in every chat.
- **`Working Notes/INDEX.md`** has one entry per source document, with its date, a short summary and links.
- **`Working Notes/Extracts/`** holds an exhaustive, readable note for every source document, filed by company and document type.
- **`Working Notes/Sources/`** holds the original documents, renamed and filed the same way. Use these when exact wording, tables or figures matter.
- **`Working Notes/Outputs/`** holds everything produced later in chats: datasets, artifacts, primers and analyses.
- **`Working Notes/_Archive/`** holds duplicates and off-topic files that are kept out of the analysis.
- **`Inbox/`** is where new files are dropped. Run `python _Build/build.py ingest` afterwards to file and process them.
- **`_Build/`** holds the build script, its state and its log.

**What each Core Notes file covers.** The files run from Illumina itself, through its sources by type, to the competitors and then to thematic deep-dives.

| File | What it covers |
|---|---|
| 00_Start_Here | This orientation, the master timeline, the glossary, and source coverage and gaps |
| 01_ILMN_Company_Primer | What Illumina sells, who buys it, how it makes money, its corporate history, and its strategy and guidance |
| 02_ILMN_Financial_History_and_Guidance | Reported results from 2022 onward, the balance sheet and cash flow, and how guidance changed over time |
| 03_ILMN_Consensus_Estimates | Wall Street's average forecasts for future years and how they have moved |
| 04_ILMN_Earnings_Calls_2023-2024 | Quarter-by-quarter management commentary during the GRAIL and NovaSeq X transition years |
| 05_ILMN_Earnings_Calls_2025-2026 | Quarter-by-quarter commentary during the China, tariff, SomaLogic and recovery period |
| 06_ILMN_Conferences_and_Investor_Events | Investor conferences, strategy days and the J.P. Morgan healthcare presentations |
| 07_ILMN_Expert_Calls | Interviews with former employees, customers and competitors' staff |
| 08_ILMN_Equity_Research | Sell-side and independent analysts' views, ratings and price targets |
| 09_Competitive_Landscape | Illumina against every rival, segment by segment |
| 10 to 15: Peer files | One file each on Oxford Nanopore, PacBio, Roche, Thermo Fisher, 10x Genomics and MGI Tech |
| 16_Addendum_Clinical_Consumables_Thesis | Deep-dive on whether clinical consumables can sustain Illumina's growth |
| 17_Addendum_Open_Offer_Pricing_Power | Deep-dive on Illumina's multi-year customer pricing deals and its pricing power |
| 18_Addendum_Thesis_Scrape_Alt_Data | Alternative data scraped to test the investment thesis |

## Illumina and its market in one page

### What DNA sequencing is

Every living cell carries instructions written in DNA, a long molecule spelled with four chemical "letters": A, C, G and T. **DNA sequencing** means reading the order of those letters. A human **genome**, the full set of a person's DNA, runs to about three billion letters.

Reading genomes cheaply lets scientists study disease. It also lets doctors find the mutations driving a patient's cancer, lets labs screen pregnancies for chromosomal problems, and lets breeders improve crops and livestock.

Output is measured in **gigabases** (Gb, billions of letters read). The cost of reading a genome has collapsed. Illumina's HiSeq X Ten broke the $1,000-per-genome barrier in 2014 [BI, 2025-11-13]. Today's flagship NovaSeq X can produce a genome for as little as $200 [10-K FY2025].

### What Illumina sells

Illumina is the market leader in **next-generation sequencing** (NGS, reading millions of DNA fragments in parallel). Its core chemistry is **sequencing by synthesis** (SBS): the machine copies DNA one letter at a time with chemically tagged building blocks while a camera records each letter added. Its technology came from Solexa, which it bought for $480 million in 2007. Bloomberg Intelligence (BI) calls that purchase possibly "one of the best health-care deals in history" [BI, 2025-11-13].

Illumina sells four things:

- **Instruments**, from small benchtop MiSeq machines to the factory-scale NovaSeq X.
- **Consumables**, the reagent kits and flow cells (the glass slides on which DNA is read) that customers must buy for every run.
- **Services**, such as support contracts and sequencing done in its own labs.
- **Software**, such as DRAGEN, which turns raw reads into a list of genetic variants.

It also sells **microarrays**, an older and cheaper chip technology that checks a pre-set list of known variants. Newer **multiomics** products (measuring RNA, proteins and chemical marks on DNA alongside DNA) aim to push more kinds of data through Illumina machines. The largest such move is the SomaLogic proteomics acquisition, which closed on 2026-01-30 [10-K FY2025].

### Who the customers are

Illumina serves more than 8,000 customers in about 160 countries [JPM, 2026-01-13].

- **Research and applied customers** include universities, government labs, genome centers, pharma companies and agriculture.
- **Clinical customers** are hospitals and diagnostic labs working in cancer, inherited disease and prenatal testing.

By share of sequencing consumables, the split is about 60% research and applied and about 40% clinical [JPM, 2026-01-13]. The two halves are moving in opposite directions. Outside China, clinical consumables grew 12% in FY2025 and 15% year over year in Q2 2026. Research and applied shrank 7% in both periods [Q4 2025 and Q2 2026 slides].

Research demand depends heavily on government money. BI says government funding drives almost half of sales [BI, 2025-11-13], and cuts at the U.S. National Institutes of Health (NIH) were a headwind in 2025 [10-K FY2025].

### How Illumina makes money

Illumina runs a "razor and razor blades" model. It places machines, then earns recurring consumable revenue from each one for years. Management counts consumables plus services as **recurring revenue**, about 90% of the company [JPM, 2026-01-13]. Consumables alone were $3,227 million in FY2025, or 74% of revenue, up 2% from FY2024 [10-K FY2025].

Two numbers drive this engine:

- **The installed base** is the number of active machines. It was about 21,000 at end-FY2025.
- **Pull-through** is the average annual consumables spend per machine. A NovaSeq X pulls through about $1.35 million a year, roughly twice a NovaSeq 6000 and about 15 times a NextSeq [Q4 2025 deck].

That gap is why the **NovaSeq X transition**, moving customers off the older NovaSeq 6000, has dominated the story since 2023.

**Recent results.** FY2025 revenue was $4,343 million, flat against $4,332 million for "Core" FY2024 (Illumina excluding the divested GRAIL). **Non-GAAP** earnings per share (EPS, adjusted profit per share excluding items such as acquisition amortization) were $4.84, up from $4.16 [Q4 2025 deck].

Growth then picked up. Q2 2026 revenue of $1,159 million rose 6.5% **organically** (excluding currency and acquisitions) [Q2 2026 slides]. Guidance for FY2026 was raised twice, to $4.60–4.64 billion of revenue and $5.30–5.40 of EPS in July, up from $4.50–4.60 billion and $5.05–5.20 in February.

After the 2026-10-10 snapshot, Illumina reported Q3 2026 revenue of about $1.17 billion and EPS of $1.44. Bloomberg consensus (the average analyst forecast) had been $1,154 million and $1.36. Management raised FY2026 guidance again, to $4.64–4.66 billion and EPS of $5.40–5.45 [Q3 2026 call, 2026-10-29].

### Who the competitors are

Illumina now faces a different rival in nearly every part of its market. A former Illumina associate director put it this way: "they're trying to compete with many companies, while these competitors are only competing with Illumina" [Expert: ex-Illumina AD now at Kailos, Aug 2026].

- **High-volume short reads.** Roche's AXELIOS sequencer launched on 2026-06-29 at a $150-per-genome list price, and private Ultima Genomics targets $80–100 genomes [Roche DX Day, 2026-05-12; JPM, 2026-05-13].
- **Mid-sized labs.** Private Element Biosciences (AVITI, and VITARI shipping in H2 2026) is the main mid-range winner in expert interviews.
- **Long reads.** Oxford Nanopore and PacBio read much longer DNA stretches. Nearly every expert sizes this niche at about 10% of demand.
- **China.** MGI Tech claims about 70% of Chinese public tenders [management, via UBS].
- **Single-cell and spatial biology.** 10x Genomics leads.
- **Proteomics.** Thermo Fisher's Olink is the rival to SomaLogic.

No source gives an audited market-share figure. Expert estimates of Illumina's share range from a loose "95%" guess to the mid-60s% [Expert calls, Jul–Aug 2026].

### The key debates right now

1. **Price versus volume.** Barclays and BI suspect Illumina is quietly trading price for volume. In Q1 2026 NovaSeq X's share of gigabases rose to 76% while its revenue share held at 55% [Barclays, 2026-04-30; BI, 2026-05-01]. Management called that reading "a frivolous exercise." J.P. Morgan's 62-customer survey implied only modest price cuts [JPM, 2026-06-10].
2. **How dangerous Roche is.** Views range from "will just simply die out" [Expert: South Carolina core] to 10–20% share within three years [Expert: ONT senior director]. Sell-side views split the same way: UBS calls Roche's pricing "benign," while Barclays sees "another round of pricing headwinds in 2027 and beyond."
3. **Clinical stickiness versus concentration.** Clinical tests are costly to revalidate on a new machine. But clinical revenue comes from roughly 10–20 large labs with real bargaining power [Expert calls, 2026].
4. **Whether placements are sustainable.** NovaSeq X placements beat Illumina's 50–60-unit quarterly framework three quarters running. Seeking Alpha and Barclays ask whether customers pulled purchases forward ahead of AXELIOS.
5. **China, NIH funding and tariffs.** China revenue fell 21% in FY2025 after Beijing blacklisted Illumina. Research funding is weak, and tariffs added cost [10-K FY2025].
6. **Whether multiomics pays off.** Management expects multiomics and BioInsight (its data and AI unit) to add 1–2 points of growth in 2027. Barclays says this cannot be verified, and experts report little customer uptake of SomaLogic so far.
7. **Valuation after the rally.** J.P. Morgan's target rose from $120 (Feb 2026) to $230 (Jul 2026). Freedom Broker, by contrast, downgraded the stock to Hold on 2026-08-05, saying the good news was "priced in."

## Master timeline

The timeline below merges every dated event in the sources into one chronological list. Dates marked "approx." are approximate in the source. Where only a month or year was given, only that is shown. Purely internal Roche pharma and Thermo Fisher bioproduction items, such as drug approval dates, are left to the peer files.

### Before 2020

- **2005.** Oxford Nanopore (ONT) was spun out of the University of Oxford with £0.5M from IP Group [ONT research].
- **2007.** Illumina bought Solexa for $480M, and Solexa's technology became the basis of its sequencing business [BI, 2025-11-13].
- **Early 2008 (approx.).** The expert later interviewed as an ONT senior director joined Illumina and stayed about six years [Expert: ONT senior director].
- **Q3 2011.** Illumina shipped the first MiSeq benchtop sequencer [Q4 2025 deck].
- **2012.** U.S. budget sequestration and a federal shutdown temporarily capped Illumina's growth [BI, 2025-11-13].
- **2014.** Illumina offered the HiSeq X Ten, which broke the $1,000-per-genome barrier, and shipped the first NextSeq 500 in Q1 [BI; Q4 2025 deck].
- **Q1 2015.** The NextSeq 550 first shipped [Q4 2025 deck].
- **2015-08-18.** Illumina announced Helix, a consumer-genomics platform funded with $100M from two venture investors [BI, 2025-11-13].
- **2016.** Illumina formed GRAIL to develop a blood test for early cancer detection, and the MiniSeq first shipped in Q1. Roche began a collaboration with NVIDIA, partly to handle sequencer data [BI; Roche research].
- **Q1 2017.** The NovaSeq 6000, Illumina's previous flagship, first shipped [Q4 2025 deck].
- **2018.** The iSeq 100 first shipped in Q1, and Illumina announced a deal to buy PacBio [Q4 2025 deck; Barclays].
- **2019.** Illumina deconsolidated Helix (removed it from its financial statements), which BI called "a prudent step to tighten the portfolio" [BI, 2025-11-13].

### 2020

- **2020-02-05.** Illumina's board authorized a $750M share buyback, of which only $15M later remained [10-K].
- **Q1 and Q4 2020.** The NextSeq 2000 and NextSeq 1000 mid-throughput sequencers began shipping [Q4 2025 deck].
- **2020.** Illumina abandoned its PacBio acquisition after Federal Trade Commission (FTC) opposition [Barclays]. Roche bought Stratos Genomics, the source of its SBX sequencing technology [Roche research]. Illumina also bought a clinical sequencing start-up spun out of ARUP [Expert: ONT senior director].

### 2021

- **2021-03-08 and 03-23.** Illumina entered a $750M revolving credit facility and issued $500M of notes due 2023 and $500M due 2031 [10-K].
- **2021-05-20.** Ameriprise added Illumina to its Recommended List as a Buy at $385.31 [Ameriprise].
- **2021-08-18.** Illumina completed its reacquisition of GRAIL without first obtaining EU approval, a decision that triggered years of regulatory fights [10-K; BI].
- **2021-09-30.** Illumina's market capitalization (total stock-market value) peaked at $76B in the third quarter [BI, 2025-11-13].
- **2021-11-10.** J.P. Morgan initiated coverage of Oxford Nanopore at Overweight [JPM, ONT].

### 2022

- **2022-01-03.** Illumina adopted a new accounting rule (ASU 2020-06) that reduced reported interest expense on its convertible notes [10-K].
- **2022-06-09.** CFO Sam Samad departed, and Joydeep Goswami became interim CFO [8-K].
- **2022-07-13.** The EU General Court ruled that the European Commission (EC) had jurisdiction to review the GRAIL deal [10-Q].
- **2022-07-14 and 07-25.** Illumina settled patent litigation with BGI/Complete Genomics for $325M and paid it 11 days later [10-Q].
- **2022-07-15.** The NHS-Galleri trial of GRAIL's cancer test completed enrollment of 140,000 participants [Q2 2022 materials].
- **2022-07-19.** The EC issued a Statement of Objections (formal charges) for closing the deal during review, and Illumina accrued $453M for a likely fine [10-Q].
- **2022-09-01 and 09-06.** An FTC administrative law judge ruled for Illumina on GRAIL, but five days later the EC prohibited the acquisition [10-Q].
- **2022-09-29 (approx.).** Illumina unveiled the NovaSeq X at its Genomics Forum, at its lowest-ever cost per gigabase and 2.5 times prior throughput [BI].
- **October 2022.** At its investor day, Illumina set targets of mid-teens growth and a 25% operating margin. It also estimated an addressable market above $125B, with 34% of research captured by 2027 [BI; conferences].
- **2022-10-21.** UBS rated MGI a Buy with a Rmb140 target [UBS, MGI].
- **2022-11-03.** Illumina's Q3 10-Q recorded a $3,914M GRAIL goodwill impairment (a write-down of the acquisition premium) and guided 2022 revenue flat to up 1% [10-Q].
- **November 2022.** Illumina announced its first cost-cutting actions [Q4 2022 materials].
- **2022-12-13.** Illumina issued $500M of 5.80% notes due 2025 and $500M of 5.75% notes due 2027 [10-K].

### 2023

- **January 2023.** The Czech Republic added comprehensive genomic profiling (broad tumor testing) to its national fee schedule [conference materials]. J.P. Morgan's ONT target peaked at 460p on 2023-01-03, with the shares at 246p [JPM].
- **2023-01-04.** Illumina replaced its credit line with a new $750M facility maturing 2028-01-04 [10-K].
- **2023-02-07 and 02-08.** Illumina guided 2023 revenue growth of 7–10% with EPS of $1.25–1.50, and J.P. Morgan rated it Neutral with a $271 target [Q4 2022 call; JPM].
- **2023-02-17.** The FY2022 10-K reported revenue of $4,584M (up 1%) and a net loss of $4,404M, driven by GRAIL impairments [10-K FY2022].
- **March 2023.** The NovaSeq X Plus began shipping globally (first shipments in Q1), and Illumina announced its first long-read sequencing offering. It repaid its $500M 2023 notes on 2023-03-23 [10-K; Q1 2023 call].
- **2023-03-31.** The full FTC ordered Illumina to divest GRAIL [10-Q].
- **2023-04-25.** On the Q1 call, Illumina said it had shipped 67 NovaSeq X units and raised its 2023 X target to more than 330. It held guidance, announced more than $100M of cost cuts, and set Core operating margin targets of 25% for 2024 and 27% for 2025 [Q1 2023 call]. The 10-Q showed revenue down 11% [10-Q].
- **2023-05-10.** Barclays initiated PacBio at Equal Weight with a $14 target [Barclays].
- **June 2023.** CEO Francis deSouza departed after a proxy contest (a shareholder campaign for board seats) led by Icahn, and Charles Dadswell became interim CEO. A late-June 8-K disclosed headcount and real-estate cuts [8-K].
- **July 2023.** Illumina received an SEC document request (approx.), and on 2023-07-12 the EC fined it €432M for closing GRAIL during review [10-Q].
- **2023-08-09.** On the Q2 call, Illumina cut 2023 guidance to roughly flat Core revenue (about 1% consolidated growth) and raised NovaSeq X supply to more than 390 units after shipping 109 [Q2 2023 call].
- **2023-08-15 to 09-11.** Illumina repaid $750M of convertible notes in cash. At investor conferences, management cited about 260 NovaSeq X orders [UBS summit, 2023-08-17] and called the 2024 25% margin target "a stretch" [MS conference, 2023-09-11].
- **Late September 2023.** Jacob Thaysen became CEO [8-K].
- **2023-10-12.** The EC adopted its GRAIL Divestment Decision [10-Q].
- **2023-10-17.** Icahn Partners filed a derivative suit (a shareholder suit on the company's behalf) against directors over GRAIL [10-K].
- **Late October 2023.** Illumina launched the 25B flow cell, the NovaSeq X's highest-capacity consumable, cutting cost per genome to about $200 [Q3 2023 call].
- **2023-11-09.** On the Q3 call, Illumina cut 2023 guidance a second time, cut X shipments to 330–340 and formed a GRAIL special committee. It took an $821M GRAIL impairment [Q3 2023 call; 10-Q].
- **2023-11-10.** Analysts slashed targets after the stock collapsed: J.P. Morgan to $110, UBS to $111 and Barclays to an adjusted $48.59 [research].
- **2023-11-11.** The first federal securities class action over GRAIL was filed [10-K].
- **2023-11-28 and 11-29.** Management said 2024 revenue would be roughly flat. New CEO Thaysen ruled out large acquisitions and put China at about 10% of revenue [Evercore and Piper Sandler conferences].
- **Late 2023.** Illumina acquired Partek, a multiomics software company [conference materials].
- **2023-12-15 to 12-17.** The U.S. Fifth Circuit vacated the FTC order and sent it back. The EU Court of Justice heard the jurisdiction case, and Illumina announced it would divest GRAIL [10-K].
- **FY2023 (ended 2023-12-31).** Revenue was $4,504M (down 2%), the net loss was $1,161M and GAAP EPS was −$7.34 [10-K]. The primer cites $4,438M for FY2023, which appears to be a different basis. Bloomberg's adjusted EPS of $0.86 is on a different basis from company figures. A 2023 layoff wave was also recalled by a former field scientist.

### 2024

- **January 2024.** Illumina launched a 1.5B NovaSeq X kit and cut more jobs, bringing cumulative role cuts to about 12%. At JPM on 2024-01-09, it reported 352 NovaSeq X units shipped in 2023 and $175M of cost savings [JPM 2024].
- **2024-02-02.** California state securities class actions were filed over the 2020–21 GRAIL registration statements [10-K].
- **2024-02-08 and 02-09.** On the Q4 2023 call, Illumina guided 2024 Core revenue flat with an operating margin of about 20%, and targeted GRAIL's divestiture by end-June. Freedom Broker rated the stock Hold with a $150 target [Q4 2023 call; Freedom].
- **February to April 2024.** The City of Omaha (02-26) and City of Roseville (04-16) filed further derivative suits [10-K].
- **2024-03-06.** J.P. Morgan cut its ONT target to 210p as ONT set a mid-term plan of more than 30% annual revenue growth [JPM, ONT].
- **March 2024.** XLEAP-SBS chemistry and the P4 flow cell came to the NextSeq 1000/2000, and Illumina merged its marketing and commercial teams [Q1 2024 call].
- **2024-03-31.** Q1 2024 revenue was $1,076M, with a net loss of $126M [10-Q].
- **April 2024.** The EC approved Illumina's GRAIL divestment plan, and Ankur Dhingra joined as CFO in mid-April [Q1 2024 call].
- **2024-05-02.** Core Q1 revenue was about $1.06B (down 2%), and FY2024 guidance was reiterated [Q1 2024 call]. Shareholder Michael Warner filed a litigation demand on 2024-05-01 [10-K].
- **2024-06-17 and 06-20.** Illumina signed and fully drew a $750M delayed-draw term loan at 6.7% to fund GRAIL [10-Q].
- **2024-06-24.** Illumina spun off GRAIL. It distributed 85.5% of the shares (one GRAIL share for every six Illumina shares), kept 14.5% and funded GRAIL with $974M of cash [10-K; BI].
- **2024-06-30.** Q2 2024 included $1,886M of GRAIL impairments and a $1,988M net loss [10-Q].
- **2024-08-06.** On the Q2 call, Illumina cut FY2024 revenue guidance to −2% to −3%, raised its margin guide to 20.5–21%, introduced EPS guidance of $3.80–3.95 and set a $200M savings plan [Q2 2024 call].
- **2024-08-13.** A strategy update set 2027 targets: high-single-digit growth, at least 500 basis points of operating margin expansion and double-digit-to-teens EPS growth. The board authorized a $1.5B buyback, and Illumina previewed its 5-base and comprehensive-genome products [strategy update].
- **2024-08-14 and 08-21.** Barclays rated Illumina Equal Weight with a $125 target, and shareholder Jane Davidson filed a GRAIL litigation demand [Barclays; 10-K].
- **2024-09-03 and 09-06.** The EU Court of Justice ruled the EC lacked jurisdiction over GRAIL. The EC withdrew its €432M fine, and Illumina booked a $481M net gain [10-K].
- **2024-09-09.** Illumina issued $500M of 4.65% notes due 2026 and repaid the term loan. In Q3 it also acquired Fluent BioSciences (single-cell; other sources say the deal closed early 2025) and began buybacks [10-K].
- **September and October 2024.** Two expert sources left Illumina: a former associate director, who said clinical was then 52% of revenue, and a former field application scientist [Expert calls].
- **2024-11-04.** On the Q3 call, Illumina cut FY2024 revenue to about −3%, raised its margin guide to 21–21.5% and EPS to $4.05–4.15. Analysts debated a "clinical cliff," the fear that clinical customers moving to cheaper NovaSeq X would sharply cut revenue [Q3 2024 call].
- **2024-11-20.** CFO Dhingra said Q3 volume rose about 40% while consumables rose about 5%, "largely price," and put China at about $75M a quarter [Wolfe conference].
- **December 2024.** The MiSeq i100 began shipping (more than 70 placed by year-end) and the single-flow-cell NovaSeq X shipped. Management reported 528 NovaSeq X units installed [Evercore, 2024-12-03]. Pavers and Road Builders filed a derivative suit on 2024-12-23 [10-K].
- **FY2024 (ended 2024-12-29).** Consolidated revenue was $4,372M (down 2.9%) and the net loss was $1,223M. Company non-GAAP EPS was $4.16, while Bloomberg's adjusted EPS of $2.45 is on a different basis [10-K; consensus sheet]. Illumina also received $83M from a Helix contingent value right in 2024 [10-K].

### 2025

- **January 2025.** Illumina launched Single Cell 3' RNA Prep and closed the Fluent acquisition (approx.). It announced NVIDIA and Truveta partnerships on 2025-01-13. ONT announced "CapEx-first" device pricing and its first restructuring [JPM 2025; ONT materials].
- **2025-01-14.** At JPM, Illumina previewed Q4 2024 revenue of about $1.1B with 91 NovaSeq X placements. It guided 2025 to low-single-digit growth and about a 23% margin [JPM 2025].
- **2025-02-04.** China added Illumina to its Unreliable Entities List, a blacklist allowing trade, investment and staffing penalties [10-K FY2025].
- **2025-02-06.** On the Q4 2024 call, Illumina reported revenue of $1.1B (up 1%) and reaffirmed 2025 guidance excluding China [Q4 2024 call].
- **2025-02-10.** Barclays downgraded Illumina to Underweight ($100 target), while Freedom Broker moved to Buy ($130) [research].
- **February 2025.** Roche unveiled its SBX sequencing chemistry at the AGBT conference. Illumina priced its Constellation long-read technology in the "hundreds of dollars" and announced a 5-billion-cell atlas with the Broad Institute [AGBT investor session, 2025-02-25]. UBS upgraded Roche to Buy (CHF338) [UBS].
- **2025-03-04.** China banned imports of Illumina sequencing instruments [10-K FY2025]. J.P. Morgan cut its ONT target to 190p [JPM].
- **2025-03-18.** UBS downgraded MGI to Neutral with a Rmb98 target [UBS].
- **Q1 2025 (ended 2025-03-30).** Revenue was $1,041M with non-GAAP EPS of $0.97. Illumina launched an extra $100M cost-reduction program in response to China and NIH uncertainty [Q1 2025 slides].
- **April 2025.** U.S. and foreign tariffs took effect, mainly hitting imports from Illumina's Singapore plant, with an estimated cost of about $85M. The Icahn suit reached an agreement in principle on 2025-04-11 [10-K].
- **2025-05-08 to 05-13.** On the Q1 call, Illumina cut FY2025 guidance to $4.18–4.26B of revenue and EPS of $4.20–4.30, citing China, NIH funding and tariffs [Q1 2025 call]. J.P. Morgan cut its target to $85 near the stock's low of about $80, and UBS cut to $98 [research]. 10x Genomics withdrew its guidance amid U.S. research funding changes (approx.).
- **2025-05-28.** CEO Thaysen reaffirmed the 2027 plan excluding China and explained an insider share purchase [Bernstein conference].
- **2025-06-22.** Illumina agreed to buy SomaLogic from Standard BioTools for $350M plus up to $75M in milestones and royalties [Q2 2025 slides].
- **Q2 2025 (ended 2025-06-29).** Revenue was $1,059M, non-GAAP EPS was $1.19, and buybacks totaled $370M [Q2 2025 slides].
- **2025-07-04.** U.S. tax legislation restored immediate R&D deduction, which triggered a valuation allowance on Illumina's foreign tax credits [10-K].
- **2025-07-22.** Illumina settled a Department of Justice False Claims Act probe for $9.8M [10-Q].
- **2025-07-31.** With Q2 results, Illumina announced SomaLogic, raised FY2025 EPS guidance to $4.45–4.55 and guided China revenue at $190–210M [Q2 2025 call].
- **August 2025.** ONT said co-founder and CEO Gordon Sanghera would step down. PacBio's Q2 revenue of $40M beat forecasts (08-07). The Icahn settlement was formalized on 2025-08-21 with no payment [ONT; PacBio; 10-Q].
- **September 2025.** Illumina launched its Protein Prep proteomics assay. A California court overruled Illumina's demurrer (motion to dismiss) in the state GRAIL case (09-03). The Icahn suit was dismissed (09-19), and a federal court dismissed the securities suit with leave to amend (09-26) [10-K].
- **Q3 2025 (ended 2025-09-28).** Revenue was $1,084M, and the non-GAAP operating margin peaked at 24.5%. NovaSeq X passed its year-end transition targets early, with more than 75% of high-throughput gigabases and more than 50% of revenue [Q3 2025 deck].
- **October 2025.** Illumina launched the 5-Base Solution and announced BioInsight. The first All of Us long-read data were published [Q3 2025 deck; PacBio].
- **2025-10-13.** MGI licensed its CoolMPS chemistry outside Asia to Swiss Rockets for $20M upfront plus milestones and royalties [UBS, MGI].
- **2025-10-27.** Plaintiffs filed a third amended federal securities complaint over GRAIL [10-K].
- **2025-10-30 and 10-31.** On the Q3 call, Illumina reported a return to about 2% growth excluding China and raised FY2025 EPS guidance to $4.65–4.75. UBS raised its target to $120 [Q3 2025 call; UBS]. A California appeals court denied Illumina's writ on 2025-10-31 [10-K].
- **November 2025.** China granted permission on 2025-11-05 for Illumina instrument exports to resume, effective 11-10, "on a case-by-case basis" [10-K FY2025]. Thaysen said sanctions were lifted and that the 2027 growth target now excludes China [Wolfe, 2025-11-19]. PacBio's Q3 missed, and its guide was cut to $155–160M (11-05). ONT announced a "strategic realignment." Natera acquired Foresight Diagnostics [Expert recollection].
- **2025-11-13.** BI published its Illumina business profile and M&A note [BI].
- **2025-11-25.** Illumina issued $500M of 4.75% notes due December 2030 [10-K].
- **December 2025.** ONT named Francis van Parys as CEO (12-08). Illumina repaid its $500M 5.80% notes on 12-12. J.P. Morgan raised its target to $130 and Barclays to $110 (12-15) [research].
- **FY2025 (ended 2025-12-28).** Revenue was $4,343M, GAAP net income $850M and non-GAAP EPS $4.84, against guidance of $4.65–4.75. The non-GAAP operating margin was 23.1%, free cash flow $931M and cash $1,418M [10-K FY2025].

### 2026

- **2026-01-13.** At JPM, Illumina pre-announced Q4 2025 revenue of about $1.16B (up 4% constant currency, up 7% excluding China), more than 95 NovaSeq X placements and FY2025 EPS of $4.76–4.79. It reaffirmed its FY2027 targets and launched BioInsight [JPM, 2026-01-13]. ONT pre-announced FY2025 revenue of £223–224M (up 24%) [ONT].
- **2026-01-15 and 01-16.** PacBio sold its short-read (Onso) assets to Illumina for about $48.1M net. Chief Commercial Officer Everett Cunningham departed [PacBio; 10-K].
- **2026-01-30.** Illumina closed SomaLogic. Sources quote $350M upfront as the headline, $363M net cash, and a $460M accounting purchase price ($382M cash plus $81M of contingent payments, less $3M) [Q2 2026 10-Q]. Illumina also moved to new geographic reporting regions in January.
- **February 2026.** The U.S. Supreme Court ruled tariffs under the International Emergency Economic Powers Act (IEEPA) improper. MGI bought nanopore and spatial platforms from BGI Tech (02-01), and 10x reinstated 2026 guidance of $600–625M [10-Q; UBS; 10x].
- **2026-02-03.** An Anthropic clinical-research plug-in triggered a sell-off in tools and contract-research stocks, dubbed the "Claude crash" [Barclays, PacBio].
- **2026-02-04.** Illumina's board again deferred Michael Warner's GRAIL litigation demand [10-K].
- **2026-02-05 and 02-06.** Illumina reported Q4 2025 revenue of $1,159M and EPS of $1.35. It guided FY2026 to $4.50–4.60B of revenue and EPS of $5.05–5.20. UBS raised its target to $135, J.P. Morgan cut to $120 and Barclays held $110 Underweight [Q4 2025 call; research].
- **2026-02-10 to 02-13.** Freedom Broker raised its target to $140 (02-10). Illumina filed its FY2025 10-K (02-11). PacBio guided 2026 to $165–180M (02-12). A Delaware court heard the motion to dismiss the GRAIL derivative suit (02-13) [research; 10-K; PacBio].
- **2026-02-19.** Element Biosciences unveiled its VITARI sequencer, which UBS said keeps pressure on Illumina [UBS, 2026-02-19].
- **2026-02-24.** MGI agreed to sell its U.S. unit Complete Genomics for $50M and licensed StandardMPS in North America [UBS, MGI].
- **2026-02-26.** Roche priced AXELIOS at $150 per genome at AGBT. J.P. Morgan put that about 25% below its roughly $200 NovaSeq X estimate [JPM; UBS, 2026-02-26].
- **2026-03-02.** ONT reported FY2025 revenue of £223.9M (up 24.2% at constant currency). It guided 2026 growth to 21–25%, below 27.5% consensus, dropped its 30%-plus target, and the shares fell 12%. Van Parys became CEO [ONT].
- **2026-03-03.** Illumina launched TruPath at $395 per genome and put Q70 accuracy and a 35B flow cell on its roadmap [TD Cowen conference].
- **March 2026.** The Court of International Trade ordered IEEPA tariff refunds. Barclays downgraded PacBio to Underweight, citing TruPath and AXELIOS (03-06). Illumina's federal motion to dismiss became fully briefed (03-06). BI refreshed its outlook (03-11). Thermo closed its $9B Clario purchase [10-Q; research].
- **Q1 2026 (ended 2026-03-29).** Revenue was $1,091M (up 4.8% reported, 1.2% organic) and EPS $1.15 [Q1 2026 slides].
- **April 2026.** Illumina paid the $25M 2025 SomaLogic milestone. The board authorized another $1.5B buyback (04-28). 10x launched its Atera spatial platform at AACR (approx. 04-22). MGI reported 2025 revenue down 7.7%, and UBS cut its target to Rmb58 (04-29) [10-Q; 10x; UBS].
- **2026-04-30.** Illumina reported more than 80 NovaSeq X placements for Q1 and raised FY2026 guidance to $4.52–4.62B and EPS of $5.15–5.30. Barclays kept its Underweight rating at $122 [Q1 2026 call; Barclays].
- **May 2026.** BI said Illumina was "trading price for volume" (05-01). Freedom raised its target to $155 (05-06). PacBio cut its guide to $165–175M (05-07). Roche's Diagnostics Day set a 100-placement first-year target for AXELIOS (05-12). The California court certified a class in the GRAIL suit (05-15) [research; 10-Q].
- **June 2026.** Illumina launched StrataMap spatial. J.P. Morgan upgraded Illumina to Overweight with a $185 target on a 62-customer survey (06-10). Barclays raised its target to $145 (06-23). A California court denied Illumina's motion for judgment on the pleadings (06-26). Roche launched AXELIOS for research use only (06-29) [research; 10-Q; Roche].
- **Q2 2026 (ended 2026-06-28).** Revenue was $1,159M (up 9.5% reported, 6.5% organic) and EPS $1.31 [Q2 2026 slides].
- **July 2026.** ONT's trading update came in about 7% below consensus (07-13). J.P. Morgan raised its target to $220 (07-16). A wave of 20-plus expert calls ran from 07-22 to 07-31. Illumina paid $30M to buy out the remaining SomaLogic obligations (07-27) and sought appellate review of class certification (07-28) [research; Expert calls; 10-Q].
- **2026-07-30 and 07-31.** Illumina reported more than 95 NovaSeq X placements and raised FY2026 guidance to $4.60–4.64B and EPS of $5.30–5.40. It also announced a whole-genome MRD workflow and six Billion Cell Atlas partners. J.P. Morgan moved its target to $230 and Barclays to $160 Underweight [Q2 2026 call; research].
- **August 2026.** Freedom downgraded Illumina to Hold at $185 (08-05). PacBio's CEO Christian Henry stepped down and guidance was cut to $155–165M (08-05). ONT's H1 results set 2030 targets of more than $700M revenue (08-19). MGI's H1 revenue rose 18.9% (08-24) [research; PacBio; ONT; UBS].
- **September 2026.** Roche's CEO said about one-third of roughly 100 first-year AXELIOS placements were made (09-08). Seeking Alpha set a $188 fair value with a Hold (09-08). Illumina's $500M 4.65% notes matured (09-09). CMS proposed lab-pricing cuts under PAMA (09-21) [JPM, 2026-09-15; research; 10-Q].
- **2026-09-27 (approx.).** Illumina's Q3 2026 ended. It was a normal 13-week quarter. Bloomberg dates the quarter end 10/04, which would imply 14 weeks, but management says the extra week falls in Q4 (Q2 and Q3 2026 calls). Consensus was $1,154M revenue and $1.36 EPS [consensus sheet].
- **2026-10-10.** The Bloomberg consensus snapshot showed FY2026 revenue of $4,624.8M and EPS of $5.36, and FY2032 revenue of $7,370.5M and EPS of $12.30 [consensus sheet].
- **2026-10-28 (after snapshot).** The U.S. announced trade restrictions on some Chinese sequencing competitors [Q3 2026 call].
- **2026-10-29 (after snapshot).** Illumina reported Q3 revenue of $1.17B, EPS of $1.44 and a 25% operating margin, with about 360 NovaSeq X placements over four quarters. It raised FY2026 guidance to $4.64–4.66B and EPS of $5.40–5.45. It also reported GSK joining the Billion Cell Atlas and China returning to growth [Q3 2026 call].
- **2026-10-30.** A hearing is scheduled on Illumina's motion to amend its answer in the California GRAIL suit [10-Q].

### 2027 and later (scheduled or expected)

- **January 2027.** Illumina's 35B flow cell is expected [Expert: genome center VP]. Fiscal 2026 ends on 2027-01-03 after 53 weeks, with Q4 consensus at $1,220M and $1.54 EPS. UBS assumes the Complete Genomics sale completes in early 2027.
- **2027.** ONT targets adjusted EBITDA breakeven, and PacBio targets a high-throughput platform launch. Illumina's ERP system upgrade is due to go live in H1 2027, and its FY2027 targets fall due.
- **2027-12-13.** Illumina's $500M 5.75% notes mature [10-Q].
- **2028.** Fiscal 2027 ends on 2028-01-02, with consensus at $4,918M revenue and $6.11 EPS. Illumina's revolver matures on 2028-01-04. PacBio and ONT target cash-flow breakeven. FY2028 consensus is $5,263M and $7.01 EPS [consensus sheet].
- **2030 to 2035.** Illumina's 4.75% notes mature in December 2030 and its 2.55% notes in March 2031. GRAIL CVR obligations end in August 2033, and Illumina's Singapore tax holidays expire in 2035 [10-K].

## Glossary

The glossary below merges all term lists into one definition per term. Duplicate definitions were reconciled, and the clearest version kept. Terms used only in non-sequencing peer businesses, such as Roche drugs or Thermo Fisher bioproduction, are defined in their peer files.

### Genomics and technology

- **16S sequencing**: Sequencing one bacterial marker gene to identify the microbes in a sample.
- **Amplicon sequencing**: Targeted sequencing of specific, known DNA regions that are first copied many times.
- **Amplification-free workflow**: Sequencing without first copying DNA by PCR, which saves time and avoids copying errors.
- **Aptamer**: A short DNA or RNA molecule designed to bind a specific target, such as a protein.
- **ATAC-seq / CUT&RUN**: Lab methods that map which DNA regions are open and where proteins bind DNA.
- **Base calling (basecaller)**: Software that converts a sequencer's raw signals into DNA letters.
- **Base pair**: One letter-pair of double-stranded DNA, the unit used for read length.
- **Batch effect**: A systematic technical difference between data generated on different machines or runs.
- **Bioinformatics**: Analyzing biological data with software.
- **Bulk sequencing**: Sequencing a pooled sample of many cells together.
- **Callability**: Whether a method can reliably identify variants in a given gene or region.
- **Cell barcodes / UMI**: DNA tags recording which cell a read came from (barcodes) or which individual molecule it came from (unique molecular identifiers).
- **Cell-free DNA (cfDNA) / circulating tumor DNA (ctDNA)**: DNA fragments floating in the blood. ctDNA is the share shed by tumors.
- **CMOS sensor**: A semiconductor chip, like a camera sensor, with millions of wells that detect molecules. Roche's AXELIOS uses one.
- **Copy number**: How many copies of a DNA segment a genome contains.
- **Coverage (depth, e.g. 30X)**: How many times, on average, each DNA position is read. A 30X human genome is about 100 Gb of data.
- **CRISPR perturbation**: Using gene editing to switch genes off or on and observe the effect.
- **De novo assembly**: Building a genome from scratch without a reference.
- **DNA sequencing**: Reading the order of the chemical letters (A, C, G, T) in DNA.
- **Duplex / simplex**: Reading both strands of a DNA molecule for higher accuracy (duplex), or one strand for more output (simplex).
- **Epigenetics / epigenomics**: The study of chemical marks on DNA that change gene activity without altering the sequence.
- **Exome / whole exome sequencing (WES)**: The protein-coding 1–2% of the genome, and sequencing only that part (about 8 Gb per sample).
- **FASTQ / VCF**: Standard files for raw reads with quality scores (FASTQ) and for the list of variants found (VCF).
- **FFPE**: Formalin-fixed, paraffin-embedded tissue, the standard way hospitals preserve biopsies. Its DNA is fragmented.
- **Flow cell**: The consumable glass slide or chip on which sequencing takes place. Names such as 10B, 25B and 35B give roughly the billions of reads it yields.
- **Fragmentomics**: Analysis of size and end patterns in cell-free DNA fragments.
- **Genome**: An organism's complete DNA, about three billion letters in a human.
- **Germline / somatic**: Inherited DNA present in every cell (germline), versus mutations acquired by a tumor (somatic).
- **Gigabase / terabase / petabase / megabase**: A billion, trillion, quadrillion or million DNA letters of sequence.
- **HiFi**: PacBio's long reads that are also highly accurate.
- **Homopolymer**: A run of the same letter repeated, which some sequencers misread.
- **Hybrid capture / target enrichment**: Pulling out selected genes with probes before sequencing, as in cancer panels.
- **Isoform**: One of several RNA versions a single gene can produce.
- **Library prep**: The lab steps that turn a raw DNA or RNA sample into fragments a sequencer can read.
- **Long-read sequencing**: Reading continuous stretches of thousands of letters or more, as PacBio and Oxford Nanopore do. It suits rearrangements, repeats and methylation.
- **Methylation / methylome**: Chemical methyl tags on DNA that help switch genes on and off (sometimes called the "fifth base"), and their genome-wide pattern.
- **Metagenomics**: Sequencing all DNA in a mixed sample to identify the organisms present.
- **Microarray (array)**: A chip dotted with DNA probes that checks a sample for a pre-set list of known variants. It is cheaper but less complete than sequencing.
- **Mid-read sequencing**: Reads of roughly 175–1,500 letters, between short and long reads, as claimed for Roche AXELIOS.
- **Multiomics**: Measuring several biological layers (DNA, RNA, proteins, methylation) from the same samples.
- **Multiplexing**: Pooling many tagged samples in one sequencing run.
- **Nanopore sequencing**: Reading native DNA or RNA by pulling it through a tiny pore and measuring changes in electrical current.
- **Native DNA/RNA sequencing**: Reading the original molecule directly, without copying or chemical conversion.
- **Next-generation sequencing (NGS)**: High-throughput technology that reads millions or billions of DNA fragments in parallel.
- **Pangenome / reference genome**: A standard genome sequence for a species, used for comparison. A pangenome is built from many individuals.
- **Paralog**: A near-duplicate copy of a gene elsewhere in the genome.
- **PCR / digital PCR**: A method for copying specific DNA, and a highly sensitive version that counts individual molecules.
- **Perturb-Seq**: Experiments that disrupt genes in many cells and sequence each cell to see what each gene does.
- **Phasing (haplotype)**: Working out which parent's copy of a chromosome each variant sits on.
- **Primary, secondary and tertiary analysis**: Turning signals into letters, then aligning reads and calling variants, then interpreting results into reports.
- **Proteomics**: Large-scale measurement of proteins. **Affinity proteomics** uses binding reagents, **mass spectrometry** weighs molecules, and **native protein sequencing** reads proteins directly.
- **Q score**: A logarithmic accuracy measure. Q30 is one error per 1,000 letters, Q40 one per 10,000, Q60 one per million, and Q70 is on Illumina's roadmap.
- **Read**: A single stretch of DNA sequence produced by a sequencer. **Paired reads** read a fragment from both ends.
- **Repeat expansion**: An abnormally lengthened run of repeated DNA that can cause disease, such as Huntington's.
- **Resequencing**: Sequencing a genome and comparing it with a known reference.
- **RNA-seq / transcriptomics**: Measuring which genes are active by sequencing RNA.
- **RNA splicing**: Cutting and joining a gene's RNA message before it is used to make protein.
- **Sequencing by expansion (SBX) / Xpandomer**: Roche's chemistry, which converts DNA into an enlarged copy (the Xpandomer) that is read through a sensor.
- **Sequencing by synthesis (SBS)**: Illumina's chemistry, which builds a DNA copy one tagged letter at a time and images each step.
- **Short-read sequencing**: Reading DNA in fragments of a few hundred letters at very high volume and low cost, Illumina's core approach.
- **Single-cell sequencing**: Measuring gene activity cell by cell rather than as a tissue average.
- **SNP / SNV**: A single-letter DNA variant. **SNP genotyping** tests which versions a sample carries.
- **Spatial biology (spatial transcriptomics)**: Measuring gene activity while preserving its location in tissue. It can be imaging-based (read by microscope, no sequencer) or sequencing-based (barcoded slides, then sequencing).
- **Structural variant**: A large rearrangement, deletion or duplication of DNA, often missed by short reads.
- **Synthetic long reads**: Long-range information rebuilt by stitching short reads together, as in Illumina's TruPath.
- **T2T genome**: A complete telomere-to-telomere genome with no gaps.
- **Throughput (high, mid, low)**: How much data a sequencer produces per run. It is used to sort machines from factory-scale to benchtop.
- **Variant calling**: Identifying where a sample's DNA differs from the reference.
- **Whole genome sequencing (WGS)**: Reading essentially all of a genome, more than 120 Gb per human sample.
- **XLEAP-SBS**: Illumina's newest, faster and more robust SBS chemistry, with reagents shipped at room temperature.

### Products and business

- **5-Base Solution**: Illumina's product that reads DNA sequence and methylation from one library prep (launched October 2025).
- **Academic and government (A&G)**: University and public-institute research customers.
- **AGBT / AACR / AMP / ASHG / JPM conference**: Major annual meetings on genomics technology, cancer research, molecular pathology, human genetics and healthcare investing.
- **AVITI / AVITI24 / VITARI**: Element Biosciences' benchtop sequencers and its larger system, announced in February 2026.
- **AXELIOS 1**: Roche's SBX sequencer, launched for research use on 2026-06-29 at $150 per genome.
- **BaseSpace / Illumina Connected Analytics**: Illumina's cloud platforms for managing runs and for storing and analyzing data.
- **Benchtop sequencer**: A small instrument that fits on a lab bench.
- **BioInsight / Billion Cell Atlas**: Illumina's data and AI business for drug discovery, and its first product, a large dataset of how cells respond to gene perturbations.
- **Biosecure**: Proposed U.S. legislation restricting certain Chinese biotech firms such as BGI.
- **Budget flush**: Year-end buying by customers spending leftover annual budgets.
- **Clinical cliff**: The 2024 worry that clinical customers moving to the cheaper NovaSeq X would sharply cut consumables revenue.
- **Clinical vs. research and applied**: Patient-testing labs, versus academic, government, pharma and other non-clinical customers.
- **CLIA / CAP**: U.S. certification and accreditation required to run clinical laboratories.
- **Companion diagnostic (CDx)**: A test required to select patients for a specific drug.
- **Comprehensive genomic profiling (CGP)**: A broad tumor test across hundreds of cancer genes to guide treatment.
- **Consumables**: Reagent kits and flow cells customers must buy for every run. They are Illumina's largest, highest-margin, recurring revenue line.
- **Core lab (core facility)**: A shared institutional facility that runs sequencing for many researchers.
- **Cost per gigabase / cost per genome**: The price of reading a billion letters, or one human genome, which is the industry's headline efficiency yardstick.
- **Counting applications**: Uses such as RNA-seq and single-cell work that count molecules and are priced per million reads.
- **CRO / CDMO**: Firms that run research and trials (CRO) or develop and manufacture drugs (CDMO) for drug companies.
- **DRAGEN**: Illumina's hardware-accelerated secondary-analysis software, run on FPGA chips and now GPUs.
- **Elasticity (price elasticity)**: How much more customers sequence when prices fall.
- **Emedgene / Connected Insights / Connected Multiomics**: Illumina software for rare-disease interpretation, research variant interpretation, and multiomic analysis (the last built on Partek).
- **Fluent / PIPseq**: The single-cell company Illumina acquired, and its instrument-free library-prep technology.
- **Galleri / GRAIL**: GRAIL's multi-cancer blood test, and the company Illumina formed in 2016, reacquired in 2021 and spun off in June 2024.
- **Hart-Scott-Rodino**: The U.S. law requiring antitrust review before large acquisitions close.
- **Helix**: The consumer-genomics venture Illumina launched in 2015 and deconsolidated in 2019.
- **HiSeq / HiSeq X Ten**: Older Illumina high-throughput lines. The X Ten broke the $1,000 genome in 2014.
- **IEEPA**: The U.S. emergency-powers law used to impose tariffs, which the Supreme Court ruled improper in February 2026.
- **Illumina Protein Prep**: Illumina's sequencing-based assay measuring up to 9,500 proteins per sample.
- **Import substitution**: Chinese buyers replacing foreign products with domestic ones.
- **Installed base**: The number of a vendor's active instruments at customer sites.
- **Instruments**: The sequencing machines and array scanners themselves, sold as capital equipment.
- **Ion Torrent / Genexus**: Thermo Fisher's semiconductor-based sequencers for small panels.
- **ISO 13485**: The international quality standard for medical-device manufacturing.
- **IVD / IVDR**: A regulated diagnostic test or kit run on samples outside the body, and the EU regulation governing them.
- **Key opinion leader (KOL)**: An influential researcher or clinician whose adoption shapes the field.
- **Laboratory-developed test (LDT)**: A test designed and validated within a single lab rather than sold as an approved kit.
- **Liquid biopsy**: A blood test detecting cancer from tumor DNA in the bloodstream.
- **Long-range plan (LRP)**: Illumina's 2027 targets set at its August 2024 strategy update.
- **MCED (multi-cancer early detection)**: Blood tests screening for many cancers at once.
- **MiSeq / MiSeq i100 / MiniSeq / iSeq 100**: Illumina's low-throughput benchtop sequencers. The i100 is the 2024 successor, with room-temperature reagents.
- **MRD (minimal residual disease)**: Testing for traces of cancer left after treatment. **Tumor-informed** versions build the test from the patient's own tumor; **tumor-naive** versions do not need it.
- **NextSeq 550 / 1000 / 2000**: Illumina's mid-throughput sequencers, workhorses for clinical labs.
- **NIH**: The U.S. National Institutes of Health, the main funder of academic research customers.
- **NIPT**: Noninvasive prenatal testing, a blood test of a pregnant person that screens the fetus for chromosomal conditions.
- **NovaSeq 6000**: Illumina's previous flagship high-throughput sequencer (2017), now being replaced.
- **NovaSeq X / X Plus / X Dx**: Illumina's flagship high-throughput sequencer (shipped from Q1 2023), with a clinical diagnostic version.
- **NovaSeq X transition**: Customers' shift from the NovaSeq 6000 to the X, which lowers price per gigabase but raises pull-through.
- **OEM / white labeling**: Partners selling Illumina-made instruments under their own brand.
- **Olink**: Thermo Fisher's proteomics business, the main rival to SomaLogic.
- **Onso**: PacBio's short-read sequencer, whose assets Illumina bought in January 2026.
- **Open offer letter**: Illumina's multi-year customer pricing arrangements that are not tied to a specific instrument.
- **PacBio Revio / Vega / SMRT Cell / SPRQ-Nx**: PacBio's high-throughput and benchtop long-read sequencers, its chip, and its 2026 chemistry allowing up to three uses per chip.
- **PAMA / CMS**: The U.S. law setting Medicare lab-test prices, and the agency that administers it.
- **Placement**: An instrument sold, leased or rented into a customer site.
- **PMA / 510(k)**: The FDA's longer, costlier device approval needing clinical evidence (PMA), and its shorter clearance pathway based on equivalence (510(k)).
- **PromethION / GridION / MinION**: Oxford Nanopore's high-throughput, benchtop and portable sequencers.
- **Pull-forward**: Customers buying earlier than planned, borrowing demand from later periods.
- **Pull-through**: Average annual consumables revenue generated per installed instrument.
- **Razor-razor blade model**: Placing instruments to drive years of recurring consumables purchases.
- **Reagent rental**: Placing an instrument free or cheaply in exchange for a multi-year consumables commitment.
- **Recurring revenue**: Illumina's term for consumables plus service and other, about 90% of revenue.
- **Reimbursement**: What insurers or governments pay for a test.
- **Research Use Only (RUO)**: A label meaning a product is not cleared for diagnosing patients.
- **Sequestration**: Automatic across-the-board U.S. federal spending cuts.
- **Service and other**: Revenue from support contracts, sequencing and genotyping services, and licensing.
- **SomaLogic / SomaScan / SOMAmer**: The proteomics company Illumina acquired in January 2026, its protein assay, and the engineered binding molecules the assay uses.
- **StrataMap**: Illumina's sequencing-based spatial product, launched in June 2026.
- **Switching cost / validation**: The money, time and formal re-qualification needed to move a clinical test to a new platform.
- **Technology transfer**: A test company training a hospital lab to run its test locally on partner equipment.
- **Total addressable market (TAM)**: The total revenue opportunity for a product category.
- **Total cost of workflow**: The full cost of getting a result, including sample prep, sequencing and analysis.
- **TSO 500 / TSO Comprehensive**: Illumina's roughly 500-gene tumor-profiling kit, and its FDA-approved version.
- **TruPath (Constellation)**: Illumina's on-flow-cell genome workflow that skips most library prep and adds long-range information, launched at $395 per genome.
- **Ultima UG 200 / ppmSeq**: Ultima Genomics' low-cost sequencer and its high-accuracy library-prep method.
- **Unreliable Entities List (UEL)**: A Chinese government blacklist allowing penalties on named foreign firms, including Illumina since February 2025.
- **Win rate**: The share of competitive deals a company wins.
- **Xenium / Visium / Atera / Chromium / Flex**: 10x Genomics' imaging spatial, sequencing spatial, whole-transcriptome imaging, single-cell and preserved-sample single-cell products.

### Finance and valuation

- **Accretive / dilutive**: Raising or lowering a metric such as EPS or margin.
- **Amortization (of acquired intangibles)**: Gradually expensing the purchase value of acquired technology, trade names and customer relationships.
- **Anti-dilutive buyback**: Repurchases sized to offset shares issued to employees.
- **Backlog / remaining performance obligations (RPO)**: Orders received, or contracted revenue, not yet delivered or recognized.
- **Basis point (bp)**: One hundredth of a percentage point. 100 bp equals 1 point.
- **Beat / miss / beat-and-raise**: Results above or below consensus, and a quarter that beats and then raises guidance.
- **Beta / volatility**: How much a stock moves relative to the market, and how much its price swings.
- **Book value per share**: Shareholders' equity divided by shares outstanding.
- **CAGR**: Compound annual growth rate, the smoothed yearly growth over a period.
- **Capital expenditures (capex)**: Spending on long-lived assets such as plants and equipment.
- **Cash burn / cash-flow breakeven**: The rate a loss-making firm uses cash, and the point it stops.
- **Clearing event**: A guidance reset that removes an overhang of doubt from a stock.
- **Consensus (Street)**: The average of sell-side analysts' forecasts.
- **Consolidated / Core Illumina**: Whole-company totals including GRAIL until its 2024 spin-off, versus Illumina excluding GRAIL.
- **Constant currency (CC)**: Growth with exchange-rate effects removed.
- **Contingent consideration**: Future acquisition payments owed if targets are met, revalued each quarter.
- **Contingent value right (CVR)**: A security paying holders based on a future outcome. Illumina's GRAIL CVRs pay a share of GRAIL revenue through August 2033.
- **Contract liabilities**: Cash received or billed before revenue is earned (deferred revenue).
- **Convertible notes / term notes / coupon**: Bonds exchangeable for shares, fixed-rate bonds with set maturities, and a bond's annual interest rate.
- **Deconsolidate**: Remove a subsidiary from a company's financial statements.
- **Delayed-draw term loan**: A bank loan that can be drawn after signing.
- **Demurrer**: A California court motion arguing a complaint fails legally.
- **Derivative suit**: A shareholder lawsuit brought on the company's behalf against its directors.
- **Diluted shares**: Share count including options and other securities that could become shares.
- **Discounted cash flow (DCF) / WACC / terminal growth**: Valuing a firm by discounting projected cash flows at the weighted average cost of capital, with a long-run growth rate after the forecast period.
- **Disposal Funding**: The $974M of cash Illumina gave GRAIL at spin-off to cover about 2.5 years of operations.
- **EBIT / EBITDA**: Operating profit, and operating profit before depreciation and amortization, a rough proxy for cash earnings.
- **Effective tax rate**: Tax expense as a share of pre-tax income.
- **Enterprise value (EV) and multiples**: Market value plus net debt. EV/EBITDA and EV/sales divide it by earnings or revenue.
- **EPS (earnings per share)**: Net profit divided by the number of shares.
- **Excise tax on buybacks**: A 1% U.S. tax on the value of share repurchases.
- **Fiscal year (52/53-week)**: Illumina's year ends on a Sunday near December 31 and occasionally has an extra week. FY2026 has 53 weeks, and management places the extra week in Q4 2026 (holidays and early January, "minimal" revenue impact; CFO, Q3 2026 call). Bloomberg's dates imply a 14-week Q3, which conflicts with this.
- **Fixed-cost absorption / operating leverage**: Margins rising as fixed costs are spread over more volume, so profit grows faster than revenue.
- **Form 10 / 8-K / 10-Q / 10-K**: SEC filings for a spin-off registration, material events, quarterly reports and annual reports.
- **Free cash flow (FCF) / FCF conversion / FCF yield**: Operating cash flow minus capex, that figure as a share of non-GAAP net income, and that figure as a share of market value.
- **GAAP / non-GAAP (adjusted)**: Standard U.S. accounting results, versus management-adjusted results that exclude items such as amortization, restructuring and investment gains. Illumina's non-GAAP figures still include stock-based compensation.
- **GILTI**: A U.S. minimum tax on certain foreign earnings.
- **Goodwill**: The premium paid in an acquisition above the fair value of identifiable assets.
- **Gross leverage**: Gross debt divided by trailing twelve-month EBITDA, about 1.6x for Illumina at June 2026.
- **Gross margin / operating margin / net margin**: Revenue left after direct costs, after operating expenses, and after all costs, each as a share of revenue.
- **Guidance**: Management's official forecast of future results.
- **Hold-separate order**: A regulator's requirement that an acquired company be run independently.
- **Impairment**: A write-down when an asset's book value exceeds its fair value.
- **In-process R&D (IPR&D)**: An acquired unfinished research project recorded as an asset.
- **Inventory step-up**: Writing acquired inventory up to fair value, which is expensed as it is sold.
- **Investment-grade rating**: A credit rating signalling low default risk.
- **LSD / MSD / HSD / DD**: Low-, mid- and high-single-digit, and double-digit, percentage growth.
- **Market capitalization**: The total stock-market value of a company.
- **Monte Carlo simulation**: Valuing an uncertain liability by simulating many possible outcomes.
- **Net debt / net cash**: Borrowings minus cash. A negative figure means net cash.
- **NPV / ROIC / ROE**: Today's value of future cash flows, and profit relative to invested capital or to equity.
- **Operating cash flow**: Cash generated by day-to-day operations.
- **Operating expenses (OpEx): R&D, SG&A, COGS**: Research and development; selling, general and administrative costs; and the cost of goods sold.
- **Organic growth / ROW organic**: Growth excluding currency and acquisitions, and that measure additionally excluding Greater China.
- **P/E (forward, trailing)**: Share price divided by expected or past twelve-month EPS.
- **Price target / ratings**: An analyst's expected price in about 12 months. Overweight and Buy mean expected outperformance; Neutral, Equal Weight and Hold mean in line; Underweight means expected underperformance.
- **Pro forma**: Restated results as if an acquisition had happened earlier.
- **Proxy contest**: A shareholder campaign to elect its own board nominees, such as Icahn's in 2023.
- **R&D capitalization (Section 174)**: A 2022 tax rule forcing R&D to be deducted over several years. It was reversed by the July 2025 legislation.
- **Restructuring charges / transformational initiatives**: Severance and exit costs from cost cuts. Illumina also excludes ERP-upgrade costs from non-GAAP under the "transformational initiatives" label.
- **Revolving credit facility**: A standing bank credit line the company can draw on as needed.
- **Run rate**: The current pace of revenue, cost or savings, extended to a full year.
- **Sell-side / buy-side / independent research**: Bank analysts publishing for investors, investors themselves, and firms such as Bloomberg Intelligence that neither trade nor bank the stock.
- **Sequential / year over year (YoY)**: Compared with the prior quarter, or the same period a year earlier.
- **Share repurchase (buyback) / treasury stock**: A company buying its own shares, and the shares it then holds.
- **Spin-off**: Separating a business by distributing its shares to the parent's shareholders.
- **Statement of Objections / Article 22**: A formal EU charge sheet, and the EU merger rule the Commission used to review GRAIL.
- **Stock-based compensation (SBC)**: The non-cash cost of paying employees in shares.
- **Tax holiday**: A temporary tax exemption. Illumina's Singapore holidays run to 2035.
- **Valuation allowance**: A write-down of deferred tax assets unlikely to be used.
- **Working capital**: Current assets minus current liabilities.

## Source coverage and known gaps

### What the folder holds

The folder holds 188 source documents. Most (116) concern Illumina itself, so the company file is deep. Illumina material spans earnings calls, SEC filings, investor conferences, research notes, consensus sheets, insider data and 23 expert calls.

Among peers, Oxford Nanopore is the best covered, with 43 documents, mostly research. Thermo Fisher, 10x Genomics and MGI are thin, with two to five documents each. Conclusions about those companies rest on little primary material.

The table below counts documents by company and type.

| Company | Document types (count) | Total |
|---|---|---|
| Illumina (ILMN) | Research 31, expert calls 23, filings 18, conferences 16, earnings calls 15, decks 6, insider data 4, consensus 3 | 116 |
| Oxford Nanopore (ONT) | Research 30, news 6, transcripts 5, consensus 2 | 43 |
| PacBio (PACB) | Research 6, transcripts 3, consensus 2 | 11 |
| Roche | Research 3, transcripts 2, consensus 2 | 7 |
| MGI Tech | Research 4, consensus 1 | 5 |
| 10x Genomics (TXG) | Transcripts 2, annual meeting 1 | 3 |
| Thermo Fisher (TMO) | Transcripts 2 | 2 |
| Sector | Research 1 | 1 |
| **Total** | | **188** |

### Known gaps

**Expert calls.** The folder holds 23 distinct expert calls, short of the goal of 29. Four further files were the same calls saved from both Tegus and AlphaSense, and those duplicates are archived.

Read the expert material with two cautions. Several experts' knowledge of Illumina is three to five years old, and many now work for competitors (Roche, PacBio, ONT, SOPHiA). Interviewers also supplied some widely repeated figures themselves, such as the 10% long-read share.

**Illumina conferences.** No transcripts exist after the TD Cowen conference of 2026-03-03. The likely missing events are Bernstein (May), Goldman Sachs (June) and Morgan Stanley (September 2026).

**Q2 2026 research.** Reaction notes to Illumina's Q2 2026 results (2026-07-30) are in hand from J.P. Morgan, Barclays, Freedom Broker, Ameriprise and Bloomberg Intelligence, but not from UBS.

**History.** Earnings call transcripts begin at Q1 2023, while SEC filings begin at Q1 2022. The 2022 GRAIL and EU events therefore rest on filings alone.

**Peers:**

- **Roche:** only one recent results call (H1 2026) is held, and the Q1 2026 sales call is missing. Q3 2026 sales are due around 22–23 October 2026.
- **Thermo Fisher:** the Q1 2026 call, consensus estimates and research are missing. Q3 2026 results are due around 22 October 2026.
- **10x Genomics:** the Q2 2026 call, consensus estimates and research are missing.
- **MGI Tech:** no call transcripts are held. MGI is listed in Shanghai, and English transcripts generally do not exist.
- **Element Biosciences and Ultima Genomics:** both are private, so they appear only through expert calls and other companies' commentary.

**Timing.** These notes are a snapshot as of 2026-10-10. Illumina's Q3 2026 call (2026-10-29) arrived afterwards. Its headline figures are added to the timeline above, but other Core Notes sections may not yet fully reflect it.
