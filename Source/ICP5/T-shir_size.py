import matplotlib.pyplot as plt
import numpy as np
import random
from sklearn.cluster import KMeans                #importing KMeans from sklearn
random.seed(2)                                 #setting seed so that same random numbers would be generated
height=[round(random.uniform(4,7),2) for i in range(20)]                 #dynamically generating heights within 4 t 7
weight =[random.randint(50,70) for j in range(20)]                        #generating weights within 50 to 70
X = np.vstack((height, weight)).T                                # combining to 2D array using vertical stack
print(X)
kmeans = KMeans(n_clusters=3)                                   #Defining KMeans model with 3 clusters
kmeans.fit(X)                                                   #Applying KMeans
plt.scatter(X[:,0], X[:,1], c=kmeans.labels_, cmap='rainbow')               # scatterplot by grouping clusters with colors
plt.scatter(kmeans.cluster_centers_[:,0] ,kmeans.cluster_centers_[:,1], color='black')             #Plotting the centroid of each cluster in black
plt.show()