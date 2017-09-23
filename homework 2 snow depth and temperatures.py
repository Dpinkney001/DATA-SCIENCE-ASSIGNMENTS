# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 18:52:18 2017

@author: Duvall Pinkney
"""
import numpy as np
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
        

def main():
    prefix = "http://www.wunderground.com/history/airport/KLGA/"
    middle = "/"
    suffix = "/01/DailyHistory"
    days = []
    minVals = []
    #years = []
    year = 2017
    day = 1
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
    
    
    output = getSnowDepth(url)
    """
    snowDepthArr = []
    item = 1
    for item in range(1, 32):
        snowDepthArr[item] += output[item]
        item += 1
    return snowDepthArr    
    #N = 50
    """
    colors = 'b'
    area = np.pi * (15 * np.random.rand(output))**2 
    plt.title("Daily NYC Temps for Jan 2017 and Snow Depth")
    plt.xlabel("Days")
    plt.ylabel("Temperatures")
    plt.scatter(days, minVals, s=area, c=colors, alpha=0.5)
    plt.show()
    
    
    print(getSnowDepth(url))
    #create histogram of max temps for march 31
    #xAxis = range(29)
    #yAxis = range(101)
    #plt.hist(maxVals)
    #plt.axis([1986, 2017, 0, 101])
    #plt.title("Histogram of Max Temps on March 31 Since 1986")
    #plt.xlabel("Temperatures")
    #plt.show()
    
    #print("The list of max values are: ", maxVals)
    
    """
    print("The list of minumum values follows:)
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
    print("End of min values");
    """     
    
main()    


