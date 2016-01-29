#from the raw data(i.e. worm skeleton time series) I would like to obtain:
#1. normalized worm skeletons
#2. angle arrays
#2. mean angle arrays
#3. posture arrays
#4. variances array
#5. tangent_angle_distance

import numpy as np
import os

from behavioral_syntax.utilities.loading_data import loading_data

directory = '/Users/cyrilrocke/Documents/c_elegans/data/'
files = os.listdir(directory+'/test1/20_videos')

g = io.loadmat(directory+'postures')
postures = g.get('postures')

pos_x = np.load(directory+'/test1/features/pos_x.npy')
pos_y = np.load(directory+'/test1/features/pos_y.npy')

Angles = []
mean_angles = []
all_postures = []
variances = []
errors = []
skeletons = []

def get_features(directory,sampling_fraction):
    
     angles = loading_data(directory, sampling_fraction)
     
     for i in range(len(angles)):
         Angles = angles[i][0]

       
         #initialize Vars and posture_sequence:
         Vars = np.zeros(Angles)
         posture_sequence = ''
         angle_err = np.zeros(len(Angles))
            
         for j in range(len(Angles)):
             distances = [np.inf]*90
             for k in range(90):
                 distances[j] = np.linalg.norm(Angles[j][0]-postures[:,k])
             val = min(distances)
             angle_err[j] = val
             ind = distances.index(val)
             Vars[j] = np.corrcoef(Angles[j],postures[:,ind])[0][1]**2
             posture_sequence = posture_sequence + ' ' + str(ind)
            
         #collect features
         variances.append(Vars)
         all_postures.append(posture_sequence)
         mean_angles.append(m_a)
         skeletons.append(np.vstack((X,Y)))
         errors.append(angle_err)
        
        #save everything to the specified file path:
        np.save(directory+'/test1/features/skeletons'+str(finish),skeletons)
        np.save(directory+'/test1/features/all_postures'+str(finish),all_postures)
        np.save(directory+'/test1/features/angles'+str(finish),Angles)
        np.save(directory+'/test1/features/mean_angles'+str(finish),mean_angles)
        np.save(directory+'/test1/features/errors'+str(finish),errors)
        np.save(directory+'/test1/features/variances'+str(finish),variances)
