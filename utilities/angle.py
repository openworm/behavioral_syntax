import numpy as np
import math

def angle(x, y):

#given a series of x and y coordinates over time, calculates the angle
#between each vector making up the skeleton and the x-axis.  The mean angle
#is subtracted from each frame so that the average orientation is always
#the same in the output angleArray.




    [numFrames, lengthX] = np.shape(x)
    
    # initialize arrays
    angleArray = np.zeros([numFrames, lengthX-1])
    meanAngles = np.zeros([numFrames,1])
    
    
    for i in range(numFrames):
        
        # calculate the x and y differences
        dX = np.diff(x[i], n=1, axis=0)
        dY = np.diff(y[i], n=1, axis=0)
        
        # calculate tangent angles.  atan2 uses angles from -pi to pi instead...
        # of atan which uses the range -pi/2 to pi/2.
        angles = np.arctan2(dY, dX)
        
        # need to deal with cases where angle changes discontinuously from -pi
        # to pi and pi to -pi.  In these cases, subtract 2pi and add 2pi
        # respectively to all remaining points.  This effectively extends the
        # range outside the -pi to pi range.  Everything is re-centred later
        # when we subtract off the mean.
        
        # find discontinuities
        positiveJumps = np.array((np.diff(angles, n=1, axis=0) > 5)) + 1
        negativeJumps = np.array((np.diff(angles, n=1, axis=0) < -5)) + 1
        
        # subtract 2pi from remainging data after positive jumps
        for j in range(len(positiveJumps)):
            angles[positiveJumps[j]:] = angles[positiveJumps[j]:] - 2*math.pi
        
        # add 2pi to remaining data after negative jumps
        for j in range(len(negativeJumps)):
            angles[negativeJumps[j]:] = angles[negativeJumps[j]:] + 2*math.pi
        
        # rotate skeleton angles so that mean orientation is zero
        meanAngle = np.mean(angles)
        meanAngles[i] = meanAngle
        angles -= meanAngle
        
        # append to angle array
        angleArray[i] = angles
        
    return angleArray, meanAngles
