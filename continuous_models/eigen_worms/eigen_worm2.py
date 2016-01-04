# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 22:10:19 2016

@author: aidanrocke
"""

import numpy as np
import seaborn as sns

from scipy.stats import spearmanr

from scipy.io import loadmat

postures = loadmat('/Users/cyrilrocke/behavioral_syntax/data/postures.mat')

pos = postures.get('postures')



rho, pval = spearmanr(pos)

sns.heatmap(rho)

eigen = np.linalg.eig(rho)

eigen = eigen[0]



