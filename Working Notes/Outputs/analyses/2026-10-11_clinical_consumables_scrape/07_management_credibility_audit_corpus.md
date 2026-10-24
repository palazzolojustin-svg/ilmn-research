# Agent 07: Management credibility audit (corpus)

*Model: sonnet. Run 2026-10-11 02:01:35. Cost $1.38 (API-equivalent).*

## Key findings

1. **The transition-metric "phase out" was not fully carried out, and the remaining gap sits where the thesis needs data.**
   - FACT: The Q4'25 deck said "With transition milestones achieved, we will phase out transition-specific metrics after Q4 earnings" [ILMN Q4 2025 slides, 2026-02-05, Extracts/ILMN/deck/ILMN_2025Q4_Earnings_Slides.md].
   - FACT: The Q1'26 and Q2'26 decks still carry a "High-throughput transition" slide (slide 8). The Q2'26 call still gave HT volume and revenue share on the X (83%/59%) and clinical volume share (78%) [ILMN Q2 2026 slides, 2026-07-30; ILMN Q2 2026 call, 2026-07-30].
   - What was dropped: the 40-customer cohort ("Illumina will stop reporting cohorts", JPM, 2026-01-13) and any explicit clinical-only revenue share on the X. The Q4'25 deck charted the clinical revenue split, but the extract could not attribute the chart labels.
   - Thaysen also said it is "a little bit dangerous to read the figure precisely, since it is directional" when the 55% revenue share stayed flat Q4'25→Q1'26 [Q1 2026 call, 2026-04-30].
   - Severity: **High**. Directly relevant to Thesis Q1.

2. **The "no clinical cliff" claim rests on a selected cohort, and the tracking of that cohort stopped as the hard part began.**
   - MGMT: "There's no cliff happening" (Q2'25). "I've heard this clinical cliff a few times… that's not how we see it" (Q3'24). "It's not a cliff. It's a wave, and we are surfing it" (Q2'26).
   - FACT: The evidence was the Q3'25 case study of 40 "fully converted" clinical customers: "volume offset price in year 1 and then revenue and volume both accelerated in year 2". Thaysen said at Wolfe (2025-11-19) that the case study "excludes brand-new sequencing customers".
   - OPINION: This is survivorship-biased. The first customers to fully convert are the ones with expanding assays. Clinical was only ~64% converted by volume at the time, and Q1'26 laggards with FDA-regulated tests were said to "stay longer".
   - Severity: **High**. Directly relevant.

3. **Management dodged the "over-earning / parallel 6000 and X" question (Jefferies, Q2'26) and gave contradictory signals on 6000 longevity.**
   - MGMT: Thaysen called it normal, saying HiSeq systems "were in the portfolio until a few quarters ago" and that it was not a real headwind. No volumes, no estimate of 6000-attributable consumables, and no quantification of the later headwind [Q2 2026 call, Extracts/ILMN/earnings_call/ILMN_2026Q2_Earnings_Call.md].
   - FACT: Illumina placed "more than 10 NovaSeq 6000s" in Q2'26 "for customers planning to keep using that platform for years". Only ~30 were shipped in all of FY25.
   - FACT: The 6000 base was ~1,360 at end-FY25 after ~330 decommissions [JPM Jan 2026 slides]. In Q1'23 the CFO expected only "10 to 12 decommissions" among early X customers [Q1 2023 call, 2023-04-25].
   - Severity: **High**. Directly relevant.

4. **Guidance pattern: low-ball, then beat. The pattern is consistent, with real misses only in 2023.**
   - FACT: FY25 non-GAAP EPS guide went from ~$4.50 (Mar) to $4.20–4.30 (May) to $4.45–4.55 (Jul) to $4.65–4.75 (Oct), against an actual of $4.84.
   - FACT: The Jan'26 pre-announcement (Q4 EPS $1.27–1.30; FY $4.76–4.79) was beaten three weeks later ($1.35; $4.84).
   - FACT: FY26 EPS guide went $5.05–5.20 (Feb) to $5.15–5.30 (Apr) to $5.30–5.40 (Jul).
   - FACT: Q3'26 organic growth is guided at ~4.5% against Q2's 8.1% RoW organic. This is likely another conservative step-down.
   - Severity: **Low–Med**. Reliable direction, but headline "raises" are partly mechanical (e.g., a $20M raise after a $20M beat; "decimal points move").

5. **Operating-margin quality in H1'26 is flattered by government incentives.**
   - FACT: The Q2'26 10-Q reports government incentives of $28M year to date against $6M a year earlier [Core Notes 02, citing the Q2 2026 10-Q].
   - OPINION (my arithmetic, assuming the incentives sit in non-GAAP opex): the +$22M is ~1.0 pt of H1 revenue ($2,251M). H1 non-GAAP operating margin was 22.2% vs 22.1%, so ex-incentives it would be ~0.9 pt lower y/y.
   - FACT: Q2'26 non-GAAP opex also included ~60 bps of deferred compensation, offset in other income (EPS-neutral). Management cited "~23% excluding" it.
   - Severity: **Med**. Bears on the consumables-margin question.

6. **Clinical share of consumables has a loose, shifting definition, and the Core Notes contain a likely mislabel.**
   - FACT: Management gave these shares: ~50% (Q1'23), ~53% (Q2'23), 56% (Jan'25), ~60% (Q2'25 and Jan'26), >65% (Q1'26), ~65% (Q2'26).
   - OPINION: My growth arithmetic reconciles the 60%→65% move: ~58% a year earlier, with clinical +20% and research −12%.
   - MGMT/FACT: A former senior manager said it has "always been a very loose statement" and that Illumina "has been very generous and very broad in terms of classifying clinical use" [Tegus expert, Extracts/ILMN/expert_call/Expert_Tegus_Former_Senior_Manager_Global_Market_Development…].
   - FACT: The only FDA-approved CGP kit cited is TSO Comprehensive, and most clinical volume is LDTs at large labs.
   - Data issue: The extract of the JPM Jan'26 deck says "~60% Research & Applied / ~40% Clinical". The original lists "~40% … ~60% … Research & Applied … Clinical", so the label order is ambiguous. Management said ~60% clinical at that conference, so treat the extract's mapping as likely inverted. Verify in `Sources/ILMN/deck/ILMN_2026-01-13_JPM_Healthcare_Conference_Slides.md` lines 103–109.
   - Severity: **Med**. Relevant to Thesis Q1.

7. **The 2027 targets have been redefined and re-based twice.**
   - FACT: The Apr 2023 targets were 25% Core operating margin in 2024 and 27% in 2025, plus "mid-teens" long-term growth that "has not changed" (Aug'23). They were abandoned by Feb'24 (2024 guide ~20% margin) and replaced in Aug'24 with high-single-digit growth, 26% margin and double-digit-to-teens EPS growth in 2027.
   - FACT: In May'25 the target was re-stated as ex-China. At Wolfe (Nov'25) Thaysen said "the high single-digit growth is ex China at this point".
   - MGMT: After SomaLogic, Illumina will "get as close to the 26% operating margin as possible in '27". Thaysen said it stays "within 50 basis points" (TD Cowen, Mar'26).
   - MGMT: Thaysen called the $4.25 EPS midpoint "the new base" in May'25, and actual EPS came in at $4.84.
   - Severity: **Med**. Moderately relevant.

8. **Insider selling is concentrated and large; executive sales are small.**
   - FACT: Director Keith Meister sold ~3.06M shares (~$591M) between May and Sept 2026 at $145–$227, with no offsetting purchases [OpenInsider extract, 2026-10-10].
   - FACT: Roughly 2.06M of those shares (~$436M) were sold Aug 4–Sep 4, 2026, starting five days after Q2 earnings.
   - FACT: CEO Thaysen and CFO Dhingra bought $1.0M and $0.5M at ~$81 on 2025-05-12 and recorded no sales in the data. Four other executives sold ~$1.7M combined, with the General Counsel's sales at round prices ($160/$180/$200), which looks like a price-limit plan.
   - Data issue: The extract's headline total of "$1.13 billion" contradicts its own line items (~$591M for Meister plus ~$1.7M for others).
   - Severity: **Med** for sentiment, **Low** for thesis.

9. **Disclosure on instrument placements vs. revenue is thin, and reagent-rental economics are not quantified.**
   - FACT: Q1'26 had "83 units" (or "more than 80") but instrument revenue was $118M, below the ~$125–130M one analyst expected. Dhingra attributed the gap to volume discounts and rental/lease placements, with no count.
   - FACT: Q4'25 had ~5 rental/lease units among 100+ placements.
   - FACT: The ~21,000 "active instruments" include reagent-rental units.
   - OPINION: Rental units embed instrument cost recovery in consumable prices, which inflates pull-through. This matters if the X base is rising partly via rental.
   - Severity: **Med–High**.

10. **Cost-inflation messaging reversed in 90 days.**
    - MGMT (Apr 30): Mitigation is "meant to fully offset the inflation during the year" [Q1 2026 call].
    - MGMT (Jul 30): Memory and freight were a headwind "we didn't anticipate to the level we have seen". Illumina is "sharing some of the increase with customers" and stockpiled inventory [Q2 2026 call].
    - FACT: Net inventory rose $564M→$655M (YE25→Q2'26), while the inventory reserve fell $133M→$123M. Q2 operating cash flow was $201M vs $234M a year earlier [Core Notes 02, 10-Qs].
    - Severity: **Med**. A customer price increase is also a datapoint for pricing power.

11. **Leadership churn has been very high at the commercial and finance functions.** The detail is in section 6.
    - FACT: Four commercial or finance heads changed in under three years, and the CCO seat has been filled ad hoc.
    - Severity: **Med**.

12. **Capital allocation: a stated no-buyback stance was reversed within months.**
    - FACT: 10-Ks and the Q1'24 10-Q said "We do not intend to make any share repurchases during fiscal year 2024". A $1.5B authorization followed in Aug'24, with $116M bought in 2024.
    - FACT: Illumina then bought $742M in 2025 (avg $95), $366–370M in H1'26 (avg ~$124), and added another $1.5B on Apr 28, 2026.
    - Severity: **Low–Med**.

## 1. Guidance vs. actual, 2023–2026

Figures are non-GAAP unless noted. Sources: [Core Notes 04 and 05, built from the earnings-call extracts in Extracts/ILMN/earnings_call/]. I have not re-opened each transcript.

**FY2023 (Core / consolidated)**

| Date | Revenue | EPS | Core op. margin | X units | Notes |
|---|---|---|---|---|---|
| Feb 2023 | +7–10% consolidated | $1.25–1.50 | ~22% | >300 | Initial guide |
| Apr 25 | Held (7–10%) | Held | Held | >330 | Itemised "offsetting changes" inside an unchanged range |
| Aug 9 | ~+1% | $0.75–0.90 | ~20% | >390 supply | Cut, ~750 bp at midpoint |
| Nov 9 | −2% to −3% | $0.60–0.70 | 19–19.5% | 330–340 | Cut again |
| **Actual** | **−2% ($4,504M)** | Q1–Q4 sum **~$0.87** (derived: 0.08+0.32+0.33+0.14) | ~19–22% by quarter | **352 shipped** | |

- OPINION: The ~$0.17+ EPS beat vs the Nov range is again low-ball, but the revenue path was a ~1,000 bp miss vs the initial guide.
- FACT: Q2'23 quarterly EPS was $0.32 vs ~$0.01 guided. Q3'23 was $0.33 vs $0.10–0.15 guided. The Q3'23 call also called the quarter "a disappointing result" on revenue.

**FY2024 (Core)**

| Date | Revenue | Operating margin | EPS | Notes |
|---|---|---|---|---|
| Feb 2024 | ~Flat | ~20% | None | Instruments down high-teens |
| May | Held | ~20% | None | |
| Aug | −2% to −3% | 20.5–21% | $3.80–3.95 | First EPS guide; instruments down mid-30s |
| Nov | ~−3% | 21–21.5% | $4.05–4.15 | |
| **Actual** | **−2.4% ($4,332M)** | 21.3% | **$4.16 Core** | Just above the top of the range |

- FACT: In Q3'23 Thaysen said 2024 would "look very similar to 2023". The April-2023 target of 25% for 2024 was missed by ~370 bp.

**FY2025**

| Date | Revenue | Operating margin | EPS | Notes |
|---|---|---|---|---|
| Jan 2025 | $4.28–4.40B (low-single-digit growth) | ~23% | ~+10% (≈$4.58) | Prelim at JPM |
| Mar | n/a | n/a | ~$4.50 | |
| May | $4.18–4.26B | 21.5–22% | $4.20–4.30 | China cut $125M; tariffs ~$85M gross |
| Jul | $4.23–4.31B | 22–22.5% | $4.45–4.55 | |
| Oct | $4.27–4.31B | 22.75–23% | $4.65–4.75 | |
| Jan 2026 (prelim) | ~$4.339B | ~23% | $4.76–4.79 | |
| **Actual** | **$4,343M** | 23.1% | **$4.84** | |

- OPINION: The final revenue figure equals the original January midpoint, even though the China forecast was cut by ~$125M and recovered. Clinical strength refilled the hole.
- FACT: China guide went $165–185M → ~$200M → ~$220M → actual $243M.

**FY2026**

| Date | Revenue | Op. margin | EPS | Other |
|---|---|---|---|---|
| Feb 5 | $4.50–4.60B | 23.3–23.5% | $5.05–5.20 | ROW organic +2–4% |
| Apr 30 | $4.52–4.62B | 23.4–23.6% | $5.15–5.30 | Upper end of range |
| Jul 30 | $4.60–4.64B | 23.4–23.6% | $5.30–5.40 | ROW organic >5% |

- FACT: Quarterly beats: Q1'26 EPS $1.15 vs $1.02–1.07; Q2'26 EPS $1.31 vs $1.20–1.25 (revenue $1.159B vs $1.12–1.14B).
- FACT: Q1'26 margin was 150 bp above guidance.
- MGMT: The clinical-consumables guide stayed "double-digit to mid-teens" from February to April, even with a ~20% exit rate, and was lifted to "mid-teens" in July. H1 clinical growth was ~17%, so the guide implies ~13% in H2. Dhingra called it an "improvement from what we looked at in the beginning of the year".

## 2. KPIs introduced, redefined or discontinued

| Date | Change | Stated reason | Severity / thesis link |
|---|---|---|---|
| Q1'23 | Activity reported as run counts; clinical hit 50% of consumables "for the first time" | n/a | Low |
| Q2'23 (Aug) | Switch from run counts to **gigabases**; X pull-through "no figure until the ramp stabilizes" | X/NextSeq runs generate more data per run | Low; the Gb basis later became the core "elasticity" metric |
| Q4'23 (Feb'24) | NovaSeq 6000 **installed base reported net** of deactivations ("does not change reported revenue in any way") | n/a | **Med**. It raises measured 6000 pull-through. Pull-through is "simply quarterly consumables divided by the active base" (CFO). Guide moved from $800–900K to $700–800K (2024) to ~$670K actual (FY25) to $600–650K (FY26) |
| Q2'24 (Aug) | **New X-transition disclosures**: share of HT Gb and HT revenue on the X | "Increasing our disclosures" | Positive, but self-selected. Cohort and clinical-split data were later cut |
| Q1'25 (May) | **China separated**; headline becomes "ex-China"; 2027 target restated ex-China | Export ban / entity list | **Med** |
| Q3'25 | New slide 10 (ex-China consumables growth by clinical / research); 40-customer cohort slide 12 | Evidence of elasticity | Med |
| Q4'25 deck / Jan'26 | "Phase out transition-specific metrics"; stop reporting cohorts; "new KPIs" on clinical reimbursement, test launches, protein/spatial traction | "Transition milestones achieved" | **High**. Partially reversed in practice (see finding 1) |
| Jan'26 | **Four-region realignment**, prior periods restated | Align with the commercial organisation | Low |
| Q4'25–Q1'26 | **"Organic" and "RoW organic"** become the headline. RoW organic is "management's preferred measure of the business it can control" | Strips FX, SomaLogic and China | **Med**. Q2'26: 9.5% reported, 6.5% organic, 8.1% RoW organic |
| Q2'26 | Microarray line now includes SomaLogic (acquisitions added ~25 pts to microarray growth); SomaLogic revenue "reported mostly within microarrays" | n/a | Low–Med. Protein Prep is reported within library prep, with "better disclosure under consideration" (TD Cowen, Mar'26) |
| Q2'26 | BioInsight / Billion Cell Atlas revenue sits in services, "no commitment to a separate breakout" | n/a | **Med**. Services +14% included this lumpy revenue; no size given |
| Jan'26 | "Clinical" share cited from ~60% to >65%; classification unchanged but loose | n/a | See finding 6 |
| FY26 10-Q | **EPS-based PSUs "resumed in fiscal 2026"** alongside operating-margin and relative-TSR PSUs | Not stated in the extract | **Med**. Compensation metric change; Illumina says non-GAAP operating margin and EPS drive pay. It is unclear when EPS PSUs were suspended |

## 3. Statements later contradicted or qualified

| Statement | Later evidence | Verdict |
|---|---|---|
| deSouza (Apr'23): X supply "more manufacturing bound than demand bound"; ~750 single-6000 customers imply ~750 X units "right off the bat" | By Aug'23, onboarding was a "more challenging process than we anticipated". X guide went >390 → 330–340. Orders rose only ~50 vs 97 shipped in Q3'23 (BofA challenge). X base is ~890 at end-FY25 | Contradicted. **High** (credibility). Bears on the conversion timeline |
| Goswami (Apr'23): "only 10 to 12 decommissions" among early X customers | ~330 decommissions in FY25 alone | Contradicted in magnitude (different periods). **Med** |
| Goswami (Aug'23): "the issue is not competition at all"; mid-teens long-term growth "has not changed" | Mid-throughput and China competition repeatedly cited in 2023–24. Mid-teens abandoned Aug'24 | Contradicted. Med |
| Thaysen (Q1'24): "We didn't pull anything forward" | Dhingra, same call: early deliveries were ~¼ of the revenue beat. The prepared remarks said customers "accelerat[ed] delivery… from Q2 into Q1" | Internally inconsistent. Low |
| Thaysen (Q2'25 and Q3'25): no tariff or NIH pull-forward | Q1'25: "a little bit of pull-in in China". Beat in Q4'25 included a "small benefit" from year-end budget buying | Minor. Low |
| Management (Q1'25, RBC): a competitor's announcement was "a technology overview… it's easy to impress"; "there's no impact" | AXELIOS launched Jun 2026; Thaysen was critiquing it in detail at TD Cowen (Mar'26) and described "the consequences". Also Q1'25 on Ultima: "If you want to give your sequencing wafer free… you don't have a business"; Jan'26 pricing: "we are all for it" where elasticity is unlocked | Posture shifted. Med; relevant |
| Thaysen (Jan'26): the 40-customer cohort showed no "negative bump," only "flattish" year 1 | The Q3'25 slide: "volume offset price in year 1" | Consistent, but "flattish" is not the same as "accelerated". Wolfe read <5% growth in year 1 | 
| Dhingra (Apr'26): inflation mitigation to "fully offset"; Thaysen: manageable | Jul'26: "didn't anticipate to the level we have seen"; passing through price; stockpiling | Partly contradicted. Med |
| Dhingra (Q1'26): new X units generate consumables after "roughly six months" (Thaysen) | Jul'26: "at least six to nine months"; "modest" 2026 benefit, most in 2027 | Slipped. Low–Med; the raised consumables outlook gets less from placements than the headline implied |
| Instruments: placements "80+" | Revenue lagged (reagent rental, discounts); unit counts quoted three ways ("more than 80", "83", "80+") | Unresolved. Med |
| China: "transitory" (Q1'25) | Sanctions lifted Nov'25 but Illumina remains on the unreliable-entity list; China guided down again for 2026 | Open. Low |

## 4. Margin-quality items

- **Government incentives:** $28M YTD vs $6M [Q2 2026 10-Q]; see finding 5. Grant receivables rose to $45M at Q2 from $24M at Q1. **Med**.
- **Deferred compensation:** ~60 bps in Q2'26 opex, EPS-neutral, offset in other income; the "~23% ex" margin is a management construct. **Low–Med**.
- **Add-backs:**
  - FY25 GAAP→non-GAAP EPS add-backs: acquisition costs $0.53, "transformational initiatives" (restructuring plus the ERP upgrade) $0.39, impairment $0.15, "other" $0.14.
  - Restructuring totalled $261M since Q2'23.
  - ERP spend is still being excluded (due H1'27; management warns it "could affect internal controls").
  - Q1'26 restructuring fell to $1M vs $31M, so it is nearly absent.
  - On the positive side, Illumina's non-GAAP includes stock-based comp.
  - **Low–Med**.
- **Strategic investment gains** (retained GRAIL stake): $2.13/share of FY25 GAAP EPS ($5.45 GAAP vs $4.84 non-GAAP). Excluded from non-GAAP appropriately. Low.
- **Tariff refunds:**
  - FACT: IEEPA tariffs were struck down in Feb 2026, and the CIT ordered phased refunds in Mar 2026.
  - FACT: Illumina is "pursuing refunds, but recoveries so far are immaterial".
  - OPINION: Watch whether a one-off refund gets treated as non-GAAP and whether tariff costs are removed from the margin guide. **Low now, potential Med**.
- **Inventory and reserve:** see finding 10. The reserve fell while 6000-related stock exposure is arguably rising. OPINION; **Low–Med**.
- **Cash conversion:**
  - MGMT: ">140% FCF conversion" (JPM Jan'26, TTM to Sep'25).
  - OPINION (derived): H1'26 FCF was $412M vs ~$378M non-GAAP net income (EPS $2.46 × ~153.5M shares), or ~109%, driven by inventory build, capex and tax timing. Capex is guided to $225M vs $148M in FY25. **Med**.
- **Gross margin:** Non-GAAP 68.2% in both Q1'26 and Q2'26, vs 69.4% in Q2'25. Operating margin Q2'26 22.5% vs 23.8%. The H2 ramp to ~24% in Q3 is guided (not yet reported). Management explained the Q3 step as a consumables mix shift and cost actions.
- **Tax:** The 20% tax-rate cut in Jul'25 came from the July 4, 2025 law. It contributed $0.10 of the $0.25 EPS raise. Singapore tax holidays saved $37M in 2025. **Low**.

## 5. Capital allocation

- FACT: No buybacks 2022–1H24, with explicit statements of no intent for FY22–FY24 [FY2022/FY2023 10-Ks; Q1 2024 10-Q]. Then a $1.5B authorization in Aug 2024 (after the June GRAIL spin, before the Sept 6 EU fine withdrawal). Also a new $1.5B on Apr 28, 2026, with $1.8B available at Q2'26. **Low–Med**.
- FACT: Buyback prices by quarter: Q1'25 $200M at $115.74; Q2'25 $380M at $84.66; Q3'25 $120M at $97.10; Q4'25 $42M at $124.12; Q1'26 $242M at $120.85; Q2'26 $122M at $129.07. Purchases were heavy at lows and lighter as the price rose.
- OPINION: Buying at ~$121–129 in H1'26 while a director sold at $145–$227 is a fair "signal" question for the analyst, though it is not misconduct.
- FACT: M&A has been small and mostly unprofitable so far. Total SomaLogic cash outlay is ~$418M+ ($363M net at close + $25M milestone + $30M early buy-out), against the "$350M upfront" headline, with the contingent consideration booked at $81M and goodwill of $171M. Management said SomaLogic would turn profitable on a non-GAAP basis in 2027. Q1'26 dilution was −$0.04 EPS; the FY26 guide includes −$0.18 EPS and −100 bp of margin. **Low–Med**.
- FACT: Thaysen said "MRD is likely not the space we will be looking into" for M&A (Q1'25). Illumina also bought PacBio Onso IP (Q4'25) and a $50M patent portfolio (Q1'26) with no timeline. Low.
- FACT: Debt is $2.0B in four $500M notes. The 4.65% notes due Sept 9, 2026 are now current, against $1.17B cash and short-term investments at Q2'26. Gross leverage is ~1.6x. The 5.8% 2025 notes were refinanced into 4.75% 2030 notes in Nov'25. The Jun-2024 term loan (6.7%) was repaid by 4.65% bonds. Low.
- FACT: GRAIL legacy: $4.7B+ of impairments (2022–24), a $974M "Disposal Funding" outlay in the 2024 spin, EU fine withdrawn ($481M net gain), $9.8M DOJ settlement (Jul 2025), and derivative and securities suits still open (California class certified May 15, 2026; hearing Oct 30, 2026). Low for the clinical-consumables thesis.

## 6. Leadership churn

| Function | Sequence | Date |
|---|---|---|
| CEO | deSouza → interim Dadswell (GC) → Thaysen | Jun 2023 → Sept 2023 |
| CFO | Samad (left 2022) → Goswami (interim 2022, then CFO) → Dhingra | Apr 2024 |
| CTO | Aravanis (left Aug 2023) → Barnard | Aug 2023 |
| CMO | Febbo (left 2023) → Eric Green (joined Q4'25) | |
| CCO | Reeves (left 2024) → Cunningham (joined Aug 2024; left Jan 16, 2026) → Thaysen interim CCO (Q4'25–Q1'26) → Sullivan (joined by Q2'26; role not confirmed in the transcript) | |
| IR | Schwartz → Blanchett (interim, Q1'25) → McNamara (Q3'25) | |
| Chair | Thompson → MacMillan (2023) → Gottlieb (2025) | |
| Board | Meister joined 2025; three outgoing directors thanked in Apr'26; King and Skovronsky joined by Q2'26 | |
| Strategy | Goswami (also CFO) → Wedel (Nov 2023) | |
| Legal | Dadswell → Davies (GC, sells shares in 2026) → "Julie Coletti" joined by Q2'26 (legal experience) | |

- FACT: Thaysen is 3 years in. FACT: In Q3'23 executives received no stock or variable pay for 2023 because performance was "not up to par" [Goswami, Q3 2023 call] (positive credibility).
- OPINION: The CCO seat vacated in Jan'26 coincided with the strongest-ever placement numbers, so the sales leadership gap has not hurt reported results. A former Illumina associate director complained about the "Danish management team" lacking sequencing experience [Expert, 2026-07-24].
- Thesis link: The head of commercial is the person who negotiates clinical-lab contracts and pricing, so a new Sullivan era is worth tracking at the 35B / January 2027 price move.

## 7. Items bearing on the clinical-consumables thesis

| Item | Severity | Why it matters |
|---|---|---|
| Transition metrics partly retired; clinical-only revenue share on X unclear | High | Core input for Q1 (revenue at risk) |
| 40-customer cohort selection; cohort reporting stopped | High | Supports "volume offsets price" case, but biased |
| Jefferies question deflected; 6000s still placed (>10 in Q2'26) | High | Directly tests "parallel use" inflating consumables |
| Clinical definition loose (mostly LDTs) | Med | Customer-concentration and bargaining-power risk (Natera, Tempus, Caris, Foundation) |
| Gb growth >30% vs consumables ~5% | Med | "Output outpacing consumables revenue reflects the X price effect" (Dhingra, Q1'26). Management's long-term model: volume mid-20s, price mid-teens → ~7–10% growth |
| Pull-through definition changes (net base, rental units included) | Med | Per-instrument numbers can flatter |
| Reagent rental not quantified | Med–High | Embedded instrument payments in consumables |
| Government incentives / deferred comp in margin | Med | Margin trend is less strong than headline |
| Guidance sandbagging | Low–Med | Raises are a weaker signal than usual |
| Insider selling (Meister) | Med | Sentiment only |

## Contradictions and stale data

- Core Notes 01/06 state "60% Research & Applied / 40% Clinical" for the Jan'26 JPM slide. The original's order is ambiguous and management said ~60% clinical. Likely a mislabel [Extracts/ILMN/deck/ILMN_2026-01-13_JPM_Healthcare_Conference_Slides.md vs Sources version].
- The OpenInsider extract's "$1.13 billion" total sold conflicts with its own line items (~$591M for Meister).
- X placement counts vary within one call (Q1'26: "more than 80", "83", "80+"); JPM says ~95 in Q4'25 while the Q4 deck says "over 100".
- Q1'26 RoW sequencing consumables: Dhingra said +5% organic, Thaysen said "about 7%" (likely reported vs organic).
- Q4'25 margin change: Thaysen said 180 bp, Dhingra "nearly 200 bp".
- Q3'25 prepared remarks cited a "20%" operating-margin target; the Q&A said "26% in '27 and above" (likely a slip).
- Core Notes 02 says Q1'26 investment loss is $45M (10-Q), $37M (slides) or $38M (cash flow). FY2024 core consumables differ ($3,169M vs $3,155M) between filings. The FY25 foreign-tax-credit valuation allowance is $62M (10-K) vs $42M in Q3.
- The Q4'25 deck chart for X share of volume shows ~90% at Q4'25, while calls say ~80% at that point (the deck appears to chart a different cut, possibly research-only). Q2'24 starting point differs: ~45% (call) vs "mid-30s" (deck). Verify in the Sources decks.
- Volume share "mid-30s/45%" in Q2'24 is flagged in your known facts as ~45%.

## Gaps / what I could not find

- I relied on the Core Notes syntheses (02, 04, 05, 06) for most guidance and quote tracking and did not re-open every transcript. I opened originals only for: the JPM Jan'26 deck, the Q4'25 and Q2'26 deck extracts, the insider extracts and one Tegus expert call. Exact quotes from the transcripts should be verified before publication.
- I did not read the 10-K/10-Q originals for the deferred-compensation plan, the government-incentive line placement, the PSU history (when EPS PSUs were suspended) or the reserve methodology. These are flagged above as open.
- No disclosure found for the clinical-only X revenue share in 2026, the number of reagent-rental placements, the size of BioInsight / Billion Cell Atlas revenue, the SBC bridge, or the dollar backlog.
- The research notes (JPM, Barclays, UBS, BI) and the 20 expert-call extracts were not systematically audited for management-credibility commentary beyond the Tegus former-manager call and what Core Notes cite. Other agents may cover them.
- Q3 2026 results had not been reported as of the corpus date (2026-10-10). Q3'26 guidance is ~4.5% organic, $1.14–1.16B revenue, EPS $1.33–1.38, ~24% operating margin.
