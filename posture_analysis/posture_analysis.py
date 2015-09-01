

from scipy.stats import itemfreq
from scipy import io 
import os
import numpy as np
import h5py

from matplotlib import pyplot as plt

directory = '/Users/macbook/Documents/c_elegans/features/'

files = os.listdir('/Users/macbook/Documents/c_elegans/features/')

g = io.loadmat('/Users/macbook/Documents/c_elegans/postures')

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
