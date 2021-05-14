# -*- coding: utf-8 -*-
"""
Created on Sun May  9 19:25:08 2021

@author: blah
"""
filename = 'C:/Users/blah/Desktop/AxiDraw/font/font1.svg'
with open(filename, 'r') as r:
  lines = r.read().split('\n')
  glyphs = [x for x in lines if '<glyph' in x]
  # for every glyph element in the file
  for i in range(0, len(glyphs)):
    with open(str(i + 1).rjust(3, '0') + '.svg', 'w') as w:
      w.write('<?xml version="1.0" standalone="no"?>\n')
      w.write('<svg width="1500px" height="1500px" version="1.1" xmlns="http://www.w3.org/2000/svg">\n')
      # replace 'glyph' with 'path' and flip vertically
      w.write(glyphs[i].replace('<glyph', '<path transform="scale(1, -1) translate(0, -1500)"') + '\n')
      w.write('</svg>')
      
      
      
import xml.etree.ElementTree as ET
tree = ET.parse(filename)
root = tree.getroot()



from collections import OrderedDict

def flatten_dict(d):
    def items():
        for key, value in d.items():
            if isinstance(value, dict):
                for subkey, subvalue in flatten_dict(value).items():
                    yield key + "." + subkey, subvalue
            else:
                yield key, value

    return OrderedDict(items())

import xmltodict

# Convert to dict
with open(filename, 'rb') as f:
    xml_content = xmltodict.parse(f)

# Flatten dict
flattened_xml = flatten_dict(xml_content)

# Print in desired format
for k,v in flattened_xml.items():
    print('{} = {}'.format(k,v))