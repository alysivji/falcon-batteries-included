from __future__ import annotations

import falcon

from app.hooks import LoadObjectFromDB
from app.models import User
from app.schemas.users import users_item_schema, users_patch_schema, users_exists_schema
from app.workflows.user import process_new_user


class UsersExistsResource:
    auth = {"auth_disabled": True}
    deserializers = {"post": users_exists_schema}

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Check if email is already in database
        tags:
            - User
        parameters:
            - in: body
              schema: UserExistsSchema
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: User exists
            404:
                description: User does not exist
        """
        resp.status = falcon.HTTP_OK
        resp.media = {}


class UsersResource:
    auth = {"exempt_methods": ["POST"]}
    deserializers = {"post": users_item_schema}
    serializers = {"post": users_item_schema}

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
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
        user = req._deserialized

        user = process_new_user(db, user)

        resp.status = falcon.HTTP_CREATED
        resp._data = user


@falcon.before(LoadObjectFromDB(User))
class UsersItemResource:
    deserializers = {"patch": users_patch_schema}
    serializers = {"get": users_item_schema, "patch": users_item_schema}

    def on_delete(self, req: falcon.Request, resp: falcon.Response, id: int) -> None:
        """
        ---
        summary: Delete user from database
        tags:
            - User
        parameters:
            - in: path
              schema: UserPathSchema
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
        user = req._item

        db = req.context["db"]
        db.session.delete(user)
        db.session.commit()

        resp.status = falcon.HTTP_NO_CONTENT
        resp.media = {}

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: int) -> None:
        """
        ---
        summary: Get user from database
        tags:
            - User
        parameters:
            - in: path
              schema: UserPathSchema
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
        resp.status = falcon.HTTP_OK
        resp._data = req._item

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: int) -> None:
        """
        ---
        summary: Update user details in database
        tags:
            - User
        parameters:
            - in: path
              schema: UserPathSchema
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
        user = req._item
        user.patch(req._deserialized)

        db = req.context["db"]
        db.session.add(user)
        db.session.commit()

        resp.status = falcon.HTTP_OK
        resp._data = user
