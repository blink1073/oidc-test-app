import os
from pymongo import MongoClient
client = MongoClient(os.environ['MONGODB_URI'])
client.test.test.insert_one({})