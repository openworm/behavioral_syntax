# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 14:41:55 2015

@author: aidanrocke99
"""
#duration_distributions

from behavioral_syntax.plotting.vis_functions import grid_plot
from scipy.stats import itemfreq
from matplotlib import pyplot as plt
from scipy import io
from pandas import Series

import os
import numpy as np
import h5py

"""
remark: there are no absolute pauses that can be detected with certainty. 
        So we can't say that we have detected pauses unless the raw data
        confirms that. But, we can say that we can detect insignificant 
        movement.
        """

directory = '/Users/macbook/Documents/c_elegans/raw_data/on-food-1/'
files = os.listdir(directory)[1:16]

g = io.loadmat('/Users/macbook/Github/behavioral_syntax/data/'+'postures.mat')
postures = g.get('postures')

all_postures = []




def duration_distributions(directory,postures):
    files = os.listdir(directory)
    
    N = len(files)

    for i in range(N):
        #get skeleton data:
        f = io.loadmat(directory+files[i])
        #getting the right cell array:
        X = f['worm']['posture'][0][0][0]['skeleton'][0][0][0][0]
        Y = f['worm']['posture'][0][0][0]['skeleton'][0][0][0][0]
        
        X = X.T
        Y= Y.T
        
        indices = []
        for j in range(len(X)):
            if sum(np.isnan(X[j]))== 0:
                indices.append(j)
            
        X = X[indices] 
        Y = Y[indices]
        
        angles, mean = angle(X,Y)
        C,c = np.shape(X)
    
        
        posture_sequence = list(np.zeros(C))
        
        for i in range(C):
            distances = [np.inf]*90
            for j in range(90):
                distances[j] = np.linalg.norm(angles[i]-postures[:,j])
            val = min(distances)
            posture_sequence[i] = distances.index(val)
            
        all_postures.append(posture_sequence)
        
    #distribution of pauses:
    def pauses(ts):
        """ Return the distribution of pauses.
        """
        j = 0
        pauses = []
        most_recent_elem = None
        for e in ts:
            if e == most_recent_elem:
                j+=1
            else:
                most_recent_elem = e
                pauses.append(j)
                j=0
    
        return pauses
    
    all_pauses = []
    for i in range(N):
        all_pauses.append(pauses(all_postures[i]))
        
    grid_plot(all_pauses,directory[:-24]+'plotting/pauses/','15_pause_distributions')
      
    
    #one plot of everything:
    P = []
    for i in range(N):
        P+=all_pauses[i]
        
    fig, axis = plt.subplots(ncols=1, nrows=1)
    fig.set_size_inches(20, 20)
    z = itemfreq(P)
    axis.plot(z[:,0],z[:,1],'o')
    axis.set_title('length of pauses',size='medium',weight='bold',color='steelblue',backgroundcolor=(1,  0.85490196,  0.7254902))
    fig.savefig('/Users/macbook/Github/behavioral_syntax/plotting/pauses/'+'distribution of pauses'+'.png',dpi=fig.dpi)
    
    
    
    #time spent in each posture:
    posture_distribution = []
    #correct for segmentation faults:
    for i in range(15):
        z = itemfreq(all_postures[i])
        rows, cols = np.shape(z)
        q = np.zeros((rows,cols))
        q[:,1] = z[:,1]/sum(z[:,1])
        q[:,0] = z[:,0]
        posture_distribution.append(q)
        
    
    for i in range(15):
        fig = plt.figure()
        plt.bar(posture_distribution[i][:,0],posture_distribution[i][:,1])
        fig.savefig('/Users/macbook/Github/behavioral_syntax/plots/'+str(i)+'.png',dpi=fig.dpi)
