import falcon

from app.exceptions import HTTPError
from app.models import User
from app.schemas.login import login_schema


class LoginResource:
    deserializers = {"post": login_schema}

    def on_post(self, req, resp):
        db = req.context["db"]

        email = req._deserialized["email"]
        password_hash = req._deserialized["password_hash"]

        user = (
            db.query(User)
            .filter(User.email == email, User.password_hash == password_hash)
            .first()
        )

        if not user:
            raise HTTPError(falcon.HTTP_UNAUTHORIZED, errors={"message": "Login unsuccessful"})

        # TODO send back token
        resp.media = {"login": "successful!"}
