#!/bin/sh

# python manage.py flush --no-input
python manage.py makemigrations
python manage.py migrate
# python manage.py syncdb
# python manage.py collectstatic --no-input --clear

exec "$@"
