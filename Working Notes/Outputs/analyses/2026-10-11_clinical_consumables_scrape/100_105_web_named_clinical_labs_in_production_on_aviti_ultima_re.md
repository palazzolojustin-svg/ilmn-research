# Agent 100: 105-web-named-clinical-labs-in-production-on-AVITI-Ultima-Revio-AXELIOS-and-6000-end-of-li

*Model: sonnet. Run 2026-10-11 10:23:05. Cost $1.10 (API-equivalent).*

**Assignment:** Close open gap 3: find named clinical labs (CLIA/CAP/ISO15189, or IVD) that run or have validated patient testing on a non-Illumina high-throughput platform, with a stated cost saving or volume, and any evidence on revalidation time and cost from 6000 to X. Sources to pursue that earlier waves have not exhausted: (a) the OncoDNA AVITI24 deck and press; (b) lab press releases and newswire (PR Newswire, Business Wire, GlobeNewswire) from Jan to Oct 2026 using the queries 'CLIA validated AVITI', 'Element Biosciences clinical laboratory validation 2026', 'Ultima UG 100 clinical laboratory launch', 'AXELIOS early access clinical', 'PacBio Revio clinical laboratory launch', 'Element Biosciences Q3 2026 announcement'; (c) Element's, Ultima's and Roche's own newsrooms and customer-story pages, plus Ultima's Precure, Mayo and Labcorp/Quest MRD updates; (d) conference abstracts and posters from ASCO 2026, AACR 2026, AMP 2026, ESHG 2026 and ASHG 2026 on platform comparison or concordance for MRD, CGP or WGS on AVITI or UG100 versus NovaSeq; (e) Illumina trade press since 1 Aug 2026 on customer complaints or 6000 end-of-life (Illumina's 6000 support or service end date, any sunset or trade-in program, parts supply). Try GenomeWeb or 360Dx via archive.org, Fierce Biotech and Genetic Engineering News. For each named lab record: the platform, the assay, the sample volume, the status (RUO, validated, in production), the saving claimed in $ per sample or per Gb, and the date. Also count: how many of Natera, Guardant, Tempus, Caris, GeneDx, Foundation, Labcorp, Quest and Myriad now have non-Illumina production use. Separate verified facts from vendor claims. Skip the 10-K supplier-concentration text, which agents 29, 34, 41, 54, 62 and 66 already covered.

## Key findings

Little new evidence turned up. I found no named clinical lab in production on a non-Illumina high-throughput platform with a stated saving, and no 6000-to-X revalidation time or cost. This matches open gap 3. The items below are small additions to the ledger.

- **Medicover Genetics runs AVITI in an IVDR-kit workflow (not in the ledger).**
  - FACT: Medicover announced it integrated Element AVITI into its VERACITY NIPT workflow and IVDR-certified kits (TarCET clinical panels, plus prenatal, hereditary cancer and other panels). [Medicover Genetics release, 2025-05-23, https://medicover-genetics.com/news-room/medicover-genetics-broadens-access-to-its-end-to-end-genomics-platform-with-integration-of-element-biosciences-aviti-sequencing-system-into-veracity-nipt-workflow-and-ivdr-c/]
  - FACT: The AVITI instrument itself is "not CE-IVDR marked". Only Medicover's kits are certified.
  - MGMT: The only saving claimed is "improved cost-efficiency". No volume or $/sample is given.
  - This is a kit vendor enabling partner labs. It is not a lab reporting patient volumes. It is the closest thing found to AVITI in production for clinical NIPT, but it is weak and vendor-reported.
  - Ledger E129 and file 51 said no clinical AVITI user was found. This is a qualified exception.
- **Element's regulatory timeline (update to E129).**
  - FACT: Element's own post says AVITI Dx is planned for 2026, with an initial EU filing for CE-IVD as a Class A device. Target uses are newborn screening, oncology and rare disease. [elementbiosciences.com/blog/beyond-2026-what-we-shared-and-whats-next, undated]
  - FACT (search snippet only): ISO 13485 certification on 2026-06-17. File 51 already carried this as unverified. [elementbiosciences.com news page]
  - FACT: That Element post names no clinical customers. Its only named user is Mount Sinai (research pilots).
- **Element validation work is mostly "verification" or partnership, not production.**
  - FACT: ABL Diagnostics (2026-06-09) is running an "ongoing" DeepChek verification on AVITI with 48 clinical virology samples. It states it "do[es] not constitute a complete regulatory validation." No lab is named and no cost is given. [einpresswire.com/article/918135269]
  - FACT: Element partnered with Genoox (rare disease) and Fabric Genomics (2022 vintage) on "validation". These are software partnerships, not lab production. [BioSpace]
- **Foundation Medicine's AXELIOS MRD data (small update to E124).**
  - FACT: A 2026-09-24 summary says Foundation presented early-access MRD data: "MRD positivity was modestly higher with Axelios", concentrated in stages I and II. Lower cfDNA background error is the claimed reason. [oncodaily.com/science/svetlana-nikic-593041, 2026-09-24]
  - Hartwig's ~99% concordance on 1,229 events and the ~29% modelled cost saving versus the NovaSeq X 25B are already in the ledger (file 72, line 381). I did not re-report them.
  - OPINION: This is vendor-sponsored (a Roche workshop) and still RUO. It is not a CLIA patient-reporting deployment.
- **PacBio is the only non-Illumina platform with a verified CLIA/CAP clinical test (not in the ledger).**
  - FACT: Azenta (GENEWIZ) launched a long-read clinical WGS test on Revio in its CLIA/CAP lab, with regulatory approval to offer it in the US. [CLP Magazine, 2024-11-18]
  - The article gives no volume or price. It does not give the regulator, and I did not confirm it was New York State.
  - FACT: Bioscientia (Germany) bought multiple Revio systems to sequence "several thousand human genomes per year". The release is explicitly RUO. [PacBio release, 2023-06-28]
  - This is long-read rare-disease WGS. It is not a displacement of Illumina consumables at scale.
- **Novogene's 6000 phase-out is the only hard "sunset" evidence (not in the ledger).**
  - FACT: Novogene stopped new NovaSeq 6000 quotes on 2024-12-01. Sample submission closed 2025-02-01, production ended 2025-03-01, and all service ended 2025-06-01. It is moving to a NovaSeq X Plus fleet. [web.novogene.com/Facebook_Phasing_out_NovaSeq_6000, Nov 2024]
  - OPINION: This is a large outsourced provider, not a clinical lab. It shows a provider-driven 6000 sunset, with no Illumina announcement involved. It is also a demand-side example of X-only capacity.
- **Revalidation: one dated lab statement (not in the ledger).**
  - FACT: Discovery Life Sciences (CLIA/CAP) said in April 2023 it was cross-validating workflows across both chemistries to "quickly bridge the NovaSeq 6000 and X-Plus" and planned five X Plus systems by year-end 2023. [256today.com, 2023-04-04]
  - No duration or cost is stated.
  - Illumina's own transition page makes no revalidation time or cost claim. It says only that the X is "fully compatible with the entire portfolio of sequencing consumables". [illumina.com NovaSeq X transition page, undated]
  - E031 (12–18 months, "validation cost outweighs the savings") and E116 ($100–200K per switch) therefore remain the only quantification.
- **Ultima clinical evidence is development-stage.**
  - FACT: A clinical-services evaluation of the UG 100 is on bioRxiv (10.64898/2025.12.11.693628, Dec 2025). Search snippets show 61 samples with 70 pathogenic variants (short variants, CNVs, SVs, STR expansions), SNV F1 99.8% and indel F1 99.4%.
  - The preprint's own lab and conclusion are unread (HTTP 429). It likely overlaps with ledger E252's homopolymer caveat.
  - FACT: An ASM Spectrum paper (CSF metagenomics, UG 100) cites ~$12 per 50M reads, ~$60 sequencing per sample and ~$100 total. It is a university-lab evaluation, not production. [journals.asm.org/doi/10.1128/spectrum.01874-25, 2025]
  - Labcorp, Myriad, Quest and NeoGenomics remain at "explore" or "develop" stage (E114). The Quest Q2'26 8-K exhibit contains no Ultima, sequencer or Illumina mention. [sec.gov dgx063020268-kex991, 2026]

## Count: big-9 labs with non-Illumina production use

Verified production use: **0 of 9** (Natera, Guardant, Tempus, Caris, GeneDx, Foundation, Labcorp, Quest, Myriad).

| Lab | Non-Illumina status | Label |
|---|---|---|
| Labcorp | Ultima ppmSeq MRD; AACR 2026 validation already in E114 | Development stage |
| Quest | Ultima, Haystack MRD collaboration; 8-K silent | Development stage |
| Myriad | Bought a UG 100 for the Precise MRD test; "explore" | Development stage |
| Foundation | AXELIOS early access (MRD, WGS baseline) | RUO / early access |
| Natera, Guardant, Tempus, Caris, GeneDx | No public non-Illumina announcement found | None |

Foundation is Roche-owned, so its AXELIOS use is a captive pool (E125).

## Illumina 6000 end-of-life and trade-press (item e)

- I found no Illumina announcement of a 6000 end-of-sale, end-of-service date, trade-in or parts-supply program since 1 Aug 2026. Searches for customer complaints returned nothing relevant.
- Illumina has a generic "Instrument End-of-Sale/End-of-Life Policy" (doc 1000000117071_01). The PDF was binary and Bash was unavailable. The notice period, service length and parts terms are **unread**. This is the one concrete next step. Decode the policy with pdftotext to size the 6000 service tail. The saved copy is at `...\153b5169-ea2c-4757-ba17-fb8b36f44786\tool-results\webfetch-1791732043445-sftjjf.pdf`.
- OPINION: The ledger's "no cliff" framing (E016) has no contradicting external evidence. The Novogene case is the only observed 6000 sunset, and it is provider-driven.

## Contradictions and stale data

- E129 says 20% and file 51 says >25% for Element's clinical-research revenue share. I did not resolve this.
- Most Element and Ultima "validation" items are 2022–2025 vintage (Genoox, Fabric, Medicover May 2025, Azenta Nov 2024, Bioscientia 2023, Discovery 2023). None is a 2026 production milestone. Do not read them as recent momentum.
- Foundation's "modestly higher MRD positivity" is vendor-sponsored and unaudited.

## Gaps / what I could not find

- GenomeWeb and 360Dx returned 403. The AXELIOS clinic article and node/592296 stayed unread.
- Several fetches (bioRxiv UG 100 preprint, Burning Rock/AVITI paper) hit HTTP 429. Retry later.
- The OncoDNA AVITI24 deck (saved binary webfetch-1791731799138-pmzua0.pdf) was not decoded, because Bash was unavailable. A search for OncoDNA with AVITI24 found nothing.
- No ASCO, AACR, AMP, ESHG or ASHG 2026 abstract on AVITI or UG 100 concordance for MRD, CGP or WGS was found.
- No Element Q3 2026 announcement was found.
- No lab-director or revalidation-cost source beyond the ledger's expert estimates (E031, E116).

Sources:
- [Medicover Genetics, 2025-05-23](https://medicover-genetics.com/news-room/medicover-genetics-broadens-access-to-its-end-to-end-genomics-platform-with-integration-of-element-biosciences-aviti-sequencing-system-into-veracity-nipt-workflow-and-ivdr-c/)
- [Element Biosciences, "Beyond 2026"](https://www.elementbiosciences.com/blog/beyond-2026-what-we-shared-and-whats-next)
- [ABL Diagnostics via EIN Presswire, 2026-06-09](https://www.einpresswire.com/article/918135269/abl-diagnostics-advances-platform-agnostic-ngs-strategy-through-deepchek-verification-on-element-biosciences-aviti)
- [OncoDaily, 2026-09-24](https://oncodaily.com/science/svetlana-nikic-593041)
- [CLP Magazine (Azenta), 2024-11-18](https://clpmag.com/diagnostic-technologies/molecular-diagnostics/long-read-whole-genome-sequencing-test-gets-regulatory-nod/)
- [PacBio/Bioscientia, 2023-06-28](https://www.pacb.com/press_releases/pacbios-revio-system-empowers-bioscientia-to-scale-long-read-whole-genome-sequencing-and-unravel-the-mysteries-of-rare-disease)
- [Novogene NovaSeq 6000 phase-out, Nov 2024](https://web.novogene.com/Facebook_Phasing_out_NovaSeq_6000)
- [256today, Discovery Life Sciences, 2023-04-04](https://256today.com/discovery-hosts-largest-fleet-of-genomic-research-accelerators/)
- [ASM Spectrum UG 100 CSF evaluation](https://journals.asm.org/doi/10.1128/spectrum.01874-25)
- [Illumina NovaSeq X transition page](https://www.illumina.com/systems/sequencing-platforms/novaseq-x-plus/applications/transition.html)
- [Quest Q2'26 8-K ex. 99.1](https://www.sec.gov/Archives/edgar/data/0001022079/000102207926000067/dgx063020268-kex991.htm)
