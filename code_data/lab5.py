# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from pylab import plot
from pylab import show
import numpy as np
import matplotlib.pyplot as plt

infile = open('pulse_data.txt')
index = 0
data_list = []
Xs = list(range(1, 51))

for line in infile:
    data_list.append(float(line))
    #ndex += 1

#data_list.sort()

BINS = 50
minval = min(data_list)
maxval = max(data_list)
vspan = maxval - minval
binId_list = []
counter = []*BINS

for value in data_list:    
    binId = int(BINS * (value - minval) / vspan)
    
    if binId == BINS:
        binId = BINS-1
    
    binId_list.append(binId)

for countx in binId_list:
    counter[countx] += 1
    
#plot(Xs, binId)
plt.hist(binId_list, bins=BINS)    
show()
    
print(counter)    