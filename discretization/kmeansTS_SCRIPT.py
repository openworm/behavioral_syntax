# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 21:00:24 2015

@author: ltopuser
"""

import os
import scipy

# find a set of representative postures by loading angleArrays from a
# directory and performing k-means clustering.

# clear angleTotal so that it doesn't accumulate from previous script runs
# in case workspace was not totally cleared

# set the root directory
# directory = ['/Users/abrown/Andre/wormVideos/results-12-05-10/'...
#     'Laura Grundy/'];
# directory = ['/Users/abrown/Andre/wormVideos/results-12-05-10/'...
#     'Laura Grundy/gene_NA/allele_NA/N2/on_food/XX/30m_wait/'];
# directory = ['/Users/abrown/Andre/wormVideos/results-12-05-10/' ...
#     'wild-isolates/'];

directory = 'C:/Users/ltopuser/behavioral_syntax/utilities/'

# ---------------------------- Set Parameters -----------------------------
minFrames = 1000; # the minimum number of acceptable frames in a file
fileNum = 200; # the number of random files to process.  N.B. if fileNum is
               # >= to the number of files in fileList, then the script
               # will simply run deterministically on all files in the list
frameNum = 5000; # the number of random frames to take per file
k = 500; # the number of centres to use for k-means clustering
# -------------------------------------------------------------------------

# seed random number generator for reproducibility
#rng(49230);

# get the list of files (includes data from mutant classes)
fileList = os.listdir(directory)

isRandom = 1
# check if random files or all files should be analysed
if fileNum >= len(fileList):
    fileNum = len(fileList)
    isRandom = 0

# loop through files
angleTotal = [];
for i in range(fileNum):
    if isRandom == 1:
        # get a random file
        # N.B. if directory has a small number of files there could be
        # repeats keep searching until angleArray has enough elements
        angleArray = []
        x, y = np.shape(angleArray)
        while (x < minFrames) or np.count_nonzero(~np.isnan(angleArray[:,i])) < 2:
            fileInd = random.randint(1,len(fileList))
            
            # load the angle array data
            file = directory + fileList[fileInd]
            angles_dict = scipy.io.loadmat(file)
            angleArray = angles['x']
            
    else:
        fileInd = i
        file = directory + fileList[fileInd]
        angles_dict = scipy.io.loadmat(file)
        angleArray = angles['x']
        
    # instead of dropping NaN values, interpolate over NaNs
    # initialise anglesNoNaN
    anglesNoNaN = angleArray
    
    # interpolate over NaN values
    for j in range(x):
        pAmp = angleArray[j]
        true = np.isnan(pAmp)
        ix_t = np.where(true == True)
        ix_f = np.where(true == False)
        f = interpolate.interp1d(~true, pAmp[ix_f])
        pAmp[ix_t] = f(ix_t)
        anglesNoNaN[j] = pAmp
    
    # since extrapolation was not used, there could still be some remaining
    # NaNs.  Remove these here.
    nanRows = find(isnan(anglesNoNaN(:, 1)))
    anglesNoNaN(nanRows, :) = []
    
    # take a random subset of frames (could include repeats)
    frameInds = randi(size(anglesNoNaN, 1), frameNum, 1);
    anglesNoNaN = anglesNoNaN(frameInds, :);
    
    # if the worm is in the "left" folder, invert all the angles.
    if ~isempty(strfind(fileList{fileInd}, '/L/'))
        anglesNoNaN = anglesNoNaN * -1;
    end
    
    # add the current angle array to the total
    angleTotal = [angleTotal; anglesNoNaN];
end

# do the clustering
[~, postures] = kmeans(angleTotal', k);

# save the representative postures in a mat file
save([directory 'BENZALDEHYDE_postures_' num2str(k) '-centers_' num2str(fileNum) ...
    '-files_' num2str(frameNum) '-framesPerFile.mat'], 'postures')
