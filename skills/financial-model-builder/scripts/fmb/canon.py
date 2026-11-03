"""Canonical statement line sets with label synonyms (Bloomberg / CapIQ wording).

Each entry: id, display label, synonyms (matched case- and punctuation-insensitively),
role (how it is projected), and group (for subtotal ranges). Lines absent from the
data are dropped; reported totals that do not tie to the mapped lines get an
"Other ... (plug)" line so history always foots.
"""
from __future__ import annotations

IS_LINES = [
    # below operating income
    ("interest_income", "Interest Income", ["Interest Income", "Finance Income", "Interest and Investment Income", "Interest & Investment Income", "Interest and Invest. Income"], "driver"),
    ("interest_expense", "Interest Expense", ["Interest Expense", "Finance Costs", "Interest Expense, Net"], "driver"),
    ("other_nonop", "Other Non-Operating Income (Expense)", ["Other Non-Operating Income", "Other Non-Operating Income (Expense)", "Other Non Operating Inc. (Exp.)", "Other, Net", "Other Income (Expense), Net"], "driver"),
    ("tax", "Income Tax Expense", ["Income Tax Expense", "Income Tax Expense (Benefit)", "Provision for Income Taxes", "Income Taxes"], "tax"),
    ("nci", "Net Income Attributable to Noncontrolling Interest", ["Minority Interest in Earnings", "Net Income Attributable to Noncontrolling Interest", "Minority Int. in Earnings"], "driver"),
    ("ni", "Net Income", ["Net Income", "Net Income to Company", "Net Income Attributable to Common Shareholders"], "computed"),
    # memo
    ("dep", "Depreciation", ["Depreciation Expense", "Depreciation", "Depreciation & Amort."], "driver"),   # CapIQ's cash-flow "Depreciation & Amort." excludes acquired intangibles
    ("amort", "Amortization of Intangibles", ["Amortization of Intangible Assets", "Amortization of Intangibles", "Amort. of Goodwill and Intangibles"], "driver"),
    ("da", "Depreciation & Amortization", ["Depreciation & Amortization", "Depreciation & Amort.", "Depreciation & Amort., Total", "D&A"], "driver"),
    ("sbc", "Stock-Based Compensation", ["Stock-Based Compensation", "Stock Based Compensation", "Share-Based Compensation"], "driver"),
    ("adj_oi", "Adjusted Operating Income", ["Adjusted Operating Income", "Adj. Operating Income", "Non-GAAP Operating Income"], "adjusted"),
    ("adj_ni", "Adjusted Net Income", ["Adjusted Net Income", "Adj. Net Income", "Non-GAAP Net Income"], "adjusted"),
    ("adj_eps", "Adjusted Diluted EPS", ["Adjusted Diluted EPS", "Adj. Diluted EPS", "Non-GAAP EPS", "Non-GAAP Diluted EPS"], "adjusted"),
    ("shares_basic", "Basic Weighted Avg Shares", ["Basic Weighted Avg. Shares", "Basic Weighted Avg Shares", "Weighted Average Basic Shares Outstanding", "Weighted Avg. Basic Shares Out."], "driver"),
    ("shares_dil", "Diluted Weighted Avg Shares", ["Diluted Weighted Avg. Shares", "Diluted Weighted Avg Shares", "Weighted Average Diluted Shares Outstanding", "Weighted Avg. Diluted Shares Out."], "driver"),
    ("eps_basic", "Basic EPS", ["Basic EPS", "Basic EPS Excl. Extra Items"], "computed"),
    ("eps_dil", "Diluted EPS", ["Diluted EPS", "Diluted EPS Excl. Extra Items", "Diluted EPS Excl. Extra Items"], "computed"),
]

BS_LINES = [
    ("cash", "Cash & Cash Equivalents", ["Cash & Cash Equivalents", "Cash And Equivalents", "Cash and Cash Equivalents"], "ca", "cash"),
    ("st_inv", "Short-Term Investments", ["Short-Term Investments", "Short Term Investments", "Marketable Securities"], "ca", "flat"),
    ("receivables", "Accounts Receivable", ["Accounts Receivable", "Trade & Other Receivables", "Total Receivables", "Accounts Receivable, Net"], "ca", "pct_rev"),
    ("inventory", "Inventories", ["Inventories", "Inventory"], "ca", "pct_cogs"),
    ("prepaid", "Prepaid Expenses & Other Current Assets", ["Prepaid Expenses & Other Current Assets", "Prepaid Exp.", "Other Current Assets", "Prepaid Expenses"], "ca", "pct_rev"),
    ("other_ca", "Other Current Assets (plug)", [], "ca", "plug"),
    ("ppe", "Property, Plant & Equipment", ["Property. Plant & Equipment", "Property, Plant & Equipment", "Net Property, Plant & Equipment", "Property & Equipment"], "nca", "ppe"),
    ("rou", "Operating Lease Right-of-Use Assets", ["Operating Lease Right-of-Use Assets", "Lease Right-of-Use Assets", "Right-of-Use Assets"], "nca", "flat"),
    ("goodwill", "Goodwill", ["Goodwill"], "nca", "flat"),
    ("intangibles", "Intangible Assets", ["Intangible Assets", "Other Intangibles", "Intangibles"], "nca", "intangibles"),
    ("lt_inv", "Long-Term Investments", ["Long-Term Investments", "Long-term Investments", "LT Investments"], "nca", "flat"),
    ("dta", "Deferred Tax Assets", ["Deferred Tax", "Deferred Tax Assets, LT", "Deferred Tax Assets"], "nca", "flat"),
    ("other_nca", "Other Non-Current Assets", ["Other Assets", "Other Long-Term Assets", "Other Non-Current Assets"], "nca", "flat"),
    ("other_nca_plug", "Other Non-Current Assets (plug)", [], "nca", "plug"),
    ("payables", "Accounts Payable", ["Accounts Payable", "Trade & Other Payables"], "cl", "pct_costs"),
    ("accrued", "Accrued Liabilities", ["Accrued Liabilities", "Accrued Exp.", "Accrued Expenses & Other Liabilities", "Accrued Expenses"], "cl", "pct_costs"),
    ("deferred_rev", "Deferred Revenue", ["Deferred Revenue", "Unearned Revenue, Current", "Contract Liabilities"], "cl", "pct_rev"),
    ("st_debt", "Current Portion of Debt", ["Current Portion of Debt", "Current Portion of Long-Term Debt", "Short-Term Borrowings", "Curr. Port. of LT Debt"], "cl", "flat"),
    ("lease_liab_cur", "Current Lease Liabilities", ["Current Portion of Leases", "Current Portion of Operating Lease Liabilities", "Curr. Port. of Leases"], "cl", "flat"),
    ("other_cl", "Other Current Liabilities", ["Other Current Liabilities"], "cl", "flat"),
    ("other_cl_plug", "Other Current Liabilities (plug)", [], "cl", "plug"),
    ("lt_debt", "Long-Term Debt", ["Long-Term Debt", "Long Term Debt"], "ncl", "debt"),
    ("lease_liab", "Operating Lease Liabilities", ["Operating Lease Liabilities", "Lease Liabilities", "Long-Term Leases"], "ncl", "flat"),
    ("dtl", "Deferred Tax Liabilities", ["Deferred Tax Liabilities", "Def. Tax Liability, Non-Curr.", "Deferred Tax Liability"], "ncl", "flat"),
    ("other_ncl", "Other Long-Term Liabilities", ["Other Long-Term Liabilities", "Other Non-Current Liabilities", "Other Non Current Liabilities"], "ncl", "flat"),
    ("other_ncl_plug", "Other Non-Current Liabilities (plug)", [], "ncl", "plug"),
    ("apic", "Additional Paid-In Capital", ["Additional Paid-In Capital", "Additional Paid In Capital", "Other Paid-In Capital", "Common Stock & APIC"], "eq", "apic"),
    ("treasury", "Treasury Stock", ["Treasury Stock", "Treasury Shares"], "eq", "treasury"),
    ("retained", "Retained Earnings", ["Retained Earnings", "Retained Earnings (Accumulated Deficit)"], "eq", "retained"),
    ("aoci", "Accumulated Other Comprehensive Income", ["Accumulated Other Comprehensive Income", "Comprehensive Inc. and Other", "Other Reserves", "Accumulated Other Comprehensive Income (Loss)"], "eq", "flat"),
    ("nci_eq", "Noncontrolling Interest", ["Minority Interest", "Noncontrolling Interest"], "eq", "flat"),
    ("other_eq_plug", "Other Equity (plug)", [], "eq", "plug"),
]
BS_TOTALS = {
    "ca": ("Current Assets", ["Current Assets", "Total Current Assets"]),
    "nca": ("Non-Current Assets", ["Non-Current Assets", "Total Non-Current Assets", "Total Non Current Assets"]),
    "assets": ("Total Assets", ["Total Assets"]),
    "cl": ("Current Liabilities", ["Current Liabilities", "Total Current Liabilities"]),
    "ncl": ("Non-Current Liabilities", ["Non-Current Liabilities", "Total Non-Current Liabilities", "Total Non Current Liabilities"]),
    "liab": ("Total Liabilities", ["Total Liabilities"]),
    "eq": ("Total Shareholders' Equity", ["Total Shareholders' Equity", "Total Equity", "Total Common Equity", "Total Stockholders' Equity"]),
    "le": ("Total Liabilities & Shareholders' Equity", ["Total Liabilities & Shareholders' Equity", "Total Liabilities And Equity", "Total Liabilities & Equity"]),
}

CFS_LINES = [
    ("cf_ni", "Net Income", ["Net Income"], "op", "link_ni"),
    ("cf_da", "(+) Depreciation & Amortization", ["Depreciation & Amortization", "Depreciation & Amort., Total", "Depreciation & Amort."], "op", "link_da"),
    ("cf_sbc", "(+) Stock-Based Compensation", ["Stock-Based Compensation", "Stock Based Compensation"], "op", "link_sbc"),
    ("cf_deftax", "(+/-) Deferred Income Taxes", ["Deferred Income Taxes", "Change in Deferred Taxes"], "op", "zero"),
    ("wc_recv", "(+/-) Change in Accounts Receivable", ["Accounts Receivable", "Change in Acc. Receivable", "Change In Accounts Receivable"], "op", "wc:receivables"),
    ("wc_inv", "(+/-) Change in Inventories", ["Inventory", "Inventories", "Change In Inventories"], "op", "wc:inventory"),
    ("wc_prepaid", "(+/-) Change in Prepaid & Other Current Assets", ["Prepaid Expenses", "Change in Other Current Assets", "Prepaid Expenses & Other Current Assets"], "op", "wc:prepaid"),
    ("wc_pay", "(+/-) Change in Accounts Payable", ["Accounts Payable", "Change in Acc. Payable", "Change In Accounts Payable"], "op", "wc:payables"),
    ("wc_accrued", "(+/-) Change in Accrued Liabilities", ["Accrued Liabilities", "Change in Accrued Liabilities"], "op", "wc:accrued"),
    ("wc_defrev", "(+/-) Change in Deferred Revenue", ["Deferred Revenue", "Change in Unearned Rev.", "Change in Deferred Revenue"], "op", "wc:deferred_rev"),
    ("wc_other", "(+/-) Change in Other Operating Assets & Liabilities", ["Other Assets", "Change in Other Net Operating Assets", "Other Operating Activities", "Other Operating Activities, Total"], "op", "zero"),
    ("other_op", "(+/-) Other Operating Items (plug for actuals)", [], "op", "plug"),
    ("capex", "(-) Capital Expenditures", ["Capital Expenditures", "Capital Expenditure", "Purchase of Property, Plant & Equipment"], "inv", "driver"),
    ("acquisitions", "(-) Acquisitions", ["Acquisitions", "Cash Acquisitions", "Acquisitions, Net of Cash Acquired"], "inv", "zero"),
    ("investments", "(+/-) Net (Purchases)/Sales of Investments", ["Net (Purchases)/Sales of Investments", "Invest. in Marketable & Equity Securt.", "Purchases of Investments", "Sale/Maturity of Investments"], "inv", "investments"),
    ("other_inv", "(+/-) Other Investing", ["Other Investing Activities", "Other Investing Activities, Total"], "inv", "plug"),
    ("debt_change", "(+/-) Change in Debt", ["Change in Debt", "Net Debt Issued (Repaid)", "Total Debt Issued"], "fin", "driver"),
    ("debt_repaid", "(-) Debt Repayments", ["Debt Repayments", "Total Debt Repaid", "Long-Term Debt Repaid"], "fin", "zero"),
    ("buybacks", "(-) Share Repurchases", ["Share Repurchase", "Repurchase of Common Stock", "Repurchase of Common Stock, Total"], "fin", "driver"),
    ("dividends", "(-) Dividends Paid", ["Common Dividends Paid", "Dividends Paid", "Dividends Paid, Total"], "fin", "driver"),
    ("stock_issued", "(+) Proceeds from Stock Issuance", ["Proceeds from Issuance of Common Stock", "Issuance of Common Stock", "Proceeds from Stock Options"], "fin", "driver"),
    ("rsu_tax", "(-) Taxes Paid on Net Share Settlement", ["Taxes Paid Related to Net Share Settlement of", "Taxes Paid Related to Net Share Settlement of Equity Awards", "Tax Withholding on Equity Awards"], "fin", "driver"),
    ("other_fin", "(+/-) Other Financing", ["Other Financing Activities", "Other Financing Activities, Total"], "fin", "plug"),
    ("fx", "(+/-) FX Effect on Cash", ["Effect of Foreign Exchange Rates", "Foreign Exchange Rate Adj.", "Effect of Exchange Rate Changes on Cash"], "fx", "plug"),
]
CFS_TOTALS = {
    "op": ("Cash Flow from Operations", ["Cash Flow from Operations", "Cash from Ops.", "Cash from Operations", "Net Cash from Operating Activities"]),
    "inv": ("Cash Flow from Investing", ["Cash Flow from Investing", "Cash from Investing", "Net Cash from Investing Activities"]),
    "fin": ("Cash Flow from Financing", ["Cash Flow from Financing", "Cash from Financing", "Net Cash from Financing Activities"]),
    "net": ("Net Change in Cash", ["Net Change in Cash"]),
    "beg": ("Cash & Cash Equivalents (BOP)", ["Cash & Cash Equivalents (BOP)", "Cash at Beginning of Period"]),
    "end": ("Cash & Cash Equivalents (EOP)", ["Cash & Cash Equivalents (EOP)", "Cash at End of Period"]),
    "fcf": ("Free Cash Flow", ["Free Cash Flow"]),
}

# default uncased drivers created for every model (id, label, section, fmt, fy aggregation, target line on the statements)
DEFAULT_DRIVERS = [
    ("interest_income", "Interest Income", "is", "amount_s", "sum", ("interest_income", None)),
    ("interest_expense", "Interest Expense", "is", "amount_s", "sum", ("interest_expense", None)),
    ("other_nonop", "Other Non-Operating Income (Expense)", "is", "amount_s", "sum", ("other_nonop", None)),
    ("tax_rate", "Tax Rate", "is", "pct_s", "last", ("tax_rate", None)),
    ("dep", "Depreciation", "is", "amount_s", "sum", ("dep", None)),
    ("amort", "Amortization of Intangibles", "is", "amount_s", "sum", ("amort", None)),
    ("da", "Depreciation & Amortization", "is", "amount_s", "sum", ("da", None)),
    ("sbc", "Stock-Based Compensation", "is", "amount_s", "sum", ("sbc", None)),
    ("adj_other", "Other Non-GAAP Adjustments (pre-tax)", "is", "amount_s", "sum", None),
    ("adj_tax_rate", "Adjusted Tax Rate", "is", "pct_s", "last", ("adj_tax_rate", None)),
    ("shares_basic", "Basic Weighted Avg Shares", "is", "shares", "avg", ("shares_basic", None)),
    ("shares_dil", "Diluted Weighted Avg Shares", "is", "shares", "avg", ("shares_dil", None)),
    ("recv_pct", "Accounts Receivable % of Qtr. Revenue", "bs", "pct_s", "last", None),
    ("inv_pct", "Inventories % of Qtr. Cost of Revenue", "bs", "pct_s", "last", None),
    ("prepaid_pct", "Prepaid & Other Current Assets % of Qtr. Revenue", "bs", "pct_s", "last", None),
    ("pay_pct", "Accounts Payable % of Qtr. (CoR + Opex)", "bs", "pct_s", "last", None),
    ("accrued_pct", "Accrued Liabilities % of Qtr. (CoR + Opex)", "bs", "pct_s", "last", None),
    ("defrev_pct", "Deferred Revenue % of Qtr. Revenue", "bs", "pct_s", "last", None),
    ("capex", "Capital Expenditures", "cf", "amount_s", "sum", ("capex", None)),
    ("debt_change", "Net Debt Issued / (Repaid)", "cf", "amount_s", "sum", ("debt_change", None)),
    ("buybacks", "Share Repurchases", "cf", "amount_s", "sum", ("buybacks", None)),
    ("dividends", "Dividends Paid", "cf", "amount_s", "sum", ("dividends", None)),
    ("stock_issued", "Proceeds from Stock Issuance", "cf", "amount_s", "sum", ("stock_issued", None)),
    ("rsu_tax", "Taxes Paid on Net Share Settlement", "cf", "amount_s", "sum", ("rsu_tax", None)),
]

# Sections of an export that a statement line should be read from first (prefix match, in order),
# and sections it must never be read from. Bloomberg repeats labels across blocks (balance-sheet
# "Accounts Receivable" and the working-capital change of the same name; GAAP and adjusted
# "Income Tax Expense"), so a bare label is ambiguous without these.
PREFER_SECTIONS = {
    "is": ["gaap results", "income statement (gaap)", "income statement", "highlights"],
    "bs": ["assets", "liabilities & equity", "liabilities", "equity", "investments", "balance sheet", "condensed balance sheet"],
    "cf": ["cash from operating", "cash from investing", "cash from financing", "changes in working capital", "cash flow", "condensed cash flow"],
    "memo": ["company specific adjustments", "cash from operating", "special company reference", "cash flow", "income statement - supplemental"],
}
# CapIQ sheets that never hold a statement line (pension amounts, segment detail, debt detail ...)
NON_STATEMENT = ["pension", "supplemental", "industry specific", "segments", "capital structure", "historical capitalization", "key stats", "multiples", "ratios"]
EXCLUDE_SECTIONS = {
    "is": ["cash from", "changes in working capital", "condensed cash flow", "condensed balance sheet", "assets", "liabilities & equity", "investments", "cash flow", "balance sheet"] + NON_STATEMENT,
    "bs": ["cash from", "changes in working capital", "condensed cash flow", "company specific adjustments", "special company reference", "cash flow", "income statement"] + NON_STATEMENT,
    "cf": ["highlights", "income statement", "gaap results", "condensed balance sheet", "assets", "liabilities & equity", "investments", "segment revenue", "business breakdown", "balance sheet"] + NON_STATEMENT,
    "memo": ["pension", "industry specific", "segments", "capital structure", "historical capitalization", "key stats", "multiples", "ratios"],
}

# label groups above operating income (the statement tables start below it); used with the
# IS/BS/CFS synonyms to find a line's equivalent in another export (Bloomberg vs CapIQ naming)
TOP_SYNONYMS = [
    ["Revenue", "Total Revenue", "Total Revenues", "Revenues", "Net Sales", "Net Revenue", "Net Revenues"],
    ["Cost of Revenue", "Cost Of Goods Sold", "Cost of Goods Sold", "Cost of Sales", "Total Cost of Revenue", "Cost of Revenues"],
    ["Gross Profit"],
    ["Selling, General & Administrative", "Selling General & Admin Exp.", "Selling, General & Admin. Expenses", "SG&A", "SG&A Expense",
     "Selling, General and Administrative", "Selling, General & Administrative Expenses"],
    ["Research & Development", "R & D Exp.", "R&D Exp.", "Research and Development", "R&D", "Research & Development Expense"],
    ["Operating Income", "Operating Income (Loss)", "Operating Profit"],
    ["Pre-Tax Income", "Pretax Income", "Income Before Taxes", "EBT Incl. Unusual Items", "Pre-Tax Income (Loss)", "Income (Loss) Before Income Taxes", "Earnings Before Tax"],
    ["Stock-Based Compensation", "Stock Based Compensation", "Stock-Based Comp., Total", "Share-Based Compensation"],
]


def _n(s: str) -> str:
    import re as _re
    return _re.sub(r"[^a-z0-9%]+", " ", str(s).lower()).strip()


def synonyms_of(label: str):
    """Other names of the same line across exports, from every synonym group that holds the label."""
    key = _n(label)
    groups = list(TOP_SYNONYMS) + [x[2] for x in IS_LINES] + [x[2] for x in BS_LINES] + [x[2] for x in CFS_LINES]
    groups += [v[1] for v in BS_TOTALS.values()] + [v[1] for v in CFS_TOTALS.values()]
    out = []
    for grp in groups:
        if key in {_n(s) for s in grp}:
            out += [s for s in grp if _n(s) != key and s not in out]
    return out


WC_DRIVER_FOR = {"receivables": ("recv_pct", "rev"), "inventory": ("inv_pct", "cogs"), "prepaid": ("prepaid_pct", "rev"),
                 "payables": ("pay_pct", "costs"), "accrued": ("accrued_pct", "costs"), "deferred_rev": ("defrev_pct", "rev")}
