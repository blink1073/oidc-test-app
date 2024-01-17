# OIDC Test App

## Prerequisites

- Azure Managed Identity with associated Group
- Azure VM with associated Managed Identity
- MongoDB Cluster configured with OIDC
- Local version of Python 3.8+ and Git.

## Setup

Clone this repository onto your VM.

Run `bash bootstrap.sh` to create a virtual environment with
an OIDC-enabled version of PyMongo.

Edit `test_provider.py` and `test_custom_callback.py` as desired to excercise test.

Create an `env.sh` file with the appropriate variables:

```bash
export MONGODB_URI="<uri_of_cluster>"
export AZURE_APP_CLIENT_ID="<client_id_of_azure_application>"
export AZURE_IDENTITY_OBJECT_ID="<object_id_of_azure_application>"
```

## Usage

Run `run.sh` to run the test script in the virtual environment.
By default it will run `test_provider.py`.  To test the custom callback
run ad `run.sh test_custom_callback.py`.