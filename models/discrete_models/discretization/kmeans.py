from scipy import io
import numpy as np
from matplotlib import pyplot as plt
from sklearn import manifold, cluster

directory = '/Users/cyrilrocke/Documents/c_elegans/data/'
angles = np.load(directory+'/test1/features/angles10.npy')

#kmeans finds the template postures using kmeans++ and returns the 
#average variance explained(r_squared), the templates, and labels.

#decision_rule calls the kmeans as many times as required to satisfy
#the criterion that the r_squared gain is negligible. 

angle_0 = angles[0]

def kmeans(k):
    """kmeans uses Kmeans++ to obtain the template postures

    Input: the number k of template postures you want
    Output:
        average_variance = the average variance explained
        centroids = the template postures
        labels = the labels associated with each centroid

    """
    kmeans = cluster.KMeans(init='k-means++',n_clusters=k,max_iter=1000)
    kmeans.fit(angle_0)
    
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_
    
    #compute average variance explained:
    total_var = []
    for i in range(len(centroids)):
        total_var+= [np.corrcoef(centroids[i],j)[0][1]**2 for j in angle_0[np.where(labels == i)]]

    average_variance = np.mean(total_var)
    
    return [average_variance, centroids, labels]


# start = minimum cluster size
# inc = increase in cluster size k
# delta = 
def decision_rule(prev,inc,delta):
    """this function runs the kmeans function defined above as many times as 
        necessary until the difference is less than delta.

        Inputs:
        prev: initial cluster size
        inc: the marginal increase in cluster size k
        delta: R_squared gain that is considered negligible

        Outputs: 
            average_variance = the average variance explained
            centroids = the template postures
            labels = the labels associated with each centroid"""
    
    while kmeans(prev+inc)[0]-kmeans(prev)[0] > delta:
        prev = prev+inc
    variance,centroids,labels = kmeans(prev)
    return variance,centroids,labels
