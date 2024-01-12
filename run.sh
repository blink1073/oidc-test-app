#!/usr/bin/env bash
set -o errexit  # Exit the script with error if any of the commands fail

source ./env.sh

VARLIST=(
AZURE_IDENTITY_OBJECT_ID
ATLAS_URI
AZURE_APP_CLIENT_ID
)

# Ensure that all variables required to run the test are set, otherwise throw
# an error.
for VARNAME in ${VARLIST[*]}; do
[[ -z "${!VARNAME}" ]] && echo "ERROR: $VARNAME not set" && exit 1;
done

export MONGODB_URI="${AZURE_IDENTITY_OBJECT_ID}@${MONGODB_URI}/?authMechanism=MONGODB-OIDC&authMechanismProperties=PROVIDER_NAME:azure,TOKEN_AUDIENCE:api%3A%2F%2F${AZURE_APP_CLIENT_ID}"
.venv/bin/python3 test.py