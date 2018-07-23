import falcon

from app.exceptions import HTTPError
from app.models import Movie
from app.schemas.movies import (
    movies_item_schema,
    movies_list_schema,
    movies_patch_schema,
)


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

    def _find_by_id(self, id, db):
        """Helper method to find movie or return 404"""
        movie = db.query(Movie).get(id)
        if not movie:
            raise HTTPError(falcon.HTTP_404, errors={"id": "does not exist"})
        return movie

    def on_delete(self, req, resp, id):
        db = req.context["db"]
        movie = self._find_by_id(id, db=db)
        db.session.delete(movie)
        db.session.commit()

        resp.status = falcon.HTTP_NO_CONTENT
        resp.media = {}

    def on_get(self, req, resp, id):
        db = req.context["db"]

        resp.status = falcon.HTTP_OK
        resp._data = self._find_by_id(id, db=db)

    def on_patch(self, req, resp, id):
        db = req.context["db"]
        movie = self._find_by_id(id, db=db)
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
