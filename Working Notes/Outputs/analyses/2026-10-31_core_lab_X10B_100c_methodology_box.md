# Methodology box: NovaSeq X 10B 100-cycle core-lab pricing chart (2026-10-31)

Slide text, in the same format as the dicks.com methodology box:

**[1]** Pulled public sequencing rate cards from 28 academic core labs (US and Europe), live and archived (Wayback Machine), Oct-24 to Oct-26.
**[2]** Recorded the NovaSeq X 10B 100-cycle price at each core, for internal users and for external academic users.
**[3]** Converted each price to $ per Gb at Illumina's rated 10B output and took the monthly median across cores.
**[4]** **41 price series** (27 internal, 14 external) over **25 months**; about **190** dated price points, carried forward between updates.
**[5]** **6 price cuts** across internal and external rates from Jul to Oct-26 (6% to 30%), vs **5** in the prior 20 months combined. Like-for-like internal prices are now falling **~7%** a year, up from **~2%**: nearly **4x** faster.

*Full count of Jul–Oct 2026 price moves (both tables).* There are 8 downward moves:
- Duke int −28%.
- UIUC int −30% (Aug), later reversed by a +39% raise in Oct.
- Northwestern int −15%.
- Northwestern ext −12%.
- UC San Diego int −12%.
- UCLA int −6%.
- CNAG int −0.1% and CNAG ext −0.1%. Both are rounding/FX and excluded from the 6.

There are 4 increases: Case Western +8%, NCI +3%, Utrecht +9% and UIUC +39%. The short line segments that start inside the highlighted window are 8 cores entering the data (Weill Cornell Jul; U Florida Sep; Texas A&M, UCLA Broad Stem Cell, U Chicago, Penn and UC Berkeley Oct, several in both tables). They are not price cuts.

*Superseded version of [5]:* 5 price cuts across internal and external rates from Jul to Oct-26 (6% to 28%), as many as in the prior 20 months combined. This version excluded UIUC because it reversed.

*Earlier version of [5], superseded:* 4 cores cut internal prices from Jul to Oct-26 (6% to 28%), 3 of them in October, vs 3 cuts in the prior 20 months: about 4x the pace per core.

## Backup for [5] (not for the slide)

- **Cuts Jul–Oct 2026 (internal, sustained):**
  - UCLA, Jul: $9.34 to $8.74/Gb (−6%).
  - UC San Diego, Oct: $7.50 to $6.60 (−12%).
  - Northwestern, Oct: $13.89 to $11.75 (−15%).
  - Duke, Oct: $11.12 to $8.02 (−28%).
  - Northwestern also cut its external rate in Oct: $16.67 to $14.69 (−12%).
- **Excluded:**
  - UIUC cut 30% in Aug but raised above its old price in Oct.
  - CNAG's −0.1% in Aug is a rounding or FX artifact.
- **Cuts Nov 2024–Jun 2026 (internal):**
  - Utrecht, Dec-25: −25%.
  - U Kansas Medical Center, Mar-26: −43%.
  - Case Western, May-26: −21%.
- **Pace per core:**
  - Prior 20 months: 3 cuts over 261 core-months (1.1%).
  - Jul–Oct 2026: 4 cuts over 91 core-months (4.4%).
- **Cuts across internal and external rates combined:**
  - Jul–Oct 2026: 5, which are the four internal cuts above plus Northwestern's external cut.
  - Nov 2024–Jun 2026: 5, which are the three internal cuts plus two external: CNAG −11% (Aug-25) and U Kansas Medical Center −43% (Mar-26).
  - Per core-month, that is 1.4% before and 3.7% after, about 2.7x.
- **Like-for-like internal rate of decline:**
  - Each month, average the log price change across cores priced in both that month and the month before, then chain the months together.
  - Nov 2024–Jun 2026: −3.3% over 20 months, or −0.17% a month (about −2.0% a year).
  - Jul–Oct 2026: −2.5% over 4 months, or −0.63% a month (about −7.3% a year).
  - The rate of decline is about 3.7x faster.
  - External rates did not accelerate on this measure: −0.46% a month before vs −0.29% a month after.
- **Why the slide uses like-for-like prices rather than the headline median:**
  - The headline internal median fell 7.9% over the prior 20 months ($10.14 to $9.34) and then 14.1% in four months ($9.34 to $8.02), which looks like about 9x acceleration.
  - Most of the October move comes from 5 new cores entering the panel.
- **Why the earlier version cited cuts rather than the median:**
  - The internal median's drop to $8.02 in Oct-26 partly reflects 5 cores entering the panel that month (22 to 27).
  - On the same 20 cores priced in both Jun and Oct 2026, the median moved only $9.34 to $9.30.
  - The count of cuts is the cleaner signal.
- **Output basis:** $/Gb uses the 10B's rated 4,000 Gb (2x150) for all read lengths, so absolute 100-cycle levels are understated. Changes over time are unaffected.
- **Source:** `Outputs/datasets/2026-10-13_core_lab_price_per_gb.xlsx` (sheets `RL_X10B_int_100c`, `RL_X10B_ext_100c`); combined in `2026-10-31_core_lab_X10B_100c_int_vs_ext.xlsx`.
