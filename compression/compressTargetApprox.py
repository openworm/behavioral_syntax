# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 22:05:27 2015

@author: ltopuser
"""

#function [matchN, meanDist, stdDist, compVec] = ...
#    compressTargetApprox(dataVec, grammar, distTable, thresh)

def compressTargetApprox(dataVec, grammar, distTable, thresh):
    
# COMPRESSTARGETAPPROX uses a grammar derived from another sequence to 
# compress a target data vector that was not used to derive the grammar. It
# calculates the compressed version of the target vector as well as the
# number of occurances of each of the elements of the grammar.
#
# See also: compressSequenceApprox.m
#
# Inputs
#   dataVec  - a numpy array of numbers to be compressed
#   grammar  - an N by 2 cell array. The first column has the
#              left hand side of each replacement rule while the second
#              column has the right hand side (so the first column lists
#              all non-terminals in the grammar).
#   distTable   - a 2-dimensional list of distances.  distTable[i][j] is the
#                distance between state i and state j.
#   thresh      - the distance threshold for calling matches.  Distances
#                 less than or equal to thresh are considered matches.
#                 N.B. this is the threshold PER MATCH, so for a 5-gram,
#                 the threshold will be 5*thresh
#
# Output
#   matchN   - a vector of counts.  matchN(i) contains the count of the ith
#              element in grammar.
#   meanDist - a vector indicating the mean distance between each grammar
#              rule and its approximate matches in compVec
#   stdDist  - a vector indicating the standard deviation of the distances
#              between each grammar rule and its matches in compVec
#   compVec  - the vector that has been compressed using grammar.  dataVec
#              can be recovered by applying the grammar rules in reverse.



    # initialisation
    N = np.shape(grammar)[0]
    M = np.shape(distTable)[0]
    matchN = np.zeros(N)[np.newaxis].T
    meanDist = np.zeros(N)[np.newaxis].T
    stdDist = np.zeros(N)[np.newaxis].T
    compVec = dataVec

    # add enough new rows and columns to distTable to accommodate the
    # the largest index in grammar.  Only exact matches are allowed for
    # non-terminals so set distance above threshold for all new matches
    # except self-matches which of course have zero distance.
    distTable = [distTable ...
        ones(size(distTable, 1), ...
        grammar{end, 1} - size(distTable, 1)...
        ) + thresh];
    
    distTable = [distTable; ...
        ones(grammar{end, 1} - size(distTable, 1), ...
        size(distTable, 2) ...
        ) + thresh];
    
    for k in range(grammar[N][0],M)
        distTable[k][k] = 0


    # make all replacements until none remaining is compressive
    isCompressive = 1
    while isCompressive == 1:
        # reset best savings
        bestSavings = 0;
        bestCount = 0;
        sequence = [];
        bestInd = -1;
    
    % check each rule in the grammar and take most compressive
    for i in range(N)
        % get the current sequence to check
        currentSequence = grammar[i][1]
        n = len(currentSeq)
        
        #get all of the n-grams
        nGrams = n_gramsNumerical(compVec, n)
        
        # get all the distances
        distVec = distSeq(currentSeq, nGrams, distTable)
        
        # get the matching indices
        matchInds = [i for i, x in enumerate(list(distVec <= n * thresh)) if x]
        
        # remove the overlaps
        while np.any(np.diff(matchInds, n=1, axis=0) < n):
            # find the first overlap
            overlapInd1 = np.nonzero(np.diff(matchInds, n=1, axis=0) < n)[0][0] + 1
            np.delete(matchInds,overlapInd1)
        
        # calculate number of matches without overlap
        count = len(matchInds)
        
        # calculate the savings of the current element
        savings = (len(currentSeq) - 1) * (count - 1) - 2
        if savings > bestSavings:
            bestSavings = savings
            bestCount = count
            bestMean = np.mean(distVec[i] for i in matchInds)
            bestStd = np.std(distVec[i] for i in matchInds)
            sequence = currentSeq
            inds = matchInds
            bestInd = i # index of best sequence in grammar

    
    # if no sequence was found with positive savings, compression is
    # finished
    if bestSavings == 0:
        isCompressive = 0
    else:
        # include the number of matches of the most compressive grammar
        # element in matchN
        matchN[bestInd] = bestCount
        meanDist[bestInd] = bestMean
        stdDist[bestInd] = bestStd
        
        # make the replacements in compVec
        for j in range(len(inds)):
            compVec(inds(jj):inds(jj) + numel(sequence) - 1) = ...
                [grammar{bestInd, 1} NaN(1, numel(sequence) - 1)];
        end
        compVec(isnan(compVec)) = [];
