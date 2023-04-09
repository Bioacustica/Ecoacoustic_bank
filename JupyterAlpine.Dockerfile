FROM alpine:3.9

# Instalar OpenJDK 8
RUN \
  apk update && \
  apk add --no-cache openjdk8-jre && \
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


COPY ./source /code
COPY JupyterRequirements.txt .


RUN \
    pip3 install --upgrade pip setuptools && \
    pip3 install -r JupyterRequirements.txt  &&\
    pip3 install --upgrade pip &&\
    rm -rf /var/lib/apt/lists/* \

RUN ln  /bin/python3 /bin/python

WORKDIR /data

ADD start_develop.sh /
RUN chmod +x /start_develop.sh

ENTRYPOINT ["sh", "/start_develop.sh"]

