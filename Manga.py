# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 19:47:05 2019

@author: Yutyrannus
"""

import csv
import pymongo
import pandas as pd
from pymongo import MongoClient
from matplotlib import pyplot as plt


"Setting up Mongo"
client = MongoClient('mongodb+srv://jojo:weak@cluster0-ua5e8.mongodb.net')
db = client['MangaDB']

col = db.Manga

pd.set_option('display.precision', 1)

mdf = pd.DataFrame(list(col.find()))

"Drop data we won't need"
mdf = mdf.drop(['_id', 'i', '_class'], axis=1)


nulls = mdf[mdf.RealID == -1]
nulls.info()

mdf = mdf[mdf.RealID != -1]
mdf.info()



"""The different quantiles of popularity"""
percents = [x / 100 for x in [25,40,50,70,90,95,99, 99.5]]
 
for percent in percents:
    print(f"manga with {mdf['h'].quantile(percent)} views are in the {percent*100}th percentile")



"""Get Top 20 most popular"""
top20 = mdf.sort_values(by=['h'], ascending=False).head(20)

top20.corr()









"Turns it into csv"
mdf.to_csv('manga.csv', index=False)
mcsv = pd.read_csv('manga.csv')