#k-means
#mikafan88
#6/3/2023

"""k-means graph
this is a program to do a 3 cluster k-means on 3 points

"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

#things to change dataset to dataset
ourCSV = "/Users/joshuajayaprakash/Desktop/research summer 2023/violin plot stuff/INPUT (2).csv"
clusterNumber = 3

#step 1 - Feature Reduction
"""
Feature reduction is important because the data must be trimmed to a manageable size
before you run certain methods here. There are various ways to do featue reduction,
and here we will be using principal component analysis.
"""

df = pd.read_csv(ourCSV).tail(-1).transpose().tail(-1) #remove extraneous information
scaler = StandardScaler()
scaler.fit(df)
scaled_data = scaler.transform(df)

pca = PCA(n_components = 3) #number of dimensions we're using for our dataset. this graph is in 3d. 
pca.fit(scaled_data)
x_pca = pca.transform(scaled_data)


#step 2 - clustering


kmeans = KMeans(n_clusters = clusterNumber)
kmeans = kmeans.fit(x_pca)
labels = kmeans.predict(x_pca)
centroids = kmeans.cluster_centers_

"""
increase/decrease the amount of things under here depending on how many components you're using.
i'm using x, y, and z for the value 3 in clusterNumber, since we're making 3 clusters. 
"""
x = np.array(labels==0) 
y = np.array(labels==1)
z = np.array(labels==2)

#step 3 - graphing

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.scatter(centroids[:,0],centroids[:,1],centroids[:,2],c="black")

#change these so it corresponds to the number of clusters in clusterNumber
ax.scatter(x_pca[x,0], x_pca[x, 1], x_pca[x, 2], c="blue")
ax.scatter(x_pca[y,0], x_pca[y, 1], x_pca[y, 2], c="red")
ax.scatter(x_pca[z,0], x_pca[z, 1], x_pca[z, 2], c = "yellow")
plt.show()
