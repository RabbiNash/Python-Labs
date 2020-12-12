#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 09:35:36 2020

@author: nashe
"""


#class file tool box

class FileToolBox():
    
    def __init__(self, fileName):
        self.file = open(fileName, "a")
        self.fileName = fileName
        
    def write_to_file(self,message):
        self.file.write(message)
   
    def num_words_in_file(self):
        file_content = self.file.read()
        self.file.close()
        
        content_list = file_content.split()
        
        return len(content_list)
    
    def frequency(words):
        word_list = words.split()
        word_set = set(word_list)
        
        frequency_dict = {}
        
        for word in word_set:
            frequency_dict[word] = word_list.count(word)
                
        return frequency_dict
    
    def unique(sentence):
        word_list = sentence.split()
        word_list_set = set(word_list)
        
        return list(word_list_set)
    
    def sum_elements(list):
        sum = 0
        for i in list:
            sum = sum + i
        
        return sum
    
    def openFile(self, mode):
        self.file = open(self.fileName, mode)
   
    def closeFile(self):
        self.file.close

toolBox = FileToolBox("makuti")
toolBox.write_to_file("Tinashe Makuti")
toolBox.closeFile()
toolBox.openFile("r")
print(toolBox.num_words_in_file())

