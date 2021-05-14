# -*- coding: utf-8 -*-
"""
Created on Thu May 13 14:06:35 2021

@author: blah
"""

import os 

from addDim import *  
import svgutils
import sys
import re
import string
from axidrawinternal import axidraw

ad = axidraw.AxiDraw()             # Create class instance




# getting our directories
dir_path = os.path.dirname(os.path.realpath(__file__))
font_path = dir_path + '\\font2\\'


# creating the spacing dictionary 

lcAlpha = list(string.ascii_lowercase)
spacingDict = {}
spacingDict[' '] = 12 

for char in lcAlpha:
    if char in ['f', 'i', 'l']:
        spacingDict[char] = 8 
        
    elif char in ['t', 's', 'c']:
        spacingDict[char] = 12
    
    elif char in ['m']:
        spacingDict[char] = 27
        
    elif char in ['w', 'y']:
        spacingDict[char] = 23
        
    else: 
        spacingDict[char] = 18
        

# # aside, lets figure out what scaling first 
# ad = axidraw.AxiDraw()             # Create class instance

# try:    
#     file = font_path + 'a.svg'
#     ad.plot_setup(file)    # Parse the input file
# except:
#     print('error loading')

# ad.options.speed_pendown = 50 # Set maximum pen-down speed to 50%
# ad.plot_run()   # plot the document    


def writeSVG(xStart, yStart, lineList, scaleFactor, spacing = False, indexCard = True):
    # spacing option hard codes what the spacing is. Used for re-testing later
    # else it uses the spacingDict imported dictionary
    
    # indexCard boolean determines whether indexcard or envelope settings
    # assuming #10 envelo

    ad = axidraw.AxiDraw()
    if indexCard == True: 
        figure = svgutils.transform.SVGFigure(width="15.24cm", height ="10.16cm")
    else: 
        # envelope #10
        figure = svgutils.transform.SVGFigure(width="24.13cm", height ="10.47cm")
        
    # use start as origin points 
    xPos = xStart 
    yPos = yStart
    
    for line in lineList: 
        charList = list(line)
        for char in charList: 
            # check if exist?
            print(char)
            if os.path.exists(font_path + char + '.svg'):
                svg = svgutils.transform.fromfile(font_path + char +'.svg').getroot()
                svg.moveto(xPos, yPos, scaleFactor)
                figure.append(svg)
            if spacing == False and char in spacingDict:
                xPos = xPos + spacingDict[char]
            else: 
                xPos = xPos + 20
        
        xPos = xStart
        yPos = yPos + 40 # new line
    figure.save('printTemp.svg')
    addDim('printTemp.svg')
    ad.plot_setup('printTemp.svg')
    ad.plot_run()
                
writeSVG(0, 0, ['where were u', 'when netflix', 'was kill', 'stacy btfo'], '.15', spacing=False, indexCard = True)

# ad = axidraw.AxiDraw()             # Create class instance
# # originalSVG = svgutils.compose.SVG('testA.svg')
# scaleFactor = .15
# figure = svgutils.transform.SVGFigure(width="15.24cm", height ="10.16cm")
# yPos = 0 
# xPos = 0



# # alphabet = list(string.ascii_lowercase)

# # for i in range(len(alphabet)):
# #     # 4 rows 7, 7, 6, 6
# #     if i == 7: 
# #         # 8th term, 
# #         yPos = yPos + 40 
# #         xPos = 0
# #     if i == 14:
# #         yPos = yPos + 40
# #         xPos = 0 
# #     if i == 20:
# #         yPos = yPos + 40
# #         xPos = 0
# #     svg = svgutils.transform.fromfile(font_path + alphabet[i] +'.svg').getroot()
# #     svg.moveto(xPos, yPos, scaleFactor)
# #     xPos = xPos + 20
# #     figure.append(svg)
    
    

# toWrite = 'mn'

# toWrite = list(toWrite)

# for i in range(len(toWrite)):
#     if toWrite[i] != ' ':
#         svg = svgutils.transform.fromfile(font_path + toWrite[i] +'.svg').getroot()
#         svg.moveto(xPos, yPos, scaleFactor)
#         figure.append(svg)
#     xPos = xPos + 30


       

# ad.plot_setup('scaleTest.svg')
