# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 15:01:39 2018

@author: acb16ua
"""

from lab7_countwords import countWords
from lab7_countwords import printTop20


task1Result = countWords('mobydick.txt')

task2Result = printTop20(task1Result)    

print(task1Result, task2Result)
print(task2Result)
#print(type(task1Result))