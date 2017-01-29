[![Build Status](https://travis-ci.org/openworm/behavioral_syntax.svg?branch=master)](https://travis-ci.org/openworm/behavioral_syntax)

[![Build Status](https://travis-ci.org/AidanRocke/behavioral_syntax.svg?branch=master)](https://travis-ci.org/AidanRocke/behavioral_syntax)

[![Coverage Status](https://coveralls.io/repos/AidanRocke/behavioral_syntax/badge.svg?branch=master&service=github)](https://coveralls.io/github/AidanRocke/behavioral_syntax?branch=master)

#briefly:
1. This is a behavioral turing test derived from ideas in Andre Brown's behavioral syntax code: https://github.com/aexbrown/Behavioural_Syntax and other sources.
2. The comparisons are based on the movement of individual worms in petri dishes in three different environments. Off food, on food, and with chemical gradients. 
3. For more information, please check the docs: http://behavioral-syntax.readthedocs.org/en/latest/


### Main functions:
1. extract a minimal number of template postures using Kmeans++
2. discretize the video sequences of worm skeletons using this set of template postures
3. use a simple time-warping algorithm to reduce the video sequences of postures to sequences that don't have
adjacent duplicates. i.e. {3,4,4,5,75,75,6,6,6} = {3,45,75,6}
4. After step 3 is done, all kinds of NLP methods(ex. trigrams) or bio-informatic methods for discrete sequences of data may be used.

### Dependencies:
1. numpy
2. pandas
3. h5py
4. statsmodels
5. sklearn
6. scipy
7. matplotlib
8. seaborn
9. bokeh

##### Example of a template with 90 postures extracted using Kmeans++:
![hr] (https://raw.githubusercontent.com/openworm/behavioral_syntax/master/lab_reports/figures/postures.png)

##### Visualizing the tangent angle distance between postures:
![hr] (https://raw.githubusercontent.com/openworm/behavioral_syntax/master/lab_reports/figures/mds.png)
8. seaborn
9. bokeh

##### Example of a template with 90 postures extracted using Kmeans++:
![hr] (https://raw.githubusercontent.com/AidanRocke/behavioral_syntax/master/data/90_postures.png)

##### Visualizing the tangent angle distance between postures:
![hr] (https://github.com/AidanRocke/behavioral_syntax/blob/master/data/bokeh_postures_mds.png)
