# Example 2.17 — read the CSV back (README Step 13.2)
# TODO:
# - read 16-data-name_age.csv (written by 16-data.py) into a new DataFrame
# - print it
# Expected: same table as 16-data.py printed — the round-trip works.
import pandas as pd
data = pd.read_csv("16-data-name_age.csv")
print(data)