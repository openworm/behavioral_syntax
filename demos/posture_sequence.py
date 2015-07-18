import numpy as np

import scipy, h5py

from angle import angle

#get angle data:
f = h5py.File('C:/Users/Dell/Documents/brown_data/feature_files/worm_data.mat')
  
#getting the right cell array:
l1 = f.get('worm')
l2 = l1.get('posture')
l3 = l2.get('skeleton')
  
#getting the x and y coordinates:
X = l3.get('x')
  
Y = l3.get('y')
  
angles, meanAngles = angle(X,Y)

#get posture data:
g = scipy.io.loadmat('C:/Users/Dell/Documents/brown_data/90_postures.mat')

postures = g.get('postures')

N, M = np.shape(angles)

neighbors = list(np.zeros(N))
    
for i in range(N):
    distances = [np.inf]*90
    for j in range(90):
        distances[j] = np.linalg.norm(angles[i]-postures[:,j])
    val = min(distances)
    neighbors[i] = distances.index(val)
