# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 12:41:16 2015

@author: macbook
"""

import matplotlib.pyplot as plt
from math import sqrt
from scipy.stats import itemfreq
import numpy as np




plt.style.use('ggplot')

def grid_plot(list,image_loc,image_name):
    N = len(list)
    
    #we select an n*n subset of the multi_array of length N which for n>=16
    #is always greater than 99% of the members of the multi_array. 
    n = round(sqrt(N))
    

    fig, axes = plt.subplots(ncols=n, nrows=n+1)
    
    fig.set_size_inches(30, 30)
    ax = axes.ravel()
    
    fig.suptitle(image_name,fontsize=40,weight='bold')
    
    j = 0
    for i in range(N):
        z = itemfreq(list[j])
        ax[i].plot(z[:,0],z[:,1],'o')
        ax[i].set_title(str(j),size='medium',weight='bold',color='steelblue',backgroundcolor=(1,  0.85490196,  0.7254902))
        j+=1
        
    
    
    fig.savefig(image_loc+image_name+'.png',dpi=fig.dpi)
    
grid_plot(all_pauses,'/Users/macbook/Github/behavioral_syntax/plotting/pauses/','15_pause_distributions')
    
