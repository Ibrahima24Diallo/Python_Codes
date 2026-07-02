#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue June 18 10:44:37 2026

@author: ibrahim
"""

import tabula
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#==== Read the pdf file into a list of DataFrames then convert it to CSV file ====

tables = tabula.read_pdf("Top_50_World_Banks.pdf", pages="all")
# Save the table and export to CSV file
tables[0].to_csv("top_banks.csv")

# Load data into Pandas
df = pd.read_csv("top_banks.csv")
# Delete the first column (which is an index column) from the original dataframe directly.
df.drop(df.columns[0], axis=1, inplace=True)

# Inspecting columns to see if they appear as expectated
# print(df.columns)
# print(df.head())

#=========== Cleaning the Data ======================

#Find any duplicates and show the total of duplicates
duplicates = df[df.duplicated()]
#print(duplicates)
num_duplicates = df.duplicated().sum()
#print(f"Duplicates: {num_duplicates}")

# Replace the column headers with numbers and retain columns with Index[2, 3, 4, 7]
df.columns = range(df.shape[1])
df = df[[2, 3, 4, 7]]
#print(df)

# Rename the Columns headers we will be focusing on
df.columns = ['Bank Name', 'Yearend', 'Country', 'Assets $m']
df.rename(columns={"Yearend": "Year", "Assets $m": "Bank Assets (USD)"}, inplace=True)

# Remove commas from values then convert str data type to int
df['Bank Assets (USD)'] = (
        df['Bank Assets (USD)'].str.replace(',', '').astype(int)
        )
# Check if the data type was converted to int
# print(df['Bank Assets (USD)'].dtype)  

# Convert the Bank Assets from Millions to Billions rounded to two decimal places 
df[['Bank Assets (USD)']] = np.round(df[['Bank Assets (USD)']]/1000, 2)

# Rename the Column Bank Assets (USD) from Millions to Billions
df.rename(columns={'Bank Assets (USD)': 'Assets (Billions USD)'}, inplace=True)
#df= df.iloc[1:]
#print(df)

#============= Analyzing the Data =====================
print(df.describe())

# Count the total number of each country
count_country = df["Country"].value_counts()
print(f"\n{count_country}")

#Display all rows of Bank Name and its Asset where Country is "China"
bank_country_asset = df.loc[df['Country'] == 'China', 
                            ['Bank Name', 'Country', 'Assets (Billions USD)']]
print(bank_country_asset)

#============= Plotting the Data ======================

#Creating a chart for Rows with index 1-15, indicating the top 15 largest banks in the world.
df = df.iloc[0:15, :]

# Sort the Largest banks in descending order before creating a chart 
df = df.sort_values(by='Assets (Billions USD)', ascending=False)

#Creating a Bar chart
plt.style.use("fivethirtyeight")
fig = plt.figure(dpi=160, figsize=(10,8))
plt.bar(df['Bank Name'], df['Assets (Billions USD)'], color='green', alpha=0.5)

#Format the plot
plt.title('List of 15 largest banks in the world', fontsize= 16)
plt.xlabel('Bank Names', fontsize= 14)
fig.autofmt_xdate() #draws the date labels diagonally to prevent them from overlapping.
plt.ylabel('Total Assets (Billions USD)', fontsize= 14)
plt.tick_params(axis='both', which='major', labelsize= 10)
plt.savefig("largest_banks.png")
plt.show()





























