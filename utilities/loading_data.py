from behavioral_syntax.utilities.angle_and_skel import angle
import numpy as np
import scipy, h5py

#filepath = 'C:/Users/ltopuser/behavioral_syntax/utilities/data.mat'

def loading_data(filepath):
      
  flag = True;
  try:
    f = h5py.File(filepath)
  except:
    flag = False;

  try:
    if not flag:
        f = scipy.io.loadmat(filepath)
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
      
    
  angleArray, meanAngles = angle(X,Y)
  
  #save data
  scipy.io.savemat('angleArray.mat', dict(x=angleArray))
  scipy.io.savemat('meanAngles.mat', dict(y=meanAngles))
  
  return angleArray, meanAngles

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
