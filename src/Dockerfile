FROM python:3.8-slim-buster

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential \
        libpq-dev \
        postgresql-client

RUN pip install --upgrade pip setuptools poetry
RUN poetry --version
COPY ./poetry.lock .
COPY ./pyproject.toml .
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY . .

ENTRYPOINT [ "./entrypoint.sh" ]