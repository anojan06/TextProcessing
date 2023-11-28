# import block

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from pathlib import Path
import pandas as pd
import glob


def heatmap():
    directoryname = "wiki_articles"

    # gets all file names
    text_files = glob.glob(directoryname + "/*.txt")
    file_names = [Path(text).stem for text in text_files]

    # does the TF-IDF counting
    tfidf_vectorizer = TfidfVectorizer(input='filename', stop_words='english')
    tfidf_vector = tfidf_vectorizer.fit_transform(text_files)

    # This converts the results to a pandas dataframe, which makes it easier to
    # process and visualize
    tfidf_df = pd.DataFrame(tfidf_vector.toarray(), index=file_names, columns=tfidf_vectorizer.get_feature_names_out())
    tfidf_df.stack().reset_index()
    tfidf_df = tfidf_df.stack().reset_index()
    tfidf_df = tfidf_df.rename(columns={0:'tfidf', 'level_0': 'document','level_1': 'term', 'level_2': 'term'})
    tfidf_df.sort_values(by=['document','tfidf'], ascending=[True,False]).groupby(['document']).head(10)

    # This line of code just saves the above output to a variable so that you can query it.

    top_tfidf = tfidf_df.sort_values(by=['document','tfidf'], ascending=[True,False]).groupby(['document']).head(10)

    # This says "find all the documents that have war in their top 10".

    top_tfidf[top_tfidf['term'].str.contains('war')]

    # This says "find the top ten words in the Ukraine document

    top_tfidf[top_tfidf['document'].str.contains('Ukraine')]

    # heatmap
    import altair as alt
    import numpy as np


    # adding a little randomness to break ties in term ranking
    top_tfidf_plusRand = top_tfidf.copy()
    top_tfidf_plusRand['tfidf'] = top_tfidf_plusRand['tfidf'] + np.random.rand(top_tfidf.shape[0])*0.0001

    # base for all visualizations, with rank calculation
    base = alt.Chart(top_tfidf_plusRand).encode(
        x = 'rank:O',
        y = 'document:N'
    ).transform_window(
        rank = "rank()",
        sort = [alt.SortField("tfidf", order="descending")],
        groupby = ["document"],
    )

    # heatmap specification
    heatmap = base.mark_rect().encode(
        color = 'tfidf:Q'
    )

    # text labels, white for darker heatmap colors
    text = base.mark_text(baseline='middle').encode(
        text = 'term:N',
        color = alt.condition(alt.datum.tfidf >= 0.23, alt.value('white'), alt.value('black'))
    )

    # display the three superimposed visualizations
    (heatmap + text).properties(width = 600)

import re

# will write all data about each company in this text file to however many names there are in the file specified by filepath
def write_info(filepath):
    with open(filepath, 'r') as f:
        company_list = f.read().splitlines()
    df = pd.read_csv("Text_Processing_Code/raw/raw/branded_food.csv", delimiter = ',')
    df = df[['brand_owner', 'ingredients']]
    for company in company_list:
        all_ingredients = ""
        company_name = re.sub(" ", "_", company)
        with open("Text_Processing_Code/company_ingredient_data/" + company_name + ".txt", "w", encoding="utf-8") as w:
            # can change this to randomly select, to get better representative sample
            for ind in df.index:
                if df["brand_owner"][ind] == company:
                    all_ingredients += str(df["ingredients"][ind])
                    all_ingredients += ", "
            w.write(all_ingredients)

write_info("Text_Processing_Code/top_companies.txt")