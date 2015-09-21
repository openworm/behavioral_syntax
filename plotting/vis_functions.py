# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 12:41:16 2015

@author: macbook
"""

import matplotlib.pyplot as plt
from math import sqrt
from scipy.stats import itemfreq
import numpy as np
from scipy import io
#for bokeh charts:
from bokeh.plotting import show, output_file
from bokeh.charts import Bar

#visualizing postures is probably one of the most important tasks:
g = io.loadmat('/Users/cyrilrocke/Documents/c_elegans/data/postures')
postures = g.get('postures')
plt.style.use('ggplot')

def N_postures(sequence,color,title,image_loc,image_name):
    sequence = list(sequence)
    mean_angles = np.zeros(90)
    
    for i in sequence:
        mean_angles[i] = np.mean(postures[:,i])
        
    X,Y = MA2skel(postures.T,mean_angles,1)
    
    N = len(sequence)
    if N>6:
        n = round(sqrt(N))+1
        fig, axes = plt.subplots(ncols=n, nrows=n)
        fig.set_size_inches(n, n)
    else:
        fig, axes = plt.subplots(ncols=N, nrows=1)
        fig.set_size_inches(N, round(N/2))
    fig.suptitle(title, fontsize=14, fontweight='bold')
    
    axes = axes.ravel()
    j = 0
    for j in range(len(sequence)):
        axes[j].plot(X[sequence[j]],Y[sequence[j]],color=color,lw=5)
        axes[j].set_title(str(j),size='medium',weight='bold',color='steelblue',backgroundcolor=(1,  0.85490196,  0.7254902))
        axes[j].axis('off')
        j+=1
    
    #save to file only if that's what you actually want 
    if isinstance(image_loc+image_name,str):
        fig.savefig(image_loc+image_name+'.png',dpi=fig.dpi)
        

def bokeh_bars(liszt,name):
    
    z = itemfreq(liszt)
    z = z[np.argsort(z[:,1])]
    data = {"y": list(z[:,1])}
    
    #it would be great if there was a way to automatically fit the bokeh plot to the screen: 
    bar = Bar(data, list(map(str,z[:,0])), title="bars",width=1000,height=500)
    
    output_file(name+".html", title=name)
    
    show(bar)

plt.style.use('ggplot')

def grid_plot(list,kind,image_loc,image_name):
    N = len(list)
    
    #we select an n*n subset of the multi_array of length N which for n>=16
    #is always greater than 99% of the members of the multi_array. 
    n = round(sqrt(N))
    

    fig, axes = plt.subplots(ncols=n, nrows=n+1)
    
    fig.set_size_inches(30, 30)
    ax = axes.ravel()
    
    fig.suptitle(image_name,fontsize=40,weight='bold')
    
    if kind == 'histogram':
    
        j = 0
        for i in range(N):
            z = itemfreq(list[j])
            z = z[np.argsort(z[:,1])]
            ax[i].plot(z[:,1],'o')
            ax[i].set_xticks(z[:,1])
            #ax[i].plot(z[:,0],z[:,1],'o')
            ax[i].set_title(str(j),size='medium',weight='bold',color='steelblue',backgroundcolor=(1,  0.85490196,  0.7254902))
            j+=1
            
    elif kind == 'CDF':
        j = 0
        for i in range(N):
            ax[i].plot(list[j],'o')
            ax[i].set_title(str(j),size='medium',weight='bold',color='steelblue',backgroundcolor=(1,  0.85490196,  0.7254902))
            j+=1
        
    
    if isinstance(image_loc+image_name,str):
        fig.savefig(image_loc+image_name+'.png',dpi=fig.dpi)
    
