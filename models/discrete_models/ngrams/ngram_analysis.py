"""
Created on Wed Sep  2 23:47:50 2015
@author: aidanrocke
"""

#note: it might be a good idea to add constraints to the simulation...the trigram
#model will result in a lot of sequences that are 'ungrammatical'. 

from behavioral_syntax.utilities.vis_functions import grid_plot
from behavioral_syntax.utilities.string_conversion import plist_to_pstr  
from scipy.stats import itemfreq
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
#import random

all_postures = np.load('/Users/cyrilrocke/Documents/c_elegans/data/arrays/all_postures.npy')

def n_grams(posture_seq, n):
    """ 
    Input:
      posture_seq: a list of posture sequences
      n:            the n in n-grams (also the number of columns in output nGrams)
     
      Output
        nGrams: a len(dataVec)-(n+1) by n array containing all the n-grams in dataVec  
        nGram_seq: a len(dataVec)-(n+1) by n array containing all the n-grams in dataVec
        occurrences: the number of times each unique nGram occurs""" 
    
    #posture_seq = plist_to_pstr(posture_seq)
        
    nGram_seq = []   

    # check inputs
    if len(np.shape(posture_seq)) > 1:
        raise Exception('dataVec must be a row vector')
        
    posture_seq = posture_seq.split(' ')
    dictionary = {}
    for i in range(len(posture_seq)-n+1):
      g = ' '.join(posture_seq[i:i+n])
      nGram_seq.append(g)
      dictionary.setdefault(g, 0)
      dictionary[g] += 1
    
    nGrams = list(dictionary.keys())
    occurrences = dictionary.values()

    
    return dictionary, nGrams, occurrences, nGram_seq
        
        
    
def nGram2traj(postures, nGrams):
    """
      NGRAM2TRAJ converts a matrix of n-grams into a corresponding matrix of
      angle trajectories using the input postures.
     
     Input:
         nGrams: a len(dataVec)-(n+1) by n list containing all the n-grams in dataVec
         postures: an array of template postures that is used as a dictionary
         
    Output:
        angle_trajectories: the trajectory of angles
        """ 
    
    
    n, m = len(nGrams), len(nGrams[0].split(' '))
    
    angle_trajectories = [[0 for x in range(m)] for x in range(n)]
    
    for i in range(n):
        l1 = nGrams[i].split(' ')
        l2 = [int(i) for i in l1]
        angle_trajectories[i] = [postures[l2[0]],postures[l2[1]],postures[l2[2]]]
    
    return angle_trajectories
    


def ngram_discovery(nGram_seq, stepSize):
    """
         ngram_discovery Works through the input matrix of n-grams in
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
        trigram = n_grams(all_postures[0],3)
        
        #looking at the distribution of trigram frequency:
        dist = itemfreq(list(trigram.values()))
    
        #plot cumulative distribution...see whether it's Zipfian or not:
        cum = 0
        cumsum = np.zeros(len(dist[:,1]))
        for j in range(len(dist[:,1])):
            cum+=dist[:,1][j]
            cumsum[j]=cum/np.dot(dist[:,0],dist[:,1])
        
        cumulative.append(cumsum)
        
    grid_plot(cumulative,'CDF','/Users/cyrilrocke/behavioral_syntax/utilities/','trigram_dists')
