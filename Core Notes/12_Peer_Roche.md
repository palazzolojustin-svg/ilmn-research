# Peer: Roche (sequencing and diagnostics)

*Core Notes section 12. Synthesized from 5 source extracts as of 2026-10-10. Bracketed tags cite the source; full detail is in Working Notes (see INDEX.md).*

## Why Roche matters to Illumina

Roche is the world's largest in vitro diagnostics (IVD) company. IVD means tests run on samples such as blood or tissue outside the body. Until mid-2026 Roche did not sell DNA sequencers. That changed on 29 June 2026, when it launched AXELIOS 1, a next-generation sequencing (NGS) instrument. NGS means reading millions or billions of DNA fragments in parallel, which is Illumina's core business. AXELIOS 1 uses a new chemistry Roche calls sequencing by expansion (SBX).

Roche is therefore a direct new entrant in Illumina's market. It brings a large diagnostics sales force, a presence in more than 100 countries, an owned cancer-testing lab (Foundation Medicine), and a stated ambition of more than $1 billion in sequencing sales. This section covers the technology, launch, pricing and early traction first. It then covers the diagnostics division's results and outlook, and finally what sell-side analysts (bank research analysts writing for investors) say.

On naming: Roche writes "AXELIOS" ("AXELIOS 1" for the launched model), J.P. Morgan writes "Axelios 1", and Barclays' September 2026 note writes "ALEXIOS", apparently a typo for the same product.

## Sequencing strategy: SBX and AXELIOS

### Origins and timeline

SBX came from Roche's 2020 acquisition of Stratos Genomics [H1 2026 call, 2026-07-23]. Group CEO Thomas Schinecker said Roche's work with NVIDIA, begun in 2016, started partly because the sequencer needed chips able to handle a data flow of "three high-definition movies per second," which will rise further and which no earlier chip could cope with [Roche DX Day, 2026-05-12].

Roche unveiled SBX at the AGBT conference (Advances in Genome Biology and Technology, the main annual sequencing-technology meeting) in February 2025 [Roche DX Day; H1 2026 call]. Pre-launch early-access sites included the Hartwig Medical Foundation in Europe, Broad Clinical Labs in the US and Foundation Medicine. In April 2026 Roche hosted a few hundred prospective US and European customers. Palani Kumaresan (Head of Roche Diagnostic Solutions) reported "tremendously positive feedback" on speed, throughput, accuracy, flexibility and the $0.06 per million reads price [Roche DX Day].

At the London Diagnostics Investor Day on 12 May 2026, Roche said the global launch would come in summer 2026. Head of IR Bruno Eschli called its "special focus" the "upcoming global launch of our truly transformative next-generation DNA sequencing technology" [Roche DX Day]. Schinecker attended, although he now alternates years between Pharma Day and Diagnostics Day, specifically because of the sequencing launch and the PathAI deal. AXELIOS 1 launched on 29 June 2026 [H1 2026 call].

Schinecker framed the launch as a promise kept. In May he said that when asked for years about timing, "I always said we are going to launch, and we will have a very competitive solution" [Roche DX Day]. In July he said, "I've always promised that we will deliver, and we did deliver on the sequencing with really a differentiated product" [H1 2026 call].

### How SBX works

Most NGS today, including Illumina's, uses sequencing by synthesis (SBS), in which a DNA copy is built one base at a time and each step is imaged. Matthew Sause, CEO of Roche Diagnostics, called SBX "truly differentiated chemistry… a move away from sequencing by synthesis to sequencing by expansion" [Roche DX Day].

Josh Lauer (Molecular Labs) described three parts of the system [Roche DX Day]:

1. **Synthesis instrument.** This converts each DNA molecule into an "Xpandomer," a stretched-out surrogate molecule. Lauer said this improves the signal-to-noise ratio, making single-molecule sequencing at scale possible.
2. **Sequencing instrument.** This passes Xpandomers through an 8-million-well, reusable CMOS sensor array (CMOS is the chip technology used in camera sensors), producing very high data rates.
3. **Analysis module.** A high-performance computing stack processes reads in real time, so analysis is almost complete when the run ends, with no waiting for flow cycles to finish each read.

Lauer added several operating points [Roche DX Day]:

- **Flexible loading.** Customers can load one to four sample pools per run, so "mid-throughput users can actually access the same economics as high throughput users."
- **Familiar library prep.** Library preparation (the lab steps that ready DNA for the sequencer) is similar to existing methods and has been automated on Roche, Beckman and Hamilton liquid-handling robots.
- **Sensor reuse.** The sensor module can be reused up to 20 times.
- **Low carryover.** Carryover (leftover material contaminating the next run) is lower than in traditional systems, because Xpandomers are more delicate than DNA and wash out easily.

### Run modes and performance

AXELIOS has two run modes: SBX-Duplex, which emphasizes accuracy, and SBX-Simplex, which emphasizes raw read count. Sause said together they offer "flexibility, speed and scalability that is unprecedented" and "differentiated cost effectiveness" [H1 2026 call]. The table below lines up how the figures were described in May and July. Some terms first: a **terabase** is a trillion DNA letters; a **Q score** measures sequencing quality (Q30 is one error in 1,000 bases, Q38 roughly one in 6,000); **isoforms** are alternative versions of a gene's RNA message; **structural variants** are large DNA rearrangements.

| Metric | May 2026 [Roche DX Day, Lauer] | July 2026 [H1 2026 call, Sause] |
|---|---|---|
| Duplex output | "Roughly a couple of terabases" per run | 1.8 terabases in 4 hours of sequencing |
| Duplex genomes per run | Always 16 or more | About 16 whole human genomes |
| Duplex accuracy | Q38 or higher | Q38 (about 99.98% accuracy) |
| Duplex insert length | Longer than the traditional 150 base pairs | Not stated |
| Simplex reads | Over 40 billion short reads in 4 hours (over 10 billion an hour) | 40 billion reads averaging 175 base pairs in 4 hours |
| Simplex long reads | 500 to 1,000 base pairs, still over 10 billion reads in 4 hours | Up to 1,500 bases, enabling isoform and structural-variant detection |

The main change between the dates is the long-read ceiling, which rose from about 1,000 to 1,500 bases; the Duplex figure was also made more precise at 1.8 terabases.

Lauer said the AGBT statistics were what Roche expected at launch, that with Simplex "the sequencing world has never seen output like this," and that a new technology matching or beating incumbents on accuracy, cost and performance "out of the gate" is "a rare thing." Customers keep stressing "speed, speed, speed" [Roche DX Day]. He gave two examples:

- **Throughput.** A fully loaded instrument with four queued runs produces 64 genomes in under two days, whereas traditional technologies need "significantly more than 2 days" of on-board sequencing time alone.
- **Rapid diagnosis.** In a world-record neonatal intensive care (NICU) run with an amplification-free workflow, Roche went from sample to a finished variant file (VCF, the standard list of genetic differences found) in under four hours. The Broad Institute and Boston Children's Hospital showed same-day results.

**Target enrichment.** Target enrichment means pulling out only selected genes before sequencing, as in cancer panels. After AGBT, analysts asked how this works on SBX, because Roche had shown only Simplex data using UMIs (unique molecular identifiers, molecular barcodes that let several reads of one molecule be stacked into a consensus). Lauer said SBX errors are largely random, so stacking reads pushes accuracy beyond Q38; Roche has shown Q50 and does not yet know the ceiling. Enrichment also works in Duplex mode through a traditional workflow with PCR steps at the end that extend at a hairpin to make a Duplex construct, suited to applications where two reads per molecule are enough [Roche DX Day].

### Pricing

Roche disclosed list prices at the May Investor Day [Lauer, Roche DX Day]:

- **Whole genome: $150 per human genome**, with "no volume-based discounting. Everyone can achieve this pricing." Lauer called this competitive with high-throughput platforms and "way more than competitive" for lower-throughput labs, which normally pay much more per genome.
- **Simplex reads: $0.06 per million reads**, which Lauer called "multiples lower than the nearest competing technology."
- **Liquid biopsy panels** (cancer tests on DNA shed into the blood): about $25 per sample for a common 1.1-megabase panel (1.1 million DNA letters) at normal clinical depth, "multiples lower than what you can achieve with other technologies."

These are Roche's claims; no source document contains independent price checks.

### Applications, ecosystem and openness

Lauer called AXELIOS Roche's "first-gen RUO platform." RUO means research use only, not yet cleared for diagnosing patients. Demonstrated uses [Roche DX Day]:

- **Core applications:** germline sequencing (inherited DNA) and oncology, with high accuracy.
- **Sample types:** fresh-frozen and FFPE tissue (formalin-fixed, paraffin-embedded, the standard way hospitals preserve biopsies).
- **MRD testing,** shown by Foundation Medicine. MRD (minimal residual disease) testing looks for trace cancer DNA after treatment.
- **Research long tail:** single-cell sequencing, Perturb-seq CRISPR screens (gene-editing experiments read out by sequencing), spatial biology, proteomics (protein measurement, via collaborations with Olink, Pixelgen and Alamar) and novel isoform detection.

Roche calls AXELIOS an open platform. It has data with Watchmaker and other vendors and a partnership with 10x Genomics, and will engage the wider NGS ecosystem. Kumaresan said Roche will introduce many workflows itself and support customers building more. Long term, Roche wants a clinical platform with end-to-end workflows, automation and library prep, used for multi-omics beyond DNA. Lauer said Roche "intend[s] to invest in the next 20 years of improvements on SBX": scaling up and down, longer reads, better accuracy and more sensor reuse [Roche DX Day].

**Clinical evidence so far.** Foundation Medicine presented data at AACR 2026 (the American Association for Cancer Research meeting) showing AXELIOS detected more MRD-positive cases than a competing technology and did better in earlier-stage disease [Lauer, Roche DX Day]. Freenome is evaluating AXELIOS for its multi-cancer early detection (MCED) platform, a blood test screening for many cancers at once. Sause said adoption into Freenome's workflow depends on the evaluation's outcome [Roche DX Day].

### Launch targets, traction and the $1 billion ambition

**Ambition.** Asked about market share in May, Sause gave no number, saying AXELIOS would be "an accelerant" and capture "significant market share," differentiated by technology, applications and channel (for example selling through Foundation Medicine). Schinecker called it a "blockbuster potential" product, defined as "[$1 billion] plus," with no timeline; Sause echoed "Blockbuster" [Roche DX Day]. Schinecker groups sequencing with mass spectrometry and continuous glucose monitoring as three launches that could each be $1 billion-plus and "even for Pharma terms, [each] would be a blockbuster" [H1 2026 call; JPM CEO call, 2026-09-08], adding he knew of no other diagnostics company that had launched three such instruments so quickly [Roche DX Day]. Sause reaffirmed the "more than CHF 1bn" ambition in late September [Barclays, 2026-09-28]; management said dollars, Barclays reported francs.

**Year-one target and progress.** In May, Sause said a successful first year would be "ideally… 100 of these systems in the first year, thereabouts," with first orders already arriving from around the world [Roche DX Day, answering TD Cowen]. In September the two updates used different measures:

- Schinecker said roughly one-third of the approximately 100 first-year placements (instruments installed at customers) had been made, all with external customers and with no "teaser offers," meaning discounted come-on deals [JPM CEO call, 2026-09-08].
- Barclays reported Roche "progressing well" in the first 60 days against its "initial order target of 100 systems in 12 months" [Barclays, 2026-09-28].

Barclays frames the 100 as orders, J.P. Morgan as placements. On either reading, the pace is ahead of a straight-line one-twelfth per month.

**Demand and recurring revenue.** Schinecker cited positive early feedback and expects reagent revenue (consumable kits bought for every run, usually the most profitable part of a sequencing business) to build as customers migrate assays onto AXELIOS [JPM CEO call]. Sause said early demand comes from clinical labs and academic centers, supported by long reads, clinical accuracy and economics. Roche will present more data at ASHG (the American Society of Human Genetics meeting, autumn 2026) and wants progress to be "data-driven" [Barclays, 2026-09-28].

**Customers.** Lauer expects academic centers to drive early momentum. Community oncology practices, which often want to bring testing in-house for reimbursement reasons, could be served by "a capable, economic solution"; centralized and decentralized models will coexist [Roche DX Day, answering Jefferies].

**Profitability.** Asked by Canaccord, Lauer said there is no reason sequencing "can't be massively profitable," even at blockbuster scale. Molecular diagnostics are high-margin, and Roche has "every technical entitlement to be just as cost efficient, if not more" than public sequencing peers. As per-genome costs fall, cost shifts to library prep and sample collection. Kumaresan added this assumes continued R&D investment [Roche DX Day].

### Market sizing

In May, Roche put the sequencing market at CHF 7 billion growing about 7% a year, versus the PCR molecular market at CHF 9 billion, with the molecular lab overall growing 4% [Roche DX Day]. In July, Sause cited an NGS market of about USD 7.3 billion (assessed in 2025), growing as clinical applications become routine, and said Roche is entering "very ambitiously" [H1 2026 call]. The two figures are roughly consistent allowing for currency.

### Sequencing within Roche's oncology ecosystem

Roche argues AXELIOS will not be sold as a standalone box. It sits inside an end-to-end cancer-testing portfolio that Sause said lets Roche "shape the future of the Oncology testing market in a way that no other company can" [Roche DX Day]:

- **AXELIOS** for molecular oncology, "the core of that backbone" for oncology and translational research [Sause, answering Kepler].
- **Foundation Medicine (FMI)** for comprehensive genomic profiling (CGP, a large-panel tumor DNA test that guides therapy choice).
- **SAGA Diagnostics** for ultrasensitive MRD: a pending "definitive merger agreement" in May, described as acquired by July.
- **Freenome partnership** for early cancer detection.
- **VENTANA tissue staining plus PathAI** digital pathology.
- **Digital LightCycler**, Roche's digital PCR system for low-cost repeat monitoring.

**How SAGA uses AXELIOS.** A patient's tumor is sequenced on AXELIOS to find its mutations; the patient is then monitored with tumor-specific primers on Roche's cost-effective digital PCR. Schinecker said Roche is "extremely well positioned here to really scale this on a global level, much better than some of the other players," pointedly referring to other MRD companies' market capitalizations [H1 2026 call]. Sause said MRD "is going to be one of the biggest drivers of the diagnostics industry" [Roche DX Day].

**Foundation Medicine as a channel.** FMI CEO Dan Malarek said FMI, an AXELIOS early-access site, expects shorter turnaround and a lower cost base, plans to move its installation-and-services partner sites onto AXELIOS later, and expects it to enhance FMI's biopharma services [Roche DX Day]. This matters for Illumina because FMI is a large-volume clinical sequencing customer. FMI facts [Roche DX Day]:

- Founded in 2010 out of the Broad Institute; first to launch a CGP test; more than 1.5 million CGPs delivered.
- More than 40% of US oncologists ordered from FMI in the last 12 months.
- More than 100 approved companion diagnostics (tests required to select patients for a specific drug), "more than the entire rest of the industry combined."
- Works with the top 80 biopharma companies and supports more than 300 active trials.

The FMI and SAGA product plan around AXELIOS:

- **Pathlight MRD** (SAGA) detected breast cancer recurrence more than 13 months before CT/PET imaging in early-stage disease. It has Medicare coverage for stage II and III breast cancer across all subtypes, over 6 years and 12 time points. AXELIOS would provide a whole-genome tissue baseline and Digital LightCycler the monitoring.
- **SAGA pipeline:** breast and colorectal launched, ovarian studies underway, lung next; Malarek would say no more before closing.
- **F1 Monitor:** a blood-only test for metastatic patients that detects progression with roughly half the lead time of CT/PET and reports resistance mutations.
- **Flexomics platform:** extends FMI into neurodegenerative, metabolic and autoimmune disease.

Malarek's market and quality points [Roche DX Day]:

- **Adoption gap.** One large community oncology network treating about 20% of US cancer patients gets CGP for only about 50% of metastatic patients; Malarek says it should exceed 90%.
- **Market growth.** He expects oncology testing across biopharma, therapy selection and monitoring to "essentially double over the next 5 years," driven by new drug types (bispecifics, antibody-drug conjugates, molecular glues), CGP adoption and monitoring. About 50 million people live with cancer, nearly double 10 years ago.
- **Quality.** MTAP loss, present in about 10% of cancers, is a biomarker for MAT2A and PRMT5 inhibitor trials. In a Sarah Cannon Research Institute study of three labs, FMI detected it at published rates while the others found 40% to 60% less. FMI is the enrollment assay for 15 MTAP trials. FoundationOne CDx is the only FDA-approved tissue NGS test validated to detect a copy-number loss (PTEN).
- **Delivery models.** Centralized testing runs in US and German labs, with samples from more than 50 countries. Roche Diagnostics sells FMI outside the US and Chugai in Japan. Installation-and-services sites include the UK (where FMI won 50% of the NHS liquid-biopsy tender), Gustave Roussy in Paris and University Hospital Zurich. FMI also sells decentralized AVENIO kits.
- **Software.** VENTANA staining and navify Clinical Hub (trial matching, dynamic NCCN guidelines, AI patient education) are being built into the FMI ordering portal.

**Differentiation and regulatory debate.** Asked by Guggenheim, Malarek said clinicians and pharma still see FMI as best-in-class, and FMI gains scale through Roche, especially outside the US. Asked by JPMorgan about an FDA advisory committee (ODAC) that rejected earlier molecular testing over imaging-based progression for lack of data, he called it "a setback in a specific case, but not a setback overall," arguing pharma needs surrogate endpoints (early measures that stand in for survival) that ultrasensitive MRD can supply. Sause closed by saying MRD-enabled surrogate endpoints will enable trials "that cannot run today," benefiting Diagnostics and Pharma [Roche DX Day].

**Oncology testing market sizes to 2030** [Roche DX Day]:

- **Early detection (MCED):** 35% compound annual growth rate (CAGR, average yearly growth) to CHF 5.3 billion. Sause later said the 35% is global, "early days," and potentially higher.
- **Therapy selection:** CHF 17 billion, growing 9%, covering companion diagnostics, digital pathology and CGP.
- **Monitoring:** growing 32% to CHF 5 billion, driven by MRD.

## PathAI and digital pathology

Roche announced a definitive merger agreement to acquire PathAI, a Boston AI-pathology company, around 8 May 2026; Eschli said it was announced "just last Friday" before the 12 May event, subject to regulatory approval [Roche DX Day]. The July call referred to the agreement being signed "earlier in July 2026" [H1 2026 call]. The sources disagree; the May transcript is more contemporaneous.

**Rationale.** Schinecker said cancer cases and diagnostic complexity are rising while pathologist numbers fall [Roche DX Day]. Sause called PathAI "wholly complementary to our Ventana business," giving earlier engagement with pharma on companion diagnostics [H1 2026 call]. Moritz Hartmann (Roche Information Solutions) said Roche will pair its scanners and algorithms with a next-generation AI-centric image management system, build on companion-diagnostic algorithm partnerships, and offer AI services to biopharma for trial efficiency and biomarker discovery [Roche DX Day].

**PathAI's view.** CEO Andrew Beck said PathAI was founded 10 years ago with "one foot in biopharma and one in diagnostics." Only a minority of pathology is digital today; he expects it to be routine and AI-assisted by about 2035, with AI companion diagnostics accompanying most new drug approvals [Roche DX Day].

**Products** [Roche DX Day]: PathExplore and IHC Explore for translational research; PathAssist Derm (FDA breakthrough device designation, Q1 2026); AIM-MASH AI-Assist, the first AI algorithm qualified by both the EMA and FDA for MASH liver-disease trials (2025); and AISight Dx image management, which gained CE-IVDR and FDA clearance in 2025 as the first such system with a predetermined change control plan. PathAI has partnered with Roche since 2024, including an AI companion-diagnostic deal with VENTANA.

**Case study.** Beck cited Genentech work at AACR 2023. Deep learning on standard slides from the OAK lung cancer trial found a "CP1" signature (more lymphocytes and plasma cells, fewer fibroblasts) predicting the best response to anti-PD-L1 immunotherapy, even in patients negative on the standard PD-L1 test. In the held-out IMpower150 dataset, the hazard ratio was 0.56 in PD-L1-negative patients versus about 0.7 in the broader evaluable population (below 1 means lower risk of death or progression). Beck framed this as a way to widen immunotherapy eligibility.

Asked by Citi about PathAI's third-party pharma contracts, Beck said PathAI has operated independently and expects the Roche combination to increase the value it offers those partners [Roche DX Day].

## Diagnostics division: strategy, results and outlook

### Strategy and market position

Sause said the strategy has been unchanged for six years [Roche DX Day]. Its three pillars are high-medical-value tests, clinical decision-support tools, and combining the two into solutions across the patient journey. Its four goals are to expand leadership in the clinical lab, lead in decentralized testing, differentiate in the highest-burden disease areas, and help patients navigate the oncology and neurology "continuum."

Roche claims more than 50% of FDA diagnostics approvals over six years without spending more than half the industry's R&D, and 31 billion tests delivered, 3 to 4 per person on Earth [Schinecker, Roche DX Day]. It has more than 48,000 Elecsys immunoassay instruments installed and a direct presence in more than 150 countries [Gillieron, Roche DX Day]. Sause said the IVD market grows a little above 3%, so mid-to-high single-digit growth is up to double the market, and about 5% is at least 66% above it [Roche DX Day].

**Customer areas.** The table shows Roche's four customer areas with the market sizes and growth rates it presented in May. Sequencing is the fastest-growing of the large lab markets; Core Lab is the biggest but slowest.

| Area | Market size / growth (May 2026) | Roche position |
|---|---|---|
| Core Lab (routine chemistry, immunoassays, mass spec) | CHF 40 billion; growing 3% | No. 1; largest unit |
| Molecular Lab: PCR | CHF 9 billion; molecular lab growing 4% | No. 1 in lab molecular diagnostics |
| Molecular Lab: sequencing | CHF 7 billion; growing 7% | New entrant via AXELIOS |
| Pathology Lab | Growing 8% | No. 1 in precision oncology diagnostics |
| Near Patient Care | Growing 3% (CGM within it growing 14%) | Diabetes management largest segment |

Roche cut its Core Lab five-year growth assumption from 4% a year earlier to 3%, blaming China, probably the second-largest immunoassay market, where reimbursement cuts and healthcare reform have shrunk the market [Sause, Roche DX Day, answering Citi].

**Disease burden and other 2030 opportunities.** Roche's focus areas account for about 60% of global health burden; it projects mortality increases to 2040 of 50% in oncology, 67% in neurology, 40% in cardiometabolic and 29% in infectious disease. Other 2030 markets cited [Roche DX Day]:

- **Neurology:** early detection CHF 480 million; therapy selection growing 17%.
- **Cardiometabolic:** early detection CHF 6.9 billion; acute cardiovascular diagnosis CHF 4.2 billion.
- **Infectious disease:** diagnosis CHF 25 billion; viral-load monitoring CHF 1.6 billion, a market Roche says it "shaped and built… over several decades."

Instrument placements across the three lab areas grew double digits in 2025, and Roche plans more than 140 new tests [Roche DX Day].

### First-half 2026 results

H1 2026 Diagnostics sales were CHF 6.7 billion, up 3% at constant exchange rates (CER, growth with currency effects removed), or CHF 228 million [H1 2026 call]. Excluding China's pricing reform, growth was 6%; a weak Northern Hemisphere respiratory season cost a further CHF 50 million. Pharma and the group each grew 6% at CER. By region: North America +8%, EMEA +3%, Latin America +10%, Asia-Pacific −5% (China −15%, Asia-Pacific ex-China +6%).

The table below shows growth by customer area: Pathology was strongest, Near Patient Care weakest, and Core Lab would have grown 8% without China.

| Customer area | H1 2026 growth (CER) | Drivers |
|---|---|---|
| Core Lab | +4% (+8% ex-China effect) | China policy drag |
| Molecular Lab | +3% | Transplant testing +18%, offset by mild respiratory season |
| Near Patient Care | −5% | Lower cobas Liat sales; blood glucose monitoring +3% on competitive wins |
| Pathology Lab | +11% | Advanced staining +7%, companion diagnostics +24% |

In May, Kumaresan and Laura Apitz (Pathology Lab) said Pathology Lab had grown 14%, presumably in 2025, with more than 13,000 installed systems [Roche DX Day].

**Profit and costs.** Diagnostics core operating profit ("core" excludes one-off and non-cash items) was CHF 1.2 billion, up 6% at CER, helped by CHF 126 million of extraordinary patent-licensing income [H1 2026 call]. The core margin rose 0.6 percentage points at CER, aided by CHF 24 million from centralizing SG&A costs (selling, general and administrative) such as legal under corporate. Cost of sales rose 5% on China reform, the manufacturing ramp for launches, more installed instruments and about CHF 43 million of US tariffs. R&D rose 3% (AXELIOS and the i601 mass spectrometer) and SG&A 3% (distribution volume and launch investment). Volume grew 5%.

### Outlook: growth, margins and China

**Growth.** The long-term ambition is mid-to-high single-digit sales growth, outgrowing the market, with core operating profit growing faster than sales [Sause and Schinecker, Roche DX Day]. For 2026 the ambition is mid-single-digit growth with a smaller China impact, and for 2027 a return to mid-to-high single digits [H1 2026 call]. Schinecker repeated his confidence in mid-to-high single digits from the base business plus launches in September [JPM CEO call, 2026-09-08].

**Margins.** The 2026 Diagnostics core margin is meant to be "broadly stable" at CER versus 14.4% in 2025, absorbing China and tariffs, with a negative currency effect noted [H1 2026 call]. In May, after BNP's Peter Verdult noted peers citing about 100 basis points of oil impact with oil above $100, Sause said all headwinds were built in, and that an operational-improvement program begun in 2025 creates P&L room to fund launches [Roche DX Day]. Barclays heard the same stable-FY26 message, supported by efficiency programs [Barclays, 2026-09-28]. The longer-term target is notably higher: Schinecker said Diagnostics should return to "at least 20%" over time, after two years of significant China price cuts [JPM CEO call, 2026-09-08].

**China timing has slipped slightly.** In May, Sause said China should stabilize "next year" and return to growth after that, and only then would Roche consider raising its ambition [Roche DX Day, answering UBS]. By late September he told Barclays the reforms will still weigh in FY27, with a return to single-digit growth in FY28; Roche's in-market China volume is already growing, pricing headwinds are manageable and in guidance, and Roche has no plan to shrink its China presence [Barclays, 2026-09-28]. The July target of mid-to-high single-digit division growth in 2027 implies the rest of the business offsets China. Outside China, underlying market growth is low-to-mid single digits, and Roche says it keeps outperforming competitors despite a weak respiratory season [Barclays, 2026-09-28].

**Acquisitions.** Sause expects "significant tailwind" from acquisitions and launches, but said Roche's size as the largest IVD company limits its room for inorganic growth [Roche DX Day, answering Wolfe].

**US reimbursement.** PAMA (the Protecting Access to Medicare Act, which sets Medicare lab-test prices) drew questions. In May, Sause said Roche lobbies through ACLA and AdvaMed, including for the RESULTS Act; the year-end outcome is impossible to call, but even non-extension would not be "really material" to Roche [Roche DX Day]. After CMS proposed PAMA cuts on 21 September 2026, Barclays said it believes Roche is insulated because it sells to labs, which are the ones Medicare reimburses; that is Barclays' view, not management's [Barclays, 2026-09-28].

**Launch progress.** By mid-2026 Roche had achieved 7 of its 11 key Diagnostics launches for the year [H1 2026 call].

### Other launches (non-sequencing)

**Mass spectrometry (cobas i 601).** Mass spectrometry identifies molecules by their mass [Roche DX Day].

- It addresses a CHF 3 billion segment that is largely manual and based on laboratory-developed tests. Roche launched a fully automated IVD version a little over a year before May 2026, with placements in Asia, Europe and North America, including LabCorp; some customers have issued press releases.
- The menu has 39 assays in CE-mark countries, with 4 more in 2026. In the US, the instrument plus vitamin D and six steroid tests are approved for CLIA labs (labs certified under US federal quality rules); the rest go through 510(k) FDA clearance from late 2026 into 2027, with drugs of abuse next.
- Roche targets an installed base of 100 instruments by end-2026, still held in September as a "stretch target," with strong interest from large reference labs despite longer-than-expected validation cycles [Barclays, 2026-09-28].

**Continuous glucose monitoring (Accu-Chek SmartGuide).** CGM is a wearable sensor that tracks blood sugar continuously [Roche DX Day, Amann-Zalan and Sause].

- It is AI-powered, with Glucose Predict and Night Low Predict algorithms. Controlled launch now covers 45 markets, up from 4 to 5 at the previous update. Roche has 11 automated manufacturing facilities, and its mySugr app (more than 7 million downloads) is built in.
- Roche aims for approval of factory calibration (removing the initial finger-prick) in H2 2026 and a pediatric claim. A next-generation patch will have a smaller inserter, a different battery and fewer manufacturing steps.
- Roche wants to upgrade its 30 million blood-glucose-meter users (11 million on insulin, 20 million not). Sause said CGM can revive a franchise whose meter business declined for years.

**Alzheimer's blood test (Elecsys pTau217).** This received a CE mark on 12 May 2026 as the first blood-based rule-in/rule-out Alzheimer's test intended for primary care [Roche DX Day; H1 2026 call].

- It uses two cutoffs, with sensitivity and specificity all above 93%. In primary care, NPV (the chance a negative is truly negative) is 98.6% and PPV is close to 80%; fewer than 20% of patients land in the intermediate zone [Gillieron, Roche DX Day].
- In Alzheimer's, 75% of patients are undiagnosed, diagnosis takes about 3 to 3.5 years, and 98% are untreated; Roche expects the market to quadruple in 10 years. Schinecker claims a "significant head start versus our other major competitors," especially combined with Roche's drug trontinemab [H1 2026 call].
- No one offers an annual screening test for people without symptoms; Kumaresan called it "a pretty tough problem" [Roche DX Day]. The NfL test for multiple sclerosis progression got a CE mark in Q1 2026, and the Alzheimer's portfolio has seven solutions, including pTau181 and ApoE4.

**Tuberculosis test (Elecsys IGRA TB).** IGRA (interferon-gamma release assay) is a blood test for latent TB. It received a CE mark in July 2026 after validation in close to 2,000 patients, with 91.1% positive and 94.6% negative agreement versus standard of care, and runs up to 400 samples an hour on four e 801 modules. About 30 million IGRA tests are run annually; Gillieron sees a market above CHF 1 billion by 2034 [Roche DX Day]. US trials are progressing [Kumaresan, Roche DX Day], but in September Sause gave no US timing, conceding that without a gold-standard reference Roche cannot prove superiority and is generating more data; tender-driven European contracts are slow to validate [Barclays, 2026-09-28].

**Point-of-care PCR (Liat).** Roche says it has "around one thousand" Liat systems installed this year, with new placements largely additive and no meaningful competitive impact so far. Flu demand stayed weak; declining vaccination and rising Flu-A activity can signal a severe season, but its size is hard to predict [Barclays, 2026-09-28].

**Other instruments and assays** [Roche DX Day]:

- **cobas smart e:** low-volume immunoanalyzer for a CHF 1 billion market growing about 5%, succeeding the e 411 (more than 18,000 installed), with CE launch planned for late 2026.
- **cobas ultra lab automation:** controlled launch in 2026, with omni transport with Hitachi to follow. A next-generation staining platform is also being developed with Hitachi.
- **cobas sense:** benchtop immunoanalyzer launching in 2027 with high-sensitivity troponin T, 0.995 correlation to the lab assay.
- **cobas pulse:** more than 24,000 placements, US launch later in 2026.
- **LumiraDx:** portable point-of-care platform, available in more than 43 countries and approved in more than 75.
- **Blood screening:** the MPX-E multiplex assay adds hepatitis E, for a CHF 1.8 billion donor-screening market. The first fully automated hepatitis D RNA test is coming.
- **HPV genotyping:** a 14-high-risk-type test plus a self-collection kit, planned next year.
- **TROP2:** set to be Roche's first computational-pathology companion diagnostic, launching in lung cancer in 2027.

### Digital

Hartmann said Roche has turned its analyzer base into the "largest connected digital software footprint globally" and plans an AI-native lab operating system in three phases: by end-2026, AI on operational data such as demand forecasting and quality-control anomaly detection; then lab clinical intelligence, adding lab results to a trained large language model; and finally a "precision engine" adding selected electronic medical record data [Roche DX Day].

## Group context (where it bears on Diagnostics)

Diagnostics is about 25% of Roche's sales and Pharma about 75% [UBS, 2026-09-14]; group performance shapes how much Diagnostics can invest.

**H1 2026.** Group sales grew 6% at CER, core operating profit 10% and core EPS (earnings per share) 9% [H1 2026 call]. In Swiss francs sales fell 2% on an 8-point currency headwind. A weak flu season cost about 1% of group sales (more than CHF 200 million). Roche confirmed 2026 guidance of mid-single-digit sales growth, high-single-digit core EPS growth and a higher dividend, and cut its expected 2026 loss-of-exclusivity (LOE, sales lost when patents expire and copies arrive) hit to about CHF 600 million.

**Pipeline and productivity.** Schinecker says pipeline value is up versus end-2022, by 63% (May) and then 93% (July); up to 19 new medicines could launch by 2030, and the marketed Pharma portfolio will keep growing with no near-term patent cliff [Roche DX Day; H1 2026 call; JPM CEO call]. Pharma margins are guided "at least stable," and Roche says it has "significant firepower" for M&A [JPM CEO call]. About CHF 1 to 1.3 billion of R&D has been reallocated, and Flatiron, which lost about EUR/CHF 250 million a year three years ago, turned profitable in Q1 2026 [Roche DX Day; H1 2026 call]. AI is embedded in all large-molecule drug discovery; Roche claims the highest compute power in pharma and is a founding member of the SAIL Foundation with companies including Anthropic, Microsoft and IBM [Roche DX Day].

**Pharma catalysts analysts track:** giredestrant breast-cancer FDA decisions on 30 November 2026 (lidERA) and 18 December 2026 (evERA); the fenebrutinib MS filing; full data for the competing remibrutinib at MSToronto, 21–23 October 2026; the obesity drug enicepatide (CT-388), which Roche calls best-in-class; and Pharma Day on 28 September 2026.

## What analysts say

**Questions at the May Investor Day.** Analysts focused on how acquisitions change the growth and margin model (UBS), AXELIOS share and year-one placements (BNP Paribas, TD Cowen), sequencing profitability (Canaccord), and SAGA and Freenome integration (Jefferies). Management gave no share target, offered "about 100" first-year systems, and asserted sequencing can be "massively profitable" [Roche DX Day].

**J.P. Morgan (Neutral).** Neutral means J.P. Morgan expects performance in line with its coverage [JPM, 2026-09-15]. The share price was CHF 361.10 on 14 September 2026; the last published target is CHF 325 (12 March 2026). J.P. Morgan was Underweight from October 2023 to July 2025, moving to Neutral at a CHF 350 target on 8 December 2025. The note relays Schinecker's points without its own estimates or valuation: roughly one-third of about 100 first-year placements, no teaser pricing, reagent revenue building as assays migrate, and the "at least 20%" Diagnostics margin goal. J.P. Morgan is a market maker in Roche and has banking ties to the company.

**UBS (Buy).** UBS rates Roche Buy with a CHF 376 target, unchanged since 27 April 2026, versus CHF 344.20 on 11 September 2026 [UBS, 2026-09-14]. That implies a 12.2% forecast total return (9.2% price gain plus 2.9% dividend yield), 6.9% above UBS's 5.2% market assumption. UBS values Roche on a multiple of 2026–27 EPS, cross-checked with a product-by-product net present value. The table shows UBS's EPS forecasts sit below consensus (the average of analysts' forecasts) in every year.

| Year | UBS EPS (CHF) | Consensus EPS (CHF) |
|---|---|---|
| 2026E | 19.61 | 20.43 |
| 2027E | 20.77 | 21.97 |
| 2028E | 21.93 | 23.66 |

UBS forecasts group revenue rising from CHF 61.5 billion in 2025 to CHF 72.2 billion in 2030, the operating margin from 35.5% to 40.5%, and net debt of CHF 16.2 billion turning into net cash by 2028. Its takeaways were mostly pharma: Roche says it can sustain mid-single-digit growth to 2030 without new Phase 3 readouts, and is confident in about CHF 500 million of 2027 giredestrant sales. For diagnostics, UBS lists "Diagnostics sales growth ahead of expectations on new technology launches (NGS, CGM, mass spec)" as an upside risk.

**Barclays (Overweight).** Barclays reiterated Overweight with a CHF 430 target versus CHF 363.40 on 24 September 2026, implying 18.3% upside [Barclays, 2026-09-28]. The target rose from CHF 260 in October 2023 through CHF 390 and 410 in January 2026 to CHF 430 on 7 September 2026. It is set at 18 times 2028 core EPS, about a 34% premium to the roughly 14x sector multiple, justified by faster 2028–2032 EPS growth (5.1% a year versus a 4.0% sector median), limited LOE exposure, and Diagnostics' durability, since it "isn't subject to LOEs in the same way a Pharma business is." The Overweight case also cites giredestrant and margin expansion.

Barclays calls the near-term Diagnostics outlook "balanced": AXELIOS and mass spec look strong but early, there is little visibility on the US TB launch, China weighs until 2028, and flu is weak. Longer term it expects NGS and mass spec to become "large, differentiated revenue drivers," and Roche to become the preferred development partner for labs and pharma through its end-to-end oncology offering of Digital LightCycler, AXELIOS, SAGA, PathAI and Elecsys.

**What this means for Illumina.** None of the analyst notes quantifies AXELIOS revenue or discusses Illumina directly. The open questions are whether early placements convert into reagent pull-through, how the $150 genome and $0.06 per million reads prices hold up against incumbents, and whether clinical demand, especially through FMI and SAGA's MRD workflow, materializes as Roche claims. ASHG data in autumn 2026 is the next disclosed checkpoint.
