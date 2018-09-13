from __future__ import annotations

import logging.config

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from elasticsearch import Elasticsearch
import falcon
from falcon_apispec import FalconPlugin
from falcon_auth import FalconAuthMiddleware, JWTAuthBackend
from sqlalchemy_wrapper import SQLAlchemy
import redis
from rq import Queue


from .config import (
    DATABASE_URI,
    ELASTICSEARCH_URI,
    LOGGING_CONFIG,
    REDIS_URI,
    SECRET_KEY,
)
from .middleware import SerializationMiddleware, SQLAlchemySessionManager

# Logging
logging.config.dictConfig(LOGGING_CONFIG)

# Redis
redis_conn = redis.StrictRedis.from_url(REDIS_URI)
q: Queue = Queue(connection=redis_conn)

# Elasticsearch
es = Elasticsearch(ELASTICSEARCH_URI) if ELASTICSEARCH_URI else None
# TODO might have to load a different configuration for production, look into

# SQLAlchemy
db: SQLAlchemy = SQLAlchemy(DATABASE_URI)
from app import models  # noqa

# Authentication
from .utilities import user_loader  # noqa

auth_backend = JWTAuthBackend(user_loader, secret_key=SECRET_KEY)
auth_middleware = FalconAuthMiddleware(auth_backend, exempt_routes=["/swagger"])

# Falcon
app_middleware = [
    auth_middleware,
    SQLAlchemySessionManager(db),
    SerializationMiddleware(),
]
api = falcon.API(middleware=app_middleware)

# Documentation
spec = APISpec(
    title="Movie Recommendation",
    version="0.0.1",
    openapi_version="2.0",
    info=dict(description="An example project API"),
    plugins=[FalconPlugin(api), MarshmallowPlugin()],
)

from . import routes  # noqa
from . import apispec  # noqa
