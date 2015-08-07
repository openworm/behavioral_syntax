import scipy

from scipy.stats import itemfreq

from angle import angle

import os

from scipy import interpolate
from pandas import Series
import numpy as np
import h5py

from matplotlib import pyplot as plt

#from matplotlib import pyplot as plt

#from simple_compression import simple_compression
#from angle import angle

directory = '/Users/macbook/Documents/c_elegans/features/'

files = os.listdir('/Users/macbook/Documents/c_elegans/features/')

g = scipy.io.loadmat('/Users/macbook/Documents/c_elegans/postures')

postures = g.get('postures')

all_postures = []

NaNs = []



for i in range(len(files)):
    if files[i].endswith('.mat'):
        #get skeleton data:
        f = h5py.File(directory+files[i])
        #getting the right cell array:
        l1 = f.get('worm')
        l2 = l1.get('posture')
        l3 = l2.get('skeleton')
        
        #getting the x and y coordinates:
        X = np.array(l3.get('x'))
        Y = np.array(l3.get('y'))
        
        indices = []
        for j in range(len(X)):
            if sum(np.isnan(X[j]))== 0:
                indices.append(j)
                
        X = X[indices] 
        Y = Y[indices]
        
        angles, mean = angle(X,Y)
        C,c = np.shape(X)
        
        
        j = 0
        #count the number of nan arrays:
        for i in range(C):
            if sum(np.isnan(X[i])) > 0:
                j+=1
            
        NaNs.append(round(j/C,3))
        
        posture_sequence = ''
        
        for i in range(C):
            distances = [np.inf]*90
            for j in range(90):
                distances[j] = np.linalg.norm(angles[i]-postures[:,j])
            val = min(distances)
            posture_sequence = posture_sequence + ' ' + str(distances.index(val))
            
        all_postures.append(posture_sequence)
    
    #indices = list(range(C))
    #get difference:
    #nonan_indices = list(set(indices)-set(nans))
    
'''posture_distribution = []
#correct for segmentation faults:
for i in range(16):
    z = itemfreq(all_postures[i])
    z[0][1] = z[0][1]-NaNs[i]
    posture_distribution.append(z)
    
directory = '/Users/macbook/Documents/c_elegans/posture_analysis/'
for i in range(16):
    fig, ax = plt.subplot(nrows=1,ncols=1)
    ax.bar(posture_distribution[i][:,0],posture_distribution[i][:,1])
    fig.savefig()'''
