# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 19:47:05 2019

@author: Yutyrannus
"""

import pymongo
import pandas as pd
from pymongo import MongoClient

client = MongoClient('mongodb+srv://jojo:weak@cluster0-ua5e8.mongodb.net')
db = client['MangaDB']

col = db.Manga

mdf = pd.DataFrame(list(col.find()))

mdf = mdf.drop(['_id', '_class'], axis=1)