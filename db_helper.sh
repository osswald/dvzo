#! /usr/bin/bash

rm db.sqlite3
rm train_management/migrations/*.py
python setup.py install
python manage.py makemigrations
python manage.py migrate
