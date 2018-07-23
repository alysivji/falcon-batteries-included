import falcon

from app.exceptions import HTTPError
from app.models import User
from app.schemas.users import users_item_schema, users_patch_schema


class UsersResource:
    deserializers = {"post": users_item_schema}
    serializers = {"post": users_item_schema}

    def on_post(self, req, resp):
        db = req.context["db"]
        db.session.add(req._deserialized)
        db.session.commit()

        resp.status = falcon.HTTP_CREATED
        resp._data = req._deserialized


class UsersItemResource:
    deserializers = {"patch": users_patch_schema}
    serializers = {"get": users_item_schema, "patch": users_item_schema}

    def _find_by_id(self, id, db):
        """Helper method to find user or return 404"""
        user = db.query(User).get(id)
        if not user:
            raise HTTPError(falcon.HTTP_404, errors={"id": "does not exist"})
        return user

    def on_delete(self, req, resp, id):
        db = req.context["db"]
        user = self._find_by_id(id, db=db)
        db.session.delete(user)
        db.session.commit()

        resp.status = falcon.HTTP_NO_CONTENT
        resp.media = {}

    def on_get(self, req, resp, id):
        db = req.context["db"]

        resp.status = falcon.HTTP_OK
        resp._data = self._find_by_id(id, db=db)

    def on_patch(self, req, resp, id):
        db = req.context["db"]
        user = self._find_by_id(id, db=db)
        user.patch(req._deserialized)
        db.session.add(user)
        db.session.commit()

        resp.status = falcon.HTTP_OK
        resp._data = user
