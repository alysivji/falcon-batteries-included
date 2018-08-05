# Falcon Batteries Included

This example project will demonstrate on how use Falcon and various python libraries to build a REST API for a movie recommendation website.

## Design

Most of the CRUD logic is in controllers, but if we have to do perform multiple tasks for an endpoint, a process is kicked off.

## Batteries

### SQLAlchemy

Load database (well, declarative base) into the request object. Remove database from request before sending response. Follow pattern described in [SQLAlchemy docs](http://docs.sqlalchemy.org/en/latest/orm/session_basics.html#when-do-i-construct-a-session-when-do-i-commit-it-and-when-do-i-close-it) re: constructing / closing sessions.

Migrations with [Alembic](http://alembic.zzzcomputing.com/en/latest/).

### Marshmallow

We have marshmallow to serialize objects into JSON (response) and to deserialize JSON into object (request).

* [`toasted-marshmallow`](https://github.com/lyft/toasted-marshmallow) has 10x performance, investigate adding

### Authentication

JWT authentication via [falcon-auth](https://github.com/loanzen/falcon-auth).

### Asynchronous Task Queue

redis + [rq](https://github.com/rq/rq).

[rq-dashboard](https://github.com/eoranged/rq-dashboard) for monitoring. Available at [http://0.0.0.0:9181/](http://0.0.0.0:9181/)

### Documentation

Created an [apispec](https://github.com/marshmallow-code/apispec) plugin for Falcon to generate the `swagger.json` schema, [falcon-apispec](https://github.com/alysivji/falcon-apispec). Serving with [falcon-swagger-ui](https://github.com/rdidyk/falcon-swagger-ui)
