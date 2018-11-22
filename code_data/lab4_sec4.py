# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 15:11:06 2018

@author: acb16ua
"""
from pylab import *


infile = open('noisy_signal.txt')
token = 0
time_value = list()
intensity_value = list()
index = 0

for line in infile:
    token += 1
    vals = line.split()
    time_value.append(float(vals[0]))
    intensity_value.append(float(vals[1]))
    index = index+1
    
#print(token)    
#print(time_value)
#print(intensity_value)

#plot(time_value,intensity_value)
#show()

window = 20

time_value_average = []
intensity_value_average = []

for data in time_value:
    time_value_average.a