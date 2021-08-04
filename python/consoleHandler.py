# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 19:55:36 2021

@author: blah
"""

### The control line scripter ####



    
    
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
from delimSys import *

import fixedLists # code for fixed lists of char/paths for project 
import createProfile # code for accessing, modifying profiles 
import spacingHandler # code for profile spacing load and write 
import writeSVG # code for actually writing. 
import writeScripts


def introHandler():
    while True:
        print("###############################")
        print("Welcome to the Handwriting Console \n")
        print("Valid options are: \n")
        print("1. Create new profile or reInitialize profile \n")
        print("2. Assign Printing Task  \n")
        print("3. Exit \n")
        print("###############################")
        
        val = input("Enter the number of your selection: ") 
        if val == '1': 
            profileHandler()
        elif val == '2' :
            taskHandler()
        elif val == '3' :
            return None 
        else: 
            print("Invalid Selection. Try Again?   \n")

    
def profileHandler(): 
    print("###############################")
    print("Welcome to the Profile Handler \n")  
    print("We try to create a new Profile")
    val = input("Enter the new Profile Name. Preferably with No Spaces: ") 
    createProfile.createProfile(val)


def taskHandler(): 
    print("###############################")
    print("Welcome to the Task Handler")
    # going two levels up, past Python
    masterDir = Path(__file__).parents[1]

    # get into Profiles 
    profileDir = str(masterDir) + delim + 'Profiles' 
    print("here are the current list of profiles")
    for directory in os.listdir(profileDir):
        print(directory)
            
    profile = input("input profile to use: ")
    while profile not in os.listdir(profileDir):
        print('profile not in list. Try again?')
        profile = input("input profile to use: ")
    
    print('profile exists')
    
    if createProfile.profileProfile(profile) == False: 
        print('invalid profile, this profile is missing source files')
        return None 
    
    print('source files confirmed. loading profile')
    
    addressDict = spacingHandler.loadAddress(profile)
    
    print(addressDict)
    correct = input('Is the address input correct? y/n?: ')
    while correct not in ['y', 'n']:
        print('bad input')
        correct = input('Is the address input correct? y/n?: ')
    if correct == 'n':
        print('cancelling task, please edit profile')
        return None
    
    jobType = input("select task. envelope or postcard: ")
    while jobType not in ['envelope', 'postcard']:
        print('incorrect input')
        jobType = input("select task. envelope or postcard: ")
    
    reps = int(input("how many copies (up to 500): "))
    while reps <= 0 or reps > 500 or isinstance(reps, int) == False: 
        print('choose an integer in range') 
        reps = int(input("how many copies (up to 500): ")) 
    
    print('ready for tasks, time to adjust axidraw pen')
    
    ad = axidraw.AxiDraw() # Create class instance
    ad.plot_setup()        # Run setup without input file
    
    ad.moveto(0, 0)
    ad.plot_run
    ad.options.mode = "manual"
    ad.options.manual_cmd = "lower_pen"
    ad.plot_run()          # Execute the command
    
    input("After finished adjusting pen. Press any key to continue")
    
    ad.options.mode = "manual"
    ad.options.manual_cmd = "raise_pen"
    ad.plot_run()          # Execute the command
    
    input("Ready to start task. Load paper and press enter key to continue")
    if jobType == 'envelope':
        for i in range(reps):
            print('job count {}'.format(i+1))
            writeScripts.writeEnvelope(profile)
            input("press enter key to continue")
            
    if jobType == 'postcard':
        for i in range(reps):
            print('job rep: {}'.format(i+1))
            writeScripts.writePostcard(profile)
            input("press enter key to continue")
    print('task completed!')
        
if __name__ == "__main__":
   introHandler()
        
    
        
