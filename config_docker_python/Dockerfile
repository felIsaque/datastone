FROM python:3
ENV PYTHONUNBUFFERED=1

RUN apt-get install bash

RUN mkdir /src

COPY . /src/

WORKDIR /src/data_stone_app

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install
