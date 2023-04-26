#django

#syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY ./djangorequirements.txt /code
RUN pip install -r djangorequirements.txt

#COPY second_tables.xlsx /
#COPY relaciones_data.xlsx /
RUN apt-get update  && \
    apt-get install -y make

# ENTRYPOINT  python /LoadMasterTable.py && \
ENTRYPOINT  python manage.py makemigrations && \
            python manage.py migrate  && \
            python manage.py collectstatic --noinput && \
            python manage.py shell < initAdmin.py && \
            gunicorn apidev.wsgi --bind 0.0.0.0:8000 --workers 4 --timeout 240