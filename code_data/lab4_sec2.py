# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def sum_list(num):
    
    sum = 0
    for i in num:
        sum += i
        
    return sum    

""""""""""""""""""""""""""""""
def triangular_number(num):
    
    sum = 0
    num += 1
    for i in range(num):
        sum += i
        
    return sum    

""""""""""""""""""""""""""""""
def square_list(num):
    
    nlist = list(num)
    index = 0
    for i in num:
        nlist[index] = i ** 2
        index += 1
        
    return nlist  
        
""""""""""""""""""""""""""""""
def triangular_list(num):
    
    nlist = list(num)
    index = 0
    for i in num:
        nlist[index] = triangular_number(i)
        index += 1
        
    return nlist    