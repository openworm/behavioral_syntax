from scipy.stats import itemfreq
import math
import os
import numpy as np
import h5py

from matplotlib import pyplot as plt


directory = 'C:/Users/Dell/Documents/balazs_project/features/features/'

files = os.listdir(directory)


speed = []
velocity = []


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
    
    temp_skel_nans = []

    temp_angle_nans = []
    
    s_peed = []
    v_elocity = []
    
    #compute speed and velocity:
    j =0
    while j<C+1:
        if sum(np.isnan(X[j]))+sum(np.isnan(X[j+1]))== 0:
            norm = math.sqrt(np.linalg.norm(X[j+1][25]-X[j][25])**2+np.linalg.norm(Y[j+1][25]-Y[j][25])**2)
            s_peed.append(norm)
            v = np.array([X[j+1][25]-X[j][25],Y[j+1][25]-Y[j][25]])
            v_elocity.append(v)
        else:
            j+=1
            
    speed.append(s_peed)
    velocity.append(v_elocity)
    
s_peed = []
v_elocity = []

#compute speed and velocity:
j =0
while j<C+1:
    if sum(np.isnan(X[j]))+sum(np.isnan(X[j+1]))== 0:
        norm = math.sqrt(np.linalg.norm(X[j+1][25]-X[j][25])**2+np.linalg.norm(Y[j+1][25]-Y[j][25])**2)
        s_peed.append(norm)
        v = np.array([X[j+1][25]-X[j][25],Y[j+1][25]-Y[j][25]])
        v_elocity.append(v)
    else:
        j+=1
