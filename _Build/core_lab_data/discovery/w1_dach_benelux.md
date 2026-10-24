I found only a few cores in this slice, well short of the 15–30 target. Most cores in Germany, Austria, the Netherlands, Belgium and Luxembourg don't publish sequencing prices publicly, or their pages don't show up in search. I found no public price pages for FGCZ, VBCF, DKFZ, EMBL, Cologne, Dresden, Kiel, Tübingen, Leiden, Utrecht, Amsterdam, Nijmegen, VIB Nucleomics, Ghent, Leuven or LCSB. I also found none for Basel/QGF, Munich or Hamburg. VBCF says fees are given on request. Lausanne GTF gives only an AVITI "from ~CHF 200 per 100M reads" in a May 2026 newsletter.

- **Best source: EPFL GECF (Switzerland).** It has a dated PDF for each price change, covering NovaSeq and AVITI/AVITI24, and its news log records the cuts. I didn't open the PDFs, because the fetch returned raw PDF content, so I have no sample price line for any of them.
- **Pages I opened:**
  - EPFL GECF rate page (confirmed AVITI, NovaSeq, MiSeq and ONT are priced).
  - Geneva iGE3 fee page ("NovaSeq" only, no model named, no date).
  - Bern NGS homepage (confirmed it has a pricelist link and a NovaSeq X Plus).
- **Not opened:** the PDFs for Bern, MDC, FAU and MOseq came back as binary, so those are unverified. Their contents come from search snippets only.
- **Bern price list.** The only sequencing-relevant item in the May 2024 PDF snippet was library prep, and it is the only Bern price document I found. It is the 2024 version, so I have marked it not current; I couldn't find a newer one.
- **MDC Berlin lists** are all pre-2024 (the one I read is dated April 2021, covering NovaSeq 6000 S1/S4), so they're useful only as old history. The other two MDC pages show no date.
- **FAU Erlangen** has a dated old-versus-new comparison (7 Oct 2024) for the NovaSeq X Plus, with new prices from 1 Jan 2025. It lists per-service prices, not per-lane prices.

```json
{"cores": [
{"institution": "EPFL", "core": "Gene Expression Core Facility (GECF)", "country": "Switzerland", "kind": "university",
 "platforms": ["NovaSeq", "AVITI", "AVITI24"],
 "urls": [
  {"url": "https://www.epfl.ch/research/facilities/gene-expression-core-facility", "type": "announcement", "current": true, "public": true, "verified": true, "as_of": "2026-09"},
  {"url": "https://epfl.ch/research/facilities/gene-expression-core-facility/page-154614-en-html", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": "2026-09"},
  {"url": "https://www.epfl.ch/research/facilities/gene-expression-core-facility/wp-content/uploads/2026/09/GECF-price-list-for-EPFL-users-09-September-2026.pdf", "type": "pdf", "current": true, "public": true, "verified": false, "as_of": "2026-09"},
  {"url": "https://www.epfl.ch/research/facilities/gene-expression-core-facility/wp-content/uploads/2026/02/GECF-price-list-for-EPFL-users-15-February-2026.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2026-02"},
  {"url": "https://www.epfl.ch/research/facilities/gene-expression-core-facility/wp-content/uploads/2025/07/GECF-price-list-for-EPFL-users-01-July-2025.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2025-07"},
  {"url": "https://www.epfl.ch/research/facilities/gene-expression-core-facility/wp-content/uploads/2025/03/GECF-price-list-for-EPFL-users-01-March-2025.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2025-03"},
  {"url": "https://epfl.ch/research/facilities/gene-expression-core-facility/wp-content/uploads/2024/11/GECF-price-list-for-EPFL-users-01-November-2024.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2024-11"},
  {"url": "https://epfl.ch/research/facilities/gene-expression-core-facility/wp-content/uploads/2024/07/GECF-price-list-for-EPFL-users-01-July-2024.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2024-07"},
  {"url": "https://www.epfl.ch/research/facilities/gene-expression-core-facility/wp-content/uploads/2023/09/GECF-price-list-for-EPFL-users-October-2023.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2023-10"},
  {"url": "https://www.epfl.ch/research/facilities/gene-expression-core-facility/wp-content/uploads/2023/07/GECF-price-list-internal-users-July-2023.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2023-07"}
 ],
 "notes": "CHF, internal EPFL users; per-run price excludes or includes labour/chip depending on item. The news log records cuts: NovaSeq in 2024, AVITI and NovaSeq in 2025 (Mar 2025, Oct 2025 'strong decrease in NovaSeq prices'), NovaSeq 300-cycle in early 2026, AVITI24 upgrade Nov 2025. Unseen: the Feb 2026 and Sep 2026 PDFs and the 2024 to 2025 intermediate versions. I did not extract a sample price line."},
{"institution": "University of Geneva", "core": "iGE3 Genomics Platform - Next Gen Sequencing", "country": "Switzerland", "kind": "university",
 "platforms": ["NovaSeq"],
 "urls": [{"url": "https://ige3.genomics.unige.ch/fees", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": null}],
 "notes": "Indicative only, no date. Sample: NovaSeq PE100 ~350M-read fraction CHF 1,750; SR100 CHF 1,200. Model (NovaSeq X vs 6000) not stated; no AVITI. Prices are per 'fraction' of a flow cell. Quotes on request."},
{"institution": "University of Bern", "core": "Next Generation Sequencing (NGS) Platform", "country": "Switzerland", "kind": "university",
 "platforms": ["NovaSeq X", "MiSeq i100", "PromethION"],
 "urls": [
  {"url": "https://www.ngs.unibe.ch/", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": null},
  {"url": "https://ngs.unibe.ch/unibe/portal/fak_vetmedizin/micro_ngs/content/e1539654/PriceList_NGSP_MAY_2024003.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2024-05"}
 ],
 "notes": "Homepage shows a pricelist shortcut and a new NovaSeq X Plus. The May 2024 PDF has Tariff 1 (internal) and Tariff 2 (external); snippet showed only library prep (e.g. PCR-free DNA lib 225/269 CHF). Sequencing run prices unseen, and a newer pricelist likely exists behind the shortcut. Should be checked."},
{"institution": "University of Lausanne / CHUV", "core": "Genomic Technologies Facility (GTF)", "country": "Switzerland", "kind": "university",
 "platforms": ["AVITI24", "NovaSeq"],
 "urls": [
  {"url": "https://wp.unil.ch/gtf/news-letter/", "type": "announcement", "current": true, "public": true, "verified": false, "as_of": "2026-06"},
  {"url": "https://wp.unil.ch/gtf/files/2026/06/gtf-newsletter-–-fbm-edition.pdf", "type": "announcement", "current": true, "public": true, "verified": false, "as_of": "2026-06"}
 ],
 "notes": "No rate card found. The newsletter (May/June 2026) says AVITI pricing starts near CHF 200 for ~100M reads and goes up to 25B reads. Contact contactGTF@unil.ch. Weak lead."},
{"institution": "FAU Erlangen-Nürnberg", "core": "Core Unit NGS (CU NGS)", "country": "Germany", "kind": "academic_medical_center",
 "platforms": ["NovaSeq X Plus"],
 "urls": [{"url": "https://www.med.fau.de/files/2024/11/NGS.pdf", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2024-10"}],
 "notes": "Old-vs-new price comparison dated 2024-10-07, new NovaSeq X Plus prices effective 2025-01-01 (per search snippet; PDF not readable). Sample: bulk RNA-seq EUR 395 -> 245; 3' scRNA-seq 2,995 -> 1,945. Per-service prices, not per lane. A current official list was not found."},
{"institution": "MDC Berlin", "core": "Genomics Platform (NGS)", "country": "Germany", "kind": "nonprofit_institute",
 "platforms": ["NovaSeq 6000"],
 "urls": [
  {"url": "https://www.mdc-berlin.de/media/39029", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": "2021-04"},
  {"url": "https://www.mdc-berlin.de/media/39941", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": null},
  {"url": "https://www.mdc-berlin.de/media/38662", "type": "pdf", "current": false, "public": true, "verified": false, "as_of": null}
 ],
 "notes": "Old lists (the clearest one valid from 2021-04-15), MDC and Charité users only. NovaSeq 6000 S1 300-cycle about EUR 5,420. No 2024 to 2026 list found. Only useful as history."},
{"institution": "Medical University of Innsbruck", "core": "MOseq (Molecular sequencing facility)", "country": "Austria", "kind": "academic_medical_center",
 "platforms": ["NovaSeq"],
 "urls": [{"url": "https://moseq.i-med.ac.at/wp-content/uploads/2025/12/MOseq-Costs-Examples.pdf", "type": "pdf", "current": true, "public": true, "verified": false, "as_of": "2025-12"}],
 "notes": "Per-sample cost examples for internal and external users (QuantSeq 3' library prep plus sequencing from about EUR 100 internal / 115 external, per snippet). Platform and lane prices unconfirmed. PDF not readable."},
{"institution": "Medical University of Graz", "core": "NovaSeq X Plus (Institute for Diagnosis and Research in Human Genetics)", "country": "Austria", "kind": "academic_medical_center",
 "platforms": ["NovaSeq X Plus"],
 "urls": [{"url": "https://forschungsinfrastruktur.bmfwf.gv.at/de/fi/novaseq-x-plus-sequencing-system_6458", "type": "rate_page", "current": true, "public": true, "verified": false, "as_of": null}],
 "notes": "Registry listing only, no prices (fees on request). Weak lead; likely not usable."}
]}
```

Sources:
- [EPFL GECF](https://www.epfl.ch/research/facilities/gene-expression-core-facility)
- [iGE3 fees](https://ige3.genomics.unige.ch/fees)
- [Bern NGS](https://www.ngs.unibe.ch/)