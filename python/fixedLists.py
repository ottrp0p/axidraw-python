# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 12:45:19 2021

@author: blah
"""
 
# fixed list files
# in case multiple files reference for pulling file path lists 
# or char lists or what not
import string 



# dict describing 'type' for each char 
# doubles as the list of usable chars by using the keys 
# note that we do not cover blank space. 
def charMapping(): 
    mapDict = {}
    for letter in list(string.ascii_lowercase):
        mapDict[letter] = 'lower'
    for letter in list(string.ascii_uppercase):
        mapDict[letter] = 'upper'
    for number in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']: 
        mapDict[number] = 'numeric'
    for char in ['#', '@', ',', '.', "'"]:
        mapDict[char] = 'char'
    return mapDict
        
# folder list gen
def folderList(): 
    charmap = charMapping()
    folderList = []
    for char in charmap:
        folderList.append(charmap[char] + '-'+ char + '-')
    return folderList 



