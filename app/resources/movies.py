from app.models import Movie
from app.schemas.movies import movies_list_schema, movies_post_schema


class MoviesResource:
    deserializers = {
        "get": None,
        "post": movies_post_schema,
    }

    serializers = {
        "get": movies_list_schema,
        "post": movies_post_schema,
    }

    def on_get(self, req, resp):
        resp._data = req.db.query(Movie).all()

    def on_post(self, req, resp):
        resp.media = {"data": "healthy"}
