# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 20:40:43 2015

@author: aidanrocke
"""

#looking at similarity of heatmaps is uninteresting unless
#there's a particular stimulus that is expected to generate
#a similar deterministic response over short time scales. 

#this file should output a statistical test for similar reactions...

#it would be great if the computation in compare_matrices was parallelized.

#show heatmaps if and only if the result is non-trivial. 

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

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

#what follows is just pseudo-code.

# 1. get a number(N) randomly chosen sequences of worm skeletons from worm_A_response
#    and worm_B_response to the same stimulus. 
# 2. compute average Dynamic Time Warping distance within-group for both
#    worm_A_response and worm_B_response
# 3. If this average distance for either group is small then produce a heat-map
#    for three randomly selected skeleton sequences and their average.

# This will require loading_data.py, get_features.py,metrics/dynamic_time_warp.py

import loading_data
import get_features
import dynamic_time_warp

skel_A, skel_B = loading_data(group_A), loading_data(group_B) 

#we suppose that 10 is a sufficiently large sample size:
skel_A, skel_B = sample(skel_A,10), sample(skel_B,10)

dist_A, dist_B = np.zeros(45), np.zeros(45)

k = 0
for i in range(10):
    for j in range(i+1,10):
        k+=1
        dist_A[k] = DTW(skel_A[i],skel_A[j])
        
k = 0
for i in range(10):
    for j in range(i+1,10):
        k+=1
        dist_A[k] = DTW(skel_B[i],skel_B[j])
    
distances = np.zeros(100)

for i in range(10):
    p = skel_A[i]
    for j in range(10):
        distances[i,j] = DTW(p,skel_B[j])



# If the distance is small 


def p_matrix(sequence):
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
    
    #initialize matrix:
    matrix = np.zeros((90,N))
    
    #checking the probability that a posture occurs at a particular time. 
    for i in range(90):
        matrix[i] = [sequence[j:j+1].count(i) for j in range(N)]    
    
    #return matrix
    return matrix
    
#apply structural similarity measure to compare heat maps: 
def compare_matrices(group_A_path,group_B_path, image_loc,image_name):
    """do a hypothesis test to see whether there is a significant difference
       between the behaviors demonstrated by the word in seq_folder_a and
       worms in seq_folder_b
       
       Input:
           group_A: this is the numpy file of all posture sequences for a group
                    of worms that responded to a stimulus
           group_B: this is the numpy file of all posture sequences for a group
                    of worms(different from A) that responded to a stimulus
                    
                    it's assumed that there are posture sequences of 
       
       we assume that all the files in """
    
    #load data:
    group_A = np.load(group_A_path)
    group_B = np.load(group_B_path)
    
    n_A = min([len(group_A[i]) for i in range(len(group_A))])
    n_B = min([len(group_B[i]) for i in range(len(group_B))])
    
    N, M = min(n_A, n_B), len(group_A)
    
    matrices_A = [p_matrix(group_A[i][0:N]) for i in range(M)]
    matrices_B = [p_matrix(group_B[i][0:N]) for i in range(M)]
    
    n, m = np.shape(matrices_A[0])
    
    L = []
    
    for j in range(n*m):
        a = np.zeros(M)
        L.append()
        
    
    #plot the average number of occurrences for each matrix:
    ax = plt.axes()
    
    ax.set_title(image_name)    
        
    sns.heatmap(matrix,xticklabels=window,ax=ax)
    
     
    #save the figure:
    #plt.savefig(image_loc+image_name+'.png')


    #perform hierarchical clustering on the matrices:


image_loc = '/Users/cyrilrocke/Documents/c_elegans/data/'
image_name = 'heatmap'
window_fraction = .20

if __name__=='__main__':
    from timeit import Timer
    t = Timer(lambda: posture_probability(image_loc,image_name,sequence,window_fraction))
    print(t.timeit(number=1))
    

    
    
    