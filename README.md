# Falcon Batteries Included

This example project will demonstrate on how use Falcon and various python libraries to build a REST API for a movie recommendation website.

## Middleware

### SQLAlchemy

Load database (well, declarative base) into the request object. Remove database from request before sending response. Follow pattern described in [SQLAlchemy docs](http://docs.sqlalchemy.org/en/latest/orm/session_basics.html#when-do-i-construct-a-session-when-do-i-commit-it-and-when-do-i-close-it) re: constructing / closing sessions.
