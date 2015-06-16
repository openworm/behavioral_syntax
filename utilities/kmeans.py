import numpy as np
#from sklearn import cluster


def initialize(X, K):
    C = [X[0]]
    for k in range(1, K):
        D2 = scipy.array([min([scipy.inner(c-x,c-x) for c in C]) for x in X])
        probs = D2/D2.sum()
        cumprobs = probs.cumsum()
        r = scipy.rand()
        for j,p in enumerate(cumprobs):
            if r < p:
                i = j
                break
        C.append(X[i])
    return C

def calcJ(X, centers):
    diffsq = (centers[:,np.newaxis,:]-X)**2
    return np.sum(np.min(np.sum(diffsq,axis=2),axis=0))
    
def kmeans(X,k,n=100):
    #initialize centers and list J to track performance metric
    centers = initalize(X,k)
    J = []
    
    #repeat n times
    for iteration in range(n):
        #zhich center is each sample closest to?
        sqdistances = np.sum((centers[:,np.newaxis,:]-X)**2,axis=2)
        closest = np.argmin(sqdistances, axis=0)
        
        #calculate J and append to list J
        J.append(calcJ(X,centers))
        
        #update cluster centers
        for i in range(k):
            centers [i,:] = X[closest=i,:].mean(axis=0)
            
        #calculate J a final time and return results
        J.append(calcJ(data,centers))
        return centers, J, closest
