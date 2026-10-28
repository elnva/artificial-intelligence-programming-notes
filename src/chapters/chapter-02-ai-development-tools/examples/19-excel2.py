# Example 2.19 — read the Excel file back (README Step 14.2)
# TODO:
# - read test.xlsx with pd.read_excel(..., sheet_name="Sheet1")
# - print it
# Expected: same four rows as 18-excel.py.
import pandas as pd
data = pd.read_excel("18-data-name_age.xlsx", sheet_name="Sheet1")
print(data)
