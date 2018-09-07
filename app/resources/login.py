from __future__ import annotations

import falcon

from app import auth_backend
from app.schemas.login import login_schema


class LoginResource:
    auth = {"auth_disabled": True}
    deserializers = {"post": login_schema}

    def on_post(self, req: falcon.Request, resp: falcon.Response):
        """
        ---
        summary: Login into user account and generate JWT
        tags:
            - Login
        parameters:
            - in: body
              schema: LoginSchema
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Login Successful
                schema:
                    type: object
                    properties:
                        message:
                            type: string
                        jwt:
                            type: string
            401:
                description: Login Unsuccessful
            422:
                description: Input body formatting issue
        """
        user = req._deserialized
        jwt_token = auth_backend.get_auth_token({"id": user.id})

        resp.status = falcon.HTTP_OK
        resp.media = {"message": "login successful!", "jwt": jwt_token}
