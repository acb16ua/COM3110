# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 13:59:07 2018

@author: acb16ua
"""

def countWords(file):
    
    infile = open(file)
    wordCount = {}
    
    for line in infile:
        x = line.split()
        
        for word in x:
            if word in wordCount:
               wordCount[word] += 1
            else:
                wordCount[word] = 1            
                
    return wordCount

def printTop20(count):
    
    sorted_keys = sorted(count.keys(), reverse=True)
    sorted_values = sorted(count.values(), reverse=True)
    
    for index in range(20):
        print(sorted_keys[index], '=', sorted_values[index] )
    
    #for word in sortedList:
     #   print(word)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    #index = 0
    #top20List = {}
    
    #for key in sorted(count.values(), reverse=True):
    #sortedDict = sorted(count.values(), reverse=True)
    #for index in range(20):
     #   print(sorted)
    
        
        
   # return key        