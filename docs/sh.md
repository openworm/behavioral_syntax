
#briefly:
1. This is the Python implementation of Andre Brown's behavioral syntax code: https://github.com/aexbrown/Behavioural_Syntax
2. But, the ultimate goal of this project is to define the benefits as well as limitations of the 'behavioral syntax' approach. 
3. For more information please consult the wiki.
4. continous_models are included to compare with the findings of the discrete approach. 


### Main functions:
1. extract a minimal number of template postures using Kmeans++
2. discretize the video sequences of worm skeletons using this set of template postures
3. use a simple time-warping algorithm to reduce the video sequences of postures to sequences that don't have
adjacent duplicates. i.e. {3,4,4,5,75,75,6,6,6} = {3,45,75,6}
4. After step 3 is done, all kinds of NLP methods(ex. trigrams) or bio-informatic methods for discrete sequences of data may be used.