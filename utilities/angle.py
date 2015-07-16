import numpy as np

def angle(x, y):

#given a series of x and y coordinates over time, calculates the angle
#between each vector making up the skeleton and the x-axis.  The mean angle
#is subtracted from each frame so that the average orientation is always
#the same in the output angleArray.




    [numFrames, lengthX] = np.shape(x)
    
    # initialize arrays
    angleArray = np.zeros([numFrames, lengthX-1])
    meanAngles = np.zeros([numFrames,1])
    
    return angleArray, meanAngles
