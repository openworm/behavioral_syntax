from behavioral_syntax.utilities.angle_and_skel import MA2skel
from behavioral_syntax.utilities.numericalc import largest_factors
import numpy as np

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

plt.style.use('ggplot')

#postures_file = '/Users/cyrilrocke/behavioral_syntax/data/postures'

def view_postures(order,image_loc,image_name,postures,annotation):
    """this function outputs a grid of postures with some annotation as
        desired.
        
        Inputs:
            order: the order in which you want the images
            image_loc: the directory where you want to save the image
            postures: the 1-d angle array of N template postures
            annotation: additional annotation that you would like on the image
            image_name: desired name for the image
        
        Output:
            the image will be saved as desired
    """
    
    N = max(np.shape(postures))
    k = min(np.shape(postures))
    
    if order == 0:
        order = list(range(N))
    
    mean_angles = np.zeros(N)
    
    for i in range(N):
        mean_angles[i] = np.mean(postures[:,i])
        
    X,Y = MA2skel(postures.T,mean_angles,1)
    
    #define the dimensions of the plot
    m, n = largest_factors(N)
    
    fig, axes = plt.subplots(ncols=m, nrows=n)
    fig.set_size_inches(m, n)
    
    fig.suptitle(image_name, fontsize=16)
    
    #head and tail so they can be colored separately
    tail = int(0.9*k)
    head = tail-1
    
    #worm head is colored green:
    j = 0
    for ax in axes.ravel():
        ax.plot(X[order[j]][0:tail],Y[order[j]][0:tail],lw=3)
        ax.plot(X[order[j]][head:k],Y[order[j]][head:k],lw=3,color='green')
        #place a text box in upper left in axes coords:
        ax.set_title(str(order[j])+'/'+"{0:.0f}%".format(annotation[j]*100),size='medium',weight='bold',color='steelblue',backgroundcolor=(1,  0.85490196,  0.7254902))
        ax.axis('off')
        j+=1
        
        
    if isinstance(image_loc+image_name,str):
            fig.savefig(image_loc+image_name+'.png',dpi=fig.dpi)