FROM python:3.7.3


WORKDIR /usr/src/app

COPY requirements.txt ./
COPY requirements-test.txt ./
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

RUN python setup.py develop
