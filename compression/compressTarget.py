import numpy as np
import re

def compressTarget(dataVec, grammar):

# COMPRESSTARGET uses a grammar derived from another sequence to compress a
# target data vector that was not used to derive the grammar.  It
# calculates the compressed version of the target vector as well as the
# number of occurances of each of the elements of the grammar.
#
# See also: compressSequenceNFast.m and expandGrammar.m
#
# Inputs
#   dataVec  - a row vector of numbers to be compressed
#   grammar  - a number of rules by 2 list. The first column has the
#              left hand side of each replacement rule while the second
#              column has the right hand side (so the first column lists
#              all non-terminals in the grammar).
#
# Output
#   matchN   - a vector of counts.  matchN(i) contains the count of the ith
#              element in grammar.
#   compVec  - the vector that has been compressed using grammar.  dataVec
#              can be recovered by applying the grammar rules in reverse.



    # initialisation
    N = np.shape(grammar)[0]
    matchN = np.zeros(N)[np.newaxis].T
    compVec = np.array(dataVec).tolist()
     
    # make all replacements until none remaining is compressive
    isCompressive = 1
    while isCompressive == 1:
        # reset best savings
        bestSavings = 0;
        bestCount = 0;
        sequence = [];
        bestInd = -1;
        
        # make a string version of compVec for the search in the loop
        dataString = '  '.join(str(e) for e in compVec)
        
        # check each rule in the grammar and take most compressive
        for i in range(N):
            # get the current sequence to check
            currentSequence = grammar[i][1]
            
            # first do fast check to see if the sequence is even present before
            # doing slower no-overlap  count
            if np.core.defchararray.find(compVec, currentSequence) >= 0:
                
                # get the non-overlapping counts of the current n-gram. Pad
                # uniqueNGrams with spaces to avoid matches like: '76 7'
                # matching '76 78' in dataString.  Each element of compVec is
                # separated by two spaces, so separate each element of the 
                # current n-gram with two spaces but only pad with one on 
                # either side.  This allows overlaps to be correctly counted.  
                # E.g. ' 2  2 ' will be found twice in '12  2  2  2  2  22  5' 
                # as it should be.
                currentString = '  '.join(str(e) for e in currentSequence)
                count = np.size( [m.start() for m in re.finditer(currentString, dataString)] );
                
                # calculate the savings of the current element
                savings = (len(currentSequence) - 1) * (count - 1) - 2
                if savings > bestSavings:
                    bestSavings = savings
                    bestCount = count
                    sequence = currentSequence
                    bestInd = i # index of best sequence in grammar
        
        # if no sequence was found with positive savings, compression is finished
        if bestSavings == 0:
            isCompressive = 0
        else:
            # include the number of matches of the most compressive grammar
            # element in matchN
            matchN[bestInd] = bestCount
            
            # get the locations with overlaps
            inds = [m.start() for m in re.finditer(sequence, compVec)]
            
            # remove the overlaps
            while any(diff(inds) < numel(sequence))
                % find the first overlap
                overlapInd1 = ...
                    find(diff(inds) < numel(sequence), 1, 'first') + 1;
                inds(overlapInd1) = [];
            end
            
            # make the replacements in compVec
            for jj = 1:numel(inds)
                compVec(inds(jj):inds(jj) + numel(sequence) - 1) = ...
                    [grammar{bestInd, 1} NaN(1, numel(sequence) - 1)];
            end
            compVec(isnan(compVec)) = [];
