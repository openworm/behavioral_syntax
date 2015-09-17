# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 16:30:49 2015

@author: aidanrocke
"""
import numpy as np

def angle_error(angle_arr1,angle_arr2):
    return np.linalg.norm(angle_arr1-angle_arr2)

def variance_explained(angle_arr1,angle_arr2):
    return np.corrcoef(angle_arr1,angle_arr2)[0][1]**2
