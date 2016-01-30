#from the raw data(i.e. worm skeleton time series) I would like to obtain:
#1. normalized worm skeletons
#2. angle arrays
#2. mean angle arrays
#3. posture arrays
#4. variances array
#5. tangent_angle_distance

import numpy as np
from scipy import io

from behavioral_syntax.utilities.loading_data import loading_data

postures = '/Users/cyrilrocke/Documents/c_elegans/data/postures'
g = io.loadmat(postures)
postures = g.get('postures')

Angles = []
mean_angles = []
all_postures = []
variances = []
errors = []
skeletons = []

def get_features(directory,postures,sampling_fraction,output):
    """
        inputs: 
            directory = where your files are stored
            
            postures = the numpy file of template postures
            
            sampling_fraction = the fraction of the files in the directory that
                                you want to sample, sampled without replacement.
                                
            output = the actual output you want. 1 if you want all outputs.
                    2 if you want just the postures
    """
    angles = loading_data(directory, sampling_fraction)
    
    for i in range(len(angles)):
         Angles = angles[i][0]

       
         #initialize Vars and posture_sequence:
         Vars = np.zeros(len(Angles))
         posture_sequence = ''
         angle_err = np.zeros(len(Angles))
         m_a = np.zeros(len(Angles))
            
         for j in range(len(Angles)):
             distances = [np.inf]*90
             for k in range(90):
                 distances[k] = np.linalg.norm(Angles[j]-postures[:,k])
             m_a = np.mean(Angles[j][0])
             val = min(distances)
             angle_err[j] = val
             ind = distances.index(val)
             Vars[j] = np.corrcoef(Angles[j],postures[:,ind])[0][1]**2
             posture_sequence = posture_sequence + ' ' + str(ind)
             
    
            
         #collect features
         variances.append(Vars)
         all_postures.append(posture_sequence)
         mean_angles.append(m_a)
         errors.append(angle_err)
         
    if output == 1:
        return variances,all_postures,mean_angles,errors
    else:
        return all_postures
        
        """
        #save everything to the specified file path:
        np.save(directory+'/test1/features/skeletons'+str(finish),skeletons)
        np.save(directory+'/test1/features/all_postures'+str(finish),all_postures)
        np.save(directory+'/test1/features/angles'+str(finish),Angles)
        np.save(directory+'/test1/features/mean_angles'+str(finish),mean_angles)
        np.save(directory+'/test1/features/errors'+str(finish),errors)
        np.save(directory+'/test1/features/variances'+str(finish),variances)"""
