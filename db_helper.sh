#! /usr/bin/bash

rm db.sqlite3
rm train_management/migrations/*.py
python setup.py install
python manage.py makemigrations train_management
python manage.py migrate
python db_helper.py