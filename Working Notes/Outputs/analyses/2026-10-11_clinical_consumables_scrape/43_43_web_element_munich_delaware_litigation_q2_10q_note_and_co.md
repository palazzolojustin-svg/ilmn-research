# Agent 43: 43-web-Element-Munich-Delaware-litigation-Q2-10Q-note-and-competitor-patent-dockets

*Model: sonnet. Run 2026-10-11 03:05:32. Cost $0.58 (API-equivalent).*

**Assignment:** Goal: close the litigation and IP gap, which affects competitor viability and pricing power. (1) Read Illumina's Q2 2026 10-Q (ilmn-20260628.htm on EDGAR, CIK 1110803) legal-proceedings note (Note 8 or equivalent) in full. Capture every matter: Element Biosciences, BillionToOne, Roche/other, securities class actions, derivative suits, and any government or antitrust matter. Quote the accrual amounts and loss-contingency wording, and compare them with the Q1 2026 and FY25 10-K wording to see what was added or dropped. (2) Element dispute: find the Delaware case numbers (search CourtListener, RECAP, PACER-mirrors, Justia dockets, Law360/Bloomberg Law snippets, Element's Sept 2025 press release) and which products are accused (is AVITI, AVITI24, VITARI or NovaSeq X accused?). Look up the '301, '174 and '887 patents on Google Patents or USPTO Patent Center: assignee, filing and priority dates, claim 1 summary, expiry, any IPR petitions at PTAB. (3) Munich Regional Court (Landgericht München I) injunction against Element: security amount, whether Element posted it (Element said on 14 Jul 2026 it expected to post security 'soon'), any appeal to the Higher Regional Court, effect on EU AVITI sales. Check Element's newsroom, GenomeWeb, 360Dx, Fierce Biotech, Business Wire and UPC/Munich court press. (4) Search for any other patent suits involving Ultima, Roche (AXELIOS/SBX), MGI/Complete Genomics (the Illumina v. BGI history and any 2026 revival), PacBio, and Singular. (5) Any antitrust or FTC/EC inquiry (e.g. residual GRAIL-related obligations, EC fine appeal status, and EU Court of Justice outcomes). Quantify damages sought, bond or security amounts, dates and deadlines. Label each point FACT with docket or URL and date. Hard stop at 20 minutes; state what is blocked.

## Key findings

1. **The brief's Munich premise is reversed.** The Regional Court of Munich I ruled on 14 Jul 2026 against **Illumina**, not Element. Element is the patentee and Illumina is the infringer. Illumina GmbH is also a defendant. [Element press release, 2026-07-14, elementbiosciences.com/news/element-biosciences-prevails-in-german-patent-case-against-illumina; Business Wire 20260714274374] FACT
2. **The Munich ruling's scope.**
   - The court found direct infringement (Illumina's own use in Germany) and indirect infringement (offering systems, reagent kits, flow cells and cartridges).
   - Illumina is enjoined from offering or supplying infringing systems and consumables in Germany.
   - It must recall systems and kits put into circulation since **31 Mar 2023**, with refunds and return costs paid by Illumina.
   - Illumina is jointly and severally liable for damages and must render an account of quantities, customers, prices and profits. [same sources] FACT
3. **Products named in the judgment.** The press release names MiSeq, MiSeqDx "and any other Illumina imaging system that functions as described." [Element release, 2026-07-14] FACT
   - The patent is reported as DE112008000363, "Device for detection and its use" [ipfray, 2026-07, paywalled preview]. FACT (secondary source)
   - This extends E201's open-scope point. I could not confirm whether NovaSeq 6000 or X is covered in Germany.
4. **Security.** The security amount is **not in any accessible source**. The release says the judgment is provisionally enforceable once Element posts the court-set security and that Element "expects to post the required security soon." Searches found no later report that it was posted, and none of an appeal to the Higher Regional Court (Oberlandesgericht). Illumina retains appeal rights. FACT (absence of evidence). Gap 4 stays open on all three points.
5. **Delaware: Illumina is the plaintiff.** Illumina sued Element on **15 May 2025** (D. Del., **1:25-cv-00602**). It asserted five patents on imaging systems and flow-cell cartridges: US 12,251,702; 8,951,781; 11,117,130; 11,697,116; 12,151,241. Illumina's counsel is Kelly Farnan of Richards, Layton & Finger. Accused product: the AVITI system, with no variants named. [ipfray, 2025-05; search summary citing the case number] FACT
6. **Element's counterclaims.** Element's counterclaims came in Sept 2025. Element asserts four patents against Illumina in Delaware: **8,612,161; 9,605,301 ('301); 9,909,174 ('174); 11,001,887 ('887)**. The accused Illumina products are **MiSeq, MiSeq i100, MiniSeq, NextSeq 1000/2000, NovaSeq 6000 and NovaSeq X**. [Element release, Sept 2025, via search summary; ipfray 2026] FACT (summary-level)
   - This answers Gap 4's "is NovaSeq X accused": yes, per Element's release. The release itself was unfetchable (the redirect URL returned 404).
   - It also updates E120. The Sept 2025 filings were a patent countersuit in Delaware, a patent suit in Munich, and an antitrust suit in N.D. Cal.
   - Damages sought were not found. I did not reach the patents' assignee, expiry or claim 1, or any IPR record.
7. **10-Q Note 8 could not be read.** WebFetch returned only the front matter of ilmn-20260628.htm (accession 0001110803-26-000160). It showed the CVR contingent-consideration liability of **$40M** at 28 Jun 2026, payable quarterly through Aug 2033. FACT
   - The 10-Q's accounting policy is to accrue when a loss is probable and reasonably estimable. Accrual amounts for Element and the other matters, and any wording changes versus Q1 and FY25, are unverified.
   - The Munich ruling came 16 days after quarter-end, so it is a post-period event. Any disclosure would be in the Q3 10-Q or a subsequent-events note. OPINION
8. **Icahn derivative suit settlement (8-K, 2026-08-07).**
   - *Icahn Partners v. DeSouza*, Del. Ch. C.A. No. 2023-1045-PAF.
   - A Release Agreement was executed effective 21 Aug 2025, with mutual releases and **no monetary payment**.
   - It is dismissed with prejudice as to the named plaintiffs only.
   - The approval hearing is **2 Nov 2026, 1:30pm ET**. Signed by CLO Julie Coletti. [sec.gov 0001110803-26-000168] FACT
   - This matches the ledger's "Icahn hearing 2 Nov" (E159). The new details are the no-money term and that the CLO signing the 8-K is Coletti. E-series governance notes mention a departing CLO, Davies.
9. **BillionToOne suit details (adds to E094).** Filed in D. Del. on 7 May 2026, asserting US 10,612,096; 12,139,760; 12,435,373. They cover fetal-fraction determination and variant identification in mixed DNA. Accused product: Unity prenatal tests. Illumina seeks a permanent injunction or future royalties, past damages, and fees. BillionToOne says the claims are "without merit." [Bloomberg Government, 2026-05; GenomeWeb] FACT
10. **10x Genomics suits against Illumina.** On 21 Oct 2025, 10x filed two Delaware suits covering nine patents. One is with Prognosys (spatial) and one with Roche Sequencing Solutions. Illumina "denies the allegations." Accused: Illumina's spatial technology. [Bloomberg Law, 2025-10-21] FACT
    - Roche is a co-plaintiff with 10x, so Roche is both an adversary and an AXELIOS competitor.
    - This is not in the ledger. It is not a consumables risk, but it is a litigation and IP-cost item.

## Contradictions and stale data

- The assignment says the Munich injunction is "against Element." The sources say the opposite (see finding 1).
- The assignment says Element's Delaware case dates from Sept 2025. Illumina filed first, in May 2025. Element's Sept 2025 filings are counterclaims plus the separate Munich and N.D. Cal. actions.
- The briefing says "'301, '174 and '887 patents." These are **Element-owned** patents asserted *against* Illumina. Element is the assignee per the Element release, which I have not verified at the patent register.
- The ledger E201 says the ruling is "legacy MiSeq only" per Illumina. The sources only confirm MiSeq and MiSeqDx plus the open-ended clause.
- Complete Genomics v. Illumina and the BGI battle are history. Illumina paid $325M to settle with the BGI affiliates (GenomeWeb). I did not verify the settlement date. FACT

## Gaps / what I could not find

- Munich security amount, posting, appeal, and effect on EU AVITI or Illumina sales. GenomeWeb (403) and the full ipfray article were blocked.
- The Q2 10-Q Note 8 text (accruals, loss-contingency wording, comparison with Q1 and FY25). A local download is needed. Also unchecked: accrual amounts for the SEC investigation and the state securities class action.
- Delaware counterclaim case number (probably the same 1:25-cv-00602 docket, unconfirmed), the judge, and the schedule. Also not found: Markman and trial dates, damages sought, patent expiry, claim 1 and any PTAB IPR petitions. Google Patents and Patent Center were not queried.
- Any 2026 patent suit involving Ultima, Roche (AXELIOS or SBX, beyond the 10x co-plaintiff role), PacBio, Singular or MGI. A single search found none.
- The EC fine and the CJEU outcome, and any residual FTC or EC obligations. The 10-Q text only references the EC decisions as background. I did not verify the current status.
