#! /usr/bin/bash

rm db.sqlite3
rm train_management/migrations/*.py
rm users/migrations/*.py
python setup.py install
python manage.py makemigrations train_management
python manage.py makemigrations users
python manage.py migrate
python manage.py compilemessages
python db_helper.py
python manage.py createsuperuser --username admin
