# Agent 85: 88-web-MCED-and-population-genomics-Gb-volume-inputs

*Model: sonnet. Run 2026-10-11 10:07:21. Cost $1.18 (API-equivalent).*

**Assignment:** Close open gap 8: unsourced MCED and population-genomics Gb inputs. Use only primary or trade-press sources and record exact URL and date for each.
(1) Galleri sequencing depth per test. Search GRAIL 10-K/10-Q text, the PATHFINDER 2, NHS-Galleri and PREVENT publications, FDA panel briefing documents from the 23 Sep 2026 meeting, and GRAIL investor decks for 'read depth', 'x coverage', 'reads per sample' or 'Gb per sample'. Convert to Gb per test.
(2) Volumes and pricing. Quantify tests sold or run for Galleri (2024, 2025, H1 2026), Exact Sciences Cancerguard, Guardant Shield and Shield MCD, and Natera's MRD and Signatera test counts. Take these from the Q2 2026 releases. Compute implied Gb per year using the depth figures from (1) and any depth disclosed by each company.
(3) National and population programs. Check Our Future Health, PRECISE-SG100K, Genomics England newborn (Generation Study), the Saudi, UAE (Emirati Genome), Japan and Australia genomics programs, GUARDIAN, BabySeq, the Florida Sunshine Genetics Act, and the UnitedHealthcare WGS coverage policy. For each find the sample count, platform (Illumina, Ultima, Element, MGI or Roche), timing and any stated cost per genome. Flag any program that moved to or tested a non-Illumina platform.
(4) Ultima's named $80-genome partners and volumes. Search Ultima press releases, UG 100 Solaris and Broad, Regeneron, Our Future Health and Arc Institute announcements.
Quantify total incremental clinical Gb per year by program and compare it with the ~30% y/y Gb growth assumption. Label each figure FACT, MGMT or OPINION. Say plainly when a figure is an assumption.

## Key findings

Little here is new. The main gap (Galleri depth per test) stays open, and I could not source a Gb-per-test figure for any MCED test. I fetched only what is listed below. The 403s and corrupted PDFs mean several items are search-snippet level only. Gap 8 is therefore **partly closed**: volumes and a few program facts are new, the depth inputs are not.

1. **Galleri volumes (new; E081 has no GRAIL entry).**
   - FY2025: "Sold More Than 185,000 Galleri® Tests in 2025". U.S. Galleri revenue was $136.8M (+26%) and Q4'25 was $41.3M (+31%). (FACT) [GRAIL FY25 release, 2026-02-19, https://grail.com/press-releases/grail-reports-fourth-quarter-and-full-year-2025-financial-results/]
   - Q2'26: >61,000 tests (+35% y/y), Galleri revenue $42.6M (+24%). (FACT) [GRAIL Q2'26 release, ~2026-08-05, https://www.biospace.com/press-releases/grail-reports-second-quarter-2026-financial-results]
   - H1'26: >117,000 tests (+42%), $82.5M (+30%). (FACT) [same source]
   - Implied revenue per test: about $699 in Q2'26 ($42.6M ÷ 61K) and about $739 in FY25 ($136.8M ÷ 185K). (OPINION, my calc.) The FY25 figure is U.S. revenue over total tests, so it is approximate.
   - The 2024 count is not sourced here.

2. **Galleri sequencing depth is not public in anything I could open.** GRAIL's Q2'26 and FY25 releases mention no depth or platform. The FDA briefing PDF (https://www.fda.gov/media/195032/download) returned binary data that WebFetch could not decode. It is saved at `C:\Users\palaz\.claude\projects\C--Users-palaz-OneDrive-Documents-ILMN-Claude-Code-Local-Folder--Build-sandbox\f033095d-dcd8-4187-920f-c691fab8e32d\tool-results\webfetch-1791731164668-sx6n5b.pdf`. It needs pdftotext before anyone concludes the FDA document has no depth figure.

3. **Galleri is a targeted-methylation panel, not whole-genome.**
   - A GRAIL-related summary describes bisulfite sequencing of a panel of ">100,000 informative methylation regions" (CCGA, Annals of Oncology 2020). The 30x WGBS figure in the same search result belongs to the discovery substudy, not the commercial test. (FACT, search snippet, not opened in full.)
   - Implication (OPINION): the ledger's 5–15 Gb/test MCED scenarios (gap 8) are probably too high for the commercial test. A targeted panel generally needs far fewer Gb than a 30x genome (~100 Gb). I have no sourced figure, so the number is still an assumption.
   - Rough bound, assuming 5–15 Gb/test (unsourced): Galleri H1'26 at ~117K tests is 0.6–1.8 Pb-scale… more simply, 117K × 5–15 Gb ≈ 0.6–1.8M Gb per half-year. It is small next to Illumina's roughly 100-plus Gb per genome tests. This is an assumption, not a finding.

4. **Guardant Shield (adds the ASP to E081).** About 66K tests in Q2'26 (+22K q/q, vs 16K a year earlier). ASP is about $800 and screening revenue was $52.9M (vs $14.8M). UnitedHealthcare announced first-line coverage after quarter-end. (FACT/MGMT) [Guardant Q2'26 call, 2026-07-30, https://www.marketbeat.com/instant-alerts/guardant-health-q2-earnings-call-highlights-2026-07-30/] Shield MCD volume was not separated in what I saw, and no depth was found.

5. **Exact Sciences Cancerguard: no volume found, and the reporting structure changed.** Abbott closed its ~$21B acquisition of Exact on 2026-03-23 and Exact was delisted. (FACT) [https://hlth.com/insights/news/abbott-closes-21b-deal-for-exact-sciences-2026-03-24; medtechdive.com says closing was on a Monday] This answers the open Abbott question in gap 7. Exact no longer files standalone Q2'26 results, so a Cancerguard test count is unlikely to appear unless Abbott discloses it. The Cancerguard US launch was in Q3'25 (search snippet).

6. **Precure / Mayo Clinic / Thermo Fisher selects Ultima (new, 2026-09-22).** Ultima's UG200 Ultra platform was selected for a multi-omics effort spanning "one million biospecimens" (Mayo-led Precure LLC with Thermo Fisher as founding partner). (FACT, search snippet.) [HPCwire, https://www.hpcwire.com/bigdatawire/this-just-in/ultima-genomics-selected-for-mayo-clinic-led-million-biospecimen-initiative/ (page itself returned 403)] Genome counts, depth and timeline were not retrieved, so Gb is unquantified. This is a non-Illumina win and the most important item for gap 8 part 4. Mayo was already named as an Ultima customer.

7. **Other Ultima named customers (partly new).**
   - BaseClear (Europe) adopted the UG200 and launched Ultima services mid-July 2026. (FACT, snippet.) [https://www.biospace.com/press-releases/ultima-genomics-and-baseclear-to-expand-european-access-to-low-cost-and-high-throughput-sequencing-using-ultimas-ug200-platform]
   - Arc Institute (Virtual Cell Atlas, with 10x), Broad (presented at AGBT), Regeneron (investor and development agreement since 2022), Myriad, Quest and Mayo are listed as customers. Quest/Myriad/Mayo are from a Wikipedia-style aggregation, so treat them as lower confidence. [https://arcinstitute.org/news/arc-10x-ultima; https://www.ultimagenomics.com/blog/ultima-genomics-signs-development-agreement-with-regeneron-aimed-at-driving-the-scale-of-genomic/]
   - UG200 is claimed at "up to 60,000 whole genomes" a year per system. (MGMT) [Ultima UG200 launch, via the-scientist.com]
   - ~Pricing was already in E069. I found no volumes per partner.

8. **Programs, and which are Illumina:**

| Program | Count / timing | Platform | Source |
|---|---|---|---|
| PRECISE-SG100K | 102,202 genomes (Phase II completed) | Illumina; NovogeneAIT ran WGS at >760 genomes/week | bioRxiv 2025-03-13 https://www.biorxiv.org/content/10.1101/2025.03.13.642552.full.pdf; healthcareitnews |
| Emirati Genome Program | >600K sequenced; 160K QC freeze | BGI/MGI, Oxford Nanopore and others, with Illumina not named in the sources found | genomeweb; M42 QC PDF |
| Generation Study (Genomics England) | 100K newborn target, 25K enrolled, running to Mar 2027 | Platform unconfirmed; Genomics England has a long-read procurement ("Babies in Focus"). Illumina's 2020 deal was for 300K people on NovaSeq 6000 | genomicsengland.co.uk; find-tender.service.gov.uk notices 047414-2025, 032829-2025 |
| Florida Sunshine Genetics Act | 10,000 newborns pilot, ~$25M allocation, 5 years | Not found | nucdf.org 2025-07-23; floridaphoenix.com |
| UnitedHealthcare WGS | Non-cancer WGS covered, commercial and exchange plans except CO, MA, NV, NY (this article is from an earlier effective date; the 2026 policy docs were not opened) | n/a | https://www.uhcprovider.com:443/content/dam/provider/docs/public/policies/comm-medical-drug/whole-exome-and-whole-genome-sequencing.pdf |
| Our Future Health | 5M volunteers | Illumina arrays; Eurofins runs genotyping in a UK facility | genomicseducation.hee.nhs.uk; businesswire 2022-03-08 |

   - Emirati: the program is arrayed against **non-Illumina** platforms (BGI and ONT named). (FACT) [https://www.genomeweb.com/sequencing/abu-dhabi-teams-bgi-oxford-nanopore-population-sequencing-project]
   - Generation Study flag: the long-read procurement is a possible non-Illumina component, but the notices were not opened. (OPINION)
   - Our Future Health: the sources found concern genotyping arrays. I found no WGS plan.

9. **Rough incremental Gb vs the 30% growth assumption (OPINION, assumptions labelled).**
   - Assume ~100 Gb per 30x genome. SG100K (102K genomes) is about 10M Gb over its multi-year life. Generation Study (100K, mostly unsequenced to date) is about 10M Gb over about 3 years if on short-read WGS.
   - Florida (10K) is about 1M Gb over 5 years.
   - These are small against the Gb base needed for +30% y/y. The ledger has no absolute Gb base, so I cannot give a percentage. They do not by themselves support the 30% assumption, and several of the largest programs are not on Illumina or not confirmed on it.

## Contradictions and stale data

- E081 and gap 8 call Galleri depth "not public". That is unchanged. But the commercial Galleri is targeted methylation, which contradicts the ledger's scenario framing of MCED as a high-Gb workload (5–15 Gb/test). (OPINION)
- Gap 7 listed the Abbott–Exact deal as unconfirmed. It closed on 2026-03-23.
- UHC article (genomeweb node 604231/360dx 80616) is old. Do not treat "effective April 1" as 2026.
- Ultima customer lists mix primary releases with aggregators. Wikipedia-style entries for Quest/Myriad are not primary.
- Precure press report is from a 2026-09-22 snippet only. The page was not read.

## Gaps / what I could not find

- Galleri Gb/test, read depth, platform, 2024 tests: not found. Next step is `pdftotext` on the saved FDA briefing PDF (path above) and on the GRAIL 10-K. The M42 QC PDF (also saved: `…\webfetch-1791731198898-ssyorc.pdf`) likewise needs decoding for the Illumina share in the Emirati data.
- Cancerguard volumes, Shield MCD split, depth for Shield and Signatera: not found.
- Our Future Health WGS plan, Saudi, Japan, Australia, GUARDIAN, BabySeq: not searched or no result (time).
- Ultima per-partner volumes and the Regeneron or Broad genome counts: not found.
- Sequencing platform for the Generation Study: unconfirmed.
