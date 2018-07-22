import falcon
from sqlalchemy_wrapper import SQLAlchemy

from .config import DATABASE_URI
from .middleware import SQLAlchemySessionManager

########
# Config
########

# SQLAlchemy
db = SQLAlchemy(DATABASE_URI)
import app.models  # noqa

# Falcon
app_middleware = [
    SQLAlchemySessionManager(db)
]
api = falcon.API(middleware=app_middleware)

from . import routes  # noqa
