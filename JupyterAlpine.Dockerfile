# FROM alpine:3.9
FROM python:3.6-alpine3.13

WORKDIR /data

# Instalar OpenJDK 8
RUN \
  apk update && \
  apk add --no-cache openjdk8-jre && \
#  apk add --no-cache graphviz && \
  apk add --no-cache graphviz-dev && \
  apk add --no-cache zeromq-dev && \
  apk add && apk add python3-dev \
                gcc\
                libc-dev && \
  rm -rf /var/lib/apt/lists/*

RUN \
   apk add python3 py3-pip python3-dev iputils


COPY ./source /code
COPY JupyterRequirements.txt .


RUN \
    pip3 install -r JupyterRequirements.txt  &&\
    pip3 install --upgrade pip setuptools

RUN ln -s /bin/python3 /bin/python
ADD start_develop.sh /
RUN chmod +x /start_develop.sh

ENTRYPOINT ["sh", "/start_develop.sh"]

