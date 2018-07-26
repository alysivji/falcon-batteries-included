import falcon

from app.models import User
from app.schemas.users import users_item_schema, users_patch_schema
from app.utilities import find_item_by_id


class UsersResource:
    auth = {'exempt_methods': ['POST']}
    deserializers = {"post": users_item_schema}
    serializers = {"post": users_item_schema}

    def on_post(self, req, resp):
        """
        ---
        summary: Create new user
        tags:
            - User
        parameters:
            - in: body
              schema: UserSchema
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: User created successfully
                schema: UserSchema
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


class UsersItemResource:
    deserializers = {"patch": users_patch_schema}
    serializers = {"get": users_item_schema, "patch": users_item_schema}

    def on_delete(self, req, resp, id):
        """
        ---
        summary: Delete user from database
        tags:
            - User
        produces:
            - application/json
        responses:
            204:
                description: User deleted successfully
            401:
                description: Unauthorized
            404:
                description: User does not exist
        """
        db = req.context["db"]
        user = find_item_by_id(db=db, model=User, id=id)
        db.session.delete(user)
        db.session.commit()

        resp.status = falcon.HTTP_NO_CONTENT
        resp.media = {}

    def on_get(self, req, resp, id):
        """
        ---
        summary: Get user from database
        tags:
            - User
        produces:
            - application/json
        responses:
            200:
                description: Return requested user details
                schema: UserSchema
            401:
                description: Unauthorized
            404:
                description: User does not exist
        """
        db = req.context["db"]

        resp.status = falcon.HTTP_OK
        resp._data = find_item_by_id(db=db, model=User, id=id)

    def on_patch(self, req, resp, id):
        """
        ---
        summary: Update user details in database
        tags:
            - User
        parameters:
            - in: body
              schema: UserPatchSchema
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Return requested user details
                schema: UserSchema
            401:
                description: Unauthorized
            404:
                description: User does not exist
            422:
                description: Input body formatting issue
        """
        db = req.context["db"]
        user = find_item_by_id(db=db, model=User, id=id)
        user.patch(req._deserialized)
        db.session.add(user)
        db.session.commit()

        resp.status = falcon.HTTP_OK
        resp._data = user
