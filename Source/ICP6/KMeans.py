import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
df = pd.read_csv('sample_stocks.csv')      #Loading the dataset using Pandas

sse={}                                     # Defining sum of squared errors

x = df.returns
y = df.dividendyield
X = np.vstack((x, y)).T
print(X)

for k in range(1,11):
    kmeans = KMeans(n_clusters=k)                     #Defining KMeans model for a custom value of k
    kmeans.fit(X)                                     #Applying the KMeans model
    plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='rainbow')          # scatterplot by grouping clusters with colors
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
                color='black')                         # Plotting the centroid of each cluster in black
    plt.show()
    sse[k] = kmeans.inertia_          #Calculating sum of squared errors i.e., with in each cluster and adding them up for the whole no.of clusters
print(sse)
plt.plot(sse.keys(), sse.values())     #Plotting all the calculated SSE and finding the best K
plt.show()
