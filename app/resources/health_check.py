class HealthCheckResource:
    deserializers = {"get": None}
    serializers = {"get": None}

    def on_get(self, req, resp):
        resp.media = {"data": "healthy"}
