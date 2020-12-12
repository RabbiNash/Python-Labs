#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 08:39:30 2020

@author: nashe
"""


#writing to files


file = open("text_file.txt", "a")

def write_to_file(file, message):
    file.write(message)
    file.close()
    
write_to_file(file, "Tinashe Makuti")


    
read_file = open("text_file.txt", "r")

def num_words_in_file(file):
    file_content = file.read()
    file.close()
    
    content_list = file_content.split()
    
    return len(content_list)

print(num_words_in_file(read_file))