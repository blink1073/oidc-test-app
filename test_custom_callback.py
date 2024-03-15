import os
from azure.identity import DefaultAzureCredential
from pymongo import MongoClient
from pymongo.auth_oidc import OIDCCallback, OIDCCallbackContext, OIDCCallbackResult

app_id = os.environ['AZURE_APP_CLIENT_ID']
client_id = os.environ['AZURE_IDENTITY_CLIENT_ID']
uri = os.environ['MONGODB_URI']

class MyCallback(OIDCCallback):
    def fetch(self, context: OIDCCallbackContext) -> OIDCCallbackResult:
        credential = DefaultAzureCredential(managed_identity_client_id=client_id)
        token = credential.get_token(f"api://{app_id}/.default").token
        return OIDCCallbackResult(access_token=token)

props = dict(OIDC_CALLBACK=MyCallback())
c = MongoClient(uri, authMechanismProperties=props)
c.test.test.insert_one({})
c.close()