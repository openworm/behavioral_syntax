# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 22:10:19 2016

@author: aidanrocke
"""

import numpy as np
import seaborn as sns

from behavioral_syntax.utilities import angle_and_skel
#from angle_and_skel import angle, angle2skel
from behavioral_syntax.utilities import loading_data

#from scipy.stats import spearmanr

from scipy.io import loadmat

#raw = loadmat('/Users/cyrilrocke/Documents/c_elegans/data/raw_data/N2 on food L_2009_11_19__12_47_47___4___7_features.mat')

postures = loadmat('/Users/cyrilrocke/behavioral_syntax/data/postures.mat')

#pos = postures.get('postures')
import os

files = os.listdir('/Users/cyrilrocke/Documents/c_elegans/data/raw_data/')
#angles = angles[0]

for i in range(1):
    x,y = loading_data.get_skeletons('/Users/cyrilrocke/Documents/c_elegans/data/raw_data/N2 on food L_2009_11_19__12_47_47___4___7_features.mat')
    #angles2 = angle_and_skel.angle((x,y))[0]
    #angles = np.vstack((angles,angles2))


#rho, pval = spearmanr(pos)

#covariance_matrix = np.cov(pos)

#sns.heatmap(covariance_matrix)
"""
eigen, eigenvec = np.linalg.eigh(covariance_matrix)

zog = [np.abs(i) for i in eigen]
"""
#biggest_eigen = np.sort(mag)
"""


theta = 0

for i in range(48):
    theta += eigenvec[i]

theta_ = np.multiply(theta,pos[:,0])

x,y = angle_and_skel.angle2skel(theta_,np.mean(theta_),1,48)

x2,y2 = angle_and_skel.angle2skel(pos[:,0],np.mean(pos[:,0]),1,48)

plt.plot(x,y)

plt.plot(x2,y2,'steelblue')"""

#looking at more angles:
angles = angle_and_skel.angle((x,y))

angles = angles[0]

covar = np.cov(np.transpose(angles))

eigen, eigenvec = np.linalg.eigh(covar)


theta = np.zeros(48)

for i in range(48):
    theta += eigenvec[i]*np.dot(eigenvec[i],angles[0])
    

x,y = angle_and_skel.angle2skel(theta,np.mean(theta),1,48)

x2,y2 = angle_and_skel.angle2skel(angles[0],np.mean(angles[0]),1,48)

sns.plt.plot(x,y)

sns.plt.plot(x2,y2)

#let's look at how good N eigenvectors are on average:
stat_vec = np.zeros(21004)

for i in range(21004):
    theta = np.zeros(48)

    for j in range(48):
        theta += eigenvec[j]*np.dot(eigenvec[j],angles[j])

    stat_vec[i] = spearmanr(theta,angles[i])[0]


#theta_ = np.multiply(theta,pos[:,0])


def arc_length(x,y):
    d = 0
    for i in range(len(x)-1):
        d += np.sqrt((x[i]-x[i-1])**2+(y[i]-[i-1])**2)
        
    return d
