# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 16:16:01 2015

@author: aidanrocke
"""
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
      locations.append([i,i+n])
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
    
def rules(sequence):
    k = int(len(sequence.split(' '))/2)
    i = 0
    output = {}
    while k > 2:
        data = subsequences(sequence,k)
        counts = data['sequences'].value_counts()
        if len(counts) > 0 and counts[0] > 1:
            new_rule = counts.index[0]
            sequence = sequence.replace(new_rule,'A'+str(i))
            output['A'+str(i)] = new_rule
            k = int(len(sequence.split(' '))/2)
            i+=1
        else:
            k-=1
            
    df = pd.DataFrame.from_dict(data=output,orient='index')
    N = len(df)
            
    for i in range(N):
        i = 0
        old = df.ix[i][0]
        new = df.index[i]
 
        labels = [df.ix[j][0] for j in range(N)]
        #update df:
        modified = labels[0:i+1]+[j.replace(old,new) for j in labels[i+1:N]]
        df = pd.DataFrame(modified,index = df.index)
            
    return sequence, output, df
    

    
            
 
