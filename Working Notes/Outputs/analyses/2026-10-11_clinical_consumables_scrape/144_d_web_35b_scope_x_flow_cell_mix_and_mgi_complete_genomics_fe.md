# Agent 144: D-web-35B-scope-X-flow-cell-mix-and-MGI-Complete-Genomics-Federal-Register

*Model: sonnet. Run 2026-10-11 12:09:44. Cost $0.48 (API-equivalent).*

**Assignment:** Goal: close open gaps 10 and 7 with sources not yet used. Part 1 (about 12 minutes): (a) NovaSeq X flow cell mix. Find the Gb output and list price per flow cell for the 1.5B, 10B, 25B and the new 35B on illumina.com spec sheets, the Illumina Store, tech notes and release notes, and any Illumina statement on the share of X volume on 25B. Compute $/Gb for each, and the 35B's implied $/Gb if ~20% lower than 25B. (b) 35B scope: whether it is open to all customers or only to volume-commit and clinical customers. Search the Illumina press release, ASHG 2026 coverage (GenomeWeb, 360Dx, Fierce, Endpoints, BioPharma Dive), LinkedIn posts by Illumina executives, and any 8-K. Note the launch date, whether it requires NovaSeq X Plus, and any reagent-rental or commit conditions. (c) Any source that splits clinical vs research share of HT Gb (the model's 64% is an assumption) such as an Illumina investor deck, 10-K segment or customer-type text, or analyst notes. Part 2 (about 8 minutes): Federal Register notice 2026-11571 (MGI Tech entity-list or listing action): date, entities and what it restricts. Confirm whether the sale of Complete Genomics closed, and its terms. Check public statements on Illumina dependence by Azenta, KAPA (Roche), IDT (Danaher), Watchmaker and Eurofins. Quantify and quote exactly; give URL and publication date for each item; label anything not found as not found. Hard stop at 20 minutes.

## Key findings

Most of what I checked was already in the ledger or came back thin. Three items are new. The Federal Register notice is a DoD list and it does name Complete Genomics. The Complete Genomics sale had not closed as of the sources I found. The Illumina order page lists 5B, 14B and 35B differently from the earlier wave.

1. **FACT: Federal Register notice 2026-11571 is not an MGI Entity List action.** It is a Department of Defense notice, "Notice of Availability of Designation of Chinese Military Companies," published 10 Jun 2026 (Federal Register API, https://www.federalregister.gov/api/v1/documents/2026-11571.json). The list itself was released 8 Jun 2026 under Section 1260H of the FY2021 NDAA. This corrects the gap 7 framing, which called it an "MGI listing."
2. **FACT: The 1260H update added 65 entities.** That is 17 new parents and 48 new subsidiaries, with 10 removals (WilmerHale, 11 Jun 2026, https://www.wilmerhale.com/en/insights/client-alerts/20260611-pentagon-adds-65-new-entities-to-the-1260h-list-of-chinese-military-companies). The genomics names are WuXi AppTec and Novogene (new parent listings) and Complete Genomics (a new subsidiary, under BGI Group). WilmerHale and the Federal Register summary gave no separate MGI Tech or BGI Genomics listing, and I could not open the notice text to confirm that.
3. **FACT: STOmics Americas was also listed, and Novogene says it was listed in error.** Novogene is seeking removal and says it has no state ownership or control (GenomeWeb and Vir.com.vn snippets, June 2026). I could not fetch the GenomeWeb article (HTTP 403) or the Novogene statement itself.
4. **FACT, with a gap: The Complete Genomics sale to Swiss Rockets had not closed in any source I found.** It was announced 23 Feb 2026 for USD 50M, for 100% of Complete Genomics, paired with a CoolMPS licence. MGI's board, Swiss Rockets' board and the Chinese authorities had approved it. MGI shareholder approval was still expected (Complete Genomics press release; Jones Day 2026; Yicai Global; GenomeWeb, Feb 2026). No closing notice turned up. This qualifies E131, which says MGI "sold" the unit.
5. **OPINION (my inference): Complete Genomics was named on the DoD list on 8 Jun 2026, so the Swiss Rockets deal was probably still pending then.** Whether it closed after that date is not found. If it closes, the listing may become moot or contested, but I found no source saying so.
6. **FACT: The 1260H list triggers phased restrictions** (WilmerHale, 11 Jun 2026).
   - From 30 Jun 2026, the Pentagon cannot enter into, renew or extend contracts with listed entities.
   - From 30 Jun 2027, it cannot procure goods or services "produced or developed by" them.
   - WilmerHale links the listing to the BIOSECURE provisions in the FY2026 NDAA. These restrict federal contract, grant and loan funds for "Biotechnology Companies of Concern."
7. **OPINION (my inference): This is mildly positive for Illumina in federal and academic accounts**, because it adds friction for Complete Genomics and Novogene sequencing and services. It is not quantified, and I found no Illumina statement on it.
8. **FACT: The Illumina order page lists these kits** (https://www.illumina.com/systems/sequencing-platforms/novaseq-x-plus/order.html, fetched 2026-10-11).
   - 1.5B: 100, 200, 300 and 600 cycle.
   - 5B: 100, 200 and 300 cycle.
   - 10B: 100, 200 and 300 cycle.
   - 25B: 100, 200 and 300 cycle.
   - Prices show "Sign in to add to cart or see pricing."
   - The page lists no 35B or 14B kit, so as of 11 Oct 2026 neither is orderable, which is consistent with Illumina's H1 2027 roadmap window (E057/E135 corrections).
   - The extracted Gb column ("8–10.5 Tb" for every row) was a parsing artefact and is unreliable. Ignore it.
9. **FACT, a secondary source:** A search summary of Genohub listed maximum outputs of 8,000 Gb for the 25B, 3,000 Gb for the 10B and 500 Gb for the 1.5B (https://genohub.com/ngs-sequencer/2/illumina-novaseq-x/, undated). The 25B figure conflicts with the 930–1,000 Gb per lane in E259, but the units may differ, so I did not use it.
10. **FACT: Illumina's roadmap page confirms the timing of each change** (https://www.illumina.com/systems/sequencing-platforms/novaseq-x-plus/applications/innovation-roadmap.html).
    - H1 2026: 5B and 1.5B-600 cycle, and staggered starts.
    - H2 2026: high-throughput mode.
    - H1 2027: 14B (a 40% yield increase on 10B) and the 35B.
    - This agrees with the E057/E135 corrections. It gives no price or eligibility for the 35B.

## Part 1 results

**(a) $/Gb by flow cell.** No Illumina list prices were retrievable. The order page hides them, and no spec sheet or tech note surfaced in search. So I cannot give a sourced Illumina list $/Gb for the 1.5B, 10B, 25B or 35B.
- The only prices in my results are third-party core prices (Illinois, TxGen), mostly already covered by E054 and E051.
- **35B implied $/Gb:** this cannot be sourced. At roughly 20% below the 25B (E058), it would sit at about $2.30–2.40/Gb if the 25B-300 GSA price of $24,155 (E054 correction) gives $2.90–3.00/Gb. That is my arithmetic on ledger figures only.

**(b) 35B scope.** NOT FOUND.
- I found no Illumina press release, 8-K, ASHG 2026 coverage or executive LinkedIn post about the 35B scope.
- That includes whether it needs the NovaSeq X Plus, whether it is open to all customers or only volume-commit and clinical customers, and any reagent-rental conditions.
- The only primary statements are the 23 Feb 2026 roadmap press release (https://www.illumina.com/company/news-center/press-releases/2026/7b4175f1-a13f-401e-9335-3e5eadbb1fe0.html) and the roadmap page, both with timing only.

**(c) Clinical vs research share of HT Gb.** NOT FOUND in the searches I ran.

## Part 2 results

- **Complete Genomics:** pending as of the latest dated sources (Feb 2026 deal terms, June 2026 listing). The terms are USD 50M for 100% and a CoolMPS licence.
- **Dependence of Azenta, KAPA (Roche), IDT (Danaher), Watchmaker and Eurofins on Illumina:** NOT FOUND. My one search returned only Twist results (NGS applications revenue +12% y/y to $61.8M in fiscal Q3 2026, with no Illumina-dependence statement). I did not search KAPA, IDT, Watchmaker or Azenta separately.

## Contradictions and stale data

- E131 says MGI "sold" Complete Genomics to Swiss Rockets for $50M. Closing is unconfirmed, and the DoD list on 8 Jun 2026 still named Complete Genomics as a BGI-linked subsidiary.
- Open gap 7 describes 2026-11571 as an MGI listing. It is the DoD 1260H notice, and MGI Tech is not separately named in the sources I could read.
- The order page extract's "8–10.5 Tb" for every kit is wrong. Do not use it.

## Gaps / what I could not find

- The text of notice 2026-11571, which redirects to an unblock page. Fetch the PDF or govinfo version to confirm whether MGI Tech or BGI Genomics appear.
- Illumina list prices for any NovaSeq X flow cell, which sit behind a login.
- The 35B scope, price and eligibility, and any clinical-versus-research Gb split.
- Whether the Complete Genomics sale has closed since June 2026.
- Illumina-dependence statements from the five named companies other than Twist.

Sources:
- [Federal Register API, 2026-11571](https://www.federalregister.gov/api/v1/documents/2026-11571.json)
- [WilmerHale, 1260H update, 11 Jun 2026](https://www.wilmerhale.com/en/insights/client-alerts/20260611-pentagon-adds-65-new-entities-to-the-1260h-list-of-chinese-military-companies)
- [Illumina NovaSeq X order page](https://www.illumina.com/systems/sequencing-platforms/novaseq-x-plus/order.html)
- [Illumina NovaSeq X innovation roadmap](https://www.illumina.com/systems/sequencing-platforms/novaseq-x-plus/applications/innovation-roadmap.html)
- [Illumina roadmap press release, 23 Feb 2026](https://www.illumina.com/company/news-center/press-releases/2026/7b4175f1-a13f-401e-9335-3e5eadbb1fe0.html)
- [Jones Day, MGI sells Complete Genomics](https://www.jonesday.com/en/practices/experience/2026/02/mgi-tech-sells-complete-genomics-to-swiss-rockets)
- [GenomeWeb on the DoD list](https://www.genomeweb.com/sequencing/us-dod-expands-chinese-military-companies-list-include-novogene-complete-genomics-others), seen in search results only (403 on fetch)
