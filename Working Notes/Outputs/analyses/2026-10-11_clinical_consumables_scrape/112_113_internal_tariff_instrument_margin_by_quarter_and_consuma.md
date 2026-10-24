# Agent 112: 113-internal-tariff-instrument-margin-by-quarter-and-consumables-margin-bridge-plus-Q3-26-

*Model: sonnet. Run 2026-10-11 10:39:38. Cost $0.63 (API-equivalent).*

**Assignment:** Close open gaps 3 and 6 using only the local corpus. Read INDEX.md first, then the ILMN Q1'25 to Q2'26 earnings-call Extracts and Sources (open the originals for exact numbers), 10-Q MD&A extracts, and the sell-side notes. (a) Extract, per quarter from Q1'25 to Q2'26: reported tariff cost in dollars or basis points, total gross margin (GAAP and non-GAAP), instrument revenue, any stated instrument gross margin, service and other margin, and the consumables margin if given or implied. Reconstruct the implied consumables gross margin each quarter, with and without the tariff adjustment, and show your arithmetic and the error range. (b) Find every explanation given for the 120 bp y/y gross margin decline in Q2'26 and flag whether a bridge was supplied. Find the inventory reserve ratio (reserves/inventory) by quarter and any statement about excess and obsolete (E&O) provisions for NovaSeq 6000 stock during the migration. (c) Search for the phrases 'reduced pricing', 'as customers transition to NovaSeq X', 'price', 'mix' in the guidance language, and tabulate when each phrase appeared or disappeared across the calls. (d) Output a prioritized list of 10 sharp, specific questions for the Q3'26 call, each tied to the evidence and a number. Cite file and date for each point. Stop at about 20 minutes.

## Key findings

Nothing in this wave changes the ledger's core thesis. It does correct E036 and E037, quantifies the 120 bp decline for the first time, and adds a reserve-ratio series.

1. **E036 is partly wrong; the negative clause is what disappeared.**
   - FACT: The FY25 10-K still says "Core Illumina consumables revenue increased in 2025 primarily due to demand for high-throughput consumables as customers continue to transition to NovaSeq X" [ILMN_10-K_FY2025, Extracts/ILMN/filing, lines 24 and 403].
   - FACT: The Q3'25 10-Q says "driven by demand for high-throughput consumables as customers transition to the NovaSeq X platform" [10-Q Q3'25, line 25].
   - FACT: The Q2'25 10-Q uses similar positive wording [10-Q Q2'25, line 17].
   - What is gone is the offsetting clause. The FY24 10-K said "decreases in consumables across our other high-throughput instruments, as customers transition to NovaSeq X". The 2023 10-Qs said "lower pull-through of NovaSeq 6000 consumables".
   - OPINION: The 10-Qs reframed the transition from a drag to a driver. The Q2'26 and Q1'26 10-Q extracts show no transition wording in the consumables paragraph, but both have omitted long lines I could not check.

2. **The 120 bp decline is the non-GAAP figure; GAAP gross margin rose.** The Q2'26 10-Q reports GAAP gross margin of 66.4% vs 65.6% (+80 bp) [10-Q Q2'26, lines 59-61].
   - The 10-Q says the rise is "primarily attributable to a $23 million intangible asset impairment charge recorded in Q2 2025".
   - The 10-Q says "Excluding that one-time item, gross margin declined".
   - OPINION (calc): $23M ÷ ~$1,058M Q2'25 revenue is about 217 bp. Q2'25 GAAP excluding the impairment is about 67.8%, so the underlying GAAP decline is about 140 bp.

3. **Management gave no bp bridge for the 120 bp (confirms F108).** The explanations in the corpus are:
   - **Call:** "slightly better than expectations despite instrument-heavy mix and higher freight and memory costs" [Q2'26 call, 2026-07-30, line 29]; "memory cost is already in Q2 results… the bulk is in gross margin and Q2 is a starting run rate" [line 155].
   - **10-Q, as drivers:** tariffs, mix toward lower-margin instruments, SomaLogic, memory, and freight/energy.
   - **10-Q, as offsets:** lower field-service and warranty costs.
   - **10-Q, on tariffs:** Q2'26 tariff costs were "lower than the prior quarter" with no dollar figure.

4. **My bridge of the 120 bp: instrument mix explains about half, and the remainder is unattributed.** All of this is OPINION (calc), with the arithmetic below.
   - **Instrument share:** Q2'26 instruments were $125M (+31%) on $1,159M of revenue [Q2'26 call, lines 21-26]. That is 10.8%. Q2'25 was 125/1.31 = $95M on 1,159/1.095 = $1,058M, or 9.0%. The shift is +1.8 pts.
   - **Instrument margin:** At an assumed 40% instrument margin, the rest of the business earned about 72.6% in Q2'25 (69.4 = 0.09×40 + 0.91×r).
   - **Mix effect:** 1.8 pts × (72.6 − 40) ≈ **−59 bp**.
   - **Tariffs:** Q2'25 had about 110 bp, and Q2'26 was "lower" than Q1'26. Tariff cost dollars are not disclosed, so the y/y tariff effect is unknown. Anywhere from a modest tailwind to about −100 bp is plausible.
   - **Remainder:** About −60 bp is left after mix. It is spread across SomaLogic, memory, freight and tariffs, net of the field-service and warranty offsets. The 6000-to-X price effect cannot be separated from these.
   - **Error range:** An instrument margin of 30–50% moves the mix effect to −75 bp (30%) or −43 bp (50%). The ±0.1 pt rounding on the margins is small by comparison.

5. **Inventory reserve ratio by quarter is new.** The reserve fell from 19.1% to 15.8% while the X share of HT revenue went from 55% to 59%. Reserve ÷ gross inventory:

| Period | Reserve | Gross inventory | Ratio | Source |
|---|---|---|---|---|
| Dec 2024 | $113M | $660M | 17.1% | 10-Q Q1'25 line 162 |
| Mar 2025 | $109M | $646M | 16.9% | same |
| Jun 2025 | $118M | 227+419+47 = $693M | 17.0% | 10-Q Q2'25 line 262 |
| Sep 2025 | ~$129M (derived) | 251+418+50 = $719M | ~17.9% | 10-Q Q3'25 lines 127-130, net $590M |
| Dec 2025 | $133M | $697M | 19.1% | 10-K FY25 lines 874-880 |
| Mar 2026 | $119M | $750M | 15.9% | 10-Q Q1'26 line 119 |
| Jun 2026 | $123M | 295+426+57 = $778M | 15.8% | 10-Q Q2'26 lines 540-544 |

   - FACT/calc: The ratio peaked at the end of 2025, then dropped about 3.2 pts in one quarter. The reserve fell $14M in Q1'26 while gross inventory rose $53M.
   - FACT: The Q1'26 10-Q extract gives no explanation for that drop.
   - FACT: The Q2'26 10-Q says only that the reserve decreased "$10 million, reflecting management's periodic assessment of excess and obsolete inventory" [line 548].
   - FACT: The Q3'25 10-Q cites an "increase in inventory reserves" as a gross-margin headwind.
   - OPINION: A $14M reserve release or write-off in Q1'26 could have helped that quarter's gross margin by about 20 bp on $1,159M of revenue. That is unquantified, because a write-off uses the reserve without a P&L charge.
   - FACT: No statement in the corpus ties E&O provisions specifically to NovaSeq 6000 stock. The FY25 10-K lists "product transitions (customer migration to NovaSeq X)" as one of four reserve drivers [10-K FY25 line 888].

6. **The Q2'26 10-Q mislabels the inventory increase (extends E037).**
   - The 10-Q says "$91 million increase in gross inventory (+13%)". That is the net change (655 − 564).
   - Gross inventory was $697M → $778M, which is +$81M (+11.6%).
   - The 10-Q attributes the build to SomaLogic, higher production for X demand, and memory and raw-material input costs. No 6000 line is mentioned.
   - This sits alongside F106's like-for-like figures in the ledger correction to E037, and I did not re-derive those.

7. **Tariff dollars by quarter are still not disclosed for Q1'26 or Q2'26. I found only reconstructions.**

| Quarter | Reported tariff cost |
|---|---|
| Q1'25 | $85M gross for FY25 guided; $15M direct cost in guide [Q1'25 call, 2025-05-08, lines 102 and 117]. Q1'25 itself had none, since tariffs started in April 2025. |
| Q2'25 | ~110 bp net |
| Q3'25 | ~220 bp |
| Q4'25 | 205 bp |
| Q1'26 | Not disclosed |
| Q2'26 | Not disclosed |

   - **2025 total:** OPINION (calc): ~$12M + $24M + $24M ≈ $60M for 2025, which is below the $85M gross guide. The gap is plausibly mitigation, and F108 reached the same number.
   - **Q1'26 gross margin:** The call said "partly offset by tariffs" [Q1'26 call, line 41]. The Q1'26 10-Q says "higher tariff costs" y/y and "no quantification" [10-Q Q1'26 lines 15 and 47].
   - **Q1'26 ex-tariff margin:** Q1'25 had no tariffs, so a Q1'26 gross margin up 80 bp despite tariffs implies an ex-tariff improvement of well over 80 bp. If tariffs ran ~150–200 bp, that is about +230–280 bp (OPINION, calc).

8. **The tariff-adjusted consumables margin cannot be extended to Q1'26 and Q2'26 with confidence.** Taking F108's central case of 75.0% for Q2'26 at 40% instrument margin:
   - Adding back tariffs of 100–200 bp (an assumption) raises product gross margin by 1.2–2.3 pts (bp × 1,159 ÷ 982 product revenue).
   - Dividing by the 0.869 consumables weight (O(calc)) lifts the implied consumables margin by about 1.4–2.7 pts, to about 76.4–77.7%.
   - That is the same band F108 gave for $15–24M of tariff cost.
   - It sits in the same band as Q3'25 (78.4%) and Q4'25 (76.8%) within error. The error range is ±2 pts, mostly from the instrument margin and the tariff assumption.
   - No visible erosion is evident even with the mix-driven decline.

9. **Guidance-language tabulation for price and the transition is thin; the extracts are paraphrased, so exact wording needs the transcripts.**

| Call | Language found |
|---|---|
| Q1'25 (2025-05-08) | "Pricing actions tied to tariff mitigation: about 1 point contribution" to growth [line 190]. This is price used as an offset to cost, not a transition headwind. |
| Q2'25 | Analysts quote the framework: "volume growth of 20% to 30%, price declines in the mid-teens" [lines 163 and 168]. |
| Q3'25 | "Growing volumes are 'more than offsetting transitional pricing effects'" [line 71]. Pricing headwinds easing "now that 91% of high-throughput volume is on the X" [line 61]. This is the high point of explicit price language. |
| Q4'25 | Research consumables flat "because of funding uncertainty and year-over-year pricing effects from converting customers to the X" [line 45]. |
| Q1'26 | Dhingra: "no change in pricing-transition assumptions… price effects are already in the guide" [line 130]. He gave no number. |
| Q2'26 | The extract line is the summarizer's paraphrase: "Despite transition dynamics (customers move from older, higher-priced-per-unit platforms to a cheaper-per-base one)" [line 105]. I found no management quote with "price" or "pricing" tied to the transition. |

   - OPINION: The language moved from "transitional pricing effects" (Q3'25) to "price effects already in the guide" (Q1'26). The Q2'26 extract's own paraphrase is not management language. Per Q3'25, the research price drag has run its course. In clinical, the drag is still ahead.
   - Reduced pricing as a gross-margin driver (Q1'25 10-Q) remains a single appearance, as F108 found.

10. **The margin step-up guidance has changed shape.**
    - Dhingra said the Q2→Q3 operating margin step is about 100 bp excluding the 60 bp deferred-compensation effect [Q2'26 call, line 181].
    - "Part comes from higher consumables mix, and part from several cost actions in gross margin during Q3, with more in Q4."
    - No Q3 consumables-versus-instrument split was given.
    - OPINION: Q3 gross margin is the first test of the claim that most cost actions land in gross margin.

## Contradictions and stale data

- **E036** says the "as customers transition to NovaSeq X" phrase is gone from the FY25 10-K and Q3'25–Q2'26 10-Qs. The FY25 10-K and Q3'25 10-Q both still contain it, in positive framing (findings 1 and 9). What dropped is the negative clause.
- **The 10-Q's "$91M gross inventory increase" is the net change.** Gross inventory rose $81M (finding 6).
- **"120 bp decline" is non-GAAP.** GAAP gross margin was up 80 bp y/y because of the Q2'25 impairment (finding 2).
- **The Q4'25 inventory reserve was a one-quarter peak.** It fell in Q1'26 with no explanation (finding 5). E037 shows only the endpoints.

## Gaps / what I could not find

- Q1'26 and Q2'26 tariff dollars or bp, in any call, deck, 10-Q or sell-side note I opened.
- Instrument gross margin and consumables-only gross margin by quarter. Both stay assumption-based.
- The explanation for the Q1'26 reserve drop.
- Any 6000-specific E&O statement.
- I did not open the sell-side notes in this wave, nor the original transcripts, so phrase presence or absence rests on extracts only. The original Q1'26 and Q2'26 10-Q MD&A lines marked "omitted long line" are unchecked.

## Ten questions for the Q3'26 call, in priority order

Each is tied to evidence above.

1. **Q2'26 gross margin bridge.** "Non-GAAP gross margin fell 120 bp y/y to 68.2%. Please give the bp contribution of instrument mix, SomaLogic, memory, freight, tariffs and cost actions." Mix alone is about −60 bp on my estimate [Q2'26 call line 29; 10-Q Q2'26 lines 59-73].
2. **Tariff dollars.** "Tariffs were 110, 220 and 205 bp in Q2–Q4'25, then you stopped quantifying. What were they in Q1'26 and Q2'26, and what is the IEEPA refund potential?" [Q3'25 call line 141; Q4'25 call line 29; 10-Q Q2'26 line 65].
3. **Reserve ratio.** "The inventory reserve fell from 19.1% to 15.8% of gross inventory in six months (reserve $133M → $123M) while gross inventory rose $81M. What was released or written off in Q1'26, and what P&L benefit resulted?" [10-K FY25 lines 874-880; 10-Q Q1'26 line 119; 10-Q Q2'26 lines 540-548].
4. **6000 stock.** "How much NovaSeq 6000 instrument, flow-cell and reagent inventory do you hold, and what reserve covers the 6000 as clinical goes to 80–85% X by year-end?" [10-K FY25 line 888, which lists the NovaSeq X migration as a reserve driver].
5. **Consumables margin.** "You say X consumables margins are 'comparable at scale' to the 6000. Is that true today, and what is the consumables-only gross margin in Q2'26?" The implied value is about 75% (raw) or 76–78% (tariff-adjusted).
6. **Instrument margin.** "You said instrument gross margin improvement is a lever but not yet in the P&L. What was the instrument gross margin in Q2'26 against Q2'25?" Instruments were $125M, +31% [Q3'25 call line 187].
7. **Q3 mix.** "Q3 margin guide steps up ~100 bp ex deferred compensation. What are the assumed consumables-versus-instrument revenue shares, and how many bp are cost actions versus mix?" [Q2'26 call line 181].
8. **Price language.** "In Q3'25 you cited 'transitional pricing effects'. In Q1'26 you said price effects are 'already in the guide'. What is the price decline per Gb assumed in the 2H26 clinical guide, including the January 35B cut?" [Q3'25 call line 71; Q1'26 call line 130].
9. **Disclosure.** "The 10-Q has dropped the sentence that other high-throughput consumables decrease as customers transition to NovaSeq X. Is the 6000 consumables decline now immaterial, and what were 6000 consumables in Q2'26?" The ledger's calc is about $219M (E003) [FY24 10-K; FY25 10-K lines 24 and 403].
10. **Non-GAAP presentation.** "You cited ~23% operating margin excluding 60 bp of deferred compensation. Will you report the effect in a reconciliation each quarter, and will you also quantify tariffs, memory and freight in gross margin?" [Q2'26 call lines 30-31].
