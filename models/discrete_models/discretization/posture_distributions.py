# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 18:38:57 2016

@author: aidanrocke
"""
from behavioral_syntax.utilities.get_features import get_features
from scipy import io

import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import itemfreq

plt.style.use('ggplot')

postures = '/Users/cyrilrocke/Documents/c_elegans/data/postures'
g = io.loadmat(postures)
postures = g.get('postures')

data = '/Users/cyrilrocke/Documents/c_elegans/data/chemotaxis/'

pos_seq = get_features(data,postures,0.3,2)

N = len(pos_seq)
distribution = np.zeros((N,90))    

fig, axes = plt.subplots(ncols=10, nrows=9)

fig.set_size_inches(30, 30)
ax = axes.ravel()

image_name = 'posture_distributions'

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
            
for k in range(90):
    ax[k].bar(range(N),distribution[:,k])
    ax[k].set_title(str(k),size='medium',weight='bold',color='steelblue',backgroundcolor=(1,  0.85490196,  0.7254902))
    
image_loc = '/Users/cyrilrocke/Documents/c_elegans/data/'


if isinstance(image_loc+image_name,str):
        fig.savefig(image_loc+image_name+'.png',dpi=fig.dpi)