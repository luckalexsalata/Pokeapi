#!/bin/sh
echo 'Run migration'
python3 manage.py makemigrations api
python3 manage.py migrate api

python3 manage.py runserver 0.0.0.0:8080