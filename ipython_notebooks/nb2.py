# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 11:21:55 2015

@author: aidanrocke
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 16:35:56 2015

@author: aidanrocke
"""

from scipy.stats import itemfreq
import numpy as np
from scipy.io import loadmat

postures = loadmat('/Users/cyrilrocke/Documents/c_elegans/data/postures.mat')

directory = '/Users/cyrilrocke/Documents/c_elegans/behavioral_syntax/'

pos = postures['postures']


toy_seq = [time_warp(all_postures[i]) for i in range(39)]

def shape_frequency(toy_seq[0:9]):
    j = 0
    for i in toy_seq[0:9]:
        j+=1
        arr.append(list(map(int, i.split(' '))))
    from vis_functions import grid_plot
    grid_plot(arr,'histogram',directory,'shape_frequency')

j = 0
for i in toy_seq[0:12]:
    arr= list(map(int, i.split(' ')))
    bokeh_bars(arr,str(j))
    j+=1
        



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
    
#non_trivial = [i[0] for i in n_probs if i[1]==max(probs)]


    
def angle_error(angle_arr1,angle_arr2):
    return np.linalg.norm(angle_arr1-angle_arr2)

def variance_explained(angle_arr1,angle_arr2):
    return np.corrcoef(angle_arr1,angle_arr2)[0][1]**2
    
#shapes 80,83,25,64...what do they have in common?
error_matrix = np.zeros((90,90))
for i in range(90):
    error_matrix[i] = np.array([angle_error(pos[:,i],pos[:,j]) for j in range(90)])
    
#looking at the variance matrix:
variance_matrix = np.zeros((90,90))
for i in range(90):
    variance_matrix[i] = np.array([variance_explained(pos[:,i],pos[:,j]) for j in range(90)])
    

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

#Here's a list of the most frequently occurring shapes:
q = [i for i in range(90) if len(missing[i])==1 and missing[i][0] == 25]
    
closest_matches = []
for i in q:
    l = matches(str(i),toy_seq,'closest')
    closest_matches.append(l)
    
    
    

S = set(l[0])
for i in range(1,10):
    S = S.intersection(set(l[i]))

missing = []
for i in range(90):
    missing.append(show_missing(str(i),toy_seq))
    
q = [i for i in range(90) if len(missing[i])==1 and missing[i][0] == 25]


fig, ax = plt.subplots(ncols=1, nrows=1)
plt.plot(z[:,1],'o')
plt.xticks(range(len(z[:,0])), z[:,1], rotation=50, horizontalalignment='right', weight='bold', size='large')


import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows=3, ncols=4)

# Set the ticks and ticklabels for all axes
plt.setp(axes, xticks=[0.1, 0.5, 0.9], xticklabels=['a', 'b', 'c'],
        yticks=[1, 2, 3])

# Use the pyplot interface to change just one subplot...
plt.sca(axes[1, 1])
plt.xticks(range(3), ['A', 'Big', 'Cat'], color='red')

fig.tight_layout()
plt.show()
