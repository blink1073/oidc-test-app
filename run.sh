#!/usr/bin/env bash
set -o errexit  # Exit the script with error if any of the commands fail

source ./env.sh

VARLIST=(
AZURE_IDENTITY_CLIENT_ID
AZURE_APP_CLIENT_ID
)

# Ensure that all variables required to run the test are set, otherwise throw
# an error.
for VARNAME in ${VARLIST[*]}; do
[[ -z "${!VARNAME}" ]] && echo "ERROR: $VARNAME not set" && exit 1;
done

TARGET=${1:-test_provider.py}

MONGODB_URI="${MONGODB_URI:-mongodb://localhost:27017/}"
export MONGODB_URI="${MONGODB_URI}?authMechanism=MONGODB-OIDC"
echo $MONGODB_URI
.venv/bin/python3 $TARGET
