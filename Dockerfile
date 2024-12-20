FROM python:3.11-slim
LABEL authors="OldSumerian"

WORKDIR /app

COPY pyproject.toml .

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root

COPY . .
