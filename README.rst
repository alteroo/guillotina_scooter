Scooter MPI
***************

This is an experimental Master Patient Index. The goal is to make it possible
to distribute the entire system using Docker.

# Quick start

Clone this repository.
===================

Change into the project directory
===================

```cd guillotina_scooter```


Build & download docker images
===================

```docker-compose build```


Run docker-compose
===================

```docker-compose up```

This launches all the servers necessary to manage the patient index.
Your app is now running on ```localhost:8080```


Elasticsearch
----------------------

Before using Elasticsearch you have to install it on your guillotina site.
Do a `POST` request to the `/scooter/@caralog` endpoint with an empty JSON body.
