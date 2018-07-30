from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
import falcon
from falcon_apispec import FalconPlugin
from falcon_auth import FalconAuthMiddleware, JWTAuthBackend
from falcon_swagger_ui import register_swaggerui_app
from sqlalchemy_wrapper import SQLAlchemy

from .config import DATABASE_URI, SECRET_KEY
from .middleware import SerializationMiddleware, SQLAlchemySessionManager

# SQLAlchemy
db = SQLAlchemy(DATABASE_URI)
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

SWAGGERUI_URL = "/swagger"
SCHEMA_URL = "/apispec"
register_swaggerui_app(
    api,
    SWAGGERUI_URL,
    SCHEMA_URL,
    page_title="Movie Recommendation",
    favicon_url="https://falconframework.org/favicon-32x32.png",
    config={"supportedSubmitMethods": ["get"]},
)

from . import routes  # noqa
from . import apispec  # noqa
