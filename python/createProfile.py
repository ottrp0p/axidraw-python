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
import platform 

import fixedLists # code for fixed lists of char/paths for project 
import spacingHandler
from delimSys import *



def createProfile(profile):

    
    # going two levels up, past Python
    masterDir = Path(__file__).parents[1]

    # get into Profiles 
    profileDir = str(masterDir) + delim + 'Profiles' 
    
    
    # folder list gen
    folderList = fixedLists.folderList()

        
    
    if os.path.isdir(profileDir) == False: 
        os.mkdir(profileDir)
        print('profile directory did not exist. Created')
    
    if os.path.isdir(profileDir + delim + profile ) == False :
        os.mkdir(profileDir + delim + profile)
        os.mkdir(profileDir + delim + profile + delim + 'Originals')
        print('new profile does not exist yet. Now created') 
        
        for path in folderList :
            os.mkdir(profileDir + delim + profile + delim + 'Originals' + delim + path) 
        print('created all new subfolders in Originals')
        spacingHandler.loadSpacings(profile)
        print('initalized Spacings')
    
        spacingHandler.loadAddress(profile)
        print('intialized profile')
        
    else: 
        print('profile already exists')
        if os.path.isdir(profileDir + delim + profile + delim + 'Originals') == False: 
            os.mkdir(profileDir + delim + profile + delim + 'Originals')
                        
        
        for path in folderList :
            if os.path.isdir(profileDir + delim + profile + delim + 'Originals' + delim + path)  == False:
                os.mkdir(profileDir + delim + profile + delim + 'Originals' + delim + path)  
        print('all subfolders checked. all missing subfolders created')
        
        spacingHandler.loadSpacings(profile)
        print('initalized Spacings')
    
        spacingHandler.loadAddress(profile)
        print('intialized profile')
        
    
    print('please populate the folders with the necessary original SVGs')

def profileProfile(profile):
    # bad naming. To profile the a given profile 
    # by deriving OG source counts. 
    taskReady = True
    
    # going two levels up, past Python
    masterDir = Path(__file__).parents[1]

    # get into Profiles 
    profileDir = str(masterDir) + delim + 'Profiles'+ delim + profile + delim + 'Originals'
    folderList = fixedLists.folderList()
    for folder in folderList: 
        if os.path.isdir(profileDir + delim + folder ):
            print('{} folder exists'.format(folder))
            print('{} source files'.format(len(os.listdir(profileDir + delim + folder))))
            if len(os.listdir(profileDir + delim + folder)) == 0 : 
                   taskReady = False
        else:
            print('ERROR, {} does not exist'.format(folder))
            taskReady = False
    return taskReady
        
    
    
    
createProfile('Allen')
# profileProfile('Allen')