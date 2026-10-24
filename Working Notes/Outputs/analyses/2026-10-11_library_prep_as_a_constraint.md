# Is library prep a constraint, and how is it trending?

Prepared 11 Oct 2026. Sources: ILMN AGBT Feb 2025, Bernstein May 2025, Q4'25 call, JPM Jan 2026 and TD Cowen Mar 2026; Roche Investor Day 12 May 2026; PacBio and ONT calls and Barclays notes; 10x Q1'26 call; expert calls of Jul–Aug 2026 (Core Notes 07).

## Short answer

Library prep is a real cost and labour burden but not a hard limit on adoption. Sources name reimbursement, sample availability and data interpretation as the binding constraints. Prep matters more each year in relative terms, because sequencing keeps getting cheaper while prep costs stay "roughly flat". Its absolute burden is easing only where new products remove steps or labs automate. There is no evidence of a prep reagent shortage or capacity limit.

## By type of constraint

| Constraint | Binding? | Trend | Evidence |
|---|---|---|---|
| **Cost per sample** | Yes in RNA, single-cell and spatial work, where sequencing is only 10–20% of cost; no for clinical genomes | Worsening in relative terms | Illumina (AGBT 2025; TD Cowen 2026): halving the sequencing price yields "maybe 20% more" experiments because prep dominates. Expert (Jul 2026): sequencing was >90% of spend 20–25 years ago; prep and data costs have been "roughly flat"; genome prep is under $100 against ~$250 sequencing and $500–1,000 interpretation. Roche CEO (May 2026): costs "shift to library prep and sample collection." PacBio expert: ancillary costs are flat or rising. |
| **Labour and automation** | Yes, a real pain point | Improving, mainly via third-party robots | Experts: prep is "a major labor-cost and error bottleneck"; stitching together third-party machines is "a pain"; above ~100 samples a day automation is "significantly cheaper" than staff. Illumina has robot workflows for genome, exome and TSO, but none for TSO Comprehensive [expert]. Oxford Nanopore stopped its own prep-automation platform; PacBio is adding prep automation after clinical-lab requests. |
| **Turnaround** | Rarely | Stable | Prep plus sequencing takes 24–36 hours on Illumina; halving it saves ~12 hours; "not going to kill anyone" [experts]. It matters only for rapid newborn-ICU genomes. |
| **Sample input and quality** | Yes for specific uses | Improving, vendor by vendor | Roche AXELIOS's fast run needs 150 ng of DNA, "nearly impossible from a real patient" [Natera expert]. TruPath needs long DNA fragments, so preserved tumour tissue may fail. Ultima and PacBio cut input needs. 10x's Flex Apex handles preserved tissue. |
| **Complexity for new applications** | Yes | Improving through product launches | Spatial prep takes two days with expensive kits. Illumina's CEO calls Protein Prep "a little too complicated" for now. TruPath cuts genome hands-on time to ~10 minutes, against two days for PacBio prep (management claims). |
| **Reagent supply and capacity** | No evidence | n/a | Only pricing complaints: kit prices "go up exclusively" [expert]. |

## Why it matters for Illumina

1. **It caps how much volume a price cut can buy.** Prep now sets much of the total cost, so cheaper flow cells such as the 35B buy less volume than they used to. This weakens the "price elasticity" bull case, especially in research counting work.
2. **It defines Illumina's strategy.** Illumina has moved from selling "cost per gigabase" to "total cost of workflow". The goal is to capture prep spend (single-cell, Protein Prep and spatial kits) or remove it (TruPath, priced as "really just the cost of sequencing").
3. **It is a battleground with Roche.** Roche owns a large prep franchise (KAPA, general knowledge) and is betting on it as sequencing gets cheap. AXELIOS's high DNA-input requirement is a prep-side weakness.
4. **The binding clinical constraints lie elsewhere.** Reimbursement, samples ("sequenced everything in the freezer") and interpretation cost are the real limits. Fixing prep alone would not unlock much clinical volume.

## Gaps

- No time series of prep cost per sample.
- No Illumina prep revenue.
- Most figures are single-expert recollections or management claims.
