#from the raw data(i.e. worm skeleton time series) I would like to obtain:
#1. normalized worm skeletons
#2. angle arrays
#2. mean angle arrays
#3. posture arrays
#4. variances array
#5. tangent_angle_distance

import numpy as np
import os
from scipy import io
import h5py

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

def get_features(files,directory,postures,start,finish):
    
    for i in range(start,finish):
        #fetch skeletons: 
        if files[i].endswith('.mat'):
            #get skeleton data:
            f = h5py.File(directory+'test1/20_videos/'+files[i])
            #getting the right cell array:
            for i in ['worm','posture','skeleton']:
                f = f.get(i)
                
            #getting the x and y coordinates:
            X = np.array(f.get('x'))
            Y = np.array(f.get('y'))
                
            indices = []
            for j in range(len(X)):
                if np.sum(np.isnan(X[j]))== 0:
                    indices.append(j)
                        
            X = X[indices] 
            Y = Y[indices]
        
            #get angles for the skeletons
            angles, m_a = angle(X,Y)
            X, Y = angle2skel(angles, m_a, 1)
            
            #initialize Vars and posture_sequence:
            Vars = np.zeros(len(X))
            posture_sequence = ''
            angle_err = np.zeros(len(X))
            
            for i in range(len(X)):
                distances = [np.inf]*90
                for j in range(90):
                    distances[j] = np.linalg.norm(angles[i]-postures[:,j])
                val = min(distances)
                angle_err[i] = val
                ind = distances.index(val)
                Vars[i] = np.corrcoef(angles[i],postures[:,ind])[0][1]**2
                posture_sequence = posture_sequence + ' ' + str(ind)
        
        #collect features
        variances.append(Vars)
        all_postures.append(posture_sequence)
        Angles.append(angles) 
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
