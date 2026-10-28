# Example 2.18 — write an Excel file with pandas (README Step 14.1)
# TODO:
# - reuse the Name/Age DataFrame from 16-data.py
# - save it to 18-data-name_age.xlsx, sheet_name="Sheet1", via pd.ExcelWriter(..., engine="xlsxwriter")
# Expected: test.xlsx opens in Numbers/Excel and shows the four rows.
import pandas as pd

data = pd.DataFrame({"Name": ["Alice", "Bob", "Charlie", "David"], "Age": [25, 30, 35, 40]})

with pd.ExcelWriter("18-data-name_age.xlsx", engine="xlsxwriter") as writer:
    data.to_excel(writer, sheet_name="Sheet1", index=False)