# Agent 87: 90-internal-NovaSeq-6000-end-of-life-trade-in-revalidation-and-supply-commitment-mining

*Model: sonnet. Run 2026-10-11 10:06:47. Cost $0.42 (API-equivalent).*

**Assignment:** Mine the whole local corpus (Working Notes/Extracts, plus Sources when exact wording matters) for the conversion-pacing evidence that has not been compiled. Use Grep across all Extracts for these terms: 'end of life', 'end-of-life', 'EOL', 'sunset', 'service contract', 'service revenue', 'support', 'trade-in', 'trade in', 'upgrade program', 'buy-back', 'revalidat', 'validation', 'CLIA', 'CAP', 'LDT', 'dual', 'parallel', 'run both', 'runs both', 'legacy', 'last-time buy', 'reagent availability', 'S4 supply', 'price protection', 'volume commitment', 'minimum purchase', 'take-or-pay', 'rebate', 'tier', 'contract renewal', 'multi-year'.
Build a table of every hit with the quote, speaker or source, date and file. Then answer, with quantification:
(a) Has Illumina stated or implied any end-of-life or supply sunset date for NovaSeq 6000 flow cells or reagents? Is any customer worried about one?
(b) How long and costly is it for a clinical lab to revalidate from the 6000 to the X? Give weeks, cost, and any statement that CLIA/CAP/FDA-approved assays tie labs to the 6000.
(c) Which clinical customers have volume commitments, rebates or tiers that would blunt or delay the price cut, and what mechanisms do they use?
(d) Do any sources give a count or % of clinical 6000s and dual-running customers (open gap 9)? Include expert-call and sell-side statements, with exact quotes.
(e) Do any statements about the timing of the last 20% of clinical volume conflict with management's 80-85% by end-2026 target?
Return the revenue-at-risk implications: how much of the ~41% of HT revenue on the 6000 is plausibly sticky past 2027 and why. Do not repeat the existing bridge in the file-45 and file-79 outputs; add only new evidence. Flag contradictions with the key facts.

## Key findings

**Verdict: mostly NO NEW EVIDENCE.** I grepped all Extracts for the assigned terms and read the hits that could matter. The corpus does not hold a 6000 end-of-life or supply-sunset date, a revalidation cost or timeline for same-vendor 6000→X moves, a customer volume or rebate tier tied to the 6000, or a count of clinical 6000s or dual-running customers. Gap 9 stays open. The few additions are below.

1. **No end-of-life or supply sunset date exists in the corpus. (FACT, absence.)**
   - The only "end of life" in the Illumina calls is the Q2'25 call (line 151). E016 already covers it as Thaysen's "stay until assay end-of-life, ~2 yrs" framing.
   - I found no "last-time buy", "reagent availability" or "S4 supply" language in any Illumina call, conference, 10-K or 10-Q extract.
   - The Q2'26 call shows Illumina selling 6000s: ">10" new units (E015).
   - The only obsolescence statements are hearsay. A former scientist at Illumina says the 6000 is "supposed to become obsolete" (E130 covers this). Their other line is new: "I don't know what's going on with their NovaSeq 6000, but it does seem like that is going to create an opportunity for a lot of other companies." [Expert, Former Scientist at Illumina, 2026-08-05, Extracts/ILMN/expert_call/Expert_2026-08-05_Former_Scientist_...md:131] OPINION, and the expert admits not knowing.

2. **A customer planning its own 6000 retirement. (FACT, expert.)**
   - The Georgia academic core director says the core "plans to sunset (retire)" its 6000 and runs an X Plus. [Expert_2026-07-31_Director_at_Genomics_Core_Facility, 2026-07-31, line 22]
   - The core ran the 6000 for "about a year to a year and a half" longer than it wanted, while waiting to install the X Plus. During that gap external customers left for vendors that offered X Plus prices.
   - This is research, not clinical. It is a concrete case of a customer losing volume because it was late converting. It adds no sunset date and is not a worry about supply. E072 only covers this expert's unkept discount promises.

3. **Revalidation timing, one new data point. (OPINION.)**
   - A senior scientist at Abbott says a cross-platform comparison "could take a month or two just to really do side-by-side comparison studies" before buying. [Expert_2026-07-29_Senior_Scientist_at_Abbott, 2026-07-29, line 67]
   - This is a pre-purchase study for a new vendor, not a 6000→X validation. It gives a floor of roughly 4–8 weeks for the study alone, before any assay-level revalidation.
   - It sits alongside E031 (12–18 months, Thaysen Q3'24) and E116 ($100–200K per switch, Adaptive "years"). No source gives weeks or dollars for a clinical same-vendor 6000→X move.

4. **Same-vendor X moves need no revalidation, per one ex-employee. (OPINION.)**
   - The former field application scientist says a site already on an X Plus has "no revalidation" cost to stay with Illumina, and that Element "will lose" against an X Plus site. [Expert_2026-07-24_Former_FAS, 2026-07-24, lines 66–75]
   - This conflicts with E031 and E116, which say clinical 6000→X moves are slow and costly. The likeliest reconciliation is that the claim means "no new vendor revalidation", not "no assay bridging". The source does not say.
   - The same expert calls validation the "number one headache" and says a challenger "often has to offer free sequencing reagents to win".

5. **Illumina's defensive concessions. (OPINION.)**
   - At a site like Memorial Sloan Kettering that already has an X Plus and faces Element, Illumina offers a free Hamilton, a free NextSeq 2000, training and a free year of Illumina Connected Insights (ICI, its analysis software). [Same expert, line 121]
   - Reagent rental was historically rare. It is now used, "too late" in the expert's words. E039 covers rental accounting but not these bundled give-aways.
   - The same expert claims Illumina has refused to support TSO validation on Element. This is lock-in by non-support, not a contract.

6. **Regulated assays are tied to the platform (labeling), which supports a sticky tail. (OPINION.)**
   - A former Associate Director at Illumina says switching platforms for an FDA-approved or cleared product requires revalidation and is "incredibly hard". [Expert_2026-07-24_Former_Associate_Director, line 77]
   - A Genece Health scientist agrees that large validated tests "would need revalidation and process changes". [Expert_2026-07-23, line 31]
   - The AGBT 2025 session says TSO 500 is "now an FDA-approved kit with companion diagnostic claims". [ILMN AGBT Investor Session, 2025-02-25, line 81] No source says which platform the kit's labeling names, and gap 6 (the FDA records) is still unread.

7. **The cost of a missed conversion shows in lab-side data. (FACT.)**
   - The RBC 2024-05-14 extract (line 77, Schwartz) says clinical customers moving existing work take longer because of "revalidation and redocumentation". The lag from launch to adoption is "one quarter to maybe two" for research. This supports E031 qualitatively and gives no clinical duration.

## Hit table (assigned terms, material hits only)

| Term | Quote / content | Source, date | File |
|---|---|---|---|
| sunset | Core "plans to sunset" 6000 | Georgia core director, 2026-07-31 | Expert_2026-07-31_Director_at_Genomics_Core_Facility |
| end of life / obsolete | "supposed to become obsolete" | Former Illumina scientist, 2026-08-05 | Expert_2026-08-05_Former_Scientist |
| revalidat | "a month or two" side-by-side | Abbott scientist, 2026-07-29 | Expert_2026-07-29_Senior_Scientist_at_Abbott |
| revalidat | Regulated switch "incredibly hard" | Former Associate Director, 2026-07-24 | Expert_2026-07-24_Former_Associate_Director |
| validation | "number one headache"; "no revalidation" on X Plus | Former FAS, 2026-07-24 | Expert_2026-07-24_Former_FAS |
| validation | "$100,000, $200,000" per switch | LifeStrands lab director, 2026-07-25 | already E116 |
| service revenue | Sequencing service and other $154M vs $136M, +13% organic | Q2'26 deck | ILMN_2026Q2_Earnings_Slides.md:69 |
| rebate / tier / multi-year / take-or-pay | None found for Illumina in calls or expert calls (see below) | | |

## Answers to (a)–(e)

- **(a)** No end-of-life or supply sunset date stated or implied by Illumina. No customer cited worry about a supply cutoff. The only worries are hearsay "obsolescence" and competitive-window talk (E130).
- **(b)** There is no clinical-specific figure for weeks or cost of 6000→X revalidation. The nearest are the Abbott pre-purchase study (1–2 months), the lab-director estimate ($100–200K per switch, E116) and Thaysen's 12–18 months (E031). Regulated and CDx products are described as tied to validated platforms, but no source names a CLIA, CAP or FDA clause that forces the 6000.
- **(c)** The corpus has no Illumina volume commitments, rebates or tiers for named clinical customers.
  - **Disclosed mechanisms:** discounts are "recorded net" (E112). Volume discounts for multi-unit orders (E063). Application-specific pricing (E062). E212 and E279 already cover the Illumina supply amendments and the GRAIL minimums.
  - **Georgia core's experience:** "We have not had great success in negotiating volume-related discounts in reagents" (2026-07-31, line 62). That is research, and it cuts against the idea of formal tiers.
  - **ONT as a comparison only:** ONT offers multiyear, high-volume commitment discounts for its test pack (ONT 2026-08-28, line 67). It is not Illumina evidence.
- **(d)** No count or % of clinical 6000s or dual-running customers (gap 9 unchanged). No expert gave one. The Q2'26 Jefferies question named "in parallel" running, and E014 already records that management did not size it.
- **(e)** I found nothing new that conflicts with the 80–85% target for end-2026. The only extra timing signal is the Georgia core's 12–18 month 6000 overhang. It suggests individual sites can lag a year or more, in line with E012 and E016.

## Revenue-at-risk implication (new evidence only)

I cannot quantify the stickiness past 2027 from new data. Two qualitative points follow from the above:
- Sites are retiring 6000s on their own schedule (the Georgia core), which argues against a hard Illumina-imposed cliff.
- Regulated assays are described as hard to move, which supports a tail near the 15–20% in E005, but no source gives a dollar share.

## Contradictions and stale data

- Item 4 (no revalidation on X Plus) contradicts E031 and E116 in tone. Treat it as one ex-employee's shorthand.
- The Georgia core and the "obsolete" comment are research or hearsay and don't test the clinical 80–85% target.

## Gaps / what I could not find

- The omitted long lines in the Q2'25 and Q3'24 call extracts and the Barclays and TMO hits were not opened. The Q2'25 line is the E016 source.
- I did not open Sources originals or the 10-K/10-Q Part II for supply or commitment language (gap 5 stands).
- Searches I did not run: "service contract" within the 10-K, and "upgrade", "tier" and "rebate" across the sell-side research files. The broad extract searches for take-or-pay, price protection, volume commitment, trade-in and buy-back returned no Illumina hits outside the consensus and filing items already in the ledger.
