from __future__ import annotations

import falcon

from app import spec


class ApiSpecResource:
    auth = {"auth_disabled": True}

    def on_get(self, req: falcon.Request, resp: falcon.Response):
        swagger_specification = spec.to_dict()

        resp.status = falcon.HTTP_200
        resp.media = swagger_specification
