# Agent 31: 31-web-35B-pricing-procurement-tenders-and-competitor-placements

*Model: sonnet. Run 2026-10-11 02:42:17. Cost $0.66 (API-equivalent).*

**Assignment:** Goal: find new price-per-Gb and traction evidence for open gaps 3 and 14, from sources earlier agents have not used. Do not repeat core-facility price lists already captured (Salk, UConn, CWRU, Dana-Farber, TGen), the NGI Sweden note or the Roche investor day content.
(1) Procurement and government records. Search USAspending.gov and SAM.gov (awards to Illumina, Roche, Ultima and Element for NovaSeq X, flow cells or AXELIOS), NIH RePORTER S10 shared-instrument grants 2025-26 (instrument and reagent budgets), UK Find a Tender and Contracts Finder, NHS Genomic Medicine Service and Genomics England tenders, the EU TED portal, Australian AusTender, and state and VA contracts. Pull any published unit prices for flow cells and kits, or $/Gb or $/genome, with dates.
(2) Illumina's own channels. The illumina.com product pages for NovaSeq X flow cells (1.5B, 10B, 25B, 5B, any 35B or 14B), the Illumina press room, the ASHG 2026 (20-24 Oct) preview announcements and exhibitor schedule, the Illumina roadmap page, and distributor listings (Fisher, VWR, Cytiva, Genome Technologies) showing catalog prices for X and 6000 flow cells. Compute $/Gb and the NovaSeq 6000 S4 versus X 25B comparison. Check for any Jan 2027 list-price notices, and the Q1'25-style 'pricing actions' language.
(3) Trade press and conference material: GenomeWeb, 360Dx, Fierce Biotech, STAT, Evaluate Vantage and BioSpace coverage from Aug to Oct 2026 on AXELIOS, Ultima UG200 and Element VITARI placements and named customers, any clinical lab production switch, and Roche's placement count. Also AGBT 2026, ESHG 2026 and ASCO/AACR 2026 posters and abstracts on lab cost per genome or per MRD test with Ultima, Element, AXELIOS or NovaSeq X. Also Ultima, Element and Roche press releases, and ONT, PacBio and 10x commentary on pricing since 1 Sept 2026.
(4) Patents and customer-side filings on the Element, Ultima and Roche side: customers named in 8-Ks.
Return a dated table (source, date, product, price, unit, implied $/Gb, URL) plus a list of named clinical or large-scale customers of each challenger with the evidence level (announced, validated, in production). Mark anything unverified. Hard stop at 20 minutes.

Status: I've read the ledger and gaps file and run searches on Illumina pricing, Roche, Ultima, Element and federal procurement. I'm now writing up what's new.

## Key findings

1. **New: Illumina published list prices for the NovaSeq X 25B kits that the ledger lacks.** The 25B 100-cycle kit lists at $11,700 and the 200-cycle kit at $14,500 (catalog 20125968). These are shipped-since-Dec-2024 prices announced 7 Jan 2025. FACT (secondary: Vilella/"Rhymes with Haystack" ASHG25 recap, https://albertvilella.substack.com/p/everything-you-need-to-know-from). A search summary of Illumina's ordering page gave the same $14,500 figure. The ordering page itself shows "Sign in to see pricing" (https://assets.illumina.com/systems/sequencing-platforms/novaseq-x-plus/order.html). This updates E054/E055, which only had core-facility prices and the "$2.00/Gb" launch claim.
2. **Implied $/Gb from those list prices.** This is my calc and unverified, because I could not find an output spec per cycle count. Illumina's page gives only "8–10.5 Tb" for the 25B across all cycle counts.
   - Assuming output scales with cycles (25B read pairs × 2 × read length), the 300-cycle kit gives ~7.5 Tb, consistent with the 7.8 Tb that UConn lists.
   - On that basis the 200-cycle kit is ~5.0 Tb, so $14,500 ÷ 5,000 Gb ≈ **$2.90/Gb**.
   - The 100-cycle kit is ~2.5 Tb, so ≈ **$4.68/Gb**.
   - Shorter-read kits are therefore not the "$2.00/Gb" product. The 300-cycle list price, which is the real $2.00/Gb test, is still not found (OPINION/calc).
3. **Core resale ratio.** UConn lists the 25B 300-cycle at $24,951 ($3.20/Gb, 7,800 Gb). CWRU (Jul 2026) lists $25,093. If Illumina's 300-cycle list were ~$15K, which would match $2.00/Gb, cores are marking up ~65%. That is consistent with E051's note that core lists include labor and overhead. The 300-cycle list price is unverified, so treat this as a hypothesis only.
4. **No 35B price or ASHG 2026 pricing announcement exists in public sources as of 11 Oct 2026.** The ordering page lists 1.5B, 5B, 10B and 25B only, with no 35B or 14B SKU. This confirms E214 and adds that no catalog numbers exist yet. FACT (order page, read 2026-10-11).
5. **Roche named customer: Macrogen.** Korea Biomedical Review (30 Jun 2026) reports Macrogen as "the first institution in Asia" to adopt AXELIOS 1, citing WGS, automated interpretation and "clinical decision support." No unit count or price is given. It is not in E124. FACT (announced) (https://www.koreabiomed.com/news/articleView.html?idxno=32246).
6. **Ultima Hartwig adoption date.** Hartwig adopted the UG200 on 12 Jun 2026, ahead of the Precure selection on 22 Sep 2026 (E128). The UG200 is quoted at up to 60,000 30x WGS per year for the Ultra and 30,000 for the standard model. These are company capacity claims. MGMT (search summaries of the Ultima release, the-scientist.com and clpmag.com).
7. **BaseClear.** BaseClear launched Ultima-enabled services in mid-July 2026. This extends E128's "first EU certified provider" line. MGMT (search summary of the biospace.com press release).
8. **Element VITARI: still no named customers.** The Feb 2026 release says "significant interest from existing AVITI customers," and pre-orders are open. The ledger already has $689K and H2 2026 shipping (E069). Nothing new.
9. **Procurement and government records yielded no unit prices.** Details are in the table below.

## Dated table (new items only)

| Source | Date | Product | Price | Unit | Implied $/Gb | URL |
|---|---|---|---|---|---|---|
| Vilella recap of Illumina announcement | 7 Jan 2025 (published ASHG25 recap) | NovaSeq X 25B 100-cycle kit | $11,700 | kit | ~$4.68 (calc, ~2.5 Tb assumed) | albertvilella.substack.com/p/everything-you-need-to-know-from |
| Same | 7 Jan 2025 | NovaSeq X 25B 200-cycle kit (cat. 20125968) | $14,500 | kit | ~$2.90 (calc, ~5.0 Tb assumed) | same |
| Illumina order page | read 11 Oct 2026 | All X kits (1.5B, 5B, 10B, 25B) | login-gated | – | – | assets.illumina.com/systems/sequencing-platforms/novaseq-x-plus/order.html |
| UConn core list (via search snippet) | 2026 | 25B 300-cycle flow cell | $24,951 | flow cell | $3.20 | honeycrisp.core.uconn.edu/products/358 |
| CWRU (via search snippet) | Jul 2026 | 25B 300-cycle flow cell | $25,093.04 | flow cell | ~$3.22 (calc at 7.8 Tb) | case.edu/medicine/genomics/pricing |

The UConn and CWRU rows are already known in substance (E054). I list them only to anchor the resale-markup point in finding 3.

## Named challenger customers and evidence level

| Challenger | Customer | Evidence level | Date and source |
|---|---|---|---|
| Roche AXELIOS | Macrogen (Asia, first adopter) | Announced; RUO; no volume | 30 Jun 2026, Korea Biomedical Review |
| Roche AXELIOS | Hartwig, Broad Clinical Labs | Collaborators named in the launch release (already in E124) | Roche release, Jun 2026 |
| Ultima UG200 | Hartwig | Announced adoption (12 Jun 2026) | Press release via aijourn.com |
| Ultima UG200 | Precure/Mayo with Helix and Thermo Fisher | Selected, fleet to be built (22 Sep 2026; already E128) | hpcwire.com |
| Ultima UG200 | BaseClear | Service launch, mid-Jul 2026 | biospace.com |
| Element VITARI | None named | Pre-orders only | Element release, 19 Feb 2026 |

No challenger customer shows evidence of "in production" for clinical use.

## Procurement checks (items 1 and 4 of the brief)

- **USDA-ARS (31 Jul 2026, SAM.gov mirror cleat.ai).** This is a small-business set-aside for trout WGS on "NovaSeq X or equivalent." No award value or unit price is published. It confirms agencies write "or equivalent" into solicitations. That would let Ultima or Element bid, but it is a single research example (https://www.cleat.ai/government/contracts/illumina-novaseq-x-whole-genome-sequencing-omt1).
- **USDA-ARS PIRU.** It specifies one 10B lane yielding about 375 Gb per pooled library. That gives a 10B lane output of ~375 Gb, with no price (search summary of a SAM.gov listing).
- **NCI (Frederick).** A NovaSeq X Plus service agreement for 26 Mar 2026–25 Mar 2027 requires Silver Support. No amount is shown (frederick.cancer.gov/node/10161).
- **Not reachable:** the GenomeWeb pages returned HTTP 403, including the AGBT Roche $150-genome article.

## Contradictions and stale data

- **E054 ("Illumina's own list is $2.00/Gb").** I could not corroborate this from the 25B kit prices. The 200-cycle kit implies ~$2.90/Gb on my assumption. The $2.00 claim may apply only to the 300-cycle kit or to a net-price basis. Treat it as unverified until the 300-cycle list price is found.
- **Output spec.** Illumina's order page shows an identical "8–10.5 Tb" for every 25B cycle count, which cannot be right for 100- or 200-cycle runs. It looks like a template artifact, so my cycle-scaled outputs are assumptions.
- **Vilella recap dating.** The post is an ASHG25 (Oct 2025) recap, and the list prices it cites date from Jan 2025. They may have changed since, and the 5% tariff surcharge (E170) is not reflected.

## Gaps / what I could not find

- **25B 300-cycle Illumina list price.** I did not find it. A distributor listing (Fisher, VWR, Cytiva, Genome Technologies) is the likely route, and none surfaced in the searches.
- **Jan 2027 list-price notices and the "pricing actions" footnote (E208).** Nothing public.
- **ASHG 2026 (20–24 Oct) previews.** Nothing found yet, and no Illumina press release on the 35B. Re-check during the week of ASHG.
- **Trade press, Aug–Oct 2026.** I found no GenomeWeb, 360Dx, Fierce, STAT or BioSpace piece on an AXELIOS placement count or a clinical production switch. Two searches on Natera, Guardant, Caris and Tempus returned only older validation documents (the one 2026 item was Tempus xH, a WGS assay announced June 2026).
- **Not checked, for lack of time:** NHS and Genomics England tenders, EU TED, AusTender, UK Contracts Finder, NIH RePORTER S10 budgets, 8-K customer disclosures for Element, Ultima and Roche, patent filings, and AGBT, ESHG, ASCO and AACR cost-per-test abstracts. Peer commentary since 1 Sep 2026 from ONT, PacBio and 10x is also unchecked.

**Overall: partial new evidence, with items 1–4 above as the useful additions.** The 25B list prices are the main one, with a caveat on how I derived $/Gb.

Sources:
- [Rhymes with Haystack (Vilella), ASHG25 recap](https://albertvilella.substack.com/p/everything-you-need-to-know-from)
- [Illumina, Order the NovaSeq X Series](https://assets.illumina.com/systems/sequencing-platforms/novaseq-x-plus/order.html)
- [Korea Biomedical Review, Macrogen/AXELIOS](https://www.koreabiomed.com/news/articleView.html?idxno=32246)
- [cleat.ai USDA-ARS solicitation](https://www.cleat.ai/government/contracts/illumina-novaseq-x-whole-genome-sequencing-omt1)
- [HPCwire, Ultima/Precure](https://www.hpcwire.com/bigdatawire/this-just-in/ultima-genomics-selected-for-mayo-clinic-led-million-biospecimen-initiative/)
- [BioSpace, Ultima/BaseClear](https://www.biospace.com/press-releases/ultima-genomics-and-baseclear-to-expand-european-access-to-low-cost-and-high-throughput-sequencing-using-ultimas-ug200-platform)
- [Element, VITARI launch](https://www.elementbiosciences.com/news/element-biosciences-introduces-vitari-redefining-what-high-throughput-sequencing-makes-possible)
