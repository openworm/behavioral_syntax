#import scipy.io as sio
#import numpy as np

#I assume that I will get a numpy array rather than a matlab matrix
#as Python lists can hold any object, just like cell arrays

def mat2rowcell(matrix):
  list = matrix.tolist()
  return list
