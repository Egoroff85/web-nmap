# pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/program

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN python -m pip install --upgrade pip
COPY ./requirements.txt /usr/src/program/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# install nmap
RUN apk add nmap

# copy project
COPY . /usr/src/program


# run entrypoint.sh
ENTRYPOINT ["/usr/src/program/entrypoint.sh"]
