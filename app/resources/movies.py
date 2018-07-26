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
        """
        ---
        summary: Get all movies in the database
        tags:
            - Movie
        produces:
            - application/json
        responses:
            200:
                description: List of movies
                schema:
                    type: array
                    items: MovieSchema
            401:
                description: Unauthorized
        """
        db = req.context["db"]

        resp.status = falcon.HTTP_OK
        resp._data = db.query(Movie).all()

    def on_post(self, req, resp):
        """
        ---
        summary: Add new movie to database
        tags:
            - Movie
        parameters:
            - in: body
              schema: MovieSchema
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: Movie created successfully
                schema: MovieSchema
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        db = req.context["db"]
        db.session.add(req._deserialized)
        db.session.commit()

        resp.status = falcon.HTTP_CREATED
        resp._data = req._deserialized


class MoviesItemResource:
    deserializers = {"patch": movies_patch_schema}
    serializers = {"get": movies_item_schema, "patch": movies_item_schema}

    def on_delete(self, req, resp, id):
        """
        ---
        summary: Delete movie from database
        tags:
            - Movie
        produces:
            - application/json
        responses:
            204:
                description: Movie deleted successfully
            401:
                description: Unauthorized
            404:
                description: Movie does not exist
        """
        db = req.context["db"]
        movie = find_item_by_id(db=db, model=Movie, id=id)
        db.session.delete(movie)
        db.session.commit()

        resp.status = falcon.HTTP_NO_CONTENT
        resp.media = {}

    def on_get(self, req, resp, id):
        """
        ---
        summary: Get movie from database
        tags:
            - Movie
        produces:
            - application/json
        responses:
            200:
                description: Return requested movie details
                schema: MovieSchema
            401:
                description: Unauthorized
            404:
                description: Movie does not exist
        """
        db = req.context["db"]
        movie = find_item_by_id(db=db, model=Movie, id=id)

        resp.status = falcon.HTTP_OK
        resp._data = movie

    def on_patch(self, req, resp, id):
        """
        ---
        summary: Update movie details in database
        tags:
            - Movie
        parameters:
            - in: body
              schema: MoviePatchSchema
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Return requested movie details
                schema: MovieSchema
            401:
                description: Unauthorized
            404:
                description: Movie does not exist
            422:
                description: Input body formatting issue
        """
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
        """
        ---
        summary: Add many movies to database
        tags:
            - Movie
        parameters:
            - in: body
              schema:
                type: array
                items: MovieSchema
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: Movies created successfully
                schema:
                    type: array
                    items: MovieSchema
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        db = req.context["db"]
        for item in req._deserialized:
            db.session.add(item)
        db.session.commit()

        resp.status = falcon.HTTP_CREATED
        resp._data = req._deserialized
