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
