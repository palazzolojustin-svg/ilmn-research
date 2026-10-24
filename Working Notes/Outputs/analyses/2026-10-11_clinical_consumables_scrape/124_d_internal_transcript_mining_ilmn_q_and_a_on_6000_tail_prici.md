# Agent 124: D-internal-transcript-mining-ILMN-Q-and-A-on-6000-tail-pricing-35B-and-sell-side-model-rec

*Model: sonnet. Run 2026-10-11 11:43:53. Cost $1.26 (API-equivalent).*

**Assignment:** Use the local corpus only (Working Notes/INDEX.md, then Extracts/ and Sources/ for ILMN earnings_call, conference, deck, and research folders, plus the Outputs/analyses/2026-10-11_clinical_consumables_scrape files). Three tasks not yet done. (1) Sell-side model reconciliation: from every sell-side note and consensus sheet in the corpus (JPM, Barclays, UBS, Freedom, Evercore, Bernstein, Wolfe, TD Cowen, Guggenheim, RBC, Deutsche, Canaccord, Jefferies), extract each analyst's explicit assumptions on (a) NovaSeq 6000 revenue/decline, (b) clinical consumables growth for 2026/2027/2028, (c) price per Gb decline, (d) Gb growth, (e) the 35B price cut, and (f) gross margin. Build a table of analyst, date, assumption, and quote, and identify which assumptions are implicitly inconsistent with the Q2'26 83%/59% share math (for example, a model that has HT revenue growing while the 6000 converts). (2) Management word-choice diff across the Q1'26, Q2'26 calls, the Jun-Sep 2026 conferences and the latest available material (Aug-Oct 2026): list every statement about price per Gb, 'elasticity', 'laggards', 'cliff', '6000 end of life', 'reagent rental', 'multi-year agreements', 'commitments' and 'volume discounts', and note where the statement softened, hardened or contradicts an earlier statement. Give exact short quotes with date and file. (3) Build a Q3'26 earnings checklist (call expected around late Oct/early Nov 2026): the metrics whose reporting or omission would signal over-earning unwinding (X revenue/volume share, clinical X volume share vs the 80-85% target, 6000 pull-through vs the $600-650K guide, ex-China clinical growth vs mid-teens guide, GM vs 68.2%), with thresholds from the corpus for 'good', 'neutral' and 'bad'. Flag all contradictions and unverifiable numbers. Do not repeat the existing ledger items E001-E146; add only new quotes, numbers or inconsistencies, and cite file names and dates.

## Key findings

The ledger already holds most of the management quotes. What I could add is (a) a per-analyst model table, (b) how JPM's estimates moved over time, and (c) one correction to E016. I did not find any model that states an explicit 6000 revenue decline or a 35B price assumption.

1. **No sell-side note in the corpus models the NovaSeq 6000 revenue decline, a $/Gb path or the 35B price cut explicitly (FACT).** I read every ILMN research extract dated 2026 for JPM, Barclays, UBS and Freedom. None of them gives a 6000 revenue line. None gives a $/Gb path or a 35B price assumption, and none models HT or X consumables separately. Evercore, Bernstein, Wolfe, TD Cowen, Guggenheim, RBC, Deutsche, Canaccord and Jefferies appear only as call questioners or in E172 (price targets, no model). The 83%/59% share math therefore cannot be tested against any analyst's model line. It can only be tested against implied growth rates and the qualitative claims below.

2. **JPM's out-year revenue rose sharply with no new tail data (FACT).**

| JPM note | FY27E revenue | FY28E revenue | FY29E revenue | FY27E GM | FY28E GM |
|---|---|---|---|---|---|
| 3 Mar | $4,886M (+7.4%) | $5,147M (+5.4%) | $5,429M | 69.0% | 69.2% |
| 1 May | $4,799M (+4.9%) | $5,075M (+5.8%) | $5,414M | 68.8% | 69.0% |
| 10 Jun | $4,919M (+7.3%) | $5,401M (+9.8%) | $5,876M | 68.8% | 69.0% |
| 16 Jul | $5,000M (+9.1%) | $5,601M (+12.0%) | $6,199M | 68.8% | 69.1% |
| 31 Jul | $5,047M (+9.1%) | $5,652M (+12.0%) | $6,261M | 68.8% | 69.1% |

   - From May to Jul-31, FY28E revenue is up 11.4% and FY29E is up 15.6%.
   - FY28E EPS went from $6.48 to $7.41, up 14% (JPM 1Q26 recap, 2026-05-01; JPM 2Q26 recap, 2026-07-31).
   - Gross margin barely moved, even though JPM itself flags that reagent rentals "may pressure average selling prices" (JPM, 2026-06-10).
   - The 16 Jul note says only that outer-year revenue was raised "to reflect improved visibility into consumables-led growth."
   - The 12% FY28E growth is above management's own "HSD" 2027 framing.
   - This is OPINION on the interpretation. The revisions follow the stock (target $120 → $125 → $185 → $220 → $230) and JPM's own May customer survey.

3. **JPM and Illumina do not agree on the price decline (FACT, then OPINION).**
   - Management's long-term model has mid-teens price decline per year (E047).
   - JPM says its survey implies a pricing gap of 2.4 to 5.2 points, "smaller than the '-DD%' pricing pressure seen for Illumina recently" (JPM, 2026-06-10).
   - JPM's thesis is that the transition headwinds are "largely gone exiting this year" (E173). That treats the 6000 → X step as finished.
   - But 41% of HT revenue is still on the 6000, and the 6000-to-X revenue ratio per Gb is 3.4x. E004 puts full conversion at about −29% of HT consumables.
   - Back-solving E004 gives roughly $36M a year of revenue lost per 1 point of HT volume that moves from the 6000 to the X (−$617M ÷ 17 points). I derived that figure and it is not reported. Moving the clinical X volume share from 78% to 85% costs a similar amount, before any volume growth.

4. **Barclays is the only house with falling gross margin, and its own multiple logic is inconsistent (FACT, then OPINION).**
   - Barclays' gross margin forecast is 68.4% (2026E), 67.8% (2027E) and 67.9% (2028E) (Barclays, 2026-07-31). Every other model has GM rising to about 69%.
   - Barclays says it "cannot justify the 35x PE" but raised its target multiple from 21x to 23.5x to 28x across three notes (Apr and Jul). It also rolled the base year forward to 2027, and the target is 28x FY27E EPS of $5.73.
   - Barclays' Feb note shows 2027E/2028E GM of 71.2%/71.9%. That conflicts with 67.8%/67.9% six months later and looks like a data or definition error (unverifiable).
   - Barclays' FY25A GM is 68.5% (Aug). The company, JPM and UBS show 68.2%, and Barclays' own Feb note showed 68.6%.

5. **Freedom's own text and model contradict each other on gross margin (FACT, calc).**
   - From Freedom's Aug 5 tables, gross profit divided by revenue gives GM of 67.6% (2026E), 68.0% (2027E) and 68.5% (2028E). Quarterly it is 67.7% (Q3'26E) and 66.6% (Q4'26E).
   - Q4'26E at 66.6% is well below Q2's actual 68.2%. Yet Freedom's EBIT margin rises to about 25% in Q4 (309 ÷ 1,234).
   - The text says it "expects meaningful gross margin expansion... from 2027." The model has 2027E only 40bp above 2026E and still below FY25 (68.2%).
   - Freedom lists "completion of the NovaSeq X transition" as something that "should help offset price erosion." That is the reverse of the mechanism in E004. Conversion of the remaining 6000 base is the price erosion.

6. **Correction to E016: "not a cliff, a wave" was not about the 6000 tail (FACT).**
   - In the Q2'26 call source, Leerink's question was about a "clinical cliff" in demand growth.
   - Thaysen answered: "Talking about the clinical cliff, I agree, it's not a cliff. It's a wave, and we are surfing it" (ILMN Q2 2026 call, 2026-07-30, Sources/ILMN/earnings_call/ILMN_2026Q2_Earnings_Call.md, line 230).
   - The 6000 answer (Jefferies/Peterson) used a different frame: "standard part of the business."
   - E016 merges the two. "Cliff" was an analyst's word about demand. Management has never described the 6000 revenue run-off itself with that word.

7. **Elasticity language is inconsistent across audiences (MGMT).**
   - JPM Jan 2026: "elasticity dynamics" are "clearly taking hold... most evident in clinical."
   - Q1'26 call, to Stifel: "aggressive pricing brings aggressive volume growth."
   - TD Cowen, 2026-03-03, on counting applications: if sequencing price halves, "you might be able to do 20% more." That is an elasticity of about 0.3.
   - The word does not appear in the Q2 call extract. Management applies "elasticity" where it helps (exome → genome) and rejects it where Roche competes (counting). There is no disclosed volume-versus-price data to settle it.

8. **Management let the price discussion fade as the Roche price landed (MGMT).**
   - TD Cowen (3 Mar): "there's definitely still some pricing headwind," which "shouldn't be worse than '25."
   - Q1 call: "the price headwind is receding." Dhingra said "no change in pricing-transition assumptions."
   - Q2 call: no explicit price-per-Gb statement. The Jefferies answer calls the 6000 conversion "not a true headwind."
   - "Not worse than '25" is a low bar. 2025 had a roughly −DD price effect (JPM's wording).

9. **JPM's model changes show the 6000 tail is not in the Street's numbers (OPINION).**
   - JPM's model rests on three claims: sticky clinical customers, "meaningful switching friction," and the survey.
   - None of these addresses the revenue per Gb of the remaining 6000 base.
   - The Q2'26 JPM note records "over 10" new 6000s sold and "as much as half" of clinical X placements as incremental. JPM calls the 6000 sales "interesting" but does not model them.

10. **JPM's WACC moved again in the Aug note (FACT).** Aug 2026 uses 9.8%. The Jun note used 9.1% and the Jul note 8.9%. E173 has only 10.2% → 8.9%. The DCF target went up while the discount rate went back up, so the $230 (Dec-27) target is not a like-for-like comparison with $220 (Dec-26).

## 1. Sell-side model table

All figures are the analyst's own, taken from the research extracts. "n/e" means no explicit assumption in the note. I have not cross-checked these figures against the original documents.

| Analyst, date | (a) 6000 revenue | (b) Clinical consumables growth 2026 / 2027 / 2028 | (c) $/Gb, price | (d) Gb growth | (e) 35B | (f) Gross margin 26E / 27E / 28E |
|---|---|---|---|---|---|---|
| JPM, Jun-10 (upgrade) | n/e | FY26 guide mid-teens; ROW clinical "+low/mid-teens CAGR 2026–30E"; China clinical −LDD | Survey gap +2.4 to +5.2 pts; reagent rental "only LSD% of boxes" | n/e (survey volume +14.6%/+19.1% clinical) | n/e | 68.3 / 68.8 / 69.0 |
| JPM, Jul-31 (2Q26) | n/e | FY26 mid-teens (raised) → "path to +HSD in 2027" | n/e; "pricing pressure from competition" listed as a risk | n/e | n/e | 68.3 / 68.8 / 69.1 |
| JPM, Mar-3 (Roche alert) | n/e | n/e | "pressured pricing dynamics leave us on the sideline" (Neutral then) | n/e | n/e | 68.6 / 69.0 / 69.2 |
| Barclays, Feb-5 | n/e | Clinical ~20% in 4Q25; guide low-DD to mid-teens | "another round of pricing headwinds in 2027 and beyond" | n/e | n/e | 2027E 71.2% / 2028E 71.9% (anomalous) |
| Barclays, Apr-30 | n/e | n/e | X revenue share flat at 55%, read as "lower price/Gb on NSX volumes", "warrants watching" | n/e | n/e | n/e |
| Barclays, Jul-31 | n/e | "60% of the business grows more than 20%" (bull math, not Barclays' view); Barclays says "a MSD business" | Competition requires "continued price concessions, bundling, and favorable terms" | n/e | "would need to be priced to compete"; "inherent technological barriers" may prevent | 68.4 / 67.8 / 67.9 |
| UBS, Feb-5 | n/e | FY26 mid-teens guide; "increased 2027-and-beyond outlook" | Risk list: pricing could fall faster than expected | n/e | n/e | 68.4 / 68.7 / 68.9 |
| UBS, Mar-3 (First Read) | n/e | n/e | Roche $0.06 vs Illumina $0.68 per M reads; counting ~16% of seq. consumables | n/e | Roadmap gives "a path to about $150 per genome", "assumes" 35B priced "consistently with" 25B | n/e |
| Freedom, May-6 | n/e | Consumables FY26 +4.7%, '27 +5.2%, '28 +4.6% (3,381/3,556/3,721) | "Completion... should help offset pricing erosion" | n/e | n/e | n/e |
| Freedom, Aug-5 | n/e | Consumables $3,386M (+4.9%), $3,591M (+6.1%), $3,788M (+5.5%) | same as May | n/e | n/e | 67.6 / 68.0 / 68.5 (calc from GP ÷ revenue) |

Other points on the table:

- **Revenue growth, 2027E:** UBS +4.1% (stale; Feb), Barclays +5.5%, Freedom +5.7%, JPM +9.1%, FactSet ~+5.8% (E102). Management's own range, "HSD" ROW, is roughly 7–9% before China drag. JPM's 9.1% reported sits at the top. The others are below the target.
- **Consensus EPS:** FY27 consensus is about $5.92–5.93 and FY28 $6.81. Barclays ($5.73) is below it and JPM ($6.16, $7.41) is above. A 0.3x multiple shift on the $0.43 gap does not matter here, but the spread is a measure of disagreement about the post-2026 tail. JPM's FY28E EPS is 9% above consensus.
- **UBS is stale.** The only UBS items in the corpus are dated Feb–Mar. They use FY26E revenue of $4,535M against a current guide of $4.60–4.64B, a gap of about $75M (1.6%). There is no UBS post-Q2 model.
- **Freedom's May Q&A inconsistency:** Freedom says its consumables rows "match the 'Previous' revenue estimates." It did not update consumables despite "strong" placements. Consumables moved only +0.1% (FY26), +1.0% (FY27) and +1.8% (FY28) between May and Aug. That is a cautious revision of the line the thesis depends on.

## 2. Implied inconsistencies with the 83%/59% share math

Rule of thumb from the Q2 mix: the X sits at about 0.71 and the 6000 at about 2.41 on a "revenue-share per volume-share" basis (that is, 3.4x). If the X volume share rises to 85% with the same relative prices, X revenue share would be about 62.5%. At 84% it is 60.7%. At 86% it is 64.4%. These are my calculations. A model with HT or sequencing consumables growing at a steady mid-single digit while volume converts is only consistent if the Gb growth is well above 30% or the X per-Gb price is flat.

- **JPM (FY27 +9.1%, FY28 +12%):** this needs Gb growth of 32% or more if price falls at management's 15%, or a price decline of about 5% (the survey figure). The second is what JPM's survey says, but that is stated intention, not realized pricing (E067 correction). JPM does not reconcile its view with management's own model.
- **Freedom ("transition completes, offsets price erosion"):** the mechanism is reversed. The remaining 17% of volume is high-price volume. Its conversion raises the erosion unless it is already priced in elsewhere.
- **Barclays:** not inconsistent with the share math. It is the only model with GM falling in 2027, which is what the tail would imply. Barclays' Q1 "price/Gb is falling on NSX" read was not repeated in Q2, when X revenue share went from 55% to 59% on a 1-point volume increase (E066).
- **UBS:** stale and not testable.
- **All four houses:** none models the 35B cut. UBS's roadmap point is arithmetically odd. A 35B has about 40% more reads than a 25B. At the same price per read, $/genome would not fall at all. For $200 → $150 per genome, $/Gb must fall about 25%. The user's ~20% figure would give $160 (calc).

## 3. Management word-choice diff

All quotes are short and can be matched to the files cited. "Softened" means a move away from admitting a pricing headwind. "Hardened" means a more specific commitment.

| Term | Earlier | Later | Direction |
|---|---|---|---|
| Price headwind | "definitely still some pricing headwind"; "shouldn't be worse than '25" (TD Cowen, 2026-03-03) | "the price headwind is receding" (Q1'26 call, Guggenheim answer); research ">90%" moved so comparisons improve (Q1'26 call) | Softened. "Not worse than '25" was never quantified |
| Price / transition in guide | "no change in pricing-transition assumptions... price effects are already in the guide" (Dhingra, Q1'26) | Q2'26 call: no explicit statement. 6000 answer is "not a true headwind" (Thaysen) | Softened to silence |
| Elasticity | "elasticity dynamics... clearly taking hold" (JPM Jan); "aggressive pricing brings aggressive volume growth" (Q1'26) | Counting apps: "you might be able to do 20% more" (TD Cowen, Mar); word absent from Q2 extract | Contradicts itself by segment |
| Laggards / tail | "laggards" with FDA assays; "leaving a long tail" after end-2026 (Q1'26 Brennan answer) | "standard part of the business"; HiSeq "in the portfolio only a few quarters ago" (Q2'26) | Softened. The HiSeq analogy supports a very long tail |
| "Cliff" | Not used by management on the 6000 | Analyst-framed "clinical cliff" in demand; answer "it's not a cliff. It's a wave" (Q2'26) | Correction to E016 |
| 35B pricing | "we are not ready at this point to go out and talk about pricing" (Q1'26, Stifel) | "We don't see any value in coming out too early with pricing" (TD Cowen, on a different product) | Consistent dodge; same pattern as E158 |
| Volume discounts | "Customers ordering 5, 10 or more get a volume discount, which... is reasonable" (Q1'26, BofA answer) | "continues to offer volume discounts on NovaSeq X instruments" (Q2'26, per JPM) | Unchanged. Quantity never given |
| Reagent rental | "some of the roughly 83 units were placed under reagent-rental or lease models" (Dhingra, Q1'26) | Not on Q2 call. JPM: "only LSD% of boxes today" (Jun) | Hardened for JPM, unspecified for Illumina. No Q2 update |
| Clinical X target | "over 85%" (Thaysen, Q1) vs "over 80% to 85%" (Dhingra, Q1) | "80% to 85%" (Q2) | Already in E011 |
| Multi-year / commitments | Not stated in any call extract (grep of Q1, Q2, TD Cowen, JPM Jan) | 10-Q: RPO $1.0B, 83% in 12 months (E159, E198) | Never disclosed. Gap for an "over-earning" claim |
| Memory / freight cost | "sharing some of the increase with customers" (Q2'26, Thaysen) | n/a | New: a price increase on customers, which cuts against the "price falls" story. Not in E-numbers I could match |

New point on that last row: Thaysen said Illumina is "sharing some of the increase with customers" when asked about memory and freight costs (Q2'26 call, Guggenheim answer). That is either a price rise or a surcharge on consumables or instruments. It was not sized and was not repeated in the guidance Q&A.

## 4. Q3'26 earnings checklist

Call date: ledger E176 says 29 Oct 2026 after the close (unverified). E176 also cautions that the consensus revenue (~$1.15B) is unconfirmed. The EPS range is $1.36–1.41 (E176 correction).

The thresholds below combine reported figures and my calculations. They are OPINION where marked and are not management guidance.

| Metric | Last | Reassuring (no unwind) | Neutral | Warning |
|---|---|---|---|---|
| X share of HT volume | 83% (Q2) | ≥ 84.5% | 83.5–84.5% | ≤ 83%, or not disclosed |
| X share of HT revenue | 59% | ≥ 61% with volume ≥ 84% (matches the 3.4x gap; calc) | 59–61% | ≤ 59%: price/Gb erosion on the X (Barclays Q1 type), or not disclosed |
| Clinical X volume share | 78% (+2 pts in Q2) | ≥ 80% | 79–80% | ≤ 78%: the 80–85% year-end target needs +2 to +7 pts in two quarters |
| 6000 pull-through ($ per active instrument) | FY25 ~$670K; FY26 guide $600–650K | Within or above guide (≈ $150–163K per quarter) | Slightly below | Not disclosed, or a sharp drop |
| Ex-China clinical consumables growth | +20% Q1, +15% Q2 | ≥ 15% | 12–15% | < 12% (below the guide's lower, low-double-digit bound) |
| Non-GAAP gross margin | 68.2% (Q2); 68.2% (Q1) | ≥ 68.5% (JPM models 68.6%) | 67.8–68.5% | < 67.7% (Freedom's Q3 number is 67.7%) |
| Sequencing consumables | $775M (Q2) | ≥ $789M (E050 Q3'26E; +5.6% y/y vs $747M) | $780–789M | < $780M |
| Reporting changes | Cohort data dropped (E027) | Share data restated or expanded | Same format | Share table or "elasticity" data dropped |

- **Volume math for the clinical target:** the average of the share thresholds assumes clinical X volume share moves in line with the target (80–85%). From Q2 (78%) to the 80% low end is about +1 point per quarter. Q1 → Q2 added only +2 (E010 correction). A Q3 print of 79% or lower means the "good" case needs a steeper Q4.
- **The key read is the relationship between X volume and revenue.**
  - If volume share rises (more 6000 → X conversion) but revenue share rises faster than in the table, the 6000 base is carrying higher revenue per Gb. That is the over-earning pattern.
  - If revenue share lags volume share (Q1'26 pattern), the X price per Gb is falling. That would be consistent with the 35B, discounts or reagent rental.
- **Placements:** Q3 placements are guided to step down q/q and rebound in Q4 (JPM, 2026-07-31). Below 80 is not a thesis signal. A fall below ~60 would be.
- **Guidance language:** watch for "headwind" or "tail" returning, a quantified 35B price, any new 6000 shipment count (">10" in Q2), and any change to the 80–85% target.
- **Insider and compensation items** are in the ledger (insider sales by Keith Meister in Aug–Sep are in the insider_data extracts). I did not re-check them.

## Contradictions and stale data

- **E016 vs Q2 call (above):** "cliff/wave" was about demand durability, not the 6000.
- **JPM cover vs body:** the Aug JPM note cites a 9.8% WACC, with 8.9% in July and 9.1% in June. The $230 target and the DCF are not comparable with prior ones.
- **Barclays GM:** 71.2%/71.9% (Feb) vs 67.8%/67.9% (Aug); FY25A is 68.5% vs 68.2% elsewhere. Barclays' Feb model also shows 0.0 for several 2026E margin lines (a data gap).
- **Freedom:** gross-margin text vs model (above); the May table's consumables rows match "Previous" estimates; prior-close $198.16 vs $203.01 on the key-data panel.
- **UBS:** FY26E revenue $4,535M is stale against the $4.60–4.64B guide. No UBS note exists in the corpus after 4 Mar.
- **JPM Q2 recap:** gross margin "in line" at 68.2% while down 120bp y/y. This is not a conflict. It is worth knowing when comparing "beat" language across notes.
- **JPM Q2 recap, FCF:** $162M vs Street $321M. This is already in the ledger (line 165), so I did not expand on it.

## Gaps / what I could not find

- No sell-side notes in the corpus for Evercore, Bernstein, Wolfe, TD Cowen, Guggenheim, RBC, Deutsche, Canaccord or Jefferies with model assumptions. Only price targets appear (E172), plus questions in the calls.
- No consensus sheet gives a $/Gb path, a 6000 revenue line or a clinical consumables growth path. The BI note's model grid is illegible (BI extract, 2026-07-31) and its only readable numbers are operating margins (2026 ~23.7%, 2027 ~25–26%).
- No ILMN conference transcripts exist in the corpus between 3 Mar 2026 and the Q2 call (30 Jul). The Jun–Sep 2026 conference part of the word-diff therefore uses only the JPM Jan, TD Cowen Mar and the two calls. The Roche H1 call and the Sept CEO/Barclays items in E123 are about Roche, not Illumina. I found no Illumina statements after 30 Jul.
- The Q1 and Q2 call quotes come from the extracts and, for the "cliff" check, the source file. The other quotes were not verified against the sources.
- The Q3 thresholds are my construction from the corpus and do not come from any company or analyst source. The 3.4x-ratio revenue-share table assumes unchanged relative pricing, which is exactly what is in question.
