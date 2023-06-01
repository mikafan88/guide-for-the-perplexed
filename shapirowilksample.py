#Shapiro-Wilk test
#mikafan88
#6/1/2023

#imports. these are the libraries which we'll be using
import pandas as pd
import numpy as np
import scipy.stats

#things to modify:
#csv file
ourCSV = "/Users/joshuajayaprakash/Desktop/research summer 2023/violin plot stuff/INPUT (2).csv"

#shapiro wilks tests the null hypothesis that the data was drawn from a normal distribution
#should probably clarify that the 3rd row of the CSV file is what I'm using for row 0. 

entry = 0

#creating the dataframe
df = pd.read_csv(ourCSV)

#deleting the first line of this dataset, which is extra labels.
df = df.tail(-1)
ourArray = np.array([float(x) for x in df.iloc[entry][1:].transpose()]) #converting dataframe to array


statistic, pvalue = scipy.stats.shapiro(ourArray)
print("t statistic is", statistic)
print("p value is", pvalue)
