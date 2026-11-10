import sys, openpyxl
path = sys.argv[1]
wb = openpyxl.load_workbook(path)


def clear_rows(ws, r0, r1, ncols):
    for r in range(r0, r1 + 1):
        for c in range(1, ncols + 1):
            ws.cell(r, c).value = None


def write_rows(ws, r0, rows):
    for i, row in enumerate(rows):
        for j, v in enumerate(row):
            ws.cell(r0 + i, 1 + j).value = v


BB = "Business Breakdown"

# Revenue Tree: parents, kinds and labels of the analyst's new lines; tree order parent-first
ws = wb["Revenue Tree"]
clear_rows(ws, 4, 26, 15)
write_rows(ws, 4, [
    ["product", "Product Revenue", None, "sum", None, None, None, "Total Product Revenue", BB],
    ["consumables", "Consumables", "product", "sum", None, None, None, "Total Consumables", BB, None, None, None,
     "sum what is necessary to get to this on revenue build"],
    ["seq_cons", "Sequencing Consumables", "consumables", "sum", None, None, None, "Sequencing Consumables", BB, None, None, None,
     "calcualted via sum of sequencing consumables ex china and china seq consumables rev on revenue build"],
    ["seq_cons_exchina", "Sequencing Consumables Ex-China", "seq_cons", "sum", None, None, None, "Sequencing Consumables Ex-China", BB],
    ["clins_cons", "Clinical Consumables Ex-China", "seq_cons_exchina", "growth", None, None, None, "Clinical Consumables Ex-China", BB],
    ["research_cons", "Research & Applied Consumables Ex-China", "seq_cons_exchina", "growth", None, None, None, "Research Consumables Ex-China", BB],
    ["china_seq_cons", "Greater China Sequencing Consumables", "seq_cons", "growth", None, None, None, "China Seq Consumables Revenue", BB],
    ["array_cons", "Microarray Consumables", "consumables", "growth", None, None, None, "Microarray Consumables", BB],
    ["instruments", "Instruments", "product", "sum", None, None, None, "Total Instruments", BB],
    ["seq_inst", "Sequencing Instruments", "instruments", "growth", None, None, None, "Sequencing Instruments", BB],
    ["array_inst", "Microarray Instruments", "instruments", "growth", None, None, None, "Microarray Instruments", BB],
    ["service", "Service & Other Revenue", None, "growth", None, None, None, "Total Service & Other Revenue", BB],
])

# Drivers: ids without spaces, literal target ids, FY aggregation only on uncased rows, no stray targets on ratio drivers
ws = wb["Drivers"]
ws["A4"] = "clins_cons_g"
ws["D4"] = "clins_cons"
ws["A5"] = "research_cons_g"
ws["D5"] = "research_cons"
ws["D6"] = "china_seq_cons"
for r in range(4, 15):
    ws.cell(r, 9).value = None
for r in range(4, ws.max_row + 1):
    if ws.cell(r, 1).value in ("recv_pct", "inv_pct", "prepaid_pct", "pay_pct", "accrued_pct", "defrev_pct"):
        ws.cell(r, 4).value = None

# Side Builds: name, linked line, the analyst's description in the right columns
ws = wb["Side Builds"]
clear_rows(ws, 4, 11, 4)
write_rows(ws, 4, [
    ["Clinical Consumable", "clins_cons", "to calculate historical revenues"],
    ["Research Consumable", "research_cons", "to calculate historical revenues"],
    ["Implied Discounting Build", "seq_cons",
     "take the produced growth rate for this from our underlying estimates and then at an assumed 30% volume growth calculate the implied level of discounting in revenue/gb y/y for each time period"],
])
wb.save(path)
print("saved", path)
