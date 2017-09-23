# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 04:49:47 2017

@author: Duvall Pinkney

Using the birthday data set (see above), display a histogram of the number of 
collisions that occur each hour. That is, your x-axis will have the hours from
 0 to 23 and the y-axis will be the number of collisions. Make sure to include
 in the title of your plot the date plotted. 

#1: Submit your Python program as a .py file.
#2: Submit a screen shot of the graphics window containing the plot.


Hint: In this file, times of collisions are stored as "H:MM" or "HH:MM". To
 get the hour to use as a key for your dictionary, you can first find the 
 location of the ":" in the string and then use it. For example, if timeString 
 holds the string, then c = timeString.find(":") finds the location, and 
 hour = int(timeString[:c]) 
will give the hour as an integer.






"""
from matplotlib import pyplot as plt
import csv

def readfile():
    with open("NYPDCollisionDataOnMyBirthday.csv") as f:
        reader = csv.reader(f)
        next(reader)
        
        for row in reader:
            
            #print(row)
            #print(row[1])
            timeOfCollision = row[1]
            c = timeOfCollision.find(":")
            hour = int(timeOfCollision[:c])
            #for collision in range(len(row[1])):
            numOfCollisions = len(row[1])
            #print(len(row[1])) 
        #times = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,
        #         21,22,23]
        #for collisions in range(0,)
        #numOfCollisions = len(row[1])    
        plt.plot(hour, numOfCollisions, color='green', marker='o', linestyle='solid')
        plt.title("Collision per hour in 10458")
        plt.axis([0,24,0,24])
        plt.xlabel("Hours")
        plt.ylabel("# of Collisions")
        plt.show
#def plotData(file):

                
            
def main():

    readfile()


main()            