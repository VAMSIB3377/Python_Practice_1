import pymongo

Conn = "mongodb+srv://Vamsi_Batta:12345@cluster0.x5qyupy.mongodb.net/?retryWrites=true&w=majority"

try:
    client = pymongo.MongoClient(Conn)
except Exception:
    print("Error : ", Exception)

myDB = client["Pymongo_CRUD_Operations"]

myCollection = myDB["Document"]

# Insertion
# Document Contains ID of The Student, Name of a Student, Total Marks he/she Secured
# myDOC1 = {"_id": 1, "Name": "Abc", "T_Marks": 567}
# myDOC2 = {"_id": 2, "Name": "Bcd", "T_Marks": 400}
# myDOC3 = {"_id": 3, "Name": "Cde", "T_Marks": 528}
# myDOC4 = {"_id": 4, "Name": "Def", "T_Marks": 342}

# Insert Many
"""myDOC = [{"_id": 1, "Name": "Abc", "T_Marks": 567},
        {"_id": 2, "Name": "Bcd", "T_Marks": 400},
        {"_id": 3, "Name": "Cde", "T_Marks": 528},
        {"_id": 4, "Name": "Def", "T_Marks": 342}]

myCollection.insert_many(myDOC)
"""
# myCollection.insert_one(myDOC1)
# myCollection.insert_one(myDOC2)
# myCollection.insert_one(myDOC3)
# myCollection.insert_one(myDOC4)

# Reading the Document

"""records = myCollection.find({})
for i in records:
    print(i)
    print("\n")"""




#print(client.list_database_names())

# Updating the Record
"""
query = {
    "T_Marks": 400
}
new_val = {"$set": {"T_Marks": 520}}

myDOC1_Update = myCollection.update_one(query, new_val)

"""

# Deleting The Record

query_del = {
    "_id": 4

}

record_del = myCollection.delete_one(query_del)

records = myCollection.find()

for i in records:
    print("\n", i)


