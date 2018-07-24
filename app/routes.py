from . import api

from .resources.health_check import HealthCheckResource
from .resources.login import LoginResource
from .resources.movies import MoviesBulkResource, MoviesItemResource, MoviesResource
from .resources.ratings import RateResource
from .resources.users import UsersItemResource, UsersResource
from .resources.swagger import Py2SwaggerResource

api.add_route("/health-check", HealthCheckResource())

# movies CRUD with bulk add endpoint
api.add_route("/movies", MoviesResource())
api.add_route("/movies/{id:int}", MoviesItemResource())
api.add_route("/movies/bulk", MoviesBulkResource())

api.add_route("/movies/{id:int}/rate", RateResource())

# user CRUD
api.add_route("/users", UsersResource())
api.add_route("/users/{id:int}", UsersItemResource())

# miscellaneous
api.add_route("/login", LoginResource())
api.add_route("/py2swagger", Py2SwaggerResource())
