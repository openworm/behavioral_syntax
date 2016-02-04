# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 18:38:57 2016

@author: aidanrocke
"""
from behavioral_syntax.utilities.get_features import get_features
from behavioral_syntax.visualization.view_postures import view_postures
from scipy import io

import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import itemfreq

image_loc = '/Users/cyrilrocke/Documents/c_elegans/data/'
image_name = 'posture_distribution'

plt.style.use('ggplot')
postures = '/Users/cyrilrocke/Documents/c_elegans/data/postures'
g = io.loadmat(postures)
postures = g.get('postures')

data = '/Users/cyrilrocke/Documents/c_elegans/data/chemotaxis/'

def posture_distributions(image_loc, image_name,data, postures,sample_ratio,get_features_param=2):
    """we want to see the fractional contribution of each posture to the total
    posture sequence and see whether we observe anything interesting. 
    
    Inputs:
        image_loc: the location where you want to save the output images
        data: the directory containing the files you are interested in
        postures: the template postures that are in use
        sample_ratio: the fraction of the data you want to sample
        gf_param: the get_features_parameter which defines what type of data 
                you want. The default is 2, as this gives you posture sequences.
    
    Outputs:
        frequency distribution image: frequency distributions for each posture
        posture probability image: order of most likely postures from most to 
        least likely
    """

    pos_seq = get_features(data,postures,sample_ratio,get_features_param)
    
    N = len(pos_seq)
    distribution = np.zeros((N,90))    
    
    fig, axes = plt.subplots(ncols=10, nrows=9)
    
    fig.set_size_inches(30, 30)
    ax = axes.ravel()
        
    fig.suptitle(image_name,fontsize=40,weight='bold')
    
    for i in range(N):
        alpha1 = pos_seq[i].split(' ')
        alpha2 = list(map(int,[i for i in alpha1 if i != '']))
        z = itemfreq(alpha2)
        
        set1 = list(z[:,0])
        
        for j in range(90):
            if set1.count(j) == 0:
                distribution[i][j] = 0
            else:
                distribution[i][j] = z[:,1][set1.index(j)]
                
    for i in range(N):
        total = sum(distribution[i])
        for j in range(90):
            distribution[i][j] = distribution[i][j]/total
    
    #compute the average frequency of each posture across different videos:
    average_freq = [np.mean(distribution[:,i]) for i in range(90)]
    sorted_average_freq = np.sort(average_freq) 
    order = [average_freq.index(i) for i in sorted_average_freq]
    
    #show the order in which the postures appear from most probable to least
    #probable.
    view_postures(order,image_loc,'posture probability',postures,sorted_average_freq)
                
    #plot the posture frequency distributions:
    for k in range(90):
        ax[k].bar(range(N),distribution[:,k])
        ax[k].set_title(str(k),size='medium',weight='bold',color='steelblue',backgroundcolor=(1,  0.85490196,  0.7254902))
    
    
    if isinstance(image_loc+image_name,str):
            fig.savefig(image_loc+image_name+'.png',dpi=fig.dpi)