# 18 Addendum: Alternative-data evidence for the pricing and research thesis

*Hand-added Core Notes file (12 Oct 2026). A condensed version of the overnight alternative-data scrape. The full write-up, with every item, link and caveat, is `Working Notes/Outputs/analyses/2026-10-12_thesis_scrape_addendum.md` (published as a private artifact: https://claude.ai/artifact/RiZ8vo9hoooukAgVnAkG6Z). Item tags such as [F540] or [D029] point to rows in `Working Notes/Outputs/datasets/2026-10-12_thesis_scrape_findings.csv`: F = a sourced finding, D = our own arithmetic on findings. Everything here was new to the corpus when found, and a skeptical reviewer checked each item.*

## The thesis being tested

The analyst's short thesis has two legs and five labels:

- **1A. The 6000 mix shift is not done.** About 17% of high-throughput (HT) consumables volume but 41% of HT revenue still sat on the NovaSeq 6000 in Q2 2026. The remaining users are less volume-elastic, about 5 more points shift in 2027, and management's "permanent tail" claim is doubtful.
- **1B. Discounting will speed up.** The 35B flow cell, Ultima and Element, and big-account leverage push net price down faster than the street's flat-discount assumption.
- **1C. Volume growth will slow** from about 30% to about 25%. MRD and WGS are too small to offset a maturing NIPT market, and sequencing cost is no longer what limits volume.
- **2A. Research customers fight hardest on price** when funding is tight.
- **2B. Research consumables see flat volume and worse price,** not the street's flat revenue, partly because of Roche's AXELIOS.

## The short answer

The scrape found its strongest support for the two pricing labels, 1A and 1B. It also found good support for the part of 1C that says payers, not sequencing cost, now limit clinical volume. Research (2A and 2B) is mixed. Funding stress is clearly confirmed, but direct evidence of deep research discounts is thin, and rival platforms are still small outside a few university cores, Taiwan and MGI in China.

The most important counter-evidence: converting a 6000 user to the X looks like a 40–60% price cut per Gb at like-for-like core prices, not the roughly 70% implied by Illumina's 3.4x revenue-per-Gb ratio. Government buyers pay close to list. Natera's MRD franchise shows no slowdown.

What the scrape could not reach is exactly what matters most: the clinical 6000 tail and Illumina's net prices to its largest accounts. Neither is published anywhere.

## How to read the price evidence

Most prices here come from university **cores**, labs that resell sequencing to researchers. A core's **recharge rate** includes labor and overhead, so it sits 26–70% above Illumina's per-lane list price and is not Illumina's net price [D019].

All prices are turned into **$/Gb** (dollars per billion DNA letters of output). The output assumptions behind that are:

| Flow cell or wafer | Output used |
|---|---|
| X 25B, 300-cycle | about 8,000 Gb per flow cell; one user measured about 8,800 Gb [F146] |
| X 10B, 300-cycle | about 3,000 Gb per flow cell |
| 6000 S4, 300-cycle | about 3,000 Gb per flow cell |
| Ultima wafer | 2.5–3.0 Tb, the realistic figure |

The **GSA price** (the US federal distributor schedule) is about 1.47x Illumina's catalog list for the 25B [D048]. Treat it as an inflated reference point, not a discount baseline.

## 1A. The 6000 mix shift

- **The remaining 6000 users are the expensive end of the fleet.**
  - Illumina reports 6000 Gb earning about 3.4x X Gb (Q2 2026).
  - At list, the S4-to-25B gap is only about 2.6–2.8x, and it narrowed from about 2.76x (2024) to 2.58x (2025–26), while the reported ratio widened from about 2.8x to 3.4x [D049].
  - At cores, the small 6000 flow cells cost far more per Gb than the 25B: S2 3.6–4.7x and SP 6–9.8x (Salk Jul 2025; Pitt Jun 2025) [D028, D032].
  - Inference: the residual tail is weighted toward small, high-price users, so each conversion is a large price step.
- **The 3.4x ratio implies deep off-schedule discounts on the X.** If 6000 users paid NCI's academic net rate (about $5.13/Gb), 3.4x implies X revenue of about $1.51/Gb. That is about 30% below the academic net 25B price (about $2.15/Gb). It is close to an independent estimate of a negotiated 25B price, about $1.59/Gb [D029, D011]. Reviewer caveat: tail mix and the gap between Gb shipped and Gb used could explain part of this.
- **Public data shows the mix shift still moving fast.**
  - In the European archive (ENA), weighted by data volume, the X family's share of NovaSeq output went from about 5% (Q3 2024) to 16–17% (Q3 2025) to 33–36% (Q3 2026). Estimated 6000 output fell about 13% year on year [F644, D064].
  - The 6000's share of GEO deposits fell about 12 points a year (96.9% to 82.4% to 70.5%), with no plateau [F577, D066].
  - About 74% of remaining public 6000 output is still in large runs of 10 Gb or more, so the tail is not shrinking to a small-run rump [D059].
  - Caveat: public deposits lag sequencing by up to two years and are research-heavy [D052].
- **The clinical tail is visible only in fragments.**
  - Mayo Clinic Laboratories holds 104 of 130 Genetic Testing Registry (GTR) records naming the 6000 and none naming the X [F123].
  - Tempus xT, UCSF500 and JAX Genome still declare the 6000 [F962, F971, F996].
  - Labcorp registered a genome-scale MRD test on the 6000Dx in Dec 2025, 13 months after moving its NIPT to the X Plus [F970].
  - No GTR record shows a 6000-to-X move [D090].
  - The registry is stale and self-reported, so read these as names, not rates.
- **Illumina controls the timetable for the tail.**
  - Under its end-of-life policy, service ends about 5 years after notice, service prices can rise from the notice date, and kits can be pulled early "if demand is low" [F897].
  - No third-party 6000 service exists; Illumina charges about $110–145K per box a year [F899].
  - The 6000 control software has had 1 release in 35 months, versus 6 for the X [F1053].
- **List-price history.** Illumina raised 6000 kits 15.1% (Sep 2022 to Feb 2024; S4-300 from $14,400 to $16,578) while holding the X 10B at $9,600. It then trimmed the 6000 3.9–5.2% by Feb 2026 [F538, F479].
- **Cores are dropping the 6000.** UConn deactivated all its 6000 products in 2026, and Toronto's TCAG lists the 6000 only as "contact facility" [F489, F947].

## 1B. Discounting

- **Ultima undercuts Illumina at research cores by roughly 2–3x per Gb, and the saving reaches the customer.**
  - The University of Minnesota core (UMGC) sells an all-in 30x Ultima genome for $192 internal ($221 external). Sequencing is about 71% of that price [D099].
  - Ultima's wafer works out to $1.07–1.28/Gb, against $2.6–2.9/Gb for 25B lanes at UCSD and UCSF, so 2.0–2.7x cheaper [D003, D076].
  - 99.6% of UMGC's queue runs on Element or Ultima, and it offers the X only through outsourcing [F1100, F1068].
  - Against a negotiated Illumina price of about $1.59/Gb, Ultima's edge shrinks to 1.2–1.5x [D011].
- **Illumina's price cuts are landing where the headline 25B price does not show them.**
  - The UC cores (UCSD and UCSF) cut 25B-300 lanes 9–11% and 10B lanes 16–18% in the latest cycle, while Illumina's 25B list rose about 3%. Their markup over per-lane list fell from about 1.40x to 1.24x [F1037, D092, D093].
  - UCLA (which passes reagents through "at cost") cut its 10B lane 21% with the 25B flat. TGen cut its 10B about 16% [D018, D005].
  - Across cores, the 10B's per-Gb premium over the 25B is now 1.03–1.5x [D034].
- **Big-account discounts must be bespoke.** Illumina's published Open Offer schedule caps the 25B discount at 12% (about $1.76/Gb at the top tier) [F540]. The cheapest public 25B price is Novogene's $2.55/Gb (Sep 2026) [D051]. Experts' "half or a quarter" of small-lab prices therefore needs individual contracts.
- **Service-lab pricing shows the same pressure.** Taiwanese hospital genome awards at NT$12,800 (about US$410 all-in) imply the winning lab pays at most about $1.8–2.5/Gb for Illumina reagents [D070, D072].
- **GeneDx is planning on lower reagent prices in 2027.**
  - Its CFO said a genome costs "nearly twice" an exome, "almost entirely higher reagent costs", with cost per test flat in H2 2026 and "step improvements in 2027" (Q2 2026 call) [F568].
  - Revenue per test is falling 8–12% a year [D017, D055].
  - It says it has not validated a second sequencer, which limits its leverage [F239].
- **Rivals are cutting faster than Illumina at one core.**
  - UCLA's MGI T7 flow cells fell 36–37% (Mar 2024 to Jul 2026) while its 25B was flat [F058, D001].
  - UMGC cut AVITI prices three times in about 14 months; its AVITI cost per read fell about two-thirds in two years [F140, F1063].
- **Illumina is building tools to price by segment.** A Jun 2026 posting for an Associate Director of Pricing Transformation covers pricing "by market, by customer type, and by application", plus pay-per-use models [F559].

## 1C. Volume growth

- **Payers, not sequencing cost, limit clinical volume.**
  - XiFin's blended denial rate on lab, molecular and genomic claims rose from 8.0% (2024) to 11.2% (2025). Prior authorization's share of molecular denials more than doubled, from 13.1% (2021) to 27.6% (2025) [F347, F348].
  - GeneDx cut FY26 revenue guidance about 12%, mostly on price: it still guides volume growth of at least 30%. Its outpatient genome collection rate is about 32% [D017, F188].
  - BillionToOne's gross profit per test rose 30%, entirely from price [D006].
- **GeneDx's growth uses less data.** Genomes fell from close to 40% of its insurance outpatient volume (Q1 2026) to 32% (Q2), and reflex exomes now exceed genomes. Under illustrative depths (a genome about 100 Gb, an exome about 10 Gb), 30% test growth becomes roughly 7–18% Gb growth [D013].
- **The fast-growing programs are rounding errors in Gb.** Against Illumina's roughly 800M Gb a year of HT output:

  | Program | Share of HT output |
  |---|---|
  | Natera MRD, at the Q2 2026 run-rate | 0.02–0.5% [D039] |
  | Adaptive clonoSEQ | 0.004–0.02% [D095] |
  | The GUARDIAN newborn genome study | about 0.1% [D095] |
  | GeneDx's extra tests from new payer coverage | 0.03–0.5% [D102] |

- **NIPT is maturing.**
  - The combined Natera and Myriad NIPT pool grew about 8% in Q2 2026 [D014].
  - Myriad's prenatal business fell 9% in volume and 8% in price per test [D021].
  - US births were down 1% in 2025 (3,606,400) [D030].
  - NIPT already reaches an estimated 70–80% of US pregnancies, leaving at most about 5–9% a year of headroom [D086].
- **MRD is concentrated at Natera and not accelerating.**
  - Natera's quarterly unit adds held at +20K to +24K. The record +34K in Q2 2026 included weather catch-up [F176].
  - Medicare data show 2.16 Signatera draws per patient a year, below the 3–4 experts assume, and payment per service fell 8.3% [F414, D040].
  - Tempus's MRD volume is about 3% of Natera's [F293].
- **Big oncology labs' revenue growth overstates their sequencing growth.**
  - At Caris, revenue per case rose 31% while cases rose 18% [F280].
  - Medicare service counts for the large therapy-selection and MRD labs rose 22%, but only 4% excluding Natera [F440].
  - Guardant's guide implies H2 2026 oncology test growth of about 46%, down from 63% in Q2 [D009].

## 2A and 2B. Research

- **NIH is funding fewer labs.**
  - Through 31 Aug 2026, NIH had made 1,924 fewer grants than at the same point in FY25, and 9,714 fewer than FY24. Competitive R01s were down 14% versus FY24 [F402, F404] (AAMC).
  - Multiyear funding paid up front ($1.6B) explains most of the shortfall: the same dollars fund fewer labs [D036].
- **Government reagent buying fell sharply in Canada.**
  - The Public Health Agency of Canada's Illumina consumable-type buying fell 77% in H1 2026 [F510].
  - Canadian federal Illumina contract value fell 56% in calendar 2025 [F447].
  - Part of the decline is budget rather than share loss: Oxford Nanopore fell too [F454].
- **Taiwan's national health research institute (NHRI) shows the 2B pattern.** Its Illumina outsourcing spend fell 26% (2023–25) while genome prices fell 47–59%, which implies volume rose 1.4–1.8x [D081].
- **Research buying is pooling into large, price-led channels.**
  - Canada's National Research Council cut direct Illumina orders about 90% and outsourced to the TCAG and Génome Québec cores [D041].
  - UC Berkeley moved all its lanes to UCSF's core [F390].
  - Plasmidsaurus sells $50 3' RNA-seq [F727].
  - Volume stays on Illumina, but buying power concentrates.
- **Rivals are winning specific research accounts.**
  - The University of Iowa core migrated routine NGS to AVITI [F305].
  - Element's Taiwan reagent ceiling at NTU is now about 2x Illumina's [D084, D100].
  - Rivals' share of direct US federal sequencer obligations rose to 16.8% in FY26 [F924].
  - In SRA, AVITI plus MGI's T7 went from 2.3% to 7.6% of runs in two years, mostly MGI and China-linked [F611, D056]. US research share loss runs at about 1.7 points a year in GEO [D089].
- **Research volume is rising only modestly.** Weighted by data volume, public NovaSeq output grew about 12% year on year, against 42% by run count [D060].

## Watch-outs: evidence against the thesis

- **The conversion step may be smaller.**
  - Core S4-to-25B ratios run from 1.6–1.9x (Calgary, UConn; Missouri cited a 40% rate cut) to 2.4–3.1x (MD Anderson, UCSF, Emory, Salk), with a median of about 2.5x [D022, D025].
  - If tail labs pay near list, each point of conversion costs about $15–17M a year rather than about $24M [D022].
  - The regulated 6000Dx S4 is cheaper than the research S4 ($13,876 vs $16,578), so Dx sites lose about 57% per Gb on conversion versus about 64% [D054].
- **The regulated tail can last.**
  - Illumina has no X Dx in the EU [F531].
  - Under the MiSeq precedent, even a Q1 2027 end-of-life notice keeps 6000 service to about late 2031 [D083].
  - So a 2027 step has to come from economics or Illumina's price levers, not forced retirement.
- **Government buyers pay about list.**
  - NIH's new Illumina reagent contract ($90M ceiling, May 2026) was sole-sourced with one bid [F040].
  - NCI Frederick's recharge is about 104–107% of catalog list [D023].
- **Several cores held or raised X prices.**
  - Harvard's Bauer core raised its 25B-300 lane 17.8% in FY27, after cutting it 17.4% in FY26 [F906].
  - TGen's 25B lane rose 8.8% (2024–26) [F222].
  - Novogene's lane prices erode only about 5–7% a year [D044].
- **Element is small and often pricier per Gb than the 25B.** It has about 450 systems and $58–85M of 2025 revenue [F082, D007].
- **AXELIOS is slow.** Roche had not delivered SBX to Freenome by 30 Jun 2026. Its evaluation runs up to 2 years from delivery, so a move likely lands 2028–31 [F1073].
- **Natera is strong.**
  - Its clinical MRD units grew 52–56% for six straight quarters [F267].
  - It is building a $6.0M Austin sequencing core [F837].
  - Its non-oncology growth (mostly NIPT) re-accelerated to +12.5% in Q2 2026 [D010].
- **Payer gates are opening for genomes.** 39 state Medicaid programs now cover outpatient exome or genome testing, and Medi-Cal pays genomes at 100% of Medicare from Jul 2026 [F193, F1117].
- **Price can still unlock volume.** When Taipei VGH's genome price fell 47%, contracted genomes nearly tripled [D068].

## Gaps and the best next leads

- **No direct data exists on the clinical 6000 tail** (about 80% of remaining 6000 output) **or on Illumina's net price to its largest accounts.**
- **The amended Element v. Illumina antitrust complaint** (N.D. Cal. 5:25-cv-08026) should name discount conditions and customers.
- **Q3 2026 results from Natera, GeneDx and BillionToOne** (early to mid November) will test whether NIPT re-acceleration holds, whether MRD adds slow and whether GeneDx's genome mix keeps falling.
- **Look for the first AXELIOS evidence**, in ASHG 2026 abstracts and the first core rate cards listing AXELIOS or the 35B.
- **Four Apify jobs were queued but never ran:**
  - Japanese and Taiwanese award notices.
  - University pages publishing Illumina discount percentages.
  - eBay sold prices for used 6000s.
  - Archived Pitt price tables.
- **Several downloaded PDFs were never read**, because the agents had no text-extraction tool. They include Element's JPM 2026 deck, the CMS Part B summary file and a William Blair OB-GYN survey.

## Sources for future scrapes

**Productive sources:**
- Taiwan's government e-procurement API.
- NCBI GEO, SRA and the Genetic Testing Registry.
- The ENA archive count API.
- Canada's proactive contract disclosure.
- University core rate cards: UCLA, UCSD, UCSF, Berkeley, UMGC, Salk, Pitt, KUMC, Calgary, UConn, Emory, MIT, TCAG, OICR, Fred Hutch, Carver and Iowa.
- AAMC's NIH award briefs.
- CMS Medicare Part B provider data.
- Illumina's Open Offer appendices.
- Customer 10-Qs, decks and calls (Natera, GeneDx, Myriad, Freenome).
- The UK Find a Tender OCDS API.

**Blocked sources:**
- The Wayback Machine and archive.today.
- Reddit.
- USAspending and TED (POST-only).
- The NIH RePORTER API.
- Korea's KONEPS.
- Japan's PMDA PDFs.
- Harvard's Bauer core pages.
- The UK Contracts Finder web pages.

**Dry sources:**
- Used-equipment marketplaces.
- EDGAR full-text search.
- Customer filings for Illumina supply terms (redacted).
- Distributor catalogs.
- Purchasing cooperatives.
- Most service-provider price pages.
- Most job boards.
- Procurement portals in Brazil, India, mainland China and most of the EU.
