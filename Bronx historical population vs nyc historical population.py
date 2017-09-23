# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 16:05:16 2017

@author: Duvall Pinkney

Using gradient descent compute the linear regression for the historical Bronx 
population versus the total New York City population. Display a plot containing
 the pairs (bx[i],nyc[i]) where bx[i] is the Bronx population in year i and 
 nyc[i] is the total New York city population in year i 
 (Hint: use a scatter plot to show this part). Include on your plot the
 linear regression line that you computed. 

Make sure to include in the title of your plot the date plotted. 

#1: Submit your Python program as a .py file.
#2: Submit a screen shot of the graphics window containing the plot.
"""

from matplotlib import pyplot as plt
import math
from collections import Counter
#import Counter
# From:  https://en.wikipedia.org/wiki/Demographics_of_New_York_City

Year = [1790, 1800, 1810, 1820, 1830, 1840, 1850, 1860, 1870, 1880, 1890, 1900, 
        1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]

Manhattan = [33131, 60515, 96373, 123706, 202589, 312710, 515547, 813669, 942292,
             1164673, 1441216, 1850093, 2331542, 2284103, 1867312, 1889924, 
             1960101, 1698281, 1539233, 1428285, 1487536, 1537195, 1585873]

Brooklyn = [4549, 5740, 8303, 11187, 20535, 47613, 138882, 279122, 419921,
            599495, 838547, 1166582, 1634351, 2018356, 2560401, 2698285, 2738175,
            2627319, 2602012, 2230936, 2300664, 2465326, 2504700] 

Queens = [6159, 6642, 7444, 8246, 9049, 14480, 18593, 32903, 45468, 56559, 87050,
          152999, 284041, 469042, 1079129, 1297634, 1550849, 1809578, 1986473,
          1891325, 1951598, 2229379, 2230722]

Bronx = [1781, 1755, 2267, 2782, 3023, 5346, 8032, 23593, 37393, 51980, 88908, 
         200507, 430,980, 732016, 1265258, 1394711, 1451277, 1424815, 1471701,
         1168972, 1203789, 1332650, 1385108]

StatenIS = [3827, 4563, 5347, 6135, 7082, 10965, 15061, 25492, 33029, 38991, 
              51693, 67021, 85969, 116531, 158346, 174441, 191555, 221991, 
              295443, 352121, 378977, 443728, 468730]

Total = [49447, 79215, 119734, 152056, 242278, 391114, 696115, 1174779, 1478103,
         1911698, 2507414, 3437202, 4766883, 5620048, 6930446, 7454995, 7891957,
         7781984, 7894862, 7071639, 7322564, 8008278, 8175133]

Borough = [Manhattan, Bronx, Brooklyn, Queens, Bronx, StatenIS]


def percentageOfPop(Year, Pop, Total, Borough):
    output = 0.0
    year = 0    
    borough = 0 
    total = 0    
    for year in Year:
        for borough in Borough:
            for total in Total:
                print("The year: ",Year[year])
                print("The Borough: ",Borough[year])
                print("The Population total: ",Total[year])
                pop += Borough[year]
                totalPop += Total[year]
                output = (pop / totalPop) * 100
                print("The percentage of NYC Population ",Borough, " takes up is", 
                      output)
                year += 1
                borough += 1
                total += 1
                
def nycHistoricalTotal(year, Total):
    year = 0
    poptotal = 0
    for year in range (0, len(Year)):
        poptotal += Total[year]
        print(" the pop total for year", year," is ", Total[year])
        year += 1
    return poptotal                
                
def bronxHistoricalTotal(year, Borough):
     year = 0
     pop = 0
     #Borough = Bronx
     for year in range(0, len(Year)):
        pop += Bronx[year]
        print(" the pop total for year", year, " is ", Bronx[year])
        
        year += 1
        
     return pop 

   
             
def main():

    print("The bronx historical total is :", bronxHistoricalTotal(Year, Bronx))
    print("The NYC historical total is : ", nycHistoricalTotal(Year, Total))
    bronx = 0
    total = 0
    for i in range(0, 23):
        bronx += Bronx[i]
        total += Total[i]
        i += 1
        
        
    plt.scatter(bronx, total)
    plt.title("Bronx Historical population vs NYC Total")
    plt.xlabel("Bronx total")
    plt.ylabel("NYC total")
    plt.show()
main()     