FROM python:3.7.6-buster as builder

# Init Postgres DB
COPY scooter_base_db.sql /docker-entrypoint-initdb.d/

WORKDIR /app

COPY setup.py requirements.txt /app/
RUN pip install -r requirements.txt && \
  pip install -e .

COPY . /app/

ENV PYTHONUNBUFFERRED=1
ENV SENTRY=1

ENTRYPOINT ["guillotina"]