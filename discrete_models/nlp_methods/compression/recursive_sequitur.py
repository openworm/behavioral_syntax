# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 14:09:51 2015

@author: aidanrocke
"""

import numpy as np

sequence = '1 2 3 4 2 3 z 6 c 1 2 3 4 2 3 z 6 1 1 1 1 a b 1 1 1 1'

rules = []

def non_overlap(block,n):
    if type(block) == str:
        L = block
    else:
        L = ''
        for i in block[0:-1]:
            L+=i+' '
        L+=block[-1]
    j = 0
    while j < len(L)-1: 
        if word_count(L[0:j]) < n:
            j+=1
        else:
            L = L[j-1:]
    q = 0
    m = len(L)  
    while q < m-1:
        if word_count(L[m-1-q:m])<n:
            q+=1
        else:
            L=L[j-1:m-1-q-1]
        
    return L

def get_indices(z,val,n):
    L = [i for i, x in enumerate(z) if x == val]
    
    M = [L[0]]
    j = 0
    for i in range(1,len(L)):
        if L[i]-M[j]>n:
            M.append(L[i])
            j+=1
    return M, L


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
    
    Z = posture_seq
    posture_seq = posture_seq.split(' ')
    output = {}
    for i in range(len(posture_seq)-n+1):
      g = ' '.join(posture_seq[i:i+n])
      nGram_seq.append(g)
      output[g] = Z.count(g)
    
    nGrams = list(output.keys())
    occurrences = output.values()
    
    return nGrams, occurrences, nGram_seq

def word_count(sequence):
    Z = sequence.split(' ')
    total = 0
    for i in Z:
        if len(i)>0:
            total+=1
    return total

def new_rule(sequence,rules,x,y,z):
    y = list(y)
    if max(y)>1 and len(y) > 1:
        ind = y.index(max(y))
        
        n = word_count(x[ind])
        locations, occurrences = get_indices(z,x[ind],n)
        
        #srr=sequence[0:locations[0]-1]
        
        new_rule = 'A'+str(len(rules)+1)+'A'
        for i in locations:
            sequence[i] = new_rule
    
    
    rules.append([new_rule,x[ind]])
                
    return sequence, rules



def sequitur(sequence,rules):
    count_down = word_count(sequence)-1
    
    x,y,z = n_grams(sequence,count_down)
    
    while count_down>1:
        #len(y) > 1 and 
        if len(y) > 1 and max(y) > 1:
            sequence, rules = new_rule(sequence,rules,x,y,z)
            x,y,z = n_grams(sequence,count_down)
            
        else:
            count_down-=1
            x,y,z = n_grams(sequence,count_down)
            
    return sequence, rules
    
def rule_recursion(rules):
    for i in range(len(rules)):
        M = len(rules)
        S, rule_X = sequitur(rules[i][1],rules)
        
        N = len(rule_X)-M
        if N > 0:
            for j in range(N):
                rule_X[i][1] = rule_X[i][1].replace(rule_X[M+j][1],rule_X[M+j][0])
            
            rules = rule_X
            
    return rules
    
def recursive_sequitur(sequence, rules):
    sequence, rules = sequitur(sequence, rules)
    return sequence, rule_recursion(rules)
    
print(recursive_sequitur(sequence, []))

#tests:
def get_unique(seq, val=1):

    for i in range(1,word_count(seq)-1):
        x,y,z = n_grams(seq,i)
        x = np.array(x)
        y = np.array(list(y))
        L = [i[0]=='A' for i in x[y>1]]
        
        if len(L)>0 and np.mean(L)<1:
            val=0
            raise ValueError("we aren't getting unique values")
            
    print(val)
