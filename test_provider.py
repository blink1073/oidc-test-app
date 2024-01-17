import os
from pymongo import MongoClient

client_id = os.environ['AZURE_APP_CLIENT_ID']
username = os.environ['AZURE_IDENTITY_OBJECT_ID']
mech_props=dict(PROVIDER_NAME="azure",TOKEN_AUDIENCE=f"api%3A%2F%2F{client_id}")
kwargs = dict(authmechanismproperties=mech_props, username=username)
client = MongoClient(os.environ['MONGODB_URI'], **kwargs)
client.test.test.insert_one({})
client.close()