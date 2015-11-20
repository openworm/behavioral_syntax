from scipy import io
from behavioral_syntax.utilities.angle_and_skel import MA2skel
from behavioral_syntax.utilities.number_theory import largest_factors
import numpy as np
from matplotlib import pyplot as plt

plt.style.use('ggplot')

#postures_file = '/Users/cyrilrocke/behavioral_syntax/data/postures'

def view_postures(postures_file):
    """its assumed that the skeletons are 2-dimensional"""

    postures_mat = io.loadmat(postures_file)
    postures = postures_mat.get('postures')
    
    N = max(np.shape(postures))
    k = min(np.shape(postures))
    
    mean_angles = np.zeros(N)
    
    for i in range(N):
        mean_angles[i] = np.mean(postures[:,i])
        
    X,Y = MA2skel(postures.T,mean_angles,1)
    
    #define the dimensions of the plot
    m, n = largest_factors(N)
    
    fig, axes = plt.subplots(ncols=m, nrows=n)
    fig.set_size_inches(m, n)
    
    #head and tail so they can be colored separately
    tail = int(0.9*k)
    head = tail-1
    
    #worm head is colored green:
    j = 0
    for ax in axes.ravel():
        ax.plot(X[j][0:tail],Y[j][0:tail],lw=3)
        ax.plot(X[j][head:k],Y[j][head:k],lw=3,color='green')
        ax.set_title(str(j),size='medium',weight='bold',color='steelblue',backgroundcolor=(1,  0.85490196,  0.7254902))
        ax.axis('off')
        j+=1
