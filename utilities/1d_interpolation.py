from scipy import interpolate
from pandas import Series
import numpy as np
import h5py

from matplotlib import pyplot as plt

#from matplotlib import pyplot as plt

#from simple_compression import simple_compression
#from angle import angle

#get angle data:
f = h5py.File('C:/Users/Dell/Documents/brown_data/feature_files/wormdata.mat')
  
#getting the right cell array:
l1 = f.get('worm')
l2 = l1.get('posture')
l3 = l2.get('skeleton')

#getting the x and y coordinates:
X = np.array(l3.get('x'))
  
Y = np.array(l3.get('y'))

def fill_nan(A):
    '''
    interpolate to fill nan values
    '''
    inds = np.arange(A.shape[0])
    good = np.where(np.isfinite(A))
    f = interpolate.interp1d(inds[good], A[good],bounds_error=False)
    B = np.where(np.isfinite(A),A,f(inds))
    return B
    
def interpol(A):
    return Series(A).interpolate().values
    
#let's start the music:
x_nans = []
y_nans = []
    
for i in range(26994):
    if sum(np.isnan(X[i])) > 0:
        x_nans.append(i)
       
for i in range(len(x_nans)):
    X[x_nans[i]] = interpol(X[x_nans[i]])
    Y[x_nans[i]] = interpol(Y[x_nans[i]])


maximum = 0
count = []
maxi = []
for i in range(len(x_nans)-1):
    if x_nans[i+1]-x_nans[i] == 1:
        maximum+=1
        if maximum > 5:
            maxi.append(x_nans[i])
    else:
        count.append(maximum)
        maximum = 0
        
plt.hist(count, bins=max(count))
        
