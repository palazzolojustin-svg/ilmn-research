# 16 Addendum: Is Illumina Over-Earning on Clinical Consumables?

*As of 2026-10-11. Built from iterative waves of research agents covering every relevant Core Notes source plus outside data (customer filings, price lists, Medicare and payer data, competitor news, insider filings and job postings). How it was built and its limits are at the end. An index of where every ledger tag is cited sits in a companion appendix file in the same folder as the ledger.*

## How to read this addendum

**Labels.** Each numbered evidence item starts with a bold title and an italic label saying what kind of evidence it is:

- *Fact*: a reported number or the text of a document (a filing, a slide, a contract, a price list, a call transcript showing what was asked and said).
- *Mgmt*: something Illumina management said. It may be accurate, but it is a claim, not a verified number. Statements by other companies' executives are marked *Mgmt (customer)* or *Mgmt (competitor)*.
- *Opinion*: a judgement by an analyst, expert, competitor or customer, or by us. Expert calls are with former employees or industry staff and are hearsay. Our own judgements, such as calling an answer a "deflection", are marked *Our opinion*.
- *Our calc*: our own arithmetic on reported inputs. It is opinion, because it rests on stated assumptions.

When an item mixes kinds of evidence, each sentence carries its own label (for example "*Fact:* … *Our calc:* …"), so it is always clear which statement is sourced and which is our inference.

**Severity and relevance (conduct section only).** Each conduct item also carries two ratings, both *our opinion*. **Severity** is how serious the conduct is in itself (none, low, medium, high). **Relevance** is how much it bears on the two thesis questions (low, medium, high).

**Tags.** Every item ends with one or more ledger tags in square brackets, such as [E001, E046]. They point to the master evidence ledger (`Working Notes/Outputs/analyses/2026-10-11_clinical_consumables_scrape/00_evidence_ledger.md`), which gives each item's full source. Where a later research wave corrected an item, this addendum uses the corrected version. Items flagged *weak source* rest on a search snippet or a tool summary rather than a full read of the document.

**Cross-references.** "Question 1, section C" means the lettered section under Question 1 below. Ledger tags always start with "E" followed by three digits; section letters never do.

**Key terms used throughout.** These are explained once here; rarer terms are explained where they first appear.

*Sequencing basics*

- **Gb (gigabase)**: a billion DNA letters read; the unit of sequencing output. A terabase (Tb) is 1,000 Gb and a petabase is 1,000 Tb. A megabase (Mb) is a million letters.
- **NovaSeq 6000 and NovaSeq X**: Illumina's older (2017) and newer (2022–23) high-throughput sequencers. **HT** means high-throughput; **MT** means mid-throughput (smaller benchtop machines such as the NextSeq).
- **Flow cell**: the consumable glass slide on which DNA is read, sold in kits named by output (S1, S2, SP and S4 on the 6000; 1.5B, 5B, 10B, 25B and, from 2027, 35B on the X). On the X, the number in each name is roughly the flow cell's output in billions of reads, so the 25B is the largest on sale today.
- **Installed base**: the number of instruments in use at customers. **Decommission** means retiring an instrument, so it leaves the active installed base.
- **Pull-through**: Illumina's term for annual consumables revenue per installed instrument.
- **Reagent rental**: a deal in which the customer gets the instrument for little or nothing upfront and pays for it through a higher price on consumables.
- **Elasticity**: the idea that cheaper sequencing creates enough new demand (new tests, deeper tests) to make up for the lower price.
- **Core facility (core)**: a university or institute lab that sequences samples for other researchers and publishes a price card.

*Clinical tests*

- **Clinical**: Illumina's label for consumables sold to labs running patient tests. It is management's own, unaudited category.
- **MRD (minimal residual disease) testing**: repeated blood tests that look for traces of a patient's cancer after treatment, to catch a relapse early. **WGS-MRD** (or genome-based MRD) is a version that starts from a whole-genome read of the tumor and tracks many more DNA changes, so it uses far more data. **ctDNA** is circulating tumor DNA, the fragments of cancer DNA in blood that MRD tests look for.
- **NIPT (non-invasive prenatal testing)**: a blood test in pregnancy that screens the fetus's DNA for chromosome problems. It needs very little sequencing per test.
- **CGP (comprehensive genomic profiling)**: a broad test of hundreds of cancer genes, run on tumor tissue or on blood (a **liquid biopsy**), used to choose a treatment.
- **MCED (multi-cancer early detection)**: a blood test that screens healthy people for many cancers at once, such as GRAIL's Galleri.
- **Exome and genome**: an exome test reads only the roughly 2% of DNA that codes for proteins (about 8–11 Gb a test); a whole-genome test reads all of it (about 100–120 Gb at "30x", meaning each letter is read about 30 times).

*Regulation and payers*

- **LDT (laboratory-developed test)**: a test a lab designs and validates itself under **CLIA**, the US federal lab-quality rules. Changing the sequencer means revalidating the test, but no FDA review.
- **FDA-approved test and IVD**: an **IVD** (in-vitro diagnostic) is a test or instrument cleared by a regulator for patient testing. An FDA-approved test has been through the US regulator's review, so any change of sequencer needs FDA sign-off. A **CDx** (companion diagnostic) is an approved test used to choose a specific drug. **CE mark / IVDR** is the European equivalent.
- **RUO (research use only)**: an instrument or kit not cleared for patient testing.
- **Medicare, CMS and Part B**: Medicare is the US federal health plan for over-65s, run by **CMS** (the Centers for Medicare & Medicaid Services). **Part B** is the part that pays for outpatient services, including lab tests. **MolDX** is the Medicare contractor program that decides coverage for molecular tests.
- **NCCN**: the National Comprehensive Cancer Network, whose guidelines largely decide which cancer tests US doctors order and insurers pay for.

*Finance, filings and governance*

- **Ex-China**: excluding Greater China, where Illumina's sales collapsed after 2025 trade sanctions.
- **10-K, 10-Q, 8-K, S-1**: a US company's audited annual report, quarterly report, current-event filing and pre-listing registration statement, filed with the SEC (the US securities regulator). Contracts filed with them are called **exhibits**.
- **Form 4, Form 144, 13D and 13G**: SEC filings for insider trades, advance notice of insider sales, and holdings above 5% by active (13D) or passive (13G) investors. A **10b5-1 plan** is a pre-set trading plan that lets insiders sell on a schedule fixed in advance, which protects them from insider-trading claims.
- **EPS**: earnings per share. **Non-GAAP** (also called **"core"** by Illumina) means profit measures that exclude items such as amortization and one-off charges, as opposed to the audited GAAP figures.
- **Gross margin**: revenue minus the direct cost of making the product, as a percentage of revenue. **Operating income** also subtracts sales, research and administrative costs (opex; **SG&A** is selling, general and administrative cost).
- **bp (basis points)**: hundredths of a percentage point. 100bp equals 1 point.
- **Consensus**: the average forecast of the brokers who cover the stock (here mostly from Bloomberg).
- **EY**: Ernst & Young, Illumina's auditor.

**Our three models.** Three pieces of our own arithmetic recur. None is a forecast with a track record, and all are labelled *Our calc*:

- **The scenario model** projects clinical consumables revenue for 2026–2028 from assumed Gb growth, conversion pace and price cuts. It is set out in "The model: scenarios for 2026–2028".
- **The bottom-up test model** builds clinical Gb growth from test volumes by category (MRD, cancer profiling, rare disease and so on) times assumed Gb per test (Question 2, section A).
- **The revenue-at-risk bridge** phases the 6000 tail's conversion year by year and prices it, allowing converting customers to buy some extra volume (Question 1, section F).

## The answer in brief

### Question 1: Is Illumina over-earning on clinical consumables?

**Yes, moderately, but it is a slow leak rather than a cliff.** About $0.5B a year of clinical revenue depends on labs paying old-platform prices, and our base case has about $150–190M a year of it disappearing in 2027–28, part of which is already in guidance.

**What "over-earning" means here** (*our definition*). Clinical revenue is "over-earned" to the extent it exists only because some labs still pay NovaSeq 6000 prices per Gb for work the NovaSeq X could do far more cheaply. The yardstick is the X's own revenue per Gb today. That gives two different measures, which this addendum keeps apart:

- **The stock**: how much clinical revenue would vanish if every clinical 6000 Gb were priced like an X Gb today. We put it at about $0.5B a year.
- **The flow**: how much of that stock is actually lost in a given year as labs convert. We put it at about $150–190M a year in 2027–28, about 7–9% of our FY26 clinical consumables estimate.

**The key caveat.** The 6000's price premium (about 3.4 times the X per Gb) is measured across all high-throughput customers, research and clinical together. Illumina does not report clinical revenue by platform, so applying the same premium to clinical labs is our assumption, and every clinical dollar figure inherits it.

The supporting evidence, in short (full detail in Question 1, sections A to G, and the sizing section):

1. **The premium, measured across all HT customers.** *Fact:* In Q2 2026 the 6000 carried 17% of HT Gb shipped but earned 41% of HT consumables revenue (Q2 2026 deck). *Our calc:* So each 6000 Gb earned about 3.4 times what an X Gb did, a ratio that covers research and clinical together. [E001, E447]
2. **Clinical holds most of the tail.** *Fact:* Clinical labs still have 22% of their HT volume on the 6000, against 8% for research labs (Q2 2026 deck). *Our calc:* That puts about 80% of the Gb still on the 6000 in clinical. [E186, E009]
3. **The clinical 6000 business.** *Our calc:* Assuming clinical labs pay the same 3.4x gap, the clinical 6000 business is about $182M a quarter, or about $0.73B a year. That is about 36% of Q2 2026 clinical sequencing consumables (about $504M that quarter), or about 34% of our full-year FY26 clinical estimate of $2.17B. [E187, E076]
4. **The stock.** *Our calc:* Pricing those clinical Gb like X Gb would remove about $500M a year ($728M × (1 − 1 ÷ 3.39)), about 23% of FY26 clinical consumables or 16% of all sequencing consumables. [E187, E447]
5. **The flow.** *Our calc:* In the base case conversion removes about $190M of revenue in 2027 and a further $145M in 2028, and the bear case reaches about $240M in 2027. Smaller and larger flow figures elsewhere differ only in what they assume, and are reconciled in one table in "Sizing". [E187, E342, E246]
6. **Part of the flow is already in guidance.** *Our calc:* Illumina's own FY26 pull-through guide implies 6000 revenue falls about $40M a quarter in the second half of 2026, so the numbers the Street uses already assume part of the unwind. [E245]
7. **Why the tail is slow.** *Fact:* No FDA-approved sequencing test we checked has moved to the X (openFDA, through Sep 2026), and Illumina placed more than 10 new 6000s in Q2 2026. *Mgmt:* Management aims for only 80–85% of clinical volume on the X by end-2026 (Q2 2026 call). [E287, E015, E342]
8. **The last transition left a long tail.** *Fact:* About 1,000 of the older HiSeq sequencers were still running at end-2020, four years after the 6000 launched (Illumina calls). [E377]
9. **The profit at stake is an assumption.** *Our calc:* If 6000 consumables earn the 80–85% gross margin we assume (Illumina does not disclose platform margins), the 6000 supplies about 22–24% of gross profit and roughly two-thirds of core operating income, and full conversion would cost about $1.75–2.63 of annual EPS against a run-rate of about $5.24. *Our calc:* Tariff-adjusted consumables margin shows no erosion so far, so we hold these profit figures with low confidence. [E367, E368, E366]

### Question 2: Will clinical volume growth offset the lower price per Gb on the X?

**So far, yes, comfortably. For 2027–28, only barely in our base case, and not at all if the next flow cell (the 35B) brings a broad price cut. We lean below consensus.**

In 2025 and the first half of 2026 clinical Gb grew about 40% a year while clinical price per Gb fell about 20–28%, so clinical revenue still grew in the mid-teens. From 2027 three price layers stack up: the rest of the 6000 conversion, the 35B, and normal repricing. In our base case (clinical Gb +30%), that leaves clinical HT revenue up only about 2.5% in 2027 (about +4% for all clinical consumables), against the 13–14% clinical growth that consensus implies.

The supporting evidence, in short (full detail in Question 2, sections A to H, and the model section):

1. **The trailing record.** *Fact:* Clinical consumables outside China grew 12% in 2025 and about 17% in the first half of 2026, while the 6000-to-X price cut flowed through (Illumina decks). [E073]
2. **Implied volume versus management's claim.** *Our calc:* Backing volume out of revenue implies clinical Gb grew about 35–50% a year over 2025 to mid-2026, centrally about 42%. *Mgmt:* Management says clinical volume is growing "over 30%" (JPM conference, Jan 2026). [E205, E266]
3. **The 35B.** *Fact:* Illumina's roadmap puts the 35B flow cell in the first half of 2027, with no price (roadmap page, read Oct 2026). *Opinion (expert, hearsay):* One former Illumina employee expects it to cut price per Gb about 20%. [E214, E058]
4. **Three price layers fill management's model.** *Our calc:* The remaining 6000 conversion, the 35B and normal repricing on the X together already use up management's "mid-teens" annual price decline, leaving no room for a price response to competitors. [E247]
5. **The hurdle.** *Our calc:* To hold 2027 clinical HT revenue flat, clinical Gb must grow about 15% for conversion alone, about 27% in our base case, or about 47% if a full 35B cut lands on top of management's mid-teens decline. Our base case assumes +30%, only about 3 points above its own hurdle. [E267, E305, E084]
6. **Our scenarios versus consensus.** *Our calc:* Clinical sequencing consumables grow about +4% in 2027 and +6% in 2028 in our base case (bear −10% and −3%; bull +19% and +17%). *Fact:* Bloomberg consensus has all sequencing consumables up 8.8% in 2027 and 9.4% in 2028, which implies clinical growth of about 13–14%, nearer our bull case. [E205, E247, E067, E080]
7. **Why our confidence is only low to moderate.** *Our calc:* A back-test of a similar model predicted +1% sequential HT growth for Q2 2026, against an actual +6.8%, so our models may lean bearish. [E446]
8. **Test counts overstate Gb growth.** *Fact:* Natera's MRD tests grew 56%, Guardant's oncology tests 63% and GeneDx's exomes and genomes 32% in Q2 2026 (company releases and 10-Qs). *Our calc:* But a classic MRD blood test uses well under 1 Gb, against more than 100 Gb for a genome. [E081, E432]
9. **Customers spend savings on depth.** *Our calc:* Natera's cost per test rose about 9% and Caris's cost per case about 5–6% year on year in Q2 2026 (from their 10-Qs). *Mgmt (customer):* Caris's CEO summed it up as "always deeper, not cheaper" (Caris Q2 2026 call). [E089, E294, E092]
10. **Customers hold price protection.** *Fact:* Natera's and Caris's supply contracts contain clauses under which their price per Gb can only fall (SEC exhibits), and Illumina's FY25 10-K newly warns of pricing pressure from "a small number of large, centralized laboratory customers". [E212, E232, E107]

### Management conduct and credibility

**We found no accounting misconduct. In our judgement, though, Illumina tends to disclose transition data when it flatters and to blur or withdraw it when it does not, and the two analyst questions closest to this thesis got no numbers in reply.** The full list, with severity and relevance ratings, is in "Management conduct and credibility" below.

1. **Clean audit.** *Fact:* The auditor's opinion is clean, there are no restatements, and the SEC's comment letters never challenged Illumina's metrics (10-K and SEC correspondence). [E373, E381]
2. **The volume share measures Gb shipped.** *Fact:* The X's share of volume is measured on Gb shipped, not Gb sequenced, and is never reconciled with the separate ">30%" growth metric (decks and calls). [E204]
3. **The growth metric changed scope.** *Fact:* The ">30%" Gb growth metric widened from high-throughput to high- and mid-throughput instruments in Q3 2025, and is reported only as a floor (Q2 and Q3 2025 calls). [E207]
4. **Two disclosures stopped.** *Fact:* The clinical-versus-research activity split last appeared in Q2 2023, and the FY26 pull-through guide has not been repeated since February 2026 (calls and decks). [E208, E276]
5. **A claim without a number.** *Fact:* Q2 2026 prepared remarks said pull-through "increased year-over-year", the first time the claim came with no figure (Q2 2026 call). [E277]
6. **A mislabelled "91%".** *Fact:* The CFO said 91% of HT volume had moved to the X, but her own prepared remarks put 91% on research only, and the total was 78% (Q3 2025 call). *Our opinion:* The wrong denominator made the fading headwind sound stronger than the clinical data supported. [E392]
7. **The price cut faded from filings.** *Fact:* Only the Q1 2025 10-Q blamed lower margins on "reduced pricing"; later 10-Qs and the 10-K cite tariffs, mix and other causes. *Our opinion:* The price effect has become less visible in the filings than in the share data. [E036]
8. **The over-earning question.** *Fact:* Asked directly about over-earning on the 6000, the CEO gave no 6000 revenue, decommission pace or customer count (Q2 2026 call). *Our opinion:* That was a deflection of the question closest to this thesis. [E014]
9. **The initial-price-hit question.** *Fact:* Asked about the price hit at labs newly converting, the CFO said it was "built into the guide" and gave no number (Q1 2026 call). *Our opinion:* Also a deflection. [E209, E338]
10. **Guidance is set low and beaten on EPS.** *Fact:* FY25 and FY26 EPS guidance started low and was beaten or raised each time (guidance history). [E141, E143]
11. **A director's share sales and a customer stake.** *Fact:* Director Keith Meister's fund sold about $591M of Illumina stock from May to September 2026 while buying into GeneDx, a large Illumina customer (Form 4 and 13D/A filings). *Our opinion:* This is a governance issue, not a consumables signal. [E150, E151, E196]
12. **Executives did not sell.** *Fact:* The CEO and CFO bought shares in May 2025 and have sold only to cover tax on vesting since (Form 4 filings). [E152]

### What would change the view

**The Q3 2026 print on 29 October is the first test; the 35B's price and scope in the first half of 2027 is the decisive one.**

1. **Bull signals in Q3.** *Our calc:* Derived 6000 revenue below about $210M (against $219M in Q2), an X share of HT revenue of 61% or more (59% in Q2), and ex-China clinical growth of 13–16%. [E270, E450]
2. **Bear signals in Q3.** *Our calc:* 6000 revenue at or above $219M, an X revenue share stuck near 59%, or clinical growth below 12%. [E270]
3. **A silently dropped guide.** *Our opinion:* If the FY26 pull-through guide disappears without comment, that would be a bear signal in itself. [E276]
4. **The biggest swing factor.** *Our calc:* The 35B's price and how much of the X base it reaches are worth roughly $60–250M of annual revenue, depending on adoption. [E247]
5. **A regulatory tripwire.** *Fact:* No FDA-approved test has been approved on the X so far (through Sep 2026); the first one would open the regulated tail to conversion. [E287]
6. **The open Guardant question.** *Fact:* Whether Guardant's newly approved blood test (May 2026) names the X or the 6000 is the one unresolved item in the FDA record. [E297]
7. **A competitive tripwire.** *Fact:* None of the nine largest US clinical customers we checked has a Roche, Ultima or Element sequencer in production (as of Oct 2026); the first that does would be the first real switch. [E353]

## How the NovaSeq 6000-to-X conversion hits revenue: the mechanics

This section explains, from the basics, why moving customers from one sequencer to another can cut revenue even while the customers do more work. It starts with a short primer, then lists the evidence item by item.

**The business model, as a primer.** Illumina sells DNA sequencers (instruments) and then sells the chemistry those instruments use (consumables): the instrument is the razor and the consumables are the blades. The key consumable is the flow cell, sold as a kit with reagents, and each flow cell produces a known number of Gb. A newer sequencer that reads more DNA per flow cell, for not much more money per flow cell, lowers the price of each Gb. If customers do not buy proportionately more Gb, Illumina's revenue falls.

**The general rule.** Revenue growth is roughly (1 + volume growth) × (1 − price decline) − 1. With volume up 30% and price down 15%, revenue grows about 10.5%; with volume up 30% and price down 25%, revenue falls about 2.5%. During a platform transition the price decline has two parts. The first is mix (Gb moving from the expensive platform to the cheap one), which stops once the old platform is gone; the second is repricing within each platform (a new, cheaper flow cell or a discount on renewal), which does not stop.

### The evidence, item by item

1. **Consumables are the business.** *Fact:* Consumables were about 74% of Illumina's revenue in FY25, and sequencing consumables were $2,939M (FY25 10-K). [E374, E050]
2. **High-throughput is most of it.** *Our calc:* HT consumables are roughly 69% of sequencing consumables, a figure we derive and test at 65–72% (Question 1, section B). [E003]
3. **An X earns about twice what a 6000 does per machine.** *Fact:* Pull-through was about $670K a year for a 6000 and about $1.35M for an X in FY25 (Q4 2025 deck). [E017, E038]
4. **Why the X cuts the price per Gb.** *Fact:* The X's largest flow cell, the 25B, produces about 8–10.5 Tb per run, against about 3 Tb for the 6000's largest, the S4. On one US government-channel price list a 25B kit costs only about 11% more than an S4 kit for about 2.7 times the data. [E234]
5. **Management's description of the cut.** *Mgmt:* The CFO called the drop "easily more than 60% to 70% on a Gb-to-Gb basis" (Q2 2024 call). [E030]
6. **The premium in Illumina's own numbers.** *Our calc:* In Q2 2026 the X had 83% of HT Gb and 59% of HT revenue, so revenue per Gb was 59 ÷ 83 = 0.71 on the X and 41 ÷ 17 = 2.41 on the 6000, a ratio of about 3.4x. Because Illumina rounds the shares to whole percentages, the ratio is known only within about 3.2–3.6x. [E001, E447]
7. **The upper bound for all HT.** *Our calc:* Moving all remaining 6000 volume to the X at the X's price, with no extra volume, cuts HT consumables revenue 29% (about $617M a year, about 20% of sequencing consumables). Getting back to flat needs 41% more total HT Gb, or about 3.4 times the converting customers' old volume (+240%) if only they add volume. [E004]
8. **The upper bound for clinical.** *Fact:* Clinical labs still have 22% of their HT Gb on the 6000 (Q2 2026 deck). *Our calc:* At the same 3.4x ratio those Gb earn about 49% of clinical HT revenue, so full conversion would cut clinical HT revenue about 35% and need about 53% more clinical Gb to offset. [E186, E187]
9. **Caveat: shipped, not used.** *Fact:* The share data measure Gb shipped (flow-cell capacity sold), not Gb actually sequenced (Illumina decks). *Our opinion:* If 6000 customers buy flow cells they do not fully use, the true premium per Gb used could be larger or smaller. [E204]
10. **Caveat: clinical revenue by platform is not reported.** *Fact:* Illumina reports the clinical X share only for volume, not revenue. *Our opinion:* Every clinical revenue figure in this addendum therefore assumes the same 6000-versus-X price gap in clinical as in research, which no source confirms. [E187]
11. **List prices show a smaller gap than revenue does.** *Fact:* Same-core price cards put the X about 35–60% cheaper per Gb than the 6000, not the roughly 70% the revenue data imply (core rate cards, 2024–26; details in "Alternative data"). [E051, E311]
12. **Reason one for the difference: under-filled flow cells.** *Mgmt:* Illumina's former CFO said customers "never batch samples at the rate needed to fill a flow cell… pay a slightly higher effective price that we recover" (2023). [E032]
13. **Reason two: list-price rises.** *Fact:* Illumina raised list prices in 2024 and again for tariffs in 2025, while the 6000 base shrank (calls and core price notices). [E033]
14. **Reason three: the X's biggest flow cell.** *Fact:* Moving from the X's 10B to its 25B flow cell cuts price per Gb by a further 24–37% at every core checked. *Our opinion:* Together with a 6000 tail that probably leans to smaller, pricier flow cells, these effects plausibly explain the gap, but the disclosed data cannot separate them. [E308]
15. **Why conversion is not instant: lab-developed tests.** *Opinion (former employees, hearsay):* Moving a validated lab-developed test to a new sequencer means months of side-by-side runs costing about $100–200K per test, and tests in long clinical trials essentially cannot move (expert calls). [E116]
16. **Why conversion is not instant: FDA-approved tests.** *Fact:* For an FDA-approved test the lab needs FDA approval of a supplement or new application, which has taken about 11–17 months per change in the cases we found (openFDA). [E298]
17. **Management's framing.** *Mgmt:* Management calls the transition "a wave", not "a cliff" (Q2 2026 call). *Our opinion:* The evidence above fits a pattern in which labs put new and growing tests on the X and leave old tests on the 6000 until they retire. [E016]
18. **What can offset the price cut.** *Mgmt:* Illumina's long-term model assumes Gb grows in the mid-20s percent a year while price falls in the mid-teens, netting high-single-digit revenue growth (Strategy Day, Aug 2024; JPM conference, Jan 2026). *Fact:* The levers are more tests, more Gb per test (a genome uses about 100–120 Gb against about 8–11 Gb for an exome), and new applications made affordable by the lower price. [E047, E082, E435]

The question for the rest of this addendum is whether clinical customers can deliver that much volume once the 6000 tail and the 35B are both in play.

## Question 1: Is clinical consumables revenue over-earning?

The evidence below is grouped into seven themes: the size of the 6000's price premium, how much 6000 revenue is left, how fast the clinical tail is converting, why the regulated part of it is sticky, the HiSeq precedent, what conversion does to revenue and profit, and whether any of this shows in gross margin. A sizing section closes the question and reconciles the different dollar figures in one place.

### A. The size of the 6000's price premium

1. **The core fact.** *Fact:* In Q2 2026 the NovaSeq X carried 83% of HT Gb shipped but only 59% of HT consumables revenue (Q2 2026 deck). *Our calc:* So the 6000 earned about 3.4 times the X's revenue per Gb, which makes the X about 70% cheaper, with a rounding band of about 3.2–3.6x. The arithmetic is set out in the mechanics section. [E001, E447]

2. **Volume moved first, revenue followed.** *Fact:* The X's share of HT Gb rose from about 45% in Q2 2024 to 83% in Q2 2026, while its share of HT revenue rose from about 27% to 59% (quarterly decks; table below). That lag is what a cheaper platform taking share looks like. [E046, E186]

3. **The premium widened as the tail shrank.** *Our calc:* The 6000's revenue per Gb relative to the X's rose from about 2.2x in 2024 to about 3.4x since Q3 2025. The X's own revenue per Gb stayed in a stable band, so the gap widened because the 6000 volume that remains is the high-priced tail, not because the X was repriced. [E002]

The table sets out the quarterly series behind items 2 and 3. The takeaway is that the X's revenue share has run about 25 points behind its volume share throughout, and the per-Gb premium jumped in Q3 2025 and has since held in a 3.3–3.7x band, with quarter-to-quarter moves inside the rounding error. [E046, E186, E002]

| Quarter | X share of HT Gb shipped | X share of HT revenue | 6000 revenue per Gb ÷ X revenue per Gb |
|---|---|---|---|
| Q2 2024 | ~45% | ~27% | ~2.2x |
| Q3 2024 | 55% | 36% | ~2.2x |
| Q4 2024 | 66% | 40% | ~2.8–2.9x |
| Q1 2025 | 68% | 43% | ~2.8x |
| Q2 2025 | 69% | 44% | ~2.8x |
| Q3 2025 | 78% | 51% | ~3.4x |
| Q4 2025 | 80% | 55% | ~3.3x |
| Q1 2026 | 82% | 55% | ~3.7x |
| Q2 2026 | 83% | 59% | ~3.4x |

4. **A broker's reading of the Q1 stall.** *Opinion (broker):* Barclays read the Q1 2026 stall in the X's revenue share (55%, flat while volume rose) as "lower price/Gb on NSX volumes" (Barclays, Apr 2026; its "76%" was the clinical figure, not the total). *Mgmt:* Management called that reading "a frivolous exercise". [E066]

5. **Neither the stall nor the Q2 rebound is measurable.** *Our calc:* The Q2 rebound in the X-to-6000 price ratio, from about 0.27 to 0.30, sits inside overlapping rounding bands. So neither the Q1 stall nor the Q2 "improvement" is statistically established. [E447]

6. **Management's 2024 description ran ahead of the data.** *Mgmt:* In August 2024 the CFO described the move as "overall, all-inclusive, easily more than 60% to 70% price decline on a Gb-to-Gb basis" (Q2 2024 call, verified verbatim). *Our calc:* Illumina's own share data showed a gap of only about 54–55% at the time, reaching 65–71% only from Q3 2025. *Our opinion:* So the remark overstated the then-current gap but now matches the data. [E030, E046]

7. **A garbled management sizing, now superseded.** *Mgmt:* CEO Jacob Thaysen told Bernstein the X cut price "by two-thirds" and that volume must rise "100%" to make up the revenue (Bernstein, May 2025). *Our calc:* A two-thirds cut actually needs volume to triple (+200%), and the Q2 2026 share data (needing +240% on converting Gb) supersede the remark. [E029, E004]

8. **List-price moves add to the premium but cannot be measured.** *Fact:* One Barcelona core raised its 6000 prices about 4% in 2026 while leaving every X price flat, and Illumina's 2025 tariff price rise was worth about 1 point of growth. *Our opinion:* None of this can be separated in Illumina's disclosures, so the over-earning case rests on the revenue-implied ratio, not on disclosed price data. [E312, E045]

9. **Mix explains most of the per-Gb decline.** *Our calc:* In H1 2026 the shift of volume to the X (from 69% to 83%) explains about 16 points of the fall in blended revenue per Gb, leaving about 4–7 points of genuine repricing. *Our opinion:* So the headwind should shrink once mix stops, but the 35B lands on top. [E008]

10. **Backing out volume from price.** *Our calc:* Holding the Q2 2025 and Q2 2026 shares fixed, total Gb growth of only +20% would require the 6000's price per Gb to have risen 16%, which is implausible because 6000 list prices fell 16–24% on core-facility lists. The answer that fits is total Gb growth of about +33–45%, with the X's price relative to the 6000's down at least 8% year on year in every rounding case. [E265]

### B. How much 6000 revenue is left, and who holds it

1. **About $219M a quarter across all HT.** *Our calc:* Assuming HT is 69% of sequencing consumables (tested at 65–72%), the 6000 earned about $219M in Q2 2026, about $0.88B annualized (range $0.83–0.92B). A cross-check on the FY25 base (about 1,360 units times about $670K pull-through) gives about $0.9B. [E003]

2. **The X has mostly replaced 6000 dollars.** *Our calc:* Derived X revenue rose from $136M to $316M a quarter between Q2 2024 and Q2 2026, while 6000 revenue fell from $367M to $219M and total HT stayed in a $480–535M band. The 6000's year-on-year fall slowed to $7M in Q2 2026 from $67M a year earlier, consistent with a sticky tail. [E040]

3. **The disclosed pull-through figures add up.** *Our calc:* Multiplying average installed bases by disclosed pull-through across six platforms gives about $2.98B for FY25, within about 1.5% of the reported $2,939M, which supports the 69% HT share. On average bases the 6000 earned about half of FY25 HT dollars. [E041, E210, E395]

4. **Most of the remaining 6000 volume is clinical.** *Our calc:* Solving the three disclosed volume shares (83% total, 78% clinical and 92% research on the X) puts clinical at about 64% of HT Gb (range 55–71%). So about 80–83% of the Gb still on the 6000 is clinical. [E009]

5. **The clinical 6000 business: about $0.73B a year.** *Our calc:* Assuming the same price gap in clinical as in research, clinical 6000 revenue is about $182M a quarter (range $172–191M). That is about 36% of Q2 2026 clinical sequencing consumables (about $504M, using management's ">65%" clinical share of the $775M quarter), or about 34% of our full-year FY26 clinical estimate ($2.17B, which assumes a 70% share). [E187, E076]

6. **The clinical tail is bigger in dollars than in Gb.** *Our calc:* The clinical 6000 business earns about 49% of clinical HT revenue from only 22% of clinical HT Gb. So the X's share of clinical HT revenue is only about 51%, against about 77% in research. [E187]

7. **A broker's comment confirms the method.** *Our calc:* The same method gives a clinical X revenue share of about 34% at Q3 2025, when the X had about half of total HT revenue. *Opinion (broker):* That matches Wolfe's statement that clinical X revenue was then "less than 50%" (Wolfe, Nov 2025). [E104]

8. **6000 pull-through has held up.** *Mgmt:* Guided 6000 pull-through fell from about $1M (2022) to $600–650K (FY26 guide), with about $670K actual in FY25. *Our calc:* Yet implied quarterly pull-through stayed at about $670–700K from Q3 2025 to Q2 2026 (table below). *Opinion (broker):* Guggenheim said pull-through was "holding up better than expected" (Q4 2025). [E017, E394]

The table shows the quarterly figures behind item 8. The takeaway is that the 6000's revenue is falling because units are being switched off, not because each remaining unit is buying less. Either per-unit use is not yet falling, or more 6000s are active than we assume. [E017, E394]

| Quarter | Derived 6000 revenue | Implied 6000 pull-through (annualized) |
|---|---|---|
| Q3 2025 | $252M | ~$685K |
| Q4 2025 | $234M | ~$669K |
| Q1 2026 | $225M | ~$679K |
| Q2 2026 | $219M | ~$698K |

9. **The denominator was redefined in 2024.** *Fact:* From February 2024, 6000 pull-through is calculated on a "net" installed base that removes inactive units, which lifts the metric. *Mgmt:* The CFO said pull-through is "simply quarterly consumables divided by the active base" and "does not change reported revenue" (Q4 2023 call). [E018]

10. **The installed base has shrunk fast.** *Fact:* The 6000 base fell from about 1,770 net units at end-2023 to about 1,700 by Q3 2024 and about 1,360 at end-FY25, with about 330 decommissions against about 30 new shipments in FY25 alone (Q4 2025 deck). [E019]

11. **Decommissions ran far ahead of the first guide.** *Fact:* In Q1 2023 Illumina guided "only 10–12 decommissions" among early X buyers, but about 110 units were deactivated by end-2023 (2023 calls and decks). That is about ten times the guide, an early sign that management under-called the pace of switching. [E019]

12. **Disclosure stopped where the tail begins.** *Fact:* Since Q4 2025 Illumina has not given the 6000 installed base, a decommission guide, a count of customers running both platforms, or any 6000 revenue or Gb. The pull-through table, defined only in a deck footnote as a "FY25 average annualized figure per instrument", last appeared in the Q4 2025 and January 2026 JPM-conference decks, and the Q2 2026 X base (about 1,065 by our calculation) is also undisclosed. [E020, E276]

13. **Guidance already assumes the 6000 falls.** *Our calc:* The FY26 6000 pull-through guide ($600–650K on an average base of about 1,200–1,300) implies full-year 6000 revenue of about $0.72–0.83B. With H1 at about $444M, H2 must run at $138–200M a quarter, against $219M in Q2. So guidance and Q3/Q4 consensus ($789M and $815M of sequencing consumables) fit together only if the 6000 loses about $40M a quarter within six months, which Q3 will test. [E245]

14. **The X pull-through guide looks stretched.** *Our calc:* Implied X pull-through dipped from about $1.34–1.37M a year (Q4 2024 and Q4 2025) to $1.19–1.24M (Q1–Q2 2026), about 10% lower, because new units take 6–9 months to ramp. Hitting the FY26 guide of $1.35–1.40M needs H2 pull-through of about $1.46–1.55M annualized, about 20–25% above the H1 run-rate. *Our opinion:* Either the guide is cut or 6000 volume moves onto installed X units much faster than trend. [E038, E268]

15. **The only time filings sized the 6000 loss.** *Fact:* Illumina's 2023 filings said lower 6000 consumables pull-through cut sequencing consumables revenue by $127M in FY23, about 4–5% of that year's sequencing consumables ($92M in Q1, $5M in Q2, $30M in Q3). The FY25 10-K and 2026 10-Qs no longer name the 6000 in the revenue discussion, so no comparable figure exists for the much larger tail of 2025–26. [E188]

16. **Reagent rental is invisible.** *Mgmt:* Some X placements are on reagent rental: about 5 of 100+ placements in Q4 2025 and some of about 83 in Q1 2026 (Q4 2025 and Q1 2026 calls). *Fact:* Illumina's filings contain no reagent-rental figures (a $94.7M figure found in one search came from another company). *Our opinion:* So rental could inflate X pull-through by an unknown amount. [E039]

17. **Shorter shelf life on the X.** *Mgmt:* X consumables are committed at 3–4 months of shelf life, against a 6-month minimum for the 6000 (Evercore conference, Dec 2024). *Our opinion:* That makes X revenue more sensitive to customers running down stock at year-end. [E042]

### C. How fast the clinical tail is converting

1. **The clinical X volume share.** *Fact:* Clinical customers' X share of HT Gb went from 35% (Q2 2024) to 53% (Q2 2025) and 78% (Q2 2026), against 92% for research (decks, labels read from slides). The curve is flattening: the last two quarters added 7 points, and the last one only 2. [E010, E186]

2. **The end-2026 target has drifted down.** *Mgmt:* Management went from "substantially complete by end of 2026" (Q4 2025 call) to "over 80% to 85%" and "more than 85%" (Q1 2026 call), then "80% to 85%" (Q2 2026 call). *Our calc:* From 78%, that needs only 2–7 more points in two quarters, so a 15–20% clinical tail is built into the target itself. [E011, E342]

3. **Management has said the tail is sticky.** *Mgmt:* Thaysen said about 20% of Gb will "stay and shrink over time; the last portion takes much longer than the first 75–80%" (Q4 2024 call). CFO Ankur Dhingra said some customers will never move existing tests (Wolfe, Nov 2024), and Thaysen later said some will stay "until the end of life… for the assay… maybe 2 years more" because moving "doesn't make sense" financially (Q2 2025 call). [E012, E013, E393]

4. **The framing has shifted each quarter.** *Mgmt:* The tail was "no cliff" in Q2 2025, "laggards" with FDA or regulated tests and a "long tail" after end-2026 in Q1 2026, and "a standard part of the business" in Q2 2026. *Fact:* The phrase "not a cliff, a wave" (Q2 2026 call) answered a question about clinical demand, not about the 6000 run-off. [E016]

5. **What was asked about over-earning.** *Fact:* On the Q2 2026 call Tycho Peterson (Jefferies) asked whether Illumina is over-earning on the 6000. [E014]

6. **What was answered.** *Mgmt:* Thaysen replied that some customers bought "a few 6000 this quarter", that this was not "a standard part of the business", that HiSeq was "in the portfolio until a few quarters ago", and that there was no "true headwind". *Fact:* He gave no 6000 revenue, decommission pace or count of labs running both platforms, and there was no follow-up. *Our opinion:* The question closest to this thesis therefore went unanswered in numbers. [E014]

7. **Illumina is still selling 6000s.** *Fact:* The CFO said Illumina "placed over 10 NovaSeq 6000 units" in Q2 2026, against about 30 shipped in all of FY25. *Mgmt:* He said this was because "some [customers] plan to remain on that platform for years to come" (Q2 2026 call). [E015]

8. **Earlier guidance on who was left.** *Mgmt:* Dhingra said about 50% of clinical volume and about 80% of research volume was on the X at end-2024, so 2025's remaining conversion had to come from clinical (Feb 2025). The former CFO had said the 6000's decline would be "more muted than HiSeq" because about half its consumables were clinical, noting some tests were still on the HiSeq six years after the 6000 launched (2024). [E181]

9. **Faster than the "one test at a time" framing.** *Mgmt:* Thaysen said in Q3 2024, "I've heard this clinical cliff a few times, and I don't think that's the way we look at the business", describing an "assay by assay… 12–18 months" move. *Fact:* Clinical X share then rose from 43% to 78% in seven quarters. [E180]

10. **2024 transition targets were mostly met, a little late on revenue.** *Mgmt:* In August 2024 Illumina said the X would be about half of HT revenue by mid-2025 and about 75% of volume by H2 2025. *Fact:* Revenue share reached 44% in Q2 2025 and 51% in Q3 2025 (one to two quarters late), and volume share reached 78% in Q3 2025 (met). Illumina had guided about 5 points of revenue shift a quarter, but Q3 2024 alone jumped 10. [E179]

11. **Layering rather than replacing.** *Mgmt:* Management said the largest clinical cohort "either transitions fully to the X or layers incremental volume onto X alongside existing NovaSeq 6000 workflows", and that 6000 pull-through "stays up" for validated tests (JPM conference, Jan 2026; Q4 2025 call). [E023]

12. **New X placements are mostly extra capacity.** *Mgmt:* Clinical was ">60% of placements, mostly incremental rather than conversions of 6000s" (Q1 2026 call) and about 70% (Q2 2026 call). *Opinion (broker):* JPM's recap said "as much as half of clinical placements appear to be incremental" (Aug 2026). [E024, E397]

13. **Many clinical labs own both machines.** *Fact (survey):* Of 32 clinical respondents in JPM's May 2026 customer survey, 24 (75%) own at least one 6000 and 17 (53%) own an X (a "16%" summary figure is a typo). *Our calc:* By simple counting, 9 to 17 labs own both, 37.5–71% of clinical 6000 owners, though the survey says nothing about how their volume is split. [E021]

14. **What those dual owners could move without new purchases.** *Our calc:* Applied to the ~$728M of clinical 6000 revenue, $277–517M sits at labs that already own an X, and moving all of it to their existing X capacity would cost Illumina $195–364M a year (a 10%, 20% or 30% shift costs about $62M, $124M or $185M). *Our opinion:* The caveat is large, because this is a count of 32 labs, not revenue. [E248]

15. **Job postings show both machines in use.** *Fact (anecdotal):* A Tempus technologist posting lists "Illumina Novaseq6000 and NovaX", and Natera postings name "NovaSeq and NovaSeq X Plus" (2026 postings). *Fact (weak source):* A search summary says Caris's FY25 10-K mentions both platforms; we did not verify this in the filing. [E022]

16. **Parallel instruments at the biggest accounts.** *Opinion (competitor employee, hearsay):* A Roche precision-medicine lead said vendor labs embedded in the UK's NHS (Foundation, Guardant, Natera) typically run the vendor-recommended sequencer plus a second Illumina sequencer (expert call, Jul 2026). *Opinion (expert):* A former Illumina senior manager said ex-China clinical growth of about 20% is "largely driven by big accounts: Natera, Tempus, Caris and Foundation Medicine". [E426]

17. **Management's map of clinical customers.** *Mgmt:* Thaysen described four groups (Wolfe, Nov 2025). Two are small: low-volume labs that never convert, and price-motivated movers such as NIPT labs, "<20%" and mostly moved. The other two are labs keeping old tests on the 6000 while putting new, larger ones on the X, and labs moving from exomes to genomes. [E028]

18. **Which groups matter, and what they pay.** *Mgmt:* Thaysen said those two middle groups are "absolutely the largest" and use the 25B flow cell, while the others stay on the smaller 10B at "more like high-volume 6000 pricing" (Wolfe, Nov 2025). *Our opinion:* So some X volume is priced close to the 6000, which narrows the gap that conversion removes. [E028]

19. **The "40 converted customers" cohort.** *Fact:* The Q3 2025 deck showed 40 clinical customers that had "fully or largely" converted, with growth labels but no axis values. It excludes brand-new HT customers and has not been updated since September 2025. [E025]

20. **What management said the cohort shows.** *Mgmt:* Dhingra said "volume offset price in year 1 and then revenue and volume both accelerated in year 2". Thaysen accepted an analyst's reading of year-1 revenue growth as under 5%, calling it "a little bit flattish… almost in an equilibrium" (Q3 2025 call; JPM conference, Jan 2026). [E026]

21. **Why the cohort says little about the tail.** *Our opinion:* Early converters are the most motivated to grow, and the laggards (validated, FDA-approved and low-volume labs) are absent; Illumina has said it will not keep reporting cohorts (JPM conference, Jan 2026). *Our calc:* Flat year-1 revenue after a 60–70% price cut needs converting Gb to rise 2.5–3.3 times, which fits new tests, not old workloads moving over. [E027, E303]

22. **Why labs wait.** *Mgmt:* The former CFO said tests validated on the 6000 "will not immediately switch" and the X gets "newer assays that were marginally viable or not viable on the 6K" (Evercore, Nov 2023). Thaysen said "validation cost outweighs the savings of moving an existing assay" in some cases (Q3 2024 call). [E031]

23. **Illumina defends key sites with give-aways.** *Opinion (expert, hearsay):* A former field application scientist said that at a site like Memorial Sloan Kettering, Illumina offers a free liquid-handling robot, a free NextSeq 2000, training and a free year of software (expert call, Jul 2026). *Our opinion:* These would be hidden concessions beyond list price. [E329]

24. **And makes rival platforms harder to validate.** *Opinion (expert, hearsay):* The same source said Illumina has refused to support validating its TruSight Oncology cancer panel on Element's sequencer, and a former associate director called switching an FDA-approved test "incredibly hard" (expert calls, 2026). [E329]

25. **Outsourced research has already left the 6000.** *Fact:* Novogene, a large commercial sequencing provider, stopped quoting 6000 work on 1 December 2024 and ended all 6000 support on 1 June 2025, moving to an X Plus fleet. *Our opinion:* So what remains of the tail is mostly in-house clinical and large-lab work. [E280]

26. **Late conversion costs a core its customers.** *Opinion (customer):* A Georgia academic core kept its 6000 about 1–1.5 years longer than it wanted while waiting for an X Plus, and lost external customers to vendors with X Plus prices (expert call, 2026). [E169]

27. **The X "cannibalized the business".** *Opinion (expert):* A former Illumina associate director (left Sep 2024) said the X delivered four 6000s' worth of output at "almost half, if not 1/3" of the run cost (expert call). [E330]

### D. Why the regulated part of the tail is sticky

1. **No high-throughput X for regulated tests, so far.** *Fact:* We found no FDA-cleared or CE-marked NovaSeq X; the only IVD high-throughput Illumina sequencer is the NovaSeq 6000Dx (2022). Illumina's own FDA-approved cancer panel, TruSight Oncology Comprehensive, still runs only on the smaller NextSeq 550Dx through its latest supplement (4 Sep 2026). *Fact (weak source):* A European web page mentioning X ordering for that panel is unverified. [E250]

2. **The FDA database shows no move to the X.** *Fact:* An openFDA check found that FoundationOne CDx moved from the HiSeq 4000 to the NovaSeq 6000, approved 25 April 2024 after about 11 months. No supplement for Guardant360 CDx, FoundationOne Liquid CDx, Tempus xT CDx or Guardant Shield names the X, through September 2026. [E287]

3. **Caris's FDA-approved test is anchored to the 6000.** *Fact:* Caris MI Cancer Seek (approved Nov 2024) is specified on the "Illumina NovaSeq 6000", and none of its 10 supplements through July 2026 names a sequencer. Caris's lab-developed volume may run elsewhere; we did not check. [E296]

4. **Guardant moved its lab-developed liquid biopsy to the X.** *Fact:* Guardant moved Guardant360 Liquid, the lab-developed version of its blood test, to the X in May 2026 (Guardant Q2 2026 call). [E288]

5. **Whether the FDA-approved version followed is unknown.** *Fact:* The same month the FDA approved a new application, Guardant360 Liquid CDx (19 May 2026). We could not read which sequencer it names, and its only supplement since is a 30-day manufacturing notice, not a sequencer change. [E297, E317]

6. **Why the Guardant question matters.** *Our opinion:* If the new approval names the X, an FDA route to the X exists and the regulated tail could start to move. If it names the 6000, Guardant's move covers only the lab-developed version. [E297]

7. **How long FDA steps take.** *Fact:* Initial approvals took about 7 months (Caris), about 10 months (Guardant Liquid CDx) and 17 months (TruSight Oncology Comprehensive); content supplements took about 9–17 months (openFDA). [E298]

8. **The lag after a platform launch is years.** *Fact:* FoundationOne CDx moved to the 6000 about 5.5 years after the 6000 launched. *Our opinion:* On that precedent, approved tests could reach the X (launched 2022–23) around 2028. [E298]

9. **A European lab was still validating on the 6000 in late 2025.** *Fact:* A regulated Italian clinical-exome lab (Siena) was still validating a 6000 workflow against the CE-marked 6000Dx in November 2025, with no mention of the X (published validation). [E251]

10. **A US genome program validated on the 6000 in 2025.** *Fact:* Providence/ISB's clinical genome program validated its 30x genome test on the 6000 in mid-2025, at about 125 Gb per sample (24 genomes per S4 flow cell) for over 2,000 patients (published validation). [E289]

11. **No 6000 end-of-life notice yet.** *Fact:* Illumina's product-retirement page lists only the iSeq 100, MiniSeq and MiSeq (end of sale 30 Sep 2025, service to 31 Dec 2029), with no 6000 entry and no 6000 trade-in program. *Our opinion:* On that template, a notice in mid-2027 would keep 6000 service running to about 2031–32, so 6000 consumables would not stop on the announcement. [E359]

12. **Experts say established tests do not move.** *Opinion (expert):* "You cannot switch an assay or a sequencer middle of a trial", trials last 5–7 years, and revalidation can cost up to "$200 million of clinical trials" for FDA products (expert calls). Adaptive's same-vendor move from the 6000 to the X reportedly took "years", and a cross-vendor move is a "four- or five-year project". [E116]

13. **Where conversion happens, customers keep the saving.** *Mgmt (customer):* Guardant said moving Guardant360 Liquid to the X cut its cost per test by about $200, and Adaptive said its MRD sequencing gross margin rose to 72% from 64%, "helped by the NovaSeq X transition" (Q2 2026 calls). *Fact:* Yet Guardant's consolidated gross margin was flat at 65% year on year, so the saving is not visible at company level. [E043, E044, E454]

### E. The precedent: the HiSeq-to-NovaSeq transition (2017–2020)

The last time Illumina moved its high-throughput customers to a cheaper platform (from the HiSeq to the NovaSeq 6000) is the best guide to how long a tail lasts and whether volume beats price.

1. **Volume did not offset price per Gb in 2019.** *Fact:* Data generated on Illumina sequencers rose 50% in 2019, while sequencing consumables revenue rose 14% (Q4 2019 call). *Our calc:* So revenue per Gb fell about 24%, and each 1% of extra volume added only about 0.3% to revenue. *Our opinion:* Management's current "mid-teens" annual price decline is lighter than that, though the comparison is rough because it blends all platforms. [E375]

2. **Growth and guidance through the transition.** *Fact:* Sequencing consumables grew 15% in FY17, 23% in FY18 (to about $1.8B), 14% in FY19 and −2% in FY20 (a COVID year). 2019 had been guided "above 20%" and came in at 14%, and Q3 2019 revenue guidance was cut to about 6% growth. *Our opinion:* So the transition years were good for consumables, but not as good as guided. [E376]

3. **Conversion took years.** *Mgmt:* Of about 850 HiSeq customers when the NovaSeq launched (Jan 2017), about 630 had not bought a NovaSeq by end-2018, and only "a little over 1/3" had started by end-2019 (Illumina calls). [E377, E386]

4. **And it left a tail.** *Mgmt:* At end-2020, 320 customers had still not started and about 1,000 HiSeq units were still active, four years after launch. *Fact:* Illumina cut the cost of converting for stragglers with cheaper "v1.5" reagents. *Our opinion:* That is a possible analog for the 35B. [E377, E386]

5. **The new platform took nearly all the growth.** *Mgmt:* NovaSeq consumable shipments "almost doubled" in 2019 to more than 110 petabases, while total Illumina data rose 50% to more than 150 petabases. *Our calc:* So data on older platforms fell about 20% (a unit caveat applies to the 2018 source). [E387]

6. **The genome price fell about 25% in a year.** *Mgmt:* The largest customers reached about $800 per whole genome (Q4 2019 call), and "labs of any size can now access the $600 genome" (JPM conference, Jan 2021). [E388]

7. **Pull-through halves as a platform ages.** *Mgmt:* NovaSeq pull-through was about $1.2M per system in 2019. *Fact:* The 6000's FY25 figure of about $670K is roughly half that, and the X guides $1.35–1.40M for FY26. [E378]

8. **Clinical was much smaller then.** *Fact:* Clinical consumables were about $830M in 2019 (+20%) and about $890M in 2020 (+8%), well under half today's size. *Our opinion:* So the 6000 tail is more clinical, and therefore stickier, than the HiSeq tail was. [E378]

### F. What conversion does to revenue and profit

These items are our own arithmetic on reported inputs. Each states its key assumption. They differ in what they assume about pace, volume and price, so they are best read together: the full-conversion numbers in the mechanics section are an upper bound, the phased numbers here are a better guide to any one year, and the profit numbers depend on margins Illumina does not disclose. The "Sizing" section that closes Question 1 reconciles the dollar figures in one table.

1. **If a fifth never moves.** *Our calc; assumes about 20% of 6000 volume never converts (Thaysen's rule of thumb).* The full hit then falls to about 23% of HT revenue (about $494M a year), against 29% if everything moves. Ordinary Gb growth of +30% would offset that within a year. [E005]

2. **The cost of each point of conversion.** *Our calc; assumes constant Gb and today's price ratio.* Each point of HT volume moving to the X costs about $36M a year of HT revenue, and each point of clinical volume about $24M. Reaching management's 80–85% clinical target from 78% therefore costs only about $18–35M a quarter in H2 2026. [E006]

3. **A rule of thumb for volume and revenue shares.** *Our calc; same assumptions.* Each 5 points of HT volume share moving to the X costs about 8.5% of HT revenue (about $45M a quarter), so an 85% X volume share costs about $18M a quarter against today and 90% about $64M. An 85% X volume share goes with about a 62.5% X revenue share at today's prices (60.7% at 84%, 64.4% at 86%). [E413]

4. **Timing matters more than the endpoint.** *Our calc; assumes Gb +30% and a 5% price fall within each platform.* Moving the X from 83% to 90% of volume over 12 months still leaves HT revenue up about 9%, while moving to 95% gives about −2%; at Gb +25% and 90%, the result is about +5%. *Our opinion:* The risk is fast, lumpy conversion, not where it ends. [E007]

5. **The revenue-at-risk bridge, at full conversion.** *Our calc; assumes converting customers get a 60% price cut and buy 15% more volume.* On that basis the whole $876M HT tail is worth $473M a year of lost revenue at full conversion, 15.2% of 2026 consensus sequencing consumables (range $307–613M). Extra volume on converted work barely helps, because the price cut dominates. [E246]

6. **The same bridge, phased.** *Our calc; assumes 25%, 60% and 80% of the tail has converted by end-2026, 2027 and 2028.* The cumulative loss is then about 3.8%, 9.1% and 12.2% of 2026 consumables. That is roughly 5 points of growth to make up in 2027 and 3 points in 2028. [E246]

7. **Three price layers already use up management's model.** *Our calc; assumes a 20% 35B cut and about 4% normal repricing a year.* From 2027, tail conversion takes about 6–7% a year off sequencing consumables, the 35B about 4% and normal repricing about 4%. Together that is the "mid-teens" decline management already models, so the model has no room for a price response to Roche or Ultima. [E247]

8. **What the 35B alone costs.** *Our calc; assumes a 20% cut, constant Gb, and an X consumables base of about $1.27B.* The 35B costs $63M, $127M or $253M a year (2.0%, 4.1% or 8.2% of 2026 consumables) at 25%, 50% or 100% adoption. [E247]

9. **A combined worst-but-plausible case.** *Our calc; assumes full conversion, a broad 35B and normal repricing by end-2028.* That combination costs about $640M (about 30% of HT revenue) and needs about +26% Gb a year to break even. [E247]

10. **Two-year break-even by scenario.** *Our calc; assumes a 4% a year residual price fall.* The table below shows the clinical Gb growth needed each year in 2027–28 to hold clinical revenue flat. Our base-case Gb path (+30% then +26%) roughly equals break-even in the two harshest rows, so there is little cushion if they happen. [E267]

The table lists the scenarios behind item 10, from mildest to harshest. The takeaway is that conversion alone is easy to absorb, while a broad 35B plus any competitive price cut pushes the hurdle into the mid-to-high 20s. (Question 2, section H, gives the single-year 2027 hurdles on a different price basis.) [E267]

| 2027–28 scenario (each row adds to the one above unless noted) | Clinical Gb growth needed per year |
|---|---|
| No more conversion, 4% residual price fall | +4.1% |
| Clinical X reaches 85% | +10.4% |
| Clinical X reaches 90% | +15.5% |
| Plus a 20% 35B cut on 60% of X dollars | +19.9% |
| Plus a further 10% competitive cut | +24.0% |
| 35B on all X volume (instead of 60%) | +28.1% |

11. **What Q3 consensus implies.** *Our calc (independent check by a second research agent); assumes our base price paths.* Q3 2026 consensus for sequencing consumables ($789M) needs clinical Gb growth of about 31% if the X price is flat, or about 47% if it falls 10% a year. Against trailing growth of about 42%, the first is easy and the second a stretch. [E445]

12. **What FY27 consensus implies.** *Our calc; same check.* FY27 consensus ($3,378M, +8.8%) needs HT Gb growth of 35–53%, roughly 50–77% for clinical. Clinical Gb growth of 20–30% gives only about $2.86–2.97B for FY27, about 12–15% below consensus. [E445]

13. **The same kind of model has missed recent quarters.** *Our calc:* Back-tested on Q1 to Q2 2026, the bridge predicted HT consumables up about 1% quarter on quarter, against an actual +6.8% ($501M to $535M). *Our opinion:* Either Q2 held one-offs or true Gb growth is well above management's mid-20s model, so these models are stress tests, not forecasts, and may lean bearish. [E446]

14. **Q4 2026 has an extra week.** *Mgmt:* Q3 2026 has the normal 13 weeks and Q4 has 14, "largely a consumables story" (CFO, Q2 2026 call). *Our calc; assumes the week is worth between nothing and a full thirteenth of the quarter:* On a 13-week basis the $815M Q4 consensus is worth $815M, $792M (management's "0.5 point") or $757M, which is growth of +3%, flat or −4% against Q3. *Our opinion:* So Q4 may flatter the trend. [E269, E448]

15. **How to read the Q3 X revenue share.** *Our calc; assumes an X price per Gb about 28–31% of the 6000's.* The X's revenue share follows mechanically from its volume share: an 85% volume share gives a 61–64% revenue share, 86% gives 63–66%, and the roughly 68–69% that fits guidance needs about 88%. A single quarter's move in the price ratio is within rounding and not informative. [E270]

16. **Our proposed Q3 break signals.** *Our calc:* Derived 6000 revenue above $210M, X pull-through below $1.20M, an X revenue share below 60%, and clinical growth below 12% would each argue that the tail is not running off as guided. [E270]

17. **The profit pool, if 6000 margins are as high as we assume.** *Our calc; assumes an 80–85% gross margin on 6000 consumables, which Illumina does not disclose.* On that assumption the 6000's roughly $219M a quarter (18.9% of revenue) supplies about 22–24% of Q2 2026 core gross profit ($790M) and about 67–71% of core operating income ($261M). Gross margin excluding the 6000 would be about 64.8%, against 68.2% reported, and if the real 6000 margin is lower these shares shrink. [E367]

18. **EPS at risk.** *Our calc; assumes the same margin, a 60–70% lower price per Gb on conversion, Gb +30% and unchanged opex.* Full conversion would cut gross profit about $84–127M a quarter, about $1.75–2.63 a year of non-GAAP EPS against an annualized Q2 2026 EPS of $5.24, or about $1.6–1.9 if 20% never moves. To keep gross profit flat, converting customers would need 175–215% more Gb. [E368]

19. **What the margin model predicts.** *Our calc; assumes our 80–85% 6000 margin and constant Gb.* Each 5-point rise in the X's revenue share would cost about $39M a quarter of gross profit, about 0.76 points of gross margin. So the 24-point rise since Q3 2024 implies about −3.6 points of gross margin. [E369]

20. **What actually happened to margin.** *Fact:* Core gross margin moved only −2.3 points over the same period (70.5% to 68.2%), about 2 points of it tariffs. *Our opinion:* So volume growth and cost cuts have so far absorbed the repricing. [E369]

21. **The X must be much cheaper to make.** *Mgmt:* Management says X consumables margins will be "comparable at scale" to the 6000's. *Our calc; assumes the 6000 earns 80–85%:* At a 70% lower price and equal cost per Gb, X consumables would earn only about a 41% margin, so keeping 70–80% needs X cost per Gb 50–67% below the 6000's. *Our calc:* Revenue per Gb fell about 34% from Q3 2024 to Q2 2026 while implied cost per Gb fell only about 21–29%, so margin per Gb has narrowed. [E370]

### G. Is the over-earning visible in gross margin?

1. **Reported gross margin has been range-bound.** *Fact:* Core (non-GAAP) gross margin stayed between 64.7% and 70.5% in every quarter from 2023 to mid-2026 (table below), and consumables margin is not disclosed. *Our opinion:* The swings track instrument mix, tariffs, memory and freight more than the X transition. [E034]

2. **Product and service margins.** *Our calc from 10-Q lines:* GAAP product gross margin, excluding amortization, moved between 68.5% and 74.3% from Q3 2024 to Q2 2026 (table below). *Fact:* Service gross margin rose from about 49% to about 55% over the same period. [E364]

The table shows both margin series by quarter. The takeaway is that neither series shows a steady slide as the X took over HT revenue: the lows (Q4 2023, Q4 2025) and the high (Q3 2024) reflect instrument mix and tariffs more than consumables pricing. [E034, E364]

| Quarter | Core (non-GAAP) gross margin | GAAP product gross margin, ex-amortization |
|---|---|---|
| Q1 2023 | 65.2% | n/a |
| Q2 2023 | 67.0% | n/a |
| Q3 2023 | 66.0% | n/a |
| Q4 2023 | 64.7% | n/a |
| Q1 2024 | 67.1% | n/a |
| Q2 2024 | 69.4% | n/a |
| Q3 2024 | 70.5% | 74.3% |
| Q4 2024 | 67.4% | n/a |
| Q1 2025 | 67.4% | 71.2% |
| Q2 2025 | 69.4% | 69.7% (72.3% excluding a $23M impairment) |
| Q3 2025 | 69.2% | 71.2% |
| Q4 2025 | 67.0% | 68.5% |
| Q1 2026 | 68.2% | 70.2% |
| Q2 2026 | 68.2% | 70.4% |

3. **The tariff bridge was given, then dropped.** *Fact:* Management quantified the tariff hit to gross margin at about 110bp in Q2 2025, 220bp in Q3 2025 and 205bp in Q4 2025, so Q4 2025 margin excluding tariffs was up about 165bp year on year. Q1 2026 said only "partly offset by tariffs", and Q2 2026 gave no figure even though margin fell 120bp. [E365]

4. **Consumables margin: the raw series fell.** *Our calc; assumes a 40% instrument margin.* Backing out consumables margin on that assumption, it fell from 78.8% (Q3 2024) to 75.0% (Q2 2026). [E366]

5. **But tariffs explain the fall.** *Our calc:* With tariffs added back, consumables margin is flat (78.8% against 78.4% for Q3 2024 versus Q3 2025, and 76.6% against 76.8% for Q4), and its link with the X's share almost disappears (a correlation of about −0.16 over six quarters, against −0.88 unadjusted). *Our opinion:* That partly supports management's "comparable at scale" claim. [E366]

6. **Q2 2026 margin fell on a non-GAAP basis.** *Fact:* Non-GAAP gross margin fell 1.2 points year on year (68.2% against 69.4%). GAAP margin rose 0.8 points (66.4% against 65.6%), but only because Q2 2025 included a $23M impairment; excluding it, GAAP fell about 1.4 points. [E389, E390]

7. **What explains the Q2 2026 fall.** *Our calc:* About 0.6 points of the non-GAAP fall comes from instruments, a lower-margin product, rising to 10.8% of revenue from 9.0%; the other 0.6 points is unexplained. [E390, E406]

8. **The 10-Q gives reasons but no sizes.** *Fact:* The Q2 2026 10-Q cites instrument mix, "rising memory costs, higher freight costs resulting from the Middle East conflict" and lower-margin SomaLogic revenue, "partially offset by lower tariff costs", with no figures. *Our opinion:* So a price effect cannot be ruled in or out. [E406]

9. **Product cost grew slightly faster than consumables.** *Fact:* The Q2 2026 10-Q's total consumables line was $852M (+4.8% year on year; broader than the $775M sequencing figure), while cost of product revenue grew 5.4% to $291M. *Mgmt:* The CFO said Illumina bought extra memory components "for next several quarters", so part of the inventory build is a pre-buy (Q2 2026 call). [E407, E451]

10. **Management's margin claims.** *Mgmt:* The former CFO said 6000 consumables are "highly profitable" and losing them hurts margin, and that X consumables were "designed so margins at scale would be comparable to NovaSeq 6000", with lower margins early (Q3 and Q4 2023 calls). *Fact:* No 6000-versus-X margin per Gb has been disclosed. [E035]

### Sizing: how big is the over-earning?

This section brings the sizing together and reconciles the different dollar figures that appear in this addendum. Two kinds of number appear, and they should not be confused. The **stock** is how much revenue would vanish if all remaining 6000 Gb were priced at X rates today. The **flow** is how much of that stock is lost in a given year as the tail converts.

**The headline.** *Our calc:* The clinical stock is about $500M a year, about 23% of our FY26 clinical consumables estimate. The clinical flow is about $150–190M a year in our base case, and the over-earning is much larger in profit than in revenue if our margin assumption holds. [E187, E447, E342]

**Why the denominators differ.** *Our calc:* The ~$728M clinical 6000 business is about 36% of Q2 2026 clinical consumables (a quarterly run-rate of about $504M, using management's ">65%" clinical share) and about 34% of our full-year FY26 estimate of $2.17B (which assumes a 70% share). The 23% stock figure uses the $2.17B base. [E187, E076]

The first table reconciles the **stock** figures. The takeaway is that they are the same calculation applied to different slices of the business, with or without a volume offset.

| Stock figure | What it covers | Key assumption | Tags |
|---|---|---|---|
| ~$617M/yr (−29% of HT) | All HT, research and clinical | All 6000 Gb at X prices, no extra volume | [E004] |
| ~$500M/yr (~23% of FY26 clinical, ~16% of all seq. consumables) | Clinical only | $728M × (1 − 1/3.39); same price gap in clinical | [E187, E447] |
| ~$494M/yr (−23% of HT) | All HT | A fifth of 6000 volume never moves | [E005] |
| ~$473M/yr (15.2% of FY26 consumables; range $307–613M) | All HT | 60% price cut, converting customers buy 15% more volume | [E246] |

The second table reconciles the **flow** figures, the annual amounts quoted in the answer in brief and elsewhere. The takeaway is that the figures from $145M to $240M are consistent once you see what each covers: the base-case $150–190M is the central figure, the bridge is a little lower because it allows extra volume, and the bear case is higher because conversion is faster.

| Flow figure | Year | What it covers | Key assumption | Tags |
|---|---|---|---|---|
| ~$40M a quarter (~$175M annualized) | H2 2026 | All HT 6000 revenue | Implied by the FY26 pull-through guide | [E245] |
| ~$190M, then ~$145M more | 2027, 2028 | Clinical, base case | Scenario model; constant 2026 Gb; 38% then 67% of clinical 6000 Gb converted | [E187, E342, E012] |
| ~$240M, then ~$116M more | 2027, 2028 | Clinical, bear case | Faster conversion (48% then 71%) | [E187, E342] |
| ~$120M, then ~$95M more | 2027, 2028 | Clinical, bull case | Slower conversion (24% then 43%) | [E187, E342] |
| ~$165M, then ~$96M more | 2027, 2028 | All HT | Revenue-at-risk bridge; 60% then 80% converted; converting customers buy 15% more volume | [E246] |
| ~$24M per point | Any year | Clinical | Each point of clinical Gb moving to the X, at constant Gb (~$31–33M at 2027 volumes after the 35B) | [E006, E413] |

The third table lists the other main sizing estimates, each detailed earlier in Question 1. The takeaway is that the premium and the clinical share are well supported, while the profit figures rest on an assumed margin.

| Measure | Estimate | Basis |
|---|---|---|
| 6000 premium per Gb vs X | ~3.4x (band 3.2–3.6x); X ~70% cheaper | Q2 2026 shares, Gb shipped [E001, E447] |
| Remaining 6000 revenue, all HT | ~$219M/qtr, ~$0.88B/yr | 69% HT share assumed [E003] |
| Remaining 6000 revenue, clinical | ~$182M/qtr, ~$0.73B/yr; ~49% of clinical HT | Same price gap assumed in clinical [E187] |
| Gb growth to break even on full conversion | Total HT +41%; clinical +53% | Constant price ratio [E004, E187] |
| Profit share of the 6000 | ~22–24% of gross profit; ~67–71% of core operating income | Assumed 80–85% margin [E367] |
| EPS at risk, full conversion | ~$1.75–2.63/yr vs ~$5.24 run-rate | Assumed margin [E368] |

**Confidence.** *Our opinion, on the evidence cited.*

1. **High confidence that a large premium exists and that clinical holds most of what is left.** The premium follows directly from Illumina's own share data, and the clinical share of the remaining 6000 volume follows from its three disclosed volume shares. [E001, E447, E009, E186]
2. **Moderate confidence in the dollar sizes.** They rest on three assumptions Illumina does not confirm: the 69% HT share, the 64% clinical share of HT Gb, and an equal price gap in clinical and research. [E003, E009, E187]
3. **Low confidence in the profit figures.** Platform margins are not disclosed, and tariff-adjusted gross margin shows no erosion so far. [E367, E368, E366]
4. **The pace is the real question.** The regulated evidence (FDA records, the HiSeq precedent and management's own 80–85% ceiling) points to a tail of 15–20% of clinical volume lasting into 2028 and beyond. [E287, E377, E342]
5. **Part of the unwind is already priced in.** The guidance arithmetic says the faster-moving part of the tail is being absorbed during H2 2026. [E245]

## Question 2: Will clinical volume growth offset the price decline?

This section is organized by driver: what Illumina reports, test volumes by application, how many Gb each test uses, the forward price per Gb, customers' own economics, competition, and customer concentration. It ends by comparing the Gb growth needed with the Gb growth the evidence supports, and gives a single bottom line.

### A. What Illumina reports about clinical growth and volume

1. **Clinical consumables growth outside China.** *Fact:* Ex-China clinical consumables growth accelerated from high single digits in 2024 to 12% for 2025 and 15–20% in H1 2026, while research and applied consumables (academic, pharma and other non-patient work) kept shrinking (Illumina decks; table below). *Our opinion:* Clinical growth accelerated while the price cut flowed through, which is the core of the bull case. [E073]

The table gives the quarterly growth rates behind item 1. The takeaway is that clinical peaked at +20% in Q4 2025 and Q1 2026 and slowed to +15% in Q2 2026, while research has been negative in every period shown except Q4 2024. [E073]

| Period | Ex-China clinical consumables growth | Research and applied consumables growth |
|---|---|---|
| Q1 2024 | +7% | −11% |
| Q2 2024 | +5% | −9% |
| Q3 2024 | +11% | −8% |
| Q4 2024 | +8% | 0% |
| Q1 2025 | +8% | n/a |
| Q2 2025 | +10% | n/a |
| Q3 2025 | +12% | n/a |
| Q4 2025 | +20% | n/a |
| FY 2025 | +12% | −7% |
| Q1 2026 | +20% | −12% |
| Q2 2026 | +15% | −7% |

2. **The FY26 clinical guide.** *Mgmt:* Clinical guidance moved from "double-digit to mid-teens" (February and April) to "mid-teens" (July), and US and Canadian clinical grew more than 20% while Europe, the Middle East and Latin America were slower (Q2 2026 call). *Our calc:* With H1 at about 17%, the guide implies about 13–14% in H2. [E074]

3. **The Q3 guide implies a slowdown.** *Mgmt:* The Q3 2026 guide for total organic revenue outside China is about 4.5% growth, against 8.1% in Q2 (Q2 2026 call). *Our opinion:* That is a clear deceleration, though it covers all products, not only clinical. [E074]

4. **Two-year stacks point to a soft Q4.** *Our calc:* Adding each quarter's growth to the prior year's gives a "two-year stack" of 28 points in Q1 2026 (20 + 8) and 25 in Q2 (15 + 10). If the stack holds, Q3 2026 clinical growth is about 13–16% against an easy +12% comparison, but Q4 only about 5–8% against a tough +20%. Hitting a mid-teens full year therefore needs Q4 well above that. [E306]

5. **Clinical is now about two-thirds of sequencing consumables.** *Mgmt:* Management put clinical at about 50–53% of sequencing consumables in 2023, 56% in January 2025, about 60% in mid-2025 and January 2026, and above 65% from April 2026 (calls and JPM-conference decks). *Our calc:* The latest rise is what you would expect when clinical grows about 20% and research shrinks about 12%. *Our opinion:* It matters because the clinical share sets how much of the business the 6000 tail and the 35B touch. [E076]

6. **"Clinical" is a loose, unaudited category.** *Opinion (broker, expert):* Bernstein said the bucket "includes clinical research" (May 2024), and a former Illumina senior manager called it "very generous and very broad", mostly lab-developed tests. *Fact:* Illumina's 10-Q reports one segment with no clinical split, so "clinical" exists only in earnings materials, and Dhingra has said the split between diagnostic and drug-development work is not disclosed. [E077, E211]

7. **How the January 2026 deck defines clinical.** *Fact:* The JPM-conference deck puts clinical at about 60% of sequencing consumables, counts Illumina's own TruSight Oncology 500 business (over $100M) inside clinical, and excludes about 3% "Other" (mainly infectious disease). [E211]

8. **What clinical is made of.** *Fact:* Clinical consumables are about 51% oncology, 25% genetic disease and 21% reproductive health (JPM-conference slides, Jan 2026); one deck pie showing 60% research appears to be a data-extraction error. *Mgmt:* MRD is "starting to drive momentum" but "therapy selection is still larger in dollars", early cancer detection "we don't really see… in the number today", and rare disease and NIPT are "still growing nicely" (Q2 2026 call). [E078, E079]

9. **How Illumina reports volume.** *Fact:* Illumina switched from counting runs to counting Gb after Q2 2023 and reported Gb growth of +29% to +46% a quarter from Q3 2023 to Q3 2024 (+29%, +46%, over 35%, then over 40% in Q2 and Q3 2024), after run-based activity growth of +9% in Q2 2023. From Q4 2024 it has given only ">30%", a floor that hides the true rate, with clinical "well above" (earnings calls). *Our opinion:* Against a ten-year average of about 25%, ">30%" is above history but says nothing about acceleration. [E049]

10. **The remaining price headwind is in clinical.** *Mgmt:* Dhingra said research Gb "still grew, albeit below the 30% kind of number" while clinical was "much, much stronger" (Q3 2025 call), which makes clinical well above 30% arithmetically. Thaysen said "we have now converted most of our Xs in the research business… we're not seeing the price headwind as we did before" (Q1 2026 call). [E206]

11. **Management's stated clinical volume number.** *Mgmt:* Thaysen said clinical sequencing volume growth is "above 30%" and "will continue for a while", with the whole business "approximately 25%". Dhingra said volume will "grow, we believe, over 30% in clinical" (JPM conference, Jan 2026). [E266]

12. **Genomes are the big lever, but still small.** *Fact:* A genome needs about 15 times the data of an exome (over 120 Gb against about 8 Gb). *Mgmt:* Whole-genome volume is "much, much smaller" than exome volume today, with no share given, and Thaysen said Illumina is "not splitting growth into mix and volume" and that intensity (more data per test) should be the main driver over time (Q4 2025 call). [E085, E086]

13. **Installed capacity, and why it is not a useful check on volume.** *Fact:* The January 2026 JPM-conference deck shows about 21,000 active Illumina instruments (over 12,000 low-, over 6,000 mid- and about 2,000 high-throughput) and says theoretical HT capacity "roughly doubled" from 2022 to 2025. *Our calc:* That is roughly 19–30% a year depending on the start date and how loosely "roughly" is read, and a bottom-up check on installed bases (an X is about 2.5 times a 6000 on spec) gives about 22%. *Our opinion:* This should not be read as volume outrunning capacity. The capacity figure is theoretical maximum output, while the ">30%" metric is actual output; since Q3 2025 it also includes mid-throughput machines, which management describes as muted while high-throughput grows faster, so high-throughput output growth is probably well above 30%. Actual output can outgrow capacity for years as new Xs ramp and utilization rises, so the comparison is neither a volume ceiling nor a bear signal. [E189, E207]

14. **Management's long-term model.** *Mgmt:* Volume grows in the mid-20s percent a year and price falls in the mid-teens, giving high-single-digit revenue growth (Strategy Day, Aug 2024; JPM conference, Jan 2026). In August 2024 the price impact was modelled at 20–25% a year, and Q3 2024 came in "closer to 25 rather than 20". *Our opinion:* The HiSeq-era figure was about −24% per Gb, so the mid-teens model is at the lighter end of history. [E047]

15. **The 2024 record: volume up, revenue flat.** *Mgmt:* In Q3 2024 Gb grew 40% while consumables grew 5–7%, "largely price… about, say, 25% decline on the price" (Dhingra, Wolfe Nov 2024); in Q2 2024 Gb grew 40% while HT revenue grew about 1%. *Fact:* On the Q3 2024 call Dhingra also said consumables grew "at a high single-digit rate", possibly meaning HT only, and the two figures are unreconciled. [E048]

16. **The elasticity claim has a mixed record.** *Mgmt:* Thaysen said "elasticity is… already happening now" in May 2024, when consumables were growing only 1%. *Opinion (broker):* An Evercore analyst said in 2023 that investors "are not seeing 3x volumes". [E105]

17. **Where elasticity is supposed to come from.** *Mgmt:* Most elasticity comes from new tests rather than old tests repriced: many tests become "volume-accretive within two to five years", MRD within the three-year plan and early detection "probably further out" (Strategy Day, Aug 2024). [E106]

18. **The biggest customers are expected to grow fastest.** *Mgmt:* Dhingra said "business with the largest customers is projected to grow faster than the company average" (Q3 2025 call), and Q2 2026 cited "several multi-unit capacity expansions from large clinical customers". [E103]

19. **Sell-side growth views.** *Opinion (brokers):* JPM models ex-China clinical consumables growing at a low-to-mid-teens rate through 2030, Barclays says "60% of the business grows more than 20%" (though Q2 already ran at 15%), and Freedom models consumables growth of only 5.5% a year for 2025–28. [E101]

20. **Broker revenue forecasts for 2027.** *Opinion (brokers):* For total 2027 revenue growth, JPM has +9.1%, Freedom about +5.7%, Barclays +5.5%, UBS +4.1% and FactSet consensus about +5.8%, against management's "high single digit". Only JPM is at management's level, so the Street is not uniformly bullish. [E102]

21. **Consensus for sequencing consumables.** *Fact:* Bloomberg consensus (10 Oct 2026) has $3,104M for FY26 (+5.6%), $3,378M for FY27 (+8.8%) and $3,694M for FY28 (+9.4%), accelerating to +13.1% by FY32 (few contributors after FY30). *Our opinion:* FY27–30 roughly match management's long-term model, so consensus is effectively management's model. [E080]

22. **The volume-versus-revenue puzzle.** *Our calc:* At Gb +30% and price −15%, revenue should grow about 10%, yet ex-China clinical grew 15–20%. So clinical Gb is well above 30%, or clinical price is falling less than the blended mid-teens, or mix helps. Dividing reported clinical growth by a 15% price fall gives clinical Gb growth of about +35–38% in H1 2026, consistent with management's "well above 30%". [E075, E304]

23. **Revenue-implied clinical Gb growth is high.** *Our calc; assumes equal price ratios in clinical and research:* A fuller bridge, using clinical X volume shares and the 6000-to-X price ratio, gives trailing clinical Gb growth of about +35–50% for 2025 to mid-2026, centrally about +42%. It also implies clinical price per Gb fell about 20–28% a year, more than the mid-teens management cites. A higher method (+60–65%) clashed with total Gb of ">30%" and was discarded. [E205]

24. **The bottom-up test model came in lower at first.** *Our calc:* The bottom-up test model (category volumes times assumed Gb per test) first gave clinical Gb growth of about +9–10% (low), +23% (base) and +35% (high) a year for 2026–28, which at a mid-teens price fall means clinical revenue of −7%, +5% and +14%. Its +23% base also implied total HT Gb of only +19–22%, which cannot be squared with management's ">30%". [E083, E264]

25. **Re-run on Q2 2026 prints, it agrees with management.** *Our calc:* Re-run on Q2 2026 test volumes, the same model gives about +31% (+33–34% with Gb-based weights), so the original +23% is superseded. [E263]

26. **What the 35B does to the hurdle.** *Our calc; assumes the 35B cuts price per Gb 20%.* A 20% cut alone needs about 25% more Gb to keep revenue flat, and stacked on a 15% base decline the effective cut is 32%, so clinical Gb must grow about 47%. With only half the 35B cut the hurdle is about 31%, and on a 10% base decline with the full cut about 39%. [E084, E305]

27. **The hurdle for growth, not just flat revenue.** *Our calc; same assumption.* For +10% clinical revenue in FY27, Gb must grow 29% without a 35B cut and about 62% with a full cut on a 15% base decline. [E084, E305]

### B. Test volumes by application

Test growth is not Gb growth. Each item below gives the Q2 2026 test print (company releases and 10-Qs) and what it means for Gb. For comparison, Illumina's own ex-China clinical consumables grew 15% in the same quarter. [E081]

1. **Natera: fast MRD growth, but light on Gb.** *Fact:* Natera ran 283K clinical MRD tests in Q2 2026 (+56% year on year), within 296.7K oncology tests (+57%) and 1.04M tests in total (+22%; non-MRD about +13%). *Our calc:* Its classic Signatera MRD test uses well under 1 Gb per blood draw, so test growth overstates Gb growth unless the genome-based version takes share. [E081, E432]

2. **Guardant: blood-based cancer profiling is Gb-heavy.** *Fact:* Guardant ran about 104K oncology tests (+63%), with Guardant360 Liquid up over 30% and its Reveal MRD test up over 100%. *Opinion (our estimate):* Liquid-biopsy profiling probably uses about 35–120 Gb a test, so this is one of the most Gb-rich growth streams. [E081, E082]

3. **Guardant Shield: screening volume quadrupled.** *Fact:* Shield, Guardant's colorectal screening blood test, ran about 66K tests (about 4x a year earlier). Gb per Shield test is not disclosed. [E081]

4. **GeneDx: exomes and genomes are mid-to-high intensity.** *Fact:* GeneDx ran 30,785 exomes and genomes (+32%). *Our opinion:* An exome uses about 8–11 Gb and a genome over 100 Gb, so any mix shift to genomes lifts Gb sharply. [E081, E435]

5. **Tempus: steady oncology growth, small MRD.** *Fact:* Tempus's oncology volume grew 31%, and MRD reached about 9K tests (+38% quarter on quarter). Its clinical sequencing volume was over 212,000 tests in Q2 2025 (+30%), and MRD year-on-year growth cannot be built because volume was held back pending Medicare coverage. [E081, E453]

6. **Caris: decelerating, but the deepest tests.** *Fact:* Caris's clinical cases grew 18% to 59.2K, down from 22.0% growth (50,032 cases) in Q2 2025. *Our opinion:* Caris runs whole-exome and whole-transcriptome tests, among the heaviest per case, so its slowdown matters more for Gb than its case count suggests. [E081, E452]

7. **Adaptive: MRD volume up 43%.** *Fact:* Adaptive's clonoSEQ MRD tests (immune-cell sequencing for blood cancers) grew 43% to 36,111. It has already moved to the X, so it adds volume at the lower X price. [E081, E044]

8. **Smaller names: mixed, and light on Gb.** *Fact:* Veracyte's Decipher prostate test grew 17%, BillionToOne's tests 35% and Myriad's volume fell 1%, against Natera's +22% total and Illumina's +15% clinical consumables growth. *Our opinion:* BillionToOne is mostly prenatal (about 1–2 Gb a test), Myriad sells hereditary panels and Decipher's sequencing intensity is unclear, so together these add little Gb either way. [E081, E095]

9. **Tempus is buying a high-data MRD test.** *Fact:* Tempus's MRD business is near break-even at about 9K tests a quarter, and Tempus is buying Personalis (about $1.5B enterprise value, $16.25 a share, announced 20 Jul 2026, closing late 2026 or early 2027). Personalis's NeXT Personal test starts from a whole tumor genome. *Our opinion:* That would raise Gb per MRD patient at Tempus. [E093]

10. **Our ranges for test growth (not Gb).** *Opinion (our research agents):* Our ranges have MRD growing fastest and NIPT and hereditary screening slowest, with growth slowing in every category by 2028 (table below). These are test counts, so they must be multiplied by Gb per test (section C) before they say anything about volume. [E099]

The table shows those ranges by category and year. The takeaway is that the fastest-growing category, MRD, is also one of the lightest in Gb per test, while the Gb-heavy categories (CGP, liquid biopsy, rare-disease genomes) grow more slowly. [E099]

| Test category | 2026 | 2027 | 2028 |
|---|---|---|---|
| MRD | +45–60% | +30–45% | +20–35% |
| CGP and liquid biopsy | +25–35% | +20–30% | +15–25% |
| Rare disease | +25–35% | +25–40% | +20–30% |
| NIPT | +5–10% (no split by year given) | | |
| Hereditary and carrier screening | low single digits to +10% (no split by year given) | | |

11. **Experts see saturation outside MRD.** *Opinion (expert):* Experts said NIPT already reaches about 70–80% of pregnancies, CGP is "quite saturated", rare disease is "not a very large growing market", and MRD repeat testing runs 3–4 times a year. They added that the adoption bottleneck is reimbursement "even if sequencing is free" (expert calls). [E096]

12. **MRD guideline progress: bladder.** *Fact:* NCCN added ctDNA-based MRD to its muscle-invasive bladder cancer guideline on 23 June 2026, after the FDA approved the immunotherapy drug atezolizumab (Roche's Tecentriq) for ctDNA-positive patients with Signatera as the companion test (May 2026). *Our opinion:* The guideline favors a tumor-informed panel test, so it adds tests but not necessarily many Gb. [E418]

13. **The bladder trial implies frequent testing.** *Fact:* In IMvigor011, the trial behind that approval (about 761 patients), blood was drawn every 6 weeks for up to a year, up to about 8–9 draws per patient-year, with clear survival benefits. [E427]

14. **MRD guideline progress: colon is stuck.** *Fact:* NCCN's colon and rectal guidance (Feb 2025) still calls ctDNA prognostic only, with "insufficient evidence to recommend routine use… outside of a clinical trial". The DYNAMIC-III trial (1,002 patients, Oct 2025) showed that testing can safely reduce treatment but not that it helps to intensify it, and the CIRCULATE-Japan ALTAIR trial missed its primary endpoint (Jun 2026). [E419, E429]

15. **A misread colon result.** *Fact:* The ASCO 2026 "CIRCULATE" result (62% vs 19% recurrence) came from the German CIRCULATE-AIO trial, which was formally negative on intention to treat, with only 2.9% of patients ctDNA-positive from a single draw. The US Signatera trial (CIRCULATE-US) has no readout yet. *Our opinion:* So colon MRD volume has no guideline tailwind before then. [E430, E440]

16. **MRD draw cadence.** *Fact:* The GALAXY study draws blood every 3 months for two years, about 4 a year (2,625 patients). Medicare covers Signatera Genome in colorectal cancer "with the same frequency as CEA" monitoring (CEA is a routine blood marker test for colon cancer, typically done every 3–6 months), so roughly 2–4 draws a year. [E428, E439]

17. **How many patients there are.** *Fact:* US cancer incidence for 2026 is estimated at 2,114,850 new cases, 158,850 of them colorectal (American Cancer Society). *Our opinion:* With the draw cadence above, these are the inputs for any MRD patient model. [E443]

18. **Roche's MRD design uses little sequencing.** *Mgmt (competitor):* Roche's MRD approach is to "sequence the cancer, then monitor with specific primers on digital PCR" (a cheaper, non-sequencing DNA test), so repeat monitoring needs no sequencing at all; its Pathlight example covers 12 time points over 6 years (Roche H1 2026 call). [E088]

19. **NIPT guidelines could widen, with little Gb.** *Fact (weak source for ACMG):* The American College of Medical Genetics (ACMG, Dec 2025) recommends cell-free DNA prenatal screening as first-line for all pregnancies, stronger than the obstetricians' college (ACOG), which has no 2024–26 update we could find. *Our opinion:* At about 1–2 Gb a test, broader NIPT adds tests but few Gb. [E431]

20. **A weak NIPT read from a supplier.** *Fact:* Revvity's reproductive health business grew mid-teens in Q2 2026. *Our opinion:* It is a weak positive for NIPT volume, since the sequencer is not named. [E415]

21. **Rare disease: NHS England.** *Fact:* NHS England widened genome-sequencing eligibility from April 2026, and Genomics England extended its Illumina genome contract (£4.67M, on the 6000). *Fact (weak source, provisional search summary):* The NHS ran 42,461 rare-disease genomes and 3,294 rapid genomes for sick children in 2025/26. *Our calc:* That is roughly 4.5–5.5M Gb a year, under 1% of an estimated ~800M Gb HT base. [E100, E262]

22. **Rare disease: a cheaper genome raised demand in one hospital.** *Fact:* Uppsala University Hospital put an X into rare-disease genomes in 2024 and saw rare-disease patients rise about 40%. *Our opinion:* It is one site, but it is a direct example of elasticity. [E321]

23. **Public-sector demand is small or shrinking.** *Fact:* All of Us, the US NIH genome program, has about $153M of funding in FY26, about 72% below FY23, and the UK Generation Study had recruited 52,000 of 100,000 babies by March 2026. UK Biobank proteomics and Truveta's 10M-exome project run with Regeneron, an Ultima user. *Our opinion:* Identifiable programs add only about 1–2 points to clinical Gb growth through 2027. [E322]

24. **A children's genome bill is not law.** *Fact:* A US bill to make genome sequencing a covered Medicaid service for children from 2027 (H.R. 7118) has not been enacted. [E323]

25. **MCED: Galleri volumes.** *Fact:* GRAIL sold more than 185,000 Galleri tests in FY25 (US revenue $136.8M, +26%) and more than 117,000 in H1 2026 (+42%), including more than 61,000 in Q2 2026 (+35%). *Our calc:* In Q2 its screening cost was about $382 a test, against revenue of about $698 a test. [E178, E331]

26. **MCED: the FDA panel.** *Fact:* An FDA advisory panel voted 6–4 that Galleri is effective, 10–0 that it is safe and 7–2 that benefits outweigh risks (23 Sep 2026), and GRAIL expects a decision in early 2027. Reported sensitivity (the share of real cancers the test catches) was about 31–35%, with specificity (the share of healthy people correctly told they are clear) above 99.7%; list price is $949. [E318, E320]

27. **MCED: no NHS rollout soon.** *Fact:* The NHS-Galleri trial missed its primary endpoint. *Our opinion:* So an NHS rollout is not a near-term volume source. [E349]

28. **MCED: Medicare comes in 2028 at the earliest.** *Fact:* The Medicare MCED Screening Coverage Act was signed on 3 Feb 2026; coverage starts in 2028, only for FDA-approved tests, at one test a year. [E319]

29. **MCED: how much sequencing it uses.** *Fact:* Galleri's published research design used about 34 Gb per sample. *Mgmt (customer; weak source):* GRAIL says its enhanced version (late 2024) fits about 4 times more samples per flow cell, perhaps about 8.5 Gb a test. *Fact:* GRAIL's FY25 cost of screening rose 16% on 36% more volume, about 15% less per test. [E334, E335, E336]

30. **MCED: what it is worth to Illumina.** *Our calc:* At 1M tests a year, Galleri would add about $25–102M of Illumina consumables, 1–5% of clinical. *Our opinion:* That is consistent with management's "we don't really see that in the number today". [E362]

31. **Medicare spending on genetic tests.** *Fact:* Medicare Part B spent $3.6B of its $8.4B lab spending (43%) on genetic tests in 2024, up 20% in 2023–24, about 18M tests against 7M in 2018. The HHS inspector general (OIG, the health department's watchdog) flags these tests for fraud scrutiny (OIG, Jan 2026). *Our opinion:* Fast payer spending growth invites tighter rules, which is the risk in the next item. [E098]

32. **Medicare's 2027 fee cuts spare branded tests.** *Fact:* CMS's preliminary 2027 lab fee schedule (21 Sep 2026) cuts generic genomic-sequencing billing codes 23% and molecular pathology 22% on average, but proprietary lab-specific codes (PLA codes, which cover single branded tests) only 2.4%, with any one test's cut capped at 15% a year in 2027–29. ACLA, the clinical-lab trade association, counts 775 tests taking the full 15% in 2027. *Our opinion:* So branded MRD and CGP tests are mostly protected, and generic hereditary and exome panels are most exposed. [E097, E219]

33. **Local Medicare coverage decisions.** *Fact:* The regional Medicare (MolDX) coverage policies effective 12 Oct 2026 are not sequencing-relevant; the relevant ones (blood-cancer NGS and genome-wide copy-number testing) are still proposals. About 24 US states have biomarker-coverage laws (which require insurers to pay for guideline-backed biomarker tests) and about 11 more are pending. *Our opinion:* None of these can be sized in Gb, and none changes 2027 volume materially on current evidence. [E098, E203]

34. **Adjacent suppliers show solid but not explosive demand.** *Fact:* Twist's NGS revenue grew 12% in its June 2026 quarter, with a target to "return to 20%" on an MRD ramp (a top-10-customers-at-48% figure is unverified). Qiagen's NGS panels for third-party sequencers grew more than 20% in Q2 2026 (against 2% for its wider NGS group), and Azenta's multiomics grew 8% organically. *Our opinion:* These are revenue-per-sample signals, a weak proxy for Gb, and all are well below the ~40% Gb growth implied for Illumina's clinical customers. [E402, E403, E414, E416]

35. **Research demand remains a drag.** *Fact:* The NIH indirect-cost cap was permanently blocked (Jan 2026), but NIH grant obligations were 34% below FY2024 by March 2026, Bruker's US academic revenue fell more than $15M and 10x called academic funding "tenuous". Thermo said US academic "returned to growth", which conflicts with Bruker and 10x. *Our opinion:* Weak research keeps the clinical share rising, but also keeps total consumables growth below clinical. [E423, E424, E425]

### C. Sequencing intensity: how many Gb each test uses

1. **The intensity ladder.** *Opinion (our estimates from published specs):* Rough Gb per test is about 1–2 for NIPT, about 8 for an exome, about 15 for tissue CGP, about 100–120 or more for a 30x genome, and well under 1 per blood draw for classic amplicon MRD (plus a one-off tumor exome). Liquid-biopsy CGP was first put at about 120 Gb, but later checks suggest about 35–100 Gb; a "≥250 Gb" figure belongs to Personalis's NeXT Liquid Biopsy, not its MRD test. [E082]

2. **Classic MRD uses very little data per draw.** *Fact (spec):* Signatera sequences 16 tumor-specific variants at about 100,000x depth. *Our calc:* That is about 0.16 Gb per blood draw, so across a patient-year the one-off tumor exome carries about 80–90% of the Gb, and fast MRD test growth lifts Gb much less than test counts suggest. [E432]

3. **Genome-based MRD is 10–15 times heavier per draw.** *Fact (weak source: snippet-level spec):* Signatera Genome, launched broadly in April 2025, tracks 64 variants at up to 350,000x, about 22M reads. *Our calc:* That is roughly 2.2–3.4 Gb per draw against 0.16–0.24 Gb for classic Signatera. *Our opinion:* A shift of MRD mix toward genome-based tests is the main route to large Gb gains in MRD. [E438]

4. **Illumina's own whole-genome MRD kit.** *Fact:* It entered early access on 28 May 2026, with global launch in 2027 and sensitivity of 10 parts per million now; depth and Gb per sample are undisclosed. *Mgmt:* Management has a single-digit parts-per-million goal, and Thaysen expects Illumina's next chemistry to unlock high-sensitivity MRD within about 18 months. [E087]

5. **NIPT could get deeper.** *Fact:* At 20M reads (about 6 Gb), NIPT detected microdeletions (small missing chromosome pieces) with 79% sensitivity, against about 3M reads for standard NIPT (published study). *Our opinion:* Microdeletion panels would be an upside lever for NIPT Gb. [E455]

6. **Illumina's own planning figures.** *Fact:* The X specification page assumes more than 120 Gb per 30x genome and about 11.3 Gb per 100x exome, above our ~8 Gb exome estimate. The 6000 product page is still live as an active product, with no end-of-life notice. [E435]

7. **Named customers explain only a slice of clinical Gb.** *Our calc:* Multiplying Q2 2026 test volumes at Natera, Guardant, GeneDx, Caris, Adaptive and BillionToOne by estimated Gb per test gives about 10 petabases a quarter. Top-down clinical HT Gb is about 81–139 petabases (at an assumed net price of $1.75–3.00 per Gb), so the named labs explain only about 7–13%. *Our opinion:* Either our intensity estimates are too low for the big oncology names, or most clinical Gb sits at unnamed labs. [E271]

8. **Savings get reinvested in depth.** *Mgmt (customer):* Fulgent raised its mean coverage on one test from 40x to 60x to 70x (Fulgent Q2 2026 call). [E379]

9. **But only where the economics allow.** *Fact:* Personalis's gross margin was 1.8% in Q1 and about 21% in Q2 2026, on clinical revenue of about $250 per test, which it blamed on unreimbursed tests. *Our opinion:* So cheaper Gb alone would not fix its economics, and labs without reimbursement cannot spend savings on depth. [E379]

### D. The forward price per Gb

1. **The 35B has no public price.** *Mgmt:* Thaysen refused to price the 35B flow cell: "we are not ready at this point to go out and talk about pricing", adding that "aggressive pricing brings aggressive volume growth" (Q1 2026 call; TD Cowen conference, Mar 2026). *Fact:* The 35B produces about 40% more output than the 25B and sits on the X's "18-month" roadmap. [E057]

2. **Illumina's own timetable is H1 2027.** *Fact:* Illumina's roadmap page (read 11 Oct 2026) lists the 35B and 14B flow cells for H1 2027, with no prices, and the 23 Feb 2026 press release gives the 14B a 20–22 hour run time. The order page lists only the 1.5B, 5B, 10B and 25B kits. [E214]

3. **The rest of the roadmap.** *Fact:* Other items are the 5B, a mid-sized X flow cell listed for H1 2026 (list about $5,986–6,750); a higher-accuracy chemistry called Q70 duplex (which reads both DNA strands to cut errors; early access in H2 2026); TruPath genomes ($395); and the whole-genome MRD kit (Illumina roadmap and press releases, 2026). No reagent-rental or formal price-cut program has been announced. [E135, E214]

4. **Expected size of the 35B cut.** *Opinion (expert, hearsay):* A former Illumina associate director (left Jul 2025) said the 35B would take cost from about $2.50 to about $2.00 per Gb, about 20% lower and "definitely" a price decrease (expert call, 2026). [E058]

5. **Why a 20% cut barely moves labs' total costs.** *Opinion (same expert, hearsay):* The same source said a clinical lab's total workflow cost would fall only about 5%, because sample preparation and data processing cost $600–1,100 per sample. *Our opinion:* So the 35B cuts Illumina's revenue per Gb far more than it cuts customers' cost per test. [E058]

6. **The 35B's timing, by hearsay.** *Opinion (customer, hearsay):* A Massachusetts genome-center VP said the 35B is "expected to come out in January" 2027. That fits Illumina's H1 2027 window but is not confirmed. [E058]

7. **What a genome costs today.** *Opinion (expert):* One UBS expert said customers pay about $175 per genome after discounts and larger users about $125, and that the 35B "likely brings Illumina pricing to $150 anyway" (26 Feb 2026). *Opinion (brokers):* UBS's own view is "a path to ~$150/genome", about 25% below the ~$200 list (UBS, 3 Mar 2026), and JPM lists Illumina at about $200 per genome against Roche at $150. [E059, E190]

8. **No 35B signal ahead of ASHG.** *Fact:* Illumina's page for the ASHG genetics conference (20–24 Oct 2026) shows no NovaSeq X or flow-cell content, and its newsroom has nothing on instruments or pricing since 1 October. *Our opinion:* The 25B launched at ASHG 2024, so this lowers but does not remove the chance of an ASHG launch. [E300]

9. **Price per Gb also falls without a list cut.** *Fact:* A Texas A&M customer quoted on Illumina's roadmap page says usable output per run "has increased by roughly 30 percent" since purchase. *Our calc:* On an unchanged flow-cell price, that is a 23% cut in price per Gb. [E056]

10. **More output upgrades are coming.** *Fact:* The roadmap promises an "HT mode" in H2 2026 (a run setting that, in Illumina's words, will "increase reads for better sequencing economics") and a 40% yield gain on 10B flow cells (roadmap page, read Oct 2026). *Our opinion:* Each is in effect a cut in price per Gb, even with list prices unchanged. [E056]

11. **Flow-cell prices were evened out.** *Fact:* In late 2025 Illumina "harmonised" the cost per read across its 5B, 10B and 25B flow cells, so the price per read no longer depends on flow-cell size at that customer (Swedish national genomics core, Nov 2025). [E261]

12. **Illumina is moving to deal-by-deal pricing.** *Mgmt:* "I don't think we're going to do global pricing going forward" (Aug 2024); "active talks with quite a few clinical customers on separate pricing for emerging tests" (Feb 2025); "if there are segments with significant elasticity… we are all for it" (Q4 2025 call). [E062]

13. **Volume discounts on multi-unit orders.** *Mgmt:* Thaysen calls volume discounts on 5- or 10-unit orders "reasonable", and says some customers are considering "tens of Xs" (Q4 2025 call). [E063]

14. **Large accounts already pay far less.** *Opinion (expert):* Former employees say large accounts pay "half or even a quarter" of what a small core facility or contract research organization (CRO) pays, and that Broad Institute discounts are "insane" (expert calls). [E063]

15. **Some costs are being passed to customers.** *Mgmt:* On the Q2 2026 call management said "we're sharing some of the increase with customers" for memory and freight costs, after saying in Q1 2026 that its own mitigation would "fully offset" inflation. *Our opinion:* That is a customer-facing price increase while competitors are cutting. [E064]

16. **Management prefers to talk about total workflow cost.** *Mgmt:* Since August 2024 management has framed the debate as "total cost of workflow" rather than price per Gb; Thaysen: "Only talking about cost per gigabase is probably too simplistic" (Feb 2024). It claims more than 30% savings from sample to answer, which we could not verify. [E065]

17. **Management conceded a premium and room to cut.** *Mgmt:* Asked whether cost per Gb is a lever "to compete more effectively", Thaysen said "on the mid throughput, we certainly have an opportunity to use our pricing if we need to… even when we provide premium cost per gigabase… we continue to be highly differentiated" (Q2 2024 call). [E278]

18. **Illumina's defense on "counting" applications.** *Mgmt:* Thaysen said counting applications exposed to Roche (such as RNA counting) are "probably less than USD 100 million" of Illumina's business, and that halving sequencing cost gives "maybe 20% more" experiments because library preparation dominates (TD Cowen, Mar 2026). Illumina's CTO said sequencing is 10–20% of cost in those applications (AGBT 2025). [E061]

19. **Customers say they expect a mild price decline.** *Fact (survey):* In JPM's survey (62 customers, May 2026), clinical respondents planned volume growth of +14.6% in 2027 and +19.1% in 2028, against spending growth of +9.4% and +14.0%. *Opinion (broker):* JPM infers a price decline of only about 4–5% a year (about 2–4% for research). [E067]

20. **That conflicts with every other estimate.** *Our opinion:* The survey is stated plans from 32 clinical labs, not realized pricing, and its 4–5% conflicts with management's mid-teens and our revenue-implied 20–28%. It is the weakest of the three. [E067]

21. **Former employees describe steady deflation.** *Opinion (expert):* One said the blended HT consumables price fell 30–40% from 2022 (about $5 per Gb to about $2.50), that "the price decrease is keeping up with demand", and that "flat would be a huge win" (expert calls). [E071]

22. **The earlier transition got more volume per price cut.** *Opinion (expert):* In the earlier NextSeq-to-NovaSeq era a 4x price cut brought 5–10x volume, while the X era's 20–50% cuts brought volume that "didn't get ahead" (expert calls; likely one person across two calls). [E071]

23. **Service-provider prices are flat to lower.** *Opinion (expert):* Outsourced providers' lane prices are about $1,800–2,000, flat to slightly lower; Illumina "prefers individualized quotes", and rep discounts may lapse after a year (expert calls). [E072]

24. **No peer shows revenue growing faster than volume.** *Mgmt (peers):* 10x's CEO says price per read "dropped like hugely" with Ultima and Roche; Oxford Nanopore's flow-cell volumes grew more than 20% while prices fell; MGI's 2025 units rose to 1,470 from 1,260 at lower prices; and PacBio cut its genome price about 30% (peer calls and results, 2025–26). *Our opinion:* The whole industry is trading price for volume. [E070]

### E. Customers' own economics: is their cost per test falling?

If labs simply pocketed cheaper sequencing, their cost per test would fall. Mostly it is not, which suggests the savings are being spent on more data per test.

1. **Natera: cost per test up about 9%.** *Fact:* Natera's cost of product revenue was $266.6M on 1,043,900 tests in Q2 2026, against $199.5M on 853,100 tests a year earlier (Natera Q2 2026 10-Q). *Our calc:* That is about $255 a test against about $234, while revenue per test rose about 12.5% to about $721. [E089]

2. **Natera's pricing is rising, not falling.** *Mgmt (customer):* Signatera's average price is about $1,275 (Q2 2026) against about $1,225 (Q4 2025), with a long-term target of $2,000, and gross margin was 64.5%, guided 64–66% for FY26 and 70%+ long term (Natera Q2 2026 call). *Fact:* Medicare's Signatera rate fell from $3,920 to $3,590 in January 2026. *Our opinion:* Even so, Natera can absorb sequencing cost without cutting its own price. [E089, E293]

3. **Guardant: a cost-down plan on Shield.** *Mgmt (customer):* Shield costs about $410 a test against a price of about $800, with a new workflow from August 2026 to cut about 15% by year-end and a 2028 target of $200 (Guardant Q2 2026 call). [E090]

4. **Guardant: volume guide raised.** *Mgmt (customer):* FY26 Shield volume is guided at 270–285K tests, and Guardant raised its FY26 oncology volume growth guide to about 50% from 35%, with non-GAAP gross margin of 67% (Guardant Q2 2026 call). [E090]

5. **GeneDx: unit cost appears to be falling.** *Fact:* Exome and genome volume grew 32% but revenue only 17%, as average reimbursement fell to $3,258 from about $3,700, and cost of services rose 13.8% to $36.2M (GeneDx Q2 2026 10-Q and call). *Our calc:* So cost per exome or genome fell about 14% (about $1,176 against $1,364), which is directional because the line includes other costs. [E091]

6. **GeneDx expects suppliers to cut prices in 2027.** *Mgmt (customer):* GeneDx says a genome costs "nearly double" an exome and that cost per test is "relatively flat" in H2 2026, and it expects "step improvements in 2027" as "manufacturers advance their technology" (GeneDx Q2 2026 call). *Fact:* Commercial insurance coverage for genomes rose from 47% to 87% of covered lives. [E091, E309]

7. **GeneDx's largest supplier share fell.** *Fact:* One unnamed supplier of reagents and equipment was about 14% of GeneDx's spend in Q2 2026, against about 20% a year earlier, while exome and genome tests grew 32%; GeneDx has $41.5M of purchase commitments through 2030 with no vendor named (GeneDx Q2 2026 10-Q). *Our opinion:* If that supplier is Illumina, this would be price deflation per Gb, but the supplier is not named. [E444]

8. **Caris: "always deeper, not cheaper".** *Fact:* Caris runs more than 114,000 whole-exome and whole-transcriptome tests a quarter within 345,000+ oncology tests, and its blood tests sequence twice. *Mgmt (customer):* Its CEO said cheaper rivals "create the opportunity to increase our capacity and decrease our cost of goods simultaneously", with gross margin guided to the "high 60s" (Caris Q2 2026 call). [E092]

9. **Caris's cost per case is rising.** *Fact:* Caris's molecular-profiling cost of services rose 24.5% to $81.3M, driven by blood-lab materials (+$8.6M) (Caris Q2 2026 10-Q). *Our calc:* So cost per case rose about 5–6% (about $1,373 against $1,301). *Fact:* Its FY25 gross margin of 66% (against 43%) was a price and mix gain, not cost deflation. [E294, E310]

10. **BillionToOne: fast growth from cheaper tests in 2025.** *Fact:* FY25 revenue was $305.1M (+100%) on 51% more tests, with gross margin of 68% (against 53%), citing "reductions in Overall Cost-Per-Test" (BillionToOne FY25 10-K). [E094, E295]

11. **BillionToOne: the cost decline has plateaued.** *Mgmt (customer):* In H1 2026 cost per test "stayed relatively stable" as oncology mix rose. *Fact:* Q2 2026 tests were 196K (+35%), revenue $109.4M (+64%) and gross margin 70% (BillionToOne Q2 2026 release and 10-Q). *Our opinion:* So in shallow prenatal testing, cheaper sequencing has already been passed through. [E094, E295]

12. **Myriad is a volume headwind.** *Fact:* Q2 2026 revenue was $190.7M (−11%), volume −1%, revenue per test −9% and prenatal −9%, and FY26 guidance was cut to $770–790M (Myriad Q2 2026 results 8-K). [E095]

### F. Competition, in brief

Competitors matter to Question 2 in two ways: they cap Illumina's price, and they could take the new, high-growth clinical volume that is supposed to offset the 6000 tail. The headline prices are in "Read-through from competitors": Roche's AXELIOS lists at $150 a genome, Ultima markets about $80, and UBS puts Element's VITARI at about half the X's cost per Gb. Three points matter here.

1. **Roche's list sits about 15–25% below Illumina's effective price.** *Opinion (broker, expert):* JPM lists Illumina at about $200 per genome, and a UBS expert puts the after-discount price at about $175 (Feb 2026). *Our calc:* Against Roche's $150 list, that is a gap of about 15–25%, which caps what Illumina can charge with the 35B. [E059, E190, E123]

2. **No big US clinical lab has switched.** *Fact:* None of the nine largest US clinical customers we checked (Natera, Guardant, Tempus, Caris, GeneDx, Foundation, Labcorp, Quest and Myriad) has a verified production test on a non-Illumina short-read sequencer, as of October 2026. This is the main reference for that finding; later sections point back here. [E353]

3. **Where challengers have clinical traction.** *Fact:* Challengers' clinical traction so far is in research-use pilots, prenatal and newborn kits in Europe, and one German pathology lab (*weak source* for the German lab). *Our opinion:* So competition caps price before it takes volume. [E353, E363]

### G. Customer concentration and bargaining power

1. **Illumina added a new concentration warning.** *Fact:* The FY25 10-K says revenue is "increasingly derived from a small number of large, centralized laboratory customers… Increased customer concentration may result in greater pricing pressure, reduced negotiating leverage." The word "centralized" appears in no earlier 10-K, and no customer exceeded 10% of revenue in FY23–25. [E107]

2. **More of Illumina is exposed to consumables pricing.** *Fact:* Consumables rose to 74% of revenue in FY25 from 72% (FY24) and 68% (FY23), with instruments at 11% and services 15%; sequencing is 92% of revenue (FY25 10-K). [E374]

3. **A few labs drive most of the volume.** *Mgmt:* Dhingra said the top ~30 customers per region drive planned purchases (Dec 2024), and in 2023 Illumina had about 1,000 HT customers (about 750 with one 6000, about 250 with several). *Opinion (expert):* Experts say the top 10–20 clinical labs drive most volume. *Fact:* There is no revenue-concentration table anywhere in Illumina's disclosures. [E108]

4. **Customers have leverage.** *Opinion (expert):* Former employees say large accounts (Broad, Natera, Guardant, Foundation) pay "half or even a quarter" of small accounts' prices, and that contracts "can quickly become null and void" when a rival undercuts by 25–50%. They add that Illumina's consumable margins could fall "below 50% in some cases" against Element and that "customers have big bargaining power" (expert calls). [E113]

5. **Contracts tilt toward lower prices.** *Fact:* The supply contracts we could read (Natera, Caris, Guardant, Tempus) let the customer leave on 90 days' notice and carry no dollar purchase minimums, and the Natera and Caris contracts contain clauses under which the price per Gb can only fall (SEC exhibits). Details are in "Read-through from clinical customers". [E212, E228, E232, E284]

### H. Putting it together: the Gb growth needed versus the Gb growth in evidence

**The bottom line for Question 2.** *Our opinion:* Volume has clearly beaten price in 2025–26. For 2027, our base case says volume only barely offsets price (+2.5% clinical HT revenue), a broad 35B cut would tip it to a decline, and consensus needs trailing volume growth to continue undiminished. The two tables below show why.

The first table shows how much clinical Gb growth is needed just to hold clinical HT revenue flat in 2027 under different price assumptions. The takeaway is that the hurdle runs from about 15% (conversion only) to about 47% (conversion plus management's mid-teens plus a full 35B cut), so the answer hinges on the 35B. All rows are *Our calc*; the two-year 2027–28 version is the table in Question 1, section F.

| 2027 scenario | Clinical Gb growth needed for flat clinical HT revenue | Tags |
|---|---|---|
| Conversion only (clinical X 79% to 87%), X price flat | +14.6% | [E187, E342] |
| Management's mid-teens price decline alone | +17.6% | [E047] |
| Our base case: conversion, 35B on half of X volume, −5% residual | +26.8% | [E058, E247] |
| Mid-teens decline plus a full −20% 35B cut | +47% | [E084, E305] |

The second table lists the evidence on what clinical Gb growth actually is or will be. The takeaway is that backward-looking evidence (+35–50%) clears every hurdle, while forward-looking evidence from customers and bottom-up models (+15–31%) clears only the lower ones.

| Evidence | Clinical Gb growth | Time basis | Reliability |
|---|---|---|---|
| Revenue-implied bridge (*Our calc*) | +35–50%, central ~42% | Trailing, 2025–H1 2026 | Moderate; assumes equal price gap [E205, E304] |
| Management (*Mgmt*) | "above 30%… for a while"; whole business ~25% long term | Forward | Claim; floor metric [E266] |
| Bottom-up test model, re-run on Q2 prints (*Our calc*) | ~+31% (+33–34% Gb-weighted) | 2026 | Assumption-heavy [E263] |
| Original bottom-up base (*Our calc*) | +23% (range +10% to +35%) | 2026–28 forecast | Superseded by later prints [E083] |
| JPM customer survey, clinical, n=32 (*Fact (survey)*) | Volume +14.6% (2027), +19.1% (2028) | Forward plans | Small sample, self-reported [E067] |

**Our base-case assumption, which is a judgement, not evidence.** *Our opinion:* We assume clinical Gb grows +30% in 2027 and +26% in 2028. That is a slowdown from the trailing ~42%, toward management's ">30%" and the re-run model's ~31%, and well above the survey's high teens [E205, E266, E263, E067].

**How the two tables fit together.** *Our calc:* Our base case needs about +27% clinical Gb in 2027 to stand still and assumes +30%, a cushion of only about 3 points [E247, E267]. That is why it delivers just +2.5% clinical HT revenue, or about +4% for all clinical consumables once smaller sequencers are added, and about +6% in 2028 [E205, E247].

**What would make the answer "yes" or "no" for 2027.** *Our opinion:* If trailing Gb growth of about 40% persists, volume beats price comfortably again (about +10% clinical HT revenue at the base price path). If customers' own high-teens plans are right, or the 35B cut covers all X volume, volume does not offset price and clinical HT revenue falls. Consensus (implying 13–14% clinical growth) sits near the first outcome, and our base case is well short of it [E067, E080, E058, E214]. Confidence is low to moderate, because the same kind of model under-predicted Q2 2026 [E446].

## The model: scenarios for 2026-2028

This section sets out the scenario model behind the answers. It was built by one research agent and then cleaned and checked against later research waves. Everything in it is *Our calc*: a transparent way to combine the evidence, not a forecast with a track record. Its most important caveat is that a similar model under-predicted Q2 2026 HT consumables (+1% predicted quarter on quarter, +6.8% actual) [E446].

### How the model works

In plain words: clinical HT revenue equals the clinical Gb sold times an average price per Gb, and the average price falls as more Gb moves from the expensive 6000 to the cheap X and as the X itself gets cheaper. Clinical consumables for smaller sequencers (non-HT, such as the NextSeq) are added separately.

**A walk-through, step by step.** *Our calc.* The model uses made-up "price units" rather than dollars, because only the ratios matter.

1. **Price an X Gb at 1 unit.** On Illumina's revenue shares, a 6000 Gb then earns about 3.39 units (the 3.4x premium). [E001, E447]
2. **Work out the average price today.** In 2026, about 79 of every 100 clinical HT Gb run on the X (the year average of the Q1 and Q2 2026 prints) and 21 on the 6000. The average Gb therefore earns 0.79 × 1 + 0.21 × 3.39 = 1.5019 units, the 2026 starting point that every later year is compared with. [E186, E187, E010]
3. **Move a year forward.** In the base case for 2027, the X's share rises to 87%, and the X's own price falls 14.5%, to 0.855 units (a 5% routine price decline, plus a 20% 35B cut applied to half of X volume: 0.95 × 0.90 = 0.855). The average Gb now earns 0.87 × 0.855 + 0.13 × 3.39 = 1.1846 units. [E058, E247]
4. **Compare the averages.** 1.1846 ÷ 1.5019 is about 0.79, so the average price per clinical Gb falls about 21% in a year, from mix (more Gb on the cheap X) and repricing (the X itself getting cheaper) together. [E186, E058, E247]
5. **Add volume.** Clinical HT Gb is indexed to 1.00 at the Q2 2026 run-rate and grown at each scenario's rate, anchored on trailing growth and management's claim. If it grows 30%, revenue is 1.30 × 0.79, about 1.025 times 2026, or +2.5%: a 21% fall in average price almost cancels a 30% rise in volume. [E205, E266]

**The same steps as one formula.** Clinical HT revenue index = Gb index × [X share × X price + (1 − X share) × 3.39] ÷ 1.5019. [E187]

### Calibration: the dollar anchors

The table lists the inputs that tie the index to dollars. The takeaway is that two of the most important inputs, the clinical share of HT Gb and the clinical share of consumables, are our derivations rather than disclosed figures.

| Input | Value | Source and status |
|---|---|---|
| Q2 2026 HT consumables revenue | $535M (X $316M, 6000 $219M) | Our calc from shares, 69% HT assumed [E040] |
| X share of HT revenue / Gb | 59% / 83% | Fact, Q2 2026 deck [E001] |
| 6000 vs X revenue per Gb | 3.39x (band 3.2–3.6x) | Our calc [E447] |
| Clinical share of HT Gb | ~64% (tested 55–75%) | Our calc [E009] |
| Clinical X volume / revenue share | 78% / ~51% | Fact / our calc [E186, E187] |
| Clinical 6000 revenue | ~$182M a quarter (~$728M a year) | Our calc [E187] |
| FY25 sequencing consumables | $2,939M | Fact [E050] |
| Clinical share of FY26 consumables | ~70%, i.e. ~$2.17B of ~$3.10B | Our assumption; management says ">65%", which on the Q2 2026 quarter gives ~$504M (the base for the "36%" figure; see Sizing) [E076, E080] |
| Clinical HT share of clinical | ~69% (HT ~$1.50B, non-HT ~$0.67B) | Our assumption, equal to the 69% HT share of all sequencing consumables [E003] |

One unresolved cross-check: the model's FY26 clinical 6000 revenue (~$710M) plus research 6000 revenue at the Q2 run-rate (~$172M) comes to slightly more than the $0.76–0.83B the FY26 pull-through guide implies for all 6000 revenue. The gap is about $50–100M and probably means the guide assumes faster H2 decline than the model's year-average mix [E245].

### Scenario assumptions

The next table shows what each scenario assumes. The takeaway is that the scenarios differ most in Gb growth and in how much of the X base the 35B cut reaches; the conversion paths are fairly similar.

| Parameter | Bear | Base | Bull | Anchor |
|---|---|---|---|---|
| Clinical Gb growth, 2027 / 2028 | +15% / +12% | +30% / +26% | +40% / +32% | Trailing +35–50% [E205]; management ">30%" [E266]; survey +14.6% / +19.1% [E067] |
| Year-average clinical X share, 2026 / 2027 / 2028 | 79 / 89 / 94% | 79 / 87 / 93% | 79 / 84 / 88% | 80–85% by end-2026 [E342]; ~20% sticky [E012] |
| X price index, 2027 | 0.792 | 0.855 | 0.92 | Residual −10% / −5% / −3% plus a −20% 35B on 60% / 50% / 25% of X Gb [E058, E247] |
| X price index, 2028 | 0.729 | 0.812 | 0.894 | Further −8% / −5% / −3% |
| Clinical non-HT growth | +5% | +8% | +12% | Assumption |
| 2026 clinical growth | +13% | +15% | +17% | Guide mid-teens; H1 ~17% [E074] |

### Results

All results are *Our calc* on the inputs above [E001, E187, E205, E247, E067, E074]. The first results table shows clinical HT revenue as an index (2026 = 1.00). The takeaway is that the spread between bear and bull is very wide by 2028, which reflects genuine uncertainty about Gb growth and the 35B.

| Clinical HT revenue index | 2027 | 2028 |
|---|---|---|
| Bear | 0.825 | 0.762 |
| Base | 1.025 | 1.082 |
| Bull | 1.227 | 1.469 |

The second table converts the index to total clinical sequencing consumables, adding non-HT. The takeaway is a base case of low-to-mid single-digit growth in 2027–28, sharply down from about 15% in 2026.

| Case | 2027 ($M, y/y) | 2028 ($M, y/y) |
|---|---|---|
| Bear | 1,942 (−10.5%) | 1,882 (−3.1%) |
| Base | 2,262 (+4.2%) | 2,406 (+6.4%) |
| Bull | 2,591 (+19.4%) | 3,043 (+17.4%) |
| Weighted 25/50/25 | +4.3% | +6.8% |

The third table adds research and other consumables (assumed −4% / −2% / 0% in 2027 and −2% / 0% / +2% in 2028 for bear / base / bull) and compares the total with Bloomberg consensus. The takeaway is that consensus sits between our base and bull cases, nearer the bull; even if trailing Gb growth of about 40% persisted, our base price path gives total growth of only about +6% in 2027.

| Total sequencing consumables | 2027 | 2028 |
|---|---|---|
| Bear | −8.6% | −2.8% |
| Base | +2.3% | +4.6% |
| Bull | +13.6% | +13.3% |
| Weighted | +2.4% | +4.9% |
| Base price path with Gb +40% | about +6% | not run |
| Bloomberg consensus | +8.8% ($3,378M) | +9.4% (~$3,694M) |

**How consensus compares, step by step.** *Our calc.*

- **What consensus implies for clinical.** Consensus total growth of +8.8% in 2027, with research (about a third of the total) flat to slightly down, implies clinical consumables growth of roughly 13–14% a year. [E080, E076]
- **Where that sits.** That is about 9–10 points above our base case (+4%) and about 5–6 points below our bull case (+19%), so consensus is closer to the bull. [E080]
- **What consensus needs in volume.** Under our base-case price and mix, 13–14% clinical growth needs clinical Gb growth of about +47% in 2027 and +38% in 2028, slightly above the trailing ~42%. Under bull-case price and mix (a narrow 35B and slower conversion) it needs +32% in 2027. In other words, consensus assumes either that trailing volume growth continues undiminished or that the 35B is narrow. [E080, E205]
- **An independent check agrees.** A separate hand calculation by another research agent also lands well below consensus (FY27 sequencing consumables about $2.86–2.97B, against $3,378M). [E445]
- **Why we hold this loosely.** Both checks may be too bearish, given the Q2 back-test miss, and management has given no 2027 clinical guide, only "high single digit" total revenue growth outside China. [E446, E102]

### Excess revenue unwound

The next table shows how much of the ~$500M of "excess" clinical revenue (6000 Gb priced above X rates) has been lost by the end of each year as the tail converts, at constant 2026 Gb. The figures are cumulative. The takeaway is that the base case unwinds about $190M in 2027 and a further $145M in 2028, roughly $150–190M a year, or 7–9% of FY26 clinical consumables (about $2.17B) that volume growth must cover before any new price cut. How this "flow" figure relates to the other flow figures in this addendum (the guidance-implied $40M a quarter and the revenue-at-risk bridge's ~$165M) is reconciled in one table under "Sizing" in Question 1. [E187, E342, E012]

| Case | Share of 2026 clinical 6000 Gb converted (2027 / 2028) | Excess revenue unwound, cumulative (2027 / 2028) |
|---|---|---|
| Bear | 48% / 71% | ~$240M / ~$356M |
| Base | 38% / 67% | ~$190M / ~$336M |
| Bull | 24% / 43% | ~$120M / ~$215M |

### Sensitivity tables

**Sensitivity 1: 2027 clinical HT revenue growth by Gb growth and X price change.** This assumes the clinical X share moves from 79% to 87%. Read down a column to see how much Gb growth is needed at a given X price path. The takeaway: at the base X price path (−14.5%), clinical needs about +27% Gb just to stay flat, and +40% gives about +10%. [E187, E247]

| Clinical Gb growth | X price 0% | −8% | −14.5% (base) | −21% |
|---|---|---|---|---|
| +15% | +0.4% | −5.0% | −9.3% | −13.6% |
| +25% | +9.1% | +3.3% | −1.4% | −6.1% |
| +30% | +13.5% | +7.4% | +2.5% | −2.4% |
| +35% | +17.8% | +11.6% | +6.5% | +1.4% |
| +40% | +22.2% | +15.7% | +10.4% | +5.1% |
| +50% | +30.9% | +24.0% | +18.3% | +12.7% |

**Sensitivity 2: one year of conversion (79% to 87% X), X price flat, by the 6000/X price ratio.** The takeaway: the exact ratio matters less than Gb growth. Moving from 3.39x to 5x costs about 5 points of growth, while the rounding band (3.2–3.6x) moves growth by under 1 point. [E447, E204]

| Gb growth | Ratio 2.5x | 3.39x | 4x | 5x |
|---|---|---|---|---|
| +15% | +4.5% | +0.4% | −1.9% | −5.0% |
| +25% | +13.6% | +9.1% | +6.6% | +3.3% |
| +35% | +22.7% | +17.8% | +15.1% | +11.5% |
| +45% | +31.8% | +26.5% | +23.7% | +19.8% |
| Break-even Gb | +10% | +14.6% | +17.3% | +21% |

**Sensitivity 3: net growth from a single blended price decline.** Net growth = (1 + Gb growth) × (1 − price decline) − 1. The takeaway: management's own model (Gb +25–30%, price −15%) nets only about +6–10%, before the separate drag from the 6000 tail [E047].

| Gb growth | Price −10% | −15% | −20% | −25% |
|---|---|---|---|---|
| +20% | +8% | +2% | −4% | −10% |
| +30% | +17% | +10.5% | +4% | −2.5% |
| +40% | +26% | +19% | +12% | +5% |

### What would change the answer most

The ranking below (*Our calc*) orders the unknowns by their effect on 2027 base clinical consumables (about $2.26B). The takeaway is that the 35B and 2027 Gb growth dominate; everything else is second order.

1. **The 35B's scope and size.** Whether the −20% applies to all X volume or only to new or 25B-flow-cell volume is worth about $107M of clinical HT revenue (about 5% of clinical) in the model. The three-layer price-stack calculation puts it at $63M, $127M or $253M of total consumables at 25%, 50% or 100% adoption [E058, E247].
2. **Clinical Gb growth in 2027.** Each ±5 points is worth about ±$59M of clinical HT revenue. The gap between the original bottom-up +23% and the trailing +42% is worth about $250M [E083, E205].
3. **The pace of clinical conversion.** Each point of Gb moved costs about $24M at constant Gb and about $31–33M at 2027 volumes [E413].
4. **Whether management's mid-teens price model already includes the 35B.** If it does, our 35B layer double-counts; if not, mid-teens understates the headwind [E338, E305].
5. **The true price ratio on consumed Gb.** The share data are on shipped Gb; a 5x consumed-Gb ratio would cost about 5 points a year [E204].
6. **The clinical share of HT Gb.** Moving it across 55–75% changes clinical 6000 dollars from about $144M to $196M a quarter, about ±15% on the excess estimate [E009].
7. **The Q3 2026 numbers (29 Oct).** 6000 revenue against $219M, X pull-through against $1.21–1.24M, ex-China clinical growth against 13–16%, X revenue share against 60–62%, and whether the FY26 pull-through guides survive [E270, E450].

### What the model cannot know

The corpus contains no net price per Gb by platform, no disclosed clinical share of HT Gb, no 35B price or scope, no count of labs running both platforms, no 6000 or X installed base after Q4 2025, no 2027–28 clinical guide, and no sell-side model with a 6000 line or a price-per-Gb path [E020, E411]. The model also holds the 6000's price per Gb flat even though 6000 list prices fell 16–24% on core-facility cards, so any further 6000 repricing would add to the downside [E053]. Finally, it cannot test elasticity: no disclosed data show whether price cuts raise Gb, and the one cohort Illumina disclosed is biased toward expanding customers [E027, E303].

## Management conduct and credibility

**The short answer.** Illumina's accounts look clean, but its disclosure about the 6000-to-X transition does not. The audit opinion is clean, internal controls are rated effective, nothing has been restated, and the SEC has never questioned Illumina's metrics [E373, E381, E380]. The problem for this thesis is a pattern, in our judgement, of giving transition numbers when they look good and blurring or dropping them when they do not. On the two earnings-call questions closest to the over-earning thesis, management also gave no numbers [E014, E209, E338].

Three other points round out the picture. First, guidance is habitually set low and then beaten on EPS [E141, E143]. Second, director Keith Meister's large share sales are mostly a governance-optics issue. The exception is that he was buying into GeneDx, a big Illumina customer, at the same time [E150, E196]. Third, no executive has sold shares in the open market.

**How this section is organized.** Items are grouped from most to least material. Each carries the evidence label plus two ratings that are *our opinion*: **severity** (how serious the conduct is in itself) and **relevance** (how much it bears on the clinical-consumables thesis). The first three groups matter for the thesis. The last two groups are listed briefly for completeness.

### Metrics, definitions and disclosure (most material)

1. **The volume share is Gb shipped, and only the slide title says so.** *Fact:* Every transition slide is titled "NovaSeq X % of HT Gb Shipped", which is flow-cell capacity sold. The ">30%" growth metric instead measures "Gb output on connected HT and MT instruments" (Q2 2026 call), and the two are never reconciled. *Our opinion:* So the 83%/59% split and the 3.4x ratio carry a definition most readers would miss. Severity medium; relevance high. [E204]

2. **The ">30%" Gb metric quietly changed scope.** *Fact:* In Q2 2025 the metric covered runs on connected high-throughput instruments; from Q3 2025 it covers "high- and mid-throughput", and it is reported only as a floor. *Mgmt:* Dhingra said "China hasn't been connected", so the metric excludes China, which the prepared scripts never state. Severity medium; relevance high. [E207]

3. **The clinical-versus-research activity split stopped.** *Fact:* Illumina reported clinical sequencing activity +15% and research −4% on the Q1 2023 call, and clinical +23% and research −1% on the Q2 2023 call, then gave only totals. Severity medium; relevance high. [E208]

4. **The activity metric was also downgraded.** *Fact:* Illumina's description of activity changed from "directionally correlated with revenue over time" (2023) to "not a predictor of near-term revenue" (Q2 2024 on). A deck footnote saying values "include pricing actions announced in Q1'25" was not found in the 2026 decks. Severity low; relevance medium. [E208]

5. **"Phase out transition metrics", then partly kept.** *Fact:* The Q4 2025 deck said "we will phase out transition-specific metrics after Q4 earnings", but the Q1 and Q2 2026 decks still gave X volume and revenue shares and the clinical volume share. What was dropped is the 40-customer cohort and any clinical-only X revenue share. Severity low; relevance high. [E138]

6. **Replacement measures were named but not given.** *Mgmt:* When the X's revenue share stalled at 55%, Thaysen said it was "a little bit dangerous to read this figure precisely" (Q1 2026 call). *Fact:* The replacement measures Dhingra named (reimbursement wins, new tests) have not been given as numbers. Severity low; relevance medium. [E138]

7. **Numbers released once they look good.** *Fact:* X pull-through was refused in August 2023 ("only once ramp-up has stabilized") and February 2024 ("the math is not relevant"). It was then given as ">$1M" in August 2024 and "$1.3M" for 2024. Severity medium; relevance medium. [E139]

8. **Other metrics were swapped or withheld.** *Fact:* Quarterly X placements were dropped in 2024 but still guided at 50–60 a quarter. Run counts became Gb in Q2 2023, and the clinical/research split is "not normally" given (earnings calls, 2023–24). Severity low; relevance medium. [E139]

9. **"Pull-through increased", with no number.** *Fact:* Q1 2026 prepared remarks said X "utilization increased year-over-year", and Q2 2026 said "pull-through increased year-over-year", the first such claim without a figure. The FY26 pull-through guide ($1.35–1.40M for the X, $600–650K for the 6000) has not been repeated since the Q4 2025 deck. *Our calc:* Our arithmetic suggests the X figure is hard to reach (Question 1, section B). Severity medium; relevance high. [E277, E276, E268]

10. **What the CFO said about "91%".** *Fact:* The CFO's closing outlook on the Q3 2025 call said "pricing headwinds easing now that 91% of high throughput volume has transitioned to X". Her own prepared remarks put 91% on research only, with the total at 78% and clinical at about 64%, and no correction appears. [E392]

11. **Why the "91%" matters.** *Our opinion:* The wrong denominator made "the headwind is fading" sound stronger than the clinical data supported. We read it as a slip rather than an intent to mislead, but it went uncorrected. Severity medium; relevance high. [E392]

12. **Charts and calls did not always match.** *Fact:* The Q4 2025 deck's ~90% line, which looked like a contradiction of the ~80% total, turned out to be research volume. The Q2 2024 starting point was "~45%" on the call but "mid-30s" on the deck (the clinical series). Severity low; relevance medium. [E157]

13. **Placement counts differ by venue.** *Fact:* Q4 2025 placements were ">100" on the call and deck but "~95" at the JPM conference. FY25 was about 260 or about 270, and Q1 2026 was "80+" or "83". Severity low; relevance low. [E156]

14. **Other small slips in placement data.** *Fact:* The clinical share of X installs was given as ~40%, ~35%, "roughly half and half" and ~40% at different times. Thaysen's "second-highest quarter" claim sits against 109 placements in Q2 2023, and at Q4 2024 the installed-base arithmetic does not add up (527 + 91 does not equal 630). Severity low; relevance low. [E156]

15. **What the filings say about pricing.** *Fact:* The Q1 2025 10-Q blamed "lower product margins, primarily due to reduced pricing". That is the only appearance; later quarters cite tariffs, impairment, mix and field service instead. In 2023 the filings had said "lower pull-through of NovaSeq 6000 consumables". [E036]

16. **A 10-K sentence lost its negative half.** *Fact:* The FY24 10-K said other HT consumables decrease "as customers transition to NovaSeq X", and that clause is gone from the FY25 10-K. The positive half ("demand for high-throughput consumables as customers transition") remains, and the tariff margin bridge was also dropped after Q4 2025. [E036, E365]

17. **What we infer from the filing changes.** *Our opinion:* Together, items 15 and 16 make the price effect less visible in the filings than it is in the share data. We cannot tell whether that was deliberate. Severity medium; relevance high. [E036, E365]

18. **The language softened while the numbers barely moved.** *Mgmt:* Thaysen went from blended consumables "still face headwinds" (Feb 2026), to the price headwind "receding" (Apr), to the 6000 "not a true headwind" (Jul). In between, Dhingra said the price effect "should keep shrinking" (JPM conference, Jan 2026), and Thaysen said there is "definitely still some pricing headwind… shouldn't be worse than '25" (TD Cowen, Mar 2026). [E344, E449]

19. **What the numbers did meanwhile.** *Fact:* Over the same months the 6000 still held 41% of HT revenue, and the X-to-6000 price ratio stayed near 0.30. *Our opinion:* So the tone improved faster than the data did. Severity low; relevance high. [E344, E449]

20. **The "ex-China" framing flatters growth a little.** *Fact:* After a January 2026 realignment into four regions, "rest of world organic" growth became the headline. Q2 2026 reported growth was +9.5%, organic +6.5% and ex-China organic +8.1%, and Bloomberg still shows the old regional basis. *Our calc:* So stripping out Greater China (which includes Taiwan and Hong Kong) adds about 1.2 points. Severity low; relevance medium. [E145, E325]

21. **Targets were restated ex-China.** *Fact:* The 2027 high-single-digit growth and 26% margin targets were restated ex-China in May 2025. Q1 2026 total organic growth was only +1.2%, while ex-China clinical was +20%, which shows how much the framing matters. Severity low; relevance medium. [E145, E325]

22. **China in dollars, and why it collapsed.** *Fact:* Greater China revenue was $308M in FY24 (7.0%) and $243M in FY25 (about 5.6%), then $52M in Q1 2026 (−28%) and $56M in Q2 2026 (−11%), figures given in the 10-Q and 10-K but not the press release. Illumina was put on China's unreliable-entity list in February 2025 and banned from exporting sequencers there from March 2025, with exports resuming "case by case" around November 2025. China's drag is now under 1 point of total growth. Severity low; relevance low. [E324, E326]

### Questions asked and answers given (material)

1. **Questions that got no number.** *Fact:* Analysts asked about 35B pricing (Stifel, Q1 2026; TD Cowen, Mar 2026), backlog dollars (Jefferies, Q1 2026), the size of cost inflation (JPM, Q1 2026), the genome share of clinical volume, and customers "waiting" for competitors (Guggenheim). None of the answers contained a number, and a 2023 Morgan Stanley question on excess HT capacity and Ultima also went unanswered. *Our opinion:* The questions most useful to this thesis are the ones not answered in figures. Severity medium; relevance high. [E158]

2. **The "freezing" question.** *Fact:* Citi asked about "pressure or freezing… on the clinical side" (Q3 2025 call). Thaysen replied that "Illumina is really the only one that's delivering across all these dimensions" and did not address freezing. *Our opinion:* The question was sidestepped. Severity low; relevance medium. [E158]

3. **The initial-price-hit question: what was asked.** *Fact:* On the Q1 2026 call Puneet Souda (Leerink) asked about the price hit at labs newly converting from the 6000, and whether it is in the guide. Thaysen called it "one question with many sub-questions" and answered on placements and research conversion. [E209, E338]

4. **The initial-price-hit question: what was answered.** *Mgmt:* Dhingra said "all of those price assumptions are already built into the guide", and Thaysen said "the price headwind is getting behind us". *Fact:* No number was given. *Our opinion:* This is the second of the two thesis questions that was deflected. Severity medium; relevance high. [E209, E338]

5. **The over-earning question.** *Fact:* The Q2 2026 exchange (Peterson of Jefferies asking about over-earning on the 6000, and an answer with no 6000 revenue, pace or customer count) is set out in Question 1, section C. *Our opinion:* It is the most direct deflection on record. Severity medium; relevance high. [E014]

6. **The Q2 2026 call tested the thesis less than usual.** *Fact:* Two questioners (Piper's David Westenberg and TD Cowen's Dan Brennan) were cut off by technical issues. No analyst asked about Roche AXELIOS (launched a month earlier), Ultima, Element, 35B pricing or the per-Gb decline. The one competition-adjacent question (Guggenheim) got "a very healthy market". Severity low; relevance medium. [E337]

### Guidance behavior (medium relevance)

1. **The 2023–2024 growth record was poor.** *Fact:* FY23 core growth guidance went from +6–9% to −3/−4% (actual −2%), and FY24 went from flat to −2/−3% (actual −2.4%). FY24 EPS guidance began only in August 2024, at $3.80–3.95 (actual $4.16). Severity medium; relevance medium. [E140]

2. **Long-term targets were abandoned and reset.** *Fact:* The 25% and 27% operating-margin targets for 2024 and 2025 were abandoned. The mid-teens growth target reaffirmed in August 2023 was replaced by January 2024 with high-single-digit growth by 2027 and a 26% margin. Severity medium; relevance medium. [E140]

3. **2025: set low, beaten on EPS.** *Fact:* FY25 EPS guidance started at $4.50–4.65 and the year finished at $4.84. FY25 revenue landed on the original midpoint ($4,343M). Severity low; relevance medium. [E141]

4. **2026: raised twice.** *Fact:* FY26 guidance rose from revenue of $4.50–4.60B and EPS of $5.05–5.20 (Feb), to $4.52–4.62B and $5.15–5.30 (Apr), to $4.60–4.64B and $5.30–5.40 (Jul), with operating margin held at 23.4–23.6%. Q1 EPS of $1.15 beat a $1.02–1.07 guide, and Q2's $1.31 beat $1.20–1.25. Severity low; relevance medium. [E141]

5. **Brokers have noticed.** *Opinion (broker):* Freedom says "we no longer consider management's outlook conservative" (2026). *Our opinion:* The beat pattern holds for EPS but not for FY24–25 revenue. Severity low; relevance medium. [E141, E327]

6. **Low-balling is a habit.** *Fact:* The initial 2026 guide used the H2 2025 average and Q3 2025 growth as its low end. Placements were guided at 50–60 a quarter and came in at 80–100, Q1 EPS was guided below consensus, and clinical was held at "double-digit to mid-teens" after two quarters of +20%. *Mgmt:* Thaysen says Illumina is "always guiding for the midpoint". Severity low; relevance medium. [E143]

7. **The placement guide was beaten, then dropped.** *Fact:* Dhingra guided "about 200 to 240" X placements for 2026 (Q4 2025 call, Feb 2026), and the guide was not repeated at any later event. Actuals were over 100 (Q4 2025), 83 (Q1 2026) and over 95 (Q2 2026), so H1 alone reached about 70–80% of the annual range. *Our opinion:* Any model still using the guide is stale. Severity low; relevance medium. [E339, E343]

8. **Forecasts that slipped within a quarter.** *Mgmt:* On 30 April management said cost mitigation was "meant to fully offset the inflation during the year". On 30 July it said "we didn't anticipate to the level we have seen", began sharing costs with customers and stockpiled inventory. The time for a new X to reach full consumables use also went from "roughly six months" to "at least six to nine months". Severity low; relevance medium. [E160]

9. **Over-promising on the X launch in 2023.** *Mgmt:* Then-CEO Francis deSouza spoke of about 750 X units "right off the bat" (Apr 2023). *Fact:* Only 352 shipped by end-2023, and the X guide fell from over 390 to 330–340. *Mgmt:* Charles Dadswell, then interim CEO, called the rollout "more challenging than anticipated", while then-CFO Joydeep Goswami said "nothing out of the ordinary". Severity low; relevance medium. [E155]

10. **The expected 6000 swap did not happen.** *Mgmt:* Management said customers "swapping two 6Ks for one X… never played out" (Nov 2023). *Fact:* Net HT instruments rose only from 2,122 to about 2,250. Severity low; relevance medium. [E155]

11. **Rivals dismissed, then taken more seriously.** *Mgmt:* Management contrasted Element's placements with its orders (2023), said of Ultima's free wafers "you don't have a business", and called 6000 win rates "range-bound". Dhingra said customers add "an 11th instrument from another vendor if they have 10 Illumina boxes". Thaysen called a competitor preview "a technology overview… not a product launch" with "no impact" (Q1 2025), then softened to "no market freezing" (Q1 2026). Severity low; relevance medium. [E137, E127]

12. **Small contradictions about pulled-forward demand.** *Mgmt:* In Q1 2024 Thaysen said "we didn't pull anything forward", while Dhingra's prepared remarks cited customers pulling X deliveries from Q2 into Q1, about a quarter of the beat. For Q4 2025, management first said "not a budget flush", then cited a "small benefit" from year-end budget buying. Severity low; relevance low. [E144]

13. **The 2027 margin target has softened.** *Mgmt:* The 26% FY27 operating-margin target is now "within 50 bps", with about 1 point of dilution from the SomaLogic acquisition in FY26 (Dhingra: "get as close to the 26% operating margin as possible in '27"). *Fact:* SomaLogic cost $350M upfront plus up to $75M of milestones and royalties, and it costs $0.18 of FY26 EPS. Severity low; relevance low. [E146]

14. **An unexplained pre-announcement gap.** *Fact:* In January 2026 Illumina pre-announced Q4 2025 EPS of $1.27–1.30 (FY $4.76–4.79). It then reported $1.35 (FY $4.84) on 5 February on the same $1.159B revenue, and the extra $0.05–0.08 was not explained. Severity low; relevance low. [E142]

### Earnings quality and accounting (lower relevance)

These items bear on the quality of reported profit rather than on clinical consumables. The two worth watching for this thesis are inventory reserves (items 6–8) and contract terms that let customers move to cheaper flow cells (item 11).

1. **Government incentives jumped in 2026.** *Fact:* Government incentives (grants that reduce costs) were $28M in H1 2026, about $20M of it in Q2, against $6M a year earlier. Grant receivables rose to $45M from $21M, and the Q1 2026 10-Q had called incentives "immaterial". Severity medium; relevance low. [E147]

2. **They explain most of the Q2 profit improvement.** *Opinion (Seeking Alpha author):* Ayers estimates that about $26M of the $31M year-on-year rise in Q2 operating income came from incentives (+$18M) and the absence of restructuring (+$8M), leaving about $5M of underlying improvement (2026). *Our calc:* Excluding incentives, H1 non-GAAP operating margin was about 0.9 points lower year on year. Severity medium; relevance low. [E147]

3. **Gains on acquisition payouts reduce overhead costs.** *Fact:* Illumina owes contingent payments on past deals. One is a contingent value right (CVR) to former GRAIL holders, paying 2.5% of GRAIL revenue up to $1B a year and 9% above, through August 2033; another is earn-outs to SomaLogic's sellers. When the estimated value of these debts falls, the gain lowers SG&A, and the gain was $32M in H1 2026 (about $14M CVR, $18M SomaLogic; $16M a quarter, after $11M in Q4 2025). Severity low; relevance low. [E148, E417]

4. **The payout accounts reconcile.** *Fact:* The liability went from $54M, plus $81M of additions, less $32M of gains and $26M paid, to $77M ($40M for the CVR, $37M for SomaLogic). Illumina paid $30M to settle SomaLogic on 27 July 2026. *Our calc:* So a further gain of about $7M may land in Q3. Severity low; relevance low. [E282, E301, E302]

5. **A donation counted as a non-GAAP adjustment.** *Fact:* The Q4 2025 non-GAAP overhead adjustment of $0.30 a share (about $46M) was $21M acquisition-related, $6M restructuring and $19M footnoted as a donation to the Illumina Foundation. *Our calc:* Excluding the donation lifted Q4 non-GAAP operating margin by about 1.6 points. *Our opinion:* That matters because non-GAAP operating margin is a pay metric. Severity medium; relevance low. [E396]

6. **Inventory is up and reserve coverage is down.** *Fact:* Like-for-like inventory rose 11.5% (from $564M to $629M) between December 2025 and June 2026. Reserves for obsolete stock fell from $133M to $123M, cutting coverage of gross inventory from 19.1% to 15.8%, with no explanation. *Our opinion:* Lower reserves while the 6000 winds down are worth watching. Severity medium; relevance medium. [E037, E372]

7. **What the inventory build is made of.** *Fact:* The build is in raw materials and work in progress, partly a memory pre-buy. Inventory days run about 147–150, against 119–131 from 2023 to mid-2024 (10-Qs and Q2 2026 call). Severity low; relevance medium. [E383, E391]

8. **The audit flags inventory for the first time.** *Fact:* EY's only critical audit matter for FY25 (the area the auditor judged hardest to audit) is excess and obsolete inventory, the first not about GRAIL. It cites "the release of new products that may supersede old ones" and manual inputs from supply-chain staff. The words "customer migration to NovaSeq X" appear in the inventory note, not the audit matter. Severity low; relevance medium. [E380]

9. **Free cash flow has missed three quarters running.** *Fact:* Free cash flow (operating cash flow less capital spending) was $267M against $412M expected (Q4 2025), $251M against $502M (Q1 2026) and $162M against $321M (Q2 2026). *Mgmt:* Management cited tax timing and inventory builds. *Fact:* H1 2026 FCF of $412M is about 109% of non-GAAP net income, against a claimed ">140% conversion" (Sep 2025), and capital spending is guided at $225M against $148M. Severity medium; relevance low. [E161]

10. **A one-quarter receivables spike, unexplained.** *Fact:* Receivables were $854M at end-2025, up $119M on revenue growth of 5%, and days sales outstanding (DSO, how long customers take to pay) rose to about 67 from about 60 before falling back to 61.5 (Q1 2026) and 60.0 (Q2 2026). The Q3-to-Q4 build was $125M, against $36–44M in prior years, and neither the 10-K nor the call explains it. *Our opinion:* It fits the Q4 cash-flow miss and December-weighted shipments. Severity medium; relevance low. [E371, E382]

11. **Contract terms that favor customers.** *Fact:* Revenue is recognized net of discounts, and contracts "may allow product substitutions as we launch new products" (10-K). *Our opinion:* That could let customers swap into a cheaper flow cell such as the 35B. Severity low; relevance medium. [E112]

12. **Contracted future revenue.** *Fact:* Remaining performance obligations (RPO, contracted revenue not yet delivered) rose from $738M (Dec 2025) to $1.1B (Q1 2026) and $1.0B (Q2 2026), about 83% due within 12 months. Contract liabilities (customer prepayments) fell to $333M from $346M (10-Qs). Severity low; relevance low. [E112]

13. **Non-GAAP adjustments are moderate and shrinking.** *Fact:* The gap between GAAP and non-GAAP operating profit was $45M in H1 2026 (9% of non-GAAP), down from $86M (19%) a year earlier, and stock-based pay is not added back, a quality positive. Restructuring charges total $261M since Q2 2023 and are now relabelled "transformational initiatives", shifting from severance to IT-system costs. Severity low; relevance low. [E148, E384]

14. **Smaller adjustment and tax notes.** *Fact:* About 0.6 points of deferred-compensation cost in Q2 2026 opex is offset in other income, and an $8M legal-contingency add-back sits in Q4 2025 ($10M for FY25, after the FY24 reversal of the $456M EU fine over GRAIL). The 2026 year-to-date tax rate was 18.4% against 25.1%, a Singapore tax holiday was worth $37M in FY25, and Bloomberg's "adjusted" operating income does not reconcile with company figures. Severity low; relevance low. [E404, E384, E405, E162]

15. **Pieces that are not broken out.** *Fact:* BioInsight revenue sits in services with "no commitment to a separate breakout", SomaLogic sits inside microarrays, and inventory with cycles over a year is now non-current ($26M). *Opinion (broker):* Multiomics is said to add 1–2 points to 2027 growth with no sizing ("no way to confirm", Barclays). Severity low; relevance low. [E162]

16. **The clean side of the ledger.** *Fact:* SEC comment letters since 2019 concern only the GRAIL merger filings, the CVR exchange offer and proxy wording, never non-GAAP measures, metrics, revenue recognition or segments. No 8-K has been filed for a restatement or an auditor change, and EY was ratified with about 95% support. An upgrade of the company-wide accounting system (ERP) going live in H1 2027 "could materially affect" internal controls (FY25 10-K). Severity none to low; relevance low. [E373, E381, E380]

17. **Legal disclosures.** *Fact:* An SEC investigation (July 2023 document request) is disclosed in the 10-Q but not on calls. A state GRAIL securities class action has a hearing on 30 Oct 2026, and Icahn's derivative suit over the GRAIL acquisition is settling with no payment (objection deadline 19 Oct, hearing 2 Nov 2026). Severity low; relevance low. [E159, E198, E230, E243]

### Insiders, pay and governance (low relevance; mostly noise for this thesis)

1. **Meister's fund sold about $591M of stock.** *Fact:* Director Keith Meister's fund, Corvex, sold about 3,059,258 shares for about $591M from 13 May to 4 Sep 2026, at about $145–231 a share, with no purchases. That cut its holding about 81%, to 770,350 shares (six Form 4 filings). Other totals in circulation ($1.13B, $593M, $586M, $436.7M, $430M, $227M) are wrong or partial. Severity medium; relevance low. [E150, E151]

2. **The sales were not pre-scheduled.** *Fact:* Every Form 4 opened has the 10b5-1 box unchecked, so the sales were not made under a pre-set plan. For contrast, Illumina itself bought back stock at about $124 on average in H1 2026 ($366M). Severity medium; relevance low. [E150, E195]

3. **Where Corvex's shares came from, and when it sold.** *Fact:* Corvex's Form 144 notices say the shares were bought in the open market from October 2023 to March 2025. The first sale came about two weeks after Q1 results and the 4 August sale five days after the Q2 call, both in open trading windows, and a cash-settled swap was also partly ended in May. Severity low; relevance low. [E165, E239, E283]

4. **The last sale preceded a big rise.** *Fact:* The last sale was on 4 September, the day S&P announced Illumina's inclusion in the S&P 500 (effective 21 Sep), and the stock later reached about $294 (5 Oct), roughly 30% higher. *Our opinion:* No source suggests Meister knew of the inclusion in advance. Severity low; relevance low. [E165, E239, E283]

5. **A customer-side conflict.** *Fact:* Through Corvex, Meister owns about 16.1% of GeneDx, a large Illumina clinical customer (13D/A, May 2026). Corvex bought about $60M of GeneDx stock on 11 and 15 May (prices from an aggregator), just as its Illumina sales began on 12–13 May. *Our opinion:* So an Illumina director is a major owner of a customer that negotiates prices with Illumina. Severity medium; relevance medium. [E196]

6. **Executives bought, and have not sold.** *Fact:* Thaysen bought 12,350 shares at $80.86 (about $1.0M) in May 2025, and Dhingra 6,100 at $81.21 (about $495K). Thaysen's direct holdings then rose from 83,390 to 107,770 (Oct 2026) through vesting, with sales only to cover tax (most recently 1,303 shares at $293.69). *Fact:* Thaysen had a $1M pre-set purchase plan in 2023, Cunningham ended a pre-set plan on 9 Feb 2026, and a "100 shares" purchase figure from one source is doubtful. Severity none; relevance low. [E152, E164]

7. **Officer sales are small and look pre-set.** *Fact:* From May to August 2026 four officers (Wedel, Ericksen, Leckman and Davies) sold 615–2,000 shares at a time ($139–200 a share), each 2–12% of their holdings. None of Thaysen, Dhingra, Goswami or Barnard sold in the open market from May to October, and the two months before Q3 show only tax withholding, grants and director fee shares. *Our opinion:* Davies sold at exactly $180.00 and $200.00, which suggests limit prices in a pre-set plan. Severity none; relevance low. [E348, E358]

8. **Pay is tied to revenue, margin, EPS and share returns, not clinical or pricing.** *Fact:* The 2026 proxy says the annual bonus uses revenue and non-GAAP operating income in dollars, funded at 77% for 2025, on a CEO target raised to 150% of salary (payout $1,155,000). Performance share units (PSUs, stock that vests only if targets are hit) granted in 2025 vest half on three-year operating margin and half on total shareholder return (TSR) relative to the Nasdaq Biotech index. The 2026 grants to the new commercial and legal chiefs use three-year non-GAAP EPS growth and relative TSR, matching a 10-Q statement that EPS-based PSUs "resumed in fiscal 2026". Severity low; relevance low. [E149, E197, E347, E441]

9. **What we could not check on pay.** *Fact:* The proxy's detailed compensation discussion (CD&A) was not read in full, and one bonus table from a search summary did not reconcile and was not used. Executives received no stock or variable pay in 2023. Severity low; relevance low. [E149, E441]

10. **CEO pay versus returns.** *Fact:* Thaysen's reported pay was $11,018,895 (2025), $14,802,924 (2024) and $4,691,233 (2023), with "compensation actually paid" of $12,832,816, $17,689,413 and $4,439,576, and a CEO pay ratio of 97:1. The company-selected measure is revenue ($4,343M against $4,332M), and Illumina's TSR index stands at 36.47 against 122.07 for the Nasdaq Biotech index. *Our opinion:* Pay has risen while shareholder returns lagged. Severity low; relevance low. [E220]

11. **Shareholders back the board; the board has turned over.** *Fact:* Say-on-pay passed with about 91% (2025) and 93.5% (2026), and one director drew 13.7M votes against in 2025 and retired in 2026. Board changes since March 2025 include Stephen MacMillan's resignation, Meister joining, Scott Gottlieb becoming chair, three retirements in May 2026, and David King and Daniel Skovronsky joining (ten directors), each with no disagreement disclosed. Severity low; relevance low. [E221, E222]

12. **Large long-only holders.** *Fact:* Fidelity (FMR) reports 16,169,439 shares (10.7%, as of 30 Sep 2026), Capital World Investors 15,776,452 (10.3%, as of 31 Mar 2026) and Vanguard Capital Management 7,939,213 (5.19%), all on 13G filings. No activist 13D was found. Severity none; relevance low. [E229, E240]

13. **Leadership churn at the top.** *Fact:* Since 2023 Illumina has changed CEO (deSouza to Dadswell to Thaysen), CFO (Goswami to Dhingra, Apr 2024), CTO, CMO, head of investor relations and chair (8-Ks). Severity medium; relevance medium. [E153, E328]

14. **Three commercial chiefs in about 30 months.** *Fact:* Susan Tousi left in January 2024 for Delfi Diagnostics, Cunningham left in January 2026 after about 19 months, and Mike Sullivan, formerly Caris's commercial chief, started on 20 July 2026. *Our opinion:* Sullivan's Caris link matters because Caris is the clearest switching candidate among large customers. Severity medium; relevance medium. [E153, E328]

15. **CFO and legal-chief exits.** *Fact:* CFO Goswami left on 15 April 2024 with a $360,000 advisory payment and no disagreement on "operations or financial reporting", and Dhingra received a $650K salary, a $500K sign-on bonus and a $3.5M equity grant. General counsel Dadswell left in a "mutually agreed separation" on 3 October 2024 ($600,000 advisory payment plus $620,000 severance), and Julie Coletti became chief legal officer on 3 August 2026 after a 22-month interim. Severity low; relevance low. [E241, E385]

16. **Thin disclosure of new officers.** *Fact:* No 8-K was filed for the new commercial chief (Sullivan) or legal chief (Coletti); both appear only in Form 3 and Form 4 insider filings. *Our opinion:* That is not a rule breach if they are not among the top named executives, but it is thin disclosure for a commercial chief arriving from Caris. Severity low; relevance low. [E254]

17. **Employee sentiment.** *Opinion (former employees, hearsay):* Former employees describe a "Danish management team" with little sequencing-market experience, "lifers", talent loss and rumored layoffs. *Fact:* Glassdoor and Blind both rate Illumina 3.4 out of 5, and an employee post says "no more RSUs [restricted stock units] for director level and below". Severity low; relevance low. [E163]

18. **Buyback intentions reversed quickly.** *Fact:* Filings said "We do not intend to make any share repurchases during fiscal year 2024", yet a $1.5B buyback was authorized in August 2024. Illumina bought $742M in FY25 (average about $95) and $366M in H1 2026 (about $124), and a new $1.5B program was authorized on 28 April 2026 but used for only 32K shares in Q2. A $500M note matured on 9 Sep 2026, and a $300M 2029 note was issued in August. Severity low; relevance low. [E154]

19. **Suing a customer.** *Fact:* Illumina sued BillionToOne, one of its own prenatal-testing consumables customers, in Delaware on 7 May 2026 over three patents on fetal-DNA analysis; the accused product is the UNITY prenatal test, not a sequencer. *Our opinion:* It shows Illumina is willing to use patents against customers in a segment where price-motivated labs have already moved. Severity low; relevance medium. [E226]

## Read-through from clinical customers

**What the customers tell us.** Three messages come through. First, the big clinical labs are growing test volumes fast, but their cost per test is mostly not falling, so savings are going into deeper testing (Question 2, sections B and E). Second, their contracts with Illumina give them flexibility and price protection, not lock-in: they can generally leave on 90 days' notice, have no dollar purchase minimums, and in several cases have clauses under which the price per Gb can only fall. Third, what actually holds them to Illumina is the cost and time of revalidating tests, which is high for FDA-approved tests and lower for lab-developed ones (Question 1, section D). No large US clinical customer we checked has a verified production test on a rival short-read sequencer.

Most contract evidence below comes from supply agreements filed as exhibits to customers' SEC filings, including S-1s (the registration statement a company files before listing its shares). Several key clauses are redacted.

### Natera (prenatal, transplant and MRD testing; Illumina's largest visible clinical account)

1. **Validated only on Illumina.** *Fact.* Natera's FY25 10-K says its tests are "only validated to perform on Illumina's sequencing platform" and names Illumina the sole supplier for Panorama, Horizon, Signatera and Prospera. The August 2033 end date is attributed to the 10-K narrative, which we did not read directly. [E109]

2. **A most-favored-customer clause.** *Fact.* The Eighth Amendment (effective 31 Dec 2023) gives Natera "Volume-Based Net Prices that are no less favorable than... provided to an Equivalent customer or to GRAIL" (Natera SEC exhibit). This is a most-favored-nation (MFN) clause: Natera automatically gets any better price Illumina gives a comparable customer. [E192]

3. **Redacted discounts, and the MFN may be superseded.** *Fact.* The same amendment has a 20-tier discount table keyed to annual spend, a five-tier NIPT credit and a capped R&D discount, all redacted. The Eleventh Amendment (2026) replaced the price definition and contains no "most favored" wording, so whether the clause survives is unverified. [E192]

4. **A discount ladder and re-opener for genome-based MRD.** *Fact.* The Tenth Amendment (January 2025) adds a seven-tier spend-based discount table for whole-genome MRD consumables, "to accommodate Natera's anticipated increased demand", and lets either party reopen the discounts "if market conditions for MRD Tests materially change". So Natera's price per Gb on its most data-heavy growth product falls with scale. [E193]

5. **A limited tariff pass-through.** *Fact:* The Eleventh Amendment (2 Mar 2026) lets Illumina pass through tariffs above a redacted threshold, non-retroactively, 30 days after it starts paying them, with refunds shared. At signing the relevant tariff was the 10% "Section 122 duty", a temporary across-the-board US import tariff the president can impose under the 1974 Trade Act. [E194]

6. **A price freeze, extended to all MRD.** *Fact:* The same amendment says the inflation-adjusted net price "shall not increase further" except for material cost increases outside Illumina's control, and extends discount tiers to both exome- and genome-based MRD, with monthly reporting. *Our opinion:* This limits Illumina's ability to pass memory and freight inflation to its largest clinical account. [E194]

7. **A ceiling, not a floor, on price per Gb for new products.** *Fact:* Section 7(l) of the Eleventh Amendment requires new product versions to keep a comparable "inflation-adjusted... price per gigabase of sequencing", and section 7(k) bars further inflation-adjusted price increases. *Our opinion:* So a new flow cell such as the 35B cannot raise Natera's price per Gb, and no clause protects Illumina's revenue per Gb. [E212]

8. **No dollar commitment to Illumina.** *Fact:* Natera's FY25 commitments total $256.9M, including $107.3M to material suppliers ($89.3M in 2026, only $7.3M in 2027) and $18.9M to an instrument supplier, none named as Illumina (Natera FY25 10-K). *Our calc:* Material commitments are about 13% of product cost, so long-dated Illumina volume is not locked in. [E227]

9. **A redacted quarterly minimum.** *Fact:* The Eleventh Amendment keeps a quarterly minimum purchase, but its amount is redacted. [E227]

10. **A short rolling take-or-pay.** *Fact:* The original 2013 supply agreement (amended 2014), refiled with Natera's Q2 2026 10-Q for an unstated reason, makes "the 4th calendar month of each Forecast" a binding take-or-pay commitment within ±25%. That means Natera must pay for that month's forecast quantity whether or not it uses it, a short-horizon commitment rather than a dollar minimum. [E258]

11. **Building "the largest sequencing capacity in the world".** *Mgmt (customer).* Natera announced a dedicated sequencing facility in Austin with up to 400 jobs, tied to oncology volume growth of +54% in Q1 2026, and described it in those words (Natera press release, 21 May 2026). No sequencer count or model was given. [E401]

### Guardant Health (liquid-biopsy cancer tests and Shield screening)

Guardant's test volumes, its move to the X and the FDA question are in Question 1, section D, and Question 2, sections B and E.

1. **A long contract it can leave at any time.** *Fact.* Guardant's Illumina agreement runs to about January 2033 and then renews yearly. The main exhibit (Amendment 5, December 2020) shows no minimum purchase, no exclusivity and no tariff clause; pricing is a tiered discount off "then-current list price". Guardant may terminate "for convenience upon 90 days' prior written notice" without liability, while Illumina may not; the August 2023 settlement 8-K mentions only "a new long-term purchase and supply commitment". [E110, E228]

2. **The barrier is qualification, not contract terms.** *Fact.* Guardant's 10-K speaks of a "limited number of vendors", says a switch "would require qualification to transition to a different vendor", and describes a "multi-month, multi-lot safety stock strategy". It discloses no dollar commitments to Illumina. [E110]

### Caris Life Sciences (tissue and blood tumor profiling)

Caris's FDA-approved test, cost trends and volume growth are in Question 1, section D, and Question 2, sections B and E.

1. **The GRAIL "Open Offer" contract.** *Fact.* To win approval for its GRAIL acquisition, Illumina offered oncology-test customers a standard contract (the "Open Offer"). Caris's version runs 12 years from the GRAIL deal closing (August 2021) to August 2033, which is why Natera and Caris share that end date (Caris S-1 exhibit). [E232]

2. **Its terms favor the customer.** *Fact.* Caris may terminate on 90 days' notice without liability, there are no purchase commitments, pricing must be no less favorable than GRAIL's, and the inflation-adjusted price "shall not increase" except for material cost increases outside Illumina's control (Caris S-1 exhibit). [E232]

3. **A promised 43% cut in price per Gb.** *Fact:* The Open Offer requires the highest-throughput flow cell to be "at least 43% lower than the comparable cost per gigabase today" by 2025, measured against the inflation-adjusted NovaSeq S4 price. *Our calc (weak source for the baseline):* With a baseline of about $4 per Gb at the top tier (March 2021, from one fetch summary), the target is about $2.30 per Gb before inflation. [E249, E255]

4. **No sign the promise was checked.** *Fact.* No document shows the 43% commitment was measured or met, and no remedy for a miss was found. Illumina's test-terms web page also promises no price increases on covered products. [E249, E255]

5. **Better prices elsewhere become refunds.** *Fact.* If Illumina offers better pricing to an "Equivalent customer" (or, in Natera's Eighth Amendment, to GRAIL), it "will refund to Customer the difference… multiplied by the number of affected units". A lower price for any comparable customer therefore becomes a cash liability on units already bought. [E256]

6. **Caris is weighing rivals.** *Mgmt (customer):* Caris said "there are two competitors out there now against the longstanding sequencing supplier", with higher throughput and lower cost, which "create the opportunity to increase our capacity and decrease our cost of goods simultaneously" (Caris Q2 2026 call). [E199]

7. **And is about to triple capacity.** *Mgmt (customer):* Caris said current capacity supports about $1B of revenue "and we're just about to triple that", naming no platform or timeline (Caris Q2 2026 call). *Our opinion:* The question for Illumina is whether the added capacity is dual-sourced. [E199]

8. **A large, Illumina-based fleet.** *Fact.* Caris reported running "over 50" NovaSeq systems and "over one trillion reads per day" across four labs as of 31 March 2025 (S-1/A), the only hard instrument count we found for a clinical lab. [E400]

### GRAIL (Galleri multi-cancer screening; spun out of Illumina)

1. **A possible renewal deadline right after Q3.** *Fact (weak source; not confirmed in the agreement itself):* A search summary of GRAIL's FY25 10-K says its Illumina supply agreement "is scheduled to expire on February 28, 2027" and renews for two-year terms unless either side gives notice at least 120 days before, i.e. by about 31 Oct 2026, two days after Illumina's Q3 print. *Fact:* Illumina is GRAIL's sole supplier of sequencers, certain reagents and service. [E257]

2. **Royalties to Illumina resume in Q4 2026.** *Fact:* GRAIL pays Illumina a royalty on Galleri sales, suspended by a June 2024 amendment until 24 Dec 2026; after that the rate is 9%, falling to 7% with offsets and to 5% once $1B has been paid. *Our calc:* At about 7% of roughly $698 revenue per test, that is about $49 a test, or about $9M a year at FY25 volume, and royalties are not consumables revenue. [E257, E362]

3. **GRAIL's contract lacks the Open Offer protections.** *Fact.* GRAIL's own supply agreement prices at "Illumina's then current List Price… subject to the discount table", and "List Prices may increase or decrease during the Term in Illumina's sole discretion". Part of each monthly forecast is binding, and Illumina's investment exclusivity was tied to GRAIL using only Illumina sequencers (partial reading of a truncated file). *Our opinion:* This contrasts with the Natera and Caris clauses, where price can only fall. [E292]

4. **No take-or-pay on consumables at GRAIL.** *Fact.* GRAIL's FY25 commitments total $52.8M (mostly web services and lab supplies), and its Illumina-related minimums are "minimum annual royalty payments which are cancellable" (GRAIL FY25 10-K). Illumina has not been a GRAIL related party since Q4 2025. [E279, E286]

5. **Or anywhere else we checked.** *Our calc.* Across all customers checked, hard commitments that could be Illumina purchases total at most about $53M, under 5% of about $1.9B of clinical consumables. So clinical revenue is protected by switching costs, not contract dollars. [E279, E286]

6. **A possible 2027 change in contract terms.** *Opinion (unverified).* The Open Offer was extended to customers developing oncology tests "for six years from closing" (GRAIL Form 10), which one research agent reads as closing about August 2027; Illumina's terms page gives a March 2021 start and no expiry. If the window closes, new oncology customers might not get the MFN and price-freeze protections. [E233]

7. **Open Offer terms move with the platform.** *Mgmt.* Thaysen said multi-year arrangements are "not instrument specific and continue with the X" (Q3 2024 call). Illumina discloses no contract terms, volumes, price schedules or customer counts. [E111]

### Tempus, GeneDx, Exact, Fulgent and other labs

1. **Tempus: a large share of its spend goes to one supplier.** *Fact.* Tempus's FY25 10-K says one sole supplier "for certain laboratory materials, equipment and services" took about 33% of vendor payments in 2025, 39% in 2024 and 33% in 2023. The note does not name Illumina, and a $15.9M payable to Illumina appears only in search summaries (*weak source*), so the attribution is unverified. [E213]

2. **Tempus: no contract lock-in.** *Fact.* Its 2021 Illumina agreement (S-1 exhibit) runs 12 years, lets Tempus terminate "at any time and for any reason without termination liability upon ninety (90) days' prior written notice", states no minimum purchase and redacts the pricing tiers. Later amendments are unknown. [E284]

3. **GeneDx: a rising, then falling, top-supplier share.** *Fact.* GeneDx's FY25 10-K says one unnamed supplier accounted for about 20%, 13% and 11% of purchases in 2025, 2024 and 2023, and names Illumina among five possible suppliers. GeneDx manages the risk with surplus stock and says "alternative suppliers are available for some or all of these reagents". The Q2 2026 share fell to about 14% (Question 2, section E). [E216, E285]

4. **Exact Sciences (now part of Abbott) has an alternative.** *Fact (stale, secondhand reading of FY2023-era 10-Ks):* Exact bought from Illumina on purchase orders with no long-term supply agreement, with its OncoExTra test validated only on Illumina, but it signed a "long-term supply agreement" with Ultima as an investor in June 2022 and joined its early-access program. *Fact:* Abbott closed its roughly $21B purchase of Exact on 23 March 2026, so Exact no longer reports separately. *Our opinion:* Its main test, Cologuard, is not Gb-heavy, so the volume at stake is modest. [E177, E281]

5. **Fulgent says it could switch.** *Fact.* Fulgent's FY25 10-K calls Illumina the "sole supplier of the next generation sequencers and associated reagents" but adds "there are several sequencer suppliers that we believe could replace Illumina". It is the only second-tier lab wording that asserts a credible switch, though no platform is named. [E398]

6. **Illumina played down large labs' rival work.** *Mgmt:* Asked in August 2024 whether Quest and Labcorp had expanded collaborations with a competitor, Thaysen called it "a little bit over rotation… a very limited application space". [E114]

7. **Large labs have opened doors to Ultima.** *Fact:* Labcorp works with Ultima on whole-genome MRD, with validation data showing specificity over 99.9% (fewer than 1 in 1,000 cancer-free samples wrongly flagged) and detection of tumor DNA below 3 parts per million (AACR conference, 2026). Quest has Ultima-based Haystack MRD, Myriad bought an Ultima UG 100, and NeoGenomics works with Ultima. *Our opinion:* All are development-stage, with no volumes disclosed, so they are options rather than lost volume. [E114]

8. **Who has the incentive and the ability to switch.** *Opinion (our research agents):* Caris has very high incentive and moderate ability, and Foundation (owned by Roche) has the highest incentive and high ability, already using Roche prototypes and planning AXELIOS at European service sites. Tempus and GeneDx have high incentive; Adaptive less, having just captured the X saving; and Natera and Guardant face high barriers ("barriers to bypass… very, very high", per an expert). [E115]

9. **A UK route to switching.** *Opinion (competitor employee, hearsay):* A Roche precision-medicine lead said NHS technology-transfer deals require the partner's sequencer, so if Natera, Guardant or Foundation validated a non-Illumina platform, the transfer labs would follow. The same source said these labs "are talking to Ultima and… the Roche sequencer", but works for Roche. [E117]

10. **The court found no proof of lock-in.** *Fact:* A federal judge dismissed Element's antitrust claims against Illumina on 28 May 2026, with leave to amend: exclusive dealing failed because Element alleged no "specific provisions that locked customers", and predatory pricing failed for lack of cost data (the only discount figure was Element's unproven "50%+" bundled-discount allegation). Element filed an amended complaint, and Illumina replied on 23 July 2026. *Our opinion:* The case remains a risk to commitment-based discounting, but so far the record says clinical customers are free to dual-source. [E120, E202]

11. **A partner's allegations.** *Opinion (biased source).* A former field application scientist at SOPHiA (an Element partner) alleged that Illumina will not support TruSight Oncology validation on Element, raises prices "out of nowhere" for third-party panel users, offers perks to key opinion leaders, and that "some population-genome projects are secretly validating Ultima". These are uncorroborated, and four channel checks reported no price change in 90 days. [E121]

## Read-through from competitors

**What competitors tell us.** Rivals are pushing the price of sequencing down across the industry, and Roche is the most credible new clinical threat. But in October 2026 none of them has a verified production clinical test at a major US lab on a short-read platform. Their direct threat to the 6000 tail is therefore small for now. Their bigger effect is indirect: they cap what Illumina can charge on the 35B and on new tests, and every challenger's own results show volume growing faster than revenue.

### Roche (AXELIOS, launched June 2026)

1. **The launch price.** *Fact.* Roche launched AXELIOS on 29 June 2026 for research use only (RUO, meaning not yet cleared for patient testing), at $150 list per genome and $0.06 per million reads, with an instrument of about $750K. That list price is about 25% below Illumina's roughly $200 genome list, so it caps what Illumina can charge with the 35B. [E123]

2. **The machine's capacity.** *Fact.* AXELIOS produces 1.8 terabases in 4 hours (about 16 genomes) or 64 genomes per two-day run, and its sensor can be reused about 20 times (Roche launch materials, Jun 2026). [E123]

3. **Early placements.** *Mgmt (competitor):* Roche's first-year goal is about 100 placements, about a third were placed within 60–80 days ("external customers only"), and Roche keeps its ambition of over CHF 1bn in sales (Roche CEO, 8 Sep 2026; Barclays, 28 Sep). *Opinion (broker):* For comparison, JPM notes Illumina shipped 352 X units in the X's first year, PacBio 173 Revios and Element 112 AVITIs, so Roche's pace is in line with past launches, not faster. [E123, E124]

4. **Early adopters are mostly research and service labs.** *Fact:* Named early users are Foundation Medicine, Hartwig, Broad Clinical Labs, CNAG, the Sanger Institute, 10x, Freenome (only "evaluating"), SAGA, Macrogen (the first in Asia, 30 Jun 2026) and Centogene (rare-disease work, labelled research). [E124, E218, E253]

5. **Foundation is the one with captive clinical volume.** *Fact:* Foundation, owned by Roche, has run more than 1.5M cancer profiling tests and plans AXELIOS for whole-genome tumor baselines in its Pathlight MRD test and at EU service sites. *Our opinion:* That makes it the most likely first large clinical switch. [E124, E218]

6. **Roche's pricing pitch: no volume discounts.** *Mgmt (competitor).* Roche says there is "no volume-based discounting. Everyone can achieve this pricing", and that "mid-throughput users can actually access the same economics as high-throughput users" (Investor Day, May 2026). It quotes about $25 per sample for a 1.1 Mb (megabase, a million DNA letters) liquid-biopsy panel. [E068]

7. **Roche's headline prices are not like-for-like.** *Fact:* The $150 genome uses duplex reads (both DNA strands) at 30x, while the $0.06 per million reads is for simplex (single-strand) reads (Roche, May–Jun 2026). *Our opinion:* Neither compares directly with Illumina's roughly $200 genome. [E068]

8. **The per-read gap is smaller than the headline.** *Opinion (broker):* UBS put Roche's $0.06 per million reads against Illumina's $0.68 on the 25B list, about 11x cheaper (UBS, Mar 2026). *Our calc:* Converted to Gb the gap is roughly 7x to 19x, depending on Roche's read length, and on government-channel kit prices Illumina is about $0.97 per million. [E060, E237]

9. **Some see Roche's price as unremarkable.** *Opinion (secondary pricing post).* One post puts Ultima at about $0.24 per million reads and says AXELIOS pricing "isn't aggressively low" in an $80–200 genome market (2026). [E307]

10. **The first like-for-like cost comparison: about 29% cheaper.** *Fact (partner model):* Hartwig showed about 99% agreement with Illumina across 1,229 cancer findings, and a modelled tumor/normal genome cost about 29% lower on AXELIOS than on the X's 25B (European pathology congress, Sep 2026). *Our opinion:* That is far below the 11x per-read headline and close to the 25% list-genome gap, though it is a research partner's model, not invoices. [E299]

11. **Roche is the most credible clinical challenger, but not yet clinical.** *Fact:* Roche has a captive pool of tests (Foundation) but no IVD clearance or timeline for AXELIOS. [E125]

12. **Share forecasts for Roche vary widely.** *Opinion (expert, broker):* Views range from 10–15 of every 100 new instruments in 2027, or 10–20% of Illumina's base over three years if aggressive, to "minimal" in year one, to "will just simply die out" (expert calls and broker notes, 2026). These views are not independent of each other. [E125]

13. **Workflow hurdles.** *Opinion (expert):* Experts describe a "cumbersome" two-box workflow, complex library preparation, and a need for 150 ng of DNA for the 4-hour claim ("nearly impossible from a real patient"); Broad Clinical Labs' amplification-free route needs 500 ng. These matter because clinical samples are often small. [E126, E253]

14. **Buyer caution.** *Opinion (customer, expert):* A Massachusetts genome center with a beta unit expects to buy "a couple", priced "on par, if not a little bit cheaper", and called it "a lot of hype without a lot of data" (expert call, 2026). UBS experts said sensor reuse is "a nonstarter" in the clinic for half of pathologist users, so adoption looks incremental rather than a wholesale switch. [E126]

15. **What customers say they would do.** *Fact (survey):* In JPM's survey (Jun 2026), 40% of customers were unfamiliar with AXELIOS, and purchase intent was 6.2/10 in research and 4.7/10 in clinical. Of would-be buyers, 65% expect to cut Illumina usage but only about 11% would decommission an Illumina machine, and reagent rental would make 39% of academic and 37% of clinical buyers less likely to buy. [E118]

16. **Clinical labs expect Illumina to hold share.** *Fact (survey):* Over three years, mid-size clinical labs in the same survey expect Illumina's share of their work to rise from 50% to 57%, and large and small labs expect it to stay flat (54% and 63%) (JPM, Jun 2026). [E118]

17. **The bar for switching is high.** *Opinion (broker, customer):* Evercore's Kumar said Roche could "gain share in an expanding market rather than… a knife fight", but "you know exactly what you're dealing with Illumina for 20 years… the bar has to be very, very high". A Zurich core head said larger labs would test Roche alongside existing machines (Reuters, Jun 2026). [E136]

18. **Roche's market sizing.** *Mgmt (competitor):* Roche sizes sequencing at about CHF 7B growing 7% a year, MCED at CHF 5.3B by 2030 (35% a year), MRD at CHF 5B (32%) and therapy selection at CHF 17B (9%), and Foundation expects oncology testing to "essentially double over 5 years" (Roche Investor Day, May 2026). [E132]

19. **What that sizing implies for price.** *Our calc:* A sequencing market growing 7% a year while volume grows in the mid-20s implies steady price deflation of roughly 15% a year, in line with Illumina's own mid-teens model. [E132]

20. **Roche's own diagnostics business.** *Fact:* Roche cut its diagnostics guidance to mid-single digits on Chinese price reform and booked CHF 126M of one-off patent income in H1 2026. Separately, PacBio changed CEO in August 2026 (no direct Illumina read). [E185]

21. **Roche is also suing Illumina.** *Fact:* 10x Genomics, with Prognosys and Roche Sequencing Solutions, filed two Delaware patent suits against Illumina's spatial products on 21 Oct 2025. *Our opinion:* So Roche is both a co-plaintiff and a sequencing challenger. [E244]

### Ultima Genomics

1. **The low-cost claim.** *Mgmt (competitor).* The UG200 (Feb 2026) costs $850K ($1.25M with two wafers) and is marketed at about $80 a genome, with a paired-end chemistry later in 2026 (Ultima launch materials, Feb 2026). It is the lowest headline price in the market, about 60% below Illumina's ~$200 list. [E069]

2. **Wins are research and population work.** *Fact.* Mayo Clinic's Precure project (1M biospecimens, Helix lab, Thermo as a founding partner) selected the UG200 on 22 Sep 2026, and BaseClear is the first certified EU service provider. Hartwig's UG200 adoption upgrades the UG 100 it has run since 2024 rather than replacing Illumina, and none of these is US clinical production volume. [E128]

3. **Ultima takes a growing share of work lost by cores.** *Opinion (customer).* A Georgia core director said Ultima's share of the work the core loses rose from about 10% to about 20% in two years, with 80–90% of lost work going to low-cost providers such as Novogene (expert call, 2026). Ultima's finances are opaque. [E272]

4. **A clinical-grade lab prices Ultima about 40% below the X.** *Fact:* Broad Clinical Labs offers the X Plus "starting as low as $2,375 per 25B lane" (at least 2.8B reads) and the Ultima UG 100 "as low as $4,000 per wafer" (at least 8B reads), and still offers 6000 flow cells too (Broad price page, undated). *Our calc:* That is about $0.85 and $0.50 per million reads, so even at a lab that runs both, Illumina's price per read is well above Ultima's. [E260]

5. **An academic cost estimate.** *Fact.* A university infectious-disease evaluation put Ultima at about $12 per 50M reads, about $100 all-in per sample. [E355]

6. **Illumina's accuracy counter-argument.** *Mgmt (Illumina).* Illumina's own benchmark (Oct 2025) says the X makes "6x fewer SNV errors and 22x fewer indel errors" (single-letter and small insertion/deletion errors) than the UG 100, and that Ultima's high-confidence region excludes about 4.2% of the genome, including 793 disease genes such as BRCA1 and FMR1. This is a vendor claim, untested by a third party, but it quantifies the hurdle for regulated tests. [E231, E273]

7. **Independent studies split.** *Fact.* An Owkin preprint (Mar 2026) found "highly comparable results" between the UG 100 and a NovaSeq on clinical tumor tissue across four test types (research use). A Health 2030 Genome Center preprint (Dec 2025) found the UG 100 "reduces genome sequencing costs to $80" but that problems reading long single-letter repeats "undermine the application of this technology to short variant calling in clinical settings", so Ultima's accuracy for clinical use is unsettled. [E238, E252]

### Element Biosciences

1. **VITARI's economics.** *Opinion (broker):* UBS says Element's VITARI lists at $689K, about 40% below the X Plus (implying about $1.15M), with consumables of about $3K per run against about $32K for the X Plus, for about a fifth of the output (3 against 16 terabases) (UBS Fast Take, Feb 2026). *Our calc:* That works out to about $1.00 against $2.00 per Gb, half Illumina's cost. [E069, E191]

2. **VITARI's launch status.** *Fact.* It is marketed as a "$100 genome" and ships in H2 2026, with no named customers (UBS Fast Take, Feb 2026). [E069, E191]

3. **Element's clinical footprint is small.** *Fact:* About 20% of Element's customers are in clinical research, up from 15% (one source says over 25%), and its AVITI Dx and a Revvity newborn IVD kit have no clearance yet. [E129]

4. **Strongest against small and mid-size sites.** *Opinion (expert):* Experts call Element "the strongest small/mid challenger" but say it cannot do deep MRD or CGP at the depths Natera needs (expert calls, 2026). In their view an X Plus site "has little reason to switch", while a 6000 site loses to AVITI on price. [E129]

5. **The 6000's end of life is the opening.** *Opinion (expert, hearsay):* A former field application scientist said Element is "moving customers from X Plus to VITARI", and a Roche-employed expert said the 6000 is "supposed to become obsolete", making it the competitive window (expert calls, 2026). *Mgmt:* The CEO's own "stay until end of life" comment (Q2 2025 call) confirms the tail is the exposed base. [E130, E393]

6. **Well funded through the VITARI ramp.** *Fact.* Element raised an upsized Series E on 9 June 2026 with $175M from Samsung Electronics (the Series D was $277M in July 2024), for VITARI, AVITI Dx and tissue profiling, with customers in 40+ countries. [E200]

7. **A first clinical prenatal user, in Europe.** *Fact.* Medicover Genetics put AVITI into its VERACITY NIPT workflow and IVDR-certified kits in May 2025 (IVDR is the EU's in-vitro-diagnostic regulation), though the instrument itself is not IVDR-marked and no volume or saving is given. Prenatal testing is low-Gb, so this matters more as a precedent than as volume. [E353]

8. **A first clinical cancer user, in Germany.** *Fact (weak source: search summary of a partner deck):* Leipzig pathology lab PathoNext has run AVITI24 for clinical cancer profiling since October 2025, citing cost and "reducing dependency towards a single provider". [E363]

*Pointer, not new evidence:* none of the nine large US clinical labs we checked uses Element (or any rival) in production; the finding is set out in Question 2, section F [E353].

9. **Core-facility prices conflict.** *Fact:* Northwestern's core charges about $10.8 per Gb for AVITI high-output and $19 for AVITI Ultra Q, against $3.2–5.0 for the X 25B, so AVITI costs 2–3x the X per Gb there. The University of Minnesota says AVITI costs fell 62–71% since FY24, to about $2.6–3.6 per Gb (similar to 25B core rates), and that outsourcing X work is "faster and less expensive". *Our opinion:* So Element's price advantage depends heavily on the site. [E290, E315]

10. **Patent fights: a German ruling against old machines.** *Fact:* On 14 July 2026 a Munich court found that Illumina's legacy MiSeq and MiSeqDx infringe an Element imaging patent, and ordered a German injunction, a recall of systems and reagents placed since 31 March 2023, and an accounting of sales and profits. The ruling becomes enforceable once Element posts security, and no appeal has yet been announced. [E201, E215]

11. **The two sides read the ruling differently.** *Mgmt (weak source):* Illumina calls the ruling "narrow", says it does not touch NextSeq or NovaSeq, and says a software update keeps German MiSeqs running. *Mgmt (competitor):* Element says it covers "any other Illumina imaging system that functions as described by the court". *Our opinion:* It matters for this thesis only if it widens to the NovaSeq family. [E201, E215]

12. **Patent fights: the US case reaches the X.** *Fact:* Illumina sued Element first, in Delaware on 15 May 2025 (case 1:25-cv-00602), accusing AVITI of infringing imaging and flow-cell patents; sources list four or five patents. *Fact (weak source: accused-product list from a search summary):* Element's September 2025 counterclaims accuse the MiSeq, MiSeq i100, MiniSeq, NextSeq 1000/2000, NovaSeq 6000 and NovaSeq X, with no damages or schedule known. [E223, E224]

13. **But the US risk is capped.** *Fact:* One Element patent (US 8,612,161, licensed from IsoPlexis) expires about July 2030, which caps any damages period, and another (US 12,656,313, granted June 2026) is assigned to Qiagen. [E225, E242]

### PacBio, Oxford Nanopore and long reads

1. **Long-read clinical growth is fast from a small base.** *Fact.* PacBio's Q2 2026 clinical shipments grew 67% (mid-teens percent of consumables), with 20 Revios placed, mostly clinical; Oxford Nanopore's H1 2026 clinical revenue was £17.6M (+35.4%); and MGI's clinical revenue grew 36.6% (company results, 2026). None threatens NovaSeq-class consumables directly. [E131, E133]

2. **A broker sees the same clinical tilt.** *Opinion (broker).* Deutsche Bank: "Illumina's growth is increasingly Clinical-led and most PacBio Revio placements went to Clinical accounts" (Sep 2026). PacBio sold its short-read technology (Onso) to Illumina for $48.1M net in January 2026. [E131, E133]

3. **PacBio shows volume without pricing power.** *Fact:* Q2 2026 revenue was $39.0M, consumables grew only 6% (to $20.1M), and non-GAAP gross margin fell to 36% from 38% on compute and memory costs and "multi-system pricing concessions". *Mgmt (competitor):* Asked whether lower costs bring volume that offsets lower prices, PacBio's CEO said "customer demand and project scale should close the revenue gap" (PacBio Q2 2026 call). *Our opinion:* That is an expectation rather than evidence. [E421, E442]

4. **Long reads as a rare-disease test.** *Fact.* A Radboud UMC paper models long-read genomes as a first-tier rare-disease test, raising diagnostic yield from 16.4% to 18.9%, and PacBio's 20x genome lists at $345. [E354, E422]

5. **Long-read clinical contracts are small.** *Fact.* Genomics England awarded Oxford Nanopore a £5.23M long-read contract (Dec 2024), similar in size to Illumina's £4.67M extension. Azenta launched long-read clinical genomes on Revio in its certified lab (Nov 2024), the only verified non-Illumina clinical genome launch found, and it complements rather than displaces short-read work. [E354, E422]

6. **Oxford Nanopore.** *Fact:* H1 2026 revenue was £116.7M (+10.5%, +12% at constant currency), short of expectations as China fell 15.7% and the Middle East 14%, while gross margin rose to 62.2% from 58.2%. *Mgmt (competitor):* It credits the margin gain partly to a "new pricing model" and targets 2030 revenue above $700M with an EBITDA margin (operating profit before depreciation and amortization, as a share of revenue) above 15%. *Our opinion:* Its China weakness mirrors Illumina's. [E333, E436]

### MGI, Complete Genomics and China

1. **MGI is growing, mostly in China.** *Fact.* MGI's H1 2026 revenue rose 18.9% to RMB 1.366B; overseas revenue rose 33.8% to RMB 483M (about $67M), and the Americas 96% to RMB 201M. Reagents grew 16.3% and instruments fell 6.4%, with gross margin of 57.0% and a net loss of RMB 158M. [E332]

2. **MGI is a minor high-throughput threat outside China.** *Fact:* MGI sold 1,470 sequencers in 2025 (898 to clinical customers) but only 27 of its largest T7+. *Mgmt (competitor):* It claims a 50% running-cost cut on the T7+ but gives no price per Gb. Its sequencing revenue appears as RMB 1.062B in one source and 1.10B in another. [E350]

3. **Complete Genomics is being sold.** *Fact.* MGI agreed to sell Complete Genomics, its US arm, to Swiss Rockets for $50M plus a technology licence (announced 23 Feb 2026); no closing was found. [E420, E456]

4. **And is on a US blacklist.** *Fact.* The US Defense Department's 1260H list of "Chinese military companies" (8 Jun 2026) added Complete Genomics, Inc. among BGI Group subsidiaries, and Novogene and WuXi AppTec as parents; MGI is probably listed through its parent, and Novogene says it was listed in error. Complete Genomics' listing was first denied by one source, then confirmed by the law firm WilmerHale. [E420, E456]

5. **BIOSECURE limits federal, not private, purchases.** *Fact:* The BIOSECURE Act became law in December 2025 and relies on the 1260H list; the federal list of designated companies is due by December 2026, contract rules follow within a year, and existing contracts are grandfathered for five years. It restricts federal contracts and grants, not private clinical labs. *Opinion (legal commentary and ours):* Prohibitions are "likely sometime in 2027", so a forced switch away from Chinese platforms by US clinical labs is unlikely before 2027–28. [E420]

### Thermo Fisher and service providers

1. **Thermo Fisher.** *Mgmt (peer):* Q2 2026 organic growth was 5%, and US academic and government demand "returned to growth" in a "stabilization period"; sequencing was not mentioned (Thermo Q2 2026 call). *Fact:* Its Ion Torrent platform wins small-panel work, not genomes, and Thermo is a founding partner in the Ultima-linked Precure project. *Our opinion:* Its funding read conflicts with Bruker and 10x (Question 2, section B). [E134]

2. **Novogene: volume up a third, revenue flat.** *Fact:* Novogene's FY25 data output rose 33% and data sales volume 28%, but sequencing-platform services revenue rose only 0.6% (total revenue +4.7%) (Novogene FY25 annual report). *Our calc:* So revenue per unit of data fell about 18–22% (the volume measure is unclear). *Our opinion:* This is outside evidence that about 30% volume growth can come with flat revenue. [E351, E360, E399]

3. **Novogene in 2026.** *Fact.* H1 2026 revenue rose 7.1%, slowing to +3.6% in Q2, while Q1 2026 gross margin improved on "reduced industry competitive pressure". Its fleet includes the X Plus, Ultima, MGI and Revio, with 10 X Plus systems recently added. [E351, E360, E399]

4. **Macrogen: margin pressure, then recovery.** *Mgmt (peer):* Macrogen, a Korean service lab and a named AXELIOS customer, said in Q1 2026 that sequencing (88% of revenue) faces unit-cost decline "requiring volume expansion for viability". *Fact:* It made an operating loss of KRW 0.5B in Q1 and H1 2026 operating profit of KRW 2.4B (+152%) on cost cuts, though its quarterly revenue figures do not reconcile across sources. [E352, E361]

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

## What to watch next

The first table lists dated events in order, with what each could tell us. The takeaway is that the next six weeks (ASHG, the Q3 print, the GRAIL renewal deadline and customer prints) will test the near-term numbers, while the 35B launch in H1 2027 is the event that decides the 2027–28 answer.

| Date | Event | What to look for and what it would mean |
|---|---|---|
| 19 Oct 2026 | Objection deadline, Icahn derivative settlement | Minor; settlement has no payment [E243] |
| 20–24 Oct 2026 | ASHG conference | Any 35B price, date or scope (bear if an across-the-board ~20% cut from January); Roche AXELIOS clinical data [E300, E123] |
| 29 Oct 2026 | Illumina Q3 2026 results | The checklist table below [E176, E450] |
| 30 Oct 2026 | Hearing in the state GRAIL securities class action | Legal overhang only [E159] |
| ~31 Oct 2026 (weak source; date to check, not a confirmed event) | Possible notice deadline for GRAIL supply agreement renewal | Only if the date is confirmed: a non-renewal notice from either side would change GRAIL's pricing terms [E257] |
| 2 Nov 2026 | Icahn settlement hearing | Minor [E230] |
| Early–mid Nov 2026 | Natera, Guardant, Tempus, Caris, GeneDx, BillionToOne, GRAIL Q3 results | Volumes, cost per test, any second-sourcing or price-concession comments; whether Guardant360 Liquid CDx runs on the X [E297, E293, E309] |
| Nov 2026 | CMS final 2027 lab fee schedule | Whether the −23% sequencing-code average and 15% cap hold [E097, E219] |
| 18 Dec 2026 | Federal BIOSECURE list due | Whether MGI, Complete Genomics or Novogene are designated [E420, E456] |
| 24 Dec 2026 | GRAIL royalty suspension ends | Royalty income resumes at up to 9% [E257] |
| Early 2027 | FDA decision on Galleri | Approval is a precondition for Medicare MCED coverage from 2028 [E318, E319] |
| ~Feb 2027 | Q4 2026 results and FY27 guide | 14-week quarter; whether the pull-through table returns; FY27 clinical framing [E269, E276] |
| H1 2027 | 35B and 14B flow cells | Price, eligibility, and whether the cut reaches existing contract customers [E214, E212] |
| H1 2027 | Illumina ERP go-live | Internal-control risk flagged by the auditor [E380] |
| 2027 | Global launch of Illumina's whole-genome MRD (WGS-MRD) kit; Element VITARI ramp and AVITI Dx CE filing | Gb per sample; first non-Illumina clinical IVD [E087, E129] |
| ~Aug 2027 | Possible close of the Open Offer window (unverified) | New oncology customers may lose MFN and price-freeze terms [E233] |
| 2028 | Medicare MCED coverage begins; 2025 PSU cycle ends 2 Jan 2028 | MCED volume; disclosure of the margin hurdle [E319, E441] |

The second table is the Q3 2026 checklist. Each row gives the reading that would support the bull side, the reading that would support the bear side, and why it matters. The takeaway is that the most informative single number is derived 6000 revenue (total HT minus X), because it shows whether the guided H2 decline is happening.

| Metric (Q3 2026) | Bull reading | Bear reading | Why it matters |
|---|---|---|---|
| Ex-China clinical consumables growth | 13–16% | Below 12% (weak), below 10% (break) | Tests the mid-teens FY guide against an easy +12% comparison [E306, E450] |
| Sequencing consumables vs $789M consensus | $789M or more | Below $775M (a sequential fall) | Q3 has 13 weeks; Q4's extra week flatters Q4 only [E269, E448] |
| Derived 6000 revenue (vs $219M in Q2) | $213M or less, trending to $138–200M | $219M or more | Shows whether the tail is running off as the guide implies [E245, E394] |
| X share of HT revenue / volume | 61%+ revenue; 84–86% volume | Flat near 59% / 83%, or the slide is dropped | A 62–64% revenue share needs 85–86% volume share [E270, E413] |
| Clinical X volume share | 79–80% or higher | Flat at 78% | Path to the 80–85% end-2026 target [E342] |
| X pull-through and FY26 guides | Guides reaffirmed; X run-rate rising toward $1.4M | Guides dropped or cut; run-rate below $1.20M | Guide needs H2 pull-through of $1.46–1.55M [E268, E277] |
| ">30%" Gb language | Retained with a number | Softened or dropped | The only volume metric left [E049, E207] |
| 35B commentary | H1 2027, selective scope, reinvested in volume | January, across-the-board ~20% | Worth $63–253M a year depending on adoption [E247] |
| Answers on dual running and the 6000 tail | Stated decommission pace or 6000 count | Another deflection | The thesis question [E014, E338] |
| Gross margin bridge | Drivers quantified, tariff help visible | Unexplained decline, no bridge | Separates price from tariffs, memory and freight [E365, E406] |
| Inventory reserve and receivables | Coverage stable, receivables normal | Coverage falls further, receivables spike | Earnings-quality checks [E372, E371] |

## Where sources disagree, and stale or weak evidence

The disagreements are ranked by how much they move the thesis. The first five change the answer to Question 1 or 2, and the next four change details. Smaller source errors are noted where they appear in the text and summarized briefly at the end.

### Disagreements that move the thesis

1. **How fast clinical Gb is growing.** *Our calc vs our calc:* The original bottom-up test model said +23% (forward), while the revenue-implied bridge first said +35–60% (trailing). *Our opinion:* Most of the gap is time basis and weighting: re-run on Q2 prints, the bottom-up model gives about +31–34%, and the defensible trailing range is +35–50%. The original +23% also cannot be squared with total ">30%", so it is superseded. [E083, E205, E263, E264]

2. **How fast clinical price is falling.** *Mgmt vs our calc vs survey:* Management models mid-teens a year, the revenue bridge implies 20–28% a year for clinical, and the JPM survey implies only 4–5%. *Our opinion:* They cannot all be right; the survey is the weakest (stated plans, 32 labs), and the gap between management and the bridge is the one that matters for 2027. [E047, E067, E205]

3. **The size of the 6000-to-X gap.** *Fact vs Mgmt vs price cards:* Revenue shares imply the X is about 70% cheaper per Gb, the CFO said "easily more than 60–70%", Illumina's launch claim was "up to 59%", same-core cards show 34–60% for S4 pairs, and a grant applicant claims "up to ~80%". *Our opinion:* The probable reasons are the 6000's flow-cell mix, under-filled flow cells and core overheads. [E030, E051, E291, E311, E434]

4. **35B timing and size.** *Opinion (hearsay) vs Fact (company):* "January 2027" is hearsay, while Illumina's roadmap says H1 2027; the 20% size is one former employee's estimate, and the genome-price base differs between sources ($200 list against $175 effective). *Our opinion:* This is the single biggest swing factor for 2027. [E058, E190, E214]

5. **Illumina's "$2.00 per Gb".** *Mgmt vs price lists:* No current list or distributor price reaches it: the government-channel 25B-300 is $2.30–3.02 per Gb, the 200-cycle list $2.07–2.74, and the cheapest cores $2.50–2.63. Only a Spanish tender award (about €2.00 per Gb at an assumed output) comes close. *Our opinion:* Treat it as a launch or large-account figure. [E055, E217, E235, E437]

### Disagreements that change details

6. **Gb per test.** *Opinion (estimates) vs Fact (Illumina spec page):* An exome is about 8 Gb in estimates but 11.3 Gb on Illumina's spec page, and liquid-biopsy profiling is 120 Gb in one estimate and 35–100 Gb in a later one. *Our opinion:* This affects how much Gb the named customers explain, not the direction of the answer. [E082, E435]

7. **The fiscal calendar.** *Fact (Bloomberg dates) vs Mgmt:* Bloomberg's dates suggested Q3 2026 has 14 weeks, adding about 7% to Q3 growth, but management says the extra week is in Q4. *Our opinion:* How much it is worth ("0.5 point" per management against a full thirteenth of the quarter) is unresolved, and it matters for reading Q4. [E184, E269, E448]

8. **Contract terms we could not confirm.** *Fact (secondhand):* Natera's August 2033 term (10-K narrative not read), GRAIL's February 2027 term and October 2026 notice date (summary only), Tempus's Illumina attribution and $15.9M payable, and whether Natera's MFN clause survived the Eleventh Amendment all rest on summaries. *Our opinion:* Until confirmed, the contract evidence should be read as directional. [E109, E192, E213, E257]

9. **Pay metrics.** *Fact vs fact:* The proxy extract says 2025 PSUs use operating margin and relative TSR, while 2026 grant filings and a 10-Q say EPS-growth PSUs resumed; a search-derived bonus table did not reconcile, and the CD&A was not read. *Our opinion:* None of these metrics is clinical or price-related, so the disagreement does not affect the thesis. [E149, E197, E441]

### Minor source errors (do not affect the conclusions)

10. **Q3 2024 consumables growth.** *Mgmt vs Mgmt:* Recorded as +5–7%, but Dhingra also said "high single-digit" on the same call, possibly for HT only. *Our opinion:* Either way, Gb grew about 40% that quarter, so the point that price absorbed most of the volume stands. [E048]

11. **X Plus instrument prices.** *Opinion (press and blogs) vs broker inference:* Sources give $689K (actually Element's VITARI), $985K–1.25M (Reuters), $1.165M or $1.5M (a blogger) and about $1M (Seeking Alpha), while UBS's "VITARI is ~40% below X Plus" implies about $1.15M. *Our opinion:* Instrument-price comparisons therefore carry a wide error band, but the consumables thesis rests on price per Gb. [E182]

12. **Transcription errors in broker and Bloomberg data.** *Fact (source errors):* Barclays' "76%" is the clinical figure, not the total 82%; a Barclays August note attributes AXELIOS to Element; FY24 sequencing consumables appear as $2,858M (Bloomberg) and $2,872M (deck); and a Q4 2024 EPS header shows $0.86 against $0.95. *Our opinion:* So this addendum uses Illumina's own decks and filings over broker and Bloomberg transcriptions. [E183]

13. **Other small mismatches, noted where they appear.** *Fact:* Insider-sale totals in secondary reports (Management conduct), Macrogen and MGI revenue figures, Twist's customer-concentration figure, the Element patent count, Complete Genomics' 1260H listing, Element's clinical-research share, and Thermo's academic read against Bruker and 10x (Question 2 and "Read-through from competitors") all differ between sources. *Our opinion:* None changes a conclusion. [E150, E151, E152, E352, E361, E350, E414, E224, E420, E129, E425]

### Stale evidence

Each item says what kind of evidence has aged and what that means for the conclusions.

1. **Illumina's platform data.** *Fact (stale).* Illumina's last full platform data is from Q4 2025 (installed bases, pull-through table), and the 40-customer cohort from September 2025. Every 2026 installed-base and pull-through figure in this addendum is therefore our derivation. [E020, E025]
2. **Contract exhibits.** *Fact (stale).* Guardant's exhibit dates from December 2020, Tempus's from 2021, and the Exact reading from its FY2023 10-K. Later amendments could have changed terms, though Natera's 2026 amendment points the same way (price only falls). [E228, E281, E284]
3. **Expert views.** *Opinion (stale).* Many experts left Illumina in 2024–25, so their descriptions of X economics and pricing practice may be dated. [E113, E169]
4. **Price cards.** *Fact (stale or undated).* TCAG (Apr 2025), Salk's older S4 list, and the undated GSA and Broad pages may not reflect 2026 prices. They are used for direction (the size of the 25B-versus-S4 gap), not for levels. [E053, E234, E260, E316]
5. **Sell-side and customer counts.** *Opinion and fact (stale).* UBS's model (Feb–Mar 2026), FactSet's $175.72 target and Caris's 50-NovaSeq count (Mar 2025) predate the stock's re-rating and Caris's capacity plans. [E172, E400, E411]

### Weak evidence (snippet-level or single-source)

Search snippets or tool summaries rather than full documents underlie the items listed below. Each is flagged *weak source* where it appears in the text. *Our opinion:* None is load-bearing for the answer to either question. The GRAIL renewal date appears in the watch table only as a date to check, not as a confirmed event.

1. **Price data.** *Fact (weak source):* The Harvard core prices and the CNAG 2x100 figure (the latter later confirmed). [E274]
2. **Test specifications.** *Fact (weak source):* The Signatera Genome spec and the GRAIL "4x" throughput claim. [E438, E335]
3. **Competitor facts.** *Fact (weak source):* PathoNext's AVITI use, the Element countersuit accused-product list and Illumina's statement on the Munich ruling. [E363, E223, E215]
4. **Customer contracts, payables and filings.** *Fact (weak source):* The Tempus payable, the Caris $4 per Gb baseline, GRAIL's supply-agreement expiry date, and the claim that Caris's FY25 10-K mentions both the 6000 and the X. [E213, E249, E257, E022]
5. **Regulatory and product pages.** *Fact (weak source):* A European web page suggesting X ordering for TruSight Oncology Comprehensive. [E250]
6. **Guidelines and public programs.** *Fact (weak source):* The ACMG prenatal-screening statement and the NHS genome volumes. [E431, E262]

## How this addendum was built

**Process.** The research ran as an automated series of research-agent waves, at most four agents at a time, until a wave found no new evidence or the usage cap was reached. The first waves read the internal corpus (every Illumina call, conference, deck, filing and consensus sheet from 2023 to 2026, all 23 expert calls, sell-side research and peer material) and made first web sweeps (customer filings, price lists, Medicare and payer data, competitor news, management conduct and job postings). Separate agents then built the scenario model, wrote a bull-and-bear red team, and fact-checked about 40 decision-relevant numbers against the corpus (35 correct, 1 wrong, 2 mis-cited and 2 unverifiable; the corrections are applied here).

About thirty follow-up waves were aimed at the open gaps: SEC exhibits and insider filings, customer contracts and cost lines, FDA databases, core-facility rate cards and tenders, MRD and NIPT guidelines, the HiSeq precedent, accounting quality and the Q3 2026 set-up. A second agent independently re-checked the consensus arithmetic. Every finding was deduplicated into a master evidence ledger of 456 items (E001–E456), with later corrections, and a companion appendix in the ledger's folder lists where each ledger item is cited, so coverage can be checked.

**Sources.** Inside the folder: Illumina earnings calls, conference transcripts, decks, 10-Ks and 10-Qs; Bloomberg consensus; JPM, Barclays, UBS, Freedom and other broker notes; JPM's customer survey; and 23 expert calls. Outside: SEC EDGAR (customer 10-Ks, 10-Qs, S-1s and supply-agreement exhibits; Illumina Form 4s, 13Gs, 8-Ks and the proxy), openFDA, CMS and HHS-OIG, NCCN and trial publications, university core-facility rate cards, GSA and EU procurement records, company press releases, Chinese and Korean financial press, trade press, and market-data aggregators.

**Limits.**

- **No disclosure of the key numbers.** Illumina does not report 6000 revenue, clinical revenue by platform, net price per Gb, the clinical share of HT Gb, platform margins or the count of labs running both platforms. Every sizing in this addendum is derived from rounded share data and stated assumptions.
- **Shipped, not consumed.** The share data measure Gb shipped, so the price ratios carry that definition.
- **Web data quality.** Many web items rest on web-tool summaries or search snippets rather than verbatim reads. Long SEC filings were often truncated (the proxy's compensation discussion and the 10-Q's risk factors were never read in full), several sites blocked access, and some PDFs could not be extracted. The FDA safety and effectiveness documents (SSEDs) for Guardant and Foundation, the TGen price list and EU tender notices remain unread.
- **Alternative data gaps.** The planned automated job-postings scrape was unavailable, so job evidence rests on about a dozen postings. Illumina's own list prices are behind a login, so price evidence comes from core facilities, distributors and tenders, which include overhead.
- **Customer data.** The corpus had no customer-company transcripts, so customer facts come from their SEC filings and releases; Illumina's share of each customer's spend is mostly unnamed in those filings.
- **Models are opinion.** The scenario model and break-even grids are transparent arithmetic on assumptions, and a similar model under-predicted Q2 2026. Use them to see what has to be true, not as forecasts.
- **Open gaps** at the close of research: the 35B price and scope; which sequencer Guardant360 Liquid CDx names; the proxy's compensation thresholds; Form 4 plan flags for officers; customer purchase obligations to Illumina; Tempus MRD volume; whole-genome MRD depth; and whether the Complete Genomics sale has closed.

**The limits in one paragraph.** This addendum is a careful reading of incomplete evidence. Its central numbers (the 3.4x premium, the ~$0.73B clinical 6000 business, the ~$500M "excess" and the $150–190M annual unwind) are derived from Illumina's rounded share data and our stated assumptions, not reported by the company. The direction of the answers is well supported; the dollar sizes are moderately reliable; the profit and EPS figures are the weakest part. The Q3 2026 print on 29 October and the 35B's price and scope in the first half of 2027 are the two events most likely to change them.
