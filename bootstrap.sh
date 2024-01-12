#!/usr/bin/env bash
set -eux

python3 -m venv .venv
source .venv/bin/activate
pip install git+https://github.com/blink1073/mongo-python-driver.git@PYTHON-3467-2
pip install .
