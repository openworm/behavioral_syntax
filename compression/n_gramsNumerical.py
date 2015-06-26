import numpy as np

class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: 
            self.fall = True
            return True
        else:
            return False

def n_gramsNumerical(dataVec, n):
# Input
#   dataVec - a numpy array to be compressed
#   n       - the n in n-grams (also the number of columns in output
#             nGrams)
#
# Output
#   nGrams  - a len(dataVec)-(n+1) by n array containing all the
#             n-grams in dataVec    

    # check inputs
    if len(np.shape(dataVec)) > 1:
        print('dataVec must be a row vector')
        
    else:
        for case in switch(n):
            if case(1):
                nGrams = dataVec[np.newaxis].T

                break
            
        elif (n != 1) and (n <= 10):
            nGrams = dataVec
            for i in range(n):
                row = np.concatenate([dataVec[i+1:],np.array([np.NaN]*(i+1))])
                nGrams = np.concatenate([[nGrams],[row]])
                
                break
            if case(6):
                print(10)
                break
            if case(7):
                print(11)
            if case(8): # default, could also just omit condition or 'if True'
                print("something else!")
