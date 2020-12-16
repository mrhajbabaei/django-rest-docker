FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1
COPY ./requirement.txt /requirement.txt
RUN pip install -r /requiremnt.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
