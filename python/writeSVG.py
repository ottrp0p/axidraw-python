# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 18:18:18 2021

@author: blah
"""

# originalsTest 

# we write out all of the originals
# assuming we are in a landscale A4 paper 

# note you have to scale by .15 here 

from pathlib import Path

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
import createProfile # code for accessing, modifying profiles 
import spacingHandler # code for profile spacing load and write 
from delimSys import *

def writeSVG(xStart, yStart, letter, profile, lineList):
    
    scaleFactor = 1 # using the proliferated ones, already scaled (I think...)
    # takes starting position and set of lines
    # you can think of chunking blocks of texts here. 
    
    # passes the profile character set and spacings to use. Will load from 
    # the generation process. 
    
    # letter parameter checks for 3 types. Lets width and height appropriately 
    
    
    # set the length width params
    if letter == 'Index':
        letterWidth = "15.24cm"
        letterHeight = "10.16cm"
    elif letter == 'Envelope':
        letterWidth = "24.13cm"
        letterHeight = "10.47cm"        
    elif letter == 'Paper': 
        # assumed to be A4 here
        letterWidth = "29.7cm"
        letterHeight = "21.0cm"   
    
    #
    
    ### Build some mappings, and profile paths ###
    # char map
    charMap = fixedLists.charMapping()
    

    # build some directories
    masterDir = Path(__file__).parents[1]    
    profileDir = str(masterDir) + delim + 'Profiles' + delim + profile 
    if os.path.isdir(profileDir) == False: 
        print('Profile does not exist')
        return None 
    
    GenDir = profileDir + delim + 'Generation'
    
        
    # build the spacing dict
    spacingDict = spacingHandler.loadSpacings(profile)
    # print('spacingDict: ')
    # print(spacingDict)
    
    # folder list gen
    folderList = fixedLists.folderList()
    
    
    ad = axidraw.AxiDraw()
    figure = svgutils.transform.SVGFigure(width=letterWidth, height = letterHeight)
        
    # use start as origin points 
    xPos = xStart 
    yPos = yStart
    
    for line in lineList: 
        charList = list(line)
        for char in charList: 
            # check if exist?
            if char in spacingDict:
                charDir = GenDir + delim + charMap[char] + '-' + char + '-'
                if os.path.isdir(charDir):
                    fileList = os.listdir(charDir)
                    if len(fileList) == 0: 
                        print('no original files for character: {0} in profile {1}'.format(char, profile))
                        return None 
                    # supposing we do have files, get the list of files. random into one of them
                    charFileList = os.listdir(charDir)
                    charPath = charDir + delim + charFileList[random.randint(0, len(charFileList)-1)]
                    svg = svgutils.transform.fromfile(charPath).getroot()
                    svg.moveto(xPos + random.randint(-20, 0)/40, yPos + random.randint(-20, 20)/40, scaleFactor)
                    figure.append(svg)
                    xPos = xPos + spacingDict[char]  ##### ADD NOISE HERE #####
            else: 
                xPos = xPos + 8 + random.randint(-20, 0)/20  ##### ADD NOISE HERE #####
        
        xPos = xStart + random.randint(-20, 20)/10
        yPos = yPos + 30 + random.randint(-20, 0)/20    # new line  ###### ADD NOISE HERE ####
    figure.save('printTemp.svg')
    addDim('printTemp.svg', letter)  
    ad.plot_setup('printTemp.svg')
    ad.options.speed_pendown = 115
    ad.options.speed_penup = 115
    ad.options.accel = 100
    ad.options.pen_rate_lower = 100
    ad.options.pen_rate_raise = 100
    ad.plot_run()
                
# tempDict = spacingHandler.loadSpacings('Zain')
# print(tempDict)

# changes = {'e': 12, 
#            'w' : 13, 
#            'f': 10, 
#            'n': 10, 
#            'u': 10,
#            'q': 9, 
#            'i': 7, 
#            'r': 9, 
#            'l': 7, 
#            't': 7, 
#            'm': 12,
#            'o': 10, 
#            'v': 9, 
#            'g': 11, 
#            'a': 12, 
#            'k': 10, 
#            '0': 12, 
#            '1': 11, 
#            '2': 14, 
#            '3': 12, 
#            '6': 12, 
#            '7': 13, 
#            '5': 12,
#            'J': 14}
           
           

# spacingHandler.changeSpacings('Zain', changes)
# writeSVG(0, 0, 'Paper', 'Zain', 
#           ['quick brown fox jumped over the lazy dog', 
#           'quick brown fox jumped over the lazy dog',
#           'quick brown fox jumped over the lazy dog', 
#           'Jenny now that I got your number', 
#           'I got to make you mine', 
#           '8675309', 
#           '8675309'])