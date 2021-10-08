#django

#syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
<<<<<<< HEAD
COPY DjangoRequirements.txt /code
RUN pip install -r DjangoRequirements.txt
=======
COPY ./djangorequirements.txt /code
RUN pip install -r djangorequirements.txt
>>>>>>> 5364bf5eb3d7a8596936082627049b296c7bf15f

ENTRYPOINT  python manage.py makemigrations && \
            python manage.py migrate  && \
            python manage.py collectstatic --noinput && \
            python manage.py shell < initAdmin.py && \
            gunicorn apidev.wsgi --bind 0.0.0.0:8000 --workers 3