# Example 2.16 — write a CSV with pandas (README Step 13.1)
# TODO:
# - build a DataFrame with columns Name and Age (four rows, your choice)
# - print it
# - save it to test.csv next to this script, with index=False
# Expected: the table prints and test.csv appears.
import pandas as pd
data = pd.DataFrame({"Name": ["Alice", "Bob", "Charlie", "David"], "Age": [25, 30, 35, 40]})
print(data)
data.to_csv("16-data-name_age.csv", index=False)

