# step1 - Install and Import Pymongo

import pymongo

# step2 - Create a MongoDB Client
conn_str = "mongodb+srv://Vamsi_Batta:12345@cluster0.x5qyupy.mongodb.net/?retryWrites=true&w=majority"

try:
    client = pymongo.MongoClient(conn_str)

except Exception:
    print("Error : ", Exception)

# step 3 - Create a DB
myDB = client["Pymongo_Demo"]

# step 4 - Create a Collection
myCollection = myDB["Demo_Collection"]

# step 5 - Create a Document
myDoc = {
    "_id": 1,
    "Name": "Abc",
    "Message": "This is Pymongo Demo"
}

# step 6 - Insert the Document into The Database inside the Collection
myCollection.insert_one(myDoc)
