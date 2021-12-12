#!/bin/sh

python manage.py migrate

gunicorn -b :5000 cherno.wsgi:application
