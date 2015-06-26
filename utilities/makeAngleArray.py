import numpy as np
import math

def makeAngleArray(x, y):

    #MAKEANGLEARRAY Get tangent angles for each frame of normBlocks and rotate
    #               to have zero mean angle
    #
    #   [ANGLEARRAY, MEANANGLES] = MAKEANGLEARRAY(X, Y)
    #
    #   Input:
    #       x - the x coordinates of the worm skeleton (equivalent to 
    #           dataBlock{4}(:,1,:)
    #       y - the y coordinates of the worm skeleton (equivalent to 
    #           dataBlock{4}(:,2,:)
    #
    #   Output:
    #       angleArray - a numFrames by numSkelPoints - 1 array of tangent
    #                    angles rotated to have mean angle of zero.
    #       meanAngles - the average angle that was subtracted for each frame
    #                    of the video.
    
    
    
    
    [numFrames, lengthX] = np.shape(x);
    
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
        
        # find discontinuities larger than pi (skeleton cannot change direction
        # more than pi from one segment to the next)
        #1 to cancel diff
        positiveJumps = np.array((np.diff(angles, n=1, axis=0) > math.pi)) + 1
        negativeJumps = np.array((np.diff(angles, n=1, axis=0) < -math.pi)) + 1
        
        # subtract 2pi from remainging data after positive jumps
        for j in range(positiveJumps):
            angles[positiveJumps[j]:] = angles[positiveJumps[j]:] - 2*math.pi
        
        # add 2pi to remaining data after negative jumps
        for j in range(negativeJumps):
            angles[negativeJumps[j]:] = angles[negativeJumps[j]:] + 2*math.pi
        
        # rotate skeleton angles so that mean orientation is zero
        meanAngle = np.mean(angles)
        meanAngles[i] = meanAngle
        angles -= meanAngle
        
        # append to angle array
        angleArray[i] = angles
        
    return angleArray, meanAngles
