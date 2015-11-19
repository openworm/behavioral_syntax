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
import matplotlib.pyplot as plt

plt.style.use('ggplot')



def posture_probability(sequence,window):
    """a function that is used to plot the probability of a posture after
    x mins have passed in a given environment. 
    
    INPUTS:
    sequence: the posture sequence #list
    window:  length of the counting intervals #integer
    
    OUTPUTS:
    histogram_matrix: an len(sequence) by num_postures matrix #numpyarray"""
    N = len(sequence)   
    
    #initialize matrix:
    matrix = np.zeros((90,N))
    
    #checking the probability that a posture occurs at a particular time. 
    for i in range(90):
        matrix[i] = [sequence[j:j+window].count(i) for j in range(N-window+1)]    
    
    for i in range(N-window+1):
        if sum(matrix[:,i])>0:
            matrix[:,i] = matrix[:,i]/sum(matrix[:,i])
            
        plt.figure()
        plt.hist(matrix[i])
        
    #checking the probability that a 
        
        
    sns.heatmap(matrix,xticklabels=window)
    
    return matrix
    



    
        
    


    
    
    