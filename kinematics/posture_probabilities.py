# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 20:40:43 2015

@author: aidanrocke
"""
#an assortment of functions for evaluating the probability of a posture
#at a particular time. 

#we try to get the parameters of the best fitting weibull distribution for
#each posture. 
import numpy as np
import seaborn as sns




def posture_probability(sequence,posture,window):
    """a function that is used to plot the probability of a posture after
    x mins have passed in a given environment. We use 3 minute time intervals.
    
    INPUTS:
    sequence: the posture sequence #array
    window:  length of the counting intervals #integer
    
    OUTPUTS:
    histogram_matrix: an len(sequence) by num_postures matrix #numpyarray"""
    N = len(sequence)   
    
    #initialize matrix:
    matrix = np.zeros((90,N))
    
    for i in range(90):
        matrix[i] = [sequence[j:j+window].count(i) for j in range(len(sequence)-window+1)] 
        
    if sum(matrix[i])>0:
        matrix[i] = matrix[i]/sum(matrix[i])
        
    sns.heatmap(matrix,xticklabels=window)
    
    return matrix
    
    
    
    