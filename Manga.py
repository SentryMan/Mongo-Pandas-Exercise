# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 19:47:05 2019

@author: Yutyrannus
"""

import csv
import pymongo
import pandas as pd
from pymongo import MongoClient

"Setting up Mongo"
client = MongoClient('mongodb+srv://jojo:weak@cluster0-ua5e8.mongodb.net')
db = client['MangaDB']

col = db.Manga

mdf = pd.DataFrame(list(col.find()))

"Drop data we won't need"
mdf = mdf.drop(['_id', 'i', '_class'], axis=1)

nulls = mdf[mdf.RealID == -1]
nulls.info()

mdf = mdf[mdf.RealID != -1]
mdf.info()




"Turns it into csv"
mdf.to_csv('manga.csv', index=False)
mcsv = pd.read_csv('manga.csv')