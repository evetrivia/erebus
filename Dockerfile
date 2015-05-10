FROM ubuntu:15.04

RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y libmysqlclient-dev
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install --upgrade pip

ADD . /erebus
WORKDIR /erebus

RUN pip install -r requirements.txt

CMD python manage.py server

EXPOSE 5000
