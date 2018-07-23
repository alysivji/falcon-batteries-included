from . import api

from .resources.health_check import HealthCheckResource
from .resources.movies import (
    MoviesBulkResource,
    MoviesItemResource,
    MoviesResource,
)

api.add_route("/health-check", HealthCheckResource())

# movies CRUD
api.add_route("/movies", MoviesResource())
api.add_route("/movies/{id:int}", MoviesItemResource())
api.add_route("/movies/bulk", MoviesBulkResource())
