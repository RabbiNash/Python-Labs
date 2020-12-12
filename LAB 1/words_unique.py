#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 08:50:25 2020

@author: nashe
"""


#unique words in a sentence

def unique(sentence):
    word_list = sentence.split()
    
    word_list_set = set(word_list)
    
    return list(word_list_set)

test = "My name is someone name jamaica"

print(unique(test))