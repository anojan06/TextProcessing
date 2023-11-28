import pandas as pd
import re

df = pd.read_csv("Text_Processing_Code/raw/raw/branded_food.csv", delimiter = ',')
num_dict = {}
for i in range(len(df)-1):
    if (df.loc[i+1, "brand_owner"] not in num_dict):
        num_dict[df.loc[i+1, "brand_owner"]] = 1
    else:
        num_dict[df.loc[i+1, "brand_owner"]] += 1
num_dict = sorted(num_dict.items(), key=lambda x:x[1])
print(num_dict)
print(len(num_dict))