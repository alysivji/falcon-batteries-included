from . import spec
from .routes import (
    login_resource,
    movies_bulk_resource,
    movies_item_resource,
    movies_resource,
    rate_movie_resource,
    users_item_resource,
    users_resource,
)


# apispec documentation
spec.add_path(resource=login_resource)
spec.add_path(resource=movies_resource)
spec.add_path(resource=movies_item_resource)
spec.add_path(resource=movies_bulk_resource)
spec.add_path(resource=rate_movie_resource)
spec.add_path(resource=users_resource)
spec.add_path(resource=users_item_resource)
