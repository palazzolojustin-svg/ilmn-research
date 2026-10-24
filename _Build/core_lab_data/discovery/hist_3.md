I found one document that meets your bar, for Virginia Tech. Nearly every other core only publishes its current page, and search kept returning other institutions' price lists. I did not use any web archives.

**Confirmed (opened, dated, shows platform prices)**
- **Virginia Tech (Fralin GSC):** `https://fralinlifesci.vt.edu/Core-Services/gsc/pricing.html` is stamped "Effective 11/1/25". It lists NovaSeq X (1.5B, 5B, 10B and 25B) and NextSeq 1000/2000 (P1–P4). It does not list NovaSeq 6000 or AVITI. This may be the core's live page, so it could duplicate the Sept 2024 PDF you already have, but it is a different, later-dated version.

**Found but not usable (not in the JSON)**
- **FAU Erlangen:** `https://med.fau.de/files/2025/01/Preisliste.pdf` was created and modified on 2024-10-21, and the same site's 2024/11 NGS.pdf (which you have) is the NovaSeq X Plus price-cut sheet. I could not read the tables because the PDF text is compressed, and nothing in the readable text confirms the document is the Core Unit NGS price list. It is worth a manual look.
- **Oklahoma State:** `https://ocrid.okstate.edu/site-files/documents/fy27-fee-sheets/FY27_MBGC_Fee-Schedule_updated.pdf` is the FY27 MBGC fee schedule. The URL pattern, `fy27-fee-sheets`, suggests an FY25 folder may exist, but I did not see one, so I did not guess a URL. The FY27 file returned HTTP 403 when I tried to open it, so I could not confirm it shows sequencing prices. FY27 is also newer than your FY26 copy, not older.
- **Rush:** the GMCF fee schedule `https://rushu.rush.edu/sites/default/files/2024-07/gmcf-fee-schedule-2022.pdf` is dated Oct 2021 (file metadata July 2022). That predates your window and is probably pre-NovaSeq X, and I could not read the tables, so I left it out.
- **Duke:** the blog posts I opened carried dates but no platform prices. The "same great mRNA-seq new low price" post (Oct 2025) gives only per-sample RNA-seq pricing. The 2023 NovaSeq X Plus launch posts give no dollar figure for it.
- **UChicago:** its page is undated, so it stays a current-page duplicate.
- **UT Austin GSAF:** the price list page says new rates take effect July 1, 2026, but it is probably the live page you already have. Its truncated view showed no NovaSeq X rows, and two other wiki pages (x/9KMwF, x/aBZPAg) returned empty content.
- **Calgary:** the CHGI pricing page has no PDF links and no date. A search snippet said it was updated April 1, 2026 and links a 2026–27 list, but the page I opened did not show that.
- **NGI Sweden:** the price-examples page is updated June 2026, but it gives no per-unit prices for NovaSeq X.

**No older dated documents found**
- Weill Cornell
- Utah State (likely no NovaSeq X)
- UCSD IGM
- Yale (the search tool's cached view of the page carries conflicting date labels, 7/1/2022–6/30/2023 and "FY2024-25", so it may be stale)
- UCSF CAT
- UT Southwestern
- Exeter
- Helsinki FIMM (prices are in iLab only)
- Geneva
- Graz
- MGH
- Iowa

I did not run searches aimed at the Illumina/Element/Ultima per-platform price-change announcements, so a news post on one of these cores may still exist.

```json
{"documents": [{"core_id": "virginia-tech--fralin-life-sciences-genomics-", "url": "https://fralinlifesci.vt.edu/Core-Services/gsc/pricing.html", "as_of": "2025-11", "kind": "rate_page", "note": "GSC pricing page effective 11/1/25: NovaSeq X (1.5B/5B/10B/25B) and NextSeq 1000/2000 P1-P4 rates for VT researchers; no NovaSeq 6000 or AVITI. May be the live page, later than the Sept 2024 PDF already held."}]}
```

Sources:
- [Virginia Tech GSC pricing](https://fralinlifesci.vt.edu/Core-Services/gsc/pricing.html)
- [FAU Preisliste (unverified)](https://med.fau.de/files/2025/01/Preisliste.pdf)
- [Oklahoma State FY27 MBGC fee schedule (403, unverified)](https://ocrid.okstate.edu/site-files/documents/fy27-fee-sheets/FY27_MBGC_Fee-Schedule_updated.pdf)