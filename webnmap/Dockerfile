# pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/program

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
#ENV DEBUG 1
#ENV SECRET_KEY x*-)o@fr^#cemy#k7fs)bky)v%@xyaokblugytumk=1u9tfkdr
#ENV DJANGO_ALLOWED_HOSTS localhost 127.0.0.1 [::1]
#ENV CELERY_BROKER redis://redis:6379/0
#ENV CELERY_BACKEND redis://redis:6379/0

# install dependencies
RUN python -m pip install --upgrade pip
COPY ./requirements.txt /usr/src/program/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# install nmap
RUN apk add nmap

# copy project
COPY . /usr/src/program

# migrate db
#RUN python manage.py makemigrations
#RUN python manage.py migrate --run-syncdb

# run entrypoint.sh
ENTRYPOINT ["/usr/src/program/entrypoint.sh"]
