# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 17:28:47 2017

@author: Duvall Pinkney

Using the birthday data set, display the fraction of collisions that occur 
in Queens each hour. That is, for 0 (midnight to just before 1am), you should 
have as your y-value the fraction of: collisions that occurred in Queens at
 hour 0 over collisions across the whole city that occurred at hour 0.

#3: Submit your Python program as a .py file.
#4: Submit a screen shot of the graphics window containing the plot. 

"""

from matplotlib import pyplot as plt
import csv

def readfile():
    with open("NYPDCollisionDataOnMyBirthday.csv") as f:
        reader = csv.reader(f)
        next(reader)
        
        for row in reader:
            time = reader[row]
            location = row[2]
            c = time.find(":")
            hour = int(time[:c])
            if (hour >= 0) & (hour < 1) & (location == "QUEENS"):
                print(reader[row])
                
            elif (hour >= 0) & (hour < 1) & (location != "QUEENS"):    
                print(reader[row])
                
        minutes = hour / 60        
        plt.plot(minutes, len(r), color='green', marker='o', linestyle='solid')
        plt.title("Collision per hour in 10458")
        plt.axis([0,59,0,24])
        plt.xlabel("Hours")
        plt.ylabel("# of Collisions")
        plt.show   
        
        
        
def main():

    readfile()
main()        