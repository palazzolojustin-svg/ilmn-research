# Is Natera Illumina's only big MRD customer? Total MRD volume vs Natera

*17 Oct 2026. Sources: one corpus agent (thesis-scrape findings CSV, clinical-consumables scrape files 09, 10, 12, 13, 125, 129, 135, 138 and 143; Core Notes 07 and 16) and one web agent (Q2 2026 releases and calls). The Gb sizing is our own estimate.*

## Answer

Natera is most of the MRD market by test count, not one lab among five. In Q2 2026 Natera ran about 283K clinical MRD tests. Every other lab with disclosed volume adds about 55K a quarter:
- Adaptive clonoSEQ: 36K, in blood cancers.
- Personalis NeXT Personal: 10K.
- Tempus: 9K, which may overlap with Personalis.

Labs that don't disclose volume (Guardant Reveal, Quest Haystack, Labcorp Plasma Detect, NeoGenomics RaDaR and newer launches) probably add tens of thousands more. That puts Natera at roughly **65–85% of US MRD tests**, and total MRD at about **1.2–1.5x Natera**, not 5x. The only explicit share estimate found is old: Evercore ISI put Signatera at about 80% of MRD, around 2021–22.

In Gb (sequencing output), the non-Natera share is larger than its test share. Several newer competitors design each patient's test from a whole genome of the tumor and normal tissue, about 200+ Gb per new patient, against about 8–15 Gb for classic Signatera's exome.

## Volume table (Q2 2026 unless noted)

| Lab / assay | Latest volume | Growth | Notes |
|---|---|---|---|
| Natera Signatera (incl. a little Latitude) | ~283K clinical MRD units | +56% y/y | Illumina; includes some non-US volume |
| Adaptive clonoSEQ | 36,111 | +43% y/y | Blood-cancer MRD; moving to NovaSeq X Plus |
| Personalis NeXT Personal | 10,384 | +199% y/y | Whole-genome-designed; FY26 guide 43–45K; being acquired by Tempus |
| Tempus MRD (xM) | ~9,000 | +38% q/q | May overlap with Personalis |
| Guardant Reveal | Not disclosed | ">100%" y/y | Inside ~104K Guardant oncology tests; rough guess 15–30K |
| Quest Haystack, Labcorp Plasma Detect, NeoGenomics RaDaR, Myriad Precise MRD, Veracyte TrueMRD, Exact/Abbott Oncodetect, FoundationOne Tracker | Not disclosed | n/a | Several are recent launches; several are whole-genome-designed |

## Gb sizing (rough estimates; Illumina high-throughput base ≈ 800M Gb a year)

- **Natera:**
  - Blood draws: about 1.13M a year × 0.16–0.24 Gb = 0.2–0.3M Gb.
  - One-time tumor and normal sequencing per new patient: about 8–15 Gb for the exome version, about 200+ Gb for the Signatera Genome version.
  - Total: roughly **3–11M Gb a year (~0.4–1.4%)**. This hinges on new-patient counts and the Genome mix, neither of which is disclosed.
- **Personalis and other whole-genome-designed MRD:** each new patient uses about 200+ Gb. Personalis alone (about 40K+ tests a year) is plausibly **1–3M Gb**.
- **clonoSEQ:** about 0.03–0.14M Gb.
- **Guardant Reveal and the rest:** not sizeable from public data.
- **All MRD together:** roughly **1–3% of Illumina's high-throughput Gb**. Growing about 50% a year, that adds about 0.5–1.5 points to Illumina's total Gb growth.

## What it means for the thesis

- **1C holds across all labs, not only Natera.** Even counting every MRD lab, MRD is too small to keep Illumina's volume growth at 25–30% as NIPT matures.
- **The real upside lever is the shift to whole-genome-designed MRD.** It multiplies Gb at onboarding about 10–20x. Five of the newer launches use it.
- **That high-Gb work is exactly where Ultima competes.**
  - Labcorp has an Ultima collaboration.
  - Myriad, Quest and NeoGenomics are exploring Ultima.
  - OICR prices cell-free whole-genome work on Ultima about 74% below Illumina per unit of depth.

  So the upside may not reach Illumina at full price, which supports 1B.

## Caveats

- "Tests" are defined differently across companies, and Natera's count includes some Latitude and non-US volume.
- Several non-Natera figures come from search summaries.
- No published total US MRD test count or recent sell-side share estimate was found.
- Per-test Gb figures are estimates; no vendor publishes them.
- One corpus file uses "~800M Gb a quarter" for Illumina's base. "A year" fits Illumina's roughly $2B of high-throughput consumables revenue at about $2.5/Gb, so this note uses "a year".
