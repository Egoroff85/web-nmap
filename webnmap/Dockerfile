# pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

COPY requirements.txt ./
RUN apk update && apk upgrade && apk add nmap && mkdir /app && pip install --no-cache-dir -r requirements.txt
COPY . /app/
WORKDIR /app
EXPOSE 8080
CMD gunicorn webnmap.wsgi:application --bind 0.0.0.0:8080