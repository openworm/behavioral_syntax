from behavioral_syntax.utilities.angle_and_skel import angle
import numpy as np
import scipy, h5py

#filepath = 'C:/Users/ltopuser/behavioral_syntax/utilities/data.mat'

def get_skeletons(file):
    """get sequence of skeletons from a particular file"""
    flag = True;
    try:
        f = h5py.File(file)
    except:
        flag = False;
    
    try:
        if not flag:
            f = scipy.io.loadmat(file)
    except:
        print('Error')
          
    if type(f) == h5py._hl.files.File:
        #getting the right cell array:
        for i in ['worm','posture','skeleton']:
            f = f.get(i)
  
    #getting the x and y coordinates:
        X = np.array(f.get('x'))
        Y = np.array(f.get('y'))
      
    else:
        X = f['worm']['posture'][0][0][0]['skeleton'][0][0][0][0].T
        Y = f['worm']['posture'][0][0][0]['skeleton'][0][0][0][0].T
        
    return X, Y

def loading_data(directory,sampling_fraction):
    """function that fetches postural data from a particular file
        directory: a folder where C. Elegans .mat files are found
        sampling_fraction: the ratio of sample size to population size
                            expressed as a float
        
        ex. if sampling_fraction == 1 then you want all the files in the 
            directory. """
    file_names = os.listdir(directory)
    files = [directory+file_names[i] for i in range(len(file_names)) if file_names[i].endswith('.mat')]
    
    if sampling_fraction != 1:
        #sample without replacement: 
        N = len(files)
        sample = np.random.choice(N, int(N*sampling_fraction),replace=False)
        files = [files[i] for i in sample]
        
    skeletons = [get_skeletons(files[i]) for i in range(len(files))]
    
    angle_data = [angle(x,y=skeletons[i]) for i in range(len(skeletons))]
    
    #angleArray, meanAngles = angle(X,Y)
  
  '''
  #save data
  scipy.io.savemat('angleArray.mat', dict(x=angleArray))
  scipy.io.savemat('meanAngles.mat', dict(y=meanAngles))'''
  
  #return angleArray, meanAngles
  
  return angle_data

''''
def dict_generator(filepath, pre=None):
    pre = pre[:] if pre else []
    if isinstance(indict, dict):
        for key, value in indict.items():
            if isinstance(value, dict):
                for d in dict_generator(value, [key] + pre):
                    yield d
            elif isinstance(value, list) or isinstance(value, tuple):
                for v in value:
                    for d in dict_generator(v, [key] + pre):
                        yield d
            else:
                yield pre + [key, value]
    else:
        yield indict
        
z = sum([i for i in dict_generator(filepath)],[])

i = 0
if np.shape(z[i])==():
    i+=1
    
elif len(np.shape(z[i]))==2 and max(np.shape(z[i]))> 1000 and min(np.shape(z[i])) == 48:
    postures = z[i]
    
else:
    i+=1'''
