#I am not using the parameter k but I don't think it's necessary. 

import numpy as np
from sklearn import cluster

def kmeans(X):
    clusters = np.shape(X)[1]
    kmeans = cluster.KMeans(n_clusters=clusters, init='k-means++')
    return  kmeans.fit_predict(X)


X = np.random.rand(2,3)

kmeans(X)
 
