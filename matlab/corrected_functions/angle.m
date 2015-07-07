function [angleArray, meanAngles] = angle(x, y)

%given a series of x and y coordinates over time, calculates the angle
%between each vector making up the skeleton and the x-axis.  The mean angle
%is subtracted from each frame so that the average orientation is always
%the same in the output angleArray.
% 
% 
% André Brown, andre.brown@csc.mrc.ac.uk, aexbrown@gmail.com
% 
% The MIT License
% 
% Copyright (c)  Medical Research Council 2015
% 
% Permission is hereby granted, free of charge, to any person obtaining a copy
% of this software and associated documentation files (the "Software"), to deal
% in the Software without restriction, including without limitation the rights
% to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
% copies of the Software, and to permit persons to whom the Software is
% furnished to do so, subject to the following conditions:
% 
% The above copyright notice and this permission notice shall be included in
% all copies or substantial portions of the Software.
% 
% THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
% IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
% FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
% AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
% LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
% OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
% THE SOFTWARE.



[lengthX, noFrames] = size(x);

%arrays to build up and export
angleArray = zeros(lengthX-1, noFrames);
meanAngles = zeros(noFrames, 1);

for i=1:noFrames
    
    dX = diff(x(:,i));
    dY = diff(y(:,i));
    
    %calculate angles.  atan2 uses angles from -pi to pi instead of atan which
    %uses the range -pi/2 to pi/2.
    angles = atan2(dY, dX);
    
    %need to deal with cases where angle changes discontinuously from -pi
    %to pi and pi to -pi.  In these cases, subtract 2pi and add 2pi
    %respectively to all remaining points.  This effectively extends the
    %range outside the -pi to pi range.  Everything is re-centred later
    %when we subtract off the mean.
    
    %find discontinuities
    positiveJumps = find(diff(angles) > 5) + 1; %+1 to cancel shift of diff
    negativeJumps = find(diff(angles) < -5) + 1;
    
    %subtract 2pi from remainging data after positive jumps
    for j = 1:length(positiveJumps)
        angles(positiveJumps(j):end) = angles(positiveJumps(j):end) - 2*pi;
    end
    
    %add 2pi to remaining data after negative jumps
    for j = 1:length(negativeJumps)
        angles(negativeJumps(j):end) = angles(negativeJumps(j):end) + 2*pi;
    end
    
    %rotate skeleton angles so that mean orientation is zero
    meanAngle = mean(angles(:));
    meanAngles(i) = meanAngle;
    angles = angles - meanAngle;
    
    %append to angle array
    angleArray(:,i) = angles;
    
    %figure(i);
    %plot(angles);
    
end
