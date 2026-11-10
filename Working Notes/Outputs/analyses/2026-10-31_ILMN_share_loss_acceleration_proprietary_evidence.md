# Is Illumina's share loss accelerating? What our proprietary research shows (2026-10-31)

*This note covers our own alternative-data work: public-repository counts (SRA, GEO, ENA), US federal obligations, core rate cards and queues, tenders, and expert calls. It draws on two agent sweeps plus my own pass over the core-lab dataset. The headline figures were re-checked against `datasets/2026-10-12_thesis_scrape_findings.csv` and the expert transcripts. All alt data is dated on or before 12 Oct 2026, so it predates Illumina's Q3 print, ASHG and Roche's Q3.*

## Bottom line

Share loss is measurable only in research, and it is small. Whether it is "accelerating" depends on the measure:

- **Global run counts (SRA):** yes, accelerating. MGI's DNBSEQ-T7 drives it, mostly China-linked.
- **US research deposits (GEO):** steady, at about 1.7 points a year.
- **Large high-throughput runs:** Western rivals (Element, Ultima, Roche) show no gain.

Clinical shows no measurable share loss. None of the nine largest US labs runs a non-Illumina platform in production.

The defensible pitch line: *"Rivals are taking a rising share of incremental research sequencing: about 23% of new global public runs in Q3'26, up from 9% a year earlier. US research share is slipping about 1.7 points a year. Illumina is defending with price, not losing clinical accounts."*

Avoid "share loss is accelerating" as a blanket claim. The data contradicts it for high-throughput and for clinical.

## Evidence that supports acceleration (strongest first)

1. **Rivals are capturing a rising share of new public runs (SRA).**
   - AVITI plus DNBSEQ-T7 went from **2.3% (Q3'24) to 3.6% (Q3'25) to 7.6% (Q3'26)** of five-platform run releases [F611, verified].
   - Rivals took **9.3%** of year-on-year run growth in Q3'25 and **23.5%** in Q3'26 [D056].
   - Caveat: this is mostly MGI. T7 runs went from 12,873 to 35,144 (+173%). On AVITI alone, the share of the increment fell from 8.3% to 6.0% [D056, F610]. These are run counts, not Gb.
2. **US research share is slipping steadily (GEO series).**
   - Rival share of US-tagged GEO series went from **3.8% to 5.5%** in a year (Q3'25 to Q3'26). Rival series rose +97% against +34% for NovaSeq [F954, verified].
   - Rivals took about 10% of the US increment, which is about **1.7 points a year** of US research share [D089].
3. **US federal buying is shifting.**
   - Rivals' share of direct federal sequencer obligations was 9.5% (FY24), 10.5% (FY25) and **16.8% (FY26)**. Illumina's own obligations fell **29%** in FY26 [F924].
   - Caveat: the base is small (about $29M) and the trend is not monotonic. FY23 was 15.7% on a one-off PacBio year.
4. **One major US core has converted almost entirely.**
   - The University of Minnesota core's Oct 2026 queue has **461 of 463 runs on AVITI or Ultima** and 2 on NovaSeq X Plus [F1100].
   - Its AVITI price per billion reads fell 32–41% (FY25), then **46–51%** (FY26) [F1063].
   - Caveat: the core outsources most X Plus work, so the queue understates its Illumina use.
5. **An expert at a second core says the trend is speeding up.**
   - Georgia academic core director (31 Jul 2026): of the volume his core has lost, Ultima's slice "started maybe two years ago at about 10%, but we are seeing the volume creep up to about 20%." Asked whether the pressure would accelerate or erode slowly, he answered: "**Accelerate.**"
   - Caveat: 80–90% of his lost volume goes to Novogene-type providers, which may themselves run Illumina machines.
6. **Element is scaling usage faster than boxes.** Its installed base grew more than 60% to over 450 AVITI in 2025, and kit shipments more than doubled [F098, JPM deck, Jan 2026].
7. **Illumina is defending harder.**
   - Thaysen (Q3'26): "very willing to also talk about what the right price point is" for large-volume deals.
   - Operating-lease and reagent-rental demand is rising.
   - Core-lab 10B prices were cut at 6 of 8 cores in Aug–Oct 2026.
   - These show pressure rising, not share lost.

## Evidence on the level only

- **Expert share paths.** A former Illumina product associate director, citing DeciBio, put share at "probably around 80% down now into the mid-60s" and "eroding at like three pps a year." He also said "That wasn't going to continue… around 50% is going to be a reasonable number to flatline at" (24 Jul 2026, L77 and L121). He left in Jul 2025, so the number is about 15 months old.
- **Rival price gaps at cores.**
  - Ultima is 2.0–2.7x cheaper than an Illumina 25B lane, but only 1.2–1.5x cheaper than a negotiated Illumina price of about $1.59/Gb.
  - AVITI is still 1.7–3x *more* expensive than the 25B per Gb at four cores.
- **Core-lab rate cards (my pass).** Element appears at 12 of about 70 cores and Ultima at 3. "First seen" dates cluster in Oct 2026 for Illumina flow cells too, because of the archive timing, so this dataset cannot date adoption. The one clean case is Minnesota: Illumina from Jul 2024, Element first seen Dec 2025, Ultima Oct 2026.
- **MGI.** Sequencer units rose from 1,260 to 1,470 (+17%) in 2025. It won 47% of Chinese government installs in 2023–24. In H1'26, instruments fell 6.4% while reagents rose 16% and overseas sales rose 34%.

## Evidence against acceleration

- **The GEO sample share is slowing.** Rival share of human and mouse high-throughput samples went from 0.75% to 3.9% (+3.2 points) and then to only 4.5% (+0.5 points) [F582].
- **Large runs show no Western-rival gain.**
  - Element runs of 10 Gb or more: 440 (Q3'25) vs 462 (Q3'26), which is 0.58% of NovaSeq [F649].
  - Rival large-run share is "almost entirely MGI" [D061].
  - AXELIOS is not yet visible in public data.
- **Clinical.**
  - 0 of 9 big US labs (Natera, Guardant, Tempus, Caris, GeneDx, Foundation, Labcorp, Quest, Myriad) run a non-Illumina platform in production [E353].
  - A JPM survey has mid-size clinical labs expecting Illumina's share of their work to *rise* from 50% to 57%.
  - Revalidation costs $100–200K per test, and a switch is a "four- or five-year project."
- **Research decline is shrinking, not growing.** Illumina's ex-China research and applied consumables fell −12%, −7% and −6% in Q1–Q3'26. Management blames funding and the 6000-to-X price step.
- **Management.** Thaysen (Q3'26): "I'm not super concerned about what others are doing right now." X placements beat the 50–60 a quarter framework in every quarter of 2026.

## Gaps and staleness

- No share time series exists for Ultima (private) or Roche. Element data is annual only.
- No Illumina share or win-rate disclosure exists since 2024.
- None of this data covers Q3 prints, ASHG, Roche Q3 sales, or AXELIOS and VITARI shipments after about 12 Oct.
- MGI's H1'26 primary report is still undecoded.

## Sources

- `datasets/2026-10-12_thesis_scrape_findings.csv`: F098, F582, F583, F610, F611, F649, F924, F954, F1063, F1100; D056, D061, D089.
- `analyses/2026-10-12_thesis_scrape_addendum.md` and Core Notes 18.
- The clinical scrape ledger (E353, E118, E116) and files 100_105, 102 and 14.
- `analyses/2026-10-14_expert_quotes_ilmn_share_loss.md`.
- Expert transcripts: the Georgia core of 31 Jul 2026 (L117, L219, L361) and the ex-Illumina associate director of 24 Jul 2026 (L77, L121).
- The core-lab dataset (`datasets/2026-10-13_core_lab_price_per_gb.xlsx`, Long_data).
