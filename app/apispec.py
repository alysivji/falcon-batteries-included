from . import spec
from .routes import (
    login_resource,
    movies_bulk_resource,
    movies_item_resource,
    movies_resource,
    rate_movie_resource,
    users_exists_resource,
    users_item_resource,
    users_resource,
)
from .schemas import (
    LoginSchema,
    MoviePatchSchema,
    MoviePathSchema,
    MovieQuerySchema,
    MovieSchema,
    RatingSchema,
    UserExistsSchema,
    UserPatchSchema,
    UserPathSchema,
    UserSchema,
)

# set marshmallow schemas
spec.components.schema("Login", schema=LoginSchema)
spec.components.schema("Movie", schema=MovieSchema)
spec.components.schema("MoviePatch", schema=MoviePatchSchema)
spec.components.schema("MoviePathSchema", schema=MoviePathSchema)
spec.components.schema("MovieQuerySchema", schema=MovieQuerySchema)
spec.components.schema("Rating", schema=RatingSchema)
spec.components.schema("User", schema=UserSchema)
spec.components.schema("UserExistsSchema", schema=UserExistsSchema)
spec.components.schema("UserPatch", schema=UserPatchSchema)
spec.components.schema("UserPath", schema=UserPathSchema)

# parse docstrings for routes
spec.path(resource=login_resource)
spec.path(resource=movies_bulk_resource)
spec.path(resource=movies_item_resource)
spec.path(resource=movies_resource)
spec.path(resource=rate_movie_resource)
spec.path(resource=users_exists_resource)
spec.path(resource=users_item_resource)
spec.path(resource=users_resource)
