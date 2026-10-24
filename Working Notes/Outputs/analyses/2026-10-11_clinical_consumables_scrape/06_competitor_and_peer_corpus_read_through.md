# Agent 06: Competitor and peer corpus read-through

*Model: sonnet. Run 2026-10-11 01:58:38. Cost $0.61 (API-equivalent).*

## Key findings

Scope note: I read the Roche Investor Day extract, the Roche H1 call (AXELIOS and Q&A sections), and the three Roche broker notes in full. I also read the TXG Q1 call, the TXG BofA conference section on sequencing costs, the PacBio Q2 call (targeted grep), the ONT Q2 call and JPM Roche-day note (targeted), the MGI H1 and Q1 UBS notes, the Barclays sector note, and the TMO extracts (grep only). I did not read every ONT or PacBio broker note end to end, so ONT and PacBio depth is partial.

1. **FACT: Roche AXELIOS priced at $150/genome list, with "no volume-based discounting. Everyone can achieve this pricing."** Simplex is $0.06 per million reads, and a 1.1 Mb liquid-biopsy panel costs about $25 a sample, "multiples lower than what you can achieve with other technologies." [Roche Investor Day, 2026-05-12, Extracts/ROCHE/transcript/ROCHE_2026-05-12_Investor_Day_Diagnostics_AXELIOS.md] JPM puts Illumina at $200/genome and Ultima at a targeted $80-100. [JPM ONT note, 2026-05-13]
2. **MGMT: Roche says "mid-throughput users can actually access the same economics as high-throughput users."** [Lauer, Investor Day] This targets the smaller clinical labs that pay Illumina the most per genome. It is a pricing-power threat to Illumina's mid-tier NovaSeq 6000 and NextSeq base, not only to the largest labs.
3. **FACT: Roche's year-one placement goal is only about 100 instruments.** NovaSeq X placed 352 in its first year, Revio 173 and Element 112. [JPM, 2026-05-13] Roche says about one-third were placed within roughly 60-80 days of the 29 Jun 2026 launch, "external customers only" and "no teaser offers" (CEO call 8 Sep; Barclays 28 Sep).
   - OPINION: the instrument count is small, so near-term Illumina volume risk is limited.
   - The real exposure is where the placements go. Foundation Medicine, SAGA, Freenome and clinical labs are all named, and Roche expects reagent revenue to build "as customers migrate existing assays." [JPM CEO call, 2026-09-15]
4. **MGMT: Barclays says early demand is "from both clinical laboratories and academic centres."** Roche kept its ">CHF1bn" AXELIOS ambition and said further data would come at ASHG. [Barclays, 2026-09-28]
5. **FACT: Roche's own captive volume is a real, though small, source of share loss.** Foundation Medicine is an AXELIOS early-access site and expects "shorter turnaround and a lower cost base." [Investor Day] FMI has delivered more than 1.5M CGPs. It plans to use AXELIOS for the whole-genome tissue baseline in Pathlight MRD, and to onboard installation-and-services sites later.
   - Whether FMI is an Illumina customer today is not stated in my files.
6. **FACT/MGMT: Roche's MRD design is not sequencing-intensive for monitoring.** CEO Schinecker described the SAGA workflow as: "sequence the cancer (on AXELIOS), then monitor with specific primers on digital PCR, which is cost-effective." [Roche H1 call, 2026-07-23]
   - OPINION: this is a tumor-informed design. Sequencing happens once at baseline, and serial monitoring runs on PCR. That limits the "deeper MRD means more Gb" assumption in thesis question 2 for Roche's own volume.
   - The Pathlight example quoted 6 years and 12 time points in the Medicare coverage.
7. **FACT: Roche sizes the markets it is attacking.** Sequencing is CHF 7B growing 7% (Investor Day) or about USD 7.3B (H1 call). MCED early detection is growing at a 35% CAGR to CHF 5.3B by 2030. MRD-driven monitoring is growing 32% to CHF 5B. Therapy selection (CGP, companion diagnostics) is CHF 17B growing 9%. FMI says oncology testing will "essentially double over the next 5 years." [Investor Day]
   - Roche's CHF 7B at 7% growth is slower than the mid-20s volume growth in the Illumina management model. This suggests the market is mostly price-deflated, which fits with price per Gb falling.
8. **FACT: MGI shows clinical growth with price deflation.** H1 2026 MGI clinical sequencing revenue rose 36.6% and research was "broadly flat." Reagents rose 16.3% while instruments fell 6.4%. [UBS MGI H1, 2026-08-24]
   - Unit sales were over 1,470 sequencers in 2025 versus over 1,260 in 2024, with ASP dragged down by "pricing pressure and product mix changes." [UBS MGI Q1, 2026-04-29]
   - MGMT: "industry competition has shifted from product pricing to broader competitive capabilities." Management expects the industry to improve in 2027, with teens growth.
9. **FACT: 10x's CEO says price per read has "dropped like hugely" with Ultima and Roche.** He added that single-cell work can use simplex reads, so it becomes "even cheaper than the whole genome price would indicate." He called this "a massive change in the ecosystem" that unblocks mega-projects. [TXG BofA conference, 2026-05-13] This is a customer-side confirmation that the price per Gb is falling across the industry, not just at Illumina.
10. **FACT: PacBio's clinical shipments are growing quickly but from a small base.** Q2 2026 clinical consumable shipments rose 67% and were a mid-teens share of consumable shipments. EMEA revenue rose 52%. PacBio cut its list price to $345 per 20x HiFi genome (-30%) and expects volume to offset it in H2. [PACB Q2 call, 2026-08-06]
    - Pull-through was about $202K per system.
    - Barclays: "the true Dx opportunity unlocks when PACB gets the cost of sequencing down close to ILMN's $200." [Barclays, 2025-08-14]
11. **FACT: ONT clinical is its fastest-growing line at GBP 17.6M (+35.4%) in H1 2026.** It is driven by "reimbursement-funded labs running assays or developing methods." ONT says PromethION flow cell volumes grew over 20% while ASPs fell as customers moved into higher volume-discount tiers. That is the same volume-up, price-down pattern as Illumina's transition. [ONT Q2 call, 2026-08-19]
    - ONT says clinical beyond LDTs into IVD is "longer term" and expects it to overtake BioPharma "beyond 2030."
12. **OPINION (Deutsche Bank): "Illumina's growth is increasingly Clinical-led and most PacBio Revio placements went to Clinical accounts."** [DB ONT note, 2026-09-28] This is a sell-side read from outside Illumina's own commentary.

## Roche AXELIOS detail

**Product and performance**
- FACT: Launch date was 29 Jun 2026 and the product is RUO (research use only). Roche calls it a "first-gen RUO platform" with a long-term ambition of a clinical platform and a 20-year SBX roadmap. [H1 call; Investor Day]
- FACT: Duplex mode gives 1.8 Tb in 4 hours (about 16 genomes, Q38). Simplex gives 40B reads in 4 hours at an average of 175 bp.
- FACT: A fully loaded run of 4 queued pools yields 64 genomes in under 2 days. The sensor module is reusable up to 20 times. A NICU workflow produced a VCF in under 4 hours. The instrument is about $750K per your brief; I did not find a price in the Roche files.
- MGMT: Roche says library prep is "similar to traditional methods" and automated on Roche, Beckman and Hamilton platforms. Switching cost for Illumina users is therefore partly about validation, not workflow.

**Clinical channels Roche cites**
- Foundation Medicine: 40%+ of US oncologists ordered in the last 12 months. FMI won 50% of the NHS liquid-biopsy tender. [Investor Day]
- Freenome: Jefferies asked about it. Roche's Sause replied that Freenome "is evaluating the AXELIOS sequencer" and that workflow incorporation "depends on the outcome." Roche is also working with Freenome on MCED. So Freenome is not yet committed.
- Broad Clinical Labs and Hartwig are early-access sites. Roche has hosted "a few hundred" prospective customers.
- Lauer: community oncology "bring testing in-house" can be met with an economic solution, and "centralized and decentralized models will coexist."

**Margin intent**
- MGMT: Lauer said there is "no reason sequencing can't be massively profitable" even at scale, and Roche has "every technical entitlement to be just as cost efficient, if not more" than public peers. As per-genome cost falls, costs shift to library prep and sample collection. [Investor Day]

## Read-through to Illumina's thesis questions

**Q1: Over-earning on the 6000 base**
- No peer file addresses NovaSeq 6000 to X conversion or Jefferies' parallel-running question. Peer evidence is indirect.
- OPINION: PacBio is already lowering the price of a long-read genome by 30% to $345, Roche lists $150 with no discount, and Ultima is targeting $80-100. This suggests that a clinical lab compared against a $150-200 short-read genome sees an X price near $200 (per JPM) as the benchmark. The 6000 is the high-price point for that comparison.
- No peer commentary suggests labs are running a competitor in parallel with an Illumina platform. Roche's "external customers only" placements (CEO call, Sep) are the only hint, and no customer names were given.

**Q2: Volume offsetting price**
- PacBio, ONT, 10x and MGI all show the same pattern: volume rising faster than revenue, with price cuts of roughly 30% (PacBio) or tier discounts (ONT).
- 10x single-cell reaction volume grew double digits while single-cell consumable revenue grew +6%. 10x said Flex Apex pricing and mix would "stabilize" by 2027. [TXG Q1 call, 2026-05-07]
- OPINION: no peer shows revenue growing faster than volume, which supports the notion that clinical price-per-Gb pressure persists.
- Roche's JPM survey point (planned volume growth 2.4-5.2 pts faster than planned spend) is consistent with this pattern.

**Thermo Fisher funding read-through**
- FACT: TMO Q2 2026 organic growth was 5% and EPS grew 13%. CEO Casper described biotech funding as improving through 2025 and 2026, with a 2-3 quarter lag into spending. Clinical research is first to benefit. Academic and government funding was described as stabilizing (U.S. slightly positive, Europe strong, China muted). [TMO Q2 call 2026-07-23; MS conf 2026-09-15]
- FACT: TMO did not mention Illumina or sequencing in the Q2 call (extract note). The read-through is limited to the research-funding backdrop and says nothing about clinical consumables.

## Management behavior and credibility (peers only)

- OPINION: Roche's 100-placement target reads as a conservative bar that is easy to beat. Barclays reports Roche is "progressing well in the first 60 days." Roche has now given placement progress twice (JPM 8 Sep, Barclays 28 Sep), but not a count. Watch for a vague metric.
- FACT: Roche's 2027 diagnostics ambition (mid-to-high single digit) was cut from "mid-to-high single digit" over the long term to a 2026 "mid-single-digit" ambition. [H1 call] China price reform is the stated cause.
- FACT: Roche's core operating profit in H1 included CHF 126M of "extraordinary income from patent licensing." [H1 call] That is a one-off.
- FACT: PacBio sold its high-throughput short-read IP to Illumina (Jan 2026, $48.1M net cash) and Illumina has launched TruPath long-read. Barclays says TruPath "could freeze part of the long-read market" for PacBio, and it is "the third iteration/name change of ILMN's push into long-read." [PACB Q1 call, 2026-05-08; Barclays sector note, 2026-03-06]
- FACT: PacBio's CEO changed in Aug 2026 and it reorganized in early August. [PACB Q2 call; Barclays 2026-08-12] Not Illumina-related, but it shows weak competitor depth in long read.

## End-customer and market notes

- Barclays: Guardant fell 20% and Natera fell 14% between 3 Feb and 5 Mar 2026 on "MCED failure, Dx competition, AI noise, valuation reset." [Barclays sector note, 2026-03-06] This is read-through for clinical-lab sentiment. I could not find in my files what the "MCED failure" refers to.
- Barclays: Quest rose 10% on a "big organic volume beat in 4Q." Abbott was acquiring Exact Sciences. TXG rose 12% on the Roche kit for AXELIOS at AGBT.
- Roche's TB IGRA, pTau217 and mass-spec items in the Investor Day are not sequencing-relevant.
- PAMA: CMS announced cuts on 21 Sep 2026. Barclays thinks Roche is insulated because it sells to labs. OPINION: Illumina's clinical-lab customers are the reimbursed parties, so any PAMA cut falls on them. I found nothing on the size of the cut or its effect on NGS tests.

## Contradictions and stale data

- AXELIOS spelling is inconsistent in the Barclays note ("ALEXIOS"). It is the same product.
- Roche sizing: CHF 7B at 7% growth (Investor Day, May) versus USD 7.3B "assessed in 2025" (H1 call, Jul). These could be consistent, but the units differ.
- Roche read length: Investor Day says simplex reads of 500-1,000 bp. The H1 call says "up to 1,500 bases" and 175 bp average. JPM says 400-600 average and up to 1,000. The performance specs are moving.
- Placement timing: the CEO call says "about one-third" placed. Barclays says "first 60 days." Your brief says "by Sept."
- Barclays and MGI figures are mixed in time: MGI H1 clinical +36.6% is from a low base after a 2025 revenue decline (2025 revenue of Rmb2.78B down from Rmb3.01B).
- Barclays' Illumina rating of Underweight with a $110 target is from an ONT note dated 2026-04-06. It may be stale.
- Roche's "mid-throughput users can access the same economics" claim is Roche's, not independently verified.

## Gaps / what I could not find

- No peer statement about a named clinical lab validating AXELIOS or moving a production assay off Illumina. Only Freenome (evaluating), FMI (early access), Broad Clinical Labs and Hartwig are named.
- No AXELIOS reagent revenue, per-run cost for MRD panels beyond the $25 example, or clinical (IVD) regulatory timeline.
- No Ultima or Element files in my scope. Ultima's $80-100 figure comes second-hand from JPM.
- No peer data on 6000 to X conversion, parallel instrument use, or Illumina's 35B flow cell.
- MGI: no data on clinical pricing per Gb. Its UBS notes also do not break out China clinical (NIPT) from the rest.
- Not read in full: ONT broker notes (Sep conference and Barclays/DB H1 notes), PacBio's Sep MS conference and the Barclays PacBio notes (May and Aug 2026), and Roche consensus files. A second pass on ONT/PacBio clinical growth rates is worthwhile.
