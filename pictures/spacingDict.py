# -*- coding: utf-8 -*-
"""
Created on Thu May 13 15:06:57 2021

@author: blah
"""

import  string

lcAlpha = list(string.ascii_lowercase)
spacingDict = {}
spacingDict[' '] = 15 

for char in lcAlpha:
    if char in ['f', 'i', 'l']:
        spacingDict[char] = 10 
        
    if char in ['t', 's']:
        spacingDict[char] = 17
    
    if char in ['m']:
        spacingDict[char] = 27
        
    if char in ['w', 'y']:
        spacingDict[char] = 23
        
    else: 
        spacingDict[char] = 20
        