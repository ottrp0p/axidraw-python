# -*- coding: utf-8 -*-
"""
Created on Sun May  9 22:38:34 2021

@author: blah
"""

# filename = 'C:/Users/blah/Desktop/AxiDraw/font/font1.svg'  
# with open(filename, 'r') as r:
#   lines = r.read().split('\n')
#   glyphs = [x for x in lines if '<glyph' in x]
#   # for every glyph element in the file
#   for i in range(0, len(glyphs)):
#     with open(str(i + 1).rjust(3, '0') + '.svg', 'w') as w:
#       w.write('<?xml version="1.0" standalone="no"?>\n')
#       w.write('<svg width="1500px" height="1500px" version="1.1" xmlns="http://www.w3.org/2000/svg">\n')
#       # replace 'glyph' with 'path' and flip vertically
#       w.write(glyphs[i].replace('<glyph', '<path transform="scale(1, -1) translate(0, -1500)"') + '\n')
#       w.write('</svg>')

def addDim(filename, letter = 'Index'):
    svg =  open(filename, 'r') 
    text = svg.read()
    if letter == 'Index':
        stringToAdd = ' width = "6in" height = "4in"'
    elif letter == 'Envelope': 
        stringToAdd = ' width = "9.5in" height = "4.125in"'   
    elif letter == 'Paper': 
        stringToAdd = ' width = "11in" height = "9in"'   
    else: 
        print('unrecognized letter option')
        
    svgIndex = text.find('svg')
    newSVG = text[:(svgIndex + 3)]+ stringToAdd + text[(svgIndex + 3):]
    
    with open(filename, 'w') as svg: 
        svg.write(newSVG)
    return None