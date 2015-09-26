from matplotlib import pyplot as plt
import math
import numpy as np

def plotGrammarSequence(gExp, postures, sequenceInds):
    
#   gExp     - an N by 1 list of rules.  It is the expanded
#              version of the input grammar obtained by applying the rules
#              encoded in the grammar.  It contains the progressively
#              expanded version of each of the rules in the grammar.  For
#              any given entry gExp{ii}{end} contains only terminal
#              symbols.

#   sampRate - The sampling rate for creating the arc.  If sample rate is
#              1, there will be the same number of points as the arc
#              diameter.  Setting sampRate less than 1 will give
#              proportionately fewer points.

    N = len(gExp)
    arclength = 1
    offsetFactor = 0.3
    for i in range(len(sequenceInds)):
        currentInd = sequenceInds[i]
        currentSeq = gExp[N][currentInd]
        plt.figure(1)
        for j in range(len(currentSeq)):
            # convert the current matching posture to xy-coordinates
            x, y = angle2skel(postures(currentSeq[j])-math.pi/2, arclength)
            
            #plot the matching posture over the original skeleton
            plt.plot(x - np.mean(x) + j * offsetFactor, y - np.mean(y), 'r', lw = 3)
            
            # mark the head
            plt.plot(x[0] - np.mean(x) + j * offsetFactor, y[0] - np.mean(y), 'b', lw = 5)
