from scipy import io
from behavioral_syntax.utilities.angle_and_skel import MA2skel
import numpy as np
from matplotlib import pyplot as plt

plt.style.use('ggplot')

#g = io.loadmat('/Users/cyrilrocke/Documents/c_elegans/data/postures')

G = io.loadmat('/Users/cyrilrocke/behavioral_syntax/data/postures')

postures = G.get('postures')

mean_angles = np.zeros(90)

for i in range(90):
    mean_angles[i] = np.mean(postures[:,i])
    
X,Y = MA2skel(postures.T,mean_angles,1)

fig, axes = plt.subplots(ncols=10, nrows=9)
fig.set_size_inches(10, 9)

#worm head is colored green:
j = 0
for ax in axes.ravel():
    ax.plot(X[j][0:45],Y[j][0:45],lw=3)
    ax.plot(X[j][44:48],Y[j][44:48],lw=3,color='green')
    ax.set_title(str(j),size='medium',weight='bold',color='steelblue',backgroundcolor=(1,  0.85490196,  0.7254902))
    ax.axis('off')
    j+=1
