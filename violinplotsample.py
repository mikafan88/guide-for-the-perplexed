#violin plot
#mikafan88
#5/30/2023


"""
This is a sample program for a violin plot with the
dataset that Jessica gave me. Written in Python 3.9.6
"""

"""
Purpose:
We want to create a violin plot for every feature.
We choose at what feature we start, how many features we want, and whether the features are combined. 

Result:
Outputs a graph for every feature in the range of features.
Depending on preferences this graph is combined. 

"""

#imports. these are hte libraries which we'll be using. 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#our csv file. feel free to change this depending on what the path is in your program.
#THE STUFF TO MODIFY IS HERE
ourCSV = "/Users/joshuajayaprakash/Desktop/research summer 2023/violin plot stuff/INPUT (2).csv"
startingFeature = 0 #this is the number feature we want to start at
featureInterval = 10 #this is how many more plots after the starting interval we want.
#Example: when startingFeature is 0, and featureInterval is 10, we get plots for 0 through 10 inclusive, providing 11 graphs. 
combineGraphs = False #this determines whether our graphs are combined or not onto one graph. 





#creating the dataframe
df = pd.read_csv(ourCSV)


#deleting the first line of the dataset, which is extra labels.
df = df.tail(-1)
df = df.iloc[startingFeature : featureInterval + 1]


if combineGraphs == False:
    for index, row in df.iterrows():
        plotName = row[0]
        plottedDF = row[1:].transpose()
        ourList = plottedDF.values
        ourList = [float(x) for x in ourList]
        ourArray = np.array(ourList)
        fig, ax = plt.subplots()
        ax.violinplot(dataset = ourArray)
        ax.set_xlabel(plotName)
        plt.show()
else:
    arrayList = []
    for index, row in df.iterrows():
        plotName = row[0]
        plottedDF = row[1:].transpose()
        ourList = plottedDF.values
        ourList = [float(x) for x in ourList]
        ourArray = np.array(ourList)
        arrayList.append(ourArray)
    fig, ax = plt.subplots()
    for i in range(0,len(arrayList)):
        ax.violinplot(dataset = arrayList[i],positions=[i])
    plt.show()

        
    
