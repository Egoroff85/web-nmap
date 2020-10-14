#!/bin/sh

mkdir static
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input --clear

exec "$@"
