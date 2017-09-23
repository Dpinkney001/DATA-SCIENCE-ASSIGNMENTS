# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 20:05:05 2017

@author: Duvall Pinkney
"""
"""
For the January minimum temperature data, compute and display the running 
average of the temperatures over the previous 5 days. That is, you display 
the average temperature over the previous 5 days for each day (if all exist,
 if not use as many as do exist). 
For example, if the temperatures were 10,20,10,20,15,35,30
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
 
#function that takes the average min values    
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


#function that takes the array of data for temps and the index day and
#returns the ave of the 5 previous or the previous days up to 5 and no less than
# 1
def previousfiveDayAve(minVals, index):
    Ave = 0.0
    tempTotal = 0
    if (index == 0):
        return minVals[0]
    if (index == 1):
        print("the temperatures being averaged together are: " 
              + str(minVals[0]) + " and " + str(minVals[1]))
        tempTotal = minVals[0] + minVals[1]
        Ave = tempTotal / 2
        print(" the average of the temperatures are: "+ str(Ave))
        return (minVals[0] + minVals[1]) / 2
    
    elif (index == 2):
        print("the temperatures being averaged together are: " 
              + str(minVals[0]) + ", " + str(minVals[1]) + "  " +
                   str(minVals[2]))
        tempTotal = minVals[0] + minVals[1] + minVals[2]
        Ave = tempTotal / 3
        print(" the average of the temperatures are: "+ str(Ave))
        return (minVals[0] + minVals[1] + minVals[2]) / 3
    
    elif (index == 3):
        print("the temperatures being averaged together are: " 
              + str(minVals[0]) + "  " + str(minVals[1]) +
                   "  " + str(minVals[2]) + "  " + str(minVals[3]))
        tempTotal = minVals[0] + minVals[1] + minVals[2] + minVals[3]
        Ave = tempTotal / 4
        print(" the average of the temperatures are: "+ str(Ave))
        return (minVals[0] + minVals[1] + minVals[2] + minVals[3]) / 4
    
    elif (index == 4):
        print("the temperatures being averaged together are: " 
              + str(minVals[0]) + "  " + str(minVals[1])+
                   "  " + str(minVals[2]) + "  " +  str(minVals[3]) +
                   "  " + str(minVals[4]))
        tempTotal = minVals[0] + minVals[1] + minVals[2] + minVals[3] + minVals[4]
        Ave = tempTotal / 5
        print(" the average of the temperatures are: "+ str(Ave))
        return (minVals[0] + minVals[1] + minVals[2] + minVals[3] + minVals[4])/ 5
    
    elif (index > 4):
        dayCounter = index
        totalOfTemps = 0
        fivedayAve = 0.0
 #       for dayCounter in range(index,32):
        
        totalOfTemps  = minVals[dayCounter] + minVals[dayCounter - 4] + minVals[dayCounter - 3] + minVals[dayCounter - 2] + minVals[dayCounter - 1]
            
        print("The temps added together are: " + "  " + 
                  str(minVals[dayCounter]) + "  " + 
                     str(minVals[dayCounter - 4]) + "  " + str(minVals[dayCounter - 3]) +
                  "  " + str(minVals[dayCounter - 2]) + "  " + 
                            str(minVals[dayCounter - 1]) + "  ")
            

        fivedayAve = (totalOfTemps) / 5
        print("The 5 day average is : " + str(fivedayAve))
        
        return fivedayAve
 
    #creates an array of five days
    #if index is less than or equal to 4 it creates an array of that length
def fiveDays(minVals, index):
    fiveDaysArr = []
    item = 1
    if index > 4:
        for item in range(index, index + 1):
            fiveDaysArr[item] += minVals[item]
            item += 1
    #elif index <= 4:
        #for item in range(1,index + 1):
         #   fiveDaysArr[item] += minVals[item]
         #   item += 1
    return fiveDaysArr        
            
        
    

def main():
    '''
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
    '''

    minVals = [39, 37, 39, 36, 28, 28, 22, 19, 17, 23, 44, 48, 34, 29, 33, 31, 39, 39, 41, 41, 41, 43, 38, 38, 39, 45, 38, 36, 37, 32, 28]
    output =[]
    for index in range(1,32):
        
        output.append(previousfiveDayAve(minVals, index-1))
 #       dayArray = fiveDays(minVals, index)
        dayArray = list(range(1,32))
        print("output:" + str(output))
        print("dayArray:",dayArray)
    plt.plot(dayArray, output, color='r', label="Minimaltemp")
    plt.title("Daily NYC Temps for Jan 2017")
    plt.xlabel('Day')
    plt.ylabel('Degrees')
    plt.legend(loc = 2,fontsize = 'x-small')
    plt.show()

        
    """
        dayArray = fiveDays(minVals, index)
        if (index <= 4):
            print("The average of day " + str(index) + " temperatures "+
                  "before day "+ str(index) + "are: "+ str(output))
            
            #plot graph code here
            #
            #
            #
            plt.plot(index, minVals, color='b', label="Min Temperature")
            plt.title("5 Day Min Temperatures in Jan 2017")
            plt.xlabel('Days')
            plt.ylabel(' Temp in degrees ')
            plt.legend(loc = 2, fontsize = 'x-small')
        elif (index > 4):
            print("The average of day " + str(index) + " temperatures and 5 days" +
                  " before day "+ str(index) + " which from day "+ str(index - 5) + 
                    " are: " + str(output))
            #plot graph code here
            #
            #
            #
            plt.plot(index, dayArray, color='b', label="Min Temperature")
            plt.title("5 Day Min Temperatures in Jan 2017")
            plt.xlabel('Days')
            plt.ylabel(' Temp in degrees ')
            plt.legend(loc = 2, fontsize = 'x-small')
            plt.show()
        else:
            print("error")
    """        
         
        
    
    print("This concludes the program.......")    
                                         

main()