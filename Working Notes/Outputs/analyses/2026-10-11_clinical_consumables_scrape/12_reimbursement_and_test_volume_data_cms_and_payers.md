# Agent 12: Reimbursement and test-volume data (CMS and payers)

*Model: sonnet. Run 2026-10-11 02:04:02. Cost $0.67 (API-equivalent).*

**Assignment:** Find public data on US clinical NGS test volumes and reimbursement trends: CMS Medicare Part B / Clinical Laboratory Fee Schedule utilization for key NGS codes (e.g. 81479, 0239U, 0340U Signatera, 0242U Guardant360, 0037U FoundationOne CDx, 81420/81507 NIPT, 81425-81427 genome, 81415-81417 exome, MRD PLA codes) by year; MolDX coverage decisions for MRD and CGP (2024-2026); ADLT rate changes; the Sept 2026 CMS PAMA proposal and its effect on NGS test prices; any NIPT penetration statistics; and state biomarker-testing laws. Translate into an evidence-based range for 2026-2028 US clinical NGS test-volume growth by category, and note pricing pressure that could push labs to demand cheaper sequencing.

## Key findings

1. **CMS's preliminary 2027 lab fee schedule cuts generic sequencing codes but largely spares proprietary tests.** CMS published it on 2026-09-21. Weighted-median private-payor rates are 23% lower for genomic sequencing procedures and 22% lower for molecular pathology. Proprietary Laboratory Analysis (PLA) codes fall only 2.4%. FACT. [CMS fact sheet, 2026-09-21, cms.gov/newsroom/fact-sheets/preliminary-calendar-year-cy-2027-medicare-clinical-laboratory-fee-schedule-payment-rates]
2. **The cuts are phased in.** No test can fall more than 15% a year across 2027–2029. CMS projects about $1B a year in Medicare savings. 1,171 of 1,528 codes with private-payor data come in lower, 186 higher and 169 flat. Final rates are due in November 2026. FACT. [CMS fact sheet, 2026-09-21; MedTech Dive via medtechdive.com/news/cms-sets-preliminary-cuts-to-medicare-lab-reimbursement-rates/831031/]
3. **Branded MRD and CGP (comprehensive genomic profiling) tests mostly sit outside the cut.** The branded MRD and CGP tests are PLA codes, many with ADLT (Advanced Diagnostic Laboratory Test) pricing. That is my inference from the −2.4% PLA figure. I could not retrieve ADLT-specific 2027 rates. OPINION.
4. **Pricing pressure on sequencing demand is therefore mixed.** Generic exome/genome and panel codes (81415–81427 and similar) face real Medicare pressure. The big Illumina-consuming oncology franchises (Natera, Guardant, Tempus) face little in 2027. Medicare is only part of each lab's payer mix, so the incentive to demand cheaper sequencing is stronger in hereditary and rare disease than in MRD. OPINION.
5. **MRD volume is growing very fast.** Natera processed 283K clinical MRD units in Q2 2026, up about 56% y/y and up 34K q/q (the largest sequential gain on record). Oncology tests were 296.7K, up 57.2%. Total tests were 1.044M, up 22.4%. FACT. [Natera Q2 2026 release, 2026-08, natera.com/company/news/natera-reports-second-quarter-2026-financial-results/; Natera Q2 call, fool.com, 2026-08-13]
6. **Guardant is growing fast too.** Oncology tests were about 104K in Q2 2026, up 63%. Guardant360 Liquid grew over 30% and Reveal (MRD) more than doubled. Shield (screening) ran at about 66K tests, up from 16K a year earlier and 22K above Q1. FACT. [Guardant Q2 2026 call, 2026-07-30, fool.com/earnings/call-transcripts/2026/08/07/guardant-health-gh-q2-2026-earnings-call-transcript/]
7. **Guardant finished its move to NovaSeq X in May 2026 and saved about $200 per Guardant360 Liquid test.** MGMT. The cost cut came with a platform switch, so the saving came from the instrument rather than a price concession from Illumina. This is a customer-side read-through for Q2 below. [Guardant Q2 2026 call, same source]
8. **Shield cost of goods sold (COGS) is about $410 per test.** Guardant targets a 15% cut by end-2026 and $200 per test by 2028. Shield's average selling price (ASP) is about $800. That path requires sequencing cost per test to fall sharply, which implies price pressure on sequencing inputs. MGMT. [Guardant Q2 2026 call]
9. **Rare-disease volume is growing, but price per test is falling.** GeneDx exome/genome volume was 30,785 in Q2 2026, up 32%. Blended reimbursement was $3,258, down from about $3,700 in Q2 2025. Outpatient genome collection rate was about 32%, versus 43% a year earlier. Revenue per test is deflating while volume rises. FACT. [GeneDx Q2 2026 via marketbeat.com and fool.com, 2026-08-03/10]
10. **GeneDx expects coverage to lift volume from Q4 2026 into 2027.** Commercial genome coverage rose from 47% to 87% of covered lives. 39 states cover exome or genome testing through Medicaid. MGMT. [GeneDx Q2 2026 summary via quartr.com / webull.com]
11. **Medicare Part B genetic-test spending is large and growing.** Genetic tests were $3.6B of $8.4B total Part B lab spending in 2024 (43%, versus 18% in 2018). Genetic spending rose 20% in 2023–24, and the test count rose 160% to about 18M since 2018. FACT. [OIG report OEI-09-25-00330, Jan 2026, via darkdaily.com 2026-02-13 and cap.org] This growth is a policy target and a reason CMS and the OIG are scrutinizing genetic testing.
12. **Natera's MolDX pipeline is a volume and ASP catalyst, not a volume risk.** Natera has 7 MolDX submissions pending, worth an estimated "$150 to $200 in ASP upside." Approvals are expected from H2 2026 into H1 2027. Signatera ASP is about $1,275 against a long-term target of $2,000. Earlier, management said 30–35% of Signatera volume is for indications not covered by MolDX. MGMT. [Natera Q2 call, 2026-08-13; 360dx.com JPM 2026 article]
13. **Signatera's Medicare ADLT rate has been trimmed.** The 0340U rate was $3,920 for 2025 and $3,590 from January 2026. FACT. [discoveriesinhealthpolicy.com, 2025-01 and 2025-12 posts] The ADLT rate resets from private-payor data, so it can drift down even with ADLT status.
14. **State biomarker laws are a structural tailwind for volume.** About 24 states have passed biomarker-coverage laws, with about 11 more pending (ACS CAN, 2025–Aug 2026 white paper). Natera credits "biomarker states" for better Medicare Advantage and commercial reimbursement. FACT/MGMT. [fightcancer.org, Aug 2026 white paper (title seen, content not read); Natera Q2 call]

## 1. CMS / PAMA (Sept 2026 proposal)

- **Timing and data.** Preliminary CY2027 Clinical Laboratory Fee Schedule (CLFS) rates were released 2026-09-21. The data are private-payor rates from 2025 H1 collected under the Protecting Access to Medicare Act (PAMA), reported May 1 – Jul 31, 2026. A 30-day comment period follows, and final rates are expected in November 2026. FACT. [CMS fact sheet]
- **Scale.** 1,947 applicable codes. 1,528 (78.5%) had a weighted median from private-payor data. Average change is about −16%. FACT. [CMS fact sheet]
- **By category.**

| Category | Preliminary change vs 2026 |
|---|---|
| Genomic sequencing | −23% |
| Molecular pathology | −22% |
| Microbiology / Immunology | −19.3% each |
| Chemistry | −16% |
| Proprietary Laboratory Analysis (PLA) | −2.4% |

  [CMS fact sheet]
- **Cap.** Annual cuts are limited to 15% per test for 2027–2029. Per Medtech Dive, 775 tests would take the full 15% cut in 2027. So the 23% category cut is realized as roughly −15% in 2027, then up to a further −8% or so in 2028 for a typical code, if rates are finalized as proposed. The latter step is my arithmetic. FACT/OPINION. [medtechdive.com]
- **Industry pushback.** The American Clinical Laboratory Association says the rates "rely on data from just 2% of all labs paid under Medicare Part B in 2024." Quest fell about 5% and Labcorp more than 3% on the news. Beckers also reports the data lean toward physician-office labs. FACT. [medtechdive.com; beckersasc.com]
- **Context.** This is the first time since 2018 that market-based PAMA rates are applied. A 2026 budget law created the 15% cap. [onhealthcare.tech / pgmbilling.com summaries]
- **Not found.** I could not retrieve per-code rates for 81425–81427, 81415–81417, 81479, 0239U, 0242U, 0037U or 0340U in the 2027 file. I also could not confirm which MRD/CGP codes are ADLT-priced, which are PLA but not ADLT, and how ADLT rates move in 2027.
- **Read-through for Illumina.** Medicare is a minority payer for most labs, so a −15% to −23% cut on generic sequencing codes pushes labs toward lower cost per Gb and cheaper workflows (35B flow cell, Ultima, Element, AXELIOS) mainly in hereditary, exome/genome and non-proprietary panels. OPINION.

## 2. Medicare utilization and spend (OIG, Jan 2026)

- Part B lab spend was $8.4B in 2024, up 5%. Genetic tests were $3.6B (43%), up 20% y/y. Genetic spend per enrollee was $794 (+26%) against about $200 for non-genetic. FACT. [darkdaily.com 2026-02-13]
- About 18M genetic tests were paid in 2024, versus 7M in 2018. Enrollees receiving one grew from 2.4M to 4.5M (+85%). FACT.
- Concentration: 346 labs received over $1M in genetic payments and 55 received over $10M. The top 25 codes were about $4.1B (about 50% of Part B lab spend). FACT.
- Fastest-growing codes named: 87798 (infectious agent nucleic-acid detection) at $443M, up 51%. Code 81419 (epilepsy genomic panel) rose about 5x. Several oncology liquid biopsy assays have median payments in the thousands of dollars. FACT.
- **Caution.** The OIG signals growing fraud and abuse scrutiny of genetic testing. Katten and Mondaq describe expected enforcement in the coming year. OPINION. Most of the growth in the top codes is non-sequencing or low-Gb (87798 is PCR-type), so this data gives only a loose proxy for sequencing intensity.
- I did not get per-code 2022–2025 utilization counts for 81479, 0239U, 0340U, 0242U, 0037U, 81420/81507 or 81425–81427. CMS Part B utilization files, and CLFS code-level data, would be the next step.

## 3. MolDX coverage (MRD and CGP)

- Signatera has Medicare coverage across colorectal, breast, bladder, ovarian, lung and pan-cancer immunotherapy monitoring. Signatera Genome (whole-genome-based) got Medicare coverage (Natera, 2025-06-04). Breast coverage was in Feb 2023. FACT. [businesswire.com 2023-02-16, 2025-06-04]
- Natera has 7 pending MolDX submissions, with approvals expected H2 2026 to H1 2027 (see key finding 12). MGMT.
- Guardant has MolDX submissions ongoing for Reveal in breast, immunotherapy monitoring and chemotherapy monitoring. MGMT. [Guardant Q2 2026 call]
- Guardant360 Liquid CDx got FDA approval in May 2026. Guardant expects ADLT designation in H1 2027 and a Medicare price of $8,455 versus about $5,000 today. MGMT. [Guardant Q2 2026 call]
- Tempus xT Tumor Only was FDA approved, which moves tissue testing to ADLT pricing. The CEO guided about +$200 ASP and about $85M of annual revenue from 2027. MGMT. [Tempus Q2 2026 via chartmill.com / businesswire.com 2026-07-30]
- MolDX LCDs are active in other areas. Effective 2026-10-12 is a finalized LCD for targeted molecular panels for cancer (and hereditary thrombophilia). Proposed LCDs open for comment 2026-08-27 to 2026-10-11 cover NGS for hematologic malignancies and genome-wide methodologies. FACT. [Noridian MolDX notices, 2026] I did not read their content. These could set coverage limits on genome-wide and heme NGS, which matters to sequencing intensity.
- I could not find a standalone MolDX MRD LCD for 2024–2026. MRD coverage appears to run through test-specific technical assessments.

## 4. Test-volume data by category

| Category | Datapoint | Source |
|---|---|---|
| MRD | Natera 283K clinical MRD units, +56% y/y (Q2'26); Tempus MRD 9K, up from 6.5K q/q; Guardant Reveal >2x | Natera, Tempus, Guardant Q2 2026 |
| CGP / liquid biopsy | Guardant360 Liquid >30% growth; Tempus oncology volume +31% (+28% in Q1); Guardant oncology +63% in total | Q2 2026 calls |
| Screening (CRC, Shield) | 66K tests Q2'26; 2026 guide 270–285K tests; $218–230M revenue | Guardant Q2 2026 |
| NIPT | Natera women's health high-single-digit growth in Q2'26 on a seasonally adjusted basis (Q2 is the softest quarter); enhanced Panorama launched; no-call rate 0.5% | Natera Q2 2026 |
| Rare disease | GeneDx exome/genome 30,785, +32% y/y; Q2 volume growth outpaced revenue growth | GeneDx Q2 2026 |

- **NIPT penetration.** I found only a generic figure (25–50% of US women, third-party report cited in search results, undated) and not reliable current data. Natera's own high-single-digit women's health growth points to a mature, slow-growth segment. OPINION. Illumina's own NIPT commentary is in the corpus, and I did not check it.
- **Guardant total guide.** Revenue is guided to $1.34–1.36B for 2026 (+36–38%). MGMT.

## 5. State biomarker laws

- About 24 states have passed laws (AZ, AR, CA, CO, CT, FL, GA, IL, IN, IA, KY, LA, MA, MD, MN, NE, NM, NJ, NY, OK, PA, RI, TX, WI). Some are narrow: AR, CO and LA cover state-regulated private plans, FL covers Medicaid and state employees, CT covers Medicaid. About 11 states have pending bills (HI, ME, NC, NH, OH, NV, MO, TN, UT, VT, WA). FACT. [search summary of ACS CAN data; fightcancer.org white paper, Aug 2026]
- The state laws mostly affect commercial and Medicaid coverage. They don't change Medicare, and they don't govern self-funded ERISA plans.
- A Manatt 2026 white paper looks at biomarker testing rates among Medicaid enrollees in five states. I did not read it.

## 6. Evidence-based range for US clinical NGS test-volume growth, 2026–2028

These are my estimates (OPINION), anchored on the Q2 2026 datapoints above. Growth is in tests; sequencing Gb growth could be higher where intensity per test rises (WGS-based MRD, tumor-informed panels with more variants).

| Category | 2026 | 2027 | 2028 | Key drivers / risks |
|---|---|---|---|---|
| MRD | +45–60% | +30–45% | +20–35% | Strong momentum (Natera +56%, Tempus, Reveal doubling). New MolDX indications, NCCN guidelines. Risk: Medicare Advantage and commercial denials, competitors' pricing. |
| CGP / liquid biopsy | +25–35% | +20–30% | +15–25% | Guardant360 Liquid >30%; Tempus oncology +31%. CDx approvals broaden use. |
| Cancer screening (Shield, MCED) | Sharp ramp, +200%+ | +50–100% | +40–70% | Shield is early-stage and sensitive to payer coverage (UnitedHealth from 2026-08-01). MCED tests largely uncovered. |
| NIPT | +5–10% | +5–10% | +4–8% | Mature segment. Natera high-single-digit growth. |
| Rare disease (exome/genome) | +25–35% | +25–40% | +20–30% | GeneDx +32%; coverage rising (87% commercial genome). Price per test falling. |
| Hereditary / carrier panels | low-to-mid single digit to +10% | similar | similar | Largest Medicare PAMA exposure (generic sequencing codes). |

**Net for Illumina's thesis (OPINION).** Test volume in the oncology and rare disease growth categories looks consistent with, or above, management's "mid-20s %" long-term Gb growth model. The corpus-wide question is whether a roughly 60–70% per-Gb price drop on the X can be offset: it needs Gb volume to grow about 2.5–3.3x for flat revenue. I did not model this. The upside comes from intensity: WGS-based MRD and exome-to-genome moves. Offsetting risk: labs such as Guardant are capturing the platform saving themselves (about $200 per test).

## 7. Pricing pressure that could push labs to cheaper sequencing

- Medicare generic sequencing codes: −23% (phased, −15% cap per year, 2027–2029). FACT.
- GeneDx: reimbursement per test down about 12% y/y ($3,258 vs about $3,700) and collection rate down to 32% from 43%. FACT. Management expects improved reimbursement from coverage expansion later. A lab with falling revenue per test has a strong reason to cut sequencing cost per test.
- Guardant: targets Shield COGS of $200 by 2028 from about $410, against about $800 ASP. MGMT.
- Natera: sees "a lot of room" for COGS improvement as Latitude and Signatera Genome scale and targets a 70%+ gross margin over time. Q2'26 gross margin was 64.5% (63.4% a year earlier), with FY26 guided at 64–66%. MGMT/FACT.
- Natera's and Guardant's growth is concentrated in a few large labs, so they carry bargaining power with Illumina. OIG: 55 labs exceeded $10M in Medicare genetic payments. FACT.

## Contradictions and stale data

- Natera's Q2 2026 release gave no quantified ASP. The call and a secondary summary give about $1,275. Treat the $1,275 as MGMT from the call (via search summary and fool.com).
- The 30–35% "uncovered by MolDX" Signatera share is from the JPM 2026 coverage. Natera's Q2 call said exact covered/uncovered percentages were not disclosed. It may be stale.
- Guardant's Shield ASP of about $800 is described as "stable," but I could not tie it to CLFS rates for Shield.
- The 360dx item used for JPM 2026 and the Natera release say "Prospera" Medicare coverage expanded. I did not examine it.
- The category cuts (−23%, −22%) are weighted medians of private-payor rates. Realized Medicare payment for any single code differs, and the 15% cap applies per test.
- Search-engine summaries gave a Guardant earnings date of 2026-07-30 (marketbeat) while the Motley Fool transcript URL is dated 2026-08-07. I treat the call as 2026-07-30 and the transcript as posted later.

## Gaps / what I could not find

- Per-code CMS utilization counts and payment by year for 81479, 0239U, 0340U, 0242U, 0037U, 81420/81507, 81425–81427, 81415–81417. I did not open the CMS Part B utilization files.
- 2027 preliminary per-code rates for those codes, and the ADLT-specific 2027 treatment.
- A MolDX MRD-specific coverage decision for 2024–2026, and the content of the 2026-10-12 and proposed LCDs.
- Current NIPT penetration statistics (only an undated 25–50% range) and Illumina's NIPT exposure.
- Foundation Medicine's 2026 volumes (the 2025 Tempus/FMI items were not retrieved).
- Content of the ACS CAN August 2026 white paper and the Manatt Medicaid biomarker study (titles only).
- The corpus was not consulted for this assignment, so cross-checks against Illumina's own clinical-customer commentary remain open.

Sources:
- [CMS fact sheet, preliminary CY2027 CLFS](https://www.cms.gov/newsroom/fact-sheets/preliminary-calendar-year-cy-2027-medicare-clinical-laboratory-fee-schedule-payment-rates)
- [Forvis Mazars, 2026-10](https://www.forvismazars.us/forsights/2026/10/cms-releases-preliminary-2027-clinical-lab-fee-schedule-rates)
- [MedTech Dive](https://www.medtechdive.com/news/cms-sets-preliminary-cuts-to-medicare-lab-reimbursement-rates/831031/)
- [Natera Q2 2026 release](https://www.natera.com/company/news/natera-reports-second-quarter-2026-financial-results/)
- [Natera Q2 2026 call](https://www.fool.com/earnings/call-transcripts/2026/08/13/natera-ntra-q2-2026-earnings-call-transcript/)
- [Guardant Q2 2026 call](https://www.fool.com/earnings/call-transcripts/2026/08/07/guardant-health-gh-q2-2026-earnings-call-transcript/)
- [GeneDx Q2 2026 summary](https://www.marketbeat.com/instant-alerts/genedx-q2-earnings-call-highlights-2026-08-03/)
- [Tempus Q2 2026 release](https://www.businesswire.com/news/home/20260730328545/en/Tempus-Reports-Second-Quarter-2026-Results)
- [Dark Daily on OIG Part B report](https://www.darkdaily.com/2026/02/13/medicare-part-b-lab-spending-hits-8-4-billion-as-genetic-testing-captures-43-of-dollars/)
- [ACS CAN biomarker white paper](https://www.fightcancer.org/sites/default/files/state_biomarker_coverage_laws_white_paper_august_2026_0.pdf)
- [Discoveries in Health Policy, CLFS 0340U](https://www.discoveriesinhealthpolicy.com/2025/12/cms-issues-final-lab-fee-schedule-for.html)
