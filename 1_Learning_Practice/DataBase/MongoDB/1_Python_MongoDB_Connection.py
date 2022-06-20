import pymongo
from pymongo import MongoClient

cluster = MongoClient('mongodb+srv://Vamsi_Batta:<12345>@cluster0.x5qyupy.mongodb.net/?retryWrites=true&w=majority')

db = cluster['Test']
collection = db['Test']

data = {"_id": 0, "Name": "abc", "Score": 5}

collection.insert_one(data)
