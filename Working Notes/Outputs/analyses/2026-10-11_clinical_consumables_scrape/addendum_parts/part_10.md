## Alternative data

Alternative data here means sources outside Illumina's own reporting: public price lists, procurement records, government payment data, FDA databases, customer surveys, expert calls and job postings. Each is useful for one question and weak for others, so each subsection says what it shows and how far to trust it. Where the evidence has already been set out earlier, the subsection gives a short pointer instead of repeating it; pointers are not new evidence.

### Price lists, distributor catalogs and tenders

**What they show.** Same-core comparisons put the X's 25B flow cell about 34–60% below the 6000's S4 per Gb, and much of the X's advantage comes from using its largest flow cell [E051, E311, E308]. **How reliable.** Moderate for direction, weak for levels. Core-facility prices include labor, overhead, shipping and sometimes a 5% tariff surcharge; internal rates run 35–50% below external ones; many cards give no Gb per lane; several PDFs were unreadable (TGen, TxGen; Calgary seen only by snippet); and Illumina hides its own list prices behind a login [E170].

**How to read these prices against the 3.4x premium.** The revenue data imply the X is about 70% cheaper per Gb than the 6000, while price cards mostly show 34–60% (the mechanics section explains the likely reasons). The useful number in each item below is therefore the "X is N% cheaper" figure, compared with 70% [E001, E051].

1. **Same-core pairs show a gap of 34–60%, not 70%.** *Fact:* Paired at the same core, the 25B is 34–60% cheaper per Gb than the S4: 60% at Salk, 51% at UConn, 41% at Calgary (by snippet) and 42% on CNAG's standard 2x150 line (€2.84 against €4.90 per Gb; 63% on its 2x100 line). The cross-core median is 53% (about $3.11 against $6.66) (core rate cards, 2024–26). *Our opinion:* That sits below the CFO's "more than 60–70%". [E051, E291, E311]

2. **Only the 6000's small flow cells reach 70%-plus.** *Fact:* Pairs involving the 6000's small S1, S2 and SP flow cells reach 74–87% cheaper on the X, and S1/S2 cost 79–82% more per Gb than the 25B (core rate cards). *Our opinion:* That supports the idea that the remaining 6000 tail leans to small, pricier flow cells. [E051, E311]

3. **The per-Gb saving needs volume.** *Fact:* At Salk a 25B-300 flow cell ($42,560) costs 7% more than an S4-300 ($39,701) for about 2.7 times the data (July 2025 rates). *Our opinion:* So a customer must use far more Gb to keep its spend unchanged. [E052]

4. **Government-channel prices for both platforms.** *Fact:* The distributor Government Scientific Source, on the US government's GSA purchasing schedule, lists the 25B-300 at $24,155 and the S4-300 at $21,683 (undated). *Our calc:* So the 25B costs about 11% more for about 2.7 times the Gb, about 58% cheaper per Gb, which is close to, but still short of, the 70% the revenue data imply. [E234, E235]

5. **The X saves money only for labs that fill a 25B.** *Our calc:* On the same price list the mid-size 10B is only 33–50% cheaper per Gb than the S4, and the small 1.5B costs about the same as the S4 (table below). [E235]

The table sets out the government-channel kit prices behind items 4 and 5, with price per Gb where Gb output is known. The takeaway is that the X's price advantage per Gb depends almost entirely on flow-cell size. [E234, E235]

| Kit (platform) | GSA list price | Price per Gb |
|---|---|---|
| 25B-300 (X) | $24,155 | $2.30–3.02 |
| 25B-100 (X) | $13,650 | n/a |
| 10B-300 (X) | $14,493 | $3.62–4.83 |
| 1.5B-300 (X) | $3,928 | $5.49–7.85 |
| S4-300 (6000) | $21,683 | ~$7.23 |
| S4-200 (6000) | $19,436 | n/a |
| S2-300 (6000) | $15,633 | n/a |

6. **Moving up to the 25B is its own price cut.** *Fact:* Within the X family, moving from the 10B to the 25B cuts price per Gb by 24–37% at every core checked, for example Duke ($3.01 against $4.46 internal, Feb 2026), CNAG (35–38%), Rush (29%), Northwestern (24%) and Toronto's TCAG (33%), with Utah and Missouri showing the same step. *Our opinion:* The 10B itself is only about 35% cheaper than the S4, so a large part of the X's "price cut" is customers moving up to its biggest flow cell. [E308, E313, E051]

7. **No core reaches $2.00 per Gb.** *Fact:* The 25B runs about $2.50–3.30 per Gb at the cheapest cores (Case Western $2.63, Jul 2026; Dana-Farber $2.50–2.88; UConn $2.94; TxGen $3.11, 2024; TGen $3.14, Aug 2026), and the new 5B costs about $3.20 per Gb at Case Western. *Our opinion:* So even the best core prices sit 25–65% above Illumina's $2.00 launch claim, which matters because it suggests the X's price floor has not yet been reached at the cores. [E054, E308, E313]

8. **Illumina's own price claims.** *Mgmt:* At launch (2022) Illumina said the X is "up to 59%" cheaper per Gb than the S4, at $2.00 per Gb list, about $200 per 100 Gb genome in consumables. *Fact:* Its published 25B kits ($11,700 for 100 cycles and $14,500 for 200 cycles, announced 7 Jan 2025) work out to about $3.34–4.50 and $2.07–2.74 per Gb on Illumina's stated output. *Our opinion:* No current price we found reaches $2.00 (see "Where sources disagree"). [E055, E217]

9. **Longer runs are much cheaper per Gb.** *Fact:* The 300-cycle 25B list price was not found, but Case Western resells 25B kits at $15,900 (100-cycle) and $21,000 (300-cycle) (2026). *Our calc:* So tripling the read length raises the price only about a third. [E217]

10. **The same lane costs twice as much at different cores.** *Fact:* One 25B lane ranges from $2,059 (Harvard, internal) and $2,934 (UConn) to $3,512 (UCLA) and $4,200 internal / $4,620 external (Rush, 15 Jun 2026, 930 Gb, about $4.50–5.00 per Gb); Rush still lists a 6000 S4 option at $6,615 (unit unstated). [E259]

11. **Large service providers sit at the bottom of the range.** *Fact:* Novogene's spring 2026 promotion was $2,599 per 1,000 Gb 25B lane (about $2.60 per Gb) and $1,599 per 375 Gb 10B lane (about $4.26). *Our opinion:* So core prices mostly reflect each core's own policy, and large-scale buyers already pay near the low end, which is where clinical volume concentrates. [E259]

12. **The 6000 is being repriced where it survives.** *Fact:* Salk's S4-300 price fell from $52,098 (older, undated list) to $39,701 (24% lower) and its S4-200 from $43,586 to $36,708 (16% lower); Dartmouth's FY27 internal S4 at $3.91 per Gb is an outlier. EPFL's Swiss core (Sep 2026) lists the 6000, logs a "strong decrease in NovaSeq prices" (Sep–Nov 2025) and on 300-cycle runs (Mar 2026), and has no X on its card. [E053, E314]

13. **Other cores have dropped the 6000 or raised X prices.** *Fact:* UCLA's July 2026 card lists only X flow cells ($1,210–3,512 a lane), and Northwestern's FY26 card lists no 6000 at all. *Fact (weak source: search snippet):* Harvard's Bauer Core raised its internal 25B-300 lane price 17.8% (to $2,426) and its 1.5B-300 lane 25.5% from FY26 to FY27, with the 10B nearly flat. [E274, E275, E314]

14. **A clinical test's sequencing cost per sample.** *Fact:* Illumina's TruSight Oncology 500 HT panel runs 192 samples on an S4 or 10B and 480 on a 25B. *Our calc:* On government-channel prices, sequencing therefore costs about $113 a sample on the S4, $75 on the 10B and $50 on the 25B. [E236]

15. **What that does to Illumina and to the lab.** *Our calc:* A lab moving from S4 to 25B cuts Illumina's revenue per sample about 55%, so it needs about 2.2 times the samples to keep Illumina's revenue neutral. Yet the lab saves only about $63 a sample, against $600–1,100 of preparation and data processing, which is why the saving does little for the lab's own economics. [E236]

16. **Toronto's list prices.** *Fact (stale, Apr 2025, Canadian dollars):* TCAG lists 25B lanes at $2,500, $3,085 and $3,470 (100, 200 and 300 cycles) and a 30x genome including library preparation at CAD $650, while the 6000 line says "contact facility". *Our opinion:* The takeaway is that a full clinical-grade genome service already cost under about US$500 in 2025, consistent with the $150–200 consumables-only genome prices cited elsewhere. [E316]

17. **Public tenders and awards.** *Fact:* CIBER (Spain) tendered for 225 X Plus flow cells at €2.88M (about €12,800 each, type unstated; Jul 2025), and IDIBAPS (Barcelona) awarded 13 25B-300 kits at €16,000 each through an Illumina distributor in June 2025, 16.7% below its estimate. *Our calc:* That is about €2.00 per Gb at an assumed 8 Tb, the first actual award prices in the ledger and the only price near Illumina's $2.00 claim, though both buyers are research institutes. [E433, E437]

18. **Grant claims of larger savings.** *Fact (grant claims):* The UAMS genomics core's NIH equipment grant ($750,000, 2024–25) buys an X Plus to replace its 6000 and claims sequencing cost falls "by up to ~80%"; the University of Florida's core claims "up to 60%". *Our opinion:* These are claims written to win grants. [E434]

### Medicare and payer data

**What it shows.** Payers are tightening on generic genetic tests and leaving branded oncology tests largely alone. **How reliable.** High for the rules themselves (CMS fact sheets, statute, inspector-general reports), but the effect on Illumina's Gb is indirect and unquantified, and final 2027 rates are due in November 2026.

*Pointer, not new evidence:* the payer evidence is set out in Question 2, section B (Medicare spending, the 2027 fee schedule, MolDX policies, MCED coverage from 2028 and the children's Medicaid bill) and section E (Signatera's Medicare rate) [E097, E219, E098, E203, E319, E323, E089].

### FDA and regulatory databases

**What it shows.** No FDA-approved sequencing test we checked names the NovaSeq X. **How reliable.** High for what is in the database, but openFDA gives short summaries, not the full safety and effectiveness documents (SSEDs), and it would not show pending supplements or internal change-control plans.

*Pointer, not new evidence:* the FDA record is set out in Question 1, section D [E250, E287, E296, E298, E297, E317].

### Customer surveys

**What they show.** Customers plan slower volume growth and much smaller price declines than Illumina's numbers imply. **How reliable.** Low to moderate: one JPM survey of 62 customers (32 clinical), self-reported, with a typo in its summary page.

1. **Clinical lab spending plans.** *Fact (survey):* Clinical labs in the JPM survey spend about $965K a year on instruments and about $857K on consumables, and plan instrument spending growth of +22.2% (2027) and +31.0% (2028) (JPM, Jun 2026). Only about 5% bought an Illumina instrument in 2025–26 to date. *Our opinion:* Planned instrument spending well above planned volume growth suggests labs are building capacity, possibly including second platforms. [E119]

*Pointer, not new evidence:* the survey's other findings are in Question 1, section C (instrument ownership), Question 2, section D (implied price decline) and "Read-through from competitors" (AXELIOS purchase intent) [E021, E067, E118].

### Expert calls and channel checks

**What they show.** A research-heavy picture of flat-to-falling academic demand, sticky clinical customers and heavy discounting at large accounts. **How reliable.** Moderate. Many experts are former Illumina employees who left in 2024–25, some work for competitors (Roche, an Element partner), and most channel checks are research cores rather than clinical labs.

1. **Q2 2026 channel checks.** *Opinion (customers):* An Arizona core was flat to +5–10% (Element present), a 50-person biotech +25–50%, a South Carolina core about +40% via outsourced X work, a Georgia core flat only because of one contract (underlying demand down, 2025 about −20%), and a Massachusetts genome center flat, with FY26 about −5% on NIH cuts (channel checks, Q2 2026). Illumina list prices were unchanged in 90 days, though one expert said reagent prices go "up every year". *Our opinion:* These are research sites, so they say more about the shrinking research business than about clinical volume. [E168]

2. **A core's complaint about sales tactics.** *Opinion (customer):* The Georgia core director said the core took instruments "on Illumina's schedule to help Illumina meet its local quarterly targets" on promised discounts that were "not honored", and rated support about 6.5 out of 10 amid sales-rep turnover (expert call, 2026). [E122]

### Job postings and hiring

**What they show.** Clinical labs still list Illumina platforms, rivals are building field teams, and Illumina is not visibly cutting. **How reliable.** Weak: about a dozen postings, poor job-board indexing, and the planned automated job-postings scrape was unavailable.

1. **Clinical postings by platform.** *Fact (anecdotal):* Natera postings name the NovaSeq X Plus and NovaSeq, Tempus names both the 6000 and X, Guardant names no platform, and no clinical posting names Ultima, Element or AXELIOS (2026 postings). [E166]

2. **Rivals are hiring field staff.** *Fact (anecdotal):* Roche is hiring AXELIOS service and application roles (Nordics, Mar 2026; US, May 2026), Ultima is building field service (Fremont, Phoenix, Abu Dhabi), and Element is hiring inside sales "introducing VITARI". [E166]

3. **Illumina's own hiring and layoffs.** *Fact:* California WARN notices (legally required layoff notices) total 38 Illumina workers in 2026 (plus 1), against 172 in April 2025 and 75 in July 2023. Illumina still posts commercial, market-access and clinical roles, and there is no evidence of a 2026 layoff (search hits about a "10% R&D" cut date to June 2023). [E167]

### Illumina's web pages

**What they show.** Snapshots, not differences over time; a planned archive comparison of Illumina's pages over time added nothing usable.

*Pointer, not new evidence:* the page reads are in Question 1, section D (no 6000 retirement notice) and Question 2, sections C and D (the X specification page, the roadmap, the order page and the ASHG page) [E214, E300, E359, E435].

## Bull case vs bear case

The bull and bear cases below are summaries (*our opinion*) that draw only on the evidence above; each points to where the detail sits. The adjudication that follows says which is stronger on each question.

### The bear case

1. **A large, concentrated premium.** The 6000 earns about 3.4 times the X per Gb, and clinical holds most of what is left; on our assumed margins it may supply over half of core operating income (Question 1, sections A, B and F). [E001, E187, E367, E368]
2. **The price stack has no slack.** Tail conversion, the 35B and normal repricing already fill management's mid-teens decline before any competitive response (Question 1, section F; Question 2, section A). [E247, E305]
3. **Customers plan much slower volume.** Clinical customers' own plans are high teens, and much test growth is in low-Gb tests such as classic MRD (Question 2, sections B to D). [E067, E432]
4. **Contracts and concentration push cuts through.** Large customers can leave on 90 days' notice, have price-per-Gb ceilings and refund clauses, and Illumina itself warns about "centralized" customers (Read-through from clinical customers). [E107, E212, E232, E256]
5. **Clinical growth is slowing.** Ex-China clinical slowed from 20% to 15%, and two-year stacks imply a weak Q4 2026 (Question 2, section A). [E073, E306]
6. **Dual owners can shift volume without new placements.** Many clinical 6000 owners also own an X and could move work to idle X capacity (Question 1, section C). [E248]
7. **Management avoids the question.** The over-earning and initial-price-hit questions got no numbers, and key metrics were dropped or blurred (Management conduct). [E014, E208, E338]
8. **Consensus looks demanding.** Our base case and an independent check both land well below FY27 consensus (Question 1, section F; the model). [E445]

### The bull case

1. **Volume is beating price now.** Revenue-implied clinical Gb growth is about 35–50%, and clinical consumables grew through the heaviest conversion (Question 2, section A). [E073, E205]
2. **The tail is already in the numbers.** The FY26 guide already assumes the 6000 shrinks in H2 2026, so "no cliff" is partly arithmetic already in guidance and consensus (Question 1, section B). [E245]
3. **No margin damage yet.** Tariff-adjusted consumables margin is flat while the X's share of HT revenue rose from 35% to 59% (Question 1, sections F and G). [E366, E369]
4. **The tail is slow, which spreads the hit.** Regulated tests sit on the 6000, management's own target leaves 15–20% unconverted, and the HiSeq tail lasted more than four years (Question 1, sections C to E). [E287, E342, E377]
5. **Intensity can rise sharply.** Genome-based MRD and deeper NIPT use many times more Gb per test, and labs reinvest savings in depth (Question 2, sections C and E). [E438, E455, E092]
6. **Placements are incremental.** Up to half of clinical X placements add capacity rather than replace 6000s (Question 1, section C). [E024, E397]
7. **No rival has a clinical foothold at the big labs.** None of the nine largest US clinical customers checked runs a rival in production, and switching an approved test takes years (Question 2, section F; mechanics). [E353, E116]
8. **The history is consoling.** In the HiSeq transition, consumables still grew despite a 24% fall in revenue per Gb (Question 1, section E). [E375, E376]

### Adjudication

*Our opinion.* On **Question 1** the bear case wins on the facts (the premium is real and large), and the bull case wins on timing (the tail is slow and partly in guidance). On **Question 2** the bull case wins on trailing data and the bear case on forward data: volume growth in 2025–26 comfortably beat price, while 2027–28 depends on the 35B and on whether customers' volume plans (high teens) or the revenue-implied trend (about 40%) is right. The strongest and most recent evidence is the Q2 2026 share series, the pull-through guide arithmetic, tariff-adjusted margins, customer volume prints and the absence of any 35B kit. The weakest is the 35B cut size (hearsay), the 64% clinical share of HT Gb (derived) and the dual-owner share (a count, not revenue). The experts behind the most bearish quotes left Illumina in 2024–25 or work for competitors.

### Where the Street and the stock stand

**What this means for the thesis.** The stock has more than tripled since mid-2025 on the clinical-growth story, consensus is effectively management's long-term model, and no broker models the 6000 tail or the 35B explicitly. So if our base case is closer to right than consensus, the over-earning unwind is not in the price; if the trailing ~40% Gb growth persists, it largely is. The items below are grouped by what they tell us. Prices are compared with the 9 October 2026 close of $278.17.

**How much is already priced in**

1. **The stock has re-rated sharply.** *Fact:* Illumina traded at about $80 in May 2025, $166 on 1 June 2026, $293.69 on 5 October and $278.17 at the 9 October close (+5.1% that day), and joined the S&P 500 on 21 September 2026. *Our opinion:* At about 3.5 times its May 2025 price, the market already credits the clinical-growth story, so a clinical disappointment would matter more than before. [E171]

2. **The bullish targets are only modestly above the price.** *Opinion (brokers):* Piper ($305, 28 Sep), Leerink ($300), Guggenheim ($305) and RBC ($310) imply 8–11% upside. RBC cites a "clinical sales inflection", with no discussion of price per Gb or the 6000 tail. [E172]

3. **Many targets sit below the price.** *Opinion (brokers):* JPM ($230, 31 Jul) and UBS (Buy at $260, upgraded 9 Sep) imply 17% and 7% downside, Barclays (Underweight, raised to $200 on 7 Oct) 28%, and Citi (Sell, $113, the lowest) 59%. *Our opinion:* Several were set when the stock was far lower and have not caught up, so they say little about the thesis. [E172, E341]

4. **The average target is about 16–20% below the price.** *Fact (aggregators):* The average is $222.19 on MarketBeat (10 Buy, 6 Hold, 2 Sell) and $233.55 on S&P Global (21 analysts, range $113–365); FactSet's $175.72 is stale. [E172]

**What the Street assumes about the tail and pricing**

5. **JPM's upgrade rests on the headwind being "largely gone".** *Opinion (broker):* JPM upgraded to Overweight on 10 June 2026 (targets $120 → $185 → $230; it discloses a 1%+ holding and a banking relationship), saying transition pricing headwinds are "largely gone exiting this year" and customers face "meaningful switching friction". *Opinion (broker):* Barclays counters that price per Gb "warrants watching" and that Illumina's 35x price-to-earnings ratio is the "most expensive in core Tools". *Our opinion:* The two brokers disagree on exactly the Q1 question. [E173]

6. **JPM raised out-year numbers without new tail data.** *Fact:* Between May and 31 July JPM lifted FY27 revenue from $4,799M (+4.9%) to $5,047M (+9.1%) and FY28 EPS from $6.48 to $7.41, citing "improved visibility into consumables-led growth", while holding FY27 gross margin at 68.8%. Its discount rate moved from 9.1% to 8.9% to 9.8% between June and August, so its targets are not like-for-like. [E408, E412]

7. **No broker expects a margin hit from the tail.** *Opinion (brokers):* Against a Q2 2026 core gross margin of 68.2%, Barclays alone has margin falling (68.4%, 67.8% and 67.9% for 2026–28), while JPM has 68.3–69.1% and UBS (stale) 68.4–68.9%. *Our opinion:* A spread of about one point means the Street does not model our profit-at-risk scenario at all. [E175, E409]

8. **One broker's logic runs backwards.** *Opinion (broker):* Freedom's tables imply 67.6–68.5% gross margin while its text expects "meaningful gross margin expansion", treating completion of the X transition as offsetting price erosion. *Our opinion:* That is the reverse of the conversion mechanism described in the mechanics section. [E409]

9. **Consensus has margins and EPS rising steadily.** *Fact:* Bloomberg consensus has gross margin rising from 68.2% (FY25) to 70.8% (FY31), operating margin from 23.1% to 30.7% (FY32) and EPS from $4.84 to $12.30, with no discrete allowance for repricing. *Our opinion:* If our profit estimates are even partly right, those margin paths are vulnerable. [E410]

10. **No broker models the 6000 tail.** *Fact:* No note in the corpus has a 6000 revenue line, a price-per-Gb path or a 35B cut; only JPM, Barclays, UBS and Freedom give model detail, and UBS's FY26 revenue of $4,535M is stale. FY26 EPS estimates are $5.34 (JPM, Barclays) and FY27 $6.16 (JPM) or $5.73 (Barclays), and a Seeking Alpha discounted-cash-flow valuation gives $188 against $218 at publication. *Our opinion:* The over-earning question is simply not in the published models. [E174, E411]

**The near-term set-up**

11. **The Q3 2026 print.** *Fact:* Results are due Thursday 29 October after the close, with consensus revenue of about $1.15B (unverified) and EPS of $1.36 (one source says $1.41); no Illumina management commentary after 30 July was found. *Opinion (broker):* Bloomberg Intelligence says the "60 placements per quarter" goal is "increasingly less meaningful", the Q3 guide is "a touch softer than consensus", and high-single-digit 2027 growth is "increasingly visible". [E176]

12. **Short sellers have not given up.** *Fact:* Short interest (shares sold short by investors betting on a fall) peaked for 2026 at 7.2% of tradable shares (10.59M) on 15 September and was 6.3–6.5% (9.47M, 1.6 days of trading to cover) on 30 September, so shorts did not cover during the run from about $145 to $294. *Fact (unverified):* Options imply roughly a ±14–15% earnings-day move per two aggregators, but the only option-derived figure found is 16.9% for a six-week November expiry. *Our opinion:* A meaningful minority is positioned for the bear case, so the Q3 tail data could move the stock sharply. [E340, E345, E357]

13. **The bar is high.** *Fact:* After Q3 2025 the stock rose about 25% on a 15.5% EPS beat, but after Q2 2026 it closed flat on 31 July ($205.10) and fell 3.4% on 3 August; a reported −10% move is unsupported. *Our opinion:* A beat that left the stock flat shows that EPS beats alone no longer move it, so evidence on the tail and pricing matters more. [E346, E356]

14. **Customer stocks show the clinical story is volatile.** *Opinion (brokers):* JPM raised Natera's target to $315 and Guardant's to $185 (Jul 2026). *Fact:* Guardant (−20%) and Natera (−14%) fell between 3 February and 5 March 2026 on what Barclays called "MCED failure, Dx competition, AI noise, valuation reset". *Our opinion:* Sentiment on Illumina's biggest clinical customers can swing fast, and their volume is what has to offset Illumina's price cuts. [E177]
