# Agent 35: 35-web-litigation-dockets-and-patents-Munich-Element-BillionToOne

*Model: sonnet. Run 2026-10-11 02:47:33. Cost $0.59 (API-equivalent).*

**Assignment:** Resolve the Illumina litigation gaps using sources previous agents did not manage to open (CourtListener, Law360 and GenomeWeb returned 403). Try, in order: Justia Dockets (dockets.justia.com), PacerMonitor, RECAP archive links, govinfo.gov, Google Patents (patents.google.com/patent/US#######) for patent claims and assignees, the Unified Patent Court decisions page (unifiedpatentcourt.org) and German court press releases (Landgericht Munich I), Business Wire and PR Newswire for Element Biosciences and Illumina releases, Illumina's investor site 8-K exhibits, and the Illumina Q2 2026 10-Q legal-proceedings note (Note 8) at sec.gov.

Questions: (1) Munich ruling against Illumina on NovaSeq X: who was the plaintiff, patent numbers, the court's holding on NovaSeq X scope, the injunction scope, the security amount and whether it was posted, appeal status, and any carve-outs for existing customers or the US. Quantify any exposed revenue Illumina has given. (2) Element Biosciences v. Illumina, N.D. Cal. 25-cv-08026-NW: the amended complaint, theories (tying, exclusive dealing, loyalty discounts), the motion to dismiss and hearing dates, any ruling, and what the complaint alleges about customer contracts or discounts (this is direct evidence on pricing and bargaining power). (3) The Delaware patent case: check whether the five patents (8,612,161; 9,605,301; 9,909,174; 11,001,887; 12,656,313) exist, who owns them, and whether they are asserted against NovaSeq X. (4) Illumina v. BillionToOne in Delaware: complaint date, patent numbers, accused products, and any customer-relevance. (5) Any other suits touching Ultima, Roche, MGI/Complete Genomics, or customer disputes.
Give docket numbers, dates and quotes. Mark anything unverified. Hard stop at 20 minutes.

## Key findings

Most of my scope was already in the ledger (E120, E201, E215, E094). The additions below are new or correct a ledger item. I could not open CourtListener, Law360, GenomeWeb, Justia or the 10-Q Note 8 text.

1. **The Delaware patents are Element's counterclaims, and NovaSeq X is named as accused.** FACT, but second-hand: the accused-product list comes from a search summary that paraphrases Element's countersuit release. It names "MiSeq, MiSeq i100, MiniSeq, NextSeq 1000/2000, NovaSeq 6000, and NovaSeq X". I could not open the release itself (the redirect URL returned 404). This is the first evidence that Element's US patent exposure reaches the NovaSeq family, which E215 says the Munich ruling does not. It answers part of open gap 7. [Search summary of Element release "Element Biosciences Files Competition and Patent Infringement Countersuits Against Illumina", Sept 2025, elementbiosciences.com/news/element-biosciences-files-competition-and-patent-infringement-countersuits-against-illumina]

2. **Four of the five patents are confirmed as asserted; the fifth is not.** The search summary lists only four Delaware patents: 8,612,161; 9,605,301; 9,909,174; 11,001,887. Element's Munich release names all five, but it says they are being pursued "in Delaware". The fifth, 12,656,313, was granted on 16 Jun 2026, so it is a later addition. The two I checked on Google Patents:
   - **US 12,656,313**, "Methods and devices for sequencing nucleic acids in smaller batches". Filed 14 May 2024, granted 16 Jun 2026. Current assignee is Qiagen Sciences LLC, originally IsoPlexis. Claim 1 covers multiple small flow cells on a moveable support cycling through reagent and imaging stations. [patents.google.com/patent/US12656313B2/en]
   - **US 8,612,161**, "Methods and compositions for base calling nucleic acids". Priority 19 Mar 2008, expires about 18 Jul 2030. Current assignee IsoPlexis, originally Intelligent Bio Systems. It claims lead/lag (phasing) correction in base calling. [patents.google.com/patent/US8612161B2/en]
   - OPINION: Element says the patents are "licensed exclusively to the company", so it is a licensee, not the owner. The '161 expiry in 2030 caps any damages period and any injunction. I did not check '301, '174 or '887.

3. **Illumina's own Delaware suit against Element has its patent numbers and filing date.** Illumina sued on 15 May 2025 over five patents: 12,151,241; 8,951,781; 11,117,130; and 11,697,116 (all titled "Systems, methods, and apparatuses to image a sample…"), plus 12,251,702 ("Flowcell cartridge with floating seal bracket"). Counsel is Kelly Farnan of Richards Layton & Finger. The ip fray page gave the number "58077286", which looks like a docket-service ID, not a case number. Element's patent claims are therefore counterclaims or a separate suit against Illumina's own offensive case. [ipfray.com/illumina-sues-element-biosciences-in-delaware-over-gene-sequencing-patents/, filing 15 May 2025]

4. **Illumina v. BillionToOne now has patent numbers and accused products.** Complaint filed 7 May 2026 in D. Del. Patents: US 10,612,096; 12,139,760; 12,435,373. They cover determining the fetal fraction of DNA in maternal blood and identifying variants in DNA mixtures. The accused product is the UNITY prenatal screening tests. The judge and case number were not available. This adds detail to E094. [Bloomberg Government, 2026-05-07, news.bgov.com/delaware-brief/illumina-sues-billiontoone-says-prenatal-tests-infringe-patents]
   - OPINION on customer relevance: the suit targets a customer that buys Illumina consumables for NIPT, which is a shallow-sequencing application. It tells you Illumina will use patents against its own clinical customers. The claims concern fetal fraction and molecular-counting methods, not the sequencer, so there is no direct consumables-supply consequence I could find.

5. **The Element antitrust ruling in more detail (adds to E120).** On 28 May 2026 Judge Noël Wise dismissed with leave to amend. [A&O Shearman, lit-antitrust.aoshearman.com/northern-district-of-california-dismisses-dna-sequencing-antitrust-claims-against-illumina-with-leave-to-amend; Bloomberg Government]
   - **Alleged conduct (the complaint's four tactics):**
     - Threats to raise consumable and service prices to push customers onto new Illumina instruments.
     - Discounts conditioned on exclusive purchases.
     - Bundles discounted by "50%+" and priced below marginal cost.
     - Disparagement of Element's financial viability.
   - **Why it failed:**
     - Exclusive dealing: no pleaded facts showing customers were "substantially foreclosed". One customer rejected Illumina's exclusivity offer, which undercut the theory.
     - Tying: Element pleaded instruments, consumables and services as three separate markets while also alleging they are proprietary and not interchangeable across brands. The court saw that as contradictory.
     - Section 2: no facts showing prices were "below its costs", and no scaling of the 50%+ discounts.
   - **Pricing and bargaining evidence:** the complaint alleges written communications in which an Illumina salesperson conditioned discounts on exclusivity. The facts are only alleged and unproven. MGMT/OPINION: the dismissal turned on pleading gaps, not on whether the conduct occurred.
   - **Status:** Illumina moved to dismiss the amended complaint in July 2026 (this matches the 23 Jul reply in E120). I found no hearing date or ruling.

## Munich: what is still unknown

- **Plaintiff, patent and scope:** confirmed as in E201 and E215. The plaintiff is Element, the patent is DE 112008000363, and the ruling names MiSeq and MiSeqDx.
- **Security:** Element's release says it "expects to" post the court-set security soon. I found no amount and no confirmation that it was posted.
- **Appeal:** Element's release says Illumina "may appeal". I found no statement from Illumina on appeal.
- **Exposed revenue:** Illumina gave no figure that I found. OPINION: the German MiSeq exposure looks small against the ~$775M quarterly sequencing consumables line, but that is my inference, not a number from Illumina.

## Contradictions and stale data

- **Munich vs. Delaware scope:** Illumina says the Munich ruling reaches only legacy MiSeq (E215). Element's US claims reportedly name NovaSeq X (finding 1). The two do not conflict, but the US exposure is broader than Munich suggests.
- **E201 wording:** E201 and the Element release say the judgment covers "any other Illumina imaging system that functions as described by the court". That is open-ended, so Illumina's "legacy MiSeq only" reading is its own characterization.
- **Gap 7 premise:** the task brief refers to a "Munich ruling against Illumina on NovaSeq X". The sources show a MiSeq-only ruling, so that premise is not supported.

## Gaps / what I could not find

- The Q2 2026 10-Q Note 8 text. WebFetch returned only a table of contents and the note starts on page 26. The 10-Q is at sec.gov/Archives/edgar/data/0001110803/000111080326000160/ilmn-20260628.htm.
- The Delaware case numbers, a hearing date or ruling on the amended motion to dismiss, and whether the Delaware matters are stayed.
- The security amount and whether it was posted, any appeal filing, and the US patent claim charts against NovaSeq X.
- Whether '301, '174 and '887 are IsoPlexis or Qiagen assets, and whether the Illumina-owned patents in finding 3 are asserted against AVITI.
- Other suits touching Ultima, Roche or MGI/Complete Genomics: I did not get to them.
- The Element antitrust complaint PDF, saved at `C:\Users\palaz\.claude\projects\C--Users-palaz-OneDrive-Documents-ILMN-Claude-Code-Local-Folder--Build-sandbox\f34e8b61-8841-47b3-9d5b-36aa02930570\tool-results\webfetch-1791704809462-9muy91.pdf`. It could not be rendered (no pdftoppm). It may hold the discount detail if opened elsewhere.

Sources:
- [Element Biosciences, Munich release](https://www.elementbiosciences.com/news/element-biosciences-prevails-in-german-patent-case-against-illumina)
- [ip fray, Illumina v. Element Delaware suit](https://ipfray.com/illumina-sues-element-biosciences-in-delaware-over-gene-sequencing-patents/)
- [Bloomberg Government, Illumina v. BillionToOne](https://news.bgov.com/delaware-brief/illumina-sues-billiontoone-says-prenatal-tests-infringe-patents)
- [A&O Shearman, Element v. Illumina dismissal](https://www.lit-antitrust.aoshearman.com/northern-district-of-california-dismisses-dna-sequencing-antitrust-claims-against-illumina-with-leave-to-amend)
- [Bloomberg Government, Illumina beats Element monopolization claims](https://news.bgov.com/antitrust/lllumina-beats-rivals-dna-sequencing-tool-monopolization-claims)
- [Google Patents US12656313B2](https://patents.google.com/patent/US12656313B2/en)
- [Google Patents US8612161B2](https://patents.google.com/patent/US8612161B2/en)
