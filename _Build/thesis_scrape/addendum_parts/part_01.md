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
  - At UCLA, UCSD, UCSF and TGen, cores cut the 10B lane 16–21% in the latest cycle while the 25B held flat or rose. That squeezed the 10B's per-Gb premium to 1.03–1.5x the 25B [D018, D092, D034].
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
