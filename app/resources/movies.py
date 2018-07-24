import falcon

from app.models import Movie
from app.schemas.movies import (
    movies_item_schema,
    movies_list_schema,
    movies_patch_schema,
)
from app.utilities import find_item_by_id


class MoviesResource:
    deserializers = {"post": movies_item_schema}
    serializers = {"get": movies_list_schema, "post": movies_item_schema}

    def on_get(self, req, resp):
        db = req.context["db"]

        resp.status = falcon.HTTP_OK
        resp._data = db.query(Movie).all()

    def on_post(self, req, resp):
        db = req.context["db"]
        db.session.add(req._deserialized)
        db.session.commit()

        resp.status = falcon.HTTP_CREATED
        resp._data = req._deserialized


class MoviesItemResource:
    deserializers = {"patch": movies_patch_schema}
    serializers = {"get": movies_item_schema, "patch": movies_item_schema}

    def on_delete(self, req, resp, id):
        db = req.context["db"]
        movie = find_item_by_id(db=db, model=Movie, id=id)
        db.session.delete(movie)
        db.session.commit()

        resp.status = falcon.HTTP_NO_CONTENT
        resp.media = {}

    def on_get(self, req, resp, id):
        db = req.context["db"]
        movie = find_item_by_id(db=db, model=Movie, id=id)

        resp.status = falcon.HTTP_OK
        resp._data = movie

    def on_patch(self, req, resp, id):
        db = req.context["db"]
        movie = find_item_by_id(db=db, model=Movie, id=id)
        movie.patch(req._deserialized)
        db.session.add(movie)
        db.session.commit()

        resp.status = falcon.HTTP_OK
        resp._data = movie


class MoviesBulkResource:
    deserializers = {"post": movies_list_schema}
    serializers = {"post": movies_list_schema}

    def on_post(self, req, resp):
        db = req.context["db"]
        for item in req._deserialized:
            db.session.add(item)
        db.session.commit()

        resp.status = falcon.HTTP_CREATED
        resp._data = req._deserialized
