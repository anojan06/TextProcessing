# README for Text Processing Project
# Introduction

This project analyzes food data from the USDA, focusing on ingredients in store-bought foods, their variations across companies, and identifying common potentially unhealthy ingredients.
Contents

The codebase includes:

    findBigCompanies.py: Identifies top companies from the dataset.
    tf-idf_and_company_finder.py: Applies TF-IDF analysis to the data.
    tf-idf_and_dataset_editor.py: Pre-processes and edits the dataset.
    topcompanies.ipynb: Jupyter notebook for interactive analysis.

Setup & Running the Code

    Environment: Python 3.x.
    Dependencies: Libraries such as pandas, numpy, sklearn.
    Running the Scripts:
        Run findBigCompanies.py to extract top companies.
        Run company_ingredients_statistics.ipynb to see token statistics for the data
        Use tf-idf_and_company_finder.py for TF-IDF analysis.
        Pre-process data with tf-idf_and_dataset_editor.py.
        Explore data interactively in topcompanies.ipynb.

Conclusion

The analysis revealed the widespread use of ingredients like salt, differences in sweetener usage, and xanthan gum's prevalence. Future work could include using Word2vec for trend analysis.
