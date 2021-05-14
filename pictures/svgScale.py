# -*- coding: utf-8 -*-
"""
Created on Sun May  9 18:19:38 2021

@author: blah
"""

import os 

         
import svgutils
import sys
import re
from addDim import * 

os.chdir('C:/Users/blah/Desktop/AxiDraw/pictures/')
         

# originalSVG = svgutils.compose.SVG('testA.svg')
scaleFactor = .15
figure = svgutils.transform.SVGFigure(width="15.24cm", height ="10.16cm")

filename = ('testA.svg', 'testB.svg', 'testA.svg', 'testB.svg')
for i in range(4):
   svg = svgutils.transform.fromfile(filename[i]).getroot()
   svg.moveto(0+i*20, 0, scaleFactor)
   svg.rotate(-20 + 10*i)
   svg.skew(10, 10)
   figure.append(svg)


figure.save('scaleTest.svg')
addDim('scaleTest.svg')