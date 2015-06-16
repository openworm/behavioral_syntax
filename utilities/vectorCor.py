# Input
#   mat1,2 - Two matrices with the same number of columns.
# 
# Output
#   Rmat   - A matrix of correlation coefficients.  Rmat(i, j) is the
#            correlation coefficient between the ith row of mat1 and the
#            jth row of mat2.  Rmat has dimensions size(mat1, 1) by
#            size(mat2, 1).

import numpy as np

def vectorCor(mat1,mat2):
    N = np.shape(mat1)[0]
    M = np.shape(mat2)[0]
    Rmat = [[0 for i in range(N)] for j in range(M)]
    for i in range(N):
        for j in range(N):
            Rmat[i][j] = np.corrcoef(mat1[i],mat2[j])
    
    return Rmat
