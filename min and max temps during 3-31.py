# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 18:52:18 2017

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
    suffix = "/31/03/DailyHistory"
    years = []
    maxVals = []
    for year in range(1991,2017):
        years.append(year)
        url = prefix+str(year)+suffix
        M = getTempFromWeb("Max",url)
        maxVals.append(M)
        print(year, M)
    plt.plot(years, maxVals, color='r', label="Maxtemp")
    plt.title("NYC Temps for March 31")
    plt.xlabel('Years')
    plt.ylabel('Degrees')
    plt.legend(loc = 2,fontsize = 'x-small')
    plt.show()
    
    #create histogram of max temps for march 31
    #xAxis = range(29)
    #yAxis = range(101)
    plt.hist(maxVals)
    #plt.axis([1986, 2017, 0, 101])
    plt.title("Histogram of Max Temps on March 31 Since 1986")
    plt.xlabel("Temperatures")
    plt.show()
    
    print("The list of max values are: ", maxVals)
    
    #plot of mininum temps
    years = []
    minVals = []
    for year in range(1991,2017):
        years.append(year)
        url = prefix+str(year)+suffix
        Min = getTempFromWeb("Min",url)
        minVals.append(Min)
        print(year, Min)
    
    plt.plot(years, minVals, color='r', label="Mininumtemp")
    plt.title("NYC Temps for March 31")
    plt.xlabel('Years')
    plt.ylabel('Degrees')
    plt.legend(loc = 2,fontsize = 'x-small')
    plt.show()
    
    print("The list of min values are: ", minVals)
    
    plt.hist(minVals)
    #plt.axis([1986, 2017, 0, 101])
    plt.title("Histogram of Min Temps on March 31 Since 1986")
    plt.xlabel("Temperatures")
    plt.show()
    
main()    


