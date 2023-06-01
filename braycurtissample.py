#Bray Curtis
#mikafan88
#6/1/2023


#imports. these are the libraries which we'll be using
import pandas as pd
import numpy as np
import scipy.spatial

#things to modify:
#csv file
ourCSV = "/Users/joshuajayaprakash/Desktop/research summer 2023/violin plot stuff/INPUT (2).csv"
#entry 1
entry1 = 0
#entry 2
entry2 = 1

#creating the dataframe
df = pd.read_csv(ourCSV)

#deleting the first line of this dataset, which is extra labels.
df = df.tail(-1)
array1 = np.array([float(x) for x in df.iloc[entry1][1:].transpose()]) #converting first line to array
array2 = np.array([float(x) for x in df.iloc[entry2][1:].transpose()]) #converting second line to array


brayCurtisDistance = scipy.spatial.distance.braycurtis(array1, array2)
print("the Bray Curtis distance is", brayCurtisDistance)
