import numpy as np
import os
from scipy import io
import h5py

#directory = '/Users/cyrilrocke/Documents/c_elegans/data/'
#files = os.listdir(directory+'/test1/20_videos')

g = io.loadmat('/Users/cyrilrocke/Documents/c_elegans/data/postures')
postures = g.get('postures')

#pos_x = np.load(directory+'/test1/features/pos_x.npy')
#pos_y = np.load(directory+'/test1/features/pos_y.npy')

all_postures = []

def posture_seq(files,directory,postures,start,finish):
    
    i = start
    while i < finish :
        #fetch skeletons: 
        if files[i].endswith('.mat'):
            #get skeleton data:
            '''
            f = h5py.File(directory+files[i])
            #getting the right cell array:
            for i in ['worm','posture','skeleton']:
                f = f.get(i)'''
                
            data = io.loadmat(directory+files[i])
            X = data['worm']['posture'][0][0][0]['skeleton'][0][0][0][0]
            Y = data['worm']['posture'][0][0][0]['skeleton'][0][0][0][0]
            
            X = X.T
            Y = Y.T
            '''   
            #getting the x and y coordinates:
            X = np.array(f.get('x'))
            Y = np.array(f.get('y'))'''
                
            indices = []
            for j in range(len(X)):
                if np.sum(np.isnan(X[j]))== 0:
                    indices.append(j)
                        
            X = X[indices] 
            Y = Y[indices]
            
            if len(X) > 1000:
        
            #get angles for the skeletons
                angles, m_a = angle(X,Y)
                X, Y = MA2skel(angles, m_a, 1)
                
                #initialize Vars and posture_sequence:
                #Vars = np.zeros(len(X))
                posture_sequence = ''
                #angle_err = np.zeros(len(X))
                
                for i in range(len(X)):
                    distances = [np.inf]*90
                    for j in range(90):
                        distances[j] = np.linalg.norm(angles[i]-postures[:,j])
                    val = min(distances)
                    #angle_err[i] = val
                    ind = distances.index(val)
                    #Vars[i] = np.corrcoef(angles[i],postures[:,ind])[0][1]**2
                    posture_sequence = posture_sequence + ' ' + str(ind)
                all_postures.append(posture_sequence)
                
                i+=1
                
            else:
                i+=1
            
        return all_postures
