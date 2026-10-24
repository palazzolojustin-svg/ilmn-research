# AXELIOS's per-read price gap, and the research growth consensus implies

Prepared 11 Oct 2026. Sources: Roche Investor Day 12 May 2026 and H1 call 23 Jul 2026; JPM 26 Feb, 10 Jun and 17 Sep 2026; UBS 26 Feb 2026; Barclays 31 Jul and 2 Oct 2026; Illumina TD Cowen 3 Mar 2026; Bloomberg consensus 10 Oct 2026; primer working file 03; expert calls.

## 1. Is there a 10x gap per million reads?

Yes per read, less per base.
- **Roche:** AXELIOS in simplex mode lists $0.06 per million reads. A ~$2,400 run gives 40B reads averaging ~175 bases.
- **Illumina:** UBS puts its 25B flow cell at about $0.68 per million reads at list price. That is about 11x Roche.
- **Per base the gap is about 6–7x.** Illumina reads come in 2×150-base pairs, so the price per gigabase is roughly $0.34 for Roche against ~$2.27 for Illumina (our calculation).
- **Caveats.** Simplex accuracy is undisclosed and lower than duplex mode (Q38). Library prep takes about three days. The instrument costs ~$750K. No source gives what large Illumina customers actually pay per read.

**Why the gap matters most in research.** In "counting" applications (RNA-seq and single-cell), the unit is reads and accuracy matters less. That is where Roche's offer is strongest and research budgets are tightest.
- **Pool size is disputed.** UBS puts counting at about 40% of research usage, or ~16% of sequencing consumables (~$470M). Illumina's CEO puts it at "probably less than USD 100 million".
- **Illumina's counter-argument.** Sequencing is only 10–20% of a counting experiment's cost. Even a 6–7x cut lowers total experiment cost by only ~10–17% (our calculation). That matters for constrained labs but does not transform them. The exception is mega-scale atlas projects, where sequencing's share is higher; 10x credits Ultima and Roche for making those affordable.
- **Uptake so far.** Among academics familiar with AXELIOS, the JPM survey found purchase likelihood of 6.2/10, mostly 12–24 months out. Roche had placed about a third of ~100 first-year systems by September. One genome centre expects to buy "a couple".
- **No pricing response yet.** No Illumina price action has been disclosed for counting applications; the 35B in H1 2027 is the expected lever.
- **Exposure.** If Illumina must halve counting prices to defend, it loses ~$235M a year on UBS's sizing, or under $50M on the CEO's.

## 2. Consensus research consumables growth for the next eight quarters

**No consensus exists.** The Bloomberg printouts carry only total sequencing consumables. No broker in the folder publishes a quarterly clinical/research split.

The only segment numbers:
- **Company guidance:** FY26 research down mid to high single digits, which implies roughly −3% to −5% in H2'26.
- **JPM:** research +mid-single-digit CAGR for 2026–30; clinical +low to mid-teens.
- **JPM survey:** academic consumables spend +9% (2027) and +12.8% (2028).

**What consensus implies.** We backed out research growth from consensus sequencing consumables. Our method:
- remove China, at an estimated 76% of China revenue;
- use our derived clinical and research bases (Q3'25–Q2'26);
- assume a path for clinical growth.

| Quarter | Consensus seq. consumables y/y | Ex-China | Implied R&A if clinical ~13% (12% in 2028) | Implied R&A if clinical 15% |
|---|---|---|---|---|
| Q3'26 | +5.6% | +6.1% | −5% | −8% |
| Q4'26 | +7.9% | +8.8% | +2% | −1% |
| Q1'27 | +9.1% | +10.3% | +5% | +1% |
| Q2'27 | +8.3% | +9.4% | +3% | −1% |
| Q3'27 | +9.0% | +9.9% | +4% | 0% |
| Q4'27 | +9.0% | +9.7% | +4% | 0% |
| Q1'28 | +9.5% | +10.1% | +6% | −2% |
| Q2'28 | +10.0% | +10.6% | +8% | +1% |

**Reading it.** Consensus needs one of two things:
- clinical holds ~15% for two years while research is roughly flat; or
- clinical slows to ~13%, as the 2026 guide implies for H2'26, while research grows 3–8%.

Our view (research about −2%, clinical low teens) fits neither, which supports the below-consensus 2027–28 call.

Q4'26 includes the extra week, which flatters Q4'26 and makes the Q4'27 comparison harder. Consensus does not appear to adjust for it.

**Caveats.** All splits are derived: China's sequencing share is assumed and the clinical/research bases are backed out from growth rates (±2 points of share). Treat the implied figures as directional.
