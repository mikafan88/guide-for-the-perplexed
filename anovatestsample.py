#ANOVA
#mikafan88
#6/1/2023


#imports. these are the libraries which we'll be using
import pandas as pd
import numpy as np
import scipy.stats

#things to modify:
#csv file
ourCSV = "/Users/joshuajayaprakash/Desktop/research summer 2023/violin plot stuff/INPUT (2).csv"

#entries we want to run anova on. fill this array out with the numbers of the samples you want to run.
#should probably clarify that the 3rd row of the CSV file is what I'm using for row 0. 

entryList = [0, 1, 2]

#creating the dataframe
df = pd.read_csv(ourCSV)

#deleting the first line of this dataset, which is extra labels.

arrayList = []
df = df.tail(-1)
for i in range(len(entryList)):
    arrayList.append(np.array([float(x) for x in df.iloc[entryList[i]][1:].transpose()])) #converting rows to arrays

statistic, pvalue = scipy.stats.f_oneway(*arrayList)
print("t statistic is", statistic)
print("p value is", pvalue)
