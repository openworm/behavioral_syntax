from scipy import io
from angle2skel2 import angle2skel
import numpy as np
from matplotlib import pyplot as plt

g = io.loadmat('/Users/cyrilrocke/Documents/c_elegans/postures')

postures = g.get('postures')

mean_angles = np.zeros(90)

for i in range(90):
    mean_angles[i] = np.mean(postures[:,i])
    
X,Y = angle2skel(postures.T,mean_angles,1)

plt.style.use('ggplot')

fig, axes = plt.subplots(ncols=10, nrows=9)
fig.set_size_inches(10, 9)

j = 0
for ax in axes.ravel():
    ax.plot(X[j],Y[j],lw=3)
    ax.set_title(str(j),size='medium',weight='bold',color='steelblue',backgroundcolor=(1,  0.85490196,  0.7254902))
    ax.axis('off')
    j+=1
