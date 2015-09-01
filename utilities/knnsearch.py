@author: aidanrocke

import numpy as np

#inputs are either nxd numpy arrays in a d-dimensional space or integers for the 
#value of K.

#outputs are nxK lists

def knnsearch(*args):
    X = args
    n_args = len(args)
    
#the shape of the argument matters as well.
    
    if n_args == 1:
        neighbors = list(np.zeros(len(X)))
        for i in range(len(X)):
            distances = [np.inf]*len(X)
            members = list(set(range(len(X)))-set([i]))
            for j in members:
                distances[j] = np.linalg.norm(X[i,:]-X[j,:])
            #find the smallest value
            val = min(distances)
            neighbors[i] = distances.index(val)
        
    elif n_args == 2 and len(np.shape(X[2])) == 0:
        K = X[2]
        X = X[1]
        x1 = np.shape(X)[0]
        neighbors = [[0] * K for i in range(x1)]
        for i in range(len(X)):
            distances = [np.inf]*len(X)
            members = list(set(range(len(X)))-set([i]))
            for j in members:
                distances[j] = np.linalg.norm(X[i,:]-X[j,:])
            #find the K smallest values
            val = np.sort(distances)
            for k in range(K):
                neighbors[i][k] = distances.index(val[k])
                
    elif n_args == 2 and len(np.shape(X[2])) == 2:
        #when K is not given, K==1
        Q = X[1]
        R = X[2]
        neighbors = list(np.zeros(len(Q)))
        for i in range(len(Q)):
            distances = [np.inf]*len(Q)
            members = list(range(len(Q)))
            for j in range(len(R)):
                distances[j] = np.linalg.norm(Q[i,:]-R[j,:])
                
            #find the smallest value
            val = min(distances)
            neighbors[i] = distances.index(val)
            
    elif n_args == 3 and len(np.shape(X[2])) == 2:
        Q = X[1]
        R = X[2]
        K = X[3]
        x1 = np.shape(Q)[0]
        neighbors = [[0] * K for i in range(x1)]
        for i in range(len(Q)):
            distances = [np.inf]*len(Q)
            members = list(set(range(len(Q)))-set([i]))
            for j in range(len(R)):
                distances[j] = np.linalg.norm(Q[i,:]-R[j,:])
            #find the K smallest values
            val = np.sort(distances)
            for k in range(K):
                neighbors[i][k] = distances.index(val[k])

