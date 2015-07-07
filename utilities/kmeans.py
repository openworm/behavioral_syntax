from sklearn.cluster import KMeans

def kmeans(angle_data):
#here I'm assuming that all the angle arrays have been rotated so that 
#they are on directed to the right. 
    k_means = KMeans(init='k-means++', n_clusters=90, n_init=20)

    k_means.fit(angle_data)
    
    postures = k_means.cluster_centers_
    
    return postures
