#!/usr/bin/env bash
set -eux

python3 -m venv .venv
source .venv/bin/activate
pip install -U pip setuptools
pip install git+https://github.com/mongodb/mongo-python-driver.git
pip install .
