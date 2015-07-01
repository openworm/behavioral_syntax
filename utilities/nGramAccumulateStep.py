import numpy as np

def nGramAccumulateStep(nGrams, stepSize):

    # NGRAMACCUMULATENUMERICAL Works through the input matrix of n-grams in
    # chunks to determine growth of number of unique sequences with growing
    # number of observed n-grams.  It can be much faster that 
    # nGramAccumulateNumerical if the step size is large.
    #
    # Input
    #   nGrams   - A matrix of n-grams
    #   stepSize - The step size for moving through n-grams.
    #
    # Output
    #   accCurve - The accumulation curve of previously unseen n-grams as they
    #              occur in nGrams scanned from start to finish
    
    
    
    # get the chunk boundaries
    N = np.size(nGrams)[0]
    chunkBounds = np.linspace(stepSize,stepSize*int(N/stepSize),int(N/stepSize))
    
    # initialise
    accCurve = np.hstack((1,np.array([np.nan]*len(chunkBounds))))
    
    # loop through n-gram chunks
    for i in range(len(chunkBounds)):
        sub_nGrams = nGrams[0:chunkBounds[i]]
        unique_rows = np.array([np.array(x) for x in set(tuple(x) for x in sub_nGrams)])
        accCurve[i+1] = np.shape(unique_rows)[0]
    
    return accCurve
