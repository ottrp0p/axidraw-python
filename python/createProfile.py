# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 12:26:08 2021

@author: blah
"""

# how to manage and create profiles 

from pathlib import Path
from axidrawinternal import axidraw
import os 
import svgutils
import sys
import re
import string
import random
import math 

import fixedLists # code for fixed lists of char/paths for project 

def createProfile(profile):
    # going two levels up, past Python
    masterDir = Path(__file__).parents[1]

    # get into Profiles 
    profileDir = str(masterDir) + '\\Profiles' 
    
    
    # folder list gen
    folderList = fixedLists.folderList()

        
    
    if os.path.isdir(profileDir) == False: 
        os.mkdir(profileDir)
        print('profile directory did not exist. Created')
    
    if os.path.isdir(profileDir + '\\' + profile ) == False :
        os.mkdir(profileDir + '\\' + profile)
        os.mkdir(profileDir + '\\' + profile + '\\' + 'Originals')
        print('new profile does not exist yet. Now created') 
        
        for path in folderList :
            os.mkdir(profileDir + '\\' + profile + '\\' + 'Originals' + '\\' + path) 
        print('created all new subfolders in Originals')
        
        
    else: 
        print('profile already exists')
        if os.path.isdir(profileDir + '\\' + profile + '\\' + 'Originals') == False: 
            os.mkdir(profileDir + '\\' + profile + '\\' + 'Originals')
                        
        
        for path in folderList :
            if os.path.isdir(profileDir + '\\' + profile + '\\' + 'Originals' + '\\' + path)  == False:
                os.mkdir(profileDir + '\\' + profile + '\\' + 'Originals' + '\\' + path)  
        print('all subfolders checked. all missing subfolders created')
        
    
    print('please populate the folders with the necessary original SVGs')

def profileProfile(profile):
    # bad naming. To profile the a given profile 
    # by deriving OG source counts. 
    
    # going two levels up, past Python
    masterDir = Path(__file__).parents[1]

    # get into Profiles 
    profileDir = str(masterDir) + '\\Profiles'+ '\\' + profile + '\\Originals'
    folderList = fixedLists.folderList()
    for folder in folderList: 
        if os.path.isdir(profileDir +'\\' + folder ):
            print('{} folder exists'.format(folder))
            print('{} source files'.format(len(os.listdir(profileDir +'\\' + folder))))
        else:
            print('ERROR, {} does not exist'.format(folder))
            
        
    
    
    
# createProfile('Allen')
# profileProfile('Allen')