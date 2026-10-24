Status: I've run about 20 searches and fetches across Australia, New Zealand, Singapore, Hong Kong, Japan, Korea, Taiwan, India and Israel. Almost none of the cores in my slice publish NGS prices openly. I'm returning what I have rather than padding it.

**Notes**
- **Auckland Genomics (NZ)** is the only confirmed public price page in the slice. It shows NovaSeq X Plus and NextSeq 2000 prices in NZD, with no dates and no PDFs. Official quotes go through the InfinityX login. The iLab `show_external/3400` page is only a login page, with no prices.
- **Ramaciotti (UNSW):** the pages I opened show no sequencing prices, only "from $37/sample" for microbiome work. Everything else is quote-based.
- **AGRF:** I found only an expired 2025 promotion page (25B lane, 10% off) with no prices. Quotes are on request.
- **No public prices found** for these cores:
  - Garvan, WEHI, QIMR Berghofer, UQ IMB, Monash, SAHMRI, UTS, ANU JCSMR (a "price per sample" heading with no figure).
  - Otago Genomics: its site returned 403, and the one prices page I found (`gas.otago.ac.nz`) is for Sanger/capillary work.
  - Duke-NUS, NUS, GIS and SCELSE in Singapore.
  - HKU, CUHK, RIKEN, Kyoto, Tokyo, KAIST, Academia Sinica, NTU, IISc, NCBS.
  - HUJI (Israel): the page describes the NovaSeq 6000 but gives no costs.
- **Israel:** Technion Genome Center has a March 2020 price list in NIS covering HiSeq 2500, MiSeq, NextSeq and MinION. It has no NovaSeq line and is too old to be useful. I did not open the page. Tel Aviv University's genomics unit lists no prices.
- I did not search Korea, Japan, Taiwan or India beyond the two broad queries. I did not look for Wayback Machine copies of older Auckland versions. Both are the obvious next steps if you want more.

```json
{"cores": [
{"institution": "University of Auckland", "core": "Auckland Genomics", "country": "New Zealand", "kind": "university",
 "platforms": ["NovaSeq X", "NextSeq 2000"],
 "urls": [
  {"url": "https://www.genomics.auckland.ac.nz/pricing/", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": null},
  {"url": "https://www.genomics.auckland.ac.nz/?p=237", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": null}
 ],
 "notes": "Indicative NZD prices. Sample: NovaSeq X Plus 10B lane 2x150 (overseas partner, client-prepared libraries) NZD 4000; NextSeq 2000 2x300 (NZ partner) NZD 4,640. No AVITI or Ultima. Official quotes are through the InfinityX login at https://infinityx.ideaelan.com/auth/login (gated). No dates on page, so history would need the Wayback Machine."},
{"institution": "University of Auckland", "core": "Auckland Genomics (iLab external page)", "country": "New Zealand", "kind": "university",
 "platforms": [],
 "urls": [
  {"url": "https://uoa.ilab.agilent.com/service_center/show_external/3400", "type": "rate_page", "current": true, "public": false, "verified": true, "as_of": null}
 ],
 "notes": "Login-gated iLab page with no prices. Skip."},
{"institution": "UNSW Sydney", "core": "Ramaciotti Centre for Genomics", "country": "Australia", "kind": "university",
 "platforms": ["NovaSeq X Plus", "NextSeq 1000"],
 "urls": [
  {"url": "https://www.unsw.edu.au/science/ramaciotti/services/next-generation-sequencing", "type": "rate_page", "current": true, "public": true, "verified": true, "as_of": null}
 ],
 "notes": "No NovaSeq or NextSeq prices are published. Only 'from $37/sample' for microbiome sequencing. Quotes go through the contact page. Likely not usable."},
{"institution": "AGRF", "core": "Australian Genome Research Facility", "country": "Australia", "kind": "nonprofit_institute",
 "platforms": ["NovaSeq X"],
 "urls": [
  {"url": "https://www.agrf.org.au/25b-promo-2025", "type": "announcement", "current": false, "public": true, "verified": false, "as_of": "2025-05"}
 ],
 "notes": "I could not open the promo page (the fetch returned 404). Search results say it offered 10% off a NovaSeq X 25B lane, with samples due 30 May 2025. It shows no prices and rates are quote-based. It is useful only as a dated discount signal."}
]}
```

Sources:
- [Auckland Genomics pricing](https://www.genomics.auckland.ac.nz/pricing/)
- [Auckland Genomics NGS page](https://www.genomics.auckland.ac.nz/?p=237)
- [Auckland iLab external page](https://uoa.ilab.agilent.com/service_center/show_external/3400)
- [Ramaciotti NGS page](https://www.unsw.edu.au/science/ramaciotti/services/next-generation-sequencing)
- [AGRF 25B promo 2025](https://www.agrf.org.au/25b-promo-2025)