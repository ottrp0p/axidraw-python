# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 11:27:31 2021

@author: blah
"""

# first some comments on how folders should be structured 
# profile folder for different profiles
# under profile "default" as the main one for now 
# one folder for originals
# the other folder for generations 

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

from addDim import * # this is custom code desgined to add dim headers
# getting our directories

def proliferate(profileName):
    # going two levels up, past Python
    masterDir = Path(__file__).parents[1]
    
    # get into Profiles 
    profileDir = str(masterDir) + '\\Profiles\\' + profileName 
    
    # check if it's valid
    if os.path.isdir(profileDir) == False: 
        # path doesn't exist 
        print('Invalid profile')
        return None 
    print('Confirmed: profile exists')
    
    originalsDir = profileDir + '\\Originals' 
    generationDir = profileDir + '\\Generation'
    
    folderList = fixedLists.folderList()
    
    
    
    # if somehow there aren't originals
    if os.path.isdir(originalsDir) == False: 
        print('Error. Profile does not have originals')
        return None
    print('Confirmed: originals top level folder exists')

        
    for path in folderList:
        if os.path.isdir(originalsDir + '\\' + path) == False: 
            print('Error, missing originals subfolder: {}'.format(path))
            return None
        if len(os.listdir(originalsDir + '\\' + path)) == 0: 
            print('Error, empty originals subfolder: {}'.format(path))
    print('Confirmed: originals subfolders exist and are nonempty') 
    
    
    # generate generation folders
    if os.path.isdir(generationDir) == False: 
        os.mkdir(generationDir)
    
    for path in folderList :
        if os.path.isdir(generationDir + '\\' + path) == False: 
            os.mkdir(generationDir + '\\' + path)
            
    print('Confirmed: generation folders exist') 
    
    # proceed to the main loop. 
    # for each path, OG -> gen run the shear loop
    for path in folderList: 
        OGPath = originalsDir + '\\' + path
        GenPath = generationDir + '\\' + path
        
        svgFiles = os.listdir(OGPath)
        counter = 0 
        shearNum = 10 
        
        for file in svgFiles: 
            # generically just use postcard dims 
            figure = svgutils.transform.SVGFigure(width="15.24cm", height ="10.16cm")
            svg = svgutils.transform.fromfile(OGPath + '\\' + file).getroot()
            print('got file: {}'.format(OGPath + '\\' + file))
            svg.scale(.10) # THIS MEANS YOU DO NOT NEED TO SCALE IN LATER STEPS
            for i in range(0, shearNum):
                # generically just use postcard dims 
                
                xSkew = -1 + 2/(shearNum-1)*i
                # print('skew: {}'.format(xSkew))
                svg.skew(xSkew, 0)
                # just use the skew...
                # we just need to guess the heigh value to the median of the letter 
                # more or less
            
                pixelVal = 60*math.tan(xSkew/360*2*math.pi) 
                # original magic # is 60 pixels
                if xSkew <= 0: 
                    pixelVal =abs(pixelVal)
                else: 
                    pixelVal = -abs(pixelVal)
            
                svg.moveto(pixelVal, 0)
                # 10/(num-1)*i seems to work for height? 
                # svg.scale(random.random()*.03 + .97)
                # svg.rotate(random.random()*5-10)
                figure.append(svg)
                figure.save(GenPath + '\\' + path + str(counter) + '.svg')
                print('saved file: {}'.format(GenPath + '\\' +  path + str(counter) + '.svg'))
                addDim(GenPath + '\\' + path + str(counter) + '.svg') # add header dims
                counter +=1 
            

proliferate('Allen')


        
    
    
  

    
    