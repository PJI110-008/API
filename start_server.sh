#!/bin/bash
sleep 10
flask db init
flask db migrate
flask db upgrade
python run.py
