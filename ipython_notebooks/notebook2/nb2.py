# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 15:38:07 2015

@author: aidanrocke
"""
import itertools
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import itemfreq
from scipy import io

g = io.loadmat('/Users/cyrilrocke/Documents/c_elegans/data/postures')
postures = g.get('postures')

directory = '/Users/cyrilrocke/Documents/c_elegans/behavioral_syntax/'

pos = postures['postures']

all_postures = np.load('/Users/cyrilrocke/Documents/c_elegans/data/arrays/all_postures.npy')

#time warp function:
def time_warp(sequence):
    e = ''
    sequence = sequence.split(' ')
    l =[]
    for i in sequence:
        if i!=e:
            l.append(i)
            e = i
    #remove spaces(i.e. ''):
    Sequence = ' '.join([x for x in l if x != ''])
    
            
    return Sequence


toy_seq = [time_warp(all_postures[i]) for i in range(39)]

#part1:posture distribution

#work with ten biggest:
sizes = list(map(len,toy_seq))
ten_biggest = [sizes.index(i) for i in sizes[30:39]]
subseq = [toy_seq[i] for i in ten_biggest]

#n_gram finder:
def n_grams(posture_seq, n):
    """ 
    Input:
      posture_seq - a string of shape changes to be compressed
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


#I avoided Laplacian smoothing. There are some bigrams that never appear for
#physiological reasons that are unknown to me:
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
        if isinstance(nplus_grams.get(nplus_gram),int) == 1:
            sub_count = sum({k:v for k,v in nplus_grams.items() if k.startswith(n_gram)}.values())
            prob = (nplus_grams.get(nplus_gram)+1)/(sub_count+vocab_size)
        else:
            prob = 0
    else:
        #prob = 1/vocab_size
        prob = 0
    
    return prob

#visualize the most frequently occurring shapes:



def angle_error(angle_arr1,angle_arr2):
    return np.linalg.norm(angle_arr1-angle_arr2)
    
#shapes 80,83,25,64...what do they have in common?
error_matrix = np.zeros((90,90))
for i in range(90):
    error_matrix[i] = np.array([angle_error(pos[:,i],pos[:,j]) for j in range(90)])
    
    
truth = np.zeros(9)
for i in range(9):
    arr= list(map(int, subseq[i].split(' ')))
    freq = itemfreq(arr)
    freq = freq[np.argsort(freq[:,1])]
    #get the least frequently occurring postures:
    bottom5 = freq[:,0][0:5]
    
    #top5 permutations:
    top5 = freq[:,0][-5:len(freq)]
    top5_perms = list(itertools.permutations(top5, 2))
    top_errors = [error_matrix[i[0]][i[1]] for i in top5_perms]
    
    #mixture:
    mixed_errors = [np.mean([error_matrix[j][i] for i in bottom5]) for j in top5]
    truth[i] = np.mean(np.array(mixed_errors)>np.mean(top_errors))
    
    #look at the difference:
    N_postures(top5,'red',str(i))
    N_postures(bottom5,'steelblue',str(i))
    
    
#the most frequently occurring shapes are similar in shape on average.
fig, ax = plt.subplots()
plt.style.use('ggplot')
plt.bar(range(2),[np.mean(mixed_errors),np.mean(top_errors)],align='center')
plt.xticks(range(2),['mixed_errors','average_top_errors'])
        

    
#show pictures of top 5 most frequently occurring postures vs. 5 least frequently
#occurring postures



    
    
    
#looking at the shapes that most frequently occur with a particular shape:
def matches(posture,toy_seq,kind):
    l = []
    if kind == 'closest':
        for i in range(39):
            if i!= 25:
                n_probs = ngram_probs(toy_seq[i],posture)
                P = max([i[1] for i in n_probs])
                non_trivial = [i[0] for i in n_probs if i[1]==P]
                l.append([int(non_trivial[0]),P])
    else:
        for i in range(39):
            n_probs = ngram_probs(toy_seq[i],posture)
            probs = [i[1] for i in n_probs]
            non_trivial = [i[0] for i in n_probs if i[1]>min(probs)]
            l.append(non_trivial)
    return l
    
#find missing shapes:
#find missing:
#most problematic are 20,25...
def show_missing(posture,toy_seq):
    l = []
    for i in range(39):
        n_probs = ngram_probs(toy_seq[i],posture)
        if len(n_probs) == 0:
            l.append(i)
            
    return l

missing = []
for i in range(90):
    missing.append(show_missing(str(i),toy_seq))
