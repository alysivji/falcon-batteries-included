# Falcon Batteries Included

This example project will demonstrate on how use Falcon and various python libraries to build a REST API for a movie recommendation website.

## Batteries

### SQLAlchemy

Load database (well, declarative base) into the request object. Remove database from request before sending response. Follow pattern described in [SQLAlchemy docs](http://docs.sqlalchemy.org/en/latest/orm/session_basics.html#when-do-i-construct-a-session-when-do-i-commit-it-and-when-do-i-close-it) re: constructing / closing sessions.

Migrations with [Alembic](http://alembic.zzzcomputing.com/en/latest/).

Adapted from [eshlox](https://eshlox.net/2017/07/28/integrate-sqlalchemy-with-falcon-framework/)

### Marshmallow

We have marshmallow to serialize objects into JSON (response) and to deserialize JSON into object (request).

* [`toasted-marshmallow`](https://github.com/lyft/toasted-marshmallow) has 10x performance, investigate adding

Adapted from [eshlox](https://eshlox.net/2017/07/28/integrate-sqlalchemy-with-falcon-framework/)

### Authentication

JWT authentication via [falcon-auth](https://github.com/loanzen/falcon-auth).

### Asynchronous Task Queue

redis + [rq](https://github.com/rq/rq).

[rq-dashboard](https://github.com/eoranged/rq-dashboard) for monitoring. Available at [http://0.0.0.0:9181/](http://0.0.0.0:9181/)

- [ ] push out task to database which is a persistent store of what's been done or not
- [ ] [custom worker script](http://python-rq.org/docs/workers/) | [more](https://realpython.com/flask-by-example-implementing-a-redis-task-queue/)
- [ ] [rq-scheduler](https://github.com/rq/rq-scheduler)
- [ ] [miguel grinberg](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xxii-background-jobs)

### Documentation

Created an [apispec](https://github.com/marshmallow-code/apispec) plugin for Falcon to generate the `swagger.json` schema, [falcon-apispec](https://github.com/alysivji/falcon-apispec). Serving with [falcon-swagger-ui](https://github.com/rdidyk/falcon-swagger-ui)

* Like the format of [ReDoc](https://github.com/Rebilly/ReDoc), but would have to serve up a static site
   - [ ] create an extension to serve (like falcon-swagger-ui) or add to flask swagger

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Movie Recommender API Documentation</title>
    <!-- needed for adaptive design -->
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://fonts.googleapis.com/css?family=Montserrat:300,400,700|Roboto:300,400,700" rel="stylesheet">

    <!--
    ReDoc doesn't change outer page styles
    -->
    <style>
      body {
        margin: 0;
        padding: 0;
      }
    </style>
  </head>
  <body>
    <redoc spec-url='/apispec' hide-loading></redoc>
    <script src="https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"> </script>
  </body>
</html>
```
