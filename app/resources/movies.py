from __future__ import annotations

import falcon
from sqlalchemy_wrapper import Paginator
from webargs.falconparser import use_args

from app.models import Movie
from app.schemas.movies import (
    movies_item_schema,
    movies_list_schema,
    movies_patch_schema,
    movies_query_schema,
)
from app.utilities import find_item_by_id


class MoviesResource:
    deserializers = {"post": movies_item_schema}
    serializers = {"get": movies_list_schema, "post": movies_item_schema}

    @use_args(movies_query_schema, locations=["query"])
    def on_get(self, req: falcon.Request, resp: falcon.Response, args: dict) -> None:
        """
        ---
        summary: Get all movies in the database
        tags:
            - Movie
        parameters:
            - in: query
              schema: MovieQuerySchema
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
        page = args.get("page")
        per_page = args.get("per_page")

        resp.status = falcon.HTTP_OK
        all_items_query = db.query(Movie)
        paginated_query = Paginator(all_items_query, page=page, per_page=per_page)

        resp._data = paginated_query

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
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

    def on_delete(self, req: falcon.Request, resp: falcon.Response, id: int) -> None:
        """
        ---
        summary: Delete movie from database
        tags:
            - Movie
        parameters:
            - in: path
              schema: MoviePathSchema
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

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: int) -> None:
        """
        ---
        summary: Get movie from database
        tags:
            - Movie
        parameters:
            - in: path
              schema: MoviePathSchema
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

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: int) -> None:
        """
        ---
        summary: Update movie details in database
        tags:
            - Movie
        parameters:
            - in: path
              schema: MoviePathSchema
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

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
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
