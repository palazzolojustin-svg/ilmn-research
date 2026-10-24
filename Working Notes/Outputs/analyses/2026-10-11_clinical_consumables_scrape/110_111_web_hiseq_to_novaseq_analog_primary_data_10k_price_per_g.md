# Agent 110: 111-web-HiSeq-to-NovaSeq-analog-primary-data-10K-price-per-Gb-investor-day-claims-NHGRI

*Model: sonnet. Run 2026-10-11 10:39:14. Cost $0.43 (API-equivalent).*

**Assignment:** Close open gap 4. Find primary data for the 2016-2021 HiSeq-to-NovaSeq 6000 transition as a template for the 6000-to-X conversion. Sources: Illumina 10-Ks FY16-FY21 on EDGAR (MD&A text on sequencing consumables growth, any Gb shipped or price-per-Gb statements, instrument installed-base tables); 8-K Ex. 99.1 earnings transcripts for Q4'18, Q1'19 to Q4'19 and Q4'20 (verify the 'about 1,000 active / 320 pending' NovaSeq summary against the original transcript); the 2018 and 2019 investor-day materials and the '$600 genome' and '$100 genome' claims; NHGRI cost-per-genome and cost-per-Mb data (genome.gov/sequencingcosts). Quantify: Gb-shipped growth versus consumables revenue growth per year, implied revenue per Gb decline per year, HiSeq versus NovaSeq base by year-end, pull-through per instrument, and the 2019 guidance cuts with the stated reasons and the analyst reactions (price targets, quotes from trade press such as GenomeWeb, Fierce, Reuters). Answer the question: did volume offset price across the HiSeq conversion, and over what lag? Cite URL and date for every item. Stop at about 20 minutes.

## Key findings

Most of this is a verification and quantification of E181 and agent 107's file (`107_107_web_historical_hiseq_to_novaseq_6000_transition_analog_2.md`). Three points are new or corrective. The 2019 volume figures are NovaSeq-specific. The "1,000 active / 320 pending" summary is now checked against the transcript text. The 2018 figures and the $100 genome claim fill part of the gap.

- **The "1,000 active HiSeq / 320 customers yet to transition" summary is confirmed for Q4'20. FACT/MGMT.** The Q4'20 call (2021-02-11) says: "We ended the year with about 1,000 active HiSeq units and in 2021, we expect continued HiSeq to NovaSeq adoption among the 320 customers yet to transition."
  - Source: https://www.fool.com/earnings/call-transcripts/2021/02/11/illumina-inc-ilmn-q4-2020-earnings-call-transcript/. I read it via a fetch summary, not the SEC exhibit.
  - Agent 107 flagged this as unverified. It is now verified, and the "320" is a customer count, not a unit count.
  - The same call says Q4'20 pull-through was "over $1.2 million per instrument", with $1.1–1.2M guided for 2021.
  - It says total 2020 sequencing consumables were "$2 billion, down 2%", clinical was about $890M (+8%), and clinical was ">43%" of shipments.
  - Analysts asked whether the 20% consumables growth guide was conservative.
- **The HiSeq conversion denominator is 850 customers. FACT. This is new.** The Q4'19 call says "Of the 850 HiSeq and HiSeqX customers at launch, a little over 1/3 have initiated their transitions to NovaSeq."
  - Source: https://www.sec.gov/Archives/edgar/data/0001110803/000111080320000009/ilmntranscript20.htm (Jan 2020).
  - Agent 107 had "under half". The transcript wording is the tighter "a little over 1/3", three years after launch.
  - Q4'18 call (2019-01-30): "3/4 of our HiSeq customers have yet to purchase a NovaSeq... approximately 630 HiSeq customers". That is 630 of 850, or about 74%. The 2018 and 2019 figures agree.
  - Customers yet to start fell from about 630 (end-2018) to about 550+ (end-2019) to 320 (end-2020). Cumulative initiation was about 26%, then about 35%+, then about 62%.
  - Source for Q4'18: https://www.sec.gov/Archives/edgar/data/1110803/000111080319000002/ilmntranscript19.htm
  - OPINION: the pace is roughly 10–25 points of the customer base per year. Starting a transition is not the same as completing it.
- **2019 volume is NovaSeq-specific, which sharpens E047. FACT.** Same Q4'19 transcript: NovaSeq "consumable shipments... almost doubled in 2019, resulting in more than 110 petabases of data, more than double 2018". Total data generated was +50%, "150+ petabases".
  - Source: https://www.sec.gov/Archives/edgar/data/0001110803/000111080320000009/ilmntranscript20.htm
  - The Q4'18 call says 2018 total data was "over 100 petabytes" (the call says petabytes, not petabases; I did not resolve the unit), and "about half" was on NovaSeq, so about 50 PB.
  - OPINION: NovaSeq data grew about 2.2x in 2019 against total +50%. HiSeq and other platform data therefore stayed roughly flat to slightly down in absolute terms: 100 − 50 = 50 PB in 2018, and 150 − 110 = 40 PB in 2019, about −20%.
  - Total consumables grew 14% on +50% data, about −24% in revenue per Gb. This corroborates the F107 correction to E047.
  - Caveat: the 2018 and 2019 figures are rounded and the units are inconsistent in the original text.
- **The 2018 volume series is still missing. FACT/gap.** 2018 consumables were about +23% (Q4'18 call). I found no 2017 total-data figure, so 2018 elasticity cannot be computed. Q4'17: sequencing consumables $432M (+30%+), NovaSeq about $100M, a $19M stocking order, and about 285 NovaSeq shipments in FY17 (GenomeWeb, via search snippet).
- **The $600 genome claim is dated. MGMT.** The JPM call on 2021-01-11 says "Labs of any size can now access the $600 genome". The Q4'19 call (Jan 2020) says the largest customers reach "approximately $800" per whole genome.
  - Source: https://www.sec.gov/Archives/edgar/data/0001110803/000111080321000003/exhibit991transcript2021.htm (fetch summary).
  - OPINION: the price floor fell from about $800 (large customers, Jan 2020) to $600 (any lab, Jan 2021), a 25% decline in a year. That is consistent with the roughly 24% per-Gb decline above.
  - Correction to the transcript labels: the 2021 exhibit I fetched under the "Q4'20" name is the JPM Jan 2021 call, not the earnings call. The Feb 2021 earnings call is the Motley Fool link above.
- **The $100 genome was a roadmap claim, not a priced product. MGMT.**
  - deSouza at JPM 2019: development work continues, with no date given (GenomeWeb/GEN, Jan 2019, e.g. https://genengnews.com/news/illumina-ceo-says-100-genome-still-under-development).
  - Illumina said NovaSeq was the architecture that "would lead to" it, over time, in steps.
  - There was no investor-day price-per-Gb table, and my searches did not turn up a standalone 2018 or 2019 investor day. The materials found were JPM decks and calls.
  - I did not open the JPM 2019 deck (https://www.illumina.com/content/dam/illumina-marketing/documents/company/investor-relations/ILMN-at-JPM-2019-7-January-2019.pdf).
- **Guidance misses are confirmed on the stated reasons. FACT.**
  - Prelim Q2'19: revenue $835M vs $888M consensus. FY19 growth was cut to about 6%.
  - Stated reasons: lower near-term DTC, "a more conservative assumption about the speed with which certain population genomics initiatives ramp", and lower non-high-throughput systems and consumables.
  - NovaSeq consumables were +40% q/q and >100% y/y even at the time of the cut.
  - Sell-side (GenomeWeb search snippet): BofA's Derik de Bruin downgraded to Underperform and cut his target from $355 to $290. SVB Leerink's Puneet Souda cut from $380 to $360 and Cowen's Doug Schenkel from $380 to $320.
  - Source: https://www.genomeweb.com/sequencing/illumina-projects-q2-revenue-miss-lowers-full-year-guidance
  - Dates and attributions come from the snippet only, so verify before using.
  - Original guide to 2019: sequencing consumables "above 20%" (Q4'18 call). Actual was +14%.
  - OPINION: the cuts blamed DTC and population genomics, not NovaSeq price per Gb. Management did not name the price decline as a cause.
- **Answer to the thesis question: did volume offset price across the HiSeq conversion?** OPINION, based on the above.
  - No, not in the HiSeq/NovaSeq blend. 2019 saw +50% volume and +14% revenue.
  - The offset came from NovaSeq share gains and new demand (UK Biobank, clinical), not per-unit elasticity.
  - The lag was at least three years to reach about 1/3 of HiSeq customers initiating, and about four years with 320 of 850 customers (38%) still not started. About 1,000 HiSeq units were still active at end-2020.

## Contradictions and stale data

- **Agent 107's "under half" vs the transcript's "a little over 1/3"**: the transcript wording is tighter. Both come from fetch summaries, so verify against the full SEC text.
- **Transcript labelling**: the SEC file `exhibit991transcript2021.htm` is the 2021-01-11 JPM call, not the Q4'20 earnings call. Quote it as JPM.
- **Unit inconsistency**: Q4'18 says "petabytes" and Q4'19 says "petabases", so the 2018-to-2019 growth comparisons carry a unit caveat.
- **Trade-press snippets**: price targets and analysts' names come from search snippets, not opened articles.

## Gaps / what I could not find

- **The 10-K FY16–FY21 MD&A**: the FY19 10-K fetch gave only generic text, such as a "10,000x cost reduction" claim and the consumables share of revenue (68% in FY19, 65% in FY18, 64% in FY17). It showed no Gb, price per Gb, or installed-base tables. This looks like a real absence, not a fetch failure, but I could not confirm the full document was read.
- **NHGRI cost per genome and per Mb**: the page offers only an Excel download, which I could not open, so no 2015–2021 values were obtained.
- **A distinct 2018 or 2019 investor-day price-per-Gb deck**, and any 2017 total-data figure.
- **Sell-side commentary on 2019 pull-through** beyond the three snippet targets, and the HiSeq base by instrument at end-2017 and end-2018.
