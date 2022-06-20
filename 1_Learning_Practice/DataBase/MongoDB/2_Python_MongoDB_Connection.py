# step1 - Install and Import Pymongo
import pymongo

# step2 - Create a MongoDB Client

conn_str = "mongodb+srv://Vamsi_Batta:<12345>@cluster0.x5qyupy.mongodb.net/?retryWrites=true&w=majority"
try:
    client = pymongo.MongoClient(conn_str)
except Exception:
    print("Error : " +Exception)

# step3 = Create a DB


print(client.list_database_names())
