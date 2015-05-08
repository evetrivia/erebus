FROM ubuntu:precise

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y python python-dev python-setuptools
RUN easy_install pip

ADD . /erebus
WORKDIR /erebus

RUN pip install -r requirements.txt

CMD python manage.py server