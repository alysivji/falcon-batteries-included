# Falcon Batteries Included

This example project will demonstrate on how use Falcon and various python libraries to build a REST API for a movie recommendation website.

## Batteries

### SQLAlchemy

Load database (well, declarative base) into the request object. Remove database from request before sending response. Follow pattern described in [SQLAlchemy docs](http://docs.sqlalchemy.org/en/latest/orm/session_basics.html#when-do-i-construct-a-session-when-do-i-commit-it-and-when-do-i-close-it) re: constructing / closing sessions.

Migrations with [Alembic](http://alembic.zzzcomputing.com/en/latest/).

Adapted from [eshlox](https://eshlox.net/2017/07/28/integrate-sqlalchemy-with-falcon-framework/)

### Marshmallow

We have marshmallow to serialize objects into JSON (response) and to deserialize JSON into object (request).

Adapted from [eshlox](https://eshlox.net/2017/07/28/integrate-sqlalchemy-with-falcon-framework/)

### Authentication

JWT authentication via [falcon-auth](https://github.com/loanzen/falcon-auth).

### Documentation [WIP]

Using [py2swagger](https://github.com/Arello-Mobile/py2swagger/) to generate `swagger.json`. Serving with [falcon-swagger-ui](https://github.com/rdidyk/falcon-swagger-ui)

* Would be nice to have a plugin for [apispec](https://github.com/marshmallow-code/apispec)
  * marshmallow support FTW!
* Like the format of [ReDoc](https://github.com/Rebilly/ReDoc), but would have to serve up a static site
  * create an extension to serve (like falcon-swagger-ui)

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
    <redoc spec-url='/py2swagger' hide-loading></redoc>
    <script src="https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"> </script>
  </body>
</html>
```
