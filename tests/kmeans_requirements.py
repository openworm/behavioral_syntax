# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 23:26:31 2015

@author: macbook
"""



'''Kmeans requires that:
 1) the variance of the distribution of each variable is spherical
 2) all variables have the same variance so I can use Bartlett's test
 3) the distribution of the cluster sizes is approximately uniform
'''

import numpy as np
from scipy import stats


#let's first try Bartlett's test:
angles = np.load('/Users/cyrilrocke/Documents/c_elegans/data/test1/data/angles.npy')

#check the variances:
Vars = []
for i in range(48):
    Vars.append(np.var(angles[:,i]))

features = []
for i in range(48):
    features.append(angles[:,i])

if stats.bartlett(*features)[1] < 0.05:
    print('We cant use Kmeans')

#now let's test the assumption that cluster sizes are approximately uniformly
#distributed. This test isn't as important as the first. 
all_postures = np.load('/Users/cyrilrocke/Documents/c_elegans/data/arrays/all_postures.npy')
    
ALL = []
for i in range(39):
    ALL+=all_postures[i].split(' ')
    ALL.remove('')

ALL = [int(i) for i in ALL]

if stats.chisquare(ALL)[1] < 0.05:
    print('chisquare fail')