# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 18:15:37 2021

@author: macbo
"""

import re

with open("in.in") as reader:
    content =reader.readlines()
pattern="username:(.*?);passwd:(.*?)$"
for i in content:
    tmp=re.findall(pattern,i)
    if tmp != []:
        print(tmp)