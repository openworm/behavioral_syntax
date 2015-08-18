from scipy import io
import numpy as np
from matplotlib import pyplot as plt
from sklearn import manifold, cluster

directory = '/Users/cyrilrocke/Documents/c_elegans/data/'
angles = np.load(directory+'/test1/features/angles10.npy')

#mean_r_sq finds the template postures using kmeans++ and returns the 
#average variance explained(r_squared), the templates, and labels.

#decision_rule calls the mean_r_sq as many times as required to satisfy
#the criterion that the r_squared gain is negligible. 

angle_0 = angles[0]

def mean_r_sq(k):
    kmeans = cluster.KMeans(init='k-means++',n_clusters=k,max_iter=1000)
    kmeans.fit(angle_0)
    
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_
    
    #compute average variance explained:
    total_var = []
    for i in range(len(centroids)):
        total_var+= [np.corrcoef(centroids[i],j)[0][1]**2 for j in angle_0[np.where(labels == i)]]
    
    return [np.mean(total_var), centroids, labels]


# start = minimum cluster size
# inc = increase in cluster size k
# delta = R_squared gain that is considered negligible
def decision_rule(prev,inc,delta):
    
    while mean_r_sq(prev+inc)[0]-mean_r_sq(prev)[0] > delta:
        prev = prev+inc
        output = mean_r_sq(prev)
    return output
