FROM ubuntu:latest


# Instalar OpenJDK 8
RUN \
  apt-get update && \
  apt-get install -y openjdk-8-jdk && \
  rm -rf /var/lib/apt/lists/*

RUN apt-get update
RUN apt-get install graphviz -y
RUN apt-get install graphviz-dev -y

RUN apt-get update && apt-get install python3-dev \
                        gcc \
                        libc-dev -y

RUN \
    apt-get update && \
    apt-get install -y wget python3 python3-pip python3-dev iputils-ping

# RUN ln -s /bin/pip3 /bin/pip
COPY . /code
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

RUN ln -s /bin/python3 /bin/python

WORKDIR /data

ADD start_develop.sh /
RUN chmod +x /start_develop.sh

ENTRYPOINT ["/start_develop.sh"]