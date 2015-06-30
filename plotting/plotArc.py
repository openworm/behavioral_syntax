import numpy as np
import math

def semicircle(startX, endX, sampRate):

    # SEMICIRCLE generates points on a semicircle between startX and endX with
    # a number of points equal to the diameter*sampRate (the sample rate).

    #define trig functions:
    cos = np.vectorize(math.cos)
    sin = np.vectorize(math.sin)
    
    radius = (endX - startX)/2
    xCenter = startX + radius
    theta = np.linspace(0,math.pi,sampRate*2*radius)
    
    x = radius * cos(theta)
    x[:] += xCenter
    y = radius * sin(theta)
    return x , y

def plotArc(X, color, sampRate, plotMode):

# PLOTARC plots a semicircular arc between two line segments defined by the
# four points in X.
# 
# See SEMICIRCLE, defined below
# 
# Input
#   X        - A 1x4 numpy array that defines the arc edges.  The arc is a patch
#              defined by a semi-circle connecting X(1) -> X(4), a straight
#              line from X(4) -> X(3), and a semi-circle from X(3) -> X(2).
#   color    - A 1x4 numpy array defining the color and transparency of the
#              patch in the following format: [r g b alpha]
#   sampRate - The sampling rate for creating the arc.  If sample rate is
#              1, there will be the same number of points as the arc
#              diameter.  Setting sampRate less than 1 will give
#              proportionately fewer points.
#   plotMode - 'patch' or 'line'.  'patch' only works well if width of the
#              arc is not too much smaller than the radius.  Otherwise it
#              just looks like a line anyway.  In this case 'line' is
#              better because it uses fewer points and the matlab plotter
#              renders it better on screen.




    if plotMode =='patch':
        # get the patch coordinates
        firstArcX, firstArcY = semicircle(X[0], X[3], sampRate)
        secondArcX, secondArcY = semicircle(X[1], X[2], sampRate)
    
    # plot the patch
    patch([firstArcX, secondArcX(end:-1:1)], ...
        [firstArcY, secondArcY(end:-1:1)], color(1:3), ...
        'FaceAlpha', color(4), 'LineStyle', 'none')
    elif plotMode == 'line':
        # get line coordinates
        arcX, arcY = semicircle(X[0] + (X[1] - X[1])/2, X[2] + (X[3] - X[2])/2,sampRate)
    
        # plot the line with a width proportional to the difference between
        # X(1) and X(2)
        line(arcX, arcY, 'LineWidth', (X(2) - X(1))*0.5, 'Color', color(1:3))
    #     patch([arcX NaN], [arcY NaN], color(1:3), ...
    #         'FaceAlpha', color(4), 'LineStyle', 'none')
    else
        print('plotMode must be either patch or line')
