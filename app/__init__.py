import falcon

from .resources.health_check import HealthCheckResource

app_middleware = []
api = falcon.API(middleware=app_middleware)

# routes
api.add_route("/health-check", HealthCheckResource())
