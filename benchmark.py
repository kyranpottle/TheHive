#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 09:58:56 2018

Benchmarking Script for The Hive

@author: kyran
"""

import time


start = time.time()
print("Start")

for i in range(1,1000):
    for x in range(1,1000):
        3.141592 * 2**x

    for x in range(1,1000):
        float(x) / 3.141592
            
        for x in range(1,1000):
            float(3.141592) / x
                
end = time.time()

duration = end - start

print(duration)