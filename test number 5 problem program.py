# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 02:25:45 2017

@author: Duvall Pinkney

standard deviation
"""
from collections import Counter
from linear_algebra import sum_of_squares, dot
import math

def standard_deviation(x):
    return math.sqrt(variance(x))

def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0 # if no variation, correlation is zero
        
    
def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)    

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


def main():
    
    x = 5
    y = 4
    
    ans = correlation(x, y)
    print("corellation output:  ", ans)
    ans2 = covariance(x,y)
    print("covariance output:  ",ans2)
    ans3 = standard_deviation(x)
    print("standard deviation output-x:  ",ans3)
    ans3 = standard_deviation(y)
    print("standard deviation output-y:  ",ans3)
    varianceans = variance(x)
    print(varianceans)
    
main()    
    
    