# Agent 08: Transition and unit-economics dataset (corpus)

*Model: sonnet. Run 2026-10-11 02:01:44. Cost $1.16 (API-equivalent).*

## Key findings

I built the dataset from the call extracts, decks, 10-Qs and the earlier scrape files. Wherever a figure is mine (derived or assumed), I label it OPINION/calc.

1. **FACT: the X is much cheaper per Gb, and the gap has widened.** I divided each platform's revenue share by its volume share. In Q2'26 the NovaSeq X earned about **$0.71** of HT revenue per unit of average Gb, against **$2.41** for the 6000. That makes the 6000 about **3.4x** the X per Gb, and the X about 70% cheaper. The ratio was 2.2x in Q2'24 and has been roughly 3.3–3.7x since Q3'25. [Q2'26 deck slide 8; Q2'26 call, 2026-07-30]
2. **FACT/MGMT: the observed gap matches the "60–70%" claim only from 2025.** The CFO said the 6000→X move "would have resulted overall, all-inclusive, easily more than 60% to 70% price decline on a Gb-to-Gb basis" (Dhingra, Q2'24 call, 2024-08-06, Sources line 276). The blended gap I compute was only 54–55% in 2024 and 65–71% from Q3'25. It is a mix-weighted figure, not a like-for-like list-price comparison.
3. **OPINION/calc: the 6000 still earns about $0.9B a year.**
   - It carries about 41% of HT consumables, which is about **$219M** in Q2'26 or **~$0.88B annualized** (range $0.83–0.92B).
   - That assumes HT is 69% of sequencing consumables, with a 65–72% sensitivity (see Assumptions).
   - If all of it converted at constant Gb and today's relative price, the loss is about **$617M a year**. That is about 29% of HT consumables, or about 20% of the sequencing consumables run-rate.
   - Break-even needs about **+41% total HT Gb**. Applied to the converting 6000 Gb alone, break-even needs about **+240%** (3.4x).
4. **OPINION/calc: each further 5 points of X volume share costs about 8.5% of HT revenue at constant Gb.** That is about 5.9% of sequencing consumables, or about $45M a quarter. If the clinical X target of 80–85% by end-2026 is met, total X volume reaches roughly 84–86%. That implies only about $18–35M a quarter of mix drag in 2H26. The bigger pool is the last ~15% of volume, which earns about 2.4x the X's revenue per Gb.
5. **OPINION/calc: most of the H1'26 per-Gb price decline is mix shift, not within-platform repricing.** Sequencing consumables grew +4.3% in Q1'26 and +4.7% in Q2'26, against Gb growth of ">30%". That implies a blended revenue-per-Gb decline of about −19% to −22%. The shift of X volume share from 69% to 83% over the year explains about −16%. That leaves only about **−4% to −7%** of within-platform price/mix, if the Gb floor and my HT assumption hold. As mix shift ends, the headwind should fall toward that residual. It still has to absorb the 35B flow cell (~20% lower $/Gb).
6. **FACT: the 6000 revenue base is not visibly eroding on a per-unit basis.**
   - Q4'25 implied 6000 pull-through is about $670K, which matches the FY25 actual of ~$670K.
   - The Q2'26 implied level is about $670–680K on a ~1,300 base. That is above the FY26 guide of $600–650K, though the Q2'26 base is my estimate.
   - This fits the Q4'25 call, where an analyst said 6000 pull-through was "holding up better than expected". It supports the over-earning suspicion.
7. **FACT: Illumina's own deck gives enough data to test the X pull-through, and it holds.** Implied X pull-through (X revenue ×4 ÷ average base) is about $1.34–1.37M in Q4'24 and Q4'25, matching the reported $1.3M and ~$1.35M. It is about $1.19–1.24M in Q1–Q2'26, probably because new units ramp over 6–9 months (Dhingra, Q2'26 call).
8. **FACT: placements are far above the guided 50–60 a quarter.** They ran 80+ in Q1'26 and 95+ in Q2'26, with roughly 60–70% going to clinical customers. Q1'26 commentary says these are "mostly incremental placements rather than conversions of 6000s", so parallel running is structural. [Q1'26 call, 2026-04-30; Q2'26 call]
9. **FACT: Gb growth has been reported only as a floor, ">30%", in every quarter since Q4'24.** The earlier figures were exact: +29% (Q3'23), +46% (Q4'23), >35% (Q1'24), >40% (Q2'24 and Q3'24). The floor hides how far volume sits above price. The "volume +X% vs price −Y%" split cannot be pinned down.
10. **FACT/MGMT: the transition metrics have been under-disclosed.**
    - Clinical X revenue share is not disclosed.
    - The 6000 revenue and Gb figures are not disclosed.
    - The Q4'25 deck said transition metrics would be "phased out", yet the Q1'26 and Q2'26 decks still carry them.
    - The 6000 pull-through was re-based on a net installed base from Feb 2024. The X pull-through was withheld until it looked good.
11. **FACT: the sequencing consumables history itself is inconsistent across sources.** FY24 is $2,858M in Bloomberg and $2,872M in the Q4'25 deck, so Q4'24 is $697–711M. I use ~$699M. See Contradictions.
12. **FACT: clinical share of consumables jumped from ~50% to >65% (2023–26).** The shares are 50% (Q1'23), 53% (Q2'23), ~50% (Feb 2024), 56% (Jan 2025), ~60% (Jul 2025), >65% (Apr–Jul 2026). A change in definition is plausible and no reconciliation exists (earlier scrape, Bernstein May 2024: the clinical bucket "includes clinical research").

---

## 1. Quarterly dataset, Q1'23–Q2'26

Notation: n/d means not disclosed in the corpus, and "d" means derived by me. The sources are the earnings calls, decks and 10-Qs.

### 1a. Sequencing consumables and growth

The first table shows reported sequencing consumables dollars and growth rates. Take away that reported consumables growth has been in the low-to-mid single digits for 13 quarters, while clinical grew double digits. Q1'23 through Q4'23 and Q4'24 are derived from reported growth rates, so treat them as ±$5M.

| Qtr | Seq. consumables $M | y/y | Ex-China clinical cons. growth | Ex-China research & applied | Source |
|---|---|---|---|---|---|
| Q1'23 | ~685 (d) | −12% (Q1'22 ≈ $778M less the $92M reported decline) | "mid-teens" activity growth; clinical 50% of seq. cons. | n/d | Q1'23 call; 10-Q Q1'23 (Core Notes 02, l.165) |
| Q2'23 | 734 | −1% | clinical activity +23% y/y; ~53% of cons. | activity −1% | Q2'23 call; 10-Q |
| Q3'23 | ~686 (d) | n/d | clinical cons. +10% (earlier scrape) | −12% | Q3'23 call, 2023-11-09 |
| Q4'23 | ~684 (d, FY plug) | n/d | n/d | n/d | FY23 $2,790M, Bloomberg |
| Q1'24 | 691 | +1% | 7% (Q3'25 deck) | n/d | 10-Q Q1'24; Q3'25 deck |
| Q2'24 | 729 | ~flat | 5% | n/d | 10-Q Q2'25 (shows Q2'24 = 729) |
| Q3'24 | 741 | +8% | 11% | n/d | 10-Q Q3'24; Q3'25 deck |
| Q4'24 | ~699 (d; 697–711) | n/d | 8% | n/d | FY24 total; Q4'25 +8% to $755M |
| Q1'25 | 696 | +1% | 8% | −11% | Core Notes 02; Q4'25/Q1'26 decks |
| Q2'25 | 740 | +1.5% | 10% | −9% | 10-Q Q2'25 |
| Q3'25 | 747 | n/d | 12% | −8% | Q3'25 call |
| Q4'25 | 755 | +8% (11% ex-China) | 20% | 0% | Q4'25 call |
| Q1'26 | 726 | +4.3% | 20% | −12% | Q1'26 deck/call |
| Q2'26 | 775 | +4.7% | 15% | −7% | Q2'26 call; Bloomberg |

- Annual totals: FY22 $2,919M, FY23 $2,790M, FY24 $2,858M (Bloomberg) or $2,872M (Q4'25 deck), FY25 $2,939M. FY25 clinical growth was 12%, research and applied −7% (ex-China).
- Clinical share of sequencing consumables is in the contradictions list above (finding 12).
- Consensus FY26–FY27 sequencing consumables are $3,104M and $3,378M (Bloomberg, 2026-10-10).

### 1b. NovaSeq X share of HT volume and HT revenue

This table shows the transition path. Revenue share has lagged volume share by 18–24 points throughout, and the lag is wider now (24 points) than in 2024 (18 points). Volume has almost finished converting; revenue conversion has not.

| Qtr | X % HT Gb (total) | X % HT consumables $ | Clinical X % Gb | Research X % Gb | Source |
|---|---|---|---|---|---|
| Q1'23–Q1'24 | n/d (no disclosure) | n/d | n/d | n/d | metric first given Q2'24 |
| Q2'24 | ~45% | 27% ("a little over 25%") | ~35% (chart) | n/d | Q2'24 call; Q2'26 deck |
| Q3'24 | 55% (call ">55%") | 36% (deck; call ">35%") | ~40% | n/d | Q3'24 call; Q2'26 deck |
| Q4'24 | 65–66% (call ">65%"; deck 66%) | 40% | ~50% | ~80% | Q4'24 call; Q2'26 deck; earlier scrape |
| Q1'25 | 68% | 43% | >50% | >80% | Q1'25 call |
| Q2'25 | 69% | 44% | ~55% | >80% | Q2'25 call |
| Q3'25 | 78% | 51% | ~64% | 91% | Q3'25 call/deck |
| Q4'25 | ~80% | 55% | >2/3 (71% per Freedom, 2026-02-10) | ~90% | Q4'25 call; Core Notes 08 |
| Q1'26 | 82% | 55% | 76% | ~90% | Q1'26 call |
| Q2'26 | 83% | 59% | 78% | 92% | Q2'26 call/deck |

- Clinical and research *revenue* share on the X are not disclosed. Q2'26 deck slide 8 shows them as chart series, but the extract's text is garbled and cannot be attributed. I did not render the original image.
- Clinical X-volume target for end-2026 is 80–85% (Q2'26). Earlier phrasing was "over 80% to 85%" and "over 85%" (Q1'26).

### 1c. NovaSeq X and 6000 installed base, placements and decommissions

This table shows how the X base grew and the 6000 base shrank. The X base has more than doubled since end-2023, while the 6000 fell about 400 net of the ~30 shipped.

| Qtr | X placements | X installed base | 6000 installed base | Source |
|---|---|---|---|---|
| Q1'23 | ~67 (d) | ~67 (d) | n/d | 176 − 109 from Q2'23 |
| Q2'23 | 109 | 176 | n/d | Q2'23 call |
| Q3'23 | 97 | 273 | n/d | Q3'23 call |
| Q4'23 | 79 | 352 | ~1,770 net (≈110 deactivated 2017–23, mostly 2023) | Q4'23 call |
| Q1'24 | 55 | >400 | n/d | Q1'24 call |
| Q2'24 | 62 | 469 | n/d | Q2'24 call |
| Q3'24 | 58 | 527 (528 in Dec) | ~1,700 | Q3'24 call; Evercore 2024-12-03 |
| Q4'24 | 91 | 630 | ~1,660 (d) | Q4'24 call; calc |
| Q1'25 | 60+ | ~690 (d) | n/d | Q1'25 call |
| Q2'25 | 50+ | ~740 (d) | n/d | Q2'25 call |
| Q3'25 | 55+ | ~795 (d) | n/d | Q3'25 call |
| Q4'25 | 100+ (95 at JPM) | ~890 | ~1,360 (≈330 decommissions in FY25, ~30 shipped) | Q4'25 deck slide 15 |
| Q1'26 | 80+ ("83") | ~970 | n/d | Q1'26 call; brief |
| Q2'26 | 95+ | ~1,065 (d, +95 and no decommissions) | n/d; >10 6000s *sold* | Q2'26 call |

- FY25 X placements are ~270 in the Q4'25 deck and ~260 at JPM. The 6000 installed base figure is the number I most want for Q2'26, and it is not disclosed.
- 527 + 91 = 618, not 630, so about 12 units are unexplained in Q4'24. It may reflect reagent-rental units or restated counts.
- Q4'24→Q4'25: 630 + 270 = 900 vs 890 reported, so about 10 units of attrition.

### 1d. Pull-through (annual consumables $ per installed instrument)

The guides show the 6000 re-based down and the X guide stepping up. Note the January 2024 switch to net installed base for the denominator.

| Period | NovaSeq 6000 | NovaSeq X | NextSeq 1k/2k | Source |
|---|---|---|---|---|
| FY23 guide (Aug 2023) | $800–900K (lowered from ~$1M) | none given | $120–170K | Q2'23 call |
| FY24 guide (Feb 2024, net base) | $700–800K | none given ("the math is not relevant") | $80–130K | Q4'23 call |
| Q2'24 | n/d | ">$1M" | n/d | Q2'24 call |
| FY24 actual | n/d | ~$1.3M | n/d | Q4'24 call |
| FY25 actual | ~$670K | ~$1,350K | ~$90K | Q4'25 deck slide 15 |
| FY26 guide | $600–650K | $1,350–1,400K | $80–100K | Q4'25 deck slide 15 |

- The FY25 pull-through guides (from the Feb 2025 deck) and any Q1–Q3'26 reaffirmations are not in the corpus extracts. Thaysen said (Q1'26) he saw X pull-through "above $1.3 million" at JPM, expecting it to hold or rise.

### 1e. Gb growth, price and flow cell data

| Qtr | Total Gb y/y (connected HT+MT) | Stated or implied price/Gb | Source |
|---|---|---|---|
| Q2'23 | +9% (run-based activity) | n/d | Q2'23 call |
| Q3'23 | +29% | n/d | Q3'23 call |
| Q4'23 | +46% | n/d | earlier scrape |
| Q1'24 | >35% | n/d | earlier scrape |
| Q2'24 | >40% | HT revenue ~+1% | Q2'24 call |
| Q3'24 | >40% | "closer to 25 rather than 20" (−20% to −25% model) | Q3'24 call |
| Q4'24 | >30% | ~−20% (calc) | Q4'24 call |
| Q1'25–Q2'25 | >30% | n/d | Q1'25, Q2'25 calls |
| Q3'25 | >30% (clinical stronger; research positive but below 30%) | n/d | Q3'25 call |
| Q4'25 | >30% | model: volume mid-20s, price mid-teens | Q4'25 call |
| Q1'26 | >30% (clinical "well above") | −21% (calc) | Q1'26 call |
| Q2'26 | >30% | −19.5% (calc) | Q2'26 call |

- Flow cell and genome price points mentioned in the corpus:
  - 25B flow cell launched Q4'23, "cuts cost per genome to about $200 but requires enough samples to fill the flow cell" (Feb 2024 analyst description).
  - A "$200 genome in a production environment" (Dhingra, Bernstein 2024-05-29).
  - 35B flow cell: price "not ready to talk" (Thaysen, Q1'26 call), and again at TD Cowen 2026-03-03.
  - Roche's $150 genome is the benchmark competitors cite.
  - Management said in Q2'25 it is "not committing to a 30B at this point".
- A genome is ~15x an exome (>120 Gb vs ~8 Gb), per the JPM 2026-01-13 deck.

---

## 2. Derived: implied HT revenue on X vs 6000

### Assumptions (all mine)

1. HT consumables = **69% of sequencing consumables**, with sensitivity 65–72%. I calibrated this to FY25. X pull-through ~$1.35M on an average base of ~760 gives ~$1,026M. The 6000 at ~$670K on an average base of ~1,510 gives ~$1,012M. Together that is ~$2.04B, or 69% of the $2,939M reported. The other platforms' disclosed bases and pull-throughs sum to ~$0.95B, which closes the gap to ~$2.99B. Average base means the mean of the beginning and end counts.
2. HT revenue split uses the reported "X % of HT consumables revenue" (shares rounded to the nearest point, so ±1 point).
3. The mid-throughput share and HiSeq are assumed stable. If mid-throughput shrinks faster, the HT share rises. I did not account for the 5–10 point swings in reagent-rental, lease or inventory timing.
4. Q4'24 sequencing consumables is ~$699M (derived).
5. X average base uses my reconstructed unit counts (see 1c). 6000 base values after Q4'25 are not disclosed, so I assume ~1,300 at Q2'26.

### 2a. Dollars by platform, Q2'24–Q2'26

HT consumables ($M) equals 0.69 × the sequencing consumables in 1a. This table shows that X revenue grew 2.3x in eight quarters while 6000 revenue fell 40%. Total HT revenue stayed in a ~$480–535M band, so the X growth has mostly replaced 6000 dollars. Q2'26 is the first quarter where the 6000's decline (−$7M y/y after −$67M in Q2'25) is slowing.

| Qtr | HT cons. $M (d) | X % rev | **X $M** | **6000 $M** | X annualized ÷ avg base (implied pull-through) |
|---|---|---|---|---|---|
| Q2'24 | 503 | 27% | 136 | 367 | $1.24M |
| Q3'24 | 511 | 36% | 184 | 327 | $1.48M |
| Q4'24 | 482 | 40% | 193 | 289 | $1.34M |
| Q1'25 | 480 | 43% | 206 | 274 | $1.25M |
| Q2'25 | 511 | 44% | 225 | 286 | $1.26M |
| Q3'25 | 515 | 51% | 263 | 252 | $1.37M |
| Q4'25 | 521 | 55% | 287 | 234 | $1.36M |
| Q1'26 | 501 | 55% | 276 | 225 | $1.19M |
| Q2'26 | 535 | 59% | 316 | 219 | $1.24M |

- Check against disclosed pull-through: Q4'24 and Q4'25 implied X pull-through match the reported $1.3M and ~$1.35M within 1–2%. The Q3'24 $1.48M is a high outlier (likely the 36% share rounding plus my base estimate).
- Management said X consumables revenue grew ">10% sequentially" in Q2'25 [Q2'25 call]. My split gives +9%, so my HT assumption or the rounding of the shares is slightly off.
- 6000 FY25 total from the table is $1,046M, against the pull-through arithmetic of ~$1,012M. The gap is 3% and within error.
- 6000 implied pull-through Q4'25: $234M × 4 ÷ ~1,390 average base ≈ **$673K**. That matches the reported $670K.
- 6000 implied Q2'26: $219M × 4 = $876M, which is ~$670K on a ~1,300 base. That is above the $600–650K guide. If the HT share is higher (72%), the number rises further. A 6000 base lower than 1,300 would raise it more. I cannot resolve this without the 6000 base.

### 2b. Revenue per Gb, X vs 6000

Method: the 6000's revenue per Gb is (1 − revenue share) ÷ (1 − volume share). The X's is revenue share ÷ volume share. Both are relative to the HT-average revenue per Gb (= 1.00). The ratio and the X's price as a percent of the 6000's are independent of the HT dollar assumption. This table shows the X price as 29–46% of the 6000's, drifting down.

| Qtr | X rev share / vol share | X rev per Gb (index) | 6000 rev per Gb (index) | 6000 ÷ X | X as % of 6000 |
|---|---|---|---|---|---|
| Q2'24 | 27 / 45 | 0.60 | 1.33 | 2.2x | 45% |
| Q3'24 | 36 / 55 | 0.65 | 1.42 | 2.2x | 46% |
| Q4'24 | 40 / 65 | 0.62 | 1.71 | 2.8x | 36% |
| Q1'25 | 43 / 68 | 0.63 | 1.78 | 2.8x | 35% |
| Q2'25 | 44 / 69 | 0.64 | 1.81 | 2.8x | 35% |
| Q3'25 | 51 / 78 | 0.65 | 2.23 | 3.4x | 29% |
| Q4'25 | 55 / 80 | 0.69 | 2.25 | 3.3x | 31% |
| Q1'26 | 55 / 82 | 0.67 | 2.50 | 3.7x | 27% |
| Q2'26 | 59 / 83 | 0.71 | 2.41 | 3.4x | 29.5% |

- Rounding sensitivity is material. A ±1 point error in both X shares moves the Q2'26 ratio between about 3.1x and 3.8x.
- The X's own index is stable at 0.60–0.71 (and slightly rising), while the 6000's index is rising as its volume shrinks. The remaining 6000 volume is the high-price, low-volume, mainly clinical tail.
- Why the 6000's per-Gb revenue is high: unfilled-flow-cell premiums, validated clinical assays, annual list price rises on the 6000, and no multi-unit discounts. Goswami said (Sept/Nov 2023) customers "pay a slightly higher effective price that we recover", and the earlier scrape notes the Q1'24 price initiatives. These are explanations from the earlier scrape; I did not quantify them. This is OPINION.
- The index cannot be turned into $/Gb because total Gb is not disclosed.

### 2c. Within-platform price vs mix, H1'26

This is OPINION/calc, and it depends on Gb growth being near 30%. Between Q2'25 and Q2'26:

- X volume share rose 69% → 83%. At the Q2'25 relative prices (0.638 and 1.806), mix alone cuts HT revenue per Gb by **−16.3%**.
- Gb growth was >30% (a floor) and sequencing consumables grew +4.7%. At exactly 30%, blended revenue per Gb fell 19.5%.
- That leaves **−3.7%** within-platform price/mix. At 35% Gb growth it is −7%. The true figure is probably in this range or worse, because the Gb floor is conservative.
- The mid-throughput decline is in sequencing consumables but not in "HT", and total Gb includes mid-throughput. Both effects bias my residual.

---

## 3. 6000 revenue still to convert

This table applies the Q2'26 relative prices to the Q2'26 6000 revenue. Annualized 6000 revenue is $876M, with an assumption range of $828–916M (65–72% HT share).

| Scenario (constant Gb, today's relative prices) | Revenue change, annualized | % of HT cons. | % of seq. cons. run-rate (~$3.1B) | Gb growth needed to offset |
|---|---|---|---|---|
| 100% of 6000 volume converts | −$617M | −29% | −20% | +41% on total HT Gb (+240% on converting Gb) |
| 80% converts (20% stays, per Thaysen Feb 2025) | −$494M | −23% | −16% | +30% total HT Gb |
| Management "60–70%" cut applied to $876M | −$526M to −$613M | −25% to −29% | −17% to −20% | +150% to +233% on converting Gb |
| 2026 target: X volume 83% → 85% | −$18M/qtr (~−$70M a year) | −3.4% | −2.3% | +3.5% |
| X volume 83% → 90% | −$64M/qtr (−11.9%) | −11.9% | −8.2% | +13.5% |

The 80% scenario is based on management's statement. The "20% stays" is Thaysen's rule of thumb (Q4'24 call, 2025-02-06, per the earlier scrape).

**What this means:**

- **Volume can offset the hit only if conversion is slow.** With total Gb growth of +30% and within-platform price −5%, moving X volume to 90% over 12 months yields HT revenue of about +9% (1.30 × 0.881 × 0.95 = 1.088). Moving to 95% yields about −2% (1.30 × 0.796 × 0.95 = 0.983). Dropping Gb growth to +25% at 90% gives about +5%. This is my arithmetic.
- **Clinical dominates what is left.** Backing out the clinical share of HT Gb from 83 = 78c + 92(1−c) gives c ≈ 64% of HT Gb (it ranges from about 55% to 65% across quarters because of rounding). About **83% of the remaining 6000 Gb is clinical**. If clinical and research 6000 prices per Gb are equal (an assumption), about $0.7B of annualized 6000 revenue is clinical. That is the over-earning candidate. It is also where management's own "long tail", FDA-approved and validated assays sit.
- **The mgmt "volume offset price in year 1, then accelerated" cohort** (n=40, Q3'25 deck slide 9) has no axis values and was not updated. It excludes laggards, so it does not speak to this tail.

**Margin:** I could not test whether 6000 consumables carry a higher gross margin. Goswami called 6000 consumables "highly profitable" (Q3'23). The 10-Qs have stopped naming reduced pricing as a margin driver after Q1'25 (earlier scrape). Non-GAAP gross margin was 68.2% in Q2'26 vs 69.4% a year earlier, explained by tariffs, memory costs, instrument mix and SomaLogic.

---

## Contradictions and stale data

- **Barclays "76% X volume share" (Q1'26) conflicts with the company's 82%.** Core Notes 09 quotes Barclays saying X volume rose 500 bps to 76% while revenue stayed at 55%. The company said 82% total and 76% *clinical* (Q1'26 call). The 500 bps increase matches clinical (71% → 76%). Barclays may have compared clinical volume with total revenue. OPINION: that makes the "quiet discounting" inference less secure. Thaysen called reading the 55% precisely "a little bit dangerous".
- **Sequencing consumables history:** FY24 is $2,858M (Bloomberg) vs $2,872M (Q4'25 deck). FY24 total consumables $3,155M (FY25 10-K) vs $3,169M (FY24 10-K). Q2'24 sequencing consumables is $729M in the Q2'25 10-Q.
- **Q3'24 revenue share:** ">35%" (call) vs 36% (Q2'26 deck). **Q4'24 volume share:** ">65%" (call) vs 66% (deck).
- **X placements:** Q4'25 is ">100" (call, deck), "~95" (JPM Jan 2026), and "second-highest quarter" while Q2'23 had 109. FY25 is ~260 or ~270. Q1'26 is "80+" and "83".
- **Clinical X target:** "80–85%" (Q2'26) vs "over 85%" (Q1'26, Thaysen to Canaccord).
- **Clinical share definitions** (above). The JPM deck pie extract is reversed (40% clinical) and is likely an extraction error.
- **Stale:** the Dec 2024 Dhingra "6000 active ~1,700" and 2024 pull-through guides are on different denominators than FY25. The 2023–24 price-decline estimates (20–25% a year, 60–70% all-in) predate the 35B plan and Roche's AXELIOS. The "40 converted clinical customers" cohort data is as of 2025-09-28.
- **Q4'24 X installed base:** 527 + 91 ≠ 630.
- **Roche's JPM-survey and AXELIOS data** are outside my scope.

## Gaps / what I could not find

- No dollar HT consumables revenue, no 6000 revenue or Gb, and no total Gb figure appear in any document. All dollars by platform are my derivation from share × an assumed 69% HT share.
- No clinical-vs-research X revenue share. The Q2'26 deck chart has it, but the text extraction is garbled, and I did not render the image.
- No 6000 installed base after Q4'25, no FY26 decommission guide, and no count of dual-running customers.
- No X share of HT metrics before Q2'24, and no HT/mid/low-throughput revenue split.
- No FY25 pull-through guide from the Feb 2025 deck (not in the call extract).
- No quarterly clinical-vs-research consumables dollar split. Clinical growth numbers are ex-China and are not reported for Q4'23 and Q1–Q2'25 beyond the figures above. For 2023, only "mid-teens" and "just under 20%" activity-type statements exist.
- Q1'23 consumables dollar data and Q3/Q4'23 figures are derived, not read from filings.
- I did not open the 10-Q segment tables for Q3'23 and Q4'23 sequencing consumables, which would replace three of my derived cells.
