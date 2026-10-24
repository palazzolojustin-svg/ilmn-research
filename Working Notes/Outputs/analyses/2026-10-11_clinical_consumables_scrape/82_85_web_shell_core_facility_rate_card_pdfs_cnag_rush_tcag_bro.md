# Agent 82: 85-web-shell-core-facility-rate-card-PDFs-CNAG-Rush-TCAG-Broad-same-date-X-vs-6000-per-Gb

*Model: sonnet. Run 2026-10-11 10:03:22. Cost $1.13 (API-equivalent).*

**Assignment:** Close open gaps 1 and 2 on price per Gb. FIRST confirm you have a working shell. Download PDFs to disk with curl.exe and extract text with pdftotext -layout (or python pypdf or pdfplumber if pdftotext is missing). Do not rely on WebFetch summaries. Priority list: (a) CNAG-CRG 2026 price list. The saved tool-result files may exist in the tool-results folder (webfetch-1791730498978-fvhkrd.pdf and webfetch-1791730509549-7c1j98.pdf). If not, search for the CNAG service rates page. Extract the NovaSeq 6000 S4 / S2 / SP price and the NovaSeq X 10B / 25B price on the same date, and compute the percentage change per Gb using the stated Gb per lane or flow cell. Check the earlier claim of -63% (E291). (b) Rush University Genomics Core June 2026 card: get the lane count of the whole-run S4 at $6,615 versus the 25B lane at $4,200, and compute $/Gb for both. (c) TCAG (SickKids) April 2025 and current S4 and X prices. (d) Broad Genomics Platform, Stanford SGTC, Baylor GAC, HudsonAlpha, Garvan, Univ. of Michigan Advanced Genomics Core, Vanderbilt VANTAGE, NYU Genome Technology Center, UC Davis, UCSF IGI, Duke GCB, and Univ. of Minnesota UMGC. Find any card that lists both platforms. (e) Reagent list or catalog prices for NovaSeq X 1.5B/10B/25B kits versus NovaSeq 6000 S1/S2/S4 kits from Fisher, VWR, Cytiva, Illumina store, or GSA/NIH CIT price pages. Record the date of each. (f) Challenger $/Gb for the same period: Element AVITI24 and AVITI kits, Ultima UG100 and UG200 reagents, MGI T20 and T7+ tender prices, and Roche AXELIOS $0.06/M reads. For each datapoint record: institution, URL, card date, platform, flow cell, Gb or reads per unit, price, internal versus external rate, and computed $/Gb. Build one table of the same-date pairs and the implied X-versus-6000 price per Gb decline. Say how it compares with management's 'easily more than 60% to 70%'. Also note within-X steps (10B to 25B at -25% to -32% per Gb) and any sign of how the 35B or 5B flow cells or HT mode will be priced. Stop after about 20 minutes and return what you have.

Status: no shell was available, but the Read tool opens WebFetch-saved PDFs directly, so I read the CNAG, Rush, TCAG, EPFL and Northwestern rate cards in full. I'm now writing up the findings.

## Key findings

1. **The CNAG −63% (E291) is arithmetically correct but cherry-picked.** It compares the S4 2x100 line with the X 25B 2x100 line. The standard 2x150 pair, which is the clinical-like configuration, gives only **−42%**. This is FACT, from the full text of both PDFs. [CNAG 2026_R1 (valid Aug 2026) and 2026_R0 (valid Jan 2026), https://www.cnag.eu/sites/default/files/CNAG%20PRICES%202026_R1.pdf]
   - 2x150 public-tier price per Gb: S4 €4.90 against 25B €2.84, a −42.0% change.
   - 2x100 public-tier price per Gb: S4 €10.07 against 25B €3.77, a −62.6% change.
   - The S4 2x100 price is 2.05x the S4 2x150 price per Gb, while on the X the ratio is only 1.33x (the cycle-count ratio). So the 2x100 S4 line is unusually expensive and the −63% overstates the gap.
   - The percentages are identical across the public, international and private tiers.
2. **Core cards show a smaller decline than management's "more than 60% to 70%".** Same-date 25B-versus-S4 pairs at list level give −34% to −49% on 2x150. Only the 2x100 or smaller-flow-cell comparisons reach −60% or more (table below). OPINION: cores add a fixed labor and overhead cost to reagent cost, so the decline in Illumina's own reagent price is probably steeper than the decline on a core card. Illustration only: with €1/Gb of overhead, reagent cost falls from €3.90 to €1.84, which is −53%. The cards therefore bracket the claim without confirming it.
3. **CNAG raised 6000 prices about 4% between January and August 2026 and left X prices flat.** This is FACT, from the same two PDFs.
   - S4 2x100 went from €9.67 to €10.07 (+4.1%).
   - S2 2x100 went from €16.59 to €17.25 (+4.0%).
   - S2 2x150 went from €11.76 to €12.22 (+3.9%).
   - S1 2x150 went from €16.77 to €17.43 (+3.9%).
   - SP 2x150 went from €21.29 to €22.07 (+3.7%).
   - S4 2x150 stayed at €4.90.
   - All X lines (1.5B, 10B and 25B) were unchanged.
   - This is consistent with E033 (list increases on the 6000 tail) and with 6000 pricing power. It is one core, and it could be the core passing through a cost change.
4. **The within-X step from 10B to 25B is steeper at CNAG than the −25% to −32% in open gap 8 (CNAG R1).**
   - 2x150: €4.36 to €2.84, which is −34.9%.
   - 2x100: €6.03 to €3.77, which is −37.5%.
   - 2x50: €9.35 to €6.00, which is −35.8%.
   - 1.5B to 10B on 2x150: €7.33 to €4.36, which is −40.5%.
   - The 25B-to-10B gap is large enough that the 25B share of X Gb sets the average price. The ledger's range of −25% to −32% therefore understates the CNAG step.
5. **The new 5B flow cell has a published price (CNAG R1, Aug 2026), which the ledger only knew from CWRU.** The 5B is not a disguised cheap tier: it sits between the 1.5B and 10B in price per Gb. The CNAG 5B price is not a predictor of 35B pricing.
   - 5B 2x150 is €5.62 per Gb. That is −23% against the 1.5B (€7.33) and +29% against the 10B (€4.36).
   - 5B to 25B on 2x150 is −49.5%.
   - Fast-track on the 25B costs €4.09 per Gb against €2.84, a 44% premium.
6. **Rush: the unit for the $6,615 S4 price is not stated on the card.** Open gap 2 calls it a "whole-run S4", but the card says only "Illumina NovaSeq S4 2x150". This is FACT. [Rush GMCF fee schedule, 2026-06-15, https://www.rushu.rush.edu/sites/default/files/2026-06/GMCF%20Pricing%20June%202026.pdf]
   - The X 25B lane is $4,200 for 930 Gb ($4.52 per Gb), which matches E259.
   - If the S4 price is per lane at about 750 Gb, it is $8.82 per Gb, so the X is −48.8%. At 800 Gb it is $8.27 per Gb, or −45%.
   - A whole-flow-cell reading would put the S4 at about $2.2 per Gb (3,000 Gb), below the X. That is implausible against Rush's own SP 2x150 price of $2,499.
   - Calgary's S4 lane price of $5,820 (from the search results, not opened) supports the per-lane reading. OPINION: the S4 price is a lane price.
   - Rush's external uplift is about 5% on S4 ($6,945.75) and 10% on X ($4,620).
7. **New card, Northwestern NUSeq FY26: it lists no NovaSeq 6000 at all, only X, MiSeq, DNBSEQ, AVITI and long read.** This is FACT. [NUSeq FY26 Approved Rate, https://www.cgm.northwestern.edu/docs/nuseq/fy26-prices_finalusers.pdf; the card has no date, only "FY26", and the saved PDF is at `...\90146ecd-fcb5-4e64-b650-58fb7e43a628\tool-results\webfetch-1791730914843-ir0yqt.pdf`]
   - 25B PE150 lane: $3,000 internal, $3,750 external, $3,817 industrial.
   - At the nominal 930 Gb that is $3.23 per Gb. The card's guaranteed 2,000–2,500M read pairs gives $4.00–5.00 per Gb.
   - 10B PE150 lane: $1,600, which is $4.27 per Gb at 375 Gb, so 25B is −24% against 10B on the nominal basis.
   - Cross-check: the GSA 25B-300 kit at $24,155 (E054 correction) divides by 8 lanes to $3,019 per lane. The NU internal rate of $3,000 is therefore at or below distributor kit cost, so core prices carry no margin at this size.
8. **EPFL shows 6000 prices being cut at a core that has no X on its card (GECF, 9 Sep 2026).** This is FACT. [https://www.epfl.ch/research/facilities/gene-expression-core-facility/wp-content/uploads/2026/09/GECF-price-list-for-EPFL-users-09-September-2026.pdf]
   - "NovaSeq 6000, 10'000 mio" is CHF 8,240 (200 cycles) and CHF 10,330 (300 cycles).
   - The change log says "Price decrease of NovaSeq" (Nov 2024–Jul 2025), "Strong decrease in NovaSeq prices" (Sep–Nov 2025) and "Strong decrease of NovaSeq 10'000mio 300 cycles runs" (15 Mar 2026).
   - If "10'000 mio" means a whole S4 flow cell of 10B clusters, about 3,000 Gb, then CHF 10,330 is about CHF 3.4 per Gb. That is the lower bound; I could not confirm the unit.
   - This cuts against the idea that 6000 prices are frozen high. It is likely a core with its own volume pressure rather than Illumina list pricing.
9. **Challenger pricing at cores is higher per Gb than the X.** This is FACT, from the NU card, using the card's own read counts.
   - AVITI PE150 High-Output lane at $1,300 for 400M read pairs (120 Gb) is about $10.8 per Gb.
   - AVITI Ultra Q at $3,500 for 600M pairs is about $19 per Gb.
   - DNBSEQ FCL PE150 at $3,600 for 1,500M pairs is about $8 per Gb.
   - The 25B is at $3.2–5.0 per Gb, so AVITI is roughly 2–3x the X at NU.
   - EPFL's AVITI24 300-cycle price for 1,200M reads is CHF 2,200 against about CHF 1.03 per M reads on its 6000. That is roughly 1.8x per read, but the read definitions differ.
   - This conflicts with UMN's claim (19 Dec 2024) that AVITI "is less expensive than the Illumina NovaSeq X Plus 25B". UMN's announcement had no figures, only an unfetched chart. [https://genomics.umn.edu/AVITI-price-drop-2024]
10. **TCAG April 2025 gives X list prices but no 6000 price: the card says "Contact facility".** So there is no same-date pair at TCAG. This is FACT. [TCAG NGS Price List, April 2025, https://www.tcag.ca/documents/facilities/TCAG-NGS-Price-List April 2025.pdf; prices in CAD]
    - 25B per lane: $2,500 (100 cycles), $3,085 (200 cycles), $3,470 (300 cycles).
    - 10B per lane: $1,550 (100 cycles), $1,950 (200 cycles), $2,080 (300 cycles).
    - 1.5B per lane: $1,850 (100 cycles), $2,300 (200 cycles), $2,485 (300 cycles).
    - Human 30x WGS on the X, including library prep and 90–100 Gb: CAD $650 per sample.
    - 300-cycle 25B at 930 Gb is CAD 3.73 per Gb, and 10B at 375 Gb is CAD 5.55 per Gb, a −32.7% step.
11. **Process finding: the Read tool opens PDFs saved by WebFetch.** It works when called with no `pages` argument, even though pdftoppm is missing. Open gaps 4, 5 and 6 (GRAIL exhibit, DEF 14A, FDA SSEDs) were blocked on a shell and may be reachable this way. The method is to WebFetch the PDF URL, which saves the binary under tool-results, then Read that path. It will not help for HTML pages that truncate.

## Same-date X versus 6000 pairs

All prices are per Gb, public/internal tier, and come from the cards cited above. Each row is a comparison of a 6000 line with an X line on the same card.

| Source and date | Pair | 6000 price | X price | X versus 6000 |
|---|---|---|---|---|
| CNAG R1, Aug 2026 | S4 2x150 vs 25B 2x150 | €4.90 | €2.84 | **−42.0%** |
| CNAG R1, Aug 2026 | S4 2x150 vs 10B 2x150 | €4.90 | €4.36 | −11.0% |
| CNAG R1, Aug 2026 | S4 2x100 vs 25B 2x100 | €10.07 | €3.77 | −62.6% |
| CNAG R1, Aug 2026 | S2 2x150 vs 25B 2x150 | €12.22 | €2.84 | −76.8% |
| CNAG R1, Aug 2026 | S1 2x150 vs 25B 2x150 | €17.43 | €2.84 | −83.7% |
| CNAG R1, Aug 2026 | SP 2x150 vs 25B 2x150 | €22.07 | €2.84 | −87.1% |
| CNAG R1, Aug 2026 | S2 2x50 vs 25B 2x50 | €23.15 | €6.00 | −74.1% |
| CNAG R0, Jan 2026 | S4 "Large Scale" 2x150 vs 25B 2x150 | €4.31 | €2.84 | −34.1% |
| CNAG R0, Jan 2026 | S4 fast-track 2x150 vs 25B fast-track | €6.27 | €4.09 (from R1) | −34.8% (cross-edition) |
| Rush, 15 Jun 2026 | S4 2x150 lane (assumed 750 Gb) vs 25B lane (930 Gb) | $8.82 | $4.52 | −48.8% |
| Rush, 15 Jun 2026 | Same, S4 at 800 Gb | $8.27 | $4.52 | −45% |

OPINION: S4 is the right comparison for clinical-style 2x150 work, because the clinical 6000 base is mostly S4. The S4 pairs run from −34% to −49%. Smaller 6000 flow cells (S1, S2, SP) show −74% to −87% against the 25B, but those are less relevant to large clinical customers.

All rows are core-lab resale prices, not Illumina's price to a clinical customer, and none is net of Illumina volume discounts.

## Within-X steps

| Source | Step | Change per Gb |
|---|---|---|
| CNAG R1, 2x150 | 10B to 25B | −34.9% |
| CNAG R1, 2x100 | 10B to 25B | −37.5% |
| CNAG R1, 2x50 | 10B to 25B | −35.8% |
| CNAG R1, 2x150 | 1.5B to 10B | −40.5% |
| CNAG R1, 2x150 | 5B to 10B | −22.4% |
| CNAG R1, 2x150 | 5B to 25B | −49.5% |
| Rush, 300-cycle | 10B to 25B | −29.4% ($6.40 to $4.52) |
| NUSeq FY26, 300-cycle, nominal Gb | 10B to 25B | −24% ($4.27 to $3.23) |
| TCAG Apr 2025, 300-cycle, CAD | 10B to 25B | −32.7% |

OPINION: the step runs from −24% to −37%, so the earlier −25% to −32% is the middle of the range rather than the whole range. There is no 35B or 14B price on any card. The ASHG release on 20 Oct and the Q3 call on 29 Oct remain the checks.

## Customer-class markups (FACT)

- CNAG: international public is +12% and private is +20% over the subsidized tier, the same on both platforms.
- Rush: external is +5% on S4 and +10% on X. Rush's own letter says the 25B is cheaper per cluster than 2.5 10B flow cells.
- NU: external is +25% over internal on both X and AVITI.

## Contradictions and stale data

- **E291 (−63%):** correct arithmetic, but it is the 2x100 line. The 2x150 pair is −42%, so the "63%" should not be read as the typical decline.
- **Open gap 2 ("whole-run S4 at $6,615"):** the Rush card does not state the unit, so the lane count the gap asks for cannot be obtained from the card. A per-lane reading is more plausible, but that is inference.
- **E054 and open gap 8 within-X range (−25% to −32%):** CNAG shows −35% to −37%.
- **E001 index (−70% implied) versus core cards (−34% to −49% on S4):** the gap is explained in part by overhead in core prices, and in part by Illumina's net price including volume deals. This is OPINION and unproven.
- **UMN (Dec 2024) says AVITI is cheaper than the X 25B. NU FY26 shows AVITI roughly 2–3x the X per Gb.** The dates and read definitions differ. UMN's figures were not retrievable.
- **The search-tool summary of CNAG** said S4 2x150 is "€3.77–4.52". That mixes the X 2x100 line into the S4 line. The full PDFs show S4 2x150 at €4.90–5.88.
- **TCAG is dated April 2025**, so it is about 18 months stale.
- **The NU card has no date beyond "FY26"** and states read pairs that look conservative against the nominal 3.1B clusters per 25B lane.

## Gaps / what I could not find

- **No shell:** the assignment's curl and pdftotext approach was not possible, so I used Read on saved PDFs instead.
- **Cards not retrieved:** Broad, Stanford SGTC, Baylor, HudsonAlpha, Garvan, Vanderbilt, NYU, UC Davis, UCSF IGI and Duke were not searched or fetched in the time available. UMich returned 403 on WebFetch.
- **Catalog prices:** Fisher, VWR and Cytiva showed no prices. Illumina's store requires sign-in. A govsci.com listing exists for 20104706 (X 25B 300-cycle), but the price was not displayed. The GSA price-page dates are still unknown.
- **Ultima UG200:** the search returned no reagent $/Gb. It reconfirmed the $850K price and Solaris 2.0 Max (up to 20B reads per wafer, H2 2026). Both are already in E069.
- **MGI T20/T7+ tender price** was not searched.
- **Roche AXELIOS $/Gb** still has no verified read definition.
- **Element AVITI24 kit list prices** and Illumina X kit list prices were not found. The only AVITI numbers are core resale prices.
- **Gb per lane:** 750 Gb for the S4 lane is my assumption. The 930 Gb for the 25B lane is Rush's own figure, and NU's 2,000–2,500M read pairs gives a lower yield and a higher price per Gb.
- **Open questions that remain:** whether the 35B is already inside management's mid-teens price model, and the clinical 6000 count.

Sources:
- [CNAG 2026 R1 price list](https://www.cnag.eu/sites/default/files/CNAG%20PRICES%202026_R1.pdf)
- [CNAG 2026 R0 price list](https://www.cnag.eu/sites/default/files/CNAG%20PRICES%202026_R0.pdf)
- [Rush GMCF fee schedule June 2026](https://www.rushu.rush.edu/sites/default/files/2026-06/GMCF%20Pricing%20June%202026.pdf)
- [TCAG NGS price list April 2025](https://www.tcag.ca/documents/facilities/TCAG-NGS-Price-List%20April%202025.pdf)
- [EPFL GECF price list 9 Sep 2026](https://www.epfl.ch/research/facilities/gene-expression-core-facility/wp-content/uploads/2026/09/GECF-price-list-for-EPFL-users-09-September-2026.pdf)
- [Northwestern NUSeq FY26 rates](https://www.cgm.northwestern.edu/docs/nuseq/fy26-prices_finalusers.pdf)
- [UMN AVITI price drop, 19 Dec 2024](https://genomics.umn.edu/AVITI-price-drop-2024)
