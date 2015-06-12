import scipy.io as sio

'using the idea described here: http://www.codedisqus.com/0NzVejPWWq/creating-matlab-cell-arrays-in-python.html'

def mat2rowcell(matrix):
  N = length(matrix)
  matrix = np.array(matrix)
  cell = np.empty(matrix.shape, dtype=object)
  for i in range(N):
    cell[0,i,0] = np.array([matrix(i)])
