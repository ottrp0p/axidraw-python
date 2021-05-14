# -*- coding: utf-8 -*-
"""
Created on Sun May  9 18:19:38 2021

@author: blah
"""

import os 

         
import svgutils.transform as sg
import sys
import re


os.chdir('C:/Users/blah/Desktop/AxiDraw/pictures/')
         
logo = sg.fromfile('testA.svg')
background = sg.fromfile('testB.svg')

def convert_to_pixels(measurement):
    value = float(re.search(r'[0-9\.]+', measurement).group())
    if measurement.endswith("px"):
        return value
    elif measurement.endswith("mm"):
        return value * 3.7795275591
    elif measurement.endswith(""):
        # just assume its px
        return value
    else:
        # unit not supported
        print('unsupported')
        return value

width = convert_to_pixels(background.get_size()[0])
print('background with: {}'.format(background.get_size()[0]))
height = convert_to_pixels(background.get_size()[1])
print('background with: {}'.format(background.get_size()[1]))

logo_width = convert_to_pixels(logo.get_size()[0])
logo_height = convert_to_pixels(logo.get_size()[1])

root = logo.getroot()

# Top Left
# root.moveto(1, 1)

# Top Right
root.moveto(1, 0)

# Bottom Left
#root.moveto(1, height - logo_height - 1)

# Bottom Right
#root.moveto(width - logo_width - 1, height - logo_height - 1)

background.append([root])
os.chdir('C:/Users/blah/Desktop/AxiDraw/pictures')

background.save('output.svg')

### REMEMBER 