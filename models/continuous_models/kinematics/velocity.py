from behavioral_syntax.utilities.loading_data import get_skeletons
from scipy.stats import itemfreq
import os
import numpy as np
import h5py

from matplotlib import pyplot as plt


#dir = 'C:/Users/Dell/Documents/balazs_project/features/features/'

def velocity(directory):
    files = os.listdir(directory)
    
    speed = []
    velocity = []
    
    
    for i in range(len(files)):
        #get skeleton data:
        X,Y = get_skeletons(directory+files[i])
    
        C,c = np.shape(X)
        
        temp_skel_nans = []
    
        temp_angle_nans = []
        
        s_peed = []
        v_elocity = []
        
        #compute speed and velocity:
        j =0
        while j<C+1:
            if sum(np.isnan(X[j]))+sum(np.isnan(X[j+1]))== 0:
                norm = np.sqrt(np.linalg.norm(X[j+1][25]-X[j][25])**2+np.linalg.norm(Y[j+1][25]-Y[j][25])**2)
                s_peed.append(norm)
                v = np.array([X[j+1][25]-X[j][25],Y[j+1][25]-Y[j][25]])
                v_elocity.append(v)
            else:
                j+=1
                
        speed.append(s_peed)
        velocity.append(v_elocity)
