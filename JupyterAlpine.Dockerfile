<<<<<<< HEAD
# FROM alpine:3.9
FROM python:3.6-alpine3.13

WORKDIR /data
=======
FROM alpine:3.9
>>>>>>> 5364bf5eb3d7a8596936082627049b296c7bf15f

# Instalar OpenJDK 8
RUN \
  apk update && \
  apk add --no-cache openjdk8-jre && \
<<<<<<< HEAD
#  apk add --no-cache graphviz && \
  apk add --no-cache graphviz-dev && \
  apk add --no-cache zeromq-dev && \
  apk add && apk add python3-dev \
                gcc\
                libc-dev && \
  rm -rf /var/lib/apt/lists/*

RUN \
   apk add python3 py3-pip python3-dev iputils
=======
  apk add --no-cache graphviz -y && \
  apk add --no-cache graphviz-dev -y && \
  apk add --no-cache zeromq-dev &&\
  apk add && apk add python3-dev \
                gcc\
                libc-dev -y && \
  rm -rf /var/lib/apt/lists/* \

RUN \
   apk update && \
   apk add python3 py3-pip python3-dev iputils && \
   rm -rf /var/lib/apt/lists/* \
>>>>>>> 5364bf5eb3d7a8596936082627049b296c7bf15f


COPY ./source /code
COPY JupyterRequirements.txt .


RUN \
<<<<<<< HEAD
    pip3 install -r JupyterRequirements.txt  &&\
    pip3 install --upgrade pip setuptools

RUN ln -s /bin/python3 /bin/python

=======
    pip3 install --upgrade pip setuptools && \
    pip3 install -r JupyterRequirements.txt  &&\
    pip3 install --upgrade pip &&\
    rm -rf /var/lib/apt/lists/* \

RUN ln -s /bin/python3 /bin/python

WORKDIR /data

>>>>>>> 5364bf5eb3d7a8596936082627049b296c7bf15f
ADD start_develop.sh /
RUN chmod +x /start_develop.sh

ENTRYPOINT ["sh", "/start_develop.sh"]

