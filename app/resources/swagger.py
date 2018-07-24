import argparse

import falcon
from py2swagger.plugins.falcon import FalconPy2SwaggerPlugin


class Py2SwaggerResource:
    auth = {"auth_disabled": True}

    def on_get(self, req, resp):
        arguments = argparse.Namespace(
            app="app:api", config=None, output=None, plugin="falcon"
        )
        swagger_part = FalconPy2SwaggerPlugin().run(arguments)

        resp.status = falcon.HTTP_OK
        resp.media = swagger_part
