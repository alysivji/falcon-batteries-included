import falcon

from app import spec


class ApiSpecResource:
    auth = {"auth_disabled": True}

    def on_get(self, req, resp):
        swagger_specification = spec.to_dict()

        resp.status = falcon.HTTP_200
        resp.media = swagger_specification
