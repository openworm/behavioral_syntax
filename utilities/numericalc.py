"""
Created on Wed Sep 23 08:38:56 2015

@author: aidanrocke
"""

#taken from here: http://rosettacode.org/wiki/Miller-Rabin_primality_test#Python

import numpy as np

def sequence_filter(skeleton, angle_indices):
    """this function checks whether a sequence of frames that is being loaded
        using loading_data is sufficiently dense and means other important 
        criteria before being used for analysis. 
        
        input: sequence of type list
        output: """
        
    if max(angle_indices)/len(skeleton) > 0.6:
        return angle_indices
    else:
        return 0

#get greatest common factors:
def largest_factors(n):  
    L = [(x, n/x) for x in range(1, int(np.sqrt(n))+1) if n % x == 0]
    difference = [abs(np.diff(i))[0] for i in L]
    smallest_diff = min([abs(np.diff(i))[0] for i in L])
    index = difference.index(smallest_diff)
    return round(max(L[index])),round(min(L[index]))
