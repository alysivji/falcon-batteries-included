from . import api

from .resources.health_check import HealthCheckResource
from .resources.playground import PlaygroundResource
from .resources.swagger import ApiSpecResource

# app
from .resources.login import LoginResource
from .resources.movies import MoviesBulkResource, MoviesItemResource, MoviesResource
from .resources.ratings import RateResource
from .resources.users import UsersItemResource, UsersResource

# miscellaneous
api.add_route("/apispec", ApiSpecResource())
api.add_route("/health-check", HealthCheckResource())
api.add_route("/playground", PlaygroundResource())

# login resource
login_resource = LoginResource()
api.add_route("/login", login_resource)

# movies
movies_resource = MoviesResource()
api.add_route("/movies", movies_resource)

movies_item_resource = MoviesItemResource()
api.add_route("/movies/{id:int}", movies_item_resource)

movies_bulk_resource = MoviesBulkResource()
api.add_route("/movies/bulk", movies_bulk_resource)

# rate movie endpoint
rate_movie_resource = RateResource()
api.add_route("/movies/{id:int}/rate", rate_movie_resource)

# users
users_resource = UsersResource()
api.add_route("/users", users_resource)

users_item_resource = UsersItemResource()
api.add_route("/users/{id:int}", users_item_resource)
