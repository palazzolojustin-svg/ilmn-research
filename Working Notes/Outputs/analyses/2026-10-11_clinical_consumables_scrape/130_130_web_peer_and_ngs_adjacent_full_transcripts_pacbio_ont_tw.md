# Agent 130: 130-web-peer-and-NGS-adjacent-full-transcripts-PacBio-ONT-Twist-Qiagen-Agilent-Revvity-BIO

*Model: sonnet. Run 2026-10-11 11:54:07. Cost $0.65 (API-equivalent).*

**Assignment:** Close open gaps 5, 6 and 13 (customer and competitor read-through). Earlier agents 118 and 122 did not get full transcripts. Try other routes: company IR pages (PDF transcripts and 10-Qs), Investing.com, Motley Fool, Yahoo Finance, Quartr, Public.com, Insider Monkey, MarketScreener, Seeking Alpha free pages, and EDGAR via curl or any mirror. Pull the most recent quarter (calendar Q2/Q3 2026) for: PacBio Q2'26 call (verbatim on Illumina, WGS substitution, clinical shipments, Revio pull-through), Oxford Nanopore H1'26 results (price per Gb on PromethION, clinical share, flow-cell pricing tiers), Twist FQ3'26 (10-Q customer concentration; verify the 48% top-10 figure; NGS target-enrichment demand tied to NIPT/MRD panels; 'Element', 'Ultima', 'AVITI' and 'NovaSeq' mentions), Qiagen Q2'26, Agilent FQ3'26, Revvity Q2'26 (NIPT volume, newborn screening, AVITI Dx IVD timeline), Azenta, Roche Diagnostics/KAPA, IDT/Danaher, Watchmaker and Eurofins genomics. Quote only text that mentions Illumina, NovaSeq, clinical sequencing volume, NIPT, MRD or competing sequencers, and give exact words, the speaker and the date. Also check: OMB BIOSECURE designation list status for BGI/MGI/Complete Genomics (Federal Register, congress.gov, law-firm alerts) and any Thermo Genexus placement counts. Quantify any lab-demand signals (library prep or panel volume growth) as a Gb-growth cross-check against Illumina's >30% claim. Flag contradictions with Illumina management statements.

## Key findings

I found little that is new. The full-transcript routes mostly failed, so this is mostly partial confirmation of existing ledger items.

- **PacBio's Q2'26 call, as summarized by a transcript aggregator, has no Illumina, NovaSeq, WGS-substitution, Element, Ultima or Roche mentions.** The only quantified lines were the pull-through and price quotes below. This is OPINION, because it rests on a third-party summary, not the transcript text. It is a read-through itself: PacBio management did not frame Revio as displacing short-read volume.
  - Jim Gibson (CFO): "with annualized Revio pull-through per system at approximately $202,000."
  - Mark Van Oene (CEO): "Per genome, US list price drops to $345 per 20x HiFi human genome. A 30% reduction versus our previous Spark chemistry…"
  - [allmind.ai Q2 2026 PACB call, 2026-08-05, https://allmind.ai/earnings/event/2945974]. This confirms the $202K and $345 figures in E131 and E069. No new number.
- **Qiagen Q2'26 gives a clinical NGS demand signal.** Sales of universal NGS panels for use on third-party sequencers "rose more than 20% CER" (constant exchange rates), but the genomics/NGS line as a whole rose only 2% CER, to $61M. H1 genomics/NGS was $117M, +2% CER.
  - The release names no vendor and does not mention Illumina. Panel demand growing above 20% fits the >30% Gb-growth claim only loosely, and it is only a small slice of Qiagen's genomics line. The overall line looks flat. [Qiagen Q2 2026 press release, 6-K, Aug 2026, sec.gov/Archives/edgar/data/0001015820/000101582026000049/exhibit9912026q2pressrelea.htm]. FACT.
  - The same release says QIAGEN Digital Insights (its bioinformatics unit) grew "good single-digit CER", "led by the clinical business, which now represents about half of QDI sales." FACT.
- **Twist FQ3'26 NGS revenue was $61.8M, +12% y/y and +8% sequentially.** Twist's total revenue was $118.4M (+23%), and DSPS (DNA synthesis and protein solutions) grew 39%. FACT. [Twist 8-K Ex. 99.1, FQ3'26, sec.gov/Archives/edgar/data/0001581280/000158128026000044/twst-2026630xex991.htm; GenomeWeb search snippet].
  - NGS grew at less than a third of the DSPS rate. A +12% target-enrichment growth rate for MRD/NIPT-type panels is well below Illumina's >30% Gb growth on connected instruments. It is a weak cross-check, because it mixes revenue with volume and includes research. OPINION.
- **The Twist 48% top-10 figure is still unverified, and I could not confirm it from the 10-Q.** The fetch of the 10-Q (acc. 0001581280-26-000047) returned no customer-concentration table and no Illumina, NovaSeq, Element, Ultima or AVITI mentions. The fetch returned only part of the filing, so this is not conclusive. The page said risk factors and MD&A exist but did not show them. This tightens E414: the 48% rests on the MarketBeat summary alone.
- **BIOSECURE and the 1260H list: new detail on E420.** DoD released an updated 1260H list on 9 Jun 2026. The Mondaq alert says it names BGI Group "plus 7 affiliates", MGI Tech and Novogene, and does not mention Complete Genomics. [Mondaq/BIOSECURE update, 2026-06-09, https://www.mondaq.com/china/life-sciences-biotechnology-nanotechnology/1801038/biosecure-update-1260h-list-released]. FACT.
  - Under the Act (Section 851 of the FY2026 NDAA), a 1260H listing is the first step toward becoming a "biotechnology company of concern". The OMB list is due by 18 Dec 2026. Prohibitions take effect 60 days after the FAR revision, "likely sometime in 2027". Existing contracts are grandfathered for five years from the FAR revision date. FACT/OPINION on the timing.
  - The ledger (E420) says "BGI Group, BGI Genomics and MGI Tech". The Mondaq alert does not mention BGI Genomics by name, and it adds Novogene, which E420 does not list.
  - A search snippet attributed to a different source says the latest list includes Complete Genomics. I could not verify that, and it conflicts with the Mondaq alert and E420.
  - The ledger says MGI is selling Complete Genomics to Swiss Rockets. If it is on the list, that could matter to the sale.
- **ONT H1'26 headline confirms E131 and adds one fact:** revenue £116.7M (H1'25 £105.6M), +12.3% constant currency, gross margin 62.2% (58.2%). PromethION grew 15.7%, driven by P2i. Management credits margin to "yield improvements across Flow Cells, scale and increased adoption of the new pricing model." [Oxford Nanopore H1 2026 results via search summary, Aug 2026; directorstalkinterviews.com and nanoporetech.com ONT-H1-26 presentation]. FACT. The PDF would not parse, so there is still no price per Gb and no tier detail.
  - The gross-margin rise alongside a pricing-model change suggests ONT's volume-tier discounts are not hurting its margin. That is a different position from Illumina's.
- **Revvity Q2'26 (call 4 Aug 2026):** revenue was $711M, 3% pro forma organic growth. Diagnostics grew 11% organic. Reproductive Health grew double digits on newborn screening. The outlook was raised to 4-5% pro forma organic growth. FACT. [MarketBeat/Barchart summaries of the Revvity Q2'26 call, 2026-08-04 to 08-08]. I did not obtain the transcript, so I have no quotes on AVITI Dx or NIPT volume.
- **Agilent FQ3'26:** revenue $1.88B (+8.1% reported, +7.3% core). The Life Sciences and Diagnostics Markets Group had $746M (+11% reported, +10% core). The release has no NGS line. FACT. [Agilent 8-K Ex. 99.1, FQ3'26]. Agilent and Element have a co-marketing partnership (SureSelect on AVITI, expanded Aug 2023). FACT. [elementbiosciences.com]. That is old and not new evidence.

## Contradictions and stale data

- **BIOSECURE/MGI:** E420 lists BGI Genomics by name, but Mondaq's 9 Jun 2026 list names BGI Group plus affiliates, MGI Tech and Novogene. The snippet claiming Complete Genomics is on the list is unverified and conflicts with E420.
- **No contradiction found with Illumina management claims.** Qiagen's panel growth of >20% and Twist's NGS growth of +12% are consistent with, but do not test, the >30% Gb claim.

## Gaps / what I could not find

- **Full transcripts not obtained** for PacBio, Twist, Qiagen, Revvity or Agilent.
  - Sahm Capital returned 404.
  - Webull gave a certificate error.
  - MarketBeat pages returned the wrong page or a 503.
  - The PacBio IR PDF returned 403.
  - Quartr and roic.ai were not tried.
  - The PacBio findings above come from a single aggregator summary.
- **ONT price per Gb, flow-cell tiers and clinical share:** the PDFs would not parse. A saved copy is at `C:\Users\palaz\.claude\projects\C--Users-palaz-OneDrive-Documents-ILMN-Claude-Code-Local-Folder--Build-sandbox\ee45c64a-df67-4550-b364-149cae9a8562\tool-results\webfetch-1791737583397-jstryi.pdf`. It needs local PDF text extraction (for example, the Read tool with `pages`).
- **Twist 10-Q customer table:** needs the full filing text. Try EDGAR R pages or full-text search.
- **Not searched:** Azenta, Roche/KAPA, IDT/Danaher, Watchmaker and Eurofins genomics.
- **Thermo Genexus placement counts:** searches returned only older product announcements, with no 2026 figures.
- **Complete Genomics 1260H status** remains unconfirmed. I could not fetch the Ropes & Gray or Federal Register text.
