# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 19:58:48 2017

@author: Duvall
"""
import matplotlib.pyplot as plt
import urllib
import urllib.request
import urllib.error
import urllib.parse
import re

#get temperature data from webpage
def getTempFromWeb(kind,url):
    page = urllib.request.urlopen(url)
    lines = page.readlines()
    for i in range(len(lines)):
        if lines[i].decode("utf8").find(kind+" Temperature") >= 0:
            m = i
            break
    searchObj = re.search('\d+', lines[m+2].decode("utf8"))
    return int(searchObj.group(0))

#get snow depth data from webpage
def getSnowDepth(url):
    page2 = urllib.request.urlopen(url)
    lines2 = page2.readlines()
    for j in range(len(lines2)):
        if lines2[j].decode("utf8").find("Snow Depth"):
            m2 = j
            break
        searchObj2 = re.search('\d+', lines2[m2+2].decode("utf8"))
        if searchObj2 == None:
            return int(searchObj2.group(0))
        else:
            return searchObj2