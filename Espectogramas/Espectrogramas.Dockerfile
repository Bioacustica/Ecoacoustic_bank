FROM ubuntu:latest

RUN apt-get update && apt-get install python3-dev \
    gcc \
    libc-dev -y

RUN apt-get update && \
    apt-get install -y wget python3 python3-pip python3-dev

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt


WORKDIR /bioacustica

ADD start_develop.sh /
RUN chmod +x /start_develop.sh

ENTRYPOINT ["/start_develop.sh"]
