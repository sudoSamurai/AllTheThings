#!/usr/bin/env python

"""
Format of JSON file:
name:
Name of the package
description:
Short description of the package
brewName:
name used in "brew install"
caskName:
name used in "brew cask install"
yumName:
name used in "yum" or "dnf"
aptName:
name used in "apt get"
gitName:
user and repo name for github projects
pipName:
name used in "pip install"
flatpakName:
Not sure how to support this yet.  Maybe grab from flathub?
snapName:
Not sure how to support this yet
appimageName:
Probably a URL to download the appimage.
tags:
For future use.  Idea is to be able to specify "work" tag or "personal" tag
to determine if some packages get installed (like games vs work only tools)

### TODO ###

Functions for:
Add packages
Remove packages
List packages
Install packages
Uninstall packages?
check OS
check Version
check installed tools (is homebrew installed, etc...)

"""

import getopt
import os
import sys
import json

# Defaults
configFile="$HOME/.config/packageTool/config"
dataFile="$HOME/.config/packageTool/data.json"

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hi:o:"





if sys.argv[1] == null:
    print "NO ARGUMENTS"
else:
    print "sys.argv[1]"

# What am I running on?
def getOsDetails():
    return


# Load JSON into a python dict
def loadDataFromFile():
    with open('data.json') as jsonFile:
        parsedInput = json.load(jsonFile)

# get packages
packageList = parsedInput['packages']
for p in packageList:
    # if 'aptName' in p:
        # print(p)
        print(p['appName'])
        # print(p['appNotes'])
        # print(p['aptName'])

packageList.append({'appName':'blah', 'appNotes':'This is a thing','aptName':'blah'})
packageList.sort(key='appName')

print("")

for p in packageList:
    print(p['appName'])

# for p in packageList:
    #     if 'aptName' in p:
        #         print(p['name'])

def writeJson():
    with open('datadump.json', 'w') as outfile:
        json.dump(parsedInput, outfile, indent=2, sort_keys=True)
    return


### Interface ###
