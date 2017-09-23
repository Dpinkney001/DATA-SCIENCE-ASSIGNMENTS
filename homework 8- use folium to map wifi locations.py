# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 20:34:15 2017

@author: DUVALL NOTEBOOK

Use Folium to make a map that includes all the WiFi locations within one 
hundredth of a degree of a location of your choice.  For example,
 Lehman College is at 40.8725 degrees North and 73.8939 degrees West. 
 For this location, you would include all hotspots that are within 0.01 of 
 this location in either direction. Your map should color the inside hotspots
 blue and the outside hotspots green (GIS location as well as type available 
 in the CSV file of hotspots). 

#3: Submit your Python program as a .py file.




"""

import folium
import pandas as pd


wifiHotspots = pd.read_csv('NYC_Free_Public_WiFi_03292017.csv')
print(wifiHotspots)


mapOfNYC = folium.Map(location=[40.8725 + 0.01, 73.8939 + 0.01])

for index,row in wifiHotspots.iterrows():
    lat = row[4]
    lon = row[5]
    name = str(index)

    folium.Marker([lat,lon],popup=name).add_to(mapOfNYC)
    
mapOfNYC.save(outfile='wifiHotSpots.html')    

