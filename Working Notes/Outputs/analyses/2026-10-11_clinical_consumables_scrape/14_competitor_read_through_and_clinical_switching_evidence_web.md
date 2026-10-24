# Agent 14: Competitor read-through and clinical switching evidence (web)

*Model: sonnet. Run 2026-10-11 02:06:50. Cost $1.13 (API-equivalent).*

**Assignment:** Research July-October 2026 (and relevant 2025-2026) news on Roche AXELIOS (placements, named customers, clinical/IVD plans, Foundation Medicine/SAGA migration, ASHG 2026 data, pricing), Ultima Genomics (UG 100 Solaris, clinical customers, deals with Natera/Guardant/others, $/genome), Element Biosciences (VITARI shipments, AVITI24 clinical use, clinical customers), MGI/Complete Genomics (Swiss Rockets), PacBio and ONT clinical wins, and any clinical lab publicly validating or moving tests off Illumina. Also Illumina's competitive responses (35B flow cell pricing, reagent rental, TruPath, Q70, price cuts). Rate each item by how directly it threatens Illumina's clinical consumables price or volume.

## Key findings

I found no named clinical lab that has publicly moved a production test off Illumina. The web evidence is a threat in development, not a loss in progress. Many of the details below come from web-search summaries, because several primary pages blocked fetching (see Gaps).

1. **No production switch found.** I searched for Natera, Guardant, Tempus, Caris, GeneDx, Labcorp and Quest. The only clinical-lab links to rivals are development or validation collaborations (Ultima with Labcorp and Quest, NeoGenomics and Centogene, plus Foundation Medicine's early-access use of Axelios). Caris's Dec 2025 10-K still names Illumina as its sole NGS supplier. FACT. [Search summary of SEC filing cai-20251231, sec.gov/Archives/edgar/data/2019410/000201941026000016/cai-20251231.htm]
   - **Threat to Illumina clinical consumables: LOW today, MEDIUM over 2027–28.**

2. **Roche AXELIOS is the most credible challenger and is being aimed at the clinic.**
   - It launched 29 Jun 2026 as research-use-only (RUO), with "a clear strategic intent" for clinical use. [Roche, 2026-06-29, roche.com/investors/updates/inv-update-2026-06-29] FACT/MGMT
   - Launch partners are Hartwig Medical Foundation (Netherlands), Broad Clinical Labs, 10x Genomics (single-cell and spatial kits), and Google DeepVariant. [same Roche page] Macrogen was named in one summary but I could not confirm it.
   - Foundation Medicine (Roche-owned) is using it in early access. It is "implementing Axelios into its clinical workflows and plans to onboard the platform into its service sites across Europe." [GenomeWeb, "Roche Sets Sights on Clinic…", Jun–Jul 2026, via search snippet; page returned 403]
   - Threat: **HIGH, but later.** Roche's own lab network is a captive clinical volume pool. There is no IVD (in vitro diagnostic) clearance yet and no timeline was found.

3. **AXELIOS pricing is competitive, not predatory.**
   - Instrument is $750K (NovaSeq X is $985K–$1.25M, per Reuters via wkzo.com, 2026-06-29). FACT
   - Sensor module is "more than 1k, less than 16k" and reusable about 20 times. A run is about $2,400, or $0.06 per million reads (simplex). The duplex 30x genome is $150. [aseq.substack.com/p/roche-axelios-pricing, Jun 2026] OPINION from the author: "competitive… but it isn't aggressively low."
   - Roche expects about 100 placements in year one and a long-term $1.1B sales target. [Reuters via wkzo.com, 2026-06-29] MGMT
   - Threat to price: **MEDIUM.** It anchors the market near $100–$150 per genome versus Illumina's roughly $200 on the X.

4. **Switching costs remain high, per sell-side and lab voices.**
   - Evercore's Vijay Kumar said the technology could help Roche "gain share in an expanding market rather than making this 'a knife fight'." He also said "You know exactly what you're dealing with Illumina for 20 years… The bar has to be very, very high." [Reuters via wkzo.com, 2026-06-29] OPINION
   - A Functional Genomics Center Zurich lab head said larger labs would likely test Roche alongside existing machines before committing. Parallel running is the likely pattern, which means Illumina volume erodes gradually. [same source] OPINION
   - **Implication for thesis Q2:** competitors are more likely to take incremental growth volume than to displace the installed base in the near term.

5. **Ultima is the most advanced rival in clinical MRD (minimal residual disease) and whole-genome sequencing.**
   - Labcorp independently validated ppmSeq with specificity above 99.9% (120 donors) and a 95% limit of detection below 3 parts per million. [CLP Magazine, 2026-04-22, clpmag.com/disease-states/cancer/ultima-genomics-whole-genome-mrd-data-aacr-2026/] FACT
   - Ultima's founder and CEO Gilad Almogy: "point toward a future where whole-genome MRD is the standard of care." MGMT
   - The Labcorp expansion (UG 100 plus Plasma Detect) was announced 2024-07-29. [BioSpace] No volume was disclosed. Quest and Ultima have a collaboration on MRD and pediatric rare-disease WGS (GenomeWeb; date not retrieved).
   - NeoGenomics is integrating UG 100 and ppmSeq at its Cambridge, UK center to develop new oncology tests. [BioPharmaTrend/BioSpace] FACT
   - **Threat: MEDIUM-HIGH for the MRD volume pool, which is the fastest-growing sequencing-intensive segment.** WGS-based MRD is exactly the high-Gb use case where Ultima's $/Gb advantage matters most.

6. **Ultima's hardware is cheaper and its roadmap is escalating.**
   - UG200 launched Feb 2026 at $850K, or $1.25M for the dual-wafer Ultra. Output is up to 162 Tb per week (about 1,350 genomes), and it is marketed at about $80 per genome. [PR Newswire / Morningstar, 2026-02-23; Vilella substack] FACT/MGMT
   - Solaris 2.0 (paired-end) is "later 2026." Solaris workflows were reported at more than 15 customer sites. [CLP Magazine; search summary]
   - OPINION (omicsomics blog, Jan 2026): Ultima's finances are opaque, it likely needs funding, and aggressive Roche pricing could pressure it. So Ultima's survival is not guaranteed.

7. **Element is a research, multiomic and newborn-screening play for now, not a clinical consumables threat.**
   - VITARI (10B reads per run, "$100 genome") is priced at $689K and ships in H2 2026. No named first-shipment customers were found. [BusinessWire, 2026-02-19]
   - Element's clinical route is AVITI Dx plus the Revvity newborn-screening IVD collaboration, with no clearance found. [Revvity/Element 2025 release; GenomeWeb JPM 2026]
   - Element's customer mix was 20% clinical research (up from 15% a year earlier). [search summary of Element company disclosure; date not confirmed]
   - Threat: **LOW-MEDIUM near term.**

8. **MGI and Complete Genomics are structurally constrained in the US.**
   - MGI is selling Complete Genomics to Swiss Rockets for $50M (Feb 2026) after Biosecure Act pressure, with a CoolMPS licence to Swiss Rockets. [Jones Day, Feb 2026; Endpoints; BioCentury] FACT
   - MGI H1'26 revenue was RMB 1.36B (about $202M), with sequencing up 18%. It sold 898 platforms to clinical customers in 2025 (+68%) and 27 T7+ units. [GenomeWeb, 2026] FACT
   - Threat: **LOW in the US and Europe, MEDIUM in China and emerging markets.** Not directly relevant to the ex-China clinical growth figures.

9. **PacBio and ONT are winning clinical share in niches, not in high-throughput short-read.**
   - PacBio Q2'26: clinical shipments +67% y/y and a mid-teens % of consumables. It sold 20 Revios, most to clinical accounts, and 26 Vegas. EMEA revenue +52% to $14.4M. [PacBio 8-K, 2026-08-05, sec.gov exhibit991-earningsrelease.htm] FACT
   - ONT H1'26: clinical revenue +35.4% to £17.6M. MyOme will use ONT in its Zenith rare disease test, commercialized by Natera. A $20M licensing deal with an undisclosed diagnostics partner is expected in H2, plus about $15M of committed purchases across FY27–28. [ONT interim results, Aug 2026; GenomeWeb] FACT/MGMT
   - Threat: **LOW to NovaSeq-class consumables, though it is a complementary-modality read-through** (long-read adds to, rather than replaces, short-read).

10. **Illumina's own competitive roadmap is visible.** I did not find any announced reagent-rental programme or formal price cut beyond the roadmap items below.
    - Flow cell roadmap: 5B flow cell ($5,986–$6,750 list); 14B flow cell in H1 2027 with turnaround under 20 hours; 35B maximum flow cell (about +40% over 25B). [Vilella substack on AGBT 2026; Illumina press release] FACT
    - Quality and chemistry: XLeap chemistry targeting Q50, and Q70 duplex sequencing in "early access mode during the second half of 2026." [Vilella] MGMT
    - TruPath: $395 list per genome, 16 genomes per day. [Vilella] FACT
    - The 35B price (about 20% lower $/Gb) was not confirmed by any web source I could open.

11. **Q2'26 call: the "over-earning" question was asked and not directly answered.**
    - The question: Tycho Peterson (the transcript summary did not identify his firm, so I cannot confirm he is the Jefferies analyst): "as the customers transition to X, are you over-earning on consumables? Because at some point, the 6000s get decommissioned." [Webull transcript, Q2'26 call, 2026-07-30]
    - Thaysen's reply: "we continue to see that we have an expansion of volume on the X, and we continue to see quite a number of the 6000s being in action" and "we did see some customers actually purchasing a few 6000s this quarter to continue their operations." FACT/MGMT
    - **Credibility-relevant: some customers bought new NovaSeq 6000s in Q2'26**, which is direct evidence that part of the 6000 revenue is sticky or parallel running.
    - No mention of Axelios, Ultima or Element appears in the summarised Q&A, so competition was not a headline topic on the call. [Webull transcript summary; incomplete]

12. **European clinical growth is described as slower.** Dhingra described it as "slower," and the Vilella commentary reads this as "the clinical acceleration story is currently a US story." [Vilella substack, Q2'26] OPINION. Roche's strongest home turf and a possible entry point for Axelios.

13. **Roche's H1'26 results (23 Jul 2026) list AXELIOS 1 as a milestone** but disclose no placement counts. Diagnostics sales were +3% at constant currency to CHF 6.7B. [Roche H1 2026 release, assets.roche.com/f/176343/x/24b5ddb84d/irp260723.pdf, via search snippet] FACT

## Threat ratings table

| Item | Date | Direct threat to Illumina clinical consumables price/volume |
|---|---|---|
| Roche AXELIOS, with Foundation Medicine captive use and EU service sites | Jun 2026 | High, 2027+ (volume first, then price anchoring) |
| Ultima WGS-MRD (Labcorp, Quest, NeoGenomics) | Apr 2026 / Jul 2024 | Medium-High (high-Gb MRD pool) |
| Ultima UG200 at $80/genome | Feb 2026 | Medium (price anchor) |
| Element VITARI / AVITI Dx / Revvity | Feb 2026 | Low-Medium |
| MGI / Swiss Rockets | Feb 2026 | Low (US) |
| PacBio / ONT clinical | Aug 2026 | Low for NovaSeq consumables |
| Illumina 14B / 35B flow cells, Q50 / Q70, TruPath | 2026–27 | Self-inflicted price per Gb decline, which is a defensive move |

## Contradictions and stale data

- Labcorp–Ultima is a 2024 item (29 Jul 2024), not 2026. Do not treat it as recent momentum. The 2026 evidence is the AACR validation data (22 Apr 2026).
- Search snippets said the 35B flow cell arrives "around the same time" as the 14B (H1 2027). Your brief says about Jan 2027 for the 35B, and I could not confirm either date from a primary source.
- Illumina NovaSeq X list price: Reuters gives $985K–$1.25M, Vilella gives $1.165M (X) and $1.5M (X Plus). These are inconsistent, so check before quoting.
- The Axelios $150 genome is duplex 30x per the aseq analysis, while the $0.06 per million reads is simplex. The two are not like-for-like, which matters when comparing against Illumina's roughly $200 genome.
- The brief says Jefferies asked the parallel-running question. The transcript summary I fetched attributes "over-earning" to Tycho Peterson (the transcript did not label his firm) and does not show a Jefferies-attributed parallel-use question. The summary may be incomplete, so verify against the corpus transcript.
- The brief says Axelios placements were about one third of about 100 first-year units by September. I found no web confirmation of any placement count. Roche's H1 release gave none.
- The 10-Q (quarter ended 28 Jun 2026) as parsed contained no competitive or pricing language. Likely a parsing limitation, not proof of absence.

## Gaps / what I could not find

- No Q3 2026 or October 2026 news on named customers moving clinical volume to Axelios, Ultima or Element. Search results stopped at roughly 9 Sep 2026.
- No ASHG 2026 (Montreal, 20–24 Oct 2026) data yet. Ultima is exhibiting at booth #1009, and Roche has an ASHG page, but the meeting falls after today's date.
- No Foundation Medicine volume or migration timetable, no SAGA-on-Axelios detail beyond the colorectal assay launch and ovarian studies, and no IVD or FDA timeline for Axelios.
- No Element VITARI first-shipment customers and no AVITI Dx clearance.
- No evidence of an Illumina reagent-rental programme or a formal price cut. TruPath is a product, not a price response.
- No insider-selling, compensation-metric or disclosure-change findings (outside my scope). A DEF 14A for FY2026 surfaced in search at sec.gov/Archives/edgar/data/1110803/000119312526149669/d13789ddef14a.htm but I did not open it.
- Blocked or unreadable pages: GenomeWeb (403, several articles), Fierce Biotech (403), the Vilella Q2'26 post (paywalled), bioRxiv UG 100 clinical-services evaluation (429; the Dec 2025 preprint's authors and conclusions are unread).
- Suggested follow-ups: open the GenomeWeb Roche clinic article, the Quest–Ultima item date, and the bioRxiv preprint. Also check JPM and Evercore notes in the corpus for Axelios placement data.

Sources:
- [Roche AXELIOS 1 launch, 2026-06-29](https://www.roche.com/investors/updates/inv-update-2026-06-29)
- [Reuters via WKZO, 2026-06-29](https://wkzo.com/2026/06/29/roche-launches-axelios-gene-sequencer-in-a-bid-to-loosen-illuminas-grip/)
- [aseq: Roche Axelios Pricing](https://aseq.substack.com/p/roche-axelios-pricing)
- [GenomeWeb: Roche Sets Sights on Clinic](https://www.genomeweb.com/sequencing/roche-sets-sights-clinic-following-commercial-launch-axelios-1-sequencer)
- [CLP Magazine: Ultima WGS MRD at AACR 2026](https://clpmag.com/disease-states/cancer/ultima-genomics-whole-genome-mrd-data-aacr-2026/)
- [BioSpace: Labcorp–Ultima](https://www.biospace.com/labcorp-expands-collaboration-with-ultima-genomics-to-advance-whole-genome-sequencing-applications-and-oncology-testing-capabilities)
- [Morningstar/PRN: Ultima UG200, 2026-02-23](https://www.morningstar.com/news/pr-newswire/20260223sf92949/ultima-genomics-introduces-the-next-generation-of-sequencing-at-scale-with-the-launch-of-the-ug200-series-and-next-generation-solaris-20-workflows-delivering-higher-output-better-performance-and-more-flexible-wafer-configurations)
- [Vilella: Illumina announcements and Ultima UG200](https://albertvilella.substack.com/p/illumina-announcements-and-ultima)
- [Vilella: ILMN Q2 2026](https://albertvilella.substack.com/p/illumina-q2-2026-results-83-of-the)
- [Webull: Illumina Q2 2026 call transcript](https://www.webull.com/news/15341695177204736)
- [BusinessWire: Element VITARI, 2026-02-19](https://www.businesswire.com/news/home/20260219372875/en/Element-Biosciences-Introduces-VITARI-Redefining-What-High-Throughput-Sequencing-Makes-Possible)
- [PacBio Q2 2026 8-K](https://www.sec.gov/Archives/edgar/data/0001299130/000129913026000117/exhibit991-earningsrelease.htm)
- [ONT H1 2026 results (search summary)](https://www.directorstalkinterviews.com/oxford-nanopore-lifts-gross-margin-and-improves-ebitda-in-h1-2026/4121260718)
- [Jones Day: MGI sells Complete Genomics, Feb 2026](https://www.jonesday.com/en/practices/experience/2026/02/mgi-tech-sells-complete-genomics-to-swiss-rockets)
- [omicsomics: Sequencing Instrument Outlook 2026](http://omicsomics.blogspot.com/2026/01/sequencing-instrument-outlook-2026.html)
