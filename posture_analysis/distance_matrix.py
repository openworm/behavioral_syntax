import math
import numpy as np
import scipy
import matplotlib.pyplot as plt
import pylab as pl

g = scipy.io.loadmat('C:/Users/Dell/Documents/brown_data/90_postures.mat')

postures = g.get('postures')
skelX = np.array([[np.NaN]*49 for i in range(90)])
skelY = np.array([[np.NaN]*49 for i in range(90)])

for i in range(90):
    angle = (postures[:,i] + np.mean(postures[:,i]))*1/(49)
    cos = np.array([math.cos(i) for i in angle])
    sin = np.array([math.sin(i) for i in angle])
    
    skelX[i] = np.hstack((np.array(0),np.cumsum(cos)))
    # add up y-contributions of angleArray, rotated by meanAngle
    skelY[i] = np.hstack((np.array(0),np.cumsum(sin)))
    
cost_matrix = np.array([[np.NaN]*90 for i in range(90)])
for i in range(90):
    for j in range(90):
        cost = math.sqrt((np.linalg.norm(skelX[i]-skelX[j]))**2 + np.linalg.norm((skelY[i]-skelY[j]))**2)
        cost_matrix[i][j] = cost
        
        
#plotting the cost matrix:
H = cost_matrix
pl.pcolor(H)
pl.colorbar()
pl.figure(figsize=(100, 100), dpi=100)
pl.show()
