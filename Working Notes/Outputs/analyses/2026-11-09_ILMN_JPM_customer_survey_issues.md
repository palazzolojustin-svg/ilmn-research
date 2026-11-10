# Problems with the JPM Illumina customer survey (June 2026)

*Prepared 9 Nov 2026. Sources: the JPM survey deck "ILMN Customer Survey: Insights into Market Views of Axelios 1" (`Sources/ILMN/research/20260615_JP_Morgan_ILMN_Illumina-_Inc.md`, cited as D + line), the 10 Jun upgrade note that uses it (`20260615_JP_Morgan_ILMN_Illumina-_Inc.-_Upgrading_to_Overweight_on_a_Sticky_Clin.md`, cited as N + line), and earlier work in this folder (evidence ledger E021, E067, E248; red team file 19). Key lines were re-checked against the deck. Ranges, implied prices and confidence intervals are our arithmetic, not JPM's.*

## The short answer

Yes, the problems are serious. The survey is a poll of 62 current Illumina customers about what they intend to spend. It reflects small and mid-size academic labs and community or hospital clinical labs. It does not measure Illumina's research-segment growth, Illumina's own pricing, or the large clinical labs that drive Illumina's consumables growth. JPM's upgrade note leans on it harder than it can bear. In particular:
- The "+9% research consumables spend in 2027" figure should not be used as a forecast for Illumina research revenue.
- The implied 2–5% price decline should not anchor a pricing view.

The most useful findings are the negative ones the note left out. Among labs that know AXELIOS, most say buying one would cut their Illumina use. About a quarter of familiar labs say they would buy one within two years.

## The issues, most serious first

### 1. "Research" means academic only, and spending is measured lab-wide across all vendors
- **The sample.** The 30 "research" respondents are 13 academic labs, 10 non-profit institutes and 7 core facilities (D69). There is no pharma, biotech or applied/industrial research, and no one from China or Asia-Pacific; the sample is North America and Europe only (D15).
- **The note relabels this group "research customers"** (N171, N211) and uses it to support research-segment views.
- **The spending questions cover the whole lab, all vendors.** "Approximately how much does your lab spend per year on total sequencing consumables (e.g., reagents, kits, flow cells, library prep consumables)?" (D120). Library prep and non-Illumina platforms are included, and respondents also run PromethION, Revio and others (D25).
- **Why it matters.** Illumina's research revenue equals the lab's sequencing spend × Illumina's share × Illumina's price. The survey measures only the first term, and only for academics.

### 2. The large clinical labs are missing
- **Sample size range.** The clinical sample runs from 250 to 8,000+ patient samples a month. Half process 250–999, and only about 9% (about 3 labs) process 5,000+ (D107). The labs are 14 hospital, 10 reference and 8 academic-medical-center labs (D86).
- **Mismatch with the thesis.** JPM's clinical thesis rests on large, high-growth CLIA labs (N33, N143). Labs such as Natera, Guardant, GeneDx and Tempus, which buy most of Illumina's clinical consumables, are not identifiable in the sample and could be 3 labs at most.
- **The volume gap shows this.** Surveyed clinical labs plan +14.6% volume in 2027 (D260). The note itself cites Illumina's clinical gigabase growth at 30% or more (N165).

### 3. The questions ask about intentions two years out, and instrument purchases are lumpy
- **What the growth figures are.** They are what respondents expect to spend in 2027 and 2028, not what they have spent.
- **Instrument history.** Only about 5% of respondents bought an Illumina instrument in 2025–26 year to date, and about 47% last bought one in 2022 or earlier (D189). JPM itself notes "academic acquisition declines as you approach 2025, likely reflecting slower and/or tightening academic budgets" (D191).
- **Instrument plans.** Yet academics plan +18.6% instrument spend in 2027 and +19.0% in 2028. A year-on-year percentage on an instrument budget that is often near zero is not meaningful, and stated intentions typically overshoot.

### 4. Reported instrument spend exceeds consumables spend, which points to a definition problem
- **The numbers.** Academic labs report about $516k a year on instruments and $428k on consumables (D124, D130). Clinical labs report $965k and $857k (D126, D132).
- **Why it is implausible.** At a typical sequencing lab consumables dwarf instruments, and Illumina's own revenue is mostly consumables. The instrument question includes "leases/rentals, and major instrument upgrades" (D120) and possibly other vendors.
- **Consequence.** The instrument growth rates (+18.6%, +19.0%, +22.2%, +31.0%) sit on a base that does not look right.

### 5. The sample is current customers only, and its quality cannot be checked
- **Survivorship bias.** "All respondents are current ILMN customers" (D50). Labs that have already moved work to Element, Ultima or a contract research organization (CRO) are excluded.
- **Missing methodology.** There is no recruitment source, incentive, screening, fieldwork dates or response rate. Earlier work dates the fieldwork to May 2026.
- **Many respondents don't own the instruments.** About half the respondents reach Illumina through a core or shared facility and do not own the instrument: 33 core access, 23 owned, 6 leased (D50). They are still asked about instrument spend and purchase intent.
- **Few budget holders.** Seniority is thin. The most common academic role is "scientist/researcher" (14), and only 8 of 30 academics are primary decision-makers (D69).
- **Generic open-ended comments.** Some read like panel filler ("the performance of the PLC", "real time sequencing output just like nanopore").

### 6. The survey's own price signal is too mild to be credible
- **What it implies.** Planned volume growth runs ahead of planned spend by 2.4 points for research in 2027 and 4.5 points in 2028, and by about 5 points for clinical. That implies only about 2–5% price decline (D256, D260; ledger E067).
- **What else we see.** Management's model implies a mid-teens decline. Q3 2026 revenue per gigabase fell about 19%. Core-lab 10B lane prices fell a median 11% in the latest cycle (`2026-10-17_10B_core_discounting_tracker.md`).
- **JPM contradicts itself here.** The note says the spread indicates "favorable pricing for the customers, albeit below the -DD% pricing pressure we've seen for ILMN" (N211), while elsewhere saying "pricing headwinds largely gone" (N165).
- **Measurement problems.** Spend is lab-wide and all-vendor, volume units are undefined, and answers are in buckets. This is not a price measure.

### 7. Two share answers contradict each other
- **Share is expected to rise.** Academic labs expect Illumina's share of their sequencing to rise in every size tier: 47% to 50%, 55% to 57%, and 71% to 72% (D212).
- **But many plan to cut Illumina use.** Of the 19 academics familiar with AXELIOS, 12 would "reduce utilization of Illumina" and 2 would decommission an Illumina instrument if they bought one (D338).
- **No cross-tab.** There is no breakdown that reconciles the two, which suggests respondents answered each question in isolation.
- **The tier gains are tiny samples.** They are 1–3 percentage points on cohorts of about 8–14 labs, and the clinical "+7%" is 7 points on about 13 labs. That is within noise.

### 8. The AXELIOS results are more negative than the note says
- **Who answered.** Only 37 of 62 respondents were familiar with AXELIOS (D298), so 40% were not.
- **Intent was split.** Among the 37, 35% rated purchase likelihood 7 or higher and 43% rated it 4 or lower (D298). The academic mean is 6.2, but the most common academic score was 3 (D294), a polarized split. The 6.2 versus 4.7 gap between academic and clinical respondents is probably not statistically significant at 18 and 19 respondents.
- **Most would cut Illumina use.** If they bought AXELIOS, 24 of 37 (65%) would reduce Illumina use and 4 more (11%) would decommission an instrument. That is 28 of 37, or 76%, cutting their Illumina footprint (D338). The note does not report this.
- **The note's "stickiness" quotes come from the wrong respondents.** They come from respondents who said they were not familiar with AXELIOS or were not evaluating it.
- **Timing.** The survey was fielded before Roche's commercial launch in late June 2026 and before any 35B flow-cell pricing. No AXELIOS price was shown to respondents, and Element, Ultima and other rivals were not tested.

### 9. Means are built from buckets on tiny samples, with no error bars
- **How the means are built.** Answers are bands such as "increase 26–50%", turned into averages with an undisclosed midpoint rule. "Don't know" answers are dropped.
- **How much one answer moves them.** With 30 academics, one respondent moving up a band shifts the mean by about 0.4 points, or about 1.9 points for a ">50%" answer.
- **Our rough 95% interval.** About ±4–6 points on the academic instrument averages. No margin of error is disclosed.

### 10. Numbers and labels in the deck don't reconcile
- **6000 ownership.** The summary page says 16% of respondents own a NovaSeq 6000 (D25). The chart text says 56% (35 of 62), including 75% of clinical labs (ledger E021 correction).
- **Respondent counts.** The AXELIOS impact slide uses 19 academic and 18 clinical respondents (D338). The likelihood slide uses 18 and 19.
- **Totals.** Several percentage sets sum to 95–101%.
- **Time horizon.** The note says share rises "over the next two years" (N33). The question asked about three years (D205).
- **Overstated headline.** The note says spending is "above" Illumina's high-single-digit target (N33). In fact 2027 consumables spend is +9.0% (academic) and +9.4% (clinical), at that target, not above it.

### 11. Conflicts of interest and timing
- **No caveats on the survey.** JPM gives no methodology section or margin of error. It does disclose an investment-banking relationship and a possible conflict of interest.
- **What the survey supported.** It underpinned an upgrade from Neutral to Overweight with the price target raised from $125 to $185. The upgrade came after the stock had risen about 26% since the 1 May close of $126.74, to $160.03 on 10 Jun.

## How JPM uses it, and how much it actually leans on it

JPM's research model (research sequencing consumables growing at a mid-single-digit compound annual rate from 2026 to 2030, N188) is well below the survey's +9% and +12.8%. So JPM does not apply the survey literally, but the note never says it is discounting it. The survey is the stated evidence for calling academic and government customers "the end market that has the most upside" (N171). The recovery mechanism in that claim, grant disbursements resetting, comes from outside the survey: it asked nothing about NIH or funding.

## What the survey credibly shows

- **Switching costs are real for small and mid-size labs.** The top barriers to AXELIOS are cost per sample, data quality and workflow (D35). Respondents stay mainly because of workflow lock-in and training.
- **Awareness of AXELIOS was only about 60% in May–June 2026.**
- **Clinical labs are more Illumina-centric than academics,** and Illumina's share rises with academic lab size (D212, D214).
- **Labs expect volume to grow faster than spend,** so they expect some price decline. Only the direction is meaningful, not the size.
- **The negative AXELIOS case is the most robust finding.** About a quarter of familiar labs say they would buy within two years. About three-quarters say buying would cut their Illumina use.

## How to use it

- **Do not cite +9% (2027) / +12.8% (2028) as research growth.** It is academic, lab-wide, all-vendor stated intent, from a sample with no pharma and no China.
- **Do not use the 2–5% implied price decline.** Use reported revenue per gigabase, core-lab rate cards and channel checks instead (`2026-11-09_ILMN_customer_channel_checks_discounting_quotes.md`).
- **Do cite the AXELIOS findings as a risk marker.** About 76% of familiar labs would cut their Illumina footprint if they bought one, and roughly a quarter of all respondents say they would buy within 24 months. The note omits this.
- **The survey is consistent with our more cautious research view** (about −2% for FY27, `2026-10-11_research_segment_price_exposure.md`). The positive survey numbers come from the problems above, not from evidence of a recovery.
