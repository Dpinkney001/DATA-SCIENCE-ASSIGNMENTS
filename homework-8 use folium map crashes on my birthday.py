# -*- coding: utf-8 -*-
"""
author: Duvall Pinkney

Using the birthday data set collected in Homework 3, use Folium to plot the
 locations of all the crashes that occurred on your birthday.

#1: Submit your Python program as a .py file.
#2: Submit the .html file of the map that your program produced.



"""

import folium
import pandas as pd


collisions = pd.read_csv('collsionsOn3312016.csv')
print(collisions)


mapOfNYC = folium.Map(location=[40.75, -74.125])

for index,row in collisions.iterrows():
    lat = row[4]
    lon = row[5]
    name = str(index)

    folium.Marker([lat,lon],popup=name).add_to(mapOfNYC)
    
mapOfNYC.save(outfile='collisionsOn3312016.html')    