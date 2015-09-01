# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 23:01:49 2015

@author: macbook
"""

import numpy as np

def compressSequenceNFast(dataVec, newStart, nMax):

# COMPRESSSEQUENCE Recursively finds the most compressive subsequence in
# dataVec and creates and replaces it with a new number.  This replacement
# creates a new rule in the grammar.  Replacements are made until there are
# none left that lead to further compression.  See the following paper
# for more details: Nevill-Manning and Witten (2000) On-Line and Off-Line
# Heuristics for Inferring Hierarchies of Repetitions in Sequences.
# Proceedings of the IEEE 88:1745.
#
# Input
#   dataVec  - a row vector of numbers to be compressed
#   newStart - this is the number that will be used to label the first new
#              rule in the grammar.  It must be greater than the maximum
#              value in dataVec.  If empty, then max(dataVec) + 1 is used.
#   nMax        - the maximum length n-gram to check for compression
#
# Output
#   grammar  - a number of rules by 2 cell array. The first column has the
#              left hand side of each replacement rule while the second
#              column has the right hand side (so the first column lists
#              all non-terminals in the grammar).
#   compVec  - the vector that has been compressed using grammar.  dataVec
#              can be recovered by applying the grammar rules in reverse.
#   totSavings - the total space saving achieved during the compression,
#                taking into account the size of the created grammar rules



    # check dataVec
    if len(np.shape(posture_seq)) > 1:
        print('dataVec must be a row vector.')
    
    # define newStart if left empty
    if newStart == 0:
        newStart = max(dataVec) + 1
    
    # check that newStart is large enough
    if newStart <= max(dataVec):
        print('newStart must be greater than max(dataVec).')

    # initialise grammar
    grammar = list(np.zeros(2))
    
    # initialise compVec and make a suffix array
    compVec = dataVec
    totSavings = 0
    
    # compress segments until none are found that lead to compression
    sequence = [np.nan]
    newInd = newStart
    i = 1
    while len(sequence) > 0:
    # find the most compressive sequence in dataVec
        [sequence, locations, savings] = compressiveNFast(compVec, nMax)
    
    # update the total savings (i.e. compression)
    totSavings = totSavings + savings
    
    # add the rule to grammar
    grammar{ii, 1} = newInd
    grammar{ii, 2} = sequence
    i+=1
    # disp(ii);
    
    # make the replacements.  Note: strrep does not work here.  For example
    # if sequence is [44 68 44] and compVec has a subsequence that is 
    # [44 68 44 68 44 68 44 448], strrep will give [68 480 480 480 448]
    # which is wrong.
    for jj = 1:numel(locations)
        compVec(locations(jj):locations(jj) + numel(sequence) - 1) = ...
            [newInd NaN(1, numel(sequence) - 1)];
    end
    compVec(isnan(compVec)) = [];
    
    newInd = newInd + 1;
    
    # check that compressed lengths, savings, and grammar size are
    # consistent
    if ~isempty(sequence) # on last iteration last grammar entry is empty
        if length(compVec) + totSavings + size(grammar, 1) + ...
                sum(cellfun(@length, grammar(:, 2))) ~= length(dataVec)
            error(['Calculated savings not consistent with original' ...
                ' and compressed lengths and grammar size.'])
        end
    else
        if length(compVec) + totSavings + size(grammar, 1) - 1 + ...
                sum(cellfun(@length, grammar(:, 2))) ~= length(dataVec)
            error(['Calculated savings not consistent with original' ...
                ' and compressed lengths and grammar size.'])
        end
    end
    end
    
    # remove the last (empty) entry of the grammar
    grammar = grammar(1:end-1, :);