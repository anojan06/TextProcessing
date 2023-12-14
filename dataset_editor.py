import pandas as pd
import re
import random

# will write all data about each company in this text file to however many names there are in the file specified by filepath
def write_info(filepath):
    with open(filepath, 'r') as f:
        company_list = f.read().splitlines()
    df = pd.read_csv("data_and_tf-idf/raw/raw/branded_food.csv", delimiter = ',')
    df = df[['brand_owner', 'ingredients', 'modified_date', 'available_date']]
    for company in company_list:
        company_name = re.sub(" ", "_", company)
        line_list = []
        with open("data_and_tf-idf/company_ingredient_data/" + company_name + ".txt", "w", encoding="utf-8") as w:
            w.write('brand_owner,ingredients,modified_date,available_date\n')
            # can change this to randomly select, to get better representative sample
            for ind in df.index:
                if df["brand_owner"][ind] == company:
                    all_ingredients = ""
                    all_ingredients += str(df["ingredients"][ind])
                    all_ingredients += ","
                    all_ingredients += str(df['modified_date'][ind])
                    all_ingredients += ","
                    all_ingredients += str(df['available_date'][ind])
                    all_ingredients += ","
                    line_list.append(all_ingredients)
            list_10k = random.sample(line_list, 10000)
            for line in list_10k:
                w.write(line+"\n")
                    

write_info("data_and_tf-idf/top_companies.txt")