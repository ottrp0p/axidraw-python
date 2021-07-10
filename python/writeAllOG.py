# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 18:37:33 2021

@author: blah
"""

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
import getChar # code for turning files back into their character via folder 


def writeAllOG(xStart, yStart, scaleFactor, profile, letter = 'Index'):
    # takes starting position and set of lines
    # you can think of chunking blocks of texts here. 
    
    # passes the profile character set and spacings to use. Will load from 
    # the generation process. 
    
    # letter parameter checks for 3 types. Lets width and height appropriately 
    
    
    # set the length width params
    if letter == 'Index':
        letterWidth = "15.24cm"
        widthNum = 15.24
        letterHeight = "10.16cm"
        heightNum = 10.16
    elif letter == 'Envelope':
        letterWidth = "24.13cm"
        widthNum = 24.13
        letterHeight = "10.47cm"    
        heightNum = 10.47
    elif letter == 'Paper': 
        # assumed to be A4 here
        letterWidth = "29.7cm"
        widthNum = 29.7
        letterHeight = "21.0cm"   
        heightNum = 21.0
    
    # VERY IMPORTANT
    # PRE GENERATION, STILL HAVE TO USE .15 SCALE
    scaleFactor = '.12'
    
    ### Build some mappings, and profile paths ###
    # char map
    charMap = fixedLists.charMapping()
    
    # build the spacing dict
    spacingDict = spacingHandler.loadSpacings(profile)
    

    # build some directories
    masterDir = Path(__file__).parents[1]    
    profileDir = str(masterDir) + '\\Profiles' + '\\' + profile 
    if os.path.isdir(profileDir) == False: 
        print('Profile does not exist')
        return None 
    
    OGDir = profileDir + '\\' + 'Originals'
    
    # folder list gen
    folderList = fixedLists.folderList()
    
    
    ad = axidraw.AxiDraw()
    figure = svgutils.transform.SVGFigure(width=letterWidth, height = letterHeight)
        
    # use start as origin points 
    xPos = xStart 
    yPos = yStart
    
    OGFileDirList = []
    for folder in folderList: 
        charDir = OGDir + '\\' + folder
        tempFiles = os.listdir(charDir) 
        for file in tempFiles: 
            OGFileDirList.append(charDir + '\\' + file)
    
    
    for filePath in OGFileDirList: 

            # supposing we do have files, pi
            svg = svgutils.transform.fromfile(filePath).getroot()
            svg.moveto(xPos, yPos, scaleFactor)
            figure.append(svg)
            char = getChar.getCharFromPath(filePath)
            if char in spacingDict:
                xPos = xPos + spacingDict[char]
            else: 
                xPos = xPos + 20 ##### ADD NOISE HERE #####
                
            if xPos > 720:
                xPos = xStart
                yPos = yPos + 50 
                if yPos > 360: # into the margins
                    break 
            
        
    figure.save('printTemp.svg')
    addDim('printTemp.svg', 'Paper')
    ad.plot_setup('printTemp.svg')
    ad.options.speed_pendown = 115
    ad.options.speed_penup = 115
    ad.options.accel = 100
    ad.options.pen_rate_lower = 100
    ad.options.pen_rate_raise = 100
    ad.plot_run()
                
    
    
# changes = {
#     'f': 13,
#     'i' : 13,
#     'j' : 13,
#     'l' : 15,
#     'm' : 24,
#     's' : 13,
#     'n' : 15,
#     'x' : 15,
#     'B' : 20,
#     'E' : 22,
#     'F' : 22,
#     'J' : 22,
#     'K' : 25,
#     'L' : 22,
#     'M' : 24,
#     'N' : 22,
#     'S' : 20, 
#     'Q' : 28,
#     'U' : 28,
#     'V' : 28,
#     'W' : 28,
#     'X' : 20, 
#     'Y' : 24, 
#     'Z' : 24,
#     '@' : 22, 
#     '#' : 22
#     }
    
# spacingHandler.changeSpacings('Allen', changes)
    
changes = {
    '0' : 16,
    '2' : 15 ,
    '3' : 15,
    '4' : 15, 
    '5' : 14 , 
    '6' : 14, 
    '3' : 14 , 
    '7' : 14, 
    '9' : 14 , 
    '#' : 16, 
    '@' : 16, 
    'i' : 10, 
    'j' : 13, 
    'l' : 13, 
    'm' : 16, 
    's' : 11, 
    'A' : 14,
    'B' : 14, 
    'D' : 14, 
    'E' : 17, 
    'F' : 17, 
    'G' : 17, 
    'H' : 17, 
    'I' : 17, 
    'J' : 17, 
    'K' : 17, 
    'L' : 17, 
    'M' : 17, 
    'N' : 17, 
    'O' : 17, 
    'P' : 17, 
    'Q' : 23, 
    'R' : 14, 
    'S' : 15, 
    'T' : 16, 
    'U' : 20, 
    'V' : 20, 
    'W' : 20, 
    'X' : 20, 
    'Y' : 20, 
    'Z' : 20

}
    
spacingHandler.changeSpacings('Allen', changes)

    
writeAllOG(40, 40, '.12', 'Allen', letter = 'Paper')
