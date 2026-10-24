# Thesis Scrape Addendum: New Evidence for the ILMN Pricing and Research Thesis

*As of 2026-10-12. Built overnight by an automated research loop: 618 agent tasks across about 1,040 candidate sources. It kept only findings that are new to the existing notes, a skeptical second pass checked each one, and the derived figures are our own arithmetic on those findings.*

**A few terms used throughout.**
- **NovaSeq 6000 and NovaSeq X.** Illumina's older and newer high-throughput sequencers.
- **Flow cell.** The single-use glass cartridge that sequencing runs on, and the main consumable Illumina sells. The 6000 uses SP, S1, S2 and S4 flow cells. The X uses 1.5B, 5B, 10B and 25B flow cells, named for billions of reads. A 35B flow cell is on the roadmap for H1 2027.
- **Lane.** One of the separate channels on a flow cell. Service labs often sell by the lane.
- **Gb and $/Gb.** A gigabase is a billion DNA letters of output, so $/Gb is the price per unit of output.
- **Core.** A university sequencing service lab. Its **recharge rate** is what it charges users. That rate includes labor and overhead on top of reagent cost, so it is not Illumina's price.
- **List, GSA and net prices.** "List" is Illumina's catalog price. "GSA" is the US federal distributor schedule, about 1.47x catalog list for the 25B. "Net" is the price actually paid after discounts.
- **Clinical tests.**
  - **MRD** (minimal residual disease) tests look for leftover cancer DNA in blood after treatment.
  - **NIPT** is the prenatal blood test for chromosome conditions.
  - **WGS and WES** are whole-genome and whole-exome sequencing.
  - **RUO** kits are for research use only. **Dx** (or IVD) kits are regulated for diagnostics.
- **Tender.** A public purchasing competition.
- **GEO, SRA and ENA.** Public databases where researchers deposit sequencing data, usually one to two years after the sequencing is done.

## The most powerful new evidence

The scrape found its strongest new support for the two pricing legs of the thesis. These are 1A (the 6000 mix shift still has a costly step left) and 1B (discounting pressure from cheaper rivals and big accounts). It also found good support for the part of 1C that says payers, not sequencing cost, now limit clinical volume. Evidence on research (2A and 2B) is real but more mixed. Funding is clearly tight. Rival platforms, however, still look small outside a handful of university cores and Taiwan.

- **The remaining 6000 volume is the expensive end of the fleet, so converting it costs Illumina more per Gb than a simple comparison suggests.**
  - Illumina reports that a Gb sold on the 6000 brings in about 3.4x the revenue of a Gb on the X (Q2 2026).
  - At list prices, the 6000's biggest flow cell (S4) costs only about 2.6–2.8x the X's 25B per Gb. That gap narrowed between 2024 and 2026, while Illumina's reported ratio widened from about 2.8x to 3.4x [D049].
  - Core price lists explain the difference. At Salk and Pitt, the small 6000 flow cells (S2 and SP) cost 3.6–9.8x the X per Gb [D028, D032]. Our inference is that the residual tail is weighted toward small, high-price users.
  - If the 3.4x reflects price rather than accounting, X volume at converted large accounts sells for roughly $1.5/Gb, about 30% below a typical academic net price [D029].

- **Public data shows the mix shift still moving fast.** Weighted by data volume, the X's share of public NovaSeq output in the European archive roughly doubled in a year, from about 17% to 36% (Q3 2025 to Q3 2026). Estimated 6000 output fell about 13% over the same year [F644, D064]. These are lagged, research-heavy data, so they show direction rather than the clinical tail.

- **Ultima now undercuts Illumina at research cores by roughly 2–3x per Gb, and the saving reaches the customer.**
  - The University of Minnesota core (UMGC) sells an all-in 30x human genome on Ultima for $192 internal. Sequencing is about 71% of that price [D099].
  - Per Gb, Ultima is about 2.0–2.7x cheaper than a 25B lane at peer cores [D003, D076].
  - 99.6% of UMGC's open sequencing queue runs on Element or Ultima [F1100].
  - Caveat: at a negotiated Illumina reagent price (~$1.59/Gb), the gap shrinks to 1.2–1.5x [D011].

- **Illumina's price cuts are landing on the smaller X flow cells, where the headline 25B price does not show them.**
  - At UCLA and TGen, cores cut the 10B lane 16–21% in the latest cycle while the 25B held flat or rose. UCSD and UCSF cut both, but the 10B more (16–18% versus 9–11%). Across cores, the 10B's per-Gb premium over the 25B is now 1.03–1.5x [D018, D005, D092, D034].
  - At the two main University of California cores, the 25B lane rate fell from about 1.40x to 1.24x Illumina's per-lane list in about a year, while list rose about 3% [D093].
  - This is deflation per Gb that the street's flagship-price checks would miss. Harvard's core went the other way (see watch-outs).

- **Large-account discounts are negotiated deal by deal, which is where the thesis expects acceleration and also where it is hardest to see.**
  - Illumina's published Open Offer discount schedule caps the 25B discount at 12%, about $1.76/Gb [F540].
  - The cheapest public 25B price is Novogene's $2.55/Gb [D051].
  - Taiwanese outsourced genome prices imply the winning service lab pays at most about $2/Gb for Illumina reagents [D072].
  - So the deep discounts that experts describe have to come from bespoke contracts.

- **A large clinical customer is openly budgeting for lower reagent prices in 2027.**
  - GeneDx's CFO said a genome costs nearly twice an exome to produce, "almost entirely higher reagent costs". He guided cost per test flat for H2 2026 with "step improvements in 2027" (Q2 2026 call) [F568].
  - GeneDx's revenue per test is falling 8–12% a year [D017, D055].
  - Its leverage is limited, because it says it has not validated a second sequencer [F239].

- **Clinical volume is limited by payers, and the fast-growing tests carry very little data.**
  - GeneDx's shift away from genomes toward exomes means its sequencing output grows far slower than its 30%+ test growth [D013].
  - Natera's whole MRD run-rate uses roughly 0.02–0.5% of Illumina's annual high-throughput output [D039].
  - The combined NIPT pool at Natera and Myriad grew only about 8% [D014].
  - Insurer denials of lab and genomic claims rose from 8.0% to 11.2% in 2025 [F347].

- **Tight research funding shows up as fewer funded labs and sharply lower government reagent buying.**
  - NIH funded 1,924 fewer grants than at the same point a year earlier, and competitive R01 awards were down 14% versus FY24 [F402, F404].
  - The Public Health Agency of Canada cut consumable-type Illumina buying 77% in H1 2026 [F510].
  - In Taiwan, a national research institute's falling Illumina spend is mostly lower prices, not lower volume [D081]. That is the 2B pattern of flat volume and worse price.

The most important evidence against the thesis also comes from core price lists. Like-for-like, a lab moving from the 6000 S4 to the X 25B saves about 40–60% per Gb, not the 70% implied by the 3.4x ratio [D022, D025]. Government buyers pay close to list [D023, D048]. Natera's MRD and capacity build show no slowdown [F267, D082]. The watch-outs section covers these and the rest.

## 1A. The NovaSeq 6000 mix shift is not done

The thesis says roughly 5 more points of consumables volume will move from the 6000 to the X in 2027. Each point moved costs Illumina revenue, because 6000 users pay far more per Gb. The thesis also doubts management's claim that the remaining 6000 volume is permanent.

The new evidence supports three things. First, the remaining tail is weighted toward high-price, small-flow-cell users. Second, conversion is still moving in public data. Third, Illumina controls the clock on the tail through its end-of-life rules. It does not prove the clinical tail will convert in 2027, because almost all of the data are research-weighted.

1. **Small 6000 flow cells explain the 3.4x gap.**
   - At Salk (rates effective July 2025), the 6000's S2 flow cell costs 3.6–4.7x the X 25B per Gb, and the SP costs 7.5–9.8x. The S4 costs 2.3–3.1x.
   - Pitt (June 2025) shows the same pattern: S2 about 3.7x, SP about 6.1x.
   - On list prices, the S4-to-25B gap narrowed from about 2.76x (2024) to 2.58x (2025–26), while Illumina's reported revenue ratio widened from 2.8x to 3.4x. So the widening likely comes from tail mix and discount structure, not list moves.
   - Our inference: the users left on the 6000 are small, high-price and least volume-elastic, and each conversion is a big price step.
   - [Salk rates](https://www.salk.edu/science/core-facilities/integrative-genomics-and-bioinformatics-core/scheduling-and-rates/) [D028, D032, D049]

2. **The reported 3.4x implies converted X volume sells well below published academic prices.**
   - If 6000 and X users both paid the National Cancer Institute's net rate (about 71% of the GSA schedule), the ratio would be only about 2.4x.
   - Illumina's published Open Offer price and discount schedule gives 2.45–2.82x depending on spend tier.
   - Reaching 3.4x needs X priced near $1.5/Gb, about 17–30% below the schedule. That is consistent with deep, off-schedule discounts at large converted accounts.
   - Caveat (reviewer): the small-flow-cell mix above, and the gap between Gb shipped and Gb used, could explain part of it instead.
   - [Open Offer Appendix 1](https://assets.illumina.com/content/dam/illumina-marketing/documents/applications/cancer/7-26-2024-appendix-1.pdf) [D029, F539]

3. **Across six cores, moving from the 6000 S4 to the X 25B cuts the per-Gb price by about 60% at the median.**
   - Ratios: Calgary 1.6–1.7x, UConn 1.8–1.9x, MD Anderson about 2.5x, UCSF 2.6x, Emory 2.4–3.0x and Salk 2.3–3.1x. The median is about 2.5x.
   - Core markups over the GSA price are similar on the S4 and the 25B, so the ratio is not an artifact of overhead.
   - At MD Anderson, the S4 lane price was rising before the X arrived: member price +4.8% from FY23 to FY24.
   - These are core rates, not Illumina invoices.
   - [Emory core rates](https://enprc.emory.edu/nhp_genomics_core/rates/index.html) [D025, D027, F289, F061]

4. **Weighted by data volume, public X share doubled in a year and 6000 output fell.**
   - Using the European archive (ENA), the X family's share of NovaSeq output went from about 5% (Q3 2024) to 16–17% (Q3 2025) to 33–36% (Q3 2026).
   - Estimated 6000 output fell about 13% year over year.
   - Counting the X Plus model, the X's share of runs of 10 Gb or more went from 16% to 33%, while large 6000 runs fell 15%.
   - Caveat: release dates lag sequencing, and the data are research-heavy. Illumina already reports about 83% of high-throughput Gb on the X.
   - [ENA count API](https://www.ebi.ac.uk/ena/portal/api/count?result=read_run&query=instrument_model=%22Illumina%20NovaSeq%206000%22%20AND%20first_public%3E=2026-07-01%20AND%20first_public%3C=2026-09-30%20AND%20base_count%3E=10000000000) [F644, F627, D064]

5. **Genome-scale work is converting fastest, but most of what remains on the 6000 is still large, convertible runs.**
   - For deep samples of 60 Gb or more, the X's share rose from 8.6% to 20.3% to 39.8% (Q3 2024–Q3 2026).
   - About 74% of remaining public 6000 output is still in samples of 10 Gb or more. The fast-growing count of tiny 6000 runs carries only about 4% of 6000 output.
   - So the tail is not shrinking to a permanent small-run rump.
   - [ENA count API](https://www.ebi.ac.uk/ena/portal/api/count?result=read_run&query=instrument_model=%22Illumina%20NovaSeq%206000%22%20AND%20first_public%3E=2026-07-01%20AND%20first_public%3C=2026-09-30%20AND%20base_count%3E=150000000000) [F629, D059, F645]

6. **GEO and SRA show the 6000's share of deposits falling about 12 points a year, with no plateau.**
   - The 6000's share of human and mouse 6000+X samples in GEO went 96.9% → 82.4% → 70.5% (Q3 2024 to Q3 2026). Counting series gives the same path.
   - Counting all 15 human X platform records, the X's human series share went 4.3% → 19.3% → 31.6%.
   - In SRA, the X's run share went from about 3% to 27% in two years.
   - A simple trend gives roughly +9 to +11 points for 2027 in public data. That is a lagging read on research, not a forecast of clinical points.
   - [NCBI GEO](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=gds&term=%28GPL24676[ACCN]%20OR%20GPL24247[ACCN]%29%20AND%20gsm[ETYP]%20AND%202026/07/01:2026/09/30[PDAT]&retmax=0) [F577, F578, F753, D066, F596]

7. **No slow-decay "clinical pocket" appears in public data.**
   - Cancer-tagged GEO series are leaving the 6000 faster than the rest: the 6000's share fell 12.9 points versus 8.4 points.
   - Series mentioning patients or clinical use fell about 8 points (93.5% → 85.5%).
   - Caveat: these keywords mostly catch research papers, and the X counts here miss the X Plus model, which understates the X's share.
   - [NCBI GEO](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=gds&term=GPL24676[ACCN]+AND+gse[ETYP]+AND+%28cancer+OR+tumor+OR+tumour%29+AND+2026/07/01:2026/09/30[PDAT]&retmax=0) [F919, F920]

8. **Robustness checks on GEO hold up.**
   - The Q3 2026 jump in human 6000 samples (36,312, a 7-quarter high) is broad-based, not one giant study. The 10 largest series are at most about a third of it.
   - Earlier mouse spikes came from 2021-era studies released late.
   - These checks mainly show that GEO measures publication, not current 6000 use.
   - [NCBI GEO](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=gds&term=GPL24676[ACCN]+AND+gsm[ETYP]+AND+2026/07/01:2026/09/30[PDAT]&retmax=0) [F528, F551, F552]

9. **Illumina's own list prices show it raised 6000 consumables while holding the X, then trimmed the 6000.**
   - In Illumina's Open Offer catalog, 6000 reagent kits rose 15.1% between Sep 2022 and Feb 2024. The S4 300-cycle kit went from $14,400 to $16,578, while the X 10B kit stayed at $9,600.
   - UConn's pass-through prices then show 6000 kits cut 3.9–5.2% by Feb 2026.
   - Calgary's internal S4 price fell about 23% net over two years.
   - So list moves explain the earlier gap but not the 2024–26 widening.
   - [Open Offer addendum](https://emea.Illumina.com/content/dam/illumina-marketing/documents/applications/cancer/09-29-2022_Addendum.pdf) [F538, F479, F672]

10. **The 6000 tail is still sold at high prices to the users who remain.**
    - Core S4 flow-cell prices cluster at $20–23K across 2024–26, near the $21.7K GSA price.
    - UNMC still charges $9.95–14.79/Gb for 6000 runs.
    - MIT raised its S4 lane 8% to $5,400 while listing an X lane about 55% cheaper per read.
    - UCLA's S4 lane price fell 27% from 2019 to 2023 before the X cut it again.
    - An Italian children's hospital (Bambino Gesù, Rome) listed 6000 kits in Jan 2026 at reference prices of about €7.5–21 per Gb, roughly 3–4x a recent 25B tender.
    - [Bambino Gesù annex](https://img.ospedalebambinogesu.it/images/2026/01/26/113054540-40a836e1-b4f2-4e33-9ff3-9f07b8357c00.pdf) [F262, F243, F1040, F150, F826]

11. **No recorded clinical test in NCBI's Genetic Testing Registry (GTR) has moved from the 6000 to the X.**
    - The X records with traceable histories came from older NextSeq 550 or HiSeq 2000 instruments, not the 6000. Examples are Michigan's BRCA panel and Labcorp's MaterniT NIPT.
    - So the observed 6000-to-X conversion count in this registry is zero.
    - GTR is self-reported and lightly maintained, so this is a weak signal of regulated-lab inertia, not a rate.
    - [GTR version history](https://www.ncbi.nlm.nih.gov/gtr/tests/509980/versions/) [F995, D090]

12. **Mayo Clinic Laboratories keeps re-filing its tests on the 6000.**
    - Mayo holds 104 of the 130 GTR records naming the 6000. None of its records names the X.
    - Its Ehlers-Danlos panel went through six versions from 2022 to April 2026 and still names the 6000.
    - The field may lag the lab's actual instruments, so this names a holdout rather than proving 6000 use.
    - [GTR record 603740](https://www.ncbi.nlm.nih.gov/gtr/tests/603740/) [F123, F960, F961]

13. **Other named clinical tests still declare the 6000.**
    - Tempus's flagship xT tissue test declares the 6000 (lab review Nov 2025).
    - UCSF500 was re-filed on the 6000 in Jan 2026.
    - JAX Genome, a clinical genome test registered in late 2024, names the 6000.
    - Several non-Mayo 6000 records have not been touched in years, so stale listings are common.
    - [GTR record 613444](https://www.ncbi.nlm.nih.gov/gtr/tests/613444/) [F962, F971, F996]

14. **Labcorp filed a new whole-genome MRD test on the 6000Dx, 13 months after moving its NIPT line to the X Plus.**
    - Plasma Detect Genome MRD was registered on 8 Dec 2025 on the regulated 6000Dx.
    - This fits a pattern in which price-sensitive NIPT moves first while new regulated assays start on Dx-grade 6000 boxes.
    - The 6000Dx may only be the validation platform.
    - [GTR record 619625](https://www.ncbi.nlm.nih.gov/gtr/tests/619625/) [F970, D091]

15. **The regulated 6000Dx lock is narrower than "permanent tail" language implies.**
    - The 6000Dx product page names no assays.
    - Its US intended use is targeted panels only, "not intended for whole-genome" sequencing.
    - So true Dx-locked volume is small. However, FDA-approved tests such as FoundationOne CDx name the RUO 6000 in their approvals, so the regulated tail extends beyond Dx kits.
    - [6000Dx page](https://www.illumina.com/systems/ivd-instruments/novaseq-6000dx.html) [F534]

16. **Illumina's end-of-life policy gives it control of the tail's timetable.**
    - Service typically ends five years after an end-of-life notice.
    - Service prices may rise from the notice date.
    - Individual kits can be discontinued early "if demand is low".
    - Resold end-of-sale boxes are generally not eligible for service.
    - Government buyers say no third-party 6000 service exists, so Illumina keeps 100% of it at about $110–145K per box a year.
    - [EOL policy](https://emea.illumina.com/content/dam/illumina-marketing/documents/terms-conditions/1000000117071_01_Product_End_of_Sale_End_of_Life_Policy.pdf) [F897, F896, F899]

17. **Service contracts show 6000s kept running in parallel with X boxes, and some fading out.**
    - Labs paying for 6000 service:
      - The Navy's medical research command (Dec 2025), CDC and NIEHS renewed 6000 service plans.
      - NCI Frederick keeps a 6000 on a top-tier Gold plan through Jan 2027 alongside at least two X systems.
      - NHS Leeds signed a £119K 6000 maintenance contract in Feb 2026.
    - A fleet that faded out: Taiwan's national health research institute (NHRI) paid about $110K per box a year to service four 6000s while buying only about $24K of consumables per box, versus a fleet average of about $670K. It let the contract lapse in Dec 2024.
    - [Navy NMRC notice](https://govcontractfinder.com/contracts/comprehensive-full-service-maintenance-repair-plan-for-illum-N3239826Q4072) [F039, F619, F340, F800, D078]

18. **Illumina has put the 6000 software in maintenance mode.**
    - The 6000 control software has had one release in 35 months (Aug 2025).
    - The X has had six releases in about 37 months, including support for the new 5B flow cell.
    - The 6000's lab-system (LIMS) integration has had only security patches in 2026.
    - This is a de-prioritization signal. It says nothing direct about conversion pace.
    - [6000 downloads](https://emea.support.illumina.com/sequencing/sequencing_instruments/novaseq-6000/downloads.html) [F1053, F1054, F1112]

19. **More research cores have dropped the 6000 from their price lists.**
    - Canada's largest pediatric genomics core (TCAG, Toronto) lists the 6000 only as "Contact facility" while pricing nine X lanes.
    - UConn deactivated all its 6000 products in 2026 and now sends high-throughput work to The Jackson Laboratory's X lanes.
    - [UConn catalog](https://honeycrisp.core.uconn.edu/products/392) [F489, F947]

20. **Clinical conversions take about two years.** Adaptive says it will move all clonoSEQ MRD testing to the X Plus "over the next two years" from H2 2025, which implies completion around 2027. The move is from the NextSeq, not the 6000, so it shows only that conversions run long. [Adaptive 10-K](https://www.sec.gov/Archives/edgar/data/1478320/000119312526076902/adpt-20251231.htm) [F840]

21. **Legacy reagent buying continues after end of sale.** Taiwan's Tri-Service General Hospital bought 16 iSeq 100 reagent sets in Sep 2026, a year after the iSeq's end of sale, plus NextSeq 500/550 kits. This is a small, non-6000 example that legacy boxes keep earning reagent revenue. [Taiwan PCC](https://pcc-api.openfun.app/api/tender?unit_id=A.5.24&job_number=HJ15568P448) [F980]

## 1B. Discounting will speed up

The thesis says Illumina's discounting will speed up, while the street models it as flat. Two forces drive it. The first is the 35B flow cell. The second is heavy short-read competition from Ultima and Element at much lower cost per genome. Large accounts will use that leverage to win bigger extra discounts.

The new evidence is strongest on three points:

- **Rival price gaps at research cores.** These gaps are concrete and dated. Ultima is about 2–3x cheaper per Gb, and it is fully passed through to customers.
- **Hidden deflation inside the X price ladder.** Cuts land on the 10B and on core markups, not on the headline 25B price.
- **Bespoke deals for large accounts.** Illumina's published schedule cannot produce the discounts large accounts get, so those must come from individual deals.

It is weakest on direct proof that Illumina's net price to big accounts is falling faster. Most observable prices are core resale rates or government purchases, and those mostly sit near list. The watch-outs section covers that.

1. **A research core sells an all-in Ultima genome for $192, and sequencing is about 70% of that price.**
   - **The price list.** UMGC lists a 30x human genome on the Ultima UG100 at $192 internal and $221 external, in batches of 24. That price includes QC, PCR-free library prep, sequencing and variant calling. A 60x genome is $238 and 90x is $329. AVITI is $407 in batches of 4. The page lists no Illumina genome at all.
   - **Our split of the batch prices.** The prices imply about $3,290 per Ultima wafer, which matches UMGC's $3,204 wafer list price. Prep and analysis add only about $55 per sample. So sequencing is about $137 of a $192 genome, or about $1.1–1.3/Gb.
   - **Why it matters.** For research genomes, sequencing is not a 5–10% cost line. A vendor's price gap feeds straight into the customer's buying decision.
   - [UMGC WGS page](https://genomics.umn.edu/service/human-whole-genome-sequencing) [D099, F005, F1069]

2. **At realistic output, Ultima is about 2.3–2.7x cheaper per Gb than an Illumina 25B lane at core internal rates.**
   - UMN's Ultima wafer costs $3,204 internal, or $3,688 external, at its cheapest "Savings" tier. UMN's three speed tiers differ by only about 5%. At the 2.5–3.0 Tb per run UMN itself quotes, that is $1.07–1.28/Gb.
   - UCSD's 25B-300 lane was $2,800 UC and $3,836 outside (Oct 2025 sheet), or about $2.92 and $4.00/Gb.
   - The gap is 2.3–2.7x internal and 2.7–3.3x external. That is lower than the 3.3–3.9x the source first claimed using maximum output.
   - [UMN UG100 page](https://genomics.umn.edu/service/ug-100-sequencing) [D003, F028, F029]

3. **Ultima's whole-workflow genome costs less than Illumina's sequencing step alone at another core.**
   - At UCSD's 25B lane rate, the ~100–120 Gb of a 30x genome costs about $290–350 internal for sequencing alone, before prep.
   - UMGC's complete Ultima genome is $192–221, about 35–55% below that.
   - All-in X genomes elsewhere are about $650: C$650 at TCAG (Apr 2025) and $650 at Johns Hopkins (unverified).
   - Caveat: large accounts pay Illumina less than core rates.
   - [JHU GRCF](https://grcf.jhmi.edu/?p=15308) [D002, F017]

4. **A Canadian cancer institute prices Ultima genomes 63–65% below its Illumina genomes, or about 33% on a same-period comparison.**
   - The Ontario Institute for Cancer Research (OICR) lists a 30x research genome at C$435 on Ultima (May 2025, 20-sample minimum), against C$1,181 on Illumina (May 2024 prices).
   - The Illumina price is a year older. Against TCAG's C$650 X genome from the same period, the Ultima discount is about 33%.
   - That is still sizeable, but half the headline.
   - [OICR prices](https://genomics.oicr.on.ca/?p=2804) [F778, D075]

5. **Illumina reagents inside a core's X genome still cost well above rival marketing claims.**
   - TCAG's C$650 X genome (~US$470) splits into about C$140 of PCR-free prep, about C$330 (~US$240) of sequencing at its 25B lane rate, and about C$180 for QC and analysis.
   - Ultima markets about $80 per genome. Roche lists $150 for an AXELIOS duplex 30x genome, excluding prep.
   - So the Illumina sequencing piece is about 1.6–3x the rivals' claims. That leaves room for research price pressure.
   - [TCAG price list](https://www.tcag.ca/documents/facilities/TCAG-NGS-Price-List%20April%202025.pdf) [D043]

6. **Inside the X family, the smaller 10B flow cell is being repriced toward the 25B. This is per-Gb deflation that headline 25B prices do not show.**
   - **UCLA** passes Illumina reagents through "at cost". Its 10B-300 lane fell 21% ($2,234 → $1,765.67) between 2023–24 and Jul 2026. The 25B was flat ($3,538 → $3,512.47). On Illumina's output specs, the 10B's per-Gb premium fell from about 68% to 34%.
   - **TGen** cut the 10B about 16% while raising the 25B, so the premium fell from 1.45x to 1.13x.
   - **Other cores (2026):** Northwestern 1.25x, Berkeley 1.38x, Carver 1.48x, MD Anderson 1.50x and KUMC about 1.03x.
   - Berkeley's own stated real output puts its 25B at about $2.3/Gb.
   - [UCLA pricing](https://www.uclahealth.org/departments/pathology/research-services/technology-center-genomics-bioinformatics-tcgb/pricing) [D018, F054, D005, F223, D008, D034, D035]

7. **The University of California's two X cores cut lane prices 9–23% in the latest cycle, while Illumina's 25B list rose about 3%.**
   - **UCSD's 2026 sheet:** 25B-300 $2,800 → $2,550 (−8.9%), 25B-100 −22.9%, 10B-300 $1,700 → $1,400 (−17.6%). Some rates are pending committee approval.
   - **UCSF's CAT core:** 25B-300 $2,850 → $2,551 (−10.5%), 10B-300 −16.5%.
   - The two cores now charge within $1 of each other, and their markup over per-lane list fell from about 1.40x to 1.24x. CAT's markup per lane fell from about $850 to $490.
   - This fits a lower net price under the UC-wide Illumina agreement. A cut in core overhead would look the same. Smaller users got the bigger cut.
   - UC Berkeley now sends all its lanes to CAT. A stale UC Riverside rate was 24% higher, which shows that scale earns the low price.
   - [UCSD IGM 2026 rates](https://igm.ucsd.edu/sites/default/files/docs/2026%20rates%20flow%20cell%20fix.png) [F1037, D092, F817, D080, D093, F1021]

8. **Illumina's published discount schedule caps the 25B discount at 12%, so the steep discounts experts describe must be bespoke.**
   - In the Open Offer appendix (Jan and May 2024), the 25B discount runs from 3% to 12% at the top spend tier. The 6000 and 10B column goes up to 22%. The source gives the top-tier threshold inconsistently, as ≥$50M in one place and ≥$100M in another.
   - At the top tier, the 25B nets about $1.76/Gb. The cheapest public 25B price is Novogene's $2.55/Gb (Sep 2026), about 45% higher.
   - Experts' claims that big accounts pay "half or a quarter" of small labs imply roughly $0.9–1.3/Gb at the largest clinical accounts. Those prices are only reachable through individual contracts.
   - [Open Offer Appendix 1](https://supportassets.illumina.com/content/dam/illumina-marketing/documents/applications/cancer/1-25-2024_appendix-1.pdf) [F540, D051]

9. **Taiwanese outsourced genome prices imply the winning service lab pays at most about $2/Gb for Illumina reagents.**
   - Three hospital awards (Taipei VGH Feb 2025, Kaohsiung VGH Dec 2025 and Jan 2026) all priced WGS at NT$12,800 (~US$410), one of them including blood extraction. If reagents are 45–60% of that price, they cost about $1.8–2.5/Gb.
   - The national health research institute (NHRI) paid NT$9,800 (~US$305) in Oct 2024. That leaves about $0.75–2.0/Gb for reagents plus margin, at or below the Open Offer top tier.
   - Caveat: all three hospital awards went to one vendor (Genomics BioSci). Centogene, an AXELIOS buyer, bid NT$13,995 and was disqualified on paperwork.
   - [Kaohsiung VGH award](https://pcc-api.openfun.app/api/tender?unit_id=3.32.82&job_number=ST1412017) [D070, D072, F744]

10. **GeneDx is planning on lower reagent prices in 2027, and its economics push it to ask for them.**
    - The CFO said a genome costs "nearly twice" an exome, "almost entirely higher reagent costs", and expects those costs to fall as "manufacturers advance their technology". He guided cost per test flat for H2 2026 with "step improvements in 2027" (Q2 2026 call).
    - Adjusted cost of services grew faster than revenue in Q2 2026 (+12.1% vs +11.4%). Adjusted gross margin fell from 74% (Q3 2025) to 70.4%.
    - Its FY26 guidance floors imply exome/genome revenue per test of $3,419, down 7.7%. That requires a 14% quarter-on-quarter recovery in Q4.
    - Rough arithmetic puts GeneDx's extra reagent cost per genome Gb above negotiated 25B levels. That is a motive to seek cuts. The link to the 35B flow cell is our inference.
    - [GeneDx Q2 2026 call](https://www.webull.com/news/15381684706632704) [F568, F567, D055, F189, D015]

11. **MGI's rival flow cells got 36% cheaper at UCLA while Illumina's 25B held flat.**
    - UCLA's DNBSEQ-T7 flow cells fell 36–37% between Mar 2024 and Jul 2026: the 300-cycle went from $4,736 to $3,043.
    - On an assumed output of about 1.5 Tb per flow cell, Illumina's per-Gb premium over MGI at this core rose from about 12% to about 73%.
    - The output assumption drives the level but not the direction.
    - [UCLA pricing](https://uclahealth.acquiaedge.net/departments/pathology/research-services/technology-center-genomics-bioinformatics-tcgb/pricing) [F058, D001]

12. **UMGC cut its AVITI prices three times in about 14 months.**
    - About 40% in Jul 2024, then about 20% in Dec 2024, at which point it said AVITI had become cheaper than the 25B.
    - Then an Element upgrade gave 50% more output at the same price in Sep 2025, cutting cost per read by 33%. UMGC now says AVITI saves "several hundred to one thousand dollars per billion reads" against Illumina's cheapest platform.
    - Over a similar window, the rivals' per-read moves at this one core were roughly 2–3x larger than the 9–17% X lane cuts at UC cores.
    - [UMGC news](https://genomics.umn.edu/news/aviti-upgrade-complete) [F140, F1052, D098]

13. **Illumina customers get more data per dollar than the price sheet shows.**
    - A practitioner's measured 25B runs averaged 29.4B read pairs, about 8,800 Gb across 37 samples. That beats the 8,000 Gb spec, so it gives about 9% more data per dollar ($1.87/Gb at the $16,480 list). The same author says groups negotiate about 15% discounts (Jun 2025).
    - Separately, Illumina's reagent-rental schedule adds about $10,409 per X run to recover the instrument price. That is about $520K a year at 50 runs, and it inflates consumables per box on rental placements.
    - [LessWrong post](https://www.lesswrong.com/posts/x3DzjEofP94ki9iTp/how-much-data-from-a-sequencing-run) [F146, F558]

14. **Core lane prices sit 26–70% above Illumina's per-lane list, so flat or rising core prices cannot show that Illumina's own price is holding.**
    - The 25B-300 per-lane list is about $2,060. Core lane prices: MD Anderson $2,595, UCSD $2,800, Northwestern $3,000, TGen $3,136.63, Carver $3,380 and UCLA $3,512.47.
    - Carver's Aug 2026 card ($3,380 per lane, $3,180 at 8+ lanes, external +30.8%) implies reagent-plus-margin of 1.25–1.35x list, once its separate "kit provided" labor fee is backed out.
    - A 15% Illumina cut on a lane priced 50% above list moves the core rate only about 10%.
    - [Carver pricing](https://biotech.illinois.edu/dna-services-core/dna-services-pricing/) [D019, F164, F501]

15. **More cores trimmed small-flow-cell prices.**
    - Pitt cut its 1.5B lanes 8–20% between Nov 2024 and Jun 2025. The 2024 figures come from a search snippet.
    - Fred Hutch (page dated Sep 2026) prices the 10B at about 1.5x the 25B per Gb. Its 25B works out to about $2.05–2.64/Gb internal.
    - [Pitt pricing](https://www.genomics.pitt.edu/about/pricing) [F357, F657]

16. **At KUMC the discount lands on the 10B, not the 25B.** The internal 25B-300 price ($23,872) is about 99% of the GSA price, while the 10B-300 ($9,255) is about 64% of GSA. Per Gb the two now cost roughly the same. [KUMC pricing](https://www.kumc.edu/research/genome-sequencing-facility/services/illumina-services/pricing.html) [F386]

17. **Taiwanese tenders show discounts growing with order size, and per-test exome prices falling even without competition.**
    - Taichung VGH's Sep 2026 reagent award took 6% off budget on small kits but 21% on the larger P3 kit. Most of that gap was the hospital's own reserve price. Bid-to-award cuts were about 4% on small kits and 12% on large ones.
    - NTUH's NT$297M three-year WGS reagent-plus-instrument deal (Feb 2026) cut the sole Illumina distributor's bid 10.8%. The reviewer notes this is a routine procedural step.
    - Taipei VGH's exome-plus-mitochondria test fell 21.7% (NT$11,500 → 9,000) with one bidder and flat annual volume.
    - [Taichung VGH award](https://pcc-api.openfun.app/api/tender?unit_id=3.32.81&job_number=115A018) [F1129, F863, F809]

18. **One government research buyer may have paid about $2/Gb for 6000 S4 kits in Dec 2023, but the unit is uncertain.**
    - NHRI's award of NT$2.93M for 16 S4-300 kits works out to about US$5.9K per kit, 64% below list. The quantity is labeled "estimated demand", so the per-kit price is unconfirmed.
    - Its kit buying fell from 57 in 2020 to 16 in 2023.
    - [NHRI award](https://pcc-api.openfun.app/api/tender?unit_id=92019239&job_number=112A0C0676) [D067, F712]

19. **Deflation also reaches below the X.** In May 2024, Illumina cut NextSeq 1000/2000 list prices 20–30% per kit with its newer XLEAP chemistry, about 36% per read on the P3 300-cycle kit. Legacy kits stayed at the old list. This is already in reported history, but it shows the pattern. [Open Offer catalog](https://assets.illumina.com/content/dam/illumina-marketing/documents/applications/cancer/7-26-2024-appendix-1.pdf) [F548]

20. **Element's usage is growing faster than its box count, and it is moving toward clinical work.**
    - Element passed 450 AVITI systems in 2025 (+60%).
    - Kit shipments reportedly more than doubled, which would imply about 25% more use per box. Clinical research reportedly passed 25% of revenue.
    - The last two figures are unverified, and the base is still under 1% of Illumina's clinical consumables.
    - [GenomeWeb](https://www.genomeweb.com/node/647886) [F098, F100]

21. **Element may reach a certified EU clinical sequencer before Illumina has an X Dx.** Element earned ISO 13485 in Jun 2026 and plans an AVITI Dx (IVDR Class A) in "select countries" in late 2026. Class A is self-declared, AVITI is mid-throughput, and the launch is still a plan. [Element release](https://www.elementbiosciences.com/news/element-biosciences-achieves-iso-13485-certification-establishing-quality-foundation-for-forthcoming-diagnostic-applications) [F561]

22. **Some 6000 tail conversion is contestable by Element rather than captured by the X.**
    - UNMC still sells S4 runs at about $9.95/Gb. Its in-house alternative is AVITI at about $8.67/Gb, not an X.
    - The NCI's 25B costs about $2.15/Gb.
    - [UNMC pricing](https://www.unmc.edu/research-resources/resources/cores/genomics-core/pricing.html) [D024]

23. **In Taiwan, Element's channel has entered a clinical medical center and taken over a former Illumina partner.**
    - Chi Mei Medical Center bought a NT$9.96M "high-throughput NGS sequencer" in Feb 2026 from Element's Taiwan channel. The brand is inferred, not stated.
    - That channel, Asia Pathogenomics, signed an infectious-disease sequencing MOU with Illumina Taiwan in Aug 2023. Which sequencer runs its hospital contracts is not verified.
    - [Chi Mei award](https://pcc-api.openfun.app/api/tender?unit_id=06606103&job_number=114B01342H1) [F748, F888]

24. **Long-read is taking some hospital genomics budget in Taiwan.**
    - NTUH's Oxford Nanopore contracts grew from NT$5.4M (chips only, 2024–26) to NT$19.1M (2025–27, including an instrument), so the two are not like-for-like.
    - Cathay General spent its government grant mostly on UK-origin long-read gear (likely Oxford Nanopore). Long-read consumables alone were about 1.9x a US-origin reagent lot.
    - This is budget competition, not short-read discounting.
    - [NTUH award](https://pcc-api.openfun.app/api/tender?unit_id=3.9.20.1&job_number=TD14E130) [F750, F871]

25. **A national genomics buyer gets steep volume tiers.**
    - Genomics England's Dec 2024 Oxford Nanopore award prices option-tranche flow cells about 53% below the first tranche (~£631 vs ~£1,342). Unsplit consumables in the first tranche probably overstate the gap.
    - This is a non-Illumina example of large-buyer leverage.
    - [Find a Tender](https://www.find-tender.service.gov.uk/Notice/039504-2024) [F106]

26. **Illumina is building tools to price by segment.**
    - A Jun 2026 Illumina posting for an Associate Director of Pricing Transformation describes pricing "by market, by customer type, and by application". It covers "pay for ownership, pay for consumption, and pay for performance" models, plus new-product pricing.
    - That is a mechanism for deeper effective cuts without a list change. It could also protect price. The link to the 35B is our inference.
    - [Job posting](https://resumegeni.com/jobs/associate-director-pricing-transformation-san-diegohybrid-at-illumina-us-california-san-diego) [F559]

## 1C. Volume growth will slow

The thesis says Illumina's volume growth will slow from about 30% to about 25%. The near-term levers are used up. MRD and whole-genome testing are too small to offset a maturing NIPT market. Sequencing cost is no longer what limits demand.

The new evidence gives strong support to two parts of this:

- **The fast-growing clinical tests use very little sequencing data.** MRD blood draws, amplicon MRD and newborn programs each amount to a fraction of a percent of Illumina's roughly 800M Gb a year of high-throughput output.
- **Payers, not sequencing prices, are the binding constraint.** Denials and collection rates now set how fast clinical tests can grow.

The NIPT picture is mixed. US pregnancies are flat to falling and the combined US lab pool grows in high single digits. But the largest lab re-accelerated in 2026 and some markets are still adding uptake (see watch-outs).

None of these items measures Illumina's total Gb growth directly.

1. **GeneDx's move away from genomes means its sequencing output grows far slower than its test count.**
   - In GeneDx's insurance outpatient channel, genomes fell from close to 40% of volume in Q1 2026 to 32% in Q2. Management expects about 30% "or slightly lower" in H2. In July 2026, reflex exome volume beat genome volume for the first time.
   - Using illustrative depths, a genome is about 100 Gb and an exome about 10 Gb. On those figures, GeneDx's guided test growth of at least 30% becomes roughly +18% in Gb at a 40% genome mix, or +7% at 35%.
   - These are illustrative assumptions. Trios scale both.
   - [GeneDx Q2 2026 call](https://www.webull.com/news/15381684706632704) [D013, F187]

2. **GeneDx's growth is capped by reimbursement, not sequencing capacity.**
   - **Revenue per test is falling.** Exome/genome revenue per test fell about 12% y/y in Q2 2026, from about $3,700 to $3,258.
   - **Collections are weak.** Outpatient genome collection is stuck at about 32%, down from 43% a year earlier.
   - **The guidance cut was mostly price.** In May, management cut FY26 revenue guidance about 12%, to $475–490M. It trimmed volume growth only from 33–35% to at least 30%, while revenue growth fell to at least 20%. The CFO said the first guide "proved to be too aggressive".
   - [GeneDx Q2 2026 release](https://www.sec.gov/Archives/edgar/data/0001818331/000162828026051852/exhibit991-q22026pressrele.htm) [D017, F188, F192]

3. **GeneDx's new payer coverage is real but tiny in Illumina terms.**
   - GeneDx guides 33,200 exome/genome tests for Q3 2026, about 7.5K more per quarter than a year earlier.
   - At 8–125 Gb per test, that is about 0.25–3.7M Gb a year, or 0.03–0.5% of Illumina's high-throughput base.
   - [GeneDx Q2 2026 release](https://www.biospace.com/press-releases/genedx-reports-second-quarter-2026-financial-results) [D102]

4. **Insurer friction on lab and genomic claims is rising fast.**
   - XiFin analyzed more than 30M claims. Its blended denial rate for clinical lab, molecular and genomic claims rose from 8.0% in 2024 to 11.2% in 2025.
   - Prior authorization's share of molecular and genetic denials more than doubled, from 13.1% (2021) to 27.6% (2025). That implies roughly 3x more prior-authorization denials per claim, an illustrative figure.
   - A survey of 200 US physicians found 87.5% cite reimbursement as a barrier to NGS testing and 72% cite prior authorization. That survey's data date from 2020, so it is stale.
   - Caveats: XiFin's rate blends all lab types, and its client base may not be representative.
   - [CLP Magazine on XiFin](https://clpmag.com/?p=92893) [F347, F348, D033, F345]

5. **Natera's MRD franchise grows fast but uses very little sequencing.**
   - Clinical MRD blood draws are 94–96% of Natera's oncology tests. Non-MRD oncology is only about 6–14K tests a quarter.
   - At the Q2 2026 run-rate of about 1.13M MRD draws a year, the standard assay uses about 0.2–0.3M Gb a year. That is about 0.02–0.03% of Illumina's high-throughput output, or about 0.3–0.5% if every draw were the deeper genome version.
   - The one-time tumor sequencing per new patient adds more and scales with new patients.
   - [Natera Q2 2026 deck](https://www.sec.gov/Archives/edgar/data/0001604821/000160482126000015/ntra-20260630xex992.htm) [D039, F266]

6. **Natera's MRD growth is not accelerating.**
   - Quarterly unit adds were steady at +20K to +24K through Q1 2026.
   - The record +34K in Q2 2026 included catch-up after weather suppressed Q1 volume.
   - Management said it does not expect a new record in Q3 (call summary, not a checked transcript).
   - [GuruFocus summary](https://www.gurufocus.com/news/9015362/natera-inc-ntra-q2-2026-earnings-call-highlights-record-volumes-and-raised-guidance-signal-strong-momentum) [F176]

7. **Medicare claims show fewer MRD draws per patient than expert models assume, at a falling price.**
   - In CMS fee-for-service data, likely for 2024, Natera billed 25,746 Signatera services to 11,922 patients. That is 2.16 draws per patient a year, below the 3–4 a year experts use.
   - Medicare's payment per service fell 8.3% ($3,838 → $3,519) while services rose 87%. MRD is growing as a high-count, low-Gb line whose price is falling.
   - [CMS data](https://data.cms.gov/data-api/v1/dataset/92396110-2aed-4d63-a6a2-5d6207d46a29/data?filter[HCPCS_Cd]=0340U&size=5) [F414, D037, D040]

8. **Outside Natera, MRD is still small.**
   - Tempus ran about 9K MRD tests in Q2 2026, about 3% of Natera's volume.
   - Management said "only about 10% of our sales force is selling MRD today" (third-party transcript).
   - That also means upside if Tempus scales.
   - [Tempus Q2 2026 call](https://allmind.ai/earnings/event/2940116) [F293]

9. **Other headline growth programs are rounding errors in Gb.**
   - Adaptive's clonoSEQ ran 36,111 tests in Q2 2026 (+43%). At an estimated 0.2–1 Gb each, that is about 0.004–0.02% of Illumina's annual high-throughput Gb.
   - The GUARDIAN newborn genome study reached 30,000 babies by Oct 2026. It is enrolling about 700 a month, so a 100K scale is about 8 years away. At its current pace it uses about 0.1% of the base.
   - [GeneDx ICoNS release](https://finviz.com/news/399837/genedx-presents-new-evidence-advancing-genomic-newborn-screening-at-icons-2026) [F1029, F416, F1017, D095]

10. **Even Taiwan's largest public hospital genome contract is immaterial.**
    - Taichung VGH's NT$117.55M three-year WGS deal is roughly 3,000 genomes a year, assuming NT$12,800 each.
    - That is about 0.31M Gb, or 0.04% of Illumina's base.
    - [Taichung VGH award](https://pcc-api.openfun.app/api/tender?unit_id=3.32.81&job_number=114Y-R5) [D069]

11. **The combined US NIPT pool at Natera and Myriad grew only about 8% in Q2 2026.**
    - Natera's non-oncology tests, mostly NIPT and women's health, grew +21% in Q4 2024. Growth slowed to +5–7% through 2025 (FY25 +7.4%), then recovered to +9.8% (Q1 2026) and +12.5% (Q2 2026), with a small sequential dip.
    - Netting Myriad's prenatal loss of 15K tests, the two labs together grew +8.2%.
    - Both labs run on Illumina, so share moving between them is neutral for Illumina's NIPT volume.
    - Caveats: Natera's line includes organ health, and Myriad's includes carrier screening.
    - [Myriad Q2 2026 release](https://www.sec.gov/Archives/edgar/data/0000899923/000089992326000070/ex991mygn-xearningsrelease.htm) [D014, F121, F131]

12. **Myriad's prenatal business is shrinking in both volume and price.**
    - **Volume:** prenatal tests fell 9% in Q2 2026 and 11% in H1. Volume is about 17% below the Q1 2025 peak, after four straight yearly declines.
    - **Price:** revenue per test fell from $299 to $276. The 10-Q blames "declines in reimbursement".
    - **Revenue:** revenue fell 16%, made up of about −9% volume and −8% price. Myriad cut FY26 revenue guidance to $770–790M, citing "lower Prenatal Health test volumes".
    - Caveats: management also blames company-specific execution (see watch-outs), and the earlier quarterly series is unverified.
    - [Myriad 10-Q](https://www.sec.gov/Archives/edgar/data/0000899923/000089992326000072/mygn-20260630.htm) [F184, F212, F213, F214, D021]

13. **BillionToOne's test growth slowed about 10 points in one quarter.**
    - Delivered tests grew +44.6% in Q1 2026 but +35.2% in Q2.
    - Accessioned tests went from +38% to +33%.
    - Part of the slowdown is an easy Q1 2025 comparison.
    - [BillionToOne 8-K](https://www.sec.gov/Archives/edgar/data/0002070849/000207084926000048/a991blln-earningspressrele.htm) [F307]

14. **The US birth pool for NIPT is shrinking slowly, which leaves limited headroom.**
    - **Births and fertility:**
      - US births were 3,606,400 in 2025, down 1%.
      - The fertility rate kept falling through Q2 2026: 53.7 → 52.7 per 1,000 women aged 15–44.
      - A growing female population offsets part of that, so births likely fall only about 0.5–1.5% a year.
    - **Where the decline sits:**
      - Rates for ages 20–29 fell 6–8.5% over two years.
      - Hispanic fertility fell fastest, though those rows could not be re-checked.
    - **What it means for NIPT:**
      - NIPT already reaches an estimated 70–80% of US pregnancies.
      - Total test headroom is only about 24–41%, at most about 5–9% a year over 4–5 years.
      - So NIPT growth has to come from share or deeper tests.
    - [CDC NCHS](https://cdc.gov/nchs/pressroom/releases/20260409.html) [D030, F295, D086, F940, F941, F945]

15. **Taiwan's births fell 20% in 2025.** There were 107,812 births in 2025, down from 134,856, the 10th straight annual decline. Press reports put early 2026 down another ~15%, which is unverified. This explains local NIPT contract declines but is tiny in Illumina terms. [PeopleNews](https://www.peoplenews.tw/?p=11380) [F903]

16. **Some Taiwanese hospitals are cutting or down-tiering NIPT, but all Taiwanese NIPT is immaterial.**
    - Taipei VGH's Taoyuan branch roughly halved its annual NIPT outsourcing spend between 2020–21 and 2023–26.
    - NYCU Hospital moved its spend from an expanded 38-condition NIPT, which uses deeper sequencing, to basic NIPT. The expanded test went from 77% to 25% of NIPT spend, and total NIPT spend fell 27%.
    - All the Taiwanese NIPT contracts found add up to well under 0.01% of Illumina's Gb.
    - [Taiwan PCC](https://pcc-api.openfun.app/api/tender?unit_id=A.9.6M.1&job_number=115108L54) [F782, F989, D077]

17. **European NIPT is still adding uptake, but the extra tests barely register.**
    - Dutch NIPT tests grew 8.8% in 2024.
    - German statutory-insurance use rose from about 32% to almost 50% of pregnancies.
    - Together that is about 130K extra tests, or 0.02–0.03% of Illumina's Gb.
    - A cross-party Bundestag motion seeks NIPT monitoring and an expert panel, with results due by end-June 2027. That is a speculative overhang, not a coverage cut.
    - [Bundestag hib](https://www.bundestag.de/presse/hib/kurzmeldungen-1140288) [D094, F1019]

18. **At BillionToOne, a fast-growing customer, growth comes from price and payer coverage, not cheaper sequencing.**
    - Its FY25 10-K says third-party payers are over 90% of revenue and growth is coverage- and contract-driven. Some states' Medicaid programs do not cover carrier screening or aneuploidy testing.
    - In Q2 2026, average selling price rose 21% to $551. Implied cost per test rose about 4%, to about $165.
    - So gross profit per test rose 30%, entirely from price.
    - [BillionToOne 10-K](https://www.sec.gov/Archives/edgar/data/2070849/000207084926000017/blln-20251231.htm) [F093, D006]

19. **Big oncology customers' revenue growth overstates their sequencing growth.**
    - **Caris:** revenue per case rose 31% in Q2 2026 while cost per case rose about 5.5% and cases rose 18%.
    - **Guardant:** in Medicare fee-for-service, liquid-biopsy profiling services grew only 4–6% in 2024. Medicare dollars rose 20% because one code's payment jumped 38%.
    - **All the large labs together:**
      - Combined Medicare service counts for the large therapy-selection and MRD labs rose 22%, but only 4% excluding Natera.
      - Foundation Medicine's tissue test fell 11% and its liquid test was flat.
      - Tempus grew about 13%, a figure distorted by a billing-code change.
    - [CMS data, Guardant](https://data.cms.gov/data-api/v1/dataset/92396110-2aed-4d63-a6a2-5d6207d46a29/data?filter[Rndrng_Prvdr_Last_Org_Name]=Guardant%20Health,%20Inc.&size=100) [F280, D038, F429, F440, F674]

20. **The headline "Medicare genetic testing +20%" is partly an infectious-disease test.**
    - The single biggest lab code in Medicare Part B is a pathogen test (87798), at $442.5M in 2024 and up 51%.
    - So the genetic category overstates human sequencing demand.
    - [CLP Magazine on OIG](https://clpmag.com/lab-management/medicare-part-b-lab-spending-2024-genetic-tests-drive-growth/) [F302]

21. **Guardant's raised guidance still builds in slowing growth.**
    - The raised guides (about 50% oncology volume growth; 270–285K Shield tests) imply H2 2026 oncology test growth of about 46%. That compares with 63% in Q2, with sequential growth near 8%.
    - Test counts are not Gb.
    - [Guardant 8-K](https://www.sec.gov/Archives/edgar/data/0001576280/000157628026000036/gh-06302026xexhibit991.htm) [D009]

22. **A large hospital's renewed Illumina reagent lot shrank 41%.**
    - Taipei VGH's two-year "high-throughput sequencing reagent" lot fell from NT$6.67M (Dec 2023) to NT$3.94M (Dec 2025–Dec 2027).
    - Either volume fell or the per-kit price fell sharply. The kit is probably mid-throughput NextSeq-class, and the new lot gives no set count.
    - [Taiwan PCC](https://pcc-api.openfun.app/api/tender?unit_id=3.32.80&job_number=1140732E) [F801]

23. **Deep liquid-biopsy genome work, the high-Gb MRD design bulls rely on, is being priced on Ultima.**
    - OICR prices Ultima's cell-free genome test at C$999 for 100X raw coverage. Its Illumina plasma genome at 30X is C$1,171.
    - That is about C$10 vs C$39 per unit of raw depth (−74%).
    - Research pricing and different chemistries make this approximate.
    - [OICR Ultima page](https://genomics.oicr.on.ca/?p=5935) [F790]

## 2A. Research customers fight hardest on price

The thesis says research customers, about 35% of Illumina revenue, are very price-sensitive. In this view they demand "insane discounts", are less volume-elastic, and fight harder on price when funding is tight.

The new evidence strongly confirms the funding squeeze in the US, Canada, the UK and Taiwan. It also shows research buyers pooling their volume into fewer, larger, price-led channels, such as outsourcing, campus consolidation and $50 services. It does not show public research buyers getting deep discounts directly. Government recharge rates sit near list (see watch-outs).

1. **NIH is funding far fewer grants, even though dollars are nearly fully obligated.**
   - **Grant counts (AAMC, data through 31 Aug 2026):**
     - NIH had obligated $30.2B, 89% of its ~$34B extramural budget.
     - It had made 1,924 fewer grants than at the same point in FY25, and 9,714 fewer than FY24.
     - The gap to FY24 held near 9,000–10,000 from June to August, with no catch-up.
   - **Competitive awards:** through July, competitive R01 awards, the core investigator grant that pays for reagents, were down 14% versus FY24. All competitive research project grants were down 8%.
   - **Projects (STAT, via a secondary summary):** about 58,000 projects were funded in FY26, against about 61,000 in FY25.
   - **Why it matters:** fewer labs have new money for consumables going into 2027.
   - [AAMC Aug brief](https://www.aamc.org/about-us/biomedical-research/publication/tracking-nih-awards-fy-2026-2) [F402, F404, F403, F383]

2. **Up-front multiyear funding explains most of the missing grants.**
   - Multiyear competitive awards reached $1.6B by 31 Aug 2026, up from $769M at 30 June. That compares with $556.4M in FY25, though the comparison date is unclear.
   - Our arithmetic: if these awards pre-fund 4–5 years, about $1.2–1.3B pays for future years. At ~$586K per project, that would fund roughly 2,000–2,200 one-year awards, close to the 1,924 shortfall.
   - So the squeeze is fewer funded labs, not fewer dollars. The award-length assumptions are ours.
   - [AAMC Aug brief](https://www.aamc.org/about-us/biomedical-research/publication/tracking-nih-awards-fy-2026-2) [F405, D036]

3. **NHLBI's flagship genome-sequencing contracts are flat and lumpy.**
   - The TOPMed sequencing contracts each carry a $500M ceiling. After three years they are only 2–8% used, about $93M in total, or roughly $31M a year. That is level with the predecessor program.
   - Task orders to Broad and the New York Genome Center went $4.4M → $30.2M → $6.7M (FY23–25).
   - Big ceilings are normal, so read this as "no growth" rather than a cut.
   - [HigherGov IDV](https://www.highergov.com/idv/75N92023D00012) [F926, F927]

4. **UK academic research funding is flat to down in cash through 2029–30, which is a real-terms cut.**
   - UKRI's curiosity-driven research budget goes from £3,653m (2026–27) to £3,581m (−2.0%), then £3,638m by 2029–30 (−0.4%).
   - Quality-related funding falls 4.3% in 2027–28. Applicant-led grants rise only 0.7%, then 6% by 2029–30.
   - Separately, a £50m cut to the research capital fund (RCIF) by 2029–30, per Wonkhe, narrows its use to "sustaining current facilities". That fund pays for instruments, not consumables.
   - [UKRI budget](https://www.ukri.org/publications/explainer-ukri-budget-allocations/budget-allocations-for-uk-research-and-innovation/) [F442, F441]

5. **The Public Health Agency of Canada (PHAC) sharply cut its Illumina reagent buying in 2026.**
   - We removed duplicate amendment rows from Canada's contract disclosures first.
   - **H1 2026 decline:**
     - PHAC's Illumina spend in H1 2026 was C$1.24M, against C$2.62M a year earlier (−53%). Excluding one equipment buy, consumable-type spend fell 77%.
     - Agriculture Canada's consumable-type spend fell 70%.
   - **Fiscal year and year-end:**
     - PHAC's fiscal 2025–26 total fell 76% to C$1.76M. That figure has some amendment-row uncertainty.
     - Its year-end (Jan–Mar) reagent buying fell 88%.
   - **Large orders:** PHAC's main standing offer, a pre-negotiated supply agreement, went silent for 12.5 months. Orders of C$100K or more fell from 21 (2024) to 8 (2025) to 1 (H1 2026).
   - **All federal buyers:** consumable-type spend fell about 54–67% in H1 2026.
   - [Canada contracts data](https://open.canada.ca/data/en/api/action/datastore_search?resource_id=fac950c0-00d5-4ec1-a4d3-9cbebf98a305&filters=%7B%22vendor_name%22%3A%22ILLUMINA%20CANADA%20ULC%22%2C%22owner_org_title%22%3A%22Public%20Health%20Agency%20of%20Canada%20%7C%20Agence%20de%20la%20sant%C3%A9%20publique%20du%20Canada%22%7D&limit=400&fields=reference_number,contract_date,contract_value&sort=contract_date%20desc) [F509, F510, F508, F511, F512, D046]

6. **Canadian federal Illumina contract value roughly halved in calendar 2025.**
   - All federal departments: C$11.06M (2024) → C$4.88M (2025), −56%. Excluding one CFIA package, the fall is −42%.
   - PHAC alone: C$7.26M → C$3.35M, −54%.
   - This is Canadian federal spending only. COVID wind-down and duplicate-row caveats apply (see watch-outs).
   - [Canada contracts data](https://open.canada.ca/data/en/api/3/action/datastore_search?resource_id=fac950c0-00d5-4ec1-a4d3-9cbebf98a305&q={"vendor_name":"Illumina"}&limit=100&sort=contract_date%20desc) [F447, F448]

7. **Research sequencing is moving into larger outsourced accounts, which hold more leverage.**
   - **NRC:**
     - Canada's National Research Council cut direct Illumina orders about 90% from 2022 to 2025.
     - It moved the work to SickKids/TCAG and Génome Québec, which run the X, and it bought an Element AVITI (C$337K).
     - Counting the outsourced spend, its Illumina-related sequencing fell only about 40–50%, and more of each dollar now goes to the core's markup.
   - **DFO:** Fisheries and Oceans Canada's orders to Génome Québec tripled from 2022 to 2024 (9 → 31). They were flat in 2025.
   - [Canada contracts search](https://search.open.canada.ca/contracts/?search_text=%22Hospital+for+Sick+Children%22+%22National+Research+Council%22&sort=contract_date+desc) [F449, F487, D041, F490]

8. **A Taiwanese national research institute keeps cutting its outsourced sequencing, and it wins low prices through competition.**
   - **The Illumina lot:** NHRI's outsourced Illumina lot fell from NT$13.99M (2023) to NT$10.34M (2025). The Oct 2026 budget is NT$8.80M, 37% below 2023.
   - **Total budget:** its total outsourced sequencing budget is 71% below 2021–22. Awards are down 54% over 2021–25.
   - **Price per genome:** its Oct 2024 genome tender drew two bidders. It settled at NT$9,800 per genome, 23% below the hospital rate and 19% below its own reserve price.
   - The price fight is between Illumina-based vendors.
   - [NHRI tender](https://pcc-api.openfun.app/api/tender?unit_id=92019239&job_number=115B0D0286) [F845, F846, F759]

9. **Cores are consolidating or outsourcing to the cheapest channel.**
   - **Campus consolidation (UC):** UC Berkeley owns no X. It moved all its lanes to UCSF's core in summer 2026 and resells them at about 2% over CAT's rate.
   - **Outsourcing to cheaper providers:**
     - UMN's core says X Plus access is "faster and less expensive when outsourced".
     - Cornell (2024) and Mainz (2024, all sequencing at Novogene Munich) run outsourced models. Both sources are older.
   - **UK frameworks:** two UK university sequencing frameworks went mostly to outsourcers, including Novogene and Genewiz: Edinburgh in 2022 and Leicester in 2025, each about £1M.
   - Volume mostly stays on Illumina hardware, but buying power concentrates.
   - [Berkeley QB3 rates](https://qb3.berkeley.edu/facility/genomics/rates/) [F390, F818, F376, F391, F392, F473]

10. **A university core moved its routine sequencing to Element, citing lower cost.**
    - The University of Iowa Genomics Division says NGS "has been migrated" to AVITI.
    - It keeps the X only for large projects.
    - The page is undated.
    - [Iowa Genomics](https://humangenetics.medicine.uiowa.edu/genomics-division/genome-sequencing/sequencers) [F305]

11. **Research buyers move fast to very low prices, and cores cut prices too.**
    - **Plasmidsaurus:**
      - It launched 3' RNA-seq at $50 per academic sample with no minimum order.
      - Its CEO cites "unprecedented demand" and says the service is only "barely" profitable (GenomeWeb snippet).
    - **Baylor:** its core cut its own 3' RNA-seq price 36% from 2022 to $160, including a 16–17% step in 2025. That step predates the Plasmidsaurus launch.
    - This supports price sensitivity. It also shows research volume does respond to price, which cuts against "less volume-elastic".
    - [Plasmidsaurus](https://plasmidsaurus.com/rna) [F727, F736]

12. **An academic reagent supplier saw a flat first half and a "budget-constrained environment".**
    - Twist's academic and government revenue was +0.7% in H1 of its fiscal 2026.
    - It jumped in the next quarter when "several large customers" returned (see watch-outs).
    - [Twist call](https://allmind.ai/earnings/event/2942776) [F599]

## 2B. Research pricing gets worse from flat volume

The thesis says the street models research consumables as flat year over year. Instead, volume stays flat while pricing worsens, as Roche's AXELIOS and large labs push for bigger discounts.

The new evidence supports the "price not volume" pattern at specific buyers. It also shows rivals clearly winning research work at certain cores and in Taiwan.

Two gaps stand out. Roche's AXELIOS, launched 29 Jun 2026, has not yet appeared in any public data, core price list or tender the scrape could reach. And in public databases, rival gains are small and led by MGI, mostly outside the US.

1. **At NHRI, falling Illumina spend reflects lower prices, not lower volume.**
   - NHRI's Illumina lot awards fell 26% from 2023 to 2025. Over the same period, Taiwanese outsourced genome prices fell 47–59%.
   - That implies volume rose 1.4–1.8x while spend fell.
   - Compared budget to budget, the 57% decline matches the unit-price fall. This is the thesis's research pattern of flat-to-higher volume and worse price.
   - [NHRI tender](https://pcc-api.openfun.app/api/tender?unit_id=92019239&job_number=115B0D0286) [D081]

2. **A major US research core now runs almost entirely on rivals.**
   - **Fleet:** UMGC's in-house fleet is 5 AVITI24s and 2 Ultima UG200s. The X Plus is offered only through "partnered outsourcing".
   - **Genomes:** its genome service lists only Ultima, as the primary platform, and AVITI.
   - **Queue (Oct 2026):** 461 of 463 rows (99.6%) are on AVITI or Ultima. By nominal kit reads, Ultima dominates.
   - **Caveats:** the queue counts were not re-verified, and outsourced X work still buys Illumina reagents. So this shows UMGC's own capacity, not its users' total Illumina use.
   - [UMGC core page](https://genomics.umn.edu/general/core-facility) [F1100, F1101, F200, F1068, F112]

3. **A 10x-backed Ultima discount steers single-cell research off Illumina at about a quarter of the per-read price.**
   - **The offer:** UMGC's "preferred" Ultima pricing for 10x Genomics single-cell and spatial projects (Aug 2026) takes $500 off a wafer, giving $2,704 UMN or $3,188 external. Eligibility runs through 10x's account executives.
   - **Per read:** that is about $0.25 per million reads. Comparable figures are $0.74–1.20 per million clusters on 25B lanes at peer cores, and $0.88 at UCSD, so Ultima is about 3–4x cheaper per read.
   - **Per Gb:** against Fred Hutch's 25B, it is about 1.9–2.9x cheaper internal and 2.8–4.4x external.
   - **Caveats:** Ultima reads are single-end, and some peer prices come from search snippets.
   - [UMGC preferred pricing](https://genomics.umn.edu/news/preferred-ultima-ug-100-pricing-10x-genomics-projects) [F030, F683, D004, D062, F686]

4. **Against the right comparison, the X 25B lane, Ultima is about 1.7–2.4x cheaper per Gb.**
   - OICR's Ultima wafer is C$5,130 for about 10B reads, or C$1.71–2.05/Gb. That is 3.6–4.3x below OICR's own 10B lane, but only 1.7–2.0x below TCAG's 25B lane (C$3.47/Gb).
   - At UMGC, the wafer works out to $1.07–1.28/Gb, against about $2.62/Gb for UCSF's 25B lane, so about 2.0–2.4x.
   - OICR calls itself Canada's first certified Ultima service provider.
   - [OICR Ultima page](https://genomics.oicr.on.ca/ultima-sequencing/) [D076, F784, F1066]

5. **Element's real price advantage is in mid-size runs, where research labs buy.**
   - A full AVITI High 300-cycle run at UMGC ($1,175 for about 450 Gb, or $2.61/Gb) costs 30–40% less per Gb than an X 10B-300 lane: $3.73–3.84/Gb at UCSF and UCSD, and $4.38/Gb at Harvard.
   - Against a full 25B lane, AVITI is only at parity.
   - [UMGC AVITI page](https://genomics.umn.edu/service/aviti24-sequencing) [D096]

6. **UMGC's AVITI cost per read fell about two-thirds in two years.**
   - On UMGC's pricing sheet, cost per billion reads fell 32–41% from FY24 to FY25, then 46–51% from FY25 to FY26, on the 150- and 300-cycle kits.
   - About a third of the FY26 step came from Element's free +50% output upgrade (Sep 2025). The 19–27% residual may be a separate per-run cut, though the sheet's basis is unclear.
   - [UMGC AVITI sheet](https://docs.google.com/spreadsheets/d/1j3seGD_1whU9ppFdQOxtUTUsGdgg8fdtA4O6NFFpFRc/export?format=csv) [F1063, F1065, F688]

7. **Element has built a Taiwan research base whose reagent ceilings now exceed Illumina's at one flagship buyer.**
   - **Instrument awards:**
     - Element's Taiwan channel won about NT$41.5–51.5M (~US$1.3–1.6M) of AVITI instrument awards in 2024–26, at Academia Sinica, NTU College of Medicine and possibly Chi Mei.
     - One Academia Sinica institute that bought a NextSeq 500 in 2016 chose AVITI for its 2026 refresh. That it replaces the NextSeq is our inference.
   - **NTU reagent contract:**
     - NTU signed a NT$13.3M AVITI reagent contract running to Dec 2028, about US$140K a year. That is above Illumina's own $80–100K consumables-per-box guide for its competing NextSeq 1000/2000.
     - Over the same period, NTU College of Medicine's Illumina reagent ceiling fell from about NT$10.5M a year to NT$2.2M, though the scope narrowed. Element's ceiling is now about 2x Illumina's.
   - [Taiwan PCC, Element channel](https://pcc-api.openfun.app/api/searchbycompanyname?query=亞洲準譯股份有限公司&page=1) [D100, F1088, D084, F885, F747, F870]

8. **Taiwan's CDC is putting new sequencing money into Oxford Nanopore.**
   - Its 2026 nanopore consumables (NT$11.59M) plus a nanopore sequencer (NT$3.45M) exceed its flat Illumina library-reagent lot (NT$10.2M).
   - This is public-health spend, the lots are not like-for-like, and long-read is not a direct short-read substitute.
   - [Taiwan CDC award](https://pcc-api.openfun.app/api/tender?unit_id=A.21.1&job_number=KA115024) [F749]

9. **Rivals are taking a rising share of new public sequencing runs, but mostly through MGI.**
   - **Overall share:** in SRA, AVITI plus MGI's DNBSEQ-T7 rose from 2.3% (Q3 2024) to 3.6% to 7.6% (Q3 2026) of runs across five platforms.
   - **Share of growth:** rivals captured about 23% of the year-on-year growth in new-platform runs in Q3 2026, up from 9%.
   - **Who drives it:**
     - The increase is driven by T7, whose runs were up 2.7x and are likely China-linked.
     - AVITI runs grew 11x in two years, from 966 to 10,838, but AVITI's capture of growth fell from 8.3% to 6.0%.
   - **Large runs tell the same story.** In the European archive (ENA), MGI's DNBSEQ runs of 10 Gb or more grew 52% y/y in Q3 2026 (9,856 → 14,976). Element's grew only 5% (440 → 462), and Illumina NovaSeq's grew 5.6% (76,042 → 80,308). So rivals' share of large short-read runs rose from 11.9% to 16.1%, but almost all of the gain is MGI. That activity is weighted to China and Asia, where Illumina's revenue is already down 19%, so it says little about US or European research pricing. [ENA count API](https://www.ebi.ac.uk/ena/portal/api/count?result=read_run&query=instrument_platform=%22DNBSEQ%22%20AND%20first_public%3E=2026-07-01%20AND%20first_public%3C=2026-09-30%20AND%20base_count%3E=10000000000) [F648]
   - Runs are not Gb.
   - [NCBI SRA](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=sra&term=%22DNBSEQ-T7%22[Instrument]%20AND%202026/07/01:2026/09/30[PDAT]&rettype=count) [F611, D056, F609, F610]

10. **In GEO deposits, rival platforms are rising but still small.**
    - Rival platforms' share of human and mouse high-throughput samples rose from 0.75% to 3.9% to 4.5% (Q3 2024–Q3 2026). Most of the gain came in 2025.
    - AVITI and Ultima samples grew 79% y/y.
    - Series using AVITI rose from 5 to 112 a quarter, adding about 17–20 each quarter.
    - [NCBI GEO](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=gds&term=%28GPL34295[ACCN]%20OR%20GPL34475[ACCN]%20OR%20GPL34762[ACCN]%20OR%20GPL36595[ACCN]%20OR%20GPL29480[ACCN]%20OR%20GPL28330[ACCN]%29%20AND%20gsm[ETYP]%20AND%202026/07/01:2026/09/30[PDAT]&retmax=0) [F582, F583, F805]

11. **US research share loss to rivals runs at about 1.7 points a year.**
    - In US-tagged GEO series, rivals rose from 3.8% to 5.5%. Rival series grew 97% versus 34% for NovaSeq.
    - Rivals took about 10% of the US increase, against about 23% globally in SRA. The global gain is mostly MGI outside the US.
    - The "USA" text tag is noisy.
    - [NCBI GEO](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=gds&term=gse[ETYP]+AND+2026/07/01:2026/09/30[PDAT]+AND+USA[All+Fields]+AND+%28AVITI[All+Fields]+OR+DNBSEQ[All+Fields]+OR+MGISEQ[All+Fields]+OR+Ultima[All+Fields]%29&retmax=0&retmode=json) [F954, D089]

12. **Weighted by data volume, public research output grew only about 12%, versus 42% by run count.**
    - Estimated public NovaSeq output rose about 12% y/y in Q3 2026, while run counts rose 42%.
    - So count-based signs of a research "rebound" overstate volume. That fits the thesis's "flat-ish volume" view.
    - [ENA count API](https://www.ebi.ac.uk/ena/portal/api/count?result=read_run&query=instrument_model=%22Illumina%20NovaSeq%206000%22%20AND%20first_public%3E=2025-07-01%20AND%20first_public%3C=2025-09-30) [D060]

13. **Rivals' share of direct US federal sequencer spending rose to about 17% in FY26.**
    - Direct federal obligations to Element, PacBio and Oxford Nanopore rose from about 10% of the total (FY24–25) to 16.8% (FY26). Illumina's direct obligations fell 29% to $24.0M, which may partly be a shift to distributors.
    - Element's dollars were flat ($0.75M), but it won more awards, including an AVITI24 for an NCI research center and USDA kit buys.
    - Illumina's direct federal sales are smaller than one NHLBI sequencing program's run-rate (~$31M a year). So federal research dollars reach Illumina mostly through genome centers, which have the most price leverage.
    - [Sweetspot, Element](https://www.sweetspot.so/markets/federal/contractors/element-biosciences-inc-cz2ches131a5/) [F924, F925, D087]

14. **The lowest-price research channel keeps edging its X lane prices down.**
    - Novogene's 25B lane fell from $2.95/Gb (2023–24 launch promotion, which needed 16+ lanes) to $2.55/Gb for a single lane in Sep 2026. A full flow cell is $2.46/Gb.
    - The 10B fell 8.8%, to $4.13/Gb.
    - That is steady erosion of about 5–7% a year, with no cliff.
    - [Novogene promotion](https://web.novogene.com/Facebook_25Q2_Premade_X) [F505]

15. **MGI's consumables stream is growing.** MGI's H1 2026 reagent revenue grew 16.3% to RMB 645M, 61% of its sequencing revenue, while instrument sales reportedly fell. This is mostly China. [China Securities Journal](https://www.cs.com.cn/ssgs/01/2026/08/22/detail_2026082210033207.html) [F446]

16. **Element is pushing into research counting work.**
    - AVITI24 was more than 35% of Element's new instrument bookings in 2025, and biopharma AVITI24 bookings rose 175%.
    - Element prices counting runs below $1 per million reads.
    - These figures are on a small base, and AVITI24 is largely an in-situ instrument.
    - [Rhymes with Haystack](https://albertvilella.substack.com/p/element-bio-at-jpm26) [F099]

17. **A UK public research buyer picked Element in a two-bidder tender.**
    - The Natural History Museum bought a "DNA Sequencer" from Element for £658,756 (Mar 2025), then direct-awarded a £157,544 upgrade.
    - That it is an AVITI is inferred, and the price likely bundles consumables.
    - [Find a Tender](https://www.find-tender.service.gov.uk/Notice/022248-2025) [F341]

18. **Cheap research services still run on Illumina, which concentrates buying power in aggregators.**
    - Plasmidsaurus's $50 RNA-seq runs on Illumina. Its reagent cost at core-level prices would be roughly $14–20 per sample (our estimate).
    - The volume stays on Illumina. But it pools at high-volume buyers that can demand top-tier discounts.
    - [Plasmidsaurus](https://plasmidsaurus.com/rna) [F739]

19. **Some cores move small work off Illumina when an instrument retires.**
    - The University of Iowa's microbiome core dropped its MiSeq after 1 Feb 2026. It moved amplicon work to AVITI24 rather than Illumina's replacement MiSeq i100, at up to 31% less per sample in large batches. Small batches are about flat.
    - At UNMC, the core's AVITI is cheaper per Gb than its own 6000. The reviewer puts the gap at about 13% at realistic output.
    - [Iowa microbiome core](https://microbiomecore.sites.uiowa.edu/services-rates) [F795, F791]

20. **The University of California system lets researchers buy Element as easily as Illumina.**
    - Element sits on the same UC-wide sequencing sourcing suite as Illumina, at "net contract pricing".
    - Purchases need no extra justification.
    - That lowers switching friction, though no volume is disclosed.
    - [UCSD procurement](https://blink.ucsd.edu/buy-pay/goods/lab/agreement-suppliers/sequencing/index.html) [F820]

## Derived figures

The scrape produced 103 derived figures (tags D001–D103). They are our own arithmetic on verified source data. Each appears as evidence in the sections above or in the watch-outs below. This section explains how the most important ones were built, so the reader can judge how much weight they bear.

### How prices become $/Gb

Almost every price comparison here turns a posted price into dollars per gigabase (billion DNA letters). We divide the price by the output the flow cell, lane or wafer produces. We used these outputs:

- **NovaSeq X 25B, 300-cycle:** about 8,000 Gb per flow cell at spec, or roughly 940–1,000 Gb per lane. One user measured about 8,800 Gb [F146]. Berkeley says real output runs 25–30% above spec [D035].
- **NovaSeq X 10B, 300-cycle:** about 375 Gb per lane (3,000 Gb per flow cell).
- **NovaSeq 6000 S4, 300-cycle:** about 3,000 Gb per flow cell (750 Gb per lane). S2 is about 1,000–1,250 Gb, and SP about 200–240 Gb.
- **Ultima UG100 wafer:** 2.5–3.0 Tb at UMN's own realistic figure, not the 3.6 Tb maximum. Using the maximum overstated Ultima's advantage in the first draft [D003].
- **AVITI high-output, 2x150:** about 300–450 Gb, depending on the kit generation.

The level of any $/Gb figure moves with these assumptions. The direction of a change at one core usually does not, because the same output is used on both sides.

### The 6000-to-X price gap, and why it matters for 1A

The table below sets out every measure of the 6000-to-X per-Gb gap that the scrape found. The takeaway: like-for-like S4-versus-25B gaps at cores and on list sit at 1.6–3.1x. Illumina's reported revenue gap of 3.4x is higher, and small 6000 flow cells (4–10x) or deep X discounts would close the difference.

| Measure | Source and date | 6000 ÷ X per Gb | Tags |
|---|---|---|---|
| Core S4 vs 25B, low end | Calgary 2025, UConn 2026, Missouri 2024 ("40% rate cut") | 1.6–1.9x | D022, D063 |
| Core S4 vs 25B, high end | MD Anderson, UCSF, Emory, Salk (2024–25) | 2.4–3.1x (median ~2.5x) | D025, D027 |
| User-facing at MIT (core marks up the X more) | MIT, Jan 2025 | 2.2x (vs ~3.1x on list) | D097 |
| Illumina list, S4 vs 25B | Open Offer 2024; 2025–26 | 2.76x → 2.58x | D049 |
| Regulated 6000Dx S4 vs 25B, list | Open Offer, Feb 2024 | 2.31x | D054 |
| Academic net (NCI's ~71% of GSA) | NCI rate card, GSA | ~2.4x | D026, D029 |
| Small 6000 flow cells vs 25B | Salk 2025, Pitt 2025 | S2 3.6–4.7x; SP 6–9.8x | D028, D032 |
| Illumina reported revenue per Gb | Q2 2026 deck (known) | 3.4x | — |

Three calculations follow from the table.

- **The reconciliation [D029].** Price the S4 at the academic net rate: about $5.13/Gb. Illumina's 3.4x ratio then implies X revenue of about $5.13 ÷ 3.4 ≈ $1.51/Gb. That is about 30% below the matching academic net 25B price (~$2.15/Gb). It is close to a negotiated price estimate built separately: the $16,480 list less a ~15% discount, spread over measured output, gives ~$1.59/Gb [D011].
- **The trend test [D049].** List ratios narrowed from 2024 to 2026, yet Illumina's reported ratio widened from about 2.8x to 3.4x. So the widening must come from which customers are left on the 6000, and from discounts on the X. List prices did not drive it.
- **What a point of conversion costs [D022].** A known estimate assumes each clinical point of 6000 Gb moving to the X costs Illumina about $24M a year, based on a ~70% price step. If the true step for a tail lab paying near list is only 45–50%, a point costs about $15–17M. Five points would then cost about $75–85M rather than $112M. D025 argues the median core step is closer to 60%, so the truth likely sits between these figures.

### Ultima and Element versus Illumina

The following table compares rival prices with Illumina at matched units. It shows that Ultima's advantage is about 2–3x at core list rates. Against Illumina's best negotiated price, the advantage falls to 1.2–1.5x. AVITI wins only against the smaller X flow cells.

| Comparison | Result | Tags |
|---|---|---|
| Ultima wafer vs 25B lane, core internal rates (realistic output) | 2.3–2.7x cheaper (2.7–3.3x at external rates) | D003 |
| Ultima vs 25B in Canada (OICR vs TCAG) | 1.7–2.0x cheaper | D076 |
| Ultima vs negotiated 25B (~$1.59/Gb) | 1.2–1.5x cheaper | D011 |
| Ultima all-in genome vs Illumina sequencing-only cost at another core | 35–55% cheaper | D002 |
| Same-period genome price, OICR Ultima vs TCAG X | 33% cheaper | D075 |
| Ultima per read for 10x single-cell work (with 10x discount) | 3.2–3.8x cheaper | D004, D062 |
| AVITI full run vs X 10B lane | 30–40% cheaper | D096 |
| AVITI list vs 25B list | ~3x more expensive | D020 |

**The genome decomposition [D099].** UMGC prices Ultima genomes in batches that each fill about one wafer. Comparing the 30x batch (24 × $192 = $4,608) with the 90x batch (12 × $329 = $3,948) separates the fixed wafer cost from the per-sample cost. The difference is about $55 per sample for prep and analysis, leaving about $3,290 per wafer. That prediction matches the 60x batch to within $4, and it matches UMGC's stand-alone wafer list price of $3,204. So sequencing is about 71% of a research genome's price.

TCAG's X genome breaks down in a similar way [D043]. Of C$650, sequencing is about C$330 at the core's own 25B lane rate.

### Hidden deflation inside the X family

The 10B premium is the price per Gb of a 10B lane divided by the price per Gb of a 25B lane at the same core. In 2026 it ranges from 1.03x at KUMC to 1.50x at MD Anderson [D018, D034, D035].

- Where history exists, the premium shrank because cores cut the 10B by 16–21% while holding the 25B [D005, D092]. UCLA went from 1.58x to 1.26x and TGen from 1.45x to 1.13x.
- It is not universal. Carver, TCAG and Novogene sit at about 1.6x [D042, D045].
- At Harvard, the gap narrowed for the opposite reason: the 25B price rose 17% [D085].

To read core prices correctly, compare them with Illumina's per-lane list ($16,480 ÷ 8 ≈ $2,060).

- Cores charge 26–70% above that list [D019].
- At the two UC cores, the ratio fell from about 1.40x to 1.24x in one cycle while list rose about 3% [D093, D080]. That is a real but ambiguous signal: either a lower net price or less overhead.
- The "$24,155 list" used in several items is in fact the GSA distributor price, about 1.47x Illumina's catalog list [D048]. Once that is corrected, NCI pays roughly catalog list [D023].

### Taiwanese tenders as a window on service-lab reagent costs

An all-in genome at NT$12,800 (~US$410) works out to about $4.1/Gb including everything [D070]. If reagents are 45–60% of that, they cost $1.8–2.5/Gb. NHRI's NT$9,800 genome leaves at most $0.75–2.0/Gb for reagents plus margin [D072].

Prices fell in one step, from NT$24,000 in 2023 to NT$12,800, and then held flat [D073]. Single bidders on Illumina-only specifications settle within 0–0.02% of the buyer's reserve price, while multi-bidder tenders land 19–28% below it [D074]. Illumina's distributor settles at about 85% of its opening bid, year after year [D101, D103].

### Clinical sequencing in Gb terms, for 1C

Every clinical sizing here uses the same yardstick: about 800M Gb a year of Illumina high-throughput output, taken from the existing notes. The table below shows that none of the fast-growing named programs moves that total by even half a percent.

| Program | Annual Gb (approx.) | Share of HT base | Tags |
|---|---|---|---|
| Natera MRD draws at Q2 2026 run-rate (classic vs all-genome) | 0.2–3.8M | 0.02–0.5% | D039 |
| Adaptive clonoSEQ | 0.03–0.14M | 0.004–0.02% | D095 |
| GUARDIAN newborn genomes | ~1M | ~0.1% | D095 |
| GeneDx extra tests from new payer coverage | 0.25–3.7M | 0.03–0.5% | D102 |
| Taichung VGH genome contract | ~0.31M | ~0.04% | D069 |
| Taiwanese NIPT contracts | <0.006M | ~0.001% | D077 |
| Extra Dutch and German NIPT uptake | 0.13–0.26M | 0.02–0.03% | D094 |

**The GeneDx mix effect [D013].** Assume a genome is about 100 Gb and an exome about 10 Gb. Then Gb per average test falls from about 50.5 to 41.5 as the genome share drops from 45% to 35%. That is enough to cut 30% test growth to single-digit Gb growth.

**The NIPT pool [D014, D030, D086].**
- Netting Natera's gain against Myriad's loss gives +8.2% for the two labs.
- If NIPT already reaches 70–80% of pregnancies, full penetration adds at most 24–41% more tests (after the 1% birth decline), or about 5–9% a year.
- US birth counts are falling only about 0.5–1.5% a year. A faster drop in the fertility rate is partly offset by a growing population of women aged 15–44.

**Customer price-versus-volume splits.**
- BillionToOne's gross profit per test rose 30%, entirely from price [D006].
- GeneDx revenue per test fell 12% [D017].
- Myriad's prenatal revenue fall is −9% volume × −8% price [D021].
- Guardant's Medicare dollars rose 20% on 5–6% more tests [D038].
- Signatera's Medicare payment per service fell 8% [D040].

### Canadian federal contracts, cleaned

Canada's contract disclosure repeats amended contracts as extra rows, each carrying the cumulative value.

- Removing those rows changes the picture. PHAC's 2022 baseline falls from about C$9.6M to C$6.8M, so the 2022–25 decline is about −51%, not −65% [D050].
- Removing three instrument purchases from H1 2026 leaves consumable-type spend down about 54–67% [D046].
- Counting NRC's outsourced sequencing alongside its direct orders turns a 90% collapse into a 40–50% decline [D041].

### NIH grant counts

**Multiyear funding [D036].** Take the $1.6B of up-front multiyear funding. Assume each award covers 4–5 years, so about $1.2–1.3B pays for future years. Dividing that by about $586K per award gives roughly 2,000–2,200 awards. That is close to the 1,924-grant shortfall. The award length is our assumption.

### Public sequencing databases

- **Deposit lag [D052].** The X's share of GEO deposits (29.5% in Q3 2026) is below every research X share Illumina has reported since Q2 2024 (59–92%). So GEO lags real sequencing by about two years.
- **The X Plus fix [D065, D064].** Counting only the plain "NovaSeq X" platform misses 55–67% of X output, because the X Plus is filed separately. With the X Plus included, the X's share of large public runs went from 16% to 33% in a year.
- **Volume versus counts [D060].** Weighting by data volume, public NovaSeq output grew about 12%, against 42% by run count.
- **Rivals' share of growth [D056, D057, D089].** In SRA, rivals took about 23% of run growth. In GEO, they took only 6.5% of sample growth, and 10% of US series growth. The two databases disagree on direction.

### Smaller derived checks

- **Reagent rental [D053].** The rental surcharge adds about $520K a year per rented X box. With only about 5 of 100+ placements on rental, that lifts fleet-average consumables per box by just 1–3%.
- **Element's scale [D007].** At an assumed $290–500K per instrument, Element's non-instrument revenue is at most about $100K per average box. Illumina's X box averages about $1.24M.
- **Element at NTU [D084, D100].** NTU's AVITI reagent ceiling works out to about US$140K a year per box, about twice NTU's latest Illumina reagent ceiling.
- **Novogene [D044].** Its 25B lane price per Gb fell about 5.6% a year, against Illumina's blended revenue per Gb falling about 15–19% a year.

## Watch-outs: evidence that cuts against the thesis

This section collects every verified item that cuts against the thesis, grouped by leg. Five matter most:

- **The 6000-to-X price step may be smaller than assumed.** Like-for-like core prices put it at 40–60%, not 70% (items 1–2).
- **Government and academic buyers pay close to list,** with no visible acceleration in discounts (items 9 and 19–20).
- **Natera's MRD volume and its capacity build show no slowdown** (items 21–22).
- **NIPT is still growing in several markets** (items 24–25).
- **Rival platforms remain small and mostly MGI** in public research data (items 39–40).

### Against 1A (the 6000 mix shift)

1. **Like-for-like, converting a 6000 S4 user to the X 25B cuts that user's price per Gb by about 40–60%, not the ~70% implied by Illumina's 3.4x ratio.**
   - Core price ratios:
     - Calgary 1.64–1.70x, with the X lane outsourced (2025, CAD).
     - UConn 1.76–1.88x (Feb 2026).
     - Missouri said moving to the X let it "reduce sequencing rates by 40%" (Sep 2024).
     - UCSF 2.6x and Emory 2.4–3.0x, which are only weakly against.
   - At MIT, users saw just 2.2x against about 3.1x on list, because the core marks up X lanes more.
   - If tail labs pay near list, each point of conversion costs Illumina about $15–17M a year, not ~$24M. D025 partly rebuts this (median ~60% step).
   - [Calgary price list](https://cumming.ucalgary.ca/sites/default/files/teams/97/2025%20CHGI%20Internal%20Price%20List.pdf) [D022, F235, D063, F259, F260, F261, F230, D097]

2. **The regulated 6000Dx is the cheapest part of the tail, not the priciest.**
   - Illumina held the 6000Dx S4 kit at $13,876 while the research S4 rose to $16,578 (Feb 2024). It cut the Dx S2 kit 6.5%.
   - At list, Dx sites converting to the X lose about 57% per Gb, against about 64% for research-kit sites.
   - [Open Offer Appendix 1](https://supportassets.illumina.com/content/dam/illumina-marketing/documents/applications/cancer/1-25-2024_appendix-1.pdf) [D054, F575]

3. **Regulation and Illumina's own policy can keep the clinical tail in place for years.**
   - **No certified alternative:**
     - Illumina's EU regulatory (IVDR) page shows the 6000Dx as its only high-throughput diagnostic sequencer, with no X Dx.
     - A Japanese label for FoundationOne Liquid CDx, revised Sep 2026, still names the 6000. This comes from a snippet only.
     - The US device database flags retired Illumina Dx kits but not 6000Dx kits.
   - **Retirement timing:** under Illumina's end-of-life policy and the MiSeq precedent (4.75 years from notice to end of service), even a Q1 2027 notice would keep 6000 service to about late 2031.
   - So a 2027 step has to come from economics or Illumina's price levers, not forced retirement.
   - [EOL policy](https://emea.illumina.com/content/dam/illumina-marketing/documents/terms-conditions/1000000117071_01_Product_End_of_Sale_End_of_Life_Policy.pdf) [F531, F694, F1004, D083]

4. **Low-volume and legacy tails are sticky.**
   - Bambino Gesù's whole 6000 kit spend (about €130K a year) equals roughly two 25B flow cells. That gives it little reason to buy a ~$1M X.
   - UMN sent its retired research 6000 to its medical school rather than scrapping it.
   - NTUH (Taiwan) has contracted reagents for retired or legacy platforms well into the future:
     - MiSeq reagents worth NT$45M to Aug 2027.
     - MiniSeq kits to 2028.
     - NextSeq 500/550 kits to 2029.
   - The Canadian Food Inspection Agency's MiSeq service plans rose about 11% a year after end of sale.
   - [OPBG justification](https://img.ospedalebambinogesu.it/images/2025/12/01/170712615-29493de4-e17b-4fdf-96b0-64956a066e51.pdf) [F830, F227, F848, F861, F494, D047]

5. **One core raised its 6000 price.** Oregon's S4 lane is now $5,070 internal, about 4.5% above an earlier snippet and 13% above launch. Core rates include labor costs. [GC3F rates](https://gc3f.uoregon.edu/rates) [F658]

6. **Public databases lag, and the absolute 6000 count is not falling.**
   - GEO's X share trails Illumina's reported research X share by about two years.
   - The 6000's Q3 GEO deposits still grew 4–7% a year. SRA 6000 runs were flat year on year in Q3 2026 at about 408K.
   - Counts that filter only on the plain "NovaSeq X" platform miss 55–67% of X output, so several earlier projections were invalid.
   - [NCBI SRA](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=sra&term=%22Illumina%20NovaSeq%206000%22&retmax=0) [D052, F580, F595, D065]

7. **The clinical registry is too stale to size the tail.**
   - NCBI's Genetic Testing Registry has 130 records naming the 6000 and 12 naming the X, even though about 78% of clinical high-throughput Gb runs on the X. Excluding Mayo, the X is about 32% of records.
   - Labcorp's MaterniT NIPT, Mass General Brigham and Michigan already declare the X Plus. NIPT converted first, as known.
   - Taiwanese NIPT tenders specify no sequencer, so labs there can switch freely.
   - [GTR search](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=gtr&term=%22NovaSeq%20X%22&retmax=20) [D012, F125, F963, D088, F990]

### Against 1B (accelerating discounts)

8. **At negotiated prices, Ultima's edge is modest.** Illumina's $16,480 25B list, less the ~15% discount groups report, spread over measured output, is about $1.59/Gb. That narrows Ultima's per-Gb edge to 1.2–1.5x, from 2–3x at core rates. [LessWrong post](https://www.lesswrong.com/posts/x3DzjEofP94ki9iTp/how-much-data-from-a-sequencing-run) [D011]

9. **Large public buyers pay about catalog list.**
   - NIH's new reagent contract with Illumina (May 2026, $90M ceiling over five years) was sole-sourced with one bid.
   - NCI Frederick's recharge sits at a uniform ~71% of the GSA price across the 25B, 10B and 1.5B. That is about 104–107% of catalog list, because GSA is ~1.47x list.
   - Mass General Brigham's $14,400 S4 price matches a standard academic net, not special leverage.
   - Canada's research council paid TCAG's list price plus tax for 25B lanes (about US$2.5/Gb).
   - [NCI rate card](https://crtp.ccr.cancer.gov/fsgc/services/ngs-production/pricing) [F040, F247, D023, D048, D026, F263, F488]

10. **Several cores held or raised X prices.**
    - UCLA's at-cost 25B lane was flat for nearly three years (−0.7%) while prep rose 8–13%.
    - TGen's 25B lane rose 8.8% (2024–26), and TxGen's X flow cells rose 3%.
    - Harvard's Bauer core raised the 25B-300 lane 17.8% in FY27 after cutting it 17.4% in FY26, and raised most other X lanes. The 25B's per-read discount to the 10B narrowed from about 37–41% to 26–28%. Only the rarely run 100-cycle lane shows a deep gap.
    - The Harvard figures are from search snippets (the site returns 403).
    - [Bauer FY27](https://bauercore.fas.harvard.edu/fy27-ngs-sequencing) [F055, F222, F481, F766, F768, F775, F777, D085, F906]

11. **The 10B premium is not shrinking everywhere.** TCAG (Apr 2025), Carver (Aug 2026) and Novogene (Sep 2026) still price the 10B at about 1.4–1.6x the 25B per Gb. Carver gives a bigger volume discount on the 10B than the 25B. [Carver pricing](https://biotech.illinois.edu/dna-services-core/dna-services-pricing/) [D042, D045]

12. **The cheapest research channel is eroding only slowly.** Novogene's X lane prices are falling only about 5–7% a year. Illumina's blended revenue per Gb falls 15–19% a year, mostly from the 6000-to-X mix. [Novogene promotion](https://web.novogene.com/Facebook_25Q2_Premade_X) [D044]

13. **The Open Offer does not force further cuts.** Its commitment that the top flow cell be at least 43% cheaper per Gb than the S4 was already met on list by Feb 2024: $2.00 vs $4.80/Gb, or −58%. [Open Offer Appendix 1 (2022)](https://www.illumina.com/content/dam/illumina-marketing/documents/applications/cancer/01_6_2022revision-Appendix1_.pdf) [F543]

14. **Reagent rental hides little price erosion.** With only about 5 of 100+ X placements on rental, the per-run rental surcharge lifts fleet-average consumables per box by just 1–3%. [Illumina financing page](https://www.tst-web.illumina.com/company/doing-business-with-illumina/illumina-financial-solutions.html) [D053]

15. **Element is still small, and often pricier per Gb.**
    - **Scale:** about 450 systems and $58–85M of 2025 revenue (sources conflict), short of a $100M target. Its implied consumables per box is at most about $100K, against about $1.24M for an X.
    - **Price:**
      - Its euro list puts the AVITI 2x150 kit at about 3x the 25B list per Gb.
      - At Northwestern the 25B is the cheapest platform per read.
      - UC Davis claims only "similar per-base cost" to the X 10B.
      - UMGC's AVITI genome costs twice its Ultima genome.
    - **Hiring:** Element's job board lists no VITARI, key-account or pricing roles.
    - [Rhymes with Haystack](https://albertvilella.substack.com/p/element-bio-at-jpm26) [F082, D007, F221, D020, F202, F203, F006, F562]

16. **Roche's AXELIOS threat to large clinical accounts is slow.**
    - As of 30 Jun 2026, Roche had not delivered SBX (the technology behind AXELIOS) to Freenome. The evaluation can run two years from delivery.
    - The contract does not oblige Freenome to switch. A full move likely lands in 2028–31.
    - Freenome calls Illumina its "sole supplier" and switching "time-consuming and expensive".
    - Roche did pay $75M up front, plus option and milestone payments, to win the foothold.
    - [Freenome 8-K/A](https://www.sec.gov/Archives/edgar/data/0002017526/000114036126032873/ef20080133_ex99-1.htm) [F1073, F1074, F1075, F1076]

17. **Big customers show little leverage or pass-through.**
    - GeneDx says it has "not, to date, validated a viable alternative sequencing platform".
    - Natera's unit costs per test barely moved over two years once test mix is controlled for. Either Natera reinvests savings in depth, or its Illumina price is not falling much.
    - [Natera release](https://www.sec.gov/Archives/edgar/data/1604821/000162828026032101/ntra-20260331xex991.htm) [F239, F265]

18. **Canada's 2025 cut hit Oxford Nanopore too.** Its federal sales fell 46%, against Illumina's 56%, so the decline was budget, not share loss. Including Element, Illumina's share slipped only to about 77%. [Canada contracts data](https://open.canada.ca/data/en/api/3/action/datastore_search?resource_id=fac950c0-00d5-4ec1-a4d3-9cbebf98a305&q={"vendor_name":"Oxford%20Nanopore"}&limit=100&sort=contract_date%20desc) [F454]

19. **Taiwanese discounts are formulaic and, if anything, shrinking.**
    - Illumina's distributor settles at about 85% of its opening bid every year from 2022 to 2026. That reflects the buyer's reserve-price rules, not vendor choice.
    - Recent lots moved toward smaller concessions:
      - NTU −10% (2025).
      - Taiwan CDC 1% above reserve.
      - Tri-Service at reserve.
      - Taipei VGH's tumor-profiling deal went from 20% to 7.5% off.
      - A non-Genetech distributor gave 9%.
    - [Taiwan PCC](https://pcc-api.openfun.app/api/tender?unit_id=3.9.20&job_number=1142A007) [F1087, D101, F983, F981, F1089, D103]

20. **Some Taiwanese prices are flat.**
    - Taipei VGH paid an identical NT$201,000 per NextSeq P4 kit in 2025 and 2026.
    - Taichung's P3 kit is about 18% above US list.
    - Genome service prices dropped once (2023–24) and then held at NT$12,800.
    - A single-bidder hereditary genome price held at NT$14,260 while volume doubled.
    - FoundationOne tests stayed at NT$99,750.
    - [Taipei VGH award](https://pcc-api.openfun.app/api/tender?unit_id=3.32.80&job_number=1150157V) [F713, F751, D071, D073, F810, F1123]

### Against 1C (slowing volume)

21. **MRD momentum is intact.**
    - Natera's clinical MRD units have grown 52–56% y/y for six straight quarters.
    - Its Medicare Signatera dollars rose 47% in 2024. Draws per patient rose 10% and patients about 70%.
    - Medicare's MRD contractor (MolDX) widened coverage in 2026, including a genome-designed assay (snippet-level).
    - ctDNA trial starts in 2026 already exceed all of 2025, +29% like-for-like.
    - [Natera Q1 2026 deck](https://www.sec.gov/Archives/edgar/data/0001604821/000162828026032101/ntra-20260331xex992.htm) [F267, F426, F438, F297, F666, F667]

22. **Natera is building sequencing capacity faster than its tests grow.**
    - Permit records show a $6.0M, 12,048 sq ft "Natera Sequencing Core" in Austin, due 31 Dec 2026.
    - Gross plant and equipment rose 28% in H1 2026, and capex rose 79%.
    - Depreciation rose 47%, against tests +22%. That points to more Gb per test, or capacity ahead of demand.
    - [Natera 10-Q](https://www.sec.gov/Archives/edgar/data/0001604821/000162828026054525/ntra-20260630.htm) [F269, F837, D082]

23. **Customer guidance keeps rising.**
    - Natera raised FY26 revenue guidance twice, to $2.85–2.91B. That growth is price-led.
    - Guardant raised its Shield test guide to 270–285K, with UnitedHealthcare coverage from Aug 2026. Shield uses little data per test.
    - [Guardant Q2 call](https://www.fool.com/earnings/call-transcripts/2026/08/07/guardant-health-gh-q2-2026-earnings-call-transcript/) [F136, F143]

24. **NIPT maturity is not deepening at the leaders.**
    - Natera's non-oncology growth re-accelerated to +12.5% in Q2 2026, helped by share gains from an improved Panorama test and the Fetal Focus add-on (~200K orders a year). Fetal Focus is mostly a follow-on test for the same women.
    - BillionToOne's prenatal revenue rose 55%.
    - Myriad's decline looks company-specific and is immaterial in Gb: 35K fewer tests ≈ 35–70K Gb.
    - [Natera Q2 2026 release](https://www.sec.gov/Archives/edgar/data/0001604821/000160482126000015/ntra-20260630xex991.htm) [D010, F179, F268, F079, F215, F216]

25. **Uptake and up-tiering are still adding NIPT tests outside the US.**
    - Dutch NIPT tests rose 8.8% in 2024, at 73.5% uptake.
    - Four Taiwanese medical centers roughly doubled their NIPT spend toward expanded, deeper tiers.
    - Industry trials of monogenic, fetal-cell and exome-based NIPT could raise Gb per test.
    - US births to mothers aged 30–44 are still rising.
    - All of this is tiny in Illumina terms [D077, D094].
    - [Kamerstuk 29323](https://zoek.officielebekendmakingen.nl/kst-29323-189.html) [F1012, F779, F780, F781, F789, F705, F942]

26. **Payer gates are opening for genomes.**
    - 39 state Medicaid programs now cover outpatient exome or genome testing.
    - Carelon covers genomes for up to 56M lives (Jun 2026).
    - Medi-Cal pays genomes at 100% of Medicare from Jul 2026, after removing age and setting limits for 14.7M enrollees.
    - Flat collection rates and a falling genome mix at GeneDx offset some of this.
    - [GeneDx Q2 release](https://www.sec.gov/Archives/edgar/data/0001818331/000162828026051852/exhibit991-q22026pressrele.htm) [F193, F1115, F1116, F1117]

27. **Where price is the binding cost, cutting it unlocks genome volume.**
    - When Taipei VGH's genome price fell 47%, contracted genomes nearly tripled (173 → 490). Contracted Gb rose about 140%, while spend rose only 10%. A second channel added 60% more Gb on lower spend.
    - NTUH's genome reagent contract rose about 6x in run-rate, though it may bundle instruments.
    - Taichung signed a NT$117.6M genome deal.
    - [Taipei VGH award](https://pcc-api.openfun.app/api/tender?unit_id=3.32.80&job_number=X11204H) [F745, D068, D079, F715, F746]

28. **Government payers' genetic-test spending is still growing.** Medicare Part B genetic-test spending rose 20% in 2024, and about 17% excluding the pathogen code. Per-enrollee payment rose 26%. These are dollars, not Gb. [CLP Magazine on OIG](https://clpmag.com/lab-management/medicare-part-b-lab-spending-2024-genetic-tests-drive-growth/) [F301, D031]

29. **Sequencing cost still binds population screening.** In the UK Generation Study's costing, sequencing is 58% of the £1,208 per-infant cost, "mainly consumables". So at research-scale prices, cheaper sequencing would still unlock newborn screening volume. [Omnicuris summary](https://www.omnicuris.com/medshots/daily_updates/genomic-newborn-screening-costs-analysis) [F316]

30. **Lab staffing is not a proven brake.** Molecular lab vacancies eased from 13.4% (2022) to 10.4% (2024). No 2025–26 source links staffing to lower NGS volume. [AJCP](https://academic.oup.com/ajcp/article/161/3/289/7344701) [F335, F338]

31. **Research activity in public deposits is rising.** GEO high-throughput sequencing series grew 34.7% y/y in Q3 2026, with smaller studies spread more broadly. GEO lags, and weighted by data volume the growth is only about 12% [D060]. [NCBI GEO](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=gds&term=gse[ETYP]+AND+%22high+throughput+sequencing%22[PTYP]+AND+2026/07/01:2026/09/30[PDAT]&retmax=0) [F939]

### Against 2A (price-sensitive research buyers)

32. **A federal research account shows no sign of "insane discounts".** NCI Frederick's 25B-300 recharge of $17,196 is about 4% above catalog list, and it buys under a sole-source contract. Large academic genome centers may differ. [NCI rate card](https://crtp.ccr.cancer.gov/fsgc/services/ngs-production/pricing/) [D016]

33. **UK academic sequencing frameworks weight quality above price.** Quality got 70–90% of the score. The price weight rose from 10% (2021) to 25–30% (2025), but it is still a minority. [Find a Tender OCDS](https://www.find-tender.service.gov.uk/api/1.0/ocdsReleasePackages/ocds-h6vhtk-02ac96) [F474]

34. **Some research prices went up.** MIT's core raised Illumina service prices 6–13% from 2021 to 2025. [MIT pricing](https://openwetware.org/wiki/BioMicroCenter:PricingFY2022) [F1046]

35. **Research money and activity are partly recovering.**
    - NIH obligations caught up to 89% of budget by August.
    - Twist's academic revenue jumped 32% in the June quarter.
    - Public SRA run releases rose 24% y/y, though only about 12% weighted by data volume.
    - [Twist 10-Q](https://www.sec.gov/Archives/edgar/data/0001581280/000158128026000047/twst-20260630.htm) [F406, F598, D058]

36. **The Canadian decline is overstated in parts.**
    - Duplicate rows inflated earlier baselines. PHAC's 2022–25 fall is about −51%, not −65%.
    - A 2021 COVID-era contract only affects pre-2024 comparisons.
    - PHAC's Apr–Jun 2026 spend rose from a tiny base. NRC and DFO direct buying in H1 2026 already exceeds 2025.
    - Agriculture Canada cut outsourcing but bought a C$405K Illumina instrument, which may duplicate a Health Canada row.
    - [Canada contracts data](https://open.canada.ca/data/en/api/action/datastore_search?resource_id=fac950c0-00d5-4ec1-a4d3-9cbebf98a305) [F513, F514, D050, F515, F492, F491]

37. **No published numbers show cores losing volume to outsourcing.** Seventeen searches found no 2025–26 core volume-loss figures tied to Novogene or outsourcing. [UChicago fees](https://voices.uchicago.edu/genomicsfacility/fees/) [F396]

### Against 2B (worse research pricing)

38. **AVITI is usually not cheaper per Gb than an X 25B lane at cores.**
    - At UChicago, UC Riverside, Northwestern and Salk, AVITI costs 1.7–3.0x the 25B per Gb.
    - Iowa's AVITI lanes run $4.63–6.95/Gb. MIT's AVITI was pricier than its S4 (2025, pre-upgrade).
    - UMGC's headline AVITI cuts apply only to full runs. Small runs cost 1.7–3.4x more per read.
    - [UChicago pricing](https://voices.uchicago.edu/genomicsfacility/pricing-new) [F286, F320, F1045, F1067]

39. **Rival pressure on large research runs comes from MGI, not Western rivals.**
    - Among public runs of 10 Gb or more, MGI's DNBSEQ grew 52%. Element was flat (+5%, 0.58% of NovaSeq), and Ultima barely appears (187 GEO samples in a year).
    - AVITI's single-cell runs are mostly shallow.
    - MGI's gains are China- and Asia-weighted. AXELIOS is not yet visible anywhere.
    - [ENA count API](https://www.ebi.ac.uk/ena/portal/api/count?result=read_run&query=instrument_platform=%22ELEMENT%22%20AND%20first_public%3E=2026-07-01%20AND%20first_public%3C=2026-09-30%20AND%20base_count%3E=10000000000) [D061, F649, F641, F584]

40. **The public datasets disagree on rival momentum.**
    - In GEO, rivals' share of sample growth fell from 16% to 6.5% while it rose in SRA.
    - No country's GEO rival share rose more than 3 points.
    - GEO expression-profiling series grew 42%.
    - [NCBI GEO](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=gds&term=gse[ETYP]+AND+2026/07/01:2026/09/30[PDAT]+AND+Germany[All+Fields]+AND+%28AVITI[All+Fields]+OR+DNBSEQ[All+Fields]+OR+MGISEQ[All+Fields]+OR+Ultima[All+Fields]%29&retmax=0&retmode=json) [D057, F955, F721]

41. **Some research tenders write Illumina into the specification.**
    - A Taiwanese livestock institute requires bidders to own an X Plus.
    - Taipei Medical University requires two or more Illumina sequencers.
    - Such single-bid awards land at the buyer's reserve price, while competitive ones land 19–28% below.
    - [TMU tender](https://pcc-api.openfun.app/api/tender?unit_id=03724606&job_number=TMU115-029) [F760, F761, D074]

42. **Legal and policy brakes on the cheapest rivals.**
    - 10x Genomics sued Element in May 2026 over AVITI24, in US and European patent courts.
    - The US 1260H list now includes Novogene, MGI and BGI. Federal contract and grant restrictions are expected from late 2028.
    - [10x 10-Q](https://www.sec.gov/Archives/edgar/data/1770787/000162828026054491/txg-20260630.htm) [F635, F254]

## Where the evidence is thin, and what to look at next

The scrape is strong on posted prices and public data. It is weak in exactly the places that matter most for the short. There is almost no direct evidence on three things:

- **The clinical 6000 tail.** About 80% of remaining 6000 output is clinical, and clinical labs do not deposit data publicly.
- **Illumina's net price to its largest accounts.** Every price seen is a core resale rate, a government purchase or a published schedule.
- **Roche's AXELIOS.** It launched on 29 Jun 2026 and has not yet appeared in any price list, tender or public dataset.

The items below are the most useful next steps.

**Gaps that weaken each thesis leg**

- **1A (the clinical tail).**
  - GTR registry data is stale [D012]. Public databases are research-weighted and lag about two years [D052].
  - Untested sources that could count the regulated 6000Dx base directly:
    - European device-safety notices, which often state units in distribution (BfArM, MHRA).
    - External quality-assessment reports listing lab platforms (EMQN; PDF unreadable here).
    - UK lab accreditation schedules (UKAS; PDFs).
  - Job postings that name the 6000 versus the X would show labs mid-conversion. The Indeed scrape returned only two postings, so a broader scrape is needed.
- **1B (net prices).** The best untested lead is the Element v. Illumina amended antitrust complaint (N.D. Cal. 5:25-cv-08026). Because the first complaint was dismissed for lack of specifics, the amended version should name discount conditions and customers. Federal transaction-level kit purchases (USAspending) need a POST-capable tool.
- **1C (volume).**
  - The Natera, BillionToOne and GeneDx Q3 2026 results (early to mid November) will test three things: whether the NIPT re-acceleration holds, whether MRD adds slow as Natera guided, and whether GeneDx's genome mix keeps falling.
  - Natera's cost of goods implies Illumina spend of tens of petabytes (PB) a quarter at $2–4/Gb. That is far above the ~1–2 PB a quarter its test counts suggest. This inconsistency is unresolved.
- **2A and 2B (research).**
  - AXELIOS: look for ASHG 2026 abstracts (embargoed during the scrape) and the first core rate cards listing AXELIOS or the 35B flow cell. None existed as of 12 Oct.
  - The AAMC's September NIH brief will give final FY26 grant counts.
  - The ASCP 2026 lab vacancy survey results are due in late 2026 or 2027.

**Dated datapoints coming soon**

- **14 Oct 2026:** NHRI's Illumina outsourcing lot award, budget NT$8.80M (−37% vs 2023).
- **20 Oct 2026:** Taipei VGH's Illumina high-throughput maintenance tender opens. The model is not named.
- **After 16 Nov 2026:** Osaka University's 78-line award, covering X 25B/10B/1.5B kits, MGI kits and 10x kits. It would give realized Japanese prices.
- **Apify jobs that were queued but never ran (worth running next):**
  - A04: Japanese and Taiwanese award notices, plus any later Open Offer schedules.
  - A05: university pages publishing Illumina discount percentages, and cores that left Illumina over price.
  - A06: eBay sold prices for used 6000s and surplus S4 kits.
  - A07: archived Pitt price tables for a 2023–25 series.

**Documents already downloaded but unread.** The environment had no PDF text extractor, so a run with `pdftotext` or `python -I` plus pypdf should read these first:

- Element's JPM 2026 deck with speaker notes.
- Northwestern's "State of the Core 2024".
- UCLA's 2024 rate sheets.
- EPFL's 9 Sep 2026 price list.
- CMS's 2025 Part B national summary file (ZIP).
- William Blair's survey of 169 OB-GYNs on prenatal testing.
- OIG's top-25 Medicare lab test table.
- The Dutch RIVM NIPT monitor.
- Rush and Utah core updates.
- Kyoto University fee tables.
- Japanese PMDA package inserts.

**Conflicts to resolve**

- Element's 2025 revenue: $58M (Substack) vs ~$85M (GenomeWeb).
- The Open Offer top discount tier: ≥$50M or ≥$100M of annual spend.
- Whether NHRI's Dec 2023 S4 award really covers 16 kits (≈$2/Gb) [D067].
- Whether the Health Canada and Agriculture Canada C$405K instruments are one purchase [F510].
- The X software v1.4.0 release date: Mar 2026 or Jul 2026.
- UMGC's AVITI pricing sheet vs its live price page [F1067].

**Untested leads worth a single probe each**

- EPFL's dated log of "strong decrease" NovaSeq price entries (Oct 2025, Mar 2026).
- Element's JPM 2025 deck, for year-over-year comparisons.
- Michigan's core rate card, for a same-core Ultima vs X comparison.
- TxGen's 2019 S4 price, for a 6000-to-X series at one institution.
- Charles University (Prague) award reports with X kit bid prices.
- Leiden (LUMC)'s AVITI24 notice, which may say which Illumina boxes it replaces.
- NASA GeneLab's 2025 6000 reagent notice.
- University of Toronto's 6000 purchase notice.
- Victoria's genetics service (VCGS) 2026 clinical price changes.
- The run's own queue: Illinois Carver pricing history, Taipei VGH successor tenders, NHRI TSO500 direct buys, Illumina LIMS compatibility status for the 6000, and the X v1.4.0 release notes (for 35B and new-chemistry details).

## How this scrape was built

**Process.** The scrape ran overnight on 12 Oct 2026, from about 01:00 to 05:45, with the write-up finished by 06:00. A Python orchestrator ran an Opus "strategist" for 85 cycles. Each cycle queued narrow probe, mine and scout tasks to Sonnet and Opus agents, at most five at a time. The run completed 618 tasks and catalogued 1,042 candidate sources. It logged 1,236 raw findings.

**Filtering.** Each finding was:

- deduplicated against the analyst's existing notes;
- checked by a skeptical reviewer, which rejected 79 findings outright and corrected many others (the corrections are reflected above);
- tagged by thesis label and direction.

What survived is about 300 verified source findings (F-tags) and 103 derived figures (D-tags). Spend was about $332 (API-equivalent) including the write-up. The run stopped at its planned budget wind-down, at an estimated 42% of the weekly allowance against a 25% starting point; the measured figure afterwards was 41%.

**Tools and their limits.** Agents had web search and a GET-only page fetcher. They had no shell, no PDF text extraction and no POST requests. Four consequences follow:

- Many key documents were downloaded but not read.
- Several figures rest on search-result snippets; those are flagged in the items.
- Archived page histories (Wayback Machine, archive.today) were blocked. So almost no core price history before the current page could be built, except where old PDFs were linked directly.
- Apify actors were tried:
  - an eBay sold-listings scrape (failed: zero sold 6000s);
  - an Indeed postings scrape (two postings);
  - a Google search scrape (done);
  - four more requests were queued but never ran, because the hourly check that runs them stalled on a permission prompt (listed under "what to look at next").

**Sources that were productive (most items first)**

- Taiwan's government e-procurement API (49 items).
- NCBI GEO platform counts (26).
- Canada's proactive contract disclosure (20).
- NCBI SRA run counts (12).
- The NCBI Genetic Testing Registry (13).
- Natera filings and decks (11).
- University core rate cards: UCLA, UCSD, UCSF, Berkeley, UMGC, Salk, Pitt, KUMC, Calgary, UConn, Emory, MIT, TCAG, OICR, Fred Hutch, Carver and Iowa.
- AAMC NIH award briefs (7).
- Myriad filings (7).
- GeneDx filings and calls (9).
- CMS Medicare Part B provider data (7).
- Illumina's Open Offer appendices (5).
- Illumina support and LIMS pages (5).
- The ENA archive.
- Freenome filings (4).
- UK university frameworks.
- CDC birth data (7).

**Sources found blocked; do not retry without a different tool**

- The Wayback Machine and archive.today.
- Reddit.
- WhatDoTheyKnow.
- Harvard's Bauer core pages (403).
- Surplus Solutions resale listings (403).
- GovDeals.
- UK Contracts Finder and Find a Tender web pages (403). Their OCDS API works.
- UC Davis's core pages.
- Palmetto MolDX documents.
- Health Canada's device licence search.
- Korea's KONEPS (login).
- Japan's PMDA PDFs.
- USAspending and the TED search API (both POST-only).
- The NIH RePORTER API.
- SRA BigQuery (needs a Google account).
- Fed360.
- HigherGov, after its free views.

**Sources found dry; do not repeat**

- Used-equipment marketplaces: eBay, LabX, REUZEit, MSU Surplus and dealer listings. These are undated, so they cannot show retirement pace.
- SEC EDGAR full-text search, which returns metadata only.
- Customer filings for Illumina supply terms: Natera, Freenome, GRAIL, 10x and BillionToOne. All are redacted or absent.
- Distributor catalogs. Government Scientific Source shows only the known GSA prices; Fisher and VWR show none.
- GSA eLibrary.
- University and cooperative purchasing agreements: E&I, Sourcewell, Big Ten, Iowa State and Colorado. UC's agreement shows only 25% off service.
- NIH S10 and NSF instrument awards.
- Service-provider price pages beyond promotions: GENEWIZ, Eurofins, Psomagen, Macrogen and GenoHub.
- Roche AXELIOS launch materials. They give only the $750K instrument and $150 genome.
- Element and Ultima newsrooms and trade-in pages.
- Most job boards.
- Public procurement portals in Brazil, India, mainland China, Thailand, Colombia, Ukraine, Portugal, Poland, Czechia, Slovakia, Spain and France.
- GTR lab-level summaries.
- Extra ENA data-volume variants, which need scripting.
- ClinicalTrials.gov enrollment sums.
- ABRF surveys.
- Core annual reports.
- NHS trust spend files.

**Limits to keep in mind**

- Core recharge rates include labor and overhead, so they are not Illumina's net price [D019].
- Public databases lag and over-represent research [D052].
- Canadian federal and Taiwanese buyers are tiny in Illumina's revenue. They are useful for patterns, not totals.
- Every derived $/Gb figure depends on the stated output assumptions (see Derived figures).
