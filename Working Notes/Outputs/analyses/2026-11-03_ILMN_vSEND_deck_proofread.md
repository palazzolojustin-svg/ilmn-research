# ILMN_vSEND deck: proofread and fix list (3 Nov 2026)

Source: `C:\Users\palaz\Downloads\ILMN_vSEND.pdf` (26 slides). I read every slide as an image and as extracted text. I checked the arithmetic on every chart and table that can be recomputed. I checked the quotes and facts most likely to be challenged against the Working Notes. Slides 8–12 and 20–21 are progressive builds that repeat the same panels, so an error in a repeated panel needs fixing on every copy.

## Tier 1: fix before sending

1. **The valuation section is missing (slide 26).** The deck ends on the "Valuation" divider. Nothing supports the $145.6 price target, the 35.6% downside or the ~1.9x risk/reward on slide 1. Either add the valuation slides or check that the export didn't cut them off.
2. **Two different current share prices.**
   - Slides 1 and 14 imply $226.06 ($2,260.60 ÷ 10 shares; $145.6 ÷ $226.06 = 35.6% downside).
   - Slides 18 and 21 anchor the reverse DCF at $235.99 with 0.0% implied upside. Your model uses $235.99 as the current price.
   - At $235.99, the downside to $145.6 is 38.3%. Pick one price and date, and use it everywhere.
3. **Slide 7: equity value reads "34.41M".** It should be about **$34.4B**.
4. **Slide 7: wrong company name.** The subtitle says "Illumina Biosciences Inc". It should be **Illumina, Inc.**, as on slide 1. There is also a double space in "of  sequencing".
5. **Slide 19: wrong call label.** The Tycho Peterson stocking-orders question is labelled "Q4 2026 Analyst Question". It is from the **Q3 2026** call (30 Oct). The Q4 call hasn't happened yet, and the answer itself says "Q3 looked very much like Q2". It appears twice.
6. **Slide 12: typo in the headline.** "justify **it'** valuation" should be "**its** valuation".
7. **Slide 14: typos in the thesis bullets**, on the slide everyone reads closely:
   - "best possible **outcoming**" → "outcome"
   - "residual cohort **sill** on the 6000" → "still"
   - "and **this** are individually bigger drags" → "thus"
   - "Management is guiding for **now** conversion headwind into 2027E". This almost certainly means "lower". Don't write "no": management said the headwind will be "lower in 2027 than in 2026" (Q3'26 call, which you quote on slide 17).
   - "a residual 40% of **revenue**" should be "40% of **high-throughput** revenue", per slide 21. As written, it reads as 40% of total company revenue.
   - "$2260.60" → "$2,260.60"
8. **Slide 14: misquote.** The bullet says large clinical accounts guide for "step **reductions**" in quotation marks. GeneDx's CFO said "step **improvements** in 2027" (Q2'26 call, and your own quote on slide 23). Change the quoted word or remove the quotation marks.
9. **The 3.4x / 41% / 17% callout uses Q2'26 data next to Q3'26 charts (slides 8, 9 and 10, via the builds).**
   - In Q3'26 the 6000 was 40% of high-throughput revenue on 16% of the gigabases (slide 21 and the slide 9 line chart: 84%/60%). That is **3.5x**, as your own slide 20 chart shows for Q3'26.
   - Update the callout to "3.5x (40% of HT revenue on 16% of the volume)". The "70% revenue lost per Gb" figure stays about right (1 − 1/3.5 = 71%).
10. **Slide 8: the Barclays quote contradicts the chart beside it.** The quote says "overall X Gb % increased 500bps to 76%" in Q1'26. Your chart shows the X at 82% of high-throughput gigabases in Q1'26, up 200 bps. Your notes flag that Barclays' 76% is the clinical share, not the overall share. Add "[clinical]" to the quote or footnote it. Otherwise the quote looks like it disproves your chart.
11. **Slide 20: two bars don't match the slide 8 prices.**
    - The bars are each flow cell's price per Gb divided by the 25B's $2.81.
    - S4: $6.30 / $2.81 = **2.2x**, but the slide shows 2.1x.
    - 1.5B: $8.72 / $2.81 = **3.1x**, but the slide shows 2.9x.
    - S1 (5.6x), S2 (3.8x) and 10B (1.5x) tie out.
    - Fix the bars and the callout ("vs. 2.1x for an S4 user" → 2.2x).
12. **Slides 4 and 5 are both titled "Sequencing Explained", with the same top half.** If this is meant to be a build, fine. If not, one of them is a leftover draft. Slide 5 also drops the "End Market Users" panel.

## Tier 2: substantive accuracy and consistency (fix if time allows)

13. **Slide 4/5: "The delta between industry instrument sales growth and revenue growth in Q2 was 30%+."**
    - The data on slide 5 is Illumina's sequencing **output (Gb) growth of >30%** against consumables revenue growth of about 4%. That is a gap of about 26 points, and it has nothing to do with industry instrument sales.
    - Suggested wording: "ILMN's Q2 Gb volume grew >30% vs. ~4% consumables revenue growth ex-China."
14. **Slide 4/5: "Synthesizes via reverse terminators"** should be "**reversible** terminators". Ultima runs "on a spinning wafer instead of a **flow** cell".
15. **Slide 4/5: "Long Read: Reads 1M+ bases continuously"** overstates typical long reads. PacBio HiFi reads are about 15–25 kb. Only ultra-long ONT runs pass 1 Mb. Suggest "10K to 1M+ bases".
16. **Slide 4: "Software assembles and reads with a reference genome"** is garbled. Use "Software aligns the reads to a reference genome to identify genetic differences."
17. **Slide 12: the +1–2 pts label narrows what management said.**
    - The slide says "management's own estimate of what new **data services** add".
    - The CFO said **new products** add 1–2 points (Q2'26 and Q3'26 calls). On Q3, that was new products, data and BioInsight together (multiomics, constellation and so on), not data services alone.
    - Relabel the panel as "new products (incl. data/BioInsight)", or a bull will call it a mischaracterization.
18. **Slides 10 and 11: "NovaSeq X 25B — 35B fragments — 10,500 Gb — ~84 genomes".**
    - A "25B" flow cell listed with 35B fragments looks like a typo. 10,500 Gb is the top of the 25B's 8–10.5 Tb range at upgraded yields.
    - Either footnote it ("at max yield") or use about 26B fragments, about 8,000 Gb and about 64 genomes.
    - The "spans about 350x" headline depends on the 10,500 figure.
19. **Price per Gb for the NovaSeq X is shown three ways.**
    - Slide 8 shows the 25B at $2.81 and the **35B at $2.00**. The 35B hasn't been priced; you quote Thaysen saying so on slide 22. Label the $2.00 "est." or "launch target".
    - Slides 22 and 23 use $2.00/Gb as the X Plus cost. That is Illumina's launch claim for the 25B, not the $2.81 you use elsewhere.
    - Add a footnote, or the −50% and −25% competitor gaps look inflated or understated depending on which figure the reader picks.
20. **Instrument price for the NovaSeq X is shown two ways.** Slide 4/5 says $1.1mn and slides 22/23 say $1.15M. Align them. (The $1.350M on slide 8 is pull-through, which is fine, but write it as $1.35M.)
21. **Slide 16/17: "12% 28E EPS revision".** $6.22 → $7.06 is +13.5%. Check which starting point the bracket uses.
22. **Slide 18: "We believe that 21x 2031 EBITDA is EXTREMELY generous".** The table uses **20.5x**. Make them match.
23. **Slide 18: "(-) Operating Expenses (D&A, SBC)"** reads as if D&A and SBC are included. It presumably means **excluding** them ("ex-D&A, SBC"). Also, the 2031 EBITDA margin falls (32.8% → 32.4%) while gross margin rises, so check the 2031 opex.
24. **Slide 21 bar chart legend.** The FY26E bar is labelled "Street 26E" but is coloured like the buyside series, and the legend has no Street entry.
25. **Slide 22: the "Total clinical therapy selection cases y/y" chart** has two series but only one in the legend. The orange series is unlabelled. The x-axis also runs FY'25, Q2'25, Q3'25, Q1'26, Q2'26, skipping Q4'25 and mixing a full year in with quarters.
26. **Slide 22: "increase px by half of what you increase volume by".** The maths that follows (40% more volume → about 15% lower price per Gb) treats this as revenue growing at half the volume growth, not price increasing. Suggest: "revenue grows ~half as fast as volume — at +40% volume that's ~15% lower price per Gb vs. our ~20% — which implies discounting accelerates."
27. **Numbering mismatch.** The Thesis Overview (slide 14) numbers Why Now as 1, Conversion as 2 and Discounting as 3. The body slides call Conversion "Thesis 1" and Discounting "Thesis 2".
28. **Slide 23: missing sources.** The R&A consumables chart (−6.1% / 1.7% / 2.8%) doesn't say whose 2027E/28E these are (Street?). The "Sequencing as % of all-in cost per genome" chart has no source. That chart shows clinical at 19%, while the quote beside it says "5%-10%", so a footnote helps.
29. **Tone (your call).** "Management Bullshittery" (slide 19 title), "Absolute Nothingburger" (slide 19) and "Management **Doctored** Cohort Study" (slide 20). "Doctored" alleges falsification. "Cherry-picked" makes the same point without the accusation. If this goes to judges or anyone outside the team, consider softening all three.

## Tier 3: small typos and polish

**Slide 1**
- "Rishab Dey Also worked" → "also"
- "4 - 12 Months|" → "4–12 Months |" (spacing)

**Slide 3**
- "the complete set of DNA in your cell" → "cells"
- "how to build a protein" → "proteins"
- "Advancements… **has** given rise" → "have"
- "sequenced and **compare** it" → "compared", and remove the double space before "is"
- add a period at the end of the paragraph
- "~ $2.7B" → "~$2.7B"
- The Medicare chart shows 2025 on the axis with no bar.
- The numbered list is misaligned (item 1 is indented differently from items 2–4).

**Slide 4/5**
- "Element AVITI/**Vitari**" vs "**VITARI**" on slide 22
- "multi year" → "multi-year"
- Slide 4 has no periods at the ends of items 1–3; slide 5 has them.
- "(ex: Element) for cost **in numerous labs** around the country" repeats "labs".
- "10x's imaging-based spatial platforms **offer**" → "offers"
- "~61.8%" is falsely precise next to "~60–70%".

**Slide 7**
- XLEAP is spelled four ways across the deck: "XLeap", "XLEAP", "X-Leap" (slide 10) and "Xleap" (slide 8 quote). Use **XLEAP**.
- "converting users… to their **XLeap systems**" → "NovaSeq X systems". XLEAP is the chemistry, not the machine.
- "faces **little** repercussions" → "few"
- There is a stray orange dashed icon next to "Company" in the footer.
- In the growth chart, "Clinical consumables" and "Sequencing consumables (total)" are nearly the same orange.
- In the pie, US and Europe are both orange. In the stacked bar, Consumables and Service are both orange.
- The individual ownership figures sum to <0.07%, while the text says 0.06%.

**Slide 8**
- There is a stray word "**sizes**" after "small labs and teaching."
- "Luke Sergott Q1 '26" → "Q1'26"
- "$1.350M" → "$1.35M"
- The subtitle reads "one-time uses in the instrument". Suggest "single-use".

**Slide 9**
- The subtitle is ungrammatical. Suggest: "Illumina's volume shift hasn't produced material top-line improvement, so the consensus story is unfounded."
- The +30% / −19% / +6% bars are roughly consistent (1.30 × 0.81 = +5.3%). That is fine if the volume figure is a floor.

**Slide 10**
- "billions of  strands" has a double space.

**Slide 11**
- The title "The Value Chain" doesn't match the content.
- The stacked bar labels mix "2023" with "FY24/FY25". Use "FY23".

**Slide 12**
- The orphaned "2027E revenue growth" table header has nothing under it.
- "Thaysen, Q3'26" vs "Dhingra, Q3 '26": make the format consistent.

**Slide 14**
- "guiding on  conversion" has a double space.
- "despite horrible track record" → "despite a horrible track record"
- "discounts… **provide**" → "provides"

**Slide 16**
- "MRNA" → "mRNA"

**Slide 17**
- "question of  acceleration" has a double space.

**Slide 18**
- "sell-side analysts expectations" → "analysts'"
- "HSD growth in **‘**27" has a backwards apostrophe (’27).
- The Street Analyst quote ("But this ignores…") has no opening quotation mark.
- "themselves. .. Illumina" → "themselves… Illumina"
- The Meister bars are "shares owned *after* sale". The ~78% is measured from after the first sale, so the true reduction from the starting stake is larger. That's fine but understated.

**Slide 19**
- "north star of  HSD" has a double space.

**Slide 20/21**
- "$/gb" → "$/Gb"
- "attributable to **the** 6000 residual base"
- "smaller more expensive smaller volume cells used by smaller labs" repeats "smaller" three times.
- The JPM quote ("We do not intend…") has no opening quotation mark.
- The **yellow highlight on "Q1 26"** is an editing artifact.
- "– ILMN Former" has a truncated attribution (Former what?).
- "they don't [get] reimbursed"
- "U.S/Can" → "U.S./Canada"
- "(Natera Tempus Caris" → "(Natera, Tempus, Caris"
- The "Our View" box is a run-on sentence.

**Slide 21**
- "We plan to discontinue…" has no opening quotation mark.
- "worse than **‘**25" has a backwards apostrophe.

**Slide 22**
- The TD Cowen quote names no speaker.
- The Roche quote ("I think the CGP…") has no opening quotation mark.
- "per gb" → "per Gb"
- "which **implied**" → "implies"

**Slide 23**
- "evidence **point**" → "points"
- "street" → "Street"
- The Oxford Nanopore quote has no closing quotation mark.
- The SRA bar chart has no legend for grey (share of runs) vs orange (share of the y/y increase).

**Slide 25**
- "BillionCellAtlas" → "Billion Cell Atlas", as on slide 17
- "produced as derivative of MRD and WGS accelerates" → "produced as MRD and WGS accelerate underlying volume growth…"
- "deescalation" → "de-escalation"
- "We view the… reaction out of Q3 **of** evidence" → "as evidence"
- "expand discount" → "expand discounts"
- "existing customer" → "existing customers"

## What I checked and found correct

- **DCF (slide 18):** every revenue, gross profit, EBITDA, margin and growth figure recomputes. EV, equity value and per-share value tie out: 31,706.9 + 5,222.6 = 36,929.5; less 823 = 36,106.5; ÷ 153 = $235.99.
- **Implied price per Gb rows (slide 18):** the 2026E and 2027E rows tie to revenue growth at 25% and 30% Gb growth.
- **6000/X multiple series (slide 20):** every point recomputes from the slide 9 share data.
- **Revenue mix:** consumables / instruments / service sum to 100% each year.
- **Meister stake:** −77.8%, so "~78%" is right.
- **Competitor gaps:** VITARI −40%/−50% and AXELIOS −35%/−25% are arithmetically right.
- **SRA share:** 2.3% → 7.6% is "more than tripled".
- **LT margin misses:** −370 bps and −390 bps are right.
- **Throughput table:** the NextSeq P1–P4 and NovaSeq 6000 SP/S2/S4 outputs match the specs.
