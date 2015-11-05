import numpy as np
import pandas as pd

sequence = '1 2 3 4 2 3 z 6 c 1 2 3 4 2 3 z 6 1 1 1 1 a b 1 1 1 1'

def subsequences(posture_seq, n):
    """ 
    Input:
      posture_seq - a numpy array to be compressed
      n           - the n in n-grams (also the number of columns in output nGrams)
     
      Output
        nGrams  - a len(dataVec)-(n+1) by n array containing all the n-grams in dataVec  
        nGram_seq  - a len(dataVec)-(n+1) by n array containing all the n-grams in dataVec
        occurrences - the number of times each unique nGram occurs""" 
        
    nGram_seq = [] 
    locations = []
    
    #set membership: [x for x in nGram_seq if x in non_triv]

    # check inputs
    if len(np.shape(posture_seq)) > 1:
        raise Exception('dataVec must be a row vector')
    
    Z = posture_seq
    posture_seq = posture_seq.split(' ')
    output = {}
    for i in range(len(posture_seq)-n+1):
      g = ' '.join(posture_seq[i:i+n])
      nGram_seq.append(g)
      locations.append(list(range(i,i+n+1)))
      output[g] = Z.count(g)
    
    nGrams = np.array(list(output.keys()))
    occurrences = np.array(list(output.values()))
    
    non_triv = nGrams[occurrences>1]
    
    #create dataframe:
    columns = ['sequences','locations']
    df = pd.DataFrame(columns=columns,index = np.arange(len(nGram_seq)))
    df.sequences = nGram_seq
    df.locations = locations
    
    return df[df['sequences'].isin(non_triv)]
