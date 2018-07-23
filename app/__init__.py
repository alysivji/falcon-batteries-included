import falcon
from sqlalchemy_wrapper import SQLAlchemy

from .config import DATABASE_URI
from .middleware import SerializationMiddleware, SQLAlchemySessionManager

# SQLAlchemy
db = SQLAlchemy(DATABASE_URI)
import app.models  # noqa

# Falcon
app_middleware = [
    SQLAlchemySessionManager(db),
    SerializationMiddleware(),
]
api = falcon.API(middleware=app_middleware)

from . import routes  # noqa
