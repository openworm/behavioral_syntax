import scipy

from scipy.stats import itemfreq
import os

from scipy import io
from pandas import Series
import numpy as np
import h5py

from matplotlib import pyplot as plt

directory = '/Users/macbook/Documents/c_elegans/raw_data/on-food-1/'

files = os.listdir(directory)[1:16]

g = io.loadmat('/Users/macbook/Github/behavioral_syntax/data/'+'postures.mat')
postures = g.get('postures')

all_postures = []


skel_nans = []

angle_nans = []

NaNs = []

for i in range(len(files)):
    #get skeleton data:
    f = io.loadmat(directory+files[i])
    #getting the right cell array:
    X = f['worm']['posture'][0][0][0]['skeleton'][0][0][0][0]
    Y = f['worm']['posture'][0][0][0]['skeleton'][0][0][0][0]
    
    angles, mean = angle(X.T,Y.T)
    C,c = np.shape(X)
    
    j = 0
    #count the number of nan arrays:
    for i in range(C):
        if sum(np.isnan(X[i])) > 0:
            j+=1
        
    NaNs.append(j)
    
    posture_sequence = list(np.zeros(C))
    
    for i in range(C):
        distances = [np.inf]*90
        for j in range(90):
            distances[j] = np.linalg.norm(angles[i]-postures[:,j])
        val = min(distances)
        posture_sequence[i] = distances.index(val)
        
    all_postures.append(posture_sequence)

    nans = []
    
    for j in range(C):
        if sum(np.isnan(X[j])) > 0:
            nans.append(j)
            
    angle_nans.append(nans)
    
    #indices = list(range(C))
    #get difference:
    #nonan_indices = list(set(indices)-set(nans))
    
posture_distribution = []
#correct for segmentation faults:
for i in range(15):
    z = itemfreq(all_postures[i])
    rows, cols = np.shape(z)
    q = np.zeros((rows,cols))
    z[0][1] = z[0][1]-NaNs[i]
    q[:,1] = z[:,1]/sum(z[:,1])
    q[:,0] = z[:,0]
    posture_distribution.append(q)
    

for i in range(15):
    fig = plt.figure()
    plt.bar(posture_distribution[i][:,0],posture_distribution[i][:,1])
    fig.savefig('C:/Users/Dell/Documents/behavioral_syntax//plots/'+str(i)+'.png',dpi=fig.dpi)
