import os
from pymongo import MongoClient

app_id = os.environ['AZURE_APP_CLIENT_ID']
username = os.environ['AZURE_IDENTITY_CLIENT_ID']
mech_props=dict(PROVIDER_NAME="azure",TOKEN_AUDIENCE=f"api%3A%2F%2F{app_id}")
kwargs = dict(authmechanismproperties=mech_props, username=username)
client = MongoClient(os.environ['MONGODB_URI'], **kwargs)
client.test.test.insert_one({})
client.close()