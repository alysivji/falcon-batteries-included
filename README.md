# Falcon Batteries Included

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

This example project will demonstrate on how use Falcon and various python libraries to build a REST API for a movie recommendation website.

## Design

Most of the CRUD logic is in controllers, but if we have to do perform multiple tasks for an endpoint, a process is kicked off.

## Batteries

### Asynchronous Task Queue

* redis + [rq](https://github.com/rq/rq)
* [rq-scheduler](https://github.com/rq/rq-scheduler) to schedule jobs
* [rq-dashboard](https://github.com/eoranged/rq-dashboard) for monitoring. Available at [http://0.0.0.0:9181/](http://0.0.0.0:9181/)

### Authentication

* JWT authentication via [falcon-auth](https://github.com/loanzen/falcon-auth)

### Code Formatting

* Formatted using [Black](https://github.com/ambv/black)
* [pre-commit](https://pre-commit.com/) hooks format all commits locally
  * `pre-commit install`

### Continuous Integration, Continouous Delivery (CICD)

* CI builds with [drone](https://drone.io/)

### Documentation

* [apispec](https://github.com/marshmallow-code/apispec) + [falcon-apispec](https://github.com/alysivji/falcon-apispec) to generate OpenAPI (aka Swagger) specification
* Serve documentation with [falcon-swagger-ui](https://github.com/rdidyk/falcon-swagger-ui). Available at [http://0.0.0.0:7000/swagger](http://localhost:7000/swagger)

### Marshmallow

* serialize objects into JSON (response) and deserialize JSON into object (request)
* [`toasted-marshmallow`](https://github.com/lyft/toasted-marshmallow) has 10x performance, investigate

### SQLAlchemy

* Follow pattern described in [SQLAlchemy docs](http://docs.sqlalchemy.org/en/latest/orm/session_basics.html#when-do-i-construct-a-session-when-do-i-commit-it-and-when-do-i-close-it)
  * Load database (well, declarative base) into the request object
  * Remove database from request before sending response
* Migrations with [Alembic](http://alembic.zzzcomputing.com/en/latest/)

### Static Analysis

* Added [mypy](https://mypy.readthedocs.io/en/latest/index.html) to CI pipeline
