# -*- coding: utf-8 -*-
"""
Created on Thu May 13 15:58:46 2021

@author: blah
"""

# font Proliferate script 
from axidrawinternal import axidraw
import os 
import svgutils
import sys
import re
import string
import random
import math 

from addDim import * 
# getting our directories
dir_path = os.path.dirname(os.path.realpath(__file__))
font_path = dir_path + '\\font2\\'
generation_path = dir_path + '\\generation\\'

baseFile = font_path + 'm.svg' # this is what we're working with

num = 11
for i in range(1, num):
    figure = svgutils.transform.SVGFigure(width="15.24cm", height ="10.16cm")
    svg = svgutils.transform.fromfile(baseFile).getroot()
    svg.scale(.10)
    
    xSkew = -10 + 20/(num-1)*i
    print('skew: {}'.format(xSkew))
    svg.skew(xSkew, 0)
    # just use the skew...
    # we just need to guess the heigh value to the median of the letter 
    # more or less

    pixelVal = 60*math.tan(xSkew/360*2*math.pi) 
    if xSkew <= 0: 
        pixelVal =abs(pixelVal)
    else: 
        pixelVal = -abs(pixelVal)

    svg.moveto(pixelVal, 0)
    # 10/(num-1)*i seems to work for height? 
    # svg.scale(random.random()*.03 + .97)
    # svg.rotate(random.random()*5-10)
    figure.append(svg)
    figure.save(generation_path + 'a' + str(i) + '.svg')
    addDim(generation_path + 'a' + str(i) + '.svg')


# try to merge all 11 a's?
figure = svgutils.transform.SVGFigure(width="15.24cm", height ="10.16cm")
xPos = 0
yPos = 0 
scaleFactor = 1
for i in range(1, 11):
    if i in [11, 21]:
        xPos = 0 
        yPos = yPos + 40
    svg = svgutils.transform.fromfile(generation_path + 'a' + str(i) +'.svg').getroot()
    svg.moveto(xPos, yPos, scaleFactor)
    figure.append(svg)
    xPos = xPos + 30


figure.save(generation_path + 'mergeTest.svg')
addDim(generation_path + 'mergeTest.svg')
ad = axidraw.AxiDraw()    
ad.plot_setup(generation_path + 'mergeTest.svg')
ad.plot_run()