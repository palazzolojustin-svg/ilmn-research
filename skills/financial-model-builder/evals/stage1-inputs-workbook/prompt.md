---
tags: [financial-model-builder]
max_turns: 40
timeout_seconds: 1200
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

The parsed Illumina data is in model_data_raw.json. Set up the inputs workbook for the ILMN model with these choices: reporting and trading currency USD, history from 1Q25, quarterly estimates through 4Q28 and then 2029 and 2030 as annual columns, five cases (Disaster/Bear/Base/Bull/Blowout), comments from the workbook, author "Palazzolo, Justin J", current price from a Bloomberg formula with 205.09 as the typed fallback, valuation on EV/Adj. EBITDA with two year-end target blocks (YE2027 on FY2028 Adj. EBITDA, YE2028 on FY2029).

Revenue tree: Product revenue = Consumables (Sequencing Consumables + Microarray Consumables) + Instruments (Sequencing Instruments + Microarray Instruments); plus Service & Other revenue. The four consumables/instruments lines and Service & Other each get a y/y growth driver. Costs: Cost of Products Sold and Cost of Services Sold with gross-margin % drivers, SG&A and R&D as % of revenue. Keep the standard income statement, balance sheet and cash flow drivers.

Write all of that into the workbook, add the estimate grids, and tell me exactly what I still have to fill in. Do not fill any estimates yourself.

Input files: model_data_raw.json
