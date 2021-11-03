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

COPY requirements.txt .
RUN pip3 install --upgrade pip && \
    pip install -r requirements.txt

WORKDIR /data

ADD start_develop.sh /
RUN chmod +x /start_develop.sh
ADD LoadMasterTable.py /
RUN chmod +x /LoadMasterTable.py
COPY mapping.py /
COPY MasterTablesBuenas.xlsx /
COPY second_tables.xlsx /
COPY relaciones_data.xlsx /

ENTRYPOINT ["/start_develop.sh"]
