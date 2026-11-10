# Is the NovaSeq 6000 residual cohort mostly smaller-volume labs? What the alternative data says

*2026-10-31. Sources: the Oct-12 thesis scrape (`analyses/2026-10-12_thesis_scrape_addendum.md` and `datasets/2026-10-12_thesis_scrape_findings.csv`, IDs in brackets); the Oct-11 clinical scrape (`analyses/2026-10-11_clinical_consumables_scrape/`, ledger E-numbers); `analyses/2026-10-12_6000_vs_X_ratio_widening_decomposition.md`; the 23 expert calls; the JPM customer survey (10 Jun 2026).*

## Answer

No dataset in the corpus measures it directly. Nothing breaks the remaining 6000 base down by lab size or by flow-cell type, and Illumina has stopped disclosing the installed base.

The indirect alternative data leans *against* "largely small labs", at least when you weight by gigabases (Gb), the unit that drives revenue:
- **What contradicts it:** the named labs still tied to the 6000 are big ones, public run data shows the remaining 6000 output is still mostly large samples, and the one alt-data argument for the small-lab view (the 3.4x price premium) mostly falls apart under our own decomposition.
- **What supports it:** price cards for small flow cells, and a handful of low-use boxes at government labs.

The fair reading is that the tail may be mostly small labs *by count* but mostly large labs keeping validated tests on the 6000 *by volume*. That is also what management said in Q3: certain clinical customers are "keeping current on-market assays on the 6000 while adding X capacity for new tests" (Dhingra, Q3'26 call).

## Evidence that supports the small-lab thesis

All of this is inference. None of it directly identifies who owns the remaining 6000s.

- **Small flow cells are very expensive per Gb.**
  - At university sequencing cores, the 6000's small flow cells cost far more per Gb than the X's big 25B flow cell: the S2 3.6–4.7x and the SP 6–9.8x, against 2.3–3.1x for the large S4 (Salk, Jul 2025; Pitt, Jun 2025) [D028, D032].
  - If the remaining base leaned toward small flow cells, that could explain why 6000 revenue per Gb runs about 3.4x the X's.
  - But no source shows what flow cells the remaining base actually uses.
- **Some boxes are barely used.**
  - Taiwan's national health research institute paid about $110K a year per box in service on four 6000s but bought only about $24K a box in consumables. The fleet average is about $670K. It let the service contract lapse in Dec 2024 [D078].
  - NIEHS bought small v1.5 kits sole-source and moved to a cheaper service plan [F1000, F620].
  - These are real low-volume 6000 users, but they are research and government sites, not clinical.
- **A small European hospital order.** Bambino Gesù in Rome ordered 12 S1/S2/S4 flow cells, about €130K a year, roughly the output of two 25B flow cells [F830]. The scrape's reviewer judged it too small to generalize from.
- **Experts on the economics.**
  - A small Australian clinical lab director said small labs avoid the X because you "must be able to fill flow cells or it is a costly idle machine" (LifeStrands, 25 Jul 2026).
  - An ex-Illumina scientist said small labs must "wait for a full batch" (23 Jul 2026).
  - This explains why small labs *don't buy an X*. It doesn't show that they are sitting on 6000s.

## Evidence that contradicts it, or points to large labs

- **Public run data.**
  - In the European and US public sequencing archives, about 74% of remaining 6000 Gb (Q3 2026) still sits in samples of 10 Gb or more, so the tail is not shrinking to a small-run rump [D059].
  - Small runs dominate by *count* (72% of 6000 runs are under 3 Gb), but sub-1 Gb runs are only about 4% of 6000 Gb [F630, D059].
  - Caveat: this data is research-heavy and lags by up to two years, and clinical labs don't deposit.
- **FDA records name large labs' flagship tests on the 6000.**
  - Caris's MI Cancer Seek (PMA approved Nov 2024) names the 6000, and none of its 10 later supplements names a new sequencer.
  - Foundation Medicine only moved FoundationOne CDx from HiSeq to the 6000 in April 2024.
  - No FDA-approved test names the X (openFDA, through Sep 2026) [E296, E287].
- **The Genetic Testing Registry (GTR).**
  - 104 of the 130 records naming the 6000 belong to Mayo Clinic Laboratories, none of them on the X [F123].
  - Others include Tempus xT, UCSF500 and JAX Genome [F962, F971, F996].
  - Labcorp filed a whole-genome MRD test on the 6000Dx in Dec 2025, 13 months after moving its NIPT to the X [F970]. MRD means minimal residual disease, a blood test for leftover cancer.
  - These are large labs. Mayo's records are mostly low-volume single-gene and panel tests, so this fits "large lab, small assays", not "small lab". The registry is self-reported and stale.
- **Large sites run both platforms.**
  - A former Illumina field scientist's main account ran 21 NovaSeq 6000s alongside 15 X Plus at about 4,000 genomes a week (expert call, 24 Jul 2026).
  - Job postings at Tempus and Natera list both platforms [E022, E166].
  - Genomics England extended a £4.67M WGS contract on the 6000 [E100].
  - Aachen University Hospital awarded 6000 maintenance in Mar 2026.
- **The JPM survey points to dual running, not small holdouts.**
  - About 75% of the 32 clinical respondents own a 6000 and 53% own an X, so a large share own both.
  - Small clinical labs are the *most* Illumina-loyal (63% of their sequencing today and in three years).
  - Caveats: the survey's "small" tier starts at 250 samples a month, so it has no truly tiny labs. It doesn't cut 6000 ownership by size. The note's 6000-ownership figures don't reconcile with each other (16%, 56% and 75% appear in different places).
- **The price-premium argument weakens.**
  - Our own decomposition looks at the ratio widening from 2.8x to 3.4x (Q2'25 to Q2'26). At realistic Gb growth (35–40%), it finds that 80–100% of that widening comes from X revenue per Gb *falling* (big accounts moving onto the 25B at negotiated prices), with 6000 revenue per Gb roughly flat. The answer depends on Gb growth: at the disclosed 30% floor, the 6000 side rises about 7.6% (about 40% of the widening). That would support the small-lab thesis.
  - Core-lab S4-to-25B ratios are mostly 1.6–2.5x, well below 3.4x [D022, D025].
  - So the premium can't be read as proof of a small-flow-cell tail.
- **Small labs mostly aren't 6000 owners anyway.**
  - Experts say labs too small to batch use the NextSeq or MiSeq (PacBio lead, 3 Aug; ex-Illumina scientist, 5 Aug).
  - They also outsource, or move to Ultima or Element on price (Natera associate director, 22 Jul; Georgia core director, 31 Jul).
  - High-volume research sellers have already left the 6000: Novogene ended 6000 support in Jun 2025, and Dana-Farber, Rush and Northwestern retired theirs.

## What management has said

Management has described both groups.

At Wolfe (Nov 2025), Thaysen gave four clinical cohorts:
- Low-volume labs that "never convert", which he called "a smaller cohort… volume-wise".
- Price-driven movers such as NIPT labs.
- Labs keeping old tests on the 6000 while putting new ones on the X, which he called one of the "absolutely the largest" segments.
- Labs moving from exomes to genomes.

So management's own map puts most of the volume in the large-lab, dual-running group.

## Why the distinction matters

The two readings imply different things for 2027:
- **Mostly large labs with validated tests:** the tail converts slowly and in lumps. Each move is a revalidation project, and experts cite 1–5 years and, for a regulated product, up to "$200 million of clinical trials". When a lab does move, it is a big price step on a lot of Gb, and Illumina keeps the volume.
- **Mostly small labs:** the dollars at stake per lab are small. Many of those labs may not convert to the X at all; they may drop to NextSeq, outsource, or leave for Ultima or Element. That means volume leaving Illumina rather than repricing.

## What would actually test it

These sources are not in the corpus:
- The JPM survey's underlying data, cut by lab size.
- Natera, Guardant and Caris 10-K sequencer counts.
- New York State's CLEP lab approvals, which list each test and its platform.
- The amended Element v. Illumina antitrust complaint (N.D. Cal. 5:25-cv-08026), which may name customers.
- An expert call specifically with a mid-size US clinical lab still on the 6000.
