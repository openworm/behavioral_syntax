import numpy as np
import math

def find_subsequence(seq, subseq):
    target = np.dot(subseq, subseq)
    candidates = np.where(np.correlate(seq, subseq, mode='valid') == target)[0]
    # some of the candidates entries may be false positives, double check
    check = candidates[:, np.newaxis] + np.arange(len(subseq))
    mask = np.all((np.take(seq, check) == subseq), axis=-1)
    return candidates[mask]


def quantizeTS(timeSeries, centers, warpNum, flickThresh):

# QUANTIZETS Reduce a multidimensional time series to a quantized
# representation using a set of representative posture centers.  Each time
# point in the time series is replaced by the index in postureCenters of
# the corresponding closest representative.
#
# Input
#   timeSeries    - a numFrames x numDimensions matrix
#   centers       - a matrix of cluster centers used to represent each
#                   frame of timeSeries
#   warpNum       - the maximum length of repeated values allowed in
#                   stateSequence. If warpNum were set to 4, then a
#                   sequence 'aaaabbbb' would become 'ab'.  If warpNum were
#                   set to 3 it would become 'aabb', if 2 'aabb'.
#                   warpNum == 1 corresponds to no warping.
#   flickThresh   - the threshold for considering a state change to be a
#                   noisy "flicker".  A state change A -> B -> A is
#                   considered a flicker if B lasts for flickThresh or
#                   fewer frames.  In this case, B will be set to A to
#                   remove the flicker.  flickThresh == 0 indicates no
#                   flicker removal.  N.B. Using flickThresh > 1 might not
#                   make sense in some circumstances.  For example, it
#                   probably doesn't make sense to set B to A in a sequence
#                   like XXXABBBAXXX.
#
# Output
#   stateSequence - A numStates by 2 matrix.  The first column is the 
#                   sequence of states defined by the binned values
#                   across the channels, the second column is the number of
#                   times that state appears in the discrete version of the
#                   time series before warping by warpNum.
#   distVec       - The numFrames by 1 vector with the distance between
#                   each element of timeSeries and its nearest neighbour in
#                   centers. N.B. distVec is the distance calculated BEFORE
#                   removing 'flickers'.



# quantize the time series
    [stateSequence, distVec] = knnsearch(timeSeries, centers, 1)
    
    # get sign of state changes
    stateDiff = np.sign(np.diff(stateSequence))
    
    # find and remove different length flickers in turn
    for i in range(flickThresh):
        # find candidate flickers;
        flicks = np.hstack((np.array(1),np.zeros(i-1),np.array(-1)))
        substr = np.hstack((np.array(-1),np.zeros(i-1),np.array(1)))
        flicks = np.hstack((flicks, find_subsequence(stateDiff,substr)[0]))
        
        # check if states at beginning and end of candidates are the same
        for j in range(len(flicks)):
            if stateSequence[flicks[j]] == stateSequence[flicks[j] + i + 1]:
                # we have a flicker, mark it for removal
                stateSequence[flicks[j] + 1:flicks[j] + i] = np.matlib.repmat(stateSequence[flicks[j]], i, 1)
    
    # find places where the state changes
    changeInds = np.hstack((np.array(0), np.where(np.diff(stateSequence) != 0), np.array(len(stateSequence)+1)))
    
    # get the lengths of the constant segments
    constLengths = np.diff(changeInds)
    
    # find how many repeats must be removed from each constant segment
    targetLengths = math.ceil(constLengths/warpNum)
    cutLengths = constLengths - targetLengths
    
    # loop through constant state segments
    dropInds = np.zeros(len(stateSequence))
    for i in range(len(changeInds)-1):
        # check that this segment must be reduced
        if cutLengths[i] > 0:
            # set dropInds to 1 where constant segments must be shortened
            dropInds[changeInds[i]:changeInds[i] + cutLengths[i] - 1] = 1
    
    # reduce repeats in stateSequence
    stateSequence = np.delete(stateSequence, np.where(dropInds==1))
    
    # get the number of times each state in the reduced state sequence was 
    # present in the original
    stateLengths = np.array([np.nan]*len(stateSequence))
    count = 1;
    for i in range(len(targetLengths)):
        # if the target length is 1, then the state length is simply the
        # corresponding cutLength + 1
        if targetLengths[i] == 1:
            currentLengths = cutLengths[i] + 1
        else:
            # if the target length is greater than 1, then all lengths must be
            # warpNum, except possibly the last
            modulus = np.mod(constLengths[i], warpNum)
            if targetLengths[i] > 1 and modulus == 0:
                currentLengths = np.tile(warpNum, (targetLengths[i], 1));
            else:
                currentLengths = np.hstack(np.matlib.repmat(warpNum, targetLengths[i] - 1, 1), modulus)
        
        # add the state lengths for the current repeated segment
        stateLengths[count:count + len(currentLengths) - 1] = currentLengths
        
        # increment count
        count = count + len(currentLengths)
    
    # combine state sequence with state lengths
    stateSequence = np.hstack(stateSequence,stateLengths)
    
    return stateSequence, distVec
