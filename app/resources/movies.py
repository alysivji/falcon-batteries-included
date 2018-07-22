from ..models import Movie


class MoviesResource:
    def on_get(self, req, resp):
        movies = req.db.query(Movie).all()
        resp.deserialized = movies

    def on_post(self, req, resp):
        resp.media = {"data": "healthy"}
