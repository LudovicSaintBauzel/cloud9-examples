#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 12:05:54 2020

@author: ludo

"""
import os
def checkESSID(essid_str):
    res_str=os.popen("iwconfig wlan0").read()
    return essid_str in res_str

if checkESSID("Poupsland"):
    print("Victoire!")
else:
    print("Défaite!")
