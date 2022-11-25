#!/bin/bash

sudo apt install python3-virtualenv
virtualenv env
source env/bin/activate

pip install -r requirements.txt

export FLASK_APP=main.py
export FLASK_RUN_PORT=8080

flask run