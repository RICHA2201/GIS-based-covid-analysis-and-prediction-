# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 12:30:27 2021

@author: RICHA
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 11:45:52 2021

@author: RICHA
"""
import pandas as pd
import geopandas as gpd
import requests

r = requests.get('https://prsindia.org/covid-19/cases').text
data = pd.read_html(r)

for data_cases in data:
      print(data_cases)
      
data_cases = data_cases[['State/UT','Death']]

country_data = gpd.read_file(r'C:\Users\RICHA\Desktop\app\India_State_Boundary.shp')  

for items in data_cases['State/UT'].tolist():
     country_data_list = country_data['State_Name'].tolist()
     if items in country_data_list:
        pass
     else:
        print(items + ' is not in the country_data list') 
        
country_data.replace('Chhattishgarh','Chhattisgarh',  inplace = True)
country_data.replace('Tamilnadu', 'Tamil Nadu', inplace = True)            
country_data.replace('Telengana','Telangana',  inplace = True)
country_data.replace('Andaman & Nicobar','Andaman and Nicobar Islands',  inplace = True)
country_data.replace('Daman and Diu and Dadra and Nagar Haveli','Dadra and Nagar Haveli and Daman and Diu',  inplace = True)  

data_cases.rename(columns = {'State/UT': 'State_Name'}, inplace = True)  

final = country_data.merge(data_cases, on = 'State_Name')

final.to_file(r'C:\Users\RICHA\Desktop\app\death.shp')
  
   
     
      
     
      
      
   





