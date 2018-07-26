import falcon

from app.models import Rating
from app.schemas.ratings import rating_item_schema


class RateResource:
    deserializers = {"post": rating_item_schema}

    def on_post(self, req, resp, id):
        """
        ---
        summary: Add rating for movie as logged in user
        tags:
            - Rating
        parameters:
            - in: body
              schema: RatingSchema
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: Vote successful
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        db = req.context["db"]
        user = req.context["user"]
        rating = req._deserialized["rating"]

        user_rating = Rating(rating=rating, user=user, movie_id=id)
        db.session.add(user_rating)
        db.session.commit()

        resp.status = falcon.HTTP_CREATED
        resp.media = {"message": "rating saved"}
