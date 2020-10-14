# скачать официальный образ python 3 alpine linux
FROM python:3.8.3-alpine

# установить рабочую директорию
WORKDIR /usr/src/program

# установить переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# установить компоненты
RUN apk add nmap gcc libc-dev zlib-dev jpeg-dev

# установить зависимости python
RUN python -m pip install --upgrade pip
COPY ./requirements.txt /usr/src/program/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# скопировать файлы проекта
COPY . /usr/src/program

# запустить entrypoint.sh
ENTRYPOINT ["/usr/src/program/entrypoint.sh"]