Fetches fail (likely bot-blocking), but the search results showed the Exeter prices. I'm returning now with what I have.

**Notes**
- Only one core in this slice published sequencing prices that I could confirm: the University of Exeter Sequencing Service. It lists internal and commercial rates in GBP excluding VAT. Sample line: "NovaSeq X 10B single lane 300 cycle, internal £1,800 (commercial £2,016)". Search snippets also showed 1.5B, 10B and 25B full flow cells.
- My WebFetch calls to the Exeter pages returned 404 (possibly bot-blocking). The prices come from search-result text, so they are **not verified by opening the page**. The snippets showed no effective date, so `as_of` is null. I found no older versions.
- Edinburgh has a "Pricing changes at Edinburgh Genomics" post (an April 1 Illumina price-list change). It redirected to the Clinical Research Facility site and I couldn't open it. It gave no actual prices and no date. I list it as an unverified announcement.
- CRUK Cambridge Institute runs NovaSeq X Plus and NextSeq 2000 but showed no public prices. Its sequencing is mostly restricted to the University of Cambridge.
- UCD Conway has a NextSeq 2000 page and TCD (TrinSeq) has a MiSeq/NovaSeq 6000 page. Neither shows prices.
- Nottingham DeepSeq, Durham and Glasgow Polyomics are quote-only or showed no NGS prices. For Oxford, Manchester, Newcastle, Liverpool CGR, Bristol, Cardiff, Leeds, Sheffield, Dundee, Birmingham, UCL, Imperial, King's, QMUL and Queen's Belfast, my searches returned nothing relevant. That means no public prices were found, not that none exist. I ran only about a dozen searches, so this slice needs more targeted follow-up.
- I found no UK or Irish AVITI or UG 100 price pages.

```json
{"cores": [
{"institution": "University of Exeter", "core": "Exeter Sequencing Service", "country": "UK", "kind": "university",
 "platforms": ["NovaSeq X"],
 "urls": [
  {"url": "https://exeter.ac.uk/research/facilities/sequencing/pricing/internal", "type": "rate_page", "current": true, "public": true, "verified": false, "as_of": null},
  {"url": "https://exeter.ac.uk/research/sequencing/pricing/internal", "type": "rate_page", "current": true, "public": true, "verified": false, "as_of": null},
  {"url": "https://exeter.ac.uk/research/facilities/sequencing/pricing/commercial", "type": "rate_page", "current": true, "public": true, "verified": false, "as_of": null},
  {"url": "https://exeter.ac.uk/research/sequencing/pricing/commercial", "type": "rate_page", "current": true, "public": true, "verified": false, "as_of": null}
 ],
 "notes": "Seen in search snippets only; WebFetch returned 404. NovaSeq X 10B single lane 300 cycle internal £1,800 (commercial £2,016), excl. VAT. Full flow cells: 1.5B £3,605, 10B £14,400, 25B £24,075 internal. The two URL patterns (/facilities/sequencing/ and /sequencing/) may be the same page. No dates shown, no history found."},
{"institution": "University of Edinburgh", "core": "Edinburgh Genomics / Genetics Core (Clinical Research Facility)", "country": "UK", "kind": "university",
 "platforms": ["NextSeq 2000", "NovaSeq"],
 "urls": [
  {"url": "https://genomics.ed.ac.uk/node/75", "type": "announcement", "current": false, "public": true, "verified": false, "as_of": null}
 ],
 "notes": "Post titled 'Pricing changes at Edinburgh Genomics' (new Illumina price list from April 1; year unknown). It redirects (301) to clinical-research-facility.ed.ac.uk/core-services/geneticsnode/75, which returned 404. No prices seen. Contact is the business manager. The CRF Genetics Core page (clinical-research-facility.ed.ac.uk/core-services/genetics) was not opened."}
]}
```

Sources:
- [Exeter internal costs](https://exeter.ac.uk/research/sequencing/pricing/internal)
- [Exeter commercial costs](https://exeter.ac.uk/research/sequencing/pricing/commercial)
- [Pricing changes at Edinburgh Genomics](https://genomics.ed.ac.uk/node/75)