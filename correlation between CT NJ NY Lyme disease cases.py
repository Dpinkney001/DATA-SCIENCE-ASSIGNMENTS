# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 08:42:58 2017

@author: Duvall Pinkney

Examine the correlation between the change in incidence of Lyme Disease in Connecticut, New Jersey, and New York. Compute the pairwise correlation-- that is ρ(CT,NJ), ρ(CT,NY), and ρ(NJ,NY). Use the textbook's code to compute the correlations between each pair of states. Include all correlations that you computed in your written answer. 

#1: Submit a .txt or .pdf file with your answer.


"""
from collections import Counter
from linear_algebra import sum_of_squares, dot
import math
import matplotlib.pyplot as plt

def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0 # if no variation, correlation is zero
def standard_deviation(x):
    return math.sqrt(variance(x))        
    
def variance(x):
    """assumes x has at least two elements"""
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)


def de_mean(x):
    """translate x by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def mean(x):
    return sum(x) / len(x)

def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)
#Data from CDC's Lyme Disease page:
years = [2003,2004,2005,2006,2007,2008,2009,2010,2011]
NY = [5399,5100,5565,4460,4165,5741,4134,2385,3118]
NJ = [2887,2698,3363,2432,3134,3214,4598,3320,3398]
CT = [1403,1348,1810,1788,3058,2738,2751,1964,2004]

#We'll do the same operations for each state, so put in a function:
def scale(stateList, plt, lab,col):
     """
     Takes a list, label, and color and creates a scatter plot
     of the percentage change with respect to the first entry
     in the list.
     """
     baseNum = stateList[0]
     scaled= [i*100/baseNum-100 for i in stateList]
     plt.scatter(years, scaled, label=lab, c = col, s=75)


#Create scatter plots for each state:
scale(NY,plt,"NY", "blue")
scale(NJ,plt,"NJ", "red")
scale(CT,plt,"CT", "purple")

#Set up title, axis labels, and legend, and then show:
plt.title("Lyme Disease in NY, NJ, & CT")
plt.xlabel('Years')
plt.ylabel('Percent Change')
plt.legend()
plt.show()    
    
def main():
    ctNJrelationship = 0.0
    ctNYrelationship = 0.0
    NJNYrelationship = 0.0
    
    
    ctNJrelationship = correlation(CT, NJ)
    ctNYrelationship = correlation(CT, NY)
    NJNYrelationship = correlation(NJ, NY)
    
    print(" The (CT,NJ) correlation is: ",ctNJrelationship )
    print(" The (CT,NY) correlation is: ",ctNYrelationship )
    print(" The (NJ,NY) correlation is: ",NJNYrelationship )












main()    