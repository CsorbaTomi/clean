import pandas as pd

clean_basic = pd.read_excel("Munkafüzet2.xlsx")

clean_df = pd.DataFrame()

clean_df = clean_basic[clean_basic["Date of Analysis:"] > "2022-8-31"]
more_two_hundred = clean_df[clean_df["Metal Length [µm]:"] > 200] 

test_one = more_two_hundred.groupby("Cikkszám").count()
test_two = more_two_hundred.groupby("Gép").count()
test_three = more_two_hundred.groupby("Date of Analysis:").count()
test_four = clean_df.groupby("Date of Analysis:").count()

print(test_four["Cikkszám"])
# print(test_one["Gép"])
# print(test_two["Cikkszám"])
# print(test_three["Cikkszám"])

# print(more_two_hundred.groupby("Gép").count())
# material_no = clean_df.groupby("Cikkszám").count()

# clean_df.to_excel("september.xlsx")

# print(type(clean_df["Date of Analysis:"][0]))
# print(clean_df["Date of Analysis:"])
# print(clean_basic)