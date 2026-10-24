# Agent 04: Expert calls (all 23)

*Model: sonnet. Run 2026-10-11 01:56:34. Cost $0.91 (API-equivalent).*

## Key findings

*Labels: **EXPERT-DIRECT** = first-hand experience, **OPINION** = expert inference, **HEARSAY** = second-hand. Nothing below is a company FACT or MGMT statement; these are expert-network calls. I worked from the 23 extracts and did not open the originals in `Sources/`. Citations use the call IDs in the weighting table below.*

1. **No expert quantified the remaining NovaSeq 6000 conversion or the revenue at risk, but several describe what keeps clinical tests on the 6000.** The recurring reasons are validation, FDA/LDT lock-in, and long-running trials.
   - MRD-guided trials "take five to seven years… you cannot switch an assay or a sequencer middle of a trial" (E1, Natera, OPINION).
   - Revalidation costs "$100,000, $200,000" per switch (E11, EXPERT-DIRECT), and in the worst case "$200 million of clinical trials" for an FDA or LDT product (E4, OPINION).
   - Adaptive stayed on a NextSeq 550 for about 10 years at "close to 10X as much per read" (E6, OPINION on a former employer).
   - A same-vendor move from NovaSeq 6000 to X "probably took Adaptive years" (E23, OPINION).
   - Read-through: the 6000 tail is sticky, but the stickiness is time-limited and driven by validation, not price.
2. **The 6000-to-X move is a price-for-volume trade, and experts disagree on who wins.**
   - An ex-Illumina Associate Director (AD, product management, left Jul 2025) estimates blended HT consumables price fell 30–40% from 2022 to now, from about $5/Gb toward $2.50. He says "the price decrease is keeping up with demand" and "flat would be a huge win" for core sequencing consumables (E5, computed on the spot, OPINION).
   - A second ex-AD (precision health, left Sep 2024) says the X delivered four 6000s' output at "almost half, if not 1/3" of the run cost, "cannibalized the business," and customers "ran out of samples… we actually did sequence everything in the freezer" (E20, EXPERT-DIRECT to Sep 2024).
   - The ex-FAS (field application scientist) says X consumables are cheaper than the 6000's and an X site "has little reason to switch" (E8).
   - Read-through: this supports the over-earning thesis. Clinical labs get more output per dollar and have "no samples left" to fill it, so volume growth has to come from new patients and tests, not capacity.
3. **Parallel running of 6000 and X is supported only indirectly.** UK NHS labs run the partner-mandated instrument plus "a second Illumina sequencer for CGP and other non-MRD" work (E13). A university core delayed its X Plus purchase by 1–1.5 years and lost customers "seeking vendors that could offer X Plus prices" (E17). Nobody sized parallel running in US clinical labs.
4. **The NovaSeq 6000 end-of-life is flagged as a competitive window.** "The NovaSeq 6000… is supposed to become obsolete," and that is where "some of the other players could come in" (E21, ex-Illumina medical affairs, now at Roche). "I don't know what's going on with their NovaSeq 6000, but… that is going to create an opportunity for a lot of other companies." Rival pitches such as the Element VITARI target X-class sites, and the ex-FAS says Element is already "moving customers from the X Plus to VITARI" (E8, HEARSAY).
5. **Clinical pricing power is eroding at the largest accounts, according to ex-employees.**
   - Large accounts (Broad, Natera, Guardant, Foundation Medicine) pay "half or even a quarter" of what a small CRO or core pays (E7). With a low-throughput instrument the gap is "five or tenfold."
   - Contracts "can very quickly become null and void" when a rival undercuts by 25–50%. Illumina either price-matches or doesn't (E5, EXPERT-DIRECT to Jul 2025).
   - For clinical customers: "quite a bit of price erosion in there as well… the sequencer is not that important to the assay output anymore" (E5).
   - Element could push Illumina's consumable margins "to below 50% in some cases" (E7).
6. **Customer concentration is extreme, and the bargaining power sits with the customer.**
   - The top 10–20 clinical labs drive most of the volume (E5, E20, E23, E3).
   - "Customers have big bargaining power and probably press Illumina on margin and earn much more margin themselves" (E20).
   - Roche/Foundation was "top 10, for sure" as a customer (E5).
   - Illumina's clinical growth is "largely driven by big accounts… Natera, Tempus, Caris, Foundation" and MRD (E22).
7. **Volume growth drivers are real but concentrated in MRD and liquid biopsy.**
   - Experts name oncology (about 50–60% of clinical), MRD and liquid biopsy as the growth areas. They call CGP "quite saturated," NIPT near saturation (about 70–80% of pregnancies, E20), and rare disease "not a very large growing market" (E14).
   - MRD repeat testing is "three to four tests in a year" (E20). The Natera expert cites a $5B MRD market growing to $30B by 2030 (E1, unverified).
   - Sequencing intensity is rising: tissue-informed MRD needs more than 80–120X, CGP 150X or deeper, and tumour work "easily more than 120" (E1, E22). WGS-based MRD is "the future" (E1).
8. **Rival clinical validation is happening quietly.**
   - A Roche precision-medicine lead says Foundation, Guardant and Natera "are talking to Ultima and… the Roche sequencer… There is validation ongoing with some of the other platforms. Whether they'll be successful or not is still up in the air" (E13, competitor-employed, HEARSAY). Today "everything runs on Illumina."
   - The ex-FAS says some population-genome projects are "secretly validating Ultima without telling Illumina" (E8).
   - A Natera director says Natera uses "aspects of" Element for ctDNA, but "the big four plus Natera, they're just using Illumina" (E1).
9. **Allegations about Illumina conduct come mainly from the ex-FAS (E8), plus one customer.**
   - Hospitality perks to key opinion leaders (KOLs) that "should not be allowed" under the Sunshine Act.
   - Refusing to support TSO validation on Element, so the customer "thinks four times."
   - Price increases "out of nowhere" on customers using third-party panels.
   - Georgia core director (E18): took instruments "on Illumina's schedule to help Illumina meet its local quarterly targets" on promised discounts that "were not honored."
   - Both are uncorroborated and, in the ex-FAS's case, come from someone working for a competitor ally (SOPHiA, which partners with Element).
10. **"Clinical" classification is loose.** The ex-Illumina senior manager (E22) says the >65% clinical figure is "always been a very loose statement… Illumina has been very generous and very broad," and that most clinical volume is LDTs, with TSO Comprehensive the only FDA-approved CGP assay he named. This corroborates the ex-employee quote already in your fact base.
11. **Competitive displacement is expected to be slow in the clinical core and faster at the edges.**
    - Share estimates: 80% → "about 70%" and "lose 30% by 2029–30" (E8); 80% → "mid-60s," flattening near 50% (E6, citing DeciBio); Roche takes "10–15 of 100" new instruments in 2027 (E5) or 10–20% of Illumina over three years (E23).
    - Others are much more sanguine: "won't be a significant loss" (E15), "maintain share" (E18).
12. **Further price cuts: the 35B flow cell is consistently expected to be a price cut but not a demand catalyst.**
    - The ex-AD estimates about $2.50/Gb → about $2/Gb (about 20%) and says a clinical lab's total workflow cost falls only "about 5%." Sample prep is under $100 and data processing $500–1,000 per clinical sample (E5).
    - A Mass. genome-center VP says the 35B is "expected to come out in January" 2027 (E19).
    - The ex-FAS offers "to shock you with some of the numbers that I see" on price per Gb, "a strategy that Illumina is going to opt in soon." This was not explored (E8). **A follow-up call is worth requesting.**
13. **Channel checks show academic and research volume mixed to weak, with prices stable over 90 days.** Research cores range from flat to +40% on volume, and the largest genome center sees FY26 about −5% on NIH funding (E19). No Illumina price change in 90 days (E19, E17, E18, E15). One expert notes Illumina price moves usually come in January (E19), which coincides with the expected 35B launch.

---

## Experts: weighting by recency and proximity

The weighting is my judgment. "Clinical-lab proximity" means direct knowledge of clinical consumables buying or running.

| ID | Expert (date of call) | Type / staleness | Weight for thesis |
|---|---|---|---|
| E1 | Natera Assoc. Director, oncology (2026-07-22) | Current customer, MRD | **High** on MRD/switching; she says her view is "biased for MRD"; low on pricing |
| E2 | Univ. of Arizona core manager (07-22) | Current, Element-primary core | Low–med (research) |
| E3 | Daisy Lab CSO, ex-Auckland core (07-23) | Left core Jan 2021 but speaks in present tense; stale | Low |
| E4 | Sr. Staff ML Scientist, ex-Illumina, now Exact/Genece (07-23) | Clinical dx customer; Illumina experience 5–7 yrs old; chose Ultima at a prior start-up | **Med–high** on switching economics |
| E5 | Ex-Illumina AD, product mgmt (07-23) | Left Jul 2025; ~12 months stale; post-exit items are inference | **High** on pricing and strategy |
| E6 | Ex-Illumina AD, same title (07-24) | Left Jul 2025. Same background as E5 (possibly the same person: same title and exit date; the extracts don't say) | Med. If the same person, don't count as two sources |
| E7 | Head of synbio, 50-person biotech (07-24) | Current, small customer | Low |
| E8 | Ex-Illumina FAS (07-24) | Left Oct 2024; now at SOPHiA (Element partner); clinical dx familiarity | **Med–high**, but potentially biased |
| E9 | Ex-Roche software engineer (07-27) | Competitor ex-employee, left Feb 2025 | Low |
| E10 | LifeStrands lab director, Australia (07-25) | Current small clinical lab; the "95% share" claim is unreliable | Med on switching cost only |
| E11 | Ex-Illumina senior architect (07-27) | Left Aug 2025, AI/software focus | Low |
| E12 | SC core director (07-30) | Current, buys through outsourced providers | Low–med |
| E13 | Abbott senior scientist (07-29) | Customer, says he has not used the X | Low |
| E14 | Roche precision-medicine lead, UK/NHS (07-29) | **Competitor-employed**, ex-Thermo; NHS direct | **Med–high** on clinical decentralisation; discount Roche views |
| E15 | Ex-Illumina staff scientist (07-30) | Dated; self-declared bias | Low |
| E16 | Georgia core director (07-31) | Current customer, concrete conduct claims | Med |
| E17 | Mass. genome-center VP (07-31) | Current, largest academic genome center | Med |
| E18 | PacBio segment lead, ex-Illumina to Jun 2021 (08-03) | **Competitor-employed**; Illumina knowledge 5 yrs old | Low–med |
| E19 | Ex-Illumina medical affairs, now Roche (08-05) | **Competitor-employed**; self-described "not helpful" on HT | Low–med |
| E20 | Ex-Illumina AD, precision health (08-06) | Left Sep 2024; ~2 yrs stale; still partly owns ILMN stock | **High** on sample saturation, concentration |
| E21 | Ex-Illumina senior manager, global market dev (Tegus, est. 2026-01-15) | Date uncertain; now pharma (Astellas) | **Med–high** on clinical definition and big accounts |
| E22 | Brigham & Women's core specialist (Tegus, est. 2026-10-10) | Current customer; no hands-on AXELIOS | Low–med |
| E23 | Oxford Nanopore Sr. Director, ex-Illumina 2008–14 (Tegus, est. 2026-10-01) | **Competitor-employed**; old Illumina knowledge | Med on switching dynamics; low on Illumina specifics |

Note: the call-ID numbering in my citations matches this table, not the file order.

---

## 1. Over-earning on the 6000 base: conversion, what holds tests on the 6000, price per Gb

**What the experts say about conversion**
- **Large clinical labs convert slowly, and conversion is a factory-floor project.** Natera, Caris and Guardant have "a factory floor full of Illumina systems," so conversion is "retooling your entire factory floor" and "none of these systems move quickly. They're years-long projects to switch" (E23, OPINION, partly from Adaptive's public remarks).
- **Adaptive's clonoSEQ:** the NovaSeq X turn-on "was the difference between unprofitable and profitable" and came "a year and a half to two years after the first instruments shipped" (E23, recollection of earnings calls, HEARSAY; not checked against the corpus).
- **A same-vendor 6000-to-X conversion is the easy case.** A cross-vendor move is "a four- or five-year project" (E23, OPINION).
- **Small-vs-large asymmetry (OPINION, E8):** a site with a 6000 loses on price to an AVITI. A site with an X Plus does not, because "Element will lose" on samples per flow cell and X consumable cost. This implies the 6000 base is the exposed part of the franchise, which is consistent with the thesis but unquantified.
- **The 6000 is already being de-emphasised.** Ex-FAS: "customers are also moving from NovaSeq 6000 to NovaSeq X Plus" (E8). A Georgia core "plans to sunset" its 6000 (E16, EXPERT-DIRECT).

**Price per Gb and per genome (what was actually said)**
- **List-ish economics (E5, OPINION):**

  | Item | Expert estimate |
  |---|---|
  | 6000 era | About $5/Gb |
  | X | About $2.50/Gb |
  | 35B flow cell | About $2/Gb |
  | X list, fully loaded genome (30X, about 100 Gb) | About $250 |
  | Sample prep | Under $100 |

  The expert notes he mixed per-Gb and per-genome units in the call.
- **Outsourced-provider pricing (E12, EXPERT-DIRECT):** under about $1,800–2,000 per lane; "under $4,000 per lane for a 10B or 25B flow cell lane" (his transcript is garbled). This is flat to slightly lower.
- **Opaque pricing (E12):** "Illumina prefers… individualized quotes rather than show unified pricing policies." Reportedly "huge discounts on quotes for NovaSeq X" (not tested by him).
- **Discount durability (E4):** the main complaint he hears is "whether reps give more discount, or remove the discount after a year or so."
- **Small-scale pricing (E3, E6):** "100X more expensive" at small scale (a rough guess in E3, stated twice). E6 explains it: lower-throughput instruments plus big-customer discounts, "five or tenfold" at the extreme.
- **No unified discount mechanism is visible.** The ex-FAS says Roche gives "reagent deals (e.g. 500 samples a year with discounts and free-of-charge items)" and customers "use these deals to push Illumina's prices down" (E8, HEARSAY).
- **Reagent rental and free placements:**
  - The ex-FAS says Illumina "historically never offered reagent rental" and now does "too late." His example: for a site like MSK with an X Plus installed, Illumina offers a free Hamilton, a free NextSeq 2000, training and a year of Illumina Connected Insights (ICI) software (E8, HEARSAY).
  - Ex-AD E5: Illumina "never did reagent rental while I was there"; he is "glad to hear they're starting."
  - The UK Roche lead (E14) says reagent rental "is what Illumina used to do." That conflicts with E5 and E8.

**Is clinical consumables revenue and margin inflated by the 6000 base?**
- No expert gave a margin split. The nearest evidence is E5's claim that the sequencer is no longer the key variable to clinical customers, and E6's that competitors can push Illumina consumable margins toward 50%.
- Direct evidence on *parallel* running (the Jefferies question) is thin: the NHS dual-instrument pattern (E14) and an Arizona sister core that has both 6000 and X (E2). Both are research or UK contexts, not US clinical.
- **OPINION (mine):** the experts are consistent with a 6000 tail that is high-priced per Gb and sticky because of validation. Nobody supplied a lab-level case where a clinical lab paid down its 6000 base and kept volume constant.

## 2. Go-forward volume and competition

**Volume (Gb) growth for clinical customers**
- **Clinical is where growth is:** "where all the growth is at the moment" (E14); "Clinical now larger than research. By the time I left (Sep 2024), clinical was 52% of revenue" (E20, EXPERT-DIRECT; this is the expert's recollection of revenue mix).
- **MRD:** repeat testing multiplier of 3–4 tests per patient per year (E20); a Natera view that MRD will equal all other testing in five years (E1); Ultima has publicly targeted MRD, and Roche likely will (E20).
- **Whole-genome MRD** is a rising intensity driver: "more companies are moving to whole-genome rather than whole-exome… the future" (E1, OPINION). Mid-single-digit-percent price relief on total cost won't change that (E5).
- **Intensity per test is rising:** 30X germline ≈ 100 Gb; tumour 120–200X (E22, OPINION); CGP ≥150X plus RNA (E1). A cost cut from $100 to $80 per sample moves total sample cost by "single digit" percent (E5).
- **Saturation and demand constraints:** NIPT at about 70–80% penetration (E20); CGP "quite saturated… very small year-on-year" (E14); the sample constraint ("sequenced everything in the freezer," E20); reimbursement/adoption as the bottleneck rather than cost: "even if sequencing is free" (E22). Community oncology adoption is "the billion-dollar question" and "difficult" (E22).
- **Price elasticity is weak now:** the NextSeq-to-NovaSeq era delivered 4× price cut and 5–10× volume; X-era cuts are ~20–50% with volume that "didn't get ahead of the price decrease" (E5, E6, OPINION). E6 recalls the historical pattern of "a 25% price decrease followed by 2X or 3X more sequencing" that "really wasn't the case" for the X.
- **Net (OPINION, mine):** experts support high-teens-to-20s clinical volume growth from a few large MRD/liquid biopsy accounts, but none supports volume offsetting a 60–70% per-Gb price drop on the converting 6000 base. E5's own numbers say the offset has been about 1:1 so far.

**Competition, clinical-lab angle**
- **Ultima:** $80–110 per sample for shallow-depth applications; Solaris below $0.40/M reads and a "$50 genome" (E1, HEARSAY). Cost "2–3× cheaper" and Q60 base quality with ppmSeq attracted a start-up's LDT (E4, EXPERT-DIRECT, a few years old). Aggressive to the Broad (E5). The Georgia core says Ultima's share of its lost work rose from about 10% to about 20% in two years and will "accelerate" (E16, EXPERT-DIRECT), but 80–90% of that lost work goes to low-cost providers such as Novogene.
- **Element:** cannot do deep MRD or CGP at 50X, per Natera (E1); "no oncology or infectious disease panels," per the ex-FAS (E8). Wins small and mid labs. Element prices are static through the product life cycle (E2, direct).
- **Roche AXELIOS:** three cautions.
  - It is RUO, the chemistry is "cumbersome" and a two-box workflow (E23).
  - It needs 150 ng DNA for the four-hour claim, "nearly impossible from a real patient" (E1).
  - Real-world data is thin: "a lot of hype without a lot of data" (E18).
  - On the other side: the Mass. genome center has a beta unit and expects to buy "a couple" (E17), described as price "on par, if not a little bit cheaper" than Illumina and "good data quality."
  - E22 (Brigham, no hands-on) says single-cell quality was equivalent at Q30 and 0.1% error.
- **AXELIOS share forecasts:** 10–15 of 100 instruments in 2027 (E5); 10–20% of Illumina's base over three years, though only if Roche is "quite aggressive" on all-in price (E23); "minimal" in year one (E17); "will just simply die out" (E12). These are not independent.
- **What customers say would pull them over:** a price cut. E22 says an Illumina cut to match Roche pushes Roche's timeline to "five to seven years." The 35B flow cell may be that cut.

**Customer concentration and bargaining power**
- **Concentration:** top 10–20 accounts "make up a very large proportion" (E5); "10 or so large sequencing houses… Natera, Guardant, Tempus and Caris" (E23, OPINION); Illumina's clinical revenue "very dominantly from a few large customers" (E20).
- **Leverage:** the Broad's discounts are "insane" and Ultima's "crazy pricing" gets the Broad to renegotiate (E5, EXPERT-DIRECT to Jul 2025).
- **UK structural risk:** NHS technology-transfer deals force local labs to buy "the same sequencer… the partner uses." If Natera, Guardant or Foundation validate a non-Illumina sequencer, all their transfer labs follow (E14). Illumina would need to "partner with companies such as Natera" to prevent this.
- **Upside offset:** Illumina's own MRD kit would let smaller labs build LDTs. The ex-Illumina senior manager is skeptical because the broad, tumour-agnostic approach "needs a lot of sequencing and therefore high cost" (E21).

## 3. Conduct, credibility and disclosure (all experts' allegations, none verified)

| Topic | Source | Claim | Reliability |
|---|---|---|---|
| Sunshine Act / HCP perks | E8 | Illumina partnering with distributors and offering conferences, hotels and perks to KOLs; "should not be allowed" | Uncorroborated; ex-FAS now at a competitor-aligned vendor |
| Blocking competitor validation | E8 | Tells TSO customers its pipeline "is not validated on Element and it will not support the validation" | Plausible; no second source |
| Price hikes "out of nowhere" on third-party panel users | E8 | Some customers then placed Roche instruments | Contrasts with E15/E17/E18 saying no change in 90 days |
| Quarter-end instrument pull-forward with unkept discount promises | E16 | Took delivery to help local quarterly targets on promised discounts; "not honored"; rep turnover | EXPERT-DIRECT, single customer. **Credibility-relevant: pull-forward on promises** |
| "Clinical" definition | E21 | "Very loose," "generous and broad"; mostly LDTs | Ex-employee, undated |
| Opaque quotes | E12 | Individualized quotes rather than unified pricing | EXPERT-DIRECT |
| Moves away from past practice | E8, E5 | Free instruments, bundles, reagent rental after avoiding it for brand reasons | Contradicts E14 |
| Leadership/culture | E6 | Strategy and R&D talent loss; "Illumina lifers"; management with "very little sequencing-market experience" and "poor advice"; "lifers want to return to 20, 30, 40%" growth | Opinion; ex-employee |
| Layoffs | E8 | "There is one coming soon" per ex-colleagues | HEARSAY |
| Support | E16 | About 6.5/10; longstanding rep left, newer reps "more junior with less ability to work out deals" | EXPERT-DIRECT (managers' view guessed) |
| Metric changes / dropped disclosures | none | No expert addressed the dropped transition metrics or compensation metrics | Gap |

- Expert E20 still holds ILMN stock. E8 and E14 are tied to competitors (SOPHiA and Roche).
- E5 and E6 describe a "complete strategic shift" to an ecosystem lock-in strategy because of the "great patent cliffs." That is a framing of why Illumina pushes assays, not evidence of misconduct.

## 4. Read-through from customers and competitors

- **Clinical customers:**
  - Natera is a loyal Illumina user and says "the barriers to bypass… are very, very high" (E1).
  - A start-up that chose Ultima for cost shows the entry point is emerging assays (E4).
  - The UK shift from send-out to in-house technology transfer is a risk and an opportunity (E14).
  - The Australian lab says "Illumina, for me, is always going to win" but flags a software-lock-in reason: it regretted trying a non-Illumina sequencer (E10).
- **Competitors:**
  - **Roche:** hype, sales channel and CDx links (some pharma wary of Roche-tied tests, E21). Slow execution (E23). Roche-employed experts want to see AXELIOS adoption by Foundation.
  - **Ultima:** quietly pursuing large accounts. E23 says "Ultima's doomed in the long run," which conflicts with E16's "accelerating."
  - **Element:** the strongest small/mid challenger (E8, E20, E17), but not a deep-MRD platform.
  - **PacBio/Nanopore:** niche; PacBio's own lead says "race to the bottom" for short-read (E18).
  - **Thermo:** Ion Torrent wins on small-panel workflow but not WGS (E21, E19); "losing the market so bad" in CGP per E8.
  - **MGI:** variable. A NZ agricultural provider is "ditching their very large Illumina sequencers for MGI" (E3, possibly stale), while the ex-FAS says MGI "lost its touch" (E8).
  - **10x:** pushing back on Illumina on spatial and wins on single-cell (E6, E15, E21). Atera could "eat away at some of the activities that people use sequencing readouts for" (E17). This weakens the non-sequencing growth narrative.

## 5. Channel checks, Q2 2026 (research/core heavy)

| Source | Q2'26 volume vs Q2'25 | FY26 view | Price/discount |
|---|---|---|---|
| Arizona core (E2, Element) | ~flat to +5–10% | flat | Element price flat |
| 50-person biotech (E7) | +25–50% | +25–50% | Reagent prices "up every year"; no change in 90 days |
| SC core (E12) | ~+40% (via outsourced X) | higher | Provider lane pricing flat/lower; moving to Element for ≥80% of in-house |
| Georgia core (E16) | Flat only due to a contract; underlying down; 2025 about −20% | ~same | Hard to negotiate volume discounts |
| Mass. genome center (E17) | Flat | ~−5% | No change; list price changes usually in January |

These are research-weighted and don't speak directly to clinical.

## Contradictions and stale data

- **Share loss:**
  - E8 says 80→70% and −30% more by 2029–30. E6 says 80→mid-60s→50%. E1 says gradual (a 2–3% revenue loss "last year," a recollection that conflicts with the corpus). E15 says "not significant." E10 says Illumina has about 95% (an unreliable figure).
  - The ex-FAS's 80%→70% and E6's "mid-60s" are different metrics, and neither cites a source beyond DeciBio (E6).
- **Reagent rental history:** E5 and E8 say Illumina never did it. E14 says "that's what Illumina used to do."
- **Mechanism of flat core consumables:** E5 says flat since 2022. The corpus shows clinical growth of 8–20% ex-China, so E5's claim applies to HT blended or total, not clinical. His description of "attach rate declines almost every year" is the interviewer's.
- **Pricing stability vs hikes:** E8's "price increases out of nowhere" conflicts with four channel checks reporting no price change over 90 days (a different customer set and timeframe).
- **E5 vs E6 are likely the same person** (same title, left Jul 2025, same Atera and StrataMap content). Treat as one voice.
- **Natera inconsistency:** E1 says Natera uses Element for ctDNA and also that the "big four plus Natera… just using Illumina."
- **E19 (Roche) attributes AXELIOS to Element** ("Element's AXELIOS"); the transcript is unreliable on that point.
- **Product naming errors in transcripts:** Constellation/TruPath, "Xcelris," "Somagen." The Ultima Q60/Q70 claims differ (E4 Q60, E6 Q70).
- **Stale:** E3 (left 2021), E18 (left 2021), E23 (Illumina 2008–14), E6/E5 (Jul 2025), E20 (Sep 2024), E8 (Oct 2024), E21 date uncertain. The Brigham, ONT and Tegus calls have inferred dates (the extracts say so).

## Gaps / what I could not find

- No expert gave the remaining NovaSeq 6000 clinical base, the conversion pace, or the Q2 2026 X-share figures. None addressed Jefferies' parallel-running question directly.
- No clinical lab disclosed what it pays per Gb. Only E5/E6 give indicative tiers.
- Nothing on compensation-metric changes, dropped disclosures, insider selling, guidance games or accounting. No expert addressed them.
- Rare disease, NIPT and MCED volume data are thin (E20 on NIPT penetration, E14 on rare disease). There is no MCED view beyond a mention in E4.
- No Natera, Guardant or Exact employee spoke about their actual sequencing-cost plans. The only Natera voice (E1) is a lifecycle manager who is "biased for MRD."
- I did not open the originals in `Sources/`; the extracts carried the quotes used. A follow-up call with the ex-FAS (E8) on "price per gigabase… shock you with the numbers" is the best lead for Q2 (further price cuts).
