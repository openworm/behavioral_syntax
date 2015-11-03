import numpy as np
from scipy import io

directory = '/Users/cyrilrocke/Documents/c_elegans/data/'

g = io.loadmat('/Users/macbook/Github/behavioral_syntax/data/'+'postures.mat')
postures = g.get('postures')

Angles = []
mean_angles = []
all_postures = []

def knnsearch(angles,postures):
    #fetch skeletons: 
    
    
    #initialize Vars and posture_sequence:
    C = len(angles)
    posture_sequence = np.zeros(C)
    distance_vector = np.zeros(C)
    
    for i in range(C):
        distances = [np.inf]*90
        for j in range(90):
            distances[j] = np.linalg.norm(angles[i]-postures[:,j])
        val = min(distances)
        distance_vector[i] = val
        posture_sequence[i] = distances.index(val)
    
    #collect features
    return posture_sequence, distance_vector
