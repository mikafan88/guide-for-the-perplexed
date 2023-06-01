#T-Test
#mikafan88
#6/1/2023

"""
This is a sample program for running a T Test.
Dataset is the metabolite datatset Jessica gave me.
Written in Python 3.9.6

Purpose:
We want to run a T-Test on two different groups of metabolites.
T-Tests let you see whether two groups are really different,
by testing out whether the mean is different or not.

Result:
We get the result of a T-Test! Look up a guide on how to interpret these."
"""

#imports. these are the libraries which we'll be using
import pandas as pd
import numpy as np
import scipy.stats

#things to modify:
#csv file
ourCSV = "/Users/joshuajayaprakash/Desktop/research summer 2023/violin plot stuff/INPUT (2).csv"
#entry 1
row1 = 0
#entry 2
row2 = 1

#creating the dataframe
df = pd.read_csv(ourCSV)

#deleting the first line of this dataset, which is extra labels.
df = df.tail(-1)
array1 = np.array([float(x) for x in df.iloc[row1][1:].transpose()]) #converting first line to array
array2 = np.array([float(x) for x in df.iloc[row2][1:].transpose()]) #converting second line to array


statistic, pvalue = scipy.stats.ttest_ind(array1, array2)
print("t statistic is", statistic)
print("p value is", pvalue)
