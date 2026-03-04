#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 09:59:12 2025

@author: ibrahim
"""
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import csv
import plotly.io as pio
pio.renderers.default = 'browser'


#Project Scenario:
#An international firm that is looking to expand its business in different countries across the world 
#has recruited you. You have been hired as a junior Data Engineer and are tasked with creating a script 
#that can extract the list of the top 10 largest economies of the world 
#in descending order of their GDPs in Billion USD (rounded to 2 decimal places), 
#as logged by the International Monetary Fund (IMF).

#tables from webpage using Pandas. Retain table number 3 as the required dataframe.
url = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"
tables = pd.read_html(url)
df = tables[3]


# Replace the column headers with column numbers
df.columns = range(df.shape[1])

# Retain columns with index 0 and 2 (name of country and value of GDP quoted by IMF)
df = df[[0, 2, 3]]

# Retain the Rows with index 1 to 10, indicating the top 10 economies of the world.
df = df.iloc[0:11, :]

# Assign column names as "Country" and "GDP (Million USD)"
df.columns = ['Country', 'GDP (Million USD)', 'Year']

#Modify the GDP column of the DataFrame, converting the value available in Million USD to Billion USD. 
#Use the round() method of Numpy library to round the value to 2 decimal places. Modify the header of the DataFrame to GDP (Billion USD).

# Change the data type of the 'GDP (Million USD)' column to integer. Use astype() method.
df['GDP (Million USD)'] = df['GDP (Million USD)'].astype(int)

# Convert the GDP value in Million USD to Billion USD
df[['GDP (Million USD)']] = df[['GDP (Million USD)']]/1000

# Use numpy.round() method to round the value to 2 decimal places.
df[['GDP (Million USD)']] = np.round(df[['GDP (Million USD)']], 2)
df= df.iloc[1:]
# Rename the column header from 'GDP (Million USD)' to 'GDP (Billion USD)'
#df1 = df.rename({'GDP (Million USD)' : 'GDP (Billion USD)'})

#print(type(df1['Year']))

fig = px.bar(df, 
              x='Country', 
              y='GDP (Million USD)', 
              hover_data=['Country', 'GDP (Million USD)'],
              title='The top 10 largest economies of the world')

fig.update_traces(hovertemplate='<b>Country:</b> %{x}<br>' +
                                '<b>GDP:</b> %{y}<br>')
fig.show()



#** SECOND VERSION **
"""
This version allows you to visualizes the results within the IDE 
instead using Plotly Express to create an interactive bar chart on a webpage
"""

# Code Starts Here
"""
#Convert the data to CSV and load the DataFrame to the CSV file and name it "largest_gdp.csv"
filename = df.to_csv('largest_gdp.csv')

filename = 'largest_gdp.csv'

with open(filename, 'r') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #print(header_row)
    
    #for index, column_header in enumerate(header_row):
        #print(index, column_header)
    #Create lists to store the dates, lows and highs data
    countries, gdps = [], []
    for row in reader:
        #current_date = datetime.strptime(row[2], "%Y-%m-%d")
        country = row[1]
        gdp = float(row[2]) 
        #Append data to the lists
        
        gdps.append(gdp)
        countries.append(country)
        #lows.append(int(row[6]))
        
#Plotting the data
plt.style.use("seaborn")
fig = plt.figure(dpi=160, figsize=(10,8))
plt.bar(countries, gdps, color='red', alpha=0.5)

#Format the plot
plt.title('The top 10 largest economies of the world', fontsize= 16)
plt.xlabel('Country', fontsize= 14)
fig.autofmt_xdate() #draws the date labels diagonally to prevent them from overlapping.
plt.ylabel('GDP (Million USD)', fontsize= 14)
plt.tick_params(axis='both', which='major', labelsize= 10)
plt.show()

"""




























