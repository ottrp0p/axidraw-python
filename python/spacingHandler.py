# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 17:58:10 2021

@author: blah
"""

# These scripts are here to help test and create a profile's spacings 

import pickle 
# font Proliferate script 
from axidrawinternal import axidraw
import os 
import svgutils
import sys
import re
import string
import random
import math 
from pathlib import Path

from addDim import * 
import fixedLists # code for fixed lists of char/paths for project 


def loadSpacings(profile):
    # going two levels up, past Python
    masterDir = Path(__file__).parents[1]

    # get into Profiles 
    profileDir = str(masterDir) + '\\Profiles' +  '\\' + profile  
    if os.path.exists(profileDir + '\\' + 'spacings.p') == True:
        pickleFile = open(profileDir + '\\' + 'spacings.p', 'rb')
        spacingDict = pickle.load(pickleFile)
        pickleFile.close()
        return spacingDict 
    
    else: 
        # init the file
        spacingDict = {}
        chars = fixedLists.charMapping()
        print(chars)
        chars = chars.keys()
        print(chars)
        for char in chars:
            spacingDict[char] = 11
        pickle.dump(spacingDict, open(profileDir + '\\' + 'spacings.p', 'wb'))

        return spacingDict 

def changeSpacings(profile, newSpacings):
    # newSpacings entered as a dictionary for mutliple changes 
    # going two levels up, past Python
    masterDir = Path(__file__).parents[1]

    # get into Profiles 
    profileDir = str(masterDir) + '\\Profiles' +  '\\' + profile  
    spacingDict = loadSpacings(profile)
    for key in newSpacings.keys(): 
        spacingDict[key] = newSpacings[key]
    pickle.dump(spacingDict, open(profileDir + '\\' + 'spacings.p', 'wb'))

            
            
