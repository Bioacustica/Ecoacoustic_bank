#django

#syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY . /code
RUN pip install -r requirements.txt

ENTRYPOINT  cd ./apidev && \
            python manage.py makemigrations && \
            python manage.py migrate  && \
            python manage.py runserver 0.0.0.0:8000