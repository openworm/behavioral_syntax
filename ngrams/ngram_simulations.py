# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 18:10:01 2015

@author: aidanrocke
"""

import numpy as np
import random

all_postures = np.load('/Users/cyrilrocke/Documents/c_elegans/data/arrays/all_postures.npy')

s=''
for i in range(len(all_postures)):
    s+=all_postures[i]+' '

def time_warp(sequence):
    e = ''
    sequence = sequence.split(' ')
    l =[]
    for i in sequence:
        if i!=e:
            l.append(i)
            e = i
            
    return ' '.join(l)

def n_grams(sequence, n):
    """ 
    Input:
      sequence - a numpy array to be compressed
      n           - the n in n-grams (also the number of columns in output nGrams)
     
      Output
        nGrams  - a len(dataVec)-(n+1) by n array containing all the n-grams in dataVec  
        nGram_seq  - a len(dataVec)-(n+1) by n array containing all the n-grams in dataVec
        occurrences - the number of times each unique nGram occurs""" 
        
    nGram_seq = []   

    # check inputs
    if len(np.shape(sequence)) > 1:
        raise Exception('dataVec must be a row vector')
        
    sequence = sequence.split(' ')
    output = {}
    for i in range(len(sequence)-n+1):
      g = ' '.join(sequence[i:i+n])
      nGram_seq.append(g)
      output.setdefault(g, 0)
      output[g] += 1
    
    nGrams = list(output.keys())
    occurrences = output.values()
    
    return output, nGrams, occurrences, nGram_seq


#note laplacian smoothing creates errors. Somehow, the sum of probabilities ends up 
#being greater than 1.
def calc_prob(sequence,trigram,bigram):
    #vocab_size is set to 90 for the behavioral_syntax paper
    """ 
    Input:
      sequence - a string of posture changes
      bigram- a particular bigram in sequence
      trigram - a particular trigram that starts with the bigram
     
      Output
        prob-the conditional probability that this particular trigram occurs using 
             Laplacian smoothing. Note: Laplacian smoothing actually creates errors. 
        """ 
    vocab_size = len(set((sequence.split(' '))))
  
    trigrams, x, y, z = n_grams(sequence,3)
    
    if trigram.split(' ')[0:2] == bigram.split(' '):
        sub_count = sum({k:v for k,v in trigrams.items() if k.startswith(bigram)}.values())
        prob = (trigrams.get(trigram)+1)/(sub_count+vocab_size)
    else:
        prob = 1/vocab_size
    
    return prob

def random_distr(l):
    """function that can be used to simulate the terminal symbol of an n-gram given 
       the previous values.
    """
    r = random.uniform(0, 1)
    s = 0
    for item, prob in l:
        s += prob
        if s >= r:
            return item
    return l[-1]


def trigram_probs(sequence,bigram):
    l = []
    
    w,x,y,z = n_grams(sequence,3)

    for i in x:
        prob = calc_prob(sequence,i,bigram)
        terminal = i.split(' ')[2]
        l.append([terminal,prob])
        
    return l
    
#simulate new sequence:
def sim_seq(N,sequence,initial_conditions):
    """ 
    Input:
      N-length of the sequence you want to simulate
      initial_conditions-the two initial symbols that start the simulation
     
      Output
        simulated_seq- the simulated sequence
        """ 
    #arr = list(np.zeros(100))
    #arr[0:2] = ['z','6']
    arr = list(np.zeros(N))
    arr[0:2] = initial_conditions.split(' ')
    
    for i in range(2,len(arr)):
        bigram = ' '.join(arr[i-2:i])
        l = trigram_probs(sequence,bigram)
        arr[i] = random_distr(l)
    
    simulated_seq = ' '.join(arr)
        
    return simulated_seq
    
#see whether I have generated realistic n_grams where n>3:
def test(real_sequence, simulations):
    """ 
    Input:
      real_sequence - a string of posture changes that wasn't simulated
      simulations-the number of simulations you want to run.
     
      Output
        average_correctness- the average number of times the simulations produces
                             n_grams which actually exist. 
        """ 
    length = len(real_sequence.split(' '))
        
    w,x,y,z = n_grams(real_sequence,3)
    w,x2,y,z = n_grams(real_sequence,2)
    
    #run 50 simulations:
    values = list(np.zeros(simulations))
    
    for j in range(simulations):
        
        for i in x2:
            S = sim_seq(length,real_sequence,i)
            wS,xS,yS,zS = n_grams(S,3)
        values[j] = len(list(set(x).intersection(xS)))/len(x)
    
    return np.mean(values)
    
