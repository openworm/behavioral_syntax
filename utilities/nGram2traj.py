#from behavioral_syntax.compression.n_grams import n_grams

#can I import data from a folder?

#import numpy as np

def nGram2traj(postures, nGrams):

    # NGRAM2TRAJ converts a matrix of n-grams into a corresponding matrix of
    # angle trajectories using the input postures.
    # 
    #   nGrams  - a len(dataVec)-(n+1) by n array containing all the n-grams in dataVec  
    
    
    n, m = len(nGrams), len(nGrams[0].split(' '))
    
    angle_trajectories = [[0 for x in range(m)] for x in range(n)]
    
    for i in range(n):
        l1 = nGrams[i].split(' ')
        l2 = [int(i) for i in l1]
        angle_trajectories[i] = [postures[l2[0]],postures[l2[1]],postures[l2[2]]]
    
    return angle_trajectories
