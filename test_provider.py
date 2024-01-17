import os
from pymongo import MongoClient

client_id = os.environ['AZURE_APP_CLIENT_ID']
username = os.environ['AZURE_IDENTITY_OBJECT_ID']
mech_props=dict(PROVIDER_NAME="azure",TOKEN_AUDIENCE=f"api%3A%2F%2F{client_id}")
props = dict(authmechanismproperties=mech_props)
client = MongoClient(os.environ['MONGODB_URI'], username=username, props=props)
client.test.test.insert_one({})
client.close()