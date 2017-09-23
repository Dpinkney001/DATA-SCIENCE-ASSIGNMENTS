# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 02:15:38 2017

@author: Duvallpinkney
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
 



def averageVal(minVals):
    # compute the average temp from the 31 days
    total = 0
    average = 0.0
    item = 0
    for item in range(len(minVals)):
        total = total + minVals[item]
        item += 1
    #print("The sum is: " + total)    
    average = total / len(minVals)
    #print(" the average for the month of Jan2017 is: " + average)
    
    return average
    
    
def main():
    prefix = "http://www.wunderground.com/history/airport/KLGA/2017/01/"
    suffix = "/DailyHistory"
    days = []
    minVals = []
    #years = []
    year = 2017
    day = 1
    for day in range(1,32):
        days.append(day)
        url = prefix+str(day)+suffix
        M2 = getTempFromWeb("Min",url)
        minVals.append(M2)
        print(day, M2)
    plt.plot(days, minVals, color='r', label="Minimaltemp")
    plt.title("Daily NYC Temps for Jan 2017")
    plt.xlabel('Day')
    plt.ylabel('Degrees')
    plt.legend(loc = 2,fontsize = 'x-small')
    plt.show()
    
   
    #create scatterplots for each tent
    def scale(minVals, plt, lab,col):
        #takes the minimum values array and creates a scatter plot of
        # of the percentage change with respect to the avarage value
        baseNum = averageVal(minVals)
        scaled = [n*100/baseNum-100 for n in minVals]
        plt.scatter(days, scaled, label=lab, c = col, s=75)
        #j = 0
        #for j in range(32):
        #    scale(minVals[j],plt, str(days), "blue")
        #   j += 1
        
    #compute the average
    #scale the average with the daily min values
    #set up chart
    
    scale(minVals, plt, "days", 'green')
    plt.title("Daily temperature compared with average temp for the month")
    plt.xlabel('Days')
    plt.ylabel('Percent change')
    plt.legend()
    plt.show()
    
main()    
