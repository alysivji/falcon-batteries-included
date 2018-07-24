import falcon

from app.models import Movie, Rating
from app.schemas.ratings import rating_item_schema
from app.utilities import find_item_by_id


class RateResource:
    deserializers = {"post": rating_item_schema}

    def on_post(self, req, resp, id):
        db = req.context["db"]
        user = req.context["user"]
        movie = find_item_by_id(db=db, model=Movie, id=id)
        rating = req._deserialized["rating"]

        user_rating = Rating(rating=rating, user=user, movie=movie)
        db.session.add(user_rating)
        db.session.commit()

        resp.status = falcon.HTTP_CREATED
        resp.media = {"message": "rating saved"}
