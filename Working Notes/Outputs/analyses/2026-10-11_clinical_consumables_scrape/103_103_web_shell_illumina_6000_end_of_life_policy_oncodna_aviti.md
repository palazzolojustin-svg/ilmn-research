# Agent 103: 103-web-shell-Illumina-6000-end-of-life-policy-OncoDNA-AVITI-deck-UG100-preprint-and-named

*Model: sonnet. Run 2026-10-11 10:27:22. Cost $1.06 (API-equivalent).*

**Assignment:** Close open gap 3. (a) Download and decode Illumina's 'Instrument End-of-Sale / End-of-Life Policy' (document 1000000117071_01, support.illumina.com or emea.support.illumina.com; search the title if the ID fails). Extract: the NovaSeq 6000 end-of-sale date (if any), the number of years of service and reagent support after end-of-sale, the reagent-supply commitment, and the trade-in or upgrade programs. Find any Illumina 'NovaSeq 6000 trade-in' or 'upgrade to NovaSeq X' program terms. Size the tail, using ~1,360 6000 units and ~$600-650K pull-through. (b) Decode the OncoDNA AVITI24 deck and press release (clinical lab in production, saving per sample). (c) Retry the bioRxiv UG 100 clinical-services preprint 10.64898/2025.12.11.693628 (use the bioRxiv API api.biorxiv.org/details/biorxiv/10.64898/2025.12.11.693628, or Europe PMC). (d) Search for named clinical or CLIA labs that run Element AVITI, Ultima UG 100 or Roche AXELIOS in production, with a stated saving or cost per genome or per sample: press releases from Element and Ultima (e.g., Broad, Regeneron, Psomagen, Tempus, Caris, Natera, Invitae, Variantyx, Genomics England, NHS GMS, Radboud, Rady), Roche SBX AXELIOS customer announcements since 29 Jun 2026, and archive.org copies of GenomeWeb or 360Dx pieces. Quantify the claimed $/genome and $/Gb, the revalidation timeline and cost (CAP/CLIA/FDA IVD change control), and the date. Label FACT, MGMT or OPINION, with URLs. Hard stop at 20 minutes.

## Key findings

**Gap 3 is mostly still open: no named lab with a stated saving, and the end-of-life policy is undecoded.** The one genuinely new item is the Illumina product-retirement page, which has no NovaSeq 6000 entry. I could not fetch or decode three source PDFs. The evidence below is thin.

1. **Illumina's retirement page has no NovaSeq 6000 end-of-sale date (FACT, by absence).** It lists only iSeq 100, MiniSeq (non-OEM) and MiSeq RUO. All three have end-of-sale on 30 Sep 2025 and end-of-service-life on 31 Dec 2029. The replacement is the MiSeq i100 Series. (Illumina Product Retirement, emea.support.illumina.com/support-content/product-retirement.html, fetched 2026-10-11.)
   - This supports the ledger's "no cliff" framing (E016): management has not announced a 6000 end-of-sale. It also fits the ">10 new 6000s sold" in Q2'26 (E015).
   - The page tells customers to contact their rep to schedule "last time buys".

2. **There is a published precedent for the tail length (FACT).** Illumina's EOL announcement of 27 Mar 2025 gave about 3 months' notice before end-of-sale and about 4.25 years of service after it (30 Sep 2025 to 31 Dec 2029).
   - Service contracts had to be renewed by the end-of-sale date. Instruments off-contract by then would not be eligible for renewal.
   - Consumables: "Certain reagent kits may be discontinued earlier than the second half of 2029 if demand remains low." General consumable end-of-sale is targeted for H2 2029. (Illumina knowledge article 000009536, knowledge.illumina.com/instrumentation/general/instrumentation-general-reference_material-list/000009536.)
   - **Sizing (OPINION):** if the 6000 followed this template, the ~1,360 base × $600–650K pull-through (about $0.8–0.9B a year) would not disappear on an announcement. Service and reagents would run roughly 4 more years after any end-of-sale notice.
   - Small, low-volume instruments are the ones where Illumina allowed early reagent discontinuation. High-volume NovaSeq 6000 reagents are unlikely to be treated that way.
   - A mid-2027 end-of-sale announcement would put the end of service life around 2031–32. That is my extrapolation, not a stated date.

3. **I could not verify the EOS/EOL policy document (1000000117071_01).** I found it at emea.illumina.com/content/dam/illumina-marketing/documents/terms-conditions/1000000117071_01_Product_End_of_Sale_End_of_Life_Policy.pdf, but the fetch returned a binary PDF. The `_00` version at tst-web.illumina.com also came back as a binary PDF.
   - Bash and the PDF renderer (pdftoppm) are unavailable in this session, so I could not decode either one. I did not read the reagent-supply commitment or any trade-in terms.
   - Only the search-result summary is usable: it defines End-of-Sale (EOS) as "last day Illumina will take orders" and End-of-Service-Life (EOSL) as "last day… Service and Support". It also says HiSeq got 5 years of technical support and spares from the EOL date. That summary is a search-engine paraphrase, not a document read.

4. **No NovaSeq 6000 trade-in or "upgrade to X" program was found (FACT, by absence).** No Illumina page in search results describes one. The only retirement-page guidance is "contact your Sales Representative." Trade-in and upgrade terms therefore remain unproven.

5. **A lab with a stated cost saving on a non-Illumina platform was not found.**
   - PathoNext (Leipzig molecular pathology lab) has run an Element AVITI24 since Oct 2025. Its stated motive is cost-efficiency, expanding comprehensive genomic profiling (CGP) capability and "reducing dependency towards a single provider". It has OncoDEEP validation experience on the AVITI24. This comes from search-result summaries of OncoDNA's UGM deck, not from my own read of the deck. (OncoDNA UGM, Dec 2025, ugm.oncodna.com/wp-content/uploads/2025/12/Ioana_Lemnian_Insights-from-OncoDEEP-and-the-AVITI-Platform-24-public.pdf.)
   - **Status: FACT that it is a clinical user, MGMT on motive, no saving figure.** The OncoDNA deck itself is image-based PDF and did not extract. The application-note page (oncodna.com/scientific-application-note/ap_oncodeep-kit-element_biosciences) is a download gateway with no numbers.
   - University of Minnesota Genomics Center says AVITI is now cheaper than the NovaSeq X 25B, per its pricing page. That is a core lab, not a clinical lab. (genomics.umn.edu/AVITI-price-drop-2024.)
   - Element's blog on Burning Rock Dx (27 Nov 2023) says the move from Illumina to AVITI was "virtually seamless" on identical libraries. It gives no cost or savings figure and describes a parallel run, not a full switch. (elementbiosciences.com/blog/reducing-the-price-of-comprehensive-genomic-profiling.)

6. **The UG 100 preprint's metadata is now confirmed.** The title is "Evaluation of the Ultima Genomics UG 100 sequencing platform for clinical services" (Santuari, Kolpakov, Blin, Xenarios, Howald; 12 Dec 2025). The comparator is the NovaSeq 6000.
   - This repeats E252, which already holds the abstract. The bioRxiv API fetch returned the same abstract and no new numbers.
   - The full text (source.xml, v1.full, Europe PMC) returned HTTP 429 or 500, so no results tables were read.
   - Ledger E252 stays as is.

7. **The Roche AXELIOS customer search added nothing beyond the ledger.** The search summaries gave CNAG (bought one; test runs in April) and Broad Clinical Labs (rapid whole-genome use). Both are already in the ledger at E124 and in the Broad and CNAG entries.
   - Roche says AXELIOS 1 is RUO, with clinical use only "potentially… in the future".
   - The GenomeWeb pieces were 403-blocked, and web.archive.org is blocked by the tool.

## Contradictions and stale data
- None against the ledger. The retirement page shows only the three MiSeq-class instruments, which is consistent with E016 and E015.
- I did not verify the Q2'26 claim that the 6000 is "a standard part of the business" against any dated Illumina policy.

## Gaps / what I could not find
- **Policy PDF text (high priority).** Needed: the reagent-supply commitment, spare-parts years, and trade-in or upgrade terms. A session with Bash and `pdftotext` or `pypdf` could read the saved binaries, which are in this session's tool-results folder:
  - webfetch-1791732352336-jurer3.pdf (EOS/EOL policy `_01`)
  - webfetch-1791732367048-isrgiu.pdf (EOS/EOL policy `_00`)
  - webfetch-1791732354385-npo3ke.pdf (OncoDNA deck, image-based, may need OCR)
  - webfetch-1791732388645-5zg6yr.pdf (Element JPM 2026 deck)
  - webfetch-1791732411984-a4k86y.pdf (Element clinical-research eBook)
- UG 100 preprint full text, still HTTP 429 or 500. Retry later via biorxiv.org `.full` or Europe PMC.
- Named clinical or CLIA labs on Element, Ultima or Roche with a stated $/genome or $/sample saving. My searches covered Element, Ultima and Roche only, not MGI, and returned nothing with a number.
- 6000-to-X revalidation time or cost for a CLIA lab. Beyond E031 and E116, nothing new.
- Not checked for lack of time: Natera, Invitae, Variantyx, Genomics England, NHS GMS, Radboud, Rady, Psomagen and Regeneron press releases.

Sources:
- [Illumina Product Retirement](https://emea.support.illumina.com/support-content/product-retirement.html)
- [Illumina EOL knowledge article 000009536](https://knowledge.illumina.com/instrumentation/general/instrumentation-general-reference_material-list/000009536)
- [Illumina EOS/EOL policy 1000000117071_01 (undecoded)](https://emea.illumina.com/content/dam/illumina-marketing/documents/terms-conditions/1000000117071_01_Product_End_of_Sale_End_of_Life_Policy.pdf)
- [OncoDNA UGM deck, Dec 2025 (not decoded)](https://ugm.oncodna.com/wp-content/uploads/2025/12/Ioana_Lemnian_Insights-from-OncoDEEP-and-the-AVITI-Platform-24-public.pdf)
- [Element: Burning Rock Dx blog, 2023-11-27](https://www.elementbiosciences.com/blog/reducing-the-price-of-comprehensive-genomic-profiling)
- [UMN Genomics Center AVITI price drop](https://genomics.umn.edu/AVITI-price-drop-2024)
- [bioRxiv 10.64898/2025.12.11.693628 (abstract via API)](https://api.biorxiv.org/details/biorxiv/10.64898/2025.12.11.693628)
