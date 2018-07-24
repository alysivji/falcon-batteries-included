class HealthCheckResource:
    auth = {"auth_disabled": True}

    def on_get(self, req, resp):
        resp.media = {"service": "healthy"}
