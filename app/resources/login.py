import falcon

from app import auth_backend
from app.exceptions import HTTPError
from app.models import User
from app.schemas.login import login_schema


class LoginResource:
    auth = {"auth_disabled": True}
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
            raise HTTPError(
                falcon.HTTP_UNAUTHORIZED, errors={"message": "login unsuccessful"}
            )

        jwt_token = auth_backend.get_auth_token({"id": user.id})
        resp.media = {"message": "login successful!", "jwt": jwt_token}
