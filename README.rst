Scooter MPI
==================================

This is an experimental Master Patient Index. The goal is to make it possible
to distribute the entire system using Docker.

Dependencies
------------

Python >= 3.7


Installation
------------

This example will use python virtual env::

  python3 -m venv .
  ./bin/pip install -e .


Running
-------

The most simple way to get running::

  ./bin/g


Running Postgresql Server:

    docker run --rm -e POSTGRES_DB=guillotina -e POSTGRES_USER=guillotina -e POSTGRES_HOST_AUTH_METHOD=trust -p 127.0.0.1:5432:5432 --name postgres postgres:9.6

Demos with Docker Compose
--------------------------
::

    docker-compose -f g-api/docker-compose.yaml up

This launches a complete scooter master patient index. You can use the restful api to add new
patients.