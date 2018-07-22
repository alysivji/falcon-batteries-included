import falcon
from sqlalchemy_wrapper import SQLAlchemy

from .config import DATABASE_URI
from .middleware import SQLAlchemySessionManager
from .resources.health_check import HealthCheckResource

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


########
# Routes
########

api.add_route("/health-check", HealthCheckResource())
