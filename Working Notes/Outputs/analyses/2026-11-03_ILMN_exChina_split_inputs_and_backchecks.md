# ILMN ex-China clinical / R&A split: inputs and backchecks (3 Nov 2026)

This note covers the "Ex-China Consumables Mix" tab of `ILMN Model Claude Check .xlsx`. It asks two questions: which inputs are disclosed and which are estimated, and whether the derived clinical and research & applied (R&A) dollars reconcile with what Illumina has said.

## Bottom line

Every growth rate typed on the tab is a company disclosure, and so is every ex-China dollar figure for 2025 and 2026. Illumina has never disclosed clinical or R&A *dollars*, so those are always derived. The weakest link is the 2024 base: the tab back-solves 2024 ex-China dollars from rounded 2025 growth rates, and the split formula amplifies errors in those dollars about 5-6x.

Two disclosed 2024 figures are not yet used:

- 4Q24 ex-China sequencing consumables of $640m (Q4'25 deck), against the tab's back-solved $642.3m.
- FY2024 ex-China of $2,645m (Q4'25 deck), against the tab's $2,642.8m.

Using them moves 4Q24 R&A from $289m to $275m and clinical up by the same amount. That carries into the 4Q26E base: at the current -5% and +14% drivers, R&A goes from $274.6m to $261.2m and clinical from $483.3m to $499.3m. The ex-China total barely changes. The same constraint also narrows the gap between the tab's implied 2026 R&A growth and the reported rates.

## Inputs: disclosed versus estimated

**Disclosed** (company decks, reported basis):

| Input | Source |
|---|---|
| Ex-China y/y: total, clinical, R&A for 1Q24-3Q26, plus FY24 and FY25 | Q3'25 deck (2024 quarters), Q4'25 deck (2025), Q1-Q3'26 decks (2026) |
| Ex-China sequencing consumables $, 1Q25-3Q26 | Ex-China / "ROW" revenue table in each deck |
| 3Q24 ex-China $684m | Q3'25 deck. This resolves audit item B2: it is a reported number, not a typo. |
| 4Q24 ex-China $640m, FY24 $2,645m | Q4'25 deck, Table 1 (**not yet used by the tab**) |
| Total sequencing consumables $ | Revenue Build or 10-Q |

**Estimated** by the tab:

1. **2024 ex-China $ for 1Q, 2Q and 4Q.** Each is the 2025 figure ÷ (1 + rounded 2025 growth).
   - 4Q24 is disclosed ($640m).
   - 1Q24 and 2Q24 are pinned only as a pair: $2,645m − $640m − $684m = about $1,321m.
   - The "(0%)" in 1Q25 means a slight decline, so 1Q24 sits between $640m and $643m and 2Q24 between $678m and $681m.
2. **The 2024 clinical/R&A split.** It is solved so that the 2025 rates hold exactly, treating whole-percent rates as exact.
3. **All of 2023.** It is backed out from rounded 2024 rates, with R&A as the residual.
4. **2026 R&A.** It is ex-China minus clinical, so it absorbs all of the rounding.
5. **Greater China sequencing consumables.** Total minus ex-China, so each figure is accurate to about ±$1m, which is about ±2.5 points of growth. Illumina never states it.

## Backchecks

| # | Check | Model | Disclosed / anchor | Verdict |
|---|---|---|---|---|
| 1 | 2025 quarterly clinical and R&A growth | equal to reported | deck | True by construction, so not an independent test |
| 2 | FY2025 ex-China growth: total / clinical / R&A | +4.1% / +12.4% / -6.9% | +4% / +12% / -7% (Q4'25 deck) | Ties |
| 3 | FY2024 ex-China growth: total / clinical / R&A | +3.5% / +7.7% / -1.6% | +4% / +8% / -2% (Q3'25 deck) | Ties within rounding |
| 4 | FY2024 ex-China $ | 2,642.8 | 2,645 | $2m short |
| 5 | 4Q24 ex-China $ | 642.3 | 640 | Off by $2.3m, which moves the split by $14m |
| 6 | 2024 quarterly R&A growth (tests the 2023 back-solve) | -6.2 / -1.9 / +6.5 / -4.5% | -5 / -3 / +6 / -5% | Within about 1 point |
| 7 | 2026 R&A growth, implied vs reported | -13.8 / -8.0 / -7.3% | -12 / -7 / -6% | 1-2 points too negative in every quarter, so the 2025 R&A base looks low |
| 7b | Same, with disclosed 4Q24 and FY24 | -12.7 / -6.6 / -7.3% | -12 / -7 / -6% | 1Q and 2Q now within rounding |
| 8 | Reverse test: 2025 R&A solved from 2026 rates | 1Q-3Q25: 240 / 259 / 272 | 253 / 271 / 290 (rounding range 243-263, 255-286, 272-308) | Model is at or below the bottom of the range, which agrees with check 7 |
| 9 | 2026 ex-China growth implied from the dollar figures | +7.3 / +6.4 / +5.8% | +7 / +6 / +6% | Ties |
| 10 | Clinical share against management anchors | ex-China clinical as a share of *total* seq consumables: 2Q25 58%, 1Q26 66%, 2Q26 64%. As a share of *ex-China*: 62%, 70%, 68%. | "Roughly 60% of total sequencing consumables" (Q2'25 call); "more than 65%" (Q1'26); "approximately 65%" (Q2'26) | Fits if management means total. Runs 2-5 points high if management means ex-China. The basis is not stated. |
| 11 | Greater China consumables against all-product Greater China revenue | 3Q25-3Q26: 40, 42, 39, 41, 44 | Greater China revenue 52, 55, 52, 56, 59 | Consumables are about 73-77% of China revenue, which is plausible with instruments restricted. Direction matches. |

## Caveats

- **Reported versus organic.** All the 2026 rates on the tab are reported. Management's ex-China ("ROW") commentary and the FY26 guide are in organic or constant-currency terms, which run about 1-2 points lower for the total in 2026. Clinical and R&A are disclosed only on a reported basis. Comparing a reported Q4 R&A forecast to the "mid-to-high single-digit decline" guide therefore mixes bases.
- **Tariff refunds.** The Q3'26 deck figures ($748m and $792m) exclude tariff refunds.

## Suggested changes (analyst's call)

1. Type 4Q24 ex-China as $640m (blue; Q4'25 deck) in place of `=Q10/(1+Q6)`. This change is sourced, but it changes the 4Q26E R&A and clinical bases.
2. Split $1,321m across 1Q24 and 2Q24, for example $641.5m and $679.5m, so that FY24 ties to $2,645m. This is a judgement call, since only the sum is disclosed.
