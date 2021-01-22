import pymongo
client = pymongo.MongoClient(
    "mongodb+srv://farida:maxime080514@cluster0.yjajj.mongodb.net/country_db?retryWrites=true&w=majority")
db = client.test
print(db)
