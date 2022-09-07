# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 13:25:34 2022

@author: usbhu
"""

from requests import get
from time import sleep

# get api key from file (for gitignore so i can publish this without my key)
with open("api.txt", "r") as file:    
    apiKey = file.readlines()

# get user's config
tickerItem = input("item to track sell price of?")

# get data from api
itemsJson = get("https://api.hypixel.net/resources/skyblock/items").json()

# ergonomics
items = itemsJson["items"]

# find item id given item name
for i in items:
    if i["name"] == tickerItem:
        tickerItem = i["id"]
        break

# get start price
bazaarJson = get("https://api.hypixel.net/skyblock/bazaar?key="+apiKey[0]).json()
oldPrice = 0
currentPrice = bazaarJson["products"][tickerItem]["sell_summary"][0]["pricePerUnit"]
priceDiff = round(currentPrice-oldPrice, 1)
print(f"START! | PRICE {currentPrice} | DIFF N/A")

#ticker
while True:
    #get data from api
    bazaarJson = get("https://api.hypixel.net/skyblock/bazaar?key="+apiKey[0]).json()
    
    # get price of ticker item
    oldPrice = currentPrice
    currentPrice = bazaarJson["products"][tickerItem]["sell_summary"][0]["pricePerUnit"]
    priceDiff = round(currentPrice-oldPrice, 1)
    
    # display price
    if currentPrice != oldPrice:
        print(f"MOVED! | PRICE {currentPrice} | DIFF {priceDiff}")
        
    #wait
    sleep(0.625)