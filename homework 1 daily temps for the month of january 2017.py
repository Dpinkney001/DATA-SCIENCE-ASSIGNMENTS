# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 00:23:27 2017

@author: Duvall Pinkney
"""

import matplotlib.pyplot as plt
import urllib
import urllib.request
import urllib.error
import urllib.parse
import re

def getTempFromWeb(kind,url):
     page = urllib.request.urlopen(url)
     lines = page.readlines()
     for i in range(len(lines)):
          if lines[i].decode("utf8").find(kind+" Temperature") >= 0:
               m = i
               break
     searchObj = re.search('\d+', lines[m+2].decode("utf8"))
     return int(searchObj.group(0))
 
    
    
    
def main():
    prefix = "http://www.wunderground.com/history/airport/KLGA/"
    middle = "/"
    suffix = "/01/DailyHistory"
    days = []
    minVals = []
    #years = []
    year = 2017
    for day in range(1,32):
        days.append(day)
        url = prefix+str(year)+middle+str(day)+suffix
        M2 = getTempFromWeb("Min",url)
        minVals.append(M2)
        print(day, M2)
    plt.plot(days, minVals, color='r', label="Minimaltemp")
    plt.title("Daily NYC Temps for Jan 2017")
    plt.xlabel('Day')
    plt.ylabel('Degrees')
    plt.legend(loc = 2,fontsize = 'x-small')
    plt.show()


main()    