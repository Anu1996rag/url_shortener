FROM python:3.10-alpine
LABEL authors="Anurag Sandeep Patil"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk update  \
    && apk add postgresql-dev gcc python3-dev build-base py-pip

# Install dependencies
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install psycopg2-binary
RUN pip install -r requirements.txt

COPY . .
