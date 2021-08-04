# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 21:39:45 2021

@author: blah
"""

#writeScript 

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
import writeSVG # code for actually writing. 
from delimSys import *

def writePostcard(profile):
    addressDict = spacingHandler.loadAddress(profile)
    
    block1 = [addressDict['firstName']+' ' +  addressDict['lastName'], 
         addressDict['emailAddress'], 
         addressDict['address1'],  
         addressDict['address2']]
    block2 = ['I wish to receive Sweeps Coins to participate'
      ,'in the sweepstakes promotions offered by Chumba'
      ,'Casino. By submitting this request, I hereby'
      ,'declare that I have read, understood, and'
      ,"agree to be bound by Chumba Casino's Terms"
      ,'and Conditions and sweeps rules.']
    
    writeSVG.writeSVG(20, 20, 'Index', profile, block1)
    writeSVG.writeSVG(20, 155, 'Index', profile, block2)
    
def writeEnvelope(profile): 
    addressDict = spacingHandler.loadAddress(profile)
    block1 = ['Sweepstakes Credits',
         addressDict['address1'],  
         addressDict['address2']]
    block2 = ['VGW Games Limited', 
                'Chumba Casino Sweepstakes Department', 
                'PO Box #8486', 
                'Portsmouth, NH 03801']
    writeSVG.writeSVG(20, 20, 'Envelope', profile, block1)
    writeSVG.writeSVG(300, 155, 'Envelope', profile, block2)
    

# myDict= spacingHandler.loadSpacings('Allen')
# changes = {}
# for char in list(string.ascii_lowercase): 
#     if myDict[char] == 12:
#         changes[char] = 11

# changes['I'] = 15
# changes['Y'] = 16
# changes['S'] = 13
# changes['T'] = 15
# changes['c'] = 9
# changes['i'] = 8
# changes['f'] = 9
# changes['s'] = 9
# changes['l'] = 9
# changes['e'] = 9
# changes['g'] = 9
# changes['m'] = 14
# changes['o'] = 12
# changes['t'] = 9
# changes[','] = 6
# changes['.'] = 6
# changes["'"] = 4
# changes['h'] = 10



# spacingHandler.changeSpacings('Allen', changes)


# writePostCard('Allen', 
#               ['Allen Yu', 'amengyangyu@gmail.com', '1375 Ruby Sky Court', 'Henderson, NV 89052'], 
#               ['I wish to receive Sweeps Coins to participate'
#                 ,'in the sweepstakes promotions offered by Chumba'
#                 ,'Casino. By submitting this request, I hereby'
#                 ,'declare that I have read, understood, and'
#                 ,"agree to be bound by Chumba Casino's Terms"
#                 ,'and Conditions and sweeps rules.'])


# writeEnvelope('Allen', 
#               ['Sweepstakes Credits', 
#                 '1375 Ruby Sky Court', 
#                 'Henderson, NV 89052'], 
              # ['VGW Games Limited', 
              #   'Chumba Casino Sweepstakes Department', 
              #   'PO Box #8486', 
              #   'Portsmouth, NH 03801'])



# ad = axidraw.AxiDraw()

# ad.plot_setup()
# ad.options.mode = "toggle"
# ad.plot_run()

