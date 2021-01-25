import pymongo
import os

secret_key = os.environ.get("Mongodb_access")

# database connection
client = pymongo.MongoClient( secret_key)

client = pymongo.MongoClient('mongodb+srv://farida:maxime080514@cluster0.yjajj.mongodb.net/country_db?retryWrites=true&w=majority')