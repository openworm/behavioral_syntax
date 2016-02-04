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



def posture_probability(image_loc,image_name,sequence,window_fraction):
    """a function that is used to plot the probability of a posture after
    x mins have passed in a given environment. 
    
    INPUTS:
        sequence: the posture sequence list
        window_fraction:  the fraction that determines the size of each interval
    
    OUTPUTS:
        postures heatmap: this should reveal temporal structure in the 
                          distribution of postures
        histogram_matrix: an len(sequence) by num_postures matrix numpyarray"""
    N = len(sequence)   
    
    window = int(window_fraction*N)
    
    #initialize matrix:
    matrix = np.zeros((90,N-window+1))
    
    #checking the probability that a posture occurs at a particular time. 
    for i in range(90):
        matrix[i] = [sequence[j:j+window].count(i) for j in range(N-window+1)]    
    
    for i in range(N-window+1):
        if sum(matrix[:,i])>0:
            matrix[:,i] = matrix[:,i]/sum(matrix[:,i])
            
        #plt.figure()
        #plt.hist(matrix[i])
        
    ax = plt.axes()
    
    ax.set_title(image_name)    
        
    sns.heatmap(matrix,xticklabels=window,ax=ax)
    
    #return matrix
    
    #save the figure:
    plt.savefig(image_loc+image_name+'.png')
    



    
        
    


    
    
    