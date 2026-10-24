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
