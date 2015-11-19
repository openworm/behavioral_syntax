import numpy as np

import scipy, h5py

from scipy.stats import itemfreq

#from matplotlib import pyplot as plt

#from simple_compression import simple_compression
from shutil import copy

#get angle data:
file_1 = 'C:/Users/Dell/Documents/behavioral_syntax/data/N2 on food R_2011_03_29__12_13_57___2___5_features.mat'
file_2 = 'C:/Users/Dell/Documents/behavioral_syntax/data/N2 on food R_2010_08_20__10_17_31___7___1_features.mat'

f = h5py.File(file_1)

#getting the right cell array:
l1 = f.get('worm')
l2 = l1.get('posture')
l3 = l2.get('skeleton')
  
#getting the x and y coordinates:
X = np.array(l3.get('x'))
  
Y = np.array(l3.get('y'))
  
angles, meanAngles = angle(X,Y)

#get posture data:
g = scipy.io.loadmat('C:/Users/Dell/Documents/brown_data/90_postures.mat')

postures = g.get('postures')

N, M = np.shape(angles)

posture_sequence = list(np.zeros(N))
    
for i in range(N):
    distances = [np.inf]*90
    for j in range(90):
        distances[j] = np.linalg.norm(angles[i]-postures[:,j])
    val = min(distances)
    posture_sequence[i] = distances.index(val)
    
posture_sequence = np.array(posture_sequence)
    
posture_images_dir = 'C:/Users/Dell/Documents/behavioral_syntax/posture_images/'

movie_dir = 'C:/Users/Dell/Documents/behavioral_syntax/movie3/'

j = 1
for i in posture_sequence:
    if i > -1:
        copy(posture_images_dir+'image'+str(i)+'.png',movie_dir+str(j)+'.png')
        j+=1
        
#Now, we're interested in frequencies:
item_freq = itemfreq(posture_sequence)
    
#plt.hist(posture_sequence,bins=list(range(90)))

#result = simple_compression(posture_sequence)
