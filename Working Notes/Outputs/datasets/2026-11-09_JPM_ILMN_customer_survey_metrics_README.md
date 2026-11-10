# JPM ILMN customer survey: every metric (dataset)

**File:** `2026-11-09_JPM_ILMN_customer_survey_metrics.csv` (308 rows, UTF-8)

**What it is.** Every number in J.P. Morgan's "ILMN Customer Survey: Insights into Market Views of Axelios 1" (June 2026). The survey covers 62 current Illumina customers, 30 academic and 32 clinical, in North America (about 65%) and Europe. The upgrade note of 10 Jun 2026 added only the volume-minus-spend spreads.

**Source.** `Sources/ILMN/research/20260615_JP_Morgan_ILMN_Illumina-_Inc.md` (the deck) and `20260615_JP_Morgan_ILMN_Illumina-_Inc.-_Upgrading_to_Overweight_on_a_Sticky_Clin.md` (cited with an "N" prefix). A Sonnet agent extracted the figures on 9 Nov 2026, and the headline numbers were checked against the deck.

**Columns**

| Column | Meaning |
|---|---|
| section | Topic: Respondent profile, Lab size, Spend, Installed base, Acquisition timing, Applications, ILMN share, Spend outlook 2027-28, Axelios 1 awareness & intent, Axelios 1 impact, Reagent rental, Barriers |
| question | The survey question, shortened where long |
| segment | All, Academic, Clinical, or a size tier |
| metric | What is measured |
| value | The number, without a % sign |
| unit | %, count, $k, $M, score/10, pts, etc. |
| base_n | The respondent base, where stated or inferable |
| source_line | Line in the deck, or N + line in the upgrade note |
| notes | Flags for OCR-garbled, inferred, derived or conflicting values |

**Caveats**

- **The deck is OCR of slides.** Unreadable chart values were left out, not guessed. Some splits by group were inferred so that they add up to the stated totals; each is flagged in `notes`.
- **Known conflicts in the deck:**
  - NovaSeq 6000 ownership is 16% in the summary page but 56% in the chart (35 of 62). The 16% looks like a typo.
  - The academic and clinical bases appear swapped (19/18 against 18/19) on the Axelios-impact slide.
  - The labels for immunology and metagenomics appear swapped between two slides.
- **Survey quality.** Read with `Outputs/analyses/2026-11-09_ILMN_JPM_customer_survey_issues.md`. The figures are lab-wide, all-vendor stated intentions, not Illumina revenue.
