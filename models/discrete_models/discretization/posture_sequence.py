import numpy as np
from scipy import io

from behavioral_syntax.utilities.loading_data import loading_data

#directory = '/Users/cyrilrocke/Documents/c_elegans/data/raw_data/'
#files = os.listdir(directory+'/test1/20_videos')

g = io.loadmat('/Users/cyrilrocke/Documents/c_elegans/data/postures')
postures = g.get('postures')

#pos_x = np.load(directory+'/test1/features/pos_x.npy')
#pos_y = np.load(directory+'/test1/features/pos_y.npy')

all_postures = []


def posture_seq(directory,postures,sampling_fraction):
    #I may not always want to be limited to 90 postures. 
    num_postures = len(postures)
    
    angle_data = loading_data(directory,sampling_fraction)
    
    i = 0
    while i < len(angle_data):
        
            
        #I should probably add a test for frame sparsity as well. At present I'm 
        #assuming that frame sparsity isn't an issue. 
        if len(angle_data[i][1]) > 1000:
            
            #get angles for the skeletons
            angles, m_a = angle_data[i]
            #X, Y = MA2skel(angles, m_a, 1)
                
            #initialize Vars and posture_sequence:
            #Vars = np.zeros(len(X))
            posture_sequence = ''
                
            for i in range(len(angles)):
                distances = [np.inf]*num_postures
                for j in range(num_postures):
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
