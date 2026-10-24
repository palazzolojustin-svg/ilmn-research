# Why the 6000-to-X revenue-per-Gb ratio widened from 2.8x to 3.4x

*12 Oct 2026. The question: how much of the widening came from X revenue per Gb falling (cheaper X flow cells, discounts) versus 6000 revenue per Gb rising (a pricier remaining 6000 cohort)?*

*Inputs: Illumina's disclosed X shares of HT Gb and HT consumables revenue, and reported sequencing consumables dollars (calls, decks and 10-Qs, Q2 2024 to Q2 2026), as compiled in `2026-10-11_clinical_consumables_scrape/08_transition_and_unit_economics_dataset_corpus.md` and the ILMN call extracts. The arithmetic is ours.*

## Answer

Most of the widening most likely came from the X side: its revenue per Gb fell 10–19% in absolute terms. Over the same period the 6000's revenue per Gb was roughly flat to up about 7%. The exact split depends on high-throughput (HT) Gb growth, which Illumina discloses only as a floor of "more than 30%":

- At the 30% floor, about 60% of the widening is the X falling and 40% the 6000 rising.
- At 35–40% Gb growth, which is what the evidence in Core Notes 16 points to, 80–100% is the X falling.

Calling the X decline "new cheaper flow cells" probably gets the mechanism wrong:

- **No cheaper-per-Gb X flow cell launched in the window.** The 25B dates from late 2023, and its 100- and 200-cycle kits from Q4 2024. The 5B, launched in H1 2026, is smaller and pricier per Gb. The 35B arrives in 2027.
- **List prices didn't fall.** The 25B list price rose about 3%.
- **The likelier cause is who converted.** Large-volume users moved onto the 25B at deep negotiated discounts, which pulls down the X's average revenue per Gb.
- **The same conversions also lift the 6000's average.** When the big S4 users leave, the remaining 6000 base skews toward small, high-priced flow cells. So both halves of the widening are mostly one effect: which customers converted.

## The arithmetic (Q2 2025 to Q2 2026)

**Revenue moves.** Sequencing consumables rose from $740M to $775M (+4.7%). The X's share of HT revenue rose from 44% to 59%, and its share of HT Gb from 69% to 83%. Holding HT's share of consumables constant, that implies X HT revenue +40% and 6000 HT revenue −23%.

**Gb moves.** These depend on total HT Gb growth (g):

- X Gb grows by a factor of (83/69) × (1+g).
- 6000 Gb grows by a factor of (17/31) × (1+g).

**The identity.** Revenue per Gb is revenue divided by Gb. Whatever g is, the 6000's change is always about 1.20x the X's change. That reproduces the ratio going from 2.8x to about 3.35x. Only the split between the two sides depends on g, as the table shows:

| HT Gb growth | X revenue per Gb | 6000 revenue per Gb | Share of widening from the X |
|---|---|---|---|
| +30% (disclosed floor) | −10% | +7.6% | ~60% |
| +35% | −13.5% | +3.6% | ~80% |
| +40% | −16.6% | ~0% | ~100% |
| +45% | −19.5% | −3.5% | >100% (the 6000 fell too) |

**Cross-checks against list prices and pull-through:**
- The 6000's list price was trimmed 3.9–5.2% by Feb 2026, and the S4-to-25B list gap narrowed from about 2.76x to 2.58x. So any rise in 6000 revenue per Gb is composition, not repricing. At the 30% floor, composition would have to add about 11–12 points to offset the list cuts.
- At cores, the small 6000 flow cells cost 3.6–9.8x the 25B per Gb (Salk, Pitt). So a modest shift of the remaining base toward S2 and SP flow cells would produce that much.
- The 6000's pull-through (annual consumables per box) fell from about $670K (FY25) to a $600–650K guide (FY26), while the 6000 base shrank. That is consistent with 6000 Gb falling at least as fast as 6000 revenue.

## Caveats

- **Rounding.** The shares are rounded to whole points, so the ratio carries about ±0.3x of error. The 6000's 17% Gb share is the most sensitive input.
- **One-quarter jump.** Most of the move happened in one quarter, Q2 to Q3 2025, when the X's Gb share went 69% to 78% and the ratio 2.8x to 3.4x. Clinical conversion drove it (clinical X share 55% to 64%), not new boxes. Taken literally, that quarter implies the 6000's revenue per Gb jumped about 18%, which is implausible as pricing. Part of the step is therefore measurement: Gb shipped versus Gb used, plus lumpy timing. Even so, the ratio has held at 3.3–3.7x for four quarters, so it is not just noise.
- **Mismatched measures.** The ">30%" Gb growth covers connected HT and mid-throughput instruments and excludes China, which isn't connected. The shares measure HT Gb shipped. That mismatch adds error to g.
- **Missing disclosures.** Illumina has never disclosed the 25B's share of X output or any split of the 6000 by flow cell. Those are the two numbers that would settle the question.

## Implications for the thesis

- **The X's average revenue per Gb has been falling about 10–19% a year from conversion mix and discounts,** even without new flow cells. When the 35B arrives in H1 2027 (about −20% per Gb), it adds a list-price leg on top of that mix effect. This supports 1B.
- **The remaining 6000 cohort is not getting materially pricier per Gb.** At realistic Gb growth it is roughly flat. So the 2.4x revenue-per-Gb premium still on the 6000 (versus the HT average) is the size of the cut when it converts. Whether a converting user's price actually falls 60–70%, or only the 40–60% that like-for-like core prices suggest, remains the key open question for 1A.
