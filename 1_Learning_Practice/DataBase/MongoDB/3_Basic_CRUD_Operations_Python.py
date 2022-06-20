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


# myCollection.insert_one(myDOC1)
# myCollection.insert_one(myDOC2)
# myCollection.insert_one(myDOC3)
# myCollection.insert_one(myDOC4)

# Reading the Document
record = myCollection.find_one()
print(record)
print("\n\n")

#print(client.list_database_names())

# Updating the Record

query = {
    "T_Marks": 525
}
new_val = {"$set": {"T_Marks": 520}}

myDOC1_Update = myCollection.update_one(query, new_val)


record = myCollection.find_one()
print("\n\n", record)
print("\n\n")
