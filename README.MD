#briefly:
1. This is the Python 3 implementation of Andre Brown's behavioral syntax code: https://github.com/aexbrown/Behavioural_Syntax
2. But, the ultimate goal of this project is to define the benefits as well as limitations of the 'behavioral syntax' approach. 
3. As such, the completed project will include statistical tests that will serve to determine whether the available movement data is amenable to a 'behavioral syntax' analysis. 


### Main functions:
1. extract a minimal number of template postures using Kmeans++
2. discretize the video sequences of worm skeletons using this set of template postures
3. use a simple time-warping algorithm to reduce the video sequences of postures to sequences that don't have
adjacent duplicates. i.e. {3,4,4,5,75,75,6,6,6} = {3,45,75,6}
4. After step 3 is done, all kinds of NLP methods(ex. trigrams) or bio-informatic methods for discrete sequences of data may be used. 


![hr] (https://github.com/AidanRocke/behavioral_syntax/blob/master/90_postures.png)

