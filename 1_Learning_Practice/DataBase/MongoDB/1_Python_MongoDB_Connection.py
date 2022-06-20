# step1 - Install and Import Pymongo
import pymongo

# step2 - Create a MongoDB Client
from pymongo import MongoClient

try:
    client = MongoClient("mongodb+srv://Vamsi_Batta:12345@cluster0.x5qyupy.mongodb.net/?retryWrites=true&w=majority")

except Exception:
    print("Error : ", Exception)



print(client.list_database_names())
