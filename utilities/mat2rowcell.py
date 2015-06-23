import scipy.io as sio

'using the idea described here: http://www.codedisqus.com/0NzVejPWWq/creating-matlab-cell-arrays-in-python.html'

#matrix is assumed to be a multi-dimensional matlab array
#example input: matrix = sio.loadmat('matrix.mat')

#instead of converting to a Matlab cell array I have decided to convert to a Python list
#as Python lists can hold any object.

def mat2rowcell(matrix):
  matrix = np.array(matrix)
  N = length(matrix)
  list = matrix.tolist()
  return list
