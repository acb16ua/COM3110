# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from pylab import *
img = imread('chick.png')
(d1, d2, d3) = img.shape

for i in range(d1):
    for j in range(d2):
        #for k in range(d3):
            #img[i,j,k] = 1 - img[i,j,k]
        pixel = img[i,j]
        #if sum(pixel) < 1.5:
         #   img[i,j] = (.0, .0, .0)

        print(pixel)
imshow(img)
show()