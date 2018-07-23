from . import api

from .resources.health_check import HealthCheckResource
from .resources.login import LoginResource
from .resources.movies import (
    MoviesBulkResource,
    MoviesItemResource,
    MoviesResource,
)
from .resources.users import (
    UsersItemResource,
    UsersResource
)

api.add_route("/health-check", HealthCheckResource())

# movies CRUD with bulk add endpoint
api.add_route("/movies", MoviesResource())
api.add_route("/movies/{id:int}", MoviesItemResource())
api.add_route("/movies/bulk", MoviesBulkResource())

# user CRUD
api.add_route("/users", UsersResource())
api.add_route("/users/{id:int}", UsersItemResource())

# miscellaneous
api.add_route("/login", LoginResource())