FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1
COPY requirements.txt ./
RUN apk update && apk upgrade && apk add nmap && mkdir /app && pip install --no-cache-dir -r requirements.txt
COPY ./webnmap/ /app/
WORKDIR /app
EXPOSE 8080
CMD gunicorn webnmap.wsgi:application --bind 0.0.0.0:8080