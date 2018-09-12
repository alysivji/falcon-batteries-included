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
spec.definition("Login", schema=LoginSchema)
spec.definition("Movie", schema=MovieSchema)
spec.definition("MoviePatch", schema=MoviePatchSchema)
spec.definition("MoviePathSchema", schema=MoviePathSchema)
spec.definition("MovieQuerySchema", schema=MovieQuerySchema)
spec.definition("Rating", schema=RatingSchema)
spec.definition("User", schema=UserSchema)
spec.definition("UserExistsSchema", schema=UserExistsSchema)
spec.definition("UserPatch", schema=UserPatchSchema)
spec.definition("UserPath", schema=UserPathSchema)

# parse docstrings for routes
spec.add_path(resource=login_resource)
spec.add_path(resource=movies_bulk_resource)
spec.add_path(resource=movies_item_resource)
spec.add_path(resource=movies_resource)
spec.add_path(resource=rate_movie_resource)
spec.add_path(resource=users_exists_resource)
spec.add_path(resource=users_item_resource)
spec.add_path(resource=users_resource)
