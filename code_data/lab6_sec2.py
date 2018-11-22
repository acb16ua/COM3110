# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 14:35:16 2018

@author: acb16ua
"""

from pylab import *
import random 

img = imread('che.png')
img_copy = array(img)
(d1, d2, d3) = img.shape

for i in range(d1):
    for j in range(d2):
        for k in range(d3):
            new_pixel = random.uniform(0, 1)
            
            pixel = img[i,j,k]
            if sum(pixel) < 1:
            #img[i,j] = (.0, .0, .0)
                img_copy[i,j,k] = new_pixel #+ img[i, j, k] 
            

imshow(img_copy)
show()