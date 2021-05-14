# -*- coding: utf-8 -*-
"""
Created on Sun May  9 20:38:23 2021

@author: blah
"""

import xml.etree.ElementTree as ET
filename = 'scaleTest.svg'
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
    
    



# m 334,992 1,-1 1,-2 1,-3 1,-5 
# v -7 -7 -10 -15 
# l -1,-13 -1,-13 -1,-13 
# v -16 
# l -1,-16 
# v -15 -18 
# l -1,-14 
# v -13 
# l -1,-13 
# v -12 
# l -1,-10 -1,-10 -1,-7 -1,-7 -1,-6 -1,-6 -1,-3 
# v -1 -1 1 1 2 3 4 3 
# l 1,6 1,6 1,8 1,7 1,7 1,7 2,6 2,7 2,6 2,6 2,6 3,6 3,4 4,5 4,3 4,3 5,1 5,1 6,-2 7,-3 7,-5 7,-6 7,-7 6,-9 4,-9 3,-8 1,-9 -1,-8 -2,-9 -4,-8 -6,-8 -7,-7 -8,-5 -9,-3 
# h -10 
# l -11,3 -11,5 -10,10



