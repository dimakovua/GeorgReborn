FROM python:latest

RUN mkdir /src
WORKDIR /src
COPY . /src
RUN pip3 install aiogram
RUN pip3 install bs4
RUN python -m pip install git+https://github.com/pytube/pytube
RUN pip3 install requests