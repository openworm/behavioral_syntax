# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 18:10:01 2015

@author: aidanrocke
"""
import itertools
import numpy as np
import random

all_postures = np.load('/Users/cyrilrocke/Documents/c_elegans/data/arrays/all_postures.npy')



def time_warp(sequence):
    e = ''
    sequence = sequence.split(' ')
    l =[]
    for i in sequence:
        if i!=e:
            l.append(i)
            e = i
            
    return ' '.join(l)
    
sequence=''
for i in range(len(all_postures)):
    sequence+=all_postures[i]+' '

#have a look at all the postures:
def simplify(all_postures):
    Sequence = sequence.split(' ')
        
    Sequence = [x for x in Sequence if x != '']
    
    Sequence = ' '.join(Sequence)
        
    return time_warp(Sequence)

def n_grams(sequence, n):
    """ 
    Input:
      sequence - numpy array: a numpy array to be compressed
      n        - int: the n in n-grams (also the number of columns in output nGrams)
     
      Output
        nGrams  - list: a len(dataVec)-(n+1) by n list containing all the n-grams in dataVec  
        nGram_seq  - list: a len(dataVec)-(n+1) by n list containing all the n-grams in dataVec
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
def calc_prob(sequence,n_gram,nplus_gram):
    #vocab_size is set to 90 for the behavioral_syntax paper
    """ 
    Input:
      sequence - a string of posture changes
      n_gram - a particular ngram 
      nplus_gram- a particular (n+1)_gram that begins whose first n values 
                  are those given by n_gram
     
      Output
        prob-the conditional probability that this particular trigram occurs using 
             Laplacian smoothing. Note: Laplacian smoothing actually creates errors. 
        """
    vocab_size = len(set((sequence.split(' '))))
    
    m = len(nplus_gram.split(' '))
    nplus_grams, x, y, z = n_grams(sequence,m)
    
    if nplus_gram.split(' ')[0:m-1] == n_gram.split(' '):
        sub_count = sum({k:v for k,v in nplus_grams.items() if k.startswith(n_gram)}.values())
        prob = (nplus_grams.get(nplus_gram)+1)/(sub_count+vocab_size)
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


def ngram_probs(sequence,n_gram):
    l = []
    
    N = len(n_gram.split(' '))+1
    
    w,x,y,z = n_grams(sequence,N)

    for i in x:
        if i.split(' ')[0:N-1] == n_gram.split(' '):
            prob = calc_prob(sequence,n_gram,i)
            terminal = i.split(' ')[N-1]
            l.append([terminal,prob])
            
    #create the complete reference set of possible n_grams:
    n_gram_list = [list(i) for i in list(itertools.permutations(list(range(90)), N))]
    n_gram_list = [[str(j) for j in i] for i in n_gram_list]
    n_gram_list = [' '.join(i) for i in n_gram_list]
        
    sub_alpha = [l[i][0] for i in range(len(l))]
    diff = [x for x in n_gram_list if x not in sub_alpha]
    for i in diff:
        terminal = i.split(' ')[N-1]
        l.append([terminal,float(1/90)])
    
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
    n = len(initial_conditions.split(' '))
        
    arr = list(np.zeros(N))
    arr[0:n] = initial_conditions.split(' ')
    
    for i in range(2,len(arr)):
        bigram = ' '.join(arr[i-n:i])
        l = ngram_probs(sequence,bigram)
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
    
