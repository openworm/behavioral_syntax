import numpy as np

def nGram2traj(postures, nGrams):

    # NGRAM2TRAJ converts a matrix of n-grams into a corresponding matrix of
    # angle trajectories using the input postures.
    # 
    #   nGrams  - a len(dataVec)-(n+1) by n array containing all the n-grams in dataVec  
    
    
    
    
    # get the number of points in each posture
    nPts = np.shape(postures)[1]
    
    # convert the n-grams to trajectories
    val1 = np.shape(nGrams)[0]
    val2 = nPts * np.shape(nGrams)[1]
    trajectoryMat = np.array([[np.NaN]*val2 for i in range(val1)])
    for j in range(val1):
        for k in range(val2):
            trajectoryMat[(k-1)*nPts+1:k*nPts][:,j] = postures[nGrams[j][k]]
    
    return trajectoryMat 
