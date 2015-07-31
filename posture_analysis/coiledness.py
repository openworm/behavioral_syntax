from scipy.stats import itemfreq

import math

#from angle import angle

import os

import numpy as np
import h5py

from matplotlib import pyplot as plt

#from matplotlib import pyplot as plt

#from simple_compression import simple_compression
#from angle import angle

directory = 'C:/Users/Dell/Documents/balazs_project/features/features/'

files = os.listdir(directory)


coiledness = []


for i in range(len(files)):
    #get skeleton data:
    f = h5py.File(directory+files[i])
    #getting the right cell array:
    l1 = f.get('worm')
    l2 = l1.get('posture')
    l3 = l2.get('skeleton')
    
    #getting the x and y coordinates:
    X = np.array(l3.get('x'))
    Y = np.array(l3.get('y'))

    C,c = np.shape(X)
    
    distance = []
    
    j = 0
    #compute the 'coiledness':
    while j<C+1:
        if sum(np.isnan(X[j])):
            norm = math.sqrt(np.linalg.norm(X[j][49]-X[j][0])**2+np.linalg.norm(Y[j][49]-Y[j][0])**2)
            distance.append(norm)
        else:
            j+=1
            
    coiledness.append(distance)
