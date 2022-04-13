# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 19:33:32 2021

@author: macbo
"""
import numpy as np

A = np.random.randint(-10,10,size=(3,3))
print(A)
B = np.linalg.inv(A)
print(B)
print(np.dot(A,B))


  