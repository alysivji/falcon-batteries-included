from . import api

from .resources.health_check import HealthCheckResource  # noqa
from .resources.movies import MoviesResource  # noqa

api.add_route("/health-check", HealthCheckResource())
api.add_route("/movies", MoviesResource())
