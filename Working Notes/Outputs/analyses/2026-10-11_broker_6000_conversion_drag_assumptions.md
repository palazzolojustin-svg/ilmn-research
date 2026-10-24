# Broker assumptions on the NovaSeq 6000 → X pricing drag and conversion rate

Prepared 11 Oct 2026. Sources: all broker and independent notes in `Extracts/ILMN/research/`; ILMN calls and Strategy Day transcripts; scrape file 124; primer working file 03. Originals in `Sources/` were not re-opened.

## Answer

No broker in the folder publishes either a quantified 6000-to-X pricing drag or a modeled conversion rate. That includes points of volume per year, a 6000 decommission schedule and a 6000 revenue line. Scrape file 124 reached the same conclusion, and it also found no house models the 35B price cut. The drag sits implicitly inside each house's total consumables and gross-margin lines.

## What exists

| Source | Type | What they say |
|---|---|---|
| J.P. Morgan (Jun–Aug 2026) | Qualitative | Transition pricing headwinds "largely gone exiting this year"; recent pricing pressure "−DD%". Relays management's conversion figures (clinical 76% on X in Q1'26, 78% in Q2'26, 80–85% target by end-2026) without modeling them |
| J.P. Morgan customer survey (Jun 2026) | Survey-implied | Volume growth exceeds spend growth by 2.4–5.2 points, implying price per unit of about −2% to −4.5% a year. This is customer intention, not a modeled transition drag |
| Barclays (Feb–Aug 2026) | Qualitative, plus a margin model | "Another round of pricing headwinds in 2027 and beyond"; "lower price/Gb on NSX volumes" (X Gb share +500 bp vs revenue share flat in Q1'26, on "imperfect data"). Its gross-margin model falls to 67.8% and 67.9% in 2027–28, the only house with margin down, consistent with a drag but not stated as one |
| UBS (Mar 2026, stale) | Qualitative | "Path to about $150 per genome" if the 35B is priced like the 25B; counting applications ~16% of sequencing consumables. No conversion content |
| Freedom, Ameriprise | Qualitative | Completing the transition "should help mitigate" price erosion. 6000 placements are a "normal transition dynamic", relaying management |
| Bloomberg Intelligence | Qualitative | "Early stages of trading price for volume"; the transition "creates near-term growth headwinds" |
| Seeking Alpha (Sep 2026) | Qualitative | Illumina may have "held share by conceding on price" |

## The only numbers: analyst questions answered by management

- **RBC, Strategy Day 13 Aug 2024.** The analyst asked about a scenario of 25% volume growth with a 15% "pricing conversion headwind". The CFO said that implies mid- to high-single-digit high-throughput consumables growth.
- **Evercore, Q3'24 call.** Price per gigabase within an expected −20% to −25%? The CFO said "closer towards 25 rather than 20" because the transition accelerated. This is the only quantified drag in the corpus, and it is management's range, not a broker model.
- **Jefferies, Q2'26 call.** The analyst asked whether consumables are "over-earned" while customers run both platforms. Management said it is a "standard part of the business", not a headwind, with no number.

## Implications

- **The debate is unresolved, not mispriced on a number.** JPM treats the transition headwind as finished; Barclays expects more in 2027. No published model reconciles either view with the 83% gigabase / 59% revenue share data.
- **Any conversion path or 6000 drag must be built in-house.** The only anchors are management's disclosed shares and the 2024 −20% to −25% range. Our build is in `2026-10-11_risk_6000_tail_never_converts.md`: ~$22M a year per clinical point, ~$90–130M of 2027 drag, ~5 points by end-2027 then ~1 a year.
- **This is an edge.** Because no broker quantifies the drag or the 35B cut, a consumables print that misses on price would surprise the Street rather than confirm a published model.
