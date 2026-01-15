#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 00:09:40 2024

@author: ibrahima
"""

# Create a program named prices.py using the following pseudocode below:

# initialize the count variable to 0
# initialize the sum variable to 0
# input full_name
# input the min_price and convert it to float
# create a list of prices example: 
# price_list = [69.0, 71.0, 84.5, 91.0, 67.4, 81.2, 84.6, 58.8, 79.3, 101.2]
# for price in price_list
#     add current price to sum
#     if price > min_price
#         increment count by 1        
# output "Hello",name,"the minimum price is ",min_price
# output "There are ",count,"prices greater than the minimum price"
# output "The total price is ",sum

count = 0
sum = 0
full_name = input("Enter your full name: ")
minimum_price = float(input("Enter the minimum price: "))
price_list = [69.0, 71.0, 84.5, 91.0, 67.4, 81.2, 84.6, 58.8,
79.3, 101.2]
for price in price_list:
    sum = sum + price
    if price > minimum_price:
        count = count + 1

print("Hello",full_name + ", the minimum price is",minimum_price)
print("There are",count,"prices greater than the minimum price.")
print("The total price is","$%.2f" % sum)        
    
