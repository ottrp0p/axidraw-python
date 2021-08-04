#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 14:11:47 2021

@author: allenyu
"""
import platform 

if platform.system() == 'Windows':
    delim = '\\'
else:
    delim = '/'