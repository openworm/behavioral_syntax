import numpy as np

def n_gramsNumerical(dataVec, n):
# Input
#   dataVec - a numpy array to be compressed
#   n       - the n in n-grams (also the number of columns in output nGrams)
#
# Output
#   nGrams  - a len(dataVec)-(n+1) by n array containing all the n-grams in dataVec    

    # check inputs
    if len(np.shape(dataVec)) > 1:
        raise Exception('dataVec must be a row vector')
        
    else:
        if n == 1:
            nGrams = dataVec[np.newaxis].T
        
        elif (n != 1) and (n <= 10):
            nGrams = dataVec
            for i in range(n):
                row = np.hstack((dataVec[i+1:],np.array([np.NaN]*(i+1))))
                nGrams = np.vstack((nGrams,row))
            
        else:
            nGrams = np.empty((n,len(dataVec))
            nGrams.fill(np.nan)
            for i in range(n):
                nGrams[i] = np.roll(dataVec, i)
                
        nGrams = nGrams.T
        #drop extra rows
        nGrams = nGrams[0]
        
        return nGrams
