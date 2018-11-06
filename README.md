# Falcon Batteries Included

[![PyUp](https://pyup.io/repos/github/alysivji/falcon-batteries-included/shield.svg)](https://pyup.io/account/repos/github/alysivji/falcon-batteries-included/) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

This opinionated project demonstrates how use [Falcon](https://github.com/falconry/falcon) and various Python libraries to build a scalable REST API for a movie recommendation website.

#### Table of Contents

<!-- TOC -->

- [Design](#design)
- [Development Workflow](#development-workflow)
  - [Getting Started](#getting-started)
  - [Search Notes](#search-notes)
- [Python Best Practices](#python-best-practices)
- [Batteries](#batteries)
  - [Asynchronous Task Queue](#asynchronous-task-queue)
  - [Authentication](#authentication)
  - [Continuous Integration, Continouous Delivery (CICD)](#continuous-integration-continouous-delivery-cicd)
  - [Documentation](#documentation)
  - [Full-Text Search](#full-text-search)
  - [ORM (SQLAlchemy)](#orm-sqlalchemy)
  - [Profiler](#profiler)
  - [Security](#security)
  - [Serialization / Deserialization](#serialization--deserialization)
  - [Testing](#testing)

<!-- /TOC -->

---

## Design

> Use the best tool for the job at hand.

- Most of the CRUD logic is in controllers, but if we have to do perform multiple tasks for an endpoint, a process is kicked off.
- Took inspiration from [Twelve-Factor App](https://12factor.net/)

## Development Workflow

- Development environment leverages Docker-Compose to replicate production environment
- `Makefile` provides common operations for development
- [pre-commit](https://pre-commit.com/) hooks identify comomn code review issues before submission
- CI pipeline is triggered on push to branch and PR creation

### Getting Started

1. `make up`
2. Create virtual environment on local machine, `pip install -r requirements_dev.txt` to install dependencies locally
3. Point IDE's `PYTHONPATH` to the `python` instance in the virtual environment from above to get autocomplete and other tooling working
4. Install [`pre-commit`](https://pre-commit.com/) on your development machine
5. `pre-commit install` will run existing hook scripts (from [`.pre-commit-config.yaml`](https://github.com/alysivji/falcon-batteries-included/blob/master/.pre-commit-config.yaml))

Server available at [http://0.0.0.0:7000/](http://0.0.0.0:7000/)

### Search Notes

- Implemented in console in console only, TODO: add search endpoint

```python
Movie.reindex()
Movie.search("top gun", page=1, per_page=5)
```

## Python Best Practices

- Code Formatter: [Black](https://github.com/ambv/black)
- Logging: [Standard Library](https://docs.python.org/3/library/logging.html)
- Static Type Checker: [mypy](https://mypy.readthedocs.io/en/latest/index.html)
- Updating Dependencies: [PyUp](https://pyup.io/)

## Batteries

### Asynchronous Task Queue

- redis + [rq](https://github.com/rq/rq)
- [rq-scheduler](https://github.com/rq/rq-scheduler) to schedule jobs
- [rq-dashboard](https://github.com/eoranged/rq-dashboard) for monitoring. Available at [http://0.0.0.0:9181/](http://0.0.0.0:9181/)

### Authentication

- JWT authentication via [falcon-auth](https://github.com/loanzen/falcon-auth)

### Continuous Integration, Continouous Delivery (CICD)

- CI builds with [drone](https://drone.io/)

### Documentation

- [apispec](https://github.com/marshmallow-code/apispec) + [falcon-apispec](https://github.com/alysivji/falcon-apispec) to generate OpenAPI (aka Swagger) specification
- Serving [Redoc](https://github.com/Rebilly/ReDoc)-styled docs at [http://localhost:7000/swagger/redoc.html](http://localhost:7000/swagger/redoc.html)

### Full-Text Search

- Using [elasticsearch](https://www.elastic.co/products/elasticsearch) via [elasticsearch-py](https://github.com/elastic/elasticsearch-py)
- Leveraging developer utilities from [Kibana](https://www.elastic.co/products/kibana)

### ORM (SQLAlchemy)

- Follow pattern described in [SQLAlchemy docs](http://docs.sqlalchemy.org/en/latest/orm/session_basics.html#when-do-i-construct-a-session-when-do-i-commit-it-and-when-do-i-close-it)
  - Load database (well, declarative base) into the request object
  - Remove database from request before sending response
- Migrations with [Alembic](http://alembic.zzzcomputing.com/en/latest/)

### Profiler

- Attach [py-spy](https://github.com/benfred/py-spy) to Python process to profile
- Connect to Gunicorn process to profile web application
  - [Gunicorn architecture](http://docs.gunicorn.org/en/stable/design.html)

```console
USAGE:
    py-spy --duration <duration> --pid <pid> --rate <rate>
```

### Security

- [Bandit](https://github.com/PyCQA/bandit) is a static analysis tool to find security issues
- [10 common security gotchas in Python and how to avoid them](https://hackernoon.com/10-common-security-gotchas-in-python-and-how-to-avoid-them-e19fbe265e03)
- [Open Web Application Security Project: 2017 Top 10](https://www.owasp.org/index.php/Top_10-2017_Top_10)

### Serialization / Deserialization

- [Marshmallow](https://github.com/marshmallow-code/marshmallow) to serialize objects into JSON (response) and deserialize JSON into object (request)
- [webargs](https://github.com/sloria/webargs) to parse requests arguments (query string)
- [`toasted-marshmallow`](https://github.com/lyft/toasted-marshmallow) has 10x performance, investigate

### Testing

- [pytest](https://docs.pytest.org/en/latest/)
- Functional tests via [tavern](https://taverntesting.github.io/)
  - Works locally and not in drone (currently excluded from CI check)
  - Either write a plugin to have Tavern hit Falcon test API or use Jenkins
