FROM ubuntu:latest

RUN \
    apt-get update && \
    apt-get install -y wget python3 python3-pip python3-dev iputils-ping

RUN apt-get update && apt install htop

RUN ln -s /bin/pip3 /bin/pip

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

RUN ln -s /bin/python3 /bin/python

RUN apt-get install libsnappy-dev -y

WORKDIR /data

CMD ["bash"]