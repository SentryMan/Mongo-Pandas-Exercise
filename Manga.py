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



"""Get Top 20 most popular In categories and plot category stats"""

def getTop20(*args):
    
    top20 = mdf
    
    for cat in args:
    
        top20['flag'] = top20.c.apply(lambda l:
                True if cat in l else False )    
        
        top20 = top20[top20.flag == True]
    
    return top20.head(20).sort_values(by=['h'], ascending=False)


def plotPopular(*args):
    
    meanList = []
    genreList = []
    
    for cat in args:
        meanList.append(getTop20(cat)['h'].mean())
        genreList.append(cat)
        
    plt.xlabel("Genre")
    plt.ylabel("Average Views")
    plt.bar(genreList, meanList)
    plt.show()


plotPopular("Action", "Adventure", "Romance", "Comedy", "Supernatural" )













"Turns it into csv"
mdf.to_csv('manga.csv', index=False)
mcsv = pd.read_csv('manga.csv')