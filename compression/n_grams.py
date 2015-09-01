# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 07:28:51 2015

@author: aidanrocke

this function takes a posture_sequence and returns as output:
1) unique n_grams
2) the frequency of their occurrence
"""

import numpy as np

def n_grams(posture_seq, n):
# Input
#   posture_seq - a numpy array to be compressed
#   n       - the n in n-grams (also the number of columns in output nGrams)
#
# Output
#   nGrams  - a len(dataVec)-(n+1) by n array containing all the n-grams in dataVec   
#   occurrences - the number of times each unique nGram occurs 

    # check inputs
    if len(np.shape(posture_seq)) > 1:
        raise Exception('dataVec must be a row vector')
        
    posture_seq = posture_seq.split(' ')
    output = {}
    for i in range(len(posture_seq)-n+1):
      g = ' '.join(posture_seq[i:i+n])
      output.setdefault(g, 0)
      output[g] += 1
    return list(output.keys()), output.values()