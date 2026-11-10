# Start Here: Illumina Research Core Notes

*As of 2026-10-10.*

# 00 Start Here

*Core Notes section 00. Written as of 2026-10-10. Some material added in later builds runs to early November 2026, including Illumina's Q3 2026 results of 29 October and expert calls loaded on 9 November; those items are flagged by date. Bracketed tags cite the source. Full detail is in the Working Notes (see `Working Notes/INDEX.md`).*

This file is the front door to the research folder. It covers four things in turn:

- How the folder and the Core Notes are laid out.
- A one-page plain-English orientation to Illumina and its market.
- A single merged timeline of everything dated in the sources.
- A glossary, followed by an honest account of which sources are in hand and which are missing.

If you read nothing else, read the one-page orientation and skim the 2025–2026 parts of the timeline.

## How these notes are organized

### The folder

The folder keeps three things apart: original documents, readable notes on each document, and synthesized briefings.

- **`CLAUDE.md`** sets the rules Claude Code follows in every chat on this folder. It covers what to read first, how to use agents, how to write and where to save outputs.
- **`Core Notes/`** holds this master briefing, about 150,000 tokens across 19 files. Read it first in every chat.
- **`Working Notes/INDEX.md`** lists every source document once, with its date, a short summary and links. It is the fastest way to find material.
- **`Working Notes/Extracts/`** holds an exhaustive, readable note on every source document, filed by company and document type.
- **`Working Notes/Sources/`** holds the original documents, renamed and filed the same way. Use them when exact wording, tables or numbers matter.
- **`Working Notes/Outputs/`** holds everything produced in later chats: datasets, artifacts, primers and analyses.
- **`Working Notes/_Archive/`** holds duplicates and off-topic files. Do not use them unless asked.
- **`Inbox/`** is where new files go. After adding them, run `python _Build/build.py ingest`.
- **`_Build/`** holds the build script that turns the Inbox into extracts and Core Notes, along with its state and log.

### The Core Notes files

The Core Notes move from basic orientation to specific debates. Files 01–08 cover Illumina itself, and file 09 ties the competition together. Files 10–15 profile each listed competitor, and files 16–18 are addenda on particular investment questions.

| File | What it covers |
|---|---|
| 00_Start_Here | This guide: folder map, one-page orientation, master timeline, glossary, coverage and gaps |
| 01_ILMN_Company_Primer | What Illumina does: technology, products, customers, geography, reporting conventions, history and strategy |
| 02_ILMN_Financial_History_and_Guidance | Reported results and how guidance moved, from the 2022 filings through Q3 2026 |
| 03_ILMN_Consensus_Estimates | What sell-side analysts expect for revenue, margins and EPS, compared with guidance |
| 04_ILMN_Earnings_Calls_2023-2024 | Calls through the GRAIL saga, the CEO change and the NovaSeq X transition |
| 05_ILMN_Earnings_Calls_2025-2026 | Calls covering China sanctions, tariffs, SomaLogic and the return to growth |
| 06_ILMN_Conferences_and_Investor_Events | Management remarks at broker conferences, JPM, AGBT and strategy days |
| 07_ILMN_Expert_Calls | What customers, former employees and competitors said in about 100 expert interviews |
| 08_ILMN_Equity_Research | Broker and independent research: ratings, price targets and the arguments behind them |
| 09_Competitive_Landscape | Arena-by-arena view of competition, from high-throughput sequencing to spatial biology |
| 10_Peer_Oxford_Nanopore | Oxford Nanopore (ONT), the faster-growing long-read rival |
| 11_Peer_PacBio | PacBio, the cash-constrained long-read rival that sold its short-read assets to Illumina |
| 12_Peer_Roche | Roche, whose Axelios sequencer launched in June 2026 |
| 13_Peer_Thermo_Fisher | Thermo Fisher: Ion Torrent sequencing and Olink proteomics |
| 14_Peer_10x_Genomics | 10x Genomics, the single-cell and spatial-biology incumbent |
| 15_Peer_MGI_Tech | MGI Tech, China's leading sequencer maker |
| 16_Addendum_Clinical_Consumables_Thesis | Whether clinical consumables growth is durable |
| 17_Addendum_Open_Offer_Pricing_Power | Illumina's pricing power and its multi-year pricing agreements ("open offer" letters) |
| 18_Addendum_Thesis_Scrape_Alt_Data | Alternative data gathered to test the investment thesis |

## Illumina and its market in one page

### What DNA sequencing is

Every living cell carries instructions written in DNA, a long molecule spelled out in four chemical "letters" called bases. DNA sequencing means reading the order of those letters. A human genome, the full set of DNA instructions, is about three billion letters long. Reading it lets doctors and scientists find the changes that cause inherited disease, drive cancer or shape a patient's response to a drug.

The dominant method is next-generation sequencing (NGS). DNA is cut into millions of short fragments, all of them are read at once, and software pieces them back together. Output is measured in gigabases (Gb), or billions of letters read. A whole human genome needs more than 120 Gb of data, against about 8 Gb for an exome (the roughly 2% of the genome that codes for proteins) [JPM, 2026-01-13].

### What Illumina sells

Illumina is the world's largest maker of sequencing machines and chemistry. It reports about 21,000 active instruments at more than 8,000 customers in about 160 countries [JPM, 2026-01-13]. Its proprietary chemistry, sequencing by synthesis (SBS), copies each DNA fragment one tagged letter at a time while a camera records each step. The chemistry came from the 2007 purchase of Solexa for $480 million, which Bloomberg Intelligence calls possibly "one of the best health-care deals in history" [BI, 2025-11-13].

Illumina sells four kinds of things:

- **Instruments (sequencers)**, from the high-throughput NovaSeq X for genome centers and big clinical labs, through the mid-sized NextSeq, to the benchtop MiSeq i100.
- **Consumables**, the reagent kits and flow cells (glass slides on which DNA is read) that customers must buy for every run.
- **Services**, including instrument service contracts, in-house sequencing and genotyping, and partnership revenue.
- **Software**, such as DRAGEN, which turns raw data into results.

Two newer businesses sit on top. "Multiomics" means measuring more than one biological layer, such as proteins or chemical marks on DNA; it is anchored by the SomaLogic protein-measurement acquisition, closed January 2026. BioInsight is a data and AI unit selling to drug makers. Illumina also has a shrinking microarray business (chips that check known DNA variants rather than reading every letter), worth $358 million, or 8% of revenue, in fiscal 2025 [10-K FY2025].

### Who the customers are

Illumina splits customers into two groups:

- **Research & Applied** (about 60% of sequencing consumables): universities, government labs, pharma research, and "applied" uses such as agriculture.
- **Clinical** (about 40%): hospitals and diagnostic labs testing patients. About half of clinical demand is cancer testing, a quarter genetic disease and a fifth prenatal screening [JPM, 2026-01-13].

These groups are moving in opposite directions, the single most important trend in the business. Clinical consumables outside China grew 12% in 2025 and 14% year over year in Q3 2026. Research & Applied fell 7% in 2025 and 6% in Q3 2026 [Q3 2026 slides]. Research depends heavily on government grants and has been hurt by cuts and delays at the U.S. National Institutes of Health (NIH).

### How Illumina makes money

The model resembles razors and blades: a placed sequencer generates years of consumables purchases. Management says about 90% of revenue is recurring, meaning consumables plus service [JPM, 2026-01-13]. In fiscal 2025 (the year to December 28, 2025) [Q4 2025 deck; 10-K FY2025]:

- **Revenue** was $4,343 million, flat against $4,332 million for Illumina excluding GRAIL in 2024.
- **Consumables** were 74% of revenue, up from 68% in 2023.
- **Non-GAAP operating margin** was 23.1%, up from 21.3% in 2024. Non-GAAP means the company's adjusted figures, which strip out items such as acquisition amortization and investment gains.
- **Non-GAAP EPS** (earnings per share) was $4.84, up from $4.16.

The key unit of value is "pull-through," yearly consumables revenue per installed instrument. A NovaSeq X pulls through about $1.35 million a year, roughly twice the older NovaSeq 6000 and about 15 times a NextSeq [Q4 2025 deck].

Management raised 2026 guidance at every quarterly report. The latest guide is $4.64–4.66 billion of revenue, about 23.6% operating margin and $5.40–5.45 of EPS [Q3 2026 slides, 2026-10-29]. Its stated 2027 targets are high-single-digit revenue growth outside China, a 26% operating margin and roughly 15% EPS growth [JPM, 2026-01-13].

### Who the competitors are

Illumina still holds most of the sequencing market, but competition now comes from every direction:

- **High-throughput:** Roche's Axelios (launched June 29, 2026, at $150 per genome), private Ultima Genomics (the cheapest) and private Element Biosciences (the mid-tier favorite).
- **Long reads:** PacBio and Oxford Nanopore sell machines that read long continuous DNA stretches.
- **China:** MGI dominates the domestic market.
- **Proteomics:** Thermo Fisher's Olink competes with SomaLogic.
- **Spatial biology:** 10x Genomics' imaging instruments need no sequencer at all.

### The key debates right now

1. **Can clinical growth outrun research decline?** Bulls point to sticky clinical customers, who face validation costs of $100,000 to millions of dollars to switch platforms [Experts, Apr–Oct 2026], and to fast-growing cancer tests such as MRD (blood tests for cancer left after treatment). JPM upgraded to Overweight on this view [JPM, 2026-06-10]. Former employees question how generously Illumina classifies "clinical" revenue.
2. **How fast does share erode, and at what price?** Former insiders put Illumina's share at 65–70%, down from 80–90% and heading toward 50–60% [Experts, Jun–Oct 2026]; these are opinions, not data. Analysts see quiet discounting: in Q1 2026 the NovaSeq X carried 76% of high-throughput volume but only 55% of revenue [Barclays, 2026-04-30]. Bloomberg Intelligence says Illumina is "trading price for volume" [BI, 2026-05-01].
3. **Is Roche's Axelios a disruptor or a parity product?** UBS called the $150 genome "relatively benign" [UBS, 2026-02-26]. Barclays sees a well-funded rival able to force "another round of pricing headwinds" [Barclays, 2026-02-05]. By September, Roche's CEO said about a third of its roughly 100 first-year placements had been made [JPM Roche CEO call, 2026-09-08].
4. **China.** China put Illumina on its sanctions list in February 2025. Greater China revenue fell from $308 million in 2024 to $243 million in 2025, then returned to 7% growth in Q3 2026 [Q3 2026 slides].
5. **Valuation.** The stock rose from about $80 in May 2025 to about $278 in early October 2026, above most analyst targets. Barclays (Underweight, $160) says it "cannot justify" about 35 times earnings; JPM (Overweight, $230) sees clinical stickiness as underappreciated [Barclays and JPM, Jul 2026].

## Master timeline

This timeline merges every dated event in the sources into one chronological list. Dates given only to the month or year are marked approximate where it matters. Forward-looking items (targets and scheduled events) appear at the end. Where sources disagree on a date or figure, the entry says so.

### Before 2020

- **2005:** Oxford Nanopore was spun out of the University of Oxford with £0.5 million from IP Group.
- **2007:** Illumina bought Solexa, inventor of its SBS chemistry, for $480 million, when Illumina's own market value was $1.8 billion [BI, 2025-11-13].
- **Q3 2011:** Illumina shipped its first MiSeq benchtop sequencer.
- **2012:** U.S. budget sequestration (automatic federal spending cuts) and a government shutdown temporarily capped Illumina's growth, showing its exposure to research funding [BI, 2025-11-13].
- **2013:** BGI's MGI acquired Complete Genomics, a U.S. sequencing company.
- **2014:** Illumina's HiSeq X Ten became the first system to break the $1,000-per-genome barrier.
- **August 18, 2015:** Illumina announced Helix, a consumer-genomics venture funded with $100 million from two venture investors.
- **2016:** Illumina formed GRAIL to develop a blood test for early cancer detection. Roche began a collaboration with NVIDIA, partly to handle sequencer data.
- **2017:** Illumina shipped its first NovaSeq 6000 (Q1) and released version 1 of its VeriSeq NIPT prenatal test. A former manager recalls Illumina holding about 92% of the instrument market in mid-2017 [Expert: former commercial-enablement manager, Jun 2026].
- **2019:** Illumina deconsolidated Helix (removed it from its accounts), which Bloomberg called "a prudent step to tighten the portfolio" [BI, 2025-11-13]. It also released VeriSeq NIPT v2, its last major prenatal-test update according to a Veritas executive [Expert, Jan 2026].

### 2020

- **February 5:** The board authorized a $750 million share buyback, of which $15 million remained unused through 2023.
- **During the year:** Illumina abandoned its planned purchase of PacBio, announced in 2018, after opposition from the U.S. Federal Trade Commission (FTC). Roche acquired Stratos Genomics, source of its sequencing-by-expansion (SBX) technology.

### 2021

- **March 8:** Illumina entered a $750 million revolving credit facility (a standing bank credit line).
- **March 23:** It issued $500 million of 0.55% notes due 2023 and $500 million of 2.55% notes due 2031.
- **May 20:** Ameriprise added Illumina to its Recommended List as a Buy at $385.31.
- **August 18:** Illumina closed its purchase of GRAIL without European Union approval, starting a multi-year regulatory fight.
- **Third quarter:** Illumina's market capitalization peaked at about $76 billion [BI, 2025-11-13].
- **November 10:** J.P. Morgan initiated Oxford Nanopore at Overweight.
- **During the year:** Illumina released a 24-sample batch format for its prenatal test. Former insiders date the arrival of BGI/MGI, Singular, Element and Ultima to 2021–22, after which Illumina "just didn't have the ability to keep the price premium high," producing flat growth from about 2022 [Expert: former Illumina AD, Jul 2026].

### 2022

- **January 3:** An accounting change (ASU 2020-06) cut reported interest expense on Illumina's convertible notes.
- **June 9:** CFO Sam Samad departed; Joydeep Goswami became interim CFO.
- **July 13:** The EU General Court ruled the European Commission had jurisdiction over the GRAIL deal.
- **July 14:** Illumina signed a $325 million patent settlement and cross-license with BGI/Complete Genomics, letting Complete Genomics re-enter the U.S. in 2023.
- **About July 15:** GRAIL's NHS-Galleri trial completed enrollment of 140,000 participants.
- **July 19:** The Commission issued a formal Statement of Objections; Illumina accrued a $453 million fine provision in Q2 2022.
- **September 6:** The Commission prohibited the GRAIL acquisition.
- **Around September 29:** Illumina unveiled the NovaSeq X, promising the lowest cost per gigabase and 2.5 times the throughput of earlier systems.
- **About October:** At its investor day, Illumina set mid-teens revenue growth and 25% operating margin targets and sized its addressable market (total revenue opportunity) at more than $125 billion.
- **October 21:** UBS rated MGI a Buy with a Rmb140 target.
- **November 3:** The Q3 2022 filing booked a $3,914 million goodwill impairment on GRAIL (a write-down of the deal premium) and guided 2022 revenue flat to up 1%.
- **November 15:** Illumina announced its first cost cuts.
- **December 13:** It issued $500 million of 5.80% notes due 2025 and $500 million of 5.75% notes due 2027.

### 2023

- **January:** The Czech Republic added comprehensive genomic profiling (broad tumor DNA testing) to its national fee schedule. JPM's Oxford Nanopore target peaked at 460p against a 246p share price (January 3). Illumina put in place a new $750 million credit line maturing January 2028 (January 4).
- **February 7–8:** Illumina guided 2023 revenue growth of 7–10% and non-GAAP EPS of $1.25–$1.50. JPM rated the stock Neutral with a $271 target the next day.
- **February 17:** The fiscal 2022 annual report (10-K) showed revenue of $4,584 million (+1%) and a net loss of $4,404 million, driven by the GRAIL write-down.
- **March:** Illumina began shipping the NovaSeq X Plus globally and repaid $500 million of notes due 2023 (March 23). It announced its first long-read offering (approximate), with rollout from around May.
- **April 25:** On the Q1 call Illumina reported 67 NovaSeq X shipments and raised its 2023 X target to more than 330. It held guidance, planned more than $100 million of cost cuts, and set core operating margin targets of 25% for 2024 and 27% for 2025. The May 5 quarterly filing showed revenue down 11% while still reiterating 7–10% growth for the year.
- **May 5:** UBS reinstated MGI at Buy with a Rmb108 target, then cut it to Rmb102 (August) and Rmb93 (January 2024).
- **May 10:** Barclays initiated PacBio at Equal Weight with a $14 target.
- **June:** CEO Francis deSouza departed and Charles Dadswell became interim CEO. A late-June filing disclosed headcount and real-estate reductions.
- **July:** Illumina received an SEC document request letter (approximate). On July 12 the Commission fined it €432 million for closing GRAIL during the regulatory review.
- **August 9–17:** On the Q2 call Illumina reported 109 NovaSeq X shipments, raised its X supply goal to more than 390, and cut 2023 guidance to roughly flat core revenue; the August 11 filing put growth at about +1%. At UBS on August 17, management explained the cut from 6–9% growth to about flat and cited about 260 X orders.
- **August 15:** Illumina repaid $750 million of 0% convertible notes in cash.
- **September 11:** At Morgan Stanley, interim CFO Goswami said about 110 NovaSeq X had been sold and called the 2024 25% margin target a stretch.
- **September 25:** Jacob Thaysen became CEO.
- **Q3 (ended around October 1):** Illumina booked an $821 million GRAIL goodwill and in-process R&D impairment.
- **October 12:** The Commission ordered Illumina to divest GRAIL.
- **Late October:** Illumina launched the 25B flow cell, the highest-capacity NovaSeq X consumable, cutting cost to about $200 per genome. One source dates the launch to late November.
- **November 9–10:** On its Q3 call Illumina cut 2023 guidance a second time, reduced X shipments to 330–340, formed a board special committee on GRAIL, and said 2024 would look "very similar" to 2023. JPM cut its target to $110 and UBS to $111 the next day.
- **Late November:** At Evercore (November 28) management said 2024 revenue would be roughly flat and Q3 orders were 50 NovaSeq X against 60 expected. At Piper Sandler (November 29) Thaysen ruled out large acquisitions and put China at about 10% of revenue.
- **Mid-December:** The EU Court of Justice heard Illumina's jurisdiction appeal. On December 17 Illumina announced it would divest GRAIL.
- **December 31:** Fiscal 2023 ended with revenue of $4,504 million (−2%) and a GAAP loss of $7.34 per share. The consensus data set shows "adjusted EPS" of $0.86, on a data-provider definition that differs from Illumina's non-GAAP EPS.

### 2024

- **January:** At JPM (January 9) Illumina pre-reported a Q4 2023 beat, 352 NovaSeq X shipped in 2023 and $175 million of cost savings. Around January 15 it launched the 1.5B flow cell kit and cut more jobs, bringing cumulative role reductions to about 12%.
- **February 8–9:** The Q4 2023 call guided 2024 core revenue flat with about a 20% operating margin and targeted GRAIL divestiture by end-June. Freedom Broker rated the stock Hold with a $150 target.
- **March:** Illumina merged its marketing and commercial teams and launched XLEAP-SBS chemistry and the P4 flow cell on the NextSeq 1000/2000. JPM cut its Oxford Nanopore target to 210p (March 6) as ONT set a medium-term plan for more than 30% annual growth. UBS dropped its Buy on PacBio (March 28).
- **March 31:** Q1 2024 ended with consolidated revenue of $1,076 million (−1%) and a $126 million net loss. Illumina planned no buybacks in 2024.
- **April:** The Commission approved Illumina's GRAIL divestment plan (April 12). Ankur Dhingra joined as CFO around mid-April.
- **May:** Dhingra's first call (May 2) reported core revenue of about $1.06 billion (−2%) and reiterated flat revenue and a 20% margin. At RBC (May 14) he held guidance and capped GRAIL cash at about $1 billion; at Bernstein (May 29) he targeted a GRAIL decision by end-June.
- **June 20:** Illumina drew a $750 million, 6.7% delayed-draw term loan to fund GRAIL's spin-off cash.
- **June 24:** GRAIL was spun off. Illumina distributed 85.5% of the shares (one GRAIL share per six Illumina shares), kept 14.5%, and gave GRAIL $974 million to fund about 2.5 years of operations. Q2 2024 (ended June 30) carried $1.9 billion of GRAIL impairments and a $1,988 million net loss.
- **July 31:** A Helix contingent value right (a payment linked to an earlier deal) was settled for $82.5 million in cash.
- **August 6:** The Q2 call cut 2024 revenue guidance to −2% to −3%, raised the margin guide to 20.5–21%, introduced EPS guidance of $3.80–3.95, and announced a $200 million savings plan.
- **August 13:** A strategy update set 2027 targets of high-single-digit growth, at least 500 basis points of margin expansion (a basis point is one hundredth of a percentage point), and double-digit-to-teens EPS growth. The board authorized a $1.5 billion buyback, and the update previewed the 5-base and "comprehensive genome" products. Barclays rated the stock Equal Weight with a $125 target (August 14).
- **August 15:** The FTC dismissed its GRAIL complaint.
- **August 29:** UBS cut its MGI target to Rmb56.70, raising it to Rmb60 in November.
- **September 3–6:** The EU Court of Justice ruled the Commission lacked jurisdiction over GRAIL. The Commission withdrew all its GRAIL decisions, including the €432 million fine, and Illumina booked a gain of about $481 million.
- **September 9:** Illumina issued $500 million of 4.65% notes due 2026 and repaid the term loan; buybacks resumed in the quarter. One summary dates the Fluent BioSciences (single-cell) acquisition to Q3 2024, while expert and broker sources put the close in early 2025.
- **October–December:** Illumina announced the MiSeq i100 benchtop sequencer, which began shipping in December with more than 70 placed by year-end. The cheaper single-flow-cell NovaSeq X also began shipping in December. UBS reinstated PacBio at Neutral with a $2 target (November 1).
- **November 4:** The Q3 call cut 2024 revenue guidance to about −3% while raising the margin guide to 21–21.5% and EPS to $4.05–4.15. Analysts debated a "clinical cliff," the fear that clinical labs moving to the cheaper NovaSeq X would cut spending.
- **November 5:** The U.S. presidential election, flagged by Thaysen as a source of uncertainty.
- **November 20:** At Wolfe, Dhingra said Q3 sequencing volume rose about 40% while consumables revenue rose about 5%, "largely price," and put China at about $75 million a quarter.
- **December 3:** At Evercore, management cited 528 NovaSeq X installed, framed 2025 placements at 200–240, and targeted 75% or more of high-throughput volume on the X in the second half of 2025.
- **December 29:** Fiscal 2024 ended with consolidated revenue of $4,372 million (−2.9%), a net loss of $1,223 million (−$7.69 per share) and backlog of $657 million. Core Illumina non-GAAP EPS was $4.16. Total assets fell to $6,303 million from $10,111 million as GRAIL left the accounts.

### 2025

- **January:** Illumina launched Single Cell 3' RNA Prep, and its Fluent acquisition closed (early 2025). It announced NVIDIA and Truveta partnerships (January 13). At JPM (January 14) it pre-reported Q4 2024 revenue of about $1.1 billion with 91 NovaSeq X placements and guided 2025 to low-single-digit growth and about a 23% margin. Oxford Nanopore announced "CapEx-first" pricing (selling devices outright instead of placing them free), live from February, and its first restructuring.
- **February 4:** China's Ministry of Commerce added Illumina to its Unreliable Entities List, a sanctions designation; some sources link the move to U.S. tariffs.
- **February 6:** The Q4 2024 call reported revenue of $1.1 billion (+1%) and reaffirmed 2025 guidance excluding the China impact.
- **February 10:** Barclays downgraded Illumina to Underweight with a $100 target; Freedom Broker moved to Buy at $130.
- **February (other):** Roche unveiled SBX at the AGBT conference. At Illumina's AGBT session (February 25), it said Constellation would cost "hundreds of dollars" and announced a 5-billion-cell atlas with the Broad Institute. UBS upgraded Roche to Buy (February 13) and set its PacBio target at $1.50.
- **March 4:** China banned exports of Illumina sequencers into China. JPM cut its Oxford Nanopore target to 190p, with the shares at 105p. UBS downgraded MGI to Neutral on March 18.
- **March 30:** Q1 2025 ended with revenue of $1,041 million and GAAP net income of $131 million. A $100 million cost-reduction program was in place, prompted partly by NIH funding uncertainty.
- **April:** U.S. and other tariffs took effect on goods from Illumina's Singapore plant; Illumina estimated the cost at about $85 million.
- **May:** 10x Genomics withdrew its full-year guidance (approximate) amid "drastic" U.S. research funding changes. On May 8 Illumina cut 2025 guidance to $4.18–4.26 billion of revenue and $4.20–4.30 of EPS, citing China, NIH funding and tariffs, and began guiding China separately. JPM cut its target to $85 (May 9) near the stock's low of about $80; UBS cut to $98 (May 13). At Bernstein (May 28) Thaysen reaffirmed the 2027 plan excluding China and explained an insider share purchase.
- **June:** On June 22 Illumina agreed to buy SomaLogic from Standard BioTools for $350 million in cash plus up to $75 million in milestones and royalties. Barclays cut its PacBio target to $1.50 (June 24).
- **July 4:** A U.S. tax law ended mandatory R&D capitalization (which had forced research costs to be deducted over years), leading Illumina to book a $42 million valuation allowance in Q3.
- **July 31:** Q2 2025 (ended June 29) revenue was $1,059 million (−3% constant currency), with EPS of $1.19 and $370 million of buybacks. Illumina announced the SomaLogic deal, guided 2025 revenue −2.5% to −0.5% and EPS $4.45–4.55, set NovaSeq X transition targets of about 75% of high-throughput volume and 50% of high-throughput revenue by year-end, and cut its instrument outlook.
- **August:** PacBio reported Q2 revenue of $40 million (August 7). Oxford Nanopore said co-founder and CEO Gordon Sanghera would step down. UBS moved its MGI target to Rmb74.50, then Rmb82.50.
- **September:** Illumina launched Protein Prep, a sequencing-based method measuring 9,500 proteins. A Massachusetts research institute received what would be its last new NIH award before March 2026 [Expert, Mar 2026].
- **October 1:** NIH's fiscal 2026 began during a federal shutdown, delaying new grants.
- **October:** Illumina launched the 5-Base Solution, reading genetic variants and DNA methylation (chemical marks that switch genes on and off) in one workflow, and announced BioInsight. The first All of Us long-read data from PacBio were published. MGI licensed CoolMPS outside Asia to Swiss Rockets for $20 million upfront plus a $20 million milestone (October 13). UBS cut its MGI target to Rmb73.80 (October 27).
- **October 30:** Q3 2025 (ended September 28) revenue was $1,084 million, roughly flat (about +2% excluding China), with EPS of $1.34 and a peak non-GAAP operating margin of 24.5%. Illumina raised 2025 EPS guidance to $4.65–4.75, said it had beaten its X transition targets early, and disclosed approval for contract manufacturing in China. UBS raised its target to $120 and JPM set $105 [UBS; JPM, 2025-10-31].
- **November:** China granted export permission on November 5, effective November 10, case by case only. PacBio's Q3 revenue of $38.4 million missed and it cut its 2025 guide to $155–160 million (November 5). Bloomberg Intelligence published its Illumina profile (November 13). At Wolfe (November 19) Thaysen confirmed the 2027 growth target now excludes China. Illumina issued $500 million of 4.75% notes due 2030 (November 25). Oxford Nanopore launched a research-use TB test with bioMérieux and announced a "strategic realignment."
- **December:** Oxford Nanopore named Francis Van Parys CEO effective March 2026 (December 8), and JPM upgraded Roche to Neutral. Illumina repaid its $500 million 5.80% notes (December 12). JPM raised its Illumina target to $130 and Barclays to $110 (December 15); Barclays raised PacBio to $2.
- **December 28:** Fiscal 2025 ended with revenue of $4,343 million, GAAP net income of $850 million, non-GAAP EPS of $4.84, a 23.1% operating margin, $931 million of free cash flow and backlog of $738 million (+12%).

### 2026

**January**

- Illumina closed the purchase of PacBio's short-read (Onso) assets for about $48.1 million net (around January 15).
- VCU's Genomics Core co-director described a newly installed NovaSeq X Plus and a 10–20% growth outlook [Expert, 2026-01-06].
- Oxford Nanopore reported fiscal 2025 revenue of £223–224 million (+24% constant currency) at JPM (January 12); its CFO called 2027 EBITDA breakeven the "North Star."
- At JPM on January 13, Illumina pre-announced Q4 2025 revenue of about $1.16 billion (+4% constant currency, +7% ex-China), more than 95 NovaSeq X placements and full-year EPS of about $4.76–4.79. It reaffirmed its 2027 targets and launched BioInsight.
- Chief Commercial Officer Everett Cunningham departed (January 16).
- A Veritas executive described a "capped" European prenatal-testing market with lab-to-lab prices down 40–50% (January 28).
- MGI pre-announced a 2025 net loss of Rmb221–273 million, worse than UBS expected (January 26). Barclays raised its Roche target to CHF 410 (January 29).
- **January 30:** Illumina closed SomaLogic. Sources give the price three ways: $350 million upfront (headline); $363 million net cash (Barclays); and $460 million under purchase accounting, made up of $382 million cash plus $81 million of contingent payments less a $3 million settlement [10-Q Q2 2026].

**February**

- MGI agreed to buy nanopore and spatial assets from BGI Tech for Rmb365.7 million (February 1).
- UIUC's DNA Services director reported billing down about 15% in late 2025 [Expert, 2026-02-02].
- An Anthropic clinical-research plug-in for Claude triggered a sell-off in tools and contract-research stocks dubbed the "Claude crash," per a broker note (February 3).
- **February 5:** Illumina reported Q4 2025 revenue of $1,159 million and EPS of $1.35, above the January preliminary range of $1.27–$1.30; the sources do not explain the gap. Clinical consumables grew 20% outside China. Initial 2026 guidance was $4.50–4.60 billion of revenue (+1–3% organic), a 23.3–23.5% margin and EPS of $5.05–5.20. UBS raised its target to $135, Barclays held $110 Underweight, and JPM cut to $120 Neutral the next day.
- Freedom Broker raised its target to $140, Buy (February 10).
- PacBio reported Q4 revenue of $44.6 million and guided 2026 to $165–180 million with a 41–44% gross margin (February 12).
- A Delaware court heard the motion to dismiss the consolidated GRAIL derivative suits (suits brought by shareholders on the company's behalf) on February 13; it was still pending at July 31.
- Around mid-February, Illumina's annual list-price increase of about 3–5% took effect, with tariff surcharges at some labs [Experts, Feb–Jul 2026].
- 10x Genomics reinstated 2026 revenue guidance of $600–625 million.
- Element unveiled its VITARI high-throughput sequencer (February 19); UBS said pressure on Illumina stays.
- The U.S. Supreme Court ruled the IEEPA emergency-powers law did not authorize the 2025 tariffs.
- MGI agreed to sell Complete Genomics for $50 million and license StandardMPS in North America to Swiss Rockets (February 24).
- **February 26:** At AGBT, Roche priced Axelios consumables at $150 per genome and $0.06 per million reads. JPM and UBS kept their Illumina ratings.
- Late-February expert calls included Mount Sinai's core director, expecting a Q1 rebound after Q4 fell more than 20%, and the University of Minnesota's director on Axelios pricing.

**March**

- Oxford Nanopore reported fiscal 2025 revenue of £223.9 million (March 2) and guided 2026 growth to 21–25%, below the 27.5% consensus, dropping its target of more than 30% annual growth. The shares fell 12%. Van Parys became CEO.
- At TD Cowen (March 3), Illumina said it had launched TruPath (formerly Constellation, a synthetic long-read product) at $395 per genome, put Q70 accuracy and a 35B flow cell on its roadmap, and called its 2026 guide prudent.
- Barclays downgraded PacBio to Underweight, citing TruPath and Axelios (March 6).
- At Barclays (March 11), ONT's CFO called TruPath "imputed… not direct." Bloomberg Intelligence refreshed its Illumina outlook the same day.
- JPM cut its Roche target to CHF 325 (March 12).
- The White House budget office released full fiscal 2026 funds to NIH (March 19). NIH had made only 496 new R01 grants since October 1, against 1,099 a year earlier.
- The Court of International Trade ordered refunds of IEEPA tariffs.
- March expert calls included UCSD (about a 10% reagent decline, X Plus discounting), Natera (Q70 for MRD), TGen (a 13% R01 success rate), the Complete Genomics CEO ("Illumina will definitely lose market share") and the South Carolina core director (planning an Element AVITI24).
- Barclays called ONT's guidance cut a "clearing event" and raised its target to 172p (March 25).

**April**

- Illumina introduced new regional reporting with Q1: USCAN, EMEALA, APAC and Greater China.
- Roche hosted a few hundred prospective Axelios customers.
- April expert calls included the Broad Institute, an Axelios beta site, whose Illumina spend was flat from 2024 to 2025 while its data doubled; an Arizona core whose consumables spend fell about 80% as work moved to Element; Cedars-Sinai, which said only a $50–75 genome would drive "massive adoption"; and Yale, whose Illumina spend fell from $6–7 million to $3–4 million but which called TruPath "exceptionally good."
- Ultima offered Vanderbilt a near-free instrument in return for reagent commitments.
- Barclays cut its PacBio target to $1.00 (April 14).
- 10x launched Atera, an imaging-based spatial instrument needing no sequencer, at AACR for about $495,000 (dated April 18 or around April 22).
- **April 28:** Illumina's board authorized a new $1.5 billion buyback.
- MGI reported 2025 revenue of Rmb2.78 billion (−7.7%); UBS cut its target to Rmb58 (April 29).
- **April 30:** Illumina reported Q1 2026 revenue of $1,091 million (+4.8% reported, +1.2% organic), EPS of $1.15 and more than 80 NovaSeq X placements. Guidance rose to $4.52–4.62 billion and EPS of $5.15–5.30. Barclays set $122 (Underweight).

**May**

- JPM set a $125 target, Neutral (May 1); Bloomberg Intelligence said Illumina was "trading price for volume." Freedom Broker raised its target to $155 (May 6).
- PacBio's Q1 revenue of $37.2 million missed and it cut its guide to $165–175 million (May 7). 10x reported Q1 revenue of $150.8 million (May 7).
- A Complete Genomics director called Roche Illumina's number-one threat (May 8).
- **May 12:** At its Diagnostics Day, Roche set a summer Axelios launch, about 100 first-year systems and a "blockbuster" ambition of more than $1 billion. A former Illumina strategy director said Roche would win a "maximum 5%" share in two years.
- **May 15:** A California state court certified the class in the GRAIL-related securities suit; Illumina sought appeal on July 28.
- Oxford Nanopore launched products at London Calling (May 21). PacBio began shipping SPRQ-Nx chemistry with reusable SMRT Cells on Revio (May 31).

**June**

- A former Illumina manager estimated share had fallen from 92% to about 70% (June 8).
- **June 10:** JPM upgraded Illumina to Overweight with a $185 target, citing "stickier-than-appreciated" clinical customers and a 62-customer survey.
- Duke reported its 10x spend halving as work shifted to spatial (June 16).
- Barclays raised its target to $145, still Underweight (June 23).
- EpiCypher said long reads would take about half its methylation work in two to three years (June 29).
- Illumina launched StrataMap, its spatial product, which works on fresh-frozen tissue only.
- **June 29:** Roche launched Axelios 1 for research use only (not cleared for diagnosing patients).

**July**

- Oxford Nanopore's H1 trading update showed revenue of £116.5 million (+12% constant currency), about 7% below consensus (July 13).
- JPM raised its Illumina target to $220 (July 16).
- Roche's H1 showed Diagnostics up 3% at constant exchange rates, with China down 15% (July 23). Thermo Fisher's Q2 call reported 5% organic growth with no discussion of sequencing (July 23).
- A large wave of expert calls (about July 6–31) produced most share estimates in the Competitive Landscape note. A former Illumina associate director said share fell from about 80% to the mid-60s (July 24), and the largest academic genome center planned to buy Axelios.
- **July 24–27:** Illumina agreed to buy out the remaining SomaLogic milestone and royalty from Standard BioTools for $30.04 million, paying on July 27.
- **July 30:** Illumina reported Q2 2026 revenue of $1,159 million (+9.5% reported, +6.5% organic), EPS of $1.31 and more than 95 NovaSeq X placements, while clinical consumables growth eased to 15%. Guidance rose to $4.60–4.64 billion and EPS of $5.30–5.40. Illumina announced a whole-genome MRD workflow, six Billion Cell Atlas partners, and new executives and board members.
- **July 31:** JPM set $230 (on a December 2027 basis) and Barclays $160 (Underweight). Bloomberg Intelligence called the 2027 goal "increasingly visible."

**August**

- Freedom Broker downgraded Illumina to Hold with a $185 target, saying "much of the upside is now priced in" (August 5).
- PacBio cut 2026 guidance to $155–165 million and pushed cash-flow breakeven to 2028 (August 5); CEO Christian Henry was replaced by Mark Van Oene.
- Illumina replaced its $750 million revolver with a new $1 billion five-year facility (August 13) and issued $300 million of 4.95% notes due 2029.
- Oxford Nanopore's H1 results (August 19) showed revenue of £116.7 million. It raised its headline guide to 23–27% but cut underlying growth to 16–20%, signed a $20 million diagnostics cross-license, and set 2030 targets of more than $700 million of revenue and an EBITDA margin above 15%.
- MGI reported H1 revenue of Rmb1.37 billion (+18.9%), with Americas sequencing up 126% (August 24).

**September**

- A South Carolina-serving core bought an Element AVITI24 with NIH funding, moving most short-read work off Illumina. Louisville's director said academic demand was "rerouted" to contract labs (September 8).
- **September 8:** Roche's CEO said about one-third of the roughly 100 first-year Axelios placements had been made. Seeking Alpha put Illumina's fair value at $188 (Hold).
- **September 9:** Illumina repaid its $500 million 4.65% notes.
- At Morgan Stanley (September 15), PacBio's new CEO targeted $40 million of 2027 savings, and Thermo's CEO expected academic and government demand to return to growth in 2027.
- CMS proposed cuts to Medicare lab-test prices under the PAMA law (September 21).
- On September 30 the federal court dismissed the GRAIL securities class action's third amended complaint with leave to amend; a new dismissal motion is pending. This conflicts with the primer, which places the dismissal in September 2025.

**October** (items after October 10 were added in later builds)

- Illumina's stock reached about $278, above most analyst targets.
- October expert calls included Sanofi, whose sequencing spend was up 25% and which preordered two Atera systems (October 5); a core describing a NovaSeq X trade-in "discount war" (October 9); a New York clinical lab that rejected Ultima for clinical use (October 16); and an ONT director forecasting Illumina's European share falling from about 80% to 55–60% in three to five years (October 23).
- Illumina launched a $1 billion commercial paper program, a form of short-term borrowing (October 8).
- Bloomberg's consensus snapshot (October 10) put fiscal 2026 revenue at $4,624.8 million and EPS at $5.36.
- **October 4 (quarter end):** Q3 2026 was a 14-week quarter; consensus expected $1,154 million of revenue and $1.36 of EPS.
- **October 28:** The U.S. announced trade restrictions on some Chinese sequencing competitors, according to Thaysen on the Q3 call.
- **October 29:** Illumina's Q3 2026 beat consensus: revenue of $1,166 million excluding tariff refunds (+4.8% organic), EPS of $1.44, a 25.0% operating margin, and Greater China back to growth (+7%). It booked a one-time $79 million cost benefit from tariff refunds and a $37 million revenue reduction for refunds passed to customers, both excluded from headline figures. Guidance rose to $4.64–4.66 billion and EPS of $5.40–5.45. GSK joined the Billion Cell Atlas, and the BioInsight platform launched with the SpliceAI2 model.

### Scheduled and targeted: late 2026 and beyond

- **Late 2026:** StrataMap and 10x's Atera become widely available, with about 40 Atera units shipping mostly in Q4. UK Biobank's 50,000-sample Oxford Nanopore methylation results are due. Roche targets 100 installed cobas i 601 mass-spectrometry instruments.
- **January 3, 2027:** Illumina's 53-week fiscal 2026 ends. Consensus expects Q4 revenue of $1,220 million and EPS of $1.54, against guidance of $1.22–1.24 billion and $1.51–$1.56.
- **2027:**
  - Illumina's 35B NovaSeq X flow cell is expected around January, cutting cost from about $2.50 to $2 per gigabase [Expert, Jul 2026].
  - Oxford Nanopore plans an mRNA quality-control assay (January), discontinuation of Flongle flow cells (February), a strategy update (February), adjusted EBITDA breakeven during the year, and a re-timed PromethION Q-Line launch late in the year.
  - Sanofi expects Atera installations around Q1, and a contract lab expects to validate TruPath in Q1.
  - Illumina's ERP (core finance software) upgrade goes live in the first half.
  - PacBio plans a new high-throughput platform; the Complete Genomics divestment should complete early in the year.
  - A Tennessee medical center has budgeted an Element purchase for June, and an Ivy League core expects rivals to start taking share from 2027.
  - $500 million of Illumina notes mature in December.
  - The FY2027 targets fall due: high-single-digit ex-China growth and a 26% operating margin. Consensus expects revenue of $4,918 million and EPS of $6.11.
- **2028:** The state GRAIL securities class action is set for trial on March 20. PacBio and Oxford Nanopore both target cash-flow breakeven. Roche expects Chinese diagnostics to return to single-digit growth. Consensus expects Illumina revenue of $5,263 million and EPS of $7.01.
- **2030 and later:** Oxford Nanopore's 2030 targets fall due. Illumina notes mature in December 2030 and March 2031. Bloomberg consensus reaches $7,370.5 million of revenue and $12.30 of EPS in 2032. The GRAIL contingent value rights run through August 2033, and Illumina's Singapore tax holidays expire in 2035.

## Glossary

Terms are grouped into three families, alphabetical within each. Where sources defined a term several ways, the clearest definition is kept.

### Genomics and technology

- **16S sequencing**: Sequencing one bacterial gene to identify which microbes are present.
- **Adapter ligation**: The library-prep step attaching platform-specific DNA tags to fragments.
- **Amplicon sequencing**: Sequencing targeted regions first copied by PCR.
- **Amplification-free (PCR-free) workflow**: Sequencing without first copying DNA, saving time and avoiding copying errors.
- **Aptamer**: A short engineered DNA or RNA molecule that binds a specific protein; SomaLogic uses them to measure proteins.
- **ATAC-seq**: Measures how accessible DNA packaging is, which reflects gene regulation.
- **Barcode (index)**: A short DNA tag identifying which sample, cell or molecule a read came from.
- **Base / base pair**: One DNA letter, or one letter-pair in double-stranded DNA; the unit of read length.
- **Base calling (basecaller)**: Converting a sequencer's raw signal into DNA letters.
- **Batching**: Waiting to collect enough samples to fill a run.
- **Bioinformatics**: Computational analysis of biological sequence data.
- **Biomarker**: A measurable biological signal indicating disease or likely treatment response.
- **Bisulfite sequencing / EM-seq / TAPS / RRBS**: Chemical or enzymatic methods for reading methylation on short-read sequencers.
- **Bulk sequencing (bulk RNA-seq)**: Measuring the average across many cells rather than cell by cell.
- **Callability**: Whether a method can reliably identify variants in a given region.
- **Carryover**: Leftover material contaminating the next run, a concern with reusable sensors.
- **Cell-free DNA (cfDNA)**: DNA fragments circulating freely in the blood.
- **ChIP-seq / CUT&RUN / CUT&Tag**: Methods mapping where proteins bind on DNA.
- **Circular consensus**: PacBio's method of reading one molecule repeatedly to raise accuracy.
- **Clonal hematopoiesis**: Age-related blood-cell mutations that sequencing can mistake for cancer signals.
- **CMOS sensor**: A camera-like semiconductor chip that reads signals; reusable in Roche's Axelios.
- **Combinatorial (split-pool) barcoding**: Labeling cells with unique tag combinations over several rounds instead of using droplets.
- **Companion diagnostic (CDx)**: A test required to decide whether a patient receives a specific drug.
- **Comprehensive genomic profiling (CGP)**: A large tumor DNA panel checking hundreds of genes to guide cancer therapy.
- **Copy-number variant / microdeletion**: A gain or loss of a DNA segment, large or small.
- **Cost per gigabase / cost per base**: The price of producing a billion DNA letters (or one); the traditional efficiency yardstick.
- **Cost per genome**: The consumables cost of sequencing one human genome.
- **Counting applications**: Uses such as RNA-seq, single-cell and protein readouts that only tally sequences, so modest accuracy suffices.
- **Coverage (depth, e.g. 30X)**: How many times each position is read on average; 30X is standard for an inherited-disease genome, while tumors need 120X or more.
- **CRISPR perturbation**: Using gene editing to switch genes on or off and observe the effect.
- **ctDNA (circulating tumor DNA)**: Tumor-derived DNA fragments in blood.
- **De novo assembly**: Building a genome from scratch without a reference.
- **Diagnostic yield**: The share of patients for whom a test finds a diagnosis.
- **Digital PCR (ddPCR)**: A highly sensitive PCR method counting single molecules by splitting a sample into thousands of droplets.
- **DNA**: The molecule carrying genetic instructions, written in four chemical letters.
- **DNA methylation (5mC, 5hmC, m6A)**: Chemical tags on DNA that regulate gene activity; the codes are distinct forms of the tag.
- **DNA sequencing**: Reading the order of the bases in DNA.
- **Duplex / simplex sequencing**: Reading both strands of a molecule for high accuracy, or one strand for more output at lower cost and accuracy.
- **Epigenomics (epigenetics)**: The study of chemical marks that change gene activity without changing the sequence.
- **Exome**: The roughly 2% of the genome that codes for proteins, often sequenced as a cheaper alternative to a whole genome.
- **F1 score**: An accuracy measure combining precision and recall.
- **FASTQ**: The standard file format for raw reads.
- **FFPE**: Formalin-fixed, paraffin-embedded tissue, the standard way hospitals preserve biopsies; it fragments DNA.
- **Fiber-seq**: A long-read assay reading DNA accessibility and methylation together.
- **Flow cell**: The consumable glass slide or chip on which a run happens. Names such as 1.5B, 10B, 25B and 35B indicate billions of reads; larger ones are cheaper per read when full.
- **Foundation model**: A large AI model trained on broad data and adaptable to many tasks.
- **FPGA / GPU**: Specialized chips that accelerate data analysis and AI.
- **Fragmentomics**: Analysis of cell-free DNA fragment sizes and patterns.
- **Fresh-frozen tissue**: Tissue frozen immediately after collection; better for some assays but rarer in clinical archives than FFPE.
- **Fully loaded cost**: The cost of a result including sample prep, labor, quality control and analysis, not just reagents.
- **Genome**: An organism's complete DNA, about three billion letters in humans.
- **Genome backbone (slicing)**: Running one whole genome and analyzing only chosen genes in software as a "virtual panel."
- **Genotyping**: Identifying which known variants a sample carries.
- **Germline vs somatic**: Inherited DNA in every cell, versus mutations acquired in a tumor.
- **Gigabase (Gb) / terabase / petabase**: A billion, trillion or quadrillion DNA letters; gigabases are the standard output unit.
- **Histology / H&E / IHC / ISH**: Microscopic study of stained tissue, using the routine stain (H&E), protein stains (IHC) or DNA and RNA stains (ISH).
- **Hybrid capture / target enrichment**: Pulling out selected regions with probes before sequencing.
- **Imaging-based spatial**: Spatial methods that read molecules in tissue optically, needing no sequencer.
- **In situ sequencing**: Reading sequence directly inside intact cells or tissue.
- **Index hopping**: Reads assigned to the wrong sample barcode, causing cross-contamination.
- **Isoform**: One of several alternative RNA versions of a gene.
- **Library / library prep**: DNA or RNA converted into a form a sequencer can read, and the lab steps that make it.
- **Limit of detection**: The smallest amount of a target a test reliably detects.
- **Liquid biopsy**: A blood test detecting cancer or other disease from circulating DNA.
- **Long-read sequencing**: Reading continuous stretches of thousands of letters or more, as PacBio and Oxford Nanopore do; suited to complex regions and structural variants.
- **Mass spectrometry**: Identifying molecules by mass, the traditional route to measuring proteins.
- **Megabase**: One million DNA letters.
- **Metagenomics**: Sequencing all DNA in a mixed sample to find every organism present.
- **Methylome**: The full pattern of methylation marks across a genome.
- **Microarray**: A chip that checks known variants rather than reading every letter.
- **Minimal residual disease (MRD)**: Testing, usually by blood, for traces of cancer left after treatment.
- **Mosaicism**: A variant present in only some of a person's cells.
- **Multi-cancer early detection (MCED)**: A blood test screening for many cancers before symptoms, such as GRAIL's Galleri.
- **Multiomics**: Measuring several biological layers (DNA, RNA, proteins, methylation) from the same samples.
- **Multiplexing**: Pooling many barcoded samples in one run to cut cost per sample.
- **Nanopore sequencing**: Reading DNA or RNA by passing it through a tiny pore and measuring changes in electrical current.
- **Native DNA/RNA sequencing**: Reading the original molecule directly, without copying or chemical conversion.
- **Next-generation sequencing (NGS)**: Reading millions of short fragments in parallel and reassembling them with software.
- **NIPT (noninvasive prenatal testing)**: A maternal blood test screening fetal DNA for chromosome conditions such as trisomies (extra chromosome copies).
- **Paired-end reads**: Reading both ends of a fragment, standard on Illumina.
- **Pangenome**: A reference built from many people's genomes rather than one.
- **PCR / qPCR**: Copying DNA many times; qPCR measures the amount as copying proceeds.
- **Perturb-seq**: Switching genes off in many cells and reading effects by single-cell sequencing; very data-hungry.
- **Phasing / haplotype**: Working out which variants sit together on the same inherited chromosome copy.
- **Population genomics**: Large, often government-funded national programs sequencing many citizens.
- **ppm (parts per million)**: A detection limit; "below 5 ppm" means finding one tumor fragment among more than 200,000 normal ones.
- **Primary / secondary / tertiary analysis**: Base calling; aligning reads and calling variants; interpreting results for a report.
- **Proteomics / proteogenomics**: Large-scale protein measurement, and doing it with DNA-barcode readouts on sequencers.
- **Q score (Q30, Q38, Q40, Q70)**: A logarithmic accuracy scale: Q30 is one error per 1,000 bases, Q40 one per 10,000, and Q70 about one per 10 million.
- **Read**: A single stretch of sequence produced by a sequencer.
- **Repeat expansion**: An abnormal lengthening of repeated DNA that can cause disease.
- **Reversible terminator**: A chemically capped letter that lets the machine add and read one base at a time.
- **RNA-seq / transcriptomics**: Sequencing RNA to measure how active each gene is; the transcriptome is all RNA a cell expresses.
- **RNA splicing**: Cutting and joining gene messages before they are used to make proteins.
- **Sequencing by expansion (SBX) / Xpandomer**: Roche's chemistry, copying DNA into an enlarged surrogate (an Xpandomer) read through a nanopore-type sensor.
- **Sequencing by synthesis (SBS)**: Illumina's core chemistry, building a copy of each fragment one tagged letter at a time and imaging each step.
- **Sequencing intensity**: The amount of data used per test or sample.
- **Short-read sequencing**: Reading fragments of a few hundred letters; cheap, accurate, and Illumina's core approach.
- **Single-cell sequencing**: Measuring gene activity cell by cell rather than averaged across tissue.
- **SNP**: A single-letter DNA difference between individuals.
- **Spatial biology / spatial transcriptomics**: Measuring gene activity while recording where in a tissue it occurs; sequencing-based or imaging-based.
- **Structural variant**: A large rearrangement, deletion, duplication or inversion that short reads often miss.
- **Synthetic long reads**: Long-range structure inferred from short reads rather than read directly, as in TruPath.
- **T2T genome**: A complete "telomere-to-telomere" genome with no gaps.
- **Targeted panel**: A test sequencing only selected genes.
- **Therapy selection**: Testing a tumor's mutations to choose the right drug.
- **Throughput (high / mid / low)**: Data per run, which sorts sequencers into production, mid-size and benchtop tiers.
- **TMB / MSI / HRD**: Tumor biomarkers for mutation load, a DNA-repair defect (microsatellite instability) and homologous recombination deficiency; they predict response to certain drugs.
- **Trio sequencing**: Sequencing a patient and both parents to interpret variants.
- **Tumor-informed vs tumor-naive MRD**: MRD tests that do or do not first sequence the patient's tumor to choose what to track.
- **UMI (unique molecular identifier)**: A tag letting reads from one molecule be combined and counted accurately.
- **Variant calling / VCF**: Identifying differences from a reference, and the standard file listing them.
- **Virtual cell model**: An AI model trained on perturbation data to simulate cell responses.
- **Whole-genome sequencing (WGS)**: Reading a person's entire DNA; whole-exome sequencing (WES) reads only protein-coding parts.

### Products and business

- **5-Base Solution**: Illumina's product, launched October 2025, reading variants and methylation in one run.
- **Academic & government (A&G)**: University and public-institute research customers.
- **AGBT / AACR / ASHG / AMP**: Major annual conferences on genomics technology (February), cancer research (April), human genetics and molecular pathology; launches cluster around them.
- **Atera**: 10x Genomics' imaging-based whole-transcriptome spatial instrument, launched April 2026 at about $495,000; needs no sequencer.
- **Attach rate**: How much of a vendor's own consumables customers buy with its instruments.
- **AVITI / AVITI24 / VITARI**: Element Biosciences' mid-throughput sequencer, its spatial-capable version, and its higher-throughput box unveiled February 2026.
- **Axelios 1**: Roche's SBX sequencer, priced at about $750,000, launched for research use June 29, 2026.
- **BaseSpace**: Illumina's cloud platform for running, storing and analyzing data.
- **Billion Cell Atlas**: BioInsight's large dataset of cell responses to gene perturbations, sold to pharma partners such as GSK.
- **BioInsight**: Illumina's data, software and AI business for drug discovery, announced October 2025.
- **Budget flush**: Year-end spending of leftover annual budgets.
- **Channel check**: An investor interview with a customer or distributor to gauge demand.
- **Chromium / Flex / Flex Apex**: 10x's single-cell instrument and its probe-based kits for large or preserved-tissue studies.
- **CLIA / CAP**: The U.S. certification a lab needs to report patient results, and the pathologists' accreditation program.
- **Clinical cliff**: The 2024 worry that clinical labs moving to the cheaper NovaSeq X would sharply cut consumables spend.
- **Clinical vs Research & Applied**: Illumina's split between patient-testing labs and academic, government, pharma, consumer and agricultural users.
- **Commoditization**: Products becoming interchangeable and competing mainly on price.
- **Complete Genomics (T1)**: MGI's U.S. subsidiary and its sequencer; MGI agreed in February 2026 to sell it to Swiss Rockets for $50 million.
- **Connected Analytics / Insights / Multiomics**: Illumina's cloud data platform and its software for interpreting and integrating data types.
- **Consumables**: Reagent kits and flow cells bought for every run; Illumina's largest, most recurring line, 74% of 2025 revenue.
- **CoolMPS / StandardMPS**: MGI's proprietary sequencing chemistries.
- **Core facility (core lab)**: A shared university or institute lab selling sequencing to many researchers and needing to recover its costs.
- **Core Illumina**: Illumina excluding GRAIL, used for like-for-like 2023–2024 comparisons.
- **CRO / CDMO**: Contract research organizations selling research or sequencing as a service, and contract drug manufacturers.
- **Decentralization / send-out / hub-and-spoke**: Testing moving to local labs, versus shipping samples to a central reference lab or regional hub.
- **DRAGEN**: Illumina's accelerated software turning raw reads into variant calls; experts disagree on how much it locks customers in.
- **Early access / bake-off**: Pre-launch placement with select customers, and a head-to-head platform comparison.
- **Elasticity (price elasticity)**: How much more sequencing customers do when price falls; experts say it has weakened.
- **Emedgene**: Illumina's AI variant-interpretation software for rare disease.
- **Expert network**: Firms such as Guidepoint, Tegus and AlphaSense that arrange paid expert interviews.
- **Fluent / PIPseq**: Illumina's instrument-free single-cell kits from the Fluent BioSciences acquisition.
- **Foundation Medicine (FoundationOne CDx)**: Roche's cancer-testing lab and its centralized tumor-profiling test, a potential Axelios channel.
- **Galleri**: GRAIL's multi-cancer early-detection blood test.
- **GRAIL**: The cancer-screening company Illumina formed in 2016, bought back in 2021, was forced to divest, and spun off in June 2024, keeping 14.5%.
- **Greater China / ROW**: Mainland China, Hong Kong and Taiwan, and "rest of world."
- **GridION / PromethION / MinION / P2**: Oxford Nanopore's benchtop, high-throughput, portable and smaller-PromethION instruments; Q-Line and Dx versions serve quality control and diagnostics.
- **Helix**: The consumer-genomics venture Illumina launched in 2015 and deconsolidated in 2019.
- **HiSeq / HiSeq X Ten**: Illumina's older high-throughput systems; the X Ten broke the $1,000 genome in 2014.
- **Import substitution**: Chinese buyers replacing foreign products with domestic ones, often under policy pressure.
- **Installed base**: Instruments in active use at customers.
- **Instruments**: Sequencers and array scanners, sold as one-time capital purchases.
- **Internalization / white labeling / OEM**: Labs bringing testing in-house; reselling another lab's test under one's own brand; partners selling Illumina-made products under their own name.
- **IVD / IVDR / CE-IVD**: Regulated diagnostic products, and the EU regulation and mark governing them.
- **KAPA**: Roche's library-prep reagent brand.
- **Key opinion leader (KOL)**: An influential researcher or clinician whose adoption shapes the field.
- **Laboratory-developed test (LDT)**: A test designed, validated and run within one lab rather than sold as an approved kit.
- **List price / rack rate**: A vendor's published, undiscounted price.
- **MiSeq / MiSeq i100 / MiniSeq / iSeq 100**: Illumina's benchtop sequencers; the i100 (shipping from late 2024) uses room-temperature reagents.
- **NextSeq 500/550/1000/2000**: Illumina's mid-throughput sequencers, important in clinical labs.
- **NIH / R01 / payline / notice of award**: The main U.S. research funder, its standard multi-year grant, the funding cutoff score, and the formal notice a grant is funded.
- **NovaSeq 6000**: Illumina's previous flagship, first shipped 2017, now being retired.
- **NovaSeq X / X Plus / X Dx**: Illumina's flagship high-throughput sequencer, first shipped Q1 2023, and its clinical-cleared version.
- **Olink**: Thermo Fisher's antibody-based proteomics platform read out on sequencers; SomaLogic's main rival.
- **Open offer letter**: Illumina's multi-year customer pricing arrangements, not tied to a specific instrument.
- **P1–P4 / S4 flow cells**: Flow cells for the NextSeq 1000/2000 and the NovaSeq 6000.
- **Placement**: An instrument sold, leased or rented into a customer site.
- **Protein Prep**: Illumina's sequencing-based assay measuring up to 9,500 proteins, launched September 2025.
- **Pull-through**: Average annual consumables revenue per installed instrument, about $1.35 million for a NovaSeq X.
- **Pull-forward / stocking order**: Customers buying ahead of need, borrowing demand from later periods.
- **Razor-razor blade model**: Placing instruments to drive recurring consumables sales.
- **Reagent rental**: An instrument placed at little or no upfront cost in return for committed reagent purchases.
- **Recurring revenue**: Consumables plus service and other revenue, about 90% of Illumina's total.
- **Research Use Only (RUO)**: A label meaning a product is not cleared for diagnosing patients.
- **Revio / Vega / Sequel / Onso**: PacBio's high-throughput, benchtop and older long-read sequencers, and its short-read box sold to Illumina.
- **Service and other**: Revenue from service contracts, in-house sequencing, partnerships and licensing.
- **SMRT Cell / SPRQ-Nx / HiFi / Kinnex**: PacBio's sequencing chip (now reusable), newer chemistry, accurate long reads, and RNA kits.
- **SomaLogic (SomaScan, SOMAmer)**: The aptamer-based proteomics business Illumina acquired in January 2026, with its assay and binding reagents.
- **StrataMap**: Illumina's sequencing-based spatial product, launched June 2026, about 1 µm resolution, fresh-frozen tissue only.
- **Switching costs / validation**: The cost of proving a test works on a new platform, which experts put at $100,000 to millions per assay.
- **Tender**: A government-run competitive bidding process.
- **Total cost of ownership (TCO)**: Instrument, service, reagents, labor and switching costs combined.
- **Trade-in credit**: A discount on a new instrument for returning an old one.
- **TruPath (formerly Constellation)**: Illumina's synthetic long-read genome product, launched early 2026 at $395 list.
- **TSO 500 / TSO Comprehensive**: Illumina's large cancer gene panel and its FDA-approved version.
- **Ultima UG200 / ppmSeq**: Ultima Genomics' low-cost high-throughput sequencer and its high-accuracy mode.
- **Unreliable Entities List (UEL)**: A Chinese sanctions list that can restrict a foreign company's trade; Illumina was added in February 2025.
- **USCAN / EMEALA / APAC / AMEA**: Illumina's regions from 2026 (U.S. and Canada; Europe, Middle East, Africa and Latin America; Asia Pacific outside Greater China) and its former Asia Pacific, Middle East and Africa region.
- **Utilization**: The share of an instrument's capacity actually used, which drives consumables sales.
- **VeriSeq NIPT**: Illumina's prenatal-test kit, without a major update since 2019.
- **Visium / Visium HD / Xenium**: 10x's sequencing-based and imaging-based spatial platforms.
- **XLEAP-SBS**: Illumina's newest, faster and more robust sequencing chemistry.
- **Regulatory and policy terms**:
  - **510(k)**: The shorter FDA clearance route, based on equivalence to an existing device.
  - **PMA (premarket approval)**: The costlier FDA route requiring clinical evidence.
  - **Hart-Scott-Rodino**: U.S. antitrust review of large deals.
  - **IEEPA**: The emergency-powers law behind the 2025 tariffs, ruled improper in February 2026.
  - **PAMA**: The law setting Medicare lab-test prices.
  - **Biosecure / DoD 1260H / NIH 1271 lists**: U.S. measures steering federally funded work away from certain Chinese firms.

### Finance and valuation

- **Adjusted (non-GAAP)**: Company-adjusted results excluding items such as acquired-intangible amortization, acquisition costs, restructuring and investment gains. Illumina's version still includes stock-based pay.
- **Amortization (of intangibles)**: Spreading the cost of acquired technology or brands over their useful life.
- **Backlog / remaining performance obligations**: Firm orders or contracted revenue not yet recognized.
- **Basis point (bp)**: One hundredth of a percentage point; 100 bp is 1 point.
- **Beat / miss / beat-and-raise**: Results above or below consensus, and a quarter that beats and then raises guidance.
- **Beta**: How much a stock moves relative to the market.
- **CAGR**: Compound annual growth rate, the smoothed yearly growth over a period.
- **Capital expenditures (capex)**: Spending on long-lived assets such as plants and equipment.
- **Commercial paper**: Short-term unsecured borrowing sold to investors.
- **Consensus (the Street)**: The average sell-side forecast, the market's baseline.
- **Constant currency (CC/CER)**: Growth with exchange-rate effects removed.
- **Contingent consideration / earnout / milestone**: Extra acquisition payments owed only if targets are hit.
- **Contingent value right (CVR)**: A payment right tied to a business's results. Illumina's GRAIL CVRs pay 2.5% of GRAIL's first $1 billion of annual revenue and 9% above that, through August 2033.
- **Convertible notes**: Bonds exchangeable for shares at a preset price.
- **DCF / WACC / terminal growth**: Valuing a company by discounting forecast cash flows at its cost of capital, with an assumed long-run growth rate.
- **Deconsolidation**: Removing a business from consolidated accounts.
- **Depreciation**: Spreading an asset's cost over its life; for customers it delays instrument replacement.
- **Derivative lawsuit / securities class action / class certification**: Shareholder suits on the company's behalf, investor group suits over misleading statements, and the order letting a group suit proceed.
- **Dilution / accretion**: Lowering or raising a per-share or margin metric, for example through an acquisition.
- **EBIT / EBITDA**: Operating profit, and operating profit before depreciation and amortization, a rough cash-earnings measure.
- **Effective tax rate**: Income tax as a share of pre-tax profit.
- **Enterprise value (EV)**: Equity market value plus net debt.
- **EPS (diluted)**: Net profit per share, counting shares options and convertibles could create.
- **EV/EBITDA, EV/Sales, P/E**: Multiples comparing value with operating earnings, revenue or per-share earnings.
- **Fiscal year (52/53-week)**: Illumina's year ends on a Sunday near December 31; fiscal 2026 has 53 weeks and a 14-week Q3.
- **Free cash flow (FCF) / FCF yield / FCF conversion**: Operating cash flow minus capex; that figure over market value; and that figure over net income.
- **GAAP**: Standard U.S. accounting rules used in official filings.
- **Goodwill / impairment**: The price paid above identifiable assets in a deal, and a write-down when an asset is worth less than book value.
- **Gross leverage / net debt**: Gross debt over trailing 12-month EBITDA, and debt minus cash.
- **Gross margin**: Revenue left after the direct cost of products and services, as a share of revenue.
- **Guidance**: Management's official forecast.
- **Intangible assets / IPR&D**: Non-physical assets such as technology and brands, and unfinished acquired research.
- **Investment-grade rating**: A credit rating signaling low default risk.
- **LSD / MSD / HSD / DD**: Low-, mid- and high-single-digit and double-digit growth (about 1–3%, 4–6%, 7–9%, 10%+).
- **Market capitalization**: A company's total stock-market value.
- **NTM / TTM**: Next and trailing twelve months.
- **Operating leverage**: Profits growing faster than revenue because costs grow more slowly.
- **Operating margin**: Operating profit as a percentage of revenue.
- **Organic growth / ROW organic growth**: Growth excluding currency and acquisitions, and that measure also excluding Greater China.
- **Price target / ratings**: An analyst's 12-month price estimate. Overweight or Buy means expected outperformance; Neutral, Equal Weight or Hold means in-line; Underweight means expected underperformance.
- **Purchase accounting**: Valuing an acquired company's assets and liabilities at fair value on closing.
- **Restructuring charges**: One-time costs of layoffs and facility exits.
- **Revolving credit facility / term notes / delayed-draw term loan**: A standing bank credit line; fixed-rate bonds with set maturities; a loan drawn after signing.
- **ROIC / ROE**: Return on invested capital and return on equity.
- **Section 174 (R&D capitalization)**: A U.S. tax rule forcing R&D to be deducted over years, removed in July 2025.
- **Sell-side / buy-side / independent research**: Broker research for clients; investors who buy securities; research from firms that neither trade nor bank the stock, such as Bloomberg Intelligence.
- **SG&A / R&D / OpEx / COGS**: Selling, general and administrative costs; research and development; total operating expenses; direct cost of goods sold.
- **Share repurchase (buyback)**: A company buying back its own stock, reducing the share count.
- **Spin-off**: Separating a business by distributing its shares to existing shareholders.
- **Stock-based compensation**: The non-cash cost of paying employees in shares.
- **Tariff refund**: Recovery of IEEPA duties, booked by Illumina in Q3 2026 as lower costs and partly as customer credits.
- **Tax holiday / valuation allowance**: Reduced tax granted to attract investment, and a reserve against tax assets unlikely to be used.
- **Total addressable market (TAM)**: The total revenue opportunity in a market.
- **Year-over-year (YoY) / sequential (QoQ)**: Compared with the same period a year earlier, or with the prior quarter.

## Source coverage and known gaps

### What is in hand

The research base holds about 270 source documents, heavily weighted toward Illumina (about 196) with thinner competitor files. Expert calls (101) are the largest block, more than a third of the total, so the competitive and customer analysis leans on interviews with customers, former employees and competitors: informative, but anecdotal and often biased. Illumina's own disclosures are well covered, with earnings calls from Q1 2023 and SEC filings from Q1 2022. Among peers, Oxford Nanopore is best covered (mostly research); Thermo Fisher and 10x Genomics rest on two or three transcripts each. One transcript is filed under the ticker WGS, which belongs to GeneDx, a clinical genome-testing lab.

The table below gives exact counts by company and document type.

| Company | Document type | Count |
|---|---|---|
| Illumina (ILMN) | Expert calls | 101 |
| Illumina | Research | 31 |
| Illumina | Filings | 19 |
| Illumina | Conferences | 16 |
| Illumina | Earnings calls | 15 |
| Illumina | Decks | 7 |
| Illumina | Insider data | 4 |
| Illumina | Consensus | 3 |
| Oxford Nanopore (ONT) | Research | 30 |
| Oxford Nanopore | News | 6 |
| Oxford Nanopore | Transcripts | 5 |
| Oxford Nanopore | Consensus | 2 |
| PacBio (PACB) | Research | 6 |
| PacBio | Transcripts | 3 |
| PacBio | Consensus | 2 |
| MGI Tech | Research | 4 |
| MGI Tech | Consensus | 1 |
| Roche | Research | 3 |
| Roche | Transcripts | 2 |
| Roche | Consensus | 2 |
| 10x Genomics (TXG) | Transcripts | 2 |
| 10x Genomics | Annual meeting | 1 |
| Thermo Fisher (TMO) | Transcripts | 2 |
| Sector | Research | 1 |
| WGS (GeneDx) | Transcript | 1 |

### Known gaps

Keep these gaps in mind when weighing conclusions.

1. **Expert calls.** The 101 calls are distinct as of 9 November 2026: 23 AlphaSense and Tegus calls from the first build, plus 63 AlphaSense calls and 15 moderated academic interviews added on 9 November. Calls saved from more than one service or compilation were de-duplicated. Even so, several experts appear under different labels, and many later calls are AI-run scripted surveys. Treat individual figures as anecdotes.
2. **Illumina conferences.** Nothing after TD Cowen (3 March 2026) is in hand. Bernstein (May), Goldman Sachs (June) and Morgan Stanley (September 2026) are likely missing, so mid-year management commentary is known only through earnings calls and research.
3. **Illumina research after Q2 2026.** Reactions to the 30 July 2026 results are in hand from JPM, Barclays, Freedom Broker, Ameriprise and Bloomberg Intelligence, but not UBS.
4. **Early history.** Call transcripts begin at Q1 2023 and filings at Q1 2022, so management's view of 2022 comes only from filings and later commentary.
5. **Roche.** Only one recent results call is held (H1 2026); the Q1 2026 sales call is missing. Q3 2026 sales were due around 22–23 October 2026.
6. **Thermo Fisher.** The Q1 2026 call, consensus and research are missing, and Q3 2026 results were due around 22 October 2026. Thermo's 2026 calls never discussed Ion Torrent, so that business's trajectory is undocumented.
7. **10x Genomics.** The Q2 2026 call, consensus and research are missing.
8. **MGI Tech.** No transcripts exist, because MGI is listed in Shanghai and English transcripts generally are not produced. Its picture rests on four UBS notes, which never mention Illumina.
9. **Private competitors.** Element Biosciences and Ultima Genomics appear only through expert calls and others' commentary, so their prices, installed bases and share claims cannot be checked against company disclosures.

Two data-quality cautions apply across the folder:

- **Sources conflict.** Bloomberg's claim that consumables are 60% of sequencing revenue conflicts with the roughly 74% implied by filings, and BI's 20% fall in Q1 service revenue conflicts with every other source. Errors also appear: one Barclays note calls Axelios an Element product.
- **"Adjusted EPS" in the consensus data set** uses a data-provider definition that differs from Illumina's non-GAAP EPS; its 2024 figure was $2.45 against the company's $4.16. Always check which basis a number uses before comparing.
