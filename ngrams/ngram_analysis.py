"""
Created on Wed Sep  2 23:47:50 2015
@author: aidanrocke
"""

#note: it might be a good idea to add constraints to the simulation...the trigram
#model will result in a lot of sequences that are 'ungrammatical'. 

#from behavioral_syntax.plotting.vis_functions import grid_plot
from scipy.stats import itemfreq
import numpy as np
import random

#all_postures = np.load('/Users/macbook/Documents/c_elegans/all_postures.npy')

def n_grams(posture_seq, n):
    """ 
    Input:
      posture_seq - a numpy array to be compressed
      n           - the n in n-grams (also the number of columns in output nGrams)
     
      Output
        nGrams  - a len(dataVec)-(n+1) by n array containing all the n-grams in dataVec  
        nGram_seq  - a len(dataVec)-(n+1) by n array containing all the n-grams in dataVec
        occurrences - the number of times each unique nGram occurs""" 
        
    nGram_seq = []   

    # check inputs
    if len(np.shape(posture_seq)) > 1:
        raise Exception('dataVec must be a row vector')
        
    posture_seq = posture_seq.split(' ')
    output = {}
    for i in range(len(posture_seq)-n+1):
      g = ' '.join(posture_seq[i:i+n])
      nGram_seq.append(g)
      output.setdefault(g, 0)
      output[g] += 1
    
    nGrams = list(output.keys())
    occurrences = output.values()
    
    return output, nGrams, occurrences, nGram_seq
        
        
    
def nGram2traj(postures, nGrams):
    """
      NGRAM2TRAJ converts a matrix of n-grams into a corresponding matrix of
      angle trajectories using the input postures.
     
        nGrams  - a len(dataVec)-(n+1) by n list containing all the n-grams in dataVec """ 
    
    
    n, m = len(nGrams), len(nGrams[0].split(' '))
    
    angle_trajectories = [[0 for x in range(m)] for x in range(n)]
    
    for i in range(n):
        l1 = nGrams[i].split(' ')
        l2 = [int(i) for i in l1]
        angle_trajectories[i] = [postures[l2[0]],postures[l2[1]],postures[l2[2]]]
    
    return angle_trajectories
    


def nGramAccumulateStep(nGram_seq, stepSize):
    """
         NGRAMACCUMULATENUMERICAL Works through the input matrix of n-grams in
          chunks to determine growth of number of unique sequences with growing
          number of observed n-grams.  It can be much faster that 
          nGramAccumulateNumerical if the step size is large.
         
          Input
            nGram_seq   - A temporal sequence of n-grams
            stepSize - The step size for moving through n-grams.
         
          Output
            accCurve - The accumulation curve of previously unseen n-grams as they
                       occur in nGrams scanned from start to finish"""
    
    
    
    # get the chunk boundaries
    N = len(nGram_seq)
    chunkBounds = np.linspace(stepSize,stepSize*int(N/stepSize),int(N/stepSize))
    
    # initialise
    accCurve = np.hstack((1,np.array([np.nan]*len(chunkBounds))))
    
    # loop through n-gram chunks
    for i in range(len(chunkBounds)):
        sub_nGrams = nGram_seq[0:int(chunkBounds[i])]
        accCurve[i+1] = len(set(sub_nGrams))
    
    return accCurve

#plotting nGram cumulative distribution:

def cumulative():
    N = len(all_postures)
    cumulative = []
    
    for i in range(N):
        trigram = ngrams(all_postures[0],3)
        
        #looking at the distribution of trigram frequency:
        dist = itemfreq(list(trigram.values()))
    
        #plot cumulative distribution...see whether it's Zipfian or not:
        cum = 0
        cumsum = np.zeros(len(dist[:,1]))
        for j in range(len(dist[:,1])):
            cum+=dist[:,1][j]
            cumsum[j]=cum/np.dot(dist[:,0],dist[:,1])
        
        cumulative.append(cumsum)
        
    grid_plot(cumulative,'CDF','/Users/macbook/Github/behavioral_syntax/plotting/','trigram_dists')
