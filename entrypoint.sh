#!/bin/sh

python manage.py migrate

gunicorn -b :5000 cookery.wsgi:application
