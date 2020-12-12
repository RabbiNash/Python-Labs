#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 08:58:57 2020

@author: nashe
"""


#frequency

def frequency(words):
    word_list = words.split()
    
    word_set = set(word_list)
    
    frequency_dict = {}
    
    for word in word_set:
        frequency_dict[word] = word_list.count(word)
        
            
    return frequency_dict
        
print(frequency("My name is Tinashe, Makuti"))