FROM python:3.7-alpine

# ENV PYTHONUNBUFFERED 1
# RUN virtualenv /venv
ENV PATH="/venv/bin:$PATH"
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
