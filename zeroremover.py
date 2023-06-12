#zeroremover
#mikafan88
#6/6/2023

"""
lol
ty amanda for reminding me to convert this into an integer
"""

#imports
import pandas as pd
import numpy as np

#things to change dataset to dataset
ourCSV = "/Users/joshuajayaprakash/Desktop/research summer 2023/violin plot stuff/INPUT (2).csv" #csv file
saveMinimum = 2 #minimum number to not purge.
#let's take the example of saveMinimum = 2.
#for version 1, all rows with 0 or 1 entries will be purged
#for version 2, all rows that do not have at least two entries in at least one of the same groups will be purged

version = 1 #version 1 allows entries in different categories to be counted, version 2 doesn't allow this

df = pd.read_csv(ourCSV)
df.iloc[1:, 1:] = df.iloc[1:, 1:].applymap(float)


def version1(df):
    nonzero_counts = df.apply(lambda row: row.astype(bool).sum(), axis=1)
    newDF = df[nonzero_counts >= saveMinimum]
    return newDF


def version2(df):
    newDF = df.applymap(lambda x: 1 if isinstance(x, float) and x != 0.0 else x)
    first_entries = newDF.iloc[0]
    rename_dict = {col: entry for col, entry in zip(newDF.columns, first_entries)}
    newDF = newDF.rename(columns=rename_dict).drop(0)
    newDF = newDF.groupby(newDF.columns, axis=1).sum()
    newDF = newDF.drop(newDF.columns[0], axis=1).max(axis = 1)
    row_numbers = newDF[newDF >= saveMinimum].dropna(how='all').index.tolist()
    newDF = df.iloc[row_numbers]
    return newDF


#calling version 1. feel free to swap this out. 
print(version1(df))

