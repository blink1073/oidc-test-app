import os
from pymongo import MongoClient
client = MongoClient(os.environ['MONGODB_URI'], username=os.environ['AZURE_IDENTITY_OBJECT_ID'])
client.test.test.insert_one({})
