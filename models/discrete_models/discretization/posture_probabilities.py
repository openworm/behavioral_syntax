# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 20:40:43 2015

@author: aidanrocke
"""

#looking at similarity of heatmaps is uninteresting unless
#there's a particular stimulus that is expected to generate
#a similar response. 

#this file should output a statistical test for similar reactions...

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from skimage.measure import structural_similarity as ssim


vec = np.zeros(90)
    
for i in range(90):
    vec[i] = np.corrcoef(mat1[i],mat4[i])[1][0]
    
[i for i in range(90) if vec[i]>0.5]

#mat1 vs mat2
#[9, 18, 39, 64, 68, 73, 83]

#mat1 vs mat3
#87

#mat1 vs mat4:
#37


def posture_probability(image_loc,image_name,sequence,window_fraction):
    """a function that is used to plot the probability of a posture after
    x mins have passed in a given environment. 
    
    INPUTS:
        image_loc: the location where you would like to save the document.
        image_name: the name of the plot that is being generated
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
    
    return matrix
    
#apply structural similarity measure to compare heat maps: 
    



image_loc = '/Users/cyrilrocke/Documents/c_elegans/data/'
image_name = 'heatmap'
window_fraction = .20

if __name__=='__main__':
    from timeit import Timer
    t = Timer(lambda: posture_probability(image_loc,image_name,sequence,window_fraction))
    print(t.timeit(number=1))
    

    
    
    