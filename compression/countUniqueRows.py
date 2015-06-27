

# COUNTUNIQUEROWS counts the number of occurances of each of the unique
# rows found in dataMat.
# 
# Input
#   data       - A matrix of row vectors whose unique rows will be counted
# 
# Output
#   uniqueRows - A matrix containing only the unique rows of dataMat
#   counts     - A vector of counts.  The first element of counts gives the
#                number of occurances in dataMat of the corresponding row
#                in uniqueRows

#other ideas from here http://stackoverflow.com/questions/16970982/find-unique-rows-in-numpy-array:
#b = np.ascontiguousarray(data).view(np.dtype((np.void, data.dtype.itemsize * data.shape[1])))
#_, idx = np.unique(b, return_index=True)
#unique_rows = data[idx]
 
#assuming the data is in matrix format:

from np import unique, array, all

def countUniqueRows(input):
  unique_rows = array([array(x) for x in set(tuple(x) for x in input)])
  counts = array([len(input[all(input==x, axis=1)]) for x in unique_rows],dtype=int)
  return unique_rows, counts
    


    

