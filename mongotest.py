import pymongo
client = pymongo.MongoClient("mongodb+srv://Prateek7898:<Prateek#1721>@cluster0.hqcnud5.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "Prateek",
    "email":"pareteek@gmail.com",
    "surname":"purohit"
}

db1 = client["mongotest"]
coll = db1['test']
coll.insert_one(d )