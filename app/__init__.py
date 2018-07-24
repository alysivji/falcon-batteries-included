import falcon
from falcon_auth import FalconAuthMiddleware, JWTAuthBackend
from sqlalchemy_wrapper import SQLAlchemy

from .config import DATABASE_URI, SECRET_KEY
from .middleware import SerializationMiddleware, SQLAlchemySessionManager

# SQLAlchemy
db = SQLAlchemy(DATABASE_URI)
from app import models  # noqa

# Authentication
from .utilities import user_loader  # noqa
auth_backend = JWTAuthBackend(user_loader, secret_key=SECRET_KEY)
auth_middleware = FalconAuthMiddleware(auth_backend)

# Falcon
app_middleware = [
    auth_middleware,
    SQLAlchemySessionManager(db),
    SerializationMiddleware(),
]
api = falcon.API(middleware=app_middleware)

from . import routes  # noqa
