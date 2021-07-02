# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 08:30:28 2021

@author: Kushan
"""

import numpy as np

inputArr = np.array(list(map(int, input().rstrip().split())))

minOfInputArr = np.min(inputArr)
maxOfInputArr = np.max(inputArr)

duplicateArr = np.arange(minOfInputArr, maxOfInputArr+2)

for elem in duplicateArr:
    if elem > 0:
        if elem not in inputArr:
            print(elem)
            break