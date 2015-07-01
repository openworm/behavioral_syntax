def ismember(A, B):
    return [ np.sum(a == B) for a in A ]

def simSeq(uniqueNGrams, counts, seqLength, startState):

# SIMSEQ simulates a new sequence of length seqLength based on the input 
# matrix of unique n-grams and corresponding count vector, which define the
# empirical distribution that will be drawn on to generate the simulated 
# sequence.
# 
# Input
#   uniqueNGrams - an N x n numpy array of n-grams observed in the set of
#                  training sequences (N is the number of unique n-grams)
#   counts       - an N x 1 numpy array of counts (the number of times each
#                  unique n-gram was observed in the training set)
#   seqLength    - the length of the simulated sequence
#   startState   - a 1 x (n - 1) vector defining the starting state
# 
# Output
#   sequence     - a 1 x seqLength sequence of states



    # get n-gram order
    n = np.shape(uniqueNGrams)[1]
    m = np.shape(uniqueNGrams)[0]
    
    # check arguments
    if np.shape(uniqueNGrams)[0] != len(counts):
        raise Exception('Sizes of uniqueNGrams and counts do not match.')
        
    [testGrams, cts] = countUniqueRows(uniqueNGrams)
    
    if np.any(testGrams.ravel() != uniqueNGrams.ravel()):
        raise Exception('uniqueNGrams must have only unique, sorted rows.')
        
    if len(startState) != n - 1:
        raise Exception('startState must be 1 element shorter than input n-grams.')
    
    # get the largest state label (note, it doesn't matter if the number of
    # possible states in the training data is larger than this in principle
    # because we are only sampling from the states that were actually observed)
    maxState = max(uniqueNGrams.ravel())
    
    # get the unique (n - 1)-grams from uniqueNGrams
    [roots, cts] = countUniqueRows(uniqueNGrams[:,:-1])
    
    # fill in the transition probability matrix
    transProb = np.zeros([np.shape(roots)[0], maxState])
    currentRoot = uniqueNGrams[1,:-1]
    
    j = 1
    for i in range(m):
        # check to see if the root has changed
        if any(currentRoot != uniqueNGrams[i, :-1]):
            # convert transProb from counts to probabilities
            transProb[j] = transProb[j] / sum(transProb[j])
            
            # update current root
            currentRoot = uniqueNGrams[i, :-1];
            
            # increment transProb index
            j+=1
        
        # fill in the current row of the transition probability matrix
        transProb[j][uniqueNGrams[i][n]] = counts[i]
    
    # also normalise the last row
    transProb[n] = transProb[n]/sum(transProb[n])
    
    # get the cummulative probability for each row
    cumProb = np.cumsum(transProb, 1)
    
    # initialise the output sequence
    sequence = [np.nan]*seqLength
    sequence[:n - 1] = startState
    
    # get random numbers for selecting next part of sequence
    randNums = np.random.rand(seqLength, 1)
    
    # generate the sequence
    for i in range(n,seqLength-len(startState)):
        # find the current root
        [~, matchInd] = ismember(roots, sequence(ii-n+1:ii-1), 'rows')
        matchInd = logical(matchInd)
        
        # find the next element in the sequence
        binInd = np.digitize(randNums[i], cumProb[matchInd])
        
        # add 1 to binInd to change from zero indexing
        sequence[i] = binInd + 1
