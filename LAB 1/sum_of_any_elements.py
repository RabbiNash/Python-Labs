#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 08:35:14 2020

@author: nashe
"""


#sum of any elements

def sum_elements(list):
    sum = 0
    for i in list:
        sum = sum + i
    
    return sum
   
total = sum_elements([1,2,3,4,5,6,7,9])      

print(total)  