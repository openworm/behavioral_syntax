# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 12:41:16 2015

@author: macbook
"""
from behavioral_syntax.utilities.angle_and_skel import MA2skel

import matplotlib.pyplot as plt
from behavioral_syntax.utilities.numbericalc import largest_factors
from scipy.stats import itemfreq
import numpy as np
from scipy import io
#for bokeh charts:
"""
from bokeh.plotting import show, output_file
from bokeh.charts import Bar
"""
#visualizing postures is probably one of the most important tasks:
postures = '/Users/cyrilrocke/Documents/c_elegans/data/postures'
g = io.loadmat(postures)
postures = g.get('postures')

plt.style.use('ggplot')


"""
def bokeh_bars(liszt,name):

    z = itemfreq(liszt)
    z = z[np.argsort(z[:,1])]
    data = {"y": list(z[:,1])}
    
    #it would be great if there was a way to automatically fit the bokeh plot to the screen: 
    bar = Bar(data, list(map(str,z[:,0])), title="bars",width=1000,height=500)
    
    output_file(name+".html", title=name)
    
    show(bar)

plt.style.use('ggplot')"""

def grid_plot(list,kind,image_loc,image_name):
    N = len(list)
    
    #we select an n*n subset of the multi_array of length N which for n>=16
    #is always greater than 99% of the members of the multi_array. 
    n = round(np.sqrt(N))
    

    fig, axes = plt.subplots(ncols=n, nrows=n+1)
    
    fig.set_size_inches(30, 30)
    ax = axes.ravel()
    
    fig.suptitle(image_name,fontsize=40,weight='bold')
    
    if kind == 'histogram':
    
        j = 0
        for i in range(N):
            if type(list[j]) == str:
                list[j] = list[j].split(' ')
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
    
