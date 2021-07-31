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



def loadAddress(profile):
    print('creating profile address dict')
    masterDir = Path(__file__).parents[1]

    # get into Profiles 
    profileDir = str(masterDir) + '\\Profiles' +  '\\' + profile  
    if os.path.exists(profileDir + '\\' + 'address.p') == False:
        print('address dict does not exist. initializing')
        firstName = input("Input profile First Name: \n" )
        lastName = input("Input profile Last Name: \n")
        address1 = input("Input Street Address (i.e. 1200 E California Blvd): \n")
        address2 = input("Input City, State Zipcode: \n")
        emailAddress = input("Input profile email address: \n")
        addressDict = {'firstName' : firstName, 
                    'lastName' : lastName, 
                    'address1' : address1, 
                    'address2' : address2, 
                    'emailAddress' : emailAddress 
            }
        pickle.dump(addressDict, open(profileDir + '\\' + 'address.p', 'wb'))
        return addressDict
    else: 
        print('address dict exists. loading')
        pickleFile = open(profileDir + '\\' + 'address.p', 'rb')
        addressDict = pickle.load(pickleFile)
        pickleFile.close()
        return addressDict 
        
        

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
        # this is hardcoded off of Allen's profile 
        # numbers derived from testing against general spacing. 
        # the starting point.
        spacingDict = {'a': 11,
        'b': 11,
        'c': 9,
        'd': 11,
        'e': 9,
        'f': 9,
        'g': 9,
        'h': 10,
        'i': 8,
        'j': 13,
        'k': 11,
        'l': 9,
        'm': 14,
        'n': 11,
        'o': 12,
        'p': 11,
        'q': 11,
        'r': 11,
        's': 9,
        't': 9,
        'u': 11,
        'v': 11,
        'w': 11,
        'x': 11,
        'y': 11,
        'z': 11,
        'A': 14,
        'B': 14,
        'C': 14,
        'D': 14,
        'E': 17,
        'F': 17,
        'G': 17,
        'H': 17,
        'I': 15,
        'J': 17,
        'K': 17,
        'L': 17,
        'M': 17,
        'N': 17,
        'O': 17,
        'P': 17,
        'Q': 23,
        'R': 14,
        'S': 13,
        'T': 15,
        'U': 20,
        'V': 20,
        'W': 20,
        'X': 20,
        'Y': 16,
        'Z': 20,
        '0': 14,
        '1': 12,
        '2': 15,
        '3': 14,
        '4': 15,
        '5': 14,
        '6': 14,
        '7': 14,
        '8': 12,
        '9': 14,
        '#': 16,
        '@': 16,
        ',': 6,
        '.': 6,
        "'": 4}
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
    
    
# initDict = loadSpacings('Allen')

            
            
